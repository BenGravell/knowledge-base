## Introduction

Reinforcement Learning (RL) is a powerful set of methods for an agent to learn how to act optimally in a given environment to maximize some reward signal. In contrast to other methods such as dynamic programming, RL achieves this task of learning an optimal policy, which dictates the optimal behavior, via a trial-and-error process of interacting with the environment. Most early successful applications of RL use value-based methods (e.g., ), which estimate the expected future rewards to inform the agent's decisions. However, these methods only indirectly optimize the true objective of learning an optimal policy and are non-trivial to apply in settings with continuous action spaces.

In this work, we discuss policy gradient algorithms as an alternative approach, which aims to directly learn an optimal policy. Policy gradient algorithms are by no means new, but this subfield only gained traction in recent years following the emergence of deep RL with the development of various powerful algorithms (e.g., ). Deep RL is a subfield of RL, which uses neural networks and other deep learning methods. The increased interest in policy gradient algorithms is due to several appealing properties of this class of algorithms. They can be used natively in continuous action spaces without compromising the applicability to discrete spaces. In contrast to value-based methods, policy gradient algorithms inherently learn stochastic policies, which results in smoother search spaces and partly remedies the exploration problem of having to acquire knowledge about the environment in order to optimize the policy. In some settings, the optimal policy may also be stochastic itself. Lastly, policy gradient methods enable smoother changes in the policy during the learning process, which may result in better convergence properties.

Our goal is to present a holistic overview of policy gradient algorithms. In doing so, we limit the scope to on-policy algorithms, which we will define in Section 2. Thus, we exclude some popular algorithms including DDPG, TD3 and SAC. See Figure 1 for an overview of RL and the subfields we cover. Our contributions are as follows:

We give a comprehensive introduction to the theoretical foundations of policy gradient algorithms including a detailed proof of the continuous version of the Policy Gradient Theorem.

We derive and compare the most prominent policy gradient algorithms and provide high quality pseudocode to facilitate understanding.

We release competitive implementations of these algorithms, including the, to the best of our knowledge, first publicly available V-MPO implementation displaying performance on par with the results in the original paper.

Figure 1: Simplified taxonomy of RL algorithms. Subfields of RL we focus on are highlighted in gray.

The remainder of this paper is organized as follows. Section 2 introduces fundamental definitions in RL as well as an overview of deep learning. Section 3 derives the theoretical foundations of policy gradient algorithms with a special focus on proving the Policy Gradient Theorem, based on which we will construct several existing practical algorithms in Section 4. In Section 5, we discuss convergence results from literature. Section 6, presents the results of our numerical experiments comparing the discussed algorithms. Section 7 concludes.

## Preliminaries

In this section, we present prerequisites for subsequent chapters. Specifically, we introduce our notation in Section 2.1 and present overviews of RL in Section 2.2 and of deep learning in Section 2.3. Furthermore, we list several well-known definitions and results from probability theory, measure theory and analysis, which we use in our paper, in Appendix Appendix D.

### Notation

We denote the set of natural numbers by $\mathbb{N}$, natural numbers including zero by ${\mathbb{N}}_{0}$, real numbers by $\mathbb{R}$ and positive real numbers by ${\mathbb{R}}_{+}$. We denote $d$-dimensional real-numbered vector spaces as ${\mathbb{R}}^{d}$. By $\mathcal{P}{(\mathcal{A})}$, we denote the power set of a set $\mathcal{A}$. Where possible, we denote random variables with capital letters and their realizations with the corresponding lower case letters. For any probability measure $\mathbb{P}$, we denote the probability of an event $X = x$ as ${\mathbb{P}}{({X = x})}$. Similarly, we write ${\mathbb{P}}{({X = {x \mid Y} = y})}$ for conditional probabilities. When it is clear, which random variable is referred to, we regularly omit it to shorten notation, i.e. ${{\mathbb{P}}{({X = x})}} = {{\mathbb{P}}{(x)}}$. We identify measurable spaces $(\mathcal{A},\Sigma)$ just by the set $\mathcal{A}$ as we always use the respective power set $\mathcal{P}{(\mathcal{A})}$ for discrete sets and the Borel algebra for intervals in ${\mathbb{R}}^{d}$ as the respective $\sigma$-algebra $\Sigma$. We express most Lebesgue integrals w.r.t. the Lebesgue measure $\lambda$ using Theorem D.9. To simplify notation, we write integrals for measurable functions $f$ on $\mathcal{A}$ as ${\int_{a \in \mathcal{A}}{f{(a)}{da}}} ≔ {\int_{a \in \mathcal{A}}{f{(a)}{d\lambda}{(a)}}}$. We denote that a random variable $X$ follows a probability distribution $p$ by $X \sim p$. For any random variable $X \sim p$, we denote by ${\mathbb{E}}_{X \sim p}{\lbrack X\rbrack}$ and ${Var}_{X \sim p}{\lbrack X\rbrack}$ its expectation and variance. We denote the set of probability distributions over some measurable space $\mathcal{A}$ as $\Delta{(\mathcal{A})}$. We write $|\mathcal{A}|$ for the cardinality of a finite set $\mathcal{A}$ or area of a region $\int_{a \in \mathcal{A}}{da}$. For any variable or function $x$, we commonly denote approximations to it by $\hat{x}$.

### Reinforcement Learning

In the following, we formally describe the general problem setting encountered in RL, define fundamental functions and introduce the subfields of RL our work is further concerned with. Sections 2.2.1 and 2.2.2 are based on, Chapter 3.

### Problem Setting

Each problem instance in RL consists of an agent and an environment with which he interacts to achieve some specific goal. The environment comprises everything external to the agent and can be formalized as a Markov Decision Process (MDP). Let an action space $\mathcal{A}$ be the set of all actions the agent can take and let a state space $\mathcal{S}$ be the set of all possible states, i.e. snapshots of the environment at any given point in time. State and action spaces can be discrete or continuous^11^1Here, we call a state/action space continuous if it is an interval in ${\mathbb{R}}^{d}$ for $d \in {\mathbb{N}}$. and we assume both to be compact and measurable. We write an MDP as a tuple $\mathcal{M} = {(\mathcal{S},\mathcal{A},P,\gamma,p_{0})}$, where $P:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{({\mathcal{S} \times {\mathbb{R}}})}}}$ is the environment's transition function, which defines the probability^22^2Technically, this is the value of the probability density function for continuous distributions. However, we unify terminology by referring to the values of probability density functions as probabilities here and in the following. $P{(s^{\prime},{r \mid {s,a}})}$ of transitioning to a new environment state $s^{\prime}$ and receiving reward $r \in {\mathbb{R}}$ when the agent uses action $a$ in state $s$, $\gamma \in {\lbrack 0,1\rbrack}$ is a discount rate and $p_{0} \in {\Delta{(\mathcal{S})}}$ is a probability distribution over potential starting states. We assume rewards $r$ to be bounded. In the following, our notation assumes state and action spaces to be continuous.

We call sequences of states, actions and rewards $(s_{t},a_{t},r_{t + 1},s_{t + 1},a_{t + 1},r_{t + 2},\ldots,s_{{t + k} - 1},a_{{t + k} - 1},r_{t + k},s_{t + k})$ trajectories. A one-step trajectory, i.e. a tuple $(s_{t},a_{t},r_{t + 1},s_{t + 1})$ is called a transition. In this work, we limit ourselves to episodic settings, where the agent only interacts with the environment for a finite number of at most $T$ steps after which the environment is reset to a starting state. An episode may however be shorter than $T$ if a terminal state is reached. Therefore each episode consists of a trajectory $(s_{0},a_{0},r_{1},s_{1},a_{1},r_{2},\ldots,s_{\overset{\sim}{T} - 1},a_{\overset{\sim}{T} - 1},r_{\overset{\sim}{T}},s_{\overset{\sim}{T}})$, with $\overset{\sim}{T} \leq T$. Rewards are occasionally omitted from the trajectory notation since they do not influence future states. Correspondingly, we also can compute the alternative transition probabilities ${P{({s^{\prime} \mid {s,a}})}} = {\int_{r \in {\mathbb{R}}}{P{(s^{\prime},{r \mid {s,a}})}{dr}}}$.

The main goal in reinforcement learning is to solve the control problem of learning a policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ to maximize the expected return. The return $G_{t} ≔ {\sum_{k = 0}^{T}{\gamma^{k}r_{t + k + 1}}}$ is the discounted sum of rewards from timestep $t$ onwards. Note that $G_{t}$ is bounded since rewards are bounded. We denote the probability of taking action $a$ in state $s$ under policy $\pi$ with $\pi{({a \mid s})}$. For a policy $\pi$, its stationary state distribution $d^{\pi}$ determines the probability of being in a specific state $s \in \mathcal{S}$ at any point in time when following $\pi$.

Let $\Pi$ be the set of all possible policies. RL algorithms ${\mathfrak{A}}:{\Pi\rightarrow\Pi}$ for the control problem now iteratively learn policies by interacting with the environment using the current policy to sample transitions, which are then used to update the policy. We will discuss how these updates can look like in Section 2.2.3. A key characteristic of many RL problems is a necessary trade-off between exploration and exploitation in this learning process. The agent has no prior knowledge of the environment and thus needs to explore different transitions in order to learn which states and actions are desirable. As state and action spaces are typically large however, exploiting the already acquired knowledge about the environment is also crucial to guide the search process for an optimal policy to subspaces that hold most promise. A common approach to this exploration problem is to add noise to the policy.

### Value Functions

Based on the return, we define the value and action-value functions, which are fundamental in RL. The value function

gives the expected return from state $s$ onwards when following policy $\pi$, which selects all subsequent actions. Thus, the value function states how good it is to be in a specific state $s$ given a policy $\pi$. Note that here we follow the general convention to write this just as an expectation over $\pi$. However, it should be noted that this expectation integrates over all subsequent states and actions that are obtained by following policy $\pi$, i.e. Equation computes the expected return given that all subsequent actions are sampled from $\pi$ and all rewards and next states are sampled from $P$. This is implicit in our notation here as well as in further expectations.

Next, we define the action-value function

which differs from the value function in that the very first action $a$ is provided as an input to the function and not determined by the policy. We observe the following relation between $V_{\pi}$ and $Q_{\pi}$:

the advantage function, which determines how good an action $a$ is in state $s$ in relation to other possible actions.

From the definitions of $V_{\pi}$ and $Q_{\pi}$ we can derive the so-called Bellman equations. Starting from Equation, we use the definition of the return $G_{t}$, explicitly write out the expectation for the first transition and then apply the definition of $V_{\pi}$ again:

Thus, we find a formulation of the value function, which depends on the value of subsequent states. Collapsing the expectation again yields the form known as the Bellman equation of the value function:

Similarly, we can find the Bellman equation for the action-value function:

Now, we can formally define what optimality means in RL. An optimal policy $\pi^{\ast}$ is defined by ${V_{\pi^{\ast}}{(s)}} \geq {V_{\pi}{(s)}}$ for all states $s$ and policies $\pi$, i.e. any optimal policy maximizes the expected return. It can be shown that in every finite MDP, a deterministic optimal policy exists. All optimal policies share the same optimal value function ${V^{\ast}{(s)}} ≔ {{\max_{\pi \in \Pi}V_{\pi}}{(s)}}$ and optimal action-value function ${Q^{\ast}{(s,a)}} ≔ {{\max_{\pi \in \Pi}Q_{\pi}}{(s,a)}}$ and select actions $a \in {{{\arg\max}_{a^{\prime}}Q^{\ast}}{(s,a^{\prime})}}$ for every state. Applying this to Equation yields the Bellman optimality equation

We cite the following result without proof from on how to obtain an optimal policy, which we will revisit in Section 5.

### Theorem 2.1

(Generalized Policy Iteration) Let $\pi_{\text{old}}$ be the current policy. Then, Generalized Policy Iteration updates its policy by

for all $s \in \mathcal{S}$. Let $\left( \pi_{n} \right)_{n = 0}^{\infty}$ be a sequence of policies obtained through Generalized Policy Iteration. Then, this sequence converges to an optimal policy, i.e.

### On-Policy Policy Gradient Methods

Finally, we will delineate the subfields of RL on which our work focuses. In this context, we will successively introduce function approximation, policy gradient methods and the on-policy paradigm.

