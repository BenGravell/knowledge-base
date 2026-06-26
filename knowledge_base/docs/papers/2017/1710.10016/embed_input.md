<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regularization via Mass Transportation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The goal of regression and classification methods in supervised learning is to minimize the empirical risk, that is, the expectation of some loss function quantifying the prediction error under the empirical distribution. When facing scarce training data, overfitting is typically mitigated by adding regularization terms to the objective that penalize hypothesis complexity. In this paper we introduce new regularization techniques using ideas from distributionally robust optimization, and we give new probabilistic interpretations to existing techniques. Specifically, we propose to minimize the worst-case expected loss, where the worst case is taken over the ball of all (continuous or discrete) distributions that have a bounded transportation distance from the (discrete) empirical distribution. By choosing the radius of this ball judiciously, we can guarantee that the worst-case expected loss provides an upper confidence bound on the loss on test data, thus offering new generalization bounds. We prove that the resulting regularized learning problems are tractable and can be tractably kernelized for many popular loss functions. We validate our theoretical out-of-sample guarantees through simulated and empirical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fields of machine learning and optimization are closely intertwined. On the one hand, optimization algorithms are routinely used for the solution of classical machine learning problems. Conversely, recent advances in optimization under uncertainty have inspired many new machine learning models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a conceptual point of view, many statistical learning tasks give naturally rise to stochastic optimization problems. Indeed, they aim to find an estimator from within a prescribed hypothesis space that minimizes the expected value of some loss function. The loss function quantifies the estimator's ability to correctly predict random outputs (i.e., dependent variables or labels) from random inputs (i.e., independent variables or features). Unfortunately, such stochastic optimization problems cannot be solved exactly because the input-output distribution, which is needed to evaluate the expected loss in the objective function, is not accessible and only indirectly observable through finitely many training samples. Approximating the expected loss with the empirical loss, that is, the average loss across all training samples, yields fragile estimators that are sensitive to perturbations in the data and suffer from overfitting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regularization is the standard remedy to combat overfitting. Regularized learning models minimize the sum of the empirical loss and a penalty for hypothesis complexity, which is typically chosen as a norm of the hypothesis. There is ample empirical evidence that regularization reduces a model's generalization error. Statistical learning theory reasons that regularization implicitly restricts the hypothesis space, thereby controlling the gap between the training error and the testing error, see, e.g., Bartlett and Mendelson. However, alternative explanations for the practical success of regularization are possible. In particular, ideas from modern robust optimization (Ben-Tal et al. ) recently led to a fresh perspective on regularization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust regression and classification models seek estimators that are immunized against adversarial perturbations in the training data. They have received considerable attention since the seminal treatise on robust least-squares regression by El Ghaoui and Lebret, who seem to be the first authors to discover an intimate connection between robustification and regularization. Specifically, they show that minimizing the worst-case residual error with respect to all perturbations in a Frobenius norm-uncertainty set is equivalent to a Tikhonov regularization procedure. Xu et al. disclose a similar equivalence between robust least-squares regression with a feature-wise independent uncertainty set and the celebrated Lasso (least absolute shrinkage and selection operator) algorithm. Leveraging this new robustness interpretation, they extend Lasso to a wider class of regularization schemes tailored to regression problems with disturbances that are coupled across features. In the context of classification, Xu et al. provide a linkage between robustification over non-box-typed uncertainty sets and the standard regularization scheme of support vector machines. A comprehensive characterization of the conditions under which robustification and regularization are equivalent has recently been compiled by Bertsimas and Copenhaver.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

New learning models have also been inspired by recent advances in the emerging field of distributionally robust optimization, which bridges the gap between the conservatism of robust optimization and the specificity of stochastic programming. Distributionally robust optimization seeks to minimize a worst-case expected loss, where the worst case is taken with respect to all distributions in an ambiguity set, that is, a family of distributions consistent with the given prior information on the uncertainty, see, e.g., Calafiore and El Ghaoui, Delage and Ye, Goh and Sim, Wiesemann et al. and the references therein. Ambiguity sets are often characterized through generalized moment conditions. For instance, Lanckriet et al. propose a distributionally robust minimax probability machine for binary classification, where both classes are encoded by the first and second moments of their features, and the goal is to find a linear classifier that minimizes the worst-case misclassification error in view of all possible input distributions consistent with the given moment information. By construction, this approach forces the worst-case accuracies of both classes to be equal.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Huang et al. propose a generalization of the minimax probability machine that allows for uneven worst-case classification accuracies. Lanckriet et al. extend the minimax probability machine to account for estimation errors in the mean vectors and covariance matrices. Strohmann and Grudic and Bhattacharyya develop minimax probability machines for regression and feature selection, respectively. Shivaswamy et al. study linear classification problems trained with incomplete and noisy features, where each training sample is modeled by an ambiguous distribution with known first and second-order moments. The authors propose to address such classification problems with a distributionally robust soft margin support vector machine and then prove that it is equivalent to a classical robust support vector machine with a feature-wise uncertainty set. Farnia and Tse investigate distributionally robust learning models with moment ambiguity sets that restrict the marginal of the features to the empirical marginal. The authors highlight similarities and differences to classical regression models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ambiguity sets containing all distributions that share certain low-order moments are computationally attractive but fail to converge to a singleton when the number $N$ of training samples tends to infinity. Thus, they preclude any asymptotic consistency results. A possible remedy is to design spherical ambiguity sets with respect to some probability distance functions and to drive their radii to zero as $N$ grows. Examples include the $\phi$-divergence ambiguity sets proposed by Ben-Tal et al. or the Wasserstein ambiguity sets studied by Mohajerin Esfahani and Kuhn and Zhao and Guan. Blanchet and Murthy and Gao and Kleywegt consider generalized Wasserstein ambiguity sets defined over Polish spaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we investigate distributionally robust learning models with Wasserstein ambiguity sets. The Wasserstein distance between two distributions is defined as the minimum cost of transporting one distribution to the other, where the cost of moving a unit point mass is determined by the ground metric on the space of uncertainty realizations. In computer science the Wasserstein distance is therefore sometimes aptly termed the 'earth mover's distance' (Rubner et al. ). Following Mohajerin Esfahani and Kuhn, we define Wasserstein ambiguity sets as balls with respect to the Wasserstein distance that are centered at the empirical distribution on the training samples. These ambiguity sets contain all (continuous or discrete) distributions that can be converted to the (discrete) empirical distribution at bounded transportation cost.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Wasserstein distances are widely used in machine learning to compare histograms. For example, Rubner et al. use the Wasserstein distance as a metric for image retrieval with a focus on applications to color and texture. Cuturi and Benamou et al. propose fast iterative algorithms to compute a regularized Wasserstein distance between two high-dimensional discrete distributions for image classification tasks. Moreover, Cuturi and Doucet develop first-order algorithms to compute the Wasserstein barycenter between several empirical probability distributions, which has applications in clustering. Arjovsky et al. utilize the Wasserstein distance to measure the distance between the data distribution and the model distribution in generative adversarial networks. Furthermore, Frogner et al. propose a learning algorithm based on the Wasserstein distance to predict multi-label outputs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization models with Wasserstein ambiguity sets were introduced to the realm of supervised learning by Shafieezadeh-Abadeh et al., who show that distributionally robust logistic regression problems admit a tractable reformulation and encapsulate the classical as well as the popular regularized logistic regression problems as special cases. When the Wasserstein ball is restricted to distributions on a compact set, the problem becomes intractable but can still be addressed with an efficient decomposition algorithm due to Luo and Mehrotra. Support vector machine models with distributionally robust chance constraints over Wasserstein ambiguity sets are studied by Lee and Mehrotra. These models are equivalent to hard semi-infinite programs and can be solved approximately with a cutting plane algorithm.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Wasserstein ambiguity sets are popular for their attractive statistical properties. For example, Fournier and Guillin prove that the empirical distribution on $N$ training samples converges in Wasserstein distance to the true distribution at rate $\mathcal{O}{(N^{- {1/{({n + 1})}}})}$, where $n$ denotes the feature dimension. This implies that properly scaled Wasserstein balls constitute natural confidence regions for the data-generating distribution. The worst-case expected prediction loss over all distributions in a Wasserstein ball thus provides an upper confidence bound on the expected loss under the unknown true distribution; see Mohajerin Esfahani and Kuhn. Blanchet et al. show, however, that radii of the order $\mathcal{O}{(N^{- {1/2}})}$ are asymptotically optimal even though the corresponding Wasserstein balls are too small to contain the true distribution with constant confidence. For Wasserstein distances of type two (where the transportation cost equals the squared ground metric) Blanchet et al. develop a systematic methodology for selecting the ground metric.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generalization bounds for the worst-case prediction loss with respect to a Wasserstein ball centered at the true distribution are derived by Lee and Raginsky in order to address emerging challenges in domain adaptation problems, where the distributions of the training and test samples can differ.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper extends the results by Shafieezadeh-Abadeh et al. on distributionally robust logistic regression along several dimensions. Our main contributions can be summarized as follows: Tractability: We propose data-driven distributionally robust regression and classification models that hedge against all input-output distributions in a Wasserstein ball. We demonstrate that the emerging semi-infinite optimization problems admit equivalent reformulations as tractable convex programs for many commonly used loss functions and for spaces of linear hypotheses. We also show that lifted variants of these new learning models are kernelizable and thus offer an efficient procedure for optimizing over all nonlinear hypotheses in a reproducible kernel Hilbert space. Finally, we study distributionally robust learning models over families of feed-forward neural networks. We show that these models can be approximated by regularized empirical loss minimization problems with a convex regularization term and can be addressed with a stochastic proximal gradient descent algorithm.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Probabilistic Interpretation of Existing Regularization Techniques: We show that the classical regularized learning models emerge as special cases of our framework when the cost of moving probability mass along the output space tends to infinity. In this case, the regularization function and its regularization weight are determined by the transportation cost on the input space and the radius of the Wasserstein ball underlying the distributionally robust optimization model, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generalization Bounds: We demonstrate that the proposed distributionally robust learning models enjoy new generalization bounds that can be obtained under minimal assumptions. In particular, they do not rely on any notions of hypothesis complexity and may therefore even extend to hypothesis spaces with infinite VC-dimensions. A naïve generalization bound is obtained by leveraging modern measure concentration results, which imply that Wasserstein balls constitute confidence sets for the unknown data-generating distribution. Unfortunately, this generalization bound suffers from a curse of dimensionality and converges slowly for high input dimensions. By imposing bounds on the hypothesis space, however, we can derive an improved generalization bound, which essentially follows a dimension-independent square root law reminiscent of the central limit theorem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relation to Robust Optimization: In classical robust regression and classification the training samples are viewed as uncertain variables that range over a joint uncertainty set, and the best hypothesis is found by minimizing the worst-case loss over this set. We prove that the classical robust and new distributionally robust learning models are equivalent if the data satisfies a dispersion condition (for regression) or a separability condition (for classification). While there is no efficient algorithm for solving the robust learning models in the absence of this condition, the distributionally robust models are efficiently solvable irrespective of the underlying training datasets.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Confidence Intervals for Error and Risk: Using distributionally robust optimization techniques based on the Wasserstein ball, we develop two tractable linear programs whose optimal values provide a confidence interval for the absolute prediction error of any fixed regressor or the misclassification risk of any fixed classifier.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Worst-Case Distributions: We formulate tractable convex programs that enable us to efficiently compute a worst-case distribution in the Wasserstein ball for any fixed hypothesis. This worst-case distribution can be useful for stress tests or contamination experiments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper develops as follows. Section 2 introduces our new distributionally robust learning models. Section 3 provides finite convex reformulations for learning problems over linear and nonlinear hypothesis spaces and describes efficient procedures for constructing worst-case distributions. Moreover, it compares the new distributionally robust method against existing robust optimization and regularization approaches. Section 4 develops new generalization bounds, while Section 5 addresses error and risk estimation. Numerical experiments are reported in Section 6. All proofs are relegated to the appendix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We first introduce the basic terminology and then describe our new perspective on regularization.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Classical Statistical Learning", "weight": 1.0} -->

