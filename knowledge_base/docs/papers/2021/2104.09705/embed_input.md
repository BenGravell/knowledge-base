<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Neural Tree Expansion for Multi-Robot Planning in Non-Cooperative Environments

Topics include Robotics, Neural networks, Real-time systems, Online algorithms, Planning, Control, Monte Carlo methods, Neural tree expansion, NTE, Monte Carlo tree search.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a self-improving, Neural Tree Expansion (NTE) method for multi-robot online planning in non-cooperative environments, where each robot attempts to maximize its cumulative reward while interacting with other self-interested robots. Our algorithm adapts the centralized, perfect information, discrete-action space method from AlphaZero to a decentralized, partial information, continuous action space setting for multi-robot applications. Our method has three interacting components: (i) a centralized, perfect-information "expert" Monte Carlo Tree Search (MCTS) with large computation resources that provides expert demonstrations, (ii) a decentralized, partial-information "learner" MCTS with small computation resources that runs in real-time and provides self-play examples, and (iii) policy & value neural networks that are trained with the expert demonstrations and bias both the expert and the learner tree growth. Our numerical experiments demonstrate Neural Tree Expansion's computational advantage by finding better solutions than a MCTS with 20 times more resources.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The resulting policies are dynamically sophisticated, demonstrate coordination between robots, and play the Reach-Target-Avoid differential game significantly better than the state-of-the-art control-theoretic baseline for multi-robot, double-integrator systems. Our hardware experiments on an aerial swarm demonstrate the computational advantage of Neural Tree Expansion, enabling online planning at 20Hz with effective policies in complex scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-agent interactions in non-cooperative environments are ubiquitous in robotic applications such as self-driving, space exploration, urban air mobility, and human-robot collaboration. Planning, or sequential decision-making, in these settings requires a prediction model of the other agents, which can be generated through a game theoretic framework.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, the success of AlphaZero at the game of Go has popularized a self-improving machine learning algorithm: bias a Monte Carlo Tree Search with value and policy neural networks, use the tree statistics to train the networks with supervised learning and then iterate over these two steps to improve the policy and value networks over time. However, this algorithm is designed for classical artificial intelligence tasks (e.g. chess or Go), and applications in multi-robot domains require different assumptions: continuous state-action, decentralized evaluation, partial information, and limited computational resources. To the best of our knowledge, our work is the first to provide a complete multi-robot adaption from algorithm design to hardware experiment of the AlphaZero method.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The overview of our algorithm is shown in Fig. 1. The key algorithmic innovation of our approach is to create two distinct MCTS policies to bridge the gap between high-performance simulation and real-world robotic application: the "expert" tree search is centralized and has access to perfect information and large computational resources, whereas the "learner" tree search is decentralized and has access to partial information and limited computational resources. During the offline phase, the neural networks are trained in an imitation learning style using the self-play states of the learner and the high-quality demonstrations of the expert. The expert's high-quality demonstrations enable policy improvement through iterations to incrementally improve the policy and value networks. The learner's self-play samples states that should appear more frequently at runtime. At deployment, each robot uses the learner to effectively plan online with partial information and limited computational budget. Our contribution is the Neural Tree Expansion algorithm that extends AlphaZero methods to (i) decentralized evaluation with local information, (ii) continuous state-action domain, and (iii) limited computational resources.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate our method in simulation and experiment. We demonstrate numerically that our approach generates compact trees of similar or better performance with 20 times fewer nodes, and the resulting policies play the Reach-Target-Avoid differential game with double-integrator dynamics significantly better than the current state of the art. Our method is compatible with arbitrary game specifications; we demonstrate this by generating visual examples of canonical games in Fig. 2 and empirical evaluation of the Reach-Target-Avoid game for double-integrator and $3$D Dubin's vehicle dynamics in Sec. IV. Our hardware experiments demonstrate that the solutions are robust to the gap between simulation and real world and neural expansion generates compact search trees that are effective real-time policies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: Our work relates to multiple communities: planning, machine learning, and game theory. Planning, or sequential decision-making, problems can be solved in an online setting with Monte Carlo Tree Search (MCTS). MCTS searches through the large decision-making space by rolling out simulated trajectories and biasing the tree growth towards areas of high reward. MCTS was first popularized by the Upper Confidence Bound for Trees algorithm that uses a discrete-action, multi-armed bandit solution to balance exploration and exploitation in node selection. Recent work uses a non-stationary bandit analysis to propose a polynomial, rather than logarithmic, exploration term. As an anytime algorithm, the space and time complexity of MCTS is user-determined by the desired number of simulations. Recent finite sample complexity results of MCTS show the error in root node value estimation converges at a rate of the order $n^{- {1/2}}$ where $n$ is the number of simulations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Application of MCTS to a dynamically-constrained robot planning setting requires extending the theoretical foundations to a continuous state and action space. In general, the recent advances in this area answer two principal questions: i) how to select an action, and ii) when a node is fully expanded. Regarding the former question, some solutions select an action using the extension of the multi-armed bandit in continuous domains, whereas our approach uses a policy network to generate actions. Regarding the latter question, a popular method to determine whether a node is expanded is to use progressive widening and variants; we adapt one such method, the Polynomial Upper Continuous Trees (PUCT) algorithm. Despite the advance in theory for continuous action spaces, there have been relatively few studies of biasing continuous MCTS with deep neural networks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key idea of AlphaZero is using MCTS as a policy improvement operator; i.e. given a policy neural network to guide MCTS, the resulting search produces an action closer to the optimal solution than that generated by the neural network. Then, the neural network is trained with supervised learning to imitate the superior MCTS policy, matching the quality of the network to that of MCTS in the training domain. By iterating over these two steps, the model improves over time. The first theoretical analysis of this powerful method is recently shown for single-agent discrete action space problems. In comparison, our method is applied to a continuous state-action, multi-agent setting. Whereas AlphaZero methods use the policy network to bias the node selection process, i.e. given a list of actions, select the best one, our policy network is an action generator for the expansion process to create edges to children, i.e. given a state, generate an action. A neural expansion operator has previously been explored in motion planning, but not decision-making.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, our method's supervised learning step is closer to imitation learning, as used in DAgger, because the learner benefits from an adaptive dataset generation of using self-play to query from an expert.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although the AlphaZero methods use a form of supervised learning to train the networks, they can be classified as a reinforcement learning method because the networks are trained without a pre-existing labelled dataset. Policy gradient is a conventional reinforcement learning solution and there are many recent advances in this area. Adding an underlying tree structure to deep reinforcement learning provides a higher degree of interpretability and a more stable learning process, enabled by MCTS's policy improvement property.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to data-driven methods, traditional analytical solutions can be studied and derived through differential game theory. The game we study, Reach-Target-Avoid, was first introduced and solved for simple-motion, 1 vs. 1 systems. Later, multi-robot, single-integrator solutions have been proposed. Solutions considering multi-robots with non-trivial dynamics, such as the double-integrator, are an active area of research. Shepherding, herding, and perimeter defense are variants of the Reach-Target-Avoid game and are also active areas of research.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Notation: We denote the learning iteration with $k$ and the physical timestep with a subscript $t$, which is suppressed for notation simplicity, unless necessary. Robot-specific quantities are denoted with $i$ or $j$ superscript, and, in context, the absence of superscript denotes a joint-space quantity, e.g. the joint state vector is the vertical stack of all individual robot vectors, $\mathbf{s}_{t} = {\lbrack\mathbf{s}_{t}^{1};\ldots;\mathbf{s}_{t}^{N}\rbrack}$ where $N$ is the number of robots.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 can be relaxed by considering specialized variants that are not the focus of this work. For example, realistic robotic scenarios with localization uncertainty from measurement noise can be handled with the observation widening variant.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Problem Statement: At time $t$, each robot $i$ makes a local observation, $\mathbf{z}^{i}$, uses it to formulate an action, $\mathbf{a}^{i}$, and updates its state, $\mathbf{s}^{i}$, according to the dynamical model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $\mathcal{U}^{i} \subseteq \mathcal{A}^{i}$ is the set of available actions (e.g. bounded control authority constraints), and $\mathcal{X}^{i} \subseteq \mathcal{S}^{i}$ is the set of safe states (e.g. collision avoidance) and $\mathbf{s}_{0}^{i}$ is the initial state condition. The optimization problems for each robot $i$ are simultaneously coupled through the evolution of the global state vector $\mathbf{s}$, where each robot attempts to maximize its own reward function $\mathcal{R}^{i}$. We evaluate our method on canonical cases and present visualizations in Fig. 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Reach-Target-Avoid Game: An instance of the above formulation is the Reach-Target-Avoid game for two teams of robots, where team $A$ gets points for robots that reach the goal region, and team $B$ gets points for defending the goal by tagging the invading robots first. The teams are parameterized by index sets $\mathcal{I}_{A}$ and $\mathcal{I}_{B}$, respectively, where the union of the two teams represents all robots, ${\mathcal{I}_{A} \cup \mathcal{I}_{B}} = \mathcal{I}$. An example of the Reach-Target-Avoid game is shown in Fig. 2(c), where the red robots try to tag the blue robots before the blue robots reach the green goal region. The $x$ and $o$ on the trajectory indicates tagged state and reached goal.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

