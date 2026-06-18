<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Imitation of Diverse Behaviors

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep generative models have recently shown great promise in imitation learning for motor control. Given enough data, even supervised approaches can do one-shot imitation learning; however, they are vulnerable to cascading failures when the agent trajectory diverges from the demonstrations. Compared to purely supervised methods, Generative Adversarial Imitation Learning (GAIL) can learn more robust controllers from fewer demonstrations, but is inherently mode-seeking and more difficult to train. In this paper, we show how to combine the favourable aspects of these two approaches. The base of our model is a new type of variational autoencoder on demonstration trajectories that learns semantic policy embeddings. We show that these embeddings can be learned on a 9 DoF Jaco robot arm in reaching tasks, and then smoothly interpolated with a resulting smooth interpolation of reaching behavior. Leveraging these policy representations, we develop a new version of GAIL that is much more robust than the purely-supervised controller, especially with few demonstrations, and avoids mode collapse, capturing many diverse behaviors when GAIL on its own does not.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate our approach on learning diverse gaits from demonstration on a 2D biped and a 62 DoF 3D humanoid in the MuJoCo physics environment.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building versatile embodied agents, both in the form of real robots and animated avatars, capable of a wide and diverse set of behaviors is one of the long-standing challenges of AI. State-of-the-art robots cannot compete with the effortless variety and adaptive flexibility of motor behaviors produced by toddlers. Towards addressing this challenge, in this work we combine several deep generative approaches to imitation learning in a way that accentuates their individual strengths and addresses their limitations. The end product of this is a robust neural network policy that can imitate a large and diverse set of behaviors using few training demonstrations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We first introduce a variational autoencoder (VAE) for supervised imitation, consisting of a bi-directional LSTM encoder mapping demonstration sequences to embedding vectors, and two decoders. The first decoder is a multi-layer perceptron (MLP) policy mapping a trajectory embedding and the current state to a continuous action vector. The second is a dynamics model mapping the embedding and previous state to the present state, while modelling correlations among states with a WaveNet. Experiments with a 9 DoF Jaco robot arm and a 9 DoF 2D biped walker, implemented in the MuJoCo physics engine, show that the VAE learns a structured semantic embedding space, which allows for smooth policy interpolation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While supervised policies that condition on demonstrations (such as our VAE or the recent approach of Duan et al. ) are powerful models for one-shot imitation, they require large training datasets in order to work for non-trivial tasks. They also tend to be brittle and fail when the agent diverges too much from the demonstration trajectories. These limitations of supervised learning for imitation, also known as behavioral cloning (BC), are well known.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Ho and Ermon showed a way to overcome the brittleness of supervised imitation using another type of deep generative model called Generative Adversarial Networks (GANs). Their technique, called Generative Adversarial Imitation Learning (GAIL) uses reinforcement learning, allowing the agent to interact with the environment during training. GAIL allows one to learn more robust policies with fewer demonstrations, but adversarial training introduces another difficulty called mode collapse. This refers to the tendency of adversarial generative models to cover only a subset of modes of a probability distribution, resulting in a failure to produce adequately diverse samples. This will cause the learned policy to capture only a subset of control behaviors (which can be viewed as modes of a distribution), rather than allocating capacity to cover all modes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Roughly speaking, VAEs can model diverse behaviors without dropping modes, but do not learn robust policies, while GANs give us robust policies but insufficiently diverse behaviors. In section 3, we show how to engineer an objective function that takes advantage of both GANs and VAEs to obtain robust policies capturing diverse behaviors. In section 4, we show that our combined approach enables us to learn diverse behaviors for a 9 DoF 2D biped and a 62 DoF humanoid, where the VAE policy alone is brittle and GAIL alone does not capture all of the diverse behaviors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Behavioral cloning with variational autoencoders suited for control", "weight": 1.0} -->

In this section, we follow a similar approach to Duan et al., but opt for stochastic VAEs as having a distribution $q_{\phi}{(\left. z \middle| x_{1:T} \right.)}$ to better regularize the latent space.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Behavioral cloning with variational autoencoders suited for control", "weight": 1.0} -->

In our VAE, an encoder maps a demonstration sequence to an embedding vector $z$. Given $z$, we decode both the state and action trajectories as shown in Figure 1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Behavioral cloning with variational autoencoders suited for control", "weight": 1.0} -->

Our encoder $q$ uses a bi-directional LSTM. To produce the final embedding, it calculates the average of all the outputs of the second layer of this LSTM before applying a final linear transformation to generate the mean and standard deviation of an Gaussian. We take one sample from this Gaussian as our demonstration encoding.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Behavioral cloning with variational autoencoders suited for control", "weight": 1.0} -->

The action decoder is an MLP that maps both the state and the embedding to the parameters of a Gaussian. The state decoder is similar to a conditional WaveNet model. In particular, it conditions on the embedding $z$ and previous state $x_{t - 1}$ to generate the vector $x_{t}$ autoregressively. That is, the autoregression is over the components of the vector $x_{t}$. Wavenet lessens the load of the encoder which no longer has to carry information that can be captured by modeling auto-correlations between components of the state vector. Finally, instead of a Softmax, we use a mixture of Gaussians as the output of the WaveNet.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

