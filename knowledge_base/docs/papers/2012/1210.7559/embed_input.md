<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tensor Decompositions for Learning Latent Variable Models

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work considers a computationally and statistically efficient parameter estimation method for a wide class of latent variable models - including Gaussian mixture models, hidden Markov models, and latent Dirichlet allocation - which exploits a certain tensor structure in their low-order observable moments (typically, of second- and third-order). Specifically, parameter estimation is reduced to the problem of extracting a certain (orthogonal) decomposition of a symmetric tensor derived from the moments; this decomposition can be viewed as a natural generalization of the singular value decomposition for matrices. Although tensor decompositions are generally intractable to compute, the decomposition of these specially structured tensors can be efficiently obtained by a variety of approaches, including power iterations and maximization approaches (similar to the case of matrices). A detailed analysis of a robust tensor power method is provided, establishing an analogue of Wedin's perturbation theorem for the singular vectors of matrices. This implies a robust and computationally tractable estimation approach for several popular latent variable models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The method of moments is a classical parameter estimation technique (Pearson, 1894) from statistics which has proved invaluable in a number of application domains. The basic paradigm is simple and intuitive: (i) compute certain statistics of the data---often empirical moments such as means and correlations---and (ii) find model parameters that give rise to (nearly) the same corresponding population quantities. In a number of cases, the method of moments leads to consistent estimators which can be efficiently computed; this is especially relevant in the context of latent variable models, where standard maximum likelihood approaches are typically computationally prohibitive, and heuristic methods can be unreliable and difficult to validate with high-dimensional data. Furthermore, the method of moments can be viewed as complementary to the maximum likelihood approach; simply taking a single step of Newton-Raphson on the likelihood function starting from the moment based estimator often leads to the best of both worlds: a computationally efficient estimator that is (asymptotically) statistically optimal.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary difficulty in learning latent variable models is that the latent (hidden) state of the data is not directly observed; rather only observed variables correlated with the hidden state are observed. As such, it is not evident the method of moments should fare any better than maximum likelihood in terms of computational performance: matching the model parameters to the observed moments may involve solving computationally intractable systems of multivariate polynomial equations. Fortunately, for many classes of latent variable models, there is rich structure in low-order moments (typically second- and third-order) which allow for this inverse moment problem to be solved efficiently. What is more is that these decomposition problems are often amenable to simple and efficient iterative methods, such as gradient descent and the power iteration method.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this work, we observe that a number of important and well-studied latent variable models---including Gaussian mixture models, hidden Markov models, and Latent Dirichlet allocation---share a certain structure in their low-order moments, and this permits certain tensor decomposition approaches to parameter estimation. In particular, this decomposition can be viewed as a natural generalization of the singular value decomposition for matrices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

While much of this (or similar) structure was implicit in several previous works, here we make the decomposition explicit under a unified framework. Specifically, we express the observable moments as sums of rank-one terms, and reduce the parameter estimation task to the problem of extracting a symmetric orthogonal decomposition of a symmetric tensor derived from these observable moments. The problem can then be solved by a variety of approaches, including fixed-point and variational methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

One approach for obtaining the orthogonal decomposition is the tensor power method of Lathauwer et al.. We provide a convergence analysis of this method for orthogonally decomposable symmetric tensors, as well as a detailed perturbation analysis for a robust (and a computationally tractable) variant (Theorem 5.1). This perturbation analysis can be viewed as an analogue of Wedin's perturbation theorem for singular vectors of matrices, providing a bound on the error of the recovered decomposition in terms of the operator norm of the tensor perturbation. This analysis is subtle in at least two ways. First, unlike for matrices (where every matrix has a singular value decomposition), an orthogonal decomposition need not exist for the perturbed tensor. Our robust variant uses random restarts and deflation to extract an approximate decomposition in a computationally tractable manner. Second, the analysis of the deflation steps is non-trivial; a naïve argument would entail error accumulation in each deflation step, which we show can in fact be avoided. When this method is applied for parameter estimation in latent variable models previously discussed, improved sample complexity bounds (over previous work) can be obtained using this perturbation analysis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Finally, we also address computational issues that arise when applying the tensor decomposition approaches to estimating latent variable models. Specifically, we show that the basic operations of simple iterative approaches (such as the tensor power method) can be efficiently executed in time linear in the dimension of the observations and the size of the training data. For instance, in a topic modeling application, the proposed methods require time linear in the number of words in the vocabulary and in the number of non-zero entries of the term-document matrix. The combination of this computational efficiency and the robustness of the tensor decomposition techniques makes the overall framework a promising approach to parameter estimation for latent variable models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

The role of tensor decompositions in the context of latent variable models dates back to early uses in psychometrics. These ideas later gained popularity in chemometrics, and more recently in numerous science and engineering disciplines, including neuroscience, phylogenetics, signal processing, data mining, and computer vision. A thorough survey of these techniques and applications is given by Kolda and Bader. Below, we discuss a few specific connections to two applications in machine learning and statistics, independent component analysis and latent variable models (between which there is also significant overlap).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

Tensor decompositions have been used in signal processing and computational neuroscience for blind source separation and independent component analysis (ICA). Here, statistically independent non-Gaussian sources are linearly mixed in the observed signal, and the goal is to recover the mixing matrix (and ultimately, the original source signals). A typical solution is to locate projections of the observed signals that correspond to local extrema of the so-called "contrast functions" which distinguish Gaussian variables from non-Gaussian variables. This method can be effectively implemented using fast descent algorithms. When using the excess kurtosis (*i.e.*, fourth-order cumulant) as the contrast function, this method reduces to a generalization of the power method for symmetric tensors. This case is particularly important, since all local extrema of the kurtosis objective correspond to the true sources (under the assumed statistical model); the descent methods can therefore be rigorously analyzed, and their computational and statistical complexity can be bounded.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

Higher-order tensor decompositions have also been used to develop estimators for commonly used mixture models, hidden Markov models, and other related latent variable models, often using the the algebraic procedure of R. Jennrich, which is based on a simultaneous diagonalization of different ways of flattening a tensor to matrices. Jennrich's procedure was employed for parameter estimation of discrete Markov models by Chang via pair-wise and triple-wise probability tables; and it was later used for other latent variable models such as hidden Markov models (HMMs), latent trees, Gaussian mixture models, and topic models such as latent Dirichlet allocation (LDA) by many others. In these contexts, it is often also possible to establish strong identifiability results, without giving an explicit estimators, by invoking the non-constructive identifiability argument of Kruskal ---see the article by Allman et al. for several examples.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

