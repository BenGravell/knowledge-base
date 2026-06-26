<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Wasserstein GAN

Topics include Stability analysis, Optimization, Learning, Wasserstein distances, Wasserstein generative adversarial network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new algorithm named WGAN, an alternative to traditional GAN training. In this new model, we show that we can improve the stability of learning, get rid of problems like mode collapse, and provide meaningful learning curves useful for debugging and hyperparameter searches. Furthermore, we show that the corresponding optimization problem is sound, and provide extensive theoretical work highlighting the deep connections to other distances between distributions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem this paper is concerned with is that of unsupervised learning. Mainly, what does it mean to learn a probability distribution? The classical answer to this is to learn a probability density. This is often done by defining a parametric family of densities ${(P_{\theta})}_{\theta \in {\mathbb{R}}^{d}}$ and finding the one that maximized the likelihood on our data: if we have real data examples ${\{ x^{(i)}\}}_{i = 1}^{m}$, we would solve the problem If the real data distribution ${\mathbb{P}}_{r}$ admits a density and ${\mathbb{P}}_{\theta}$ is the distribution of the parametrized density $P_{\theta}$, then, asymptotically, this amounts to minimizing the Kullback-Leibler divergence $KL{({{\mathbb{P}}_{r} \parallel {\mathbb{P}}_{\theta}})}$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For this to make sense, we need the model density $P_{\theta}$ to exist. This is not the case in the rather common situation where we are dealing with distributions supported by low dimensional manifolds. It is then unlikely that the model manifold and the true distribution's support have a non-negligible intersection (see ), and this means that the KL distance is not defined (or simply infinite).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The typical remedy is to add a noise term to the model distribution. This is why virtually all generative models described in the classical machine learning literature include a noise component. In the simplest case, one assumes a Gaussian noise with relatively high bandwidth in order to cover all the examples. It is well known, for instance, that in the case of image generation models, this noise degrades the quality of the samples and makes them blurry. For example, we can see in the recent paper that the optimal standard deviation of the noise added to the model when maximizing likelihood is around 0.1 to each pixel in a generated image, when the pixels were already normalized to be in the range $\lbrack 0,1\rbrack$. This is a very high amount of noise, so much that when papers report the samples of their models, they don't add the noise term on which they report likelihood numbers. In other words, the added noise term is clearly incorrect for the problem, but is needed to make the maximum likelihood approach work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rather than estimating the density of ${\mathbb{P}}_{r}$ which may not exist, we can define a random variable $Z$ with a fixed distribution $p{(z)}$ and pass it through a parametric function $g_{\theta}:{\mathcal{Z}\rightarrow\mathcal{X}}$ (typically a neural network of some kind) that directly generates samples following a certain distribution ${\mathbb{P}}_{\theta}$. By varying $\theta$, we can change this distribution and make it close to the real data distribution ${\mathbb{P}}_{r}$. This is useful in two ways. First of all, unlike densities, this approach can represent distributions confined to a low dimensional manifold. Second, the ability to easily generate samples is often more useful than knowing the numerical value of the density (for example in image superresolution or semantic segmentation when considering the conditional distribution of the output image given the input image). In general, it is computationally difficult to generate samples given an arbitrary high dimensional density.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variational Auto-Encoders (VAEs) and Generative Adversarial Networks (GANs) are well known examples of this approach. Because VAEs focus on the approximate likelihood of the examples, they share the limitation of the standard models and need to fiddle with additional noise terms. GANs offer much more flexibility in the definition of the objective function, including Jensen-Shannon, and all $f$-divergences as well as some exotic combinations. On the other hand, training GANs is well known for being delicate and unstable, for reasons theoretically investigated.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we direct our attention on the various ways to measure how close the model distribution and the real distribution are, or equivalently, on the various ways to define a distance or divergence $\rho{({\mathbb{P}}_{\theta},{\mathbb{P}}_{r})}$. The most fundamental difference between such distances is their impact on the convergence of sequences of probability distributions. A sequence of distributions ${({\mathbb{P}}_{t})}_{t \in {\mathbb{N}}}$ converges if and only if there is a distribution ${\mathbb{P}}_{\infty}$ such that $\rho{({\mathbb{P}}_{t},{\mathbb{P}}_{\infty})}$ tends to zero, something that depends on how exactly the distance $\rho$ is defined.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Informally, a distance $\rho$ induces a weaker topology when it makes it easier for a sequence of distribution to converge.^11^1More exactly, the topology induced by $\rho$ is weaker than that induced by $\rho'$ when the set of convergent sequences under $\rho$ is a superset of that under $\rho'$. Section 2 clarifies how popular probability distances differ in that respect.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to optimize the parameter $\theta$, it is of course desirable to define our model distribution ${\mathbb{P}}_{\theta}$ in a manner that makes the mapping $\theta\mapsto{\mathbb{P}}_{\theta}$ continuous. Continuity means that when a sequence of parameters $\theta_{t}$ converges to $\theta$, the distributions ${\mathbb{P}}_{\theta_{t}}$ also converge to ${\mathbb{P}}_{\theta}$. However, it is essential to remember that the notion of the convergence of the distributions ${\mathbb{P}}_{\theta_{t}}$ depends on the way we compute the distance between distributions. The weaker this distance, the easier it is to define a continuous mapping from $\theta$-space to ${\mathbb{P}}_{\theta}$-space, since it's easier for the distributions to converge.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main reason we care about the mapping $\theta\mapsto{\mathbb{P}}_{\theta}$ to be continuous is as follows. If $\rho$ is our notion of distance between two distributions, we would like to have a loss function $\theta\mapsto{\rho{({\mathbb{P}}_{\theta},{\mathbb{P}}_{r})}}$ that is continuous, and this is equivalent to having the mapping $\theta\mapsto{\mathbb{P}}_{\theta}$ be continuous when using the distance between distributions $\rho$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are: In Section 2, we provide a comprehensive theoretical analysis of how the Earth Mover (EM) distance behaves in comparison to popular probability distances and divergences used in the context of learning distributions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3, we define a form of GAN called Wasserstein-GAN that minimizes a reasonable and efficient approximation of the EM distance, and we theoretically show that the corresponding optimization problem is sound.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4, we empirically show that WGANs cure the main training problems of GANs. In particular, training WGANs does not require maintaining a careful balance in training of the discriminator and the generator, and does not require a careful design of the network architecture either. The mode dropping phenomenon that is typical in GANs is also drastically reduced. One of the most compelling practical benefits of WGANs is the ability to continuously estimate the EM distance by training the discriminator to optimality. Plotting these learning curves is not only useful for debugging and hyperparameter searches, but also correlate remarkably well with the observed sample quality.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Different Distances", "weight": 1.0} -->

