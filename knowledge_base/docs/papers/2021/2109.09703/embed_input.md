<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Forecast Dynamical Systems from Streaming Data

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Kernel analog forecasting (KAF) is a powerful methodology for data-driven, non-parametric forecasting of dynamically generated time series data. This approach has a rigorous foundation in Koopman operator theory and it produces good forecasts in practice, but it suffers from the heavy computational costs common to kernel methods. This paper proposes a streaming algorithm for KAF that only requires a single pass over the training data. This algorithm dramatically reduces the costs of training and prediction without sacrificing forecasting skill. Computational experiments demonstrate that the streaming KAF method can successfully forecast several classes of dynamical systems (periodic, quasi-periodic, and chaotic) in both data-scarce and data-rich regimes. The overall methodology may have wider interest as a new template for streaming kernel regression.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Forecasting problems are ubiquitous in physical science and engineering applications, including climate prediction, navigation, and medicine. In these settings, we do not possess complete information about the state of the system, and we may not have full knowledge of the equations of motion. Owing to our lack of omniscience, it is not possible to make predictions by integrating the current state forward in time. Instead, we may acquire training data by observing some aspect of the system's evolution. The goal is to build a compact model of the dynamics of this observable. Given a new observation, the model should allow us to forecast the future trajectory from the initial condition.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kernel analog forecasting (KAF) offers a promising approach to this problem. KAF is a data-driven, non-parametric forecasting technique that is best understood as a type of regularized kernel regression (Section 2). KAF emerged from recent efforts to translate Koopman operator theory into effective computational methodologies for forecasting (Section 2.7). The approach belongs to a rapidly expanding literature on operator-theoretic techniques for low-order modeling of dynamical systems, including methods based on kernels.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

KAF is mathematically rigorous, and it provides good-quality predictions for benchmark examples. Nevertheless, the straightforward implementation ("naïve KAF") has several weaknesses. First, naïve KAF requires multiple views of the training data, so it cannot operate in the "streaming" setting where we only see the training data once (Section 3.1). Second, the process of constructing the model is computationally expensive: to form the kernel matrix, the costs of arithmetic and storage are both quadratic in the length of the training data. Third, the basic method must store all of the training data to make predictions, so the forecasting model is quite large. Fourth, the arithmetic cost of a single forecast is linear in the amount of training data. These issues have limited the applicability of the KAF methodology.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In response to this challenge, we propose a novel streaming KAF algorithm (Section 3). Our approach depends on two prominent techniques from the field of randomized matrix computation: random Fourier features for kernel approximation and the randomized Nyström method for streaming PCA. Overall, the streaming KAF method builds a model using time and storage linear in the amount of training data, and it can make forecasts with time and storage that are independent of the amount of training data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computational experiments (Section 4) demonstrate that streaming KAF is a practical method for making predictions of two benchmark dynamical systems: Lorenz '63 (L63) and two-level Lorenz '96 (L96). In particular, streaming KAF exhibits forecasting skill similar to naïve KAF in a range of situations, including systems that are periodic, quasi-periodic, and chaotic. At the same time, streaming KAF can operate in settings where naïve KAF is prohibitively expensive, including cases where the observables are high-dimensional or the amount of training data is enormous. In the data-rich setting, after just a few minutes of training time, streaming KAF can drive the forecasting error toward zero. As a consequence, we believe that the streaming KAF algorithm has the potential to unlock the full potential of KAF as a forecasting methodology.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Remark 1.1 (Prior work)", "weight": 1.0} -->

Although developed independently, our methodology is related to recent papers that apply random features to perform streaming kernel principal component analysis and kernel ridge regression. The details of our algorithm are somewhat different from these works, and we believe that our work yields a novel approach for streaming kernel regression. We have also studied a streaming KAF algorithm based on AdaOja, an adaptive variant of Oja's algorithm, which is a competitive alternative to the Nyström method. See Section 5 for more discussion of related work.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Outline", "weight": 1.0} -->

Section 2 motivates the existing KAF procedure as a form of regularized kernel regression that is specifically designed for dynamical systems. Section 3 describes how to develop a streaming implementation of KAF. In particular, we discuss kernel approximation via random Fourier features and the randomized Nyström method. Finally, Section 4 presents computational experiments which demonstrate that our methodology is effective for two classical dynamical systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction to KAF", "weight": 1.5} -->

Suppose we have access to snapshots of a discrete dynamical system as it evolves in time, and we would like to forecast its future values. Let us begin with the most basic setting; we will discuss more general observation models in Section 2.6.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction to KAF", "weight": 1.5} -->

To formalize the problem, let $\mathcal{M} \subseteq {\mathbb{R}}^{d}$ be a closed subset of a Euclidean space. We call $\mathcal{M}$ the state space. Let $F:{\mathcal{M}\rightarrow\mathcal{M}}$ be a mapping, called the flow map.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction to KAF", "weight": 1.5} -->

In most settings, we do not actually know the flow map $F$. Rather, the goal is to use information latent in the measured trajectory $({\mathbf{x}}_{0},\ldots,{\mathbf{x}}_{n - 1})$ to infer the dynamics. Afterward, we are given a new initial condition ${\mathbf{y}} \in \mathcal{M}$, and we are asked to forecast the future state $F^{q}{({\mathbf{y}})}$ of the system after $q$ time steps.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear forecasting", "weight": 1.0} -->