RL algorithms are mostly concerned with learning functions such as $\pi$, $V_{\pi}$ or $Q_{\pi}$. Early reinforcement methods learn exact representations of these by maintaining lookup tables with entries for each possible function input. While this approach yields theoretical convergence guarantees, it is practically very limited. Similar states are treated independently such that learnings do not generalize from one state to others while specific states are only rarely visited in large state spaces. Moreover, this approach is not applicable to continuous spaces. Function approximation remedies these shortcomings by parameterizing the function to be learned. Let $f_{\theta}{(x)}$ be this learnable function, where $\theta$ are the function's parameters, which are adjusted over the course of learning, and $x$ are the functions inputs such as states and actions or representations thereof. By choosing $f_{\theta}$ to be continuous in its inputs, we can ensure that $f_{\theta}$ generalizes across its inputs when we fit it to sampled transitions. $f_{\theta}$ can be as simple as a linear mapping, i.e. ${f_{\theta}{(x)}} = {\theta^{T}x}$, however recent works mostly use neural networks as function approximators (e.g., ). The field using neural networks as function approximators is coined deep RL. For the remainder of this paper, you can consider any learned function to be a neural network unless explicitly stated otherwise, although all our statements apply to any differentiable function approximators. We will introduce deep learning and neural networks in detail in Section 2.3.

Policy gradient methods pose an alternative to value-based methods in RL. Most early successes in RL use value-based methods such as Q-Learning or SARSA, that aim at learning a sequence of value functions converging to the optimal value function, from which an optimal policy can then be inferred. In contrast, policy-based RL, which we focus on in this work, directly learns a parameterized policy $\pi_{\theta}$. The main idea in this learning process is to increase the probability of those actions that lead to higher returns until we reach an (approximately) optimal policy. While this optimization problem can be approached in several ways, gradient-based methods are most commonly used. Following, we define policy gradient methods as follows.

### Definition 2.2

(Policy Gradient Algorithm) Let $\pi_{\theta}:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ be a fully differentiable function with learnable parameters $\theta \in {\mathbb{R}}^{d}$ mapping states to a probability distribution over actions. Let $J:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be some performance measure of the parameters. We call any learning algorithm a policy gradient algorithm if it learns its policy $\pi_{\theta}$ by updating $\theta$ via gradient ascent (or descent) on $J$, i.e. its updates have the general form

where $\alpha \in {\mathbb{R}}$ is a step size parameter of the algorithm.

In policy-based RL, two distinct ways exist to have the policy output a probability distribution over actions, from which actions can be sampled. For discrete action spaces, we construct a discrete distribution over the action space by normalizing the policies' raw outputs via a softmax function. In this case, we have

For continuous action spaces, we let $\pi_{\theta}$ output the mean $\mu$ and standard deviation $\sigma$ of a Gaussian distribution, i.e. ${\pi_{\theta}{(s)}} = \left( {\mu_{\theta}{(s)}},{\sigma_{\theta}{(s)}} \right)$ such that

This parameterization of a Gaussian distribution for the policy was first introduced by. As action spaces are commonly bounded, the actions sampled from such a Gaussian are typically transformed to be within these bounds either by clipping or by applying a squashing distribution. Further, we highlight that the policies learned by policy gradient methods in both the discrete and the continuous case are generally stochastic. This stands in contrast to value-based methods which generally learn deterministic policies. Policy gradient methods are the core focus of this paper and will be discussed in-depth in subsequent sections.

Lastly, we delineate on-policy from off-policy algorithms. In RL, we distinguish between behavior and target policies. A behavior policy is a policy which generates the data in form of trajectories from which we want to learn, i.e. this is the policy from which we sample actions when interacting with the environment. Conversely, the target policy is the policy which we want to learn about to evaluate how good it is in the given environment and improve it. Algorithms where behavior and target policy are not identical, e.g. Q-Learning or DQN, are referred to as off-policy algorithms. In this work, we only discuss on on-policy algorithms, where behavior and target policy are identical. Hence, when speaking of policy gradient algorithms in the following, we always implicitly mean on-policy policy gradient algorithms if not mentioned otherwise.

### Deep Learning

