<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Random Fourier Features for Kernel Ridge Regression: Approximation Bounds and Statistical Guarantees

Topics include Regression, Datasets, Sampling, Random fourier features, Kernel methods.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Random Fourier features is one of the most popular techniques for scaling up kernel methods, such as kernel ridge regression. However, despite impressive empirical results, the statistical properties of random Fourier features are still not well understood. In this paper we take steps toward filling this gap. Specifically, we approach random Fourier features from a spectral matrix approximation point of view, give tight bounds on the number of Fourier features required to achieve a spectral approximation, and show how spectral matrix approximation bounds imply statistical guarantees for kernel ridge regression. Qualitatively, our results are twofold: on the one hand, we show that random Fourier feature approximation can provably speed up kernel ridge regression under reasonable assumptions. At the same time, we show that the method is suboptimal, and sampling from a modified distribution in Fourier space, given by the leverage function of the kernel, yields provably better performance. We study this optimal sampling distribution for the Gaussian kernel, achieving a nearly complete characterization for the case of low-dimensional bounded datasets. Based on this characterization, we propose an efficient sampling scheme with guarantees superior to random Fourier features in this regime.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kernel methods constitute a powerful paradigm for devising non-parametric modeling techniques for a wide range of problems in machine learning. One of the most elementary is Kernel Ridge Regression (KRR).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The KRR estimator can be derived by minimizing a regularized square loss objective function over a hypothesis space defined by the reproducing kernel Hilbert space associated with $k{(\cdot, \cdot)}$; however, the details are not important for this paper.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While simple, KRR is a powerful technique that is well understood statistically and capable of achieving impressive empirical results. Nevertheless, the method has a key weakness: computing the KRR estimator can be prohibitively expensive for large datasets. Solving (1 [AKM+17].")) generally requires $\Theta{(n^{3})}$ time^22^2The running time can be improved using fast matrix products. However fast matrix products are typically not employed in practice due to large hidden constants. and $\Theta{(n^{2})}$ memory. Thus, the design of scalable methods for KRR (and other kernel based methods) has been the focus of intensive research in recent years.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the most popular approaches to scaling up kernel based methods is random Fourier features sampling, originally proposed by Rahimi and Recht. For shift-invariant kernels (e.g. the Gaussian kernel), Rahimi and Recht presented a distribution $D$ on functions from $\mathcal{X}$ to ${\mathbb{C}}^{s}$ ($s$ is a parameter) such that for every ${\mathbf{x},\mathbf{z}} \in {\mathbb{R}}^{d}$ The random features approach is then to sample a $\varphi$ from $D$ and use ${\overset{\sim}{k}{(\mathbf{x},\mathbf{z})}} \equiv {\varphi{(\mathbf{x})}^{\ast}\varphi{(\mathbf{z})}}$ as a surrogate kernel.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting approximate KRR estimator can be computed in $O{({ns^{2}})}$ time and $O{({ns})}$ memory (see §2.2 [AKM+17].") for details), giving substantial computational savings if $s \ll n$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approach naturally raises the question: how large should $s$ be to ensure a high quality estimator? Or, using the exact KRR estimator as a natural baseline: how large should $s$ be for the random Fourier features estimator to be almost as good as the exact KRR estimator? Answering this question can help us determine when random Fourier features can be useful, whether the method needs to be improved, and how to go about improving it.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The original random Fourier features analysis bounds the point-wise distance between $k{(\cdot, \cdot)}$ and $\overset{\sim}{k}{(\cdot, \cdot)}$ (for other approaches for analyzing random Fourier features, see §2.3 [AKM+17].")). However, the bounds do not naturally lead to an answer to the aforementioned question. In contrast, spectral approximation bounds on the entire surrogate kernel matrix, i.e. of the form naturally have statistical and algorithmic implications. Indeed, in §3 [AKM+17].") we show that when (2 [AKM+17].")) holds we can bound the excess risk introduced by the random Fourier features estimator when compared to the KRR estimator. We also show that $\overset{\sim}{\mathbf{K}} + {\lambda\mathbf{I}_{n}}$ can be used as an effective preconditioner for the solution of (1 [AKM+17].")).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This motivates the study of how large $s$ should be as a function of $\Delta$ for (2 [AKM+17].")) to hold.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we rigorously analyze the relation between the number of random Fourier features and the spectral approximation bound (2 [AKM+17].")). Our main results are the following: We give an upper bound on the number of random features needed to achieve (2 [AKM+17].")) (Theorem 9 [AKM+17].")). This bound, in conjunction with the results in §3 [AKM+17]."), positively shows that random Fourier features can give guarantees for KRR under reasonable assumptions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We give a lower bound showing that our upper bound is tight for the Gaussian kernel (Theorem 10 [AKM+17].")).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that the upper bound can be improved dramatically by modifying the sampling distribution used in classical random Fourier features (§4 [AKM+17].")). Our sampling distribution is based on an appropriately defined leverage function of the kernel, closely related to so-called leverage scores frequently encountered in the analysis of sampling based methods for linear regression. Unfortunately, it is unclear how to efficiently sample using the leverage function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the lack of an efficient way to sample using the leverage function, we propose a novel, easy-to-sample distribution for the Gaussian kernel which approximates the true leverage function distribution and allows random Fourier features to achieve a significantly improved upper bound (Theorem 12 [AKM+17].")). The upper bound has an exponential dependence on the data dimension, so it is only applicable to low dimensional datasets. Nevertheless, our results demonstrate that the classic random Fourier sampling distribution can be improved for spectral approximation and motivates further study. As an application, our improved understanding of the leverage function yields a novel asymptotic bound on the statistical dimension of Gaussian kernel matrices over bounded datasets, which may be of independent interest (Corollary 18 [AKM+17].")).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Setup and Notation", "weight": 1.0} -->

