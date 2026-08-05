<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Plan Online, Learn Offline: Efficient Learning and Exploration via Model-Based Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a plan online and learn offline (POLO) framework for the setting where an agent, with an internal model, needs to continually act and learn in the world. Our work builds on the synergistic relationship between local model-based control, global value function learning, and exploration. We study how local trajectory optimization can cope with approximation errors in the value function, and can stabilize and accelerate value function learning. Conversely, we also study how approximate value functions can help reduce the planning horizon and allow for better policies beyond local solutions. Finally, we also demonstrate how trajectory optimization can be used to perform temporally coordinated exploration in conjunction with estimating uncertainty in value function approximation. This exploration is critical for fast and stable learning of the value function. Combining these components enable solutions to complex simulated control tasks, like humanoid locomotion and dexterous in-hand manipulation, in the equivalent of a few minutes of experience in the real world.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a setting where an agent with limited memory and computational resources is dropped into a world. The agent has to simultaneously act in the world and learn to become proficient in the tasks it encounters. Let us further consider a setting where the agent has some prior knowledge about the world in the form of a nominal dynamics model. However, the state space of the world could be very large and complex, and the set of possible tasks very diverse. This complexity and diversity, combined with the limited computational capability, rules out the possibility of an omniscient agent that has experienced all situations and knows how to act optimally in all states, even if the agent knows the dynamics. Thus, the agent has to act in the world while learning to become competent.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on the knowledge of dynamics and its computational resources, the agent is imbued with a local search procedure in the form of trajectory optimization. While the agent would certainly benefit from the most powerful of trajectory optimization algorithms, it is plausible that very complex procedures are still insufficient or inadmissible due to the complexity or inherent unpredictability of the environment. Limited computational resources may also prevent these powerful methods from real-time operation. While the trajectory optimizer may be insufficient by itself, we show that it provides a powerful vehicle for the agent to explore and learn about the world.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will first provide intuitions for why there may be substantial performance degradation when acting greedily using an approximate value function. We also show that value function learning can be accelerated and stabilized by utilizing trajectory optimization integrally in the learning process, and that a trajectory optimization procedure in conjunction with an approximate value function can compute near optimal actions. In addition, exploration is critical to propagate global information in value function learning, and for trajectory optimization to escape local solutions and saddle points. In POLO, the agent forms hypotheses on potential reward regions, and executes temporally coordinated action sequences through trajectory optimization. This is in contrast to strategies like $\epsilon -$greedy and Boltzmann exploration that explore at the granularity of individual timesteps. The use of trajectory optimization enables the agent to perform directed and efficient exploration, which in turn helps to find better global solutions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The setting studied in the paper models many problems of interest in robotics and artificial intelligence. Local trajectory optimization becomes readily feasible when a nominal model and computational resources are available to an agent, and can accelerate learning of novel task instances. In this work, we study the case where the internal nominal dynamics model used by the agent is accurate. Nominal dynamics models based on knowledge of physics mujoco12, or through learning SysIDbook, complements a growing body of work on successful simulation to reality transfer and system identification Ross2012AgnosticSI; Rajeswaran2016EPOpt; Peng2017SimtoRealTO; Lowrey2018ReinforcementLF; OpenAIHand. Combining the benefits of local trajectory optimization for fast improvement with generalization enabled by learning is critical for robotic agents that live in our physical world to continually learn and acquire a large repertoire of skills.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The POLO framework", "weight": 1.0} -->

The POLO framework combines three components: local trajectory optimization, global value function approximation, and an uncertainty and reward aware exploration strategy. We first present the motivation for each component, followed by the full POLO procedure.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Definitions, Notations, and Setting", "weight": 1.0} -->

We model the world as an infinite horizon discounted Markov Decision Process (MDP), which is characterized by the tuple: $\mathcal{M} = {\{\mathcal{S},\mathcal{A},\mathcal{R},\mathcal{T},\gamma\}}$. $\mathcal{S} \in {\mathbb{R}}^{n}$ and $\mathcal{A} \in {\mathbb{R}}^{m}$ represent the continuous (real-valued) state and action spaces respectively. $\mathcal{R}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ represents the reward function.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Definitions, Notations, and Setting", "weight": 1.0} -->