In this section, we introduce deep learning as a subfield of machine learning since its methods are commonly used in policy gradient algorithms. In recent years, deep learning has emerged as the premier machine learning method in various fields, enabling state-of-the-art performance in domains such as computer vision (e.g., ) and natural language processing (e.g.,. Following and, we define deep learning as a set of techniques to solve prediction tasks by learning multiple levels of representations from raw data using a composition of simple non-linear functions. This composition of functions, that we will describe in detail later, is referred to as (deep) neural network. Deep learning stands in contrast to conventional machine learning techniques like logistic regressions, which typically require hand-engineered representations as inputs to be effective. In the following, we introduce the general problem setting of deep learning using the notation of, formalize neural networks and describe how they are trained.

Consider measurable spaces $\mathcal{X}$ and $\mathcal{Y}$. $\mathcal{Z} ≔ {\mathcal{X} \times \mathcal{Y}}$ is the data space with each element $z = {(x,y)} \in \mathcal{Z}$ being a tuple of input features $x \in \mathcal{X}$ and a label $y \in \mathcal{Y}$. Let $\mathcal{M}{(\mathcal{X},\mathcal{Y})}$ be the set of measurable functions from $\mathcal{X}$ to $\mathcal{Y}$. The problems we encounter in deep learning are prediction tasks. Thus, the goal is to learn a mapping $f \in {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$ from inputs to labels by minimizing some loss function $\mathcal{L}$ over training data $S = {\{ z^{},\ldots,z^{(m)}\}}$ such that it generalizes to unseen data $z \in \mathcal{Z}$. To learn the function $f$, we first select a hypothesis set $\mathcal{F} \subset {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$. Deep learning then provides learning algorithms ${\mathfrak{A}}:{\mathcal{Z}\rightarrow\mathcal{F}}$ that use training data $S$ to learn the desired function $f = {{\mathfrak{A}}{(S)}}$. Before we discuss this learning process, we will first further characterize the mapping to be learned.

In deep learning, functions in the hypothesis set $\mathcal{F}$ represent instances of neural networks. Note that here we limit ourselves to feedforward networks, also called multilayer perceptrons (MLP), and will not discuss transformers, recurrent (RNN) or convolutional neural networks (CNN).

### Definition 2.3

(Feedforward Neural Network) A feedforward neural network $f:{\mathcal{X}\rightarrow\mathcal{Y}}$ is a composition of functions

that is differentiable almost everywhere. We refer to ${{f^{(i)},i} = 1},{\ldots,n}$ as hidden layers, whereas $f^{({n + 1})}$ is the non-hidden output layer. Consequently, $n$ denotes the number of of hidden layers in the network. Each hidden layer is characterized by a layer width $N_{i}$. Let $N_{0}$ and $N_{n + 1}$ further be the size of the input and output vectors respectively. Then, we can write each layer as

where $x$ is the output of the previous layer or the network's inputs for $i = 1$, $W^{(i)} \in {\mathbb{R}}^{N_{i} \times N_{i - 1}}$ and $b^{(i)} \in {\mathbb{R}}^{N_{i}}$ are the layer's weight matrix and bias vector respectively and $g:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is a differentiable activation function introducing non-linearity. $g$ is applied element-wise.

An MLP can be characterized by its architecture $a = \left( {(N_{i})}_{i = 0}^{n + 1},g \right)$, consisting of layer sizes and the activation function to be used. The number of layers $n + 1$ is also referred to as the depth of the network. The Universal Approximation Theorem underpins the expressivity of neural networks: a two-layer network can already approximate any measurable function arbitrarily well under weak conditions on the activation function. Technically, each layer can feature a different activation function albeit this is uncommon. The activation function of the output layer is not defined by the architecture $a$ but is derived from the prediction task. The standard choice for activation functions in the hidden layers is a rectified linear unit (ReLU)^33^3Note that the ReLU function is not differentiable at 0. In practice, this is circumvented by using its sub-derivatives., due to typically fast learning. See for an overview of other commonly used activation functions. The output layer typically uses no activation function for regression tasks and sigmoid or softmax functions for classification tasks. Each element of a layer $f^{(i)}$ is called a neuron. The outputs $a^{(i)} = {\left( {f^{(i)} \circ \cdots \circ f^{}} \right){(x)}}$ of any layer are the learned representations of the inputs $x$. We denote the outputs $f{(x)}$, i.e. the predictions, of the neural network with $\hat{y}$. Figure 2 depicts a neural network as an acyclic directed graph.

Figure 2: A neural network with hidden layers of sizes 5 and 4 as a directed graph.

Selecting a hypothesis set $\mathcal{F}$ is done implicitly by specifying an architecture $a$. Hence, we denote the hypothesis set for architecture $a$, whose elements are all MLPs with that architecture, by $\mathcal{F}_{a}$. The MLPs in $\mathcal{F}_{a}$ therefore differ only in their weights and biases. We call these the (learnable) parameters of the network and typically collect them in a flattened parameter vector $\theta \in {\mathbb{R}}^{d}$. We denote an MLP with parameters $\theta$ as $f_{\theta}$.

Given a hypothesis set $\mathcal{F}_{a}$, we now aim to learn a neural network $f_{\theta} \in \mathcal{F}_{a}$, i.e. to learn parameters $\theta$, such that we reduce the expected loss or risk,

over the data distribution ${\mathbb{P}}_{Z}$ for some appropriately chosen differentiable loss function $\mathcal{L}:{{\mathcal{F} \times \mathcal{Z}}\rightarrow{\mathbb{R}}}$. Here ${\mathbb{P}}_{Z}$ is the image measure of $Z$ on $\mathcal{Z}$, from which the training data $S = {\{ z^{},\ldots,z^{(m)}\}}$ and unknown out-of-sample data $z$ is drawn. We generally assume that training $z^{},\ldots,z^{(m)}$ and out-of-sample data $z$ are realizations of i.i.d. random variables ${Z^{},\ldots,Z^{(m)},Z} \sim {\mathbb{P}}_{Z}$. For a given MLP $f_{\theta} = {{\mathfrak{A}}{(S)}}$ trained on $S$, the risk becomes ${\mathcal{R}{(f_{\theta})}} = {{\mathbb{E}}_{Z \sim {\mathbb{P}}_{Z}}\left\lbrack {{\mathcal{L}{(f_{\theta},Z)}} \mid S} \right\rbrack}$. In practice, noisy data results in a positive lower bound on risk, i.e. an irreducible error. Common loss functions are binary cross-entropy loss,

for (binary) classification and mean squared error (MSE),

for regression tasks. Sometimes, loss functions are augmented by regularization terms $\Omega{(\theta)}$ such as an L2-penalty of the parameters, i.e. $\beta{\parallel\theta\parallel}_{2}^{2}$ with $\beta \in {\mathbb{R}}$.

The data distribution ${\mathbb{P}}_{Z}$ is generally unknown. Hence, we replace it by an empirical distribution based on the sampled training data $S$ and use empirical risk minimization (ERM) as the learning algorithm to minimize it.

### Definition 2.4

(Empirical Risk). Given training data $S = {\{ z^{},\ldots,z^{(m)}\}}$ and a function $f_{\theta} \in {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$, the empirical risk is defined by

### Definition 2.5

(ERM learning algorithm). Given hypothesis set $\mathcal{F}_{a}$ and training data $S$, an empirical risk minimization algorithm ${\mathfrak{A}}^{erm}$ terminates with an (approximate^44^4In practice, the empirical risk is generally highly non-convex prohibiting guaranteed convergence to a global minimum.) minimizer ${\hat{f}}_{S} \in \mathcal{F}_{a}$ of empirical risk:

We approximately minimize empirical risk typically via gradient-based methods due to efficient computation of point-wise derivatives via the backpropagation algorithm. Backpropagation means the practical application of the chain rule to neural networks. The gradient of the objective function $\mathcal{L}$ with respects to the $i$-th layer's inputs $a^{({i - 1})}$ can be computed by working backwards from the gradient with respects to the layer's outputs $a^{(i)}$ as ${\nabla_{a^{({i - 1})}}\mathcal{L}} = {\sum_{j}{{({\nabla_{a^{({i - 1})}}a_{j}^{(i)}})}\frac{\partial\mathcal{L}}{\partial a_{j}^{(i)}}}}$. From these gradients, the gradients with respects to the weights and biases in each layer can be calculated similarly. Due to this flow of information from the objective function to each of the layers, the optimization of MLPs is also referred to as backwards pass, in contrast to the forward pass of calculating $\hat{y} = {f{(x)}}$. The full backpropagation algorithm for MLPs is formulated in Algorithm 1.

labels y, regularizer Ω (θ), network outputs ŷ, activated and unactivated layer outputs a(k) and h(k) for k = 1, …, n, activation function g, loss ℒ
δ ← ∇h(k)ℒ = δ ⊙ g′ (h(k)) ⊳ hadamard product if g is element-wise
Algorithm 1 Backpropagation, pseudocode taken from

The gradients computed via backpropagation are used to update the parameters in each layer using gradient descent. However, due to the prohibitive computational costs of evaluating the expectation in Equation, computing gradients only on a subset of the training data is generally preferred and typically also results in faster convergence. At each iteration, a batch $S^{\prime}$ of data with size $m^{\prime} \leq m$ (typically $m^{\prime} \ll m$) is randomly sampled from the training data to conduct the update

Here, $\Theta$ is a random variable whose realizations are neural network parameters $\theta$. $\alpha_{k}$ is the step size or learning rate on the k-th optimization step. The learning rate is commonly decayed over the training process to help convergence. The procedure using updates as in Equation is known as stochastic (minibatch) gradient descent (SGD)^55^5Sometimes SGD refers to updates which only involve a single data point. We however follow the nowadays common terminology of calling any sample-based gradient descent stochastic. and dates back to. Using SGD has the additional benefit of introducing random fluctuations which enable escaping saddle points. SGD in its general form is depicted in Algorithm 2, where in our context ${r{(\theta)}} = {{\hat{\mathcal{R}}}_{S}{(f_{\theta})}}$. The neural network parameters $\theta$ are set to be the realization of the final $\Theta^{(K)}$ or a convex combination of $\left( \Theta^{(k)} \right)_{k = 1}^{K}$.

Differentiable function r: ℝd → ℝ, step sizes αk ∈ (0,∞), k = 1, …, K, ℝd-valued random variable Θ
Let Dk be a random variable such that 𝔼 [D(k)∣Θ(k−1)] = ∇r (Θ(k−1))
Algorithm 2 Stochastic Gradient Descent, pseudocode from

Despite the stochasticity of SGD and highly non-convex loss landscapes, SGD's convergence can be guaranteed in some regimes, and it exhibits strong performance in practice. Hence, SGD and its variants are the default choice to optimize neural networks. The most prominently used variant is Adam, which uses momentum and an adaptive scaling of gradients to stabilize learning. Nonetheless, the initialization of $\theta$ is also important for convergence. Biases are commonly initialized to 0 whereas weights are randomly initialized close to 0 using various strategies. Finally, note that regardless of the non-convexity of the loss landscapes, local minima are not considered problematic if the neural networks are large enough

In practice, the training of neural networks is an iterative process. We alternate between choosing the network architecture $a$ as well as further hyperparameters of the learning algorithm such as the learning rates $\alpha$, and approximately minimizing the empirical risk for this set of hyperparameters. This is generally a trial-and-error process to find a suitable set of hyperparameters to maximize generalization performance, i.e. to minimize risk. To approximate risk, the trained models are typically evaluated by the empirical risk on a held-out test data set, which was not seen during training. The achieved empirical risk can be decomposed into a generalization error, an optimization error, an approximation error and the irreducible error. The generalization error is the difference between empirical and actual risk stemming from the random sampling of training data, which may not be representative of the actual data distribution ${\mathbb{P}}_{Z}$. The optimization error is the result of potentially not finding a global mimimum during the learning process. The approximation error is the difference between the minimum achievable risk over functions in $\mathcal{F}_{a}$ and over all $f \in {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$.

## Theoretical Foundations of Policy Gradients

Having introduced the fundamentals of deep RL, we can now discuss policy gradient algorithms in detail. In this section, we derive their theoretical foundations. Our main focus is going to be the Policy Gradient Theorem, on which all policy gradient algorithms build. This theorem will be discussed in Section 3.1. Furthermore, Sections 3.2 and 3.3 introduce the theoretical justifications for additional methods that are frequently used in policy gradient algorithms.

### Policy Gradient Theorem

Given an MDP $\mathcal{M} = {(\mathcal{S},\mathcal{A},P,\gamma,p_{0})}$, consider a parameterized policy $\pi_{\theta}$, which is differentiable almost everywhere, and the following objective function $J$ for maximizing the expected episodic return:

The idea of policy gradient algorithms is to maximize $J{(\theta)}$ over the parameters $\theta$ by performing gradient ascent. Hence, we require the gradients ${\nabla_{\theta}J}{(\theta)}$, however it is a priori not obvious how the right-hand side ${\mathbb{E}}_{S_{0} \sim {p_{0},\pi_{\theta}}}\left\lbrack G_{0} \right\rbrack$ depends on $\theta$ as changes in the policy $\pi$ also affect the state distribution $d^{\pi}$. The Policy Gradient Theorem yields an analytic form of ${\nabla_{\theta}J}{(\theta)}$ from which we can sample gradients that does not involve the derivative of $d^{\pi}$. Here, we focus on the undiscounted case, i.e. $\gamma = 1$. Note that any discounted problem instance can be reduced to the undiscounted case by letting the reward function absorb the discount factor.

### Theorem 3.1

(Policy Gradient Theorem) For a given MDP, let $\pi_{\theta}$ be differentiable w.r.t. $\theta$ and $\nabla_{\theta}\pi_{\theta}$ be bounded, let $Q_{\pi_{\theta}}$ be differentiable w.r.t. $\theta$ and $\nabla_{\theta}Q_{\pi_{\theta}}$ be bounded for all $s \in \mathcal{S}$ and $a \in \mathcal{A}$. Then, there exists a constant $\eta$ such that

### Proof

We largely follow the proof by albeit in a more detailed form and extended to continuous state and action spaces. To enhance readability, we omit subscripts $\theta$ for the policy $\pi$ and all gradients $\nabla$ but both always depend on the parameters $\theta$.

Starting from the definition of the objective function, we explicitly write out the expectation over starting states, use the relationship between value and action-value function, ${{V_{\pi}{(s)}} = {\int_{a \in \mathcal{A}}{\pi{({a \mid s})}Q_{\pi}{(s,a)}{da}}}},$ and differentiate by parts.

Note that in the last step via used the Leibniz integral rule (Theorem D.10) to swap the order of integration and differentiation prior to applying the product rule. The conditions for Leibniz are satisfied since $\pi{( \cdot \mid s)}Q_{\pi}{(s, \cdot )}$ is integrable for any $s \in \mathcal{S}$ and its partial derivatives exist and are bounded for all $s \in \mathcal{S}$ and $a \in \mathcal{A}$ since $\pi$ and $Q_{\pi}$ are bounded and $\nabla Q_{\pi}$ and $\nabla\pi$ exist and are bounded by assumption.

Now, consider the recursive formulation of the action-value function

Due to the identity ${\int_{r \in {\mathbb{R}}}{P{(s^{\prime},{r \mid {s,a}})}{dr}}} = {P{({s^{\prime} \mid {s,a}})}}$ and since realized rewards $r$ and environment transitions for a given action no longer depend on the policy, we can reformulate the gradients of $Q_{\pi}$ w.r.t. $\theta$, again using the Leibniz integral rule.

Further, note that for all $s \in \mathcal{S}$

which is equivalent to the inner expression in Equation. By using and, we can transform into a recursive form, which we are then going to unroll subsequently to yield an explicit form. In the following, we simply notation by defining

Applying and to in order and rearranging the integrals gives

In the final step, we switched the order of integration using Fubini's Theorem (Theorem D.11), which is applicable since $\nabla V_{\pi}$ is bounded and $\pi{( \cdot \mid s)}P{( \cdot \mid s, \cdot )}$ is a probability measure on $\mathcal{S} \times \mathcal{A}$ such that $|\pi{( \cdot \mid s)}P{( \cdot \mid s, \cdot )}\nabla V_{\pi}|$ is integrable over the product space $\mathcal{S} \times \mathcal{A}$. To unroll Equation across time, we introduce notation for multi-step transition probabilities. Let $\rho_{\pi}{({s\rightarrow{s^{\prime},k}})}$ be the probability of transitioning from state $s$ to $s^{\prime}$ after $k$ steps under policy $\pi$. We have that

and ${\rho_{\pi}{({s\rightarrow{s^{\prime},1}})}} ≔ {\int_{a \in \mathcal{A}}{\pi{({a \mid s})}P{({s^{\prime} \mid {s,a}})}{da}}}$. Now, we can recursively write

Using this notation, iteratively substituting in and and applying Fubini, we can unroll:

We set ${\eta_{s}{(s^{\prime})}} ≔ {\sum_{t = 0}^{T}{\rho_{\pi}{({s\rightarrow{s^{\prime},t}})}}}$, rearrange the integrals and multiply by 1 to obtain

In the final step, we used the identity

which can be seen as $\eta_{s}{(s^{\prime})}$ is the accumulate sum over probabilities of reaching $s^{\prime}$ after any number of steps for a given starting state. Integrating over the starting state distribution and normalizing hence yields the probability of visiting state $s^{\prime}$ and thereby the stationary distribution $d^{\pi}$ over states under the current policy.

Finally, we can derive the canonical form of the Policy Gradient Theorem from by using the definition of $\phi{(s)}$, setting

and multiplying with 1:

The Policy Gradient Theorem provides us with an explicit form of the policy gradients from which we can sample gradients. This allows the use of gradient-based optimization to directly optimize the policy using the methods presented in Section 2.3. Thus, the theorem serves as the foundation for the policy gradient algorithms which we will discuss in Section 4.

We conclude this section with some further remarks on Equation. First, we note that for any starting state $s \in \mathcal{S}$, we have that

which is the average episode length^66^6Note that ${\rho_{\pi}{({s_{t}\rightarrow{s_{t + 1},1}})}} = 0$ if the episode already terminated due to reaching a terminal state on any previous step. under policy $\pi$. Second, the use of gradient-based methods makes it sufficient to sample gradients which are only proportional to the actual gradients since any constant of proportionality can be absorbed by the learning rate parameter of the optimization algorithms. Hence, $\eta$ is commonly omitted, i.e.

We observe that all terms on the right hand side are known or can be estimated via sampling.

### Value Function Estimation with Baselines

In practice, the resulting estimates of the policy gradients can become very noisy when sampling from Equation. Therefore, a main practical challenge of policy gradient algorithms is to introduce measures to reduce the variance of the gradients while keeping the bias low. In this context, a well-known and widely used technique is to use a baseline when sampling an estimate of the action-value function $Q_{\pi}$. In this section, we show that using an appropriately chosen baseline does not bias the estimate but can greatly reduce the variance of the sampled gradients.

Let $\hat{Q}{(s,a)}$ be a sampled estimate of $Q_{\pi}{(s,a)}$, assuming ${{\mathbb{E}}\left\lbrack {\hat{Q}{(s,a)}} \right\rbrack} = {Q_{\pi}{(s,a)}}$. Then, we can construct a new estimator ${\hat{Q}}_{b}{(s,a)}$ by subtracting some baseline $b:{\mathcal{S}\rightarrow{\mathbb{R}}}$, i.e. ${{\hat{Q}}_{b}{(s,a)}} = {{\hat{Q}{(s,a)}} - {b{(s)}}}$. Our only condition towards $b$ is that it does not depend on the action $a$, though it can depend on the state $s$ and even be a random variable. Our sampled estimate of the gradient ${\nabla_{\theta}J}{(\theta)}$ becomes

In expectation over the policy $\pi$, this yields

using the linearity of the expectation. Now, we show that the second part is 0. Using the Leibniz integral rule, we have that

since $\pi{( \cdot \mid s)}$ is a probability distribution over actions. Thus, subtracting an action-independent baseline $b$ from an action-value function estimator $\hat{Q}$ does indeed not add any bias to the gradient estimate. While here we have shown this for a baseline which only depends on the current state, this result can be extended to baselines which depend on the current and all subsequent states.

Next, we analyze the effect on the variance of the gradient estimates. Here, we only provide an approximate explanation, see for a more thorough analysis which derives bounds of the true variance. We can compute the variance using ${{Var}{\lbrack X\rbrack}} = {{{\mathbb{E}}{\lbrack X^{2}\rbrack}} - {{\mathbb{E}}{\lbrack X\rbrack}^{2}}}$. Due to the above, ${\mathbb{E}}{\lbrack X\rbrack}^{2}$ is independent of the baseline in our case. This yields

where we approximated the variance by assuming independence of the two terms in the second step. Under this approximation, the variance of sampled gradients can be minimized by minimizing ${\mathbb{E}}_{\pi}\left\lbrack \left( {{\hat{Q}{(S,A)}} - {b{(S)}}} \right)^{2} \right\rbrack$. This is a common least squares problem resulting in the optimal choice of ${b{(s)}} = {{\mathbb{E}}_{\pi}{\lbrack{\hat{Q}{(s,A)}}\rbrack}}$ (see Theorem D.8). This result indicates that an appropriately chosen baseline can potentially significantly reduce variance of the gradients. Using this choice for the baseline, we would like to compute gradients for sampled states and actions as

Here, we used the relation of the value function $V_{\pi}$ to $Q_{\pi}$ and the definition of the advantage function $A_{\pi}$. Despite our approximations, this choice of a baseline turns out to yield almost the lowest possible variance of the gradients. However, note that in practice the advantage function must also be estimated. Learning this estimate typically introduces bias.

### Importance Sampling

Importance sampling is a technique to calculate expectations under one distribution given samples from another. Traditionally, this is only needed in off-policy RL, where we sample transitions using a behavior policy $\beta$ but want to calculate expectations over the target policy $\pi$. However, in some implementations of on-policy algorithms the policy may be updated before all data generated by it is processed. This makes these implementations slightly off-policy and thus importance sampling becomes relevant even for theoretically on-policy algorithms. We build our presentation of importance sampling on, Section 5.5.

Given a behavior policy $\beta$, we want to estimate the value function $V_{\pi}$ of our target policy $\pi$. Generally, we have

We can calculate the probability of a trajectory $(a_{t},s_{t + 1},a_{t + 1},\ldots,a_{T - 1},s_{T})$ under any policy $\pi$ as

Now, we can define the importance sampling ratio.

### Definition 3.2

(Importance Sampling Ratio) Given a target policy $\pi$, a behavior policy $\beta$ and a trajectory $\tau = {(a_{t},s_{t + 1},a_{t + 1},\ldots,s_{T})}$ generated by $\beta$, the importance sampling ratio is defined as

Let $\mathcal{T}$ be the set of possible trajectories. By multiplying returns of trajectories $\tau \in \mathcal{T}$ generated by the behavior policy $\beta$ with the importance sampling ratio $\rho$ we get

The intuition behind this importance sampling correction is that, to evaluate $\pi$, we want to weigh returns more heavily that are more likely under $\pi$ than under $\beta$ and vice versa. As an extension of the derivation above, we also get the per-decision importance sampling ratio $\rho ≔ \frac{\pi{({a \mid s})}}{\beta{({a \mid s})}}$.

Using importance sampling, we can derive the following approximate policy gradients of the target policy $\pi_{\theta}$ in an off-policy setting with behavior policy $\beta$:

See for a proof. Note that $\eta$ now is the average episode length under $\beta$.

## Policy Gradient Algorithms

Building on Theorem Theorem 3.1, several policy gradient algorithms have been proposed, which compute sample-based estimates ${\hat{\nabla}}_{\theta}J{(\theta)}$ of the actual policy gradients ${\nabla_{\theta}J}{(\theta)}$. This is done by constructing surrogate objectives $J_{\ast}$ such that ${{\hat{\nabla}}_{\theta}J{(\theta)}} = {{\nabla_{\theta}J_{\ast}}{(\theta)}}$. Additionally, most algorithms focus on stabilizing learning by regularizing the policy and reducing the variance of ${\hat{\nabla}}_{\theta}J{(\theta)}$. In this section, we derive the most prominent^77^7As determined by their impact on subsequent research and the adoption rate by users. algorithms before than comparing them in the final subsection.

### REINFORCE

REINFORCE (REward Increment = Non-negative Factor $\times$ Offset Reinforcement $\times$ Characteristic Eligibility) is the earliest policy gradient algorithm. While this algorithm precedes the formulation of the Policy Gradient Theorem, REINFORCE can be seen as a straightforward application of it. By using Monte Carlo methods to estimate $Q_{\pi}$ in Equation, i.e. by sampling entire episodes to compute the sample returns $G_{t} = {\sum_{k = 0}^{T}{\gamma^{k}r_{t + k + 1}}}$, REINFORCE samples policy gradients

Using the generic policy gradient update from Equation results in the gradient ascend updates

where $\alpha \in {(0,1\rbrack}$ is the learning rate determining the step size of the gradient steps and is set as a hyperparameter. At times, REINFORCE is extended by subtracting some baseline value from $G_{t}$ to reduce variance. The pseudocode for REINFORCE is presented in Algorithm 3.

for all episodes do
Generate trajectory s0, a0, r1, s1 …, sT under policy πθ
$G_{t}\leftarrow{\sum_{k = t}^{T}{\gamma^{k - t}r_{k}}}$ ⊳ estimate expected return Qπ
θ ← θ + α Gt ∇θln πθ (at∣st) ⊳ update policy parameters

### A3C

Instead of estimating $Q_{\pi}$ directly via sampling as in REINFORCE, we can alternatively learn such an estimate via function approximation. Algorithms that use this approach to learn a parameterized action-value function ${\hat{Q}}_{\phi}$ or value function ${\hat{V}}_{\phi}$ (called critic) with parameters $\phi$ in addition to learning the parameterized policy $\pi_{\theta}$ (called actor) are referred to as actor-critic algorithms. Note that in practice the actor and the critic may also share parameters.

The most archetypical representative of this class of algorithms is Asynchronous Advantage Actor-Critic (A3C). A3C builds on two main ideas from which the algorithm's name originates. First, as suggested by the results from Section 3.2, A3C learns an estimate ${\hat{A}}_{\phi}$ of the advantage function indirectly by learning an estimate ${\hat{V}}_{\phi}$ of the value function. Second, A3C introduces the concept of using multiple parallel actors to interact with the environment to stabilize training. We will discuss both ideas in detail below. The algorithm samples policy gradients

where $\mathcal{D}$ is a batch of transitions collected by the actors. The pseudocode for A3C is presented in Algorithm 4.

In the original work, the advantage function is estimated via

To understand this estimate, observe that

for any $k \in {\mathbb{N}}$, which follows from the definition of the value and action-value functions as well as their relationship. Sampling this n-step temporal difference expression and replacing $V_{\pi}$ with our learned ${\hat{V}}_{\phi}$ yields Equation. Simultaneously to updating $\pi_{\theta}$, we learn ${\hat{V}}_{\phi}$ by minimizing the mean squared error loss

over $\phi$ via SGD. Note that the inner expression is identical to the right hand side in Equation. In Equation, we compute the difference between the estimated return when choosing action $a_{t}$ in state $s_{t}$ and the estimated return when in state $s_{t}$, under policy $\pi$ respectively. However, $a_{t}$ is sampled from $\pi$ such that in expectation this difference should be 0 for the true value function $V_{\pi}$. Hence, we minimize this squared difference to optimize $\phi$ by treating the first term, $\sum_{i = 0}^{k - 1}\left( {{\gamma^{i}r_{t + i}} + {{\hat{V}}_{\phi}{(s_{t + k})}}} \right)$, as independent of $\phi$.

The use of multiple parallel actors is justified as follows. Deep RL is notoriously unstable, which was first resolved by off-policy algorithms using replay buffers that store and reuse sampled transitions for multiple updates. As an alternative, propose using several actors $\pi_{\theta}^{},\ldots,\pi_{\theta}^{(k)}$ to decrease noise by accumulating the gradients over multiple trajectories. These accumulated gradients are applied to a centrally maintained copy of $\theta$, which is then redistributed to each actor. By doing this asynchronously, each actor has a potentially unique set of parameters at any point in time compared to the other actors. This decreases the correlation of the sampled trajectories across actors, which can further stabilize learning.

Initialize θ and ϕ at random
θ(i) ← θ, ϕ(i) ← ϕ ⊳ synchronize parameters on actors
st ∼ p0 ⊳ sample start state
while st not terminal and t − tstart ≤ tMAX do
st + 1, rt + 1 ∼ P (st,at) ⊳ sample next state and reward
$R\leftarrow\begin{cases}
0 &amp; {\text{if~}s_{t}\text{~is terminal}} \\
{V_{\phi^{(i)}}{(s_{t})}} &amp; \text{else}
\end{cases}$ ⊳ bootstrap if necessary
update θ and ϕ using d θ and d ϕ via gradient ascent / descent

As a final implementation detail, the policy loss function of A3C, from which the policy gradients are obtained, is typically augmented with an entropy bonus for the policy. Thus, the policy gradients become

where $H$ is the entropy (see Definition D.4) and the entropy coefficient $\beta$ is a hyperparameter. This entropy bonus, first proposed by, regularizes the policy such that it does not prematurely converges to a suboptimal policy. By rewarding entropy, the policy is encouraged to spread probability mass over actions which improves exploration.

### TRPO

Excessively large changes in the policy can result in instabilities during the training of RL algorithms. Even small changes in policy parameters $\theta$ can lead to significant changes in the resulting policy and its performance. Hence, small step sizes during gradient ascent cannot fully remedy this problem and would impair the sample efficiency of the algorithm. Trust Region Policy Optimization (TRPO) mitigates these issues by imposing a trust region constraint on the Kullback-Leibler (KL) divergence (see Definition D.5) between consecutive policies. In addition, TRPO uses an off-policy correction through importance sampling as discussed in Section 3.3 to account for the interleaved optimization and collection of transitions.

TRPO samples gradients

and postprocesses them as detailed below to solve the approximate trust region optimization problem

where $\pi_{\text{old}} = \pi_{\theta_{\text{old}}}$ is the previous policy and $\theta_{\text{old}}$ the corresponding parameters. This optimization problem is an approximation to an objective with convergence guarantees, which we will show in the following. We start by presenting 's main theoretical result. Consider the objective of maximizing the expected return ${\mathbb{E}}_{S_{0} \sim {p_{0},\pi}}\left\lbrack G_{0} \right\rbrack$ under policy $\pi$, which we denote as $\eta{(\pi)}$ here. Let $L_{\pi}$ be the following local approximation of $\eta$:

with ${L_{\pi_{\theta}}{(\pi_{\theta})}} = {\eta{(\pi_{\theta})}}$ and ${{{\nabla_{\theta}L_{\pi_{\theta_{0}}}}{(\pi_{\theta})}}|}_{\theta = \theta_{0}} = {{{\nabla_{\theta}\eta}{(\pi_{\theta})}}|}_{\theta = \theta_{0}}$. Based on the total variation divergence $D_{TV}$ (see Definition D.6), we define

### Theorem 4.1

Let $\alpha = {D_{TV}^{max}{(\pi_{\text{old}},\pi_{\text{new}})}}$, then

where $\varepsilon = {\max_{{s \in \mathcal{S}},{a \in \mathcal{A}}}{|{A_{\pi}{(s,a)}}|}}$.

See the appendix in for a proof. By using the relationship between total variation divergence and KL divergence ${D_{TV}{({\pi \parallel \overset{\sim}{\pi}})}^{2}} \leq {D_{KL}{({\pi \parallel \overset{\sim}{\pi}})}}$ and setting $D_{KL}^{max}{(\pi,\overset{\sim}{\pi})} ≔ \max_{s \in \mathcal{S}}D_{KL}{(\pi{( \cdot \mid s)} \parallel \overset{\sim}{\pi}{( \cdot \mid s)})}$ and $C = \frac{4\varepsilon\gamma}{{({1 - \gamma})}^{2}}$, we derive the following lower bound for the objective from Equation:

Iteratively maximizing the right-hand side yields a sequence of policies $\pi_{i},\pi_{i + 1},\pi_{i + 2},\ldots$ with the monotonic improvement guarantee ${\eta{(\pi_{i})}} \leq {\eta{(\pi_{i + 1})}} \leq {\eta{(\pi_{i + 2})}} \leq \ldots$. This is because we have equality in for $\pi_{\text{new}} = \pi_{\text{old}}$ and hence

which is non-negative as we maximize over $\pi$ each iteration. Thus, we could construct a Minorization-Maximization-type algorithm which maximizes the right-hand side of Inequality at each iteration and is thereby guaranteed to converge to an optimum as the objective is bounded.

Such an algorithm would be impractical as it requires evaluating the advantage function at every point in the state-action product space $\mathcal{S} \times \mathcal{A}$ and the KL penalty at every point in the state space $\mathcal{S}$. Hence, apply several approximations to the objective stemming from Inequality. We replace the KL penalty, which would yield restrictively small step sizes given by $C$, by a trust region constraint:

To avoid computing $D_{KL}^{\text{max}}$, we use the average KL divergence

between policies as heuristic constraint, which we can sample. Further, we rewrite the surrogate objective ${\max_{\theta}L_{\pi_{\text{old}}}}{(\pi_{\theta})}$ as an expectation over the old policy $\pi_{\text{old}}$ via importance sampling. Note that $\eta{(\pi_{\text{old}})}$ is a constant w.r.t $\theta$:

Using these modifications, we are now left with solving the trust region problem

To approximately solve this constrained problem, use backtracking line search, where the search direction is computed by Taylor-expanding (see Theorem D.12) the objective function and the constraint. Let $g = {{\nabla_{\theta}{\mathbb{E}}_{{S \sim d^{\pi_{\text{old}}}},{A \sim \pi_{\text{old}}}}}\left\lbrack {\frac{\pi_{\theta}{({A \mid S})}}{\pi_{\text{old}}{({A \mid S})}}A_{\pi_{\text{old}}}{(S,A)}} \right\rbrack}$. Approximating $L_{\pi_{\text{old}}}{(\pi_{\theta})}$ to first order around $\theta_{\text{old}}$ yields

where we again ignored the constant $\eta{(\pi_{\text{old}})}$. The quadratic approximation of the constraint at $\theta_{\text{old}}$ is

where $H$ is the Fisher information matrix, which is estimated via

albeit the full matrix is not required. We solve the resulting approximate optimization problem analytically using Lagrangian duality methods leading to

However, due to the Taylor approximations, this solution may not satisfy the original trust region constraint or may not improve the surrogate objective of Problem. Therefore, TRPO employs backtracking line search along the search direction $H^{- 1}g$ with search parameter $\beta \in {}$:

We choose the exponent $m$ as the smallest non-negative integer such that the trust region constraint is satisfied and the surrogate objective improves. We circumvent the computationally expensive matrix inversion of $H$ for the search direction $d \approx {H^{- 1}g}$ by computing $d$ via the conjugate gradient algorithm. To further reduce the computational costs, the Fisher-vector products in this process can also be only calculated on a subset of the dataset $\mathcal{D}$ of sampled transitions.

Initialize θ and ϕ at random
s, r ∼ P (s,a) ⊳ sample next state and reward
for all epochs do
Compute returns R and advantages A
$g\leftarrow{\frac{1}{|\mathcal{D}|}{\sum_{\mathcal{D}}{\nabla_{\theta}{\frac{\pi_{\theta}{({a \mid s})}}{\beta{({a \mid s})}}A}}}}$
Compute Ĥ as the Hessian of the sample average KL-divergence
Compute d ≈ Ĥ−1 g via conjugate gradient algorithm
$\theta\leftarrow{\theta_{\text{old}} + {b^{m}\sqrt{\frac{2\delta}{d^{\mathsf{T}}\hat{H}d}}d}}$
until (sample loss improves and KL constraint satisfied) or m &gt; K
$d\phi\leftarrow\frac{1}{|\mathcal{D}|}\sum_{\mathcal{D}}\nabla_{\phi}{(R - V_{\phi}{(s)})}^{2}$
Update ϕ using d ϕ via gradient descent

do not specify an advantage estimator to be used in TRPO. The algorithm is commonly used with either the estimator used by A3C or the one which we present in the next subsection. TRPO is typically used with multiple parallel actors as A3C. The pseudocode for TRPO is presented in Algorithm 5. We remark that while being a policy-based algorithm, TRPO does not strictly adhere to Definition 2.2 as it solves a constrained optimization problem via line search. Yet, it does compute gradients of its objective function w.r.t. the policy parameters and therefore we treat it as a policy gradient algorithm.

### PPO

Given the complexity of TRPO, Proximal Policy Optimization (PPO) is designed to enforce comparable constraints on the divergence between consecutive policies during the learning process while simplifying the algorithm to not require second-order methods. This is achieved by heuristically flattening the gradients outside of an approximate trust region around the old policy. In addition, PPO uses a novel method to learn an estimate of the advantage function.

Let ${r_{\theta}{({a \mid s})}} = \frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}}$. Then, PPO uses the following estimate of the policy gradients:

Here, the clip-function $\text{clip}:{{{\mathbb{R}} \times {\mathbb{R}} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$ is defined by

and is applied element-wise to $r_{\theta}$. $\varepsilon$ is a hyperparameter.

This clipped objective conservatively removes the incentive for moving the new policy to far away from the old one. Intuitively, this can be seen as follows. We distinguish two cases: positive and negative estimated advantages $\hat{A}{(s,a)}$, i.e. whether action $a$ is good or bad. If ${\hat{A}{(s,a)}} > 0$, the surrogate objective $J_{\text{PPO}}{(\theta)}$ increases when $a$ becomes more likely. Similarly, if ${\hat{A}{(s,a)}} < 0$, $J_{\text{PPO}}{(\theta)}$ increases when $a$ becomes less likely. Hence, we want to adjust the policy parameters $\theta$ accordingly. However, by clipping the policy ratio $r_{\theta}$, this positive effect on the objective function disappears once we move outside the clip range. This clipping process is conservative as we only clip if the objective function would improve. If the policy is changed in the opposite direction such that $J_{\text{PPO}}{(\theta)}$ decreases, $r_{\theta}$ is not clipped due to taking the minimum in Equation. Figure 3 illustrates this explanation. The pseudocode for PPO is presented in Algorithm 6.

Figure 3: Illustration of the conservative clipping of PPO’s objective function, which is shown as a function of the ratio rθ for a single transition depending on whether the advantages are positive (a) or negative (b). Replicated from.

Initialize θ and ϕ at random
s, r ∼ P (s,a) ⊳ sample next state and reward
for all epochs do
R, A ← computeGAE (v,r,λ,γ) ⊳ Compute returns and advantages
${d\theta}\leftarrow{{\nabla_{\theta}\frac{1}{|\mathcal{D}|}}{\sum_{\mathcal{D}}{{\min\left( \frac{\pi{({a \mid s})}}{\beta{({a \mid s})}},{\text{clip}{(\frac{\pi{({a \mid s})}}{\beta{({a \mid s})}},{1 - \varepsilon},{1 + \varepsilon})}} \right)}A}}}$
${d\phi}\leftarrow{{\nabla_{\phi}\frac{1}{|\mathcal{D}|}}{\sum_{\mathcal{D}}{({R - {V_{\phi}{(s)}}})}^{2}}}$
update θ and ϕ using d θ and d ϕ via gradient ascent / descent

To compute the estimate ${\hat{A}}_{\phi}$ of the advantage function, PPO uses generalized advantage estimation (GAE) to further reduce the variance of gradients. GAE computes the estimated advantage as

where $\delta_{i} = {{r_{i} + {\gamma{\hat{V}}_{\phi}{(s_{i + 1})}}} - {{\hat{V}}_{\phi}{(s_{i})}}}$. The value function estimate ${\hat{V}}_{\phi}$ is learned by minimizing

where the first term is treated as independent of $\phi$. GAE relates to the idea of eligibility traces to use both the sampled rewards and the current value function estimate on every time step. By computing such an exponentially weighted estimator, GAE reduces the variance of the policy gradients at the cost of introducing a slight bias to the value function estimate. The hyperparameters $\gamma$ and $\lambda$ both adjust this bias-variance tradeoff. $\gamma$ does so by scaling the value function estimate $\hat{V}$ whereas $\lambda$ controls the dependence on delayed rewards. Note that GAE is a strict generalization of A3C's advantage estimate as Equation reduces to Equation when $\lambda = 1$. The pseudocode for GAE is presented in Algorithm 7.

if transition was terminal then

Beyond these main innovations, PPO uses several implementational details to improve learning. PPO conducts multiple update epochs for each batch of data such that several gradient descent steps are based on the same transitions to increase sample efficiency and speed up learning. Moreover, PPO commonly augments its surrogate objective with an entropy bonus $H{(\pi_{\theta}{( \cdot \mid s)})}$ and uses multiple actors similarly to A3C. Lastly, we note that further algorithms have been proposed as modifications of PPO, e.g. Phasic Policy Gradients and Robust Policy Optimization, which we will not discuss further as they only modify minor details.

### V-MPO

In the previous algorithms, we learn a policy from the control perspective by selecting actions to maximize expected rewards. In this subsection, we consider an alternative formulation of RL problems, which casts them as probabilistic inference problems of estimating posterior policies that are consistent with a desired outcome. This problem is then solved via Expectation Maximization (EM). This procedure was first proposed in the off-policy algorithm Maximum a-posteriori Policy Optimization (MPO). Here, we discuss its on-policy variant V-MPO, where the \"V\" in the name refers to learning the value function $V_{\pi}$ instead of $Q_{\pi}$ as in MPO.

The main idea of V-MPO is to find a maximum a posteriori estimate of the policy by sequentially finding a tight lower bound on the posterior and then maximizing this lower bound. This problem can be transformed into the objective function

where $\mathcal{L}_{\pi}$ is the policy loss

$\mathcal{L}_{\eta}$ is the temperature loss

and $\mathcal{L}_{\nu}$ is the trust-region loss

Here, ${sg}{\lbrack{\lbrack \cdot \rbrack}\rbrack}$ is a stop-gradient operator, meaning its arguments are treated as constants when computing gradients, $\eta$ is a learnable temperature parameter, $\nu$ is a learnable KL-penalty parameter, $\varepsilon_{\nu}$ and $\varepsilon_{\eta}$ are hyperparameters, $\mathcal{D}$ is a batch of transitions and $\overset{\sim}{\mathcal{D}} \subset \mathcal{D}$ is the half of these transitions with the largest advantages. We will provide a sketch of how to derive this objective function in the following. We refer the interested reader to Appendix Appendix C for a more detailed derivation.

Let ${p_{\theta}{(s,a)}} = {\pi_{\theta}{({a \mid s})}d^{\pi_{\theta}}{(s)}}$ denote the joint state-action distribution under policy $\pi_{\theta}$ conditional on the parameters $\theta$. Let $\mathcal{I}$ be a binary random variable whether the updated policy $\pi_{\theta}$ is an improvement over the old policy $\pi_{\text{old}}$, i.e. $\mathcal{I} = 1$ if it is an improvement. We assume the conditional probability of $\pi_{\theta}$ being an improvement given a state $s$ and an action $a$ is proportional to the following expression

Given the desired outcome $\mathcal{I} = 1$, we seek the posterior distribution conditioned on this event. Specifically, we seek the maximum a posteriori estimate

where $\rho$ is some prior distribution. ${\ln p_{\theta}}{({\mathcal{I} = 1})}$ can be rewritten as

for some distribution $\psi$ over $\mathcal{S} \times \mathcal{A}$. Observe that, since the KL divergence is non-negative, the first term is a lower bound for ${\ln p_{\theta}}{({\mathcal{I} = 1})}$. Akin to EM algorithms, V-MPO now iterates by choosing the variational distribution $\psi$ in the expectation (E) step to minimize the KL divergence in Equation to make the lower bound as tight as possible. In the maximization (M) step, we maximize this lower bound and the prior ${\ln\rho}{(\theta)}$ to obtain a new estimate of $\theta^{\ast}$ via Equation.

First, we consider the E-step. Under the proportionality assumption, we turn the problem of finding a variational distribution $\psi$ to minimize $D_{KL}{(\psi \parallel p_{\theta_{\text{old}}}{( \cdot, \cdot \mid \mathcal{I} = 1)})}$ into an optimization problem over the temperature $\eta$. This is formulated as a constrained problem subject to a bound on the KL divergence between $\psi$ and the previous state-action distribution $p_{\theta_{\text{old}}}$ while ensuring that $\psi$ is a state-action distribution. To enable optimizing $\eta$ via gradient descent, we transform this constrained problem into an unconstrained problem via Lagrangian relaxation, which emits both the form of the variational distribution

and the temperature loss

find that using only the highest 50 % of advantages per batch when sampling these expressions, i.e. replacing $\mathcal{D}$ with $\overset{\sim}{\mathcal{D}}$, substantially improves the algorithm. The advantage function $A_{\pi}$ is estimated by ${\hat{A}}_{\phi}$, which is learned as in A3C.

Then, in the M-Step we solve the maximum a posterior estimation problem over the policy parameters $\theta$ for the constructed variational distribution $\psi{(s,a)}$ and the thereby implied lower bound. This lower bound, i.e. the first term in Equation, becomes the weighted maximum likelihood policy loss

after dropping terms independent of $\theta$. This loss is computed over the same reduced batch $\overset{\sim}{\mathcal{D}}$ as the temperature loss, effectively assigning out-of-sample transitions a weight of zero. Simultaneously, we want to maximize the prior $\rho{(\theta)}$ according to the maximization problem. V-MPO follows TRPO and PPO to choose a prior such that the new policy is kept close to the previous one, i.e.

with learnable parameter $\nu$. However, optimizing the resulting sample-based maximum likelihood objective directly tends to result in overfitting. Hence, a sequence of transformations is applied. First, the prior is transformed into a hard constraint on the KL divergence when optimizing the policy loss. To employ gradient-based optimization, we use Lagrangian relaxation to transform this constrained optimization problem back into an unconstrained problem and use a coordinate-descent strategy to simultaneously optimize for $\theta$ and $\nu$. This can equivalently be written via the stop-gradient operator yielding the trust-region loss.

Initialize θ and ϕ at random
s, r ∼ P (s,a) ⊳ sample next state and reward
for all epochs do
Compute returns R and advantages A
Compute $\overset{\sim}{\mathcal{D}}$
$L_{\nu}\leftarrow{{\frac{1}{|\mathcal{D}|}{\sum_{\mathcal{D}}{\nu{({\varepsilon_{\nu} - {{sg}{({D_{KL}{({\pi_{\text{old}} \parallel \pi_{\theta}})}})}}})}}}} + {{sg}{(\nu)}D_{KL}{({\pi_{\text{old}} \parallel \pi_{\theta}})}}}$ ⊳ KL loss
$L_{\pi}\leftarrow{- {\frac{1}{|\overset{\sim}{\mathcal{D}}|}{\sum_{\overset{\sim}{\mathcal{D}}}{{\ln\pi_{\theta}}{({a \mid s})}\psi{(s,a)}}}}}$ ⊳ Policy loss
$L_{\eta}\leftarrow{{\eta\varepsilon_{\eta}} + {\eta{\ln{({\frac{1}{|\overset{\sim}{\mathcal{D}}|}{\sum_{\overset{\sim}{\mathcal{D}}}{\exp\frac{A}{\eta}}}})}}}}$ ⊳ Temperature loss
d θ ← ∇θ(Lπ+Lν), ${d\eta}\leftarrow{\frac{\partial}{\partial\eta}L_{\eta}}$, ${d\nu}\leftarrow{\frac{\partial}{\partial\nu}L_{\nu}}$ ⊳ Compute gradients
$d\phi\leftarrow\frac{1}{|\mathcal{D}|}\sum_{\mathcal{D}}\nabla_{\phi}{(R - V_{\phi}{(s)})}^{2}$
update θ, η, ν and ϕ using d θ, d η, d ν and d ϕ via gradient ascent / descent

The learnable parameters $\eta$ and $\nu$ are Lagrangian multipliers and hence must be positive. We enforce this by projecting the computed values to small positive values $\eta_{\text{min}}$ and $\nu_{\text{min}}$ respectively if necessary. The pseudocode for V-MPO is depicted in Algorithm 8. As implementational details, V-MPO typically uses decoupled KL constraints for the mean and covariance of the policy in continuous action spaces following. This enables better exploration without moving the policy mean as well as fast learning by rapidly changing the mean without resulting in a collapse of the policy due to vanishing standard deviations. In addition, V-MPO can be used with an off-policy correction via an importance sampling ratio similarly to TRPO and PPO and uses multiple actors following A3C.

### Comparing Design Choices in Policy Gradient Algorithms

Having outlined the main on-policy policy gradient algorithms, we want to shortly compare them to characterize the main design choices in constructing such algorithms.

The predominant differences across policy gradient algorithms lie in the estimators ${\hat{\nabla}}_{\theta}J{(\theta)}$ of the policy gradients. We summarize these estimates in Table 1^88^8For V-MPO, we focus on the policy loss, thus ignoring the gradient of the KL loss $\mathcal{L}_{\nu}$ w.r.t. the policy parameters $\theta$ here.. The algorithms can be distinguished along several dimensions with respects to the gradients. First, they use different variance reduction techniques, which are especially reflected in how $Q_{\pi}$ in the policy gradient formula is estimated. Second, various policy regularization strategies are used. Third, the algorithms employ further lower-level details to stabilize learning. We will discuss each of these dimensions in the following.

$\frac{1}{|\mathcal{D}|}{\sum_{\mathcal{D}}{\hat{A}{{\nabla_{\theta}\ln}\pi_{\theta}}{({a \mid s})}}}$

$\frac{1}{|\mathcal{D}|}{\sum_{\mathcal{D}}{\hat{A}{\nabla_{\theta}\frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}}}}}$

$\frac{1}{|\mathcal{D}|}{\sum_{\mathcal{D}}{\hat{A}{{\nabla_{\theta}\min}\left( \frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}},{\text{clip}\left( \frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}},{1 - \varepsilon},{1 + \varepsilon} \right)} \right)}}}$