We now introduce our notation. Let $\mathcal{X}$ be a compact metric set (such as the space of images ${\lbrack 0,1\rbrack}^{d}$) and let $\Sigma$ denote the set of all the Borel subsets of $\mathcal{X}$. Let $\text{Prob}{(\mathcal{X})}$ denote the space of probability measures defined on $\mathcal{X}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Different Distances", "weight": 1.0} -->

We can now define elementary distances and divergences between two distributions ${{\mathbb{P}}_{r},{\mathbb{P}}_{g}} \in {\text{Prob}{(\mathcal{X})}}$: The *Total Variation* (TV) distance The *Kullback-Leibler* (KL) divergence where both ${\mathbb{P}}_{r}$ and ${\mathbb{P}}_{g}$ are assumed to be absolutely continuous, and therefore admit densities, with respect to a same measure $\mu$ defined on $\mathcal{X}$.^22^2Recall that a probability distribution ${\mathbb{P}}_{r} \in {\text{Prob}{(\mathcal{X})}}$ admits a density $p_{r}{(x)}$ with respect to $\mu$, that is, ${\forall A} \in \Sigma$,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Different Distances", "weight": 1.0} -->

The *Jensen-Shannon* (JS) divergence where ${\mathbb{P}}_{m}$ is the mixture ${({{\mathbb{P}}_{r} + {\mathbb{P}}_{g}})}/2$. This divergence is symmetrical and always defined because we can choose $\mu = {\mathbb{P}}_{m}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Different Distances", "weight": 1.0} -->

