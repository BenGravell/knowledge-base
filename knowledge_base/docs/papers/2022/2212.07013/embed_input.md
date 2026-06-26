<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning and Predicting Multimodal Vehicle Action Distributions in a Unified Probabilistic Model without Labels

Topics include Vehicles, Self-supervised learning, Probabilistic models, Clustering, Learning, Variational inference.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a unified probabilistic model that learns a representative set of discrete vehicle actions and predicts the probability of each action given a particular scenario. Our model also enables us to estimate the distribution over continuous trajectories conditioned on a scenario, representing what each discrete action would look like if executed in that scenario. While our primary objective is to learn representative action sets, these capabilities combine to produce accurate multimodal trajectory predictions as a byproduct. Although our learned action representations closely resemble semantically meaningful categories (e.g., "go straight", "turn left", etc.), our method is entirely self-supervised and does not utilize any manually generated labels or categories. Our method builds upon recent advances in variational inference and deep unsupervised clustering, resulting in full distribution estimates based on deterministic model evaluations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central challenge in robotics and artificial intelligence is to develop discrete representations that can translate the high-dimensional continuous spaces of real-world sensor data and robot configuration into forms that are compatible with algorithms for abstract reasoning, such as search and logical or probabilistic inference. Although representation learning has been studied extensively in the machine learning literature, and learned action representations are often used in robotics, it remains an open challenge to distill unlabeled natural data into a representative set of discrete actions. In particular, learned discrete action representations have not been widely adopted in the recent autonomous vehicle literature, possibly because many essential components of an autonomous vehicle system can be engineered or learned to a considerable degree without them. For example, predicted trajectories for other vehicles on the road can be fed directly into a planning system to avoid collision, without those predicted trajectories representing distinct maneuvers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, there are important cases in an autonomous vehicle system in which it would be useful to describe behavior in terms of a representative discrete action set. For example, communicating intent or receiving instruction from a user would require a relatively small set of meaningfully distinct action choices, perhaps with semantic labels attached. Similarly, right-of-way conventions and rules of the road are understood in terms of discrete actions, necessitating a way to classify continuous-valued trajectories as members of an action set in order to evaluate their legality.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, we observe that there is enormous variability in the behaviors of drivers in real-world scenarios. There is also great diversity in the design of roads, intersections, parking lots, sidewalks and other environments where we must understand and predict movements of other agents. There is a substantial challenge in developing a representative discrete action set under these highly variable conditions. For example, if a vehicle is following a road that curves gently to the left, does that constitute a "go straight" or "turn left" maneuver? We adopt the position that manually defining maneuvers and classifiers beyond the few simplest categories will quickly become untenable and therefore the categories themselves should arise automatically from the data without manually generated labels.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal in this paper is primarily to learn a representative discrete set of actions that can be used to describe and predict intent, and secondarily to forecast continuous-valued trajectories using that set. We aim to provide a means of answering queries such as "What is the probability of taking action $i$ in this scenario?", as well as: "What would the distribution of action $i$ look like if executed in this scenario?" An additional goal is to estimate full distributional information, since uncertainty information is essential to safe and effective autonomous vehicle operation. To achieve these objectives, we develop a unified probabilistic model based on methods that combine variational inference and unsupervised clustering. Our model assumes that trajectories are explained by both discrete and continuous underlying latent variables, and that those underlying factors are determined by (or can be inferred from) an input scenario. We begin by motivating our work with respect to relevant literature, and then we develop our model and illustrate its effectiveness in both learning and predicting vehicle motions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Learning and Predicting Multi-Modal Action Distributions", "weight": 1.0} -->

Our primary objective is to jointly learn a set of representative actions and a model that predicts the discrete probability of each action in a given scenario. We consider an action to be not a single fixed trajectory, but a continuous distribution of similar trajectories that might serve the same functional purpose across a range of different scenarios and map geometries. Therefore, we have both discrete and continuous elements of variation that we wish to model, however we assume no prior knowledge of manually-defined behavior categories or action shapes and we aim for both the discrete action categories and the associated continuous-valued distributions over trajectories to arise naturally from the data. First, we will develop a model that learns a representative set of actions in a self-supervised manner, and then we will extend that model to make accurate motion predictions conditioned on a given scenario.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

