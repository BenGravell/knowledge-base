<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Connection between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models

Topics include Reinforcement learning, Inverse reinforcement learning, Imitation learning, Optimal control, Control, Learning, Generative adversarial network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generative adversarial networks (GANs) are a recently proposed class of generative models in which a generator is trained to optimize a cost function that is being simultaneously learned by a discriminator. While the idea of learning cost functions is relatively new to the field of generative modeling, learning costs has long been studied in control and reinforcement learning (RL) domains, typically for imitation learning from demonstrations. In these fields, learning cost function underlying observed behavior is known as inverse reinforcement learning (IRL) or inverse optimal control. While at first the connection between cost learning in RL and cost learning in generative modeling may appear to be a superficial one, we show in this paper that certain IRL methods are in fact mathematically equivalent to GANs. In particular, we demonstrate an equivalence between a sample-based algorithm for maximum entropy IRL and a GAN in which the generator's density can be evaluated and is provided as an additional input to the discriminator. Interestingly, maximum entropy IRL is a special case of an energy-based model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We discuss the interpretation of GANs as an algorithm for training energy-based models, and relate this interpretation to other recent work that seeks to connect GANs and EBMs. By formally highlighting the connection between GANs, IRL, and EBMs, we hope that researchers in all three communities can better identify and apply transferable ideas from one domain to another, particularly for developing more stable and scalable algorithms: a major challenge in all three domains.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generative adversarial networks (GANs) are a recently proposed class of generative models in which a generator is trained to optimize a cost function that is being simultaneously learned by a discriminator. While the idea of learning objectives is relatively new to the field of generative modeling, learning cost or reward functions has long been studied in control and was popularized in 2000 for reinforcement learning problems. In these fields, learning the cost function underlying demonstrated behavior is referred to as inverse reinforcement learning (IRL) or inverse optimal control (IOC). At first glance, the connection between cost learning in RL and cost learning for generative models may appear to be superficial; however, if we apply GANs to a setting where the generator density can be efficiently evaluated, the result is exactly equivalent to a sample-based algorithm for maximum entropy (MaxEnt) IRL. Interestingly, as MaxEnt IRL is an energy-based model, this connection suggests a method for using GANs to train a broader class of energy-based models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

MaxEnt IRL is a widely-used objective for IRL, proposed by Ziebart et al.. Sample-based algorithms for performing maximum entropy (MaxEnt) IRL have scaled cost learning to scenarios with unknown dynamics, using nonlinear function classes, such as neural networks. We show that the gradient updates for the cost and the policy in these methods can be viewed as the updates for the discriminator and generator in GANs, under a specific form of the discriminator. The key difference to a generic discriminator is that we need to be able evaluate the density of the generator, which we integrate into the discriminator in a natural way.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditionally, GANs are used to train generative models for which it is not possible to evaluate the density. When it is possible to evaluate the density, for example in an autoregressive model, it is typical to maximize the likelihood of the data directly. By considering the connection to IRL, we find that GAN training may be appropriate even when density values are available. For example, suppose we are interested in modeling a complex multimodal distribution, but our model does not have enough capacity to represent the distribution. Then maximizing likelihood will lead to a distribution which "covers" all of the modes, but puts most of its mass in parts of the space that have negligible density under the data distribution. These might be images that look extremely unrealistic, nonsensical sentences, or suboptimal robot behavior. A generator trained adversarially will instead try to "fill in" as many of modes as it can, without putting much mass in the space between modes. This results in lower diversity, but ensures that samples "look like" they could have been from the original data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By drawing an exact correspondence between adaptive, sample-based algorithms for MaxEnt IRL and GAN training, we show that this phenomenon occurs and is practically important: GAN training can significantly improve the quality of samples even when the generator density can be exactly evaluated. This is precisely analogous to the observed ability of inverse reinforcement learning to imitate behaviors that cannot be successfully learned through behavioral cloning, direct maximum likelihood regression to the demonstrated behavior.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Interestingly, the maximum entropy formulation of IRL is a special case of an energy-based model (EBM). The learned cost in MaxEnt IRL corresponds to the energy function, and is trained via maximum likelihood. Hence, we can also show how a particular form of GANs can be used to train EBMs. Recent works have recognized a connection between EBMs and GANs. In this work, we particularly focus on EBMs trained with maximum likelihood, and expand upon the connection recognized by Kim & Bengio for the case where the generator's density can be computed. By formally highlighting the connection between GANs, IRL, and EBMs, we hope that researchers in all three areas can better identify and apply transferable ideas from one domain to another.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

