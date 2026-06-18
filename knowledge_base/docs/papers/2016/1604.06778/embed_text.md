## Introduction

Reinforcement learning addresses the problem of how agents should learn to take actions to maximize cumulative reward through interactions with the environment. The traditional approach for reinforcement learning algorithms requires carefully chosen feature representations, which are usually hand-engineered. Recently, significant progress has been made by combining advances in deep learning for learning feature representations with reinforcement learning, tracing back to much earlier work of Tesauro and Bertsekas & Tsitsiklis. Notable examples are training agents to play Atari games based on raw pixels and to acquire advanced manipulation skills using raw sensory inputs. Impressive results have also been obtained in training deep neural network policies for 3D locomotion and manipulation tasks.

Along with this recent progress, the Arcade Learning Environment (ALE) has become a popular benchmark for evaluating algorithms designed for tasks with high-dimensional state inputs and discrete actions. However, these algorithms do not always generalize straightforwardly to tasks with continuous actions, leading to a gap in our understanding. For instance, algorithms based on Q-learning quickly become infeasible when naive discretization of the action space is performed, due to the curse of dimensionality. In the continuous control domain, where actions are continuous and often high-dimensional, we argue that the existing control benchmarks fail to provide a comprehensive set of challenging problems (see Section 7 for a review of existing benchmarks). Benchmarks have played a significant role in other areas such as computer vision and speech recognition. Examples include MNIST, Caltech101, CIFAR, ImageNet, PASCAL VOC, BSDS500, SWITCHBOARD, TIMIT, Aurora, and VoiceSearch. The lack of a standardized and challenging testbed for reinforcement learning and continuous control makes it difficult to quantify scientific progress. Systematic evaluation and comparison will not only further our understanding of the strengths of existing algorithms, but also reveal their limitations and suggest directions for future research.

We attempt to address this problem and present a benchmark consisting of 31 continuous control tasks. These tasks range from simple tasks, such as cart-pole balancing, to challenging tasks such as high-DOF locomotion, tasks with partial observations, and hierarchically structured tasks. Furthermore, a range of reinforcement learning algorithms are implemented on which we report novel findings based on a systematic evaluation of their effectiveness in training deep neural network policies. The benchmark and reference implementations are available at [https://github.com/rllab/rllab](https://github.com/rllab/rllab), allowing for the development, implementation, and evaluation of new algorithms and tasks.

## Preliminaries

In this section, we define the notation used in subsequent sections.

The implemented tasks conform to the standard interface of a finite-horizon discounted Markov decision process (MDP), defined by the tuple $(\mathcal{S},\mathcal{A},P,r,\rho_{0},\gamma,T)$, where $\mathcal{S}$ is a (possibly infinite) set of states, $\mathcal{A}$ is a set of actions, $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\mathbb{R}}_{\geq 0}}$ is the transition probability distribution, $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is the reward function, $\rho_{0}:{\mathcal{S}\rightarrow{\mathbb{R}}_{\geq 0}}$ is the initial state distribution, $\gamma \in {(0,1\rbrack}$ is the discount factor, and $T$ is the horizon.

For partially observable tasks, which conform to the interface of a partially observable Markov decision process (POMDP), two more components are required, namely $\Omega$, a set of observations, and $\mathcal{O}:{{\mathcal{S} \times \Omega}\rightarrow{\mathbb{R}}_{\geq 0}}$, the observation probability distribution.

Most of our implemented algorithms optimize a stochastic policy $\pi_{\theta}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}_{\geq 0}}$. Let $\eta{(\pi)}$ denote its expected discounted reward: ${\eta{(\pi)}} = {{\mathbb{E}}_{\tau}\left\lbrack {\sum_{t = 0}^{T}{\gamma^{t}r{(s_{t},a_{t})}}} \right\rbrack}$, where $\tau = {(s_{0},a_{0},\ldots)}$ denotes the whole trajectory, $s_{0} \sim {\rho_{0}{(s_{0})}}$, $a_{t} \sim {\pi{(\left. a_{t} \middle| s_{t} \right.)}}$, and $s_{t + 1} \sim {P{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}}$.

For deterministic policies, we use the notation $\mu_{\theta}:{\mathcal{S}\rightarrow\mathcal{A}}$ to denote the policy instead. The objective for it has the same form as above, except that now we have $a_{t} = {\mu{(s_{t})}}$.