We assume a dataset of trajectory-scenario pairs ${(X,S)} = {({(x_{1},s_{1})},\ldots,{(x_{N},s_{N})})}$, where $x_{i}$ is a vector of future vehicle position coordinates for the target vehicle of interest in data sample $i$, and $s_{i}$ is a scenario (or context) represented as a multi-channel rasterization of the map and past states of the target vehicle and other agents in the scenario. To capture both discrete and continuous elements of variation in driving behaviors, we propose a latent variable model using both discrete and continuous latent variables. We model the system according to the graphical model illustrated in Figure 1. In this model, $x$ and $s$ represent the trajectory and scenario, respectively, $y \in {1,\ldots,K}$ is a discrete latent variable and $z \in {\mathbb{R}}^{D}$ is a continuous latent variable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

The latent variables $y$ and $z$ together constitute a Gaussian mixture model (GMM) where the value of $y$ selects a particular component of the GMM and each component is represented with a mean and covariance. Our goal is to maximize $\text{ln~}p{(\left. X \middle| S \right.)}$ over the parameters of this model, thereby learning a set of GMM components that decode via $p{(\left. x \middle| z \right.)}$ to continuous action distributions, as well as a predictor $p{(\left. y \middle| s \right.)}$ of discrete action probabilities given a scenario.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

Since direct optimization of this model is difficult, we adopt the method of variational inference and specify a variational model $q{(y,\left. z \middle| {x,s} \right.)}$ to approximate the distribution over latent variables. We assume that the generative and variational models factorize as follows: In Figure 1, the generative model is illustrated with solid arrows while the variational model is illustrated with dashed arrows. This factorization gives rise to a relationship between $z$ and $x$ that closely resembles a conventional variational autoencoder, where $q{(\left. z \middle| x \right.)}$ acts as an encoder into a continuous-valued latent space and $p{(\left. x \middle| z \right.)}$ acts as a decoder. However, unlike a conventional VAE, our latent space prior comprises $K$ Gaussians whose parameters are optimized to capture the modes of the encoded data. Learning in this model simultaneously shapes the latent space $z$ and clusters data in that space.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

These clusters, when decoded to the trajectory space $x$ define our learned action set.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