(a) NTE finds the intuitive value and policy function for the “bugtrap” motion planning problem. The robot starts at the orange dot, and terminates at the green square after reaching the goal.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

(b) The state trajectories generated by NTE approximate the primary solution and barrier surface for the “homicidal chauffeur” game. The plot is shown in Isaac’s reduced space with an example trajectory in blue terminating in a capture condition.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

(c) NTE scales to high dimensional team games for the 10 agent vs. 10 agent “Reach-Target-Avoid” with double-integrator dynamics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

(d) NTE is compatible with arbitrary dynamics, here is the “Reach-Target-Avoid” game with 3D Dubin’s vehicle dynamics.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $\mathbf{p}^{i}$ and $\mathbf{v}^{i}$ denote position and velocity and $\Delta_{t}$ denotes the simulation timestep. We use a simultaneous turn game formulation where at a given timestep, each team's action is chosen without knowledge of the other team's action.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

When a robot exits the admissible state or action space, or a robot on team $A$'s position is within an $r_{g}$ radius about the goal position $\mathbf{p}_{g}$, it becomes inactive.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Observation Model: Under Assumption 1, for each robot $i$, we define a measurement model that is similar to visual relative navigation $h^{i}:{\mathcal{S}\rightarrow\mathcal{Z}^{i}}$, which measures the relative state measurement between neighboring robots, as well as relative state to the goal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $\mathbf{g}$ is the goal position embedded in the state space, e.g. for 2D double-integrator $\mathbf{g} = {\lbrack\mathbf{p}_{g};0;0\rbrack}$. Then, $\mathcal{N}_{A}^{i}$ and $\mathcal{N}_{B}^{i}$ denote the $i^{\text{th}}$ robot's neighbors on team $A$ and $B$, respectively.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Reward: The robot behavior is driven by the reward function; the inter-team cooperation behavior is incentivized by sharing the reward function and intra-team adversarial behavior is incentivized by assigning complementary reward functions only dependent on global state, ${{\mathcal{R}^{i}{(\mathbf{s})}} = {- {\mathcal{R}^{j}{(\mathbf{s})}}}},{{{\forall i} \in \mathcal{I}_{A}},{j \in \mathcal{I}_{B}}}$. The reward can be defined by a single, robot-agnostic game reward, $\mathcal{R}{(\mathbf{s})}$ that team $A$ tries to maximize and team $B$ tries to minimize.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