The complex conjugate of $x \in {\mathbb{C}}$ is denoted by $x^{\ast}$. For a vector $\mathbf{x}$ or a matrix $\mathbf{A}$, $\mathbf{x}^{\ast}$ or $\mathbf{A}^{\ast}$ denotes the Hermitian transpose. The $l \times l$ identity matrix is denoted $\mathbf{I}_{l}$. We use the convention that vectors are column-vectors.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Setup and Notation", "weight": 1.0} -->

A Hermitian matrix $\mathbf{A}$ is positive semidefinite (PSD) if ${\mathbf{x}^{\ast}\mathbf{A}\mathbf{x}} \geq 0$ for every vector $\mathbf{x}$. For any two Hermitian matrices $\mathbf{A}$ and $\mathbf{B}$ of the same size, $\mathbf{A} \preceq \mathbf{B}$ means that $\mathbf{B} - \mathbf{A}$ is PSD.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Setup and Notation", "weight": 1.0} -->

The statistical dimension or effective degrees of freedom given the regularization parameter $\lambda$ is denoted by ${s_{\lambda}{(\mathbf{K})}} \equiv {{Tr}\left( {{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{K}} \right)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

Random Fourier features is an approach to scaling up kernel methods for shift-invariant kernels. A shift-invariant kernel is a kernel of the form ${k{(\mathbf{x},\mathbf{z})}} = {k{({\mathbf{x} - \mathbf{z}})}}$ where $k{( \cdot )}$ is a positive definite function (we abuse notation by using $k$ to denote both the kernel and the defining positive definite function).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

The underlying observation behind random Fourier features is a simple consequence of Bochner's Theorem: for every shift-invariant kernel for which ${k{(\mathbf{0})}} = 1$ there is a probability measure $\mu_{k}{(\cdot)}$ and possibly a corresponding probability density function $p_{k}{(\cdot)}$, both on ${\mathbb{R}}^{d}$, such that In other words, the inverse Fourier transform of the kernel $k{(\cdot)}$ is a probability density function, $p_{k}{(\cdot)}$. For simplicity we typically drop the $k$ subscript, writing ${\mu{(\cdot)}} = {\mu_{k}{(\cdot)}}$ and ${p{(\cdot)}} = {p_{k}{(\cdot)}}$, with the associated kernel function clear from context.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

We remark that while it is not always the case that the probability measure $\mu_{k}{(\cdot)}$ has an associated density function $p_{k}{(\cdot)}$, we assume the existence of a density function for the kernels we consider in this paper.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

If ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ are drawn according to $p{(\cdot)}$, and we define ${\varphi{(\mathbf{x})}} \equiv {\frac{1}{\sqrt{s}}\left(e^{- {2\pii{\mathbf{η}}_{1}^{T}\mathbf{x}}},\cdots,e^{- {2\pii{\mathbf{η}}_{s}^{T}\mathbf{x}}} \right)^{\ast}}$, then it is not hard to see that The idea of the Random Fourier features method is then to define the substitute kernel: To summarize, the density function $p{(\cdot)}$ is just the $d$-dimensional Fourier transform of the kernel $k{(\cdot)}$, and the random Fourier features method approximates

<!-- chunk {"id": "body-0022", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

$k{(\cdot)}$ by sampling $s$ ($d$-dimensional) frequencies ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ according to their weight in the Fourier transform.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Classical Random Fourier Features", "weight": 1.0} -->

Note that in order for $p{(\cdot)}$ to be a proper probability density function (integrating to $1$) we must have ${k{(\mathbf{0})}} = 1$. We assume this without loss of generality, since any kernel can be scaled to satisfy this condition.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Modified Random Fourier Features", "weight": 1.0} -->

While it seems to be a natural choice, there is no fundamental reason that we must sample the frequencies ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ using the Fourier transform density function $p{( \cdot )}$. In fact, we will see that it is advantageous to use a different sampling distribution based on the kernel leverage function (defined later).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Modified Random Fourier Features", "weight": 1.0} -->

Let $q{(\cdot)}$ be any probability density function whose support includes that of $p{(\cdot)}$. If we sample ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ using $q{(\cdot)}$, and define we still have ${k{(\mathbf{x},\mathbf{z})}} = {{\mathbb{E}}_{\varphi}\left\lbrack {\varphi{(\mathbf{x})}^{\ast}\varphi{(\mathbf{z})}} \right\rbrack}$. We refer to this method as modified random Fourier features and remark that it can be viewed as a form of importance sampling.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Spectral Bounds and Statistical Guarantees", "weight": 1.0} -->

Given a feature transformation, like random Fourier features, how do we analyze it and relate its use to non-approximate methods? A common approach, taken for example in the original paper on random Fourier features, is to bound the difference between the true kernel $k{(\cdot, \cdot)}$ and the approximate kernel $\overset{\sim}{k}{(\cdot, \cdot)}$. However, it is unclear how such bounds translate to downstream guarantees on statistical learning methods, such as KRR. In this paper we advocate and focus on spectral approximation bounds on the regularized kernel matrix, specifically, bounds of the form for some $\Delta < 1$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The main mathematical question we seek to address in this paper is: when using random Fourier features, how large should $s$ be in order to guarantee that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$? To motivate this question, in the following two subsections we show that such bounds can be used to derive risk inflation bounds for approximate kernel ridge regression. We also show that they can be used to analyze the use of ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ as a preconditioner for $\mathbf{K} + {\lambda\mathbf{I}_{n}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1", "weight": 1.0} -->

While this paper focuses on KRR for conciseness, we remark that in the sketching literature, spectral approximation bounds also form the basis for analyzing sketching based methods for tasks like low-rank approximation, k-means and more. In the kernel setting, such bounds where analyzed, without regularization, for the polynomial kernel. Cohen et al. recently showed that (6 [AKM+17].")) along with a trace condition on ${\mathbf{Z}\mathbf{Z}}^{\ast}$ (which holds for all sampling approaches we consider) yields a so called "projection-cost preservation" condition for the kernel approximation. With $\lambda$ chosen appropriately, this condition ensures that ${\mathbf{Z}\mathbf{Z}}^{\ast}$ can be used in place of $\mathbf{K}$ for approximately solving kernel k-means clustering and for certain versions of kernel PCA and kernel CCA. See Musco and Musco for details, where this analysis is carried out for the Nyström method.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Risk Bounds", "weight": 1.0} -->

One way to analyze estimators is via risk bounds; several recent papers on approximate KRR employ such an analysis. In particular, these papers consider the fixed design setting and seek to bound the expected in-sample predication error of the KRR estimator $\overline{f}$, viewing it as an empirical estimate of the statistical risk. More specifically, the underlying assumption is that $y_{i}$ satisfies for some $f^{\star}:{\mathcal{X}\rightarrow{\mathbb{R}}}$. The $\{\nu_{i}\}$'s are i.i.d noise terms, distributed as normal variables with variance $\sigma_{\nu}^{2}$. The empirical risk of an estimator $f$, which can be viewed as a measure of the quality of the estimator, is (note that $f$ itself might be a function of $\{\nu_{i}\}$).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2", "weight": 1.0} -->

An approximation $\overset{\sim}{\mathbf{K}}$ is only useful computationally if ${{rank}{(\overset{\sim}{\mathbf{K}})}} \ll n$ so $\overset{\sim}{\mathbf{K}}$ gives a significantly compressed approximation to the original kernel matrix. Ideally we should have ${{{rank}{(\overset{\sim}{\mathbf{K}})}}/n}\rightarrow 0$ as $n\rightarrow\infty$ and so the additive term in (8 [AKM+17].")) will also approach $0$ and generally be small when $n$ is large.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Random Features Preconditioning", "weight": 1.0} -->

Suppose we choose to solve ${{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}{\mathbf{α}}} = \mathbf{y}$ using an iterative method (e.g. CG). In this case, we can apply ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ as a preconditioner. Using standard analysis of Krylov-subspace iterative methods it is immediate that if ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ then the number of iterations until convergence is $O{(\sqrt{{(1 + \Delta)}/{(1 - \Delta)})})}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Random Features Preconditioning", "weight": 1.0} -->

Thus, if ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is, say, a $1/2$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$, then the number of iterations is bounded by a constant. The preconditioner can be efficiently applied (after preprocessing) via the Woodbury formula, giving cost per iteration (if $s \leq n$) of $O{(n^{2})}$. The overall cost of computing the KRR estimator is therefore $O{({{ns^{2}} + n^{2}})}$. Thus, as long as $s = {o{(n)}}$ this approach gives an advantage over direct methods which cost $O{(n^{3})}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Random Features Preconditioning", "weight": 1.0} -->

For small $s$ it also beats non-preconditioned iterative methods cost $O{({n^{2}\sqrt{\kappa{(\mathbf{K})}}})}$. See Cutajar et al. and Avron et al. for a detailed discussion. The upshot though is that we reach again the question that was poised earlier: how big should $s$ be so that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $1/2$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ridge Leverage Function Sampling and Random Fourier Features", "weight": 1.0} -->

In this section we present upper bounds on the number of random Fourier features needed to guarantee that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$. Our bounds apply to any shift-invariant kernel and a wide range of feature sampling distributions (in particular, classical random Fourier features).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Ridge Leverage Function Sampling and Random Fourier Features", "weight": 1.0} -->

Our analysis is based on relating the sampling density to an appropriately defined *ridge leverage function*. This function is a continuous generalization of the popular leverage scores and ridge leverage scores used in the analysis of linear methods. Bach defined the leverage function of the integral operator given by the kernel function and the data distribution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Lower Bound for Classic Random Fourier Features", "weight": 1.0} -->

Our lower bound shows that the upper bound of Theorem 9 [AKM+17].") on the number of samples required by classic random Fourier features to obtain a spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ is essentially best possible. The full proof is given in Appendix F [AKM+17].").

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Theorem 10 [AKM+17].") gives a lower bound of $s = {\Omega{({n_{\lambda}/2^{O{(d)}}})}}$. However, since a lower dimensional dataset can be embedded in an higher dimension without affecting the kernel matrix or its approximation by adding zero coordinates, the stronger bound of $s = {\Omega{(n_{\lambda})}}$ also holds. Nevertheless, we state a weaker version of the theorem since the certificate dataset is a uniform grid in $d$ dimensions (and not a one dimensional dataset embedded in an higher dimension).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Theorem 10 [AKM+17].") shows that the number of samples $s$ required for ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ to be a $1/2$-spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ for a bounded dataset of points must depend at least linearly on $n_{\lambda}$. So there is an asymptotic gap between what is achieved with classical random Fourier features and what is achieved by modified random Fourier features using leverage function sampling.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3", "weight": 1.0} -->

As we will see in §7 [AKM+17]."), the key idea behind the proof of Theorem 10 [AKM+17].") is to show that for a dataset contained in ${\lbrack{- R},R\rbrack}^{d}$, the ridge leverage function is large on a range of low frequencies. In contrast, the classic random Fourier features distribution is very small at the edges of this frequency range, and so significantly undersamples some frequencies and does not achieve spectral approximation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3", "weight": 1.0} -->

