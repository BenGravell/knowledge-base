<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Latent Dynamics for Planning from Pixels

Topics include Model-based, Reinforcement learning, Contact dynamics, Partial observability, Sparse rewards, Sample efficiency, Dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

One of the earlier papers describing a successful approach using a deep-learned predictive world model from image inputs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning has been very successful for control tasks with known environment dynamics. To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world. However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains. We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space. To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps. We approach this using a latent dynamics model with both deterministic and stochastic transition components. Moreover, we propose a multi-step variational inference objective that we name latent overshooting. Using only pixel observations, our agent solves continuous control tasks with contact dynamics, partial observability, and sparse rewards, which exceed the difficulty of tasks that were previously solved by planning with learned models. PlaNet uses substantially fewer episodes and reaches final performance close to and sometimes higher than strong model-free algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning is a natural and powerful approach to decision making problems with known dynamics, such as game playing and simulated robot control. To plan in unknown environments, the agent needs to learn the dynamics from experience. Learning dynamics models that are accurate enough for planning has been a long-standing challenge. Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning using learned models offers several benefits over model-free reinforcement learning. First, model-based planning can be more data efficient because it leverages a richer training signal and does not require propagating rewards through Bellman backups. Moreover, planning carries the promise of increasing performance just by increasing the computational budget for searching for actions, as shown by Silver et al.. Finally, learned dynamics can be independent of any specific task and thus have the potential to transfer well to other tasks in the environment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has shown promise in learning the dynamics of simple low-dimensional environments. However, these approaches typically assume access to the underlying state of the world and the reward function, which may not be available in practice. In high-dimensional environments, we would like to learn the dynamics in a compact latent space to enable fast planning. The success of such latent models has previously been limited to simple tasks such as balancing cartpoles and controlling 2-link arms from dense rewards.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent space. To learn the dynamics, we use a transition model with both stochastic and deterministic components. Moreover, we experiment with a novel generalized variational objective that encourages multi-step predictions. PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, shown in LABEL:fig:domains, by learning a dynamics model and efficiently planning in its latent space. Our agent substantially outperforms the model-free A3C and in some cases D4PG algorithm in final performance, with on average $200 \times$ less environment interaction and similar computation time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recurrent state space model We design a latent dynamics model with both deterministic and stochastic components. Our experiments indicate having both components to be crucial for high planning performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Latent overshooting We generalize the standard variational bound to include multi-step predictions. Using only terms in latent space results in a fast regularizer that can improve long-term predictions and is compatible with any latent sequence model.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Latent Space Planning", "weight": 1.0} -->

1 Initialize dataset 𝒟 with S random seed episodes.;
2 Initialize model parameters θ randomly.;
3 while not converged do
4 for update step s = 1..C do
5 Draw sequence chunks {(ot rt)t = kL + k}i = 1B ∼ 𝒟 uniformly at random from the dataset.;
6 Compute loss ℒ (θ) from Equation 3.;
7 Update model parameters θ ← θ − α ∇θℒ (θ).;
10 for time step $t = 1..\left\lceil \frac{T}{R} \right\rceil$ do
11 Infer belief over current state q (st,a &lt; t) from the history.;
12 at ← planner( q (st,a &lt; t), p ), see Algorithm 2 in the appendix for details.;
13 Add exploration noise ϵ ∼ p (ϵ) to the action.;
14 for action repeat k = 1..R do
15 rtk, ot + 1k ← env.step( at );
Algorithm 1 Deep Planning Network (PlaNet)

<!-- chunk {"id": "body-0012", "role": "body", "section": "Latent Space Planning", "weight": 1.0} -->

To solve unknown environments via planning, we need to model the environment dynamics from experience. PlaNet does so by iteratively collecting data using planning and training the dynamics model on the gathered data. In this section, we introduce notation for the environment and describe the general implementation of our model-based agent. In this section, we assume access to a learned dynamics model. Our design and training objective for this model are detailed in Section 3.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Since individual image observations generally do not reveal the full state of the environment, we consider a partially observable Markov decision process (POMDP). We define a discrete time step $t$, hidden states $s_{t}$, image observations $o_{t}$, continuous action vectors $a_{t}$, and scalar rewards $r_{t}$, that follow the stochastic dynamics

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setup", "weight": 1.0} -->

where we assume a fixed initial state $s_{0}$ without loss of generality. The goal is to implement a policy $p{({a_{t}{}_{}},a_{< t})}$ that maximizes the expected sum of rewards $E_{p}\left\lbrack {\sum_{t = 1}^{T}r_{t}} \right\rbrack$, where the expectation is over the distributions of the environment and the policy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model-based planning", "weight": 1.0} -->