The goal of supervised learning is to infer an unknown target function $f:{{\mathbb{X}}\rightarrow{\mathbb{Y}}}$ from limited data. The target function maps any input ${\mathbf{x}} \in {\mathbb{X}}$ (e.g., information on the frequency of certain keywords in an email) to some output $y \in {\mathbb{Y}}$ (e.g., a label $+ 1$ ($- 1$) if the email is likely (unlikely) to be a spam message). If the true target function was accessible, it could be used as a means to reliably predict outputs from inputs (e.g., it could be used to recognize spam messages in an automated fashion).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Classical Statistical Learning", "weight": 1.0} -->

In a supervised learning framework, however, one has only access to finitely many input-output examples $({\hat{\mathbf{x}}}_{i},{\hat{y}}_{i})$ for $i = {1,\ldots,N}$ (e.g., a database of emails which have been classified by a human as legitimate or as spam messages). We will henceforth refer to these examples as the training data or the in-sample data. It is assumed that the training samples are mutually independent and follow an unknown distribution $\mathbb{P}$ on ${\mathbb{X}} \times {\mathbb{Y}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Classical Statistical Learning", "weight": 1.0} -->

The supervised learning problems are commonly subdivided into *regression problems*, where the output $y$ is continuous and ${\mathbb{Y}} = {\mathbb{R}}$, and *classification problems*, where $y$ is categorical and ${\mathbb{Y}} = {\{{+ 1},{- 1}\}}$. As the space of all functions from $\mathbb{X}$ to $\mathbb{Y}$ is typically vast, it may be very difficult to learn the target function from finitely many training samples. Thus, it is convenient to restrict the search space to a structured family of candidate functions ${\mathbb{H}} \subseteq {\mathbb{R}}^{\mathbb{X}}$ such as the space of all linear functions, some reproducible kernel Hilbert space or the family of all feed-forward neural networks with a fixed number of layers. We henceforth refer to each candidate function $h \in {\mathbb{H}}$ as a hypothesis and to $\mathbb{H}$ as the hypothesis space.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Classical Statistical Learning", "weight": 1.0} -->

A learning algorithm is a method for finding a hypothesis $h \in {\mathbb{H}}$ that faithfully replicates the unknown target function $f$. Specifically, in regression we seek to approximate $f$ with a hypothesis $h$, and in classification we seek to approximate $f$ with a thresholded hypothesis $\text{sign}{(h)}$. Many learning algorithms achieve this goal by minimizing the in-sample error, that is, the empirical average of a loss function $\ell:{{{\mathbb{R}} \times {\mathbb{Y}}}\rightarrow{\mathbb{R}}_{+}}$ that estimates the mismatch between the output predicted by $h{({\mathbf{x}})}$ and the actual output $y$ for a particular input-output pair $({\mathbf{x}},y)$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Classical Statistical Learning", "weight": 1.0} -->

Any such algorithm solves a minimization problem of the form where ${\hat{\mathbb{P}}}_{N} = {\frac{1}{N}{\sum_{i = 1}^{N}\delta_{({\hat{\mathbf{x}}}_{i},{\hat{y}}_{i})}}}$ denotes the empirical distribution, that is, the uniform distribution on the training data. For different choices of the the loss function $\ell$, the generic supervised learning problem reduces to different popular regression and classification problems from the literature.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

For ease of exposition, we focus here on learning models with ${\mathbb{X}} \subseteq {\mathbb{R}}^{n}$ and ${\mathbb{Y}} \subseteq {\mathbb{R}}$, where $\mathbb{H}$ is set to the space of all linear hypotheses ${h{({\mathbf{x}})}} = {\langle{\mathbf{w}},{\mathbf{x}}\rangle}$ with ${\mathbf{w}} \in {\mathbb{R}}^{n}$. Thus, there is a one-to-one correspondence between hypotheses and weight vectors $\mathbf{w}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

Moreover, we focus on loss functions of the form $\ell{(h{({\mathbf{x}})},y)} = L{(h{({\mathbf{x}})} - y)} = L{({\langle{\mathbf{w}},{\mathbf{x}}\rangle})} - y)$ that are generated by a univariate loss function $L$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

A rich class of robust regression problems is obtained from if $\ell$ is generated by the Huber loss function with robustness parameter $\delta > 0$, which is defined as ${L{(z)}} = {\frac{1}{2}z^{2}}$ if ${|z|} \leq \delta$; $= {\delta{({{|z|} - {\frac{1}{2}\delta}})}}$ otherwise. Note that the Huber loss function is both convex and smooth and reduces to the squared loss ${L{(z)}} = {\frac{1}{2}z^{2}}$ for $\delta \uparrow \infty$, which is routinely used in ordinary least squares regression. Problem with squared loss seeks a hypothesis $\mathbf{w}$ under which $\langle{\mathbf{w}},{\mathbf{x}}\rangle$ approximates the mean of $y$ conditional on $\mathbf{x}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

The Huber loss function for finite $\delta$ favors similar hypotheses but is less sensitive to outliers.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

The support vector regression problem emerges as a special case of if $\ell$ is generated by the $\epsilon$-insensitive loss function ${L{(z)}} = {\max{\{ 0,{{|z|} - \epsilon}\}}}$ with $\epsilon \geq 0$. In this setting, a training sample $({\hat{\mathbf{x}}}_{i},{\hat{y}}_{i})$ is penalized in only if the output $\langle{\mathbf{w}},{\hat{\mathbf{x}}}_{i}\rangle$ predicted by hypothesis $\mathbf{w}$ differs from the true output ${\hat{y}}_{i}$ by more than $\epsilon$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

Support vector regression thus seeks hypotheses $\mathbf{w}$ under which all training samples reside within a slab of width $2\epsilon$ centered around the hyperplane $\{{({\mathbf{x}},y)}:{{\langle{\mathbf{w}},{\mathbf{x}}\rangle} = y}\}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Examples of Regression Models", "weight": 1.0} -->

The quantile regression problem is obtained from if $\ell$ is generated by the pinball loss function ${L{(z)}} = {\max{\{{- {\tauz}},{{({1 - \tau})}z}\}}}$ defined for $\tau \in {\lbrack 0,1\rbrack}$. Quantile regression seeks hypotheses that approximate the $\tau \times {100\%}$-quantile of the output conditional on the input. More precisely, it seeks hypotheses $\mathbf{w}$ for which $\tau \times {100\%}$ of all training samples lie in the halfspace $\{{({\mathbf{x}},y)}:{{\langle{\mathbf{w}},{\mathbf{x}}\rangle} \geq y}\}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Examples of Classification Models", "weight": 1.0} -->

More precisely, support vector machines seek hypotheses $\mathbf{w}$ under which the inputs of all training samples with output $+ 1$ reside in the halfspace $\{{\mathbf{x}}:{{\langle{\mathbf{w}},{\mathbf{x}}\rangle} \geq 1}\}$, while the inputs of training samples with output $- 1$ are confined to $\{{\mathbf{x}}:{{\langle{\mathbf{w}},{\mathbf{x}}\rangle} \leq {- 1}}\}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Examples of Classification Models", "weight": 1.0} -->

An alternative support vector machine problem is obtained from if $\ell$ is generated by the smooth hinge loss function, which is defined as ${L{(z)}} = {\frac{1}{2} - z}$ if $z \leq 0$; $= {\frac{1}{2}{({1 - z})}^{2}}$ if $0 < z < 1$; $= 0$ otherwise. The smooth hinge loss inherits many properties of the ordinary hinge loss but has a continuous derivative. Thus, it may be amenable to faster optimization algorithms.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Examples of Classification Models", "weight": 1.0} -->

