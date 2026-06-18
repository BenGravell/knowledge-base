<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Descent Provably Optimizes Over-parameterized Neural Networks

Topics include Gradient descent, Neural networks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

One of the mysteries in the success of neural networks is randomly initialized first order methods like gradient descent can achieve zero training loss even though the objective function is non-convex and non-smooth. This paper demystifies this surprising phenomenon for two-layer fully connected ReLU activated neural networks. For an m hidden node shallow neural network with ReLU activation and n training data, we show as long as m is large enough and no two inputs are parallel, randomly initialized gradient descent converges to a globally optimal solution at a linear convergence rate for the quadratic loss function. Our analysis relies on the following observation: over-parameterization and random initialization jointly restrict every weight vector to be close to its initialization for all iterations, which allows us to exploit a strong convexity-like property to show that gradient descent converges at a global linear rate to the global optimum. We believe these insights are also useful in analyzing deep models and other first order methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neural networks trained by first order methods have achieved a remarkable impact on many applications, but their theoretical properties are still mysteries. One of the empirical observation is even though the optimization objective function is non-convex and non-smooth, randomly initialized first order methods like stochastic gradient descent can still find a global minimum. Surprisingly, this property is not correlated with labels. In Zhang et al., authors replaced the true labels with randomly generated labels, but still found randomly initialized first order methods can always achieve zero training loss.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A widely believed explanation on why a neural network can fit all training labels is that the neural network is over-parameterized. For example, Wide ResNet (Zagoruyko and Komodakis, ) uses 100x parameters than the number of training data. Thus there must exist one such neural network of this architecture that can fit all training data. However, the existence does not imply why the network found by a randomly initialized first order method can fit all the data. The objective function is neither smooth nor convex, which makes traditional analysis technique from convex optimization not useful in this setting. To our knowledge, only the convergence to a stationary point is known.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we demystify this surprising phenomenon on two-layer neural networks with rectified linear unit (ReLU) activation. Formally, we consider a neural network of the following form.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on the empirical risk minimization problem with a quadratic loss. Given a training data set $\left\{ {(\mathbf{x}_{i},y_{i})} \right\}_{i = 1}^{n}$, we want to minimize

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main focus of this paper is to analyze the following procedure. We fix the second layer and apply gradient descent (GD) to optimize the first layer^11^1In Section 3.2, we also extend our technique to analyze the setting where we train both layers jointly.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\eta > 0$ is the step size. Here the gradient formula for each weight vector is ^22^2 Note ReLU is not continuously differentiable. One can view $\frac{\partial{L{(\mathbf{W})}}}{\partial\mathbf{w}_{r}}$ as a convenient notation for the right hand side of and this is the update rule used in practice.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though this is only a shallow fully connected neural network, the objective function is still non-smooth and non-convex due to the use of ReLU activation function. ^33^3We remark that if one fixes the first layer and only optimizes the output layer, then the problem becomes a convex and smooth one. If $m$ is large enough, one can show the global minimum has zero training loss. Though for both cases (fixing the first layer and fixing the output layer), gradient descent achieves zero training loss, the learned prediction functions are different. Even for this simple function, why randomly initialized first order method can achieve zero training error is not known. Many previous works have tried to answer this question or similar ones. Attempts include landscape analysis, partial differential equations (Mei et al., ), analysis of the dynamics of the algorithm, optimal transport theory, to name a few. These results often make strong assumptions on the labels and input distributions or do not imply why randomly initialized first order method can achieve zero training loss. See Section 2 for detailed comparisons between our result and previous ones.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we rigorously prove that as long as no two inputs are parallel and $m$ is large enough, with randomly initialized $\mathbf{a}$ and $\mathbf{W}{}$, gradient descent achieves zero training loss at a linear convergence rate, i.e., it finds a solution $\mathbf{W}{(K)}$ with ${L{({\mathbf{W}{(K)}})}} \leq \epsilon$ in $K = {O{({\log\left( {1/\epsilon} \right)})}}$ iterations.^44^4Here we omit the polynomial dependency on $n$ and other data-dependent quantities. Thus, our theoretical result not only shows the global convergence but also gives a quantitative convergence rate in terms of the desired accuracy.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Analysis Technique Overview", "weight": 1.0} -->

