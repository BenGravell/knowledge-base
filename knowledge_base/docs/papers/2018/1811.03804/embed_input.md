<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Descent Finds Global Minima of Deep Neural Networks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gradient descent finds a global minimum in training deep neural networks despite the objective function being non-convex. The current paper proves gradient descent achieves zero training loss in polynomial time for a deep over-parameterized neural network with residual connections (ResNet). Our analysis relies on the particular structure of the Gram matrix induced by the neural network architecture. This structure allows us to show the Gram matrix is stable throughout the training process and this stability implies the global optimality of the gradient descent algorithm. We further extend our analysis to deep residual convolutional neural networks and obtain a similar convergence result.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the mysteries in deep learning is randomly initialized first-order methods like gradient descent achieve zero training loss, even if the labels are arbitrary. Over-parameterization is widely believed to be the main reason for this phenomenon as only if the neural network has a sufficiently large capacity, it is possible for this neural network to fit all the training data. For example, Lu et al. proved that except for a measure zero set, all functions cannot be approximated by ReLU networks with a width less than the input dimension. In practice, many neural network architectures are highly over-parameterized. For example, Wide Residual Networks have 100x parameters than the number of training data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second mysterious phenomenon in training deep neural networks is "deeper networks are harder to train." To solve this problem, He et al. proposed the deep residual network (ResNet) architecture which enables randomly initialized first order method to train neural networks with an order of magnitude more layers. Theoretically, Hardt & Ma showed that residual links in linear networks prevent gradient vanishing in a large neighborhood of zero, but for neural networks with non-linear activations, the advantages of using residual connections are not well understood.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we demystify these two mysterious phenomena. We consider the setting where there are $n$ data points, and the neural network has $H$ layers with width $m$. We focus on the least-squares loss and assume the activation function is Lipschitz and smooth. This assumption holds for many activation functions including the soft-plus and sigmoid. Our contributions are summarized below.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a warm-up, we first consider a fully-connected feedforward network. We show if $m = {\Omega\left( {{poly}{(n)}2^{O{(H)}}} \right)}$^11^1The precise polynomials and data-dependent parameters are stated in Section 5, 6, 7., then randomly initialized gradient descent converges to zero training loss at a linear rate.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Next, we consider the ResNet architecture. We show as long as $m = {\Omega\left( {{poly}{(n,H)}} \right)}$, then randomly initialized gradient descent converges to zero training loss at a linear rate. Comparing with the first result, the dependence on the number of layers improves exponentially for ResNet. This theory demonstrates the advantage of using residual architectures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lastly, we apply the same technique to analyze convolutional ResNet. We show if $m = {{poly}{(n,p,H)}}$ where $p$ is the number of patches, then randomly initialized gradient descent achieves zero training loss.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proof builds on two ideas from previous work on gradient descent for two-layer neural networks. First, we use the observation by that if the neural network is over-parameterized, every weight matrix is close to its initialization. Second, following, we analyze the dynamics of the predictions whose convergence is determined by the least eigenvalue of the Gram matrix induced by the neural network architecture and to lower bound the least eigenvalue, it is sufficient to bound the distance of each weight matrix from its initialization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Different from these two works, in analyzing deep neural networks, we need to exploit more structural properties of deep neural networks and develop new techniques for analyzing both the initialization and gradient descent dynamics. In Section 4 we give an overview of our proof technique.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Organization", "weight": 1.0} -->