Generative adversarial networks are an approach to generative modeling where two models are trained simultaneously: a generator $G$ and a discriminator $D$. The discriminator is tasked with classifying its inputs as either the output of the generator, or actual samples from the underlying data distribution $p{(\mathbf{x})}$. The goal of the generator is to produce outputs that are classified by the discriminator as coming from the underlying data distribution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

Formally, the generator takes noise as input and outputs a sample $\mathbf{x} \sim G$, while the discriminator takes as input a sample $\mathbf{x}$ and outputs the probability $D{(\mathbf{x})}$ that the sample was from the data distribution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

The generator's loss can be defined one of several similar ways. The simplest definition, originally proposed, is simply the opposite of the discriminator's loss. However, this provides very little training signal if the generator's output can be easily distinguished from the real samples. It is common to instead use the log of the discriminator's confusion.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Energy-Based Models", "weight": 1.0} -->

The energy function parameters $\theta$ are often chosen to maximize the likelihood of the data; the main challenge in this optimization is evaluating the partition function $Z$, which is an intractable sum or integral for most high-dimensional problems. A common approach to estimating $Z$ requires sampling from the Boltzmann distribution $p_{\theta}(\mathbf{x})$ within the inner loop of learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Energy-Based Models", "weight": 1.0} -->

Sampling from $p_{\theta}(\mathbf{x})$ can be approximated by using Markov chain Monte Carlo (MCMC) methods; however, these methods face issues when there are several distinct modes of the distribution and, as a result, can take arbitrarily large amounts of time to produce a diverse set of samples. Approximate inference methods can also be used during training, though the energy function may incorrectly assign low energy to some modes if the approximate inference method cannot find them.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

The goal of inverse reinforcement learning is to infer the cost function underlying demonstrated behavior. It is typically assumed that the demonstrations come from an expert who is behaving near-optimally under some unknown cost. In this section, we discuss MaxEnt IRL and guided cost learning, an algorithm for MaxEnt IRL.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Maximum entropy inverse reinforcement learning", "weight": 1.0} -->

A more general form of this equation can be derived for stochastic dynamics. However, the analysis largely remains the same: the probability of a trajectory can be written as the product of conditional probabilities, but the conditional probabilities of the states $\mathbf{x}_{t}$ are not affected by $\theta$ and so factor out of all likelihood ratios.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Maximum entropy inverse reinforcement learning", "weight": 1.0} -->

Under this model, the optimal trajectories have the highest likelihood, and the expert can generate suboptimal trajectories with a probability that decreases exponentially as the trajectories become more costly. As in other energy-based models, the parameters $\theta$ are optimized to maximize the likelihood of the demonstrations. Estimating the partition function $Z$ is difficult for large or continuous domains, and presents the main computational challenge. The first applications of this model computed $Z$ exactly with dynamic programming. However, this is only practical in small, discrete domains, and is impossible in domains where the system dynamics $p{(\left. \mathbf{x}_{t + 1} \middle| {\mathbf{x}_{t},\mathbf{u}_{t}} \right.)}$ are unknown.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

Guided cost learning introduces an iterative sample-based method for estimating $Z$ in the MaxEnt IRL formulation, and can scale to high-dimensional state and action spaces and nonlinear cost functions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

Guided cost learning alternates between optimizing $c_{\theta}$ using this estimate, and optimizing $q(\tau)$ to minimize the variance of the importance sampling estimate.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

The optimal importance sampling distribution for estimating the partition function $\int{{\exp{({- {c_{\theta}{(\tau)}}})}}{d\tau}}$ is ${q(\tau)} \propto {|{\exp{({- {c_{\theta}{(\tau)}}})}}|} = {\exp{({- {c_{\theta}{(\tau)}}})}}$. During guided cost learning, the sampling policy $q(\tau)$ is updated to match this distribution by minimizing the KL divergence between $q(\tau)$ and $\frac{1}{Z}{\exp{({- {c_{\theta}{(\tau)}}})}}$, or equivalently minimizing the learned cost and maximizing entropy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

Conveniently, this optimal sampling distribution is the demonstration distribution for the true cost function. Thus, this training procedure results in both a learned cost function, characterizing the demonstration distribution, and a learned policy $q(\tau)$, capable of generating samples from the demonstration distribution.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

