<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Enhancing a Risk Model by Adding Transient Statistical Factors

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Estimating the covariance of asset returns, i.e., the risk model, is a key component of financial portfolio construction and evaluation. Most risk modeling approaches produce a factor model that decomposes the asset variability into two components: the first attributed to a small number of factors that are common among the assets and the second attributed to the idiosyncratic behavior of each asset. Third-party providers typically provide risk models to investors, and while these models are typically of high quality, they may fail to capture important information, e.g., changing market regimes and transient factors. To overcome these limitations, we propose a systematic method based on maximum likelihood estimation to enhance an existing factor model by both refining the given model and adding new statistical factors. Our approach relies only on the observed sequence of realized returns and on the choice of two hyperparameters: the number of additional factors and the half-life parameter that determines the weights assigned to returns in the log-likelihood objective. Importantly, our methodology applies to the situation where asset returns may be missing, making it suitable for typical equity datasets.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate our approach on the Barra short-term US risk model, a high-quality risk model used in practice, for a universe of US high-capitalization equities. We show that the proposed extension captures structure in the returns that is missed by the original model.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The covariance of asset returns is a central quantity in several areas of finance, including Markowitz portfolio construction, risk management, asset pricing, and performance attribution analysis. The variance of a portfolio (or investment strategy) is a linear function of the asset return covariance. An accurate (as judged by its statistical fit) asset return covariance allows investors to build portfolios with a desired level of risk and also evaluate the risk of existing portfolios. An inaccurate risk model can over-estimate or under-estimate portfolio risk. As a result, during portfolio construction, it may be overly restrictive, causing the investor to miss out on potentially good investments, or fail to account for certain risk sources, potentially exposing the investment strategy to unexpected risks. Risk modeling is therefore a challenging problem in any investment process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A challenge is that only information available at the current time can be used to estimate the risk model, which should be predictive of the assets' behavior in the future (that is, out-of-sample). Prediction is particularly difficult because of changing market conditions, extreme events (e.g., COVID-19), and fat tails in the distribution of returns. In addition, asset returns can fluctuate significantly even on a daily basis, making it difficult to separate meaningful structure from randomness. The high dimensionality of the data, i.e., the large number of assets (possibly thousands), is another challenge. Capturing the dependence structure of thousands of assets requires simultaneously and accurately estimating a very large number of parameters from return data. For instance, the sample covariance based on the observed data is singular when the number of assets is larger than the number of sample return vectors. This implies that there are directions in asset space with zero estimated variance, and it is easy to understand that this will cause problems in portfolio construction.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of these challenges, various companies, for example MSCI Barra \[21, 19, Methodology Notes")\], offer risk models as products and a Nobel Memorial Prize in Economic Sciences was awarded for work directly related to volatility estimation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A standard model for the asset returns is the factor model. At any time $t$, it assumes that the vector of asset returns, $x_{t} \in {\mathbb{R}}^{n}$, is driven by a low-dimensional vector of factor returns, $s_{t} \in {\mathbb{R}}^{n_{1}}$, and a vector of residual returns $\epsilon_{t} \in {\mathbb{R}}^{n}$, i.e.,

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $F_{t} \in {\mathbb{R}}^{n \times n_{1}}$ is the matrix of factor exposures, $\epsilon_{t}$ is independent of $s_{t}$, the $n$ elements of $\epsilon_{t}$ are independent, and $n_{1} \ll n$. In this model, $x_{t}$, $s_{t}$, and $\epsilon_{t}$ are random vectors and $F_{t}$ is a non-random matrix that can vary with time $t$. The model implies that there are common factors that influence the returns of the assets. For equities, factors typically include the returns of specific portfolios, such as the overall market (with weights proportional to capitalization), industries, and style portfolios like the Fama-French factors. The model also implies that there is a part of the returns that cannot be attributed to these factors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We call this part the idiosyncratic return, $\epsilon_{t}$, which is independent of the factor returns, $s_{t}$, and also independent for each asset.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under these assumptions the asset return covariance is given by the low-rank-plus-diagonal form

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

