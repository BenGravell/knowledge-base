## Introduction

Kernel methods constitute a powerful paradigm for devising non-parametric modeling techniques for a wide range of problems in machine learning. One of the most elementary is Kernel Ridge Regression (KRR). Given training data ${{(\mathbf{x}_{1},y_{1})},\ldots,{(\mathbf{x}_{n},y_{n})}} \in {\mathcal{X} \times \mathcal{Y}}$, where $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is an input domain and $\mathcal{Y} \subseteq {\mathbb{R}}$ is an output domain, a positive definite kernel function $k:{{\mathcal{X} \times \mathcal{X}}\rightarrow{\mathbb{R}}}$, and a regularization parameter $\lambda > 0$, the response for a given input $\mathbf{x}$ is estimated as:

where ${\mathbf{α}} = {({\alpha_{1}\cdots\alpha_{n}})}^{\text{T}}$ is the solution of the equation

In the above, $\mathbf{K} \in {\mathbb{R}}^{n \times n}$ is the kernel matrix or Gram matrix defined by $\mathbf{K}_{ij} \equiv {k{(\mathbf{x}_{i},\mathbf{x}_{j})}}$ and $\mathbf{y} \equiv {\lbrack{y_{1}\cdotsy_{n}}\rbrack}^{\text{T}}$ is the vector of responses. The KRR estimator can be derived by minimizing a regularized square loss objective function over a hypothesis space defined by the reproducing kernel Hilbert space associated with $k{( \cdot, \cdot )}$; however, the details are not important for this paper.

While simple, KRR is a powerful technique that is well understood statistically and capable of achieving impressive empirical results. Nevertheless, the method has a key weakness: computing the KRR estimator can be prohibitively expensive for large datasets. Solving (1 [AKM+17].")) generally requires $\Theta{(n^{3})}$ time^22^2The running time can be improved using fast matrix products. However fast matrix products are typically not employed in practice due to large hidden constants. and $\Theta{(n^{2})}$ memory. Thus, the design of scalable methods for KRR (and other kernel based methods) has been the focus of intensive research in recent years \[ \].

One of the most popular approaches to scaling up kernel based methods is random Fourier features sampling, originally proposed by Rahimi and Recht \[\]. For shift-invariant kernels (e.g. the Gaussian kernel), Rahimi and Recht \[\] presented a distribution $D$ on functions from $\mathcal{X}$ to ${\mathbb{C}}^{s}$ ($s$ is a parameter) such that for every ${\mathbf{x},\mathbf{z}} \in {\mathbb{R}}^{d}$

The random features approach is then to sample a $\varphi$ from $D$ and use ${\overset{\sim}{k}{(\mathbf{x},\mathbf{z})}} \equiv {\varphi{(\mathbf{x})}^{\ast}\varphi{(\mathbf{z})}}$ as a surrogate kernel. The resulting approximate KRR estimator can be computed in $O{({ns^{2}})}$ time and $O{({ns})}$ memory (see §2.2 [AKM+17].") for details), giving substantial computational savings if $s \ll n$.

This approach naturally raises the question: how large should $s$ be to ensure a high quality estimator? Or, using the exact KRR estimator as a natural baseline: how large should $s$ be for the random Fourier features estimator to be almost as good as the exact KRR estimator? Answering this question can help us determine when random Fourier features can be useful, whether the method needs to be improved, and how to go about improving it.

The original random Fourier features analysis \[\] bounds the point-wise distance between $k{( \cdot, \cdot )}$ and $\overset{\sim}{k}{( \cdot, \cdot )}$ (for other approaches for analyzing random Fourier features, see §2.3 [AKM+17].")). However, the bounds do not naturally lead to an answer to the aforementioned question. In contrast, spectral approximation bounds on the entire surrogate kernel matrix, i.e. of the form

naturally have statistical and algorithmic implications. Indeed, in §3 [AKM+17].") we show that when (2 [AKM+17].")) holds we can bound the excess risk introduced by the random Fourier features estimator when compared to the KRR estimator. We also show that $\overset{\sim}{\mathbf{K}} + {\lambda\mathbf{I}_{n}}$ can be used as an effective preconditioner for the solution of (1 [AKM+17].")). This motivates the study of how large $s$ should be as a function of $\Delta$ for (2 [AKM+17].")) to hold.

In this paper we rigorously analyze the relation between the number of random Fourier features and the spectral approximation bound (2 [AKM+17].")). Our main results are the following:

We give an upper bound on the number of random features needed to achieve (2 [AKM+17].")) (Theorem 9 [AKM+17].")). This bound, in conjunction with the results in §3 [AKM+17]."), positively shows that random Fourier features can give guarantees for KRR under reasonable assumptions.

We give a lower bound showing that our upper bound is tight for the Gaussian kernel (Theorem 10 [AKM+17].")).

We show that the upper bound can be improved dramatically by modifying the sampling distribution used in classical random Fourier features (§4 [AKM+17].")). Our sampling distribution is based on an appropriately defined leverage function of the kernel, closely related to so-called leverage scores frequently encountered in the analysis of sampling based methods for linear regression. Unfortunately, it is unclear how to efficiently sample using the leverage function.

To address the lack of an efficient way to sample using the leverage function, we propose a novel, easy-to-sample distribution for the Gaussian kernel which approximates the true leverage function distribution and allows random Fourier features to achieve a significantly improved upper bound (Theorem 12 [AKM+17].")). The upper bound has an exponential dependence on the data dimension, so it is only applicable to low dimensional datasets. Nevertheless, our results demonstrate that the classic random Fourier sampling distribution can be improved for spectral approximation and motivates further study. As an application, our improved understanding of the leverage function yields a novel asymptotic bound on the statistical dimension of Gaussian kernel matrices over bounded datasets, which may be of independent interest (Corollary 18 [AKM+17].")).

## Preliminaries

### Setup and Notation

The complex conjugate of $x \in {\mathbb{C}}$ is denoted by $x^{\ast}$. For a vector $\mathbf{x}$ or a matrix $\mathbf{A}$, $\mathbf{x}^{\ast}$ or $\mathbf{A}^{\ast}$ denotes the Hermitian transpose. The $l \times l$ identity matrix is denoted $\mathbf{I}_{l}$. We use the convention that vectors are column-vectors.

A Hermitian matrix $\mathbf{A}$ is positive semidefinite (PSD) if ${\mathbf{x}^{\ast}\mathbf{A}\mathbf{x}} \geq 0$ for every vector $\mathbf{x}$. For any two Hermitian matrices $\mathbf{A}$ and $\mathbf{B}$ of the same size, $\mathbf{A} \preceq \mathbf{B}$ means that $\mathbf{B} - \mathbf{A}$ is PSD.

We use ${L_{2}{({d\rho})}} = {L_{2}{({\mathbb{R}}^{d},{d\rho})}}$ to denote the space of complex-valued square-integrable functions with respect to some measure $\rho{( \cdot )}$. $L_{2}{({d\rho})}$ is a Hilbert space equipped with the inner product

In the above, $p_{\rho}{( \cdot )}$ is the density associated with $\rho{( \cdot )}$ (assuming one exists).

We denote the training set by ${{(\mathbf{x}_{1},y_{1})},\ldots,{(\mathbf{x}_{n},y_{n})}} \in {\mathcal{X} \times \mathcal{Y}} \subseteq {{\mathbb{R}}^{d} \times {\mathbb{R}}}$. Note that $n$ denotes the number of training examples, and $d$ their dimension. We denote the kernel, which is a function from $\mathcal{X} \times \mathcal{X}$ to $\mathbb{R}$, by $k$. We denote the kernel matrix by $\mathbf{K}$, with $\mathbf{K}_{ij} \equiv {k{(\mathbf{x}_{i},\mathbf{x}_{j})}}$. The associated reproducing kernel Hilbert space (RKHS) is denoted by $\mathcal{H}_{k}$, and the associated inner product by ${\langle \cdot, \cdot \rangle}_{\mathcal{H}_{k}}$. Some results are stated for the Gaussian kernel ${k{(\mathbf{x},\mathbf{z})}} = {\exp{({- {{{\|{\mathbf{x} - \mathbf{z}}\|}_{2}^{2}/2}\sigma^{2}}})}}$ for some bandwidth parameter $\sigma$.

We use $\lambda = \lambda_{n}$ to denote the ridge regularization parameter. While for brevity we omit the $n$ subscript, the choice of regularization parameter generally depends on $n$. Typically, $\lambda_{n} = {\omega{}}$ and $\lambda_{n} = {o{(n)}}$. See Caponnetto and De Vito \[\] and Bach \[\] for discussion on the asymptotic behavior of $\lambda_{n}$, noting that in our notation, $\lambda$ is scaled by an $n$ factor as compared to those works. As the ratio between $n$ and $\lambda$ will be an important quantity in our bounds, we denote it as $n_{\lambda} \equiv {n/\lambda}$.

The statistical dimension or effective degrees of freedom given the regularization parameter $\lambda$ is denoted by ${s_{\lambda}{(\mathbf{K})}} \equiv {{Tr}\left( {{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{K}} \right)}$.

### Random Fourier Features

### Classical Random Fourier Features

Random Fourier features \[\] is an approach to scaling up kernel methods for shift-invariant kernels. A shift-invariant kernel is a kernel of the form ${k{(\mathbf{x},\mathbf{z})}} = {k{({\mathbf{x} - \mathbf{z}})}}$ where $k{( \cdot )}$ is a positive definite function (we abuse notation by using $k$ to denote both the kernel and the defining positive definite function).

The underlying observation behind random Fourier features is a simple consequence of Bochner's Theorem: for every shift-invariant kernel for which ${k{(\mathbf{0})}} = 1$ there is a probability measure $\mu_{k}{( \cdot )}$ and possibly a corresponding probability density function $p_{k}{( \cdot )}$, both on ${\mathbb{R}}^{d}$, such that

In other words, the inverse Fourier transform of the kernel $k{( \cdot )}$ is a probability density function, $p_{k}{( \cdot )}$. For simplicity we typically drop the $k$ subscript, writing ${\mu{( \cdot )}} = {\mu_{k}{( \cdot )}}$ and ${p{( \cdot )}} = {p_{k}{( \cdot )}}$, with the associated kernel function clear from context. We remark that while it is not always the case that the probability measure $\mu_{k}{( \cdot )}$ has an associated density function $p_{k}{( \cdot )}$, we assume the existence of a density function for the kernels we consider in this paper.

If ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ are drawn according to $p{( \cdot )}$, and we define ${\varphi{(\mathbf{x})}} \equiv {\frac{1}{\sqrt{s}}\left( e^{- {2\pii{\mathbf{η}}_{1}^{T}\mathbf{x}}},\cdots,e^{- {2\pii{\mathbf{η}}_{s}^{T}\mathbf{x}}} \right)^{\ast}}$, then it is not hard to see that

The idea of the Random Fourier features method is then to define the substitute kernel:

To summarize, the density function $p{( \cdot )}$ is just the $d$-dimensional Fourier transform of the kernel $k{( \cdot )}$, and the random Fourier features method approximates $k{( \cdot )}$ by sampling $s$ ($d$-dimensional) frequencies ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ according to their weight in the Fourier transform. Note that in order for $p{( \cdot )}$ to be a proper probability density function (integrating to $1$) we must have ${k{(\mathbf{0})}} = 1$. We assume this without loss of generality, since any kernel can be scaled to satisfy this condition.

Now suppose that $\mathbf{Z} \in {\mathbb{C}}^{n \times s}$ is the matrix whose $j^{th}$ row is $\varphi{(\mathbf{x}_{j})}^{\ast}$, and let $\overset{\sim}{\mathbf{K}} = {\mathbf{Z}\mathbf{Z}}^{\ast}$. $\overset{\sim}{\mathbf{K}}$ is the kernel matrix corresponding to $\overset{\sim}{k}{( \cdot, \cdot )}$. The resulting random Fourier features KRR estimator is ${\overset{\sim}{f}{(\mathbf{x})}} \equiv {\sum_{j = 1}^{n}{\overset{\sim}{k}{(\mathbf{x}_{j},\mathbf{x})}{\overset{\sim}{\alpha}}_{j}}}$ where $\overset{\sim}{\mathbf{α}}$ is the solution of ${{({\overset{\sim}{\mathbf{K}} + {\lambda\mathbf{I}_{n}}})}\overset{\sim}{\mathbf{α}}} = \mathbf{y}$. Typically, $s < n$ and we can represent $\overset{\sim}{f}{( \cdot )}$ more efficiently as:

(this is a simple consequence of the Woodbury formula). We can compute $\mathbf{w}$ in $O{({ns^{2}})}$ time, making random Fourier features computationally attractive if $s < n$.

### Modified Random Fourier Features

While it seems to be a natural choice, there is no fundamental reason that we must sample the frequencies ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ using the Fourier transform density function $p{( \cdot )}$. In fact, we will see that it is advantageous to use a different sampling distribution based on the kernel leverage function (defined later).

Let $q{( \cdot )}$ be any probability density function whose support includes that of $p{( \cdot )}$. If we sample ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ using $q{( \cdot )}$, and define

we still have ${k{(\mathbf{x},\mathbf{z})}} = {{\mathbb{E}}_{\varphi}\left\lbrack {\varphi{(\mathbf{x})}^{\ast}\varphi{(\mathbf{z})}} \right\rbrack}$. We refer to this method as modified random Fourier features and remark that it can be viewed as a form of importance sampling.

### Additional Notations and Identities

Now that we have defined (modified) random Fourier features, we can introduce some additional notation and identities. The $(j,l)$ entry of $\mathbf{Z}$ is given by:

Let $\mathbf{z}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{C}}^{n}}$ be defined by