$\frac{1}{\sum_{\overset{\sim}{\mathcal{D}}}{\exp\left( \frac{\hat{A}}{\eta} \right)}}{\sum_{\overset{\sim}{\mathcal{D}}}{{\exp\left( \frac{\hat{A}}{\eta} \right)}{{\nabla_{\theta}\ln}\pi_{\theta}}{({a \mid s})}}}$

Table 1: Policy gradient estimates used by various policy gradient algorithms.

Reducing variance is important to stabilize learning and speed up convergence. However, while high variance means algorithms require more samples to converge, bias in the estimates is not resolvable even with infinite samples. All contemporary policy gradient algorithms, i.e. all presented algorithms except REINFORCE, make use of baselines to reduce variance as discussed in Section 3.2 when approximating the unknown $Q_{\pi}$. While REINFORCE samples returns as an unbiased but high-variance estimate, the other algorithms learn a value function $\hat{V}$ to estimate the advantage function $\hat{A}$. Notably, this reduces variance at the cost of introducing bias. Further differences arise from how advantages are estimated, albeit these strategies can be easily transferred between algorithms. PPO uses GAE to estimate advantages, which generalizes the n-step temporal difference estimates used in A3C, TRPO and V-MPO. In addition, V-MPO scales the advantages via the learned temperature $\eta$ and only uses the top 50 % of advantages per batch.

