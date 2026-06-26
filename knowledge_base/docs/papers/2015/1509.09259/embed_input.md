<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Logistic Regression

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper proposes a distributionally robust approach to logistic regression. We use the Wasserstein distance to construct a ball in the space of probability distributions centered at the uniform distribution on the training samples. If the radius of this ball is chosen judiciously, we can guarantee that it contains the unknown data-generating distribution with high confidence. We then formulate a distributionally robust logistic regression model that minimizes a worst-case expected logloss function, where the worst case is taken over all distributions in the Wasserstein ball. We prove that this optimization problem admits a tractable reformulation and encapsulates the classical as well as the popular regularized logistic regression problems as special cases. We further propose a distributionally robust approach based on Wasserstein balls to compute upper and lower confidence bounds on the misclassification probability of the resulting classifier. These bounds are given by the optimal values of two highly tractable linear programs. We validate our theoretical out-of-sample guarantees through simulated and empirical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Logistic regression is one of the most frequently used classification methods applied. Its objective is to establish a probabilistic relationship between a continuous feature vector and a binary explanatory variable. However, in spite of its overwhelming success in machine learning, data analytics and medicine etc., logistic regression models can display a poor out-of-sample performance if training data is sparse. In this case modelers often resort to ad hoc regularization techniques in order to combat overfitting effects. This paper aims to develop new regularization techniques for logistic regression---and to provide intuitive probabilistic interpretations for existing ones---by using tools from modern distributionally robust optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Logistic Regression", "weight": 1.0} -->

Let $x \in {\mathbb{R}}^{n}$ denote a feature vector and $y \in {\{{- 1},{+ 1}\}}$ the associated binary label to be predicted. In logistic regression, the conditional distribution of $y$ given $x$ is modeled as where the weight vector $\beta \in {\mathbb{R}}^{n}$ constitutes an unknown regression parameter. Suppose that $N$ training samples ${\{{({\hat{x}}_{i},{\hat{y}}_{i})}\}}_{i = 1}^{N}$ have been observed.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Logistic Regression", "weight": 1.0} -->

Then, the maximum likelihood estimator of classical logistic regression is found by solving the geometric program whose objective function is given by the sample average of the *logloss function* ${{l_{\beta}{(x,y)}} = {\log{({1 + {\exp{({- {y{\langle\beta,x\rangle}}})}}})}}}.$ It has been observed, however, that the resulting maximum likelihood estimator may display a poor out-of-sample performance. Indeed, it is well documented that minimizing the average logloss function leads to overfitting and weak classification performance feng2014robust; plan2013robust. In order to overcome this deficiency, it has been proposed to modify the objective function of problem ding2013t; liu2004robit; rousseeuw2003robustness. An alternative approach is to add a regularization term to the logloss function in order to mitigate overfitting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Logistic Regression", "weight": 1.0} -->

These regularization techniques lead to a modified optimization problem where $R{(\beta)}$ and $\varepsilon$ denote the regularization function and the associated coefficient, respectively. A popular choice for the regularization term is ${R{(\beta)}} = {\|\beta\|}$, where $\parallel \cdot \parallel$ denotes a generic norm such as the $\ell_{1}$ or the $\ell_{2}$-norm. The use of $\ell_{1}$-regularization tends to induce sparsity in $\beta$, which in turn helps to combat overfitting effects Tibshirani94regressionshrinkage. Moreover, $\ell_{1}$-regularized logistic regression serves as an effective means for feature selection. It is further shown in ng2004feature that $\ell_{1}$-regularization outperforms $\ell_{2}$-regularization when the number of training samples is smaller than the number of features.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Logistic Regression", "weight": 1.0} -->

On the downside, $\ell_{1}$-regularization leads to non-smooth optimization problems, which are more challenging. Algorithms for large scale regularized logistic regression are discussed in Koh07aninterior-point; shalev2011stochastic; shi2010fast; yun2011coordinate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Distributionally Robust Optimization", "weight": 1.0} -->

Regression and classification problems are typically modeled as optimization problems under uncertainty. To date, optimization under uncertainty has been addressed by several complementary modeling paradigms that differ mainly in the representation of uncertainty. For instance, stochastic programming assumes that the uncertainty is governed by a known probability distribution and aims to minimize a probability functional such as the expected cost or a quantile of the cost distribution shapiro2014lectures; birgelouveaux. In contrast, robust optimization ignores all distributional information and aims to minimize the worst-case cost under all possible uncertainty realizations ben2002robust; bertsimas2004price; ben2009robust. While stochastic programs may rely on distributional information that is not available or hard to acquire in practice, robust optimization models may adopt an overly pessimistic view of the uncertainty and thereby promote over-conservative decisions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Distributionally Robust Optimization", "weight": 1.0} -->

