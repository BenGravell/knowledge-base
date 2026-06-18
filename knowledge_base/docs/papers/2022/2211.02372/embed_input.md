<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Planning Using Wassertein Distributionally Robust Deep Q-learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate the problem of risk averse robot path planning using the deep reinforcement learning and distributionally robust optimization perspectives. Our problem formulation involves modelling the robot as a stochastic linear dynamical system, assuming that a collection of process noise samples is available. We cast the risk averse motion planning problem as a Markov decision process and propose a continuous reward function design that explicitly takes into account the risk of collision with obstacles while encouraging the robot's motion towards the goal. We learn the risk-averse robot control actions through Lipschitz approximated Wasserstein distributionally robust deep Q-learning to hedge against the noise uncertainty. The learned control actions result in a safe and risk averse trajectory from the source to the goal, avoiding all the obstacles. Various supporting numerical simulations are presented to demonstrate our proposed approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the tremendous increase in the computing power, many computationally expensive control theory problems can now be addressed using the deep reinforcement learning approaches. So far, the motion planning problem with uncertainty has been investigated from two different perspectives namely the control theory and the reinforcement learning (RL). When stochastic uncertainties are considered in the problems such as path planning, both the above said approaches resort to the powerful stochastic optimization techniques as in to ensure satisfaction of specifications with high probability. However, when assumptions of certain functional forms for the system uncertainties are made in the name of tractability, they may lead to potentially severe miscalculation of risk when the uncertain robot is made to operate in a dynamic environment. Such shortcomings can be addressed through carefully designed risk bounded motion planning approaches using distributionally robust optimization techniques. The interested readers are referred to these non-exhaustive list of papers on risk averse motion planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Risk averse path planning problems emphasize the need for exact propagation of uncertainties. For instance, either the distributions of all the uncertainties or the moments defining the distributions are required to be known in advance or calculated exactly for all time steps to evaluate the risk of obstacle collision as. It is an usual practice to associate a particular distribution to the uncertainty (often Gaussian) just for the sake of tractability. But often in reality, all we have is just a collection of samples of the uncertainty and trying to fit a distribution to it may cause undue risk. On a parallel note, the central idea of safe and robust RL as described in is to learn control policies for agents that encourage safety or robustness, and to design methods that can formally certify the safety of a learned control policy. For instance, a maximum entropy based lower bound on a robust RL objective was used to learn policies that are robust to some disturbances in the dynamics and the reward function. But analysis of safe and robust RL algorithms with distributional uncertainty has received very less attention. Authors in use the Wasserstein distributionally robust deep Q-learning to hedge against the distributional uncertainty and approximately solve the Bellman equation associated with the deep Q-learning approach given.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we stick to the sample based uncertainty modeling of process noise and take a similar approach as, and further use the Lipschitz constant based approximations advocated in Theorem 5 of to learn risk-averse robot control actions. A similar problem was investigated, albeit with usual Gaussian assumptions and no formal risk consideration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contributions:* This article leverages powerful results in deep reinforcement learning theory and distributionally robust optimization to learn control policies for robots to operate in a risk-averse manner in an environment.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

we learn safe robot control actions at all the state space positions to infer a trajectory to move from source to goal by avoiding all obstacles. We account for the uncertainty due the robot initial states and the process noise through reward function design and learn the risk averse control actions using approximated Wasserstein distributionally robust $Q$-learning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

we demonstrate our proposed approach using a series of numerical simulations and show the effectiveness of our proposed approach.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following a short summary of notations and preliminaries, the rest of the paper is organized as follows. In §II, the risk-averse path planning problem associated with the uncertain robot system is presented. The Wasserstein distributionally robust $Q$-learning approach is discussed in §III. The proposed idea is then demonstrated using a numerical simulation in §IV. Finally, the paper is closed in §V. Due to the page restrictions, some proofs are available in the appendix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

The robot is modeled as a stochastic discrete time linear time invariant system and it is assumed to move within a bounded environment $\mathcal{X} \subset {\mathbb{R}}^{n_{x}}$. There are in total $M \in {\mathbb{Z}}_{+}$ obstacles in the environment, each disjoint with the other and they are collectively referred as $\mathcal{O}$ with $|\mathcal{O}| = M$. Further, each obstacle is assumed to be static and of convex polytope shape. Then, the free space that the robot can traverse namely $\mathcal{X}_{\mathbf{f}\mathbf{r}\mathbf{e}\mathbf{e}} \subset \mathcal{X}$ is given by

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