This paper is organized as follows. In Section 2, we discuss related works. In Section 3, we formally state the problem setup. In Section 4, we present our main analysis techniques. In Section 5, we give a warm-up result for the deep fully-connected neural network. In Section 6, we give our main result for the ResNet. In Section 7, we give our main result for the convolutional ResNet. We conclude in Section 8 and defer all proofs to the appendix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Recently, many works try to study the optimization problem in deep learning. Since optimizing a neural network is a non-convex problem, one approach is first to develop a general theory for a class of non-convex problems which satisfy desired geometric properties and then identify that the neural network optimization problem belongs to this class. One promising candidate class is the set of functions that satisfy: a) all local minima are global and b) there exists a negative curvature for every saddle point. For this function class, researchers have shown (perturbed) gradient descent can find a global minimum. Many previous works thus try to study the optimization landscape of neural networks with different activation functions. However, even for a three-layer linear network, there exists a saddle point that does not have a negative curvature, so it is unclear whether this geometry-based approach can be used to obtain the global convergence guarantee of first-order methods.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Another way to attack this problem is to study the dynamics of a specific algorithm for a specific neural network architecture. Our paper also belongs to this category. Many previous works put assumptions on the input distribution and assume the label is generated according to a planted neural network. Based on these assumptions, one can obtain global convergence of gradient descent for some shallow neural networks. Some local convergence results have also been proved. In comparison, our paper does not try to recover the underlying neural network. Instead, we focus on minimizing the training loss and rigorously prove that randomly initialized gradient descent can achieve zero training loss.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

The most related papers are who observed that when training an over-parametrized two-layer fully-connected neural network, the weights do not change a large amount, which we also use to show the stability of the Gram matrix. They used this observation to obtain the convergence rate of gradient descent on a two-layer over-parameterized neural network for the cross-entropy and least-squares loss. More recently, Allen-Zhu et al. generalized ideas from to derive convergence rates of training recurrent neural networks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our work extends these previous results in several ways: a) we consider deep networks, b) we generalize to ResNet architectures, and c) we generalize to convolutional networks. To improve the width dependence $m$ on sample size $n$, we utilize a smooth activation (e.g. smooth ReLU). For example, our results specialized to depth $H = 1$ improve upon in the required amount of overparametrization from $m = {\Omega\left( n^{6} \right)}$ to $m = {\Omega\left( n^{4} \right)}$. See Theorem 5.1. ‣ 5 Warm Up: Convergence Result of GD for Deep Fully-connected Neural Networks ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") for the precise statement.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

Chizat & Bach brought to our attention the paper of Jacot et al. which proved a similar weight stability phenomenon for deep networks, but only in the asymptotic setting of infinite-width networks and gradient flow run for a finite time. Jacot et al. do not establish the convergence of gradient flow to a global minimizer. In lieu of their results, our work can be viewed as a generalization of their result to: a) finite width, b) gradient descent as opposed to gradient flow, and c) convergence to a global minimizer.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Works", "weight": 1.0} -->

Mei et al.; Chizat & Bach; Sirignano & Spiliopoulos; Rotskoff & Vanden-Eijnden; Wei et al. used optimal transport theory to analyze gradient descent on over-parameterized models. However, their results are limited to two-layer neural networks and may require an exponential amount of over-parametrization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related Works", "weight": 1.0} -->

Daniely developed the connection between deep neural networks with kernel methods and showed stochastic gradient descent can learn a function that is competitive with the best function in the conjugate kernel space of the network. Andoni et al. showed that gradient descent can learn networks that are competitive with polynomial classifiers. However, these results do not imply gradient descent can find a global minimum for the empirical loss minimization problem. Our analysis of the Gram matrices at random initialization is closely related to prior work on the analysis of infinite-width networks as Gaussian Processes. Since we require the initialization analysis for three distinct architectures (ResNet, feed-forward, and convolutional ResNet), we re-derive many of these prior results in a unified fashion in Appendix E.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Related Works", "weight": 1.0} -->

Finally, in concurrent work, Allen-Zhu et al. also analyze gradient descent on deep neural networks. The primary difference between the two papers is that we analyze general smooth activations, and Allen-Zhu et al. develop specific analysis for ReLU activation. The two papers also differ significantly on their data assumptions. We wish to emphasize a fair comparison is not possible due to the difference in setting and data assumptions. We view the two papers as complementary since they address different neural net architectures.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Related Works", "weight": 1.0} -->

