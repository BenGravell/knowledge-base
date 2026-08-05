<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conformalized Quantile Regression

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conformal prediction is a technique for constructing prediction intervals that attain valid coverage in finite samples, without making distributional assumptions. Despite this appeal, existing conformal methods can be unnecessarily conservative because they form intervals of constant or weakly varying length across the input space. In this paper we propose a new method that is fully adaptive to heteroscedasticity. It combines conformal prediction with classical quantile regression, inheriting the advantages of both. We establish a theoretical guarantee of valid coverage, supplemented by extensive experiments on popular regression datasets. We compare the efficiency of conformalized quantile regression to other conformal methods, showing that our method tends to produce shorter intervals.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many applications of regression modeling, it is important not only to predict accurately but also to quantify the accuracy of the predictions. This is especially true in situations involving high-stakes decision making, such as estimating the efficacy of a drug or the risk of a credit default. The uncertainty in a prediction can be quantified using a prediction interval, giving lower and upper bounds between which the response variable lies with high probability. An ideal procedure for generating prediction intervals should satisfy two properties. First, it should provide valid coverage in finite samples, without making strong distributional assumptions, such as Gaussianity. Second, its intervals should be as short as possible at each point in the input space, so that the predictions will be informative. When the data is heteroscedastic, getting valid but short prediction intervals requires adjusting the lengths of the intervals according to the local variability at each query point in predictor space. This paper introduces a procedure that performs well on both criteria, being distribution-free and adaptive to heteroscedasticity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work is heavily inspired by *conformal prediction*, a general methodology for constructing prediction intervals. Conformal prediction has the virtue of providing a nonasymptotic, distribution-free coverage guarantee. The main idea is to fit a regression model on the training samples, then use the residuals on a held-out validation set to quantify the uncertainty in future predictions. The effect of the underlying model on the length of the prediction intervals, and attempts to construct intervals with locally varying length, have been studied in numerous recent works. Nevertheless, existing methods yield conformal intervals of either fixed length or length depending only weakly on the predictors, as argued.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quantile regression offers a different approach to constructing prediction intervals. Take any algorithm for *quantile regression*, i.e., for estimating conditional quantile functions from data. To obtain prediction intervals, say, nominal 90% coverage, simply fit the conditional quantile function at the 5% and 95% levels and form the corresponding intervals. Even for highly heteroscedastic data, this methodology has been shown to be adaptive to local variability. However, the validity of the estimated intervals is guaranteed only for specific models, under certain regularity and asymptotic conditions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we combine conformal prediction with quantile regression. The resulting method, which we call *conformalized quantile regression* (CQR), inherits both the finite sample, distribution-free validity of conformal prediction and the statistical efficiency of quantile regression.^11^1Source code implementing CQR is available online at On one hand, CQR is flexible in that it can wrap around any algorithm for quantile regression, including random forests and deep neural networks. On the other hand, a key strength of CQR is its rigorous control of the miscoverage rate, independent of the underlying regression algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Summary and outline", "weight": 1.0} -->

Suppose we are given $n$ training samples ${\{{(X_{i},Y_{i})}\}}_{i = 1}^{n}$ and we must now predict the unknown value of $Y_{n + 1}$ at a test point $X_{n + 1}$. We assume that all the samples ${\{{(X_{i},Y_{i})}\}}_{i = 1}^{n + 1}$ are drawn exchangeably---for instance, they may be drawn i.i.d.---from an arbitrary joint distribution $P_{XY}$ over the feature vectors $X \in {\mathbb{R}}^{p}$ and response variables $Y \in {\mathbb{R}}$. We aim to construct a *marginal distribution-free prediction interval* ${C{(X_{n + 1})}} \subseteq {\mathbb{R}}$ that is likely to contain the unknown response $Y_{n + 1}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Summary and outline", "weight": 1.0} -->

That is, given a desired miscoverage rate $\alpha$, we ask that for any joint distribution $P_{XY}$ and any sample size $n$. The probability in this statement is marginal, being taken over all the samples ${\{{(X_{i},Y_{i})}\}}_{i = 1}^{n + 1}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Summary and outline", "weight": 1.0} -->

To accomplish this, we build on the method of conformal prediction. We first split the training data into two disjoint subsets, a proper training set and a calibration set.^22^2Like conformal regression, CQR has a variant that does not require data splitting. We fit two quantile regressors on the proper training set to obtain initial estimates of the lower and upper bounds of the prediction interval, as explained in Section 2. Then, using the calibration set, we conformalize and, if necessary, correct this prediction interval. Unlike the original interval, the conformalized prediction interval is guaranteed to satisfy the coverage requirement regardless of the choice or accuracy of the quantile regression estimator. We prove this in Section 4 ‣ Conformalized Quantile Regression").