where ${\mathbf{c}\mathbf{o}\mathbf{v}}{( \cdot )}$ denotes the covariance. Because the elements of $\epsilon_{t}$ are independent, ${\mathbf{c}\mathbf{o}\mathbf{v}}{(\epsilon_{t})}$ is a diagonal matrix with positive diagonal entries. This structure is especially appealing in high dimensions ($n$ in the order of hundreds or thousands), because we only need to estimate $\mathcal{O}{({nn_{1}})}$ parameters, instead of $\mathcal{O}{(n^{2})}$ in the case of a generic $n \times n$ covariance matrix. The smaller number of parameters required in the low-rank-plus-diagonal structure is also a form of regularization, which avoids overfitting and can improve the covariance estimate, especially for out-of-sample applications (such as predicting future portfolio risk).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The low-rank-plus-diagonal structure also allows for a positive definite covariance matrix even when there are fewer than $n$ return samples. Finally, in the context of portfolio construction using convex optimization, the low-rank-plus-diagonal structure can be exploited to bring the computational complexity down from $\mathcal{O}{(n^{3})}$ to $\mathcal{O}{({nn_{1}^{2}})}$ operations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we assume a low-rank-plus-diagonal risk model is provided. We call this the base or existing model. This scenario is typical in the case of investors or quantitative traders, e.g., an MSCI Barra \[21, 19, Methodology Notes")\] model is available. We propose a principled method based on maximum likelihood estimation to refine the existing model and extend it with additional statistical factors using the time series of realized asset returns. Our method can be used to capture market shifts of a shorter time horizon than the update period of the provided risk model. Furthermore, the added statistical factors capture structure in the returns that is missed by the base model. As a demonstration of our approach, we extend the Barra short-term US risk model (already high-quality and widely used in practice) for a universe of 870 US high-capitalization equities and obtain an improvement in terms of the model's out-of-sample statistical fit. We show that the extended model uncovers hidden structure in the returns that is missed by the base model. As a secondary contribution, we also show how to handle missing return data within our framework.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Missing returns arise in financial datasets for several practical reasons, such as reporting delays, non-synchronous trading across time zones, or unavailable price observations on certain dates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. In Section 2, we discuss related work in covariance estimation and low-rank-plus-diagonal risk modeling. In Section 3, we mathematically formulate our maximum likelihood estimation problem. Our proposed approach is described in Section 4. We discuss metrics and results in Section 5. The paper concludes with Section 6.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Prior work", "weight": 1.0} -->

We review in Section 2.1 the standard approaches to empirical covariance estimation that rely solely on the time series of historical returns and do not impose any structural assumptions. Next, in Section 2.2 we turn to techniques that introduce additional structure into the covariance matrix---most notably low-rank-plus-diagonal decompositions---which aim to capture common risk factors and improve stability in high-dimensional settings.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Empirical covariance estimation", "weight": 1.0} -->

Given a time-series of historical returns, the simplest covariance estimate is the sample covariance. However, when the number of assets is large relative to the number of return samples (which is almost always true in practice), the sample covariance is a very poor approximation of the true covariance and its eigenvalues can have high variance. Generally, the sample covariance may fail to capture the time-dependence and regime shifting of financial markets. A simple way to deal with the regime shifting is to use a rolling window estimate, which has a fixed memory window and only averages the return outer products in this window. To improve the quality of the estimator we can add regularization or shrinkage. Practitioners often replace rolling window covariance estimates with exponentially weighted moving averages (EWMAs) to place greater weight on recent observations, thereby adapting more quickly to time-varying conditions \[12, 19, Methodology Notes"), 13\]. The EWMA estimator is controlled by the half-life parameter that dictates how far in the past the weight of an observation is reduced to $0.5$. The half-life parameter is thus completely interpretable.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Empirical covariance estimation", "weight": 1.0} -->

The EWMA estimate also allows for fast, recursive computation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Empirical covariance estimation", "weight": 1.0} -->

When the number of assets is large and the half-life (or the length of the returns time-series) is small, naive covariance estimation leads to singular matrices. In these cases, even though it might fail to capture information in the returns, a popular remedy is to learn a factor model, which we discuss next.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Low-rank-plus-diagonal risk models", "weight": 1.0} -->

Factor models are a natural way to represent correlations among assets, because assets in similar market sectors tend to behave similarly. We discuss methods that produce risk models in low-rank-plus-diagonal form. These methods differ in how they obtain the factor exposure matrix, the covariance of the factor returns, and the covariance of the idiosyncratic returns. Each method corresponds to a different category of factors: fundamental, macroeconomic, and statistical. Fundamental and macroeconomic factors are built from observable economic, financial, or asset-specific characteristics. Such a factor can correspond to a concept that has an intuitive interpretation grounded in economics, corporate structure, or investor behavior. Fundamental factors include industry/sector classifications, while macroeconomic factors include inflation, unemployment, industrial productivity, as well as oil, gold, and interest rates. Statistical factors are extracted directly from historical return data through dimensionality-reduction techniques. They attempt to capture the main directions of covariance in the return vector without imposing any economic interpretation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Methods based on fundamental factors", "weight": 1.0} -->

In this case, we calculate the factor exposure matrix and then estimate the factor returns by regressing the asset returns on the factor exposures. Either ordinary or generalized least squares (where we scale each asset by its volatility) is used in this empirical approach. We then estimate the covariance of the factor returns using a method from Section 2.1 and the variances of the idiosyncratic returns similarly from the regression residuals. We mention an example of a fundamental factor: the price-to-earnings ratio. We can assign the price-to-earnings ratio of each asset as its exposure to the factor, perhaps with some cross-sectional (i.e., across assets) standardization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Methods based on macroeconomic factors", "weight": 1.0} -->

In this case, we calculate the factor returns first. For example, we can use the returns of style portfolios as the factor returns. We then compute the factor exposure matrix by regressing the historical asset returns on the historical factor returns. We estimate the covariance of the factor returns using a method from Section 2.1 and the variances of the idiosyncratic returns similarly from the regression residuals. Note that the estimation of the factor exposure matrix is separable across assets. This is also an empirical approach.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methods based on statistical factors", "weight": 1.0} -->