To stabilize learning beyond variance reduction, several regularization techniques are proposed by TRPO, PPO and V-MPO to limit the change in policies across iterations. TRPO imposes a constraint on the KL divergence between the newly learned and the previous policy. Thus, the policy gradients are not directly applied to update the policy parameters $\theta$ but instead they are postprocessed to yield an approximate solution to this constrained optimization problem. This comes at the cost of algorithmic complexity however. Whereas the other algorithms directly compute the estimated policy gradients via automatic differentiation, TRPO requires the estimation of a hessian and the application of the conjugate gradient algorithm followed by a line search. PPO avoids such complexity by introducing a heuristic, which bounds the probability ratio $\frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}}$, into its objective function. By conservatively clipping this ratio, large policy changes induced by overfitting the advantage function are prevented. This also enables PPO to conduct multiple updates on the same data to accelerate learning. V-MPO too limits the KL divergence across policies. The prior distribution is selected such that V-MPO arrives at a similar optimization problem with a penalty on the KL divergence as TRPO. Following TRPO, V-MPO transforms this into a constrained optimization problem, albeit now with the goal of automatically tuning the penalty parameter by applying coordinate-descent to the Lagrangian relaxation of this constrained optimization problem.

Lastly, we point out that different lower-level details are employed by the discussed algorithm. Except for REINFORCE, all algorithms use several actors, which are potentially updated asynchronously, and average gradients over batches of transitions to further reduce their variance. Here, V-MPO slightly diverges from the other algorithms as it computes a weighted average based on the advantages of the transitions, i.e. with weights