Our proof relies on the following insights. First we directly analyze the dynamics of each individual prediction $f{(\mathbf{W},\mathbf{a},\mathbf{x}_{i})}$ for $i = {1,\ldots,n}$. This is different from many previous work which tried to analyze the dynamics of the parameter ($\mathbf{W}$) we are optimizing. Note because the objective function is non-smooth and non-convex, analysis of the parameter space dynamics is very difficult. In contrast, we find the dynamics of prediction space is governed by the spectral property of a Gram matrix (which can vary in each iteration, c.f. Equation ) and as long as this Gram matrix's least eigenvalue is lower bounded, gradient descent enjoys a linear rate. It is easy to show as long as no two inputs are parallel, in the initialization phase, this Gram matrix has a lower bounded least eigenvalue. (c.f. Theorem 3.1). Thus the problem reduces to showing the Gram matrix at later iterations is close to that in the initialization phase.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Analysis Technique Overview", "weight": 1.0} -->

Our second observation is this Gram matrix is only related to the activation patterns (${\mathbb{I}}\left\{ {{\mathbf{w}_{r}^{\top}\mathbf{x}_{i}} \geq 0} \right\}$) and we can use matrix perturbation analysis to show if most of the patterns do not change, then this Gram matrix is close to its initialization. Our third observation is we find over-parameterization, random initialization, and the linear convergence jointly restrict every weight vector $\mathbf{w}_{r}$ to be close to its initialization. Then we can use this property to show most of the patterns do not change. Combining these insights we prove the first global quantitative convergence result of gradient descent on ReLU activated neural networks for the empirical risk minimization problem. Notably, our proof only uses linear algebra and standard probability bounds so we believe it can be easily generalized to analyze deep neural networks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations", "weight": 1.0} -->

We let ${\lbrack n\rbrack} = {\{ 1,2,\ldots,n\}}$. Given a set $S$, we use ${unif}\left\{ S \right\}$ to denote the uniform distribution over $S$. Given an event $E$, we use ${\mathbb{I}}\left\{ A \right\}$ to be the indicator on whether this event happens. We use $N{(\mathbf{0},\mathbf{I})}$ to denote the standard Gaussian distribution. For a matrix $\mathbf{A}$, we use $\mathbf{A}_{ij}$ to denote its $(i,j)$-th entry. We use $\left. \parallel \cdot \parallel{}_{2} \right.$ to denote the Euclidean norm of a vector, and use $\left. \parallel \cdot \parallel{}_{F} \right.$ to denote the Frobenius norm of a matrix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations", "weight": 1.0} -->

If a matrix $\mathbf{A}$ is positive semi-definite, we use $\lambda_{\min}{(\mathbf{A})}$ to denote its smallest eigenvalue. We use $\langle \cdot, \cdot \rangle$ to denote the standard Euclidean inner product between two vectors.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Comparison with Previous Results", "weight": 1.0} -->

In this section, we survey an incomplete list of previous attempts in analyzing why first order methods can find a global minimum.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Landscape Analysis", "weight": 1.0} -->

A popular way to analyze non-convex optimization problems is to identify whether the optimization landscape has some good geometric properties. Recently, researchers found if the objective function is smooth and satisfies all local minima are global and for every saddle point, there exists a negative curvature, then the noise-injected (stochastic) gradient descent can find a global minimum in polynomial time. This algorithmic finding encouraged researchers to study whether the deep neural networks also admit these properties.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Landscape Analysis", "weight": 1.0} -->

For the objective function defined in Equation, some partial results were obtained. Soudry and Carmon showed if ${md} \geq n$, then at every differentiable local minimum, the training error is zero. However, since the objective is non-smooth, it is hard to show gradient descent convergences to a differentiable local minimum. Xie et al. studied the same problem and related the loss to the gradient norm through the least singular value of the "extended feature matrix" $\mathbf{D}$ at the stationary points. However, they did not prove the convergence rate of the gradient norm. Interestingly, our analysis relies on the Gram matrix which is ${\mathbf{D}\mathbf{D}}^{\top}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Landscape Analysis", "weight": 1.0} -->

Landscape analyses of ReLU activated neural networks for other settings have also been studied in many previous works. These works establish favorable landscape properties but none of them implies that gradient descent converges to a global minimizer of the empirical risk. More recently, some negative results have also been discovered and new procedures have been proposed to test local optimality and escape strict saddle points at non-differentiable points. However, the new procedures cannot find global minima as well. For other activation functions, some previous works showed the landscape does have the desired geometric properties. However, it is unclear how to extend their analyses to our setting.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Analysis of Algorithm Dynamics", "weight": 1.0} -->