The logistic regression problem emerges as a special case of if $\ell$ is generated by the logloss function ${L{(z)}} = {\log{({1 + e^{- z}})}}$, which is large if $z$ is small---similar to the hinge loss function. In this case the objective function of can be viewed as the log-likelihood function corresponding to the logistic model ${{\mathbb{P}}{({y = \left. 1 \middle| {\mathbf{x}} \right.})}} = {\lbrack{1 + {\exp{({- {\langle{\mathbf{w}},{\mathbf{x}}\rangle}})}}}\rbrack}^{- 1}$ for the conditional probability of $y = 1$ given $\mathbf{x}$. Thus, logistic regression allows us to learn the conditional distribution of $y$ given $\mathbf{x}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2.1 (Convex approximation)", "weight": 1.0} -->

Note that the hinge loss and the logloss functions represent convex approximations for the (discontinuous) one-zero loss defined through ${L{(z)}} = 1$ if $z \leq 0$; $= 0$ otherwise.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2.1 (Convex approximation)", "weight": 1.0} -->

In practice there may be many hypotheses that are compatible with the given training data and thus achieve a small empirical loss. Any such hypothesis would accurately predict outputs from inputs within the training dataset. However, due to overfitting, these hypotheses might constitute poor predictors beyond the training dataset, that is, on inputs that have not yet been recorded in the database.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2.1 (Convex approximation)", "weight": 1.0} -->

Regularization is the standard remedy to combat overfitting. Instead of naïvely minimizing the in-sample error as is done, it may thus be advisable to solve the regularized learning problem which minimizes the sum of the emiprial average loss and a penalty for hpothesis complexity, which consists of a regularization function $\Omega{({\mathbf{w}})}$ and its associated regularization weight $c$. Tikhonov regularization, for example, corresponds to the choice ${\Omega{({\mathbf{w}})}} = {\|{\mathbf{\Gamma}{\mathbf{w}}}\|}_{2}^{2}$ for some Tikhonov matrix $\mathbf{\Gamma} \in {\mathbb{R}}^{n \times n}$. Setting $\mathbf{\Gamma}$ to the identity matrix gives rise to standard $L_{2}$-regularization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2.1 (Convex approximation)", "weight": 1.0} -->

Similarly, Lasso (least absolute shrinkage and selection operator) regularization or $L_{1}$-regularization is obtained by setting ${\Omega{({\mathbf{w}})}} = {\|{\mathbf{w}}\|}_{1}$. Lasso regularization has gained popularity because it favors parsimonious interpretable hypotheses.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2.1 (Convex approximation)", "weight": 1.0} -->

Most popular regualization methods admit probabilistic interpretations. However, these interpretations typically rely on prior distributional assumptions that remain to some extent arbitrary (e.g., $L_{2}$- and $L_{1}$-regularization can be justified if $\mathbf{w}$ is governed by a Gaussian or Laplacian prior distribution, respectively ). Thus, in spite of their many desirable theoretical properties, there is a consensus that "most of the (regularization) methods used successfully in practice are heuristic methods".

<!-- chunk {"id": "body-0043", "role": "body", "section": "New Perspective on Regularization", "weight": 1.0} -->

When linear hypotheses are used, problem minimizes the in-sample error ${\mathbb{E}}^{{\hat{\mathbb{P}}}_{N}}{\lbrack{\ell{({\langle{\mathbf{w}},{\mathbf{x}}\rangle},y)}}\rbrack}$. However, a hypothesis $\mathbf{w}$ enjoying a low in-sample error may still suffer from a high out-of-sample error ${\mathbb{E}}^{\mathbb{P}}{\lbrack{\ell{({\langle{\mathbf{w}},{\mathbf{x}}\rangle},y)}}\rbrack}$ due to overfitting. This is unfortunate as we seek hypotheses that offer high prediction accuracy on future data, meaning that the out-of-sample error is the actual quantity of interest. An ideal learning model would therefore minimize the out-of-sample error.

<!-- chunk {"id": "body-0044", "role": "body", "section": "New Perspective on Regularization", "weight": 1.0} -->

This is impossible, however, for the following reasons: The true input-output distribution $\mathbb{P}$ is unknown and only indirectly observable through the $N$ training samples. Thus, we lack essential information to compute the out-of-sample error.

<!-- chunk {"id": "body-0045", "role": "body", "section": "New Perspective on Regularization", "weight": 1.0} -->

Even if the distribution $\mathbb{P}$ was known, computing the out-of-sample error would typically be hard due to the intractability of high-dimensional integration; see, e.g., \[38, Corollary 1\].

<!-- chunk {"id": "body-0046", "role": "body", "section": "New Perspective on Regularization", "weight": 1.0} -->

The regularized loss ${{\mathbb{E}}^{{\hat{\mathbb{P}}}_{N}}{\lbrack{\ell{({\langle{\mathbf{w}},{\mathbf{x}}\rangle},y)}}\rbrack}} + {c\Omega{({\mathbf{w}})}}$ used, which consists of the in-sample error and an overfitting penalty, can be viewed as an in-sample estimate of the out-of-sample error. Yet, problem remains difficult to justify rigorously. Therefore, we advocate here a more principled approach to regularization. Specifically, we propose to take into account the expected loss of hypothesis $\mathbf{w}$ under every distribution $\mathbb{Q}$ that is close to the empirical distribution ${\hat{\mathbb{P}}}_{N}$, that is, every $\mathbb{Q}$ that could have generated the training data with high confidence. To this end, we first introduce a distance measure for distributions.

<!-- chunk {"id": "body-0047", "role": "body", "section": "New Perspective on Regularization", "weight": 1.0} -->

For ease of notation, we henceforth denote the input-output pair $({\mathbf{x}},y)$ by $\mathbf{ξ}$, and we set $\Xi = {{\mathbb{X}} \times {\mathbb{Y}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2.3 (Support information)", "weight": 1.0} -->

The uncertainty set $\Xi$ captures prior information on the range of the inputs and outputs. In image processing, for example, pixel intensities range over a known interval. Similarly, in diagnostic medicine, physiological parameters such as blood glucose or cholesterol concentrations are restricted to be non-negative. Sometimes it is also useful to construct $\Xi$ as a confidence set that covers the support of $\mathbb{P}$ with a prescribed probability. Such confidence sets are often constructed as ellipsoids, as intersections of different norm balls or as sublevel sets of kernel expansions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2.3 (Support information)", "weight": 1.0} -->

In the remainder we establish that the distributionally robust learning problem has several desirable properties. (i) Problem is computationally tractable under standard assumptions about the loss function $\ell$, the input-output space $\Xi$ and the transportation metric $d$. For specific choices of $d$ it even reduces to a regularized learning problem of the form. (ii) For all univariate loss functions reviewed in Section 2.1, a tight conservative approximation of is kernelizable, that is, it can be solved implicitly over high-dimensional spaces of nonlinear hypotheses at the same computational cost required for linear hypothesis spaces. (iii) Leveraging modern measure concentration results, the optimal value of can be shown to provide an upper confidence bound on the out-of-sample error. This obviates the need to mobilize the full machinery of VC theory and, in particular, to estimate the VC dimension of the hypothesis space in order to establish generalization bounds.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2.3 (Support information)", "weight": 1.0} -->

(iv) If the number of training samples tends to infinity while the Wasserstein ball shrinks at an appropriate rate, then problem asymptotically recovers the ex post optimal hypothesis that attains the minimal out-of-sample error.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Tractable Reformulations", "weight": 1.0} -->

In this section we demonstrate that the distributionally robust learning problem over linear hypotheses is amenable to efficient computational solution procedures. We also discuss generalizations to nonlinear hypothesis classes such as reproducing kernel Hilbert spaces and families of feed-forward neural networks.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Distributionally Robust Linear Regression", "weight": 1.0} -->

Throughout this section we focus on linear regression problems, where ${\ell{({\langle{\mathbf{w}},{\mathbf{x}}\rangle},y)}} = {L{({{\langle{\mathbf{w}},{\mathbf{x}}\rangle} - y})}}$ for some convex univariate loss function $L$. We also assume that $\mathbb{X}$ and $\mathbb{Y}$ are both convex and closed and that the transportation metric $d$ is induced by a norm $\parallel \cdot \parallel$ on the input-output space ${\mathbb{R}}^{n + 1}$. In this setting, the distributionally robust regression problem admits an equivalent reformulation as a finite convex optimization problem if either (i) the univariate loss function $L$ is piecewise affine or (ii) $\Xi = {\mathbb{R}}^{n + 1}$ and $L$ is Lipschitz continuous (but not necessarily piecewise affine).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 3.5 (Relation to classical regularization)", "weight": 1.0} -->

Assume now that the mass transportation costs are additively separable with respect to inputs and outputs, that is, for some $\kappa > 0$.^11^1By slight abuse of notation, the symbol $\parallel \cdot \parallel$ now denotes a norm on ${\mathbb{R}}^{n}$. Note that $\kappa$ captures the costs of moving probability mass along the output space. For $\kappa = \infty$ all distributions in the Wasserstein ball ${\mathbb{B}}_{\rho}{({\hat{\mathbb{P}}}_{N})}$ are thus obtained by reshaping ${\hat{\mathbb{P}}}_{N}$ only along the input space. It is easy to verify that for $\kappa = \infty$ and $\Xi = {\mathbb{R}}^{n + 1}$ the learning models portrayed in Corollaries 3.2. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")-3.4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 3.5 (Relation to classical regularization)", "weight": 1.0} -->

‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") all simplify to where $c = {\rho\delta}$ for robust regression with Huber loss, $c = \rho$ for support vector regression with $\epsilon$-insensitive loss and $c = {{\max{\{\tau,{1 - \tau}\}}}\rho}$ for quantile regression with pinball loss. Thus, (29. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) is easily identified as an instance of the classical regularized learning problem, where the dual norm term ${\|{\mathbf{w}}\|}_{\ast}$ plays the role of the regularization function, while $c$ represents the usual regularization weight.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 3.5 (Relation to classical regularization)", "weight": 1.0} -->