Note that column $l$ of $\mathbf{Z}$ from the previous section is exactly $\mathbf{z}{({\mathbf{η}}_{l})}\sqrt{{p{({\mathbf{η}}_{l})}}/{\lbrack{{s \cdot q}{({\mathbf{η}}_{l})}}\rbrack}}$. So we have:

Finally, by (3 [AKM+17].")) we have

and thus ${{\mathbb{E}}\left\lbrack {\mathbf{Z}\mathbf{Z}}^{\ast} \right\rbrack} = \mathbf{K}$.

### Related Work

Rahimi and Recht's original analysis of random Fourier features \[\] bounded the point-wise distance between $k{( \cdot, \cdot )}$ and $\overset{\sim}{k}{( \cdot, \cdot )}$.

In follow-up work, they give learning rate bounds for a broad class of estimators using random Fourier features \[\]. However, their results do not apply to classic KRR. Furthermore, their main bound becomes relevant only when the number of sampled features is on order of the training set size.

Rudi et al. \[\] prove generalization properties for KRR with random features, under somewhat difficult to verify technical assumptions, some of which can be seen as constraining the leverage function distribution that we study. They leave open improving their bounds via a more refined sampling approach. Bach \[\] analyzes random Fourier features from a function approximation point of view. He defines a similar leverage function distribution to the one that we consider, but leaves open establishing bounds on and effectively sampling from this distribution, both of which we address in this work. Finally, Tropp \[\] analyzes the distance between the kernel matrix and its approximation in terms of the spectral norm, ${\|{\mathbf{K} - \overset{\sim}{\mathbf{K}}}\|}_{2}$, which can be a significantly weaker error metric than (2 [AKM+17].")).

Outside of work on random Fourier features, risk inflation bounds for approximate KRR and leverage score sampling have been used to analyze and improve the Nyström method for kernel approximation \[ \]. We apply a number of techniques from this line of work.

Spectral approximation bounds, such as (2 [AKM+17].")), are quite popular in the sketching literature; see Woodruff's survey \[\]. Most closely related to our work is analysis of spectral approximation bounds without regularization (i.e. $\lambda = 0$) for the polynomial kernel \[\]. Improved bounds with regularization (still for the polynomial kernel) were recently proved by Avron et al. \[\].

## Spectral Bounds and Statistical Guarantees

Given a feature transformation, like random Fourier features, how do we analyze it and relate its use to non-approximate methods? A common approach, taken for example in the original paper on random Fourier features \[\], is to bound the difference between the true kernel $k{( \cdot, \cdot )}$ and the approximate kernel $\overset{\sim}{k}{( \cdot, \cdot )}$. However, it is unclear how such bounds translate to downstream guarantees on statistical learning methods, such as KRR. In this paper we advocate and focus on spectral approximation bounds on the regularized kernel matrix, specifically, bounds of the form

for some $\Delta < 1$.

### Definition 1

We say that a matrix $\mathbf{A}$ is a $\Delta$-spectral approximation of another matrix $\mathbf{B}$, if ${{({1 - \Delta})}\mathbf{B}} \preceq \mathbf{A} \preceq {{({1 + \Delta})}\mathbf{B}}$.

### Remark 1

When $\lambda = 0$, bounds of the form of (6 [AKM+17].")) can be viewed as a low-distortion subspace embedding bounds. Indeed, when $\lambda = 0$ it follows from (6 [AKM+17].")) that ${{\mathbf{S}\mathbf{p}\mathbf{a}\mathbf{n}}\left( {k{(\mathbf{x}_{1}, \cdot )}},\ldots,{k{(\mathbf{x}_{n}, \cdot )}} \right)} \subseteq \mathcal{H}_{k}$ can be embedded with $\Delta$-distortion in ${{\mathbf{S}\mathbf{p}\mathbf{a}\mathbf{n}}\left( {\varphi{(\mathbf{x}_{1})}},\ldots,{\varphi{(\mathbf{x}_{n})}} \right)} \subseteq {\mathbb{R}}^{s}$.

The main mathematical question we seek to address in this paper is: when using random Fourier features, how large should $s$ be in order to guarantee that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$? To motivate this question, in the following two subsections we show that such bounds can be used to derive risk inflation bounds for approximate kernel ridge regression. We also show that they can be used to analyze the use of ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ as a preconditioner for $\mathbf{K} + {\lambda\mathbf{I}_{n}}$.

While this paper focuses on KRR for conciseness, we remark that in the sketching literature, spectral approximation bounds also form the basis for analyzing sketching based methods for tasks like low-rank approximation, k-means and more. In the kernel setting, such bounds where analyzed, without regularization, for the polynomial kernel \[\]. Cohen et al. \[\] recently showed that (6 [AKM+17].")) along with a trace condition on ${\mathbf{Z}\mathbf{Z}}^{\ast}$ (which holds for all sampling approaches we consider) yields a so called "projection-cost preservation" condition for the kernel approximation. With $\lambda$ chosen appropriately, this condition ensures that ${\mathbf{Z}\mathbf{Z}}^{\ast}$ can be used in place of $\mathbf{K}$ for approximately solving kernel k-means clustering and for certain versions of kernel PCA and kernel CCA. See Musco and Musco \[\] for details, where this analysis is carried out for the Nyström method.

### Risk Bounds

One way to analyze estimators is via risk bounds; several recent papers on approximate KRR employ such an analysis \[ \]. In particular, these papers consider the fixed design setting and seek to bound the expected in-sample predication error of the KRR estimator $\overline{f}$, viewing it as an empirical estimate of the statistical risk. More specifically, the underlying assumption is that $y_{i}$ satisfies

for some $f^{\star}:{\mathcal{X}\rightarrow{\mathbb{R}}}$. The $\{\nu_{i}\}$'s are i.i.d noise terms, distributed as normal variables with variance $\sigma_{\nu}^{2}$. The empirical risk of an estimator $f$, which can be viewed as a measure of the quality of the estimator, is

(note that $f$ itself might be a function of $\{\nu_{i}\}$).

Let $\mathbf{f} \in {\mathbb{R}}^{n}$ be the vector whose $j^{th}$ entry is $f^{\star}{(\mathbf{x}_{j})}$. It is quite straightforward to show that for the KRR estimator $\overline{f}$ we have \[, \]:

Since ${\lambda^{2}\mathbf{f}^{\text{T}}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 2}\mathbf{f}} \leq {\lambda\mathbf{f}^{\text{T}}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{f}}$ and ${{Tr}\left( {\mathbf{K}^{2}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 2}} \right)} \leq {{Tr}\left( {\mathbf{K}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}} \right)} = {s_{\lambda}{(\mathbf{K})}}$, we define