Related simultaneous diagonalization approaches have also been used for blind source separation and ICA (as discussed above), and a number of efficient algorithms have been developed for this problem. A rather different technique that uses tensor flattening and matrix eigenvalue decomposition has been developed by Cardoso and later by De Lathauwer et al.. A significant advantage of this technique is that it can be used to estimate overcomplete mixtures, where the number of sources is larger than the observed dimension.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

The relevance of tensor analysis to latent variable modeling has been long recognized in the field of algebraic statistics, and many works characterize the algebraic varieties corresponding to the moments of various classes of latent variable models. These works typically do not address computational or finite sample issues, but rather are concerned with basic questions of identifiability.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

The specific tensor structure considered in the present work is the symmetric orthogonal decomposition. This decomposition expresses a tensor as a linear combination of simple tensor forms; each form is the tensor product of a vector (*i.e.*, a rank-$1$ tensor), and the collection of vectors form an orthonormal basis. An important property of tensors with such decompositions is that they have eigenvectors corresponding to these basis vectors. Although the concepts of eigenvalues and eigenvectors of tensors is generally significantly more complicated than their matrix counterpart---both algebraically and computationally ---the special symmetric orthogonal structure we consider permits simple algorithms to efficiently and stably recover the desired decomposition. In particular, a generalization of the matrix power method to symmetric tensors, introduced by Lathauwer et al. and analyzed by Kofidis and Regalia, provides such a decomposition. This is in fact implied by the characterization of Zhang and Golub, which shows that iteratively obtaining the best rank-$1$ approximation of such orthogonally decomposable tensors also yields the exact decomposition.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tensor Decompositions", "weight": 1.0} -->

We note that in general, obtaining such approximations for general (symmetric) tensors is NP-hard.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Latent Variable Models", "weight": 1.0} -->

This work focuses on the particular application of tensor decomposition methods to estimating latent variable models, a significant departure from many previous approaches in the machine learning and statistics literature. By far the most popular heuristic for parameter estimation for such models is the Expectation-Maximization (EM) algorithm. Although EM has a number of merits, it may suffer from slow convergence and poor quality local optima, requiring practitioners to employ many additional heuristics to obtain good solutions. For some models such as latent trees and topic models, maximum likelihood estimation is NP-hard, which suggests that other estimation approaches may be more attractive.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Latent Variable Models", "weight": 1.0} -->

More recently, algorithms from theoretical computer science and machine learning have addressed computational and sample complexity issues related to estimating certain latent variable models such as Gaussian mixture models and HMMs (Dasgupta, 1999; Arora and Kannan, 2005; Dasgupta and Schulman, 2007; Vempala and Wang, 2004; Kannan et al., 2008; Achlioptas and McSherry, 2005; Chaudhuri and Rao, 2008; Brubaker and Vempala, 2008; Kalai et al., 2010; Belkin and Sinha, 2010; Moitra and Valiant, 2010; Hsu and Kakade, 2013; Chang, 1996; Mossel and Roch, 2006; Hsu et al., 2012b; Anandkumar et al., 2012c; Arora et al., 2012a; Anandkumar et al., 2012a). See the works by Anandkumar et al. and Hsu and Kakade for a discussion of these methods, together with the computational and statistical hardness barriers that they face.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Latent Variable Models", "weight": 1.0} -->

The present work reviews a broad range of latent variables where a mild non-degeneracy condition implies the symmetric orthogonal decomposition structure in the tensors of low-order observable moments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Latent Variable Models", "weight": 1.0} -->

Notably, another class of methods, based on subspace identification and observable operator models/multiplicity automata, have been proposed for a number of latent variable models. These methods were successfully developed for HMMs by Hsu et al., and subsequently generalized and extended for a number of related sequential and tree Markov models models, as well as certain classes of parse tree models. These methods use low-order moments to learn an "operator" representation of the distribution, which can be used for density estimation and belief state updates. While finite sample bounds can be given to establish the learnability of these models, the algorithms do not actually give parameter estimates (*e.g.*, of the emission or transition matrices in the case of HMMs).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Organization", "weight": 1.0} -->

The rest of the paper is organized as follows. Section 2 reviews some basic definitions of tensors. Section 3 provides examples of a number of latent variable models which, after appropriate manipulations of their low order moments, share a certain natural tensor structure. Section 4 reduces the problem of parameter estimation to that of extracting a certain (symmetric orthogonal) decomposition of a tensor. We then provide a detailed analysis of a robust tensor power method and establish an analogue of Wedin's perturbation theorem for the singular vectors of matrices. The discussion in Section 6 addresses a number of practical concerns that arise when dealing with moment matrices and tensors.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Tensor Structure in Latent Variable Models", "weight": 1.0} -->

In this section, we give several examples of latent variable models whose low-order moments can be written as symmetric tensors of low symmetric rank; some of these examples can be deduced using the techniques developed in the text by McCullagh. The basic form is demonstrated in Theorem 3.1 ‣ 3.1 Exchangeable Single Topic Models ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models") for the first example, and the general pattern will emerge from subsequent examples.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

We first consider a simple bag-of-words model for documents in which the words in the document are assumed to be *exchangeable*. Recall that a collection of random variables $x_{1},x_{2},\ldots,x_{\ell}$ are exchangeable if their joint probability distribution is invariant to permutation of the indices. The well-known De Finetti's theorem implies that such exchangeable models can be viewed as mixture models in which there is a latent variable $h$ such that $x_{1},x_{2},\ldots,x_{\ell}$ are conditionally i.i.d. given $h$ (see Figure 1(a) for the corresponding graphical model) and the conditional distributions are identical at all the nodes.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

In our simplified topic model for documents, the latent variable $h$ is interpreted as the (sole) topic of a given document, and it is assumed to take only a finite number of distinct values. Let $k$ be the number of distinct topics in the corpus, $d$ be the number of distinct words in the vocabulary, and $\ell \geq 3$ be the number of words in each document. The generative process for a document is as follows: the document's topic is drawn according to the discrete distribution specified by the probability vector $w:={(w_{1},w_{2},\ldots,w_{k})} \in \Delta^{k - 1}$. This is modeled as a discrete random variable $h$ such that Given the topic $h$, the document's $\ell$ words are drawn independently according to the discrete distribution specified by the probability vector $\mu_{h} \in \Delta^{d - 1}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