<!-- chunk {"id": "body-0010", "role": "body", "section": "Summary and outline", "weight": 1.0} -->

Our method differs from the standard method of conformal prediction, recalled in Section 3, in that we calibrate the prediction interval using conditional quantile regression, while the standard method uses only classical, conditional mean regression. The result is that our intervals are adaptive to heteroscedasticity whereas the standard intervals are not. We evaluate the statistical efficiency of our framework by comparing its miscoverage rate and average interval length with those of other methods. We review existing state-of-the-art schemes for conformal prediction in Section 5 and we compare them with our method in Section 6. Based on extensive experiments across eleven datasets, we conclude that conformal quantile regression yields shorter intervals than the competing methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Quantile regression", "weight": 1.0} -->

The aim of conditional quantile regression is to estimate a given quantile, such as the median, of $Y$ conditional on $X$. Recall that the *conditional distribution function* of $Y$ given $X = x$ is and that the $\alpha$th *conditional quantile function* is Fix the lower and upper quantiles to be equal to $\alpha_{\text{lo}} = {\alpha/2}$ and $\alpha_{\text{hi}} = {1 - {\alpha/2}}$, say. Given the pair $q_{\alpha_{\text{lo}}}{(x)}$ and $q_{\alpha_{\text{hi}}}{(x)}$ of lower and upper conditional quantile functions, we obtain a conditional prediction interval for $Y$ given $X = x$, with miscoverage rate $\alpha$, as By construction, this interval satisfies Notice that the length of the interval $C{(X)}$ can vary greatly depending on the value of $X$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Quantile regression", "weight": 1.0} -->

The uncertainty in the prediction of $Y$ is naturally reflected in the length of the interval. In practice we cannot know this ideal prediction interval, but we can try to estimate it from the data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Estimating quantiles from data", "weight": 1.0} -->

Classical regression analysis estimates the conditional mean of the test response $Y_{n + 1}$ given the features $X_{n + 1} = x$ by minimizing the sum of squared residuals on the $n$ training points: Here $\theta$ are the parameters of the regression model, $\mu{(x;\theta)}$ is the regression function, and $\mathcal{R}$ is a potential regularizer.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Estimating quantiles from data", "weight": 1.0} -->

Analogously, quantile regression estimates a conditional quantile function $q_{\alpha}$ of $Y_{n + 1}$ given $X_{n + 1} = x$. This can be cast as the optimization problem where $f{(x;\theta)}$ is the quantile regression function and the loss function $\rho_{\alpha}$ is the "check function" or "pinball loss", defined by and illustrated in Figure 1. The simplicity and generality of this formulation makes quantile regression widely applicable. As in classical regression, one can leverage the great variety of machine learning methods to design and learn ${\hat{q}}_{\alpha}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Estimating quantiles from data", "weight": 1.0} -->

All this suggests an obvious strategy to construct a prediction band with nominal miscoverage rate $\alpha$: estimate ${\hat{q}}_{\alpha_{\text{lo}}}{(x)}$ and ${\hat{q}}_{\alpha_{\text{hi}}}{(x)}$ using quantile regression, then output ${\hat{C}{(X_{n + 1})}} = {\lbrack{{\hat{q}}_{\alpha_{\text{lo}}}{(X_{n + 1})}},{{\hat{q}}_{\alpha_{\text{hi}}}{(X_{n + 1})}}\rbrack}$ as an estimate of the ideal interval $C{(X_{n + 1})}$ from equation. This approach is widely applicable and often works well in practice, yielding intervals that are adaptive to heteroscedasticity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Estimating quantiles from data", "weight": 1.0} -->

However, it is not guaranteed to satisfy the coverage statement when $C{(X)}$ is replaced by the estimated interval $\hat{C}{(X_{n + 1})}$. Indeed, the absence of any finite sample guarantee can sometimes be disastrous. This worry is corroborated by our experiments, which show that the intervals constructed by neural networks can substantially undercover.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Estimating quantiles from data", "weight": 1.0} -->

Under certain regularity conditions and for specific models, estimates of conditional quantile functions via the pinball loss are known to be asymptotically consistent. Related methods that do not minimize the pinball loss, such as quantile random forests, are also asymptotically consistent. But to get valid coverage in finite samples, we must draw on a different set of ideas, from conformal prediction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