and note that ${\mathcal{R}{(\overline{f})}} \leq {{\hat{\mathcal{R}}}_{\mathbf{K}}{(\mathbf{f})}}$. The first term in the above expressions for $\mathcal{R}{(\overline{f})}$ and ${\hat{\mathcal{R}}}_{\mathbf{K}}{(\mathbf{f})}$ is frequently referred to as the bias term, while the second is the variance term.

### Lemma 2

Suppose that (7 [AKM+17].")) holds, and let $\mathbf{f} \in {\mathbb{R}}^{n}$ be the vector whose $j^{th}$ entry is $f^{\star}{(\mathbf{x}_{j})}$. Let $\overline{f}$ be the KRR estimator, and let $\overset{\sim}{f}$ be KRR estimator obtained using some other kernel $\overset{\sim}{k}{( \cdot, \cdot )}$ whose kernel matrix is $\overset{\sim}{\mathbf{K}}$. Suppose that $\overset{\sim}{\mathbf{K}} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ for some $\Delta < 1$, and that ${\|\mathbf{K}\|}_{2} \geq 1$. The following bound holds:

### Proof

Note that $\mathbf{A} \preceq \mathbf{B}$ implies that $\mathbf{B}^{- 1} \preceq \mathbf{A}^{- 1}$ so for the bias term we have:

We now consider the variance term. Denote $s = {{rank}{(\overset{\sim}{\mathbf{K}})}}$, and let ${\lambda_{1}{(\mathbf{A})}} \geq {\lambda_{2}{(\mathbf{A})}} \geq \cdots \geq {\lambda_{n}{(\mathbf{A})}}$ denote the eigenvalues of a matrix $\mathbf{A}$. We have:

where we use the fact that $\mathbf{A} \preceq \mathbf{B}$ implies that ${\lambda_{i}{(\mathbf{A})}} \leq {\lambda_{i}{(\mathbf{B})}}$ (this is a simple consequence of the Courant-Fischer minimax theorem).

Combining the above variance bound with the bias bound in (9 [AKM+17].")) yields:

and the bound ${\mathcal{R}{(\overset{\sim}{f})}} \leq {{\hat{\mathcal{R}}}_{\overset{\sim}{\mathbf{K}}}{(\mathbf{f})}}$ completes the proof. ∎

In short, Lemma 2 [AKM+17].") bounds the risk of the approximate KRR estimator as a function of both the risk upper bound ${\hat{\mathcal{R}}}_{\mathbf{K}}{(\mathbf{f})}$ and an additive term which is small if ${rank}{(\overset{\sim}{\mathbf{K}})}$ and/or $\Delta$ is small. In particular, it is instructive to compare the additive term ${{{({\Delta/{({1 + \Delta})}})}n^{- 1}\sigma_{\nu}^{2}} \cdot {rank}}{(\overset{\sim}{\mathbf{K}})}$ to the variance term ${{n^{- 1}\sigma_{\nu}^{2}} \cdot s_{\lambda}}{(\mathbf{K})}$.

### Remark 2

An approximation $\overset{\sim}{\mathbf{K}}$ is only useful computationally if ${{rank}{(\overset{\sim}{\mathbf{K}})}} \ll n$ so $\overset{\sim}{\mathbf{K}}$ gives a significantly compressed approximation to the original kernel matrix. Ideally we should have ${{{rank}{(\overset{\sim}{\mathbf{K}})}}/n}\rightarrow 0$ as $n\rightarrow\infty$ and so the additive term in (8 [AKM+17].")) will also approach $0$ and generally be small when $n$ is large.

### Random Features Preconditioning

Suppose we choose to solve ${{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}{\mathbf{α}}} = \mathbf{y}$ using an iterative method (e.g. CG). In this case, we can apply ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ as a preconditioner. Using standard analysis of Krylov-subspace iterative methods it is immediate that if ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ then the number of iterations until convergence is $O{(\sqrt{{(1 + \Delta)}/{(1 - \Delta)})})}$. Thus, if ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is, say, a $1/2$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$, then the number of iterations is bounded by a constant. The preconditioner can be efficiently applied (after preprocessing) via the Woodbury formula, giving cost per iteration (if $s \leq n$) of $O{(n^{2})}$. The overall cost of computing the KRR estimator is therefore $O{({{ns^{2}} + n^{2}})}$. Thus, as long as $s = {o{(n)}}$ this approach gives an advantage over direct methods which cost $O{(n^{3})}$. For small $s$ it also beats non-preconditioned iterative methods cost $O{({n^{2}\sqrt{\kappa{(\mathbf{K})}}})}$. See Cutajar et al. \[\] and Avron et al. \[\] for a detailed discussion. The upshot though is that we reach again the question that was poised earlier: how big should $s$ be so that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $1/2$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$?

## Ridge Leverage Function Sampling and Random Fourier Features

In this section we present upper bounds on the number of random Fourier features needed to guarantee that ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is a $\Delta$-spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$. Our bounds apply to any shift-invariant kernel and a wide range of feature sampling distributions (in particular, classical random Fourier features).

Our analysis is based on relating the sampling density to an appropriately defined *ridge leverage function*. This function is a continuous generalization of the popular leverage scores \[\] and ridge leverage scores \[, \] used in the analysis of linear methods. Bach \[\] defined the leverage function of the integral operator given by the kernel function and the data distribution. For our purposes, a more appropriate definition is with respect to a fixed input dataset:

### Definition 3

For $\mathbf{x}_{1},\ldots,\mathbf{x}_{n}$ and shift-invariant kernel $k{( \cdot, \cdot )}$, define the ridge leverage function as

In the above, $\mathbf{K}$ is the kernel matrix and $p{( \cdot )}$ is the distribution given by the inverse Fourier transform of $k{( \cdot, \cdot )}$.

We begin with two simple propositions. Recall that we assume ${k{(\mathbf{x},\mathbf{x})}} = {k{(\mathbf{0})}} = 1$ for any $\mathbf{x}$, however our results apply to general shift invariant kernel after appropriate scaling.

### Proposition 4

For all $\mathbf{η}$,

### Proof

Since $k$ is positive definite and ${k{(\mathbf{0})}} = 1$, ${|{k{(\mathbf{x},\mathbf{z})}}|} \leq 1$ for all $\mathbf{x}$ and $\mathbf{z}$. This implies that the maximum eigenvalue of $\mathbf{K}$ is bounded by $n$. The lower bound follows, after noting that ${\|{\mathbf{z}{({\mathbf{η}})}}\|}_{2}^{2} = n$. The upper bound follows similarly, since all eigenvalues of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ are lower bounded by $\lambda$. ∎

### Proposition 5

### Proof

The second and third equalities follow from the cyclic property and linearity of the trace respectively. ∎

Recall that we denote the ratio $n/\lambda$, which appears frequently in our analysis, by $n_{\lambda} = {n/\lambda}$. As discussed, theoretical bounds generally set $\lambda = {\omega{}}$ (as a function of $n$) so $n_{\lambda} = {o{(n)}}$. However we remark that in practice, it may sometimes be the case that $\lambda$ is very small and $n_{\lambda} \gg n$.

An immediate result of Propositions 4 [AKM+17].") and 5 [AKM+17].") (which can also be obtained algebraically from $\mathbf{K}$) is a generic bound on statistical dimension:

### Corollary 6

For any $\mathbf{K}$, ${\mathbf{s}_{\lambda}{(\mathbf{K})}} \leq n_{\lambda}$.

For any shift-invariant kernel with ${k{(\mathbf{x},\mathbf{x})}} = 1$ and ${k{(\mathbf{x},\mathbf{z})}}\rightarrow 0$ as ${\|{\mathbf{x} - \mathbf{z}}\|}_{2}\rightarrow\infty$ (e.g., the Gaussian kernel) if we allow points to be arbitrarily spread out, the kernel matrix converges to the identity matrix, and ${s_{\lambda}{(\mathbf{I}_{n})}} = {n/{({1 + \lambda})}} = {\Omega{(n_{\lambda})}}$ if $\lambda = {\Omega{}}$ so the above bound is tight. However, this requires datasets of increasingly large diameter (as $n$ grows). In contrast, the usual assumption in statistical learning is that the data is sampled from a bounded domain $\mathcal{X}$. In §7.4 [AKM+17].") we show via a leverage function upper bound that for the important Gaussian kernel, for bounded datasets we have ${s_{\lambda}{(\mathbf{K})}} = {o{(n_{\lambda})}}$.

In the matrix sketching literature it is well known that spectral approximation bounds similar to (6 [AKM+17].")) can be constructed by sampling columns relative to upper bounds on the leverage scores. In the following, we generalize this for the case of sampling Fourier features from a continuous domain. First, we need an auxiliary lemma.

### Lemma 7

Let $\mathbf{B}$ be a fixed $d_{1} \times d_{2}$ matrix. Construct a $d_{1} \times d_{2}$ random matrix $\mathbf{R}$ that satisfies

Let $\mathbf{M}_{1}$ and $\mathbf{M}_{2}$ be semidefinite upper bounds for the expected squares:

Define the quantities

Form the matrix sampling estimator

where each $\mathbf{R}_{k}$ is an independent copy of $\mathbf{R}$. Then, for all $t \geq {\sqrt{m/n} + {{{2L}/3}n}}$,

The proof of Lemma 7 [AKM+17]."), which is essentially a restatement of Corollary 7.3.3 from \[\] with slightly improved requirements, appears in appendix A [AKM+17].")

### Lemma 8

Let $\overset{\sim}{\tau}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be a measurable function such that ${\overset{\sim}{\tau}{({\mathbf{η}})}} \geq {\tau_{\lambda}{({\mathbf{η}})}}$ for all ${\mathbf{η}} \in {\mathbb{R}}^{d}$, and furthermore assume that

is finite. Denote ${p_{\overset{\sim}{\tau}}{({\mathbf{η}})}} = {{\overset{\sim}{\tau}{({\mathbf{η}})}}/s_{\overset{\sim}{\tau}}}$. Let $\Delta \leq {1/2}$ and $\rho \in {}$. Assume that ${\|\mathbf{K}\|}_{2} \geq \lambda$. Suppose we take $s \geq {\frac{8}{3}\Delta^{- 2}s_{\overset{\sim}{\tau}}{\ln{({{16s_{\lambda}{(\mathbf{K})}}/\rho})}}}$ samples ${\mathbf{η}}_{1},\ldots,{\mathbf{η}}_{s}$ from the distribution associated with the density $p_{\overset{\sim}{\tau}}{( \cdot )}$ and then construct the matrix $\mathbf{Z}$ according to (5 [AKM+17].")) with $q = p_{\overset{\sim}{\tau}}$. Then ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ with probability of at least $1 - \rho$.

### Proof

Let ${\mathbf{K} + {\lambda\mathbf{I}_{n}}} = {\mathbf{V}^{\text{T}}\mathbf{\Sigma}^{2}\mathbf{V}}$ be an eigendecomposition of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$. Note that the $\Delta$-spectral approximation guarantee (2 [AKM+17].")) is equivalent to

so by multiplying by $\mathbf{\Sigma}^{- 1}\mathbf{V}$ on the left and $\mathbf{V}^{\text{T}}\mathbf{\Sigma}^{- 1}$ on the right we find that it suffices to show that

holds with probability of at least $1 - \rho$. Let

Note that ${{\mathbb{E}}\left\lbrack \mathbf{Y}_{l} \right\rbrack} = {\mathbf{\Sigma}^{- 1}{\mathbf{V}\mathbf{K}\mathbf{V}}^{\text{T}}\mathbf{\Sigma}^{- 1}}$ and ${\frac{1}{s}{\sum_{l = 1}^{s}\mathbf{Y}_{l}}} = {\mathbf{\Sigma}^{- 1}{\mathbf{V}\mathbf{Z}\mathbf{Z}}^{\ast}\mathbf{V}^{\text{T}}\mathbf{\Sigma}^{- 1}}$. Thus, we can use matrix concentration results to prove (10 [AKM+17].")).

To apply this bound we need to bound the norm of $\mathbf{Y}_{l}$ and the stable rank ${\mathbb{E}}\left\lbrack \mathbf{Y}_{l}^{2} \right\rbrack$. Since $\mathbf{Y}_{l}$ is always a rank one matrix we have

since ${{\overset{\sim}{\tau}}_{\lambda}{({\mathbf{η}}_{l})}} \geq {\tau{({\mathbf{η}}_{l})}}$ by assumption of the lemma. We also have

Let $\lambda_{1} \geq \cdots \geq \lambda_{n}$ be the eigenvalues of $\mathbf{K}$. We have

where the third inequality is due to the assumption that $\lambda_{1} = {\|\mathbf{K}\|}_{2} \geq \lambda$ and the last inequality is due to the bound on $s$. ∎

Lemma 8 [AKM+17].") shows that if we could sample using the ridge leverage function, then $O{({s_{\lambda}{(\mathbf{K})}{\log{({s_{\lambda}{(\mathbf{K})}})}}})}$ samples suffice for spectral approximation of $\mathbf{K}$ (for a fixed $\Delta$ and failure probability). While there is no straightforward way to perform this sampling, we can consider how well the classic random Fourier features sampling distribution approximates the leverage function, obtaining a bound on its performance:

### Theorem 9

Let $\Delta \leq {1/2}$ and $\rho \in {}$. Assume that ${\|\mathbf{K}\|}_{2} \geq \lambda$. If we use $s \geq {\frac{8}{3}\Delta^{- 2}n_{\lambda}{\ln{({{16s_{\lambda}{(\mathbf{K})}}/\rho})}}}$ random Fourier features (i.e., sampled according to $p{( \cdot )}$), then ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ with probability of at least $1 - \rho$.

### Proof

Define ${\overset{\sim}{\tau}{({\mathbf{η}})}} = {{p{({\mathbf{η}})}} \cdot n_{\lambda}}$ and note that ${\overset{\sim}{\tau}{({\mathbf{η}})}} \geq {\tau_{\lambda}{({\mathbf{η}})}}$ by Proposition 4 [AKM+17].") and that $s_{\overset{\sim}{\tau}} = n_{\lambda}$. Finally, note that ${p_{\overset{\sim}{\tau}}{({\mathbf{η}})}} = {p{({\mathbf{η}})}}$, the classic Fourier features sampling probability. ∎

Theorem 9 [AKM+17].") establishes that if $\lambda = {\omega{({\log{(n)}})}}$ and $\Delta$ is fixed, $o{(n)}$ random Fourier features suffice for spectral approximation, and so the method can provably speed up KRR. Nevertheless, the bound depends on $n_{\lambda}$ instead of $s_{\lambda}{(\mathbf{K})}$, as is possible with true leverage function sampling (see Lemma 8 [AKM+17].")). This gap arises from our use of the simple, often loose, leverage function upper bound given by Proposition 4 [AKM+17].").

Unfortunately, the bound in Theorem 9 [AKM+17].") cannot be improved. Even for the special case of a one-dimensional Gaussian kernel, the classic random Fourier features sampling distribution is far enough from the ridge leverage distribution that $\Omega{(n_{\lambda})}$ features may be needed even when ${s_{\lambda}{(\mathbf{K})}} = {o{(n_{\lambda})}}$. On the otherhand, a simple modified sampling approach *does* closely approximate the true ridge leverage distribution and so yields significantly better bounds for the Gaussian kernel. We present these results in §5 [AKM+17].") and §6 [AKM+17].") respectively. We defer a discussion of their proofs to §7 [AKM+17]."), where we develop our main technical contribution: a sharper understanding of the ridge leverage function based on a formulation as the solution to two dual optimization problems which give corresponding upper and lower bounds on the distribution and, correspondingly, on sampling performance.