It will be convenient to represent the $\ell$ words in the document by $d$-dimensional random *vectors* ${x_{1},x_{2},\ldots,x_{\ell}} \in {\mathbb{R}}^{d}$. Specifically, we set where $e_{1},e_{2},{\ldotse_{d}}$ is the standard coordinate basis for ${\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

One advantage of this encoding of words is that the (cross) moments of these random vectors correspond to joint probabilities over words. For instance, observe that so the $(i,j)$-the entry of the matrix ${\mathbb{E}}{\lbrack{x_{1} \otimes x_{2}}\rbrack}$ is $\Pr{\lbrack{{1\text{st word}} = i},{{2\text{nd word}} = j}\rbrack}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

More generally, the $(i_{1},i_{2},\ldots,i_{\ell})$-th entry in the tensor ${\mathbb{E}}{\lbrack{x_{1} \otimes x_{2} \otimes \cdots \otimes x_{\ell}}\rbrack}$ is $\Pr{\lbrack{{1\text{st word}} = i_{1}},{{2\text{nd word}} = i_{2}},\ldots,{{\ell\text{-th word}} = i_{\ell}}\rbrack}$. This means that estimating cross moments, say, of $x_{1} \otimes x_{2} \otimes x_{3}$, is the same as estimating joint probabilities of the first three words over all documents. (Recall that we assume that each document has at least three words.)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Exchangeable Single Topic Models", "weight": 1.0} -->

The second advantage of the vector encoding of words is that the conditional expectation of $x_{t}$ given $h = j$ is simply $\mu_{j}$, the vector of word probabilities for topic $j$: (where ${\lbrack\mu_{j}\rbrack}_{i}$ is the $i$-th entry in the vector $\mu_{j}$). Because the words are conditionally independent given the topic, we can use this same property with conditional cross moments, say, of $x_{1}$ and $x_{2}$: This and similar calculations lead one to the following theorem.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Beyond Raw Moments", "weight": 1.0} -->

In the single topic model above, the raw (cross) moments of the observed words directly yield the desired symmetric tensor structure. In some other models, the raw moments do not explicitly have this form. Here, we show that the desired tensor structure can be found through various manipulations of different moments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spherical Gaussian Mixtures: Common Covariance", "weight": 1.0} -->

We now consider a mixture of $k$ Gaussian distributions with spherical covariances. We start with the simpler case where all of the covariances are identical; this probabilistic model is closely related to the (non-probabilistic) $k$-means clustering problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Spherical Gaussian Mixtures: Common Covariance", "weight": 1.0} -->

Let $w_{i} \in {}$ be the probability of choosing component $i \in {\lbrack k\rbrack}$, ${\{\mu_{1},\mu_{2},\ldots,\mu_{k}\}} \subset {\mathbb{R}}^{d}$ be the component mean vectors, and $\sigma^{2}I$ be the common covariance matrix. An observation in this model is given by where $h$ is the discrete random variable with ${\Pr{\lbrack{h = i}\rbrack}} = w_{i}$ for $i \in {\lbrack k\rbrack}$ (similar to the exchangeable single topic model), and $z \sim {\mathcal{N}{(0,{\sigma^{2}I})}}$ is an independent multivariate Gaussian random vector in ${\mathbb{R}}^{d}$ with zero mean and spherical covariance $\sigma^{2}I$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Spherical Gaussian Mixtures: Common Covariance", "weight": 1.0} -->

The Gaussian mixture model differs from the exchangeable single topic model in the way observations are generated. In the single topic model, we observe multiple draws (words in a particular document) $x_{1},x_{2},\ldots,x_{\ell}$ given the same fixed $h$ (the topic of the document). In contrast, for the Gaussian mixture model, every realization of $x$ corresponds to a different realization of $h$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Spherical Gaussian Mixtures: Differing Covariances", "weight": 1.0} -->

The general case is where each component may have a *different* spherical covariance. An observation in this model is again $x = {\mu_{h} + z}$, but now $z \in {\mathbb{R}}^{d}$ is a random vector whose conditional distribution given $h = i$ (for some $i \in {\lbrack k\rbrack}$) is a multivariate Gaussian $\mathcal{N}{(0,{\sigma_{i}^{2}I})}$ with zero mean and spherical covariance $\sigma_{i}^{2}I$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Independent Component Analysis (ICA)", "weight": 1.0} -->

The standard model for ICA, in which independent signals are linearly mixed and corrupted with Gaussian noise before being observed, is specified as follows. Let $h \in {\mathbb{R}}^{k}$ be a latent random *vector* with independent coordinates, $A \in {\mathbb{R}}^{d \times k}$ the mixing matrix, and $z$ be a multivariate Gaussian random vector. The random vectors $h$ and $z$ are assumed to be independent. The observed random vector is Let $\mu_{i}$ denote the $i$-th column of the mixing matrix $A$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Latent Dirichlet Allocation (LDA)", "weight": 1.0} -->

An increasingly popular class of latent variable models are *mixed membership models*, where each datum may belong to several different latent classes simultaneously. LDA is one such model for the case of document modeling; here, each document corresponds to a mixture over topics (as opposed to just a single topic).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Latent Dirichlet Allocation (LDA)", "weight": 1.0} -->

To generate a document, we first draw the topic mixture $h = {(h_{1},h_{2},\ldots,h_{k})} \sim {{Dir}{(\alpha)}}$, and then conditioned on $h$, we draw $\ell$ words $x_{1},x_{2},\ldots,x_{\ell}$ independently from the discrete distribution specified by the probability vector $\sum_{i = 1}^{k}{h_{i}\mu_{i}}$ (*i.e.*, for each $x_{t}$, we independently sample a topic $j$ according to $h$ and then sample $x_{t}$ according to $\mu_{j}$). Again, we encode a word $x_{t}$ by setting $x_{t} = e_{i}$ iff the $t$-th word in the document is $i$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Latent Dirichlet Allocation (LDA)", "weight": 1.0} -->

The parameter $\alpha_{0}$ (the sum of the "pseudo-counts") characterizes the concentration of the distribution. As $\alpha_{0}\rightarrow 0$, the distribution degenerates to a single topic model (*i.e.*, the limiting density has, with probability $1$, exactly one entry of $h$ being $1$ and the rest are $0$). At the other extreme, if $\alpha = {(c,c,\ldots,c)}$ for some scalar $c > 0$, then as $\alpha_{0} = {ck}\rightarrow\infty$, the distribution of $h$ becomes peaked around the uniform vector $({1/k},{1/k},\ldots,{1/k})$ (furthermore, the distribution behaves like a product distribution). We are typically interested in the case where $\alpha_{0}$ is small (*e.g.*, a constant independent of $k$), whereupon $h$ typically has only a few large entries.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Latent Dirichlet Allocation (LDA)", "weight": 1.0} -->

This corresponds to the setting where the documents are mainly comprised of just a few topics.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multi-View Models", "weight": 1.0} -->

(b) Hidden Markov model Figure 1: Examples of latent variable models.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Multi-View Models", "weight": 1.0} -->

Multi-view models (also sometimes called naïve Bayes models) are a special class of Bayesian networks in which observed variables $x_{1},x_{2},\ldots,x_{\ell}$ are conditionally independent given a latent variable $h$. This is similar to the exchangeable single topic model, but here we do not require the conditional distributions of the ${x_{t},t} \in {\lbrack\ell\rbrack}$ to be identical. Techniques developed for this class can be used to handle a number of widely used models including hidden Markov models, phylogenetic tree models, certain tree mixtures, and certain probabilistic grammar models.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Multi-View Models", "weight": 1.0} -->

Thus, we allow the observations $x_{1},x_{2},\ldots,x_{\ell}$ to be random vectors, parameterized only by their conditional means. Importantly, these conditional distributions may be discrete, continuous, or even a mix of both.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Multi-View Models", "weight": 1.0} -->

We first note the form for the raw (cross) moments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Mixtures of Axis-Aligned Gaussians and Other Product Distributions", "weight": 1.0} -->

The first example is a mixture of $k$ product distributions in ${\mathbb{R}}^{n}$ under a mild incoherence assumption. Here, we allow each of the $k$ component distributions to have a different product distribution (*e.g.*, Gaussian distribution with an axis-aligned covariance matrix), but require the matrix of component means $A:={\lbrack\left. {\mu_{1}{|\mu_{2}|}\cdots} \middle| \mu_{k} \right.\rbrack} \in {\mathbb{R}}^{n \times k}$ to satisfy a certain (very mild) incoherence condition. The role of the incoherence condition is explained below.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Mixtures of Axis-Aligned Gaussians and Other Product Distributions", "weight": 1.0} -->

For a mixture of product distributions, any partitioning of the dimensions $\lbrack n\rbrack$ into three groups creates three (possibly asymmetric) "views" which are conditionally independent once the mixture component is selected. However, recall that Theorem 3.6 ‣ 3.3 Multi-View Models ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models") requires that for each view, the $k$ conditional means be linearly independent. In general, this may not be achievable; consider, for instance, the case $\mu_{i} = e_{i}$ for each $i \in {\lbrack k\rbrack}$. Such cases, where the component means are very aligned with the coordinate basis, are precluded by the incoherence condition.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Mixtures of Axis-Aligned Gaussians and Other Product Distributions", "weight": 1.0} -->