This importance sampling estimate can have very high variance if the sampling distribution $q$ fails to cover some trajectories $\tau$ with high values of $\exp\left( {- {c_{\theta}(\tau)}} \right)$. Since the demonstrations will have low cost (as a result of the IRL objective), we can address this coverage problem by mixing the demonstration data samples with the generated samples. Let $\mu = {{\frac{1}{2}p} + {\frac{1}{2}q}}$ be the mixture distribution over trajectory roll-outs. Let $\overset{\sim}{p}(\tau)$ be a rough estimate for the density of the demonstrations; for example we could use the current model $p_{\theta}$, or we could use a simpler density model trained using another method. Guided cost learning uses $\mu$ for importance sampling^22^2In RL settings, where generating samples requires executing a policy in the real world, such as in robotics, old samples from old generators are typically retained for efficiency.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Guided cost learning", "weight": 1.0} -->

In this case, the density $q$ can be computed using a fusion distribution over the past generator densities.,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Direct Maximum Likelihood and Behavioral Cloning", "weight": 1.0} -->

A simple approach to imitation learning and generative modeling is to train a generator or policy to output a distribution over the data, without learning a discriminator or energy function. For tractability, the data distribution is typically factorized using a directed graphical model or Bayesian network. In the field of generative modeling, this approach has most commonly been applied to speech and language generation tasks, but has also been applied to image generation. Like most EBMs, these models are trained by maximizing the likelihood of the observed data points.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Direct Maximum Likelihood and Behavioral Cloning", "weight": 1.0} -->

When a generative model does not have the capacity to represent the entire data distribution, maximizing likelihood directly will lead to a moment-matching distribution that tries to "cover" all of the modes, leading to a solution that puts much of its mass in parts of the space that have negligible probability under the true distribution. In many scenarios, it is preferable to instead produce only realistic, highly probable samples, by "filling in" as many modes as possible, at the trade-off of lower diversity. Since EBMs are also trained with maximum likelihood, the energy function in an EBM will exhibit the same moment-matching behavior when it has limited capacity. However, designing a flexible energy function to represent a distribution's density function is generally much easier than designing a tractable generator with the same flexibility, that can to generate samples without a complex iterative inference procedure. Moreover, once we have a trained energy function, the generator is trained to be mode-seeking, by minimizing the KL divergence between the generator's distribution and the distribution induced by the energy function.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Direct Maximum Likelihood and Behavioral Cloning", "weight": 1.0} -->

As a result, even if the generator has the same capacity as a generative model trained with direct maximum likelihood, the generator trained with an EBM will exhibit mode-seeking behavior as long as the energy function is more flexible than the generator. Of course, this phenomenon is often achieved at the cost of tractability, as generating samples from an energy function requires training a generator which, in the case of IRL, is forward policy optimization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Direct Maximum Likelihood and Behavioral Cloning", "weight": 1.0} -->

In sequential decision-making domains, using direct maximum likelihood is known as behavioral cloning, where the policy is trained with supervised learning to match the actions of the demonstrating agent, conditioned on the corresponding observations. While this approach is simple and often effective for small problems, the moment-matching behavior of direct maximum likelihood can produce particularly ineffective trajectories because of compounding errors. When the policy makes a small mistake, it deviates from the state distribution seen during training, making it more likely to make a mistake again. This issue compounds and eventually, the agent reaches a state far from the training distribution and makes a catastrophic error. Generative modeling also faces this issue when generating variables sequentially. A popular approach for handling this involves incrementally sampling more from the model and drawing less from the data distribution during training. This requires that the true data distribution can be sampled from during training, corresponding to a human or algorithmic expert. Bengio et al. proposed an approximate solution, termed scheduled sampling, that does not require querying the data distribution. However, while these approaches alleviate the issue, they do not solve it completely.

<!-- chunk {"id": "body-0027", "role": "body", "section": "GANs and IRL", "weight": 1.0} -->

We now show how generative adversarial modeling has implicitly been applied to the setting of inverse reinforcement learning, where the data-to-be-modeled is a set of expert demonstrations. The derivation requires a particular form of discriminator, which we discuss first in Section 3.1. After making this modification to the discriminator, we obtain an algorithm for IRL, as we show in Section 3.2, where the discriminator involves the learned cost and the generator represents the policy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A special form of discriminator", "weight": 1.0} -->