## Lower Bound for Classic Random Fourier Features

Our lower bound shows that the upper bound of Theorem 9 [AKM+17].") on the number of samples required by classic random Fourier features to obtain a spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ is essentially best possible. The full proof is given in Appendix F [AKM+17].").

### Theorem 10

Consider the $d$-dimensional Gaussian kernel with $\sigma = {({2\pi})}^{- 1}$ (so ${p{({\mathbf{η}})}} = {{({2\pi})}^{- {d/2}}e^{- {{\|{\mathbf{η}}\|}_{2}^{2}/2}}}$). Suppose that $n \geq 17$ is any odd integer such that $m = n^{1/d} \geq {\max{({64{\log n_{\lambda}}},3)}}$ is integer. Further, assume that $1 \leq d \leq \frac{2{\log n}}{5{\log{\log n}}}$. For any $\lambda$ satisfying $\frac{10}{n} \leq \lambda \leq {\min\left\{ {\left( \frac{1}{2} \right)^{2d} \cdot \frac{n}{1024}},n^{1 - \frac{1}{128}} \right\}}$, and every radius $R$ such that ${2000{\log n_{\lambda}}} \leq R \leq \frac{n^{1/d}}{800\sqrt{\log{(n_{\lambda})}}}$, there exists a dataset of $n$ points ${\{\mathbf{x}_{j}\}}_{j = 1}^{n} \subseteq {\lbrack{- R},R\rbrack}^{d}$ such that if $s$ random Fourier features (i.e., sampled according to $p{( \cdot )}$) are sampled for some $s$ satisfying $s \leq \frac{n_{\lambda}}{13 \cdot 2^{{2d} + 4}}$, then with probability at least $0.5$, there exists a vector ${\mathbf{α}} \in {\mathbb{R}}^{n}$ such that

Furthermore, for the said dataset is a uniformly spaced grid in $d$ dimensions, with $m$ points per dimension, and we have ${s_{\lambda}{(\mathbf{K})}} = {O{({{R \cdot {poly}}\left( {\log n_{\lambda}} \right)})}}$.