The *Earth-Mover* (EM) distance or Wasserstein-1 where $\Pi{({\mathbb{P}}_{r},{\mathbb{P}}_{g})}$ denotes the set of all joint distributions $\gamma{(x,y)}$ whose marginals are respectively ${\mathbb{P}}_{r}$ and ${\mathbb{P}}_{g}$. Intuitively, $\gamma{(x,y)}$ indicates how much "mass" must be transported from $x$ to $y$ in order to transform the distributions ${\mathbb{P}}_{r}$ into the distribution ${\mathbb{P}}_{g}$. The EM distance then is the "cost" of the optimal transport plan.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Different Distances", "weight": 1.0} -->

The following example illustrates how apparently simple sequences of probability distributions converge under the EM distance but do not converge under the other distances and divergences defined above.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1 (Learning parallel lines)", "weight": 1.0} -->

Example 1. ‣ 2 Different Distances ‣ Wasserstein GAN") gives us a case where we can learn a probability distribution over a low dimensional manifold by doing gradient descent on the EM distance. This cannot be done with the other distances and divergences because the resulting loss function is not even continuous. Although this simple example features distributions with disjoint supports, the same conclusion holds when the supports have a non empty intersection contained in a set of measure zero. This happens to be the case when two low dimensional manifolds intersect in general position.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1 (Learning parallel lines)", "weight": 1.0} -->

Since the Wasserstein distance is much weaker than the JS distance^33^3 The argument for *why* this happens, and indeed how we arrived to the idea that Wasserstein is what we should really be optimizing is displayed in Appendix Appendix A. We strongly encourage the interested reader who is not afraid of the mathematics to go through it., we can now ask whether $W{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}$ is a continuous loss function on $\theta$ under mild assumptions. This, and more, is true, as we now state and prove.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Wasserstein GAN", "weight": 1.0} -->

Again, Theorem 2 points to the fact that $W{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}$ might have nicer properties when optimized than $JS{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}$. However, the infimum in is highly intractable. On the other hand, the Kantorovich-Rubinstein duality tells us that where the supremum is over all the 1-Lipschitz functions $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Wasserstein GAN", "weight": 1.0} -->