Another way to prove convergence result is to analyze the dynamics of first order methods directly. Our paper also belongs to this category. Many previous works assumed the input distribution is Gaussian and the label is generated according to a planted neural network. Based on these two (unrealistic) conditions, it can be shown that randomly initialized (stochastic) gradient descent can learn a ReLU, a single convolutional filter, a convolutional neural network with one filter and one output layer and residual network with small spectral norm weight matrix.^55^5Since these work assume the label is realizable, converging to global minimum is equivalent to recovering the underlying model. Beyond Gaussian input distribution, Du et al. showed for learning a convolutional filter, the Gaussian input distribution assumption can be relaxed but they still required the label is generated from an underlying true filter. Comparing with these work, our paper does not try to recover the underlying true neural network. Instead, we focus on providing theoretical justification on why randomly initialized gradient descent can achieve zero training loss, which is what we can observe and verify in practice.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Analysis of Algorithm Dynamics", "weight": 1.0} -->

Jacot et al. established an asymptotic result showing for the multilayer fully-connected neural network with a smooth activation function, if every layer's weight matrix is infinitely wide, then for finite training time, the convergence of gradient descent can be characterized by a kernel. Our proof technique relies on a Gram matrix which is the kernel matrix in their paper. Our paper focuses on the two-layer neural network with ReLU activation function (non-smooth) and we are able to prove the Gram matrix is stable for infinite training time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Analysis of Algorithm Dynamics", "weight": 1.0} -->

The most related paper is by Li and Liang who observed that when training a two-layer full connected neural network, most of the patterns (${\mathbb{I}}\left\{ {{\mathbf{w}_{r}^{\top}\mathbf{x}_{i}} \geq 0} \right\}$) do not change over iterations, which we also use to show the stability of the Gram matrix. They used this observation to obtain the convergence rate of GD on a two-layer over-parameterized neural network for the cross-entropy loss. They need the number of hidden nodes $m$ scales with ${poly}{({1/\epsilon})}$ where $\epsilon$ is the desired accuracy. Thus unless the number of hidden nodes $m\rightarrow\infty$, their result does not imply GD can achieve zero training loss. We improve by allowing the amount of over-parameterization to be independent of the desired accuracy and show GD can achieve zero training loss. Furthermore, our proof is much simpler and more transparent so we believe it can be easily generalized to analyze other neural network architectures.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Other Analysis Approaches", "weight": 1.0} -->

Chizat and Bach used optimal transport theory to analyze continuous time gradient descent on over-parameterized models. They required the second layer to be infinitely wide and their results on ReLU activated neural network is only at the formal level. Mei et al. analyzed SGD for optimizing the population loss and showed the dynamics can be captured by a partial differential equation in the suitable scaling limit. They listed some specific examples on input distributions including mixture of Gaussians. However, it is still unclear whether this framework can explain why first order methods can minimize the empirical risk. Daniely built connection between neural networks with kernel methods and showed stochastic gradient descent can learn a function that is competitive with the best function in the conjugate kernel space of the network. Again this work does not imply why first order methods can achieve zero training loss.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Continuous Time Analysis", "weight": 1.0} -->

In this section, we present our result for gradient flow, i.e., gradient descent with infinitesimal step size. The analysis of gradient flow is a stepping stone towards understanding discrete algorithms and this is the main topic of recent work. In the next section, we will modify the proof and give a quantitative bound for gradient descent with positive step size.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

$\mathbf{H}^{\infty}$ is the Gram matrix induced by the ReLU activation function and the random initialization. Later we will show that during the training, though the Gram matrix may change (c.f. Equation ), it is still close to $\mathbf{H}^{\infty}$. Furthermore, as will be apparent in the proof (c.f. Equation ), $\mathbf{H}^{\infty}$ is the fundamental quantity that determines the convergence rate. Interestingly, various properties of this $\mathbf{H}^{\infty}$ matrix has been studied in previous works. Now to justify this assumption, the following theorem shows if no two inputs are parallel the least eigenvalue is strictly positive.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Note Equation completely describes the dynamics of the predictions. In the rest of this section, we will show at initialization $\left\| {{\mathbf{H}{}} - \mathbf{H}^{\infty}} \right\|_{2}$ is $O{(\sqrt{1/m})}$ and for all $t > 0$, $\left\| {{\mathbf{H}{(t)}} - {\mathbf{H}{}}} \right\|_{2}$ is $O{(\sqrt{1/m})}$. Therefore, according to Equation, as $m\rightarrow\infty$, the dynamics of the predictions are characterized by $\mathbf{H}^{\infty}$. This is the main reason we believe $\mathbf{H}^{\infty}$ is the fundamental quantity that describes this optimization process.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