### Remark 3

Theorem 10 [AKM+17].") gives a lower bound of $s = {\Omega{({n_{\lambda}/2^{O{(d)}}})}}$. However, since a lower dimensional dataset can be embedded in an higher dimension without affecting the kernel matrix or its approximation by adding zero coordinates, the stronger bound of $s = {\Omega{(n_{\lambda})}}$ also holds. Nevertheless, we state a weaker version of the theorem since the certificate dataset is a uniform grid in $d$ dimensions (and not a one dimensional dataset embedded in an higher dimension).

Theorem 10 [AKM+17].") shows that the number of samples $s$ required for ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ to be a $1/2$-spectral approximation to $\mathbf{K} + {\lambda\mathbf{I}_{n}}$ for a bounded dataset of points must depend at least linearly on $n_{\lambda}$. So there is an asymptotic gap between what is achieved with classical random Fourier features and what is achieved by modified random Fourier features using leverage function sampling.

As we will see in §7 [AKM+17]."), the key idea behind the proof of Theorem 10 [AKM+17].") is to show that for a dataset contained in ${\lbrack{- R},R\rbrack}^{d}$, the ridge leverage function is large on a range of low frequencies. In contrast, the classic random Fourier features distribution is very small at the edges of this frequency range, and so significantly undersamples some frequencies and does not achieve spectral approximation.

We remark that it would have been preferable if Theorem 10 [AKM+17].") applied to bounded datasets (i.e. with $R$ fixed), as the usual assumption in statistical learning theory is that data is sampled from a bounded domain. However, our current techniques are unable to address this scenario. Nevertheless, our analysis allows $R$ to grow very slowly with $n$ and we conjecture that the upper bound is tight even for bounded domains.

## Improved Sampling for the Gaussian Kernel

Contrasting with the lower bound of Theorem 10 [AKM+17]."), we now give a modified Fourier feature sampling distribution that does perform well for the Gaussian kernel on bounded input sets. Furthermore, unlike the true ridge leverage function, this distribution is simple and efficient to sample from. To reduce clutter, we state the result for a fixed bandwidth $\sigma = {({2\pi})}^{- 1}$. This is without loss of generality since we can rescale the points by ${({2\pi\sigma})}^{- 1}$ and adjust the bounding interval.

Our modified distribution essentially corrects the classic distribution by "capping" the probability of sampling low frequencies near the origin. This allows it to allocate more samples to higher frequencies, which are undersampled by classical random Fourier features. See Figure 1 [AKM+17].") for a visual comparison of the two distributions.

### Definition 11 (Improved Fourier Feature Distribution for the Gaussian Kernel)

Define the function

Let $s_{{\overline{\tau}}_{R}} = {\int_{\mathbb{R}}{{\overline{\tau}}_{R}{({\mathbf{η}})}{d{\mathbf{η}}}}}$ and define the probability density function ${{\overline{p}}_{R}{({\mathbf{η}})}} = {{{\overline{\tau}}_{R}{({\mathbf{η}})}}/s_{{\overline{\tau}}_{R}}}$.

Note that ${\overline{p}}_{R}{({\mathbf{η}})}$ is just the uniform distribution for low frequencies with ${\|{\mathbf{η}}\|}_{\infty} \leq {10\sqrt{\log{(n_{\lambda})}}}$, and a slightly modified classic Fourier features distribution, appropriately scaled, outside this range. As we show in §7 [AKM+17]."), ${\overline{\tau}}_{R}{({\mathbf{η}})}$ upper bounds the true ridge leverage function $\tau_{\lambda}{({\mathbf{η}})}$ for all $\mathbf{η}$. Hence, simply applying Lemma 8 [AKM+17]."):

### Theorem 12

Consider the d-dimensional Gaussian kernel with $\sigma = {({2\pi})}^{- 1}$ (so ${p{({\mathbf{η}})}} = {{({2\pi})}^{- {d/2}}e^{- {{\|{\mathbf{η}}\|}_{2}^{2}/2}}}$) and any dataset of $n$ points ${\{\mathbf{x}_{j}\}}_{j = 1}^{n} \subseteq {\mathbb{R}}^{d}$ contained in a $\ell_{\infty}$-ball of radius $R$ (i.e ${\|{\mathbf{x}_{i} - \mathbf{x}_{j}}\|}_{\infty} \leq {2R}$ for all ${i,j} \in {\lbrack n\rbrack}$). Suppose that $d \leq {{5{\log{(n_{\lambda})}}} + 1}$. If we sample $s \geq {\frac{8}{3}\Delta^{- 2}s_{{\overline{\tau}}_{R}}{\ln{({{16s_{\lambda}{(\mathbf{K})}}/\rho})}}}$ random Fourier features according to ${\overline{p}}_{R}{( \cdot )}$ and construct $\mathbf{Z}$ according to (5 [AKM+17].")), then with probability at least $1 - \rho$, ${\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}_{n}}$ is $\Delta$-spectral approximation of $\mathbf{K} + {\lambda\mathbf{I}_{n}}$. Furthermore, $s_{{\overline{\tau}}_{R}} = O\left( {(248R)}^{d}\log{(n_{\lambda})}^{d/2} + {(200\log n_{\lambda})}^{2d} \right)$ and ${\overline{p}}_{R}{( \cdot )}$ can be sampled from in $O{(d)}$ time.

### Proof

The result follows from Lemma 8 [AKM+17].") and the fact that ${\overline{\tau}}_{R}{( \cdot )}$ upper bounds the true ridge leverage function, which is shown in Theorem 16 [AKM+17].") of §7 [AKM+17]."). The bound on $s_{{\overline{\tau}}_{R}}$ can be computed as follows. Let us denote ${g_{1}{(\eta)}} = {{({2\pi})}^{- {1/2}}e^{- {\eta^{2}/2}}{\max{(1,{|\eta|})}}}$ and ${g{({\mathbf{η}})}} = {{{g_{1}{(\eta_{1})}} \cdot \ldots \cdot g_{1}}{(\eta_{d})}}$. We calculate

We now have (computed using a technique shown later in the proof)

The bound $d \leq {{5{\log{(n_{\lambda})}}} + 1}$ ensures that

Sampling from ${\overline{\tau}}_{R}{(\eta)}$ amounts to sampling from a mixture of the uniform distribution on ${\lbrack{- {10\sqrt{\log n_{\lambda}}}},{10\sqrt{\log n_{\lambda}}}\rbrack}^{d}$ and the tail of the distribution defined by ${\overline{\tau}}_{R}$: with probability $\frac{1}{s_{{\overline{\tau}}_{R}}}{({20\sqrt{\log n_{\lambda}}})}^{d}$ $\cdot \left( {\left( {12.4{\max{}}} \right)^{d} + 1} \right)$ sample from the uniform distribution and with remaining probability sample from the tail. Above, we have an closed form expression for the total mass of the tail, which allows us to decide whether to sample from the uniform part or from the tail part using a single sample from a uniform distribution on $\lbrack 0,1\rbrack$.

Sampling from the uniform part, clearly takes $O{(d)}$ time. Sampling from the tail can be easily done via rejection sampling at $O{(d)}$ expected cost, as we now show. The density $p_{t}$ of the tail is:

Now we write $\mathbb{1}\left\lbrack {{\|{\mathbf{η}}\|}_{\infty} \geq {10\sqrt{\log n_{\lambda}}}} \right\rbrack$ as a union of disjoint partitions as follows:

Let $R_{j}$ denote the $j$th region in the above partition:

Thus, the density $p_{t}$ can written as follows:

Now because $R_{j}$'s are disjoint sets we can do the following.

We first take a sample $j \in {\lbrack d\rbrack}$ with probability $\frac{\int_{{\mathbf{η}} \in R_{j}}{g{({\mathbf{η}})}{d{\mathbf{η}}}}}{\int_{{\|{\mathbf{η}}^{\prime}\|}_{\infty} \geq {10\sqrt{\log n_{\lambda}}}}{g{({\mathbf{η}})}{d{\mathbf{η}}^{\prime}}}}$. In order to execute this step, we first compute:

Then given the probabilities we can sample $j$ in $O{(d)}$ time.

Next, we need to take a sample from the distribution:

We explain how to sample from this distribution in the subsequent paragraphs.

We now explain how to perform the sampling in the second step. It can be seen in the above expression that sampling from the distribution whose density is $p_{t,j}{({\mathbf{η}})}$ amounts to sampling each of $d$ coordinates of $\mathbf{η}$ independently from their corresponding distributions. There are three types of distributions that we need to sample from. Either we need to sample proportional to $g_{1}$ (coordinates whose index is higher than $j$) or we need to sample from the head of $g_{1}$ (rescaled) (coordinates $1,\ldots,{j - 1}$), or we sample from the tail (coordinate $j$).

We start with sampling proportional to $g_{1}$. This distribution is a mixture of Gaussian on $\lbrack{- 1},1\rbrack$ and enlarged Gaussian outside. The total mass is $A$, and the relative mass of the Gaussian part is ${{erf}{({1/\sqrt{2}})}}/A$. First, we sample a uniform random variable $U$, which will decide which part of the mixture we sample. If $U$ is bigger than ${{erf}{({1/\sqrt{2}})}}/A$, then the sample comes from the tail. In that case, we generate the sample by computing $G^{- 1}{(U)}$ where ${G{(\xi)}} \equiv {A^{- 1}{\int_{- \xi}^{\xi}{g_{1}{(\eta)}{d\eta}}}}$ (i.e., we use inverse transform sampling). Note that $G$ has a simple invertible closed form for values larger than $1$, we have ${G{}} = {{{erf}{({1/\sqrt{2}})}}/A}$. If $U \leq {{{erf}{({1/\sqrt{2}})}}/A}$, then the sample comes from the Gaussian part. To generate the sample from the head, we sample a standard Gaussian $X$, and test whether $X \leq 1$. If it is, then we use the sample, otherwise we reject and repeat. Obviously, the expected number of samples we need is $O{}$.

