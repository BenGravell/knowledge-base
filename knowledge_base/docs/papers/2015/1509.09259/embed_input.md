Distributionally Robust Logistic Regression

This paper proposes a distributionally robust approach to logistic regression. We use the Wasserstein distance to construct a ball in the space of probability distributions centered at the uniform distribution on the training samples. If the radius of this ball is chosen judiciously, we can guarantee that it contains the unknown data-generating distribution with high confidence. We then formulate a distributionally robust logistic regression model that minimizes a worst-case expected logloss function, where the worst case is taken over all distributions in the Wasserstein ball. We prove that this optimization problem admits a tractable reformulation and encapsulates the classical as well as the popular regularized logistic regression problems as special cases. We further propose a distributionally robust approach based on Wasserstein balls to compute upper and lower confidence bounds on the misclassification probability of the resulting classifier. These bounds are given by the optimal values of two highly tractable linear programs. We validate our theoretical out-of-sample guarantees through simulated and empirical experiments.

## Introduction

Logistic regression is one of the most frequently used classification methods applied. Its objective is to establish a probabilistic relationship between a continuous feature vector and a binary explanatory variable. However, in spite of its overwhelming success in machine learning, data analytics and medicine etc., logistic regression models can display a poor out-of-sample performance if training data is sparse. In this case modelers often resort to ad hoc regularization techniques in order to combat overfitting effects....

### Logistic Regression

Figure 3: Average logloss, CCR and risk for different Wasserstein radii ε (Ionosphere dataset)

In the experiment underlying Figure 3(c), we first fix $\hat{\beta}$ to the optimal solution of (7. ‣ 3.1 Tractable reformulation ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) for $\varepsilon = 0.003$ and $\kappa = 1$. Figure 3(c) shows the true risk $\Re{(\hat{\beta})}$ and its confidence bounds. As expected, for $\varepsilon = 0$ the upper and lower bounds coincide with the empirical risk on the training data, which is a lower bound for the true risk on the test data due to over-fitting effects....

### Theorem 2 (Out-of-Sample Performance)

In this section we demonstrate that can be reformulated as a tractable convex program and establish probabilistic guarantees for its optimal solutions.

We emphasize that (10a. ‣ 3.3 Risk Estimation: Worst- and Best-Cases ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) and (10b. ‣ 3.3 Risk Estimation: Worst- and Best-Cases ‣ 3 Tractable reformulation and probabilistic guarantees ‣ Distributionally Robust Logistic Regression")) constitute highly tractable linear programs. Moreover, we have ${\Re_{\min}{(\hat{\beta})}} \leq {\Re{(\hat{\beta})}} \leq {\Re_{\max}{(\hat{\beta})}}$ with probability $1 - {2\eta}$.

Let $x \in {\mathbb{R}}^{n}$ denote a feature vector and $y \in {\{{- 1},{+ 1}\}}$ the associated binary label to be predicted. In logistic regression, the conditional distribution of $y$ given $x$ is modeled as

where the weight vector $\beta \in {\mathbb{R}}^{n}$ constitutes an unknown regression parameter. Suppose that $N$ training samples ${\{{({\hat{x}}_{i},{\hat{y}}_{i})}\}}_{i = 1}^{N}$ have been observed....
