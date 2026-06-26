<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Regularization Can Mitigate Double Descent

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent empirical and theoretical studies have shown that many learning algorithms - from linear regression to neural networks - can have test performance that is non-monotonic in quantities such the sample size and model size. This striking phenomenon, often referred to as "double descent", has raised questions of if we need to re-think our current understanding of generalization. In this work, we study whether the double-descent phenomenon can be avoided by using optimal regularization. Theoretically, we prove that for certain linear regression models with isotropic data distribution, optimally-tuned l_2 regularization achieves monotonic test performance as we grow either the sample size or the model size. We also demonstrate empirically that optimally-tuned l_2 regularization can mitigate double descent for more general models, including neural networks. Our results suggest that it may also be informative to study the test risk scalings of various algorithms in the context of appropriately tuned regularization.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works have demonstrated a ubiquitous "double descent" phenomenon present in a range of machine learning models, including decision trees, random features, linear regression, and deep neural networks Opper; Advani & Saxe; Spigler et al.; Belkin et al.; Geiger et al.; Nakkiran et al.; Belkin et al.; Hastie et al.; Bartlett et al.; Muthukumar et al.; Bibas et al.; Mitra; Mei & Montanari; Liang & Rakhlin; Liang et al.; Xu & Hsu; Dereziński et al.; Lampinen & Ganguli; Deng et al.; Nakkiran. The phenomenon is that models exhibit a peak of high test risk when they are just barely able to fit the train set, that is, to *interpolate*. For example, as we increase the size of models, test risk first decreases, then increases to a peak around when effective model size is close to the training data size, and then decreases again in the overparameterized regime.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Also surprising is that Nakkiran et al. observe a double descent as we increase sample size, i.e. for a fixed model, training the model with more data can hurt test performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These striking observations highlight a potential gap in our understanding of generalization and an opportunity for improved methods. Ideally, we seek to use learning algorithms which robustly improve performance as the data or model size grow and do not exhibit such unexpected non-monotonic behaviors. In other words, we aim to improve the test performance in situations which would otherwise exhibit high test risk due to double descent. Here, a natural strategy would be to use a regularizer and tune its strength on a validation set.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This motivates the central question of this work: When does optimally tuned regularization mitigate or remove the double-descent phenomenon?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another motivation to start this line of inquiry is the observation that the double descent phenomenon is largely observed for *unregularized* or *under-regularized* models in practice. As an example, Figure 1 shows a simple linear ridge regression setting in which the unregularized estimator exhibits double descent, but an optimally-tuned regularizer has monotonic test performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We study this question from both a theoretical and empirical perspective. Theoretically, we start with the setting of high-dimensional linear regression. Linear regression is a sensible starting point to study these questions, since it already exhibits many of the qualitative features of double descent in more complex models (e.g. Belkin et al.; Hastie et al. and further related works in Section 1.1).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