where $p{(\tau)}$ is the actual distribution of the data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "A special form of discriminator", "weight": 1.0} -->

In the traditional GAN algorithm, the discriminator is trained to directly output this value. When the generator density $q(\tau)$ can be evaluated, the traditional GAN discriminator can be modified to incorporate this density information. Instead of having the discriminator estimate the value of Equation 3 directly, it can be used to estimate $p{(\tau)}$, filling in the value of $q(\tau)$ with its known value. In this case, the new form of the discriminator $D_{\theta}$ with parameters $\theta$ is

<!-- chunk {"id": "body-0030", "role": "body", "section": "A special form of discriminator", "weight": 1.0} -->

In order to make the connection to MaxEnt IRL, we also replace the estimated data density with the Boltzmann distribution. As in MaxEnt IRL, we write the energy function as $c_{\theta}$ to designate the learned cost.

<!-- chunk {"id": "body-0031", "role": "body", "section": "A special form of discriminator", "weight": 1.0} -->

The resulting architecture for the discriminator is very similar to a typical model for binary classification, with a sigmoid as the final layer and $\log Z$ as the bias of the sigmoid. We have adjusted the architecture only by subtracting ${\log q}(\tau)$ from the input to the sigmoid. This modest change allows the optimal discriminator to be completely independent of the generator: the discriminator is optimal when ${\frac{1}{Z}{\exp\left( {- {c_{\theta}(\tau)}} \right)}} = {p(\tau)}$. Independence between the generator and the optimal discriminator may significantly improve the stability of training.

<!-- chunk {"id": "body-0032", "role": "body", "section": "A special form of discriminator", "weight": 1.0} -->

This change is very simple to implement and is applicable in any setting where the density $q(\tau)$ can be cheaply evaluated. Of course this is precisely the case where we could directly maximize likelihood, and we might wonder whether it is worth the additional complexity of GAN training. But the experience of researchers in IRL has shown that maximizing log likelihood directly is not always the most effective way to learn complex behaviors, even when it is possible to implement. As we will show, there is a precise equivalence between MaxEnt IRL and this type of GAN, suggesting that the same phenomenon may occur in other domains: GAN training may provide advantages even when it would be possible to maximize likelihood directly.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

In this section, we show that GANs, when applied to IRL problems, optimize the same objective as MaxEnt IRL, and in fact the variant of GANs described in the previous section is precisely equivalent to guided cost learning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

Recall that the discriminator's loss is equal to

<!-- chunk {"id": "body-0035", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

where we have substituted ${\overset{\sim}{p}(\tau)} = {p_{\theta}(\tau)} = {\frac{1}{Z}{\exp\left( {- {c_{\theta}(\tau)}} \right)}}$, i.e. we are using the current model to estimate the importance weights.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

The value of $Z$ which minimizes the discriminator's loss is an importance-sampling estimator for the partition function, as described in Section 2.3.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

For this value of $Z$, the derivative of the discriminator's loss with respect to $\theta$ is equal to the derivative of the MaxEnt IRL objective.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Equivalence between generative adversarial networks and guided cost learning", "weight": 1.0} -->

The generator's loss is exactly equal to the cost $c_{\theta}$ minus the entropy of $q(\tau)$, i.e. the MaxEnt policy loss defined in Equation 2 in Section 2.3.2.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$Z$ estimates the partition function", "weight": 1.0} -->

Only the first and last terms depend on $Z$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "$Z$ estimates the partition function", "weight": 1.0} -->

Thus the minimizing $Z$ is precisely the importance sampling estimate of the partition function in Equation 4.

<!-- chunk {"id": "body-0041", "role": "body", "section": "$c_{\\theta}$ optimizes the IRL objective", "weight": 1.0} -->

We return to the discriminator's loss as computed in Equation 8, and consider the derivative with respect to the parameters $\theta$. We will show that this is exactly the same as the derivative of the IRL objective.

<!-- chunk {"id": "body-0042", "role": "body", "section": "$c_{\\theta}$ optimizes the IRL objective", "weight": 1.0} -->

Only the second and fourth terms in the sum depend on $\theta$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "$c_{\\theta}$ optimizes the IRL objective", "weight": 1.0} -->