PlaNet learns a transition model $p{({s_{t}{}_{t - 1}},a_{t - 1})}$, observation model $p{({o_{t}{}_{t}})}$, and reward model $p{({r_{t}{}_{t}})}$ from previously experienced episodes (note italic letters for the model compared to upright letters for the true dynamics). The observation model provides a rich training signal but is not used for planning. We also learn an encoder $q{({s_{t}{}_{}},a_{< t})}$ to infer an approximate belief over the current hidden state from the history using filtering. Given these components, we implement the policy as a planning algorithm that searches for the best sequence of future actions. We use model-predictive control to allow the agent to adapt its plan based on new observations, meaning we replan at each step. In contrast to model-free and hybrid reinforcement learning algorithms, we do not use a policy or value network.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experience collection", "weight": 1.0} -->

Since the agent may not initially visit all parts of the environment, we need to iteratively collect new experience and refine the dynamics model. We do so by planning with the partially trained model, as shown in Algorithm 1. Starting from a small amount of $S$ seed episodes collected under random actions, we train the model and add one additional episode to the data set every $C$ update steps. When collecting episodes for the data set, we add small Gaussian exploration noise to the action. To reduce the planning horizon and provide a clearer learning signal to the model, we repeat each action $R$ times, as common in reinforcement learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Planning algorithm", "weight": 1.0} -->