Define ${{coherence}{(A)}}:={\max_{i \in {\lbrack n\rbrack}}{\{{e_{i}^{\top}\Pi_{A}e_{i}}\}}}$ to be the largest diagonal entry of the orthogonal projector to the range of $A$, and assume $A$ has rank $k$. The coherence lies between $k/n$ and $1$; it is largest when the range of $A$ is spanned by the coordinate axes, and it is $k/n$ when the range is spanned by a subset of the Hadamard basis of cardinality $k$. The incoherence condition requires, for some ${\varepsilon,\delta} \in {}$, ${{coherence}{(A)}} \leq {{({\varepsilon^{2}/6})}/{\ln{({{3k}/\delta})}}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Mixtures of Axis-Aligned Gaussians and Other Product Distributions", "weight": 1.0} -->

Essentially, this condition ensures that the non-degeneracy of the component means is not isolated in just a few of the $n$ dimensions. Operationally, it implies the following.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Spherical Gaussian Mixtures, Revisited", "weight": 1.0} -->

Consider again the case of spherical Gaussian mixtures (*cf*. Section 3.2). As we shall see in Section 4.3, the previous techniques (based on Theorem 3.2 ‣ 3.2.1 Spherical Gaussian Mixtures: Common Covariance ‣ 3.2 Beyond Raw Moments ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models") and Theorem 3.3 ‣ 3.2.2 Spherical Gaussian Mixtures: Differing Covariances ‣ 3.2 Beyond Raw Moments ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models")) lead to estimation procedures when the dimension of $x$ is $k$ or greater (and when the $k$ component means are linearly independent). We now show that when the dimension is slightly larger, say greater than $3k$, a different (and simpler) technique based on the multi-view structure can be used to extract the relevant structure.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Spherical Gaussian Mixtures, Revisited", "weight": 1.0} -->

We again use a randomized reduction. Specifically, we create three views by (i) applying a random rotation to $x$, and then (ii) partitioning $x \in {\mathbb{R}}^{n}$ into three views ${{\overset{\sim}{x}}_{1},{\overset{\sim}{x}}_{2},{\overset{\sim}{x}}_{3}} \in {\mathbb{R}}^{d}$ for $d:={n/3}$. By the rotational invariance of the multivariate Gaussian distribution, the distribution of $x$ after random rotation is still a mixture of spherical Gaussians (*i.e.*, a mixture of product distributions), and thus ${\overset{\sim}{x}}_{1},{\overset{\sim}{x}}_{2},{\overset{\sim}{x}}_{3}$ are conditionally independent given $h$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Spherical Gaussian Mixtures, Revisited", "weight": 1.0} -->

What remains to be checked is that, for each view $t \in {\{ 1,2,3\}}$, the matrix of conditional means of ${\overset{\sim}{x}}_{t}$ for each view has full column rank. This is true with probability $1$ as long as the matrix of conditional means $A:={\lbrack\left. {\mu_{1}{|\mu_{2}|}\cdots} \middle| \mu_{k} \right.\rbrack} \in {\mathbb{R}}^{n \times k}$ has rank $k$ and $n \geq {3k}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Spherical Gaussian Mixtures, Revisited", "weight": 1.0} -->