A3C and PPO commonly use an entropy bonus to prevent premature convergence to a suboptimal policy by incentivizing a higher standard deviation of the Gaussian output by the policy. We observe that V-MPO does not use an entropy bonus but achieves a comparable effect in continuous action spaces by constraining the policy mean and standard deviation separately. Lastly, TRPO and PPO include an importance sampling correction to compensate for the slight off-policy nature of the algorithms induced by using multiple asynchronous workers. This is also mentioned as an option for V-MPO.

## Convergence Results

In this section, we discuss convergence results for policy gradient algorithms from literature. First, we present an overview of different convergence proofs in Section 5.1. Then, we thoroughly present one selected result in Section 5.2.

### Literature Overview

Several convergence results have been proposed for policy gradient algorithms. They differ along various dimensions: the specific algorithms covered, the shown strength of convergence, the problem settings and the employed proving techniques. The following overview of convergence results is not intended to be complete but rather shall showcase these differences.

As previously discussed, REINFORCE uses an unbiased estimator of the policy gradients, which in expectation therefore point in the direction of the true gradients. Hence, under common stochastic approximation assumptions towards the step sizes, REINFORCE can be shown to converge to a locally optimal policy. In the general form of policy gradient algorithms, agnostic to the specific estimator of $Q_{\pi}$, showing convergence is more complex as the estimated gradients are typically biased when using a learned value function. and consider the simplest case where state and action spaces $\mathcal{S}$ and $\mathcal{A}$ are finite and no function approximation is used, i.e. the policy uses a tabular parameterization with one parameter for each state-action combination. Using that the exact policy gradients can be calculated in this case, both studies show the global convergence to an optimal policy with a linear convergence rate.

and generalize these results to settings with function approximation, albeit under impractical conditions on the approximators, which are required to be linear in their inputs. The extension to function approximation comes at the cost of only being able to proof local convergence using stochastic approximation and the Supermartingale Convergence Theorem.

Finally, some convergence results exist for the specific algorithms such as TRPO and PPO. TRPO is based on Theorem 4.1, which comes with monotonic improvement guarantees. However, TRPO is only an approximation to the algorithm stemming from Theorem 4.1, so that no such guarantee holds for TRPO in practice. We further remark that PPO is similarly intended as an heuristic of this theoretical algorithm. Nonetheless, efforts have been made to proof the convergence of these practical algorithms. show that a slightly modified version of PPO converges to a globally optimal policy at a sublinear rate under specific assumptions. In particular, they require an overparameterized neural network as the function approximator such that they can use infinite-dimensional mirror-descent to proof the convergence. provide a proof using two time-scale stochastic approximation that PPO converges to a locally optimal policy under more realistic assumptions akin to typical learning scenarios.

### Mirror Learning

In this subsection, we focus on the convergence proof provided by. While primarily of theoretical interest, we choose to discuss this particular result as it is agnostic to the selected algorithm and parameterization and can hence by applied to a range of policy gradient algorithms. introduce a framework called *mirror learning*, which comes with global convergence guarantees for all policy gradient algorithms that adhere to a specific form. In the following, we follow in deriving their results. We start by giving some definitions, based on which we then present the general form of mirror learning updates. We show that the discussed algorithms largely adhere to this form. Finally, we proof that this implies the convergence to an optimal policy.

### Fundamentals of Mirror Learning

From here onwards, we do not explicitly write down the policy parameters, i.e. we omit the subscript $\theta$ when describing a policy $\pi$. define the drift $\mathfrak{D}$ and the neighborhood operator $\mathcal{N}$ as follows.