As pointed out earlier, it is hard for BC policies to mimic experts under environmental perturbations. Our solution to obtain more robust policies from few demonstrations, which are also capable of diverse behaviors, is to build on GAIL. Specifically, to enable GAIL to produce diverse solutions, we condition the discriminator on the embeddings generated by the VAE encoder and integrate out the GAIL objective with respect to the variational posterior $q_{\phi}{(\left. z \middle| x_{1:T} \right.)}$. Specifically, we train the discriminator by optimizing the following objective

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

A related work introduces a conditional GAIL objective to learn controllers for multiple behaviors from state trajectories, but the discriminator conditions on an annotated class label, as in conditional GANs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

We condition on unlabeled trajectories, which have been passed through a powerful encoder, and hence our approach is capable of one-shot imitation learning. Moreover, the VAE encoder enables us to obtain a continuous latent embedding space where interpolation is possible, as shown in Figure 3.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

Since our discriminator is conditional, the reward function is also conditional: ${r_{\psi}^{t}{(x_{t},\left. a_{t} \middle| z \right.)}} = {- {\log{({1 - {D_{\psi}{(x_{t},\left. a_{t} \middle| z \right.)}}})}}}$. We also clip the reward so that it is upper-bounded. Conditioning on $z$ allows us to generate an infinite number of reward functions each of them tailored to imitating a different trajectory. Policy gradients, though mode seeking, will not cause collapse into one particular mode due to the diversity of reward functions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

To better motivate our objective, let us temporarily leave the context of imitation learning and consider the following alternative value function for training GANs

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diverse generative adversarial imitation learning", "weight": 1.0} -->

This function is a simplification of our objective function. Furthermore, it satisfies the following property.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

The primary focus of our experimental evaluation is to demonstrate that the architecture allows learning of robust controllers capable of producing the full spectrum of demonstration behaviors for a diverse range of challenging control problems. We consider three bodies: a 9 DoF robotic arm, a 9 DoF planar walker, and a 62 DoF complex humanoid (56-actuated joint angles, and a freely translating and rotating 3d root joint). While for the reaching task BC is sufficient to obtain a working controller, for the other two problems our full learning procedure is critical.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

We analyze the resulting embedding spaces and demonstrate that they exhibit rich and sensible structure that an be exploited for control. Finally, we show that the encoder can be used to capture the gist of novel demonstration trajectories which can then be reproduced by the controller.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

All experiments are conducted with the MuJoCo physics engine. For details of the simulation and the experimental setup please see appendix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Robotic arm reaching", "weight": 1.0} -->

We first demonstrate the effectiveness of our VAE architecture and investigate the nature of the learned embedding space on a reaching task with a simulated Jaco arm. The physical Jaco is a robotics arm developed by Kinova Robotics.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robotic arm reaching", "weight": 1.0} -->

To obtain demonstrations, we trained 60 independent policies to reach to random target locations^11^1See appendix for details in the workspace starting from the same initial configuration. We generated 30 trajectories from each of the first 50 policies. These serve as training data for the VAE model (1500 training trajectories in total). The remaining 10 policies were used to generate test data.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robotic arm reaching", "weight": 1.0} -->

The reaching task is relatively simple, so with this amount of data the VAE policy is fairly robust. After training, the VAE encodes and reproduces the demonstrations as shown in Figure 2. Representative examples can be found in the video in the supplemental material.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Robotic arm reaching", "weight": 1.0} -->

To further investigate the nature of the embedding space we encode two trajectories. Next, we construct the embeddings of interpolating policies by taking convex combinations of the embedding vectors of the two trajectories. We condition the VAE policy on these interpolating embeddings and execute it. The results of this experiment are illustrated with a representative pair in Figure 3. We observe that interpolating in the latent space indeed corresponds to interpolation in task (trajectory endpoint) space, highlighting the semantic meaningfulness of the discovered latent space.

<!-- chunk {"id": "body-0026", "role": "body", "section": "2D Walker", "weight": 1.0} -->

We found reaching behavior to be relatively easy to imitate, presumably because it does not involve much physical contact. As a more challenging test we consider bipedal locomotion. We train $60$ neural network policies for a 2d walker to serve as demonstrations^22^2See section A.2 in the appendix for details.. These policies are each trained to move at different speeds both forward and backward depending on a label provided as additional input to the policy. Target speeds for training were chosen from a set of four different speeds (m/s): -1, 0, 1, 3. For the distribution of speeds that the trained policies actually achieve see Figure 4, top right). Besides the target speed the reward function imposes few constraints on the behavior. The resulting policies thus form a diverse set with several rather idiosyncratic movement styles. While for most purposes this diversity is undesirable, for the present experiment we consider it a feature.

<!-- chunk {"id": "body-0027", "role": "body", "section": "2D Walker", "weight": 1.0} -->