i.e. the value is the number of team $A$ robots in the goal region. The indicator function payoff is known to be sparse and makes traditional search and reinforcement learning techniques ineffective. The game termination occurs when all robots on team $A$ are inactive; typically when they have reached the goal or been tagged by a robot on team $B$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "NTE Algorithm Description", "weight": 1.0} -->

We present the meta-algorithm, the expert and learner NTE, and the policy and value neural networks.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

The input of the meta-learning is the POSG game described in Sec. II, and the outputs are the policy and value neural networks, $\overset{\sim}{\pi}$ and $\overset{\sim}{V}$. The goal of the meta-learning is to improve the models across learning iterations, especially in relevant state domains, such that at runtime, the robots can evaluate the learner.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

where $\pi^{\ast}$ is the unknown optimal policy function that inputs a joint state and returns a joint action, ${\overset{\sim}{\pi}}_{k}$ is the policy network we train, and $k,m$ are learning iteration indices. Specifically, we train robot-specific policies ${\overset{\sim}{\pi}}_{k}^{i}$ that map local observation to local action and compose them together to create the joint policy ${\overset{\sim}{\pi}}_{k} = {\lbrack{\overset{\sim}{\pi}}_{k}^{1};\ldots;{\overset{\sim}{\pi}}_{k}^{|\mathcal{I}|}\rbrack}$ that maps joint observation, $\mathbf{z}$, to joint action, $\mathbf{a}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