Note that if we replace ${\| f\|}_{L} \leq 1$ for ${\| f\|}_{L} \leq K$ (consider $K$-Lipschitz for some constant $K$), then we end up with ${K \cdot W}{({\mathbb{P}}_{r},{\mathbb{P}}_{g})}$. Therefore, if we have a parameterized family of functions ${\{ f_{w}\}}_{w \in \mathcal{W}}$ that are all $K$-Lipschitz for some $K$, we could consider solving the problem and if the supremum in is attained for some $w \in \mathcal{W}$ (a pretty strong assumption akin to what's assumed when proving consistency of an estimator), this process would yield a calculation of $W{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}$ up to a multiplicative constant.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Wasserstein GAN", "weight": 1.0} -->

Furthermore, we could consider differentiating $W{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}$ (again, up to a constant) by back-proping through equation via estimating ${\mathbb{E}}_{z \sim {p{(z)}}}{\lbrack{{\nabla_{\theta}f_{w}}{({g_{\theta}{(z)}})}}\rbrack}$. While this is all intuition, we now prove that this process is principled under the optimality assumption.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

We run experiments on image generation using our Wasserstein-GAN algorithm and show that there are significant practical benefits to using it over the formulation used in standard GANs.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

We claim two main benefits: a meaningful loss metric that correlates with the generator's convergence and sample quality improved stability of the optimization process

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

We run experiments on image generation. The target distribution to learn is the LSUN-Bedrooms dataset -- a collection of natural images of indoor bedrooms. Our baseline comparison is DCGAN, a GAN with a convolutional architecture trained with the standard GAN procedure using the $- {\log D}$ trick. The generated samples are 3-channel images of 64x64 pixels in size. We use the hyper-parameters specified in Algorithm 1 for all of our experiments.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

Because the WGAN algorithm attempts to train the critic $f$ (lines 2--8 in Algorithm 1) relatively well before each generator update (line 10 in Algorithm 1), the loss function at this point is an estimate of the EM distance, up to constant factors related to the way we constrain the Lipschitz constant of $f$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

Our first experiment illustrates how this estimate correlates well with the quality of the generated samples. Besides the convolutional DCGAN architecture, we also ran experiments where we replace the generator or both the generator and the critic by 4-layer ReLU-MLP with 512 hidden units.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

To our knowledge, this is the first time in GAN literature that such a property is shown, where the loss of the GAN shows properties of convergence. This property is extremely useful when doing research in adversarial networks as one does not need to stare at the generated samples to figure out failure modes and to gain information on which models are doing better over others.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

However, we do not claim that this is a new method to quantitatively evaluate generative models yet. The constant scaling factor that depends on the critic's architecture means it's hard to compare models with different critics. Even more, in practice the fact that the critic doesn't have infinite capacity makes it hard to know just how close to the EM distance our estimate really is. This being said, we have succesfully used the loss metric to validate our experiments repeatedly and without failure, and we see this as a huge improvement in training GANs which previously had no such facility.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

In contrast, Figure 4 plots the evolution of the GAN estimate of the JS distance during GAN training. More precisely, during GAN training, the discriminator is trained to maximize which is is a lower bound of ${2JS{({\mathbb{P}}_{r},{\mathbb{P}}_{\theta})}} - {2{\log 2}}$. In the figure, we plot the quantity ${\frac{1}{2}L{(D,g_{\theta})}} + {\log 2}$, which is a lower bound of the JS distance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

This quantity clearly correlates poorly the sample quality. Note also that the JS estimate usually stays constant or goes up instead of going down. In fact it often remains very close to ${\log 2} \approx 0.69$ which is the highest value taken by the JS distance. In other words, the JS distance saturates, the discriminator has zero loss, and the generated samples are in some cases meaningful (DCGAN generator, top right plot) and in other cases collapse to a single nonsensical image. This last phenomenon has been theoretically explained in and highlighted.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

When using the $- {\log D}$ trick, the discriminator loss and the generator loss are different. Figure 8 in Appendix E reports the same plots for GAN training, but using the generator loss instead of the discriminator loss. This does not change the conclusions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Meaningful loss metric", "weight": 1.0} -->

Finally, as a negative result, we report that WGAN training becomes unstable at times when one uses a momentum based optimizer such as Adam (with $\beta_{1} > 0$) on the critic, or when one uses high learning rates. Since the loss for the critic is nonstationary, momentum based methods seemed to perform worse. We identified momentum as a potential cause because, as the loss blew up and samples got worse, the cosine between the Adam step and the gradient usually turned negative. The only places where this cosine was negative was in these situations of instability. We therefore switched to RMSProp which is known to perform well even on very nonstationary problems.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Improved stability", "weight": 1.0} -->

One of the benefits of WGAN is that it allows us to train the critic till optimality. When the critic is trained to completion, it simply provides a loss to the generator that we can train as any other neural network. This tells us that we no longer need to balance generator and discriminator's capacity properly. The better the critic, the higher quality the gradients we use to train the generator.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improved stability", "weight": 1.0} -->

We observe that WGANs are much more robust than GANs when one varies the architectural choices for the generator. We illustrate this by running experiments on three generator architectures: a convolutional DCGAN generator, a convolutional DCGAN generator without batch normalization and with a constant number of filters, and a 4-layer ReLU-MLP with 512 hidden units. The last two are known to perform very poorly with GANs. We keep the convolutional DCGAN architecture for the WGAN critic or the GAN discriminator.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Improved stability", "weight": 1.0} -->

Figures 7, 7, and 7 show samples generated for these three architectures using both the WGAN and GAN algorithms. We refer the reader to Appendix Appendix F for full sheets of generated samples. Samples were not cherry-picked.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improved stability", "weight": 1.0} -->

In no experiment did we see evidence of mode collapse for the WGAN algorithm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced an algorithm that we deemed WGAN, an alternative to traditional GAN training. In this new model, we showed that we can improve the stability of learning, get rid of problems like mode collapse, and provide meaningful learning curves useful for debugging and hyperparameter searches. Furthermore, we showed that the corresponding optimization problem is sound, and provided extensive theoretical work highlighting the deep connections to other distances between distributions.