We trained our model with $20$ episodes per policy ($1200$ demonstration trajectories in total, each with a length of 400 steps or 10s of simulated time). In this experiment our full approach is required: training the VAE with BC alone can imitate some of the trajectories, but it performs poorly in general, presumably because our relatively small training set does not cover the space of trajectories sufficiently densely. On this generated dataset, we also train policies with GAIL using the same architecture and hyper-parameters. Due to the lack of conditioning, GAIL does not reproduce coherently trajectories. Instead, it simply meshes different behaviors together. In addition, the policies trained with GAIL also exhibit dramatically less diversity; see video.

<!-- chunk {"id": "body-0028", "role": "body", "section": "2D Walker", "weight": 1.0} -->

A general problem of adversarial training is that there is no easy way to quantitatively assess the quality of learned models. Here, since we aim to imitate particular demonstration trajectories that were trained to achieve particular target speed(s) we can use the difference between the speed of the demonstration trajectory the trajectory produced by the decoder as a surrogate measure of the quality of the imitation (cf. also ).

<!-- chunk {"id": "body-0029", "role": "body", "section": "2D Walker", "weight": 1.0} -->

The general quality of the learned model and the improvement achieved by the adversarial stage of our training procedure are quantified in Fig. 4. We draw $660$ trajectories ($11$ trajectories each for all $60$ policies) from the training set, compute the corresponding embedding vectors using the encoder, and use both the VAE policy as well as the improved policy from the adversarial stage to imitate each of the trajectories. We determine the absolute values of the difference between the average speed of the demonstration and the imitation trajectories (measured in $m/s$). As shown in Fig. 4 the adversarial training greatly improves reliability of the controller as well as the ability of the model to accurately match the speed of the demonstration. Video of our agent imitating a diverse set of behaviors can be found in the supplemental material.

<!-- chunk {"id": "body-0030", "role": "body", "section": "2D Walker", "weight": 1.0} -->

To assess generalization to novel trajectories we encode and subsequently imitate trajectories not contained in the training set. The supplemental video contains several representative examples, demonstrating that the style of movement is successfully imitated for previously unseen trajectories.

<!-- chunk {"id": "body-0031", "role": "body", "section": "2D Walker", "weight": 1.0} -->

Finally, we analyze the structure of the embedding space. We embed training trajectories and perform dimensionality reduction with t-SNE. The result is shown in Fig. 4. It reveals a clear clustering according to movement speeds thus recovering the nature of the task context for the demonstration trajectories. We further find that trajectories that are nearby in embedding space tend to correspond to similar movement styles even when differing in speed.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Complex humanoid", "weight": 1.0} -->

We consider a humanoid body of high dimensionality that poses a hard control problem. The construction of this body and associated control policies is described, and is briefly summarized in the appendix (section A.3) for completness. We generate training trajectories with the existing controllers, which can produce instances of one of six different movement styles (see section A.3). Examples of such trajectories are shown in Fig. 5 and in the supplemental video.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Complex humanoid", "weight": 1.0} -->

The training set consists of $250$ random trajectories from $6$ different neural network controllers that were trained to match $6$ different movement styles from the CMU motion capture data base^33^3See appendix for details.. Each trajectory is 334 steps or 10s long. We use a second set of $5$ controllers from which we generate trajectories for evaluation (3 of these policies were trained on the same movement styles as the policies used for generating training data).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Complex humanoid", "weight": 1.0} -->

Surprisingly, despite the complexity of the body, supervised learning is quite effective at producing sensible controllers: The VAE policy is reasonably good at imitating the demonstration trajectories, although it lacks the robustness to be practically useful. Adversarial training dramatically improves the stability of the controller. We analyze the improvement quantitatively by computing the percentage of the humanoid falling down before the end of an episode while imitating either training or test policies. The results are summarized in Figure 5 right. The figure further shows sequences of frames of representative demonstration and associated imitation trajectories. Videos of demonstration and imitation behaviors can be found in the supplemental video.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Complex humanoid", "weight": 1.0} -->

For practical purposes it is desirable to allow the controller to transition from one behavior to another. We test this possibility in an experiment similar to the one for the Jaco arm: We determine the embedding vectors of pairs of demonstration trajectories, start the trajectory by conditioning on the first embedding vector, and then transition from one behavior to the other half-way through the episode by blending their embeddings over a window of 20 control steps. Although not always successful the learned controller often transitions robustly, despite not having been trained to do so. Representative examples of these transitions can be found in the supplemental video.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have proposed an approach for imitation learning that combines the favorable properties of techniques for density modeling with latent variables (VAEs) with those of GAIL. The result is a model that learns, from a moderate number of demonstration trajectories a semantically well structured embedding of behaviors, a corresponding multi-task controller that allows to robustly execute diverse behaviors from this embedding space, as well as an encoder that can map new trajectories into the embedding space and hence allows for one-shot imitation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our experimental results demonstrate that our approach can work on a variety of control problems, and that it scales even to very challenging ones such as the control of a simulated humanoid with a large number of degrees of freedoms.