Following a common decomposition in variational inference, the log likelihood for a single element of our dataset can be written as: Since $D_{KL}{(q||p)}$ is always non-negative, we can use $\mathcal{L}{(q)}$ as a lower bound on the data likelihood, known as the evidence lower bound (ELBO). Optimizing this bound $\mathcal{L}{(q)}$ equivalently maximizes data likelihood and minimizes $D_{KL}{(q||p)}$. Substituting our factorization of $p{(x,y,\left. z \middle| s \right.)}$ and $q{(y,\left. z \middle| {x,s} \right.)}$ into equation gives: | | $\mathcal{L}$ | $= {\sum\limits_{y}{\int_{z}{q{(\left. y \middle| {x,s} \right.)}q{(\left.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

z \middle| y \right.)}$ as a linear function mapping a one-of-$K$ representation of $y$ to mean and variance of clusters in latent space $z$. While $p{(\left. x \middle| z \right.)}$ and $q{(\left. z \middle| x \right.)}$ are fully connected networks, $p{(\left. y \middle| s \right.)}$ includes a convolutional stage that extracts features from the rasterized scene input. As in many VAE implementations, the encoder $q{(\left. z \middle| x \right.)}$ learns both means and variances of $z$, while the decoder $p{(\left. x \middle| z \right.)}$ learns only means of $x$ and the output distribution is defined as a Gaussian with identity covariance (though that variance could also be learned). Note that the variance of $z$, not $x$, is what induces the distributional spread of trajectories within an action.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

We do not represent $q{(\left. y \middle| {x,s} \right.)}$ as a neural network, since this distribution can be directly computed using the other distributions. This particular model and factorization follow a mean field approximation since the variational approximation for neither $y$ nor $z$ depends on the other, therefore we follow a general result to obtain (see Appendix A ‣ Learning and Predicting Multimodal Vehicle Action Distributions in a Unified Probabilistic Model Without Labels")): where $H{({q{(\left. z \middle| x \right.)}},{p{(\left. z \middle| y \right.)}})}$ is the cross entropy between $q{(\left. z \middle| x \right.)}$ and $p{(\left. z \middle| y \right.)}$, which can be computed analytically since both distributions are Gaussian. This expression provides the intuitive result that probabilistic assignment of clusters is determined by proximity between the encoding given by $q{(\left.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

z \middle| x \right.)}$ and the cluster location given by $p{(\left. z \middle| y \right.)}$. Computing $q{(\left. y \middle| {x,s} \right.)}$ in this way is analogous to computing the E-step in the expectation maximization algorithm.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Learning a Set of Actions", "weight": 1.0} -->

For the purposes of optimizing equation LABEL:elbo with stochastic gradient descent, we can approximate the integral in the first term with a Monte Carlo estimate using a single sample, leading to the objective function: where $\overset{\sim}{z}$ is a sample drawn from $q{(\left. z \middle| x \right.)}$. At each training step, we compute $q{(\left. y \middle| {x,s} \right.)}$ using equation with the current model parameter values and hold that distribution fixed while we optimize the other distributions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

In Section III-A, we developed a model to learn a set of representative action distributions and predict the discrete probability $p{(\left. y \middle| s \right.)}$ of each action being selected given a particular scenario. However, since these action distributions are not yet conditioned on that scenario, they are not directly applicable for making accurate motion predictions. Figures 6(a) and 6(c) show imprecise predictions made by first evaluating $p{(\left. y \middle| s \right.)}$ to determine likely values of $y$, and then for each corresponding GMM component, decoding values of $z$ equal to the component mean $\pm {1\sigma}$ to obtain a distributional spread of trajectories. Although the discrete action choices in these examples may be reasonable, the trajectory predictions are not tailored to the specific scenarios.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

More concretely, in the model we developed in III-A (Figure 1), the distribution over the continuous latent variable $z$ does not depend on scenario $s$ except through the choice of $y$. In reality, the value of $z$ should depend *strongly* on $s$ because it is the geometric structure of the road and surrounding agents in the scenario that determine which actions are both feasible and likely. For instance, small variations in the value of $z$ within a given action distribution make the difference between a turn into the correct lane and a turn into oncoming traffic. Therefore, why not introduce a dependency on $s$ in the prediction of the continuous latent variable, e.g., $p{(\left. z \middle| {y,s} \right.)}$ or the decoder, e.g., $p{(\left. x \middle| {z,s} \right.)}$?

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

Since the scenario $s$ contains sufficient information in many cases to accurately predict the continuous-valued latent variable $z$ or the output trajectory $x$ directly without the use of a discrete action choice, introducing $s$ as a dependency in these distributions undermines and even prevents the model from effectively learning a multimodal action representation. Though we do not quantify this behavior here, we observe that a model whose latent variable prediction has access to the scenario (e.g., $p{(\left. z \middle| {y,s} \right.)}$) will simply bypass the discrete variable altogether, resulting in a very small number of non-degenerate clusters and one dominant cluster whose distribution spans the full continuum of actions. Similarly, in a model whose decoder has access to the scenario (e.g., $p{(\left. x \middle| {z,s} \right.)}$), the geometric shape and semantic role of each discrete action become so shifted depending on the scenario as to lose any consistent identifiable meaning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

We find that in order to achieve effective clustering of data into representative action distributions for our purposes, and to learn non-degenerate predictions of $y$ based on $s$, the learned structure of the latent space must not shift with $s$ and we must have the discrete variable $y$ as the sole conduit or bottleneck of scenario information in the generative model.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

Nevertheless, we must somehow still refine our prediction of the continuous latent variable $z$ in order to make accurate trajectory predictions. What we are truly interested in is the posterior $p{(\left. z \middle| {y,s} \right.)}$ that can be decoded to generate the distribution of trajectories for a specific discrete action choice and scenario. Fortunately the methods of variational inference are well suited to estimating posteriors over latent variables, and our approach will be to approximate the true posterior $p{(\left. z \middle| {y,s} \right.)}$ with a variational model $q{(\left. z \middle| {y,s} \right.)}$, effectively serving as a separate encoder.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Accurate Predictions with Learned Action Distributions", "weight": 1.0} -->

We could attempt to modify the model illustrated in Figure 1 by replacing the existing encoder $q{(\left. z \middle| x \right.)}$ with a different encoder $q{(\left. z \middle| {y,s} \right.)}$, however as we have noted above, such a model would simply bypass the use of the discrete variable $y$ and simply predict $z$ directly based on $s$. Therefore, we must maintain the structure illustrated in Figure 1, but we explore two options that build upon that structure. The first option is to train an alternate encoder for our original model, and the section option is to extend our original model to create a larger unified model that includes two different encoders, jointly training all of the desired distributions. We discuss these two possibilities in turn.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Learning a Dual Encoder", "weight": 1.0} -->

First, we consider learning and fixing in place the distributions in our original model, then training a separate encoder $q{(\left. z \middle| {y,s} \right.)}$ using a variant of our original objective (LABEL:elbo): | | $\mathcal{L}$ | $= {\sum\limits_{y}{\int_{z}{q{(\left. y \middle| {x,s} \right.)}q{(\left. z \middle| {y,s} \right.)}\text{ln}\left\{ \frac{p{(\left. y \middle| s \right.)}p{(\left. z \middle| y \right.)}p{(\left. x \middle| z \right.)}}{q{(\left. y \middle| {x,s} \right.)}q{(\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Learning a Dual Encoder", "weight": 1.0} -->

z \middle| x \right.)}$) separately for each value of $y$, and where we have dropped the final term from equation since we assume that $q{(\left. y \middle| {x,s} \right.)}$ and $p{(\left. y \middle| s \right.)}$ are both known and fixed. Indeed, the objective is to train $q{(\left. z \middle| {y,s} \right.)}$ only, and we assume that all other terms in this function have already been learned and fixed. We illustrate this alternative encoder in Figure 4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Learning a Dual Encoder", "weight": 1.0} -->

We consider this to be a VAE-like objective function because it contains the two terms typically found in a conventional VAE objective function: Reconstruction of the input based on a sample drawn from the variational posterior $q{(\left. z \middle| {y,s} \right.)}$, and the KL divergence between the variational posterior and the prior. We rely on the discrete distribution $q{(\left. y \middle| {x,s} \right.)}$ to correctly attribute each data sample to the appropriate discrete action, which enables $q{(\left. z \middle| {y,s} \right.)}$ to learn to predict different maneuvers (e.g., "go straight" vs. "turn left") from the same scenario $s$. We implement $q{(\left. z \middle| {y,s} \right.)}$ as a collection of $K$ neural networks, ${q_{1}{(\left. z \middle| s \right.)}},\ldots,{q_{K}{(\left.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Learning a Dual Encoder", "weight": 1.0} -->

Although this method is functional, one particular drawback of learning $q{(\left. z \middle| {y,s} \right.)}$ apart from the rest of the model is that the CNN stage that extracts scene features to predict $p{(\left. y \middle| s \right.)}$ may not learn features that are optimally tuned to predicting $q{(\left. z \middle| {y,s} \right.)}$. Therefore, it may be necessary to train a separate convolutional stage specifically for $q{(\left. z \middle| {y,s} \right.)}$ or interleave both training phases. In the next section, we introduce a single unified model that overcomes this problem by jointly learning all distributions simultaneously.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Unified Model", "weight": 1.0} -->

As we discussed in Sections III-B and III-C, we wish to learn a set of representative action distributions and a discrete action predictor, which we can accomplish with a model of form illustrated in Figure 1. But we also aim to simultaneously learn a second posterior distribution $q{(\left. z \middle| {y,s} \right.)}$ that enables us to condition each continuous action distribution on a given scenario. We can accomplish these objectives simultaneously by extending our model with dual outputs, thereby enabling us to learn two different posterior distributions (encoders). We illustrate this unified model in Figure 5. This unified model contains our original model in its entirety and is augmented with a second instance of the continuous latent variable, which we denote $z'$ and a second instance of the trajectory output variable, which we denote $x'$. We define ${p{(\left. z' \middle| y \right.)}} \equiv {p{(\left. z \middle| y \right.)}}$ and ${p{(\left.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Unified Model", "weight": 1.0} -->

x' \middle| z' \right.)}} \equiv {p{(\left. x \middle| z \right.)}}$, so the same GMM components and decoder are shared between both branches of the model.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Unified Model", "weight": 1.0} -->

One important distinction between this unified model and our original model is that our latent variables no longer follow the mean field approximation due to the dependency of $q{(\left. z' \middle| {y,s} \right.)}$ on $y$. However, we can still follow the same method to derive the following expression for $q{(\left. y \middle| {x,s} \right.)}$ in our unified model (see Appendix A ‣ Learning and Predicting Multimodal Vehicle Action Distributions in a Unified Probabilistic Model Without Labels")). Again, utilizing shorthand to simplify notation, we have: This expression differs from equation only in the appearance of the $- D_{KL}{(q_{z'}||p_{z'})}$ term, which reflects that the probability of a given data point belonging to a given cluster also depends on the proximity between the encoding $q{(\left. z' \middle| {y,s} \right.)}$ and the cluster location $p{(\left. z' \middle| y \right.)}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Unified Model", "weight": 1.0} -->

Having learned the full unified model, we can make motion predictions by first evaluating $p{(\left. y \middle| s \right.)}$ to determine the likely action choices, and then evaluating $q{(\left. z \middle| {y,s} \right.)}$ for each of the likely action choices, and decoding those latent distributions through $p{(\left. x \middle| z \right.)}$ to generate trajectory distributions. Figure 6 illustrates the difference between the generic action distributions represented by GMM components $p{(\left. z \middle| y \right.)}$ and the posterior estimates of action distributions, conditioned on the scenario, given by $q{(\left. z \middle| {y,s} \right.)}$. The posterior estimate of the continuous latent variable $z$ dramatically narrows the distribution from the original GMM component to a much smaller region of latent space that is likely given the scenario, which, in turn, decodes to a much more precise distribution of trajectories shown in Figures 6(b) and 6(d).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Unified Model", "weight": 1.0} -->

We provide additional examples of the unified model in Appendix B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-E Implementation", "weight": 1.0} -->

We trained and tested our models using the Waymo open dataset. We implemented a rasterizer to generate inputs with width and height of 224 pixels, three channels of map information, and additional channels containing the past one second of target and agent states. The distribution $p{(\left. y \middle| s \right.)}$ was implemented as a CNN with a feature extraction stage, although we also observed comparable results with a much smaller CNN. The remaining neural networks were small feed-forward networks with several hidden layers consisting of 500 nodes each and ReLU activations. We defer a thorough exploration of model architectures to future work.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-E Implementation", "weight": 1.0} -->

For all results in this paper, we used $z \in {\mathbb{R}}^{5}$ and $K = 25$. Note that Figure 2 only contains 20 actions due to the fact that five of the trained actions were never assigned any significant probability in test scenarios and were omitted. We explored a number of methods for initializing the GMM components in $p{(\left. z \middle| y \right.)}$, including random and uniform placement, which function well for very low dimensional continuous latent spaces (e.g., $z \in {\mathbb{R}}^{2}$). For higher dimensional latent spaces, we found the most effective means of initializing $p{(\left. z \middle| y \right.)}$ was to pre-train $p{(\left. x \middle| z \right.)}$ and $q{(\left. z \middle| x \right.)}$ together as a standard variational autoencoder, encoding some data points into the latent space using $q{(\left.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Implementation", "weight": 1.0} -->

z \middle| x \right.)}$, and then initializing GMM components at those locations in latent space. After initialization, all components were jointly trained to convergence.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have demonstrated in this paper that a latent variable model with both discrete and continuous latent variables is an effective way to model natural driving data and cluster vehicle behaviors into discrete actions. Although there are no "correct" actions to measure our performance against in an unsupervised setting, our learned actions are qualitatively reasonable and contain a variety of turns and straight motions at different speeds. Furthermore, the structure of the model provides an elegant means of naturally predicting the discrete action probabilities in any given scenario, which is one of the primary uses of a discrete action representation. As a convenient byproduct, our model also makes accurate multi-modal motion forecasts with meaningful distributional information over the discrete action choice as well as the continuous shape of each prediction.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have proposed two methods for incorporating the scenario $s$ directly into the motion prediction in Sections III-C and III-D. One advantage of the first method is that the structure of the continuous latent space $z$ has no complex dependence on the scenario $s$, which leads to faster convergence during training, and may result in more definitive distinctions between the clusters in latent space. On the other hand, the unified model of the second method enables the sharing of CNN features between $p{(\left. y \middle| s \right.)}$ and $q{(\left. z' \middle| {y,s} \right.)}$, leading to more efficient runtime performance, and enables the quality of the continuous motion prediction to influence the discrete action set. An important line of future research will be to quantitatively compare these approaches. Although motion prediction is not our primary objective, another line of future research will be optimize and measure the performance of these approaches as motion prediction algorithms.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have shown that the number of discrete actions needed to describe natural driving can be quite small ($\approx 20$) and is compatible with human-understandable semantic meaning, in contrast with pure motion prediction methods whose sets of anchor trajectories are often much larger. It is the continuous latent variable in our model that enables us to tailor a small number of discrete actions to fit such a wide variety of continuous vehicle motions. Our model provides a simple means of estimating an effective number of actions, which is to set a conservatively high value of $K$ and retain only those actions that are ever assigned a non-negligible probability. One possible direction of future work might be to apply fully Bayesian methods to explicitly estimate the optimal number of discrete actions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, although we made no use of manually-defined action categories or labels, it may be useful to utilize a small set of labeled actions if they are available. Fortunately our models are easily adapted to use discrete action labels when available. One method is to simply replace $q{(\left. y \middle| {x,s} \right.)}$ with the known one-of-$K$ representation of $y$ for the samples whose labels are known. Using partial labels may help to guide cluster formation for specific actions that are known to exist while enabling the self-supervised process to discover the additional remaining modes present in the data.