Such methods start by computing an empirical asset return covariance, as described in Section 2.1. The low-rank-plus-diagonal structure is imposed by dimensionality reduction. Effectively, we find the low-rank-plus-diagonal model that optimizes an objective involving the empirical covariance. We can learn the low-rank component by minimizing its Frobenius norm to the empirical covariance. The solution is related to the top eigenvalues (and corresponding eigenvectors) of the empirical estimate, \[12, Section 8.2\],. We can then set the idiosyncratic component of the risk model to match the diagonal entries of the empirical covariance estimate. This approach tends to underestimate the idiosyncratic risk. If we fit the risk model by maximizing Gaussian log-likelihood, then the solution can be obtained via an iterative algorithm called expectation-maximization (EM) or an alternating minimization approach.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Methods based on statistical factors", "weight": 1.0} -->

The risk model is time-dependent as the factor exposures, factor return covariance, and idiosyncratic return covariance are all time-dependent quantities. The update frequency of the risk model can vary from daily to, e.g., quarterly, depending on the investor's needs and the nature of the factors involved. The update frequency can be a limiting factor when it comes to the responsiveness of the risk model to changing market conditions. For example, a quarterly update frequency may not be able to capture sudden market regime shifts or transient factors that appear on shorter time scales.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Our contribution", "weight": 1.0} -->

We propose a method that can extend any given low-rank-plus-diagonal risk model, either fundamental, macroeconomic, or statistical. Our algorithm uses the history of observed returns and a weighted Gaussian log-likelihood objective to refine the base model and extend it with additional statistical factors. As such, it is a principled way to build hybrid models with both fundamental-macroeconomic and statistical factors. Spector et al. investigated how to assess the statistical fit of an existing risk model and proposed a simple method to extend the model by recursively adding factors. Our work is similarly based on a provided model, but our method both refines the given risk model and adds new statistical factors. Lee et al. also propose extending a risk model by additional factors. However, the asset exposures to these new factors are not estimated statistically, but are instead constructed. The new factor exposures are thematic narrative exposures built from news data. They are constructed based on how frequently the narrative appears in news coverage about each asset. Furthermore, the covariance of the new factor returns is estimated following an empirical approach that uses ordinary least squares.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Our contribution", "weight": 1.0} -->

In contrast, our approach relies on statistically learning the additional factors in order to improve the likelihood fit of the observed data. In addition, beyond adding new factors, our approach also refines the covariance of the factor returns of the base model.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Our contribution", "weight": 1.0} -->

We leave the algorithmic selection of the number of additional factors as future work. We note that our approach preserves the factor exposures to the base factors. As such, the methodology is particularly suitable when the base model consists of fundamental factors. By choosing the log-likelihood weights based on an EWMA with an appropriate (typically short) half-life, our work can also be regarded as a principled way to find additional transient factors in the returns, which are commonly known as themes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Suppose at time $t$ we are given a sequence of asset return vectors ${x_{1},\ldots,x_{T}} \in {\mathbb{R}}^{n}$, potentially with missing entries. We are also provided with the base asset return covariance model

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem statement", "weight": 1.0} -->

where $F_{1} \in {\mathbb{R}}^{n \times n_{1}}$ is the matrix of factor exposures to the base factors, $\Omega_{base}$ is the (positive definite) covariance of the base factor returns, and $D_{base}$ is a diagonal matrix with positive diagonal entries corresponding to the idiosyncratic asset variances. In practice, the provided covariance model depends on time $t$, i.e., $F_{1}$, $\Omega_{base}$, and $D_{base}$ depend on $t$. For simplicity we hide this dependence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The extended risk model", "weight": 1.0} -->

We consider the extended asset return covariance model (this model also depends on time $t$ but we hide this dependence)

<!-- chunk {"id": "body-0031", "role": "body", "section": "The extended risk model", "weight": 1.0} -->

where $F_{2} \in {\mathbb{R}}^{n \times n_{2}}$, $\Sigma_{f} \in {\mathbb{R}}^{{({n_{1} + n_{2}})} \times {({n_{1} + n_{2}})}}$, and $D \in {\mathbb{R}}^{n \times n}$. $D$ is a diagonal matrix with positive diagonal entries and $\Sigma_{f}$ is a positive definite matrix. The number of base factors is $n_{1}$ and the number of added factors is $n_{2}$. Typically the total number of factors, $n_{1} + n_{2}$, is much smaller than $n$. We look to find appropriate factor exposures $F_{2}$, factor return covariance $\Sigma_{f}$, and idiosyncratic covariance $D$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The extended risk model", "weight": 1.0} -->

We make a distinction between the factors involved in $F_{1}$ and $F_{2}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The extended risk model", "weight": 1.0} -->