To motivate the KAF method, we first describe an earlier approach to the forecasting problem, based on *linear inverse models* (LIMs) and the closely related dynamic mode decomposition (DMD). Fix a forecasting horizon $q \in {\mathbb{N}}$. We can arrange the observed trajectory ${{\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{n - 1},{\mathbf{x}}_{n},\ldots,{\mathbf{x}}_{{n + q} - 1}} \in {\mathbb{R}}^{d}$ into a training data set that consists of input--response pairs: ${\{{({\mathbf{x}}_{j},{\mathbf{x}}_{j + q})}\}}_{j = 0}^{n - 1}$. Equivalently, consider the pair of matrices

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear forecasting", "weight": 1.0} -->

An optimal solution to this problem is the matrix

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear forecasting", "weight": 1.0} -->

Let us manipulate the linear model for the dynamics so that it takes a more suggestive form. Recall that the pseudoinverse satisfies ${\mathbf{X}}^{\dagger} = {{({{\mathbf{X}}^{\top}{\mathbf{X}}})}^{\dagger}{\mathbf{X}}^{\top}}$. Therefore,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear forecasting", "weight": 1.0} -->

Given a new initial condition ${\mathbf{y}} \in {\mathbb{R}}^{d}$, we obtain the linear forecast

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear forecasting", "weight": 1.0} -->

Observe that this computation can be formulated in terms of inner products between states.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

Of course, dynamical systems of practical interest are highly nonlinear, so linear approximations are only valid over a short time horizon. When one needs to process data with nonlinear structure, a general principle is to "lift and linearize". That is, we apply a nonlinear map to transport the data to a high-dimensional space where it may have linear structure; we implement a linear fitting algorithm on the high-dimensional space; and then we project back down to the original domain to obtain a (nonlinear) low-dimensional model for the data. This approach gives rise to KAF, discussed below, as well as other data-driven analysis and forecasting techniques.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

Remarkably, this lifting technique can often be implemented without applying the nonlinear map explicitly. Consider a method, such as Eq. 6, that processes Euclidean data using the inner product as a measure of the similarity between data points. The kernel trick allows us to develop a nonlinear extension simply by replacing each inner product ${\mathbf{x}}^{\top}{\mathbf{y}}$ in the data space with a more general function $\kappa{({\mathbf{x}},{\mathbf{y}})}$, called a kernel.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

The kernel trick is justified by the Moore--Aronszajn theorem \[4, section 2\]. Let $\kappa:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$ be a symmetric, positive-definite function. That is,

<!-- chunk {"id": "body-0021", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

Implicitly, the feature map summarizes each data point $\mathbf{x}$ by a long list ${\varphi{({\mathbf{x}})}} \in \mathcal{H}$ of features, and the kernel computes the inner product between the feature vectors.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

One of the most popular kernel functions is the Gaussian radial basis function (RBF) kernel. For an inverse bandwidth parameter $\gamma > 0$, this kernel takes the form

<!-- chunk {"id": "body-0023", "role": "body", "section": "The kernel trick", "weight": 1.0} -->

Under this kernel, two points are "similar" precisely when they are close enough together in Euclidean distance, where the scale depends on the choice of $\gamma$. For clarity of presentation, we will work exclusively with the Gaussian RBF kernel in this paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Nonlinear kernel forecasting", "weight": 1.0} -->

We can apply the kernel trick to the linear forecasting model Eq. 6.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Nonlinear kernel forecasting", "weight": 1.0} -->

This step leads to the kernel analog forecast

<!-- chunk {"id": "body-0026", "role": "body", "section": "Nonlinear kernel forecasting", "weight": 1.0} -->

The forecast Eq. 8 provides a natural nonlinear generalization of the linear forecast Eq. 6.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Regularization", "weight": 1.0} -->

It is dangerous to implement the formula Eq. 8 as written because kernel matrices, such as ${\mathbf{K}}_{x,x}$, are notoriously ill-conditioned; for example, see. As a consequence, the method Eq. 8 can be sensitive to small changes in the observed data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Regularization", "weight": 1.0} -->

The paper proposes a mechanism for stabilizing the nonlinear forecast Eq. 8 by replacing the kernel matrix ${\mathbf{K}}_{x,x}$ with its best rank-$\ell$ approximation ${⟦{\mathbf{K}}_{x,x}⟧}_{\ell}$, where $\ell \in {\mathbb{N}}$ is a parameter. In practice, we must also shift the kernel matrix by $\mu\mathbf{I}$ by a small parameter $\mu$ to avoid numerical problems. These modifications leads to the stabilized kernel analog forecast

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regularization", "weight": 1.0} -->

The dimension $\ell$ of the regression model is usually modest (say, 100s or 1000s); it increases slowly with the required accuracy of the forecasts. The shift parameter $\mu$ is taken to be a small fixed value, such as $10^{- 6}\left\| {\mathbf{K}}_{x,x} \right\|$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regularization", "weight": 1.0} -->

The forecasting method Eq. 9 is rigorously justified. We can view the approach as a form of regularized least-squares on the feature space induced by the kernel. It is closely related to kernel ridge regression.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Resource usage", "weight": 1.0} -->

The KAF method Eq. 9 involves two phases. In the training step, we use the trajectory data $\mathbf{X}$ to compute a matrix of prediction weights. In the forecasting step, we use the trajectory data and the test state $\mathbf{y}$ to make the forecast. Let us summarize the resource usage of an uninspired implementation of the KAF procedure ("naïve KAF"). See Table 1 for a summary of this discussion.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Resource usage", "weight": 1.0} -->

In the training phase, we first construct the $n \times n$ kernel matrix ${\mathbf{K}}_{x,x}$. This step involves $O{({dn^{2}})}$ arithmetic and $O{(n^{2})}$ storage. The quadratic dependency on the number $n$ of training samples is a severe bottleneck that prevents us from performing KAF at scale.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Resource usage", "weight": 1.0} -->

Next, we must compute the $\ell$-truncated eigenvalue decomposition of the kernel matrix ${\mathbf{K}}_{x,x}$. Classical algorithms can succeed with $O{({\ell^{2}n})}$ arithmetic operations and $O{({\elln})}$ storage. Nevertheless, dense methods require random access to the kernel matrix, while Krylov methods require a long sequence of matrix--vector multiplies with the kernel matrix. Moreover, these algorithms are not fully reliable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Resource usage", "weight": 1.0} -->

Third, we form the matrix ${\mathbf{W}} ≔ {\mathbf{X}}_{\lbrack{+ q}\rbrack}{({⟦{\mathbf{K}}_{x,x} + \mu\mathbf{I}⟧}_{\ell})}^{\dagger} \in {\mathbb{R}}^{d \times n}$ of prediction weights. Using the factorized form of the eigenvalue decomposition, this product costs $O{({d\elln})}$ operations. The weight matrix requires storage $O{({dn})}$, which is comparable to the cost of storing the original trajectory data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Resource usage", "weight": 1.0} -->

To make a forecast from a single initial condition ${\mathbf{y}} \in {\mathbb{R}}^{d}$, we need to perform the kernel computation ${\mathbf{K}}_{x,y} \in {\mathbb{R}}^{n}$. The cost is $O{({dn})}$ operations and $O{(n)}$ storage. To complete the forecast, we form the matrix--vector product ${\mathbf{W}}{\mathbf{K}}_{x,y}$, at a cost of $O{({dn})}$ operations. The linear dependency on the number $n$ of training points means that forecasting is very expensive.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Other observables", "weight": 1.0} -->

The KAF methodology extends to a wider setting. Section 3 provides full details for a streaming KAF algorithm at this level of generality. For now, we just sketch the idea.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Other observables", "weight": 1.0} -->

Suppose that we observe the value of a function $u:{\mathcal{M}\rightarrow\mathcal{N}}$ of the state, which is called a covariate. For simplicity, we will always take $\mathcal{N} = {\mathbb{R}}^{d^{\prime}}$. Given an observed covariate $u{({\mathbf{x}})}$, we would like to predict a function $g:{\mathcal{M}\rightarrow{\mathbb{R}}^{r}}$ of the state $\mathbf{x}$, which is called a response variable. Functions of the state, such as $g$ and $u$, are called observables.^11^1It is important the the response variable $g$ takes values in a linear space. In principle, the covariates $u$ could take values in a nonlinear manifold $\mathcal{N}$, but we will not consider this extension.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Other observables", "weight": 1.0} -->

Replace the matrix ${\mathbf{X}}_{\lbrack q\rbrack}$ of lagged state data by the lagged matrix ${\lbrack{g{({\mathbf{x}}_{q})}},\ldots,{g{({\mathbf{x}}_{{n + q} - 1})}}\rbrack} \in {\mathbb{R}}^{r \times n}$ of observed response variables. Repeat the derivation above to obtain a KAF function $g_{\ell,q}$ for predicting the observable $g$ from the covariate $u$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Other observables", "weight": 1.0} -->

The computational costs are similar to the costs of the basic KAF method, but the state dimension $d$ is replaced by either the covariate dimension $d^{\prime}$ or the response variable dimension $r$, depending on the role of the state in the computation. See Table 2 for an accounting.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

The linear approach Eq. 6 to forecasting was originally proposed in the paper, and the nonlinear kernel forecast Eq. 8 was presented. The paper clarifies the connection between the nonlinear forecast and Koopman operator theory. The paper shows that KAF approximates the expectation of the response variable under the action of the Koopman operator, conditioned on the covariate data observed at forecast initialization. Here is an informal summary of these ideas.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

In plain language, the classical work of Koopman and von Neumann characterizes a dynamical system through its induced action on a *linear* space of observables. As a basic example, a real-valued function $g:{\mathcal{M}\rightarrow{\mathbb{R}}}$ on the state space is an observable of the dynamical system. The Koopman operator $\mathcal{K}$ is a linear operator on the space of observables that acts by composition with the flow map of the dynamics: ${{({\mathcal{K}g})}{({\mathbf{x}})}} ≔ {{({g \circ F})}{({\mathbf{x}})}} = {g{({F{({\mathbf{x}})}})}}$. Regardless of the complexity of the dynamical system, we can understand its behavior by spectral analysis of the linear operator $\mathcal{K}$ on an appropriately chosen Banach space of observables.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

In particular, since our state space $\mathcal{M}$ is a subset of ${\mathbb{R}}^{d}$, we can represent every state ${\mathbf{x}} \in \mathcal{M}$ by the "identity" observable, $\iota:{\mathcal{M}\rightarrow{\mathbb{R}}^{d}}$ with ${\iota{({\mathbf{x}})}} = {\mathbf{x}}$. Thus, the dynamical system becomes linear when lifted to a sufficiently high-dimensional space of observables: ${F{({\mathbf{x}})}} = {{({\mathcal{K}\iota})}{({\mathbf{x}})}}$. Using similar ideas, we can also represent dynamical systems with infinite-dimensional state spaces by means of linear Koopman operators.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

Building on previous work, the recent paper established that the stabilized forecast Eq. 9 is a rigorous approximation of the Koopman dynamics of observables in the limit of large data.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

We may construct the KAF function $g_{\ell,q}$ as summarized in Section 2.6. Let ${\mathbf{y}} \in \mathcal{M}$ be an initial condition with an observed covariate $u{({\mathbf{y}})}$. Then the kernel analog forecast converges^22^2Convergence takes place in the $L_{2}$ norm of the invariant measure in the iterated limit of $\ell\rightarrow\infty$ after $n\rightarrow\infty$, and almost surely with respect to the initial condition ${\mathbf{x}}_{0}$ in the training data.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Connection with Koopman operator theory", "weight": 1.0} -->

The conditional expectation is the optimal $L_{2}$ approximation to the Koopman evolution ${({\mathcal{K}^{q}g})}{({\mathbf{y}})}$, given only the measured covariate $\mathbf{v}$. In the specific case where the observables $g = u = \iota$ reproduce the full state vector, we deduce that the forecast $f_{q,\ell}{({\mathbf{y}})}$ presented in Eq. 9 converges to the true $q$-step dynamical evolution, $F^{q}{({\mathbf{y}})}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

While KAF is rigorously justified in the limit of large data, it also becomes prohibitively expensive to implement because of its storage and arithmetic costs (Section 2.5). Indeed, the time required to construct the kernel matrix is quadratic in the length $n$ of training data. The time required to make a single forecast is linear in $n$. Furthermore, we need multiple views of the training data to build the model and another view to make a forecast, so the algorithm cannot operate in the streaming setting.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

In this section, we will develop a streaming KAF method that resolves each of these issues. Our algorithm processes the trajectory data in a single pass. It reduces the arithmetic cost of training to be linear in the number $n$ of training points, and the cost of each forecast becomes independent of the amount of training data. It also limits the storage needed for the computations and for the forecasting model. Experiments (Section 4) show that the streaming KAF method is competitive with the original KAF method in forecasting skill on problem sizes where the original KAF method is tractable. But streaming KAF can achieve significantly better forecasts than naïve KAF because the streaming method can ingest large amounts of training data and resolve the dynamics more accurately.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Streaming data", "weight": 1.0} -->

Streaming data models have become popular for working with time series that have many elements, especially in high dimensions or in cases where the data arrives at high velocity. The key features of a streaming data model^33^3More general streaming models describe a sequence of update operations to a data domain. are that the elements of the time series are presented in sequential order; we must process each datum at the time it arrives; and we do not have sufficient storage to maintain the entire time series. The goal is to extract enough information to answer a particular set of questions about the observed data. These constraints necessitate algorithms that can handle each element individually and that build a compact representation of the time series to support subsequent queries.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Streaming data", "weight": 1.0} -->

Streaming models are well suited to dynamical systems data that has an explicit temporal order. It would be appealing to scan linearly through the trajectory data $({\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{n - 1})$ a single time, discarding each state after we have processed it. Our aim is to build a forecasting model that can take a query state and predict the subsequent trajectory of the system. Ideally, the forecasting model should be much smaller than the original training data. Yet the basic KAF method fails this desideratum. We will show how to accomplish this task.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Overview", "weight": 1.0} -->

Our streaming KAF method is based on two techniques from the field of randomized matrix computations. First, we use random Fourier features (RFF) to build a structured approximation of the original kernel function. This approximation allows us to rewrite the KAF target function Eq. 8, replacing the $n \times n$ kernel matrix ${\mathbf{K}}_{x,x}$ by a much smaller matrix that is easier to compute and captures the same information. This reformulation also allows us to avoid the kernel computation ${\mathbf{K}}_{x,y}$, which couples the training and test data. As a consequence, we can build a more compact forecasting model.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Overview", "weight": 1.0} -->

When we restructure the KAF target function, the low-rank approximation of the kernel matrix converts into a low-rank approximation of the covariance matrix of the features of the training data. The latter approximation may be interpreted as a streaming PCA problem. Here, we employ the randomized Nyström method devised by Halko et al. and extended to the streaming setting. This algorithm requires minimal storage and arithmetic, and it reliably produces a more accurate solution than competing methods.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Overview", "weight": 1.0} -->

The rest of this section introduces the random features construction. It shows how to integrate random features into KAF to obtain a streaming algorithm, and it highlights the role of the Nyström method. Last, we compare the resource usage of streaming KAF with the direct implementation of KAF. See Section 5 for related work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

Random Fourier features (RFF) offer a simple and effective way to approximate certain types of kernels, including the Gaussian RBF kernel. This section summarizes the RFF construction, and the next section explains how we can use RFF to forecast a dynamical system.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

Bochner's theorem provides the mathematical foundation for RFF. Let us consider a bounded, continuous, positive-definite kernel $\kappa:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$ on a Euclidean space. Assume that the kernel is also translation invariant: ${\kappa{({\mathbf{x}},{\mathbf{y}})}} ≔ {h{({{\mathbf{x}} - {\mathbf{y}}})}}$. The theorem asserts that the kernel is the Fourier transform of a bounded positive measure. More precisely, there exists a unique probability measure $\nu$ on ${\mathbb{R}}^{d}$ and a positive constant $c ≔ {h{(\mathbf{0})}}$ for which

<!-- chunk {"id": "body-0055", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

where ^∗^ denotes the complex conjugate.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

This statement follows by direct calculation using trigonometric identities. The key property of these formulas is that the integrand is a separable function of the variables $\mathbf{x}$ and $\mathbf{y}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

The simple idea behind RFF is to approximate the kernel using a Monte Carlo estimate of the integral. Let the parameter $s \in {\mathbb{N}}$ designate the number of random features. Once and for all, draw and fix independent random vectors ${{\mathbf{z}}_{1},\ldots,{\mathbf{z}}_{s}} \in {\mathbb{R}}^{d}$ that are distributed according to the probability measure $\nu$. Draw and fix independent random scalars ${\theta_{1},\ldots,\theta_{s}} \in {\mathbb{R}}$ with the $\text{uniform}{\lbrack 0,{2\pi})}$ distribution.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

Equivalently, we may define a feature map $\varphi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{s}}$ by the formula

<!-- chunk {"id": "body-0059", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

In other words, the approximate kernel is a bilinear function of nonlinear features.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

In computational settings, we are usually interested in approximating the kernel matrix ${\mathbf{K}}_{x,x}$ associated with a family ${\{{\mathbf{x}}_{0},\ldots,{\mathbf{x}}_{n - 1}\}} \subset {\mathbb{R}}^{d}$ of data points. That is,

<!-- chunk {"id": "body-0061", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

To this end, we collect the data points as the columns of a matrix ${\mathbf{X}} \in {\mathbb{R}}^{d \times n}$. Extend the feature map $\varphi$ to matrices by applying the vector feature map to each column. Thus, $\varphi:{{\mathbb{R}}^{d \times n}\rightarrow{\mathbb{R}}^{s \times n}}$. With this notation, we find that

<!-- chunk {"id": "body-0062", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

The kernel matrix approximation is the Gram matrix of the nonlinear features.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

Finally, we must discuss the number $s$ of random features that we need to ensure that the kernel matrix approximation ${\hat{\mathbf{K}}}_{x,x}$ serves in place of the true kernel matrix ${\mathbf{K}}_{x,x}$ for machine learning tasks. When we have $n$ training points, it has been shown that it suffices to use

<!-- chunk {"id": "body-0064", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

for kernel principal component analysis (KPCA) or for kernel ridge regression (KRR). The justification involves statistical assumptions on the training and test data. Our empirical study indicates that, in our application, we may extract even fewer features without much loss in forecasting performance.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

As a particular example of the RFF construction, consider the Gaussian RBF kernel Eq. 7 on ${\mathbb{R}}^{d}$ with inverse bandwidth $\gamma > 0$. The normalization constant $c = 1$, and the associated spectral measure $\nu$ satisfies

<!-- chunk {"id": "body-0066", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

That is, the random feature descriptor $\mathbf{z}$ is a centered normal vector with covariance ${({2\gamma})}\mathbf{I}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Kernel approximation by random features", "weight": 1.0} -->

Algorithm 1 contains basic pseudocode for implementing Gaussian RBF random features. In this version, the feature descriptors require $O{({ds})}$ storage, and it costs $O{({ds})}$ operations to compute the features for a single input vector. The pseudocode also includes several methods for streaming computation of matrix--matrix products with featurized data $\varphi{({\mathbf{X}})}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 3.1 (More efficient Gaussian feature maps)", "weight": 1.0} -->

We can accurately approximate the RFF map for the Gaussian RBF kernel using randomized trigonometric transforms. This construction reduces the storage cost for the random feature descriptors to $O{(s)}$, and it costs $O{({s{\log d}})}$ operations to compute the features of a single input vector. For high-dimensional state spaces (or covariates), we can obtain significant gains, but the basic construction is superior in low-dimensional settings.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.2 (Kernels that admit random feature maps)", "weight": 1.0} -->

It is also possible to construct random features for other kinds of kernel functions, including kernels that are not translation invariant. See \[57, Sec. 19\] for some discussion and references.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 3.2 (Kernels that admit random feature maps)", "weight": 1.0} -->

The constructor (RFF) generates a random feature map φ for the Gaussian RBF kernel on ℝd with inverse bandwidth γ &gt; 0 with s random features.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 3.2 (Kernels that admit random feature maps)", "weight": 1.0} -->

The Featurize method of φ applies the random feature map to the columns of the input matrix X ∈ ℝd × B to obtain φ (X) ∈ ℝs × B. The other methods featurize an input matrix X ∈ ℝd × B and compute various matrix products between φ (X) and another input M by streaming columns of X. 1local variables γ ∈ ℝ++ and d, s ∈ ℕ ⊳ RFF parameters 2local variables z1, …, zs ∈ ℝd and θ1, …, θs ∈ ℝ ⊳ Feature descriptors 3function RFF(γ ∈ ℝ++, d ∈ ℕ; s ∈ ℕ) ⊳ Initialization 4 Store RFF parameters γ, d; s 6 ${\mathbf{z}}_{i}\leftarrow{{\sqrt{2\gamma} \cdot \text{randn}}{(d,1)}}$ ⊳ Draw Gaussian vector 7 θi ← 2 π ⋅ rand ⊳ Draw uniform scalar 8 return self ⊳ Return feature map 9function Featurize(X ∈ ℝd × B) ⊳ Compute features of X 12

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 3.2 (Kernels that admit random feature maps)", "weight": 1.0} -->

${\lbrack{\varphi{({\mathbf{X}})}}\rbrack}_{ij}\leftarrow{\sqrt{2/s} \cdot {\cos{({\theta_{i} + {{\mathbf{z}}_{i}^{\top}{\mathbf{X}}{(:,j)}}})}}}$ 14function MultCov(X ∈ ℝd × B, M ∈ ℝs × ℓ) ⊳ Form product φ (X) φ (X)⊤ M 16 for j = 1, …, B do ⊳ Block for efficiency 17 v ← Featurize (X (:,j)) ⊳ Compute features 20function RMultAdj(X ∈ ℝd × B, M ∈ ℝr × B) ⊳ Form product M φ (X)⊤ 22 for j = 1, …, B do ⊳ Block for efficiency 25function RMult(X ∈ ℝd × B, M ∈ ℝr × s) ⊳ Form product M φ (X) 27 for j = 1, …, B do ⊳ Block

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3.2 (Kernels that admit random feature maps)", "weight": 1.0} -->

for efficiency Algorithm 1 Random Fourier Features for Gaussian RBF Kernel. See Section 3.3.

<!-- chunk {"id": "body-0074", "role": "body", "section": "KAF with random features", "weight": 1.0} -->

We can use RFF to approximate the kernel matrices that appear in the regularized KAF target function Eq. 9. Recall that the matrix ${\mathbf{X}} \in {\mathbb{R}}^{d \times n}$ contains the training data, while ${\mathbf{y}} \in {\mathbb{R}}^{d}$ is a piece of test data. Draw and fix a random feature map $\varphi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{s}}$ with $s$ random features. Then we can approximate the KAF as

<!-- chunk {"id": "body-0075", "role": "body", "section": "KAF with random features", "weight": 1.0} -->

The forecasting model consists of the matrix ${\mathbf{W}}_{q,\ell} \in {\mathbb{R}}^{d \times s}$ of prediction weights, along with the description of the feature map $\varphi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{s}}$. A key benefit of the reformulation Eq. 11 is the complete decoupling of the test data $\mathbf{y}$ from the forecasting model.

<!-- chunk {"id": "body-0076", "role": "body", "section": "KAF with random features", "weight": 1.0} -->

Direct substitution of random features does not lead immediately to a streaming algorithm. Indeed, the formula Eq. 11 involves the rank truncation of the $n \times n$ approximate kernel matrix $\varphi{({\mathbf{X}})}^{\top}\varphi{({\mathbf{X}})}$. We cannot form this matrix without multiple views of the columns of $\mathbf{X}$, and the matrix imposes unacceptable storage and arithmetic costs.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

To develop a streaming algorithm, we first recast the expression Eq. 11 in terms of a much smaller $s \times s$ matrix. Recall the linear-algebraic identity

<!-- chunk {"id": "body-0078", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

Using this formula, we can write the prediction weights as

<!-- chunk {"id": "body-0079", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

The matrices in parentheses have the dimensions $d \times s$ and $s \times s$, respectively. Moreover, this representation now supports a streaming algorithm.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

In sequence, we pass over the columns ${\mathbf{x}}_{i}$ of the training states, generating random features $\varphi{({\mathbf{x}}_{i})}$ on the fly. Simultaneously, we update the covariance of the features and the covariance between the features and the lagged data. Beginning with ${\mathbf{C}}_{xx} = \mathbf{0}_{s \times s}$ and ${\mathbf{C}}_{gx} = \mathbf{0}_{d \times s}$, iterate

<!-- chunk {"id": "body-0081", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

\[Because of the lag, to form the matrix ${\mathbf{C}}_{gx}$, the algorithm must buffer the input states at a cost of $O{({qd})}$.\] Once we have streamed all of the training data, we may construct the matrix of prediction weights as

<!-- chunk {"id": "body-0082", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

Since the expressions for the weights in Eqs. 11, 12, and 14 are algebraically equivalent, we have arrived at a streaming implementation of KAF with random features.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

The general recommendation Eq. 10 for the number $s$ of random features may not be appropriate for the streaming setting because $s$ depends on the number $n$ of training samples.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Streaming KAF", "weight": 1.0} -->

In other words, the number $s$ of features can be proportional to the dimension $\ell$ of the regression model, which is chosen in advance.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

To complete the description of our streaming KAF algorithm, we must provide an efficient method for computing a low-rank approximation of the feature covariance matrix ${\mathbf{C}}_{xx}$ appearing in Eq. 13.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

Evidently, ${\mathbf{C}}_{xx}$ is the covariance of vectors that are presented to us sequentially. Therefore, the low-rank approximation ${⟦{\mathbf{C}}_{xx} + \mu\mathbf{I}⟧}_{\ell}$ amounts to a streaming PCA problem. We will perform this computation using the randomized Nyström method; see Section 5 for a short discussion of alternatives.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

The Nyström approximation of a positive-semidefinite (psd) matrix ${\mathbf{C}} \in {\mathbb{R}}^{s \times s}$ with respect to a test matrix $\mathbf{\Omega} \in {\mathbb{R}}^{s \times k}$ is the best psd approximation with the same range as ${\mathbf{C}}\mathbf{\Omega}$. The construction dates back to the early literature on integral equations; it is intimately connected to Schur complements and Cholesky factorization. The randomized Nyström approximation involves a test matrix $\mathbf{\Omega}$ chosen at random.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

We can implement randomized Nyström approximation in the streaming setting. Draw and fix a random matrix $\mathbf{\Omega} \in {\mathbb{R}}^{{s \times 2}\ell}$ from the standard normal distribution.^44^4It is important that the random matrix $\mathbf{\Omega}$ has $2\ell$ columns, not merely $\ell$. Instead of forming ${\mathbf{C}}_{xx}$ as in Eq. 13, we compute the product ${\mathbf{B}} = {{\mathbf{C}}_{xx}\mathbf{\Omega}} \in {\mathbb{R}}^{s \times \ell}$ via the iteration

<!-- chunk {"id": "body-0089", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

After we have streamed all of the data, we carefully^55^5Do not use the formula Eq. 16 as written! See Algorithm 2.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

The randomized Nyström approximation ${\check{\mathbf{C}}}_{xx}$ provides a good low-rank approximation of the covariance ${\mathbf{C}}_{xx}$; see \[78, Thms. 4.1--4.2\]. Our ultimate formula for the weight matrix becomes

<!-- chunk {"id": "body-0091", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

Algorithm 2 provides numerically stable pseudocode for the randomized Nyström method applied to a sequence of random features. This method is based.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Streaming PCA", "weight": 1.0} -->

Using ordinary Gaussian random features, the arithmetic cost of forming the matrix $\mathbf{B}$ is $O{({{({\ell + d})}sn})}$. The algorithm uses auxiliary arithmetic $O{({\ell^{2}s})}$, and the storage requirement is just $O{({\ells})}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark 3.3 (Powering)", "weight": 1.0} -->

The randomized Nyström method always underestimates the eigenvalues of the covariance matrix. If necessary, we can reduce this effect by incorporating powering or Krylov subspace techniques. In the streaming setting, these modifications require us to construct and store the full covariance matrix $\mathbf{C}_{xx}$. In our numerical work, these refinements did not improve the quality of forecasting, but they may merit further study.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark 3.3 (Powering)", "weight": 1.0} -->

Given a random feature map feat and a data matrix X ∈ ℝd × n, this procedure computes an ℓ-truncated eigenvalue decomposition Q Λ Q⊤ of the covariance Cx x = φ (X) φ (X)⊤ of the featurized data using the randomized Nyström method with 2× oversampling.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Remark 3.3 (Powering)", "weight": 1.0} -->

1function FeatNyström(RFF feat, X ∈ ℝd × n, ℓ ∈ ℕ))
2 Q ← orth (randn (s,2 ℓ)) ⊳ Random subspace, oversampling ℓ → 2 ℓ
3 Z ← feat.MultCov (X,Q) ⊳ Stream the product φ (X) φ (X)⊤ Q
4 ν ← eps (∥Z∥F) ⊳ Compute shift
5 Z ← Z + ν Q ⊳ Shift for stability
6 T ← chol (Q⊤ Z) ⊳ Upper-triangular Cholesky factorization
7 S ← Z/T ⊳ Solve triangular systems
8 (Q,Σ,∼) ← svd (S) ⊳ Compact SVD
9 Λ ← max {0, Σ2 − ν I} ⊳ Remove shift to get eigenvalues
10 Q ← Q(:,1:ℓ) and Λ ← Λ(1:ℓ,1:ℓ) ⊳ Truncate to rank ℓ
Algorithm 2 Randomized Nyström for featurized data [57, Sec. 19.4.3]. See Section 3.6.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Other observables", "weight": 1.0} -->

We can easily extend streaming KAF to the more general setting outlined in Section 2.6. Suppose we wish to use a general covariate $u:{\mathcal{M}\rightarrow{\mathbb{R}}^{d^{\prime}}}$ to predict a general response variable $g:{\mathcal{M}\rightarrow{\mathbb{R}}^{r}}$ after $q$ time steps. Let $\overset{\sim}{\kappa}:{{\mathbb{R}}^{d^{\prime} \times d^{\prime}}\rightarrow{\mathbb{R}}_{+}}$ be a positive-definite kernel on the covariate space, with associated feature map $\overset{\sim}{\varphi}:{{\mathbb{R}}^{d^{\prime}}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Other observables", "weight": 1.0} -->

To train, we acquire data in the form of measured values of the covariate paired with measured values of the lagged response: $({\mathbf{u}}_{i},{\mathbf{g}}_{q + i})$ where ${\mathbf{u}}_{i} = {u{({\mathbf{x}}_{i})}}$ and ${\mathbf{g}}_{i} = {g{({\mathbf{x}}_{i})}}$ for $i = {0,\ldots,{n - 1}}$. In this setting, the underlying state trajectory $({\mathbf{x}}_{0},\ldots,{\mathbf{x}}_{n - 1})$ is unknown. By streaming the observable data, we compute the matrices

<!-- chunk {"id": "body-0098", "role": "body", "section": "Other observables", "weight": 1.0} -->

As before, the randomized Nyström method serves for the streaming PCA computation.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Other observables", "weight": 1.0} -->

Our approach gives a principled approximation of the optimal forecast of the response given the observed covariate, as described in Section 2.7.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Resource usage", "weight": 1.0} -->

Algorithm 3 lists pseudocode for the general streaming KAF method outlined in Section 3.7. Table 1 compares the costs against a naïve implementation of KAF. We also list the costs of streaming KAF with fast random features (Fast Streaming KAF; see Remark 3.1. ‣ 3.3 Kernel approximation by random features ‣ 3 Streaming KAF ‣ Learning to Forecast Dynamical Systems from Streaming DataSubmitted to the editors DATE. \fundingDG acknowledges support from NSF DMS 1854383 and ONR MURI N00014-19-1-242. AH was funded by AFOSR MURI FA9550-19-1-0005, NSF DMS 1952735. JAT was supported by ONR N00014-18-1-2363 and NSF DMS 1952777. RW acknowledges support from AFOSR MURI FA9550-19-1-0005, NSF DMS 1952735, and NSF IFML 2019844.")), omitting an exposition.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Resource usage", "weight": 1.0} -->

First, we discuss the costs of the training step of streaming KAF with covariate data ${\mathbf{X}} \in {\mathbb{R}}^{d^{\prime} \times n}$ and (lagged) observable data ${\mathbf{G}} \in {\mathbb{R}}^{r \times n}$. Assume that the truncation rank $\ell \leq s$, where $s$ is the number of random features.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Resource usage", "weight": 1.0} -->

To construct random feature descriptors, we draw and store $O{({d^{\prime}s})}$ normal random variables. The Nyström approximation of the featurized covariance matrix involves $O{({{({d^{\prime} + \ell})}sn})}$ arithmetic and local storage $O{({\ells})}$. The covariate--response matrix requires $O{({{({d^{\prime} + r})}sn})}$ arithmetic and storage $O{({rs})}$. To form the prediction weights, we expend $O{({\ellrs})}$ arithmetic and $O{({rs})}$ storage. In practice, the Nyström approximation is the most expensive step.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Resource usage", "weight": 1.0} -->

The total storage required for the forecasting model consists of the $O{({d^{\prime}s})}$ storage for the random feature descriptors and the $O{({rs})}$ storage for the prediction weights.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Resource usage", "weight": 1.0} -->

In the forecasting step, we simply featurize the test data and form a matrix--matrix product. This step uses $O{({{({d^{\prime} + r})}s})}$ arithmetic per initial condition (IC), but no additional storage.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Resource usage", "weight": 1.0} -->

Let us summarize. In comparison with naïve KAF, the streaming KAF method is significantly faster because it is a streaming method. The precise improvements to storage and arithmetic costs depend on several parameters. Loosely, the streaming method reduces training arithmetic by a factor of about $n/s$ and reduces training storage by a factor of about $n^{2}/s$. For forecasting, the arithmetic and storage both decrease by a factor of $n/s$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Remark 3.4 (Implementation)", "weight": 1.0} -->

For reasons of modularity, the pseudocode and our prototype implementation take two passes over the data, but they are mathematically equivalent to the streaming KAF algorithm.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 3.4 (Implementation)", "weight": 1.0} -->

The method Train takes covariate data X ∈ ℝd × n and (lagged) response data G ∈ ℝr × n as input. It constructs a random feature map with parameters (γ,d;s) and builds a forecasting model for the response data G using truncation rank ℓ ∈ ℕ. The method Forecast uses the model to make estimates of the response from the covariates listed as columns of Y ∈ ℝd × m.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 3.4 (Implementation)", "weight": 1.0} -->

1local variables RFF feat ⊳ Random feature map φ: ℝd → ℝs 2local variables W ∈ ℝr × s ⊳ Prediction weights 4 feat ← RFF (γ,d;s) ⊳ Initialize random feature map 5 (Q,Λ) ← FeatNyström (feat,X;ℓ) ⊳ Factor ⟦φ(X)φ(X)⊤⟧ℓ; see Section 3.6 6 Λ ← Λ + μ max (Λ) ⋅ I ⊳ Filter eigenvalues; μ = 10−6 7 C ← feat.RMultAdj (X,G) ⊳ Form product G φ (X)⊤ ∈ ℝr × s 8 W ← ((C Q)/Λ) Q⊤ ⊳ Compute prediction weights 10 ${\hat{\mathbf{F}}\leftarrow\text{feat}}.{\text{RMult}{({\mathbf{Y}},{\mathbf{W}})}}$ ⊳ Form W φ (Y) 11 return $\hat{\mathbf{F}} \in {\mathbb{R}}^{d \times m}$ ⊳ Forecasts for columns of Y Algorithm

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 3.4 (Implementation)", "weight": 1.0} -->

3 Scalable Kernel Analog Forecasting. Implements Section 3.7.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section showcases experiments that demonstrate the practical performance of streaming KAF. We study forecasting skill for several benchmark dynamical systems, we investigate sensitivity to algorithm parameters, and we make comparisons with the naïve implementation of KAF. The code for reproducing the experiments is available as a supplement to this paper.

<!-- chunk {"id": "body-0111", "role": "body", "section": "The Lorenz models", "weight": 1.0} -->

Our experiments focus on the Lorenz '63 model, a classical three-dimensional dynamical system known to exhibit chaotic behavior. We also test the method on the two-phase Lorenz '96 model, a higher-dimensional system that has periodic, quasi-periodic, and chaotic regimes. This subsection summarizes the models and the parameters that give rise to different types of dynamics.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Lorenz '63", "weight": 1.0} -->

The Lorenz '63 (L63) model was introduced by Edward Lorenz in 1963 as a crude model of atmospheric convection. Although this example is simple, its properties have been studied extensively, and it is known to exhibit many of the features that make forecasting challenging in more complex systems, including fractal attractors and mixing dynamics.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Lorenz '63", "weight": 1.0} -->

The L63 model is defined via the following system of differential equations. For a state ${\mathbf{x}} = {(x_{1},x_{2},x_{3})} \in {\mathbb{R}}^{3}$,

<!-- chunk {"id": "body-0114", "role": "body", "section": "Lorenz '63", "weight": 1.0} -->

The classical parameters for the L63 system that generate chaotic dynamics are ${(\sigma,\mu,\beta)} = {(10,28,{8/3})}$. This choice leads to the famous "butterfly attractor," a compact set in ${\mathbb{R}}^{3}$ with fractal dimension $\approx 2.06$ that supports an ergodic invariant measure with Lyapunov exponent $\lambda \approx 0.91$; see. Figure 1 presents an illustration.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Lorenz '96", "weight": 1.0} -->

We also consider the two-phase Lorenz '96 system (L96), as introduced. This model has dynamics that occur on two distinct timescales, a set of "slow variables" ${\mathbf{x}} = {\{{x{(k)}}\}}_{k \in {\lbrack K\rbrack}}$ and a set of "fast variables" ${\mathbf{z}} = {\{{z{(j,k)}}\}}_{{j \in {\lbrack J\rbrack}},{k \in {\lbrack K\rbrack}}}$. These variables evolve according to the following system of equations.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Lorenz '96", "weight": 1.0} -->

As, we set the parameters ${(h_{x},h_{y},K,J,\varepsilon)} = {({- 0.8},1,9,8,{1/128})}$. Depending on the value of the forcing constant $F$, three distinct regimes of behavior emerge.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Lorenz '96", "weight": 1.0} -->

See Fig. 1 for typical trajectories.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Lorenz '96", "weight": 1.0} -->

In our experiments, we seek to forecast the future values of the slow variables ${x{}},\ldots,{x{}}$ of the coupled system using only the slow variables as input data. This setup is motivated by the experiments of, which studied KAF for multi-scale systems but did not investigate the scalability as a function of the amount of training data.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

All of our experiments are performed using data obtained by integrating the governing equations of the L63 and L96 systems. Here are the details about how we apply streaming KAF to make forecasts and evaluate the results.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where $F$ is the flow map obtained by discretizing Eq. 19 with time step ${dt} =.01$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where $F$ is the flow map obtained by discretizing Eq. 20 with time step ${dt} =.01$. We then form the training matrix ${\mathbf{X}} = {\lbrack{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{n}\rbrack} \in {\mathbb{R}}^{9 \times n}$ using only the slow variables.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

To evaluate the performance, we use the normalized root mean square error (RMSE) metric for the forecast error.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the forecast $f_{q,\ell,i^{\ast}}$ of the response variable, applied columnwise, we define the error

<!-- chunk {"id": "body-0124", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where ${std}{({\mathbf{z}})}$ denotes the standard deviation of the vector $\mathbf{z}$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For each system and each set of parameter specifications, we consider $5$ sets of tests ${\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{5}$, each with $m = {10,000}$ data points (columns) of the same form as the training data. The first test data set ${\mathbf{Y}}_{1}$ is obtained by evolving the system from the final point ${\mathbf{x}}_{n}$ in the training data. For the remaining test sets, the initial condition is the final point in the previous set. In all figures, the line series represents the average of the errors resulting from each of the $5$ tests, and the shaded region around the error lines represents one standard deviation of uncertainty around the average.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

In each of the plots presented in sections 4.4 and 4.5, the kernel inverse bandwidth $\gamma$ and dimension of regression model $\ell$ are fixed as the size of the training data $n$ increases. For any particular plot in these sections, the values of $\gamma$ and $\ell$ were chosen based on a minimal amount of manual tuning at fixed training sample size $n = {10,000}$. As such, the corresponding error curves level off as $n$ is increased from $10,000$ to $50,000$. Principled approaches to setting the inverse bandwidth parameter $\gamma$ and dimension of regression model $\ell$ are discussed in sections 4.6.1 and 4.6.2, respectively.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Table 2 illustrates that gently increasing the inverse bandwidth $\gamma$ and regression model dimension $\ell$ together as the size of the training data $n$ increases serves as a good rule of thumb for improving the streaming KAF accuracy with increasing $n$. Table 3 indicates that the number of random features $s$ can be taken to be proportional to $\ell$, resulting in faster forecasting and incurring only a small loss in accuracy.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

As presented in Algorithm 3, streaming KAF is implemented with two passes over the training data, but it is algebraically equivalent to a true streaming method. We use ordinary Gaussian random features (rather than the "fast" variant). All the loops in Algorithm 1 are vectorized with blocks of $1,000$ vectors. We employ the randomized Nyström method described in Algorithm 2.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

The algorithms were implemented using the MATLAB programming language. All data was collected on a MacBook Pro with 16 GB of RAM and with an 8-Core Intel Core i9 Processor, clocked at 2.3 GHz.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Interpreting the results", "weight": 1.0} -->

The normalized RMSE Eq. 21 provides a measure of the quality of the forecast. When the normalized RMSE reaches $1$, the expected square error is equal to the standard deviation of the response observable with respect to the invariant measure, and the forecast is no longer providing useful information.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Interpreting the results", "weight": 1.0} -->

In dynamical systems, the maximal Lyapunov exponent of a system is commonly used to summarize the level of "unpredictability." The paper describes the intuitive meaning of this exponent: "For a chaotic trajectory, an infinitesimal perturbation in the evolution gives rise to exponential divergence---the Lyapunov exponent expresses the rate of divergence." Hence, Lyapunov time is frequently used as a horizon for forecasting. Typically, a forecast is classified as "good" if the normalized RMSE only approaches 1 after several Lyapunov timescales.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Interpreting the results", "weight": 1.0} -->

For the L63 system, the Lyapunov exponent $\lambda \approx 0.91$. Thus, we can expect to make nontrivial forecasts of the state vector for several time units. On all L63 plots, we mark the Lyapunov time scale as a yardstick. Note that there are other observables that remain predictable for much longer than the coordinates of the state vector.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Case study: L63", "weight": 1.0} -->

Our first experiment compares the forecasting skill of naïve KAF and scalable KAF for the L63 system. Figure 2 explores how forecasts of the first state coordinate $i^{\ast} = 1$ improve as the number $n$ of training samples increases. With $n = {10,000}$, both methods provide good predictions, with streaming KAF slightly better than naïve KAF. In particular, both algorithms can make informative forecasts over several Lyapunov time intervals. As we will discuss in Section 4.7, the streaming method is far more efficient, and the naïve method was unable to construct a forecasting model when $n = {50,000}$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Case study: L63", "weight": 1.0} -->

The KAF methodology has similar success at forecasting all three state variables. For each of the three variables and with $n = {10,000}$ training samples, Fig. 3 compares the forecasting error attained by the naïve and streaming methods.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Case Study: L96", "weight": 1.0} -->

In our second set of experiments, we explore the performance of scalable KAF for the L96 system in the periodic, quasi-periodic, and chaotic regimes documented. An increase in the forcing constant $F$ generates more chaotic behavior and, unsurprisingly, reduces the time horizon for which KAF can make informative forecasts.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Case Study: L96", "weight": 1.0} -->

For the periodic regime ($F = 5$), forecasting is quite easy. Figure 4 illustrates the performance of streaming KAF as a function of the number $n$ of training samples. The success of the method hardly varies as we increase $n$ from $5,000$ to $20,000$, and the RMSE remains quite small over long time scales.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Case Study: L96", "weight": 1.0} -->

For the quasi-periodic regime ($F = 6.9$), the forecasting problem becomes more challenging. For $n = {10,000}$ training samples, Fig. 5 shows that the naïve and streaming methods have similar forecasting performance for the first three slow variables. As we anticipate, the RMSE increases gradually with time. Figure 4 displays the performance of streaming KAF as a function of the number $n$ of training samples. In this case, an increase in the number of samples from $n = {10,000}$ to $n = {50,000}$ improves the performance moderately. Note that the naïve approach cannot benefit from the larger training set because it does not scale to input of this size.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Case Study: L96", "weight": 1.0} -->

Last, we consider the chaotic regime ($F = 10$), where the forecasting problem is hard. Figure 6 indicates the naïve and streaming methods produce comparable forecasting results. In both cases, the RMSE increases quite quickly. Figure 4 shows that streaming KAF can build models from an increasing number $n$ of training samples, and it can attain an advantage from the larger training set.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Case Study: L96", "weight": 1.0} -->

We conclude that streaming KAF and naïve KAF have similar forecasting skill in all three regimes, even though the streaming method makes several approximations. At the same time, streaming KAF is far more economical, so it can exploit larger sets of training data and thereby construct more accurate models.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Hyperparameter specifications and sensitivity", "weight": 1.0} -->

The streaming KAF method involves several hyperparameters: the kernel inverse bandwidth $\gamma$, the dimension $\ell$ of the regression model, and the number $s$ of random features. We performed a collection of experiments with the L63 and L96 data to gauge how much the hyperparameters affect the quality of forecasts.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Kernel bandwidth", "weight": 1.0} -->

The inverse bandwidth parameter $\gamma$ of the Gaussian RBF kernel is a notorious hyperparameter that can have a significant impact on the performance of kernel methods. One basic methodology for selecting the bandwidth is the median rule, which sets $\gamma^{- {1/2}}$ to be the median pairwise distance among elements of a subsample from the dataset. Other quantiles of the pairwise distance, such as the 0.1 and 0.9 quantiles, are sometimes employed. A different approach for bandwidth tuning leverages scaling relationships between the element sum of the $n \times n$ kernel matrix ${\mathbf{K}}_{x,x}$ and $\gamma$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Kernel bandwidth", "weight": 1.0} -->

In our experience, the KAF methodology is robust to the choice of inverse bandwidth parameter in all problem regimes. Indeed, the forecasting performance is similar over several orders of magnitude, but tuning can have a modest effect. See Fig. 7 for an illustration. To obtain better models from large training data, we invoke scaling laws for the bandwidth.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

To implement streaming KAF, we must choose the dimension, or rank, $\ell$ of the regression model. When $\ell$ is too small, the model does not capture all of the dynamics. Meanwhile, when $\ell$ is too large, we can introduce noise dimensions or encounter numerical problems. In this section, we outline some strategies for this task, and we will show that the forecasting methodology is robust to the choice of this parameter.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

One principled approach is to form the full covariance matrix ${\mathbf{C}}_{xx} \in {\mathbb{R}}^{s \times s}$ or ${\mathbf{C}}_{uu} \in {\mathbb{R}}^{s \times s}$ of the covariate data. In this case, we can explicitly compute the eigenvalues $(\lambda_{1},\lambda_{2},\ldots,\lambda_{s})$ of the matrix. Then, we choose the truncation level $\ell$ so that we capture, say, $99.9\%$

<!-- chunk {"id": "body-0145", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

This method is effective for a range of problems. At the same time, it imposes additional computational costs, and it is not compatible with the streaming algorithm.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

Instead, we typically prescribe the dimension $\ell$ of the regression model in advance using prior knowledge about the problem or to work within our computational budget. For example, in our medium-scale experiments, we make the choice $\ell = 400$, which captures over $99.9\%$ of the spectral content of the computed covariance matrices. Since we have included the ridge regularization $\mu\mathbf{I}$ in the forecasting function, we can insulate the algorithm from the negative impact of outsize $\ell$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

Given a conservative (i.e., large) initial value of $\ell$, randomized Nyström produces an estimate for the first $\ell$ eigenvalues of the covariance matrix. Using this estimate, we can apply the rule Eq. 22 a posteriori to further reduce the dimension of the regression model. This is often a good compromise, but further research on principled methods would be valuable.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Dimension of regression model", "weight": 1.0} -->

Regardless, our numerical experiments indicate that streaming KAF forecast is somewhat insensitive to the dimension $\ell$ of the regression model. See Fig. 8 for some evidence. For large training data sets, we scale up the dimension $\ell$ to obtain more accurate forecasts.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Number of random features", "weight": 1.0} -->

The last parameter in the streaming KAF algorithm is the number $s$ of random features that we use to approximate the kernel function. As discussed in Section 3.3, the choice $s = {\sqrt{n}{\log{(n)}}}$ is theoretically justified for kernel regression in a statistical setting. In the majority of our experiments, we adopt the value $s = {\sqrt{n}{\log{(n)}}}$, and we have found that the streaming KAF method always performs well. Furthermore, taking a larger number of random features does not seem to offer any further benefit, and taking fewer random features is not detrimental. See Fig. 8 for evidence.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Number of random features", "weight": 1.0} -->

In the streaming setting, we may not know the number $n$ of training points in advance and we do not want the model size to depend on the amount of input data, so the prescription $s = {\sqrt{n}{\log{(n)}}}$ might be unappealing. Our computational work supports the recommendation that the number $s$ of random features may be a small integer multiple of the dimension $\ell$ of the regression model. It would be interesting to understand this phenomenon better from both an empirical and a theoretical point of view.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Timing comparisons", "weight": 1.0} -->

We have demonstrated that streaming KAF constructs accurate forecasting models in a range of scenarios. Therefore, we may turn our attention to the computational costs of training and forecasting. Table 2 compares the runtimes of naïve KAF and streaming KAF, and it charts the average normalized RMSE of the resulting models.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Timing comparisons", "weight": 1.0} -->

These experiments are based on the L63 data. We forecast the first state variable from the full set of three state variables. The forecast horizon is fixed at $q = 0.5$ time units. The number $n$ of training samples varies, while the number of test samples remains fixed at $m = {10,000}$. The kernel inverse bandwidth $\gamma = 0.09$, and the dimension of the regression model grows from $\ell = 400$ to $\ell = 3200$ in rough proportion to $\log n$. For the streaming method, the number of random features $s = {\sqrt{n}{\log{(n)}}}$ also increases with the size of the training data. We report the average RMSE over five test runs.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Timing comparisons", "weight": 1.0} -->

To be clear, the training time includes the full cost of computing the weight matrix ${\check{\mathbf{W}}}_{q,\ell}$ for a single real-valued response at a single forecast horizon $q$. This cost includes the evaluation of random features, formation of the covariance matrices, the streaming PCA computation, and the matrix product. For making a forecast, the timing reflects the full cost of computing $m = {10,000}$ real-valued responses for the fixed time horizon $q$, including the evaluation of random features and the matrix product.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Timing comparisons", "weight": 1.0} -->

For small problems, we see that the training time for streaming KAF is 100--200$\times$ faster than naïve KAF. The test time for streaming KAF is 300--400$\times$ faster, and the models achieve similar RMSE. For large problems, naïve KAF is unable to produce a forecasting model. Meanwhile, streaming KAF can build a forecasting model from $n = {5 \cdot 10^{6}}$ training samples in less than two hours on a laptop, and this model can produce a single real-valued forecast in about $0.0003s$. As the amount of training data increases, the RMSE of the forecasting models continues to improve, which underscores how important it is to develop a scalable algorithm.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Timing comparisons", "weight": 1.0} -->

Out of a sense of fair play, we used the theoretically supported number $s = {\sqrt{n}{\log{(n)}}}$ of random features. If we adopt our empirical recommendation $s = {{Const} \cdot \ell}$, the timings improve markedly without sacrificing much accuracy. Table 3 displays the runtimes and average normalized RMSE for streaming KAF under the same experimental set-up as in Table 2, but with the regression dimension and number of random features fixed at ${(\ell,s)} = {}$. The user may judge whether the speedup warrants the modest loss in RMSE.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

Several other techniques for data-driven prediction have been proposed and studied recently. Here, we comment on the mathematical and computational characteristics of these approaches in relation to streaming KAF, focusing on methods that employ aspects of linear operator theory or randomized linear algebra. Within this context, forecasting techniques can be broadly classified as reduced modeling approaches (i.e., methods that construct a surrogate dynamical system from observed data) and regression approaches (i.e., supervised learning techniques for estimating covariate--response relationships).

<!-- chunk {"id": "body-0157", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

Examples of reduced modeling techniques are linear inverse models, (extended) DMD, and methods for approximating the Koopman generator. These methods formally assume that the training data have a (deterministic) Markovian evolution. That assumption is clearly satisfied under the autonomous dynamics in if the training data are snapshots ${\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots$ of the full system state in ${\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

On the other hand, if we have access to samples ${u{({\mathbf{x}}_{0})}},{u{({\mathbf{x}}_{1})}},\ldots$ of a covariate $u:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d^{\prime}}}$ with $d^{\prime} < d$, then training data are generally non-Markovian (unless $u$ happens to lie in a Koopman-invariant subspace). Approaches for overcoming non-Markovianity include dimension augmentation through delay-coordinate maps and incorporation of memory terms using the Mori-Zwanzig formalism.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

Other approaches model the observed data as realizations of a stochastic process. For example, techniques based on Ulam's method estimate the transfer operator of a dynamical system (which is a dual operator to the Koopman operator, acting on probability measures) in a basis of indicator functions associated with a partition of state space. The diffusion forecasting technique estimates the evolution semigroup associated with a stochastic differential equation (SDE) on a manifold in a smooth data-driven basis of kernel eigenfunctions learned through the diffusion maps algorithm. Extensions of DMD to random dynamical systems and SDEs have also been proposed recently.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

A common aspect of reduced modeling techniques is that they learn a surrogate model of the dynamics from time series data. Often, in order to make a forecast to a horizon of $q$ time units, these models are trained on a shorter timestep $q^{\prime} < q$ and iteratively applied $q/q^{\prime}$ times to reach the desired horizon. This approach is attractive because it allows simulation of the long-term statistical behavior of the system (assuming that the training phase was successful).

<!-- chunk {"id": "body-0161", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

In contrast, regression-based methodologies usually operate by constructing a forecast function at a *fixed* lead time (or a family of independent forecast functions up to a desired lead time), and they evaluate the forecast once on the initial data to yield a prediction. This approach offers greater generality than reduced modeling approaches, since Markovianity of the covariate--response observables is not required, nor is it required that the covariate and response lie in a Koopman-invariant subspace. Indeed, as discussed in Section 2.7, KAF yields asymptotically optimal predictions (in the $L_{2}$ or RMSE sense) in the large-data limit in the form of the conditional expectation of the Koopman-evolved response conditioned on the covariate. Yet, at the same time, the conditional expectation may not be a good approximation for actual dynamical trajectories, which makes direct regression approaches unsuitable for simulating the statistical behavior of the system (despite yielding RMSE-optimal forecasts). For further details, see the paper, which studies applications of KAF to multiscale systems with averaging and homogenization limits.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

A recent paper has explored applications of kernel learning to forecasting with kernel regression.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

All of the above approaches are purely data-driven, in the sense that they only use time-ordered data snapshots as inputs, without requiring knowledge of the equations of motion. Yet, in many applications, full or partial knowledge of the equations of motion *is* available, and it is natural to design methods that take advantage of that knowledge. An example is the "lift and learn" framework which employs a mapping to transport the data to a higher-dimensional space where the system is quadratic. Unlike the Koopman operator, the existence of a finite-dimensional quadratic representation of the system dynamics is not universally guaranteed, but can be constructed for many systems encountered in physical and engineering applications if the equations of motion are known. The approach of leverages the quadratic structure of the system in the lifted space by employing a projection that is compatible with quadratic nonlinearities (see also ). In this manner, the reduced model is compatible with the "physics" of the lifted model.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

In, the projection is obtained from the *proper orthogonal decomposition* (POD), which computes a low-rank approximation to the *autocorrelation* matrix ${{\mathbf{X}}{\mathbf{X}}^{\top}} \in {\mathbb{R}}^{d \times d}$ rather than the covariance matrix ${{\mathbf{X}}^{\top}{\mathbf{X}}} \in {\mathbb{R}}^{n \times n}$. The randomized singular value decomposition is also used within this forecasting framework to build a scalable implementation.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Forecasting methodologies", "weight": 1.0} -->

Note that the eigenvectors of ${\mathbf{X}}{\mathbf{X}}^{\top}$ are spatial vectors in ${\mathbb{R}}^{d}$. In DMD, the analogous objects are the eigenvectors of the matrix $\mathbf{A}$, called Koopman modes, which can also be employed for model reduction. The KAF approach can be thought of as being "dual" to these methods in that it employs $n \times n$ kernel matrices which are discretizations of operators acting on spaces of observables of the system (rather than spatial patterns in ${\mathbb{R}}^{d}$).

<!-- chunk {"id": "body-0166", "role": "body", "section": "Streaming algorithms for kernel computation", "weight": 1.0} -->

The machine learning literature contains a substantial body of work on kernel methods, techniques for combining kernels with random features, and methods for implementing these algorithms in a streaming setting. This space is not adequate for a comprehensive summary of this vast field. We recommend the book as a foundational reference on kernel methods in machine learning.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Streaming algorithms for kernel computation", "weight": 1.0} -->

The RFF technique was developed to accelerate kernel computations. There are a substantial number of papers that use RFF for KRR, such as, but we are not aware of a paper that uses random features for streaming kernel regression.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Streaming algorithms for kernel computation", "weight": 1.0} -->

There are also several papers that combine RFF with streaming PCA algorithms to obtain streaming KPCA algorithms. In particular, Ghashami et al. apply the frequent directions method, while Ullah et al. use Oja's algorithm. Henriksen & Ward have developed an adaptive extension of Oja's algorithm that is significantly more robust. Tropp and coauthors have proposed to use the randomized Nyström method for streaming PCA, perhaps in combination with random features \[57, Sec. 19.3.5\]. Our numerical work suggests that the Nyström method is more accurate and more reliable than the alternatives in the context of streaming KAF.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Streaming algorithms for kernel computation", "weight": 1.0} -->

We have also investigated the performance of streaming KAF using AdaOja for the streaming PCA computation. In our experience, this approach can be competitive, especially in cases where the spectrum of the covariance matrix decays slowly. See for a detailed report.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Kernel analog forecasting is a regression-based approach to forecasting dynamical systems that offers a theoretical guarantee of asymptotically optimal predictions (in the $L_{2}$ or RMSE sense) in the large-data limit. By incorporating two randomized approximation techniques from numerical linear algebra---random Fourier features and the randomized Nyström method---we developed a streaming implementation of kernel analog forecasting. This approach makes it possible to build forecasting models from large data sets where the KAF methodology is theoretically justified. Our experiments indicate that streaming KAF has the potential to unlock the promise of KAF as a general data-driven, non-parametric tool for making predictions of dynamical systems.