For ResNet, the primary focus of this manuscript, the required width per layer for Allen-Zhu et al. is $m \gtrsim {n^{30}H^{30}{\log^{2}\frac{1}{\epsilon}}}$ and for this paper's Theorem 6.1. ‣ 6 Convergence Result of GD for ResNet ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") is $m \gtrsim {n^{4}H^{2}}$.^22^2In all comparisons, we ignore the polynomial dependency on data-dependent parameters which only depends on the input data and the activation function. The two papers use different measures and are not directly comparable. Our paper requires a width $m$ that does not depend on the desired accuracy $\epsilon$. As a consequence, Theorem 6.1. ‣ 6 Convergence Result of GD for ResNet ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") guarantees the convergence of gradient descent to a global minimizer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Related Works", "weight": 1.0} -->

The iteration complexity of Allen-Zhu et al. is $T \gtrsim {n^{6}H^{2}{\log\frac{1}{\epsilon}}}$ and of Theorem 6.1. ‣ 6 Convergence Result of GD for ResNet ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") is $T \gtrsim {n^{2}{\log\frac{1}{\epsilon}}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Related Works", "weight": 1.0} -->

For fully-connected networks, Allen-Zhu et al. requires width $m \gtrsim {n^{30}H^{30}{\log^{2}\frac{1}{\epsilon}}}$ and iteration complexity $T \gtrsim {n^{6}H^{2}{\log\frac{1}{\epsilon}}}$. Theorem 5.1. ‣ 5 Warm Up: Convergence Result of GD for Deep Fully-connected Neural Networks ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") requires width $m \gtrsim {n^{4}2^{O{(H)}}}$ and iteration complexity $T \gtrsim {n^{2}2^{O{(H)}}{\log\frac{1}{\epsilon}}}$. The primary difference is for very deep fully-connected networks, Allen-Zhu et al. has milder dependence on $H$, but worse dependence on $n$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Related Works", "weight": 1.0} -->

Commonly used fully-connected networks such as VGG are not extremely deep ($H = 16$), yet the dataset size such as ImageNet ($n \sim 10^{6}$) is very large.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Related Works", "weight": 1.0} -->

In a second concurrent work, Zou et al. also analyzed the convergence of gradient descent on fully-connected networks with ReLU activation. The emphasis is on different loss functions (e.g. hinge loss), so the results are not directly comparable. Both Zou et al. and Allen-Zhu et al. train a subset of the layers, instead of all the layers as in this work, but also analyze stochastic gradient.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Notations", "weight": 1.0} -->

Similarly $\mathbf{A}_{:,i}$ is the $i$-th column vector and $\mathbf{A}_{j:{k,i}}$ is a part of $i$-th column vector. For a vector $\mathbf{v}$, we use $\left\| \mathbf{v} \right\|_{2}$ to denote the Euclidean norm. For a matrix $\mathbf{A}$ we use $\left\| \mathbf{A} \right\|_{F}$ to denote the Frobenius norm and $\left\| \mathbf{A} \right\|_{2}$ to denote the operator norm. If a matrix $\mathbf{A}$ is positive semi-definite, we use $\lambda_{\min}{(\mathbf{A})}$ to denote its smallest eigenvalue. We use $\langle \cdot, \cdot \rangle$ to denote the standard Euclidean inner product between two vectors or matrices.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Notations", "weight": 1.0} -->

We let $O{( \cdot )}$ and $\Omega( \cdot )$ denote standard Big-O and Big-Omega notations, only hiding constants. In this paper we will use $C$ and $c$ to denote constants. The specific value can be different from line to line.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Condition 3.1 (Lipschitz and Smooth)", "weight": 1.0} -->