By definition of the dual norm, the penalty ${\|{\mathbf{w}}\|}_{\ast}$ assigned to a hypothesis $\mathbf{w}$ is maximal (minimal) if the cost of moving probability mass along $\mathbf{w}$ is minimal (maximal). We emphasize that if $\kappa = \infty$, then the marginal distribution of $y$ corresponding to every ${\mathbb{Q}} \in {{\mathbb{B}}_{\rho}{({\hat{\mathbb{P}}}_{N})}}$ coincides with the empirical distribution $\frac{1}{N}{\sum_{i = 1}^{N}\delta_{{\hat{y}}_{i}}}$. Thus, classical regularization methods, which correspond to $\kappa = \infty$, are explained by a counterintuitive probabilistic model, which pretends that any training sample must have an output that has already been recordeded in the training dataset.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 3.5 (Relation to classical regularization)", "weight": 1.0} -->

In other words, classical regularization implicitly assumes that there is no uncertainty in the outputs. More intuitively appealing regularization schemes are obtained for finite values of $\kappa$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 3.5 (Relation to classical regularization)", "weight": 1.0} -->

To establish a connection between distributionally robust and classical robust regression as discussed, we further investigate the worst-case expected loss of a fixed linear hypothesis $\mathbf{w}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3.8 (Minimal dispersion)", "weight": 1.0} -->

Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") is reminiscent of the non-separability condition in \[76, Theorem 3\], which is necessary to prove the equivalence of robust and regularized support vector machines. In the regression context studied here, Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") ensures that, for every $\mathbf{w}$, there exists a training sample that activates the largest absolute slope of $L$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 3.8 (Minimal dispersion)", "weight": 1.0} -->

For instance, in support vector regression, it means that for every $\mathbf{w}$ there exists a data point outside of the slab of width ${2\epsilon}/{\|{({\mathbf{w}},{- 1})}\|}_{2}$ centered around the hyperplane $H_{\mathbf{w}} = {\{{{({\mathbf{x}},y)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}}:{{{\langle{\mathbf{w}},{\mathbf{x}}\rangle} - y} = 0}\}}$ (i.e., the empirical $\epsilon$-insensitive loss is not zero). Similarly, in robust regression with the Huber loss function, Assumption 3.7.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 3.8 (Minimal dispersion)", "weight": 1.0} -->

‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") stipulates that for every $\mathbf{w}$ there exists a data point outside of the slab of width ${2\delta}/{\|{({\mathbf{w}},{- 1})}\|}_{2}$ centered around $H_{\mathbf{w}}$. However, quantile regression with $\tau \neq 0.5$ fails to satisfy Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"). Indeed, for any training dataset there always exists some $\mathbf{w}$ such that all data points reside on the side of $H_{\mathbf{w}}$ where the pinball loss function is less steep.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 3.10 (Tractability of robust regression)", "weight": 1.0} -->

Assume that $\Xi = {\mathbb{R}}^{n + 1}$, while $L$ and $\parallel \cdot \parallel$ both admit a tractable conic representation. By Theorem 3.1. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"), the worst-case expected loss can then be computed in polynomial time by solving a tractable convex program. Theorem 3.9. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") thus implies that the worst-case loss (86. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) can also be computed in polynomial time if Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") holds. To our best knowledge, there exists no generic efficient method for computing (86. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) if Assumption 3.7.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 3.10 (Tractability of robust regression)", "weight": 1.0} -->

‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") fails to hold and $L$ is not piecewise affine. This reinforces our belief that a distributionally robust approach to regression is more natural.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Distributionally Robust Linear Classification", "weight": 1.0} -->

Throughout this section we focus on linear classification problems, where ${\ell{({\langle{\mathbf{w}},{\mathbf{x}}\rangle},y)}} = {L{({y{\langle{\mathbf{w}},{\mathbf{x}}\rangle}})}}$ for some convex univariate loss function $L$. We also assume that $\mathbb{X}$ is both convex and closed and that ${\mathbb{Y}} = {\{{+ 1},{- 1}\}}$. Moreover, we assume that the transportation metric $d$ is defined via where $\parallel \cdot \parallel$ represents a norm on the input space ${\mathbb{R}}^{n}$, and $\kappa > 0$ quantifies the cost of switching a label.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Distributionally Robust Linear Classification", "weight": 1.0} -->

In this setting, the distributionally robust classification problem admits an equivalent reformulation as a finite convex optimization problem if either (i) the univariate loss function $L$ is piecewise affine or (ii) ${\mathbb{X}} = {\mathbb{R}}^{n}$ and $L$ is Lipschitz continuous (but not necessarily piecewise affine).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 3.15 (Relation to classical regularization)", "weight": 1.0} -->

If ${\mathbb{X}} = {\mathbb{R}}^{n}$ and the weight parameter $\kappa$ in the transportation metric is set to infinity, then the learning problems portrayed in Corollaries 3.12. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")--3.14. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") all simplify to Thus, in analogy to the case of regression, (70. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) reduces to an instance of the classical regularized learning problem, where the dual norm term ${\|{\mathbf{w}}\|}_{\ast}$ plays the role of the regularization function, while the Wasserstein radius $\rho$ represents the usual regularization weight.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 3.15 (Relation to classical regularization)", "weight": 1.0} -->

Note that if $\kappa = \infty$, then mass transportation along the output space is infinitely expensive, that is, any distribution ${\mathbb{Q}} \in {{\mathbb{B}}_{\rho}{({\hat{\mathbb{P}}}_{N})}}$ can smear out the training samples along $\mathbb{X}$, but it cannot flip outputs from $+ 1$ to $- 1$ or vice versa. Thus, classical regularization schemes, which are recovered for $\kappa = \infty$, implicitly assume that output measurements are exact. As this belief is not tenable in most applications, an approach with $\kappa < \infty$ may be more satisfying. We remark that alternative approaches for learning with noisy labels have previously been studied by Lawrence and Schölkopf, Natarajan et al., and Yang et al..

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 3.16 (Relation to Tikhonov regularization)", "weight": 1.0} -->

The learning problem with Tikhonov regularizer enjoys wide popularity. If $L$ represents the hinge loss, for example, then (71. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) reduces to the celebrated soft margin support vector machine problem. However, the Tikhonov regularizer appearing in (71. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) is not explained by a distributionally robust learning problem of the form. It is known, however, that (70. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) with $\parallel \cdot \parallel_{\ast} = \parallel \cdot \parallel_{2}$ and (71. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) are equivalent in the sense that for every $\rho \geq 0$ there exists $c \geq 0$ such that the solution of (70.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 3.16 (Relation to Tikhonov regularization)", "weight": 1.0} -->

‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) also solves (71. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) and vice versa \[76, Corollary 6\].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.16 (Relation to Tikhonov regularization)", "weight": 1.0} -->

To establish a connection between distributionally robust and classical robust classification as discussed, we further investigate the worst-case expected loss of a fixed linear hypothesis $\mathbf{w}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 3.19 (Non-separability)", "weight": 1.0} -->

Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") generalizes the non-separability condition in \[76, Theorem 3\] for the classical and smooth hinge loss functions to more general Lipschitz continuous losses. Note that, in the case of the hinge loss, Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") effectively stipulates that for any $\mathbf{w}$ there exists a training sample $({\hat{\mathbf{x}}}_{k},{\hat{y}}_{k})$ with ${{\hat{y}}_{k}{\langle{\mathbf{w}},{\hat{\mathbf{x}}}_{k}\rangle}} < 1$, implying that the dataset cannot be perfectly separated by any linear hypothesis $\mathbf{w}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 3.19 (Non-separability)", "weight": 1.0} -->

An equivalent requirement is that the empirical hinge loss is nonzero for every $\mathbf{w}$. Similarly, in the case of the smooth hinge loss, Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") ensures that for any $\mathbf{w}$ there is a training sample with ${{\hat{y}}_{k}{\langle{\mathbf{w}},{\hat{\mathbf{x}}}_{k}\rangle}} < 0$, which implies again that the dataset admits no perfect linear separation. Note, however, that the logloss fails to satisfy Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") as its steepest slope is attained at infinity.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 3.21 (Tractability of robust classification)", "weight": 1.0} -->

Assume that ${\mathbb{X}} = {\mathbb{R}}^{n}$, while $L$ and $\parallel \cdot \parallel$ both admit a tractable conic representation. By Theorem 3.11. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"), the worst-case expected loss can then be computed in polynomial time by solving a tractable convex program. Theorem 3.20. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") thus implies that the worst-case loss (86. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) can also be computed in polynomial time if Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") holds. This confirms Proposition 4. No efficient method for computing (86. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) is know if Assumption 3.18.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3.21 (Tractability of robust classification)", "weight": 1.0} -->

‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") fails to hold.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces", "weight": 1.0} -->

In summary, given a symmetric and positive definite kernel function $k$, there exists an associated RKHS $\mathbb{H}$ and a feature map $\Phi$ with the reproducing property. As we will see below, however, to optimize over nonlinear hypotheses in $\mathbb{H}$, knowledge of $k$ is sufficient, and there is no need to construct $\mathbb{H}$ and $\Phi$ explicitly.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces", "weight": 1.0} -->

Assume now that we are given any symmetric and positive definite kernel function $k$, and construct a distributionally robust learning problem over all nonlinear hypotheses in the corresponding RKHS $\mathbb{H}$ via where the transportation metric is given by the Euclidean norm on ${\mathbb{X}} \times {\mathbb{Y}}$ (for regression problems) or the separable metric with the Euclidean norm on $\mathbb{X}$ (for classification problems).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces", "weight": 1.0} -->