To see this, observe that a random rotation in ${\mathbb{R}}^{n}$ followed by a restriction to $d$ coordinates is simply a random projection from ${\mathbb{R}}^{n}$ to ${\mathbb{R}}^{d}$, and that a random projection of a linear subspace of dimension $k$ to ${\mathbb{R}}^{d}$ is almost surely injective as long as $d \geq k$. Applying this observation to the range of $A$ implies the following.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Hidden Markov Models", "weight": 1.0} -->

Our last example is the time-homogeneous HMM for sequences of vector-valued observations ${x_{1},x_{2},\ldots} \in {\mathbb{R}}^{d}$. Consider a Markov chain of discrete hidden states $y_{1}\rightarrow y_{2}\rightarrow y_{3}\rightarrow\cdots$ over $k$ possible states $\lbrack k\rbrack$; given a state $y_{t}$ at time $t$, the observation $x_{t}$ at time $t$ (a random vector taking values in ${\mathbb{R}}^{d}$) is independent of all other observations and hidden states. See Figure 1(b).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Hidden Markov Models", "weight": 1.0} -->

Let $\pi \in \Delta^{k - 1}$ be the initial state distribution (*i.e.*, the distribution of $y_{1}$), and $T \in {\mathbb{R}}^{k \times k}$ be the stochastic transition matrix for the hidden state Markov chain: for all times $t$, Finally, let $O \in {\mathbb{R}}^{d \times k}$ be the matrix whose $j$-th column is the conditional expectation of $x_{t}$ given $y_{t} = j$: for all times $t$,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Orthogonal Tensor Decompositions", "weight": 1.0} -->

We now show how recovering the $\mu_{i}$'s in our aforementioned problems reduces to the problem of finding a certain orthogonal tensor decomposition of a symmetric tensor. We start by reviewing the spectral decomposition of symmetric matrices, and then discuss a generalization to the higher-order tensor case. Finally, we show how orthogonal tensor decompositions can be used for estimating the latent variable models from the previous section.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Review: The Matrix Case", "weight": 1.0} -->

We first build intuition by reviewing the matrix setting, where the desired decomposition is the eigendecomposition of a symmetric rank-$k$ matrix $M = {V\LambdaV^{\top}}$, where $V = {\lbrack\left. {v_{1}{|v_{2}|}\cdots} \middle| v_{k} \right.\rbrack} \in {\mathbb{R}}^{n \times k}$ is the matrix with orthonormal eigenvectors as columns, and $\Lambda = {{diag}{(\lambda_{1},\lambda_{2},\ldots,\lambda_{k})}} \in {\mathbb{R}}^{k \times k}$ is diagonal matrix of non-zero eigenvalues. In other words, Such a decomposition is guaranteed to exist for every symmetric matrix.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Review: The Matrix Case", "weight": 1.0} -->

Recovery of the $v_{i}$'s and $\lambda_{i}$'s can be viewed at least two ways. First, each $v_{i}$ is fixed under the mapping $u\mapsto{Mu}$, up to a scaling factor $\lambda_{i}$: as ${v_{j}^{\top}v_{i}} = 0$ for all $j \neq i$ by orthogonality. The $v_{i}$'s are not necessarily the only such fixed points. For instance, with the multiplicity $\lambda_{1} = \lambda_{2} = \lambda$, then any linear combination of $v_{1}$ and $v_{2}$ is similarly fixed under $M$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Review: The Matrix Case", "weight": 1.0} -->

The second view of recovery is via the variational characterization of the eigenvalues. Assume $\lambda_{1} > \lambda_{2} > \cdots > \lambda_{k}$; the case of repeated eigenvalues again leads to similar non-uniqueness as discussed above. Then the *Rayleigh quotient* is maximized over non-zero vectors by $v_{1}$. Furthermore, for any $s \in {\lbrack k\rbrack}$, the maximizer of the Rayleigh quotient, subject to being orthogonal to $v_{1},v_{2},\ldots,v_{s - 1}$, is $v_{s}$. Another way of obtaining this second statement is to consider the *deflated* Rayleigh quotient and observe that $v_{s}$ is the maximizer.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Review: The Matrix Case", "weight": 1.0} -->

Efficient algorithms for finding these matrix decompositions are well studied, and iterative power methods are one effective class of algorithms.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Tensor Case", "weight": 1.0} -->

Decomposing general tensors is a delicate issue; tensors may not even have unique decompositions. Fortunately, the orthogonal tensors that arise in the aforementioned models have a structure which permits a unique decomposition under a mild non-degeneracy condition. We focus our attention to the case $p = 3$, *i.e.*, a third order tensor; the ideas extend to general $p$ with minor modifications.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Tensor Case", "weight": 1.0} -->

An *orthogonal decomposition* of a symmetric tensor $T \in {\bigotimes^{3}{\mathbb{R}}^{n}}$ is a collection of orthonormal (unit) vectors $\{ v_{1},v_{2},\ldots,v_{k}\}$ together with corresponding positive scalars $\lambda_{i} > 0$ such that Note that since we are focusing on odd-order tensors ($p = 3$), we have added the requirement that the $\lambda_{i}$ be positive. This convention can be followed without loss of generality since ${- {\lambda_{i}v_{i}^{\otimes p}}} = {\lambda_{i}{({- v_{i}})}^{\otimes p}}$ whenever $p$ is odd. Also, it should be noted that orthogonal decompositions do not necessarily exist for every symmetric tensor.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Tensor Case", "weight": 1.0} -->

In analogy to the matrix setting, we consider two ways to view this decomposition: a fixed-point characterization and a variational characterization. Related characterizations based on optimal rank-$1$ approximations are given by Zhang and Golub.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Fixed-Point Characterization", "weight": 1.0} -->

For a tensor $T$, consider the vector-valued map which is the third-order generalization of. This can be explicitly written as Observe that is *not* a linear map, which is a key difference compared to the matrix case.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Fixed-Point Characterization", "weight": 1.0} -->

An eigenvector $u$ for a matrix $M$ satisfies ${M{(I,u)}} = {\lambdau}$, for some scalar $\lambda$. We say a unit vector $u \in {\mathbb{R}}^{n}$ is an *eigenvector* of $T$, with corresponding *eigenvalue* $\lambda \in {\mathbb{R}}$, if (To simplify the discussion, we assume throughout that eigenvectors have unit norm; otherwise, for scaling reasons, we replace the above equation with ${T{(I,u,u)}} = {\lambda{\| u\|}u}$.) This concept was originally introduced by Lim and Qi.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Fixed-Point Characterization", "weight": 1.0} -->