This work shows that optimally-tuned ridge regression can achieve both sample-wise monotonicity and model-size-wise monotonicity under certain assumptions. Concretely, we show Sample-wise monotonicity: In the setting of well-specified linear regression with isotropic features/covariates (Figure 1), we prove that optimally-tuned ridge regression yields monotonic test performance with increasing samples. That is, more data never hurts for optimally-tuned ridge regression (see Theorem 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Model-wise monotonicity: We consider a setting where the input/covariate lives in a high-dimensional ambient space with isotropic covariance. Given a fixed model size $d$ (which might be much smaller than ambient dimension), we consider the family of models which first project the input to a random $d$-dimensional subspace, and then compute a linear function in this projected "feature space." (This is nearly identical to models of double-descent considered in Hastie et al. ). We prove that in this setting, as we grow the model-size, optimally-tuned ridge regression over the projected features has monotone test performance. That is, with optimal regularization, bigger models are always better or the same. (See Theorem 3).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Monotonicity in the real-world: We also demonstrate several richer empirical settings where optimal $\ell_{2}$ regularization induces monotonicity, including random feature classifiers and convolutional neural networks. This suggests that the mitigating effect of optimal regularization may hold more generally in broad machine learning contexts. (See Section 5).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

A few remarks are in order: Problem-specific vs Minimax and Bayesian. It is worth noting that our results hold for all linear ground-truths, rather than holding for only the worst-case ground-truth or a random ground-truth. Indeed, the minimax optimal estimator or the Bayes optimal estimator are both trivially sample-wise and model-wise monotonic *with respect to the minimax risk or the Bayes risk*. However, they do not guarantee monotonicity of the risk itself for a given fixed problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Universal vs Asymptotic. We also remark that our analysis is not only non-asymptotic but also works for all possible input dimensions, model sizes, and sample sizes. Prior works on double descent mostly rely on asymptotic assumptions that send the sample size or the model size to infinity in a specific manner. To our knowledge, the results herein are the first non-asymptotic sample-wise and model-wise monotonicity results for linear regression. (See discussion of related works Hastie et al.; Mei & Montanari for related results in the asymptotic setting).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Finally, we note that our claims are about monotonicity of the actual test risk, instead of the monotonicity of the generalization bounds (e.g., results in Wei et al. ).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Towards a more general characterization. Our theoretical results crucially rely on the covariance of the data being isotropic. A natural next question is if and when the same results can hold more generally. A full answer to this question is beyond the scope of this paper, though we give the following results: Optimally-tuned ridge regression is *not* always sample-monotonic: we show a counterexample for a certain non-Gaussian data distribution and heteroscedastic noise. We are not aware of prior work pointing out this fact. (See Section 4.1 for the counterexample and intuitions.)

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

For non-isotropic Gaussian covariates, we can achieve sample-wise monotonicity with a regularizer that depends on the population covariance matrix of data. This suggests unlabeled data might also help mitigate double descent in some settings, because the population covariance can be estimated from unlabeled data. (See Section 6).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

For non-isotropic Gaussian covariates, we conjecture that optimally-tuned ridge regression is sample-monotonic even with a standard $\ell_{2}$ regularizer (as in Figure 2). We derive a sufficient condition for this conjecture, which we verify numerically on a wide variety of cases.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

The last two results above highlight the importance of the form of the regularizer, which leads to the open question: "How do we design good regularizers which mitigate or remove double descent?" We hope that our results can motivate future work on mitigating the double descent phenomenon, and allow us to train high performance models which do not exhibit nonmonotonic behaviors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Related Works", "weight": 1.0} -->

The study of nonmonotonicity in learning algorithms existed prior to double descent and has a long history going back to (at least) Trunk and LeCun et al.; Le Cun et al., where the former was largely empirical observations and the latter studied the sample non-nonmonotonicity of unregularized linear regression in terms of the eigenspectrum of the covariance matrix; the difference to our works is that we study this in the context of optimal regularization. In fact, Duin; Opper; Loog & Duin. Loog et al. introduces the same notion of risk monotonicity which we consider, and studies several examples of monotonic and non-monotonic procedures.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Related Works", "weight": 1.0} -->

Double descent of test risk as a function of model size was considered recently in more generality by Belkin et al.. Similar behavior was observed empirically in earlier work in somewhat more restricted settings Trunk; Opper; Skurichina & Duin; Le Cun et al.; LeCun et al. and more recently in Advani & Saxe; Geiger et al.; Spigler et al.; Neal et al.. Recently Nakkiran et al. demonstrated a generalized double descent phenomenon on modern deep networks, and highlighted "sample non-monotonicity" as an aspect of double descent.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Related Works", "weight": 1.0} -->

A recent stream of theoretical works consider model-wise double descent in simplified settings--- often via linear models for regression or classification. This also connects to works on high-dimentional regression in the statistics literature. A partial list of works in these areas include Belkin et al.; Hastie et al.; Bartlett et al.; Muthukumar et al.; Bibas et al.; Mitra; Mei & Montanari; Liang & Rakhlin; Liang et al.; Xu & Hsu; Dereziński et al.; Lampinen & Ganguli; Deng et al.; Nakkiran; Mahdaviyeh & Naulet; Dobriban et al.; Dobriban & Sheng; Kobak et al.. Of these, most closely related to our work are Hastie et al.; Dobriban et al.; Mei & Montanari. Specifically, Hastie et al. considers the risk of unregularized and regularized linear regression in an asymptotic regime, where dimension $d$ and number of samples $n$ scale to infinity together, at a constant ratio $d/n$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Related Works", "weight": 1.0} -->

In contrast, we show *non-asymptotic* results, and are able to consider increasing the number of samples for a fixed model, without scaling both together. Mei & Montanari derive similar results for unregularized and regularized random features, also in an asymptotic limit. The non-asymptotic versions of the settings considered in Hastie et al. are almost identical to ours--- for example, our projection model in Section 3 is nearly identical to the model in Hastie et al.. Finally, subsequent to our work, d'Ascoli et al. identified triple descent in an asymptotic setting.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sample Monotonicity in Ridge Ridgression", "weight": 1.0} -->

In this section, we prove that optimally-regularized ridge regression has test risk that is monotonic in samples, for isotropic gaussian covariates and linear response. This confirms the behavior empirically observed in Figure 1. We also show that this monotonicity is not "fragile", and using larger than larger regularization is still sample-monotonic (consistent with Figure 1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sample Monotonicity in Ridge Ridgression", "weight": 1.0} -->

Formally, we consider the following linear regression problem in $d$ dimensions. The input/covariate $x \in {\mathbb{R}}^{d}$ is generated from $\mathcal{N}{(0,I_{d})}$, and the output/response is generated by with $\varepsilon \sim {\mathcal{N}{(0,\sigma^{2})}}$ and for some unknown parameter $\beta^{\ast} \in {\mathbb{R}}^{d}$. We denote the joint distribution of $(x,y)$ by $\mathcal{D}$. We are given $n$ training examples ${\{{(x_{i},y_{i})}\}}_{i = 1}^{n}$ i.i.d sampled from $\mathcal{D}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sample Monotonicity in Ridge Ridgression", "weight": 1.0} -->

We aim to learn a linear model ${f_{\beta}{(x)}} = {\langle x,\beta\rangle}$ with small population mean-squared error on the distribution $\mathcal{D}$ For simplicity, let $X \in {\mathbb{R}}^{n \times d}$ be the data matrix that contains $x_{i}^{\top}$'s as rows and let $\overset{\rightarrow}{y} \in {\mathbb{R}}^{n}$ be column vector that contains the responses $y_{i}$'s as entries. For any estimator ${\hat{\beta}}_{n}{(X,\overset{\rightarrow}{y})}$ as a function of $n$ samples, define the expected risk of the estimator as: We consider the regularized least-squares estimator, also known as the ridge regression estimator.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sample Monotonicity in Ridge Ridgression", "weight": 1.0} -->

For a given $\lambda > 0$, define Here $I_{d}$ denotes the $d$ dimensional identity matrix. Let $\lambda_{n}^{\text{opt}}$ be the optimal ridge parameter (that achieves the minimum expected risk) given $n$ samples: Let ${\hat{\beta}}_{n}^{\text{opt}}$ be the estimator that corresponds to the $\lambda_{n}^{\text{opt}}$ Our main theorem in this section shows that the expected risk of ${\hat{\beta}}_{n}^{\text{opt}}$ monotonically decreases as $n$ increases.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model-wise Monotonicity in Ridge Regression", "weight": 1.0} -->

In this section, we show that for a certain family of linear models, optimal regularization prevents model-wise double descent. That is, for a fixed number of samples, larger models are not worse than smaller models.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model-wise Monotonicity in Ridge Regression", "weight": 1.0} -->

We consider the following learning problem. Informally, covariates live in a $p$-dimensional ambient space, and we consider models which first linearly project down to a random $d$-dimensional subspace, then perform ridge regression in that subspace for some $d \leq p$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model-wise Monotonicity in Ridge Regression", "weight": 1.0} -->

Formally, the covariate $x \in {\mathbb{R}}^{p}$ is generated from $\mathcal{N}{(0,I_{p})}$, and the response is generated by with $\varepsilon \sim {\mathcal{N}{(0,\sigma^{2})}}$ and for some unknown parameter $\theta \in {\mathbb{R}}^{p}$. Next, $n$ examples ${\{{(x_{i},y_{i})}\}}_{i = 1}^{n}$ are sampled i.i.d from this distribution. For a given model size $d \leq p$, we first sample a random orthonormal matrix $P \in {\mathbb{R}}^{d \times p}$ which specifies our model.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model-wise Monotonicity in Ridge Regression", "weight": 1.0} -->

We then consider models which operate on ${(\overset{\sim}{x_{i}},y_{i})} \in {{\mathbb{R}}^{d} \times {\mathbb{R}}}$, where $\overset{\sim}{x_{i}} = {Px_{i}}$. We denote the joint distribution of $(\overset{\sim}{x},y)$ by $\mathcal{D}$. Here, we emphasize that $p$ is some large ambient dimension and $d \leq p$ is the size of the model we learn.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model-wise Monotonicity in Ridge Regression", "weight": 1.0} -->

For any estimator $\hat{\beta}{(\overset{\sim}{X},\overset{\rightarrow}{y})}$ as a function of the observed samples, define the expected risk of the estimator as: We consider the regularized least-squares estimator. For a given $\lambda > 0$, define Let $\lambda_{d}^{\text{opt}}$ be the optimal ridge parameter (that achieves the minimum expected risk) for a model of size $d$, with $n$ samples: Let ${\hat{\beta}}_{d}^{\text{opt}}$ be the estimator that corresponds to the $\lambda_{d}^{\text{opt}}$ Now, our main theorem in this setting shows that with optimal $\ell_{2}$ regularization, test performance is monotonic in model size.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Counterexamples to Monotonicity", "weight": 1.0} -->

In this section, we show that optimally-regularized ridge regression is *not* always monotonic in samples. We give a numeric counterexample in $d = 2$ dimensions, with non-gaussian covariates and heteroscedastic noise. This does not contradict our main theorem in Section 2, since this distribution is not jointly Gaussian with isotropic marginals.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Counterexample", "weight": 1.0} -->

Here we give an example of a distribution $(x,y)$ for which the expected error of optimally-regularized ridge regression with $n = 2$ samples is worse than with $n = 1$ samples.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Counterexample", "weight": 1.0} -->

This counterexample is most intuitive to understand when the ridge parameter $\lambda$ is allowed to depend on the specific sample instance $(X,\overset{\rightarrow}{y})$ as well as $n$^11^1 Recall, our model of optimal ridge regularization from Section 2 only allows $\lambda$ to depend on $n$ (not on $X,\overset{\rightarrow}{y}$).. We sketch the intuition for this below.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Counterexample", "weight": 1.0} -->

Consider the following distribution on $(x,y)$ in $d = 2$ dimensions. This distribution has one "clean" coordinate and one "noisy" coordinate. The distribution is: where $A = 10$ and $\pm A$ is uniformly random independent noise. This distribution is "well-specified" in that the optimal predictor is linear in $x$: ${\mathbb{E}{\lbrack\left. y \middle| x \right.\rbrack}} = {\langle\beta^{\ast},x\rangle}$ for $\beta^{\ast} = {\lbrack 1,0\rbrack}$. However, the noise is heteroscedastic.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Counterexample", "weight": 1.0} -->

For $n = 1$ samples, the estimator can decide whether to use small $\lambda$ or large $\lambda$ depending on if the sampled coordinate is the "clean" or "noisy" one. Specifically, for the sample $(x,y)$: If $x = {\overset{\rightarrow}{e}}_{1}$, then the optimal ridge parameter is $\lambda = 0$. If $x = {\overset{\rightarrow}{e}}_{2}$, then the optimal parameter is $\lambda = \infty$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Counterexample", "weight": 1.0} -->

For $n = 2$ samples, with probability $1/2$ the two samples will hit both coordinates. In this case, the estimator must chose a single value of $\lambda$ uniformly for both coordinates. This yields to a suboptimal tradeoff, since the "noisy" coordinate demands large regularization, but this hurts estimation on the "clean" coordinate.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Counterexample", "weight": 1.0} -->

It turns out that a slight modification to the above also serves as a counterexample to monotonicity when the regularization parameter $\lambda$ is chosen only depending on $n$ (and not on the instance $X,y$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We now experimentally demonstrate that optimal $\ell_{2}$ regularization can mitigate double descent, in more general settings than Theorems 1 and 3.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sample Monotonicity", "weight": 1.0} -->

Here we show various settings where optimal $\ell_{2}$ regularization empirically induces sample-monotonic performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Nonisotropic Regression", "weight": 1.0} -->

We first consider the setting of Theorem 1, but with non-isotropic covariantes $x$. That is, we perform ridge regression on samples $(x,y)$, where the covariate $x \in {\mathbb{R}}^{d}$ is generated from $\mathcal{N}{(0,\Sigma)}$ for $\Sigma \neq I_{d}$. As before, the response is generated by $y = {{\langle x,\beta^{\ast}\rangle} + \varepsilon}$ with $\varepsilon \sim {\mathcal{N}{(0,\sigma^{2})}}$ for some unknown parameter $\beta^{\ast} \in {\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nonisotropic Regression", "weight": 1.0} -->

We consider the same ridge regression estimator, Figure 2: Test Risk vs. Num. Samples for Non-Isotropic Ridge Regression in d = 30 dimensions. Unregularized regression is non-monotonic in samples, but optimally-regularized regression is monotonic. Note the optimal regularization λ depends on the number of samples n. Plotting empirical means of test risk over 5000 trials. See Figure 6 for the corresponding train errors.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nonisotropic Regression", "weight": 1.0} -->

We see that unregularized regression ($\lambda = 0$) actually undergoes "triple descent"^22^2See also the "multiple descent" behavior of kernel interpolants in Liang et al.. in this setting, with the first peak around $n = 15$ samples due to the 15-dimensional large eigenspace, and the second peak at $n = d$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonisotropic Regression", "weight": 1.0} -->

In this setting, optimally-regularized ridge regression is empirically monotonic in samples (Figure 2). Unlike the isotropic setting of Section 2, the optimal ridge parameter $\lambda_{n}$ is no longer a constant, but varies with number of samples $n$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Random ReLU Features", "weight": 1.0} -->

We consider random ReLU features, in the random features framework of Rahimi & Recht. We apply random features to Fashion-MNIST Xiao et al., an image classification problem with 10 classes. Input images $x \in {\mathbb{R}}^{d}$ are normalized and flattened to ${\lbrack{- 1},1\rbrack}^{d}$ for $d = 784$. Class labels are encoded as one-hot vectors $y \in {\{\overset{\rightarrow}{e_{1}},{\ldots\overset{\rightarrow}{e_{10}}}\}} \subset {\mathbb{R}}^{10}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Random ReLU Features", "weight": 1.0} -->

For a given number of features $D$, and number of samples $n$, the random feature classifier is obtained by performing regularized linear regression on the embedding where $W \in {\mathbb{R}}^{D \times d}$ is a matrix with each entry sampled i.i.d $\mathcal{N}{(0,{1/\sqrt{d}})}$, and ReLU applies pointwise. This is equivalent to a 2-layer fully-connected neural network with a frozen (randomly-initialized) first layer, trained with $\ell_{2}$ loss and weight decay.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Random ReLU Features", "weight": 1.0} -->

(a) Test Classification Error vs. Number of Training Samples.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Random ReLU Features", "weight": 1.0} -->

(b) Test Classification Error vs. Model Size (Number of Random Features).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Model-size Monotonicity", "weight": 1.0} -->

Here we empirically show that optimal $\ell_{2}$ regularization can mitigate model-wise double descent.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Random ReLU Features", "weight": 1.0} -->

We consider the same experimental setup as in Section 5.1, but now fix the number of samples $n$, and vary the number of random features $D$. This corresponds to varying the width of the corresponding 2-layer neural network.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Convolutional Neural Networks", "weight": 1.0} -->

We follow the experimental setup of Nakkiran et al. for model-wise double descent, and add varying amounts of $\ell_{2}$ regularization (weight decay). We chose the following setting from Nakkiran et al., because it exhibits double descent even with no added label noise.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convolutional Neural Networks", "weight": 1.0} -->

We consider the same family of 5-layer convolutional neural networks (CNNs) from Nakkiran et al., consisting of 4 convolutional layers of widths $\lbrack k,{2k},{4k},{8k}\rbrack$ for varying $k \in {\mathbb{N}}$. This family of CNNs was introduced by Page. We train and test on CIFAR-100 Krizhevsky et al., an image classification problem with 100 classes. Inputs are normalized to ${\lbrack{- 1},1\rbrack}^{d}$, and we use standard data-augmentation of random horizontal flip and random crop with 4-pixel padding. All models are trained using Stochastic Gradient Descent (SGD) on the cross-entropy loss, with step size $0.1/\sqrt{{\lfloor{T/512}\rfloor} + 1}$ at step $T$. We train for $1e6$ gradient steps, and use weight decay $\lambda$ for varying $\lambda$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Convolutional Neural Networks", "weight": 1.0} -->

Due to optimization instabilities for large $\lambda$, we use the model with the minimum train loss among the last 5K gradient steps.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Towards Monotonicity with General Covariates", "weight": 1.0} -->

Here we investigate whether monotonicity provably holds in more general models, inspired by the experimental results. As a first step, we consider Gaussian (but not isotropic) covariances and homeostatic noise. That is, we consider ridge regression in the setting of Section 2, but with $x \sim {\mathcal{N}{(0,\Sigma)}}$, and $y \sim {{\langle x,\beta^{\ast}\rangle} + {N{(0,\sigma^{2})}}}$. In this section, we observe that ridge regression can be made sample-monotonic with a modified regularizer. We also conjecture that ridge regression is sample-monotonic without modifying the regularizer, and we outline a potential proof strategy along with numerical evidence.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Adaptive Regularization", "weight": 1.0} -->

The results on isotropic regression in Section 2 imply that ridge regression can be made sample-monotonic even for non-isotropic covariates, if an appropriate regularizer is applied. Specifically, the appropriate regularizer depends on the covariance of the inputs: for $x \sim {\mathcal{N}{(0,\Sigma)}}$, the following estimator is sample-monotonic for optimally-tuned $\lambda$: This follows directly from Theorem 1 by applying a change-of-variable; full details of this equivalence are in Section A.3. Note that if the population covariance $\Sigma$ is not known, it can potentially be estimated from unlabeled data.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Towards Proving Monotonicity", "weight": 1.0} -->

We conjecture that optimally-regularized ridge regression is sample-monotonic for non-isotropic covariates, even without modifying the regularizer (as suggested by the experiment in Figure 2). We derive a sufficient condition for monotonicity, which we have numerically verified in a variety of instances.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conjecture 1", "weight": 1.0} -->

For all $d \in {\mathbb{N}}$, and all PSD covariances $\Sigma \in {\mathbb{R}}^{d \times d}$, consider the distribution on $(x,y)$ where $x \sim {\mathcal{N}{(0,\Sigma)}}$, and $y \sim {{\langle x,\beta^{\ast}\rangle} + {\mathcal{N}{(0,\sigma^{2})}}}$. Then, we conjecture that the expected test risk of the ridge regression estimator: for optimally-tuned $\lambda \geq 0$, is monotone non-increasing in number of samples $n$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conjecture 1", "weight": 1.0} -->

In order to establish Conjecture 1, it is sufficient to prove the following technical conjecture.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conjecture 2", "weight": 1.0} -->

For all $n \in {\mathbb{N}}$, $d \geq n$, $\lambda > 0$, symmetric positive definite matrix $Q \in {\mathbb{R}}^{d \times d}$, the following holds. where $X \in {\mathbb{R}}^{n \times d}$ is sampled with each entry i.i.d. $\mathcal{N}{}$. Similarly, define The expected test risk for $n$ samples can be expressed as: Then, we conjecture that the following two conditions hold.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conjecture 2", "weight": 1.0} -->

Proving Conjecture 2 presents a number of technical challenges, but we have numerically verified it in a variety of cases. (One can numerically verify the conjecture for a fixed $Q$, $n$ and $d$. Here $Q$ can be assumed to be diagonal w.l.o.g. because $X$ is isotropic. The matrices and scalars in equation can be evaluated by sampling the random matrix $X$. The derivatives w.r.t $\lambda$ can be done by auto-differentiation).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conjecture 2", "weight": 1.0} -->

It can also be shown that Conjecture 2 is true when $Q = I$, corresponding to isotropic covariates. We show that Conjecture 2 implies Conjecture 1 in in Section A.3.1 of the Appendix.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this work, we study the double descent phenomenon in the context of optimal regularization. We show that, while unregularized or under-regularized models often have non-monotonic behavior, appropriate regularization can eliminate this effect.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Theoretically, we prove that for certain linear regression models with isotropic covariates, optimally-tuned $\ell_{2}$ regularization achieves monotonic test performance as we grow either the sample size or the model size. These are the first non-asymptotic monotonicity results we are aware of in linear regression. We also demonstrate empirically that optimally-tuned $\ell_{2}$ regularization can mitigate double descent for more general models, including neural networks. We hope that our results can motivate future work on mitigating the double descent phenomenon, and allow us to train high performance models which do not exhibit unexpected nonmonotonic behaviors.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Open Questions", "weight": 1.0} -->

Our work suggests a number of natural open questions. First, it is open to prove (or disprove) that optimal ridge regression is sample-monotonic for non-isotropic Gaussian covariates (Conjecture 1). We conjecture that it is, and outline a potential route to proving this (via Conjecture 2). The non-isotropic setting presents a number of differences from the isotropic one (e.g. the optimal regularizer $\lambda$ depends on number of samples $n$), and thus a proof of this may yield further insight into mechanisms of monotonicity.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Open Questions", "weight": 1.0} -->

Second, more broadly, it is open to prove sample-wise or model-wise monotonicity for more general (non-linear) models with appropriate regularizers. Addressing the monotonicity of non-linear models may require us to design new regularizers which improve the generalization when the model size is close to the sample size. It is possible that data-dependent regularizers (which depend on certain statistics of the labeled or unlabeled data) can be used to induce sample monotonicity, analogous to the approach in Section 6.1 for linear models. Recent work has introduced data-dependent regularizers for deep models with improved generalization upper bounds Wei & Ma, however a precise characterization of the test risk remain elusive.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Open Questions", "weight": 1.0} -->

Finally, it is open to understand why large neural networks in practice are often sample-monotonic in realistic regimes of sample sizes, even without careful choice of regularization.
