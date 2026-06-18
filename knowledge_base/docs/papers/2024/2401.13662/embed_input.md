<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Definitive Guide to Policy Gradients in Deep Reinforcement Learning: Theory, Algorithms and Implementations

Topics include Reinforcement learning, Control, Learning, Policy gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In recent years, various powerful policy gradient algorithms have been proposed in deep reinforcement learning. While all these algorithms build on the Policy Gradient Theorem, the specific design choices differ significantly across algorithms. We provide a holistic overview of on-policy policy gradient algorithms to facilitate the understanding of both their theoretical foundations and their practical implementations. In this overview, we include a detailed proof of the continuous version of the Policy Gradient Theorem, convergence results and a comprehensive discussion of practical algorithms. We compare the most prominent algorithms on continuous control environments and provide insights on the benefits of regularization. All code is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) is a powerful set of methods for an agent to learn how to act optimally in a given environment to maximize some reward signal. In contrast to other methods such as dynamic programming, RL achieves this task of learning an optimal policy, which dictates the optimal behavior, via a trial-and-error process of interacting with the environment. Most early successful applications of RL use value-based methods (e.g., ), which estimate the expected future rewards to inform the agent's decisions. However, these methods only indirectly optimize the true objective of learning an optimal policy and are non-trivial to apply in settings with continuous action spaces.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we discuss policy gradient algorithms as an alternative approach, which aims to directly learn an optimal policy. Policy gradient algorithms are by no means new, but this subfield only gained traction in recent years following the emergence of deep RL with the development of various powerful algorithms (e.g., ). Deep RL is a subfield of RL, which uses neural networks and other deep learning methods. The increased interest in policy gradient algorithms is due to several appealing properties of this class of algorithms. They can be used natively in continuous action spaces without compromising the applicability to discrete spaces. In contrast to value-based methods, policy gradient algorithms inherently learn stochastic policies, which results in smoother search spaces and partly remedies the exploration problem of having to acquire knowledge about the environment in order to optimize the policy. In some settings, the optimal policy may also be stochastic itself. Lastly, policy gradient methods enable smoother changes in the policy during the learning process, which may result in better convergence properties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal is to present a holistic overview of policy gradient algorithms. In doing so, we limit the scope to on-policy algorithms, which we will define in Section 2. Thus, we exclude some popular algorithms including DDPG, TD3 and SAC. See Figure 1 for an overview of RL and the subfields we cover.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We give a comprehensive introduction to the theoretical foundations of policy gradient algorithms including a detailed proof of the continuous version of the Policy Gradient Theorem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive and compare the most prominent policy gradient algorithms and provide high quality pseudocode to facilitate understanding.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release competitive implementations of these algorithms, including the, to the best of our knowledge, first publicly available V-MPO implementation displaying performance on par with the results in the original paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section 2 introduces fundamental definitions in RL as well as an overview of deep learning. Section 3 derives the theoretical foundations of policy gradient algorithms with a special focus on proving the Policy Gradient Theorem, based on which we will construct several existing practical algorithms in Section 4. In Section 5, we discuss convergence results from literature. Section 6, presents the results of our numerical experiments comparing the discussed algorithms. Section 7 concludes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

In the following, we formally describe the general problem setting encountered in RL, define fundamental functions and introduce the subfields of RL our work is further concerned. Sections 2.2.1 and 2.2.2 are based, Chapter 3.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Each problem instance in RL consists of an agent and an environment with which he interacts to achieve some specific goal. The environment comprises everything external to the agent and can be formalized as a Markov Decision Process (MDP). Let an action space $\mathcal{A}$ be the set of all actions the agent can take and let a state space $\mathcal{S}$ be the set of all possible states, i.e. snapshots of the environment at any given point in time. State and action spaces can be discrete or continuous^11^1Here, we call a state/action space continuous if it is an interval in ${\mathbb{R}}^{d}$ for $d \in {\mathbb{N}}$. and we assume both to be compact and measurable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We write an MDP as a tuple $\mathcal{M} = {(\mathcal{S},\mathcal{A},P,\gamma,p_{0})}$, where $P:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{({\mathcal{S} \times {\mathbb{R}}})}}}$ is the environment's transition function, which defines the probability^22^2Technically, this is the value of the probability density function for continuous distributions. However, we unify terminology by referring to the values of probability density functions as probabilities here and in the following.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

$P{(s^{\prime},{r \mid {s,a}})}$ of transitioning to a new environment state $s^{\prime}$ and receiving reward $r \in {\mathbb{R}}$ when the agent uses action $a$ in state $s$, $\gamma \in {\lbrack 0,1\rbrack}$ is a discount rate and $p_{0} \in {\Delta{(\mathcal{S})}}$ is a probability distribution over potential starting states. We assume rewards $r$ to be bounded. In the following, our notation assumes state and action spaces to be continuous.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We call sequences of states, actions and rewards $(s_{t},a_{t},r_{t + 1},s_{t + 1},a_{t + 1},r_{t + 2},\ldots,s_{{t + k} - 1},a_{{t + k} - 1},r_{t + k},s_{t + k})$ trajectories. A one-step trajectory, i.e. a tuple $(s_{t},a_{t},r_{t + 1},s_{t + 1})$ is called a transition. In this work, we limit ourselves to episodic settings, where the agent only interacts with the environment for a finite number of at most $T$ steps after which the environment is reset to a starting state. An episode may however be shorter than $T$ if a terminal state is reached.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

The main goal in reinforcement learning is to solve the control problem of learning a policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ to maximize the expected return. The return $G_{t} ≔ {\sum_{k = 0}^{T}{\gamma^{k}r_{t + k + 1}}}$ is the discounted sum of rewards from timestep $t$ onwards. Note that $G_{t}$ is bounded since rewards are bounded. We denote the probability of taking action $a$ in state $s$ under policy $\pi$ with $\pi{({a \mid s})}$. For a policy $\pi$, its stationary state distribution $d^{\pi}$ determines the probability of being in a specific state $s \in \mathcal{S}$ at any point in time when following $\pi$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Let $\Pi$ be the set of all possible policies. RL algorithms ${\mathfrak{A}}:{\Pi\rightarrow\Pi}$ for the control problem now iteratively learn policies by interacting with the environment using the current policy to sample transitions, which are then used to update the policy. We will discuss how these updates can look like in Section 2.2.3. A key characteristic of many RL problems is a necessary trade-off between exploration and exploitation in this learning process. The agent has no prior knowledge of the environment and thus needs to explore different transitions in order to learn which states and actions are desirable. As state and action spaces are typically large however, exploiting the already acquired knowledge about the environment is also crucial to guide the search process for an optimal policy to subspaces that hold most promise. A common approach to this exploration problem is to add noise to the policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Value Functions", "weight": 1.0} -->