where $\mathcal{X}_{\mathbf{o}\mathbf{b}\mathbf{s}}^{(i)} \subset \mathcal{X}$ is the space occupied by the obstacle $i \in \mathcal{O}$. Similar to the obstacles, we define a goal region, $\mathcal{X}_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}} \subset \mathcal{X}$, that is both static and circular in shape with constant radius $R_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}} > 0$. This is a fair assumption ^11^1Our problem formulation works perfectly fine even with convex polytopic goal regions too.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

The robot is limited to move within the environmental boundaries whose limits are $\lbrack\underset{¯}{p},\overline{p}\rbrack$ with ${\underset{¯}{p},\overline{p}} \in {\mathbb{R}}^{n_{r}}$. Hence, just like the obstacles, the environmental boundaries are also treated as terminal states. The state of the robot at time $k$ is represented as $x_{k} \in {\mathbb{R}}^{n_{x}}$ and it may include the robot's position, velocity and other states of interest so that $n_{x} \geq n_{r}$. The robot is controlled through a control input $u_{k}$ which is selected from $\mathcal{U}$ such that $u_{k} \in \mathcal{U} \subseteq {\mathbb{R}}^{n_{u}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

Given the above description, we define the dynamics (evolution) of the robot in $\mathcal{X}$ as

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

The robot is subject to a process disturbance $w_{k} \in {\mathbb{R}}^{n_{x}}$. The time invariant true distribution of the process noise $w_{k}$ at any time $k$ namely ${\mathbb{P}}_{w}$ is unknown, however it is assumed that a collection of $N \in {\mathbb{N}}$ independent samples of $w_{k}$ are available beforehand. That is, an i.i.d. sequence ${{\hat{w}}_{1},\ldots,{\hat{w}}_{N}} \in {\mathbb{R}}^{n_{r}}$ is assumed to be known in advance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Robot & Environment Model", "weight": 1.0} -->

However, at any time $k$, the distribution of $w_{k}$ can be approximated through the following empirical distribution, ${\hat{\mathbb{P}}}_{w} = {\frac{1}{N}{\sum\limits_{i = 1}^{N}\delta_{{\hat{w}}_{i}}}}$, where $\delta_{w_{i}}$ is the Dirac delta function. Note that, ${\hat{\mathbb{P}}}_{w}$ need not necessarily be the true distribution of the $w_{k}$. This is precisely where our approach differs from the existing safe RL literature, where it is a common practice to either assume a distribution for $w$ or bound for $w$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Main Problem Statement: Given the uncertain robot evolution as in with sample based process noise model, we learn the risk-averse control policy for all state space positions of the robot and hence design a trajectory for the robot from its initial state $x_{0}$ to the goal region $\mathcal{X}_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}}$ without colliding with any of the obstacles $\mathcal{O}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

Given that we have to learn what actions to take provided we land anywhere in $\mathcal{X}$ given the uncertainty in the distributional information of $w$, taking control theory perspective can be hard. Hence, we resort to the RL approaches to address this shortcoming. That is, the above planning problem can be cast as a Markov decision process that consists of the tuple $\langle\mathcal{S},\mathcal{A},{\mathbb{P}},r\rangle$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

Here, $\mathcal{S} \subset {\mathbb{R}}^{n_{\mathcal{S}}}$ is the state space, $\mathcal{A} \subset {\mathbb{R}}^{n_{\mathcal{A}}}$ is a finite set called the action space with ${|\mathcal{A}|} \in {{\mathbb{N}}_{+}\backslash\, 0}$, $r:{\mathcal{S}\rightarrow{\mathbb{R}}}$ is the reward function and ${\mathbb{P}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$ is the state transition probability which defines the probability distribution over the next states. We denote by $\hat{a}$, the null action where it does not cause a change in the position of the robot.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

At step $k$, the state $s_{k} \in \mathcal{S}$ contains the state of the robot $x_{k}$, the center of the goal $p_{g}$, and the centers of the obstacles $p_{\mathbf{o}\mathbf{b}\mathbf{s}}^{(i)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

where, $n_{\mathcal{S}} = {{({2 + M})}n_{x}}$, and $i = {1,\ldots,M}$. The state $s_{k}$ is referred as a *terminal state* if $x_{k} \in {\mathcal{X}_{\mathbf{o}\mathbf{b}\mathbf{s}} \cup \mathcal{X}_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}}}$ or if $x_{k} \notin \mathcal{X}$ and as *non-terminal state* otherwise. The dimensions of MDP state $s_{k}$ depend on the number of obstacles in the environment. Increasing the number of obstacles will cause the dimension of $s_{k}$ to increase as well ^22^2The increase in the dimension of $s_{k}$ is the price that we need to pay to handle potentially dynamic obstacles..

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