Adapting the proof concept in to our setting, the policy improvement can be shown by validating two properties and then iterating: (i) bootstrap

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

and, after generating an appropriate dataset, (ii) learning

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

where ${\overset{\sim}{V}}_{k}$ is the value network and $\pi^{e}$ is the expert that maps state to joint action while biased by the policy and value neural networks. Intuitively, the bootstrap property of MCTS generates a dataset of policy samples superior to that of the policy network, and then the supervised learning property matches the quality of the policy network to the quality of the new dataset.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

Validating these two properties drives the design of our meta-learning algorithm in Algorithm 1. At each learning iteration $k$, each robot's policy network is trained in the following manner: a set of states is generated from self-play of the multi-agent learners, $\pi_{k}^{le}$ and then the expert, $\pi_{k}^{e}$, searches on these states to create a dataset of learning targets for the supervised learning. The value network, ${\overset{\sim}{V}}_{k}$ is trained to predict the outcome of the game if each team were to play with the joint policy network ${\overset{\sim}{\pi}}_{k}$. Because the centralized expert has perfect information, coordination and large computational resources, the bootstrap property is more likely to hold. Furthermore, as the learner generates state space samples through self-play, the dataset is dense in frequently visited areas of the state space, and the models will be more accurate there, validating the learning property.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Meta Self-Improving Algorithm", "weight": 1.0} -->

Finally, we specify a simple POSG generator in Line 1 of Algorithm 1 to select opponent policies and game parameters for self-play.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Neural Tree Expansion", "weight": 1.0} -->

In order to specify the expert and learner policies, we first explain their common search tree algorithm shown in Algorithm 2 and adapted from to our setting. For a complete treatment of MCTS, we refer the reader to.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Neural Tree Expansion", "weight": 1.0} -->