The emerging field of distributionally robust optimization aims to bridge the gap between the conservatism of robust optimization and the specificity of stochastic programming: it seeks to minimize a worst-case probability functional (e.g., the worst-case expectation), where the worst case is taken with respect to an ambiguity set, that is, a family of distributions consistent with the given prior information on the uncertainty. The vast majority of the existing literature focuses on ambiguity sets characterized through moment and support information, see e.g. delage2010distributionally; goh2010distributionally; wiesemann2014distributionally. However, ambiguity sets can also be constructed via distance measures in the space of probability distributions such as the Prohorov metric erdougan2006ambiguous or the Kullback-Leibler divergence hu2013kullback. Due to its attractive measure concentration properties, we use here the Wasserstein metric to construct ambiguity sets.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution", "weight": 1.0} -->

In this paper we propose a distributionally robust perspective on logistic regression. Our research is motivated by the well-known observation that regularization techniques can improve the out-of-sample performance of many classifiers. In the context of support vector machines and Lasso, there have been several recent attempts to give ad hoc regularization techniques a robustness interpretation xu2009robustness; xu2010robust. However, to the best of our knowledge, no such connection has been established for logistic regression. In this paper we aim to close this gap by adopting a new distributionally robust optimization paradigm based on Wasserstein ambiguity sets MohKun-14. Starting from a data-driven distributionally robust statistical learning setup, we will derive a family of regularized logistic regression models that admit an intuitive probabilistic interpretation and encapsulate the classical regularized logistic regression as a special case. Moreover, by invoking recent measure concentration results, our proposed approach provides a probabilistic guarantee for the emerging regularized classifiers, which seems to be the first result of this type. All proofs are relegated to the technical appendix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contribution", "weight": 1.0} -->

We summarize our main contributions as follows: Distributionally robust logistic regression model and tractable reformulation: We propose a data-driven distributionally robust logistic regression model based on an ambiguity set induced by the Wasserstein distance. We prove that the resulting semi-infinite optimization problem admits an equivalent reformulation as a tractable convex program.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contribution", "weight": 1.0} -->

Risk estimation: Using similar distributionally robust optimization techniques based on the Wasserstein ambiguity set, we develop two highly tractable linear programs whose optimal values provide confidence bounds on the misclassification probability or *risk* of the emerging classifiers.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution", "weight": 1.0} -->

Out-of-sample performance guarantees: Adopting a distributionally robust framework allows us to invoke results from the measure concentration literature to derive finite-sample probabilistic guarantees. Specifically, we establish *out-of-sample* performance guarantees for the classifiers obtained from the proposed distributionally robust optimization model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contribution", "weight": 1.0} -->

Probabilistic interpretation of existing regularization techniques: We show that the standard regularized logistic regression is a special case of our framework. In particular, we show that the regularization coefficient $\varepsilon$ in can be interpreted as the size of the ambiguity set underlying our distributionally robust optimization model.

<!-- chunk {"id": "body-0015", "role": "body", "section": "A distributionally robust perspective on statistical learning", "weight": 1.0} -->

In the standard statistical learning setting all training and test samples are drawn independently from some distribution $\mathbb{P}$ supported on $\Xi = {{\mathbb{R}}^{n} \times {\{{- 1},{+ 1}\}}}$. If the distribution $\mathbb{P}$ was known, the best weight parameter $\beta$ could be found by solving the stochastic optimization problem In practice, however, $\mathbb{P}$ is only indirectly observable through $N$ independent training samples. Thus, the distribution $\mathbb{P}$ is itself uncertain, which motivates us to address problem from a distributionally robust perspective. This means that we use the training samples to construct an ambiguity set $\mathcal{P}$, that is, a family of distributions that contains the unknown distribution $\mathbb{P}$ with high confidence. Then we solve the distributionally robust optimization problem which minimizes the worst-case expected logloss function. The construction of the ambiguity set $\mathcal{P}$ should be guided by the following principles.

<!-- chunk {"id": "body-0016", "role": "body", "section": "A distributionally robust perspective on statistical learning", "weight": 1.0} -->

(i) Tractability: It must be possible to solve the distributionally robust optimization problem efficiently. (ii) Reliability: The optimizer of should be near-optimal, thus facilitating attractive out-of-sample guarantees. (iii) Asymptotic consistency: For large training data sets, the solution of should converge to the one of. In this paper we propose to use the Wasserstein metric to construct $\mathcal{P}$ as a ball in the space of probability distributions that satisfies (i)--(iii).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tractable reformulation and probabilistic guarantees", "weight": 1.0} -->