In the third equality, we used the definition of $Z$ as an importance sampling estimate. Note that in the second equality, we have treated $\overset{\sim}{\mu}(\tau)$ as a constant rather than as a quantity that depends on $\theta$. This is because the IRL optimization is minimizing ${\log Z} = {\log{\sum_{\tau}{\exp\left( {- {c_{\theta}(\tau)}} \right)}}}$ and using $\overset{\sim}{\mu}(\tau)$ as the weights for an importance sampling estimator of $Z$. For this purpose we do not want to differentiate through the importance weights.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The generator optimizes the MaxEnt IRL objective", "weight": 1.0} -->

The term $\log Z$ is a parameter of the discriminator that is held fixed while optimizing the generator, this loss is exactly equivalent the sampler loss from MaxEnt IRL, defined in Equation 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are many apparent differences between MaxEnt IRL and the GAN optimization problem. But, we have shown that after making a single key change---using a generator $q(\tau)$ for which densities can be evaluated efficiently, and incorporating this information into the discriminator in a natural way---generative adversarial networks can be viewed as a sample-based algorithm for the MaxEnt IRL problem. By connecting GANs to the empirical literature on inverse reinforcement learning, this demonstrates that GAN training can improve the quality of samples even when the generator's density can be evaluated exactly. By generalizing this connection, we can derive a new adversarial training strategy for energy-based models, which we discuss in the next section.

<!-- chunk {"id": "body-0046", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

Now that we have highlighted the connection between GANs and guided cost learning, the application of GANs to EBMs follows directly. As discussed in Section 2.2, the primary challenge in training EBMs is estimating the partition function, which is done by approximately sampling from the distribution induced by the energy $E_{\theta}$. Two recent papers have proposed to use adversarial training to derive fast estimates of the partition function. In particular, these methods alternate between training a generator to produce samples with minimal energy $E_{\theta}{(\mathbf{x})}$, and optimizing the parameters of the energy function using the samples to estimate the partition function.

<!-- chunk {"id": "body-0047", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

When the density of the generator is available, however, we can derive an unbiased estimate of the partition function as

<!-- chunk {"id": "body-0048", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

where $\mu$ denotes an equal mixture of generated and real data points, $q{(\mathbf{x})}$ denotes the density under the generator, and $\overset{\sim}{p}(\mathbf{x})$ denotes an estimate for the data density.

<!-- chunk {"id": "body-0049", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

If we set ${\overset{\sim}{p}(\mathbf{x})} = {p_{\theta}(\mathbf{x})}$, the resulting model is a special case of a GAN which is straightforward to implement. The discriminator's output is $\sigma\left( {{E_{\theta}(\mathbf{x})} - {{\log q}(\mathbf{x})}} \right)$, where $\sigma$ is a sigmoid with a trainable bias. The discriminator's loss is the log probability and the generator's loss is the discriminator's log odds, as defined in Section 2.1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

Kim & Bengio proposed a similar energy-based model for generative image modeling, but did not assume they could compute the generator's density. As a result, they do not use importance weights, and work with a biased estimator of the partition function which converges to the true partition function when the generator correctly samples from the energy-based model. In contrast, by using the generator density, we can get an unbiased estimate of the partition function that does not rely on any assumptions about the generator. Thus, even if the generator cannot learn to sample exactly from the data distribution, our training procedure is consistent.

<!-- chunk {"id": "body-0051", "role": "body", "section": "GANs for training EBMs", "weight": 1.0} -->

Zhao et al. also proposed an energy-based GAN model with an autoencoder discriminator where the energy is given by the mean-squared error between the data example (generated or real) and the discriminator's reconstruction. The energy function is optimized with a margin loss, and the generator is trained to minimize energy. This method also did not use the form of discriminator presented above. An interesting direction for future exploration is to consider combining the GAN training algorithm discussed here with an objective other than log-likelihood, such as one used with EBMs or different $f$-divergences used with GANs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we showed an equivalence between generative adversarial modeling and an algorithm for performing maximum entropy inverse reinforcement learning. Our derivation used a special form of discriminator that leverages likelihood values from the generator, leading to an unbiased estimate of the underlying energy function. A natural direction for future work is to experiment with combining deep generators that can provide densities, such as autoregressive models or models that use invertible transformations, with generative adversarial modeling. Such an approach may provide more stable training, better generators, and wider applicability to discrete problems such as language.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

This work also suggests a new algorithm for training energy-based models using generative adversarial networks, that trains a neural network model to sample from the distribution induced by the current energy. This method could reduce the computational challenges of existing MCMC-based solutions.