We now describe how conformal prediction constructs prediction intervals that satisfy the finite-sample coverage guarantee. To be carried out exactly, the original, or *full*, conformal procedure effectively requires the regression algorithm to be invoked infinitely many times. In contrast, the method of *split*, or *inductive*, conformal prediction avoids this problem, at the cost of splitting the data. While our proposal is applicable to both versions of conformal prediction, in the interest of space we will restrict our attention to split conformal prediction and refer the reader to for a more detailed comparison between the two methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

Under the assumptions of Section 1, the split conformal method begins by splitting the training data into two disjoint subsets: a proper training set $\left\{ {(X_{i},Y_{i})}:{i \in \mathcal{I}_{1}} \right\}$ and calibration set $\left\{ {(X_{i},Y_{i})}:{i \in \mathcal{I}_{2}} \right\}$. Then, given any regression algorithm $\mathcal{A}$,^33^3In full conformal prediction, the regression algorithm must treat the data exchangeably, but no such restrictions apply to split conformal prediction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

a regression model is fit to the proper training set: Next, the absolute residuals are computed on the calibration set, as follows: For a given level $\alpha$, we then compute a quantile of the empirical distribution^44^4The explicit formula for empirical quantiles is recalled in Appendix A. of the absolute residuals, Finally, the prediction interval at a new point $X_{n + 1}$ is given by This interval is guaranteed to satisfy, as shown. For related theoretical studies, see.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

A closer look at the prediction interval reveals a major limitation of this procedure: the length of $C{(X_{n + 1})}$ is fixed and equal to $2Q_{1 - \alpha}{(R,\mathcal{I}_{2})}$, independent of $X_{n + 1}$. Lei et al observe that the intervals produced by the full conformal method also vary only slightly with $X_{n + 1}$, provided the regression algorithm is moderately stable. This brings us to our proposal, which offers a principled approach to constructing variable-width conformal prediction intervals.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

(a) Split: Avg. coverage 91.4%; Avg. length 2.91.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

(b) Local: Avg. coverage 91.7%; Avg. length 2.86.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

(c) CQR: Avg. coverage 91.06%; Avg. length 1.99.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

In this section we introduce our procedure, beginning with a small experiment on simulated data to show how it improves upon standard conformal prediction. Figure 2 ‣ Conformalized Quantile Regression") compares the prediction intervals produced by (a) the split conformal method, (b) its locally adaptive variant (described later in Section 5), and (c) our method, conformalized quantile regression (CQR). The heteroskedasticity of the data is evident, as the dispersion of $Y$ varies considerably with $X$. The data also contains outliers, shown in Figure 7 from Appendix B. For all three methods, we construct $90\%$ prediction intervals on the test data. From Figures 2(a) ‣ Conformalized Quantile Regression") and 2(d) ‣ Conformalized Quantile Regression"), we see that the lengths of the split conformal intervals are fixed and equal to $2.91$. The prediction intervals of the locally weighted variant, shown in Figure 2(b) ‣ Conformalized Quantile Regression"), are partially adaptive, resulting in slightly shorter intervals, of average length $2.86$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

Our method, shown in Figure 2(c) ‣ Conformalized Quantile Regression"), is also adaptive, but its prediction intervals are considerably shorter, of average length $1.99$, due to better estimation of the lower and upper quantiles. We refer the reader to Appendix B for additional information about this experiment.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

Finally, given new input data $X_{n + 1}$, we construct the prediction interval for $Y_{n + 1}$ as conformalizes the plug-in prediction interval.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

For ease of reference, the CQR procedure is summarized in Algorithm 1 ‣ Conformalized Quantile Regression"). We now prove that its prediction intervals satisfy the marginal, distribution-free coverage guarantee.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conformalized quantile regression (CQR)", "weight": 1.0} -->

Quantile regression algorithm 𝒜. Randomly split {1, …, n} into two disjoint sets ℐ1 and ℐ2. Fit two conditional quantile functions: {q̂αlo, q̂αhi} ← 𝒜 ({(Xi, Yi): i ∈ ℐ1}). Compute Ei for each i ∈ ℐ2, as in equation. Compute Q1 − α (E, ℐ2), the (1 − α) (1 + 1/|ℐ2|)-th empirical quantile of {Ei: i ∈ ℐ2}. Prediction interval C (x) = [q̂αlo (x) − Q1 − α (E, ℐ2), q̂αhi (x) + Q1 − α (E, ℐ2)] for unseen input Xn + 1 = x. Algorithm 1 Split Conformal Quantile Regression.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