In this section we demonstrate that can be reformulated as a tractable convex program and establish probabilistic guarantees for its optimal solutions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Tractable reformulation", "weight": 1.0} -->

We first define a metric on the feature-label space, which will be used in the remainder.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1 (Regularized Logistic Regression)", "weight": 1.0} -->

As the parameter $\kappa > 0$ characterizing the metric $d{(\cdot, \cdot)}$ tends to infinity, the second constraint group in the convex program (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) becomes redundant. Hence, (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) reduces to the celebrated regularized logistic regression problem where the regularization function is determined by the dual norm on the feature space, while the regularization coefficient coincides with the radius of the Wasserstein ball. Note that for $\kappa = \infty$ the Wasserstein distance between two distributions is infinite if they assign different labels to a fixed feature vector with positive probability.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1 (Regularized Logistic Regression)", "weight": 1.0} -->

Any distribution in ${\mathbb{B}}_{\varepsilon}{({\hat{\mathbb{P}}}_{N})}$ must then have non-overlapping conditional supports for $y = {+ 1}$ and $y = {- 1}$. Thus, setting $\kappa = \infty$ reflects the belief that the label is a (deterministic) function of the feature and that label measurements are exact. As this belief is not tenable in most applications, an approach with $\kappa < \infty$ may be more satisfying.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Out-of-sample performance guarantees", "weight": 1.0} -->

We now exploit a recent measure concentration result characterizing the speed at which ${\hat{\mathbb{P}}}_{N}$ converges to $\mathbb{P}$ with respect to the Wasserstein distance fournier2013rate in order to derive out-of-sample performance guarantees for distributionally robust logistic regression.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Out-of-sample performance guarantees", "weight": 1.0} -->

In the following, we let ${\hat{\Xi}}_{N}:={\{{({\hat{x}}_{i},{\hat{y}}_{i})}\}}_{i = 1}^{N}$ be a set of $N$ independent training samples from $\mathbb{P}$, and we denote by ${\hat{\beta},\hat{\lambda}},$ and ${\hat{s}}_{i}$ the optimal solutions and $\hat{J}$ the corresponding optimal value of (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")). Note that these values are random objects as they depend on the random training data ${\hat{\Xi}}_{N}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2 (Worst-Case Loss)", "weight": 1.0} -->

Denoting the empirical logloss function on the training set ${\hat{\Xi}}_{N}$ by ${\mathbb{E}}^{{\hat{\mathbb{P}}}^{N}}{\lbrack{l_{\hat{\beta}}{(x,y)}}\rbrack}$, the worst-case loss $\hat{J}$ can be expressed as Note that the last term in (9. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) can be viewed as a complementary regularization term that does not appear in standard regularized logistic regression. This term accounts for label uncertainty and decreases with $\kappa$. Thus, $\kappa$ can be interpreted as our trust in the labels of the training samples. Note that this regularization term vanishes for $\kappa\rightarrow\infty$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2 (Worst-Case Loss)", "weight": 1.0} -->

One can further prove that $\hat{\lambda}$ converges to ${\|\hat{\beta}\|}_{\ast}$ for $\kappa\rightarrow\infty$, implying that (9. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) reduces to the standard regularized logistic regression in this limit.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3 (Performance Guarantees)", "weight": 1.0} -->

The following comments are in order: Light-Tail Assumption: The light-tail assumption of Theorem 2. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression") is restrictive but seems to be unavoidable for any a priori guarantees of the type described in Theorem 2. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression"). Note that this assumption is automatically satisfied if the features have bounded support or if they are known to follow, for instance, a Gaussian or exponential distribution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3 (Performance Guarantees)", "weight": 1.0} -->

Asymptotic Consistency: For any fixed confidence level $\eta$, the radius $\varepsilon_{N}{(\eta)}$ defined in (8. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) drops to zero as the sample size $N$ increases, and thus the ambiguity set shrinks to a singleton. To be more precise, with probability 1 across all training datasets, a sequence of distributions in the ambiguity set converges in the Wasserstein metric, and thus weakly, to the unknown data generating distribution $\mathbb{P}$; see (MohKun-14 Corollary 3.4) for a formal proof. Consequently, the solution of can be shown to converge to the solution of as $N$ increases.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3 (Performance Guarantees)", "weight": 1.0} -->