There are a number of subtle differences compared to the matrix case that arise as a result of the non-linearity of. First, even with the multiplicity $\lambda_{1} = \lambda_{2} = \lambda$, a linear combination $u:={{c_{1}v_{1}} + {c_{2}v_{2}}}$ may *not* be an eigenvector. In particular, may not be a multiple of ${c_{1}v_{1}} + {c_{2}v_{2}}$. This indicates that the issue of repeated eigenvalues does not have the same status as in the matrix case. Second, even if all the eigenvalues are distinct, it turns out that the $v_{i}$'s are not the only eigenvectors. For example, set $u:={{{({1/\lambda_{1}})}v_{1}} + {{({1/\lambda_{2}})}v_{2}}}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Fixed-Point Characterization", "weight": 1.0} -->

Then, so $u/{\| u\|}$ is an eigenvector. More generally, for any subset $S \subseteq {\lbrack k\rbrack}$, the vector As we now see, these additional eigenvectors can be viewed as spurious. We say a unit vector $u$ is a *robust eigenvector* of $T$ if there exists an $\epsilon > 0$ such that for all $\theta \in {\{{u' \in {\mathbb{R}}^{n}}:{{\|{u' - u}\|} \leq \epsilon}\}}$, repeated iteration of the map starting from $\theta$ converges to $u$. Note that the map rescales the output to have unit Euclidean norm. Robust eigenvectors are also called attracting fixed points of.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Fixed-Point Characterization", "weight": 1.0} -->

The following theorem implies that if $T$ has an orthogonal decomposition as given, then the set of robust eigenvectors of $T$ are precisely the set $\{ v_{1},v_{2},{\ldotsv_{k}}\}$, implying that the orthogonal decomposition is unique. (For even order tensors, the uniqueness is true up to sign-flips of the $v_{i}$.)

<!-- chunk {"id": "body-0065", "role": "body", "section": "Variational Characterization", "weight": 1.0} -->

We now discuss a variational characterization of the orthogonal decomposition. The *generalized Rayleigh quotient* for a third-order tensor is which can be compared to. For an orthogonally decomposable tensor, the following theorem shows that a non-zero vector $u \in {\mathbb{R}}^{n}$ is an *isolated local maximizer* of the generalized Rayleigh quotient if and only if $u = v_{i}$ for some $i \in {\lbrack k\rbrack}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Estimation via Orthogonal Tensor Decompositions", "weight": 1.0} -->

We now demonstrate how the moment tensors obtained for various latent variable models in Section 3 can be reduced to an orthogonal form. For concreteness, we take the specific form from the exchangeable single topic model (Theorem 3.1 ‣ 3.1 Exchangeable Single Topic Models ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models")): (The more general case allows the weights $w_{i}$ in $M_{2}$ to differ in $M_{3}$, but for simplicity we keep them the same in the following discussion.) We now show how to reduce these forms to an orthogonally decomposable tensor from which the $w_{i}$ and $\mu_{i}$ can be recovered. See Appendix D for a discussion as to how previous approaches achieved this decomposition through a certain simultaneous diagonalization method.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Estimation via Orthogonal Tensor Decompositions", "weight": 1.0} -->

Throughout, we assume the following non-degeneracy condition.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Condition 4.1 (Non-degeneracy)", "weight": 1.0} -->

Observe that Condition 4.1 ‣ 4.3 Estimation via Orthogonal Tensor Decompositions ‣ 4 Orthogonal Tensor Decompositions ‣ Tensor Decompositions for Learning Latent Variable Models") implies that $M_{2} \succeq 0$ is positive semidefinite and has rank $k$. This is often a mild condition in applications. When this condition is not met, learning is conjectured to be generally hard for both computational and information-theoretic reasons. As discussed by Hsu et al. and Hsu and Kakade, when the non-degeneracy condition does not hold, it is often possible to combine multiple observations using tensor products to increase the rank of the relevant matrices. Indeed, this observation has been rigorously formulated in very recent works of Bhaskara et al. and Anderson et al. using the framework of smoothed analysis.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The Reduction", "weight": 1.0} -->

First, let $W \in {\mathbb{R}}^{d \times k}$ be a linear transformation such that where $I$ is the $k \times k$ identity matrix (*i.e.*, $W$ whitens $M_{2}$). Since $M_{2} \succeq 0$, we may for concreteness take $W:={UD^{- {1/2}}}$, where $U \in {\mathbb{R}}^{d \times k}$ is the matrix of orthonormal eigenvectors of $M_{2}$, and $D \in {\mathbb{R}}^{k \times k}$ is the diagonal matrix of positive eigenvalues of $M_{2}$. Let so the ${\overset{\sim}{\mu}}_{i} \in {\mathbb{R}}^{k}$ are orthonormal vectors.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The Reduction", "weight": 1.0} -->

Now define ${\overset{\sim}{M}}_{3}:={M_{3}{(W,W,W)}} \in {\mathbb{R}}^{k \times k \times k}$, so that As the following theorem shows, the orthogonal decomposition of ${\overset{\sim}{M}}_{3}$ can be obtained by identifying its robust eigenvectors, upon which the original parameters $w_{i}$ and $\mu_{i}$ can be recovered. For simplicity, we only state the result in terms of robust eigenvector/eigenvalue pairs; one may also easily state everything in variational form using Theorem 4.2.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Local Maximizers of (Cross Moment) Skewness", "weight": 1.0} -->

The variational characterization provides an interesting perspective on the robust eigenvectors for these latent variable models. Consider the exchangeable single topic models (Theorem 3.1 ‣ 3.1 Exchangeable Single Topic Models ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models")), and the objective function In this case, every local maximizer $u^{\ast}$ satisfies ${M_{2}{(I,u^{\ast})}} = {\sqrt{w_{i}}\mu_{i}}$ for some $i \in {\lbrack k\rbrack}$. The objective function can be interpreted as the (cross moment) skewness of the random vectors $x_{1},x_{2},x_{3}$ along direction $u$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Tensor Power Method", "weight": 1.0} -->

