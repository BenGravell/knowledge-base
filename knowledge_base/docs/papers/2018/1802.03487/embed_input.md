<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Small Nonlinearities in Activation Functions Create Bad Local Minima in Neural Networks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate the loss surface of neural networks. We prove that even for one-hidden-layer networks with "slightest" nonlinearity, the empirical risks have spurious local minima in most cases. Our results thus indicate that in general "no spurious local minima" is a property limited to deep linear networks, and insights obtained from linear networks may not be robust. Specifically, for ReLU(-like) networks we constructively prove that for almost all practical datasets there exist infinitely many local minima. We also present a counterexample for more general activations (sigmoid, tanh, arctan, ReLU, etc.), for which there exists a bad local minimum. Our results make the least restrictive assumptions relative to existing results on spurious local optima in neural networks. We complete our discussion by presenting a comprehensive characterization of global optimality for deep linear networks, which unifies other results on this topic.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neural network training reduces to solving nonconvex empirical risk minimization problems, a task that is in general intractable. But success stories of deep learning suggest that local minima of the empirical risk could be close to global minima. Choromanska et al. use spherical spin-glass models from statistical physics to justify how the size of neural networks may result in local minima that are close to global. However, due to the complexities introduced by nonlinearity, a rigorous understanding of optimality in deep neural networks remains elusive.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Initial steps towards understanding optimality have focused on *deep linear* networks. This area has seen substantial recent progress. In deep linear networks there is no nonlinear activation; the output is simply a multilinear function of the input. Baldi & Hornik prove that some shallow networks have no spurious local minima, and Kawaguchi extends this result to squared error deep linear networks, showing that they only have global minima and saddle points. Several other works on linear nets have also appeared.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The theory of nonlinear neural networks (which is the actual setting of interest), however, is still in its infancy. There have been attempts to extend the "local minima are global" property from linear to nonlinear networks, but recent results suggest that this property does not usually hold. Although not unexpected, rigorously proving such results turns out to be non-trivial, forcing several authors (e.g., Safran & Shamir; Du et al.; Wu et al. ) to make somewhat unrealistic assumptions (realizability and Gaussianity) on data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, we prove existence of spurious local minima under the least restrictive (to our knowledge) assumptions. Since seemingly subtle changes to assumptions can greatly influence the analysis as well as the applicability of known results, let us first summarize what is known; this will also help provide a better intuitive perspective on our results (as the technical details are somewhat involved).