Finite Sample Behavior: The a priori bound (8. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) on the size of the Wasserstein ball has two growth regimes. For small $N$, the radius decreases as $N^{\frac{1}{a}}$, and for large $N$ it scales with $N^{\frac{1}{n}}$, where $n$ is the dimension of the feature space. We refer to (fournier2013rate Section 1.3) for further details on the optimality of these rates and potential improvements for special cases. Note that when the support of the underlying distribution $\mathbb{P}$ is bounded or $\mathbb{P}$ has a Gaussian distribution, the parameter $a$ can be effectively set to 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Risk Estimation: Worst- and Best-Cases", "weight": 1.0} -->

One of the main objectives in logistic regression is to control the classification performance. Specifically, we are interested in *predicting* labels from features. This can be achieved via a classifier function ${f_{\beta}:{{\mathbb{R}}^{n}\rightarrow{\{{+ 1},{- 1}\}}}},$ whose *risk* ${\Re{(\beta)}}:={{\mathbb{P}}\left\lbrack {y \neq {f_{\beta}{(x)}}} \right\rbrack}$ represents the misclassification probability. In logistic regression, a natural choice for the classifier is $f_{\beta}{(x)} = + 1\text{~if Prob}{( + 1|x)} > 0.5; = - 1\text{~otherwise.}$ The conditional probability $\text{Prob}{(\left. y \middle| x \right.)}$ is defined.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Risk Estimation: Worst- and Best-Cases", "weight": 1.0} -->

The risk associated with this classifier can be expressed as ${{\Re{(\beta)}} = {{\mathbb{E}}^{\mathbb{P}}\left\lbrack \mathbb{1}_{\{{{y{\langle\beta,x\rangle}} \leq 0}\}} \right\rbrack}}.$ As in Section 3.1, we can use worst- and best-case expectations over Wasserstein balls to construct confidence bounds on the risk.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We now showcase the power of distributionally robust logistic regression in simulated and empirical experiments. All optimization problems are implemented in MATLAB via the modeling language YALMIP yalmip and solved with the state-of-the-art nonlinear programming solver IPOPT wachter2006implementation. All experiments were run on an Intel XEON CPU (3.40GHz). For the largest instance studied ($N = 1000$), the problems (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) and (10. ‣ 3.3 Risk Estimation: Worst- and Best-Cases ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) were solved in 2.1, 4.2, 9.2 and 0.05 seconds, respectively.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiment 1: Out-of-Sample Performance", "weight": 1.0} -->

We use a simulation experiment to study the out-of-sample performance guarantees offered by distributionally robust logistic regression. As in ng2004feature, we assume that the features $x \in {\mathbb{R}}^{10}$ follow a multivariate standard normal distribution and that the conditional distribution of the labels $y \in {\{{+ 1},{- 1}\}}$ is of the form with $\beta = {(10,0,\ldots,0)}$. The true distribution $\mathbb{P}$ is uniquely determined by this information. If we use the $\ell_{\infty}$-norm to measure distances in the feature space, then $\mathbb{P}$ satisfies the light-tail assumption of Theorem 2. ‣ 3.2 Out-of-sample performance guarantees ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression") for $2 > a \gtrsim 1$. Finally, we set $\kappa = 1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiment 1: Out-of-Sample Performance", "weight": 1.0} -->

Our experiment comprises 100 simulation runs. In each run we generate $N \in {\{ 10,10^{2},10^{3}\}}$ training samples and $10^{4}$ test samples from $\mathbb{P}$. We calibrate the distributionally robust logistic regression model to the training data and use the test data to evaluate the average logloss as well as the correct classification rate (CCR) of the classifier associated with $\hat{\beta}$. We then record the percentage ${\hat{\eta}}_{N}{(\varepsilon)}$ of simulation runs in which the average logloss exceeds $\hat{J}$. Moreover, we calculate the average CCR across all simulation runs. Figure 1 displays both $1 - {{\hat{\eta}}_{N}{(\varepsilon)}}$ and the average CCR as a function of $\varepsilon$ for different values of $N$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiment 2: The Effect of the Wasserstein Ball", "weight": 1.0} -->

In the second simulation experiment we study the statistical properties of the out-of-sample logloss. As in feng2014robust, we set $n = 10$ and assume that the features follow a multivariate standard normal distribution, while the conditional distribution of the labels is of the form with $\beta$ sampled uniformly from the unit sphere. We use the $\ell_{2}$-norm in the feature space, and we set $\kappa = 1$. All results reported here are averaged over 100 simulation runs. In each trial, we use $N = 10^{2}$ training samples to calibrate problem and $10^{4}$ test samples to estimate the logloss distribution of the resulting classifier.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment 2: The Effect of the Wasserstein Ball", "weight": 1.0} -->