In this section, we consider the tensor power method of Lathauwer et al. for orthogonal tensor decomposition. We first state a simple convergence analysis for an orthogonally decomposable tensor $T$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Tensor Power Method", "weight": 1.0} -->

When only an approximation $\hat{T}$ to an orthogonally decomposable tensor $T$ is available (*e.g.*, when empirical moments are used to estimate population moments), an orthogonal decomposition need not exist for this perturbed tensor (unlike for the case of matrices), and a more robust approach is required to extract the approximate decomposition. Here, we propose such a variant in Algorithm 1 and provide a detailed perturbation analysis. We note that alternative approaches such as simultaneous diagonalization can also be employed (see Appendix D).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Convergence Analysis for Orthogonally Decomposable Tensors", "weight": 1.0} -->

The following lemma establishes the quadratic convergence of the tensor power method---*i.e.*, repeated iteration of ---for extracting a single component of the orthogonal decomposition. Note that the initial vector $\theta_{0}$ determines which robust eigenvector will be the convergent point. Computation of subsequent eigenvectors can be computed with deflation, *i.e.*, by subtracting appropriate terms from $T$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Perturbation Analysis of a Robust Tensor Power Method", "weight": 1.0} -->

Now we consider the case where we have an approximation $\hat{T}$ to an orthogonally decomposable tensor $T$. Here, a more robust approach is required to extract an approximate decomposition. We propose such an algorithm in Algorithm 1, and provide a detailed perturbation analysis. For simplicity, we assume the tensor $\hat{T}$ is of size $k \times k \times k$ as per the reduction from Section 4.3. In some applications, it may be preferable to work directly with a $n \times n \times n$ tensor of rank $k \leq n$ (as in Lemma 5.1); our results apply in that setting with little modification.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Perturbation Analysis of a Robust Tensor Power Method", "weight": 1.0} -->

0: symmetric tensor $\overset{\sim}{T} \in {\mathbb{R}}^{k \times k \times k}$, number of iterations L, N. 0: the estimated eigenvector/eigenvalue pair; the deflated tensor. 2: Draw θ0(τ) uniformly at random from the unit sphere in ℝk.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Perturbation Analysis of a Robust Tensor Power Method", "weight": 1.0} -->

8: Do N power iteration updates starting from θN(τ*) to obtain θ̂, and set $\hat{\lambda}:={\overset{\sim}{T}{(\hat{\theta},\hat{\theta},\hat{\theta})}}$. 9: return the estimated eigenvector/eigenvalue pair (θ̂, λ̂); the deflated tensor $\overset{\sim}{T} - {\hat{\lambda}{\hat{\theta}}^{\otimes 3}}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Perturbation Analysis of a Robust Tensor Power Method", "weight": 1.0} -->

Algorithm 1 Robust tensor power method Assume that the symmetric tensor $T \in {\mathbb{R}}^{k \times k \times k}$ is orthogonally decomposable, and that $\hat{T} = {T + E}$, where the perturbation $E \in {\mathbb{R}}^{k \times k \times k}$ is a symmetric tensor with small operator norm: In our latent variable model applications, $\hat{T}$ is the tensor formed by using empirical moments, while $T$ is the orthogonally decomposable tensor derived from the population moments for the given model. In the context of parameter estimation (as in Section 4.3), $E$ must account for any error amplification throughout the reduction, such as in the whitening step.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Perturbation Analysis of a Robust Tensor Power Method", "weight": 1.0} -->

The following theorem is similar to Wedin's perturbation theorem for singular vectors of matrices in that it bounds the error of the (approximate) decomposition returned by Algorithm 1 on input $\hat{T}$ in terms of the size of the perturbation, provided that the perturbation is small enough.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we discuss some practical and application-oriented issues related to the tensor decomposition approach to learning latent variable models.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Practical Implementation Considerations", "weight": 1.0} -->

A number of practical concerns arise when dealing with moment matrices and tensors. Below, we address two issues that are especially pertinent to topic modeling applications or other settings where the observations are sparse.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Efficient Moment Representation for Exchangeable Models", "weight": 1.0} -->

In an exchangeable bag-of-words model, it is assumed that the words $x_{1},x_{2},\ldots,x_{\ell}$ in a document are conditionally i.i.d. given the topic $h$. This allows one to estimate $p$-th order moments using just $p$ words per document. The estimators obtained via Theorem 3.1 ‣ 3.1 Exchangeable Single Topic Models ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models") (single topic model) and Theorem 3.5 ‣ 3.2.4 Latent Dirichlet Allocation (LDA) ‣ 3.2 Beyond Raw Moments ‣ 3 Tensor Structure in Latent Variable Models ‣ Tensor Decompositions for Learning Latent Variable Models") (LDA) use only up to third-order moments, which suggests that each document only needs to have three words.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Efficient Moment Representation for Exchangeable Models", "weight": 1.0} -->

In practice, one should use all of the words in a document for efficient estimation of the moments. One way to do this is to average over all $\binom{\ell}{3} \cdot {3!}$ ordered triples of words in a document of length $\ell$. At first blush, this seems computationally expensive (when $\ell$ is large), but as it turns out, the averaging can be done implicitly, as shown by Zou et al.. Let $c \in {\mathbb{R}}^{d}$ be the word count vector for a document of length $\ell$, so $c_{i}$ is the number of occurrences of word $i$ in the document, and ${\sum_{i = 1}^{d}c_{i}} = \ell$. Note that $c$ is a sufficient statistic for the document. Then, the contribution of this document to the empirical third-order moment tensor is given by It can be checked that this quantity is equal to where the sum is over all ordered word triples in the document.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Efficient Moment Representation for Exchangeable Models", "weight": 1.0} -->

A similar expression is easily derived for the contribution of the document to the empirical second-order moment matrix: Note that the word count vector $c$ is generally a sparse vector, so this representation allows for efficient multiplication by the moment matrices and tensors in time linear in the size of the document corpus (*i.e.*, the number of non-zero entries in the term-document matrix).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Dimensionality Reduction", "weight": 1.0} -->

