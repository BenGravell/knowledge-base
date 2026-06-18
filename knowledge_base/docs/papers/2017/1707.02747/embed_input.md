Robust Imitation of Diverse Behaviors

Deep generative models have recently shown great promise in imitation learning for motor control. Given enough data, even supervised approaches can do one-shot imitation learning; however, they are vulnerable to cascading failures when the agent trajectory diverges from the demonstrations. Compared to purely supervised methods, Generative Adversarial Imitation Learning (GAIL) can learn more robust controllers from fewer demonstrations, but is inherently mode-seeking and more difficult to train. In this paper, we show how to combine the favourable aspects of these two approaches. The base of our model is a new type of variational autoencoder on demonstration trajectories that learns semantic policy embeddings. We show that these embeddings can be learned on a 9 DoF Jaco robot arm in reaching tasks, and then smoothly interpolated with a resulting smooth interpolation of reaching behavior. Leveraging these policy representations, we develop a new version of GAIL that is much more robust than the purely-supervised controller, especially with few demonstrations, and avoids mode collapse, capturing many diverse behaviors when GAIL on its own does not....

## Introduction

Building versatile embodied agents, both in the form of real robots and animated avatars, capable of a wide and diverse set of behaviors is one of the long-standing challenges of AI. State-of-the-art robots cannot compete with the effortless variety and adaptive flexibility of motor behaviors produced by toddlers. Towards addressing this challenge, in this work we combine several deep generative approaches to imitation learning in a way that accentuates their individual strengths and addresses their limitations....

We first introduce a variational autoencoder (VAE) for supervised imitation, consisting of a bi-directional LSTM encoder mapping demonstration sequences to embedding vectors, and two decoders. The first decoder is a multi-layer perceptron (MLP) policy mapping a trajectory embedding and the current state to a continuous action vector. The second is a dynamics model mapping the embedding and previous state to the present state, while modelling correlations among states with a WaveNet....

We have proposed an approach for imitation learning that combines the favorable properties of techniques for density modeling with latent variables (VAEs) with those of GAIL. The result is a model that learns, from a moderate number of demonstration trajectories a semantically well structured embedding of behaviors, a corresponding multi-task controller that allows to robustly execute diverse behaviors from this embedding space, as well as an encoder that can map new trajectories into the embedding space and hence allows for one-shot imitation.

Our experimental results demonstrate that our approach can work on a variety of control problems, and that it scales even to very challenging ones such as the control of a simulated humanoid with a large number of degrees of freedoms.

### Lemma 1

In this section, we follow a similar approach to Duan et al., but opt for stochastic VAEs as having a distribution $q_{\phi}{(\left. z \middle| x_{1:T} \right.)}$ to better regularize the latent space.

All experiments are conducted with the MuJoCo physics engine. For details of the simulation and the experimental setup please see appendix.

While supervised policies that condition on demonstrations (such as our VAE or the recent approach of Duan et al....