(a) CVaR versus quantile of the logloss function (b) CVaR versus quantile of the logloss function (zoomed) (c) Cumulative distribution of the logloss function Figure 2: CVaR and CDF of the logloss function for different Wasserstein radii ε As expected, using a distributionally robust approach renders the logistic regression problem more 'risk-averse', which results in uniformly lower CVaR values of the logloss, particularly for smaller confidence levels. Thus, increasing the radius of the Wasserstein ball reduces the right tail of the logloss distribution. Figure 2(c) confirms this observation by showing that the cumulative distribution function (CDF) of the logloss converges to a step function for large $\varepsilon$. Moreover, one can prove that the weight vector $\hat{\beta}$ tends to zero as $\varepsilon$ grows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment 2: The Effect of the Wasserstein Ball", "weight": 1.0} -->

Specifically, for $\varepsilon \geq 0.1$ we have $\beta \approx 0$, in which case the logloss approximates the deterministic value ${\log{}} = 0.69$. Zooming into the CVaR graph of Figure 2(a) at the end of the high confidence levels, we observe that the 100%-CVaR, which coincides in fact with the expected logloss, increases at every quantile level; see Figure 2(b).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment 3: Real World Case Studies and Risk Estimation", "weight": 1.0} -->

Next, we validate the performance of the proposed distributionally robust logistic regression method on the MNIST dataset MNIST and three popular datasets from the UCI repository: Ionosphere, Thoracic Surgery, and Breast Cancer UCI2013. In this experiment, we use the distance function of Definition 2. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression") with the $\ell_{1}$-norm. We examine three different models: logistic regression (LR), regularized logistic regression (RLR), and distributionally robust logistic regression with $\kappa = 1$ (DRLR). All results reported here are averaged over 100 independent trials. In each trial related to a UCI dataset, we randomly select 60% of data to train the models and the rest to test the performance. Similarly, in each trial related to the MNIST dataset, we randomly select $10^{3}$ samples from the training dataset, and test the performance on the complete test dataset.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment 3: Real World Case Studies and Risk Estimation", "weight": 1.0} -->

The results in Table 1 (top) indicate that DRLR outperforms RLR in terms of CCR by about the same amount by which RLR outperforms classical LR (0.3%--1%), consistently across all experiments. We also evaluated the out-of-sample CVaR of logloss, which is a natural performance indicator for robust methods. Table 1 (bottom) shows that DRLR wins by a large margin (outperforming RLR by 4%--43%).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment 3: Real World Case Studies and Risk Estimation", "weight": 1.0} -->

In the remainder we focus on the Ionosphere case study (the results of which are representative for the other case studies). Figures 3(a) and 3(b) depict the logloss and the CCR for different Wasserstein radii $\varepsilon$. DRLR ($\kappa = 1$) outperforms RLR ($\kappa = \infty$) consistently for all sufficiently small values of $\varepsilon$. This observation can be explained by the fact that DRLR accounts for uncertainty in the label, whereas RLR does not. Thus, there is a wider range of Wasserstein radii that result in an attractive out-of-sample logloss and CCR. This effect facilitates the choice of $\varepsilon$ and could be a significant advantage in situations where it is difficult to determine $\varepsilon$ a priori.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment 3: Real World Case Studies and Risk Estimation", "weight": 1.0} -->

(a) The average logloss for different κ (b) The average correct classification rate for different κ (c) Risk estimation and its confidence level Figure 3: Average logloss, CCR and risk for different Wasserstein radii ε (Ionosphere dataset) In the experiment underlying Figure 3(c), we first fix $\hat{\beta}$ to the optimal solution of (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) for $\varepsilon = 0.003$ and $\kappa = 1$. Figure 3(c) shows the true risk $\Re{(\hat{\beta})}$ and its confidence bounds. As expected, for $\varepsilon = 0$ the upper and lower bounds coincide with the empirical risk on the training data, which is a lower bound for the true risk on the test data due to over-fitting effects. As $\varepsilon$ increases, the confidence interval between the bounds widens and eventually covers the true risk.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment 3: Real World Case Studies and Risk Estimation", "weight": 1.0} -->

For instance, at $\varepsilon \approx 0.05$ the confidence interval is given by $\lbrack 0,0.19\rbrack$ and contains the true risk with probability ${1 - {2\hat{\eta}}} = {95\%}$.