Another serious concern regarding the use of tensor forms of moments is the need to operate on multidimensional arrays with $\Omega{(d^{3})}$ values (it is typically not exactly $d^{3}$ due to symmetry). When $d$ is large (*e.g.*, when it is the size of the vocabulary in natural language applications), even storing a third-order tensor in memory can be prohibitive. Sparsity is one factor that alleviates this problem. Another approach is to use efficient linear dimensionality reduction. When this is combined with efficient techniques for matrix and tensor multiplication that avoid explicitly constructing the moment matrices and tensors (such as the procedure described above), it is possible to avoid any computational scaling more than linear in the dimension $d$ and the training sample size.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Dimensionality Reduction", "weight": 1.0} -->

Consider for concreteness the tensor decomposition approach for the exchangeable single topic model as discussed in Section 4.3. Using recent techniques for randomized linear algebra computations, it is possible to efficiently approximate the whitening matrix $W \in {\mathbb{R}}^{d \times k}$ from the second-moment matrix $M_{2} \in {\mathbb{R}}^{d \times d}$. To do this, one first multiplies $M_{2}$ by a random matrix $R \in {\mathbb{R}}^{d \times k'}$ for some $k' \geq k$, and then computes the top $k$ singular vectors of the product $M_{2}R$. This provides a basis $U \in {\mathbb{R}}^{d \times k}$ whose span is approximately the range of $M_{2}$. From here, an approximate SVD of $U^{\top}M_{2}U$ is used to compute the approximate whitening matrix $W$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Dimensionality Reduction", "weight": 1.0} -->

Note that both matrix products $M_{2}R$ and $U^{\top}M_{2}U$ may be performed via implicit access to $M_{2}$ by exploiting, so that $M_{2}$ need not be explicitly formed. With the whitening matrix $W$ in hand, the third-moment tensor ${\overset{\sim}{M}}_{3} = {M_{3}{(W,W,W)}} \in {\mathbb{R}}^{k \times k \times k}$ can be implicitly computed via.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Dimensionality Reduction", "weight": 1.0} -->

For instance, the core computation in the tensor power method $\theta':={{\overset{\sim}{M}}_{3}{(I,\theta,\theta)}}$ is performed by (i) computing $\eta:={W\theta}$, (ii) computing $\eta':={M_{3}{(I,\eta,\eta)}}$, and finally (iii) computing $\theta':={W^{\top}\eta'}$. Using the fact that $M_{3}$ is an empirical third-order moment tensor, these steps can be computed with $O{({{dk} + N})}$ operations, where $N$ is the number of non-zero entries in the term-document matrix.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

It is interesting to consider the computational complexity of the tensor power method in the dense setting where $T \in {\mathbb{R}}^{k \times k \times k}$ is orthogonally decomposable but otherwise unstructured. Each iteration requires $O{(k^{3})}$ operations, and assuming at most $k^{1 + \delta}$ random restarts for extracting each eigenvector (for some small $\delta > 0$) and $O{({{\log{(k)}} + {\log{\log{({1/\epsilon})}}}})}$ iterations per restart, the total running time is $O{({k^{5 + \delta}{({{\log{(k)}} + {\log{\log{({1/\epsilon})}}}})}})}$ to extract all $k$ eigenvectors and eigenvalues.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

An alternative approach to extracting the orthogonal decomposition of $T$ is to reorganize $T$ into a matrix $M \in {\mathbb{R}}^{k \times k^{2}}$ by flattening two of the dimensions into one. In this case, if $T = {\sum_{i = 1}^{k}{\lambda_{i}v_{i}^{\otimes 3}}}$, then $M = {\sum_{i = 1}^{k}{{\lambda_{i}v_{i}} \otimes {{vec}{({v_{i} \otimes v_{i}})}}}}$. This reveals the singular value decomposition of $M$ (assuming the eigenvalues $\lambda_{1},\lambda_{2},\ldots,\lambda_{k}$ are distinct), and therefore can be computed with $O{(k^{4})}$ operations.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Therefore it seems that the tensor power method is less efficient than a pure matrix-based approach via singular value decomposition. However, it should be noted that this matrix-based approach fails to recover the decomposition when eigenvalues are repeated, and can be unstable when the gap between eigenvalues is small---see Appendix D for more discussion.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

It is worth noting that the running times differ by roughly a factor of $\Theta{(k^{1 + \delta})}$, which can be accounted for by the random restarts. This gap can potentially be alleviated or removed by using a more clever method for initialization. Moreover, using special structure in the problem (as discussed above) can also improve the running time of the tensor power method.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Sample Complexity Bounds", "weight": 1.0} -->

Previous work on using linear algebraic methods for estimating latent variable models crucially rely on matrix perturbation analysis for deriving sample complexity bounds. The learning algorithms in these works are plug-in estimators that use empirical moments in place of the population moments, and then follow algebraic manipulations that result in the desired parameter estimates. As long as these manipulations can tolerate small perturbations of the population moments, a sample complexity bound can be obtained by exploiting the convergence of the empirical moments to the population moments via the law of large numbers. As discussed in Appendix D, these approaches do not directly lead to practical algorithms due to a certain amplification of the error (a polynomial factor of $k$, which is observed in practice).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Sample Complexity Bounds", "weight": 1.0} -->

Using the perturbation analysis for the tensor power method, improved sample complexity bounds can be obtained for all of the examples discussed in Section 3. The underlying analysis remains the same as in previous works, the main difference being the accuracy of the orthogonal tensor decomposition obtained via the tensor power method. Relative to the previously cited works, the sample complexity bound will be considerably improved in its dependence on the rank parameter $k$, as Theorem 5.1 implies that the tensor estimation error (*e.g.*, error in estimating ${\overset{\sim}{M}}_{3}$ from Section 4.3) is not amplified by any factor explicitly depending on $k$ (there is a requirement that the error be smaller than some factor depending on $k$, but this only contributes to a lower-order term in the sample complexity bound). See Appendix D for further discussion regarding the stability of the techniques from these previous works.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Other Perspectives", "weight": 1.0} -->

The tensor power method is simply one approach for extracting the orthogonal decomposition needed in parameter estimation. The characterizations from Section 4.2 suggest that a number of fixed point and variational techniques may be possible (and Appendix D provides yet another perspective based on simultaneous diagonalization). One important consideration is that the model is often misspecified, and therefore approaches with more robust guarantees (*e.g.*, for convergence) are desirable. Our own experience with the tensor power method (as applied to exchangeable topic modeling) is that while model misspecification does indeed affect convergence, the results can be very reasonable even after just a dozen or so iterations. Nevertheless, robustness is likely more important in other applications, and thus the stabilization approaches may be advantageous.