## Tasks

The tasks in the presented benchmark can be divided into four categories: basic tasks, locomotion tasks, partially observable tasks, and hierarchical tasks. We briefly describe them in this section. More detailed specifications are given in the supplementary materials and in the source code.

We choose to implement all tasks using physics simulators rather than symbolic equations, since the former approach is less error-prone and permits easy modification of each task. Tasks with simple dynamics are implemented using Box2D, an open-source, freely available 2D physics simulator. Tasks with more complicated dynamics, such as locomotion, are implemented using MuJoCo, a 3D physics simulator with better modeling of contacts.

### Basic Tasks

We implement five basic tasks that have been widely analyzed in reinforcement learning and control literature: Cart-Pole Balancing, Cart-Pole Swing Up, Mountain Car, Acrobot Swing Up, and Double Inverted Pendulum Balancing. These relatively low-dimensional tasks provide quick evaluations and comparisons of RL algorithms.

### Locomotion Tasks

In this category, we implement six locomotion tasks of varying dynamics and difficulty: Swimmer, Hopper, Walker, Half-Cheetah, Ant, Simple Humanoid, and Full Humanoid. The goal for all the tasks is to move forward as quickly as possible. These tasks are more challenging than the basic tasks due to high degrees of freedom. In addition, a great amount of exploration is needed to learn to move forward without getting stuck at local optima. Since we penalize for excessive controls as well as falling over, during the initial stage of learning, when the robot is not yet able to move forward for a sufficient distance without falling, apparent local optima exist including staying at the origin or diving forward slowly.

Figure 1: Illustration of locomotion tasks: 1 Swimmer; 1 Hopper; 1 Walker; 1 Half-Cheetah; 1 Ant; 1 Simple Humanoid; and 1 Full Humanoid.

### Partially Observable Tasks

In real-life situations, agents are often not endowed with perfect state information. This can be due to sensor noise, sensor occlusions, or even sensor limitations that result in partial observations. To evaluate algorithms in more realistic settings, we implement three variations of partially observable tasks for each of the five basic tasks described in Section 3.1, leading to a total of $15$ additional tasks. These variations are described below.

Limited Sensors: For this variation, we restrict the observations to only provide positional information (including joint angles), excluding velocities. An agent now has to learn to infer velocity information in order to recover the full state. Similar tasks have been explored in Gomez & Miikkulainen; Schäfer & Udluft; Heess et al.; Wierstra et al..

Noisy Observations and Delayed Actions: In this case, sensor noise is simulated through the addition of Gaussian noise to the observations. We also introduce a time delay between taking an action and the action being in effect, accounting for physical latencies. Agents now need to learn to integrate both past observations and past actions to infer the current state. Similar tasks have been proposed in Bakker.

System Identification: For this category, the underlying physical model parameters are varied across different episodes. The agents must learn to generalize across different models, as well as to infer the model parameters from its observation and action history.

### Hierarchical Tasks

Many real-world tasks exhibit hierarchical structure, where higher level decisions can reuse lower level skills. For instance, robots can reuse locomotion skills when exploring the environment. We propose several tasks where both low-level motor controls and high-level decisions are needed. These two components each operates on a different time scale and calls for a natural hierarchy in order to efficiently learn the task.

Figure 2: Illustration of hierarchical tasks: 2 Locomotion + Food Collection; and 2 Locomotion + Maze.

Locomotion + Food Collection: For this task, the agent needs to learn to control either the swimmer or the ant robot to collect food and avoid bombs in a finite region. The agent receives range sensor readings about nearby food and bomb units. It is given a positive reward when it reaches a food unit, or a negative reward when it reaches a bomb.

Locomotion + Maze: For this task, the agent needs to learn to control either the swimmer or the ant robot to reach a goal position in a fixed maze. The agent receives range sensor readings about nearby obstacles as well as its goal (when visible). A positive reward is given only when the robot reaches the goal region.

## Algorithms

In this section, we briefly summarize the algorithms implemented in our benchmark, and note any modifications made to apply them to general parametrized policies. We implement a range of gradient-based policy search methods, as well as two gradient-free methods for comparison with the gradient-based approaches.

### Batch Algorithms