While problem is hard to solve in general due to the nonlinearity of the hypotheses $h \in {\mathbb{H}}$, it is easy to solve a lifted learning problem where the inputs ${\mathbf{x}} \in {\mathbb{X}}$ are replaced with features ${\mathbf{x}}_{\mathbb{H}} \in {\mathbb{H}}$, while each nonlinear hypothesis $h \in {\mathbb{H}}$ over the input space $\mathbb{X}$ is identified with a linear hypothesis $h_{\mathbb{H}} \in {\mathbb{H}}$ over the feature space $\mathbb{H}$ through the identity ${h_{\mathbb{H}}{({\mathbf{x}}_{\mathbb{H}})}} = {\langle h,{\mathbf{x}}_{\mathbb{H}}\rangle}_{\mathbb{H}}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces", "weight": 1.0} -->

Thus, we should not expect to be equivalent to. Instead, one can show that under a judicious transformation of the Wasserstein radius, provides an upper bound on whenever the kernel function satisfies a calmness condition.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Assumption 3.22 (Calmness of the kernel)", "weight": 1.0} -->

The kernel function $k$ is calm from above, that is, there exist a concave smooth growth function $g:{{\mathbb{R}}_{+}\rightarrow{\mathbb{R}}_{+}}$ with ${g{}} = 0$ and ${g'{(z)}} \geq 1$ for all $z \in {\mathbb{R}}_{+}$ such that The calmness condition is non-restrictive. In fact, it is satisfied by most commonly used kernels.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example 3.23 (Growth Functions for Popular Kernels)", "weight": 1.0} -->

For most commonly used kernels $k$ on ${\mathbb{X}} \subseteq {\mathbb{R}}^{n}$, we can construct an explicit growth function $g$ that certifies the calmness of $k$ in the sense of Assumption 3.22. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"). This construction typically relies on elementary estimates. Derivations are omitted for brevity.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 3.28 (Kernelization in robust regression and classification)", "weight": 1.0} -->

Recall from Theorem 3.9. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") that distributionally robust and classical robust linear regression are equivalent if $\Xi = {\mathbb{R}}^{n + 1}$ and the training samples are sufficiently dispersed in the sense of Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"). Similarly, Theorem 3.20. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") implies that distributionally robust and classical robust linear classification are equivalent if $\kappa = \infty$ and the training samples are non-separable in the sense of Assumption 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"). One can show that Theorems 3.9. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") and 3.20.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 3.28 (Kernelization in robust regression and classification)", "weight": 1.0} -->

‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") naturally extend to nonlinear regression and classification models over an RKHS induced by some symmetric and positive definite kernel. Specifically, one can show that some lifted robust learning problem is equivalent to the lifted distributionally robust learning problem whenever the lifted training samples ${({\Phi{({\hat{\mathbf{x}}}_{1})}},{\hat{y}}_{1})},\cdots,{({\Phi{({\hat{\mathbf{x}}}_{N})}},{\hat{y}}_{N})}$ satisfy Assumption 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") (for regression) or 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") (for classification). Theorems 3.26.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 3.28 (Kernelization in robust regression and classification)", "weight": 1.0} -->

‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") and 3.27. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") thus imply that the lifted robust regression and classification problems can be solved efficiently under mild regularity conditions whenever Assumptions 3.7. ‣ 3.1 Distributionally Robust Linear Regression ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") and 3.18. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") hold, respectively. Unfortunately, these conditions are often violated for popular kernels. For example, the lifted samples are always linearly separable under the Gaussian kernel \[76, p. 1496\]. In this case, the lifted robust classification problem can never be reduced to an efficiently solvable lifted distributionally robust classification problem of the form. In fact, no efficient method for solving the lifted robust classification problem seems to be known.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 3.28 (Kernelization in robust regression and classification)", "weight": 1.0} -->

In contrast, the lifted distributionally robust learning problems are always efficiently solvable under standard regularity conditions.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Nonlinear Hypotheses: Neural Networks^22^2We are grateful to an anonymous referee for encouraging us to write this section", "weight": 1.0} -->

Families of neural networks represent particularly expressive classes of nonlinear hypotheses. In the following, we characterize a family $\mathbb{H}$ of neural networks with $M \in {\mathbb{N}}$ layers through $M$ continuous activation functions $\sigma_{m}:{{\mathbb{R}}^{n_{m + 1}}\rightarrow{\mathbb{R}}^{n_{m + 1}}}$ and $M$ weight matrices ${\mathbf{W}}_{m} \in {\mathbb{R}}^{n_{m + 1} \times n_{m}}$, $m \in {\lbrack M\rbrack}$. The weight matrices can encode fully connected or convolutional layers, for example.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Nonlinear Hypotheses: Neural Networks^22^2We are grateful to an anonymous referee for encouraging us to write this section", "weight": 1.0} -->

If $n_{1} = n$ and $n_{M + 1} = 1$, then we may set Each hypothesis $h \in {\mathbb{H}}$ constitutes a neural network and is uniquely determined by the collection of all weight matrices ${\mathbf{W}}_{\lbrack M\rbrack}:={({\mathbf{W}}_{1},\ldots,{\mathbf{W}}_{M})}$. In order to emphasize the dependence on ${\mathbf{W}}_{\lbrack M\rbrack}$, we will sometimes use $h{({\mathbf{x}};{\mathbf{W}}_{\lbrack M\rbrack})}$ to denote the hypotheses in $\mathbb{H}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Example 3.29 (Activation functions)", "weight": 1.0} -->

The following activation functions are most widely used.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 3.31 (Uniform upper bound on all neural networks)", "weight": 1.0} -->

For classification problems the constant $c$ in (96. ‣ 3.4 Nonlinear Hypotheses: Neural Networks2footnote 22footnote 2We are grateful to an anonymous referee for encouraging us to write this section. ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) represents a uniform upper bound on all neural networks and may be difficult to evaluate in general. It is easy to estimate $c$, however, if the last activation function is itself bounded such as the softmax function, which yields a probability distribution over the output space. In this case one may simply set $c = 2$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Remark 3.31 (Uniform upper bound on all neural networks)", "weight": 1.0} -->

The product term $\prod_{m = 1}^{M}{\operatorname{lip}{{(\sigma_{m})}{\|{\mathbf{W}}_{m}\|}}}$ in (96. ‣ 3.4 Nonlinear Hypotheses: Neural Networks2footnote 22footnote 2We are grateful to an anonymous referee for encouraging us to write this section. ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) represents an upper bound on the Lipschitz modulus of $h{({\mathbf{x}};{\mathbf{W}}_{\lbrack M\rbrack})}$. We emphasize that computing the exact Lipschitz modulus of a neural network is NP-hard even if there are only two layers and all activation functions are of the ReLU type \[58, Theorem 2\]. In contrast, the upper bound at hand is easy to compute as all activation functions listed in Example 3.29.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Remark 3.31 (Uniform upper bound on all neural networks)", "weight": 1.0} -->

‣ 3.4 Nonlinear Hypotheses: Neural Networks2footnote 22footnote 2We are grateful to an anonymous referee for encouraging us to write this section. ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") have Lipschitz modulus 1 with respect to the Euclidean norms on the domain and range spaces. For more details on how to estimate the Lipschitz moduli of neural networks we refer to.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Remark 3.31 (Uniform upper bound on all neural networks)", "weight": 1.0} -->

Note that even though (96. ‣ 3.4 Nonlinear Hypotheses: Neural Networks2footnote 22footnote 2We are grateful to an anonymous referee for encouraging us to write this section. ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) represents a finite-dimensional optimization problem over the weight matrices of the neural network, both the empirical prediction loss as well as the regularization term are non-convex in ${\mathbf{W}}_{\lbrack M\rbrack}$, which complicates numerical solution. If $\kappa = \infty$, however, one can derive an alternative upper bound on the distributionally robust learning model with a convex regularization term.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Example 3.33 (Proximal operator)", "weight": 1.0} -->

Suppose that all feature spaces ${\mathbb{R}}^{n_{m}}$ are equipped with the $p$-norm for some $p \in {\{ 1,2,\infty\}}$, which implies that all parameter spaces ${\mathbb{R}}^{n_{m + 1} \times n_{m}}$ are equipped with the corresponding matrix $p$-norm. In this case the proximal operator of ${\varphi{({\mathbf{W}}_{m})}} = {\eta{\|{\mathbf{W}}_{m}\|}_{p}}$ for some fixed $\eta > 0$ can be evaluated highly efficiently.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Example 3.33 (Proximal operator)", "weight": 1.0} -->

For any fixed $u$, the above problem decomposes into $n_{m}$ projections of the vectors ${\lbrack{\mathbf{W}}_{m}\rbrack}_{:,i}$, $i \in {\lbrack n_{m}\rbrack}$, to the $\ell_{1}$-ball of radius $u$ centered at the origin. Each of these projections can be computed via an efficient sorting algorithm proposed. Next, we can use any line search method such as the golden-section search algorithm to optimize over $u$, thereby solving the full proximal problem.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Example 3.33 (Proximal operator)", "weight": 1.0} -->

Spectral ($p = 2$): The matrix $2$-norm coincides with the spectral norm, which returns the maximum singular value.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Example 3.33 (Proximal operator)", "weight": 1.0} -->

n_{m}}$ orthogonal, the proximal operator satisfies The singular value decomposition can be accelerated using a randomized algorithm proposed.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Example 3.33 (Proximal operator)", "weight": 1.0} -->

The convergence behavior of the stochastic proximal gradient descent algorithm can be further improved by including a momentum term inside the proximal operator, see, e.g.,.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

