<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Predictive Coding as a Neuromorphic Alternative to Backpropagation: A Critical Evaluation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Backpropagation has rapidly become the workhorse credit assignment algorithm for modern deep learning methods. Recently, modified forms of predictive coding (PC), an algorithm with origins in computational neuroscience, have been shown to result in approximately or exactly equal parameter updates to those under backpropagation. Due to this connection, it has been suggested that PC can act as an alternative to backpropagation with desirable properties that may facilitate implementation in neuromorphic systems. Here, we explore these claims using the different contemporary PC variants proposed in the literature. We obtain time complexity bounds for these PC variants which we show are lower-bounded by backpropagation. We also present key properties of these variants that have implications for neurobiological plausibility and their interpretations, particularly from the perspective of standard PC as a variational Bayes algorithm for latent probabilistic models. Our findings shed new light on the connection between the two learning frameworks and suggest that, in its current forms, PC may have more limited potential as a direct replacement of backpropagation than previously envisioned.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Predictive coding (PC) is a prominent neuroscientific theory that has emerged in the last two decades as a highly compelling computational model of perception and action in the brain [rao\_predictive\_1999, friston\_theory\_2005]. From a theoretical standpoint, PC, in its standard formulation, has benefited from its interpretation as a variational Bayes algorithm for learning and inference in latent hierarchical models [friston\_learning\_2003, friston\_theory\_2005, friston\_predictive\_2009, bogacz\_tutorial\_2017] providing it credence as a plausible instantiation of normative theories such as the Bayesian brain hypothesis, and the free-energy principle.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

More empirically, its candidate neurobiological implementation has demonstrated impressively close correspondences to the canonical circuitry of the cortex [bastos\_canonical\_2012, shipp\_neural\_2016], while also successfully explaining or reproducing a number of neurophysiological and cognitive phenomena, such as end-stopping [rao\_predictive\_1999], binocular rivalry [hohwy\_predictive\_2008], attention [feldman\_attention\_2010, kanai\_cerebral\_2015], and biases in the perception of event duration [fountas\_predictive\_2022].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recent work has suggested a connection between modified forms of PC, and backpropagation, suggesting the former as an alternative to the latter with the various benefits one may naturally expect to associate for a theory formulated with neurobiological constraints in mind [millidgePredictiveCodingFuture2022, millidge\_activation\_2020, song\_can\_2020]. These include locality of computation and parallelisability that may lend it improved performance, and greater amenability to implementation on neuromorphic hardware.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The purpose of this work is to investigate these suggestions and clarify more precisely the relationship between backpropagation and PC, particularly with regards to the kinds of assumptions that are necessary to enable such a comparison, and furthermore, to define exactly what advantage PC-based formulations may have with respect to both parallelisability, locality and ultimately, practical performance. In what follows, we re-review some of the ground covered by [rosenbaum\_relationship\_2022], while extending it to discuss the implications for PC in general with respect to computational and memory complexity, as well as compute and memory locality. We also present proofs for lower bounds on the time complexity of current PC variants relative to backpropagation, and validate these proofs empirically. Our work finds that, while the examined algorithms present interesting, biologically-inspired alternative implementations of backpropagation, they are provably guaranteed to be slower under identical problem settings, and that it is unclear to what degree they improve upon locality, particularly in comparison to modern candidate proposals for backpropagation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lastly, we note that when adopting the modifications required to enable such comparisons, PC models diverge from the generative variational Bayes framework, frequently used as the motivational basis of this theory.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

Backpropagation, first introduced by [linnainmaa\_taylor\_1976] in the context of accumulating rounding errors, and later popularised by [rumelhart\_learning\_1986] in the context of neural networks, has quickly become the workhorse credit assignment algorithm for modern deep learning tasks. Described most simply, backpropagation can be seen as an algorithmically efficient implementation of the chain rule from calculus that allows the computation of high dimensional gradients for deeply nested functions with respect to scalar or low-dimensional outputs. It accomplishes this by defining gradients of values deep inside a nested function in terms of the gradients of their children (their functional dependants). The resultant recursive relationship is then evaluated for values closest to the output, sequentially backward. This recursive relationship is what enables backpropagation to efficiently compute gradients with respect to all parameters in the function chain with a single forward and backward computational pass.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

To illustrate how this operates, we present the following simple but highly generic problem setting. Let us consider an arbitrary function $F$, defined by the composition of many constituent functions $f_i$, each optionally parameterised by some set of parameters $\mathbf{\theta_i}$. We may then write the following: where we use $\mu_i$ to denote the intermediary outputs of our composite function, and $x_0, x_L$ to denote known values which are provided as inputs and outputs of our function respectively. $x_0$ and $x_L$ may for example be inputs and classification labels respectively, $\mu_\ell$ may be intermediate activation vectors for a multilayer perceptron, and $f_L$a classification loss.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

If we wish to compute the gradient of any intermediate parameters with respect to our function output $E$, we may then do so by first defining the following simple recursive relationship.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

\frac{\partial f_{\ell}}{\partial \mu_{\ell}}^T & \text{for } \ell=1,\dots,L-1 \\[5pt] \frac{\partial f_L}{\partial \mu_L} & \text{for } \ell=L For multivariate elementary functions, the $\frac{\partial f_{\ell}}{\partial \mu_L}$ terms would correspond to the Jacobian matrices for the elementary functions $f_i$ with respect to $\mathbf{x_i}$. And by virtue of the chain rule, the error terms $e_{\ell}$ would thus equal the gradient of E with respect to $x_{\ell+1}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

Having established error vectors $e_{\ell}$ that correspond to the gradient with respect to $x_\ell$, one may then compute the gradient of output E with respect to an arbitrary intermediate parameter by matrix-multiplying the error vector from the next layer by the Jacobian of the function with respect to the parameters.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Backpropagation", "weight": 1.0} -->

\frac{\partial E}{\partial \mathbf{\theta_{\ell}}} = -\frac{\partial \mu_{\ell+1}}{\mathbf{\theta_{\ell}}}^T e_{\ell+1} Though obvious in this scenario, it will be important for our later comparisons to mention here that all Jacobians mentioned above are evaluated at the values of the feed-forward outputs of our function, which, as we will discuss, may not necessarily be the case for Bayesian PC. We also note that, in practice, the Jacobians specified in Equations ([eq:parameter\_backprop\_equation]) and ([eq:recursive\_backprop\_equations]) are almost never instantiated explicitly. Rather, an automatic differentiation program that implements backpropagation would associate each elementary or constituent function with an associated vector-Jacobian product (VJP) function, which is generally far more computationally and memory efficient [paszke\_automatic\_2017, bradbury\_jax\_2018].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