An action $a_{k} \in \hat{\mathcal{A}}$ performed at state $s_{k} \in \mathcal{S}$, will cause a transition to a new state $s_{k + 1} \in \mathcal{S}$ with the probability ${\mathbb{P}}{({s_{k + 1} \mid {s_{k},a_{k}}})}$. After the transition, a deterministic reward $r_{k} = {r{(s_{k + 1})}}$ is obtained based on the state where we land. The actions, $a_{k} = {\pi{(s_{k})}}$ are chosen based on a deterministic policy $\pi:{\mathcal{S}\rightarrow\hat{\mathcal{A}}}$. The set of all admissible control policies is denoted by $\Pi$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

A sequence $\tau_{k}^{(\pi)}:={(s_{k},a_{k},s_{k + 1},a_{k + 1},\ldots,s_{K - 1},a_{K - 1},s_{K})}$ with a terminal state $s_{K}$ is called a sample path under the policy $\pi \in \Pi$. The cumulative discounted reward for this sample path is

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

where $\gamma \in {\lbrack 0,1\rbrack}$ is the discount factor. The discount factor is used in order to take in to account the future rewards. The value function is defined as the expected value calculated for the discounted returns starting from state $s$ and following policy $\pi$ and the Q-function is defined as the expected discounted return if action $a$ is taken at state $s$ and following policy $\pi$. That is,

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Markov Decision Process (MDP) Formulation", "weight": 1.0} -->

The Q values for a state determine what action is the best to take. Hence, the *modified* policy $\pi$, tailored for this path planning problem is related to the Q-function as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Reward Function Design & Its Approximation", "weight": 1.0} -->

In this work, we consider rewards that depend only on $s_{k + 1}$ and it includes a penalty for both traveling and collision with obstacles along with an incentive for being in the goal. That is,

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Reward Function Design & Its Approximation", "weight": 1.0} -->

where $\mathbf{r}_{\mathbf{t}\mathbf{r}\mathbf{a}\mathbf{v}\mathbf{e}\mathbf{l}}$ is the travel penalty, $\mathbf{r}_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}}$ is the reward for reaching the goal, and $\mathbf{r}_{\mathbf{o}\mathbf{b}\mathbf{s}}$ is the penalty for obstacle collision. The discontinuity in the reward function $\hat{r}{( \cdot )}$ due to the switching in causes its Lipschitz constant $L_{\hat{r}}\rightarrow\infty$ when we approximate the $Q$-function later on using a neural network. Hence, it has to be approximated by a Lipschitz continuous function $r{(s^{\prime})}$. The radial step function associated with switching to the goal reward can be approximated as

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Reward Function Design & Its Approximation", "weight": 1.0} -->

A similar structure, $f_{\mathbf{b}\mathbf{o}\mathbf{r}}{(p_{r})}$ can be used for the borders that takes the distance to the borders defined using limits $\lbrack\underset{¯}{p},\overline{p}\rbrack$ across all the position dimensions. The step function associated with switching to the obstacle collision penalty will have the convex polytope shape as its support. Let $\mathbf{q}:={\{ q_{i}\}}_{i = 1}^{n_{r}}$, with each $q_{i}$ being a large, positive and even integer. Then, using the modified distance function ^33^3For $n_{r} \geq 2$, the distance function should be defined using the level set of the convex obstacle obtained from its compact support and smooth approximation can be done using the $\tanh$ (or logistics) function in ${\mathbb{R}}^{n_{r}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Reward Function Design & Its Approximation", "weight": 1.0} -->

where, $i \in \mathcal{O}$. Then, the Lipschitz continuous approximation $r{(s^{\prime})}$ of the original reward function $\hat{r}{(s^{\prime})}$ is given by

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning Risk-Averse Control Actions", "weight": 1.0} -->

If the Q-values for a system is known, a policy $\pi$ can be used to maximize the expected returns. In order to estimate the Q-values, the standard temporal difference learning based Q-Learning procedure is usually employed,. From now, we drop the superscript $\pi$ on $Q^{\pi}{(s,a)}$ for the brevity of notation. We now define the Bellman operator, $\mathcal{T}:{{\mathbb{R}}^{\mathcal{S} \times \hat{\mathcal{A}}}\rightarrow{\mathbb{R}}^{\mathcal{S} \times \hat{\mathcal{A}}}}$ as

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning Risk-Averse Control Actions", "weight": 1.0} -->

where the outer expectation is over the next states $s^{\prime}$, which come from the transition probability ${\mathbb{P}}{({s^{\prime} \mid {s,a}})}$. Given the continuous state space setting, we propose to use the Deep Q Learning (DQN) approach as, which estimates the Q values by using a deep neural network. Specifically, it utilizes two neural networks namely: i) Q-network $Q{(s,a,\theta)}$, and ii) the target network $Q{(s,a,\theta^{-})}$. The Q network is trained by experience replay, where a random batch of experiences are sampled from the memory buffer and with the Bellman equation, the targets are calculated. For an experience $\langle s,a,r,s^{\prime}\rangle$, the target $y$ is calculated as

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A The Lipschitz Approximated Wasserstein Distributionally Robust Deep Q-Learning", "weight": 1.0} -->