Most of the implemented algorithms are batch algorithms. At each iteration, $N$ trajectories ${\{\tau_{i}\}}_{i = 1}^{N}$ are generated, where $\tau_{i} = {\{{(s_{t}^{i},a_{t}^{i},r_{t}^{i})}\}}_{t = 0}^{T}$ contains data collected along the $i$th trajectory. For on-policy gradient-based methods, all the trajectories are sampled under the current policy. For gradient-free methods, they are sampled under perturbed versions of the current policy.

REINFORCE: This algorithm estimates the gradient of expected return ${\nabla_{\theta}\eta}{(\pi_{\theta})}$ using the likelihood ratio trick:

where $R_{t}^{i} = {\sum_{t^{\prime} = t}^{T}{\gamma^{t^{\prime} - t}r_{t^{\prime}}^{i}}}$ and $b_{t}^{i}$ is a baseline that only depends on the state $s_{t}^{i}$ to reduce variance. Hereafter, an ascent step is taken in the direction of the estimated gradient. This process continues until $\theta_{k}$ converges.

Truncated Natural Policy Gradient (TNPG): Natural Policy Gradient improves upon REINFORCE by computing an ascent direction that approximately ensures a small change in the policy distribution. This direction is derived to be $I{(\theta)}^{- 1}{\nabla_{\theta}\eta}{(\pi_{\theta})}$, where $I{(\theta)}$ is the Fisher information matrix (FIM). We use the step size suggested by Peters & Schaal: $\alpha = \sqrt{\delta_{\text{KL}}\left( {{\nabla_{\theta}\eta}{(\pi_{\theta})}^{T}I{(\theta)}^{- 1}{\nabla_{\theta}\eta}{(\pi_{\theta})}} \right)^{- 1}}$. Finally, we replace ${\nabla_{\theta}\eta}{(\pi_{\theta})}$ and $I{(\theta)}$ by their empirical estimates.

For neural network policies with tens of thousands of parameters or more, generic Natural Policy Gradient incurs prohibitive computation cost by forming and inverting the empirical FIM. Instead, we study Truncated Natural Policy Gradient (TNPG) in this paper, which computes the natural gradient direction without explicitly forming the matrix inverse, using a conjugate gradient algorithm that only requires computing $I{(\theta)}v$ for arbitrary vector $v$. TNPG makes it practical to apply natural gradient in policy search setting with high-dimensional parameters, and we refer the reader to Schulman et al. for more details.

Reward-Weighted Regression (RWR): This algorithm formulates the policy optimization as an Expectation-Maximization problem to avoid the need to manually choose learning rate, and the method is guaranteed to converge to a locally optimal solution. At each iteration, this algorithm optimizes a lower bound of the log-expected return: $\theta = {{\arg{\max_{\theta^{\prime}}\mathcal{L}}}{(\theta^{\prime})}}$, where

Here, $\rho:{{\mathbb{R}}\rightarrow{\mathbb{R}}_{\geq 0}}$ is a function that transforms raw returns to nonnegative values. Following Deisenroth et al., we choose $\rho$ to be ${\rho{(R)}} = {R - R_{\text{min}}}$, where $R_{\text{min}}$ is the minimum return among all trajectories collected in the current iteration.

Relative Entropy Policy Search (REPS): This algorithm limits the loss of information per iteration and aims to ensure a smooth learning progress. At each iteration, we collect all trajectories into a dataset $\mathcal{D} = {\{{(s_{i},a_{i},r_{i},s_{i}^{\prime})}\}}_{i = 1}^{M}$, where $M$ is the total number of samples. Then, we first solve for the dual parameters ${\lbrack\eta^{\ast},\nu^{\ast}\rbrack} = {{\arg{\min_{\eta^{\prime},\nu^{\prime}}g}}{(\eta^{\prime},\nu^{\prime})}}$ s.t. $\eta > 0$, where

Here $\delta_{\text{KL}} > 0$ controls the step size of the policy, and ${\delta_{i}{(\nu)}} = {r_{i} + {\nu^{T}{({{\phi{(s_{i}^{\prime})}} - {\phi{(s_{i})}}})}}}$ is the sample Bellman error. We then solve for the new policy parameters:

Trust Region Policy Optimization (TRPO): This algorithm allows more precise control on the expected policy improvement than TNPG through the introduction of a surrogate loss. At each iteration, we solve the following constrained optimization problem (replacing expectations with samples):

