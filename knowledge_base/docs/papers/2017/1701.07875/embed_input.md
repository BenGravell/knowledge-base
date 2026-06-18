Wasserstein GAN

Topics include Stability analysis, Optimization, Learning, Wasserstein distances, Wasserstein generative adversarial network.

We introduce a new algorithm named WGAN, an alternative to traditional GAN training. In this new model, we show that we can improve the stability of learning, get rid of problems like mode collapse, and provide meaningful learning curves useful for debugging and hyperparameter searches. Furthermore, we show that the corresponding optimization problem is sound, and provide extensive theoretical work highlighting the deep connections to other distances between distributions.

## Introduction

The problem this paper is concerned with is that of unsupervised learning. Mainly, what does it mean to learn a probability distribution? The classical answer to this is to learn a probability density. This is often done by defining a parametric family of densities ${(P_{\theta})}_{\theta \in {\mathbb{R}}^{d}}$ and finding the one that maximized the likelihood on our data: if we have real data examples ${\{ x^{(i)}\}}_{i = 1}^{m}$, we would solve the problem

If the real data distribution ${\mathbb{P}}_{r}$ admits a density and ${\mathbb{P}}_{\theta}$ is the distribution of the parametrized density $P_{\theta}$, then, asymptotically, this amounts to minimizing the Kullback-Leibler divergence $KL{({{\mathbb{P}}_{r} \parallel {\mathbb{P}}_{\theta}})}$.

## Conclusion

We introduced an algorithm that we deemed WGAN, an alternative to traditional GAN training. In this new model, we showed that we can improve the stability of learning, get rid of problems like mode collapse, and provide meaningful learning curves useful for debugging and hyperparameter searches. Furthermore, we showed that the corresponding optimization problem is sound, and provided extensive theoretical work highlighting the deep connections to other distances between distributions.

### Proof

### Proof

Because the WGAN algorithm attempts to train the critic $f$ (lines 2--8 in Algorithm 1) relatively well before each generator update (line 10 in Algorithm 1), the loss function at this point is an estimate of the EM distance, up to constant factors related to the way we constrain the Lipschitz constant of $f$.

For this to make sense, we need the model density $P_{\theta}$ to exist. This is not the case in the rather common situation where we are dealing with distributions supported by low dimensional manifolds. It is then unlikely that the model manifold and the true distribution's support have a non-negligible intersection (see ), and this means that the KL distance is not defined (or simply infinite).

The typical remedy is to add a noise term to the model distribution. This is why virtually all generative models described in the classical machine learning literature include a noise component. In the simplest case, one assumes a Gaussian noise with relatively high bandwidth in order to cover all the examples....