The Q-function estimation defined in section II-B Formulation ‣ II Problem Formulation ‣ Path Planning Using Wassertein Distributionally Robust Deep Q-learning") will be formulated as a distributionally robust optimization problem. Taking an action $a$ at state $s$ causes the transition to an unknown state $s^{\prime}$ with unknown distribution ${\mathbb{P}}_{s^{\prime}} \triangleq {{\mathbb{P}}{({s^{\prime} \mid {s,a}})}}$. For brevity, $a$ will be omitted in the notation from now.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The true distribution ${\mathbb{P}}_{s^{\prime}}$ is a light-tailed distribution. That is, ${\exists p} > 1$ such that,

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A1 The Wasserstein Ambiguity Set", "weight": 1.0} -->

Given a robot state $x_{k} \in \mathcal{X}$ and an input $a_{k} \in \hat{\mathcal{A}}$, an empirical distribution for $x_{k + 1}$ is given,

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A1 The Wasserstein Ambiguity Set", "weight": 1.0} -->

By knowing the state of the robot $x_{k}$, the full state $s_{k}$ can be obtained by using the positions of the goal and obstacles of the current environment (which do not depend on the position of the robot), since these stay constant during an episode. For ease of notation, we refer to the next state $s_{k + 1}$ as $s^{\prime}$, and the samples of $s^{\prime}$ obtained, are denoted as ${\hat{s}}^{\prime{(i)}}$ for $i = {1,{\ldotsN}}$. Then, the empirical distribution is given by ${\hat{\mathbb{P}}}_{s^{\prime}} = {\frac{1}{N}{\sum\limits_{i = 1}^{N}\delta_{{\hat{s}}^{\prime{(i)}}}}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A1 The Wasserstein Ambiguity Set", "weight": 1.0} -->

When an action $a$ is performed while in state $s$, the nominal distribution for the center of the Wasserstein ball will be ${\hat{\mathbb{P}}}_{s^{\prime}}$, and the worst case transition will be coming from a distribution that is inside this ball. We define the ambiguity set $\mathcal{B}_{s,a}$,

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A1 The Wasserstein Ambiguity Set", "weight": 1.0} -->

The Wasserstein ball radius $\epsilon_{s^{\prime}}$ is chosen such that the true distribution ${\mathbb{P}}_{s^{\prime}}$ lies within this Wasserstein ball with probability greater than $1 - \beta$. The $\beta$ parameter will determine the allowed risk factor for the solution. A smaller $\beta$ will result in a larger radius which causes the generated policy to be much more risk averse and vice-versa. Since, the radius $\epsilon_{s^{\prime}}$ quantifies the amount of trust (distrust) that we have over the ${\hat{\mathbb{P}}}_{s^{\prime}}$, it is chosen such that

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A2 Approximated Solution to The Wasserstein Distributionally Robust $Q$-learning Problem", "weight": 1.0} -->

We define the distributionally robust Bellman operator $\hat{\mathcal{T}}:{{\mathbb{R}}^{\mathcal{S} \times \hat{\mathcal{A}}}\rightarrow{\mathbb{R}}^{\mathcal{S} \times \hat{\mathcal{A}}}}$ to represent the worst case expected returns, so that risk can be incorporates into the Q-values. That is,

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A2 Approximated Solution to The Wasserstein Distributionally Robust $Q$-learning Problem", "weight": 1.0} -->

Since the Q-function is approximated using a neural network with hidden layers and non-linear activation functions, $h{(s^{\prime})}$ turns out to be a non-convex function of the states. Since an exact solution to the infinite dimensional problem using duality theory is difficult to find when the objective function is non-convex, we resort to the Lipschitz constant based approximation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A3 Calculating the Lipschitz Constant $L_{h}$ of $h{(s^{\\prime})}$", "weight": 1.0} -->

The Lipschitz constant for $h_{r}{(s^{\prime})}$ and $h_{Q}{(s^{\prime})}$ can be calculated or estimated independently and then combined to get the Lipschitz constant of $h{(s^{\prime})}$. The second part of $h{(s^{\prime})}$ given by $h_{Q}{(s^{\prime})}$ contains the Q-function which is approximated by a neural network. The neural network takes the state $s$ as an input and returns the Q-values for each action. An upper bound for the Lipschitz constant of a dense neural network with ReLU activation functions can be approximated using the LipSDP package developed.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We consider the robot to be moving in an environment $\mathcal{X} \subset {\mathbb{R}}^{2}$ with the limits of $\mathcal{X}$ being ${\lbrack{- 10},10\rbrack}^{2}$ in both dimensions ^44^4We believe that such a toy example is rich enough to demonstrate our proposed approach given the infinite dimensional DRDQN objective.. There are in total two obstacles that are circular in shape (most simple convex shape assumption made for the sake of simplicity) and a goal region with equal radius namely, $R_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}} = R_{\mathbf{o}\mathbf{b}\mathbf{s}}^{} = R_{\mathbf{o}\mathbf{b}\mathbf{s}}^{} = 2$. The robot moves within $\mathcal{X}$ according to the following dynamics,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The state of the robot $x_{k}$ represents the position of the robot in $\mathcal{X} \subset {\mathbb{R}}^{2}$. The process disturbance $w_{k} \in {\mathbb{R}}^{2}$ shifts the position of the robot by a random amount in each axis. For simulation purposes, we considered $10^{4}$ samples of process noise $w$ that were sampled from distributions with zero mean and covariance being equal to $0.15I_{2}$. The action space $\hat{\mathcal{A}}$ consists of $\left| \hat{\mathcal{A}} \right| = 9$ actions where each action is a ${\mathbb{R}}^{2}$ vector with unit norm, that represent a step that can be taken in one of the 8 equally spaced radial directions along with a null action. The robot takes a step in a specified direction for each action and stays still if a null action is selected.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Discussion of Results", "weight": 1.0} -->