$\mathbf{H}{(t)}$ is a time-dependent symmetric matrix. We first analyze its property when $t = 0$. The following lemma shows if $m$ is large then $\mathbf{H}{}$ has a lower bounded least eigenvalue with high probability. The proof is by the standard concentration bound so we defer it to the appendix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Jointly Training Both Layers", "weight": 1.0} -->

In this subsection, we showcase our proof technique can be applied to analyze the convergence of gradient flow for jointly training both layers.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Jointly Training Both Layers", "weight": 1.0} -->

for $r = {1,\ldots,m}$. The following theorem shows using gradient flow to jointly train both layers, we can still enjoy linear convergence rate towards zero loss.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discrete Time Analysis", "weight": 1.0} -->

In this section, we show randomly initialized gradient descent with a constant positive step size converges to the global minimum at a linear rate. We first present our main theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Condition 4.1", "weight": 1.0} -->

A directly corollary of this condition is the following bound of deviation from the initialization. The proof is similar to that of Lemma 3.3 so we defer it to appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we use synthetic data to corroborate our theoretical findings. We use the initialization and training procedure described in Section 1. For all experiments, we run $100$ epochs of gradient descent and use a fixed step size. We uniformly generate $n = 1000$ data points from a $d = 1000$ dimensional unit sphere and generate labels from a one-dimensional standard Gaussian distribution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We test three metrics with different widths ($m$). First, we test how the amount of over-parameterization affects the convergence rates. Second, we test the relation between the amount of over-parameterization and the number of pattern changes. Formally, at a given iteration $k$, we check $\frac{\sum_{i = 1}^{m}{\sum_{r = 1}^{m}{{\mathbb{I}}\left\{ {{\text{sign}\left( {\mathbf{w}_{r}{}^{\top}\mathbf{x}_{i}} \right)} \neq {\text{sign}\left( {\mathbf{w}_{r}{(k)}^{\top}\mathbf{x}_{i}} \right)}} \right\}}}}{mn}$ (there are $mn$ patterns). This aims to verify Lemma 3.2.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Last, we test the relation between the amount of over-parameterization and the maximum of the distances between weight vectors and their initializations. Formally, at a given iteration $k$, we check $\max_{r \in {\lbrack m\rbrack}}\left\| {{\mathbf{w}_{r}{(k)}} - {\mathbf{w}_{r}{}}} \right\|_{2}$. This aims to verify Lemma 3.3 and Corollary 4.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

In this paper we show with over-parameterization, gradient descent provable converges to the global minimum of the empirical loss at a linear convergence rate. The key proof idea is to show the over-parameterization makes Gram matrix remain positive definite for all iterations, which in turn guarantees the linear convergence. Here we list some future directions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

First, we believe our approach can be generalized to deep neural networks. We elaborate the main idea here for gradient flow. Consider a deep neural network of the form

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Note for every $h \in {\lbrack H\rbrack}$, $\mathbf{G}^{(h)}$ is a Gram matrix and thus it is positive semidefinite. If $\sum_{h = 1}^{H}{\mathbf{G}^{(h)}{(t)}}$ has a lower bounded least eigenvalue for all $t$, then similar to Section 3, gradient flow converges to zero training loss at a linear convergence rate.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Based on our observations in Remark 3.1, we conjecture that if $m$ is large enough, $\sum_{h = 1}^{H}{\mathbf{G}^{(h)}{}}$ is close to a fixed matrix $\sum_{h = 1}^{H}\mathbf{G}_{\infty}^{(h)}$ and $\sum_{h = 1}^{H}{\mathbf{G}^{(h)}{(t)}}$ is close its initialization $\sum_{h = 1}^{H}{\mathbf{G}^{(h)}{}}$ for all $t > 0$. Therefore, using the same arguments as we used in Section 3, as long as $\sum_{h = 1}^{H}\mathbf{G}_{\infty}^{(h)}$ has a lower bounded least eigenvalue, gradient flow converges to zero training loss at a linear convergence rate.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Second, we believe the number of hidden nodes $m$ required can be reduced. For example, previous work showed $m \geq \frac{n}{d}$ is enough to make all differentiable local minima global. In our setting, using advanced tools from probability and matrix perturbation theory to analyze $\mathbf{H}{(t)}$, we may be able to tighten the bound.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Lastly, in our paper, we used the empirical loss as a potential function to measure the progress. If we use another potential function, we may be able to prove the convergence rates of accelerated methods. This technique has been exploited in Wilson et al. for analyzing convex optimization. It would be interesting to bring their idea to analyze other first order methods for optimizing neural networks.