Generalization bounds constitute upper confidence bounds on the out-of-sample error. Traditionally, generalization bounds are derived by controlling the complexity of the hypothesis space, which is typically quantified in terms of its VC-dimension or via covering numbers or Rademacher averages. Strengthened generalization bounds for large margin classifiers can be obtained by improving the estimates of the VC-dimension and the Rademacher average. We will now demonstrate that distributionally robust learning models of the type or enjoy simple new generalization bounds that can be obtained under minimal assumptions. In particular, they do not rely on any notions of hypothesis complexity and may therefore even extend to hypothesis spaces with infinite VC-dimensions. Our approach is reminiscent of the generalization theory for robust support vector machines portrayed, which also replaces measures of hypothesis complexity with robustness properties. However, we derive explicit finite sample guarantees, while establishes asymptotic consistency results. Moreover, we relax some technical conditions used in such as the compactness of the input space $\mathbb{X}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

The key enabling mechanism of our analysis is a measure concentration property of the Wasserstein metric, which holds whenever the unknown data-generating distribution has exponentially decaying tails.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

The following comments are in order.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Performance guarantees for optimal hypotheses: If $\hat{J}{(\rho)}$ denotes the minimum and $\hat{\mathbf{w}}$ a minimizer of the distributionally robust learning problem, then Theorem 4.3. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") implies that for any $N \geq 1$, $n > 1$, $\eta \in {(0,1\rbrack}$ and $\rho \geq {\rho_{N}{(\eta)}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Light-tail assumption: Assumption 4.1. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") is restrictive but unavoidable for any measure concentration result of the type described in Theorem 4.2. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation"). It is automatically satisfied if the input-output pair has bounded support or is known to follow a Gaussian or exponential distribution, for instance.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Asymptotic consistency: It is clear from that for any fixed $\eta \in {(0,1\rbrack}$, the radius $\rho_{N}{(\eta)}$ tends to 0 as $N$ increases. Moreover, Theorem 3.6 in implies that if $\eta_{N}$ converges to 0 at a carefully chosen rate (e.g., $\eta_{N} = {\exp{({- \sqrt{N}})}}$), then the solution of the distributionally robust learning problem with Wasserstein radius $\rho = {\rho_{N}{(\eta_{N})}}$ converges almost surely to the solution of the ideal learning problem that minimizes the out-of-sample error under the unknown true distribution $\mathbb{P}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Curse of dimensionality: The Wasserstein radius has two decay regimes. For small $N$, $\rho_{N}{(\eta)}$ decays as $N^{- \frac{1}{a}}$, and for large $N$ it is proportional to $N^{- \frac{1}{n + 1}}$. We thus face a curse of dimensionality for large sample sizes. In order to half the Wasserstein radius, one has to increase $N$ by a factor of $2^{n}$. This curse of dimensionality is fundamental, i.e., the dependence of the measure concentration result in Theorem 4.2. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") on the input dimension $n$ cannot be improved for generic distributions $\mathbb{P}$; see or \[32, Section 1.3\]. Improvements are only possible in special cases, e.g., if $\mathbb{P}$ is finitely supported.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Extension to nonlinear hypotheses: Theorem 4.3. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") directly extends to any distributionally robust learning problem over an RKHS $\mathbb{H}$ induced by some symmetric and positive definite kernel function $k$. Specifically, if $k$ is calm in the sense of Assumption 3.22. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") with growth function $g$, then we have for any $N \geq 1$, $n \neq 1$, $\eta \in {(0,1\rbrack}$ and $\rho \geq {cg{({\rho_{N}{(\eta)}})}}$, where $c = \sqrt{2}$ for regression problems and $c = 1$ for classification problems.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

To see this, note that the inclusion ${\mathbb{P}} \in {{\mathbb{B}}_{\rho}{({\hat{\mathbb{P}}}_{N})}}$ implies where the second inequality follows from the proof of Theorem 3.24. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"). The generalization bound (103. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) thus holds because ${{\mathbb{P}}^{N}{\{{{\mathbb{P}} \in {{\mathbb{B}}_{\rho}{({\hat{\mathbb{P}}}_{N})}}}\}}} \geq {1 - \eta}$ for any $\rho \geq {\rho_{N}{(\eta)}}$. Note that the rightmost term in (104.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) can be computed for any finitely generated hypothesis $h \in {\mathbb{H}}$ representable as ${h{({\mathbf{x}})}} = {\sum_{i = 1}^{N}{\beta_{i}k{({\mathbf{x}},{\hat{\mathbf{x}}}_{i})}}}$, which follows from Theorems 3.26. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") and 3.27. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"), while the middle term is hard to compute. We emphasize that the generalization bound (103.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) does not rely on any notion of hypothesis complexity and remains valid even if $\mathbb{H}$ has infinite VC-dimension (e.g., if $\mathbb{H}$ is generated by the Gaussian kernel).

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

Theorem 4.2. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") provides a confidence set for the unknown probability distribution $\mathbb{P}$, and Theorem 4.3. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") uses this confidence set to construct a uniform generalization bound on the prediction error under $\mathbb{P}$. The radius of the confidence set for $\mathbb{P}$ decreases slowly due to a curse of dimensionality, but the decay rate is essentially optimal. This does not imply that the decay rate of the generalization bound (102. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) is optimal, too. In fact, the worst-case expected error over a Wasserstein ball of radius $\rho$ can be a $({1 - \eta})$-confidence bound on the expected error under $\mathbb{P}$ even if the Wasserstein ball fails to contain $\mathbb{P}$ with confidence $1 - \eta$. Thus, the measure concentration result of Theorem 4.2.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 4.4 (Discussion of basic generalization bound)", "weight": 1.0} -->

‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") is too powerful for our purposes and leads to an over-conservative generalization bound. Below we will show that the curse of dimensionality in the generalization bound (102. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) can be broken if we impose the following restriction on the hypothesis space.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 4.7 (Discussion of improved generalization bound)", "weight": 1.0} -->

The following comments are in order.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 4.7 (Discussion of improved generalization bound)", "weight": 1.0} -->

Bounds on hypothesis space: Assumption 4.5. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") imposes upper and lower bounds on $\mathbb{W}$. The upper bound enables us to control the difference between the empirical and the true expected loss uniformly across all admissible hypotheses. This bound is less restrictive than the uniform bound on the loss function used to derive Rademacher generalization bounds (see, e.g., \[62, Theorem 26.4\]), which essentially imposes upper bounds both on the hypotheses and the input-output pairs. The lower bound in Assumption 4.5. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") is restrictive for classification problems but trivially holds for regression problems because ${\|{({\mathbf{w}},{- 1})}\|}_{\ast}$ is uniformly bounded away from zero for any (dual) norm on ${\mathbb{R}}^{n + 1}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Remark 4.7 (Discussion of improved generalization bound)", "weight": 1.0} -->

Breaking the curse of dimensionality: By leveraging Assumption 4.5. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation"), Theorem 4.6. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") reduces the critical Wasserstein radius in the generalization bound (102. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) from ${\rho_{N}{(\eta)}} \propto {\mathcal{O}{({\lbrack{{\log{(\eta^{- 1})}}/N}\rbrack}^{1/{({n + 1})}})}}$, which suffers from a curse of dimensionality, to $\rho_{N}'{(\eta)} \propto \mathcal{O}{({\lbrack\log{(\eta^{- 1})} + n\log{(N)})}/N\rbrack}^{1/2})$, which essentially follows a square root law reminiscent of the central limit theorem.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Error and Risk Estimation", "weight": 1.0} -->

Once a hypothesis $h{({\mathbf{x}})}$ has been chosen, it is instructive to derive pessimistic and optimistic estimates of its out-of-sample prediction error (in the case of regression) or its out-of-sample risk (in the case of classification). We will argue below that the distributionally robust optimization techniques developed in this paper also offer new perspectives on error and risk estimation. For ease of exposition, we ignore any support constraints, that is, we set ${\mathbb{X}} = {\mathbb{R}}^{n}$ and ${\mathbb{Y}} = {\mathbb{R}}$ (for regression) or ${\mathbb{X}} = {\mathbb{R}}^{n}$ and ${\mathbb{Y}} = {\{{+ 1},{- 1}\}}$ (for classification).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Error and Risk Estimation", "weight": 1.0} -->

Moreover, we focus on linear hypotheses of the form ${h{({\mathbf{x}})}} = {\langle{\mathbf{w}},{\mathbf{x}}\rangle}$. Note, however, that all results extend directly to conic representable support sets and to nonlinear hypotheses.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Error and Risk Estimation", "weight": 1.0} -->

In the context of regression, we aim to estimate the prediction error ${\mathcal{E}{({\mathbf{w}})}} = {{\mathbb{E}}^{\mathbb{P}}\left\lbrack {|{y - {\langle{\mathbf{w}},{\mathbf{x}}\rangle}}|} \right\rbrack}$ or, more precisely, the mean absolute prediction error under the unknown data-generating distribution $\mathbb{P}$. As usual, we assume that the transportation metric $d$ is induced by a norm $\parallel \cdot \parallel$ on the input-output space ${\mathbb{R}}^{n + 1}$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 5.3 (Confidence intervals for error and risk)", "weight": 1.0} -->

If the Wasserstein radius is set to $\rho_{N}{({\eta/2})}$ defined, where $\eta \in {(0,1\rbrack}$ is a prescribed significance level, then Theorem 4.3.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 5.3 (Confidence intervals for error and risk)", "weight": 1.0} -->

‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation") implies that the confidence interval for the true error $\mathcal{E}{(\hat{\mathbf{w}})}$ can be calculated analytically from (105. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation")), while Theorem 5.2. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation") implies that the confidence interval for the true risk $\mathcal{R}{(\hat{\mathbf{w}})}$ can be computed efficiently by solving the tractable linear programs (106. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation")).

<!-- chunk {"id": "body-0117", "role": "body", "section": "Remark 5.4 (Extension to nonlinear hypotheses)", "weight": 1.0} -->