We use the cross entropy method to search for the best action sequence under the model, as outlined in Algorithm 2. We decided on this algorithm because of its robustness and because it solved all considered tasks when given the true dynamics for planning. CEM is a population-based optimization algorithm that infers a distribution over action sequences that maximize the objective. As detailed in Algorithm 2 in the appendix, we initialize a time-dependent diagonal Gaussian belief over optimal action sequences $a_{t:{t + H}} \sim {{Normal}{(\mu_{t:{t + H}},{\sigma_{t:{t + H}}^{2}{\mathbb{I}}})}}$, where $t$ is the current time step of the agent and $H$ is the length of the planning horizon. Starting from zero mean and unit variance, we repeatedly sample $J$ candidate action sequences, evaluate them under the model, and re-fit the belief to the top $K$ action sequences. After $I$ iterations, the planner returns the mean of the belief for the current time step, $\mu_{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Planning algorithm", "weight": 1.0} -->

Importantly, after receiving the next observation, the belief over action sequences starts from zero mean and unit variance again to avoid local optima.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Planning algorithm", "weight": 1.0} -->

To evaluate a candidate action sequence under the learned model, we sample a state trajectory starting from the current state belief, and sum the mean rewards predicted along the sequence. Since we use a population-based optimizer, we found it sufficient to consider a single trajectory per action sequence and thus focus the computational budget on evaluating a larger number of different sequences. Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows for fast evaluation of large batches of action sequences. The next section introduces the latent dynamics model that the planner uses.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Recurrent State Space Model", "weight": 1.0} -->

For planning, we need to evaluate thousands of action sequences at every time step of the agent. Therefore, we use a recurrent state-space model (RSSM) that can predict forward purely in latent space, similar to recently proposed models. This model can be thought of as a non-linear Kalman filter or sequential VAE. Instead of an extensive comparison to prior architectures, we highlight two findings that can guide future designs of dynamics models: our experiments show that both stochastic and deterministic paths in the transition model are crucial for successful planning. In this section, we remind the reader of latent state-space models and then describe our dynamics model.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Latent dynamics", "weight": 1.0} -->

We consider sequences ${\{ o_{t},a_{t},r_{t}\}}_{t = 1}^{T}$ with discrete time step $t$, image observations $o_{t}$, continuous action vectors $a_{t}$, and scalar rewards $r_{t}$. A typical latent state-space model is shown in Figure 1(b) and resembles the structure of a partially observable Markov decision process. It defines the generative process of the images and rewards using a hidden state sequence ${\{ s_{t}\}}_{t = 1}^{T}$,

<!-- chunk {"id": "body-0022", "role": "body", "section": "Latent dynamics", "weight": 1.0} -->

where we assume a fixed initial state $s_{0}$ without loss of generality. The transition model is Gaussian with mean and variance parameterized by a feed-forward neural network, the observation model is Gaussian with mean parameterized by a deconvolutional neural network and identity covariance, and the reward model is a scalar Gaussian with mean parameterized by a feed-forward neural network and unit variance. Note that the log-likelihood under a Gaussian distribution with unit variance equals the mean squared error up to a constant.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Variational encoder", "weight": 1.0} -->

Since the model is non-linear, we cannot directly compute the state posteriors that are needed for parameter learning. Instead, we use an encoder ${q{({s_{1:T}{}_{1:T}},a_{1:T})}} = {\prod_{t = 1}^{T}{q{({s_{t}{}_{t - 1}},a_{t - 1},o_{t})}}}$ to infer approximate state posteriors from past observations and actions, where $q{({s_{t}{}_{t - 1}},a_{t - 1},o_{t})}$ is a diagonal Gaussian with mean and variance parameterized by a convolutional neural network followed by a feed-forward neural network. We use the filtering posterior that conditions on past observations since we are ultimately interested in using the model for planning, but one may also use the full smoothing posterior during training.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training objective", "weight": 1.0} -->

Using the encoder, we construct a variational bound on the data log-likelihood. For simplicity, we write losses for predicting only the observations --- the reward losses follow by analogy. The variational bound obtained using Jensen's inequality is

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training objective", "weight": 1.0} -->

For the derivation, please see Equation 8 in the appendix. Estimating the outer expectations using a single reparameterized sample yields an efficient objective for inference and learning in non-linear latent variable models that can be optimized using gradient ascent.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Deterministic path", "weight": 1.0} -->

Despite its generality, the purely stochastic transitions make it difficult for the transition model to reliably remember information for multiple time steps. In theory, this model could learn to set the variance to zero for some state components, but the optimization procedure may not find this solution. This motivates including a deterministic sequence of activation vectors ${\{ h_{t}\}}_{t = 1}^{T}$ that allow the model to access not just the last state but all previous states deterministically. We use such a model, shown in Figure 1(c), that we name recurrent state-space model (RSSM),

<!-- chunk {"id": "body-0027", "role": "body", "section": "Deterministic path", "weight": 1.0} -->

where $f{(h_{t - 1},s_{t - 1},a_{t - 1})}$ is implemented as a recurrent neural network (RNN). Intuitively, we can understand this model as splitting the state into a stochastic part $s_{t}$ and a deterministic part $h_{t}$, which depend on the stochastic and deterministic parts at the previous time step through the RNN. We use the encoder ${q{({s_{1:T}{}_{1:T}},a_{1:T})}} = {\prod_{t = 1}^{T}{q{({s_{t}{}_{t}},o_{t})}}}$ to parameterize the approximate state posteriors. Importantly, all information about the observations must pass through the sampling step of the encoder to avoid a deterministic shortcut from inputs to reconstructions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Deterministic path", "weight": 1.0} -->

In the next section, we identify a limitation of the standard objective for latent sequence models and propose a generalization of it that improves long-term predictions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Latent Overshooting", "weight": 1.0} -->

In the previous section, we derived the typical variational bound for learning and inference in latent sequence models (Equation 3). As show in Figure 2(a), this objective function contains reconstruction terms for the observations and KL-divergence regularizers for the approximate posteriors. A limitation of this objective is that the stochastic path of the transition function $p{({s_{t}{}_{t - 1}},a_{t - 1})}$ is only trained via the KL-divergence regularizers for one-step predictions: the gradient flows through $p{({s_{t}{}_{t - 1}},a_{t - 1})}$ directly into $q{(s_{t - 1})}$ but never traverses a chain of multiple $p{({s_{t}{}_{t - 1}},a_{t - 1})}$. In this section, we generalize this variational bound to *latent overshooting*, which trains all multi-step predictions in latent space.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Latent Overshooting", "weight": 1.0} -->

We found that several dynamics models benefit from latent overshooting, although our final agent using the RSSM model does not require it (see Appendix D).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Limited capacity", "weight": 1.0} -->

If we could train our model to make perfect one-step predictions, it would also make perfect multi-step predictions, so this would not be a problem. However, when using a model with limited capacity and restricted distributional family, training the model only on one-step predictions until convergence does in general not coincide with the model that is best at multi-step predictions. For successful planning, we need accurate multi-step predictions. Therefore, we take inspiration from Amos et al. and earlier related ideas, and train the model on multi-step predictions of all distances. We develop this idea for latent sequence models, showing that multi-step predictions can be improved by a loss in latent space, without having to generate additional images.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Multi-step prediction", "weight": 1.0} -->

We start by generalizing the standard variational bound (Equation 3) from training one-step predictions to training multi-step predictions of a fixed distance $d$. For ease of notation, we omit actions in the conditioning set here; every distribution over $s_{t}$ is conditioned upon $a_{< t}$. We first define multi-step predictions, which are computed by repeatedly applying the transition model and integrating out the intermediate states,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Multi-step prediction", "weight": 1.0} -->

The case $d = 1$ recovers the one-step transitions used in the original model. Given this definition of a multi-step prediction, we generalize Equation 3 to the variational bound on the multi-step predictive distribution $p_{d}$,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Multi-step prediction", "weight": 1.0} -->

For the derivation, please see Equation 9 in the appendix. Maximizing this objective trains the multi-step predictive distribution. This reflects the fact that during planning, the model makes predictions without having access to all the preceding observations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Multi-step prediction", "weight": 1.0} -->

We conjecture that Equation 6 is also a lower bound on ${\ln p}{(o_{1:T})}$ based on the data processing inequality. Since the latent state sequence is Markovian, for $d \geq 1$ we have ${I{(s_{t};s_{t - d})}} \leq {I{(s_{t};s_{t - 1})}}$ and thus ${E{\lbrack{{\ln p_{d}}{(o_{1:T})}}\rbrack}} \leq {E{\lbrack{{\ln p}{(o_{1:T})}}\rbrack}}$. Hence, every bound on the multi-step predictive distribution is also a bound on the one-step predictive distribution in expectation over the data set. For details, please see Equation 10 in the appendix. In the next paragraph, we alleviate the limitation that a particular $p_{d}$ only trains predictions of one distance and arrive at our final objective.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Latent overshooting", "weight": 1.0} -->

We introduced a bound on predictions of a given distance $d$. However, for planning we need accurate predictions not just for a fixed distance but for all distances up to the planning horizon. We introduce latent overshooting for this, an objective function for latent sequence models that generalizes the standard variational bound (Equation 3) to train the model on multi-step predictions of all distances $1 \leq d \leq D$,

<!-- chunk {"id": "body-0037", "role": "body", "section": "Latent overshooting", "weight": 1.0} -->

Latent overshooting can be interpreted as a regularizer in latent space that encourages consistency between one-step and multi-step predictions, which we know should be equivalent in expectation over the data set. We include weighting factors ${\{\beta_{d}\}}_{d = 1}^{D}$ analogously to the $\beta$-VAE. While we set all $\beta_{> 1}$ to the same value for simplicity, they could be chosen to let the model focus more on long-term or short-term predictions. In practice, we stop gradients of the posterior distributions for overshooting distances $d > 1$, so that the multi-step predictions are trained towards the informed posteriors, but not the other way around.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate PlaNet on six continuous control tasks from pixels. We explore multiple design axes of the agent: the stochastic and deterministic paths in the dynamics model, iterative planning, and online experience collection. We refer to the appendix for hyper parameters (Appendix A) and additional experiments (Appendices D, E and C). Besides the action repeat, we use the same hyper parameters for all tasks. Within less than one hundredth the episodes, PlaNet outperforms A3C and achieves similar performance to the top model-free algorithm D4PG. The training time of 10 to 20 hours (depending on the task) on a single Nvidia V100 GPU compares favorably to that of A3C and D4PG. Our implementation uses TensorFlow Probability. Please visit for access to the code and videos of the trained agent.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

For our evaluation, we consider six image-based continuous control tasks of the DeepMind control suite, shown in LABEL:fig:domains. These environments provide qualitatively different challenges. The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area overlap, finger spinning includes contact dynamics between the finger and the object, cheetah exhibits larger state and action spaces, the cup task only has a sparse reward for when the ball is caught, and the walker is challenging because the robot first has to stand up and then walk, resulting in collisions with the ground that are difficult to predict. In all tasks, the only observations are third-person camera images of size $64 \times 64 \times 3$ pixels.

<!-- chunk {"id": "body-0040", "role": "body", "section": "One agent all tasks", "weight": 1.0} -->

Data efficiency gain PlaNet over D4PG (factor)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

We present PlaNet, a model-based agent that learns a latent dynamics model from image observations and chooses actions by fast planning in latent space. To enable accurate long-term predictions, we design a model with both stochastic and deterministic paths. We show that our agent succeeds at several continuous control tasks from image observations, reaching performance that is comparable to the best model-free algorithms while using $200 \times$ fewer episodes and similar or less computation time. The results show that learning latent dynamics models for planning in image domains is a promising approach.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models. To further improve final performance, one could learn a value function to approximate the sum of rewards beyond the planning horizon. Moreover, gradient-based planning could increase the computational efficiency of the agent and learning representations without reconstruction could help to solve tasks with higher visual diversity. Our work provides a starting point for multi-task control by sharing the dynamics model.