The hyperparameter details of the training results are made available in the supplementary material. The resulting policy and the state values for the trained models can be seen in Figure 1. The arrows represent the action that the policy gives at the respective robot position and goal/obstacle positions. The heatmap represents the same values with color but in higher resolution to better understand the decision boundaries. The figures on the right side of Figure 1 represent the value of each state $s$ which can be computed by ${\max_{a \in \mathcal{A}}Q}{(s,a)}$. It can be seen that the rewards propagate from the goal and the obstacles. Further, the resulting learned policy restricts the robot moving between the obstacles and there exists a boundary around the obstacles. When compared with the DQN model, our solution exhibits the most minimum pessimism (risk aversion). This difference is due to the fact that DQN learns the expected rewards, while the DRDQN learns the worst case expected rewards.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Discussion of Results", "weight": 1.0} -->

Due to the noise samples used in DRDQN model with $\epsilon_{s^{\prime}}$ calculated using, learning the policy occurs in less steps compared to the DQN model. However DRDQN can take more time since the computational load is higher for calculating the targets. The DRDQN with $\epsilon_{s^{\prime}} = 0$ is virtually the same as DQN as it learns faster since it calculates the expected values in more accurately compared to that of DQN which uses only one sample. DQN achieves a lower score overall, since the method only uses one experience per experience replay to train itself, while DRDQN uses the samples provided which results in a much better approximation of (worst case) expected future returns. The models have been evaluated by running $10^{5}$ episodes each with random goal/obstacle configurations, for three different noise distributions. As seen in Table I both versions of DRDQN have a higher average total reward compared to DQN with lower variances.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Discussion of Results", "weight": 1.0} -->

Also in Table II, the percentage of trajectories that have reached the goal, collided with an obstacle or border or have not reached the goal or collided, has been provided. It can be inferred that as the covariance of the noise increases, the DRDQN model is able to maintain a low collision rate due to the worst case approximations. Any safe RL algorithm that assumes a particular distribution for $w$ or a bound for $w$ has a greater chance to fail in this setting as the unknown true noise distribution will lead to different transitions than the one assumed.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed a path planning using approximated Wasserstein distributionally robust deep Q-learning approach. Through carefully designed reward function, we showed how to learn safe control policy for uncertain robots operating in an environment. Our numerical simulation results demonstrated our proposed approach.\