By using the tools of Section 3.3, Theorems 5.1. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation") and 5.2. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation") generalize immediately to nonlinear hypotheses that range over a RKHS.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Remark 5.4 (Extension to nonlinear hypotheses)", "weight": 1.0} -->

Specifically, we can formulate lifted error and risk estimation problems where the inputs ${\mathbf{x}} \in {\mathbb{X}}$ are replaced with features ${\mathbf{x}}_{\mathbb{H}} \in {\mathbb{H}}$, while each nonlinear hypothesis $h \in {\mathbb{H}}$ over the input space $\mathbb{X}$ is identified with a linear hypothesis $h_{\mathbb{H}} \in {\mathbb{H}}$ over the feature space $\mathbb{H}$ through the identity ${h_{\mathbb{H}}{({\mathbf{x}}_{\mathbb{H}})}} = {\langle h,{\mathbf{x}}_{\mathbb{H}}\rangle}_{\mathbb{H}}$. Tractability is again facilitated by Theorem 3.25.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Remark 5.4 (Extension to nonlinear hypotheses)", "weight": 1.0} -->

‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation"), which allows us to focus on finitely parameterized hypotheses of the form ${h{({\mathbf{x}})}} = {\sum_{i = 1}^{N}{\beta_{i}k{({\mathbf{x}},{\hat{\mathbf{x}}}_{i})}}}$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We showcase the power of regularization via mass transportation in various applications based on standard datasets from the literature. All optimization problems are implemented in Python and solved with Gurobi 7.5.1 All experiments are run on an Intel XEON CPU (3.40GHz), and the corresponding codes are made publicly available at

<!-- chunk {"id": "body-0121", "role": "body", "section": "Regularization with Pre-selected Parameters", "weight": 1.0} -->

We first assess how the out-of-sample performance of a distributionally robust support vector machine (DRSVM) is impacted by the choice of the Wasserstein radius $\rho$, the cost $\kappa$ of flipping a label, and the kernel function $k$. To this end, we solve three binary classification problems from the MNIST database targeted at distinguishing pairs of similar handwritten digits (1-vs-7, 3-vs-8, 4-vs-9). In the first experiment we optimize over linear hypotheses and use the separable transporation metric involving the $\infty$-norm on the input space. All results are averaged over 100 independent trials. In each trial, we randomly select 500 images to train the DRSVM model (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) and use the remaining $12,000$ images for testing.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Regularization with Pre-selected Parameters", "weight": 1.0} -->

The correct classification rate (CCR) on the test data, averaged across all 100 trials, is visualized in Figure 1 as a function of the Wasserstein radius $\rho$ for each $\kappa \in {\{ 0.1,0.25,0.5,0.75,\infty\}}$. The best out-of-sample CCR is obtained for $\kappa = 0.25$ uniformly across all Wasserstein radii, and performance deteriorates significantly when $\kappa$ is reduced or increased. Recall from Remark 3.15. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation") that, as $\kappa$ tends to infinity, the DRSVM reduces to the classical regularized support vector machine (RSVM) with $1$-norm regularizer. Thus, the results of Figure 1 indicate that regularization via mass transportation may be preferable to classical regularization in terms of the maximum achievable out-of-sample CCR.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Regularization with Pre-selected Parameters", "weight": 1.0} -->

More specifically, we observe that the out-of-sample CCR of the best DRSVM ($\kappa = 0.25$) displays a slightly higher and significantly wider plateau around the optimal regularization parameter $\rho$ than the classical RSVM ($\kappa = \infty$). This suggests that the regularization parameter in DRSVMs may be easier to calibrate from data than in RSVMs, a conjecture that will be put to scrutiny in Section 6.2. Finally, Figure 1 reveals that the standard (unregularized) support vector machine (SVM), which can be viewed as a special case of the DRSVM with $\rho = 0$, is dominated by the RSVMs and DRSVMs across a wide range of regularization parameters.^55^5By slight abuse of notation, we use the acronym 'SVM' to refer to the unregularized empirical hinge loss minimization problem even though the traditional formulations of the support vector machine involve a Tikhonov regularization term. Note that the SVM problem (57.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Regularization with Pre-selected Parameters", "weight": 1.0} -->

‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) with $\rho = 0$ reduces to a linear program and may thus suffer from multiple optimal solutions. This explains why the limiting out-of-sample CCR for $\rho \downarrow 0$ changes with $\kappa$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