Based on the return, we define the value and action-value functions, which are fundamental in RL. The value function

<!-- chunk {"id": "body-0018", "role": "body", "section": "Value Functions", "weight": 1.0} -->

gives the expected return from state $s$ onwards when following policy $\pi$, which selects all subsequent actions. Thus, the value function states how good it is to be in a specific state $s$ given a policy $\pi$. Note that here we follow the general convention to write this just as an expectation over $\pi$. However, it should be noted that this expectation integrates over all subsequent states and actions that are obtained by following policy $\pi$, i.e. Equation computes the expected return given that all subsequent actions are sampled from $\pi$ and all rewards and next states are sampled from $P$. This is implicit in our notation here as well as in further expectations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Value Functions", "weight": 1.0} -->

Next, we define the action-value function

<!-- chunk {"id": "body-0020", "role": "body", "section": "Value Functions", "weight": 1.0} -->

which differs from the value function in that the very first action $a$ is provided as an input to the function and not determined by the policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Value Functions", "weight": 1.0} -->

the advantage function, which determines how good an action $a$ is in state $s$ in relation to other possible actions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Value Functions", "weight": 1.0} -->

From the definitions of $V_{\pi}$ and $Q_{\pi}$ we can derive the so-called Bellman equations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Value Functions", "weight": 1.0} -->

Thus, we find a formulation of the value function, which depends on the value of subsequent states.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Value Functions", "weight": 1.0} -->

Now, we can formally define what optimality means in RL. An optimal policy $\pi^{\ast}$ is defined by ${V_{\pi^{\ast}}{(s)}} \geq {V_{\pi}{(s)}}$ for all states $s$ and policies $\pi$, i.e. any optimal policy maximizes the expected return. It can be shown that in every finite MDP, a deterministic optimal policy exists.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Value Functions", "weight": 1.0} -->

We cite the following result without proof from on how to obtain an optimal policy, which we will revisit in Section 5.