where $\rho_{\theta} = \rho_{\pi_{\theta}}$ is the discounted state-visitation frequencies induced by $\pi_{\theta}$, $A_{\theta_{k}}{(s,a)}$, known as the advantage function, is estimated by the empirical return minus the baseline, and $\delta_{\text{KL}}$ is a step size parameter which controls how much the policy is allowed to change per iteration. We follow the procedure described in the original paper for solving the optimization, which results in the same descent direction as TNPG with an extra line search in the objective and KL constraint.

Cross Entropy Method (CEM): Unlike previously mentioned methods, which perform exploration through stochastic actions, CEM performs exploration directly in the policy parameter space. At each iteration, we produce $N$ perturbations of the policy parameter: $\theta_{i} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$, and perform a rollout for each sampled parameter. Then, we compute the new mean and diagonal covariance using the parameters that correspond to the top $q$-quantile returns.

Covariance Matrix Adaption Evolution Strategy (CMA-ES): Similar to CEM, CMA-ES is a gradient-free evolutionary approach for optimizing nonconvex objective functions. In our case, this objective function equals the average sampled return. In contrast to CEM, CMA-ES estimates the covariance matrix of a multivariate normal distribution through incremental adaption along evolution paths, which contain information about the correlation between consecutive updates.

### Online Algorithms

Deep Deterministic Policy Gradient (DDPG): Compared to batch algorithms, the DDPG algorithm continuously improves the policy as it explores the environment. It applies gradient descent to the policy with minibatch data sampled from a replay pool, where the gradient is computed via

where $B$ is the batch size. The critic $Q$ is trained via gradient descent on the $\ell^{2}$ loss of the Bellman error $L = {\frac{1}{B}{\sum_{i = 1}^{B}{({y_{i} - {Q_{\phi}{(s_{i},a_{i})}}})}^{2}}}$, where $y_{i} = {r_{i} + {\gammaQ_{\phi^{\prime}}^{\prime}{(s_{i}^{\prime},{\mu_{\theta^{\prime}}^{\prime}{(s_{i}^{\prime})}})}}}$. To improve stability of the algorithm, we use target networks for both the critic and the policy when forming the regression target $y_{i}$. We refer the reader to Lillicrap et al. for a more detailed description of the algorithm.

### Recurrent Variants

We implement direct applications of the aforementioned batch-based algorithms to recurrent policies. The only modification required is to replace $\pi{(\left. a_{t}^{i} \middle| s_{t}^{i} \right.)}$ by $\pi{(\left. a_{t}^{i} \middle| {o_{1:t}^{i},a_{1:{t - 1}}^{i}} \right.)}$, where $o_{1:t}^{i}$ and $a_{1:{t - 1}}$ are the histories of past and current observations and past actions. Recurrent versions of reinforcement learning algorithms have been studied in many existing works, such as Bakker, Schäfer & Udluft, Wierstra et al., and Heess et al..

## Experiment Setup

In this section, we elaborate on the experimental setup used to generate the results.

Performance Metrics: For each report unit (a particular algorithm running on a particular task), we define its performance as $\frac{1}{\sum_{i = 1}^{I}N_{i}}{\sum_{i = 1}^{I}{\sum_{n = 1}^{N_{i}}R_{in}}}$, where $I$ is the number of training iterations, $N_{i}$ is the number of trajectories collected in the $i$th iteration, and $R_{in}$ is the undiscounted return for the $n$th trajectory of the $i$th iteration,

Hyperparameter Tuning: For the DDPG algorithm, we used the hyperparametes reported in Lillicrap et al.. For the other algorithms, we follow the approach in, and we select two tasks in each category, on which a grid search of hyperparameters is performed. Each choice of hyperparameters is executed under five random seeds. The criterion for the best hyperparameters is defined as ${{mean}{({returns})}} - {{std}{({returns})}}$. This metric selects against large fluctuations of performance due to overly large step sizes.

For the other tasks, we try both of the best hyperparameters found in the same category, and report the better performance of the two. This gives us insights into both the maximum possible performance when extensive hyperparameter tuning is performed, and the robustness of the best hyperparameters across different tasks.

00footnotetext: aExcept for the hierarchical tasks

Double Inverted Pendulum*