To sample proportional to the head of $g_{1}$, we repeat the above procedure and test whether the sample is smaller than $10\sqrt{\log n_{\lambda}}$. If it is not, we reject the sample and repeat.

To sample proportional to the tail of $g_{1}$, we sample a uniform random variable $T$ on $\lbrack 0,{B/A}\rbrack$, and return $G^{- 1}{({1 - T})}$, using the closed from expression for $G^{- 1}$ for values close to $1$.

Thus, we can generate a sample in step 2 in $O{(d)}$ expected time, and overall the sampling procedure takes $O{(d)}$. ∎

Theorem 12 [AKM+17].") represents a possibly exponential improvement over the bound obtainable by classic random Fourier features. Consider $d = 1$ and $R \geq {\log^{1.5}{(n_{\lambda})}}$. The bound on $s_{{\overline{\tau}}_{R}}$ shows that our modified distribution requires $O{({R\sqrt{\log{(n_{\lambda})}}})}$ samples, as compared to the lower bound of $\Omega{(n_{\lambda})}$ given by Theorem 10 [AKM+17].").

Figure 1: Plot of the true ridge leverage function vs. the classic random Fourier features distribution and our modified distribution, for a dataset of n = 401 equispaced points on the range [−5, 5]. Our modified distribution closely matches the true leverage scores to within a small multiplicative factor. In contrast, the classical distribution oversamples low frequencies, at the expense of substantially undersampling higher frequencies.

## Bounding the Ridge Leverage Function

We now discuss our approach to bounding the ridge leverage function of the Gaussian kernel, which leads to Theorems 10 [AKM+17].") and 12 [AKM+17]."). The key idea is to reformulate the leverage function as the solution of two dual optimization problems. By exhibiting suitable test functions for these optimization problems, we are able to give both upper and lower bounds on the ridge leverage function, and correspondingly on the sampling performance of classic and modified Fourier feature sampling.

### Primal-Dual Characterization

Before introducing our primal-dual characterization of the ridge leverage function, we give a few definitions. Define the operator $\mathbf{\Phi}:{{L_{2}{({d\mu})}}\rightarrow{\mathbb{C}}^{n}}$ by

We first prove that the operator $\mathbf{\Phi}$ is defined on all $L_{2}{({d\mu})}$ and is a bounded linear operator. Indeed, for $y \in {L_{2}{({d\mu})}}$ we have:

Therefore, there is a unique adjoint operator $\mathbf{\Phi}^{\ast}:{{\mathbb{C}}^{n}\rightarrow{L_{2}{({d\mu})}}}$, such that ${\langle{\mathbf{\Phi}y},\mathbf{x}\rangle}_{{\mathbb{C}}^{n}} = {\langle y,{\mathbf{\Phi}^{\ast}\mathbf{x}}\rangle}_{L_{2}{({d\mu})}}$ for every $y \in {L_{2}{({d\mu})}}$ and $\mathbf{x} \in {\mathbb{C}}^{n}$. It is easy to verify that ${{({\mathbf{\Phi}^{\ast}\mathbf{x}})}{({\mathbf{η}})}} = {\mathbf{z}{({\mathbf{η}})}^{\ast}\mathbf{x}}$. We now have the following:

### Proposition 13

For every $\mathbf{x} \in {\mathbb{C}}^{n}$:

### Proof

We have that for every $\mathbf{x} \in {\mathbb{C}}^{n}$,

We can now equivalently define the ridge leverage function $\tau_{\lambda}{( \cdot )}$ via the following optimization problems. Similar characterization are known for the finite dimensional case. Here we extend these results to an infinite dimensional case.

### Lemma 14

The ridge leverage function can alternatively be defined as:

### Proof

The minimizer of the right-hand side of (13 [AKM+17].")) can be obtained from the usual normal equations, and simplified using the matrix inversion lemma for operators \[\]:

where we used Proposition 13 [AKM+17].") to replace $\Phi\mathbf{\Phi}^{\ast}$ with $\mathbf{K}$. So, ${y^{\star}{({\mathbf{ξ}})}} = {\sqrt{p{({\mathbf{η}})}}\mathbf{z}{({\mathbf{ξ}})}^{\ast}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{z}{({\mathbf{η}})}}$. We now have

Now plugging these into (13 [AKM+17].")) gives:

Recall that we define ${\mathbf{z}{({\mathbf{η}})}_{j}} = e^{- {2\pii\mathbf{x}_{j}^{\text{T}}{\mathbf{η}}}}$. So $\mathbf{\Phi}$ is just a $d$-dimensional Fourier transform of the function $y$ weighted by probability measure ${d\mu{({\mathbf{ξ}})}} = {p{({\mathbf{ξ}})}d{\mathbf{ξ}}}$, and evaluated at the frequencies given by the data points $\mathbf{x}_{1},\ldots,\mathbf{x}_{n}$. Thus, the optimization problem of Lemma 14 [AKM+17].") asks us to produce a function $y$ whose Fourier transform is close to the pure cosine wave $\sqrt{p{({\mathbf{η}})}}\mathbf{z}{({\mathbf{η}})}$ on our datapoints. At the same time, to keep the second term of (13 [AKM+17].")) small, $y$ should have bounded norm under the $\mu{({\mathbf{ξ}})}$ measure. So, the trivial solution of setting $y$ to be a Dirac delta function at $\mathbf{η}$ (whose Fourier transform is a pure cosine with frequency $\mathbf{η}$) fails. A more carefully chosen function must be constructed whose Fourier transform looks like the cosine at our datapoints but diverges elsewhere. Such a function certifies that, on our datapoints, the cosine of frequency $\mathbf{η}$ can be approximately reconstructed with low energy using other frequencies. Hence $\mathbf{η}$ is not a critical frequency for sampling, so $\tau_{\lambda}{({\mathbf{η}})}$ is small.

Dual to minimization objective of Lemma 14 [AKM+17]."), which allows us to certify upper bounds on the ridge leverage function, we have a maximization objective allowing us to certify lower bounds:

### Lemma 15

The ridge leverage function can alternatively be defined as:

### Proof