It is easy to read off the best regularization parameters $\rho$ and $\kappa$ from the charts in Figure 1. As these charts are constructed from more than 12,000 test samples, however, they are not accessible in the training phase. In practice, $\rho$ and $\kappa$ must be calibrated from the training data alone. This motivates us to revisit the three classification problems from Section 6.1 using a fully data-driven procedure, where all free model parameters are calibrated via $5$-fold cross validation; see, e.g., \[1, § 4.3.3\]. Moreover, to evaluate the benefits of kernelization, we now solve a generalized DRSVM model of the form (94. ‣ 3.3 Nonlinear Hypotheses: Reproducing Kernel Hilbert Spaces ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")), which implicitly optimizes over all nonlinear hypotheses in some RKHS. As explained in Section 3.3, kernelization necessitates the use of the separable transportation metric with the Euclidean norm on the input space.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

All free parameters of the resulting DRSVM model are restricted to finite search grids in order to ease the computational burden of cross validation. Specifically, we select the Wasserstein radius $\rho$ from within $\{{b \cdot 10^{e}}:{{b \in {\{ 1,5\}}},{e \in {\{ 1,2,3,4\}}}}\}$ and the label flipping cost $\kappa$ from within $\{ 0.1,0.25,0.5,0.75,\infty\}$. Moreover, we select the degree $d$ of the polynomial kernel from within $\{ 1,2,3,4,5\}$ and the peakedness parameter $\gamma$ of the Laplacian and Gaussian kernels from within $\{\frac{1}{100},\frac{1}{81},\frac{1}{64},\frac{1}{49},\frac{1}{36},\frac{1}{25}\}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

Otherwise, we use the same experimental setup as in Section 6.1. Table 1 reports the averages and standard deviations of the CCR scores on the test data based on 100 independent trials. We observe that the DRSVM ($\rho$, $\kappa$, $d$, and $\gamma$ learned by cross validation) outperforms the RSVM ($\rho$, $d$ and $\gamma$ learned by cross validation, $\kappa = \infty$) consistently across all tested kernel functions (Polynomial, Laplacian, Gaussian). Note that the DRSVM with polynomial kernel subsumes the non-kernelized DRSVM (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) as a special case because the polynomial kernel with $d = 1$ coincides with the linear kernel.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

In the third experiment, we assess the out-of-sample performance of the DRSVM (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) for different transportation metrics on 10 standard datasets from the UCI repository, each containing up to $1,000$ samples. Specifically, we use different variants of the separable transportation metric, where distances in the input space are measured via a $p$-norm with $p \in {\{ 1,2,\infty\}}$. We focus exclusively on linear hypotheses because the kernelization techniques described in Section 3.3 are only available for $p = 2$. The DRSVM is compared against the standard (unregularized) SVM and the RSVM with $q$-norm regularizer (${\frac{1}{p} + \frac{1}{q}} = 1$). All results are averaged across 100 independent trials. In each trial, we randomly select 75% of the data for training and the remaining 25% for testing.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

The inputs are first standardized to zero mean and unit variance along each coordinate axis. The Wasserstein radius $\rho$ and the label flipping cost $\kappa$ in the DRSVM as well as the regularization weight $\rho$ in the RSVM are estimated via stratified 5-fold cross validation.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Regularization with Learned Parameters", "weight": 1.0} -->

Classifier performance is now quantified in terms of the receiver operating characteristic (ROC) curve, which plots the true positive rate (percentage of correctly classified test samples with true label $y = 1$) against the false positive rate (percentage of incorrectly classified test samples with true label $y = {- 1}$) by sweeping the discrimination threshold. Specifically, we use the area under the ROC curve (AUC) as a measure of classifier performance. AUC does not bias on the size of the test data and is a more appropriate performance measure than CCR in the presence of an unbalanced label distribution in the training data. We emphasize that most of the considered datasets are indeed imbalanced, and thus a high CCR score would not necessarily provide evidence of superior classifier performance. The averages and standard deviations of the AUC scores based on 100 trials are reported in Table 2. The results suggest that the DRSVM outperforms the RSVM in terms of AUC for all norms by about the same amount by which the RSVM outperforms the classical hinge loss minimization, consistently across all datasets.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

The aim of object recognition is to discover instances of particular object classes in digital images. We now describe an object recognition experiment based on the PASCAL VOC 2007 dataset consisting of $9,963$ images, which are pre-partitioned into $25\%$ for training, $25\%$ for validation and $50\%$ for testing. Each image is annotated with 20 binary labels corresponding to 20 given object categories (the $n$-th label is set to $+ 1$ if the image contains the $n$-th object and to $- 1$ otherwise). A multi-label classifier is a function that predicts all labels of an unlabelled input image. The ability of a classifier to detect objects belonging to any fixed category is measured by the average precision (AP), which is defined in as (a proxy for) the area under the classifier's precision-recall curve. The overall performance of a classifier is quantified by the mean average precision (mAP), that is, the arithmetic mean of the AP scores across all object categories.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

In the first scenario, we train a separate binary RSVM and DRSVM classifier for each of the 20 object categories. This classifier predicts whether an object of the respective category appears in the input image. At the beginning we preprocess the entire dataset by resizing each image to $256 \times 256$ pixels and extracting the central patch of $244 \times 244$ pixels. As shown, the features generated by the penultimate layer of a deep convolutional neural network trained on a large image dataset provide a powerful image descriptor. Using the ALEXNET neural network trained on the ImageNet dataset, we can thus compress each (preprocessed) image of the PASCAL VOC 2007 dataset into 1,000 meaningful features. We normalize these feature vectors to lie on the unit sphere. When training the RSVM and DRSVM classifiers, we can thus work with these feature vectors instead of the corresponding images. Moreover, we restrict attention to linear hypotheses and assume that transportation distances in the input-output space are measured by the separable metric with the Euclidean norm on the input space.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

We tune the Wasserstein radius $\rho \in {\{{b \cdot 10^{e}}:{{b \in {\{ 1,\ldots,9\}}},{e \in {\{{- 2},{- 3},{- 4}\}}}}\}}$ and the label flipping cost $\kappa \in {\{ 0.1,0.2,\ldots,1,\infty\}}$ via the holdout method using the validation data. As usual, we fix $\kappa = \infty$ for RSVM. Table 3 reports the AP scores of the RSVM and DRSVM models for each object category. The ensemble of all 20 binary RSVM or DRSVM classifiers, respectively, can be viewed as a naïve multi-label classifier that predicts all labels of an image. As DRSVM outperforms RSVM on an object-by-object basis, it also wins in terms of mAP.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

In the second scenario, we construct a proper multi-label classifier by fine-tuning the last layer of the pre-trained ALEXNET network. To this end, we replace the original $M$-th layer of the network with a new fully connected layer characterized by a parameter matrix ${\mathbf{W}}_{M} \in {\mathbb{R}}^{20 \times 1000}$, and we set $\sigma_{M}$ to the Sigmoid activation function. The resulting classifer outputs for each of the 20 object categories a probability that an object from the respective category appears in the input image. The quality of a classifier (which is encoded by ${\mathbf{W}}_{M}$) is measured by the cross-entropy loss function, which naturally generalizes the logloss to multiple labels.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

By using similar arguments as in Section 3.4, one can show that the empirical cross-entropy with MACS, Spectral or MARS regularization term overestimates the worst-case expected cross-entropy over all distributions of $({\mathbf{x}}_{M},{\mathbf{x}}_{M + 1})$ in a Wasserstein ball provided that the transportation cost is given by for $\kappa = \infty$, whenever $p = 1$, $p = 2$ or $p = \infty$, respectively. Thus, the MACS, Spectral and MARS regularization terms admit a distributionally robust interpretation.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

We use the stochastic proximal gradient descent algorithm of Section 3.4 to tune ${\mathbf{W}}_{M}$, including an additional momentum term with weight $0.9$. As, we split the training phase into 100 epochs, each corresponding to a complete pass through the training dataset in a random order. As the ALEXNET requires input images of size $244 \times 244$, in each iteration we extract a random patch of $244 \times 244$ pixels from the current image and flip it horizontally at random. This procedure effectively augments the training dataset. The initial step size is set to $10^{- 3}$ and then reduced by a factor of $10$ after every $7$ epochs. The algorithm terminates after $100$ epochs. We preprocess the images in the validation and test datasets as in Scenario 1 and tune the regularization weights via the holdout method using the validation data. Table 3 reports the AP and mAP scores of the different classifiers that were tested. These results suggest that fine-tuning the last layer of a pre-trained neural network may improve classifier performance.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Multi-Label Classification", "weight": 1.0} -->

We observe that the spectral norm regularizer, which has a distributionally robust interpretation, consistently outperforms almost all other methods. For further details on the experimental setup (such as the exact search grids for all hyperparameters) we refer to the code publicized on Github.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

The next experiment estimates the scaling behavior of the smallest Wasserstein radius that verifies the generalization bound (102. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) for the synthetic threenorm classification problem. The experiment involves 1,000 simulation trials. In each trial we generate $N$ training samples for some $N \in {{\{ 10,\ldots,90\}} \cup {\{ 100,\ldots,1,000\}}}$ as well as $10^{5}$ test samples. Each sample ${({\mathbf{x}},y)} \in {{\mathbb{R}}^{20} \times {\{{- 1},1\}}}$ is constructed as follows. The label $y$ is drawn uniformly from $\{{- 1},1\}$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

If $y = {- 1}$, then $\mathbf{x}$ is drawn from a standard multivariate normal distribution shifted by $(c,\ldots,c)$ or $({- c},\ldots,{- c})$ with equal probabilities, where $c = {2/\sqrt{20}}$. If $\hat{y} = 1$, on the other hand, then $\mathbf{x}$ is drawn from a standard multivariate normal distribution shifted by $(c,{- c},{+ c},\ldots,{- c})$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

We now describe three different approaches to choose the Wasserstein radius $\rho$ in the DRSVM (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) with transportation cost, where $\kappa = \infty$ and $\parallel \cdot \parallel$ represents the $\infty$-norm on the input space. Throughout the experiment we use $P = {\{{b \cdot 10^{- e}}:{{b \in {\{ 1,\ldots,10\}}},{e \in {\{ 1,\ldots,5\}}}}\}}$ as the search space for $\rho$. Approach 1 ('cross validation') calibrates the Wasserstein radius as before via 5-fold cross validation based solely on the $N$ training samples. This approach reflects what would typically be done in practice. Approaches 2 and 3 both solve (57.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) based on the empirical distribution induced by the $N$ training samples and select the Wasserstein radius using the $10^{5}$ test samples. Specifically, approach 2 ('optimal') chooses the Wasserstain radius that leads to the lowest test error, while approach 3 ('generalization bound') selects the smallest Wasserstein radius for which the optimal value of (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) exceeds the expected loss on the test samples in at least $95\%$ of all trials, that is, it approximates the smallest Wasserstein radius that verifies the generalization bound (102. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation")) for $\eta = {5\%}$. As the test samples are not available in the training phase, the last two approaches are not implementable in practice, and we merely study them to gain insights.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

Figure 2(a) visualizes all resulting Wasserstein radii as a function of $N$. Note that the radii obtained with the first two approaches are uncertain as they depend on a particular choice of the training samples. Figure 2(a) thus only shows their averages across all simulation trials. In contrast, the radii obtained with the third approach depend on the training sample sets of all $1,000$ trials and are thus essentially deterministic.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

We observe that the Wasserstein radii of all three approaches decay approximately as $1/\sqrt{N}$, which is in line with the theoretical generalization bound of Theorem 4.6. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation"). We expect this decay rate to be optimal because any faster decay would be in conflict with the central limit theorem. Note also that our results empirically confirm Theorem 4.6. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") even though we did not impose any restrictions on $\mathbb{W}$ as dictated by Assumption 4.5. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation"). This suggests that Theorem 4.6. ‣ 4 Generalization Bounds ‣ Regularization via Mass Transportation") might remain valid under weaker conditions.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

In the experiment underlying Figure 2(b), we first fix $\hat{\mathbf{w}}$ to an optimal solution of (57. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")) for $\rho = 0.1$ and $N = 100$. Figure 2(b) shows the true risk $\mathcal{R}{(\hat{\mathbf{w}})}$ and its confidence bounds given by Theorem 5.2. ‣ 5 Error and Risk Estimation ‣ Regularization via Mass Transportation"). As expected, for $\rho = 0$ the upper and lower bounds coincide with the empirical risk on the training data, which is a lower bound for the true risk on the test data due to over-fitting effects. As $\rho$ increases, the confidence interval between the bounds widens and eventually covers the true risk.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

For instance, at $\rho \approx 0.009$ the confidence interval is given by $\lbrack 0.008,0.162\rbrack$ and contains the true risk with probability ${1 - \eta} = {95\%}$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

(a) Dependence of the Wasserstein radius on the number of training samples (b) Confidence bounds on the risk Figure 2: Results of the threenorm classification problem.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Worst-Case Distributions", "weight": 1.0} -->

Consider again the 3-vs-8 classification problems from the MNIST database and fix ${\mathbf{w}}^{\star}$ to an optimal solution of the empirical hinge loss minimization problem. The goal of the last experiment is to evaluate the worst-case hinge loss of ${\mathbf{w}}^{\star}$ for different Wasserstein radii $\rho \in {\{ 0,0.01,0.05,0.1,0.5,1\}}$ and label flipping costs $\kappa \in {\{ 0,\infty\}}$ and to investigate the corresponding worst-case distributions, which are efficiently computable by virtue of Theorem 3.17. ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")(i).

<!-- chunk {"id": "body-0148", "role": "body", "section": "Worst-Case Distributions", "weight": 1.0} -->

For illustrative purposes we only use the $N = 10$ first datapoints in the MNIST dataset as training samples. Each training sample ${\hat{\mathbf{x}}}_{i}$ corresponds to four discretization points (${\hat{\mathbf{x}}}_{i} + {{\mathbf{q}}_{ij}^{+ \star}/\alpha_{ij}^{+ \star}}$ and ${\hat{\mathbf{x}}}_{i} + {{\mathbf{q}}_{ij}^{- \star}/\alpha_{ij}^{- \star}}$ for $j = {1,2}$) in the worst-case distribution obtained from (78 ‣ Theorem 3.17 (Extremal distributions in linear classification). ‣ 3.2 Distributionally Robust Linear Classification ‣ 3 Tractable Reformulations ‣ Regularization via Mass Transportation")).

<!-- chunk {"id": "body-0149", "role": "body", "section": "Worst-Case Distributions", "weight": 1.0} -->

We observe that for every $i$ exactly one out of these four points has probability $\frac{1}{N}$, while all others have probability 0. Figure 3 depicts only those 10 discretization points that have nonzero probability for a fixed $\rho$ and $\kappa$. As expected, the perturbations of the training samples are more severe for larger Wasserstein radii. For $\kappa = \infty$ these scenarios must have the same labels as the corresponding training samples. For $\kappa = 0$, on the other hand, the labels can be flipped at no cost (flipped labels are indicated by red frames). Each scenario group shown in Figure 3 can thus be viewed as a worst-case training dataset for the corresponding Wasserstein radius and label flipping cost.