There exists a constant $c > 0$ such that $\left| {\sigma} \right| \leq c$ and for any ${z,z'} \in {\mathbb{R}}$, These two conditions will be used to show the stability of the training process. Note for softplus both Lipschitz constant and smoothness constant are $1$. In this paper, we view all activation function related parameters as constants.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Condition 3.2", "weight": 1.0} -->

$\sigma( \cdot )$ is analytic and is not a polynomial function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Condition 3.2", "weight": 1.0} -->

This assumption is used to guarantee the positive-definiteness of certain Gram matrices which we will define later. Softplus function satisfies this assumption by definition.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

In this paper, we focus on the empirical risk minimization problem with the quadratic loss function where $\left\{ \mathbf{x}_{i} \right\}_{i = 1}^{n}$ are the training inputs, $\left\{ y_{i} \right\}_{i = 1}^{n}$ are the labels, $\theta$ is the parameter we optimize over and $f$ is the prediction function, which in our case is a neural network. We consider the following architectures.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Multilayer fully-connected neural networks: Let $\mathbf{x} \in {\mathbb{R}}^{d}$ be the input, $\mathbf{W}^{} \in {\mathbb{R}}^{m \times d}$ is the first weight matrix, $\mathbf{W}^{(h)} \in {\mathbb{R}}^{m \times m}$ is the weight at the $h$-th layer for $2 \leq h \leq H$, $\mathbf{a} \in {\mathbb{R}}^{m}$ is the output layer and $\sigma(\cdot)$ is the activation function.^33^3We assume intermediate layers are square matrices for simplicity. It is not difficult to generalize our analysis to rectangular weight matrices. We define the prediction function recursively (for simplicity we let $\mathbf{x}^{} = \mathbf{x}$).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

ResNet^44^4We will refer to this architecture as ResNet, although this differs by the standard ResNet architecture since the skip-connections at every layer, instead of every two layers. This architecture was previously studied. We study this architecture for the ease of presentation and analysis. It is not hard to generalize our analysis to architectures with skip-connections are every two or more layers.: We use the same notations as the multilayer fully connected neural networks. We define the prediction recursively. where $0 < c_{res} < 1$ is a small constant. Note here we use a $\frac{c_{res}}{H\sqrt{m}}$ scaling. This scaling plays an important role in guaranteeing the width per layer only needs to scale polynomially with $H$. In practice, the small scaling is enforced by a small initialization of the residual connection, which obtains state-of-the-art performance for deep residual networks. We choose to use an explicit scaling, instead of altering the initialization scheme for notational convenience.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Convolutional ResNet: Lastly, we consider the convolutional ResNet architecture. Again we define the prediction function in a recursive way.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Each patch has size $qd_{h - 1}$ and this implies a map ${\phi_{h}{(\mathbf{x}^{({h - 1})})}} \in {\mathbb{R}}^{{qd_{h - 1}} \times p}$. For example, when the stride is $1$ and $q = 3$ where we let $\mathbf{x}_{:,0}^{({h - 1})} = \mathbf{x}_{:,{p + 1}}^{({h - 1})} = \mathbf{0}$, i.e., zero-padding. Note this operator has the property because each element from $\mathbf{x}^{({h - 1})}$ at least appears once and at most appears $q$ times. In practice, $q$ is often small like $3 \times 3$, so throughout the paper we view $q$ as a constant in our theoretical analysis.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

To learn the deep neural network, we consider the randomly initialized gradient descent algorithm to find the global minimizer of the empirical loss. Specifically, we use the following random initialization scheme. For every level $h \in {\lbrack H\rbrack}$, each entry is sampled from a standard Gaussian distribution, $\mathbf{W}_{ij}^{(h)} \sim {N{}}$ and each entry of the output layer $\mathbf{a}$ is also sampled from $N{}$. In this paper, we train all layers by gradient descent, for ${k = {1,2,\ldots}},$ and $h \in {\lbrack H\rbrack}$ where $\eta > 0$ is the step size.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

In this section, we describe our main idea of proving the global convergence of gradient descent. Our proof technique is inspired by Du et al. who proposed to study the dynamics of differences between labels and predictions. Here the individual prediction at the $k$-th iteration is and we denote ${\mathbf{u}{(k)}} = \left({u_{1}{(k)}},\ldots,{u_{n}{(k)}} \right)^{\top} \in {\mathbb{R}}^{n}$. Du et al. showed that for two-layer fully-connected neural network, the sequence $\left\{ {\mathbf{y} - {\mathbf{u}{(k)}}} \right\}_{k = 0}^{\infty}$ admits the following dynamics where ${\mathbf{H}{(k)}} \in {\mathbb{R}}^{n \times n}$ is a Gram matrix with^55^5This formula is for the setting that only the first layer is trained.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

We leverage this insight to our deep neural network setting.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

Note for all $h \in {\lbrack{H + 1}\rbrack}$, each entry of $\mathbf{G}^{(h)}{(k)}$ is an inner product. Therefore, $\mathbf{G}^{(h)}{(k)}$ is a positive semi-definite (PSD) matrix for $h \in {\lbrack{H + 1}\rbrack}$. Furthermore, if there exists one $h \in {\lbrack H\rbrack}$ that $\mathbf{G}^{(h)}{(k)}$ is strictly positive definite, then if one chooses the step size $\eta$ to be sufficiently small, the loss decreases at the $k$-th iteration according the analysis of power method.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

In this paper we focus on $\mathbf{G}^{(H)}{(k)}$, the gram matrix induced by the weights from $H$-th layer for simplicity at the cost of a minor degradation in convergence rate.^66^6Using the contribution of all the gram matrices to the minimum eigenvalue can potentially improve the convergence rate.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

We use the similar observation in that we show if the width is large enough for all layers, for all $k = {0,1,\ldots}$, $\mathbf{G}^{(H)}{(k)}$ is close to a fixed matrix $\mathbf{K}^{(H)} \in {\mathbb{R}}^{n \times n}$ which depends on the input data, neural network architecture and the activation but does not depend on neural network parameters $\theta$. According to the analysis of the power method, once we establish this, as long as $\mathbf{K}^{(H)}$ is strictly positive definite, then the gradient descent enjoys a linear convergence rate. We will show for $\mathbf{K}^{(H)}$ is strictly positive definite as long as the training data is not degenerate (c.f.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

Proposition F.1 for the Fully-connected Neural Network ‣ Appendix F Full Rankness of 𝐊^(ℎ) ‣ Gradient Descent Finds Global Minima of Deep Neural Networks") and F.2 for ResNet ‣ Appendix F Full Rankness of 𝐊^(ℎ) ‣ Gradient Descent Finds Global Minima of Deep Neural Networks")).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Technique Overview", "weight": 1.0} -->