The optimization problem (13 [AKM+17].")) can equivalently be reformulated as the following problem:

First we show that for any ${\mathbf{α}} \in {\mathbb{C}}^{n}$, the argument of the minimization problem in (14 [AKM+17].")) is no bigger than $\tau_{\lambda}{({\mathbf{η}})}$. That is because for the optimal solution to above optimization, namely $\overline{\mathbf{u}}$ and $\overline{y}$, we have:

where the last inequality follows from Cauchy-Schwarz inequality (${|{{\mathbf{α}}^{\ast}\mathbf{\Phi}\overline{y}}|} = {|{({{\mathbf{α}}^{\ast}\mathbf{\Phi}\overline{y}})}^{\ast}|} = {|{{({\mathbf{\Phi}\overline{y}})}^{\ast}{\mathbf{α}}}|} = {|{\langle\overline{y},{\mathbf{\Phi}^{\ast}{\mathbf{α}}}\rangle}_{L_{2}{({d\mu})}}|} \leq {{\|{\mathbf{\Phi}^{\ast}{\mathbf{α}}}\|}_{L_{2}{({d\mu})}} \cdot {\|\overline{y}\|}_{L_{2}{({d\mu})}}}$). By another use of Cauchy-Schwarz we have:

Therefore, for every ${\mathbf{α}} \in {\mathbb{C}}^{n}$,

Now it is enough to show that at the optimal $\mathbf{α}$ the dual problem gives the leverage scores. We show that $\overline{\mathbf{α}} = {\sqrt{p{({\mathbf{η}})}}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{z}{({\mathbf{η}})}}$ matches the leverage scores. First note that for any ${\mathbf{α}} \in {\mathbb{C}}^{n}$ we have

Now by substituting $\overline{\mathbf{α}} = {\sqrt{p{({\mathbf{η}})}}{({\mathbf{K} + {\lambda\mathbf{I}_{n}}})}^{- 1}\mathbf{z}{({\mathbf{η}})}}$ we have:

The optimization problem of Lemma 15 [AKM+17].") asks us to exhibit a set of coefficients ${\mathbf{α}} \in {\mathbb{C}}^{n}$, such that the Fourier domain representation of our point set weighted by these coefficients (i.e. $\mathbf{\Phi}^{\ast}{\mathbf{α}}$) is concentrated at frequency $\mathbf{η}$ and hence $\frac{{p{({\mathbf{η}})}} \cdot {|{{\mathbf{α}}^{\ast}\mathbf{z}{({\mathbf{η}})}}|}^{2}}{{\|{\mathbf{\Phi}^{\ast}{\mathbf{α}}}\|}_{L_{2}{({d\mu})}}^{2}}$ is large. $\mathbf{α}$ certifies that $\mathbf{η}$ is a critical frequency for representing our point set and so $\tau_{\lambda}{({\mathbf{η}})}$ must be large. $\lambda{\|{\mathbf{α}}\|}^{2}$ is a regularization term, decreasing the ridge leverage function when $p{({\mathbf{η}})}$ is very small, i.e. when $\mathbf{η}$ has small weight in the Fourier transform of our kernel.

### Bounding the Gaussian Kernel Leverage Function: Upper Bound

We start by applying Lemma 14 [AKM+17].") to prove a ridge leverage function upper bound for the Gaussian kernel. Again, to reduce clutter, we state the result for a fixed bandwidth $\sigma = {({2\pi})}^{- 1}$.

### Theorem 16

Consider the d-dimensional Gaussian kernel with $\sigma = {({2\pi})}^{- 1}$. For any integer $n$ and parameter $0 < \lambda \leq \frac{n}{2}$ such that $d \leq {n_{\lambda}/4}$, and any radius $R > 0$, if ${\mathbf{x}_{1},\ldots,\mathbf{x}_{n}} \in {\mathbb{R}}^{d}$ is contained in a $\ell_{\infty}$-ball of radius $R$ (i.e ${\|{\mathbf{x}_{i} - \mathbf{x}_{j}}\|}_{\infty} \leq {2R}$ for all ${i,j} \in {\lbrack n\rbrack}$), then for every ${\|{\mathbf{η}}\|}_{\infty} \leq {10\sqrt{\log n_{\lambda}}}$ we have:

Applying Theorem 16 [AKM+17].") for $\mathbf{η}$ with ${\|{\mathbf{η}}\|}_{\infty} < {10\sqrt{\log n_{\lambda}}}$ and Proposition 4 [AKM+17].") for $\mathbf{η}$ outside this range immediately implies our improved sampling bound Theorem 12 [AKM+17].").

### Theorem 16 [AKM+17].") Proof Outline (Details and a full proof in Appendix C [AKM+17]."))

For simplicity we focus on the case of $d = 1$. Our proof for higher dimensions uses similar ideas. To upper bound $\tau_{\lambda}{(\eta)}$ using Lemma 14 [AKM+17].") it suffices to exhibit any function $y_{\eta} \in {L_{2}{({d\mu})}}$ (i.e. with bounded norm ${\| y_{\eta}\|}_{L_{2}{({d\mu})}}^{2}$) such that, when reweighted by ${\mu{(\xi)}} = {p{(\xi)}d\xi}$, $y_{\eta}$'s Fourier transform is close to the pure cosine target function $\mathbf{z}{(\eta)}$ on our datapoints. In general the test function depends on $\eta$ and hence our subscript notation $y_{\eta}{( \cdot )}$.

One simple attempt is ${y_{\eta}{(\xi)}} = {\frac{1}{\sqrt{p{(\eta)}}}\delta{({\eta - \xi})}}$ where $\delta{( \cdot )}$ is the Dirac delta function. This choice zeros out the first term of (13 [AKM+17].")). However $\delta{( \cdot )}$ is not square integrable, $y_{\eta} \notin {L_{2}{({d\mu})}}$, so the lemma cannot be used (the norm is unbounded). Another attempt is ${y_{\eta}{(\xi)}} = 0$, which zeros out the second term and recovers the trivial bound ${\tau_{\lambda}{(\eta)}} \leq {\lambda^{- 1}{\|{\sqrt{p{(\eta)}}\mathbf{z}{(\eta)}}\|}_{2}^{2}} = {p{(\eta)}n_{\lambda}}$ of Proposition 4 [AKM+17].").

We improve this bound by replacing the Dirac delta function at $\eta$ with a 'soft spike' whose Fourier transform still looks approximately like a cosine wave on $\lbrack{- R},R\rbrack$, and hence at our data points, which are bounded on this range. The smaller $R$ is, the more spread out this function can be, and hence the smaller its norm ${\| y_{\eta}\|}_{L_{2}{({d\mu})}}^{2}$, and the better the leverage function bound.

A natural idea is to consider the inverse Fourier transform of the cosine with frequency $\eta$ restricted to the range $\lbrack{- R},R\rbrack$ -- i.e. multiplied by the box function on this range. It is well known that this is a sinc function with width ${1/2}R$, centered at $\eta$: ${g_{\eta}{(\xi)}} = {{{2R} \cdot {sinc}}\left( {2R{({\xi - \eta})}} \right)}$, where ${{sinc}(x)} = \frac{\sin x}{x}$ (see Figure 2. ‣ 7.2 Bounding the Gaussian Kernel Leverage Function: Upper Bound ‣ 7 Bounding the Ridge Leverage Function ‣ Random Fourier Features for Kernel Ridge Regression: Approximation Bounds and Statistical Guarantees1footnote 11footnote 1An extended abstract of this work appears in the Proceedings of the 34th International Conference on Machine Learning [AKM+17].")). If we set ${y_{\eta}{(\xi)}} = {{g_{\eta}{(\xi)}} \cdot \frac{\sqrt{p{(\eta)}}}{p{(\xi)}}}$, the $d\mu$ weighted Fourier transform at $x_{j} \in {\lbrack{- R},R\rbrack}$, ${({\mathbf{\Phi}y_{\eta}})}_{j}$, will be identical to the target $\mathbf{z}{(\eta)}_{j}$ and so again the first term of (13 [AKM+17].")) will be $0$. Unfortunately, ${\| y_{\eta}\|}_{L_{2}{({d\mu})}}^{2}$ will still be too large. The reweighting function ${{1/p}{(\xi)}} = {2\pie^{\xi/2}}$ grows exponentially in $\xi$, while ${sinc}\left( {2R{({\xi - \eta})}} \right)$ only falls off linearly, so $y_{\eta}$ will have unbounded energy in the high frequencies.

Figure 2: To minimize ∥Φ yη − z (η)∥22, we can choose a test function yη (ξ) whose (d μ weighted) Fourier transform Φ yη is the pure cosine e−2 π i x η multiplied by the box function on [−R, R]. Specifically, yη (ξ) p (ξ) is a sinc function centered at η. Unfortunately, ∥yη∥L2 (d μ)2 is too large to get a good leverage function bound from Lemma 14. However, this construction is the starting point for our final test function, pictured in Figure 3.

To correct this issue, we dampen the sinc at higher frequencies by multiplying with a Gaussian, which decreases ${\| y_{\eta}\|}_{L_{2}{({d\mu})}}^{2}$, but does not significantly affect the Fourier transform on $\lbrack{- R},R\rbrack$.

Specifically, for some parameters $u,v$ set $g_{\eta}{(\xi)}$ to be product of a Gaussian with standard deviation $1/u$ with a sinc function with width $1/v$, both centered at $\eta$. The corresponding Fourier transform ${\hat{g}}_{\eta}{(x)}$ is the convolution of a Gaussian with standard deviation $u$ with a box of width $v$ -- i.e. a blurred box.

If we set $v = {\Theta{({R + {u\sqrt{\log n_{\lambda}}}})}}$ then the box, when centered at $x \in {\lbrack{- R},R\rbrack}$ nearly covers the full mass of the Gaussian. Specifically, we have ${1 - {1/n_{\lambda}^{c}}} \leq {|{{\hat{g}}_{\eta}{(x)}}|} \leq 1$ for $x \in {\lbrack{- R},R\rbrack}$ and some large constant $c$. Since $g_{\eta}{(\xi)}$ is centered at $\eta$, ${\hat{g}}_{\eta}{(x)}$ is multiplied by the cosine wave $e^{- {2\piix\eta}}$, and so we have ${({\mathbf{\Phi}y_{\eta}})}_{j} = {\sqrt{p{(\eta)}}{\hat{g}}_{\eta}{(x_{j})}} \approx {\mathbf{z}{(\eta)}_{j}}$. Thus, when applying Lemma 14 [AKM+17].") to bound the leverage function, the first term of (13 [AKM+17].")) will be negligible (see Figure 3. ‣ 7.2 Bounding the Gaussian Kernel Leverage Function: Upper Bound ‣ 7 Bounding the Ridge Leverage Function ‣ Random Fourier Features for Kernel Ridge Regression: Approximation Bounds and Statistical Guarantees1footnote 11footnote 1An extended abstract of this work appears in the Proceedings of the 34th International Conference on Machine Learning [AKM+17].")).

Theorem 16 [AKM+17].") then follows from setting $u$ to minimize ${\| y_{\eta}\|}_{L_{2}{({d\mu})}}^{2}$ -- balancing increased damping for large $\eta$ with increased energy due to a more concentrated Gaussian. We eventually choose $u = {\Theta{({\log n_{\lambda}})}}$. Obtaining tight bounds and in particular achieving the right dependence on $\log n_{\lambda}$ requires several modifications, but the general intuition described above works!

Figure 3: In comparison to Figure 2, damping the sinc function with a Gaussian decreases the energy ∥yη∥L2 (d μ)2 but does not significantly affect the Fourier transform on [−R, R]. Φ yη is a pure cosine with frequency η multiplied by a blurred box function and thus (Φ yη)j ≈ z (η)j for xj ∈ [−R, R]. Accordingly, yη is ideal for bounding the leverage function via Lemma 14.

### Bounding the Gaussian Kernel Leverage Function: Lower Bound

Using the dual leverage function characterization of Lemma 15 [AKM+17]."), we can give a near matching leverage function lower bound for the Gaussian kernel. We have:

### Theorem 17

Consider the $d$-dimensional Gaussian kernel with $\sigma = {({2\pi})}^{- 1}$. For any integer $n = m^{d} \geq 55$ with integer $m \geq {\max{({64{\log{(n)}}\sqrt{\log n_{\lambda}}},{64{\log{(n_{\lambda})}}},3)}}$ and $1 \leq d \leq {\min\left( \frac{\log n}{18{\log{\log n}}},{64n_{\lambda}^{5/2}{\log^{3/2}n_{\lambda}}} \right)}$, any parameter $\frac{10}{n} \leq \lambda \leq {\min\left\{ {\left( \frac{1}{2} \right)^{2d} \cdot \frac{n}{1024}},n^{1 - \frac{1}{128}} \right\}}$, and every radius ${2000{\log n_{\lambda}}} \leq R \leq \frac{m}{500\sqrt{\log{(n_{\lambda})}}}$, there exist ${\mathbf{x}_{1},\mathbf{x}_{2},\ldots,\mathbf{x}_{n}} \in {\lbrack{- R},R\rbrack}^{d}$ such that for every ${\mathbf{η}} \in {\lbrack{- {50\sqrt{\log n_{\lambda}}}},{50\sqrt{\log n_{\lambda}}}\rbrack}^{d}$ we have

### Theorem 17 [AKM+17].") Proof Outline (Details and a full proof are given in Appendix D [AKM+17]."))

The main idea of the proof is to use Lemma 15 [AKM+17].") to get a lower bound on $\tau_{\lambda}{({\mathbf{η}})}$. Note that the expression given under the maximum in (14 [AKM+17].")) provides a lower bound for any choice of $\mathbf{α}$. However, we provide a judiciously chosen $\mathbf{α}$ that is related to the test function $y_{\mathbf{η}} \in {L_{2}{({d\mu})}}$ used in the proof of Theorem 16 [AKM+17].") which provides an upper bound on $\tau_{\lambda}{({\mathbf{η}})}$. The choice of $y_{\mathbf{η}}$ in the proof of the upper bound is essentially a sinc function that is dampened by a Gaussian centered at $\mathbf{η}$. Due to the duality of the corresponding minimization and maximization problems in Lemma 14 [AKM+17].") and Lemma 15 [AKM+17]."), respectively, the optimal $\mathbf{α}$ must essentially be a scalar multiple of $\mathbf{\Phi}y_{\mathbf{η}}$, which is a (weighted) Fourier transform of $y_{\mathbf{η}}$ evaluated on the data points $\mathbf{x}_{1},\mathbf{x}_{2},\ldots,\mathbf{x}_{n}$. Hence, we should intuitively choose $\mathbf{α}$ to be the samples of $y_{\mathbf{η}}$ on the data points. Moreoever, to provide the tightest possible lower bound, we wish to choose our data points $\mathbf{x}_{1},\mathbf{x}_{2},\ldots,\mathbf{x}_{n}$ to be as spread apart as possible, as this corresponds to a higher statistical dimension (which corresponds to higher leverage scores on average). Thus, we choose our points to be evenly spaced points on a $d$-dimensional grid located inside an $L_{\infty}$ ball of radius $R$ around the origin.

