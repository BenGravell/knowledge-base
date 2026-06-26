<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Auto-Encoding Variational Bayes

Topics include Variational autoencoders, Variational inference, Reparameterization trick, Latent variable models, Amortized inference, Generative modeling, Stochastic gradients.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the variational autoencoder framework by pairing a neural recognition model with a differentiable stochastic estimator for variational lower-bound optimization. The key contribution is the reparameterization trick for continuous latent variables, which makes scalable amortized inference practical and turns directed latent-variable models into trainable encoder-decoder systems for generation, representation, denoising, and visualization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

How can we perform efficient inference and learning in directed probabilistic models, in the presence of continuous latent variables with intractable posterior distributions, and large datasets? We introduce a stochastic variational inference and learning algorithm that scales to large datasets and, under some mild differentiability conditions, even works in the intractable case. Our contributions are two-fold. First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods. Second, we show that for i.i.d. datasets with continuous latent variables per datapoint, posterior inference can be made especially efficient by fitting an approximate inference model (also called a recognition model) to the intractable posterior using the proposed lower bound estimator. Theoretical advantages are reflected in experimental results.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

How can we perform efficient approximate inference and learning with directed probabilistic models whose continuous latent variables and/or parameters have intractable posterior distributions? The variational Bayesian (VB) approach involves the optimization of an approximation to the intractable posterior. Unfortunately, the common mean-field approach requires analytical solutions of expectations w.r.t. the approximate posterior, which are also intractable in the general case. We show how a reparameterization of the variational lower bound yields a simple differentiable unbiased estimator of the lower bound; this SGVB (Stochastic Gradient Variational Bayes) estimator can be used for efficient approximate posterior inference in almost any model with continuous latent variables and/or parameters, and is straightforward to optimize using standard stochastic gradient ascent techniques.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the case of an i.i.d. dataset and continuous latent variables per datapoint, we propose the Auto-Encoding VB (AEVB) algorithm. In the AEVB algorithm we make inference and learning especially efficient by using the SGVB estimator to optimize a recognition model that allows us to perform very efficient approximate posterior inference using simple ancestral sampling, which in turn allows us to efficiently learn the model parameters, without the need of expensive iterative inference schemes (such as MCMC) per datapoint. The learned approximate posterior inference model can also be used for a host of tasks such as recognition, denoising, representation and visualization purposes. When a neural network is used for the recognition model, we arrive at the *variational auto-encoder*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Method", "weight": 1.0} -->

The strategy in this section can be used to derive a lower bound estimator (a stochastic objective function) for a variety of directed graphical models with continuous latent variables. We will restrict ourselves here to the common case where we have an i.i.d. dataset with latent variables per datapoint, and where we like to perform maximum likelihood (ML) or maximum a posteriori (MAP) inference on the (global) parameters, and variational inference on the latent variables. It is, for example, straightforward to extend this scenario to the case where we also perform variational inference on the global parameters; that algorithm is put in the appendix, but experiments with that case are left to future work. Note that our method can be applied to online, non-stationary settings, e.g. streaming data, but here we assume a fixed dataset for simplicity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