While following the similar high-level analysis framework proposed by Du et al., analyzing the convergence of gradient descent for *deep* neural network is significantly more involved and requires new technical tools. To show $\mathbf{G}^{(H)}{(k)}$ is close to $\mathbf{K}^{(H)}$, we have two steps. First, we show in the initialization phase $\mathbf{G}^{(H)}{}$ is close to $\mathbf{K}^{(H)}$. Second, we show during training $\mathbf{G}^{(H)}{(k)}$ is close to $\mathbf{G}^{(H)}{}$ for $k = {1,2,\ldots}$. Below we give overviews of these two steps.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Analysis of Random Initialization", "weight": 1.0} -->

Unlike in which they showed $\mathbf{H}{}$ is close to $\mathbf{H}^{\infty}$ via a simple concentration inequality, showing $\mathbf{G}^{(H)}{}$ is close to $\mathbf{K}^{(H)}$ requires more subtle calculations. First, as will be clear in the following sections, $\mathbf{K}^{(H)}$ is a recursively defined matrix. Therefore, we need to analyze how the perturbation (due to randomness of initialization and finite $m$) from lower layers propagates to the $H$-th layer. Second, this perturbation propagation involves non-linear operations due to the activation function. To quantitatively characterize this perturbation propagation dynamics, we use induction and leverage techniques from Malliavin calculus. We derive a general framework that allows us to analyze the initialization behavior for the fully-connected neural network, ResNet, convolutional ResNet and other potential neural network architectures in a unified way.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Analysis of Random Initialization", "weight": 1.0} -->