We remark that it would have been preferable if Theorem 10 [AKM+17].") applied to bounded datasets (i.e. with $R$ fixed), as the usual assumption in statistical learning theory is that data is sampled from a bounded domain. However, our current techniques are unable to address this scenario. Nevertheless, our analysis allows $R$ to grow very slowly with $n$ and we conjecture that the upper bound is tight even for bounded domains.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Improved Sampling for the Gaussian Kernel", "weight": 1.0} -->

Contrasting with the lower bound of Theorem 10 [AKM+17]."), we now give a modified Fourier feature sampling distribution that does perform well for the Gaussian kernel on bounded input sets. Furthermore, unlike the true ridge leverage function, this distribution is simple and efficient to sample. To reduce clutter, we state the result for a fixed bandwidth $\sigma = {({2\pi})}^{- 1}$. This is without loss of generality since we can rescale the points by ${({2\pi\sigma})}^{- 1}$ and adjust the bounding interval.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Improved Sampling for the Gaussian Kernel", "weight": 1.0} -->

Our modified distribution essentially corrects the classic distribution by "capping" the probability of sampling low frequencies near the origin. This allows it to allocate more samples to higher frequencies, which are undersampled by classical random Fourier features. See Figure 1 [AKM+17].") for a visual comparison of the two distributions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Bounding the Ridge Leverage Function", "weight": 1.0} -->