The biased MCTS algorithm begins at some start state $\mathbf{s}$ and grows the tree until its computational budget is exhausted, typically measured by the number of nodes in the tree, $L$. Each node in the tree is a state, $\mathbf{s}$, each edge is an action $\mathbf{a}$, and each child is the new state after propagating the dynamics. Each node in the tree, $n$, is initialized with a state vector and an action edge to its parent node, $n^{p}$, i.e. $n = {\text{Node}{(\mathbf{s},{(n^{p},\mathbf{a})})}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Neural Tree Expansion", "weight": 1.0} -->

Each node stores the state vector, $S{(n)}$, the number of visits to the node, $N{(n)}$, its children set, $C{(n)}$, and its action set, ${{A{(n,n^{\prime})}},{\forall n^{\prime}}} \in {C{(n)}}$. The growth iteration in the main function, Search, has four steps: (i) node selection, Select, selects a node to balance exploration of space and exploitation of rewards (ii) node expansion, Expand, creates a child node by forward propagating the selected node with an action either constructed by the neural network or by random sampling, (iii) DefaultPolicy collects terminal reward statistics by either sampling the value neural network or by rolling out a simulated state trajectory from the new node, and (iv) Backpropagate updates the number of visits and cumulative reward up the tree. The action returned by the search is the child of the root node with the most visits. The primary changes we make from standard MCTS are the integration of neural networks, highlighted in Algorithm 2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Neural Tree Expansion", "weight": 1.0} -->

The behavior of other agents is modelled in a turn-based fashion: each depth in the tree corresponds to the turn of an agent and their action is predicted by selecting the best node for their cost function. Intuitively, the MCTS search plans for all robots, assuming that they maximize their incentive. MCTS is known to converge to the minimax tree solution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Expert NTE", "weight": 1.0} -->

The expert, $\pi^{e}$, is a function from joint state $\mathbf{s}$ to joint action $\mathbf{a}$. The expert computes the action by calling Search in Algorithm 2 with a large number of nodes $L_{\text{expert}}$. The expert produces a coordinated team action by selecting the appropriate indices of the joint-space action, where the remaining, unused actions represent the predicted opponent team action. The expert's perfect information, centralized response, and large computational budget is necessary to guarantee the bootstrap property. We found that if the expert is given less computational resources, the learning process is not stable and the quality of the policy and value networks deteriorates over learning iterations. Many of the desirable properties of the expert for theoretical performance make it an infeasible solution for multi-robot applications, motivating the design of the learner.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Learner NTE", "weight": 1.0} -->

The learner for robot $i$, $\pi^{le}$, is a function from local observation $\mathbf{z}^{i}$ to local action $\mathbf{a}^{i}$. The learner computes the action by reconstructing the state from its local observation naively: ${{\overset{\sim}{\mathbf{s}}{(\mathbf{z})}} = {\{{\overset{\sim}{\mathbf{s}}}^{j}\}}},{{\forall j} \in {\mathcal{N}_{A}^{i} \cup \mathcal{N}_{B}^{i}}}$, where we assume that the learner has prior knowledge of the absolute goal location. Then, the learner calls Search in Algorithm 2 with the estimated state and a small number of nodes $L_{\text{learner}}$, $L_{\text{learner}} < L_{\text{expert}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Learner NTE", "weight": 1.0} -->

The final action $\mathbf{a}^{i}$ is selected from the appropriate index of the joint-space action returned by Search. Because the learner only selects a single action from the joint-space action, the learner is predicting the behavior of robots on both teams. This communication-less implicit coordination enables operation in bandwidth-limited or communication-denied environments.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

We introduce each neural network with its dataset generation and training in Algorithm 1, and its effect on tree growth via integration into Algorithm 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

Policy Network: The policy network for robot $i$ maps observations to the action distribution for a single robot and is used to create children nodes. The desired behavior of the policy network is to generate individual robot actions with a high probability of being near-optimal expansions given the current observation, i.e. generate edges to nodes with a high number of visits in the expert search.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The dataset for each robot $i$'s policy network is composed of observation action pairs as computed in Line 1 of Algorithm 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

where $\mathbf{a}_{l}^{i}$ is the action label and $n_{0}$ is the root node. Recall that $C{( \cdot )}$ is a node's set of child nodes, $N{( \cdot )}$ is the number of visits to a node, and $A^{i}{(n_{0},n^{\prime})}$ is the $i$th robot's action from root node $n_{0}$ to child node $n^{\prime}$. Next, we change the input from state to observation by applying robot $i$'s observation model, $\mathbf{z}_{l}^{i} = {h^{i}{(\mathbf{s}_{l})}}$. This is a global-to-local learning technique to automatically synthesize local policies from centralized examples. The collection of observation-action samples can be written in a dataset as $\mathcal{D}_{\pi}^{i} = \left.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The policy network training in Line 1 in Algorithm 1 is cast as a multivariate Gaussian learning problem, i.e. the output of the neural network is a mean, $\mu$ and variance $\mathbf{\Sigma}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The input, $\mathbf{z}_{l}^{i}$, is encoded with a DeepSet feedforward architecture similar to that is compatible with a variable number of neighboring robots.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The policy neural network, ${\overset{\sim}{\pi}}^{i}$, is integrated in Line 2--2 in Algorithm 2 in the expansion operation by constructing a joint-space action from decentralized evaluations of the policy network for all the agents, and then forward propagating that action. We found that using a neural expansion, rather than neural selection as in AlphaZero, is necessary for planning with a small number of nodes in environments with many robots. For example, in a $10$ vs. $10$ game such as that shown in Fig. 2(c), the probability of sampling a control action from a uniform distribution that steers each robot towards the goal within $90$ degrees is ${({1/4})}^{10}$. If the learner policy is evaluated with standard parameters (see Sec. IV-A), it will generate 5 children, which collectively are not likely to contain the desired joint action. Using the neural network expansion operator will overcome this limitation by immediately generating promising child nodes.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

Similar to, the expand operation switches between uniform random and neural network sampling at relative frequency $\beta_{\pi} \in {\lbrack 0,1\rbrack}$. The stochastic nature of both expansion modes enables the tree to maintain exploration.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

Value Network: The value network is used to gather reward statistics in place of a policy rollout, and is called in the DefaultPolicy in Lines 2--2 of Algorithm 2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

where $h_{y}{(\mathbf{s})}$ is the alternative observation function and $n_{rg}$ is the number of robots that have already reached the goal. The value network maps this alternative state representation to the parameters of a multi-variate Gaussian distribution. The desired behavior of the value network is to predict the outcome of games if they were rolled out with the current policy network. The value function implementation in DefaultPolicy is the same as AlphaZero methods.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The value network dataset in Line 1 of Algorithm 1 is generated for all robots at the same time and is composed of alternative state-value pairs. The $\mathbf{y}_{l}$ state can be generated from $\mathbf{s}$, and the value label, $v_{l}$ is generated by self-play with the current policy network. The dataset, $\mathcal{D}_{V}$ can then be written as $\mathcal{D}_{V} = \left. \{{(\mathbf{y}_{l},v_{l})} \middle| {{\forall l} = {1,\ldots}}\} \right.$. Because AlphaZero methods use a policy selector rather than a generator, the dataset for the value network has to be made by rolling out entire games with MCTS. Instead, we generate the dataset by rolling out the policy network, which is much faster per sample, resulting in less total training time.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-E Policy and Value Neural Networks", "weight": 1.0} -->

The value network is trained in Line 1 of Algorithm 1 with a similar loss function as the policy network, using a learning target of the value labels, $v_{l}$, instead of the action $\mathbf{a}_{l}^{i}$. The value is also queried from the neural network in a similar fashion. The value network uses a similar model architecture as the policy network, permitting variable input size of $\mathbf{y}$. Integration of the value network in DefaultPolicy uses the same probabilistic scheme as the policy network with parameter $\beta_{V}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A MCTS and Learning Implementation", "weight": 1.0} -->

We implement Algorithm 1 in Python and Algorithm 2 in C$+ +$ with Python bindings. For the meta-algorithm, we only train the inner robot loop in Line 1 of Algorithm 1 once per team because we use homogeneous robots and policies. Our MCTS variant uses the following hyperparameters: $L_{\text{expert}} = 10\, 000$, $L_{\text{learner}} = 500$, $C_{p} = 2.0$, $C_{pw} = 1.0$, $\alpha_{pw} = 0.25$ and $\alpha_{d} = {{({1 - {3/{({100 - {10d}})}}})}/20}$ where $d$ is the depth of the node. The neural frequency hyperparameters are $\beta_{\pi} = \beta_{V} = 0.5$. The double-integrator game parameters are chosen to match the hardware used in the physical experiments (see Sec. IV-E).

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A MCTS and Learning Implementation", "weight": 1.0} -->

We use position bounds $\overline{p} = {1,2,3}$ $\ m$ and constant velocity $\overline{v} =$ $1.0\ {m/s}$ and acceleration $\overline{a} =$ $2.0\ {m/s^{2}}$ bounds. The tag, collision, and sensing radii are: $r_{t} =$ $0.2\ m$, $r_{p} =$ $0.1\ m$, $r_{sense} =$ $2.0\ m$. We train for up to $5$ agents on each team. We use a simulation and planning timestep of $\Delta =$ $0.1\ s$. Each team starts at opposite sides of the environment, and the goal is placed closer to the defenders' starting position.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A MCTS and Learning Implementation", "weight": 1.0} -->

We implement the machine learning components in PyTorch. The datasets are of size $80\, 000$ points per iteration for both value and policy datasets. The meta learning algorithm is trained until convergence. The policy and value network models both use DeepSet neural network architecture, (e.g. ) where the inner and outer networks each have one hidden layer with $16$ neurons and appropriate input and output dimensions. All networks are of feedforward structure with ReLU activation functions, batch size of $1028$, and are trained over $300$ epochs.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-B Variants and Baseline", "weight": 1.0} -->

In order to evaluate our method, we test the multiple learners and expert policies, each equipped with networks after $k$ learning iterations. To isolate the effect of the neural expansion, we consider the $k = 0$ case for both learner and expert as an unbiased MCTS baseline solution.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Variants and Baseline", "weight": 1.0} -->

As an additional baseline for the double-integrator game, we use the solution. Their work adapts the exact differential game solution for simple-motion and single-robot teams proposed in to a double-integrator, multi-robot team setting. However, their adapted solution is not exact because it assumes a constant acceleration magnitude input and relies on composition of pair-wise matching strategies.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

We evaluate our expert and learner by initializing $100$ different initial conditions of a $3$ attacker, $2$ defender game in a $3\ m$ space. Then, we rollout every combination of variants, learning iterations, and baseline for both team $A$ and team $B$ policies, for a total of $12\, 100$ games. For a single game, the performance criteria for team $A$ policies is the terminal reward and, in order to have consistency of plots (higher is better), the performance criteria for team $B$ policies is one minus the terminal reward. An example game with a different number of agents and environment size is shown in Fig. 2(c) and its animation is provided in the supplemental video. The $10$ vs. $10$ game illustrates the natural scalability in number of agents of the decentralized approach and the generalizability of the neural networks, as they were only trained with data containing up to $5$ robots per team.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

(a) Double-integrator game evaluation: the thick lines indicate the average performance and the shaded area is the variance over 100 games.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

(b) Learner defense (orange) finds emergent cooperative strategies to defend the goal (green).

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

(c) Baseline defense (orange) is vulnerable to learner’s offensive (blue) dodge maneuver.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

The statistical results of the $3$ vs. $2$ experiment are shown in Fig. 3(a) where the thick lines denote the average performance value and the shade is the performance variance. We find the expected results; for both team $A$ and team $B$, the learner with no bias has the worst performance, and learner with fully trained networks surpasses the centralized and expensive unbiased expert and approaches the biased expert. The baseline attacker is about the same strength as the unbiased expert, whereas the baseline defender is much stronger than the unbiased expert. In both cases, the fully-trained biased expert and learner are able to significantly outperform the baseline.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

To investigate the qualitative advantages of our method, we looked at the games where our learner defense outperformed the baseline defense and found two principal advantages: first, the learner defense sometimes demonstrated emergent coordination that is more effective than a pairwise matching strategy, e.g. one defender goes quickly to the goal to protect against greedy attacks while the other defender slowly approaches the goal to maintain its maneuverability, see Fig. 3(b). Second, the learner attacker is sometimes able to exploit the momentum of the baseline defender and perform a dodge maneuver, e.g. the bottom left interaction in Fig. 3(c), whereas the learner defense is robust to this behavior. These examples show the learner networks can generate sophisticated, effective maneuvers.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

As an additional experiment, we evaluate the learner (without retraining) in an environment with static and dynamic obstacles for $100$ different initial conditions; an example is shown in the supplementary video. In this environment, the fully trained learner outperforms the unbiased learner $0.246 \pm 0.022$, this value is calculated by summing the performance criteria difference across attacking and defending policies. This result demonstrates the natural compatibility of tree-based planners with safety constraints and the robustness of the performance gain in out-of-training-domain scenarios.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-D Dynamics Extension", "weight": 1.0} -->

As shown in Fig. 2, NTE can be applied to arbitrary game settings and dynamics. We evaluate the same Reach-Target-Avoid game with 3D Dubin's vehicle dynamics as a relevant model for fixed-wing aircraft applications, shown in Fig. 2(d). We consider the state, action, and dynamics: $\mathbf{s}_{t} = {\lbrack x_{t},y_{t},z_{t},\psi_{t},\gamma_{t},\phi_{t},v_{t}\rbrack}^{T}$, $\mathbf{a}_{t} = {\lbrack{\overset{˙}{\gamma}}_{t},{\overset{˙}{\phi}}_{t},{\overset{˙}{v}}_{t}\rbrack}^{T}$

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-D Dynamics Extension", "weight": 1.0} -->

where $x,y,z$ are inertial position, $v$ is speed, $\psi$ is the heading angle, $\gamma$ is the flight path angle, and $\phi$ is the bank angle and $g$ is the gravitational acceleration. The game is bounded to $\overline{p} =$$5\ m$ with a maximum linear acceleration of $2.0\ {m/s^{2}}$ and maximum angular rates of $36\ {\deg/s}$, and $g$ is set to $0.98\ {{m/s}}$ to scale to our game length scale.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-D Dynamics Extension", "weight": 1.0} -->

We initialize $2$ attacker, $2$ defender games for $100$ different initial conditions in a $5\ m$ region and test the policy variants, without an external baseline, for a total of $81\, 000$ games. The performance results are shown in Fig. 4, where we see the same trend that the learner and expert policies improve over learning iterations. In addition, the biased learner's performance quickly surpasses the unbiased expert ($k = 0$).

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-E Hardware Validation", "weight": 1.0} -->

To test our algorithm in practice, we fly in a motion capture space, where each robot (CrazyFlie 2.x, see Fig. 1) is equipped with a single marker, and we use the Crazyswarm for tracking and scripting. The centralized system simulates distributed operation by collecting the full state, computing local observations and local policies, and broadcasting only the output of each robot's learner policy. For a given double-integrator policy, we evaluate the learner to compute an action, forward-propagate double-integrator dynamics, and track the resulting position and velocity set-point using a nonlinear controller for full quadrotor dynamics. Planning in a lower-dimensional double-integrator state and then tracking the full system is enabled by the timescale separation of position and attitude dynamics of quadrotors.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-E Hardware Validation", "weight": 1.0} -->

We evaluate the double-integrator learner for up to 3 attacker, 2 defender games in an aerial swarm flight demonstration. We show the results of the experiments in our supplemental video. We use the same parameters as in simulation in Sec. IV-C. Our learner evaluation takes an average of $11\ {ms}$ with a standard deviation of $6\ {ms}$, with each robot policy process running in parallel on an Intel(R) Core(TM) i7-8665U. By comparison, the biased expert takes $329 \pm$$144\ {ms}$ to execute and the unbiased expert takes $277 \pm$$260\ {ms}$. Our computational tests show that the learner has a significant ($\approx 25$ times) computational advantage over the baseline unbiased expert. Our physical demonstration shows that our learner is robust to the gap between simulation and real world and can run in real-time on off-the-shelf hardware.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present a new approach for multi-robot planning in non-cooperative environments with an iterative search and learning method called Neural Tree Expansion. Our method bridges the gap between an AlphaZero-like method and real-world robotics applications by introducing a learner agent with decentralized evaluation, partial information, and limited computational resources. Our method outperforms the current state-of-the-art analytical baseline for the multi-robot double-integrator Reach-Target-Avoid game with dynamically sophisticated and coordinated strategies. We demonstrate our method's broad compatibility by further empirical evaluation of the Reach-Target-Avoid game for $3$D Dubin's vehicle dynamics and visualization of canonical decision-making problems. We validate the effectiveness through hardware experimentation and show that our policies run in real-time on off-the-shelf computational resources. In future work, we will combine planning under uncertainty algorithms with deep learning to handle scenarios with model and measurement uncertainty.