### Definition 5.1

(Drift) A drift functional

is a map which satisfies the following conditions for all $s \in \mathcal{S}$ and ${\pi,\overline{\pi}} \in \Pi$:

${{\mathfrak{D}}_{\pi}{({\overline{\pi} \mid s})}} \geq {{\mathfrak{D}}_{\pi}{({\pi \mid s})}} = 0$, (non-negativity)

${\mathfrak{D}}_{\pi}{({\overline{\pi} \mid s})}$ has zero gradient with respects to $\overline{\pi}{( \cdot \mid s)}$ at $\overline{\pi}{( \cdot \mid s)} = \pi{( \cdot \mid s)}$, more precisely all its Gâteaux derivatives^99^9See Definition D.16. are zero, (zero gradient)

where we used ${\mathfrak{D}}_{\pi}\left( \overline{\pi}{( \cdot \mid s)} \mid s \right) ≔ {\mathfrak{D}}_{\pi}{(\overline{\pi} \mid s)}$.

For any state distribution $\nu_{\pi}^{\overline{\pi}} \in {\Delta{(\mathcal{S})}}$, that can depend on both $\overline{\pi}$ and $\pi$, the drift from $\overline{\pi}$ to $\pi$ is given by

We require $\nu_{\pi}^{\overline{\pi}}$ to be such that this expectation is continuous in $\overline{\pi}$ and $\pi$. We call a drift trivial if ${{\mathfrak{D}}_{\pi}^{\nu}{(\overline{\pi})}} = 0$ for all ${\pi,\overline{\pi}} \in \Pi$.

### Definition 5.2

(Neighborhood Operator) A mapping

is a neighborhood operator if it satisfies the following conditions:

$\mathcal{N}$ is continuous, (continuity)

$\mathcal{N}{(\pi)}$ is compact for all $\pi \in \Pi$, (compactness)

There exists a metric $\chi:{{\Pi \times \Pi}\rightarrow{\mathbb{R}}}$ such that ${\chi{(\pi,\overline{\pi})}} \leq \zeta$ implies $\overline{\pi} \in {\mathcal{N}{(\pi)}}$ for all ${\pi,\overline{\pi}} \in \Pi$ given some $\zeta \in {\mathbb{R}}_{+}$. (closed ball)

We call ${\mathcal{N}{( \cdot )}} = \Pi$ the trivial neighborhood operator.

With these definitions, we can define the mirror learning update rule.

### Definition 5.3

(Mirror Learning Update) Let $\pi_{\text{old}}$ be the previous policy and $d^{\pi_{\text{old}}}$ the state distribution under $\pi_{\text{old}}$. Further, let

be the mirror learning operator. Then, the mirror learning update chooses the new policy $\pi_{\text{new}}$ as

Under the light of this mirror learning update, the drift $\mathfrak{D}$ from one policy to the next induces some penalty on the objective while the neighborhood operator puts a hard constraint on the divergence of subsequent policies.

### Policy Gradient Algorithms as Instances of Mirror Learning

Before proving the convergence of mirror learning to an optimal policy, we first show that the discussed policy gradient algorithms can partly be seen as instances of mirror learning, i.e. use updates of the form

A3C is a direct application of the Policy Gradient Theorem, albeit with a learned advantage function. Thus, at each iteration it approximately solves the optimization problem

This is the most trivial instantiation of mirror learning by using the trivial drift ${\mathfrak{D}}{( \cdot \mid \cdot )} = 0$ and the trivial neighborhood operator ${\mathcal{N}{( \cdot )}} = \Pi$. The same argumentation also applies to REINFORCE. Note that in practice however, we maximize the expectation over $\pi_{\text{old}}$ rather than $\pi$. For this reason, these are not exact instances of mirror learning.

TRPO's constrained optimization problems

with the average-KL ball as the neighborhood operator, i.e.

Here, we used that

and that maximizing over the action-value function is identical to maximizing over the advantage function following the discussion in Section 3.2. Thus, TRPO is a mirror learning instance with the trivial drift ${\mathfrak{D}}{( \cdot \mid \cdot )} = 0$.

Each iteration, PPO searches for

where we write $r_{\pi}{({a \mid s})}$ for $\frac{\pi{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}}$. We can rewrite the expectation over actions by adding zero as

Using the same technique as before, we can write the first expectation equivalently as ${\mathbb{E}}_{A \sim \pi}\left\lbrack {A_{\pi_{\text{old}}}{(s,A)}} \right\rbrack$. We now focus on the second expectation. We replace the $\min$ operator with a $\max$ and push the first term inside the $\max$ to obtain

This final expression is non-negative. Moreover, it is zero for $\pi$ sufficiently close to $\pi_{\text{old}}$, i.e. such that for all actions $a \in \mathcal{A}$ we have ${r_{\pi}{({a \mid s})}} = \frac{\pi{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}} \in {\lbrack{1 - \varepsilon},{1 + \varepsilon}\rbrack}$, because then the $clip$-function reduces to the identity function w.r.t. its first argument. Thus, the derivatives of this expression must also be zero at $\pi{( \cdot \mid s)} = \pi_{\text{old}}{( \cdot \mid s)}$. These properties are the exact conditions for a mapping to be considered a drift in the sense of Definition 5.1. With this preparation, we can now write the PPO update as

where ${\mathfrak{D}}_{\pi_{\text{old}}}$ is a drift given by

This is an instance of the mirror learning update with the trivial neighborhood operator ${\mathcal{N}{( \cdot )}} = \Pi$ and $\nu_{\pi_{\text{old}}}^{\pi} = d^{\pi_{\text{old}}}$.

### Convergence Proof

Now, we present the main theoretical result of.

### Theorem 5.4

Let ${\mathfrak{D}}^{\nu}$ be a drift, $\mathcal{N}$ a neighborhood operator and $d^{\pi}$ the sampling distribution, all continuous in $\pi$. Let the objective, i.e. the expected returns under a policy $\pi$, be written as ${J{(\pi)}} = {{\mathbb{E}}_{S_{0} \sim {p_{0},\pi}}\left\lbrack G_{0} \right\rbrack}$. Let $\pi_{0} \in \Pi$ be the initial policy and the sequence of policies $\left( \pi_{n} \right)_{n = 0}^{\infty}$ be obtained through the mirror learning update rule under ${\mathfrak{D}}^{\nu}$, $\mathcal{N}$ and $d^{\pi}$. Then,

(Strict monotonic improvement)

(Value function optimality)

(Maximum attainable return)

### Proof

We structure the proof by in five steps. In step 1, we start by showing that mirror learning updates lead to improvements under the mirror learning operator $\mathcal{M}_{\mathfrak{D}}^{\pi_{n}}V_{\pi_{n - 1}}$, which implies improvements in the value function $V_{\pi_{n}}$. In step 2, we prove that the sequence of value functions $\left( V_{\pi_{n}} \right)_{n = 0}^{\infty}$ converges to some limit. In step 3, we show the existence of limit points of the sequence of policies $\left( \pi_{n} \right)_{n = 0}^{\infty}$, which are fixed points of the mirror learning update. In step 4, we prove that these limit points are also fixed points of Generalized Policy Iteration (GPI), from which we conclude that these limit points are optimal policies in step 5. For simplicity, we proof Theorem 5.4 for discrete state and actions spaces. However, the results are straightforward to extended to the continuous cases (see the appendix in for details).

We start by showing by contradiction that for all $n \in {\mathbb{N}}_{0}$ and for all $s \in \mathcal{S}$:

Suppose there exists $s_{0} \in \mathcal{S}$, which violates. We define a policy $\hat{\pi}$ with

This way, we guarantee $\hat{\pi} \in {\mathcal{N}{(\pi_{n})}}$ because $\pi_{n + 1} \in {\mathcal{N}{(\pi_{n})}}$ is forced by the mirror learning update and the distance between $\hat{\pi}$ and $\pi_{n}$ is similar to the distance between $\pi_{n + 1}$ and $\pi_{n}$ at every $s \neq s_{0}$ but smaller at $s = s_{0}$.

By assumption, we have at $s_{0}$ that

where we used that ${\left\lbrack {\mathcal{M}_{\mathfrak{D}}^{\hat{\pi}}V_{\pi_{n}}} \right\rbrack{(s)}} = {\left\lbrack {\mathcal{M}_{\mathfrak{D}}^{\pi_{n + 1}}V_{\pi_{n}}} \right\rbrack{(s)}}$ for $s \neq s_{0}$. Thus,

which contradicts the mirror learning update rule, i.e. that

Hence, we have shown that the sequence of policies $\left( \pi_{n} \right)_{n = 0}^{\infty}$ created by the mirror learning updates monotonically increases the mirror learning operator at every state. Next, we show that this property, i.e. ${\left\lbrack {\mathcal{M}_{\mathfrak{D}}^{\pi_{n + 1}}V_{\pi_{n}}} \right\rbrack{(s)}} \geq {\left\lbrack {\mathcal{M}_{\mathfrak{D}}^{\pi_{n}}V_{\pi_{n}}} \right\rbrack{(s)}}$, implies the monotonic improvement in the value function

for all $s \in \mathcal{S}$ and $n \in {\mathbb{N}}_{0}$.

By using the definitions of the value function $V_{\pi}$, the action-value function $Q_{\pi}$, the mirror learning operator $\mathcal{M}_{\mathfrak{D}}^{\overline{\pi}}V_{\pi}$ and the identity ${{\mathfrak{D}}_{\pi}{({\pi \mid s})}} = 0$, adding zeros and rearranging, we obtain

where we used Inequality in the final step. We take the infimum over states and replace the expectation with another infimum over states as a lower bound:

From this expression, we obtain

since $\nu_{\pi_{n}}^{\pi_{n + 1}}{(s)}$ and $d^{\pi_{n}}{(s)}$ are probabilities and the drift $\mathfrak{D}$ is non-negative. Thus, we have proven the monotonic improvement of value functions ${V_{\pi_{n + 1}}{(s)}} \geq {V_{\pi_{n}}{(s)}}$. We observe that this already implies the strict monotonic improvement property

for all $n \in {\mathbb{N}}_{0}$ since applying and sequentially to yields for all $s \in \mathcal{S}$

We obtain the desired inequality by taking the expectation over $S \sim p_{0}$.

From step 1, we know that the value functions increase uniformly over the state space, i.e. ${{V_{\pi_{n + 1}}{(s)}} - {V_{\pi_{n}}{(s)}}} \geq 0$, for all s $\in \mathcal{S}$, $n \in {\mathbb{N}}_{0}$. As the rewards $r$ are bounded by assumption and we consider the episodic case where episode lengths are also bounded by $T$ (albeit the same argument applies for infinite time horizons via discounting), the value functions ${V_{\pi}{(s)}} = {{\mathbb{E}}_{\pi}\left\lbrack {{{\sum_{k = 0}^{T}{\gamma^{k}R_{t + k + 1}}} \mid S_{t}} = s} \right\rbrack}$ are also uniformly bounded. Via the Monotone Convergence Theorem (Theorem D.13), the sequence of value functions $\left( V_{\pi_{n}} \right)_{n = 0}^{\infty}$ must therefore converge to some limit $V$.

Now, we show the existence of limit points of the sequence of policies $\left( \pi_{n} \right)_{n = 0}^{\infty}$ and prove by contradiction that these are fixed points of the mirror learning update.

The sequence $\left( \pi_{n} \right)_{n = 0}^{\infty}$ is bounded, thus the Bolzano-Weierstrass Theorem (Theorem D.14) yields the existence of limits $\overline{\pi}$ to which some respective subsequence $\left( \pi_{n_{i}} \right)_{i = 0}^{\infty}$ converges. We denote this set of limit points as $L\Pi$. For each element of such a convergent subsequence $\left( \pi_{n_{i}} \right)_{i = 0}^{\infty}$, mirror learning solves the optimization problem

This expression is continuous in $\pi_{n_{i}}$ due to the continuity of the value function, the drift and neighborhood operator (by definition) and the sampling distribution (by assumption). Let $\overline{\pi} = {\lim_{i\rightarrow\infty}\pi_{n_{i}}}$. Berge's Maximum Theorem (Theorem D.15) now guarantees the convergence of the above expression, yielding