One important finding in our analysis is that ResNet architecture makes the "perturbation propagation" more stable. The high level intuition is the following. For fully connected neural network, suppose we have some perturbation $\left\| {{\mathbf{G}^{}{}} - \mathbf{K}^{}} \right\|_{2} \leq \mathcal{E}_{1}$ in the first layer. This perturbation propagates to the $H$-th layer admits the form Therefore, we need to have $\mathcal{E}_{1} \leq \frac{1}{2^{O{(H)}}}$ and this makes $m$ have exponential dependency on $H$.^77^7We not mean to imply that fully-connected networks necessarily depend exponentially on $H$, but simply to illustrate in our analysis why the exponential dependence arises. For specific activations such as ReLU and careful initialization schemes, this exponential dependence may be avoided.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Analysis of Random Initialization", "weight": 1.0} -->

On the other hand, for ResNet the perturbation propagation admits the form Therefore we do not have the exponential explosion problem for ResNet. We refer readers to Section E for details.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Analysis of Perturbation of During Training", "weight": 1.0} -->

In the two-layer neural network setting, they are able to show *every* weight vector of the first layer is close to its initialization, i.e., $\left\| {{\mathbf{W}^{}{(k)}} - {\mathbf{W}^{}{}}} \right\|_{2,\infty}$ is small for $k = {0,1,\ldots}$. While establishing this condition for two-layer neural network is not hard, this condition may not hold for multi-layer neural networks. In this paper, we show instead, the averaged Frobenius norm is small for all $k = {0,1,\ldots}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Analysis of Perturbation of During Training", "weight": 1.0} -->

Similar to the analysis in the initialization, showing Equation is small is highly involved because again, we need to analyze how the perturbation propagates. We develop a unified proof strategy for the fully-connected neural network, ResNet and convolutional ResNet. Our analysis in this step again sheds light on the benefit of using ResNet architecture for training. The high-level intuition is similar to Equation. See Section B, C, and D for details.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Warm Up: Convergence Result of GD for Deep Fully-connected Neural Networks", "weight": 1.0} -->

In this section, as a warm up, we show gradient descent with a constant positive step size converges to the global minimum at a linear rate. As we discussed in Section 4, the convergence rate depends on least eigenvalue of the Gram matrix $\mathbf{K}^{(H)}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence Result of GD for ResNet", "weight": 1.0} -->

In this section we consider the convergence of gradient descent for training a ResNet. We will focus on how much over-parameterization is needed to ensure the global convergence of gradient descent and compare it with fully-connected neural networks. Again we first define the key Gram matrix whose least eigenvalue will determine the convergence rate.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence Result of GD for Convolutional ResNet", "weight": 1.0} -->

In this section we generalize the convergence result of gradient descent for ResNet to convolutional ResNet. Again, we focus on how much over-parameterization is needed to ensure the global convergence of gradient descent. Similar to previous sections, we first define the $\mathbf{K}^{(H)}$ for this architecture.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we show that gradient descent on deep overparametrized networks can obtain zero training loss. Our proof builds on a careful analysis of the random initialization scheme and a perturbation analysis which shows that the Gram matrix is increasingly stable under overparametrization. These techniques allow us to show that every step of gradient descent decreases the loss at a geometric rate.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We list some directions for future research: The current paper focuses on the training loss, but does not address the test loss. It would be an important problem to show that gradient descent can also find solutions of low test loss. In particular, existing work only demonstrate that gradient descent works under the same situations as kernel methods and random feature methods. To further investigate of generalization behavior, we believe some algorithm-dependent analyses may be useful.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The width of the layers $m$ is polynomial in all the parameters for the ResNet architecture, but still very large. Realistic networks have number of parameters, not width, a large constant multiple of $n$. We consider improving the analysis to cover commonly utilized networks an important open problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The current analysis is for gradient descent, instead of stochastic gradient descent. We believe the analysis can be extended to stochastic gradient, while maintaining the linear convergence rate.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The convergence rate can be potentially improved if the minimum eigenvalue takes into account the contribution of all Gram matrices, but this would considerably complicate the initialization and perturbation analysis.