Conformalized quantile regression can accommodate a wide range of quantile regression methods to estimate the conditional quantile functions, $q_{\alpha_{\text{lo}}}$ and $q_{\alpha_{\text{hi}}}$. The estimators can be even be aggregates of different quantile regression algorithms. Recently, new deep learning techniques have been proposed for constructing prediction intervals. These methods could be wrapped by our framework and would then immediately enjoy rigorous coverage guarantees. In our experiments, we focus on quantile neural networks and quantile regression forests.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

Because the underlying quantile regression algorithm may process the proper training set in arbitrary ways, our framework affords broad flexibility in hyper-parameter tuning. Consider, for instance, the tuning of typical hyper-parameters of neural networks, such as the batch size, the learning rate, and the number of epochs. The hyperparameters may be selected, as usual, by cross validation, where we minimize the average interval length over the folds.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

In this vein, we record two specific implementation details that we have found to be useful.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

Quantile regression is sometimes *too* conservative, resulting in unnecessarily wide prediction intervals. In our experience, quantile regression forests are often overly conservative and quantile neural networks are occasionally so. We can mitigate this problem by tuning the nominal quantiles of the underlying method as additional hyper-parameters in cross validation. Notably, this tuning does not invalidate the coverage guarantee, but it may yield shorter intervals, as our experiments confirm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

To reduce the computational cost, instead of fitting two separate neural networks to estimate the lower and upper quantile functions, we can replace the standard one-dimensional estimate of the unknown response by a two-dimensional estimate of the lower and upper quantiles. In this way, most of the network parameters are shared between the two quantile estimators. We adopt this approach in the experiments of Section 6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Practical considerations and extensions", "weight": 1.0} -->

Another avenue for extension is the conformalization step. The conformalization implemented by equations (15 ‣ Conformalized Quantile Regression")) and (16 ‣ Conformalized Quantile Regression")) allows coverage errors to be spread arbitrarily over the left and right tails. By using a method reminiscent of, we can control the left and right tails independently, resulting in a stronger coverage guarantee.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Limitations of locally adaptive conformal prediction", "weight": 1.5} -->

Locally adaptive conformal prediction is limited in several ways, some more important than others. A first limitation, already noted, appears when the data is actually homoskedastic. In this case, the locally adaptive method suffers from inflated prediction intervals compared to the standard method. This is presumably due to the extra variability introduced by estimating $\hat{\sigma}$ as well as $\hat{\mu}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Limitations of locally adaptive conformal prediction", "weight": 1.5} -->

The locally adaptive method faces a more fundamental statistical limitation. There is an essential difference between the residuals on the proper training set and the residuals on the calibration set: the former are biased by an optimization procedure designed to minimize them, while the latter are unbiased. Because it uses the proper training residuals (as it must to ensure valid coverage), the locally adaptive method tends to systematically underestimate the prediction error. In general, this forces the correction constant $Q_{1 - \alpha}{(\overset{\sim}{R},\mathcal{I}_{2})}$ to be large and the intervals to be less adaptive than they could be.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Limitations of locally adaptive conformal prediction", "weight": 1.5} -->

To press this point further, suppose the conditional mean function $\hat{\mu}$ is a deep neural network. It is well attested in the deep learning literature that, given enough training samples, the best prediction error is attained by "over-fitting" to the training data, in the sense that the training error is nearly zero. The training residuals are then very poor estimates of the test residuals, resulting in severe loss of adaptivity. The original training objective of our method, in contrast, is to estimate the lower and upper conditional quantiles, not the conditional mean. Having sufficient training data, the fitted network is expected to provide reasonable approximations of these two quantile functions, which are used to construct adaptive prediction intervals.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we systematically compare our method, conformalized quantile regression, to the standard and locally adaptive versions of split conformal prediction. Among preexisting conformal prediction algorithms, we select leading variants that use random forests and neural networks for conditional mean regression. Likewise, we configure our method to use quantile regression algorithms based on random forests and neural networks. As a baseline, we also include conformal ridge regression in the comparison. A detailed description of each of the methods is given below.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct the experiments on eleven popular benchmark datasets for regression, listed in Section 6.3. In each case, we standardize the features to have zero mean and unit variance and we rescale the response by dividing it by its mean absolute value.^55^5In the experiments, we compute the needed sample means and variances only on the proper training set. This ensures that if the original data is exchangeable, then the rescaled data remains so. That being said, we could also rescale using sample means and variances computed on the test data, because it would preserve exchangeability even while it destroys independence. The performance metrics are averaged over $20$ different training-test splits; $80\%$ of the examples are used for training and the remaining $20\%$ for testing. The proper training and calibration sets for split conformal prediction have equal size. Throughout the experiments the nominal miscoverage rate is fixed and equal to $\alpha = 0.1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Methods", "weight": 1.0} -->