The cost of computing the forward pass (Equation [eq:forward] and subsequent backward recursions (Equations [eq:recursive\_backprop\_equations] and [eq:parameter\_backprop\_equation]) can be shown to have computational and time cost bounded by a small constant multiple of the cost for a single forward pass through the corresponding elementary function. This well-known result from the automatic differentiation literature is sometimes called the cheap-gradient principle and is one reason why backpropagation has been so successful as a credit assignment algorithm in modern large data settings. This constant was shown to be 3 for rational functions in the seminal work of [baur\_complexity\_1983], and 5 more generally for any function composed of elementary arithmetic and trigonometric functions [griewank\_automatic\_1997, griewank\_evaluating\_2008, griewank\_complexity\_2009]. The precise value of this constant generally also depends upon details regarding the relative costs of various basic mathematical operations (such as addition, multiplication, memory access, and non-linear operations) on the specific hardware being considered.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

For modern deep neural network operations and associated hardware, this constant is generally taken to be 3, [kaplan\_scaling\_2020, hoffmann\_training\_2022], which we adopt for our comparison.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

As we will see, the basic unit of computation for both the current implementations of PC and backpropagation algorithms are the same: the VJP. The cost of computing this VJP is bounded in terms of a forward evaluation via the cheap gradient principle. To levy a comparison between algorithms we may therefore report computational complexity with respect to the cost of computing a single forward pass, which we denote with $\mathcal{C}_i$ and $\mathcal{C}_F$, for elementary constituent functions $f_i$, and the overall composite function $F$respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Following the notation in [griewank\_evaluating\_2008] we denote a computational task associated with a function $F$ as $task(F)$, with the corresponding computational and time complexity referred to as $\text{WORK}\{task(F)\}$ and $\text{TIME} \{task(F)\}$. For simplicity, we assume scalar complexity measures for work and time, and relate the time complexity to work complexity for a single elementary function $f_i$ using some positive valued constant $w$, such that $\text{TIME} \{task(f_i)\} = w \text{WORK} \{task(f_i)\} $, note that this relationship may not be true for other high-level tasks on $F$such as PC inference due to parallel computation, which we will discuss and accommodate for in subsequent sections. Using the cheap gradient principle we can therefore write the following factorisation and bound for the time complexity of backpropagation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Variational PC", "weight": 1.0} -->

We begin by describing the standard formulation of PC as a variational Bayes algorithm, [friston\_learning\_2003, friston\_theory\_2005, bogacz\_tutorial\_2017, buckley\_free\_2017]. Within this context, the PC algorithm can be interpreted as a method for performing inference (over latent states) and learning (over parameters) for a latent hierarchical generative model. In keeping with much of recent work that renders a comparison with backpropagation we will restrict our focus to PC for static (i.e. non-dynamical/time-series-based) observations and states. We will distinguish this formulation with recent modified formulations such as FPA-PC [millidge\_predictive\_2020] and Z-IL [song\_can\_2020, salvatori\_predictive\_2021]by calling it variational PC (VPC) to emphasise that modified formulations may not necessarily correspond to a variational Bayesian inference and learning algorithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Variational PC", "weight": 1.0} -->

For the sake of enabling our subsequent comparisons of PC with backpropagation, we will reuse the elementary functions $f_i$ first defined in Section [sec:backpropagation]in this section for defining the conditional relationships within our hierarchical model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Variational PC", "weight": 1.0} -->

In particular, we will take the outputs of our constituent functions $f_i$ to correspond to means of Gaussian latent random variables, with each Gaussian latent random variable conditioning on its parents. Then, when $f_L$ is a loss function corresponding to the log-likelihood of a particular choice of output distribution $P_L$, (a common problem setting), this results in the following log-joint probability for our probabilistic graphical model: \log p(x_0,..., x_{L-1}, x_L|\theta_0,... \theta_L) = \log p(x_L|x_{L-1}, \theta_{L-1}) +... + \log p(x_1|x_0, \theta_0) x_\ell | x_{\ell-1} \sim \left.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Variational PC", "weight": 1.0} -->

\mathcal{N}(f_{\ell-1}(x_{\ell-1}, \theta_{\ell-1}), \Sigma_\ell)) & \text{for } \ell=1,...,L-1 \\& \text{for } \ell=L Given this model, PC answers the question of how one can learn the parameters $\mathbf{\theta}$ that maximise their model evidence, $\log p(\mathbf{x}_{\text{OBS}}^{},.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Variational PC", "weight": 1.0} -->

\mathbf{x}_{\text{OBS}}^{(D)}|\boldsymbol{\theta})$, where notational simplicity we have combined all observations ($x_0$ and $x_L$), latent states ($x_1,...,x_{L-1}$), and parameters ($\theta_0,...,\theta_L$) into the vectors $\mathbf{x}_{\text{OBS}}$, $\textbf{x}_{\text{LAT}}$, $\boldsymbol{\theta}$ respectively, and superscript indices denote samples from a data generating (observation) distribution $\mathcal{X}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Variational PC", "weight": 1.0} -->

The standard difficulty with this optimisation of the model parameters to maximise the model evidence rests upon the intractable marginalisation over latent states ($\textbf{x}_{\text{LAT}}$). The variational Bayes solution to this issue rests upon the optimisation of an evidence lower bound (ELBO), equivalently often called the (negative) free energy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Variational PC", "weight": 1.0} -->

This bound relies upon a tractable form for an approximate posterior density over latent states \text{ELBO} = E_{q(\mathbf{x}_{\text{LAT}})}\left[\log p (\mathbf{x}_{\text{OBS}}, \mathbf{x}_{\text{LAT}}|\boldsymbol{\theta})\right] - E_{q(\mathbf{x}_{\text{LAT}})}\left[\log q(\mathbf{x}_{\text{LAT}})\right] For the approximate posterior density $q(\textbf{x}_{\text{LAT}})$, PC adopts a point-mass (Dirac $\delta$) distribution, either implicitly [buckley\_free\_2017, bogacz\_tutorial\_2017, millidge\_predictive\_2020], or explicitly [friston\_learning\_2003, friston\_theory\_2005].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Variational PC", "weight": 1.0} -->

By denoting the centre of this Dirac $\delta$ delta distribution with $\boldsymbol{\phi}$, the above bound simplifies to the objective \text{ELBO}_{\mathbf{PC}}(\boldsymbol{\phi}, \boldsymbol{\theta}) = \log p (\mathbf{x}_{\text{OBS}}, \boldsymbol{\phi}|\boldsymbol{\theta}) PC optimises this function by first enacting an ascent with respect to the the Dirac $\delta$ parameters $\phi$ corresponding to the modes of the approximate posterior over latent states. Once the maxima for the log joint probability with respect to $\phi$ is obtained, we then update our parameters $\theta$ by computing the gradient with respect to the log joint evaluated at these values of $\phi$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Variational PC", "weight": 1.0} -->

Depending on one's perspective, this initial step can be seen, variously as: obtaining an MAP (maximum a posteriori) estimate over latent states (due to the maximisation of the log-joint), or as an expectation step within an Expectation-Maximisation scheme [friston\_theory\_2005], or as a variational bound tightening step from a variational Bayes perspective. The subsequent maximisation step (optimisation of $\theta$) can then be implemented via a mini-batch or stochastic gradient descent (SGD) procedure allowing one to tractably optimise against a large dataset of observations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Variational PC", "weight": 1.0} -->