<!-- chunk {"id": "body-0026", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

Finally, we will delineate the subfields of RL on which our work focuses. In this context, we will successively introduce function approximation, policy gradient methods and the on-policy paradigm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

RL algorithms are mostly concerned with learning functions such as $\pi$, $V_{\pi}$ or $Q_{\pi}$. Early reinforcement methods learn exact representations of these by maintaining lookup tables with entries for each possible function input. While this approach yields theoretical convergence guarantees, it is practically very limited. Similar states are treated independently such that learnings do not generalize from one state to others while specific states are only rarely visited in large state spaces. Moreover, this approach is not applicable to continuous spaces. Function approximation remedies these shortcomings by parameterizing the function to be learned. Let $f_{\theta}{(x)}$ be this learnable function, where $\theta$ are the function's parameters, which are adjusted over the course of learning, and $x$ are the functions inputs such as states and actions or representations thereof. By choosing $f_{\theta}$ to be continuous in its inputs, we can ensure that $f_{\theta}$ generalizes across its inputs when we fit it to sampled transitions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

$f_{\theta}$ can be as simple as a linear mapping, i.e. ${f_{\theta}{(x)}} = {\theta^{T}x}$, however recent works mostly use neural networks as function approximators (e.g., ). The field using neural networks as function approximators is coined deep RL. For the remainder of this paper, you can consider any learned function to be a neural network unless explicitly stated otherwise, although all our statements apply to any differentiable function approximators. We will introduce deep learning and neural networks in detail in Section 2.3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

Policy gradient methods pose an alternative to value-based methods in RL. Most early successes in RL use value-based methods such as Q-Learning or SARSA, that aim at learning a sequence of value functions converging to the optimal value function, from which an optimal policy can then be inferred. In contrast, policy-based RL, which we focus on in this work, directly learns a parameterized policy $\pi_{\theta}$. The main idea in this learning process is to increase the probability of those actions that lead to higher returns until we reach an (approximately) optimal policy. While this optimization problem can be approached in several ways, gradient-based methods are most commonly used. Following, we define policy gradient methods as follows.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

In this section, we introduce deep learning as a subfield of machine learning since its methods are commonly used in policy gradient algorithms. In recent years, deep learning has emerged as the premier machine learning method in various fields, enabling state-of-the-art performance in domains such as computer vision (e.g., ) and natural language processing (e.g.,. Following and, we define deep learning as a set of techniques to solve prediction tasks by learning multiple levels of representations from raw data using a composition of simple non-linear functions. This composition of functions, that we will describe in detail later, is referred to as (deep) neural network. Deep learning stands in contrast to conventional machine learning techniques like logistic regressions, which typically require hand-engineered representations as inputs to be effective. In the following, we introduce the general problem setting of deep learning using the notation of, formalize neural networks and describe how they are trained.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

Consider measurable spaces $\mathcal{X}$ and $\mathcal{Y}$. $\mathcal{Z} ≔ {\mathcal{X} \times \mathcal{Y}}$ is the data space with each element $z = {(x,y)} \in \mathcal{Z}$ being a tuple of input features $x \in \mathcal{X}$ and a label $y \in \mathcal{Y}$. Let $\mathcal{M}{(\mathcal{X},\mathcal{Y})}$ be the set of measurable functions from $\mathcal{X}$ to $\mathcal{Y}$. The problems we encounter in deep learning are prediction tasks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

Thus, the goal is to learn a mapping $f \in {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$ from inputs to labels by minimizing some loss function $\mathcal{L}$ over training data $S = {\{ z^{},\ldots,z^{(m)}\}}$ such that it generalizes to unseen data $z \in \mathcal{Z}$. To learn the function $f$, we first select a hypothesis set $\mathcal{F} \subset {\mathcal{M}{(\mathcal{X},\mathcal{Y})}}$. Deep learning then provides learning algorithms ${\mathfrak{A}}:{\mathcal{Z}\rightarrow\mathcal{F}}$ that use training data $S$ to learn the desired function $f = {{\mathfrak{A}}{(S)}}$. Before we discuss this learning process, we will first further characterize the mapping to be learned.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

In deep learning, functions in the hypothesis set $\mathcal{F}$ represent instances of neural networks. Note that here we limit ourselves to feedforward networks, also called multilayer perceptrons (MLP), and will not discuss transformers, recurrent (RNN) or convolutional neural networks (CNN).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Theoretical Foundations of Policy Gradients", "weight": 1.0} -->

Having introduced the fundamentals of deep RL, we can now discuss policy gradient algorithms in detail. In this section, we derive their theoretical foundations. Our main focus is going to be the Policy Gradient Theorem, on which all policy gradient algorithms build. This theorem will be discussed in Section 3.1. Furthermore, Sections 3.2 and 3.3 introduce the theoretical justifications for additional methods that are frequently used in policy gradient algorithms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Gradient Theorem", "weight": 1.0} -->

The idea of policy gradient algorithms is to maximize $J{(\theta)}$ over the parameters $\theta$ by performing gradient ascent. Hence, we require the gradients ${\nabla_{\theta}J}{(\theta)}$, however it is a priori not obvious how the right-hand side ${\mathbb{E}}_{S_{0} \sim {p_{0},\pi_{\theta}}}\left\lbrack G_{0} \right\rbrack$ depends on $\theta$ as changes in the policy $\pi$ also affect the state distribution $d^{\pi}$. The Policy Gradient Theorem yields an analytic form of ${\nabla_{\theta}J}{(\theta)}$ from which we can sample gradients that does not involve the derivative of $d^{\pi}$. Here, we focus on the undiscounted case, i.e. $\gamma = 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Gradient Theorem", "weight": 1.0} -->

Note that any discounted problem instance can be reduced to the undiscounted case by letting the reward function absorb the discount factor.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

In practice, the resulting estimates of the policy gradients can become very noisy when sampling from Equation. Therefore, a main practical challenge of policy gradient algorithms is to introduce measures to reduce the variance of the gradients while keeping the bias low. In this context, a well-known and widely used technique is to use a baseline when sampling an estimate of the action-value function $Q_{\pi}$. In this section, we show that using an appropriately chosen baseline does not bias the estimate but can greatly reduce the variance of the sampled gradients.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

In expectation over the policy $\pi$, this yields

<!-- chunk {"id": "body-0039", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

using the linearity of the expectation. Now, we show that the second part is 0. Using the Leibniz integral rule, we have that

<!-- chunk {"id": "body-0040", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

since $\pi{( \cdot \mid s)}$ is a probability distribution over actions. Thus, subtracting an action-independent baseline $b$ from an action-value function estimator $\hat{Q}$ does indeed not add any bias to the gradient estimate. While here we have shown this for a baseline which only depends on the current state, this result can be extended to baselines which depend on the current and all subsequent states.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

Next, we analyze the effect on the variance of the gradient estimates. Here, we only provide an approximate explanation, see for a more thorough analysis which derives bounds of the true variance. We can compute the variance using ${{Var}{\lbrack X\rbrack}} = {{{\mathbb{E}}{\lbrack X^{2}\rbrack}} - {{\mathbb{E}}{\lbrack X\rbrack}^{2}}}$. Due to the above, ${\mathbb{E}}{\lbrack X\rbrack}^{2}$ is independent of the baseline in our case. This yields

<!-- chunk {"id": "body-0042", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

where we approximated the variance by assuming independence of the two terms in the second step. Under this approximation, the variance of sampled gradients can be minimized by minimizing ${\mathbb{E}}_{\pi}\left\lbrack \left( {{\hat{Q}{(S,A)}} - {b{(S)}}} \right)^{2} \right\rbrack$. This is a common least squares problem resulting in the optimal choice of ${b{(s)}} = {{\mathbb{E}}_{\pi}{\lbrack{\hat{Q}{(s,A)}}\rbrack}}$ (see Theorem D.8). This result indicates that an appropriately chosen baseline can potentially significantly reduce variance of the gradients. Using this choice for the baseline, we would like to compute gradients for sampled states and actions as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Value Function Estimation with Baselines", "weight": 1.0} -->

Here, we used the relation of the value function $V_{\pi}$ to $Q_{\pi}$ and the definition of the advantage function $A_{\pi}$. Despite our approximations, this choice of a baseline turns out to yield almost the lowest possible variance of the gradients. However, note that in practice the advantage function must also be estimated. Learning this estimate typically introduces bias.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

Importance sampling is a technique to calculate expectations under one distribution given samples from another. Traditionally, this is only needed in off-policy RL, where we sample transitions using a behavior policy $\beta$ but want to calculate expectations over the target policy $\pi$. However, in some implementations of on-policy algorithms the policy may be updated before all data generated by it is processed. This makes these implementations slightly off-policy and thus importance sampling becomes relevant even for theoretically on-policy algorithms. We build our presentation of importance sampling, Section 5.5.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

Given a behavior policy $\beta$, we want to estimate the value function $V_{\pi}$ of our target policy $\pi$. Generally, we have

<!-- chunk {"id": "body-0046", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

We can calculate the probability of a trajectory $(a_{t},s_{t + 1},a_{t + 1},\ldots,a_{T - 1},s_{T})$ under any policy $\pi$ as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

Now, we can define the importance sampling ratio.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Policy Gradient Algorithms", "weight": 1.0} -->

Building on Theorem Theorem 3.1, several policy gradient algorithms have been proposed, which compute sample-based estimates ${\hat{\nabla}}_{\theta}J{(\theta)}$ of the actual policy gradients ${\nabla_{\theta}J}{(\theta)}$. This is done by constructing surrogate objectives $J_{\ast}$ such that ${{\hat{\nabla}}_{\theta}J{(\theta)}} = {{\nabla_{\theta}J_{\ast}}{(\theta)}}$. Additionally, most algorithms focus on stabilizing learning by regularizing the policy and reducing the variance of ${\hat{\nabla}}_{\theta}J{(\theta)}$. In this section, we derive the most prominent^77^7As determined by their impact on subsequent research and the adoption rate by users. algorithms before than comparing them in the final subsection.

<!-- chunk {"id": "body-0049", "role": "body", "section": "REINFORCE", "weight": 1.0} -->

REINFORCE (REward Increment = Non-negative Factor $\times$ Offset Reinforcement $\times$ Characteristic Eligibility) is the earliest policy gradient algorithm. While this algorithm precedes the formulation of the Policy Gradient Theorem, REINFORCE can be seen as a straightforward application of it. By using Monte Carlo methods to estimate $Q_{\pi}$ in Equation, i.e. by sampling entire episodes to compute the sample returns $G_{t} = {\sum_{k = 0}^{T}{\gamma^{k}r_{t + k + 1}}}$, REINFORCE samples policy gradients

<!-- chunk {"id": "body-0050", "role": "body", "section": "REINFORCE", "weight": 1.0} -->

Using the generic policy gradient update from Equation results in the gradient ascend updates

<!-- chunk {"id": "body-0051", "role": "body", "section": "REINFORCE", "weight": 1.0} -->

where $\alpha \in {(0,1\rbrack}$ is the learning rate determining the step size of the gradient steps and is set as a hyperparameter. At times, REINFORCE is extended by subtracting some baseline value from $G_{t}$ to reduce variance. The pseudocode for REINFORCE is presented in Algorithm 3.

<!-- chunk {"id": "body-0052", "role": "body", "section": "REINFORCE", "weight": 1.0} -->

for all episodes do
Generate trajectory s0, a0, r1, s1 …, sT under policy πθ
$G_{t}\leftarrow{\sum_{k = t}^{T}{\gamma^{k - t}r_{k}}}$ ⊳ estimate expected return Qπ
θ ← θ + α Gt ∇θln πθ (at∣st) ⊳ update policy parameters

<!-- chunk {"id": "body-0053", "role": "body", "section": "A3C", "weight": 1.0} -->

Instead of estimating $Q_{\pi}$ directly via sampling as in REINFORCE, we can alternatively learn such an estimate via function approximation. Algorithms that use this approach to learn a parameterized action-value function ${\hat{Q}}_{\phi}$ or value function ${\hat{V}}_{\phi}$ (called critic) with parameters $\phi$ in addition to learning the parameterized policy $\pi_{\theta}$ (called actor) are referred to as actor-critic algorithms. Note that in practice the actor and the critic may also share parameters.

<!-- chunk {"id": "body-0054", "role": "body", "section": "A3C", "weight": 1.0} -->

The most archetypical representative of this class of algorithms is Asynchronous Advantage Actor-Critic (A3C). A3C builds on two main ideas from which the algorithm's name originates. First, as suggested by the results from Section 3.2, A3C learns an estimate ${\hat{A}}_{\phi}$ of the advantage function indirectly by learning an estimate ${\hat{V}}_{\phi}$ of the value function. Second, A3C introduces the concept of using multiple parallel actors to interact with the environment to stabilize training. We will discuss both ideas in detail below. The algorithm samples policy gradients

<!-- chunk {"id": "body-0055", "role": "body", "section": "A3C", "weight": 1.0} -->

where $\mathcal{D}$ is a batch of transitions collected by the actors. The pseudocode for A3C is presented in Algorithm 4.

<!-- chunk {"id": "body-0056", "role": "body", "section": "A3C", "weight": 1.0} -->

In the original work, the advantage function is estimated via

<!-- chunk {"id": "body-0057", "role": "body", "section": "A3C", "weight": 1.0} -->

To understand this estimate, observe that

<!-- chunk {"id": "body-0058", "role": "body", "section": "A3C", "weight": 1.0} -->

for any $k \in {\mathbb{N}}$, which follows from the definition of the value and action-value functions as well as their relationship. Sampling this n-step temporal difference expression and replacing $V_{\pi}$ with our learned ${\hat{V}}_{\phi}$ yields Equation. Simultaneously to updating $\pi_{\theta}$, we learn ${\hat{V}}_{\phi}$ by minimizing the mean squared error loss

<!-- chunk {"id": "body-0059", "role": "body", "section": "A3C", "weight": 1.0} -->

over $\phi$ via SGD. Note that the inner expression is identical to the right hand side in Equation. In Equation, we compute the difference between the estimated return when choosing action $a_{t}$ in state $s_{t}$ and the estimated return when in state $s_{t}$, under policy $\pi$ respectively. However, $a_{t}$ is sampled from $\pi$ such that in expectation this difference should be 0 for the true value function $V_{\pi}$. Hence, we minimize this squared difference to optimize $\phi$ by treating the first term, $\sum_{i = 0}^{k - 1}\left( {{\gamma^{i}r_{t + i}} + {{\hat{V}}_{\phi}{(s_{t + k})}}} \right)$, as independent of $\phi$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "A3C", "weight": 1.0} -->

The use of multiple parallel actors is justified as follows. Deep RL is notoriously unstable, which was first resolved by off-policy algorithms using replay buffers that store and reuse sampled transitions for multiple updates. As an alternative, propose using several actors $\pi_{\theta}^{},\ldots,\pi_{\theta}^{(k)}$ to decrease noise by accumulating the gradients over multiple trajectories. These accumulated gradients are applied to a centrally maintained copy of $\theta$, which is then redistributed to each actor. By doing this asynchronously, each actor has a potentially unique set of parameters at any point in time compared to the other actors. This decreases the correlation of the sampled trajectories across actors, which can further stabilize learning.

<!-- chunk {"id": "body-0061", "role": "body", "section": "A3C", "weight": 1.0} -->

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

<!-- chunk {"id": "body-0062", "role": "body", "section": "A3C", "weight": 1.0} -->

As a final implementation detail, the policy loss function of A3C, from which the policy gradients are obtained, is typically augmented with an entropy bonus for the policy. Thus, the policy gradients become

<!-- chunk {"id": "body-0063", "role": "body", "section": "A3C", "weight": 1.0} -->

where $H$ is the entropy (see Definition D.4) and the entropy coefficient $\beta$ is a hyperparameter. This entropy bonus, first proposed, regularizes the policy such that it does not prematurely converges to a suboptimal policy. By rewarding entropy, the policy is encouraged to spread probability mass over actions which improves exploration.

<!-- chunk {"id": "body-0064", "role": "body", "section": "TRPO", "weight": 1.0} -->

Excessively large changes in the policy can result in instabilities during the training of RL algorithms. Even small changes in policy parameters $\theta$ can lead to significant changes in the resulting policy and its performance. Hence, small step sizes during gradient ascent cannot fully remedy this problem and would impair the sample efficiency of the algorithm. Trust Region Policy Optimization (TRPO) mitigates these issues by imposing a trust region constraint on the Kullback-Leibler (KL) divergence (see Definition D.5) between consecutive policies. In addition, TRPO uses an off-policy correction through importance sampling as discussed in Section 3.3 to account for the interleaved optimization and collection of transitions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "TRPO", "weight": 1.0} -->

and postprocesses them as detailed below to solve the approximate trust region optimization problem

<!-- chunk {"id": "body-0066", "role": "body", "section": "TRPO", "weight": 1.0} -->

where $\pi_{\text{old}} = \pi_{\theta_{\text{old}}}$ is the previous policy and $\theta_{\text{old}}$ the corresponding parameters. This optimization problem is an approximation to an objective with convergence guarantees, which we will show in the following. We start by presenting 's main theoretical result. Consider the objective of maximizing the expected return ${\mathbb{E}}_{S_{0} \sim {p_{0},\pi}}\left\lbrack G_{0} \right\rbrack$ under policy $\pi$, which we denote as $\eta{(\pi)}$ here.

<!-- chunk {"id": "body-0067", "role": "body", "section": "PPO", "weight": 1.0} -->

Given the complexity of TRPO, Proximal Policy Optimization (PPO) is designed to enforce comparable constraints on the divergence between consecutive policies during the learning process while simplifying the algorithm to not require second-order methods. This is achieved by heuristically flattening the gradients outside of an approximate trust region around the old policy. In addition, PPO uses a novel method to learn an estimate of the advantage function.

<!-- chunk {"id": "body-0068", "role": "body", "section": "PPO", "weight": 1.0} -->

and is applied element-wise to $r_{\theta}$. $\varepsilon$ is a hyperparameter.

<!-- chunk {"id": "body-0069", "role": "body", "section": "PPO", "weight": 1.0} -->

This clipped objective conservatively removes the incentive for moving the new policy to far away from the old one. Intuitively, this can be seen as follows. We distinguish two cases: positive and negative estimated advantages $\hat{A}{(s,a)}$, i.e. whether action $a$ is good or bad. If ${\hat{A}{(s,a)}} > 0$, the surrogate objective $J_{\text{PPO}}{(\theta)}$ increases when $a$ becomes more likely. Similarly, if ${\hat{A}{(s,a)}} < 0$, $J_{\text{PPO}}{(\theta)}$ increases when $a$ becomes less likely. Hence, we want to adjust the policy parameters $\theta$ accordingly. However, by clipping the policy ratio $r_{\theta}$, this positive effect on the objective function disappears once we move outside the clip range. This clipping process is conservative as we only clip if the objective function would improve.

<!-- chunk {"id": "body-0070", "role": "body", "section": "PPO", "weight": 1.0} -->

If the policy is changed in the opposite direction such that $J_{\text{PPO}}{(\theta)}$ decreases, $r_{\theta}$ is not clipped due to taking the minimum in Equation. Figure 3 illustrates this explanation. The pseudocode for PPO is presented in Algorithm 6.

<!-- chunk {"id": "body-0071", "role": "body", "section": "PPO", "weight": 1.0} -->

To compute the estimate ${\hat{A}}_{\phi}$ of the advantage function, PPO uses generalized advantage estimation (GAE) to further reduce the variance of gradients. GAE computes the estimated advantage as

<!-- chunk {"id": "body-0072", "role": "body", "section": "PPO", "weight": 1.0} -->

where the first term is treated as independent of $\phi$. GAE relates to the idea of eligibility traces to use both the sampled rewards and the current value function estimate on every time step. By computing such an exponentially weighted estimator, GAE reduces the variance of the policy gradients at the cost of introducing a slight bias to the value function estimate. The hyperparameters $\gamma$ and $\lambda$ both adjust this bias-variance tradeoff. $\gamma$ does so by scaling the value function estimate $\hat{V}$ whereas $\lambda$ controls the dependence on delayed rewards. Note that GAE is a strict generalization of A3C's advantage estimate as Equation reduces to Equation when $\lambda = 1$. The pseudocode for GAE is presented in Algorithm 7.

<!-- chunk {"id": "body-0073", "role": "body", "section": "PPO", "weight": 1.0} -->

Beyond these main innovations, PPO uses several implementational details to improve learning. PPO conducts multiple update epochs for each batch of data such that several gradient descent steps are based on the same transitions to increase sample efficiency and speed up learning. Moreover, PPO commonly augments its surrogate objective with an entropy bonus $H{(\pi_{\theta}{( \cdot \mid s)})}$ and uses multiple actors similarly to A3C. Lastly, we note that further algorithms have been proposed as modifications of PPO, e.g. Phasic Policy Gradients and Robust Policy Optimization, which we will not discuss further as they only modify minor details.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-MPO", "weight": 1.0} -->

In the previous algorithms, we learn a policy from the control perspective by selecting actions to maximize expected rewards. In this subsection, we consider an alternative formulation of RL problems, which casts them as probabilistic inference problems of estimating posterior policies that are consistent with a desired outcome. This problem is then solved via Expectation Maximization (EM). This procedure was first proposed in the off-policy algorithm Maximum a-posteriori Policy Optimization (MPO). Here, we discuss its on-policy variant V-MPO, where the \"V\" in the name refers to learning the value function $V_{\pi}$ instead of $Q_{\pi}$ as in MPO.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-MPO", "weight": 1.0} -->

The main idea of V-MPO is to find a maximum a posteriori estimate of the policy by sequentially finding a tight lower bound on the posterior and then maximizing this lower bound. This problem can be transformed into the objective function

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-MPO", "weight": 1.0} -->

and $\mathcal{L}_{\nu}$ is the trust-region loss

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-MPO", "weight": 1.0} -->

Here, ${sg}{\lbrack{\lbrack \cdot \rbrack}\rbrack}$ is a stop-gradient operator, meaning its arguments are treated as constants when computing gradients, $\eta$ is a learnable temperature parameter, $\nu$ is a learnable KL-penalty parameter, $\varepsilon_{\nu}$ and $\varepsilon_{\eta}$ are hyperparameters, $\mathcal{D}$ is a batch of transitions and $\overset{\sim}{\mathcal{D}} \subset \mathcal{D}$ is the half of these transitions with the largest advantages. We will provide a sketch of how to derive this objective function in the following. We refer the interested reader to Appendix Appendix C for a more detailed derivation.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-MPO", "weight": 1.0} -->

Let ${p_{\theta}{(s,a)}} = {\pi_{\theta}{({a \mid s})}d^{\pi_{\theta}}{(s)}}$ denote the joint state-action distribution under policy $\pi_{\theta}$ conditional on the parameters $\theta$. Let $\mathcal{I}$ be a binary random variable whether the updated policy $\pi_{\theta}$ is an improvement over the old policy $\pi_{\text{old}}$, i.e. $\mathcal{I} = 1$ if it is an improvement. We assume the conditional probability of $\pi_{\theta}$ being an improvement given a state $s$ and an action $a$ is proportional to the following expression

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-MPO", "weight": 1.0} -->

Given the desired outcome $\mathcal{I} = 1$, we seek the posterior distribution conditioned on this event. Specifically, we seek the maximum a posteriori estimate

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-MPO", "weight": 1.0} -->

where $\rho$ is some prior distribution. ${\ln p_{\theta}}{({\mathcal{I} = 1})}$ can be rewritten as

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-MPO", "weight": 1.0} -->

for some distribution $\psi$ over $\mathcal{S} \times \mathcal{A}$. Observe that, since the KL divergence is non-negative, the first term is a lower bound for ${\ln p_{\theta}}{({\mathcal{I} = 1})}$. Akin to EM algorithms, V-MPO now iterates by choosing the variational distribution $\psi$ in the expectation (E) step to minimize the KL divergence in Equation to make the lower bound as tight as possible. In the maximization (M) step, we maximize this lower bound and the prior ${\ln\rho}{(\theta)}$ to obtain a new estimate of $\theta^{\ast}$ via Equation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-MPO", "weight": 1.0} -->

First, we consider the E-step. Under the proportionality assumption, we turn the problem of finding a variational distribution $\psi$ to minimize $D_{KL}{(\psi \parallel p_{\theta_{\text{old}}}{( \cdot, \cdot \mid \mathcal{I} = 1)})}$ into an optimization problem over the temperature $\eta$. This is formulated as a constrained problem subject to a bound on the KL divergence between $\psi$ and the previous state-action distribution $p_{\theta_{\text{old}}}$ while ensuring that $\psi$ is a state-action distribution. To enable optimizing $\eta$ via gradient descent, we transform this constrained problem into an unconstrained problem via Lagrangian relaxation, which emits both the form of the variational distribution

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-MPO", "weight": 1.0} -->

find that using only the highest 50 % of advantages per batch when sampling these expressions, i.e. replacing $\mathcal{D}$ with $\overset{\sim}{\mathcal{D}}$, substantially improves the algorithm. The advantage function $A_{\pi}$ is estimated by ${\hat{A}}_{\phi}$, which is learned as in A3C.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-MPO", "weight": 1.0} -->

Then, in the M-Step we solve the maximum a posterior estimation problem over the policy parameters $\theta$ for the constructed variational distribution $\psi{(s,a)}$ and the thereby implied lower bound. This lower bound, i.e. the first term in Equation, becomes the weighted maximum likelihood policy loss

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-MPO", "weight": 1.0} -->

after dropping terms independent of $\theta$. This loss is computed over the same reduced batch $\overset{\sim}{\mathcal{D}}$ as the temperature loss, effectively assigning out-of-sample transitions a weight of zero. Simultaneously, we want to maximize the prior $\rho{(\theta)}$ according to the maximization problem. V-MPO follows TRPO and PPO to choose a prior such that the new policy is kept close to the previous one, i.e.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-MPO", "weight": 1.0} -->

with learnable parameter $\nu$. However, optimizing the resulting sample-based maximum likelihood objective directly tends to result in overfitting. Hence, a sequence of transformations is applied. First, the prior is transformed into a hard constraint on the KL divergence when optimizing the policy loss. To employ gradient-based optimization, we use Lagrangian relaxation to transform this constrained optimization problem back into an unconstrained problem and use a coordinate-descent strategy to simultaneously optimize for $\theta$ and $\nu$. This can equivalently be written via the stop-gradient operator yielding the trust-region loss.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-MPO", "weight": 1.0} -->

The learnable parameters $\eta$ and $\nu$ are Lagrangian multipliers and hence must be positive. We enforce this by projecting the computed values to small positive values $\eta_{\text{min}}$ and $\nu_{\text{min}}$ respectively if necessary. The pseudocode for V-MPO is depicted in Algorithm 8. As implementational details, V-MPO typically uses decoupled KL constraints for the mean and covariance of the policy in continuous action spaces following. This enables better exploration without moving the policy mean as well as fast learning by rapidly changing the mean without resulting in a collapse of the policy due to vanishing standard deviations. In addition, V-MPO can be used with an off-policy correction via an importance sampling ratio similarly to TRPO and PPO and uses multiple actors following A3C.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

Having outlined the main on-policy policy gradient algorithms, we want to shortly compare them to characterize the main design choices in constructing such algorithms.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

The predominant differences across policy gradient algorithms lie in the estimators ${\hat{\nabla}}_{\theta}J{(\theta)}$ of the policy gradients. We summarize these estimates in Table 1^88^8For V-MPO, we focus on the policy loss, thus ignoring the gradient of the KL loss $\mathcal{L}_{\nu}$ w.r.t. the policy parameters $\theta$ here.. The algorithms can be distinguished along several dimensions with respects to the gradients. First, they use different variance reduction techniques, which are especially reflected in how $Q_{\pi}$ in the policy gradient formula is estimated. Second, various policy regularization strategies are used. Third, the algorithms employ further lower-level details to stabilize learning. We will discuss each of these dimensions in the following.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

Reducing variance is important to stabilize learning and speed up convergence. However, while high variance means algorithms require more samples to converge, bias in the estimates is not resolvable even with infinite samples. All contemporary policy gradient algorithms, i.e. all presented algorithms except REINFORCE, make use of baselines to reduce variance as discussed in Section 3.2 when approximating the unknown $Q_{\pi}$. While REINFORCE samples returns as an unbiased but high-variance estimate, the other algorithms learn a value function $\hat{V}$ to estimate the advantage function $\hat{A}$. Notably, this reduces variance at the cost of introducing bias. Further differences arise from how advantages are estimated, albeit these strategies can be easily transferred between algorithms. PPO uses GAE to estimate advantages, which generalizes the n-step temporal difference estimates used in A3C, TRPO and V-MPO. In addition, V-MPO scales the advantages via the learned temperature $\eta$ and only uses the top 50 % of advantages per batch.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

To stabilize learning beyond variance reduction, several regularization techniques are proposed by TRPO, PPO and V-MPO to limit the change in policies across iterations. TRPO imposes a constraint on the KL divergence between the newly learned and the previous policy. Thus, the policy gradients are not directly applied to update the policy parameters $\theta$ but instead they are postprocessed to yield an approximate solution to this constrained optimization problem. This comes at the cost of algorithmic complexity however. Whereas the other algorithms directly compute the estimated policy gradients via automatic differentiation, TRPO requires the estimation of a hessian and the application of the conjugate gradient algorithm followed by a line search. PPO avoids such complexity by introducing a heuristic, which bounds the probability ratio $\frac{\pi_{\theta}{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}}$, into its objective function. By conservatively clipping this ratio, large policy changes induced by overfitting the advantage function are prevented. This also enables PPO to conduct multiple updates on the same data to accelerate learning.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

V-MPO too limits the KL divergence across policies. The prior distribution is selected such that V-MPO arrives at a similar optimization problem with a penalty on the KL divergence as TRPO. Following TRPO, V-MPO transforms this into a constrained optimization problem, albeit now with the goal of automatically tuning the penalty parameter by applying coordinate-descent to the Lagrangian relaxation of this constrained optimization problem.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

Lastly, we point out that different lower-level details are employed by the discussed algorithm. Except for REINFORCE, all algorithms use several actors, which are potentially updated asynchronously, and average gradients over batches of transitions to further reduce their variance. Here, V-MPO slightly diverges from the other algorithms as it computes a weighted average based on the advantages of the transitions, i.e. with weights

<!-- chunk {"id": "body-0094", "role": "body", "section": "Comparing Design Choices in Policy Gradient Algorithms", "weight": 1.0} -->

A3C and PPO commonly use an entropy bonus to prevent premature convergence to a suboptimal policy by incentivizing a higher standard deviation of the Gaussian output by the policy. We observe that V-MPO does not use an entropy bonus but achieves a comparable effect in continuous action spaces by constraining the policy mean and standard deviation separately. Lastly, TRPO and PPO include an importance sampling correction to compensate for the slight off-policy nature of the algorithms induced by using multiple asynchronous workers. This is also mentioned as an option for V-MPO.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Convergence Results", "weight": 1.0} -->

In this section, we discuss convergence results for policy gradient algorithms from literature. First, we present an overview of different convergence proofs in Section 5.1. Then, we thoroughly present one selected result in Section 5.2.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Literature Overview", "weight": 1.0} -->

Several convergence results have been proposed for policy gradient algorithms. They differ along various dimensions: the specific algorithms covered, the shown strength of convergence, the problem settings and the employed proving techniques. The following overview of convergence results is not intended to be complete but rather shall showcase these differences.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Literature Overview", "weight": 1.0} -->

As previously discussed, REINFORCE uses an unbiased estimator of the policy gradients, which in expectation therefore point in the direction of the true gradients. Hence, under common stochastic approximation assumptions towards the step sizes, REINFORCE can be shown to converge to a locally optimal policy. In the general form of policy gradient algorithms, agnostic to the specific estimator of $Q_{\pi}$, showing convergence is more complex as the estimated gradients are typically biased when using a learned value function. and consider the simplest case where state and action spaces $\mathcal{S}$ and $\mathcal{A}$ are finite and no function approximation is used, i.e. the policy uses a tabular parameterization with one parameter for each state-action combination. Using that the exact policy gradients can be calculated in this case, both studies show the global convergence to an optimal policy with a linear convergence rate.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Literature Overview", "weight": 1.0} -->

and generalize these results to settings with function approximation, albeit under impractical conditions on the approximators, which are required to be linear in their inputs. The extension to function approximation comes at the cost of only being able to proof local convergence using stochastic approximation and the Supermartingale Convergence Theorem.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Literature Overview", "weight": 1.0} -->

Finally, some convergence results exist for the specific algorithms such as TRPO and PPO. TRPO is based on Theorem 4.1, which comes with monotonic improvement guarantees. However, TRPO is only an approximation to the algorithm stemming from Theorem 4.1, so that no such guarantee holds for TRPO in practice. We further remark that PPO is similarly intended as an heuristic of this theoretical algorithm. Nonetheless, efforts have been made to proof the convergence of these practical algorithms. show that a slightly modified version of PPO converges to a globally optimal policy at a sublinear rate under specific assumptions. In particular, they require an overparameterized neural network as the function approximator such that they can use infinite-dimensional mirror-descent to proof the convergence. provide a proof using two time-scale stochastic approximation that PPO converges to a locally optimal policy under more realistic assumptions akin to typical learning scenarios.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Mirror Learning", "weight": 1.0} -->

In this subsection, we focus on the convergence proof provided. While primarily of theoretical interest, we choose to discuss this particular result as it is agnostic to the selected algorithm and parameterization and can hence by applied to a range of policy gradient algorithms. introduce a framework called *mirror learning*, which comes with global convergence guarantees for all policy gradient algorithms that adhere to a specific form. In the following, we follow in deriving their results. We start by giving some definitions, based on which we then present the general form of mirror learning updates. We show that the discussed algorithms largely adhere to this form. Finally, we proof that this implies the convergence to an optimal policy.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Fundamentals of Mirror Learning", "weight": 1.0} -->

From here onwards, we do not explicitly write down the policy parameters, i.e. we omit the subscript $\theta$ when describing a policy $\pi$. define the drift $\mathfrak{D}$ and the neighborhood operator $\mathcal{N}$ as follows.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

Before proving the convergence of mirror learning to an optimal policy, we first show that the discussed policy gradient algorithms can partly be seen as instances of mirror learning, i.e. use updates of the form

<!-- chunk {"id": "body-0103", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

A3C is a direct application of the Policy Gradient Theorem, albeit with a learned advantage function. Thus, at each iteration it approximately solves the optimization problem

<!-- chunk {"id": "body-0104", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

This is the most trivial instantiation of mirror learning by using the trivial drift ${\mathfrak{D}}{( \cdot \mid \cdot )} = 0$ and the trivial neighborhood operator ${\mathcal{N}{( \cdot )}} = \Pi$. The same argumentation also applies to REINFORCE. Note that in practice however, we maximize the expectation over $\pi_{\text{old}}$ rather than $\pi$. For this reason, these are not exact instances of mirror learning.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

with the average-KL ball as the neighborhood operator, i.e.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

and that maximizing over the action-value function is identical to maximizing over the advantage function following the discussion in Section 3.2. Thus, TRPO is a mirror learning instance with the trivial drift ${\mathfrak{D}}{( \cdot \mid \cdot )} = 0$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

Each iteration, PPO searches for

<!-- chunk {"id": "body-0108", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

Using the same technique as before, we can write the first expectation equivalently as ${\mathbb{E}}_{A \sim \pi}\left\lbrack {A_{\pi_{\text{old}}}{(s,A)}} \right\rbrack$. We now focus on the second expectation. We replace the $\min$ operator with a $\max$ and push the first term inside the $\max$ to obtain

<!-- chunk {"id": "body-0109", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

This final expression is non-negative. Moreover, it is zero for $\pi$ sufficiently close to $\pi_{\text{old}}$, i.e. such that for all actions $a \in \mathcal{A}$ we have ${r_{\pi}{({a \mid s})}} = \frac{\pi{({a \mid s})}}{\pi_{\text{old}}{({a \mid s})}} \in {\lbrack{1 - \varepsilon},{1 + \varepsilon}\rbrack}$, because then the $clip$-function reduces to the identity function w.r.t. its first argument. Thus, the derivatives of this expression must also be zero at $\pi{( \cdot \mid s)} = \pi_{\text{old}}{( \cdot \mid s)}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Policy Gradient Algorithms as Instances of Mirror Learning", "weight": 1.0} -->

These properties are the exact conditions for a mapping to be considered a drift in the sense of Definition 5.1. With this preparation, we can now write the PPO update as

<!-- chunk {"id": "body-0111", "role": "body", "section": "Convergence Proof", "weight": 1.0} -->

Now, we present the main theoretical result of.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Now, we empirically compare the discussed policy gradient algorithms. Consistent with the original works, we compare them on the established MuJoCo task suite, accessed through the Gymnasium library. MuJoCo features robotics simulations, where the tasks are to control and move robots of different shapes by applying torques to each joint.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Our implementations build on the PPO implementation from the BRAX library and are written in JAX. For enhanced comparability, all algorithms that estimate advantages use GAE similarly to PPO. Instead of A3C, we use its synchronous variant A2C due to its simpler implementation. Note that A2C exhibits comparable performance as A3C and only differs in that it waits for all actors to collect transitions to update them synchronously. We modify REINFORCE to average gradients over batches of transitions similarly as in the other algorithms since computing one update per environment step is computationally very costly. Note that this is however likely to improve the performance compared to a naive implementation of REINFORCE. We do not tune hyperparameters and keep choices consistent across algorithms where possible. See Appendix Appendix A for the hyperparameters we use. The experiments were run on a standard consumer CPU. All our implemented algorithms and the code for running the experiments can be found at

<!-- chunk {"id": "body-0114", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In our main experiment, we compare the performance of the algorithms in terms of the achieved episodic rewards over the course of training. The performances in different MuJoCo tasks are presented in Figure 4. We observe that PPO outperforms the other algorithms in three of four tasks by achieving higher episodic rewards while learning good policies quickly. The performance difference is most prevalent on the *Humanoid*-task, the most challenging of the four, where PPO learns much stronger policies than the other algorithms. In addition, we find our implementation of PPO to be competitive with common RL libraries as shown in Appendix B.1. V-MPO and TRPO are comparable in performance, with each of the two slightly outperforming the other on two out of four environments. We note that V-MPO is intended for training for billions of environment steps, such that its lower performance compared to PPO in our experiments is expected^1010^10Also see the discussions at on this.. A2C requires more interactions with the environment to reach similar performance levels as V-MPO and TRPO but fails to learn any useful policy in the *Ant*-task.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This slower learning^1111^11Slow in terms of the required environment steps. Note however that A2C runs significantly faster than PPO, TRPO and V-MPO in absolute time due to using less epochs per batch. is at least partially caused by A2C only using a single update epoch per batch. REINFORCE performance worst on all environments, which is unsurprising giving the high variance of gradients in REINFORCE. This also highlights the benefits of the bias-variance trade-off by the other algorithms as discussed in Section 4.6. We find our performance-based ranking of the algorithms to be consistent with literature (e.g., ).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Moreover, we remark that A2C is the only algorithm for which we used an entropy bonus because the learned policies collapsed without it. We showcase this in our expended experiments in Appendix B.2. This underlines the usefulness of the (heuristic) constraints of V-MPO, PPO and TRPO on the KL divergence, which avoid such collapses even without any entropy bonuses. To further investigate this, we show the average KL divergences between consecutive policies throughout training in Figure 5. Here, we approximated the KL divergence using the unbiased estimator

<!-- chunk {"id": "body-0117", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

for all algorithms except TRPO, which analytically calculates the exact KL divergence since it is used within the algorithm. We see that the KL divergences remain relatively constant for all algorithms after some initial movement. TRPO displays the most constant KL divergence, which is explained by its hard constraint. With the chosen hyperparameters, V-MPO uses the same bound on the KL divergence as TRPO, however without strictly enforcing it as outlined in the derivation of V-MPO. Thus, V-MPO's KL divergence exhibits slightly more variance then TRPO and also frequently exceeds this bound. PPO's clipping heuristic achieves a similar effect resulting in a comparable picture. Due to the lack of constraints on the KL divergence, A2C and REINFORCE show slightly more variance. Interestingly, their KL divergences are orders of magnitudes lower than for the other algorithms, especially for REINFORCE (note the logarithmic scale in Figure 5).

<!-- chunk {"id": "body-0118", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We reason this with A2C and REINFORCE using only a singly update epoch per batch, whereas the PPO and V-MPO use multiple epochs and TRPO uses a different update scheme via line search. In Appendix B.3, we provide experimental evidence for this hypothesis. Additionally, we note again that the entropy bonus also stabilizes and limits the KL divergence for A2C as shown in Appendix B.2.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

These findings highlight the benefits of regularization through constraining the KL divergence and incentivizing entropy. Regularization stabilizes learning and prevents a collapse of the policy. At the same time, it allows more frequent updates through multiple epochs per batch, which drastically increases the sample efficiency of the algorithms and speeds up learning.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented a holistic overview of on-policy policy gradient methods in reinforcement learning. We derived the theoretical foundations of policy gradient algorithms, primarily in the form of the Policy Gradient Theorem. We have shown how the most prominent policy gradient algorithms can be derived based on this theorem. We discussed common techniques used by these algorithms to stabilize training including learning an advantage function to limit the variance of estimated policy gradients, constraining the divergence between policies and regularizing the policy through entropy bonuses. Subsequently, we presented evidence from literature on the convergence behavior of policy gradient algorithms, which suggest that they may find at least locally optimal policies. Finally, we conducted numerical experiments on well-established benchmarks to further compare the behavior of the discussed algorithms. Here, we found that PPO outperforms the other algorithms in the majority of the considered tasks and we provided evidence for the necessity of regularization, by constraining KL divergence or by incentivizing entropy, to stabilize training.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We acknowledge several limitations of our work. First, we deliberately limited our scope to on-policy algorithms, which excludes closely related off-policy policy gradient algorithms and the novelties introduced by them. Second, we presented an incomplete overview of on-policy policy gradient algorithms as other, albeit less established, algorithms exist (e.g., ) and the development of further algorithms remains an active research field. Here, we focused on the, in our view, most prominent algorithms as determined by their impact, usage and introduced novelties. Third, the convergence results we referenced rest on assumptions that are quickly violated in practice. In particular, we want to underline that the results based mirror learning rely on the infeasible assumption of finding a global maximizer each iteration. Fourth, while we compared the discussed algorithms empirically and found results to be consistent with existing literature, our analysis is limited to the specific setting we used. Different results may arise on other benchmarks, with different hyperparameters or generally different implementations.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, we note that still many questions remain to be answered in the field of on-policy policy gradient algorithm. So far, our understanding of which algorithm performs best under which circumstances is still limited. Moreover, it is unclear whether the best possible policy gradient algorithm has yet been discovered, which is why algorithm development remains of interest. Similarly, comprehensive empirical comparisons with other classes of RL algorithms may yield further insights on the practical advantages and disadvantages of policy gradient algorithms and how their performance depends on the problem settings. Finally, we observe that still only a limited number of convergence results exist and not even all discussed algorithms are covered by these, e.g., no convergence results exist for V-MPO to the best of our knowledge. Here, further research is needed to enhance our understanding of the convergence behavior of policy gradient algorithms.