In more detail, we compare the following methods related to conformal prediction. We evaluate the original version of split conformal prediction (Section 3) using the following three regression algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Methods", "weight": 1.0} -->

Ridge: We include ridge regression as a baseline. The regularization parameter is tuned by cross validation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Methods", "weight": 1.0} -->

Random Forests: We use the implementation of (conditional mean) random forest regression in the Python package sklearn. The hyper-parameters are the package defaults, except for the total number of trees in the forest, which we set to $1000$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Methods", "weight": 1.0} -->

Neural Net: Our neural network architecture consists of three fully connected layers, with ReLU nonlinearities between layers. The first layer takes as input the $p$-dimensional feature vector $X$ and outputs $64$ hidden variables. The second layer follows the same template, outputting another $64$ hidden variables. Finally, a linear output layer returns a pointwise estimate of the response variable $Y$. The parameters of the network are fit by minimizing the quadratic loss function. We use the stochastic optimization algorithm Adam, with fixed learning rate of $5 \times 10^{- 4}$, minibatches of size $64$, and weight decay parameter equal to $10^{- 6}$. We employ dropout regularization, with the probability of retaining a hidden unit equal to $0.1$. To avoid overfitting, we found that early stopping performs well; we tune the number of epochs by cross validation, with an upper limit of $1000$ epochs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Methods", "weight": 1.0} -->

We evaluate locally adaptive conformal prediction (Section 5) using the same three underlying regression algorithms. We set the hyper-parameter $\gamma$ in equation to $1$, which improves performance considerably compared to $\gamma = 0$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Methods", "weight": 1.0} -->

Ridge Local: The conditional mean estimator $\hat{\mu}$ is fit by ridge regression, as described above, and the mean absolute deviation (MAD) estimator $\hat{\sigma}$ is $k$-nearest neighbors with $k = 11$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Methods", "weight": 1.0} -->

Random Forests Local: Both $\hat{\mu}$ and $\hat{\sigma}$ are random forests with the hyper-parameters described above.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Methods", "weight": 1.0} -->

Neural Net Local: Both $\hat{\mu}$ and $\hat{\sigma}$ are neural networks, with the network architecture, hyper-parameters, and training algorithm described above.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Methods", "weight": 1.0} -->

For our own proposal, conformalized quantile regression (Algorithm 1 ‣ Conformalized Quantile Regression")), we evaluate two variants: CQR Random Forests: We use CQR with quantile regression forests. To ensure a fair comparison, the hyper-parameters of the quantile regression forests are made identical to those of the random forests in the previous methods. Quantile regression forests have two additional parameters that control the coverage rate on the training data. We tune them using cross validation, as explained in Section 4 ‣ Conformalized Quantile Regression").

<!-- chunk {"id": "body-0050", "role": "body", "section": "Methods", "weight": 1.0} -->

CQR Neural Net: We apply CQR using neural networks for quantile regression. The network architecture is the same as above, except that the output of the quantile regression network is a two-dimensional vector, representing the lower and upper conditional quantiles. The training algorithm is also the same, except that the cost function is now the pinball loss in equation instead of the quadratic loss.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Methods", "weight": 1.0} -->

Finally, for the sake of comparison, we also include the previous two quantile regression algorithms, but without any conformalization: Quantile Random Forests: We use quantile regression forests with hyperparameters as in the CQR procedure, except that the upper and lower levels are fixed at $0.05$ and $0.95$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Methods", "weight": 1.0} -->

Quantile Neural Net: We use quantile regression neural networks with exactly the same architecture and training algorithm as in the CQR procedure.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Methods", "weight": 1.0} -->

Unlike the preceding methods, the last two methods do not need a calibration set and do not have a finite-sample coverage guarantee. We fit them on the entire training set.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Summary of results", "weight": 1.0} -->