$\mathcal{T}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\mathbb{R}}_{+}}$ represents the dynamics model, which in general could be stochastic, and $\gamma \in {\lbrack 0,1)}$ is the discount factor. A policy $\pi:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}_{+}}$ describes a mapping from states to actions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Definitions, Notations, and Setting", "weight": 1.0} -->

As described earlier, we consider the setting where an agent is dropped into a complex world. The agent has access to an internal model of the world. However, the world can be complex and diverse, ruling out the possibility of an omniscient agent. To improve its behavior, the agent has to explore and understand relevant parts of the state space while it continues to act in the world. Due to the availability of the internal model, the agent can revisit states it experienced in the world and reason about alternate potential actions and their consequences to learn more efficiently.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Value Function Approximation", "weight": 1.0} -->

The optimal value function describes the long term discounted reward the agent receives under the optimal policy. Defining the Bellman operator as: ${\mathcal{B}V{(s)}} = {{\max_{a}{\mathbb{E}}}\left\lbrack {{r{(s,a)}} + {\gammaV{(s')}}} \right\rbrack}$, the optimal value function $V^{\ast}$ corresponds to the fixed point: ${V^{\ast}{(s)}} = {\mathcal{B}V^{\ast}{(s)}{\forall s}} \in \mathcal{S}$. For small, tabular MDPs, classical dynamic programming algorithms like value iteration can be used to obtain the optimal value function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Value Function Approximation", "weight": 1.0} -->

Using this, the optimal policy can be recovered as: ${\pi^{\ast}{(s)}} = {{\arg{\max_{a}{\mathbb{E}}}}{\lbrack{{r{(s,a)}} + {\gammaV^{\ast}{(s')}}}\rbrack}}$. For continuous MDPs, computing the optimal value function exactly is not tractable except in a few well known cases like the LQR (AstromBook,). Thus, various approaches to approximate the value function have been considered in literature. One popular approach is fitted value iteration (BertsekasBook Munos2008FiniteTimeBF,), where a function approximator (e.g. neural network) is used to approximate the optimal value function. The core structure of fitted value iteration considers a collection of states (or a sampling distribution $\nu$), and a parametric value function approximator ${\hat{V}}_{\theta}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Value Function Approximation", "weight": 1.0} -->

Inspired by value iteration, fitted value iteration updates the parameters as: where the targets $y$ are computed as ${y{(s)}}:={{\max_{a}{\mathbb{E}}}{\lbrack{{r{(s,a)}} + {\gamma{\hat{V}}_{\theta_{k}}{(s')}}}\rbrack}}$. After the value function is approximated over sufficient iterations, the policy is recovered from the value function as ${\hat{\pi}{(s)}} = {{\arg{\max_{a}{\mathbb{E}}}}{\lbrack{{r{(s,a)}} + {\gamma{\hat{V}}_{\theta}{(s')}}}\rbrack}}$. The success of this overall procedure depends critically on at least two components: the capacity of the function approximator and the sampling distribution $\nu$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trajectory Optimization and Model Predictive Control", "weight": 1.0} -->

Trajectory optimization and model predictive control (MPC) have a long history in robotics and control systems (Garcia1989ModelPC Tassa2014ControllimitedDD,)^11^1In this work, we use the terms trajectory optimization and MPC interchangeably. In MPC, a locally optimal policy or sequence of actions (up to horizon $H$) is computed based on local knowledge of the dynamics model as: where the states evolve according to the transition dynamics of the MDP, i.e. $s_{t + 1} \sim {\mathcal{T}{(s_{t},a_{t})}}$. The first action from the optimized sequence is executed, and the procedure is repeated again at the next time step. The optimization is defined over the space feedback policies $(\pi_{0:{H - 1}})$, but a sequence of actions $(a_{0:{H - 1}})$ can be optimized instead, without loss in performance, if the dynamics is deterministic. See Appendix C for further discussions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Trajectory Optimization and Model Predictive Control", "weight": 1.0} -->

Here, $r_{f}{(s_{H})}$ represents a terminal or final reward function. This approach has led to tremendous success in a variety of control systems such as power grids, chemical process control MPCsurvey, and more recently in robotics (williams2016aggressive,). Since MPC looks forward only $H$ steps, it is ultimately a local method unless coupled with a value function that propagates global information. In addition, we also provide intuitions for why MPC may help accelerate the learning of value functions. This synergistic effect between MPC and global value function learning forms a primary motivation for POLO.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Accelerating convergence of the value function", "weight": 1.0} -->

In the tabular setting, for any $V_{1}$ and $V_{2}$, it is easy to verify that ${|{{\mathcal{B}^{H}V_{1}} - {\mathcal{B}^{H}V_{2}}}|}_{\infty} \leq {\gamma^{H}{|{V_{1} - V_{2}}|}_{\infty}}$. Intuitively, $\mathcal{B}^{H}$ allows for propagation of global information for $H$ steps, thereby accelerating the convergence due to faster mixing. Note that one way to realize $\mathcal{B}^{H}$ is to simply apply $\mathcal{B}$ $H$ times, with each step providing a contraction by $\gamma$. In the general setting, it is unknown if there exists alternate, cheaper ways to realize $\mathcal{B}^{H}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Accelerating convergence of the value function", "weight": 1.0} -->

However, for problems in continuous control, MPC based on local dynamic programming methods (Jacobson1970 Todorov2005, ) provide an efficient way to approximately realize $\mathcal{B}^{H}$, which can be used to accelerate and stabilize value function learning.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Planning to Explore", "weight": 1.0} -->

The ability of an agent to explore the relevant parts of the state space is critical for the convergence of many RL algorithms. Typical exploration strategies like $\epsilon$-greedy and Boltzmann take exploratory actions with some probability on a per time-step basis. Instead, by using MPC, the agent can explore in the space of trajectories. The agent can consider a hypothesis of potential reward regions in the state space, and then execute the optimal trajectory conditioned on this belief, resulting in a temporally coordinated sequence of actions. By executing such coordinated actions, the agent can cover the state space more rapidly and intentionally, and avoid back and forth wandering that can slow down the learning. We demonstrate this effect empirically in Section 3.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Planning to Explore", "weight": 1.0} -->

To generate the hypothesis of potentially rewarding regions, we take a Bayesian view and approximately track a posterior over value functions. Consider a motivating setting of regression, where we have a parametric function approximator $f_{\theta}$ with prior ${\mathbb{P}}{(\theta)}$. The dataset consists of input-output pairs: $\mathcal{D} = {(x_{i},y_{i})}_{i = 1}^{n}$, and we wish to approximate ${\mathbb{P}}{(\left. \theta \middle| \mathcal{D} \right.)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Planning to Explore", "weight": 1.0} -->

In the Bayesian linear regression setting with Gaussian prior and noise models, the solution to the following problem generates samples from the posterior Osband2018RandomizedPF: where ${\overset{\sim}{y}}_{i} \sim {\mathcal{N}{(y_{i},\sigma^{2})}}$ is a noisy version of the target and $\overset{\sim}{\theta} \sim {{\mathbb{P}}{(\theta)}}$ is a sample from the prior. Based on this, Osband et al. Osband2018RandomizedPF demonstrate the benefits of uncertainty estimation for exploration. Similarly, we use this procedure to obtain samples from the posterior for value function approximation, and utilize them for temporally coordinated action selection using MPC. We consider $K$ value function approximators ${\hat{V}}_{\theta}$ with parameters $\theta_{1},\theta_{2},{\ldots\theta_{K}}$ independently trained based on eq..

<!-- chunk {"id": "body-0021", "role": "body", "section": "Planning to Explore", "weight": 1.0} -->

We consider the softmax of the different samples as the value at a state: Since the log-sum-exp function approximates mean + variance for small $\kappa > 0$ Dvijotham2014UniversalCV; Todorov2009CompositionalityOO, this procedure encourages the agent to additionally explore parts of the state space where the disagreement between the function approximators is large. This corresponds to the broad notion of optimism in the face of uncertainty (auer2002finite,) which has been successful in a number of applications (AlphaGo Li2010ACA,).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

1: Inputs: planning horizon H, value function parameters θ1, θ2, … θK, mini-batch size n, number of gradient steps G, update frequency Z 3: Select action at according to MPC (eq. 3) with terminal reward rf (s) ≡ V̂ (s) from eq. 4: Add the state experience st to replay buffer 𝒟 7: Sample n states from the replay buffer, and compute targets using eq. 8: Update the value functions using eq. (see Section 2.5 for details) Algorithm 1 Plan Online and Learn Offline (POLO) To summarize, POLO utilizes a global value function approximation scheme, a local trajectory optimization subroutine, and an optimistic exploration scheme. POLO operates as follows: when acting in the world, the agent uses the internal model and always picks the optimal action suggested by MPC. Exploration is implicitly handled by tracking the value function uncertainties and the optimistic evaluation, as specified in eq. and. All the experience (visited states) from the world are stored into a replay buffer $\mathcal{D}$, with old experiences discarded if the buffer becomes full.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

After every $Z$ steps of acting in the world and collecting experience, the value functions are updated: (a) constructing the targets according to eq.; (b) performing regression using the randomized prior scheme using eq. where $f_{\theta}$ corresponds to the value function approximator. For state $s_{i}$ in the buffer and value network $k$ with parameters $\theta_{k}$, the targets are constructed as: which corresponds to solving a $N -$step trajectory optimization problem. As described earlier, using trajectory optimization to generate the targets for fitting the value approximation accelerates the convergence and makes the learning more stable, as verified experimentally in Section 3.3. The overall procedure is summarized in Algorithm 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Empirical Results and Discussion", "weight": 1.0} -->

Through empirical evaluation, we wish to answer the following questions: Does trajectory optimization in conjunction with uncertainty estimation in value function approximation result in temporally coordinated exploration strategies?

<!-- chunk {"id": "body-0025", "role": "body", "section": "Empirical Results and Discussion", "weight": 1.0} -->

Can the use of an approximate value function help reduce the planning horizon for MPC?

<!-- chunk {"id": "body-0026", "role": "body", "section": "Empirical Results and Discussion", "weight": 1.0} -->

Does trajectory optimization enable faster and more stable value function learning?

<!-- chunk {"id": "body-0027", "role": "body", "section": "Empirical Results and Discussion", "weight": 1.0} -->

Before answering the questions in detail, we first point out that POLO can scale up to complex high-dimensional agents like 3D humanoid schulman2015high and dexterous anthropomorphic hand OpenAIHand; Rajeswaran-RSS-18 which are among the most complex tasks studied in RL for robotics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Trajectory optimization for exploration", "weight": 1.0} -->

Exploration is critical in tasks where immediate rewards are not well aligned with long-term objectives. As a representative problem, we consider a point mass agent in different 2D worlds illustrated in figure 2: a simple finite size box with no obstacles and a maze. This domain serves to provide an intuitive understanding of the interaction between trajectory optimization and exploration while also enabling visualization of results. In the extreme case of no rewards in the world, an agent with only local information would need to continuously explore. We wish to understand how POLO, with its ensemble of value functions tracking uncertainties, uses MPC to perform temporally coordinated actions. Our baseline is an agent that employs random exploration on a per-time-step basis; MPC without a value function would not move due to lack of local extrinsic rewards. Second, we consider an agent that performs uncertainty estimation similar to POLO but selects actions greedily (i.e. POLO with a planning horizon of $1$). Finally, we consider the POLO agent which tracks value uncertainties and selects actions using a 32-step MPC procedure. We observe that POLO achieves more region coverage in both point mass worlds compared to alternatives, as quantitatively illustrated in figure 2(a).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Trajectory optimization for exploration", "weight": 1.0} -->

The ensemble value function in POLO allows the agent to recognize the true, low value of visited states, while preserving an optimistic value elsewhere. Temporally coordinated action is necessary in the maze world; POLO is able to navigate down all corridors.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Value function approximation for trajectory optimization", "weight": 1.0} -->

Next, we study if value learning helps to reduce the planning horizon for MPC. To this end, we consider two high dimensional tasks: humanoid getup where a 3D humanoid needs to learn to stand up from the ground, and in-hand manipulation where a five-fingered hand needs to re-orient a cube to a desired configuration that is randomized every $75$ timesteps. For simplicity, we use the MPPI algorithm (williams2016aggressive, ) for trajectory optimization. In Figure 3, we consider MPC and the full POLO algorithm of the same horizon, and compare their performance after $T$ steps of learning in the world. We find that POLO uniformly dominates MPC, indicating that the agent is consolidating experience from the world into the value function. With a short planning horizon, the humanoid getup task has a local solution where it can quickly sit up, but cannot discover a chain of actions required to stand upright. POLO's exploration allows the agent to escape the local solution, and consolidate the experiences to consistently stand up. To further test if the learned value function is task aligned, we take the value function trained with POLO, and use it with MPC *without any intermediate rewards*.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Value function approximation for trajectory optimization", "weight": 1.0} -->

Thus, the MPC is optimizing a trajectory of length $H = 64$ purely using the value function of the state after $64$ steps. We observe, in Figure 3, that even in this case, the humanoid is able to consistently increase its height from the floor indicating that the value function has captured task relevant details. We note that a greedy optimization procedure with this value function does not yield good results, indicating that the learned value function is only approximate and not good everywhere.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Value function approximation for trajectory optimization", "weight": 1.0} -->

While the humanoid getup task presents a temporal complexity requiring a large planning horizon, the in-hand manipulation task presents a spatial complexity. A large number of time steps are not needed to manipulate the object, and a strong signal about progress is readily received. However, since the targets can change rapidly, the variance in gradient estimates can be very high for function approximation methods Ghosh2017DivideandConquerRL. Trajectory optimization is particularly well suited for such types of problems, since it can efficiently compute near-optimal actions conditioned on the instance, facilitating function approximation. Note that the trajectory optimizer is unaware that the targets can change, and attempts to optimize a trajectory for a fixed instance of the task. The value function consolidates experience over multiple target changes, and learns to give high values to states that are not just immediately good but provide a large space of affordances for the possible upcoming tasks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trajectory optimization for value function learning", "weight": 1.0} -->

Finally, we study if trajectory optimization can aid in accelerating and stabilizing value function learning. To do so, we again consider the humanoid getup task and study different variants of POLO. In particular, we vary the horizon $(N)$ used for computing the value function targets in eq.. We observe that as we increase $N$, the agent learns the value function with fewer interactions with the world, as indicated in Figure 4(a). The benefit of using $N -$step returns for stable value function learning and actor-critic methods have been observed in numerous works (A3C Retrace GAE, ), and our experiments reinforce these observations. The use of $N -$step returns help to traverse the bias-variance trade-off. Furthermore, due to the discounting, the contribution of $V{(s_{N})}$ is made weaker and thus the targets are more stable. This mirrors ideas such as target networks (mnih2015human, ) commonly used to stabilize training. As discussed earlier, longer horizons make trajectory optimization more tolerant to errors in the value function.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trajectory optimization for value function learning", "weight": 1.0} -->

To illustrate this, we take the value function trained with POLO on a nominal humanoid model, and perturb the model by changing the size of the head to model value function degradation. Figure 4(b) shows that a longer planning horizon can mitigate this degradation. This presents intriguing future possibility of using MPC to improve transfer learning between tasks or robot platforms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

In this work we presented POLO, which combines the strengths of trajectory optimization and value function learning. In addition, we studied the benefits of planning for exploration in settings where we track uncertainties in the value function. Together, these components enabled control of complex agents like 3D humanoid and five-fingered hand. In this work, we assumed access to an accurate internal dynamics model. A natural next step is to study the influence of approximation errors in the internal model and improving it over time using the real world interaction data.