We now discuss our approach to bounding the ridge leverage function of the Gaussian kernel, which leads to Theorems 10 [AKM+17].") and 12 [AKM+17]."). The key idea is to reformulate the leverage function as the solution of two dual optimization problems. By exhibiting suitable test functions for these optimization problems, we are able to give both upper and lower bounds on the ridge leverage function, and correspondingly on the sampling performance of classic and modified Fourier feature sampling.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Bounding the Gaussian Kernel Leverage Function: Upper Bound", "weight": 1.0} -->

We start by applying Lemma 14 [AKM+17].") to prove a ridge leverage function upper bound for the Gaussian kernel. Again, to reduce clutter, we state the result for a fixed bandwidth $\sigma = {({2\pi})}^{- 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bounding the Gaussian Kernel Leverage Function: Lower Bound", "weight": 1.0} -->

Using the dual leverage function characterization of Lemma 15 [AKM+17]."), we can give a near matching leverage function lower bound for the Gaussian kernel.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bounding the Statistical Dimension of Gaussian Kernel Matrices", "weight": 1.0} -->

Theorems 16 [AKM+17].") and 17 [AKM+17].") together imply a tight bound on the statistical dimension of Gaussian kernel matrices corresponding to bounded points sets (the proof appears in Appendix E [AKM+17].")):

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We now report experiments on synthetic low-dimensional datasets. These experiments are designed to illustrate various points made in the previous sections. The datasets are not designed to be realistic.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In the first experiment, we noisily sample from the function^33^3This function was taken from Trefethen's book on approximation theory.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The function is sampled on a fine 400-point uniform grid spanning $\lbrack{- {{5/2}\pi}},{+ {{5/2}\pi}}\rbrack$. Samples are generated using the formula In the above, $x_{i}$ is a grid point, $y_{i}$ is the corresponding noisy sample, and $\{\nu_{i}\}$'s are i.i.d noise terms, distributed as normal variables with variance $\sigma_{\nu}^{2} = 0.3^{2}$. Figure 4 [AKM+17].") (left) shows $f^{\star}$ and the noisy samples.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Table 1 [AKM+17].") compares the estimators quantitatively. We clearly see that the MRF estimator enjoys both a lower risk and a lower actual in-sample error, when compared to the CRF estimator. MRF's risk is close to the KRR's risk. It is important to note that while the $\mathbf{Z}$ produced by MRF leads to a better estimator, when it comes to approximating the kernel matrix entry-wise (measured by ${\|{\mathbf{K} - {\mathbf{Z}\mathbf{Z}}^{\ast}}\|}_{F}^{2}/{\|\mathbf{K}\|}_{F}^{2}$), CRF produces a better approximation. This illustrates that entrywise error rates are not predictive of approximation quality.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In contrast, the generalized condition number (ratio between largest and smallest generalized eigenvalues) of $({\mathbf{K} + {\lambda\mathbf{I}}},{{\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}}})$, closely related to spectral approximation guarantees, is much more predictive of estimator quality (although additional experiments reveal that it is not completely predictive).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This is further examined in Figure 5 [AKM+17]."), where we vary $s$ and assess the estimator's quality. The leftmost graph shows the risk. While the MRF's risk quickly converges to the KRR risk, CRF's risk reduces very slowly, practically stagnating for higher $s$. Note that even when $s > n$ CRF's risk is larger than KRR's risk! This is while the entry-wise error of CRF consistently continues to reduce and is consistently better than MRF's (middle figure). In contrast, MRF's generalized condition number is consistently lower than CRF's (rightmost figure). MRF's generalized condition number continues to reduce when $s$ grows, while CRF's stagnates.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 6 [AKM+17].") we report experiments with the two dimensional function We sample points on a $40 \times 40$ uniform grid (total of $n = 1600$ points), and use ${\sigma = 0.181167},{\lambda = 0.00106475}$. We use a fixed $s = 400$. The MRF estimator is very close to the KRR estimator, while the CRF estimator misses or distorts some of the features of the function.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have analyzed random Fourier features from a spectral matrix approximation point of view. We show both positive and negative results regarding the use of random Fourier features to obtain spectral approximation of the kernel matrix. Our study is well motivated by the fact that spectral approximation bounds lead to statistical guarantees for KRR. Althouhgh we do not discuss in detail, our results can also be extended to bounds for other kernel-based methods such as kernel $k$-means and kernel PCA via recent results.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our results expose a potential sub-optimality of random Fourier features, and also show that a variant which uses a specially crafted feature sampling distribution can achieve better theoretical properties. However, our construction is mostly theoretical due to an exponential dependence on the data dimension. Nevertheless, our results motivate further efforts to improve random Fourier features by devising improved sampling distributions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions", "weight": 1.0} -->

From a conceptual point of view, our results are based on worst-case analysis of the leverage scores with respect to the data points. It is natural to try to replace the worst-case analysis with an analysis that assumes the data points are sampled from some distribution (e.g., as was recently done by Bach ). We leave this for future work as well.