$F_{1}$ is a known matrix of factor exposures, which have been measured and provided to us. For example, $F_{1}$ could be the matrix of factor exposures from an MSCI Barra model. However, the covariance of the factor returns involved in $F_{1}$ will be re-estimated, by learning $\Sigma_{f}$. The only information from the base model that the extended model shall rely on without modification is the matrix of factor exposures $F_{1}$. This is natural if the base model consists of fundamental factors: in such a model exposures are constructed from relatively stable asset characteristics or classification rules, while the covariance of factor returns is computed empirically.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The extended risk model", "weight": 1.0} -->

$F_{2}$ denotes a matrix of unknown factor exposures representing residual factor structure not captured by $F_{1}$. Estimating $F_{2}$ and $\Sigma_{f}$ therefore allows the model to account for additional common sources of variation in asset returns beyond those included in the base model.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

Consider first a general factor model and the implied covariance ${F\Sigma_{f}F^{\top}} + D$, where all the terms are unknown. This is different than our setting, where $F_{1}$ is known. In the general model, neither $F$ nor $\Sigma_{f}$ are identifiable, since for any invertible matrix $R$, setting

<!-- chunk {"id": "body-0036", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

yields the same covariance. With the Cholesky decomposition $\Sigma_{f} = {L_{f}L_{f}^{\top}}$, another equivalent form is

<!-- chunk {"id": "body-0037", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

Since the latter is the easiest representation, the standard form for the general model assumes $\Sigma_{f} = I$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

Our case is a little more complex, because $F_{1}$ is known. We show that the analogous representation for the family of risk models is

<!-- chunk {"id": "body-0039", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

where $\Omega \in {\mathbb{R}}^{n_{1} \times n_{1}}$ is a positive definite matrix, $F_{2} \in {\mathbb{R}}^{n \times n_{2}}$ is arbitrary and $D$ is diagonal. Note that $F_{2}$ is still only identifiable up to a rotation/reflection: if $R$ is any $n_{2} \times n_{2}$ orthogonal matrix, then the representation with $F_{2}$ replaced by $F_{2}R$ is equivalent, since ${F_{2}RR^{\top}F_{2}^{\top}} = {F_{2}F_{2}^{\top}}$ (a standard situation in factor models). We prefer the representation given by the family of models, because it ensures that the additional factors remain identifiable (up to a rotation/reflection) and allows for a decomposition of risk across the base factors $F_{1}$ and the added factors $F_{2}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Identifiability of the extended risk model", "weight": 1.0} -->

Family involves a smaller number of parameters compared to family, i.e., family is over-parameterized.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Estimation objective", "weight": 1.0} -->

We assume that at each time $\tau = {1,\ldots,T}$ we only observe the returns $x_{\tau}$ on a subset of assets indexed by the set $\mathcal{O}_{\tau} \subseteq {\{ 1,\ldots,n\}}$. Let $\mathcal{M}_{\tau} = {{\{ 1,\ldots,n\}} \smallsetminus \mathcal{O}_{\tau}}$ be the set of assets with missing returns at time $\tau$. We denote the observed portion of the return at $\tau$ as $x_{\tau,{obs}}$ and the missing portion as $x_{\tau,{mis}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Estimation objective", "weight": 1.0} -->

and $\mathcal{N}{(\mu,\Sigma)}$ is the Gaussian distribution with mean $\mu$ and covariance $\Sigma$. The covariance of the Gaussian $\mathcal{N}{(0,{{\overset{\sim}{F}\overset{\sim}{\Omega}{\overset{\sim}{F}}^{\top}} + D})}$ belongs to the family of extended risk models. Set the family of all components to be estimated as $\theta =:{(F_{2},\Omega,D)}$. We estimate $\theta$ by solving

<!-- chunk {"id": "body-0043", "role": "body", "section": "Estimation objective", "weight": 1.0} -->

and, with a slight abuse of notation, $p_{\theta}{(x_{\tau,{obs}})}$ is the marginal density of the observed returns at time $\tau$ induced by the density function $p_{\theta}{(x)}$. The weights $w_{\tau}$ are non-negative and sum to $1$. In our setting, they reflect the assumption that more recent observations are more informative and should therefore receive larger weights. Although we do not write it explicitly, $\Omega$ is positive definite and $D$ is diagonal with positive entries in its diagonal.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Estimation objective", "weight": 1.0} -->

Problem maximizes the weighted sum of the Gaussian log-likelihoods of the observed data. Although the distribution of financial returns may not be Gaussian, a Gaussian model is still a reasonable second-order approximation to the cross-sectional structure; in many risk-model applications the main object of interest is the covariance matrix, not the exact tail behavior. The Gaussian assumption also gives a simple tractable framework for estimating and manipulating covariance structure.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Estimation objective", "weight": 1.0} -->

For most daily or even weekly equity returns, the means are typically tiny compared to the random fluctuations. Therefore, assuming a zero mean often has little practical effect when the goal is to estimate the covariance. Nevertheless, we can account for a non-zero mean, by first estimating the mean return and then subtracting it from the return samples.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Solution via expectation-maximization", "weight": 1.0} -->

We propose to solve problem using an iterative method called expectation-maximization (EM). We first discuss the method in general. Then, we show how it applies to the case of fully observed returns. Finally, we discuss how to solve the problem with missing returns.

<!-- chunk {"id": "body-0047", "role": "body", "section": "General description", "weight": 1.0} -->

We have already seen this objective in the previous section in which $y_{\tau}$ was $x_{\tau,\text{obs}}$. We prefer here to use $y_{\tau}$ for generality. In many problems, the log-likelihood is either intractable or leads to difficult optimization. In some cases, e.g. in our setting, augmenting the data with unobserved latent observations simplifies the log-likelihood and permits maximization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "General description", "weight": 1.0} -->

where the conditional expectation above is over the latent variables $z_{\tau}\overset{\text{indep.}}{\sim}p_{\theta_{k}}{(\left. z_{\tau} \middle| y_{\tau} \right.)}$. This is the E-step. Then, the M-step finds

<!-- chunk {"id": "body-0049", "role": "body", "section": "General description", "weight": 1.0} -->

The point of the data augmentation is that the M-step is now tractable. It is well known that the EM produces a monotone sequence in the sense that $\ell{(\theta_{k})}$ is nondecreasing.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

In the case where asset returns are fully observed, the observations $y_{\tau}$ above are the asset returns $x_{\tau}$. The latent variables are the factor returns so that with the notation above $z_{\tau} = s_{\tau}$. The joint distribution $p_{\theta}{(x_{\tau},s_{\tau})}$ of asset returns and factor returns is

<!-- chunk {"id": "body-0051", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

Marginally $x_{\tau} \sim {\mathcal{N}{(0,{{\overset{\sim}{F}\overset{\sim}{\Omega}{\overset{\sim}{F}}^{\top}} + D})}}$, as is requested. The E-step and M-step have closed-form expressions and their derivations are in Appendix C. With these expressions, the steps of the EM algorithm are given in Algorithm 1. In the case that the number of factors in $F_{1}$ is zero ($n_{1} = 0$), our algorithm reduces to the standard EM algorithm for factor models. Algorithm 1 typically converges after $20 - 30$ iterations. That said, we do wish to clarify some of the steps in Algorithm 1 below.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

At iteration $k$, the parameter estimate is $\theta_{k}$. It holds that

<!-- chunk {"id": "body-0053", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

$L_{k}$ and $G_{k}$ are computed in lines 14-15 using standard multivariate Gaussian calculations. Furthermore,

<!-- chunk {"id": "body-0054", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

$C_{ss}^{k}$ is computed in line 15, while $C_{xs}^{k}$ is computed in line 16. Finally, in lines 17-21 we calculate $\theta_{k + 1}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

Particular attention should be given to the initialization $\theta_{0} = {(F_{2}^{0},\Omega_{0},D_{0})}$ in Algorithm 1. Once again, we wish to build the approximation

<!-- chunk {"id": "body-0056", "role": "body", "section": "Fully observed returns", "weight": 1.0} -->

The initialization for $F_{2}$ is based on the singular value decomposition of the residual returns of the base model. This is because the additional factors should explain the variance left unexplained by the base model. The initialization for $D$ preserves the asset volatilities, as given by the empirical covariance $C$. This means that the diagonal entries of the left-hand and right-hand sides in the above display are the same.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Partially observed returns", "weight": 1.0} -->

We let $y_{\tau}$ be the observed returns $x_{\tau,{obs}}$ and $z_{\tau}$ be the factor returns and missing asset returns $(s_{\tau},x_{\tau,{mis}})$. The joint distribution of $(x_{\tau,\text{obs}},x_{\tau,\text{mis}},s_{\tau})$ is $p_{\theta}{(x_{\tau},s_{\tau})}$ (up to a permutation of the variables). The E-step is a little more involved but still has a closed form expression. The M-step also has a closed-form expression. The complete analysis is given in Appendix D.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

We consider the time period between 2018-06-27 and 2023-12-28. This period contains the COVID-19 pandemic, a time of high market volatility. Our universe consists of the US large-capitalization equities in the BlackRock Systematic investment universe for which we observe complete return data over the period from 2018-06-27 to 2023-12-28. We restrict attention to assets with uninterrupted return histories and for simplicity do not consider the version of our approach that explicitly accommodates missing returns in evaluating performance. As a result, the reported performance may not be representative of the performance on the full evolving asset universe. Nevertheless, it allows us to focus on the core mechanism by which our approach refines a general risk model to a targeted investment universe. This restriction does not necessarily favor the extended model over the base model.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

Our universe consists of 870 assets for which we have access to daily returns. Every day $t$, we can observe the history of daily returns $x_{1},\ldots,x_{t}$. The return $x_{\tau}$ corresponds to the time period between day $\tau - 1$ and day $\tau$. The low-rank-plus-diagonal covariance estimate at time $t$ is denoted

<!-- chunk {"id": "body-0060", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

Note that we hide the factor return covariance (specifically its square root) in ${\hat{F}}_{t}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

Our base model is the Barra short-term US risk model, which is updated monthly. The base model consists of $73$ factors for the universe of 870 assets. The $73$ factors include sectors, such as aerodefense, airlines, and banks, where the exposure is binary ($0$ or $1$), and factors where the exposures are not binary, e.g., the beta factor. We extend the base model with an additional $7$ factors. This number is considered a good choice overall, as it allows the extended model to learn information missed by the base model, but also mitigates the risk of overfitting. We update the extended model on a daily basis. We use an EWMA with a half-life of $H = 126$ days for the weights $w_{\tau}$ on each day $t$. Our ability to pick up transient factors depends on the choice of the half-life parameter. A short half-life will allow us to pick up short-lived, rapidly changing effects, but if it is too short it may primarily capture noise rather than meaningful signal.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

A longer half-life will emphasize more persistent, slowly evolving correlations, but may be biased. We do not optimize over the choice of the half-life or the number of additional factors in this paper.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

We compare the two models--the base and the extended models--with respect to their statistical fit out-of-sample. For this purpose we consider several metrics that correspond to separate subsections below. We evaluate the models in the time period between 2019-06-26 and 2023-12-28. The days before 2019-06-26 are used as the burn-in period for the extended model.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Empirical performance", "weight": 1.0} -->

Throughout, we assume that daily returns are zero-mean. This approximation is reasonable for most stocks, because the mean returns are small compared to the random fluctuations. For example, the S&P 500 has a daily mean return of 4 basis points (bps) and a daily volatility of 100 bps.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

If the extended model uncovers covariance structure that the base model misses, then it should be able to better estimate out-of-sample returns. We quantify this by measuring the out-of-sample $R^{2}$. A larger $R^{2}$ implies a better statistical fit. A negative $R^{2}$ implies that the model is worse than simply predicting zero.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

At time $t$, we split the $n$ assets in two disjoint groups: $train$ and $test$ (we suppress the dependence on $t$ for these two groups for clarity). We use the next-day returns for the assets in the train set to get the most likely factor returns according to our model, by solving

<!-- chunk {"id": "body-0067", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

where the superscript $train$ indicates that we only consider the assets in the $train$ set. We maximize the conditional density of the factor returns given the train returns. We then predict the next-day (out-of-sample) returns for the assets in the $test$ set as

<!-- chunk {"id": "body-0068", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

where ${\hat{s}}_{t}$ is the solution of. This is the return prediction under our factor model.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

Using zero as the mean is reasonable for daily asset returns because the mean is typically much smaller than the random fluctuations. If the extended risk model achieves a higher $R^{2}$ than the base model, this suggests that it exploits missing correlations to make better predictions from available returns. We compute $R^{2}$ every day in the evaluation period.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

We include a third risk model in the results of this section as a baseline. We call this model randomly extended. We construct this risk model as follows. Let $F_{2}^{\prime} \in {\mathbb{R}}^{n \times 7}$ be a matrix of factor exposures sampled from $\mathcal{N}{}$. This risk model is then

<!-- chunk {"id": "body-0071", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

where we learn $\Omega_{t}^{\prime}$ and $D_{t}^{\prime}$ using Algorithm 1: we run Algorithm 1 using $n_{2} = 0$ with the input $F_{1}$ being $\begin{bmatrix}
\end{bmatrix}$. Essentially, we augment the base model with a random factor exposure matrix and re-learn the factor return covariance and the idiosyncratic variances to maximize the weighted log-likelihood. The added factor subspace for this model is random and for the small number of added factors we consider it is not expected to capture meaningful structure in the returns.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

The time series of $R_{t}^{2}$ is shown in Figure 1. The extended model outperforms the base model. It is also important to note that the extended model, where the 7 additional factors are learned from the returns data, outperforms the randomly extended model. We therefore conclude that the extended model actually captures covariance structure that the base model misses. The randomly extended model slightly underperforms the base model because it overfits to the assets in the train set due to the random added factors. This emphasizes what should be obvious: adding random factors does not help in estimating out-of-sample returns. We do not show the randomly extended model in future sections.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

Finally we note that the base model also captures a significant amount of structure in the returns. The $90/10$ split is chosen to ensure that the train set is significantly large to obtain meaningful factor return estimates, while the test set is large enough to obtain meaningful out-of-sample $R^{2}$ estimates. We have verified that other splits (e.g., $50/50$) lead to similar conclusions.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Estimating returns", "weight": 1.0} -->

For each risk model we report a point estimate and a dispersion for the $R^{2}$ in Table 1. The extended model offers an improvement in $R^{2}$. It allows for better return forecasts of $10\%$ of the returns given the remaining $90\%$ of the returns.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

The extended model assumes that there is additional structure in the returns beyond the factors included in the base model. If this additional structure exists and the extended model is able to learn it, then it should be able to predict out-of-sample residuals with respect to the factors of the base model using the additional learned factors. This methodology is similar, but not identical, to the measure of out-of-sample performance proposed by Spector et al..

<!-- chunk {"id": "body-0076", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

We only consider the extended model in this section. Recall that in this case ${\hat{F}}_{t} = \begin{bmatrix}
\end{bmatrix}$, where ${\hat{F}}_{1,t} = {F_{1,t}{\hat{\Omega}}_{t}^{1/2}}$ corresponds to the $n_{1}$ factors also present in the base model and ${\hat{F}}_{2,t}$ corresponds to the additional $n_{2}$ factors. The underlying return model is therefore

<!-- chunk {"id": "body-0077", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

At each time $t$, we split the $n$ assets in two disjoint groups: $train$ and $test$ (again we suppress the dependence on $t$). We use the next-day returns for the assets in the train set to compute the factor returns for the $n_{2}$ added factors. We then use these returns to estimate the residuals with respect to the base factors for the assets in the test set.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

In details, we first use the assets in the train set to get the most likely base factor returns, by solving

<!-- chunk {"id": "body-0079", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

where ${\hat{s}}_{1,t}^{train}$ is the solution of. Problem is appropriate because it maximizes the conditional density of the base factor returns, $s_{1,t}$, given the returns in train.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

We then use the train assets to obtain the most likely returns for the $n_{2}$ added factors by solving

<!-- chunk {"id": "body-0081", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

with solution ${\hat{s}}_{2,t}$. Problem maximizes the conditional density of the added factor returns, $s_{2,t}$, given that

<!-- chunk {"id": "body-0082", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

Similarly, we compute the residuals with respect to the base factors for the test assets by solving

<!-- chunk {"id": "body-0083", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

Finally, we compute the predicted residuals with respect to the base factors for the test assets as

<!-- chunk {"id": "body-0084", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

A positive $R^{2}$ here indicates that the added factors are able to explain existing structure in the out-of-sample residuals with respect to the base factors. We note that ${\hat{\epsilon}}_{t + 1}^{test}$ only depends on the next day's returns of the train assets, while $\epsilon_{t + 1}^{test}$ only depends on the next day's returns of the test assets. Our ability to predict the latter using the former depends on the quality of the risk model.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Estimating residuals with respect to the factors of the base model", "weight": 1.0} -->

The $R^{2}$ is plotted in Figure 2. The extended model achieves a positive $R^{2}$ which indicates that it is in fact learning useful structure in the returns. The added factors allow the model to predict out-of-sample residuals with respect to the base factors. The average across time cross-replication mean $R^{2}$ is $0.125$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

We demonstrate in another way that the added factors of the extended model

<!-- chunk {"id": "body-0087", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

capture structure present in the returns that the base factors miss. We consider the null hypothesis

<!-- chunk {"id": "body-0088", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

where ${\overset{\sim}{\epsilon}}_{t}$ and $s_{t}^{}$ are independent, and the elements of ${\overset{\sim}{\epsilon}}_{t}$ are independent. In other words, we assume there is no added structure, other than the base factors. We will show that our predictive ability is not consistent with this hypothesis.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

We split the $n$ assets in two disjoint groups: $train$ and $test$ (again we suppress the dependence on $t$). For each group, we solve the out-of-sample ordinary least squares problem

<!-- chunk {"id": "body-0090", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

where $group$ is either train or test. The solution of is ${\hat{s}}_{1,t}^{group}$ for each group. We compute the optimal residuals

<!-- chunk {"id": "body-0091", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

for each of the two groups: train or test. Under the alternative hypothesis that the extended risk model holds, i.e., the additional factors exist and

<!-- chunk {"id": "body-0092", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

the in-sample residuals of the train and test assets with respect to the base factors (i.e., after solving problems where we replace $x_{t + 1}$ with $x_{t}$) have factor exposures to $s_{2,t}$ equal to $P_{t}^{train}$ and $P_{t}^{test}$, respectively. Therefore, to predict $s_{2,t}$ using ${\hat{\delta}}^{train}$, we solve

<!-- chunk {"id": "body-0093", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

and obtain the solution ${\hat{s}}_{2,t}$. We then make the prediction

<!-- chunk {"id": "body-0094", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

is positive, then we are able to predict ${\hat{\delta}}_{t}^{test}$ from ${\hat{\delta}}_{t}^{train}$, which should not be possible under the null. Therefore, this would be evidence against the null and in favor of the discovered added factors. This methodology is inspired by Spector et al..

<!-- chunk {"id": "body-0095", "role": "body", "section": "Predictive ability of added factors", "weight": 1.0} -->

The time-series of $R^{2}$ is plotted in Figure 3. The predictive ability implied by the positive out-of-sample $R^{2}$ for the extended model is evidence that the added factors are present (equivalently evidence against the null). The average across time of the cross-replication mean $R^{2}$ is $0.0129$. The time periods when the extended model achieves the largest return $R^{2}$ gap to the base model (as shown in Figure 1) coincide with the periods of largest $R^{2}$ in Figure 3. The performance degrades in late 2023. This is a period when the extended model does not improve upon the base model, as shown in Figure 1.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

Every day $t$, we compute the normalized log-likelihood (i.e., log-likelihood divided by the number of assets) of the next return, $x_{t + 1}$, under our current model

<!-- chunk {"id": "body-0097", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

Given the series of returns, the best constant predictor (in terms of log-likelihood) is the empirical sample covariance

<!-- chunk {"id": "body-0098", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

with normalized log-likelihood $\ell_{t}{(\Sigma^{emp},x_{t + 1})}$. Here $\tau = 1$ corresponds to 2019-06-27 and $\tau = T$ corresponds to 2023-12-28. We therefore also report the difference

<!-- chunk {"id": "body-0099", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

This is a measure of regret and measures how much the covariance estimate underperforms the best possible constant covariance predictor. We want our covariance estimate to have small regret. Note that the regret can be negative, because our covariance is time-dependent, i.e., a time-dependent covariance can outperform $\Sigma^{emp}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

Our results are included in Table 2. We show both the average normalized log-likelihood and regret over the evaluation period, but also the standard deviation of these averages. The extended model obtains a lift in both log-likelihood and regret.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Log likelihood and regret", "weight": 1.0} -->

Std. of Average Log-Likelihood
Std. of Average Regret

<!-- chunk {"id": "body-0102", "role": "body", "section": "Whitened returns", "weight": 1.0} -->

For each risk model, we compute out-of-sample whitened returns and their empirical correlation matrix. We judge the risk model by the discrepancy between the empirical correlation matrix and the implied (by the risk model) correlation matrix of the whitened returns.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Whitened returns", "weight": 1.0} -->

We now collect the out-of-sample whitened returns ${\{{{\hat{\Sigma}}_{t}^{- {1/2}}x_{t + 1}}\}}_{t = 1}^{T}$ that should have the identity as the covariance under this hypothesis. We compute the Frobenius norm between the empirical correlation matrix ($n \times n$ matrix) of the whitened returns ${\{{{\hat{\Sigma}}_{t}^{- {1/2}}x_{t + 1}}\}}_{t = 1}^{T}$ and their theoretical correlation matrix assuming the risk model is true, i.e., the identity matrix $I$. We report the Frobenius norm for each risk model in Table 3, but normalized by $\sqrt{n{({n - 1})}}$. A larger normalized Frobenius norm indicates a greater discrepancy between the risk model and the covariance structure of the realized returns. The extended model achieves the best fit.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Whitened returns", "weight": 1.0} -->

(normalized) Frobenius norm of correlation matrix to identity

<!-- chunk {"id": "body-0105", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

We perform a similar procedure to the previous section, but instead of looking at out-of-sample whitened returns, we focus on out-of-sample whitened residuals. We describe our approach using an arbitrary risk model ${\hat{\Sigma}}_{t}$ for every time $t$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

At time $t$, we solve the out-of-sample ordinary least squares problem

<!-- chunk {"id": "body-0107", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

We assume that the risk model ${\hat{\Sigma}}_{t}$ holds for the returns, i.e., the returns follow

<!-- chunk {"id": "body-0108", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

We collect the out-of-sample whitened residuals

<!-- chunk {"id": "body-0109", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

and compute the Frobenius norm between the empirical correlation matrix of the out-of-sample whitened residuals and their theoretical correlation matrix under the assumption that the risk model holds, i.e., the identity $I$. For each of the risk models, we report the normalized (by $\sqrt{n{({n - 1})}}$) Frobenius norm in Table 4. A larger normalized Frobenius norm indicates a greater discrepancy between the risk model and the covariance structure of the realized returns. The extended model achieves the best statistical fit.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Whitened residuals", "weight": 1.0} -->

(normalized) Frobenius norm of correlation matrix to identity

<!-- chunk {"id": "body-0111", "role": "body", "section": "Discussion", "weight": 1.5} -->

We proposed a methodology to refine an available low-rank-plus-diagonal risk model and extend it with additional statistical factors. Our method is based on maximum likelihood estimation and is an instance of the expectation-maximization algorithm. This is particularly useful if the provided risk model is only infrequently updated, but we would like to incorporate information in shorter time horizons as well. We empirically show that this modification can improve the risk model's statistical fit even when the provided risk model is of high quality. Our approach is also able to handle missing returns data. However, we note that adding factors does not necessarily improve statistical fit. Furthermore, the effectiveness of our approach depends on the quality of the factors in the original risk model, namely the quality of the provided factor exposure matrix.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Discussion", "weight": 1.5} -->

We leave the problem of selecting the number of additional factors as future work, although we do note that a value in the range 2-10 typically worked well for a base risk model of roughly 70 factors. One simple approach for determining the number of additional factors is to evaluate out-of-sample $R^{2}$ and select the number of additional factors corresponding to the cutoff beyond which $R^{2}$ decreases. An important aspect not covered in this work is interpreting the added statistical factors. This can be done by looking at the cross-sectional correlation of the added factors with existing themes or by querying a large language model.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Discussion", "weight": 1.5} -->

We plan to combine our extension methodology with factor selection in the base model. This can be helpful if the base model has many factors, but only a few of them are relevant. We can reduce the number of base factors using, e.g., forward selection, and then apply our extension methodology to the reduced base model. We can also consider learning an $F_{2}$ with a specified range, if we wish to capture specific factors.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, we plan to construct portfolios via Markowitz optimization where we either use the extended or the base risk model for the asset return covariance. Preliminary results suggest that the extended model produces a Pareto frontier that dominates that of the base model in the space of realized returns and target volatilities.