For all $i \in {\mathbb{N}}_{0}$, we obtain the next policy $\pi_{n_{i} + 1}$ as the argmax of Expression. Since this expression converges to the limit in, there must exist some subsequence $\left( \pi_{n_{i_{k}} + 1} \right)_{k = 0}^{\infty}$ of $\left( \pi_{n_{i} + 1} \right)_{i = 0}^{\infty}$ which converges to some policy $\pi^{\prime}$, which is the solution to the optimization problem. We now show by contradiction that $\pi^{\prime} = \overline{\pi}$, which implies that $\overline{\pi}$ is a fixed point of the mirror learning update rule.

Suppose $\pi^{\prime} \neq \overline{\pi}$. As $\pi^{\prime}$ is induced by the mirror learning update rule, the monotonic improvement results from step 1 yield

then we have for some state $s$

In the last equality, we used that the sequence of value functions converges to some unique limit $V$, which implies $V_{\overline{\pi}} = V$. We obtain the following via this result, Inequality, which must be strict for $s$, and the non-negativity of the drift $\mathfrak{D}$:

However due to ${V_{\pi^{\prime}}{(s)}} = {\lim_{k\rightarrow\infty}V_{\pi_{n_{i_{k}} + 1}}}$, this contradicts the uniqueness of the value limit, which gives $V_{\pi^{\prime}} = V$. Therefore, we have shown by contradiction that

Following step 3, let $\overline{\pi}$ be a limit point of $\left( \pi_{n} \right)_{n = 0}^{\infty}$. We will show by contradiction that $\overline{\pi}$ is also a fixed point of GPI (see Theorem 2.1), i.e. that for all $s \in \mathcal{S}$

From step 3, we know that

as subtracting an action-independent baseline does not affect the argmax. Now, we assume the existence of a policy $\pi^{\prime}$ and state $s$ with

Let $m = {|\mathcal{A}|}$ denote the size of the action space. Then, we can write for any policy $\pi$, $\pi{( \cdot \mid s)} = \left( x_{1},\ldots,x_{m - 1},1 - \sum_{i = 1}^{m - 1}x_{i} \right)$. With this notation, we have

This shows that ${\mathbb{E}}_{A \sim \pi}\left\lbrack {A_{\overline{\pi}}{(s,A)}} \right\rbrack$ is an affine function of $\pi{( \cdot \mid s)}$, which implies that all its Gâteaux derivatives are constant in $\Delta{(\mathcal{A})}$ for fixed directions. Due to Inequality, this further implies that the Gâteaux derivatives in direction from $\overline{\pi}$ to $\pi^{\prime}$ are strictly positive. Additionally, we have that the Gâteaux derivatives of $\frac{\nu_{\overline{\pi}}^{\pi}{(s)}}{d^{\overline{\pi}}{(s)}}{\mathfrak{D}}_{\overline{\pi}}{({\pi \mid s})}$ are zero at $\pi = \overline{\pi}$. We see this by establishing lower and upper bounds, which both have derivatives of zero due to the independence of $\pi$ and the zero-gradient property of the drift:

recalling that ${{\mathfrak{D}}_{\overline{\pi}}{({\overline{\pi} \mid s})}} = 0$ for any $s \in \mathcal{S}$ and using ${\nu_{\overline{\pi}}^{\pi}{(s)}} \leq 1$. In combination, we obtain that the Gâteaux derivative of ${{\mathbb{E}}_{A \sim \pi}\left\lbrack {A_{\overline{\pi}}{(s,A)}} \right\rbrack} - {\frac{\nu_{\overline{\pi}}^{\pi}{(s)}}{d^{\overline{\pi}}{(s)}}{\mathfrak{D}}_{\overline{\pi}}{({\pi \mid s})}}$ is strictly positive as well. Therefore, we can find some policy $\hat{\pi}{( \cdot \mid s)}$ by taking a sufficiently small step from $\overline{\pi}{( \cdot \mid s)}$ in the direction of $\pi^{\prime}{( \cdot \mid s)}$ such that $\hat{\pi} \in {\mathcal{N}{(\overline{\pi})}}$ and

With this, we can construct a policy which contradicts Equation. Let $\overset{\sim}{\pi}$ be defined such that

This guarantees $\overset{\sim}{\pi} \in {\mathcal{N}{(\overline{\pi})}}$ and

which contradicts Equation, so the assumption must be wrong, proving

The main result from step 4 shows that any limit point $\overline{\pi}$ of $\left( \pi_{n} \right)_{n \in {\mathbb{N}}}$ is also a fixed point of GPI. Thus, as corollaries all properties induced by GPI (see Theorem 2.1) apply to $\overline{\pi} \in {L\Pi}$. Particularly, we have the optimality of $\overline{\pi}$, the value function optimality $V = V_{\overline{\pi}} = V^{\ast}$ and thereby also the maximality of returns as

Thus, we have shown all properties as claimed by Theorem 5.4. ∎

We close this section with some remarks. In practice, exact updates according to the mirror learning update rule are generally infeasible. Instead, we can sample the expectation to obtain batch estimators over a batch $\mathcal{D}$ of transitions

where $Q_{\pi_{\text{old}}}$ has to be estimated as well. These batch estimators can also only be approximately optimized each iteration via gradient ascent to update the policy. Given these approximations and the at-best local convergence of gradient ascent, the outlaid convergence properties remain theoretical.

## Numerical Experiments

Now, we empirically compare the discussed policy gradient algorithms. Consistent with the original works, we compare them on the established MuJoCo task suite, accessed through the Gymnasium library. MuJoCo features robotics simulations, where the tasks are to control and move robots of different shapes by applying torques to each joint.

Our implementations build on the PPO implementation from the BRAX library and are written in JAX. For enhanced comparability, all algorithms that estimate advantages use GAE similarly to PPO. Instead of A3C, we use its synchronous variant A2C due to its simpler implementation. Note that A2C exhibits comparable performance as A3C and only differs in that it waits for all actors to collect transitions to update them synchronously. We modify REINFORCE to average gradients over batches of transitions similarly as in the other algorithms since computing one update per environment step is computationally very costly. Note that this is however likely to improve the performance compared to a naive implementation of REINFORCE. We do not tune hyperparameters and keep choices consistent across algorithms where possible. See Appendix Appendix A for the hyperparameters we use. The experiments were run on a standard consumer CPU. All our implemented algorithms and the code for running the experiments can be found at [https://github.com//PolicyGradientsJax](https://github.com//PolicyGradientsJax).

Figure 4: Comparison of rewards per episode during training on several MuJoCo tasks. For each algorithm, we report means and standard deviations of three runs with different random seeds.

In our main experiment, we compare the performance of the algorithms in terms of the achieved episodic rewards over the course of training. The performances in different MuJoCo tasks are presented in Figure 4. We observe that PPO outperforms the other algorithms in three of four tasks by achieving higher episodic rewards while learning good policies quickly. The performance difference is most prevalent on the *Humanoid*-task, the most challenging of the four, where PPO learns much stronger policies than the other algorithms. In addition, we find our implementation of PPO to be competitive with common RL libraries as shown in Appendix B.1. V-MPO and TRPO are comparable in performance, with each of the two slightly outperforming the other on two out of four environments. We note that V-MPO is intended for training for billions of environment steps, such that its lower performance compared to PPO in our experiments is expected^1010^10Also see the discussions at https://openreview.net/forum?id=SylOlp4FvH on this.. A2C requires more interactions with the environment to reach similar performance levels as V-MPO and TRPO but fails to learn any useful policy in the *Ant*-task. This slower learning^1111^11Slow in terms of the required environment steps. Note however that A2C runs significantly faster than PPO, TRPO and V-MPO in absolute time due to using less epochs per batch. is at least partially caused by A2C only using a single update epoch per batch. REINFORCE performance worst on all environments, which is unsurprising giving the high variance of gradients in REINFORCE. This also highlights the benefits of the bias-variance trade-off by the other algorithms as discussed in Section 4.6. We find our performance-based ranking of the algorithms to be consistent with literature (e.g., ).

Moreover, we remark that A2C is the only algorithm for which we used an entropy bonus because the learned policies collapsed without it. We showcase this in our expended experiments in Appendix B.2. This underlines the usefulness of the (heuristic) constraints of V-MPO, PPO and TRPO on the KL divergence, which avoid such collapses even without any entropy bonuses. To further investigate this, we show the average KL divergences between consecutive policies throughout training in Figure 5. Here, we approximated the KL divergence using the unbiased estimator

for all algorithms except TRPO, which analytically calculates the exact KL divergence since it is used within the algorithm. We see that the KL divergences remain relatively constant for all algorithms after some initial movement. TRPO displays the most constant KL divergence, which is explained by its hard constraint. With the chosen hyperparameters, V-MPO uses the same bound on the KL divergence as TRPO, however without strictly enforcing it as outlined in the derivation of V-MPO. Thus, V-MPO's KL divergence exhibits slightly more variance then TRPO and also frequently exceeds this bound. PPO's clipping heuristic achieves a similar effect resulting in a comparable picture. Due to the lack of constraints on the KL divergence, A2C and REINFORCE show slightly more variance. Interestingly, their KL divergences are orders of magnitudes lower than for the other algorithms, especially for REINFORCE (note the logarithmic scale in Figure 5). We reason this with A2C and REINFORCE using only a singly update epoch per batch, whereas the PPO and V-MPO use multiple epochs and TRPO uses a different update scheme via line search. In Appendix B.3, we provide experimental evidence for this hypothesis. Additionally, we note again that the entropy bonus also stabilizes and limits the KL divergence for A2C as shown in Appendix B.2.

Figure 5: Comparison of the average KL divergence across policies during training.

These findings highlight the benefits of regularization through constraining the KL divergence and incentivizing entropy. Regularization stabilizes learning and prevents a collapse of the policy. At the same time, it allows more frequent updates through multiple epochs per batch, which drastically increases the sample efficiency of the algorithms and speeds up learning.

## Conclusion

In this work, we presented a holistic overview of on-policy policy gradient methods in reinforcement learning. We derived the theoretical foundations of policy gradient algorithms, primarily in the form of the Policy Gradient Theorem. We have shown how the most prominent policy gradient algorithms can be derived based on this theorem. We discussed common techniques used by these algorithms to stabilize training including learning an advantage function to limit the variance of estimated policy gradients, constraining the divergence between policies and regularizing the policy through entropy bonuses. Subsequently, we presented evidence from literature on the convergence behavior of policy gradient algorithms, which suggest that they may find at least locally optimal policies. Finally, we conducted numerical experiments on well-established benchmarks to further compare the behavior of the discussed algorithms. Here, we found that PPO outperforms the other algorithms in the majority of the considered tasks and we provided evidence for the necessity of regularization, by constraining KL divergence or by incentivizing entropy, to stabilize training.

We acknowledge several limitations of our work. First, we deliberately limited our scope to on-policy algorithms, which excludes closely related off-policy policy gradient algorithms and the novelties introduced by them. Second, we presented an incomplete overview of on-policy policy gradient algorithms as other, albeit less established, algorithms exist (e.g., ) and the development of further algorithms remains an active research field. Here, we focused on the, in our view, most prominent algorithms as determined by their impact, usage and introduced novelties. Third, the convergence results we referenced rest on assumptions that are quickly violated in practice. In particular, we want to underline that the results based mirror learning rely on the infeasible assumption of finding a global maximizer each iteration. Fourth, while we compared the discussed algorithms empirically and found results to be consistent with existing literature, our analysis is limited to the specific setting we used. Different results may arise on other benchmarks, with different hyperparameters or generally different implementations.

Finally, we note that still many questions remain to be answered in the field of on-policy policy gradient algorithm. So far, our understanding of which algorithm performs best under which circumstances is still limited. Moreover, it is unclear whether the best possible policy gradient algorithm has yet been discovered, which is why algorithm development remains of interest. Similarly, comprehensive empirical comparisons with other classes of RL algorithms may yield further insights on the practical advantages and disadvantages of policy gradient algorithms and how their performance depends on the problem settings. Finally, we observe that still only a limited number of convergence results exist and not even all discussed algorithms are covered by these, e.g., no convergence results exist for V-MPO to the best of our knowledge. Here, further research is needed to enhance our understanding of the convergence behavior of policy gradient algorithms.