Table 1: Performance of the implemented algorithms in terms of average return over all training iterations for five different random seeds (same across all algorithms). The results of the best-performing algorithm on each task, as well as all algorithms that have performances that are not statistically significantly different (Welch’s t-test with p &lt; 0.05), are highlighted in boldface.a In the tasks column, the partially observable variants of the tasks are annotated as follows: LS stands for limited sensors, NO for noisy observations and delayed actions, and SI for system identifications. The notation N/A denotes that an algorithm has failed on the task at hand, e.g., CMA-ES leading to out-of-memory errors in the Full Humanoid task.

Policy Representation: For basic, locomotion, and hierarchical tasks and for batch algorithms, we use a feed-forward neural network policy with 3 hidden layers, consisting of $100$, $50$, and $25$ hidden units with tanh nonlinearity at the first two hidden layers, which map each state to the mean of a Gaussian distribution. The log-standard deviation is parameterized by a global vector independent of the state, as done in Schulman et al.. For all partially observable tasks, we use a recurrent neural network with a single hidden layer consisting of $32$ LSTM hidden units.

For the DDPG algorithm which trains a deterministic policy, we follow Lillicrap et al.. For both the policy and the $Q$ function, we use the same architecture of a feed-forward neural network with 2 hidden layers, consisting of $400$ and $300$ hidden units with relu activations.

Baseline: For all gradient-based algorithms except REPS, we can subtract a baseline from the empirical return to reduce variance of the optimization. We use a linear function as the baseline with a time-varying feature vector.

Figure 3: Performance as a function of the number of iterations; the shaded area depicts the mean ± the standard deviation over five different random seeds: 3 Performance comparison of all algorithms in terms of the average reward on the Walker task; 3 Comparison between REINFORCE, TNPG, and TRPO in terms of the mean KL-divergence on the Walker task; 3 Performance comparison on TNPG and TRPO on the Swimmer task; 3 Performance comparison of all algorithms in terms of the average reward on the Half-Cheetah task.

## Results and Discussion

The main evaluation results are presented in Table 1. The tasks on which the grid search is performed are marked with (\*). In each entry, the pair of numbers shows the mean and standard deviation of the normalized cumulative return using the best possible hyperparameters.

REINFORCE: Despite its simplicity, REINFORCE is an effective algorithm in optimizing deep neural network policies in most basic and locomotion tasks. Even for high-DOF tasks like Ant, REINFORCE can achieve competitive results. However we observe that REINFORCE sometimes suffers from premature convergence to local optima as noted by Peters & Schaal, which explains the performance gaps between REINFORCE and TNPG on tasks such as Walker (Figure 3). By visualizing the final policies, we can see that REINFORCE results in policies that tend to jump forward and fall over to maximize short-term return instead of acquiring a stable walking gait to maximize long-term return. In Figure 3, we can observe that even with a small learning rate, steps taken by REINFORCE can sometimes result in large changes to policy distribution, which may explain the fast convergence to local optima.

TNPG and TRPO: Both TNPG and TRPO outperform other batch algorithms by a large margin on most tasks, confirming that constraining the change in the policy distribution results in more stable learning.

Compared to TNPG, TRPO offers better control over each policy update by performing a line search in the natural gradient direction to ensure an improvement in the surrogate loss function. We observe that hyperparameter grid search tends to select conservative step sizes ($\delta_{\text{KL}}$) for TNPG, which alleviates the issue of performance collapse caused by a large update to the policy. By contrast, TRPO can robustly enforce constraints with larger a $\delta_{\text{KL}}$ value and hence speeds up learning in some cases. For instance, grid search on the Swimmer task reveals that the best step size for TNPG is $\delta_{\text{KL}} = 0.05$, whereas TRPO's best step-size is larger: $\delta_{\text{KL}} = 0.1$. As shown in Figure 3, this larger step size enables slightly faster learning.

RWR: RWR is the only gradient-based algorithm we implemented that does not require any hyperparameter tuning. It can solve some basic tasks to a satisfactory degree, but fails to solve more challenging tasks such as locomotion. We observe empirically that RWR shows fast initial improvement followed by significant slow-down, as shown in Figure 3.