- Define a (possibly hierarchical) graphical model over latent states ($\mathbf{x}_{\text{LAT}}$) and observations ($\mathbf{x}_{\text{OBS}}$) with parameters $\boldsymbol{\theta}$ (i.e. $\log p (\mathbf{x}_{\text{OBS}}, \mathbf{x}_{\text{LAT}}|\boldsymbol{\theta})$) - For minibatch $\mathbf{x}_{\text{OBS}} \sim \mathcal{D}$, where $\mathcal{D}$ is the data-generating distribution - Obtain MAP estimates ($\mathbf{x}_{\text{MAP}}$) for the latent states by enacting a gradient descent on $-\log p (\mathbf{x}_{\text{OBS}}, \mathbf{x}_{\text{LAT}}|\boldsymbol{\theta})$ - Update the parameters

<!-- chunk {"id": "body-0028", "role": "body", "section": "Variational PC", "weight": 1.0} -->

$\boldsymbol{\theta}$ using SGD with respect to the negative log joint evaluated at the MAP estimates found at the end of inference: $-\log p (\mathbf{x}_{\text{OBS}}, \mathbf{x}_{\text{MAP}}|\boldsymbol{\theta})$ For the sake of subsequent discussion it will be useful to look at the exact functional form and computations occurring in the gradient ascent (inference) procedure outlined in the above algorithm.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Variational PC", "weight": 1.0} -->

First, since the conditional log-likelihoods of latent states in the log joint described by Equation ([eq:log\_joint]) are Gaussian, these, therefore, take the form of a series of squared precision-weighted prediction errors each corresponding to a constituent function $f_i$, plus the output log-likelihood \text{ELBO}_{\text{PC}} &= \log p(x_0, x_1,..., x_{L-1}, x_L) \span \\& \quad + (x_{\ell} - f_{\ell-1}(x_{\ell-1}))^T\Sigma^{-1}_\ell(x_{\ell} - f_{\ell-1}(x_{\ell-1})) \nonumber \\where we have temporarily removed the dependence on parameters $\theta_\ell$for brevity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Variational PC", "weight": 1.0} -->

The gradient of this objective with respect to a particular latent state $x_\ell$ is then simply the precision weighted prediction errors corresponding to predictions of $x_\ell$ from its parents as well as precision weighted prediction errors corresponding to predictions $x_\ell$ makes of its child nodes $x_{\ell+1}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Variational PC", "weight": 1.0} -->

The gradient descent (inference) procedure can therefore be described by the following discretised gradient flow, assuming a Gaussian output log-likelihood for $f_L$ (i.e. Euclidean output loss): &= x_{\ell, t} - \gamma \left.\frac{\partial F}{\partial x_{\ell}}\right|_{x_{\ell, t}} \\&= x_{\ell, t} - \gamma \left[\Sigma^{-1}_{\ell}(x_{\ell, t} - f_{\ell-1}(x_{\ell-1,t})) - \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, t}}^T \Sigma^{-1}_{\ell+1}(x_{\ell+1, t} - f(x_{\ell, t})) \right]

<!-- chunk {"id": "body-0032", "role": "body", "section": "Variational PC", "weight": 1.0} -->

\intertext{where $\gamma$ is some inference step size.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Variational PC", "weight": 1.0} -->

Under the assumption of identity variances, this equation simplifies to} &= x_{\ell, t} - \gamma \left[(x_{\ell, t} - f_{\ell-1}(x_{\ell-1,t})) - \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, t}}^T (x_{\ell+1, t} - f(x_{\ell, t})) \right] \intertext{Written more generically in terms of errors, we can write this to include arbitrary definitions of output loss log-likelihood} &= x_{\ell, t} - \gamma \left[e_{\ell, t} - \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, t}}^T e_{\ell+1, t}

<!-- chunk {"id": "body-0034", "role": "body", "section": "Variational PC", "weight": 1.0} -->

\right] \\(x_{\ell, t} - f_{\ell-1}(x_{\ell-1,t})) & \text{for } \ell=1,...,L-1 \\\frac{\partial f_L}{\partial f_{L-1}}^T & \text{for } \ell=L where we abuse notation and use $f_{L-1}$ to denote both the function, and its output evaluated at the current value of $x_{L-1}$, i.e. $f_{L-1}(x_{L-1, t})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Variational PC", "weight": 1.0} -->

We do this to distinguish it from $\mu_{L}$, and the associated Jacobian in Equation ([eq:recursive\_backprop\_equations]), which denotes the pre-loss output prediction computed using the feed-forward value $\mu_{L-1}$, i.e. $f_{L-1}(\mu_{L-1})$. That is to say, at every inference step, the latent states are updated such that they act to minimise the error corresponding to the current prediction of their latent states, and the error corresponding to the current prediction of their children's latent states.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Variational PC", "weight": 1.0} -->

The model parameters are then updated (via SGD) with the derivative of the log joint evaluated at these converged MAP values. This gradient is the product of the error associated with the conditional distribution it parameterises and the Jacobian of that function with respect to $\theta$. Let $t_c$ be the time at which the variational modes have converged. Then, the gradient of the log joint with respect to the model parameters is given by \frac{\partial F}{\partial \theta_{\ell}} = \frac{\partial f_{\ell}}{\partial \theta_{\ell}}^T e_{\ell+1, t_c} [eq:bpc\_dynamics]-[eq:bpc\_dynamics\_2]) describe the dynamics of the standard PC formulation. Under these dynamics, inference over latent states can be considered MAP inference on a corresponding probabilistic model, and learning can be considered as the maximisation of an ELBO with respect to its model parameters. In particular, this bound corresponds to a point-mass variational distribution assumed over our latent states.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Variational PC", "weight": 1.0} -->

Inverted Configurations: This particular formulation of PC is inverted relative to the standard PC formulation [rao\_predictive\_1999, friston\_learning\_2003, friston\_hierarchical\_2008, buckley\_free\_2017] present in cognitive science, and indeed most generative modelling schemes, in the sense that observations parameterise, and are thus hierarchically higher than, latents such as classification labels. Inverting PC in this way, to render a comparison with backpropagation, has non-trivial implications on neurobiological plausibility.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Variational PC", "weight": 1.0} -->

One of the strengths of standard PC formulations has historically been in the notion that latents hierarchically higher in the cortex have a non-linearly mixing and modulatory effect ($f(x_\ell, \theta_\ell))$) that is congruent with what we know about cortical anatomy; i.e. that top-down backward connections are generally more bifurcating and modulatory, while bottom-up influences, or forward connections, are more driving ($-e_\ell$) [friston\_theory\_2005, friston\_hierarchical\_2008, bastos\_canonical\_2012, shipp\_neural\_2016, markov\_anatomy\_2014].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Variational PC", "weight": 1.0} -->