Let us consider some dataset $\mathbf{X} = {\{\mathbf{x}^{(i)}\}}_{i = 1}^{N}$ consisting of $N$ i.i.d. samples of some continuous or discrete variable $\mathbf{x}$. We assume that the data are generated by some random process, involving an unobserved continuous random variable $\mathbf{z}$. The process consists of two steps: a value $\mathbf{z}^{(i)}$ is generated from some prior distribution $p_{{\mathbf{θ}}^{\ast}}{(\mathbf{z})}$; a value $\mathbf{x}^{(i)}$ is generated from some conditional distribution $p_{{\mathbf{θ}}^{\ast}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

We assume that the prior $p_{{\mathbf{θ}}^{\ast}}{(\mathbf{z})}$ and likelihood $p_{{\mathbf{θ}}^{\ast}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$ come from parametric families of distributions $p_{\mathbf{θ}}{(\mathbf{z})}$ and $p_{\mathbf{θ}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$, and that their PDFs are differentiable almost everywhere w.r.t. both $\mathbf{θ}$ and $\mathbf{z}$. Unfortunately, a lot of this process is hidden from our view: the true parameters ${\mathbf{θ}}^{\ast}$ as well as the values of the latent variables $\mathbf{z}^{(i)}$ are unknown to us.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

Very importantly, we *do not* make the common simplifying assumptions about the marginal or posterior probabilities. Conversely, we are here interested in a general algorithm that even works efficiently in the case of: *Intractability*: the case where the integral of the marginal likelihood ${p_{\mathbf{θ}}{(\mathbf{x})}} = {\int{p_{\mathbf{θ}}{(\mathbf{z})}p_{\mathbf{θ}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}{d\mathbf{z}}}}$ is intractable (so we cannot evaluate or differentiate the marginal likelihood), where the true posterior density ${p_{\mathbf{θ}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}} = {{{p_{\mathbf{θ}}{(\left.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

\mathbf{x} \middle| \mathbf{z} \right.)}p_{\mathbf{θ}}{(\mathbf{z})}}/p_{\mathbf{θ}}}{(\mathbf{x})}}$ is intractable (so the EM algorithm cannot be used), and where the required integrals for any reasonable mean-field VB algorithm are also intractable. These intractabilities are quite common and appear in cases of moderately complicated likelihood functions $p_{\mathbf{θ}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$, e.g. a neural network with a nonlinear hidden layer.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

*A large dataset*: we have so much data that batch optimization is too costly; we would like to make parameter updates using small minibatches or even single datapoints. Sampling-based solutions, e.g. Monte Carlo EM, would in general be too slow, since it involves a typically expensive sampling loop per datapoint.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

We are interested, and propose a solution to, three related problems in the above scenario: Efficient approximate ML or MAP estimation for the parameters $\mathbf{θ}$. The parameters can be of interest themselves, e.g. if we are analyzing some natural process. They also allow us to mimic the hidden random process and generate artificial data that resembles the real data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

Efficient approximate posterior inference of the latent variable $\mathbf{z}$ given an observed value $\mathbf{x}$ for a choice of parameters $\mathbf{θ}$. This is useful for coding or data representation tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

Efficient approximate marginal inference of the variable $\mathbf{x}$. This allows us to perform all kinds of inference tasks where a prior over $\mathbf{x}$ is required. Common applications in computer vision include image denoising, inpainting and super-resolution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

For the purpose of solving the above problems, let us introduce a recognition model $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$: an approximation to the intractable true posterior $p_{\mathbf{θ}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$. Note that in contrast with the approximate posterior in mean-field variational inference, it is not necessarily factorial and its parameters $\mathbf{\phi}$ are not computed from some closed-form expectation. Instead, we'll introduce a method for learning the recognition model parameters $\mathbf{\phi}$ jointly with the generative model parameters $\mathbf{θ}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem scenario", "weight": 1.0} -->

From a coding theory perspective, the unobserved variables $\mathbf{z}$ have an interpretation as a latent representation or *code*. In this paper we will therefore also refer to the recognition model $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ as a probabilistic *encoder*, since given a datapoint $\mathbf{x}$ it produces a distribution (e.g. a Gaussian) over the possible values of the code $\mathbf{z}$ from which the datapoint $\mathbf{x}$ could have been generated. In a similar vein we will refer to $p_{\mathbf{θ}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$ as a probabilistic *decoder*, since given a code $\mathbf{z}$ it produces a distribution over the possible corresponding values of $\mathbf{x}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

In this section we introduce a practical estimator of the lower bound and its derivatives w.r.t. the parameters. We assume an approximate posterior in the form $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$, but please note that the technique can be applied to the case $q_{\mathbf{\phi}}{(\mathbf{z})}$, i.e. where we do not condition on $\mathbf{x}$, as well. The fully variational Bayesian method for inferring a posterior over the parameters is given in the appendix.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

Under certain mild conditions outlined in section 2.4 for a chosen approximate posterior $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ we can reparameterize the random variable $\overset{\sim}{\mathbf{z}} \sim {q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}}$ using a differentiable transformation $g_{\mathbf{\phi}}{(\mathbf{\epsilon},\mathbf{x})}$ of an (auxiliary) noise variable $\mathbf{\epsilon}$: See section 2.4 for general strategies for chosing such an approriate distribution $p{(\mathbf{\epsilon})}$ and function $g_{\mathbf{\phi}}{(\mathbf{\epsilon},\mathbf{x})}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

We can now form Monte Carlo estimates of expectations of some function $f{(\mathbf{z})}$ w.r.t. $q_{\mathbf{\phi}}{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

can be integrated analytically (see appendix B||𝑝_𝜽(𝐳)), Gaussian case ‣ Auto-Encoding Variational Bayes")), such that only the expected reconstruction error ${\mathbb{E}}_{q_{\mathbf{\phi}}{({\mathbf{z}|\mathbf{x}^{(i)}})}}\left\lbrack {{\log p_{\mathbf{θ}}}{(\left. \mathbf{x}^{(i)} \middle| \mathbf{z} \right.)}} \right\rbrack$ requires estimation by sampling. The KL-divergence term can then be interpreted as regularizing $\mathbf{\phi}$, encouraging the approximate posterior to be close to the prior $p_{\mathbf{θ}}{(\mathbf{z})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

This yields a second version of the SGVB estimator ${{\overset{\sim}{\mathcal{L}}}^{B}{({\mathbf{θ}},\mathbf{\phi};\mathbf{x}^{(i)})}} \simeq {\mathcal{L}{({\mathbf{θ}},\mathbf{\phi};\mathbf{x}^{(i)})}}$, corresponding to eq., which typically has less variance than the generic estimator: Given multiple datapoints from a dataset $\mathbf{X}$ with $N$ datapoints, we can construct an estimator of the marginal likelihood lower bound of the full dataset, based on minibatches: where the minibatch $\mathbf{X}^{M} = {\{\mathbf{x}^{(i)}\}}_{i = 1}^{M}$ is a randomly drawn sample of $M$ datapoints from the full dataset $\mathbf{X}$ with

<!-- chunk {"id": "body-0022", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

In our experiments we found that the number of samples $L$ per datapoint can be set to $1$ as long as the minibatch size $M$ was large enough, e.g. $M = 100$. Derivatives ${\nabla_{{\mathbf{θ}},\mathbf{\phi}}\overset{\sim}{\mathcal{L}}}{({\mathbf{θ}};\mathbf{X}^{M})}$ can be taken, and the resulting gradients can be used in conjunction with stochastic optimization methods such as SGD or Adagrad. See algorithm 1 for a basic approach to compute the stochastic gradients.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

A connection with auto-encoders becomes clear when looking at the objective function given at eq.. The first term is (the KL divergence of the approximate posterior from the prior) acts as a regularizer, while the second term is a an expected negative reconstruction error. The function $g_{\mathbf{\phi}}{(.)}$ is chosen such that it maps a datapoint $\mathbf{x}^{(i)}$ and a random noise vector $\mathbf{\epsilon}^{(l)}$ to a sample from the approximate posterior for that datapoint: $\mathbf{z}^{(i,l)} = {g_{\mathbf{\phi}}{(\mathbf{\epsilon}^{(l)},\mathbf{x}^{(i)})}}$ where $\mathbf{z}^{(i,l)} \sim {q_{\mathbf{\phi}}{(\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

\mathbf{z} \middle| \mathbf{x}^{(i)} \right.)}}$. Subsequently, the sample $\mathbf{z}^{(i,l)}$ is then input to function ${\log p_{\mathbf{θ}}}{(\left. \mathbf{x}^{(i)} \middle| \mathbf{z}^{(i,l)} \right.)}$, which equals the probability density (or mass) of datapoint $\mathbf{x}^{(i)}$ under the generative model, given $\mathbf{z}^{(i,l)}$. This term is a negative *reconstruction error* in auto-encoder parlance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The SGVB estimator and AEVB algorithm", "weight": 1.0} -->

XM← Random minibatch of M datapoints (drawn from full dataset) ϵ← Random samples from noise distribution p (ϵ) $\mathbf{g}\leftarrow{{\nabla_{{\mathbf{θ}},\mathbf{\phi}}{\overset{\sim}{\mathcal{L}}}^{M}}{({\mathbf{θ}},\mathbf{\phi};\mathbf{X}^{M},\mathbf{\epsilon})}}$ (Gradients of minibatch estimator) θ, ϕ← Update parameters using gradients g (e.g. SGD or Adagrad) until convergence of parameters (θ, ϕ) Algorithm 1 Minibatch version of the Auto-Encoding VB (AEVB) algorithm. Either of the two SGVB estimators in section 2.3 can be used. We use settings M = 100 and L = 1 in experiments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

In order to solve our problem we invoked an alternative method for generating samples from $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$. The essential parameterization trick is quite simple. Let $\mathbf{z}$ be a continuous random variable, and $\mathbf{z} \sim {q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}}$ be some conditional distribution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

It is then often possible to express the random variable $\mathbf{z}$ as a deterministic variable $\mathbf{z} = {g_{\mathbf{\phi}}{(\mathbf{\epsilon},\mathbf{x})}}$, where $\mathbf{\epsilon}$ is an auxiliary variable with independent marginal $p{(\mathbf{\epsilon})}$, and $g_{\mathbf{\phi}}{(.)}$ is some vector-valued function parameterized by $\mathbf{\phi}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

Examples: Exponential, Cauchy, Logistic, Rayleigh, Pareto, Weibull, Reciprocal, Gompertz, Gumbel and Erlang distributions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

Analogous to the Gaussian example, for any "location-scale" family of distributions we can choose the standard distribution (with $\text{location} = 0$, $\text{scale} = 1$) as the auxiliary variable $\mathbf{\epsilon}$, and let $g{(.)} = \text{location} + \text{scale} \cdot \mathbf{\epsilon}$. Examples: Laplace, Elliptical, Student's t, Logistic, Uniform, Triangular and Gaussian distributions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

Composition: It is often possible to express random variables as different transformations of auxiliary variables. Examples: Log-Normal (exponentiation of normally distributed variable), Gamma (a sum over exponentially distributed variables), Dirichlet (weighted sum of Gamma variates), Beta, Chi-Squared, and F distributions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The reparameterization trick", "weight": 1.0} -->

When all three approaches fail, good approximations to the inverse CDF exist requiring computations with time complexity comparable to the PDF (see e.g. for some methods).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example: Variational Auto-Encoder", "weight": 1.0} -->

In this section we'll give an example where we use a neural network for the probabilistic encoder $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ (the approximation to the posterior of the generative model $p_{\mathbf{θ}}{(\mathbf{x},\mathbf{z})}$) and where the parameters $\mathbf{\phi}$ and $\mathbf{θ}$ are optimized jointly with the AEVB algorithm.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example: Variational Auto-Encoder", "weight": 1.0} -->

Let the prior over the latent variables be the centered isotropic multivariate Gaussian ${p_{\mathbf{θ}}{(\mathbf{z})}} = {\mathcal{N}{(\mathbf{z};\mathbf{0},\mathbf{I})}}$. Note that in this case, the prior lacks parameters. We let $p_{\mathbf{θ}}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$ be a multivariate Gaussian (in case of real-valued data) or Bernoulli (in case of binary data) whose distribution parameters are computed from $\mathbf{z}$ with a MLP (a fully-connected neural network with a single hidden layer, see appendix C). Note the true posterior $p_{\mathbf{θ}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ is in this case intractable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example: Variational Auto-Encoder", "weight": 1.0} -->

While there is much freedom in the form $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$, we'll assume the true (but intractable) posterior takes on a approximate Gaussian form with an approximately diagonal covariance. In this case, we can let the variational approximate posterior be a multivariate Gaussian with a diagonal covariance structure^22^2Note that this is just a (simplifying) choice, and not a limitation of our method.: where the mean and s.d. of the approximate posterior, ${\mathbf{μ}}^{(i)}$ and ${\mathbf{σ}}^{(i)}$, are outputs of the encoding MLP, i.e. nonlinear functions of datapoint $\mathbf{x}^{(i)}$ and the variational parameters $\mathbf{\phi}$ (see appendix C).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example: Variational Auto-Encoder", "weight": 1.0} -->

In this model both $p_{\mathbf{θ}}{(\mathbf{z})}$ (the prior) and $q_{\mathbf{\phi}}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ are Gaussian; in this case, we can use the estimator of eq. where the KL divergence can be computed and differentiated without estimation (see appendix B||𝑝_𝜽(𝐳)), Gaussian case ‣ Auto-Encoding Variational Bayes")). The resulting estimator for this model and datapoint $\mathbf{x}^{(i)}$ is: As explained above and in appendix C, the decoding term ${\log p_{\mathbf{θ}}}{(\left. \mathbf{x}^{(i)} \middle| \mathbf{z}^{(i,l)} \right.)}$ is a Bernoulli or Gaussian MLP, depending on the type of data we are modelling.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We trained generative models of images from the MNIST and Frey Face datasets^33^3Available at and compared learning algorithms in terms of the variational lower bound, and the estimated marginal likelihood.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

The generative model (encoder) and variational approximation (decoder) from section 3 were used, where the described encoder and decoder have an equal number of hidden units. Since the Frey Face data are continuous, we used a decoder with Gaussian outputs, identical to the encoder, except that the means were constrained to the interval $$ using a sigmoidal activation function at the decoder output. Note that with *hidden units* we refer to the hidden layer of the neural networks of the encoder and decoder.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Parameters are updated using stochastic gradient ascent where gradients are computed by differentiating the lower bound estimator ${\nabla_{{\mathbf{θ}},\mathbf{\phi}}\mathcal{L}}{({\mathbf{θ}},\mathbf{\phi};\mathbf{X})}$ (see algorithm 1), plus a small weight decay term corresponding to a prior ${p{({\mathbf{θ}})}} = {\mathcal{N}{(0,\mathbf{I})}}$. Optimization of this objective is equivalent to approximate MAP estimation, where the likelihood gradient is approximated by the gradient of the lower bound.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compared performance of AEVB to the wake-sleep algorithm. We employed the same encoder (also called recognition model) for the wake-sleep algorithm and the variational auto-encoder. All parameters, both variational and generative, were initialized by random sampling from $\mathcal{N}{(0,0.01)}$, and were jointly stochastically optimized using the MAP criterion. Stepsizes were adapted with Adagrad; the Adagrad global stepsize parameters were chosen from {0.01, 0.02, 0.1} based on performance on the training set in the first few iterations. Minibatches of size $M = 100$ were used, with $L = 1$ samples per datapoint.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Likelihood lower bound", "weight": 1.0} -->

We trained generative models (decoders) and corresponding encoders (a.k.a. recognition models) having $500$ hidden units in case of MNIST, and $200$ hidden units in case of the Frey Face dataset (to prevent overfitting, since it is a considerably smaller dataset). The chosen number of hidden units is based on prior literature on auto-encoders, and the relative performance of different algorithms was not very sensitive to these choices. Figure 2 shows the results when comparing the lower bounds. Interestingly, superfluous latent variables did not result in overfitting, which is explained by the regularizing nature of the variational bound.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Marginal likelihood", "weight": 1.0} -->

For very low-dimensional latent space it is possible to estimate the marginal likelihood of the learned generative models using an MCMC estimator. More information about the marginal likelihood estimator is available in the appendix. For the encoder and decoder we again used neural networks, this time with 100 hidden units, and 3 latent variables; for higher dimensional latent space the estimates became unreliable. Again, the MNIST dataset was used. The AEVB and Wake-Sleep methods were compared to Monte Carlo EM (MCEM) with a Hybrid Monte Carlo (HMC) sampler; details are in the appendix. We compared the convergence speed for the three algorithms, for a small and large training set size. Results are in figure 3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Visualisation of high-dimensional data", "weight": 1.0} -->

If we choose a low-dimensional latent space (e.g. 2D), we can use the learned encoders (recognition model) to project high-dimensional data to a low-dimensional manifold. See appendix A for visualisations of the 2D latent manifolds for the MNIST and Frey Face datasets.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced a novel estimator of the variational lower bound, Stochastic Gradient VB (SGVB), for efficient approximate inference with continuous latent variables. The proposed estimator can be straightforwardly differentiated and optimized using standard stochastic gradient methods. For the case of i.i.d. datasets and continuous latent variables per datapoint we introduce an efficient algorithm for efficient inference and learning, Auto-Encoding VB (AEVB), that learns an approximate inference model using the SGVB estimator. The theoretical advantages are reflected in experimental results.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Future work", "weight": 1.5} -->

Since the SGVB estimator and the AEVB algorithm can be applied to almost any inference and learning problem with continuous latent variables, there are plenty of future directions: (i) learning hierarchical generative architectures with deep neural networks (e.g. convolutional networks) used for the encoders and decoders, trained jointly with AEVB; (ii) time-series models (i.e. dynamic Bayesian networks); (iii) application of SGVB to the global parameters; (iv) supervised models with latent variables, useful for learning complicated noise distributions.