Random Forests Local Neural Net Local CQR Random Forests CQR Neural Net Quantile Random Forests Quantile Neural Net Table 1: Length and coverage of prediction intervals (α = 0.1) constructed by various methods, averaged across 11 datasets and 20 random training-test splits. Our methods are shown in bold font. The methods marked by an asterisk are not supported by finite-sample coverage guarantees.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Summary of results", "weight": 1.0} -->

Table 1 summarizes our 2,200 experiments, showing the average performance across all the datasets and training-test splits. On average, our method achieves shorter prediction intervals than both standard and locally adaptive conformal prediction. It may seem surprising that our method also outperforms non-conformalized quantile regression, which is permitted more training data. There are several possible explanations for this. First, the non-conformalized methods sometimes *over*cover, but that is mitigated by our signed conformity scores (14 ‣ Conformalized Quantile Regression")). In addition, by using CQR, we can tune the quantiles of the underlying quantile regression algorithms using cross-validation (Section 4 ‣ Conformalized Quantile Regression")). Interestingly, CQR selects quantiles below the nominal level.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Summary of results", "weight": 1.0} -->

Turning to the issue of valid coverage, all methods based on conformal prediction successfully construct prediction bands at the nominal coverage rate of $90\%$, as the theory suggests they should. One of the non-conformalized methods, based on random forests, is slightly conservative, while the other, based on neural networks, tends to undercover. In fact, other authors have shown that the coverage of quantile neural networks depends greatly on the tuning of the hyper-parameters for instance, the actual coverage in \[25, Figure 3\] ranging from the 95% nominal level in that paper to well below 50%. Such volatility demonstrates the importance of the conformal prediction's finite-sample guarantee.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Summary of results", "weight": 1.0} -->

When estimating a lower and an upper quantile by two separate quantile regressions, there is no guarantee that the lower estimate will actually be smaller than the upper estimate. This is known as the *quantile crossing* problem. Quantile crossing can affect quantile neural networks, but not quantile regression forests. When the two quantiles are far apart, as in the 5% and 95% quantiles, we should expect the estimates to cross very infrequently and that is indeed what we find in the experiments. Nevertheless, we also evaluated a post-processing method to eliminate crossings. It yields a slight improvement in performance: the average interval length of the CQR neural networks drops from 1.40 to 1.35 and the average interval length of the unconformalized quantile neural networks drops from 1.49 to 1.41, with the coverage rates remaining about the same.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Summary of results", "weight": 1.0} -->

As expected, adopting the two-tailed, asymmetric conformalization proposed in Theorem 2 ‣ Conformalized Quantile Regression") causes an increase in average interval length compared to the symmetric conformalization of Theorem 1 ‣ Conformalized Quantile Regression"). Specifically, the average length for CQR neural networks increases from 1.40 to 1.58, while the coverage rate stays about the same. The average length for the CQR random forests increases from 1.41 to 1.57, accompanied by a slight increase in the average coverage rate, from 90.33 to 90.99.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Performance on individual datasets", "weight": 1.0} -->

In a series of figures, we break down the performance of the different methods on each of the benchmark datasets. Figure 3 summarizes our experiments on the datasets: medical expenditure panel survey number 19 (MEPS_19), number 20 (MEPS_20), and number 21 (MEPS_21). Figure 4 shows the results: blog feedback (blog_data); physicochemical properties of protein tertiary structure (bio); and bike sharing (bike). Figure 5 shows the results: community and crimes (community); Tennessee's student teacher achievement ratio (STAR); and concrete compressive strength (concrete). Lastly, Figure 6 shows the results: Facebook comment volume, variants one (facebook_1) and two (facebook_2).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Performance on individual datasets", "weight": 1.0} -->

The performance on individual datasets confirms the overall trend in Table 1. Locally adaptive conformal prediction generally outperforms standard conformal prediction, and, on ten out of eleven datasets, conformalized quantile regression outperforms both. The CQR random forests are overly conservative on the two Facebook datasets. This is consistent with the theory, because in this case there are ties among the conformity scores and so the upper bound in Theorem 1 ‣ Conformalized Quantile Regression") does not apply.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Conformal quantile regression is a new way of constructing prediction intervals that combines the advantages of conformal prediction and quantile regression. It provably controls the miscoverage rate in finite samples, under the mild distributional assumption of exchangeability, while adapting the interval lengths to heteroskedasticity in the data.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We expect the ideas behind conformal quantile regression to be applicable in the related setting of conformal predictive distributions. In this extension of conformal prediction, the aim is to estimate a predictive probability distribution, not just an interval. We see intriguing connections between our work and a very recent, independently written paper on conformal distributions.