REPS: Our main observation is that REPS is especially prone to early convergence to local optima in case of continuous states and actions. Its final outcome is greatly affected by the performance of the initial policy, an observation that is consistent with the original work of Peters et al.. This leads to a bad performance on average, although under particular initial settings the algorithm can perform on par with others. Moreover, the tasks presented here do not assume the existence of a stationary distribution, which is assumed in Peters et al.. In particular, for many of our tasks, transient behavior is of much greater interest than steady-state behavior, which agrees with previous observation by van Hoof et al.,

Gradient-free methods: Surprisingly, even when training deep neural network policies with thousands of parameters, CEM achieves very good performance on certain basic tasks such as Cart-Pole Balancing and Mountain Car, suggesting that the dimension of the searching parameter is not always the limiting factor of the method. However, the performance degrades quickly as the system dynamics becomes more complicated. We also observe that CEM outperforms CMA-ES, which is remarkable as CMA-ES estimates the full covariance matrix. For higher-dimensional policy parameterizations, the computational complexity and memory requirement for CMA-ES become noticeable. On tasks with high-dimensional observations, such as the Full Humanoid, the CMA-ES algorithm runs out of memory and fails to yield any results, denoted as N/A in Table 1.

DDPG: Compared to batch algorithms, we found that DDPG was able to converge significantly faster on certain tasks like Half-Cheetah due to its greater sample efficiency. However, it was less stable than batch algorithms, and the performance of the policy can degrade significantly during training. We also found it to be more susceptible to scaling of the reward. In our experiment for DDPG, we rescaled the reward of all tasks by a factor of $0.1$, which seems to improve the stability.

Partially Observable Tasks: We experimentally verify that recurrent policies can find better solutions than feed-forward policies in Partially Observable Tasks but recurrent policies are also more difficult to train. As shown in Table 1, derivative-free algorithms like CEM and CMA-ES work considerably worse with recurrent policies. Also we note that the performance gap between REINFORCE and TNPG widens when they are applied to optimize recurrent policies, which can be explained by the fact that a small change in parameter space can result in a bigger change in policy distribution with recurrent policies than with feedforward policies.

Hierarchical Tasks: We observe that all of our implemented algorithms achieve poor performance on the hierarchical tasks, even with extensive hyperparameter search and $500$ iterations of training. It is an interesting direction to develop algorithms that can automatically discover and exploit the hierarchical structure in these tasks.

## Related Work

In this section, we review existing benchmarks of continuous control tasks. The earliest efforts of evaluating reinforcement learning algorithms started in the form of individual control problems described in symbolic form. Some widely adopted tasks include the inverted pendulum, mountain car, and Acrobot. These problems are frequently incorporated into more comprehensive benchmarks.

Some reinforcement learning benchmarks contain low-dimensional continuous control tasks, such as the ones introduced above, including RLLib, MMLF, RL-Toolbox, JRLF, Beliefbox, Policy Gradient Toolbox, and ApproxRL. A series of RL competitions has also been held in recent years, again with relatively low-dimensional actions. In contrast, our benchmark contains a wider range of tasks with high-dimensional continuous state and action spaces.

Previously, other benchmarks have been proposed for high-dimensional control tasks. Tdlearn includes a 20-link pole balancing task, DotRL includes a variable-DOF octopus arm and a 6-DOF planar cheetah model, PyBrain includes a 16-DOF humanoid robot with standing and jumping tasks, RoboCup Keepaway is a multi-agent game which can have a flexible dimension of actions by varying the number of agents, and SkyAI includes a 17-DOF humanoid robot with crawling and turning tasks. Other libraries such as CL-Square and RLPark provide interfaces to actual hardware, e.g., Bioloid and iRobot Create. In contrast to these aforementioned testbeds, our benchmark makes use of simulated environments to reduce computation time and to encourage experimental reproducibility. Furthermore, it provides a much larger collection of tasks of varying difficulty.

## Conclusion

In this work, a benchmark of continuous control problems for reinforcement learning is presented, covering a wide variety of challenging tasks. We implemented several reinforcement learning algorithms, and presented them in the context of general policy parameterizations. Results show that among the implemented algorithms, TNPG, TRPO, and DDPG are effective methods for training deep neural network policies. Still, the poor performance on the proposed hierarchical tasks calls for new algorithms to be developed. Implementing and evaluating existing and newly proposed algorithms will be our continued effort. By providing an open-source release of the benchmark, we encourage other researchers to evaluate their algorithms on the proposed tasks.