### Bounding the Statistical Dimension of Gaussian Kernel Matrices

Theorems 16 [AKM+17].") and 17 [AKM+17].") together imply a tight bound on the statistical dimension of Gaussian kernel matrices corresponding to bounded points sets (the proof appears in Appendix E [AKM+17].")):

### Corollary 18

Consider the $d$-dimensional Gaussian kernel with $\sigma = {({2\pi})}^{- 1}$. For any integer $n = m^{d} \geq 17$ with integer $m \geq 3$, parameter $0 < \lambda \leq \frac{n}{2}$, $1 \leq d \leq \frac{5{\log n_{\lambda}}}{\log{\log n_{\lambda}}}$, and $R > 0$, if ${\mathbf{x}_{1},\ldots,\mathbf{x}_{n}} \in {\lbrack{- R},R\rbrack}^{d}$:

Furthermore, if ${2000{\log n_{\lambda}}} \leq R \leq \frac{m}{500\sqrt{\log{(n_{\lambda})}}}$, $1 \leq d \leq \frac{\log n}{2{\log{\log n}}}$ and $m \geq {64{\log{(n)}}\sqrt{\log n_{\lambda}}}$ there exists a set of points ${\mathbf{x}_{1},\ldots,\mathbf{x}_{n}} \subseteq {\lbrack{- R},R\rbrack}^{d}$ such that:

## Numerical Experiments

We now report experiments on synthetic low-dimensional datasets. These experiments are designed to illustrate various points made in the previous sections. The datasets are not designed to be realistic.

Figure 4: Results on the wiggly function. Left graph shows the function itself, the noisy samples and the KRR estimator. Right graph shows both the classical random Fourier features estimator (labeled CRF) and a modified random Fourier features estimator (labeled MRF).

In the first experiment, we noisily sample from the function^33^3This function was taken from Trefethen's book on approximation theory \[\].

The function is sampled on a fine 400-point uniform grid spanning $\lbrack{- {{5/2}\pi}},{+ {{5/2}\pi}}\rbrack$. Samples are generated using the formula

In the above, $x_{i}$ is a grid point, $y_{i}$ is the corresponding noisy sample, and $\{\nu_{i}\}$'s are i.i.d noise terms, distributed as normal variables with variance $\sigma_{\nu}^{2} = 0.3^{2}$. Figure 4 [AKM+17].") (left) shows $f^{\star}$ and the noisy samples.

Figure 4 [AKM+17].") (left) also shows the KRR estimator, obtained using the Gaussian kernel with $\sigma = 0.0280443$ and regularization parameter $\lambda = 0.00618936$. These values where obtained by optimizing the estimator's risk, which we can compute due to our knowledge of $f^{\star}$ and the noise distribution, using MATLAB's fminsearch function starting from $\sigma_{0} = 1$ and $\lambda_{0} = 1$.

Figure 4 [AKM+17].") (right) shows the estimator obtained using $s = 200$ classical random Fourier features (labeled CRF) and $s = 200$ modified random Fourier features (labeled MRF). For modified random Fourier features, we did not use the analytical construction in §6 [AKM+17]."), but rather use a uniform distribution on $\lbrack{- {\gamma/\sigma}},{\gamma/\sigma}\rbrack$, treating $\gamma$ as a parameter (we use $\gamma = 4$). Technically, the support of the distribution is not the entire real line (as required), so the expected value of the substitute kernel is not identical to that of the true kernel, however the weight of values which are not in the support is negligible for large enough values of $\gamma$. We clearly see that while classical random Fourier features fails to estimate the higher frequency areas of $f^{\star}$, modified random Fourier features approximates them well (close to the quality of the KRR estimator).

$\frac{{\|{\mathbf{K} - {\mathbf{Z}\mathbf{Z}}^{\ast}}\|}_{F}^{2}}{{\|\mathbf{K}\|}_{F}^{2}}$

Table 1: Comparison of estimators for the wiggly function.

Table 1 [AKM+17].") compares the estimators quantitatively. We clearly see that the MRF estimator enjoys both a lower risk and a lower actual in-sample error, when compared to the CRF estimator. MRF's risk is close to the KRR's risk. It is important to note that while the $\mathbf{Z}$ produced by MRF leads to a better estimator, when it comes to approximating the kernel matrix entry-wise (measured by ${\|{\mathbf{K} - {\mathbf{Z}\mathbf{Z}}^{\ast}}\|}_{F}^{2}/{\|\mathbf{K}\|}_{F}^{2}$), CRF produces a better approximation. This illustrates that entrywise error rates are not predictive of approximation quality. In contrast, the generalized condition number (ratio between largest and smallest generalized eigenvalues) of $({\mathbf{K} + {\lambda\mathbf{I}}},{{\mathbf{Z}\mathbf{Z}}^{\ast} + {\lambda\mathbf{I}}})$, closely related to spectral approximation guarantees, is much more predictive of estimator quality (although additional experiments reveal that it is not completely predictive).

Figure 5: Assessing estimator’s quality when varying s.

This is further examined in Figure 5 [AKM+17]."), where we vary $s$ and assess the estimator's quality. The leftmost graph shows the risk. While the MRF's risk quickly converges to the KRR risk, CRF's risk reduces very slowly, practically stagnating for higher $s$. Note that even when $s > n$ CRF's risk is larger than KRR's risk! This is while the entry-wise error of CRF consistently continues to reduce and is consistently better than MRF's (middle figure). In contrast, MRF's generalized condition number is consistently lower than CRF's (rightmost figure). MRF's generalized condition number continues to reduce when $s$ grows, while CRF's stagnates.

In Figure 6 [AKM+17].") we report experiments with the two dimensional function

We sample points on a $40 \times 40$ uniform grid (total of $n = 1600$ points), and use ${\sigma = 0.181167},{\lambda = 0.00106475}$. We use a fixed $s = 400$. The MRF estimator is very close to the KRR estimator, while the CRF estimator misses or distorts some of the features of the function.

Figure 6: Approximation of the two dimensional wiggly function.

## Conclusions

We have analyzed random Fourier features from a spectral matrix approximation point of view. We show both positive and negative results regarding the use of random Fourier features to obtain spectral approximation of the kernel matrix. Our study is well motivated by the fact that spectral approximation bounds lead to statistical guarantees for KRR. Althouhgh we do not discuss in detail, our results can also be extended to bounds for other kernel-based methods such as kernel $k$-means and kernel PCA via recent results \[, \].

Our results expose a potential sub-optimality of random Fourier features, and also show that a variant which uses a specially crafted feature sampling distribution can achieve better theoretical properties. However, our construction is mostly theoretical due to an exponential dependence on the data dimension. Nevertheless, our results motivate further efforts to improve random Fourier features by devising improved sampling distributions.

From a conceptual point of view, our results are based on worst-case analysis of the leverage scores with respect to the data points. It is natural to try to replace the worst-case analysis with an analysis that assumes the data points are sampled from some distribution (e.g., as was recently done by Bach \[\]). We leave this for future work as well.
