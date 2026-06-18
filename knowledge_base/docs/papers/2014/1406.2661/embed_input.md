<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Generative Adversarial Networks

Topics include Generative model, Generative adversarial network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The promise of deep learning is to discover rich, hierarchical models that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have involved discriminative models, usually those that map a high-dimensional, rich sensory input to a class label. These striking successes have primarily been based on the backpropagation and dropout algorithms, using piecewise linear units which have a particularly well-behaved gradient. Deep generative models have had less of an impact, due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context. We propose a new generative model estimation procedure that sidesteps these difficulties. ^11^1All code and hyperparameters available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the proposed adversarial nets framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution. The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistiguishable from the genuine articles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This framework can yield specific training algorithms for many kinds of model and optimization algorithm. In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as adversarial nets. In this case, we can train both models using only the highly successful backpropagation and dropout algorithms and sample from the generative model using only forward propagation. No approximate inference or Markov chains are necessary.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

The adversarial modeling framework is most straightforward to apply when the models are both multilayer perceptrons. To learn the generator's distribution $p_{g}$ over data $\mathbf{x}$, we define a prior on input noise variables $p_{\mathbf{z}}{({\mathbf{z}})}$, then represent a mapping to data space as $G{({\mathbf{z}};\theta_{g})}$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_{g}$. We also define a second multilayer perceptron $D{({\mathbf{x}};\theta_{d})}$ that outputs a single scalar. $D{({\mathbf{x}})}$ represents the probability that $\mathbf{x}$ came from the data rather than $p_{g}$. We train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

In the next section, we present a theoretical analysis of adversarial nets, essentially showing that the training criterion allows one to recover the data generating distribution as $G$ and $D$ are given enough capacity, i.e., in the non-parametric limit. See Figure 1 for a less formal, more pedagogical explanation of the approach. In practice, we must implement the game using an iterative, numerical approach. Optimizing $D$ to completion in the inner loop of training is computationally prohibitive, and on finite datasets would result in overfitting. Instead, we alternate between $k$ steps of optimizing $D$ and one step of optimizing $G$. This results in $D$ being maintained near its optimal solution, so long as $G$ changes slowly enough. This strategy is analogous to the way that SML/PCD training maintains samples from a Markov chain from one learning step to the next in order to avoid burning in a Markov chain as part of the inner loop of learning. The procedure is formally presented in Algorithm 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

In practice, equation 1 may not provide sufficient gradient for $G$ to learn well. Early in learning, when $G$ is poor, $D$ can reject samples with high confidence because they are clearly different from the training data. In this case, $\log{({1 - {D{({G{({\mathbf{z}})}})}}})}$ saturates. Rather than training $G$ to minimize $\log{({1 - {D{({G{({\mathbf{z}})}})}}})}$ we can train $G$ to maximize ${\log D}{({G{({\mathbf{z}})}})}$. This objective function results in the same fixed point of the dynamics of $G$ and $D$ but provides much stronger gradients early in learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

for number of training iterations do
• Sample minibatch of m noise samples {z, …, z(m)} from noise prior pg (z).
• Sample minibatch of m examples {x, …, x(m)} from data generating distribution pdata (x).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

• Sample minibatch of m noise samples {z, …, z(m)} from noise prior pg (z).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Adversarial nets", "weight": 1.0} -->

end forThe gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.
Algorithm 1 Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, k, is a hyperparameter. We used k = 1, the least expensive option, in our experiments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

The generator $G$ implicitly defines a probability distribution $p_{g}$ as the distribution of the samples $G{({\mathbf{z}})}$ obtained when ${\mathbf{z}} \sim p_{\mathbf{z}}$. Therefore, we would like Algorithm 1 to converge to a good estimator of $p_{\text{data}}$, if given enough capacity and training time. The results of this section are done in a non-parametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

We will show in section 4.1 that this minimax game has a global optimum for $p_{g} = p_{\text{data}}$. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Global Optimality of $p_{g} = p_{\\text{data}}$", "weight": 1.0} -->

We first consider the optimal discriminator $D$ for any given generator $G$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experiments", "weight": 1.0} -->