It is interesting to note that supervised generative (i.e non-inverted) formulations of standard PC have thus far struggled to produce competitive or close to competitive results for complex classification tasks. For example, traditional generative PC models trained to classify and generate MNIST digits are consistently unable to surpass a test set accuracy of 80%, both from our experience and observed here [kinghorn\_preventing\_2022]. The authors are not aware of any example of a traditional (generative) PC succeeding in obtaining competitive classification performance on standard machine learning tasks. Though the possible reasons for this are outside the scope of this paper, it is likely a consequence of either the Gaussian-based supervision signal generally used in existing attempts, or the limitations of the Dirac $\delta$ (point-mass) approximate posterior, for training generative models, as highlighted in [zahid\_curvature-sensitive\_2023].

<!-- chunk {"id": "body-0040", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

(a) Weight transport problem in a standard proposal implementation for backpropagation. (b) Weight symmetry issue in standard PC formulations. Note we exclude additional connectivity necessary for PC, but not relevant to the weight transport problem, for the sake of clarity. (c) An example alternative proposal aimed at solving the weight transport issue for backpropagation Local computation within a neurobiological context generally refers to local plasticity, i.e. synaptic weight updates that are determined by the activity of the neurons they connect, that is to say pre-synaptic and post-synaptic neuronal activity, and synaptic locality. This notion of locality is often used in the context of assessing learning algorithms for their plausibility of implementation in the brain. Historically, a key criticism in the biological plausibility of backpropagation has been due to the presence of this type of non-locality, where it has been called the weight transport problem [grossberg\_competitive\_1987, crick\_recent\_1989, zipser\_neurobiological\_1993].

<!-- chunk {"id": "body-0041", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

Under the problem setting described above Equations ([eq:forward]), the weight transport problem can be summarised as the issue of a particular weight or parameter matrix (e.g. $\theta_\ell$) involved in the computation of feed-forward activation $\mu_{\ell+1}$, being transported for use in the computation of errors $e_\ell$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

Specifically, if one considers a constituent function $f_\ell$ consisting of an affine transformation given by the weight matrix $\theta_\ell$ and a non-linearity $g(\cdot)$, such that \mu_{\ell+1} &= f_\ell(\mu_\ell, \theta_\ell) = g(\theta_\ell \mu_\ell) \\\intertext{The computation of $e_\ell$ is then} e_\ell &= \frac{\partial \mu_{\ell+1}}{\partial \mu_{\ell}}^T e_{\ell+1} = g'(\theta_\ell \mu_\ell) \theta_\ell^T e_{\ell+1} where we require reusing the forward weights due to the transpose weight term $\theta_\ell^T$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

With respect to backpropagation there have been a number of well-known attempts at resolving the implausibility of the weight transport issue. These include the influential work [lillicrap\_random\_2016], where it was shown that computing the error via a fixed random matrix $B$ replacing $\theta_\ell$ could nonetheless facilitate learning without the requirement that the forward parameters be reused. However, the use of random feedback weights only remained performant for shallow networks, failing for deeper models. Subsequent and more recent work has demonstrated that training these feedback weights separately can improve performance for deeper models [amit\_deep\_2019, akrout\_deep\_2019].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

While these various models resolve the weight transport issue in one way or another, they frequently require or induce additional assumptions about the neurobiological machinery required for their implementation. The work of [zipser\_neurobiological\_1993] for example required initialising feedforward and feedback matrices identically, which was criticised and resolved using weight decay by [kolen\_backpropagation\_1994]. Both [kolen\_backpropagation\_1994] and [zipser\_neurobiological\_1993] however required transmitting the synaptic weight changes between separate networks, which has itself also been argued as implausible [akrout\_deep\_2019]. [amit\_deep\_2019] required strict and regimented sequencing of computation, with feed-forward neurons subsequently also acting as error neurons, which can be seen diagramatically in Figure [fig:weight\_transport\_vs\_symmetry].

<!-- chunk {"id": "body-0045", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

Lastly, for the sake of further comparison it, both [lillicrap\_random\_2016] and [akrout\_deep\_2019] require interactions between the activations within forward and backward pathways, usually implemented as three-factor style learning rules, which induce a complexity beyond simple two-factor Hebbian learning rules. Though, we note, this may not be particularly problematic from the standpoint of neurobiological plausibility given a growing body of literature presenting empirical evidence, or mechanistic proposals for three-factor learning rules [sjostrom\_cooperative\_2006, pawlak\_timing\_2010, urbanczik\_learning\_2014].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

A very similar but slightly different issue to weight transport exists within PC due to the presence of the Jacobian term ($\frac{\partial f_\ell}{\partial x_\ell}$) in Equations [eq:bpc\_dynamics] and [eq:bpc\_dynamics\_2].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

g(\theta_\ell x_\ell) Thus, the (negative) identical of the weights that mediate the influence of the subsequent error units ($e_{\ell+1}$) on the previous latent states ($x_\ell$), are also required for the reciprocal connection from latent states to error units.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

See Figure [fig:weight\_transport\_vs\_symmetry] for a depiction of this. This property was identified in some of the earliest narratives on PC [friston\_theory\_2005, friston\_hierarchical\_2008] albeit from the perspective of an advantage of PC's neurobiological plausibility due to the reported prevalence of reciprocal connections in the brain [felleman\_distributed\_1991]. Prevalence of reciprocal connections is not sufficient however, as we, at least naively, require exact equivalence in strengths also.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

We distinguish this issue from that of weight transport by calling it the weight symmetry problem as it requires weight equivalence for forward and reciprocal synapses between the same two pairs of neurons, which is arguably a more addressable issue from the perspective of neurobiological plausibility over the required weight transport in backpropagation. The reason for this is that plasticity is generally considered to be some simple function of pre-synaptic and post-synaptic activity, given that both these activities are accessible for forward and reciprocal synapses it is not implausible that forward and backward weights could come into parity. In particular, given a simple 2-factor Hebbian learning rule, one would expect, at least for simple Hebbian plasticity, that both forward and reciprocal connections could experience the same weight modifications (the product of pre-synaptic and post-synaptic activity). Further incorporating weight decay, would result in weights that eventually synchronise, as demonstrated for the weight transport case by [kolen\_backpropagation\_1994]. This approach, without decay, has indeed been demonstrated with minimal performance degradation on standard PC networks [millidge\_relaxing\_2020].

<!-- chunk {"id": "body-0050", "role": "body", "section": "Memory locality, weight transport and weight symmetry", "weight": 1.0} -->

We will next discuss a number of recent modified formulations of PC which have been presented as neurmorphic alternatives to backpropagation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

Underlying probabilistic model assumed by standard, i.e. variational, PC (VPC) and recent modified forms of PC. Note VPC incorporates probabilistic latent states whereas FPA-PC assumes deterministic states and observations only. Grey circles correspond to observed variables, blue circles correspond to deterministic intermediate states, and orange circles correspond to probabilistic latent states.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

- When the variational modes or latent states ($x_1,..., x_{L-1}$) are initialised to the feed-forward values of the corresponding backpropagation-based computational chain ($\mu_1,...,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

- Case 1 When the feed-forward prediction results in zero output loss (i.e. zero negative log-likelihood loss) - Case 2 When the output variance ($\Sigma_L$) is set sufficiently higher than the remaining variances ($\Sigma_{\ell<L}$), such that the ratio of $\left(\frac{\Sigma_L}{\Sigma_{\ell}}, \forall \ell < L \right)$, goes to infinity and the learning rate is scaled appropriately.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

Both these cases correspond to the same requirement, namely that the values of the latent states, $x_1,...,x_{L-1}$, remain equal, or close, to their feed-forward values at the end of the inference procedure. Said another way, this can be seen as the requirement that the MAP values for the latent states while observing both input observations (e.g. images) and output observations (e.g. classification labels), are equal to the MAP values when conditioning on input observations alone. Another more intuitive framework for understanding this requirement is to note that the inference and learning procedure that results under these set of circumstances is equivalent to doing inference and learning for a probabilistic graphical model in which the intermediate latent states have 0 conditional uncertainty, or variance, and are thus deterministic outputs of the input observations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

Given this framework, learning devolves into enacting maximimum likelihood learning for a probabilistic graphical model in which inputs $x_0$ parameterise an output likelihood via the deep "total" network function $F = f_L \circ f_{L-1}... \circ f_{1} \circ f_{0}$, with observations $x_L$. This is equivalent to enacting maximum likelihood training with backpropagation when the output loss function $f_L$ (see Equations [eq:forward]) corresponds to a valid log-likelihood. See Figure [fig:underlying\_pgm]for a depiction of the probabilistic graphical model assumed by this approach versus standard VPC.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

To see this, observe that this is trivially true for Case 1, where the weight updates from the aforementioned deterministic latent maximum likelihood objective and the PC objective with probabilistic latent states are the same, namely zero, due to the zero error.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

More interestingly, this can also be seen for Case 2, if one considers that scaling up $\Sigma_L$ and rescaling all learning rates by its inverse, is equivalent to scaling down the intermediate variances $\Sigma_{\ell}, \forall \ell < L$, while keeping the output variances fixed, and keeping the learning rate the same. This is arguably a more natural perspective to view this procedure as it allows us to understand what is happening to the underlying probabilistic graphical model that we are training as we do this: namely that we are removing uncertainty over latent states, and thus going from a variational Bayes (free energy minimising) learning procedure to a maximum likelihood learning procedure.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

To demonstrate this, we can look at what happens to the inference and learning equations as we conduct the Case 2 scaling procedure from [whittington\_approximation\_2017]: Consider that we have scaled the label variances $\Sigma_L$ by a large constant factor $k$, and subsequently scaled the parameter learning rate ($\alpha$) by $\frac{1}{k}$ to compensate, this results in the following modified inference and learning equations (previously Equations [eq:bpc\_dynamics] and [eq:bpc\_theta\_updates]), again assuming a Gaussian output log likelihood (squared Euclidean output loss) \Sigma^{-1}_{\ell}(x_{\ell, t} - f_{\ell-1}(x_{\ell-1,t})) \\ - \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, t}}^T

<!-- chunk {"id": "body-0059", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

x_{\ell}}\right|_{x_{\ell, t}}^T (k \cdot \Sigma^{-1}_{\ell+1})(x_{\ell+1} - f(x_{\ell, t})) & \text{for } \ell=1,...,L-2 \\\\ - \left.\frac{\partial f_{L-1}}{\partial x_{L-1}}\right|_{x_{L-1, t}}^T (1 \cdot \Sigma^{-1}_{L})(x_{L} - f(x_{L-1, t})) & \text{for } \ell=L-1 where, for inference, $\frac{1}{k}$ factor has been absorbed by a new step size $\gamma'$ and, thus, given Euler integration does not diverge, will result in the same converged errors at the end of inference.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

\theta_{\ell}}^T (\frac{1}{k} \cdot \Sigma^{-1}_{\ell+1})(x_{\ell+1} - f(x_{\ell, t})) & \text{for } \ell=1,...,L-2 \\\frac{\partial f_{\ell}}{\partial \theta_{\ell}}^T & \text{for } \ell=L-1 Therefore, the modification in Case 2 corresponds to downscaling the variances of the intermediate latent states towards 0 while keeping the output likelihood variance fixed.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Backpropagation as PC in the infinite variance limit", "weight": 1.0} -->

Obtaining exact equivalence to the equivalent backpropagation-based learning update for this non-latent graph would require taking k to infinity, or more practically for getting approximate equivalence, some reasonably large value; [whittington\_approximation\_2017]uses k=100 for a small network. But this scaling clearly runs the risk of being numerically unstable and is also biologically unrealistic.

<!-- chunk {"id": "body-0062", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

An alternative to the scaling procedure mentioned above, dubbed the "fixed-prediction assumption" (FPA) was presented in [millidge\_predictive\_2020], wherein the top-down predictions $f(x_\ell)$ and Jacobians $\left(\frac{\partial f_\ell}{\partial x_\ell}\right)$ corresponding to each latents were fixed to their feed-forward predictions $\mu_{\ell+1}$ and $\left(\frac{\partial f_\ell}{\partial x_\ell}|_{\mu_{\ell}}\right)$respectively, throughout the inference procedure.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

The FPA modification of PC fixes the following terms in the discretised gradient flow to specific values corresponding to their feed-forward initialisation. That is to say \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, t}} &= \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{x_{\ell, 0}} &&= \left.\frac{\partial f_{\ell}}{\partial x_{\ell}}\right|_{\mu_{\ell}} where we have assumed Requirement 1, i.e. that the latent states are initialised at the feed-forward values of the corresponding computational chain.