<!-- chunk {"id": "body-0007", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

There is a large and rapidly expanding literature of optimization of neural networks. Some works focus on the loss surface, while others study the convergence of gradient-based methods for optimizing this loss. In particular, our focus is on the loss surface itself, independent of any algorithmic concerns; this is reflected in the works summarized below.

<!-- chunk {"id": "body-0008", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

For ReLU networks, the works provide counterexample datasets that lead to spurious local minima, dashing hopes of "local implies global" properties. However, these works fail to provide statements about generic datasets, and one can argue that their setups are limited to isolated pathological examples. In comparison, our Theorem 1 shows existence of spurious local minima for *almost all* datasets, a much more general result. Zhou & Liang also give characterization of critical points of shallow ReLU networks, but with more than one hidden node the characterization provided is limited to certain regions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

There are also results that study population risk of shallow ReLU networks under an assumption that input data is i.i.d. Gaussian distributed. Moreover, these works also assume *realizability*, i.e., the output data is generated from a neural network with the same architecture as the model one trains, with unknown true parameters. These assumptions enable one to compute the population risk in a closed form, and ensure that one can always achieve zero loss at global minima. The authors of Safran & Shamir; Wu et al. study the population risk function of the form ${\mathbb{E}}_{x}{\lbrack{({{\sum_{i = 1}^{k}{\text{ReLU}{({w_{i}^{T}x})}}} - {\text{ReLU}{({v_{i}^{T}x})}}})}^{2}\rbrack}$, where the true parameters $v_{i}$'s are orthogonal unit vectors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

Through extensive experiments and computer-assisted local minimality checks, Safran & Shamir show existence of local minima for $k \geq 6$. However, this result is empirical and does not have constructive proofs. Wu et al. show that with $k = 2$, there is no bad local minima on the manifold $\left\| w_{1} \right\|_{2} = \left\| w_{2} \right\|_{2} = 1$. Du et al. study population risk of one-hidden-layer CNN. They show that there can be a spurious local minimum, but gradient descent converges to the global minimum with probability at least 1/4.

<!-- chunk {"id": "body-0011", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

Our paper focuses on empirical risk instead of population risk, and *does not* assume either Gaussianity or realizability. Theorem 1 1's assumption on the dataset is that it is *not linearly fittable*^11^1That is, given input data matrices $X$ and $Y$, there is no matrix $R$ such that $Y = {RX}$., which is vastly more general and realistic than assuming that input data is Gaussian or that the output is generated from an unknown neural network. Our results also show that Wu et al. fails to extend to empirical risk and non-unit parameter vectors (see the discussion after Theorem 2).

<!-- chunk {"id": "body-0012", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

Liang et al. showed that under assumptions on the loss function, data distribution, network structure, and activation function, all local minima of the empirical loss have zero classification error in binary classification tasks. The result relies on stringent assumptions, and it is not directly comparable to ours because both "the local minimum has nonzero classification error" and "the local minima is spurious" do not imply one another. Liang et al. proved that adding a parallel network with one exponential hidden node can eliminate all bad local minima. The result relies on the special parallel structure, whereas we analyze standard fully connected network architecture.

<!-- chunk {"id": "body-0013", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

Laurent & Brecht studies one-hidden-layer networks with hinge loss for classification. Under linear separability, the authors prove that Leaky-ReLU networks don't have bad local minima, while ReLU networks do. Our focus is on regression, and we only make mild assumptions on data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

For deep linear networks, the most relevant result to ours is Laurent & Brecht. When all hidden layers are wider than the input or output layers, Laurent & Brecht prove that any local minimum of a deep linear network under differentiable convex loss is global.^22^2Although their result overlaps with a subset of Theorem 4, our theorem was obtained independently. They prove this by showing a statement about relationship between linear vs. multilinear parametrization. Our result in Theorem 4 is *strictly* more general that their results, and presents a comprehensive characterization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "What is known so far?", "weight": 1.0} -->

A different body of literature considers sufficient conditions for global optimality in nonlinear networks. These results make certain architectural assumptions (and some technical restrictions) that may not usually apply to realistic networks. There are also other works on global optimality conditions for specially designed architectures.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions and Summary of Results", "weight": 1.0} -->

We summarize our key contributions more precisely below. Our work encompasses results for both nonlinear and linear neural networks. First, we study whether the "local minima are global" property holds for nonlinear networks. Unfortunately, our results here are negative. Specifically, we prove

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions and Summary of Results", "weight": 1.0} -->

For piecewise linear and nonnegative homogeneous activation functions (e.g., ReLU), we prove in Theorem 1 that if linear models cannot perfectly fit the data, one can *construct* infinitely many local minima that are not global. In practice, most datasets are not linearly fittable, hence this result gives a constructive proof of spurious local minima for generic datasets. In contrast, several existing results either provide only one counterexample, or make restrictive assumptions of realizability or linear separability. This result is presented in Section 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions and Summary of Results", "weight": 1.0} -->

In Theorem 2 we tackle more general nonlinear activation functions, and provide a simple architecture (with squared loss) and dataset, for which there exists a local minimum inferior to the global minimum for a realizable dataset. Our analysis applies to a wide range of activations, including sigmoid, tanh, arctan, ELU, SELU, and ReLU. Considering that realizability of data simplifies the analysis and ensures zero loss at global optima, our counterexample that is realizable and yet has a spurious local minimum is surprising, suggesting that the situation is likely worse for non-realizable data. See Section 3 for details.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions and Summary of Results", "weight": 1.0} -->

Assume that the hidden layers are as wide as either the input or the output, and that the empirical risk $\ell{({(W_{j})}_{j = 1}^{H + 1})}$ equals $\ell_{0}{({W_{H + 1}W_{H}\cdotsW_{1}})}$, where $\ell_{0}$ is a differentiable loss function and $W_{i}$ is the weight matrix for layer $i$. Theorem 4 shows if ${({\hat{W}}_{j})}_{j = 1}^{H + 1}$ is a critical point of $\ell$, then its type of stationarity (local min/max, or saddle) is closely related to the behavior of $\ell_{0}$ evaluated at the product ${\hat{W}}_{H + 1}\cdots{\hat{W}}_{1}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions and Summary of Results", "weight": 1.0} -->

If we additionally assume that any critical point of $\ell_{0}$ is a global minimum, Corollary 5 shows that the empirical risk $\ell$ only has global minima and saddles, and provides a simple condition to distinguish between them. To the best of our knowledge, this is the most general result on deep linear networks and it subsumes several previous results, e.g.,. This result is in Section 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "\"ReLU-like\" networks: bad local minima exist for most data", "weight": 1.0} -->

We study below whether nonlinear neural networks provably have spurious local minima. We show in §2 and §3 that even for extremely simple nonlinear networks, one encounters spurious local minima. We first consider ReLU and ReLU-like networks. Here, we prove that as long as linear models cannot perfectly fit the data, there exists a local minimum strictly inferior to the global one. Using nonnegative homogeneity, we can scale the parameters to get infinitely many local minima.

<!-- chunk {"id": "body-0022", "role": "body", "section": "\"ReLU-like\" networks: bad local minima exist for most data", "weight": 1.0} -->

Next, define a class of piecewise linear nonnegative homogeneous functions

<!-- chunk {"id": "body-0023", "role": "body", "section": "\"ReLU-like\" networks: bad local minima exist for most data", "weight": 1.0} -->

where ${s_{+} > 0},{s_{-} \geq 0}$ and $s_{+} \neq s_{-}$. Note that ReLU and Leaky-ReLU are members of this class.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main results and discussion", "weight": 1.0} -->

We use the shorthand $\overset{\sim}{X}:=\begin{bmatrix}
\end{bmatrix}^{T} \in {\mathbb{R}}^{{({d_{x} + 1})} \times m}$. The main result of this section, Theorem 1, considers the case where linear models cannot fit $Y$, i.e., $Y \neq {R\overset{\sim}{X}}$ for all matrix $R$. With ReLU-like activation and a few mild assumptions, Theorem 1 shows that there exist spurious local minima.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Analysis of Theorem 1", "weight": 1.0} -->

The proof of the theorem is split into two steps. First, we prove that there exist local minima ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$ whose risk value is the same as the linear least squares solution, and that there are infinitely many such minima. Second, we will construct a tuple of parameters ${({\overset{\sim}{W}}_{j},{\overset{\sim}{b}}_{j})}_{j = 1}^{2}$ that has strictly smaller empirical risk than ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Analysis of Theorem 1", "weight": 1.0} -->

Step 1: A local minimum as good as the linear solution. The main idea here is to exploit the weights from the linear least squares solution, and to tune the parameters so that all inputs to hidden nodes become positive. Doing so makes the hidden nodes "locally linear," so that the constructed ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$ that produce linear least squares estimates at the output become locally optimal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Step 2: A point strictly better than the local minimum", "weight": 1.0} -->

The proof of this step is more involved. In the previous step, we "pushed" all the input to the hidden nodes to positive side, and took advantage of "local linearity" of the hidden nodes near ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$. But to construct parameters ${({\overset{\sim}{W}}_{j},{\overset{\sim}{b}}_{j})}_{j = 1}^{2}$ that have strictly smaller risk than ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$ (to prove that ${({\hat{W}}_{j},{\hat{b}}_{j})}_{j = 1}^{2}$ is a spurious local minimum), we make the sign of inputs to the hidden nodes different depending on data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Step 2: A point strictly better than the local minimum", "weight": 1.0} -->

We present the proof for $\mathcal{J} \neq \varnothing$, and defer the other case to Appendix A2 as it is rarer, and its proof, while instructive for its perturbation argument, is technically too involved.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Step 2: A point strictly better than the local minimum", "weight": 1.0} -->

The empirical risk for this choice of parameters is

<!-- chunk {"id": "body-0030", "role": "body", "section": "Counterexample: bad local minima for many activations", "weight": 1.0} -->

The proof of Theorem 1 crucially exploits the piecewise linearity of the activation functions. Thus, one may wonder whether the spurious local minima seen there are an artifact of the specific nonlinearity. We show below that this is *not* the case. We provide a counterexample nonlinear network and a dataset for which a wide range of nonlinear activations result in a local minimum that is strictly inferior to the global minimum with exactly zero empirical risk. Examples of such activation functions include popular activation functions such as sigmoid, tanh, arctan, ELU, SELU, and ReLU.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Global optimality in linear networks", "weight": 1.0} -->

In this section we present our results on deep linear neural networks. Assuming that the hidden layers are at least as wide as either the input or output, we show that critical points of the loss with a multilinear parameterization inherit the type of critical points of the loss with a linear parameterization. As a corollary, we show that for differentiable losses whose critical points are globally optimal, deep linear networks have *only global minima or saddle points*. Furthermore, we provide an efficiently checkable condition for global minimality.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Global optimality in linear networks", "weight": 1.0} -->

Suppose the network has $H$ hidden layers having widths $d_{1},\ldots,d_{H}$. To ease notation, we set $d_{0} = d_{x}$ and $d_{H + 1} = d_{y}$. The weights between adjacent layers are kept in matrices $W_{j} \in {\mathbb{R}}^{d_{j} \times d_{j - 1}}$ ($j \in {\lbrack{H + 1}\rbrack}$), and the output $\hat{Y}$ of the network is given by the product of weight matrices with the data matrix: $\hat{Y} = {W_{H + 1}W_{H}\cdotsW_{1}X}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Global optimality in linear networks", "weight": 1.0} -->

Let ${(W_{j})}_{j = 1}^{H + 1}$ be the tuple of all weight matrices, and $W_{i:j}$ denote the product $W_{i}W_{i - 1}\cdotsW_{j + 1}W_{j}$ for $i \geq j$, and the identity for $i = {j - 1}$. We consider the empirical risk $\ell{({(W_{j})}_{j = 1}^{H + 1})}$, which, for linear networks assumes the form

<!-- chunk {"id": "body-0034", "role": "body", "section": "Global optimality in linear networks", "weight": 1.0} -->

Remark: bias terms. We omit the bias terms $b_{1},\ldots,b_{H + 1}$ here. This choice is for simplicity; models with bias can be handled by the usual trick of augmenting data and weight matrices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main results and discussion", "weight": 1.0} -->

We are now ready to state our first main theorem, whose proof is deferred to Appendix A7.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

We investigated the loss surface of deep linear and nonlinear neural networks. We proved two theorems showing existence of spurious local minima on nonlinear networks, which apply to almost all datasets (Theorem 1) and a wide class of activations (Theorem 2). We concluded by Theorem 4, showing a general result studying the behavior of critical points in multilinearly parametrized functions, which unifies other existing results on linear neural networks. Given that spurious local minima are common in neural networks, a valuable future research direction will be investigating how far local minima are from global minima in general, and how the size of the network affects this gap. Another thing to note is that even though we showed the existence of spurious local minima in the *whole* parameter space, things can be different in restricted sets of parameter space (e.g., by adding regularizers). Understanding the loss surface in such sets would be valuable. Additionally, one can try to show algorithmic/trajectory results of (stochastic) gradient descent. We hope that our paper will be a stepping stone to such future research.