We trained adversarial nets an a range of datasets including MNIST, the Toronto Face Database (TFD), and CIFAR-10. The generator nets used a mixture of rectifier linear activations and sigmoid activations, while the discriminator net used maxout activations. Dropout was applied in training the discriminator net. While our theoretical framework permits the use of dropout and other noise at intermediate layers of the generator, we used noise as the input to only the bottommost layer of the generator network.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

We estimate probability of the test set data under $p_{g}$ by fitting a Gaussian Parzen window to the samples generated with $G$ and reporting the log-likelihood under this distribution. The $\sigma$ parameter of the Gaussians was obtained by cross validation on the validation set. This procedure was introduced in Breuleux et al. and used for various generative models for which the exact likelihood is not tractable. Results are reported in Table 1. This method of estimating the likelihood has somewhat high variance and does not perform well in high dimensional spaces but it is the best method available to our knowledge. Advances in generative models that can sample but not estimate likelihood directly motivate further research into how to evaluate such models.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Figures 2 and 3 we show samples drawn from the generator net after training. While we make no claim that these samples are better than samples generated by existing methods, we believe that these samples are at least competitive with the better generative models in the literature and highlight the potential of the adversarial framework.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

Deep directed graphical models
Deep undirected graphical models

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

Inference needed during training.
Inference needed during training. MCMC needed to approximate partition function gradient.
Enforced tradeoff between mixing and power of reconstruction generation
Synchronizing the discriminator with the generator. Helvetica.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

Learned approximate inference
Learned approximate inference

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

Requires Markov chain
Requires Markov chain

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

Intractable, may be approximated with AIS
Intractable, may be approximated with AIS
Not explicitly represented, may be approximated with Parzen density estimation
Not explicitly represented, may be approximated with Parzen density estimation

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

Nearly all models incur extreme difficulty
Careful design needed to ensure multiple properties
Any differentiable function is theoretically permitted
Any differentiable function is theoretically permitted

<!-- chunk {"id": "body-0024", "role": "body", "section": "Advantages and disadvantages", "weight": 1.0} -->

This new framework comes with advantages and disadvantages relative to previous modeling frameworks. The disadvantages are primarily that there is no explicit representation of $p_{g}{({\mathbf{x}})}$, and that $D$ must be synchronized well with $G$ during training (in particular, $G$ must not be trained too much without updating $D$, in order to avoid "the Helvetica scenario" in which $G$ collapses too many values of $\mathbf{z}$ to the same value of $\mathbf{x}$ to have enough diversity to model $p_{\text{data}}$), much as the negative chains of a Boltzmann machine must be kept up to date between learning steps. The advantages are that Markov chains are never needed, only backprop is used to obtain gradients, no inference is needed during learning, and a wide variety of functions can be incorporated into the model. Table 2 summarizes the comparison of generative adversarial nets with other generative modeling approaches.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Advantages and disadvantages", "weight": 1.0} -->

The aforementioned advantages are primarily computational. Adversarial models may also gain some statistical advantage from the generator network not being updated directly with data examples, but only with gradients flowing through the discriminator. This means that components of the input are not copied directly into the generator's parameters. Another advantage of adversarial networks is that they can represent very sharp, even degenerate distributions, while methods based on Markov chains require that the distribution be somewhat blurry in order for the chains to be able to mix between modes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

A conditional generative model $p{({{\mathbf{x}} \mid {\mathbf{c}}})}$ can be obtained by adding $\mathbf{c}$ as input to both $G$ and $D$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Learned approximate inference can be performed by training an auxiliary network to predict $\mathbf{z}$ given $\mathbf{x}$. This is similar to the inference net trained by the wake-sleep algorithm but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

One can approximately model all conditionals $p{({{\mathbf{x}}_{S} \mid {\mathbf{x}}_{\mathit{S\not{}}}})}$ where $S$ is a subset of the indices of $\mathbf{x}$ by training a family of conditional models that share parameters. Essentially, one can use adversarial nets to implement a stochastic extension of the deterministic MP-DBM.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Semi-supervised learning: features from the discriminator or inference net could improve performance of classifiers when limited labeled data is available.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Efficiency improvements: training could be accelerated greatly by divising better methods for coordinating $G$ and $D$ or determining better distributions to sample $\mathbf{z}$ from during training.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

This paper has demonstrated the viability of the adversarial modeling framework, suggesting that these research directions could prove useful.