<!-- chunk {"id": "body-0064", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

We refer to the inference updating equation corresponding to these FPA modifications as $u(x_{\ell, t}, x_{\ell+1, t})$, for a particular latent $x_{\ell}$, to show that it is dependant on the instantaneous value of only the $x_{\ell, t}$ and it's child variable $x_{\ell+1, t}$, and not the parent latent states $x_{\ell-1}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

This decoupling of the dynamics of each latent state from the values of its parents means that the trajectory of the latent states is no longer guaranteed to follow the gradient of the log-joint (or the free-energy as defined for standard PC (Equation [eq:elbo\_pc])), and therefore these dynamics are also not guaranteed to find the MAP estimate of the latent states for the model defined in standard VPC, x_{\ell, t+1} = x_{\ell, t} - \gamma \, u(x_{\ell, t}, x_{\ell+1, t}) u(x_{\ell}, x_{\ell+1}) = \left.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

(x_\ell - \mu_\ell) - \frac{\partial f_{\ell}}{\partial x_{\ell}}^T (x_{\ell+1} - \mu_{\ell+1}) & \text{for } \ell=1,...,L-2 \\(x_{L-1} - \mu_{L-1}) - \left.\frac{\partial f_{L-1}}{\partial x_{L-1}}\right|_{\mu_{L-1}}^T \frac{\partial f_L}{\partial \mu_{L}}^T & \text{for } \ell=L-1 [millidge\_predictive\_2020] that the aforementioned fixed-prediction modifications (Equations [eq:fpa\_fixing\_first] and [eq:fpa\_fixing\_last]) were equivalent to the infinite variance limit of Case 2 from

<!-- chunk {"id": "body-0067", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

This is due to the fact that in the limit of infinite output variance, the predictions of the latent states change very little from their feed-forward initialisations by the end of inference. We argue however that this equivalence does not hold due to the fact that in the infinite or high-variance limit of Case 2 the latent states $x_\ell$ also remain fixed, or arbitrarily close, to their feed-forward values, and not just the predictions $f_\ell(x_\ell)$. This behaviour is necessary for the inference to accurately correspond to inference over the latent intermediate states $x_\ell$. Which, in the limit of the zero-variance (deterministic) intermediate latent states assumed by the equivalent backpropagation model, become equal to the feed-forward values $\mu_\ell$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

This is not the case for the FPA modification of PC, where the latent states are unconstrained and the prediction error is necessarily not zero except in the trivial case of a zero magnitude weight update.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The Fixed-Prediction Assumption", "weight": 1.0} -->

This suggests that FPA-PC inference corresponds neither to the probabilistic graphical model assumed by standard VPC, nor that of the scaled variance (i.e. deterministic latent states) modification from Case 2above. This leaves us with the question of how one can interpret FPA-PC inference if not in terms of inference over a probabilistic graphical model as with standard VPC. One particularly simple and elegant answer to this is that one can interpret the FPA-PC modified inference equations as directly implementing the recursive backpropagation equations via the steady state of a set of ordinary differential equations. FPA-PC inference can then be interpreted as enacting an Euler integration scheme until one reaches this steady state. We derive this perspective in the following section.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Deriving FPA-PC as a steady-state implementation of backpropagation", "weight": 1.0} -->

We can make the relationship between FPA-PC and backpropagation even more clear by showing that the FPA-PC equations can be interpreted as a direct implementation of backpropagation via differential equations. To illustrate this, we work our way backwards from backpropagation, showing how a direct implementation of its recursion relationship results in the FPA-PC inference equations.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Deriving FPA-PC as a steady-state implementation of backpropagation", "weight": 1.0} -->

The key quantities which backpropagation requires computing are the errors $e_i$ via the recursive expressions (Equations[eq:recursive\_backprop\_equations]). We can trivially convert these expressions such that they correspond to the steady state of a set of simple differential equations \dot{e}_\ell = \left. e_{\ell} - \frac{\partial \mu_{\ell+1}}{\partial \mu_{\ell}}^T e_{\ell+1} & \text{for } \ell=1,\dots,L-1 \\e_{\ell} - \frac{\partial f_L}{\partial \mu_L}^T & \text{for } \ell=L such that when $\dot{e}_\ell = 0$, we obtain the required recursive relationships (Equation [eq:recursive\_backprop\_equations]).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Deriving FPA-PC as a steady-state implementation of backpropagation", "weight": 1.0} -->

Note that $\frac{\partial \mu_{\ell+1}}{\partial \mu_{\ell}}$ and $\frac{\partial E}{\partial\mathbf{\mu_L}}$ are fixed Jacobians and require being evaluated at the feed-forward values $\mu_\ell$. Also note, the outer negative sign has been added to make the relationship with FPA-PC more clear, and this does not impact the value of $e_\ell$at the steady state.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Deriving FPA-PC as a steady-state implementation of backpropagation", "weight": 1.0} -->

We can then rewrite $e_\ell$ in terms of some variable $x_\ell$ minus the constant feed-forward values $\mu_\ell$ so that we have: $e_{\ell} = x_\ell - \mu_\ell$, allowing us to write the above dynamic equations in terms of a variable $x_\ell$ as \dot{x}_\ell = \left.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Deriving FPA-PC as a steady-state implementation of backpropagation", "weight": 1.0} -->

The practical consequences of this modified version of PC were first questioned in [rosenbaum\_relationship\_2022], who showed that in case of step size equal to 1, FPA-PC is not just functionally but algorithmically equivalent to backpropagation, suggesting at least in the specific case of inference step size equal to 1, there may be no benefit of FPA-PC over backpropagation. We extend this work and investigate the properties of [millidge\_predictive\_2020], as well as other recent modifications [song\_can\_2020, salvatori\_predictive\_2021]further, showing that these modifications have provable worse computational and time complexity for any step size.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

To investigate the computational and time complexity of the FPA-PC and other modified PC algorithms we begin by proving that under the aforementioned dynamics, the number of inference steps taken for an error to propagate from an output node in a computational chain to an intermediate node is lower-bounded by its distance to the output node. See Theorem [theorem:1] and Corollary [corollary:1]. lemma[theorem]Lemma For a particular node ($x_\ell$) in a computational chain that has non-zero gradient w.r.t an output loss $\mathcal{L}$, initialised to feed-forward values of the network, evolving under standard PC or FPA-PC dynamics, the error for that node ($e_\ell$) will first become non-zero at time $t = L - \ell$. Where L is the length of the chain, and $\ell$ is the index of that node within the chain.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Let the variational modes $x$ be initialised to feed-forward values of the network, (i.e. Requirement 1). That is, let $x_\ell = \mu_\ell$ for $\ell \in [1,...,L-1]$. [eq:fpa\_pc\_update\_equations\_1] and [eq:fpa\_pc\_update\_equations\_2] describe the dynamics of our latent states under FPA-PC dynamics, and Equations [eq:bpc\_dynamics] and [eq:bpc\_dynamics\_2]describe the dynamics under standard PC.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

- Because we are ignoring the trivial case of a zero gradient with respect to the output loss, we are guaranteed that the Jacobians $\frac{\partial f_\ell}{\partial x_\ell}$ are all non-zero as $\frac{\partial \mathcal{L}}{\partial x_{\ell}} = \frac{\partial f_\ell}{\partial x_\ell}...\frac{\partial f_{L-1}}{\partial x_{L-1}}\frac{\partial \mathcal{L}}{\partial f_{\ell-1}} \ne 0$. - At time $t=0$, the dynamics $u(x_{\ell}, x_{\ell+1})$ of all nodes are $0$, except for $x_{L-1}$, by the definition of the update equations and Requirement 1.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

- At time $t=1$, the nodes $x_{L-1}$ therefore update proportionally to $u(x_L)$ - At any particular time step $t=t+1$, if the dynamics $u(x_{\ell}, x_{\ell+1})$ associated with a node $x_\ell$ were $0$ in time step $t$, then they will become non-zero at $t+1$, if and only if, a change has occurred in $x_{\ell+1}$ from time step $t$ to $t+1$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

(By the definition of the FPA-PC ([eq:fpa\_pc\_update\_equations\_1] and [eq:fpa\_pc\_update\_equations\_2]) or standard PC ([eq:bpc\_dynamics] and [eq:bpc\_dynamics\_2]) update equations, and statement 1) - Thus, via induction, the first non-zero change to occur for an arbitrary variational mode $x_\ell$ at point $\ell$ in the computational chain will occur at a time $t = L - \ell$, i.e. its distance from the output with regards to the number of intermediary nodes.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

The convergence time for errors associated with an arbitrary node in a computational chain is lower-bounded by its distance, in nodes, to the output node.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

- The fixed convergence point for the dynamical equations of FPA-PC is guaranteed to converge to an error equal to the gradient with regards to the output loss. - For a node, with non-zero gradient with regards to an output loss, to converge, the converged error for that node must therefore be non-zero. - Under theorem 1, the time taken for the error to first become non-zero is equal to its distance to the output node $x_L$, which is $t = L - \ell$ for a computational chain of length $L$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

In words, this proof describes how, despite the ostensibly parallel computation occurring in FPA-PC, convergence nonetheless requires sufficient time steps for error information to propagate from the output node backward. This is necessary as information is still nonetheless only transmitted via adjacent nodes, as with backpropagation. Thus, inference must proceed for a minimum number of inference steps equal to this distance before convergence can occur.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

We can now ask what the time complexity of a single inference step is under FPA-PC dynamics, and thus the time complexity of inference overall for FPA-PC, as well as how this compares to backpropagation. Note that, for this comparison, we exclude the final VJP calculation for gradients associated with a particular $\theta$, for both FPA-PC and backpropagation, as this has the same computational cost for both algorithms and only occurs once, at the end of inference and error propagation respectively.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

When considering the time complexity of FPA-PC inference we will assume the error computations ($e_{\ell} = x_{\ell} - \mu_{\ell}$) contribute negligible latency to the computation at every inference step. This is a generally reasonable assumption for the intermediate errors, given that these errors can be computed entirely in parallel and thus have the latency of a single subtraction operation - which is also generally amongst the lowest latency arithmetic instructions available on modern hardware (See [wong\_demystifying\_2010, fog\_instruction\_2011]).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

\text{TIME} \{\text{\textit{FPA-PC}}(F)\} &= \text{TIME} \{\text{\textit{forward}}(F)\} + \text{TIME} \{\text{\textit{FPA-Inf}} (F) \} We assume each inference step is maximally parallel, such that VJP computations across all nodes occur simultaneously.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

However, since each inference step must wait for the slowest (VJP) computation to complete, we can take the minimum time complexity for each inference step to be equal to that of the slowest VJP computation: (Note, a similar result also follows if we assume the VJP computation for each function $f_i$ takes roughly the same amount of time) \text{TIME} \{\text{\textit{FPA-PC}}(F)\} &= \sum_{i=0}^{L} \text{TIME} \{\text{\textit{forward}}(f_i) \} + \sum_{t=0}^{t_c} \text{TIME} \{\text{\textit{vjp}}(f_{\text{slow}}) \} \\&\ge \sum_{i=0}^{L} \text{TIME} \{\text{\textit{forward}}(f_i) \} + \sum_{t=0}^{L} \text{TIME}

<!-- chunk {"id": "body-0087", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Thus, the time complexity for FPA-PC inference is provably greater than, or equal to, that of backpropagation for an equivalent computational chain.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

- We have assumed error computation ($e_{\ell} = x_{\ell} - \mu_{\ell}$) contributes negligible latency to each inference step. - Convergence will generally not occur within exactly $t_c = L$ steps except in particular circumstances (e.g. inference step size equal to 1), and so in practice, FPA-PC may have a significantly higher time complexity (scaling with inference length) than backpropagation. - Bottlenecks (slow VJP computations) will impact FPA inference significantly more as each inference step will be as slow as the slowest VJP computation (incurring a $t_c \cdot w \cdot C_{\text{max}}$ latency cost), while a single slow VJP computation would only incur a single $C_{\text{max}}$ latency cost for backpropagation.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Note that this is a separate and distinct proof to the result by [rosenbaum\_relationship\_2022], which showed that for a specific step size of 1, FPA-PC computes gradients in $t = L - \ell$ steps (i.e. in an equivalent number of steps to backpropagation). It was not clear however whether FPA-PC could converge in fewer time steps for arbitrary step sizes and whether FPA-PC inference had worse time complexity (or slower runtime), which was dependent on the time complexity of each inference step. Here we show that the FPA-PC convergence can provably never be faster than standard backpropagation for anystep size.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

We test these results by enacting FPA-PC inference on multi-layer perceptron networks of various sizes, while varying the number of inference steps relative to the size of the network. We then compute the cosine similarity of gradient updates relative to those obtained via backpropagation. We find, as expected, that cosine similarity drops rapidly as the number of inference steps falls below the number of layers in the network, demonstrating a failure to converge (Figure [fig:bp\_cosine\_similarity]). Inference learning rates lower than 1 show a failure to converge even for a number of inference steps higher than the number of layers in the network. We also report validation and test set accuracies, which experience significant drops as this occurs also (Figures [fig:fpa\_pc\_val\_accuracy] and [fig:fpa\_pc\_test\_accuracy]).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Cosine similarity between FPA-PC learning updates and backpropagation on MNIST, tested for a varying number of inference steps, relative to the size of the network.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Validation set accuracy on MNIST with FPA-PC for a varying number of inference steps, relative to the number of layers in the network.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Computational and Time Complexity", "weight": 1.0} -->

Final test set accuracy on MNIST with FPA-PC for a varying number of inference steps, relative to the number of layers in the network.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

Subsequent to the FPA-modified formulation of PC, further modified formulations of PC were presented in [song\_can\_2020, salvatori\_predictive\_2021]. The resultant algorithm, termed Zero Divergence Inference Learning(Z-IL), achieved a similar effect to FPA-PC without explicitly fixing the feed-forward values and Jacobians and did so by requiring a very specific set of changes.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

- Requirement 1: (As before): The variational modes or latent states ($x_1,..., x_{L-1}$) are initialised to the feed-forward values of the corresponding backpropagation-based computational chain ($\mu_1,..., \mu_{L-1}$) - Requirement 2: The inference learning rate $\gamma$ is set to 1 - Requirement 3: A particular layer is updated specifically and exclusively at a particular inference time-step ($t = L-\ell$) corresponding to its distance from the output node in the computational chain.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

Ablation of any one of these three requirements was shown to result in losing equivalence between Z-IL and backpropagation Note that, for the purposes of this proof, we will ignore FA-Z-IL (Fully Autonomous Z-IL), which builds upon Z-IL, as its primary purpose was to remove the neurobiologically implausible requirement that the weight update is triggered manually at a particular inference step, and thus does not impact the results in this section.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

This algorithm relies on the fact that at a particular time-step, the node corresponding to a particular layer $x_\ell$ is experiencing an update that is equivalent to that obtained under FPA-PC dynamics. This occurs because the current value of any particular node ($x_\ell$) does not deviate from the feed-forward values they were initialised with until after a particular (i.e. $t=L-\ell$) inference step (See Lemma A.3 from Supplementary Material in [song\_can\_2020]). For the node corresponding to the weight being updated, this has the effect of mimicking the fixing of feed-forward values seen under the FPA modified form (Equations [eq:fpa\_fixing\_first]-[eq:fpa\_fixing\_last]), since both its predictions and the predictions of its parents ($\ell-1$) remain fixed to their feed-forward values.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

To see this explicitly, we describe the relevant computations occurring at each inference step for the example function $F$, in table [tab:z\_il\_v\_backprop]. We restrict ourselves at each inference step to only describing the changes that occur to $x_\ell$, $e_\ell$ and $\theta_\ell$ for every timestep $\ell$. Therefore, we will not record in the table below any computations occurring at nodes $>\ell$, as they will have no future influence on any parameter learning, as well as nodes $<\ell$, as no change is occurring for that inference step. For notational simplicity we drop time indices, rather, values on the right-hand-side of the equations in Table [tab:z\_il\_v\_backprop]refer to those from the previous time step.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\underbrace{x\_1}\_{=\mu\_{1}} + \frac{\partial f\_{1}}{\partial \mu\_{1}}^T e\_{2} \\e\_{1} = \frac{\partial f\_{1}}{\partial \mu\_{1}}^T e\_{2} \label{tab:z\_il\_v\_backprop} We can see here that in each time step, for the computations relevant to parameter gradient updates, Z-IL engages in precisely the same computations as backpropagation (a VJP evaluated at the feed-forward values and the subsequent error), these are then added to a constant (the feed-forward activations $_$), before this constant is then subtracted.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

In addition to these computations, we note that Z-IL (and its variant FA-Z-IL by extension), engages in wasted computation for nodes $x_i, i > $, which we do not depict in the walk-through of the computations above. These computations occur despite not resulting, or contributing to, any parameter updates, and are thus unnecessary.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

Since the dynamics for Z-IL are a special case of the dynamics of standard PC, we may once again use Theorem theorem:1, Corollary corollary:1 and identical reasoning to that in section sec:fpa\_pc, to once again obtain complexity bounds for Z-IL. Which we find are similarly lower-bounded by that of backpropagation.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\label{eq:zil\_time\_complexity\_last} \subsection{Generalised-IL (G-IL), Learning Rate Stability and Online Learning} For completeness, we note that some recent work has suggested that Predictive Coding (PC) and related energy-based models, which do not yield backpropagation-equivalent updates, may nonetheless exhibit greater robustness to high learning rates and show less degraded performance in the online learning (batch size 1) settings.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

More specifically, demonstrates that a variant of PC with additional regularisation terms, called Generalised-IL (G-IL), may approximate implicit SGD, with the approximation becoming exact under certain limits. The authors of this work further present a modified algorithm (IL-prox), which guarantees equal updates to \textit{implicit} SGD. The resultant schemes demonstrated greater robustness to the learning rate and less degraded performance in online learning regimes. These properties are also demonstrated empirically, for energy-based models (EBMs) in general, as a consequence of a principle dubbed "prospective configuration".

<!-- chunk {"id": "body-0104", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

These findings are intriguing, as robustness to learning rates aligns with expectations for a backward Euler integration scheme -- the implicit counterpart to the forward Euler integration scheme from which SGD originates -- and an optimization approach that is demonstrably less prone to divergence in non-stochastic contexts.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

It is unclear, however, whether the differences in learning rate stability would remain when testing against optimizers such as Adam, or SGD with momentum, both of which are well-understood in theory, and practice, to ameliorate the risk of divergence under high learning rates, by improving the conditioning of the loss landscape or dampening oscillations. Moreover, there is evidence to suggest that small-batch SGD itself has a greater robustness to learning rate, possibly due to the additional stochasticity in the small-batch setting preventing the accumulation of Euler integration errors. As such, the authors posit that it would be a compelling avenue for future research to explore whether the performance gap in online learning settings persists when online SGD is combined with high learning rates.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

While these findings do not impact our presented results or the use of PC as a direct substitute for backpropagation, they raise thought-provoking questions on whether modified and unmodified PC forms may nonetheless possess attributes desirable for neuromorphic learning, even if they do not necessarily exhibit parameter updates identical to those under backpropagation.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\section{Conclusion and Key Results} In this paper, we have investigated the computational efficiency, learning dynamics, and neurobiological plausibility of various PC variants in comparison to the backpropagation algorithm. We now summarise the key results and points made: \item[Result 1] The infinite-variance limit modification from (see Case 2 above), is equivalent to assuming a model with strictly deterministic (non-probabilistic) latent states.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\item[Result 2] Modified variants of PC: FPA-PC, and Z-IL, do not follow a free energy gradient. Corollary: learning does not correspond to learning of a latent probabilistic model via variational Bayes.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\item[Result 3] Modified variants of PC: FPA-PC, and Z-IL, are guaranteed to have worse time complexity than backpropagation, even when accounting for fully parallel computation within each inference step. (See Theorem theorem:1, corresponding Corollary corollary:1 and Equations eq:fpa\_time\_complexity\_first-eq:zil\_time\_complexity\_last) \item[Point 1] Equivalence, or approximate equivalence, of PC with backpropagation mandates adopting an inverted scheme, unlike traditional formulations of generative PC, which has non-trivial implications for neurobiological plausibility.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

\item[Point 2] A naive implementation of standard PC does not suffer from the weight \textit{transport} problem in the same sense as that which is present in naive neurobiological proposals of backpropagation. It does, however, suffer from an analogous but potentially less implausible, weight \textit{symmetry} issue.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

These results raise doubt with respect to the advantages that recent variants of PC may provide with regards to backpropagation and its neuromorphic implementation, given that PC variants which result in equivalent or close to equivalent gradient updates also engage in precisely the same computations as backpropagation, and do so in much the same, equally local/non-local, way. This is despite the ostensibly parallelised computation of PC networks, which from the perspective of backpropagating errors merely results in additional, or unused, computation, and not faster error propagation.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

Furthermore, by introducing modifications to obtain, or approximate, equivalence, PC variants lose the generative variational Bayes interpretation of standard formulations of PC, and its various strengths, such as maintaining uncertainty over latent hidden states or causes, or parity with our current understanding of the organisational and functional properties of pathways within the cortex.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Zero Divergence Inference Learning (Z-IL)", "weight": 1.0} -->

The authors would like to thank Prof. Christopher L. Buckley and his group for their valuable comments and feedback on this manuscript.
