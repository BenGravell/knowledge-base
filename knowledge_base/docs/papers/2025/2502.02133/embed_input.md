<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Synthesis of Model Predictive Control and Reinforcement Learning: Survey and Classification

Topics include Reinforcement learning, Model predictive control, Predictive control, Robotics, Autonomous driving, Classification, Online algorithms, Optimization, Control, Learning, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The fields of MPC and RL consider two successful control techniques for Markov decision processes. Both approaches are derived from similar fundamental principles, and both are widely used in practical applications, including robotics, process control, energy systems, and autonomous driving. Despite their similarities, MPC and RL follow distinct paradigms that emerged from diverse communities and different requirements. Various technical discrepancies, particularly the role of an environment model as part of the algorithm, lead to methodologies with nearly complementary advantages. Due to their orthogonal benefits, research interest in combination methods has recently increased significantly, leading to a large and growing set of complex ideas leveraging MPC and RL. This work illuminates the differences, similarities, and fundamentals that allow for different combination algorithms and categorizes existing work accordingly. Particularly, we focus on the versatile actor-critic RL approach as a basis for our categorization and examine how the online optimization approach of MPC can be used to improve the overall closed-loop performance of a policy.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

S OLVING Markov decision processes (MDPs) online is a large and active research domain where different research communities have developed various solution approaches. An MDP can be stated as the problem of computing the optimal policy of an agent interacting with a stochastic environment that minimizes a cost function, possibly over an infinite horizon. Two common approaches for obtaining optimal policies are model predictive control (MPC) and reinforcement learning (RL).

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Within MPC, an optimization problem that approximates the MDP is solved online, involving a simulation of an internal This research was supported by DFG via Research Unit FOR 2401 and project 424107692, by the EU via ELO-X 953348, and by NFR through the project Safe Reinforcement Learning using Model Predictive Control (SARLEM, grant number 300172).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Rudolf Reiter, Florian Messerer, Katrin Baumg¨ artner and Moritz Diehl are with the Department of Microsystems Engineering (IMTEK), University of Freiburg, 79110 Freiburg, Germany (e-mail: { rudolf.reiter, florian.messerer, katrin.baumgaertner, moritz.diehl } @imtek.uni-freiburg.de).

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Jasper Hoffmann and Joschka Boedecker are with the Department of Computer Science, University of Freiburg, 79110 Freiburg, Germany (e-mail: { hofmaja, jboedeck } @informatik.uni-freiburg.de).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Dirk Reinhardt, Shambhuraj Sawant and Sebastien Gros are with the Department of Engineering Cybernetics, Norwegian University of Science and Technology (NTNU), 7034 Trondheim, Norway (e-mail: { dirk.p.reinhardt, shambhuraj.sawant, sebastien.gros } @ntnu.no). prediction model. The optimized controls are applied to the real-world environment in a closed loop at each time step. Historically, MPC has been developed within the field of optimization-based control engineering, driven by the success of optimization algorithms, e.g., linear programming. MPC design leverages domain knowledge to compose mathematical models, often by first principles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In contrast, within the RL framework, a policy is expressed as a parameterized explicit function of the state. The policy is iteratively improved by interacting with the environment and adapting its parameters related to the observed cost. In general, RL algorithms are not required to use models of the environment, but often, models are used during training for offline simulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Both MPC and RL found their way into classical realworld control. The applications differ depending on the availability of training data. MPC is used where measurement data is scarce and expensive, and the environment can be described by optimization-friendly models. On the contrary, RL is successfully implemented in settings where lots of training data can be generated,.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Besides their sampling efficiency, several further advantages and disadvantages of both methods are nearly orthogonal, i.e., weaknesses of either approach are strengths of the other. For instance, RL struggles with safety issues, whereas MPC can guarantee constraint satisfaction related to a particular environment model. This motivated many authors to combine the advantages and synthesize novel algorithms that build on both approaches.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper's contribution is twofold. We first analyze the properties and orthogonal strengths of MPC and RL. Secondly, we propose a systematic overview of how MPC can be combined with RL and provide an extensive literature overview guided by the proposed classification. This survey reviews practical and theoretical work and concludes with a section on available open-source software.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview", "weight": 1.0} -->

On a high level, this paper is structured into an introductory part, a comparison, and a classification scheme and survey of synthesis approaches. An overview is provided in Fig. 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview", "weight": 1.0} -->

The introductory part introduces in Sect. II the general problem setting. Sect. III and IV describe the main concepts behind RL and MPC and discuss how they aim at solving the general problem of Sect. II. Both of these sections are split into a conceptual and an algorithmic part, providing the basis for the remainder of this work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview", "weight": 1.0} -->

The comparison in Sect. V highlights practical differences between both approaches and surveys applied comparisons. Experts in the field of MPC and RL may skip Sect. III, IV and potentially the comparison in Sect. V.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview", "weight": 1.0} -->

The remaining paramount sections are devoted to the classification and review of combinations of both approaches. In Sect. VI, essential concepts are introduced to categorize existing combination variants based on the actor-critic framework of RL. Following the proposed categorization, literature that uses MPC as an expert for training an RL agent is summarized in Sect. VII. The most widespread variants using MPC within the policy are outlined in Sect. VIII, and variants that use the MPC to determine the value function at a particular state are surveyed in Sect. IX. An additional Sect. X focusses on important theoretical results from the field of MPC and RL and is aligned with the previous categorization. Current open-source software is presented in Sect. XI.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview", "weight": 1.0} -->

The work is concluded and discussed in Sect. XII.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

This section describes the Markov decision process (MDP) framework - a central concept for both RL and MPC.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

MDPs provide a framework for modeling a discrete-time stochastic decision process. An MDP is defined over a state space S, an action space A, and a stochastic transition model describing a probability distribution over the next states given a current state and action. A stage cost l (s, a) with l: S × A → R ∪ {∞} defines the cost of each state-action pair, typically discounted by a factor γ ∈ (0, 1]. The MDP is then defined by the 5-tuple Solving the MDP refers to obtaining actions that minimize the discounted stage cost, which is elaborated in the following.

<!-- chunk {"id": "body-0019", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

For solving MDPs we introduce stochastic policies π: S → Dist(A) that map a state to a probability distribution over possible actions. The value function V π: S → R ∪ {∞} is the discounted expected future cost starting from state s and following a policy π defined by Fig. 1: Paper structure. The main sections are highlighted in gray, subchapters in white, tables are green.

<!-- chunk {"id": "body-0020", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

The state S k and action A k describe a sequence of random variables generated by applying the policy π on the MDP.

<!-- chunk {"id": "body-0021", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

The aim of solving the MDP is to obtain an optimal policy π ⋆ TABLE I: Symbols used within this paper. that minimizes the expected cost for all states via Solving this equation is often also shortly referred to as solving the MDP. Note that the intersection in is never empty, and there also always exists an optimal deterministic policy µ ⋆ satisfying. All optimal policies π ⋆ share the same optimal value function V ⋆:= V π ⋆. In addition to the value function, the action-value function Q π: S × A → R ∪{∞} of a policy is the expected value of first applying an action a at the current state s and following the stochastic policy π afterwards.

<!-- chunk {"id": "body-0022", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

We define as V ⋆:= V π ⋆ and Q ⋆:= Q π ⋆ the optimal value and action-value functions. The identities are relating the optimal value function and the optimal policy to the optimal action-value function. In cases with multiple optimal actions for a state s, an optimal policy π ⋆ can be stochastic and randomly selects an action in the set of optimal actions with any probability.

<!-- chunk {"id": "body-0023", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

Remark 2.1: The optimal policy for a finite horizon problem is generally time-varying unless the terminal cost is V ⋆. Timevarying environments can be described in terms of by augmenting the state with an additional clock state.

<!-- chunk {"id": "body-0024", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

In the following, we introduce MPC and RL, the two pivotal frameworks of this survey for approximately solving MDPs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "REINFORCEMENT LEARNING", "weight": 1.0} -->

RL is a powerful approach for solving MDPs using concepts from dynamic programming, Monte Carlo simulation, and stochastic approximation. RL typically involves an agent modeled by a policy iteratively collecting data by interacting with an environment, which could be a simulation model or the real world. The collected data, consisting of state transitions, applied actions, and costs, is then used to iteratively update the policy. In most RL methods, an optimal policy is approximated via estimating the optimal action-value function using temporal difference (TD) learning or by iteratively updating the policy using policy gradient (PG) methods, whereas in actor-critic methods both forms are combined.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

In this section, a short theoretical overview of RL is provided, including dynamic programming, temporal difference methods, and policy gradient methods. 1) Dynamic Programming: Introduced, dynamic programming (DP) provides the theoretical foundation for many algorithms in RL. DP solves MDPs with known transition models by breaking them into subproblems and using stored solutions to avoid recomputation. DP systematically updates value functions given complete knowledge of the environments MDP. A general DP approach to find the action-value function Q π of a given policy π can be described by the Bellman operator T π: R S×A → R S×A, where S + is the next sampled state and A + a sampled action. In the space of value functions, the Bellman operator T π is a contraction mapping for γ < 1 with respect to the state supremum norm, and Q π is the unique fixed point. In other words, one can start with an arbitrary action-value function Q ∈ R S×A and iteratively apply T π to converge to the action-value function Q π. Determining V π and Q π for a fixed policy π is referred to as policy evaluation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Similar to the Bellman operator T π, the Bellman optimality operator T: R S×A → R S×A is defined as Equivalently to T π, T is a contraction mapping for γ < 1. Iteratively applying T on an arbitrary action-value function Q ∈ R S×A converges to the optimal value function Q ⋆. The resulting method is called value iteration (VI) and, differently to policy evaluation, tries to solve MDPs of implicitly by finding the optimal value function Q ⋆.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

The main drawback of DP methods is the unfavorable scaling to high-dimensional or continuous state and action spaces, which is often referred to as the curse of dimensionality. DP methods require full knowledge of the environment model P, which is a fundamental limitation compared to more generic model-free RL algorithms. Approximate DP (ADP) addresses the curse of dimensionality by using different approximation strategies to extend classical DP, as discussed in the following in the context of RL. 2) TD Methods: To avoid the scaling issues of DP, temporal difference (TD) methods introduce two extensions: Firstly, they learn the value functions V π or Q π for a policy π and their optimal versions V ⋆ and Q ⋆ with only transition samples utilizing stochastic approximation and without explicitly requiring a transition model P. Secondly, they use an adaptive exploration-exploitation strategy to decide favorable states for which the value function is updated.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

In the following, different TD learning algorithms are presented. The simplest policy evaluation method is called TD, which estimates the value function V π for a given policy π. Given a current value function V, an update for a given state S for V is defined by where ← denotes overwriting the function V at S, α > 0 denotes the learning rate, A ∼ π (·| S) a sampled action from the policy π at state S and S + ∼ P (·| S, A) the next state sampled from the stochastic model. Furthermore, δ is called the temporal difference, measuring the stochastic difference between the sampled target l (S, A) + γV (S +) and the current estimate V (S). Finally, the distribution D π is a sampling or exploration strategy where the fixed policy π sequentially generates new states by interacting with the environment. For a more technical discussion, see Remark 3.1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Remark 3.1: The notations S ∼ D π or (S, A) ∼ D π are mathematically not well defined as distributions. Without further elaboration, given an initial state s, an episode is simply run iteratively by applying a policy π: After each time step, an update can then be performed by a TD method. We still use this notation for instructional purposes, especially to highlight which policy was used to generate states and actions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Similar to DP, under some technical assumptions from stochastic approximation theory, the update scheme converges to the unique fixpoint V π. For example, one assumption is that the learning rate α must decrease to zero over time. The update scheme of can be extended to also learn Q π.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Besides estimating the value function V π or Q π for given policies π, a main target of RL algorithms is learning the optimal value functions V ⋆ and Q ⋆. For instance, the SARSA algorithm is an RL method for approximating the optimal value function Q ⋆ and given by the update rule The ϵ -greedy policy is implicitly defined by Q via where for notational convenience, it is assumed that there is only one optimal action for a given state s. Note that π ϵ Q is used to sample the next action A + ∼ π ϵ Q and to generate the state and action with D π ϵ Q, where the update is performed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Another variant for learning the optimal action-value function Q ⋆ is the popular Q-learning method, which, instead of sampling an ϵ -greedy action like SARSA, takes the greedy action to build the temporal difference. More explicitly, the update rule is defined via Note that Q-learning still uses the ϵ -greedy exploration policy to sample (S, A) ∼ D π ϵ Q in (13c), whereas the policy that is used for the temporal difference is the greedy policy. Thus, Q-learning is called an off-policy method, whereas SARSA is an on-policy method as the same ϵ -greedy policy is used for exploration and the temporal difference update. For a more elaborate discussion, see.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

As discussed, an essential motivation for TD methods is that learning a value function on the whole state space can be intractable, which is one of the major drawbacks of DP. Importantly, typically only a fraction of the state space is encountered under a given policy or an optimal policy. Thus, TD methods often incorporate a trade-off between exploring the state space and exploiting current knowledge using strategies like the ϵ -greedy policy π ϵ Q. Yet, for discrete state spaces, convergence to Q ⋆ is only guaranteed if each state and action is seen infinitely often. 3) Policy Gradient Methods: Different from the previous methods, policy gradient (PG) methods directly optimize a parameterized policy π θ that can be used for discrete and continuous action spaces A. Given a parameterized policy π θ: S → Dist(A) and an initial state distribution ρ 0 ∈ Distr(S), the goal of PG methods is to find the optimal parameters θ ⋆ that minimize the expected return where ρ π is the discounted visitation frequency defined as follows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

Given a policy π θ, the environment model P and an initial state s, let p (s → s +, k, π θ) be the probability of reaching state s + at time step k by starting from state s following policy π θ. The normalized discounted visitation frequency is defined by ρ π θ (s +):= (1 -γ) E S ∼ ρ 0 [∑ ∞ k =1 γ k -1 p (S → s +, k, π θ)]. It is important to highlight that finding a policy that minimizes the objective of is less restricting as solving the MDP over the full state space as defined. The reasoning is that some parts of the state space might not be reached by the policy, which could be omitted if the support of the initial state distribution ρ 0 is required to cover the whole state space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

In order to find an update direction in which the expected return improves, its gradient ∇ θ J π (θ) is required. Different reformulations of exist that allow one to derive sample estimates of the gradient of the PG objective, ∇ θ J π (θ). First, the stochastic policy-gradient theorem reformulates the policy gradient by building the theoretical foundation of the REINFORCE algorithm or the first actor-critic methods. A derivation is provided.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

The second reformulation is called the deterministic policy gradient theorem. Let µ θ: S → A be a deterministic policy. By differentiating through the expected state-action value function Q µ θ the deterministic PG (DPG) is obtained by A derivation is provided. The advantage of the DPG is particularly prominent in high-dimensional action spaces since in the stochastic PG, actions A are sampled to estimate the gradient, leading potentially to a higher gradient variance. Thus, the DPG formulation is used in many of the state-of-theart methods like twin-delayed actor-critic (TD3) and soft actor-critic (SAC). A concrete algorithm for an actor-critic algorithm using the DPG is provided in section III-B2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Theoretical Background", "weight": 1.0} -->

An important distinction between the stochastic PG and the DPG is the ability to handle discrete action spaces. With the stochastic PG, discrete and continuous action spaces can be directly optimized, whereas the DPG requires a differentiable parameterized policy with respect to the parameters. To circumvent this problem, some work extends the DPG to stochastic policies using relaxation techniques to differentiate through the sampling process of the discrete actions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

In the following, an overview of four influential deep RL algorithms, namely deep Q-networks (DQN), deep deterministic PG (DDPG), proximal policy optimization (PPO) and soft actor-critic (SAC) is given. 1) Deep Q-Networks: Function approximators like NNs approximate the action-value function to extend Q-learning to continuous state spaces. One prominent implementation of this is DQN, a combination of deep learning and RL. DQN collects transition samples in a buffer D buffer and minimizes the mean squared error between the current value function Q w and the sampled target value by For the sample target, a fixed copy ¯ w of the parameter w is used that is only periodically updated. This stabilizes the training. For an overview of different function approximation methods and their potential instabilities, see.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

Given a parameterized Q-function Q w, the resulting update scheme from DQN is given by The update rule in (18a) provides a sample-based estimate of the gradient, where B represents the batch size used for the update and α w a learning rate. Averaging over multiple samples is often called mini-batch training and leads to improved performance and accelerated convergence when training NN. Exploration in DQN is handled again by the ϵ -greedy policy π ϵ Q. Differently to the update scheme of Q-learning, the buffer D buffer stores state and actions that were generated from previous policies derived from Q w earlier in the training. Similar to Q-learning, DQN is also an off-policy method. 2) Deep Deterministic Policy Gradient: Extending DQN, deep deterministic PG (DDPG) is an off-policy actorcritic method that learns a deterministic policy µ θ and a value function Q w in parallel. Both the actor and the critic are NN s. The update rule of DDPG is given by DDPG (µ θ ≈ π ⋆) where Q ← denotes the update for Q and µ ← denotes the update for µ.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

As can be seen from the update scheme, the critic Q w is used to update the actor µ θ in (19b), in that sense 'criticizing' the actor. Differently to the update rule of DQN (18a), where the greedy action is considered to build the temporal difference, in DDPG, a single evaluation update with respect to the current policy µ θ is performed. The buffer D buffer is filled up over time by using the policy µ θ + ξ, where ξ is either an Ornstein-Uhlenbeck process for temporally correlated noise or a Gaussian. 3) Proximal-Policy Optimization: A popular on-policy actorcritic method that can be used for discrete and continuous action spaces is proximal policy optimization (PPO). Prior to each policy and critic update, data in the form of multiple episodes is collected. Since PPO is an on-policy method, transitions generated earlier in the training by outdated policies are discarded. In practice, PPO is often used with highspeed simulation environments, where generating new samples comes with low computational costs. A main advantage of PPO is its ability to prevent drastic parameter updates that could potentially destabilize the training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

Similar to trust region methods, this is achieved by restricting the policy update.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

During training, a stochastic policy π θ - often a parameterized Gaussian - is used. Assuming a given initial state s 0, a trajectory is drawn by the forward simulation S k +1 ∼ P (·| S k, A k) and A k ∼ π θ (·| S k) until a maximum roll-out length M. Given multiple roll-outs, an estimate ˆ A (S k, A k) of the advantage function defined by A π (S k, A k):= Q π (S k, A k) -V π (S k) can be derived, see. Additionally, with the probability ratio R k (θ):= π θ (A k | S k) /π ¯ θ (A k | S k), which measures how much the new policy π θ changes with respect to the current policy π ¯ θ, the PPO clipping objective is defined by where the clip function projects the ratio R k to an interval from 1 -ϵ to 1 + ϵ. Note that the clipping objective requires maximization, whereas the original PPO objective involves minimization, as in this work, costs are minimized rather than rewards being maximized.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

One of the primary advantages of PPO is its simplicity and ease of implementation compared to previous methods based on trust region optimization, see. A proof of convergence of PPO to the optimal policy for discrete MDPs is given. 4) Soft Actor-Critic: The SAC algorithm, is a widely used off-policy actor-critic method that incorporates an entropy bonus for stochastic policies with higher entropy. Using entropy regularization is considered in the framework of maximum-entropy RL. Like DQN and DDPG, SAC optimizes the policy in an off-policy manner collecting transitions encountered during training in a replay buffer, leading to an improved sample efficiency when compared to PPO.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

SAC extends the objective by introducing an entropy regularization term, leading to a 'soft' policy gradient objective where H denotes the entropy of the paramterized policy π θ (·| S) at the sampled state S. Given a distribution X, the entropy is defined by H (X) = E [-log(X)]. The entropy regularization, scaled by the parameter λ H, encourages exploration, stabilizes policy training and can lead to more robust policies. Additionally, it has been shown in that for discrete MDPs, the error introduced by the entropy regularization decreases exponentially to the inverse regularization strength, 1 /λ H.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Deep Reinforcement Learning Methods", "weight": 1.0} -->

In TD3, twin Q-networks addressing the overestimation bias in Q-value estimation were introduced. Whereas, the fundamentals of SAC are described, introduced an improved version using twin Q-networks and automatic tuning of the entropy regularization with λ H. The latter builds the basis for most implementations in current RL software frameworks.

<!-- chunk {"id": "body-0047", "role": "body", "section": "MODEL PREDICTIVE CONTROL", "weight": 1.0} -->

This section introduces MPC, a commonly used framework to obtain policies for continuous MDPs. MPC utilizes a typically deterministic - model that approximates the true stochastic environment,. Starting from the current environment state, MPC uses the internal model to predict how different choices of the planned control trajectory would affect the state trajectory and evaluates the cost associated with this prediction. Usually, evaluating the MPC policy involves solving an optimization problem online to obtain the control input. In this section, we will first give an overview of MPC problem formulations and the relevant considerations, followed by a discussion of algorithms used for finding their solution.

<!-- chunk {"id": "body-0048", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

Solving the MDP optimization problem is, in general, intractable due to several reasons, including the infinite horizon, the optimization over the space of policy functions, and the expectation over nonlinear transformations of stochastic variables. MPC leverages several approximations of in order to derive a computationally tractable optimization problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

As a first step, the optimal policy is computed only for the current state s and the infinite horizon in and is approximated by a finite horizon, resulting in the optimization problem where the terminal cost function ¯ V π is an approximation of the exact value (or cost-to-go) function V π. In the second step, the true stochastic state transition S k +1 ∼ P (S k, A k) is approximated by a simplified model. The most commonly used formulation is nominal MPC, in which a deterministic model is used, i.e., x k +1 = f MPC (x k, a k). Hence, uncertainty is not explicitly considered. Here, we introduced x k ∈ S to denote predictions of the state within the MPC problem. Since a deterministic model does not capture the possibility of deviations from the prediction, the planned action trajectory is a trajectory of fixed actions (u 0,..., u N -1), u k ∈ A, as opposed to a policy function π. The resulting deterministic optimal control problem is given by where ¯ V ⋆ is an approximation of the optimal terminal value function.

<!-- chunk {"id": "body-0050", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

In the MDP framework, the stage cost l (x k, u k) may assign some regions of the state space an infinite cost in order to prohibit them. Similarly, due to actuator limitations, the action space A is often a compact subset of R n u. In numerical optimization, this is typically handled by explicitly considering constraints h MPC (x k, u k) and the terminal safe set h MPC N (x k, u k) as part of the problem formulation. This results in a constrained nonlinear program (NLP), associated with the MPC value function V MPC (s) and the terminal value function ¯ V MPC (s) within the NLP formulation, and can be stated as using the vector of decision variables z = (x 0,... x N, u 0,..., u N -1) ∈ R n z. In the above formulation, we introduced the state trajectory (x 0,..., x N) as additional decision variables, which are constrained to start at the given value of the current state (22b), and to follow the system dynamics (22c).

<!-- chunk {"id": "body-0051", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

This is in contrast to formulation, where the state trajectory is considered as an explicit function of the action trajectory. Both approaches are equivalent in terms of the solutions they admit. However, the iterations of numerical optimization algorithms may differ depending on the formulation. The formulation in is referred to as a single shooting or sequential formulation, whereas is a multiple shooting or simultaneous formulation. For nonlinear unstable systems, the latter is typically preferable.

<!-- chunk {"id": "body-0052", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

When deploying MPC, the NLP is solved online at every discrete time instant, based on a specified value of the current state s. This yields an optimal trajectory of actions, ( u ⋆ 0,..., u ⋆ N -1 ), of which only the first one, u ⋆ 0, is applied to the environment. The resulting new state is then used as the initial state for the next optimization problem, and a new input trajectory is computed. Hence MPC defines a policy.

<!-- chunk {"id": "body-0053", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

Similarly to the definition of the value function, we can define the corresponding Q-function by additionally fixing the initial action vector u 0 to the given value, Based on this Q-function and assuming a unique minimizer, the MPC policy is where µ instead of π is used to denote that the MPC policy is deterministic.

<!-- chunk {"id": "body-0054", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

We now take a closer look at the components of the MPC problem, followed by various other relevant considerations. 1) Dynamics model: The central component is the dynamics constraint (22c), in which f MPC (x, u) is a model of the environment. This model can be derived from first principles or identified from data. In the case of nominal MPC, it is deterministic and does not consider the stochasticity of. 2) Objective: The stage cost l MPC (x, u) in the MPC objective (22a) commonly corresponds to the stage cost of the MDP. Note that the stage cost may be implicitly time-varying by including an augmented clock state. Thus, it may implicitly include a discounting factor γ. Crucially, the MPC optimization problem needs to be numerically tractable, and the ultimate goal is to provide a policy that achieves a sufficient closed-loop performance when applied to the real environment. Therefore, the stage cost may also be approximated by a function with favorable numerical properties. Often, the stage cost imposes a convex penalty on the deviation of the action and state trajectories from a reference point or trajectory.

<!-- chunk {"id": "body-0055", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

This is referred to as regulatory MPC or tracking MPC. The focus in regulatory MPC problems is mostly the stabilization of systems. Historically, the ability of MPC to incorporate inequality constraints and to handle multiple inputs simultaneously justified the additional computational complexity. In contrast, economic MPC uses a cost that directly expresses a quantity of interest to optimize, e.g., time, energy use, financial cost, or yield of a production process. Therefore, economic MPC is closely related to solving MDPs beyond stabilization.

<!-- chunk {"id": "body-0056", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

The terminal cost ¯ V MPC (x) should ideally capture the cost-to-go at the end of the MPC horizon, cf.. The choice of horizon length and terminal cost is often crucial for the performance of the resulting MPC policy. Indeed, a close-to-optimal cost-to-go approximation via the terminal cost allows for shorter prediction horizons. The approximation quality becomes less important as the horizon length grows, and ¯ V MPC (x N) ≡ 0 is a widely used choice. However, the NLP becomes computationally more expensive for longer horizons. Thus, the horizon length is typically limited by the available computational resources. In practice, the terminal cost function is often chosen heuristically or based on stability considerations. Still, there is also research on how to explicitly select it as an approximation of the infinite-horizon cost (with respect to the MPC cost), e.g., by simulating forward a pre-selected simple feedback law.

<!-- chunk {"id": "body-0057", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

When stabilizing a system at a steady state using a locally smooth convex stage cost, a straightforward choice is the infinite horizon linear quadratic regulator (LQR) cost computed for the system resulting from the linearization of the model (22c) at that steady state. 3) Constraints: The final components are the stage and terminal constraints. Stage constraints (22d) can be used to avoid prohibited regions of the state space and to take into account actuator constraints. Terminal constraints (22e) can be used to ensure stability and recursive feasibility of the resulting MPC policy. For the terminal constraints, considerations similar to the terminal cost apply. In principle, they should capture the system's future behavior over the infinite horizon and ensure that the MPC plan will not be too short-sighted regarding the stability and recursive feasibility of the resulting MPC policy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

Constraints can lead to situations in which is infeasible for the current initial state value s, i.e., there exists no value for the decision variables such that all constraints are satisfied. Consequently, the solver would not be able to return a solution, and the evaluation of the MPC policy would fail. Thus, for practical MPC implementations, it can often be helpful not to enforce the constraints strictly but to penalize their violation. For exact penalties with sufficiently high penalty weight, constraint satisfaction is guaranteed if the original problem is feasible,. Otherwise, a solution that minimizes the constraint violation is returned. 4) Uncertainty-aware MPC: In contrast to the deterministic model in (22c), stochastic and robust MPC formulations explicitly take into account the uncertainty of the model prediction. The former models the uncertainty as a probability distribution, whereas the latter predicts bounded sets of all possible realizations (respective tractable outer approximations). Both can be separated into scenario, and tube, approaches. Scenario approaches consider discrete distributions, which may be obtained by sampling from a continuous distribution.

<!-- chunk {"id": "body-0059", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

This can take the form of sampling several disturbance trajectories separately and planning the corresponding state trajectories in parallel or of constructing a tree of scenarios that are branched at every time step. Tube approaches predict parameterized approximations of the state distribution respective uncertainty set trajectories. Typical parametrizations are, e.g., normal distributions, ellipsoids or polytopes. This allows for a finite-dimensional representation of the uncertainty, such that a tractable NLP is obtained.

<!-- chunk {"id": "body-0060", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

Both scenario and tube approaches can also be classified into open-loop and closed-loop formulations. Open-loop formulations plan only one fixed trajectory of actions. This can quickly lead to unrealistically conservative uncertainty predictions because they do not encode that the noise will be counteracted in the real environment by feedback. Closed-loop predictions consider future feedback, leading to more realistic predictions. Using scenario trees, this can be achieved by planning a distinct action for every tree node. This implicitly corresponds to planning over policies with respect to the discretized disturbance space because the actions depend on past disturbances. Here, nonanticipativity with respect to the causality of the policy should be carefully considered. Closed-loop tube approaches usually consider explicitly parameterized simple feedback laws, e.g., linear feedback, which reacts to state deviations from the tube center. These feedback laws can be precomputed, or optimized. While the optimization of state feedback gains is highly nonconvex even for linear systems, the optimization over affine disturbance feedback leads to equivalent convex, but also higher-dimensional, optimization problems,.

<!-- chunk {"id": "body-0061", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

In the context of polyhedral sets, it is, under some assumptions, sufficient to consider only their vertices, which results in tree-structured formulations,. 5) Optimization problem classification: Depending on the mathematical form of the functions, the optimization problem can be classified differently. This is relevant, as it informs both the choice of solution algorithm and the theory regarding the resulting policy. In linear MPC (LMPC), the model is linear, the constraint functions are affine, and the cost functions are convex quadratic, resulting in a quadratic program (QP). LMPC problems can be solved reliably and efficiently. This is often used in contrast to nonlinear model predictive control (NMPC), where typically the model is nonlinear, and the resulting optimization problem is an NLP. When the action space is discrete, this corresponds to an additional restriction of the action variables to the space of integers, resulting in a mixed-integer NLP (MINLP) or mixed-integer QP (MIQP). If the dynamics contain nonsmooth or discontinuous events, such as contact physics, this leads to mathematical programs with complementarity constraints (MPCCs).

<!-- chunk {"id": "body-0062", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

6) Suboptimality and control theory: As discussed, the MPC problem leverages several forms of approximations of the MDP. This opens the question of how the resulting MPC policy behaves with respect to the MDP or when applied to a real system. Since it solves the MDP only approximately, it can be considered a form of suboptimal control. An overview of several sources of suboptimality can be found. The suboptimality from the finite horizon approximation is analyzed. The consequences of approximating the expected value via sampling are addressed in the stochastic programming literature in the context of the sample average approximation. In, the authors analyze the suboptimality resulting from affine feedback parametrization in a robust problem formulation. The suboptimality of nominal MPC in a stochastic environment is analyzed in and regret bounds.

<!-- chunk {"id": "body-0063", "role": "body", "section": "MPC Problem Formulations", "weight": 1.0} -->

The control theory literature often asks a different, though closely related, question, see, e.g.. It investigates under which conditions the MPC policy exhibits desirable behavior. This includes system theoretical properties of the resulting closed-loop system, such as stability and properties like recursive feasibility i.e., the controller should not maneuver itself into a state in which the MPC problem becomes infeasible. MPC should also be able to work under model-plant mismatch and reject disturbances. This is referred to as inherent robustness, and the theory covers nominal MPC, which uses no uncertainty model but can also be extended to stochastic MPC, even if it is designed with respect to a wrong disturbance model. Additionally, fast-paced applications may only allow for a suboptimal solution to in the assigned computational budget. Stability, and inherent robustness results, also exist for this case. Further, while stability results are usually derived for continuous action spaces, they can also be generalized to discrete actuators.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

We distinguish two common and fundamentally different approaches to - possibly approximately - solving finite-horizon optimal control problem (OCP) formulations: Sampling-based methods and methods leveraging derivative-based numerical optimization. In the following, we briefly introduce and discuss both approaches, focusing on algorithms that address the nominal OCP formulation. 1) Sampling-Based Methods: As a first class of methods, we consider sampling-based approaches that aim at finding an approximate solution to the stochastic open-loop or nominal OCP by sampling control trajectories and evaluating the associated cost via forward simulation.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

The simplest sampling-based method, also known as random shooting and used, e.g., in considers a finite number of independently sampled action sequences and the corresponding state trajectories, which are obtained via forward simulation. The algorithm then chooses the open-loop action trajectory associated with the lowest cost as an approximate solution.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

A second, more sophisticated, sampling-based approach is the cross-entropy method (CEM), where the probability distribution generating the open-loop action trajectory samples is iteratively refined based on previously sampled actions yielding low costs. In particular, CEM samples a finite number of action sequences and evaluates their associated costs via forward simulation. The action sequences yielding the lowest cost trajectories are used to adapt the probability distribution from which new action samples are generated. Typically, a Gaussian distribution or a Gaussian mixture model is used, in which the mean and covariance are adapted at each step. The method has been successfully implemented for MPC,.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

As a third sampling approach, we consider model predictive path integral control (MPPI), which provides a framework for solving MPC problems via trajectory sampling. In particular, the approach directly addresses the stochastic formulation without resorting to the nominal problem. As the method is derived based on a continuous-time model, we refer the interested reader to for an in-depth derivation. Crucially for this survey, the method poses some strong restrictions on the structure of the model and cost: First, the stochasticity of the dynamics needs to enter via the actions, i.e., f MPPI ( s k, a k + w k ), where w k is a random variable in the dimension of the actions. Secondly, the cost l MPC is assumed to be separable in states and actions, as well as quadratic in the actions with a weighting matrix that is inversely proportional to the noise variance. Furthermore, the main theoretical results and optimality (in the limit of infinite samples) only hold if the dynamics are affine in controls and noise. Similar to CEM, MPPI adaptively updates the probability distribution from which action trajectories are sampled.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

MPPI uses a weighted average to update the mean of this distribution where the weights are based on the associated costs. Since the underlying algorithm of MPPI requires limited implementation efforts, many papers use custom implementations. However, recently an efficient implementation as part of TorchRL and a CUDA-based parallel computation framework was published.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Sampling-based approaches naturally allow for stochastic models, and can thus directly tackle the stochastic open-loop OCP. Furthermore, sampling-based methods can be applied to problems with highly nonlinear, or even non-smooth, costs or dynamics as long as a simulator is available. While sampling-based optimization methods are typically straightforward to implement and benefit from parallelization, they scale poorly with the dimension of both the planning horizon and the dimension of the action space, i.e., they severely suffer from the curse of dimensionality. Furthermore, state constraints can be addressed only via penalty reformulations or the rejection of infeasible samples. For highly constrained systems, the rejection method further increases the sampling complexity. 2) Derivative-Based Numerical Optimization: As a second class of methods, we discuss derivative-based numerical optimization. On this account, approaches derived from a continuous-time OCP formulation, such as, e.g., indirect methods, collocation, and pseudospectral methods, as well as numerical simulation methods, fall into this class, but are outside of the scope of this survey.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

We refer the interested reader to, for a survey on numerical methods starting from a continuous-time formulation and to [2, Chap. 8] for a textbook overview of direct methods.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Assuming that all problem functions in are sufficiently smooth, OCP, which is typically referred to as multiple shooting formulation, can directly be addressed with standard numerical methods for constrained nonlinear optimization. While multiple shooting formulation keeps both states and actions as optimization variables, one may alternatively eliminate the states from via the equality constraints yielding the single shooting formulation as introduced at the beginning of this survey and given. The single-shooting formulation typically results in dense subproblems with few optimization variables and can thus be efficiently solved by general-purpose nonlinear solvers. In the following, we focus on the multiple shooting problem, given, and tailored numerical methods addressing the particular problem structure arising from this formulation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

First, we distinguish between numerical methods that use first-order derivative information versus approaches that use second-order derivative information. First-order methods are less computationally complex but may require many more iterations. Second-order methods require less but computationally more complex iterations. Due to their low complexity, first-order methods have been considered for solving OCPs in particular in the context of embedded applications. Furthermore, a tailored method for the scenario-based OCP formulations based on alternating direction method of multipliers (ADMM) has been developed.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Second-order methods include nonlinear interior point (IP) methods and sequential quadratic programming (SQP), two widely used classes of methods for numerical optimization. We will briefly discuss both of them in the following. For a more detailed overview of second-order numerical methods for optimal control, we refer to.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Nonlinear interior point methods tackle the non-smooth Karush-Kuhn-Tucker (KKT) conditions associated with the constrained nonlinear optimization problem by formulating an approximate but smooth root-finding problem parametrized by a homotopy parameter, which is iteratively lowered towards zero - in the limit recovering the nonsmooth optimality conditions. The intermediate root-finding problems are solved via Newtontype iterations. Nonlinear interior point methods tailored to the OCP structure are discussed.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Within the SQP framework, a sequence of quadratic approximations of the nonlinear OCP is solved. The quadratic subproblems arising in SQP might, in turn, be solved using an interior point method or an active-set solver. SQP methods can typically be warm-started, rendering them particularly attractive for MPC applications where the solutions to subsequent problem instances are expected to be similar. For further implementation details tailored to SQP methods for MPC, such as full and partial condensing, we refer to the survey. SQP-type solvers tailored to OCP are implemented,. A widely used approximate approach closely tied to SQP is the real time iteration (RTI). Within the RTI framework, a single iteration of an SQP method is performed, i.e., a single QP approximation to the nonlinear OCP is solved, in order to obtain an approximate solution drastically reducing the computation time per iteration.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Both IP and SQP methods require the computation of (an approximation of) the Hessian of the Lagrangian associated with the OCP. While the exact Hessian yields locally quadratic convergence to the solution, its computation is typically costly. This motivates the use of Hessian approximations, which are cheaper to compute. A common choice for OCP is the Gauss-Newton Hessian which is applicable to nonlinear least squares objectives, and typically very cheap to compute (or even for free, in the case of quadratic objectives). As an additional advantage, the resulting subproblems are convex by construction, unlike the exact Hessian, which may yield nonconvex subproblems. However, due to the neglected curvature, in general only a linear convergence rate is achieved. The core principle of Gauss-Newton can also be extended to problem classes beyond nonlinear least squares, cf. for an overview. Quasi-Newton methods define alternative choices of Hessian approximation. Most prominently, these include the BFGS Hessian, which, with each iteration, converges towards the exact Hessian, yielding a superlinear convergence rate.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Independently of the particular choice of Hessian approximation, the subproblems encountered in both IP and SQP methods applied to the multiple shooting formulation exhibit a particular sparsity pattern, which is typically exploited by tailored solvers.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Another second-order method, which can not directly be interpreted within the Newton-type framework, is differential dynamic programming (DDP), originally proposed. DDP is also based on solving QP subproblems via a Riccati recursion, followed by a nonlinear forward sweep of the system, which employs the linear feedback law returned by the Riccati recursion. The DDP variant using a Gauss-Newton Hessian approximation, which is more commonly referred to as iterative linear quadratic regulator (iLQR), especially within the robotics community, has been introduced,. In their standard form, DDP and iLQR cannot directly handle additional constraints, but extensions to OCPs with input bounds have been proposed e.g.,. Sequential linear quadratic programming (SLQ) is often mentioned in the context of DDP, although it can more precisely be classified as an SQP method with a Gauss-Newton Hessian approximation applied to the single shooting OCP for which each of the QP subproblems is solved in a sparsity exploiting manner, i.e., by a Riccati recursion, cf. also.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Crucially, all discussed methods will generally converge to a local optimum and thus require a sufficiently good initialization. The local rate of convergence is determined by the accuracy of the Jacobian and Hessian approximation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

Only in the particular case of a convex NLP, such as for LMPCs, convergence to a global optimum can be guaranteed. Under these assumptions, the solution map can be shown to be continuous and piecewise affine. This fact is leveraged in explicit MPC where the optimal feedback law is precomputed offline in order to minimize online computation. Explicit MPC is usually limited to small state dimensions, few inequality constraints, or short horizons. Explicit NMPC was investigated e.g. in In addition to algorithms and software focusing on nominal OCP formulations, numerical methods tailored to treestructured problems arising in open-loop as well as closed- loop stochastic formulations have been developed. Numerical methods addressing the tubebased open-loop and closed-loop stochastic OCP formulation are presented in and respectively.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Numerical Methods for MPC Problems", "weight": 1.0} -->

In contrast to the exponential scaling of sampling-based approaches, e.g., shown for linear unstable systems, solving the nonlinear OCP via numerical optimization alleviates the curse of dimensionality, as the computational complexity of the nominal problem typically scales linearly with the horizon and polynomially with the state and control dimension. On the other hand, the sub-problems need to be optimizationfriendly and require the availability of derivative information. In comparison, sampling-based methods only require (fast) forward simulation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Starting from the general problem of solving MDPs, we have shown how RL and MPC are different techniques that aim at deriving optimal policies, cf., Sect. III and Sect. IV, respectively. MPC, for instance, emerged from the problem of solving multivariable constrained control problems, initially with the goal of setpoint stabilization. In contrast, RL methods aim at maximizing closed-loop performance without necessarily relying on a model of the real environment. Their discrepancy is unsurprising since both approaches were developed in parallel communities with different focuses. This is further substantiated in the nearly orthogonal properties of MPC and RL, which were reviewed and emphasized in a case study for a specific linear system. The more recent adaptions towards economic MPC, e.g. fit the paradigm of solving MDPs and, hence, bring the goals of both communities closer together.

<!-- chunk {"id": "body-0083", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Considering the practicalities of MPC and RL of solving MDPs, further particularities appear, which we compare in the following. The comparison is concluded in Tab. II that shows an overview of relevant properties, similar to and Tab. III, from work that explicitly compares MPC and RL in practical applications. We compare requirements on the state space representation and the properties of the mathematical model, such as smoothness or continuity required by MPC. We refer to, for further theoretical comparisons.

<!-- chunk {"id": "body-0084", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

In the following, the main practical and conceptual differences between MPC and RL are stated. 1) State Space: Real environments can only be approximately described by a state, which is usually not always directly measurable, leading to the concept of partially observable MDPs (POMDPs). So far, we omitted a discussion about POMDPs and only mentioned some points required for a high-level discussion on the state space. Considering an environment where the state s is unknown and only observations O k ∈ R n o are made at step k, the most general concept of a state space would involve the collection of all observations O 0, O 1,... and applied actions A 0, A 1,.... Even this very general concept may not allow to fully describe the real environment due to partial observability.

<!-- chunk {"id": "body-0085", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

However, often these observations, or even the M most recent observations O M = ( O k -M, A k -M,..., A k -1, O k ) at step k are sufficient to estimate the relevant states of an environment.

<!-- chunk {"id": "body-0086", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

In MPC and RL algorithms, the state space is interpreted conceptually differently. In derivative-based MPC, the state space is usually constructed by relating it to an optimization-friendly model, usually having a physical interpretation following differential equations. Yet, alternative approaches also consider a sequence of measurements as state, cf. Sect. IV-B. States used within derivative-based MPC do not necessarily correspond to the measured sensor outputs and, thus, are often estimated by a state observer that converts a series of observations O M into a state estimate.

<!-- chunk {"id": "body-0087", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

RL methods and sampling-based MPC methods may use states based on a corresponding physics-based model and the related estimators or a state observer. However, the state may also be kept as a recent history of raw sensor data, which could be based on a variety of different input modalities, such as images or text. Often, end-to-end learning is used, where the raw sensor input, such as images, is fed directly to NNs. The NN outputs subsequently the controls, e.g.,. It is common to make the learned dynamics model or policy dependent on a window of the most recent history of observations and actions O M, cf. which is particularly useful for POMDPs. While an NN architecture does not explicitly model states, the stacking of layers, the related transformations, the exploitation of equi/invariances, and the condensing of information can be interpreted as modeling of hidden states, cf.. Subsequent layers can be interpreted as the policy based on these hidden states. Remarkably, this structure is not enforced explicitly. Also, recent approaches of the more classical observer/controller architecture propose to tune MPC and the state estimator together.

<!-- chunk {"id": "body-0088", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

2) Model and Application: Highly related to the state space are the characteristics of a potentially used model. As explained in Sect. IV, MPC requires a model to simulate the dynamics. Whereas sampling-based MPC only requires the forward simulation of a model, derivative-based MPC involves the computation of gradients through the model. Therefore, derivative-based MPC requires an optimization-friendly model with stark limitations to its structure since the model is part of the optimization problem. The MPC optimization problem becomes particularly challenging if the model is nonsmooth, stochastic, or contains integer variables.

<!-- chunk {"id": "body-0089", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

A physically motivated prediction model, which is often used in MPC, has the advantage of better understanding and explaining the environment behavior, often referred to as explainability. The possibility of predicting interpretable model states allows for the straightforward definition of constraints. For example, a certain velocity must not be exceeded in a vehicle control problem. This constraint can be readily formulated by a model that predicts the system's velocity accurately. Besides physically motivated models, more general models such as NNs or nonparametric models such as Gaussian processes can be used. These models still have the advantage of predicting the environment. However, the explainability of the states can be lost.

<!-- chunk {"id": "body-0090", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Not requiring the explicit modeling of the environment is a major claim of RL. However, that statement needs some additional framing. In fact, many successful model-free RL applications use models, at least for training the policy. One fundamental difference between models used for RL or MPC is that RL models are often used for offline simulation but not during deployment of the final policy. This allows an abundance of complex computations involved in the simulation, which could comprise logical statements or complex highfidelity models. Even though most RL methods still require simulation models, real-world RL is an active research field making significant progress.

<!-- chunk {"id": "body-0091", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

The low inference time of NNs makes it appealing to increase the sampling frequency of RL algorithms for faster feedback loops. However, a too-small discretization time step in RL can result in the function approximation error exceeding the value difference of actions, rendering deep RL methods that rely on function approximation useless. Standard offline system identification techniques used to identify the MPC model also involve problems with too high sampling frequencies, e.g., a decreased signal-to-noise ratio and an ill-conditioned model. However, in derivative-based MPC, the choice of the sampling frequency is often limited by the solution time of the underlying optimization problem. 3) Intrinsic stochasticity: As introduced, the environment is typically assumed to be intrinsically stochastic. Thus, even if the environment is perfectly known, it is not possible to precisely predict future state trajectories. Both robust and stochastic MPC explicitly take into account this uncertainty, which is in this context typically referred to as noise or disturbance. Robust MPC is, in a sense, agnostic to the question of whether the uncertainty is intrinsic or due to a systematic modeling error: it considers all trajectories possible under the given assumptions.

<!-- chunk {"id": "body-0092", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

For stochastic MPC, on the other hand, it is important to be aware of whether the prediction errors correlate over time since this affects the predicted state distribution. Intrinsically stochastic noise is often assumed to be independent, i.e., noncorrelating.

<!-- chunk {"id": "body-0093", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

As stochasticity is inherently part of the MDP framework, RL algorithms naturally consider stochastic environments. The policies can be trained directly on the real-world environment to account for the real-world uncertainty, cf., Sect. III. A form of stochasticity particularly challenging for RL algorithms are rare events, i.e., large but rare deviations from the average obtained cost. Learning value estimates with rare events is particularly difficult. 4) Model mismatch: In practice, the environment for which a policy is designed or trained will often differ from the one it is deployed. Thus, it needs to be ensured that the policy will still perform well during deployment. Standard RL algorithms can be biased towards the specific model used during training. Different strategies like domain randomization, robust RL and meta RL tackle model uncertainty. In all of these approaches, the agent is trained not only on a single model but also on a potentially adaptive distribution of models, which can improve the generalization to new models. The underlying assumption is that the real-world environment lies in the distribution of the training models. Optimization-based meta RL learns weights that can quickly adapt to new models.

<!-- chunk {"id": "body-0094", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

In contrast, in-context meta RL uses history-dependent policies to infer the current dynamics of the environment.

<!-- chunk {"id": "body-0095", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Like in the case of intrinsic stochasticity, both stochastic and robust MPC can explicitly take model mismatch into account. For stochastic MPC, it is important to consider that predictive errors due to model uncertainty are typically strongly correlated across time. Note that the model used in a stochastic MPC formulation is typically a simplification or approximation of the environment, leading to a mismatch of the stochastic MPC model with respect to the environment. The field of distributionally robust MPC aims to robustify against mismatches in the distribution model. Even without considering the model mismatch explicitly, MPC can perform remarkably well. This is the property of inherent robustness of MPC, as explained in more detail in Sect. IV. 5) Stability: Stability theory is usually not a major concern of RL algorithms since the main objective is closed-loop performance and practical stability instead. However, as denoted in Sect. IV, asymptotic stability and constraint satisfaction are, or were at least historically, the main focus of MPC algorithms and applications. A widely used tool for analyzing the stability of control problems involves the construction of Lyapunov functions.

<!-- chunk {"id": "body-0096", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

If a Lyapunov function exists for a controlled deterministic MDP, it is said to be asymptotically stable, i.e., trajectories converge. If the MDP is stochastic, the concept of input-to-state-stability can be applied, which requires the trajectories of the controlled system to converge to a region around the origin whose magnitude depends on the maximum norm of the noise.

<!-- chunk {"id": "body-0097", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Input-to-state stability and asymptotic stability may not be applied to general MDPs since they require certain properties of the cost function, such as a feasible origin. Therefore, the authors in propose a stability concept named D-stability that applies to MDPs and generalizes the dissipativity theory of economic MPC. 6) Constraints: The ability to account for constraint satisfaction and stability are some of the main reasons MPC is outstanding compared to other control techniques. In recent years, the RL community also has increasingly focused on providing safety guarantees. A widely adopted framework in RL involves modeling constraints using constrained MDPs. Following, these include: Hard constraints, the constraints are always fullfilled, chance constraints, the constraints are fullfilled with high probability, and constraint violations transformed as accumulated costs. The latter can be either formulated such that the accumulated costs can not exceed a safety budget or as a penalty integrated into the task objective. The choice of formulation dictates the strategies employed to address these constraints. Common approaches include deriving safe action sets, optimizing a Lagrange formulation with dual gradient descent, using trust-region optimization or control-barrier functions.

<!-- chunk {"id": "body-0098", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Additionally, using MPC to provide safety guarantees related to a nominal model was proposed. Further work suggests augmenting the RL state with Lagrange multipliers or with the currently used safety budget. Still, a common problem is that safe RL policies become either too conservative or, otherwise, may violate constraints. Thus, combining MPC and RL is highly desirable for constraint satisfaction. 7) Online Computation Time: A major concern in embedded applications is the maximum online computation time of an algorithm on embedded hardware. The maximum inference time of many NN architectures, which are often explicit functions, can usually be tightly bounded. However, the computation time of optimization solvers for NMPC problems is often unbounded. In fact, it cannot be guaranteed in general that a meaningful solution, i.e., at least a feasible solution, is returned by the optimization algorithm outside of particular optimization problem classes such as convex QPs,. For NMPC, the primal and, possibly, dual variable initialization of the optimization algorithm is essential for fast online computations. If the variables are sufficiently close to the optimal solution, the local convergence rate is fast.

<!-- chunk {"id": "body-0099", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

In fact, it can be quadratic or superlinear, depending on different numerical algorithms, cf. Sect. IV. 8) Offline Computation, Engineering, and Maintenance: In contrast to their fast inference time, RL algorithms usually require a tremendous amount of training samples, and therefore, training time, even for small-sized MDPs. The training may be performed without human intervention. Yet in practice, fine-tuning on the RL hyperparameters may be required. Besides the initial system identification, standard MPC does not require further training time. System identification differs from RL training by the target of predicting relevant outputs and possibly states of a system. In contrast, the RL target and the potential internal model focus on closed-loop performance. In the RL approach, the possible indirect internal model of the environment is learned only for the particular task described by the MDP. The classical system identification may also use models based on physical models, which makes it possible to adapt the controller to changing environments or requirements. RL may require a whole new training data set for changes in the cost, model changes, or changes in the distribution of the states-space, e.g., an adjusted operating range in the environment.

<!-- chunk {"id": "body-0100", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

9) Generalization: To some extent, RL policies can generalize out of their training distribution but with hardly any predictable behavior and guarantees on the closedloop performance. Thus, practitioners often need to ensure that the support of the training distribution covers the state and transition distribution encountered during deployment. An alternative is to further train the RL policy during deployment. If the model used within MPC can approximate the real environment well on the whole state space, MPC generalizes well, and safety and performance guarantees can be found. Arguably, the model may generalize well based on available knowledge, starting from first principles and physical or mathematical insight. The knowledge about the model results in a more interpretable generalization and is among the main motivations for MPC in general, learning-based MPC or model-based RL. It may not be possible to evaluate whether a physical model approximates the real environment well on the full state space of the environment. However, the physical explanation may also provide insights into its limitations. 10) Performance in Practice: In practice, the expected performance difference between MPC and RL depends on the environment's specific characteristics, computational resource availability, and the model or data quality.

<!-- chunk {"id": "body-0101", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

Both approaches have their strengths and weaknesses, depending on the particular requirements and constraints of the control problem. Several works compare both approaches on specific applications; see Tab. III. The problems differ vastly, from drone racing to multi-energy environments that involve integer variables. The MPC formulations vary depending on the applications. For high sampling times, fast solvers such as acados are used. Instead, for combinatorial problems, computationally highly demanding mixed integer solvers, such as Gurobi, are required. Most of the authors use the same state space for MPC and RL, despite the RL's ability to cope with arbitrary information inputs, which is exploited only,. For a known model, most authors report superiority of MPC w.r.t. the closed-loop performance, with less than 4% cost reduction, and 16% in when compared to RL. In, the authors report that MPC outperforms RL on a flexible robot manipulation task with a rather high-dimensional state space. RL was claimed to be superior to MPC for environments with poor models, e.g., in yet robust control techniques are not implemented.

<!-- chunk {"id": "body-0102", "role": "body", "section": "COMPARISON OF MPC AND RL", "weight": 1.0} -->

The authors in claimed superiority of a particular choice of RL algorithms against MPC in real-world experiments (RWE) of racing drones.

<!-- chunk {"id": "body-0103", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

As pointed out in the previous sections, RL is a collection of algorithms to learn an optimal policy for MDPs by interacting with the environments. MPC, in contrast, refers to a mathematical program that implicitly approximates the MDP. The two approaches exhibit different advantages. Therefore, a combination of both is appealing.

<!-- chunk {"id": "body-0104", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

Fig. 2: Modular view on combinations of MPC and RL. The combinations are aligned with the sections of this survey. The horizontal separation corresponds to using MPC as part of the expert actor, the deployed policy, and the RL critic. This overview highlights the possibility of using several instances of MPC with different roles in various parts of an RL algorithm and a deployed policy. MPC is used with fixed expert parameters within the expert actor, as a reference generator, as a postprocessing filter, or, possibly, in the critic. Learned MPC, i.e., an MPC structure involving learned parameters, can be used within the learned actor or possibly within the learned critic.

<!-- chunk {"id": "body-0105", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

We propose a categorization of combination approaches that distinguishes in which algorithmic part of RL the MPC framework is used. The related general RL building blocks are the actor, the critic, and possibly an expert actor, c.f., Fig. 2. Accordingly, we propose the categories

<!-- chunk {"id": "body-0106", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

- 1) MPC as an expert actor, cf. Sect. VII, - 2) MPC within the deployed policy, cf. Sect. VIII, - 3) MPC as part of the critic, cf. Sect. IX.

<!-- chunk {"id": "body-0107", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

In the following, we shortly outline the different categories.

<!-- chunk {"id": "body-0108", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

MPC as an expert actor. An MPC with fixed parameters and the desired behavior can be used as an expert to learn policies. The expert behavior can either be used by an IL algorithm that tries to purely mimic the behavior or to guide the exploration process during RL training. MPC used as an expert is elaborated in Sect. VII.

<!-- chunk {"id": "body-0109", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

MPC within the deployed policy. Another common variant of how MPC and RL are combined is using MPC within the deployed policy. A parameterized MPC can be used as part of the learned actor, as, for instance, proposed. Closely related are concepts that use MPC as a posterior filter or reference provider as an element of the deployed policy but are not used during learning. For instance, the authors in use MPC as a safety filter and use MPC as a reference provider, cf. Fig. 2. All concepts that use MPC within the deployed control policy are elaborated in Sect. VIII.

<!-- chunk {"id": "body-0110", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

| Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | Application-oriented comparison between MPC and RL | MPC as part of the critic. An MPC, possibly parameterized with learnable parameters, can further be used to evaluate the value function at a given state, i.e., the critic uses an MPC variant. For instance, the in uses an MPC with fixed parameters to compute the value at a given state. This structure is reviewed in Sect. IX.

<!-- chunk {"id": "body-0111", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

Sections VII to IX describe combination approaches of MPC and RL conceptually, leaving out a detailed theoretical discussion. Nonetheless, the additional theory Sect. X highlights some important findings and relevant literature when combining the two approaches.

<!-- chunk {"id": "body-0112", "role": "body", "section": "COMBINATION APPROACHES", "weight": 1.0} -->

To the best of the authors' knowledge, in the following review, the most important works that combine MPC and RL can be classified according to the proposed categories in Fig. 2. The works are further compared related to their application, whether RWEs on embedded hardware was performed, which MPC type and solver the authors used, and which RL algorithm the authors applied. While the MPC algorithm classification is more distinct, the classification of the RL algorithm can be ambiguous and intertwined with the overall presented algorithm. Besides widespread RL algorithms such as SAC and PPO, several forms of DP, such as policy iteration (PI) or VI, forms of IL such as behavior cloning (BC), and even supervised learning for learning value functions, such as maximum likelihood estimation (MLE), are denoted as RL algorithm in the tables. Applications include unmanned ground vehicle (UGV), temperature control, energy systems, chemical processes, traffic management, autonomous racing with vehicles or drones, and automated driving (AD).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

Before diving into the particular approaches of how MPC is used as part of RL or IL algorithms, a short classification of parameterized MPC architectures that use NNs is given. This distinction is particularly important for designing combination approaches as it centrally governs the desired properties and choices of algorithms.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

We consider an MPC optimization layer that can be parameterized by a parameter ϕ ∈ R n ϕ and may depend on the decision variables z of the MPC optimization problem and the current state s through a highly nonlinear function approximator (FA) ϕ = φ θ ( s, z ), e.g., an artificial neural network (NN) with the (very) high dimensional parameter vector θ ∈ R n θ. Since NNs are the most common FAs, we consecutively mainly write NN but also comprise other forms for FAs. When fixing the parameters ϕ, the MPC optimization problem is assumed to contain only optimization-friendly objective, model, and constraint functions.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

Fig. 3: Parameterized MPC architectures: Proposed architectures of actors (or potentially critics) used in RL utilizing MPCs and NNs/simple parameters. In the integratedarchitecture, the NN is part of the optimization layer and depends on the decision variables. Suppose an NN can be evaluated separately from the optimization routine but provides the parameters to an MPC optimization layer. In that case, the architecture is referred to as hierarchical. If the MPC problem is solved in parallel to the NN, we refer to a parallel architecture. If the learned parameters do not depend on the current state s, the architecture is referred to as parameterized A general form of the parameterized MPC, based, can be written as and the parameterized objective is For easing the notation, all constraints of are summarized by g ϕ (z; s) ≥ 0. Thus, the optimization problem can be concisely written as Note that we use the notation g ϕ (z; s) to indicate that z are decision variables of the optimization problem and s are parameters. The following architectures are proposed within this context, starting with the most general one, i.e., the integrated architecture, cf. Fig 3.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

1) Integrated Architecture: In the integrated setting, the parameters depend on both the state s and the optimization variables z via the function φ θ (s, z), as, for instance, within the algorithm proposed. Therefore, the NN is part of the optimization problem and can not be evaluated separately in the inference path, leading to a highly nonlinear and, possibly, nonconvex optimization problem, which may be computationally challenging. Particularly, when using derivative-based solvers, this involves differentiating the highly nonlinear parameterized function φ θ (z; s) w.r.t. the decision variables z by ∇ z φ θ (z; s) as part of solving the MPC optimization problem. Note that the optimization layer may provide any of the optimal decision variables z ⋆ or the MPC objective function V MPC θ of the MPC optimization problem. 2) Hierarchical Architecture: In the hierarchical architecture, the neural network provides an input to the MPC. Therefore, the parameter ϕ depends on the current states s via the highly nonlinear function ϕ = φ θ (s).

<!-- chunk {"id": "body-0117", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

For example, a reference trajectory parameterized by ϕ could be provided in case this architecture is used as a policy, such as in or ϕ could parameterize constraints in the OCP, similar to. Notably, the function φ θ (s) can be evaluated before solving the optimization problem. In this case, the potential nonlinearity of φ θ (s) does not influence the numerical optimization problem structure, i.e., the optimization problem does not get harder to solve, despite the changing parameters. 3) Parallel Architecture: In the parallel architecture, the MPC problem is usually not parameterized. However, an NN is evaluated in parallel to the MPC optimization problem, and its output is used to correct the optimal solution for decision variables or the value function of the MPC. This architecture holds the advantage of not requiring differentiating the optimization problem and the disadvantage of potentially unsafe actions due to the perturbation of the MPC actions. An example of this architecture used to approximate the value function can be found. 4) Parameterized Architecture: In the parameterized MPC architecture, the parameters ϕ are constant and independent of decision variables z or the state s.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

Conceptually, a parameterized optimization-friendly MPC problem is formulated that does not require the evaluation of highly nonlinear functions to obtain the paramter ϕ. For instance, such a parameterization is proposed, and.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Architectures of Parameterized MPC", "weight": 1.0} -->

Above, we introduced a number of architectures for parameterizing MPC with potentially highly nonlinear functions such as NNs. These architectures may be used in the following MPC and RL combinations, whereby some parameterized MPC architectures are more or less favored in particular MPC and RL combinations.

<!-- chunk {"id": "body-0120", "role": "body", "section": "MPC AS AN EXPERT ACTOR", "weight": 1.0} -->

For some problems, it is possible to design an expert MPC that achieves good closed-loop performance. A thorough collection of relevant literature can be found in Tab. IV and a sketch in Fig. 4. There are multiple ways to exploit such an expert motivating the structure of the following section: Fig. 4: Combinations: MPC as an expert actor. The plot is split into the learning and deployment phases. Blue boxes indicate Neural Networks (NNs), and green boxes are used for MPCs.

<!-- chunk {"id": "body-0121", "role": "body", "section": "MPC AS AN EXPERT ACTOR", "weight": 1.0} -->

- A. Imitation learning from MPC, Sect. VII-A. Here, the goal is to replace the expert MPC with a NN to achieve faster computation time using imitation learning. - B. Guided Policy Search using MPC, Sect. VII-B. In this paradigm, the expert MPC policy improves the exploration process during the RL training guiding the learned policy to low-cost regions.

<!-- chunk {"id": "body-0122", "role": "body", "section": "MPC AS AN EXPERT ACTOR", "weight": 1.0} -->

Besides the explored application, the table specifies whether the algorithm is related to imitation learning (IL) or guided policy search (GPS) and which particular MPC, RL, and IL algorithms are used as a basis.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Imitation Learning from MPC", "weight": 1.0} -->

In a problem setting where MPC achieves a sufficient closedloop performance burdened only by its online computation time, a trained NN may replace the MPC. The typically fast inference of the NN may drastically decrease the online computation time by omitting the time-consuming online optimization. In fact, in many real-world applications the computation time of the MPC solver is a significant limitation and potentially even unbounded, particularly for more complex structures, e.g., involving nonlinear systems, stochasticity or discrete decisions, c.f. Sect. IV-B. Two research directions try to alleviate the problem of large online computation times.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Imitation Learning from MPC", "weight": 1.0} -->

First, for linear systems, linear constraints, and convex quadratic costs, the optimal feedback control law is piecewise linear within a polytope of the state space. Within explicit MPC these polytopes and their control laws are computed offline and switched during deployment by determining the active region. For large state spaces or a large number of constraints, explicit MPC becomes quickly intractable. Thus, approximate explicit MPC only approximately stores the control law of the MPC policy.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Imitation Learning from MPC", "weight": 1.0} -->

A learning-based approach to approximate explicit MPC is using IL to learn the MPC expert. Methods can learn the whole trajectory predictions or learn the first applied action. Early works, and several follow-up works are aiming to imitate a complex MPC with a neural network, by training the NN with supervised learning methods. Further aspects of the learned NN policy where analyzed regarding safety stability and robustness. Another important aspect is the verification of the learned NN, where the object of interest is the worst-case approximation error to the MPC expert. This can be done in a probabilistic fashion using Hoeffdings inequality, such as in where confidence bounds are derived for an estimate of how often an approximation error threshold might be exceeded. Alternatively, verification techniques like in solve an MIQP to bound the worst-case approximation error. For a general overview of NN verification, see.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Imitation Learning from MPC", "weight": 1.0} -->

Often, a surrogate loss function as in standard BC minimizes the squared distances between the predicted action of the NN and the action of the MPC expert. However, it disregards the costs and structure of the underlying OCP while learning the policy. Thus, a natural replacement is to use instead the Qfunction of the MPC, cf. as a learning objective. Since the MPC provides a Q-value function in addition to the expert policy, cf. Fig. 2, we categorize such methods in a class named MPC as a critic, as further discussed in Sect. IX.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Guided Policy Search using MPC", "weight": 1.0} -->

In the previously mentioned IL methods, the MPC expert does not consider the progress of the learned policy during training. In the guided policy search (GPS) regime, the expert gradually guides the learned policy to better trajectories. This is ensured by coupling the trajectory optimization and policy learning by requiring that the MPC expert does not deviate too far from the current predictions of the learned policy. The final learned policies can generalize even when the MPC expert fails to find a solution. Further, the authors in have shown superior performance over policies learned from a fixed dataset of expert trajectories.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Guided Policy Search using MPC", "weight": 1.0} -->

Another possibility to guide the exploration process for RL was proposed in and is related to the options framework. A learned high-level exploration policy decides between using an MPC expert policy or the currently learned low-level RL policy. The usage of the MPC expert is regularized over time to enforce that the learned low-level RL policy works as a stand-alone policy during deployment. A benefit over GPS is that the high-level policy can avoid using the MPC expert for state regions, where the MPC expert guidance is suboptimal.

<!-- chunk {"id": "body-0129", "role": "body", "section": "MPC WITHIN THE DEPLOYED POLICY", "weight": 1.0} -->

This section discusses methods that use MPC during deployment in the real environment. A primary distinction is drawn on whether parameterized MPC is trained by RL algorithms or if MPC is used for pre/postprocessing after the RL training. When learning a parameterized MPC, we furthermore distinguish between approaches that aim to align the MPC formulation with the MDP structure, e.g., to learn an internal MPC model that aims to approximate the real environment as closely as possible or methods that primarily focus on closed-loop optimality. Accordingly, we structure this section as follows

<!-- chunk {"id": "body-0130", "role": "body", "section": "MPC WITHIN THE DEPLOYED POLICY", "weight": 1.0} -->

- A. Aligned-learning, Sect. VIII-A. In the paradigm of aligned learning, the MPC structure approximates the real-world MDP structure, i.e., it uses a transition model, costs, constraints and a terminal value function that individually approximate the MDP and the optimal value function V ⋆, respectively.

<!-- chunk {"id": "body-0131", "role": "body", "section": "MPC WITHIN THE DEPLOYED POLICY", "weight": 1.0} -->

- B. Closed-loop learning, Sect. VIII-B. In the paradigm of closed-loop learning, an MPC is used as an optimization layer within the actor policy and trained within an RL algorithm for closed-loop optimality, which, in general, does not require the individual parts of the MPC to be aligned with the MDP. For instance, the MPC model should not necessarily fit the real system expected or most likely transition to provide closed-loop optimality. - C. MPC for pre/postprocessing, Sect. VIII-C. Using MPC for pre/postprocessing does not involve MPC during learning but as part of the deployed policy. This section is further split into reference generation and filtering.

<!-- chunk {"id": "body-0132", "role": "body", "section": "MPC WITHIN THE DEPLOYED POLICY", "weight": 1.0} -->

Different structures that include MPC in the deployed policy are proposed; see Fig. 2 and Fig. 5.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

The classical design procedure of MPC focuses in its first step on finding an usually deterministic mathematical model f MPC θ ( x, u ) assumed to be parameterized by θ that describes the environment sufficiently well. Secondly, a horizon length N and a terminal value function ¯ V MPC θ ( s ) as in with parameters θ are obtained to approximate the optimization problem over a finite horizon.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

The advantage of aligning the MPC with the MDP can be seen in the well-interpretable formulation, adaptability to new problems, generalization, potential guarantees for stability and recursive feasibility, and the division of the overall design into subtasks. However, the online computation time may high if complex MPC formulations are used, e.g., stochastic MPC formulations that account for uncertainty.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

Obtaining the terminal value function to approximate the infinite horizon value function as in is computationally challenging and, therefore, usually approximated and often obtained through learning algorithms closely related to the RL framework. For simple MDPs, e.g., deterministic MDPs with linear models and a quadratic cost, the terminal value function can be computed exactly and does not require learning or approximation. The costs l MPC ( x, u ) are usually given by the application, i.e., the MDP, but may be altered to improve the numerical properties related to the optimization problem regarding smoothness and convexity. We denote parameters of both the model f MPC θ ( x, u ) and the terminal value function ¯ V MPC θ ( s ) by θ.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

Literature that can be categorized as MDP aligned typically uses the integrated or parameterized architecture according to Fig. 3. For instance, the paramters θ could parameterize a NN that is used as the internal MPC model or the terminal value function, corresponding to the integrated architecture. Tab. V summarizes literature that can be related to the MDP aligned learning paradigm. In the comparison of Tab. V, a distinction is made, whether the model or the terminal value function was learned. Additionally, the table indicates if the corresponding object was learned during the deployment of the continually improving MPC policy, referred to as on-policy learning (ON-P), or learned by using a separate off-policy sampling strategy (OFF-P). An example of an offpolicy sampling strategy would involve system identification Fig. 5: Combinations: MPC within the deployed policy. The plot is split into the learning and deployment phase. Blue boxes indicate Neural Networks (NNs), green boxes are used for MPCs, and blue/green boxes refer to parameterized MPCs that involve parameters/NNs that are learned during the learning phase, see Sect. VI-A. to identify a model before deploying the MPC.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

In the following, the two objectives of learning the model or the terminal value function are explained in further detail. 1) Learning the Model: The first target of aligned learning is to approximate the stochastic model of the real environment P with a model f MPC θ that is used within MPC. The model is usually a parameterized mathematical model designed via first principles or a more generic model using a function approximator like a NN or Gaussian process (GP). Parameters θ of candidate models are fit to observed transition data D id = { (S 0, A 0, S 1),..., (S M -1, A M -1, S M) } of state transitions and related actions. The evaluation of the model fit requires a validation or loss function L id (·), which could be, for instance, the least-square loss function. The parameters can be found by minimizing 2) Learning the Terminal Value Function: In order to approximate the MDP on a finite MPC horizon as, a terminal value function ¯ V MPC θ (s) with parameters θ needs to be established.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

From a system theoretical perspective, the terminal value function is important in terms of stability or recursive feasibility, c.f., Sect. IV. However, when focusing on closed-loop cost, the terminal value function needs to tractably approximate the true value function V ⋆ of the MDP. In the end, different aspects can be considered when learning an appropriate terminal value function.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Aligned Learning", "weight": 1.0} -->

For instance, the terminal value function ¯ V MPC θ can be learned via a temporal difference update, cf., where a learned terminal value function is incorporated into an MPPI planner. In the following, a simplified version is provided to learn a parameterized terminal value function ¯ V MPC θ, potentially a NN, that can be defined via

<!-- chunk {"id": "body-0140", "role": "body", "section": "Terminal value function learning ( ¯ V MPC θ ≈ ? 1 )", "weight": 1.0} -->

where D π MPC θ is a distribution of states generated by controlling the system via the parametrized MPC exploration policy π MPC θ and α is the learning rate. Another approach to learning the terminal value function is shown, where the authors use either model-free SAC or PPO to obtain a terminal value function for an MPC planner.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

In the following section, the paradigm of viewing MPC as a parameterized optimization layer as part of an actor policy is explained in more detail. In the closed-loop learning paradigm, the MPC model is not required to minimize a prediction loss L id or to provide a terminal value function that approximates the optimal value function as in the MDP aligned setting. Instead, the model, costs, or constraints may be changed to solely improve the closed-loop performance of the MPC policy µ MPC according to Definition 4. Fig. 5 shows a sketch of the closed-loop optimal learning paradigm.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

An advantage of this paradigm is the ability to achieve optimal closed-loop performance in the real environment without the necessity of computationally demanding aligned formulation of Sect. VIII-A. However, by modifying the various parts of the MPC purely to increase the closedloop performance, explainability, safety, generalization, and adaptability get lost, particularly if the model or constraints are allowed to change.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Practically, this paradigm differs depending on whether the controls provided by the MPC or the parameterization of the MPC obtained through a learnable NN are assumed as RL actions. This two practical implementations are explained in the following. 1) Differentiable MPC: MPC can be used as an optimization layer within the RL policy to provide a good initial performance by leveraging knowledge about the task. Ideally, the MPC 1 The question mark indicates that, to the best of the authors' knowledge, the update scheme does not converge to the optimal value function V ⋆ in general, and its convergence target remains unclear.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

| MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | MPC as an Actor: MDP Aligned Supervised Learning | performance would only be slightly suboptimal and provide safety guarantees for a known model. The hope would be that by only a few RL iterations, the parameters can be modified towards nearly optimal closed-loop performance, particularly related to stochasticity.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

However, the MPC optimization problem as part of the learned actor creates potential challenges for both the forward path, where the policy evaluation includes solving the optimization problem, and the training of parameters, which, in some algorithms, requires appropriately passing gradients through an optimization algorithm. Solving optimization problems is numerically challenging. Thus, the related iterative algorithms may slow down learning when evaluating a policy. Moreover, obtaining a global optimizer outside the class of convex optimization problems is intractable in general. Although local optima are often sufficient but require warm-starting, the initial states used to warm-start an optimization solver introduce additional states, which are required to be considered in the learning algorithm.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

When using the MPC in an RL actor, gradients need to be computed through the optimization solver as part of the backpropagation. These gradients can be computed using the implicit function theorem, cf. App. A and related literature for further details. However, existing optimization software is required to support such features. Related features were recently developed in various tools, see Sect. XI.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

When differentiating through the optimization layer, the integrated, hierarchical, parallel, and parameterized architectures according to Fig. 3 may be used, but to the best of the authors' knowledge, only the hierarchical, e.g. and the parameterized architectures, e.g. were proposed so far.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

The following algorithm based on the ideas of provides a basic version of closed-loop optimal learning, where the parameters are updated by differentiating the MPC. The temporal difference update is adapted to the parameterized MPC setting to The state-action distribution D is generated by controlling the system via the stochastic parameterized MPC exploration policy π MPC θ. Note that the update scheme only considers a single sample, which is often reasonable in the case that the Q MPC θ is just a parameterized MPC scheme as described in Fig. 3, without a NN.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Another example of closed-loop optimal learning based on a DDPG actor-critic formulation similar to was introduced in and is given by The parameters are updated for the deterministic policy µ MPC θ and a NN critic Q w with parameters w. The stochastic policy π MPC θ is used for exploration in order to fill the replay buffer D buffer. 2) MPC as part of the environment: Passing gradients through the MPC in the actor in the closed-loop optimal learning paradigm can also be omitted, conceptually, considering the MPC as part of the environment. In such a setting, a parameterized MPC that controls an environment can be seen as an augmented new environment whose actions are the MPC parameters. Accordingly, the RL critic evaluates the values related to these parameters instead of the actions provided by the MPC, which are, in fact, hidden from the RL framework. Considering the parameterization of the MPC as the environment input, instead of the actions obtained from the MPC, avoids computing sensitivities but comes at the cost of potentially vastly increasing the dimensions of the action space and obtaining gradient information through sampling.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Such a setting usually involves the hierarchical, or the parameterized architecture of Fig. 3.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Whether MPC is considered as part of the environment in literature, involving its differentiation, is indicated by the differentiating MPC column in Tab. VI. 3) Exploration: Tab. VI lists closed-loop optimal algorithms that differ in the architecture and whether they include differentiation through the optimization layer. Moreover, Tab. VI considers how exploration was performed in related literature, cf. Sect. III-B. Exploration is often required to improve the currently learned policy in RL.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

- 1) Adding noise to the action proposed by the optimization layer. The downside of adding noise posterior to the optimizer is the potentially unsafe exploration, depending on the chosen exploration noise. - 2) Modifying the cost in the optimization layer (25a) with an additive term d ⊤ u 0 where d is a possibly randomly selected vector. Given that only the cost is modified, the actions remain feasible with respect to the model while the additive term introduces a gradient over the initial control input for exploration. - 3) Add a perturbation to the parameter ϕ for the hierarchical architecture and θ for the parameterized architecture as shown in Fig. 3, guaranteeing safe actions. - 4) Instead of noise on the parameters or controls, optimistic initialization is an RL technique where Q-values (or estimates) are initialized with higher-than-expected values, encouraging the agent to explore and gradually reduce these optimistic estimates to reflect the true values. For a discussion in the context of deep RL see.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Fig. 6: MPC can be used as a reference generator for an RL policy. The distribution of the input of the policy may depend on the distribution of optimizers obtained from MPC while interacting with the environment.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Closed-Loop Learning", "weight": 1.0} -->

Closed-loop optimal learning algorithms require the MPC to be part of the RL algorithm. Yet, the following two variants in Sect. VIII-C use a hierarchical MPC and RL setting, where MPC is added posterior to the training in the deployed controller.

<!-- chunk {"id": "body-0155", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

In the following Section, two concepts are highlighted that use MPC within the deployed policy, yet, not during the training procedure. Since the trained policy is not aware of the filter, the expected performance can not be expected to be closed-loop optimal, as in the previous section. Depending on the purpose of the MPC, a distinction is made between an MPC used as a reference generator for preprocessing, cf. Fig. 6 and Sect. VIII-C1, and MPC used for postprocessing, cf. Fig. 7 and Sect. VIII-C2. Relevant literature is compared in Tab. VII. 1) Preprocessing: MPC as a Reference Generator: MPC may be used as a reference generator for an RL policy such as. This combination approach of MPC and RL is particularly useful if the output of MPC is a planned trajectory rather than a single action. Since solving the MPC may be slow, the RL policy may be trained with a computationally cheaper reference generator, as proposed. Notably, this setting may often be used in publications without an explicit statement that describes the reference provider.

<!-- chunk {"id": "body-0156", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

2) MPC for Postprocessing: Adding MPC to a trained policy may fulfill one of the two purposes: (i) providing safety w.r.t. an assumed model and constraints, known as safety filter or (ii) providing a coarse solution by a warm-start of an optimization solver.

<!-- chunk {"id": "body-0157", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

RL policies may struggle with guaranteeing safety and plan for smooth trajectories, particularly in a high-dimensional state space.

<!-- chunk {"id": "body-0158", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

As opposed to the previous Sect. VIII-B of closed-loop optimal learning, the approaches that use MPC as a filter do not consider MPC during learning. Thus, the expected behavior may not be closed-loop optimal since the policy is unaware of MPC during training.

<!-- chunk {"id": "body-0159", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

| MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | MPC as an actor: closed-loop optimal | Fig. 7: MPC can be used to smooth or filter reference trajectories. For example, MPC may be used to provide safety guarantees that are hard to achieve by RL policies.

<!-- chunk {"id": "body-0160", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

Tab. VII shows relevant work that uses the MPC for postprocessing and distinguishes the filtering of a single proposed action, e.g., used in the safety-filter framework, or a whole trajectory of actions, e.g., or filtering of a state trajectory as. The filtering of action or state trajectories can be interpreted as providing an initial guess of decision variables of a nonconvex optimization problem to a solver, which then aims to find a good local minimum. In fact, the MPC needs to be approximately aligned with the MDP, and the role of the policy rather assists the MPC optimization solver by finding global/low-cost optimizers.

<!-- chunk {"id": "body-0161", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

One ought to observe, though, that if an MPC formulation is available to ensure the safety of the action taken in the real environment, typically in the form of a robust MPC scheme, then it is debatable whether training a policy (typically based on a NN) to be filtered by the robust MPC scheme or training the robust MPC scheme directly is more effective.

<!-- chunk {"id": "body-0162", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

So far, MPC has been considered as part of the actor or as an expert actor. In the following, we also highlight works that consider MPC as part of the critic, i.e., the MPC is used solely during training to provide a value function estimate.

<!-- chunk {"id": "body-0163", "role": "body", "section": "MPC for Pre- and Postprocessing", "weight": 1.0} -->

Fig. 8: Combinations: MPC as a critic. The plot is split into the learning and deployment phases. Blue boxes indicate Neural Networks (NNs), green boxes are used for MPCs, and blue/green boxes refer to parameterized MPCs that involve parameters/NNs that are learned during the learning phase, see Sect. VI-A.

<!-- chunk {"id": "body-0164", "role": "body", "section": "MPC AS A CRITIC", "weight": 1.0} -->

As outlined in Sect. IV, parameterized variants of the OCPs and allow for a structured function approximation of value function, action-value function, and the policy. While earlier discussions focused on using MPC as an actor, we next discuss the role of MPC used as a critic, cf., Fig. 2. We distinguish between three variants of MPC as a critic.

<!-- chunk {"id": "body-0165", "role": "body", "section": "MPC AS A CRITIC", "weight": 1.0} -->

- A. MPC as an expert critic, Sect. IX-A. The MPC is parameterized based on expert knowledge of the problem at hand, entering through the cost, model, or constraints, which we refer to as expert critic. - B. MPCas a learnable critic, Sect. IX-B. The MPC involves learnable parameters to improve the accuracy of the critic. - C. MPC as a learnable actor-critic, Sect. IX-C. The critic parameterization (possibly) differs from the one of the TABLE VII: Literature that uses MPC during the deployed algorithm together with the RL policy but not within the learning phase. Algorithms either use MPC as a reference provider for an RL policy or for postprocessing. Postprocessing is used to provide safety w.r.t. a known model and constraints or to take an action or state trajectory as an initial guess for the optimization solver.

<!-- chunk {"id": "body-0166", "role": "body", "section": "MPC AS A CRITIC", "weight": 1.0} -->

| MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | MPC for Postrocessing | In Tab. VIII, different publications are presented, depending on whether MPC parameters are tuned and which critic type described in the following three sections was used.

<!-- chunk {"id": "body-0167", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

An MPC scheme, as previously discussed, can readily deliver an action-value function Q MPC, which can be used to derive policy gradient equations to train an actor. An important assumption here is that the value function Q MPC approximates Q ⋆ as closely as possible. In fact, the MPC may usually just provide a value function of a desirable good suboptimal policy. Approximating Q ⋆ by the fixed MPC Qfunction was recently proposed. Very related is the line of work, that, inspired by the HamiltonianJacobi-Bellman equations, uses a first-order approximation of a Q-value function to criticize the actions generated by a learned policy.

<!-- chunk {"id": "body-0168", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

Consider the evaluation of the critic, involving solving the MPC optimization problem to obtain the corresponding actionvalue function Q MPC. Then, for a deterministic, parameterized policy µ θ, the learning objective related to is with the discounted visitation frequency ρ µ θ as defined in Sect. III-A3. Note that the policy parameter θ is updated to minimize the objective instead of the behavior cloning objective in Sect. VII or the MDP objective.

<!-- chunk {"id": "body-0169", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

An update scheme using the Q-function from MPC to criticize the learned policy µ θ as in is defined by DDPG with an MPC expert critic (µ ≈ µ MPC which is related to the DPG in but with a fixed expert critic. Here, D could be either a fixed dataset of states or generated iteratively by a mixture of µ θ and µ MPC like.

<!-- chunk {"id": "body-0170", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

Similar to Sect. VII, using an MPC as an expert critic leads to imitating the MPC expert policy. The primary advantage of using the MPC as an expert critic when compared to standard IL that relies on the mismatch between the expert and learned controls is its ability to guide a function approximator with limited expressive power by emphasizing which actions are more important to fit by using the Q-function. It further can introduce the constraint satisfactions to the objective using slacked constraints.

<!-- chunk {"id": "body-0171", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

It is important to emphasize that the MPC expert critic remains fixed and, therefore, does not approximate the actionvalue function Q µ θ of the learned policy during training. Indeed, policy gradient methods formally require the critic to be of the policy, i.e., to deliver the policy action-value function Q µ θ. In contrast, an MPC as an expert critic instead delivers the action-value function Q MPC based on expert knowledge of the environment, with the aim of approximating the optimal action-value function Q ⋆ as accurately as possible. If the actor has enough flexibility to clone the MPC policy perfectly, then using MPC as an expert critic would ultimately result in the actor matching the MPC performance but not improving it further.

<!-- chunk {"id": "body-0172", "role": "body", "section": "MPC as an Expert Critic", "weight": 1.0} -->

Consequently, as discussed in the following sections, further improvements can be achieved by allowing the MPC critic to adapt to the currently learned policy µ θ.

<!-- chunk {"id": "body-0173", "role": "body", "section": "MPC as a Learnable Critic", "weight": 1.0} -->

In the context of policy gradient methods, a parameterized MPC of any architecture shown in Fig. 3 can be used to approximate the policy action-value function Q π, and updated using data to capture it as correctly as possible. For instance, the parallel architecture of Fig. 3 is used. Using the MPC sensitivities, the MPC parameters can be learned using value-based methods. As discussed before, a parametric MPC can fully capture Q π given that it has a rich parameterization. This approach can be thought of as introducing expert knowledge into the policy gradient pipeline, using a critic combining harmoniously modelbased knowledge and learning to capture Q π as accurately and quickly as possible. The main reasoning behind this combination is that MPC is typically capable of providing a correct structure for the action-value function Q π prior to any training, giving a good starting point for the policy-gradient method. Then, the classic learning of Q π allows the MPC to become a better critic of the policy and to remain a good critic as the policy is modified by the policy-gradient method.

<!-- chunk {"id": "body-0174", "role": "body", "section": "MPC as a Learnable Critic", "weight": 1.0} -->

It is worth mentioning here that MPC as a learnable critic can be readily combined with a more classic NN, e.g., as a summation of their contribution to the action-value approximation. In that context, the MPC scheme can deliver a broadly correct approximation, while the NN can provide fine corrections. Unlike the approach of Sec. IX-A, MPC as a learnable critic aligns well with the actor-critic framework.

<!-- chunk {"id": "body-0175", "role": "body", "section": "MPC as a Learnable Actor-Critic", "weight": 1.0} -->

Using MPC as an actor and as a learnable critic naturally offers the opportunity to combine them into an actor-critic setup using MPC for both. In this setting, MPCs can be used both as an actor, delivering a parameterized policy π MPC θ to be trained, and as a critic, delivering value functions that are by construction close to the value function of the MPC policy, i.e., V MPC θ ≈ V π MPC θ, Q MPC θ ≈ Q π MPC θ, as opposed to random intializations of NNs.

<!-- chunk {"id": "body-0176", "role": "body", "section": "MPC as a Learnable Actor-Critic", "weight": 1.0} -->

During the learning, the MPC scheme operating as an actor typically needs to differ from the MPC scheme operating as a critic because π is not a minimizer of Q π when the policy is not optimal. In practice, two different MPC schemes can be used and trained in parallel: one as a critic, maintaining a good approximation of Q π MPC θ associated with π MPC θ given, and one to support π MPC θ itself, given. It can be, however, computationally expensive to use two MPC schemes in parallel, as the optimal solution of both must be produced at every training step of the policy, rather than the solution of only the MPC supporting the policy π MPC θ.

<!-- chunk {"id": "body-0177", "role": "body", "section": "MPC as a Learnable Actor-Critic", "weight": 1.0} -->

Along that line, proposed a critic formulation based on the value function obtained from an MPC-based actor. Their formulation employed V MPC θ along with the compatible function approximation suggested in to build a local approximation of the critic by using a first-order Taylor expansion, simplifying the actor-critic formulation with a single MPC scheme. This approach is effective if the MPC policy is sufficiently close to the optimal policy.

<!-- chunk {"id": "body-0178", "role": "body", "section": "THEORETICAL CONSIDERATIONS FOR COMBINING MPC AND RL", "weight": 1.0} -->

MDPs establish a fundamental bridge between RL and MPC, as RL provides tools to solve MDPs while MPC formulations can provide approximations, as discussed in the context of aligned learning in Sect. VIII-A and closed-loop optimal learning in Sect. VIII-B. This section explores the theoretical foundations of combining MPC and RL within the framework of MPC-based MDP approximations. A central theoretical contribution by provides a theoretical link between economic nonlinear model predictive control (ENMPC) and RL by connecting the MDP value functions and policy discussed in Sect. II with those generated by derivative-based MPC formulations detailed in Sect. IV-B2. This connection provides theoretical justification for approaches that incorporate MPC as either an actor or critic, as described in Sect. VIII and Sect. IX, respectively. We begin by presenting this key theoretical result before outlining its subsequent developments.

<!-- chunk {"id": "body-0179", "role": "body", "section": "THEORETICAL CONSIDERATIONS FOR COMBINING MPC AND RL", "weight": 1.0} -->

Following the definition in Sect. III-A3, let p f MPC (s 0 → s +, k, π θ) denote the probability of reaching state s + at step k when starting from the initial state s 0 and following the policy π, under model dynamics f MPC. A key assumption, is that the optimal value function remains bounded under the optimal policy and model of the dynamics: Assumption 10.1 ([262, Assumption 1]): The following set is non-empty for a given ¯ N ∈ N.

<!-- chunk {"id": "body-0180", "role": "body", "section": "THEORETICAL CONSIDERATIONS FOR COMBINING MPC AND RL", "weight": 1.0} -->

The authors of demonstrate that discounted MPC can capture the optimal value functions and policy of a discounted MDP through modifications of the stage and terminal costs, even when the model f MPC differs from the true state-transition function. This result was later extended in to undiscounted MPC by the following Theorem, establishing a central link to classical MPC stability theory: Theorem 10.1 ([262, Theorem 1]): Suppose that Assumption 10.1 holds for ¯ N ≥ N.

<!-- chunk {"id": "body-0181", "role": "body", "section": "THEORETICAL CONSIDERATIONS FOR COMBINING MPC AND RL", "weight": 1.0} -->

Given the conditions in Theorem 10.1, we classify MPC formulations that satisfy condition 1) as closed-loop optimal, where the learning process that aims at satisfying condition 1) using MPC within the actor as closed-loop optimal learning, see VIII-B. When both conditions 1) and 2) are satisfied, the MPC is MDP complete since it captures both the optimal policy and optimal action-value function of an MDP. At the top of this theoretical hierarchy lies the MDP aligned property, which demands that the MPC model exactly matches the statetransition kernel of the MDP. However, this property is rarely satisfied in practice, as MPC formulations typically employ deterministic models, while MDP state transitions are inherently stochastic.

<!-- chunk {"id": "body-0182", "role": "body", "section": "THEORETICAL CONSIDERATIONS FOR COMBINING MPC AND RL", "weight": 1.0} -->

| MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic | MPC as a Critic |

<!-- chunk {"id": "body-0183", "role": "body", "section": "Extensions of MPC-MDP Equivalence", "weight": 1.0} -->

Theorem 10.1 was originally developed in the context of ENMPC. Subsequent research has extended the result to several MPC variants, including real-time iteration MPC, mixedinteger MPC, scenario-based MPC, or any modelbased policy.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Extensions of MPC-MDP Equivalence", "weight": 1.0} -->

Instead of using OCP formulations that rely on one-step prediction rollouts of the environment, explores the connection between MDPs and QP formulations that arise for tracking problems with linear dynamics or as subproblems in OCP solvers. By parameterizing the QP directly rather than the prediction model, this approach offers additional flexibility that can enhance the performance of the MPC policy. Building on this idea, incorporates formulations from subspace predictive control (SPC), showing that the past input/output sequences can serve as a surrogate state from which future predictions are built. While this approach effectively handles systems without state estimators, its application is restricted to problems permitting autoregressive linear maps from inputs and outputs to future trajectories.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Extensions of MPC-MDP Equivalence", "weight": 1.0} -->

For systems requiring state estimation, an estimation layer such as moving horizon estimation (MHE) can be integrated to provide state feedback to the MPC. Research, demonstrated that jointly optimizing the parameters of both the MHE and MPC leads to significantly better performance compared to optimizing MPC parameters alone. The previously discussed challenges of differentiation through optimization layers and computational complexity in the forward pass extend naturally to the MHE layer.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Extensions of MPC-MDP Equivalence", "weight": 1.0} -->

The use of MPC and safety filters to ensure the safety of learned policies has emerged as a prominent research direction. One common approach projects control actions from trained policies onto a safe set by minimizing the distance to feasible actions that satisfy model dynamics and safety constraints. The authors of, exemplify this strategy by introducing a predictive safety filter that post-processes actions from trained RL policies. However, this projection step may lead to suboptimal actions when the agent is not aware of the filter, as discussed. An approach to learning safe and stable policies by construction via robust MPC within the policy is discussed in and further developed,.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Approximating Discounted MDP with Undiscounted MPC", "weight": 1.0} -->

Research exploring the relationship between MPCs and MDPs has focused on identifying conditions under which undiscounted MPCs can approximate discounted MDPs. This connection draws from dissipativity theory, a key concept in ENMPC stability analysis. Using dissipativity arguments, investigates undiscounted Q-Learing of tracking MPC schemes that are locally equivalent to dissipative ENMPC, focusing on learning storage functions that maintain ENMPC dissipativity. The authors of prove that under weak stability conditions, the optimal policy of undiscounted and discounted MDPs coincide -enabling stable undiscounted MPCs to yield the optimal policy of stable discounted MDPs. Recent advances by extend these results to unknown dynamics, demonstrating that undiscounted MPCs can capture optimal policies of discounted MDPs, as discussed around Theorem 10.1. Complementary work in introduces methods to align undiscounted MPC cost function minimizers with those of discounted MDPs.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Approximating Discounted MDP with Undiscounted MPC", "weight": 1.0} -->

These contributions share a common thread: by enforcing parameter updates that yield dissipative ENMPC formulations, stable ENMPC policies can be designed constructively rather than by using dissipativity solely as a verification criterion.

<!-- chunk {"id": "body-0189", "role": "body", "section": "State-transition Model for Closed-Loop Optimality", "weight": 1.0} -->

Traditional MPC applications select prediction models by minimizing the identification loss, along with considerations regarding considerations such as convexity or smoothness. However, models achieving good mean-error predictions or maximum-likelihood models may not necessarily guarantee closed-loop optimality. Recent research, establishes formal requirements for prediction models in to achieve closed-loop optimality and capture optimal value functions. They demonstrate that for a model f MPC to deliver both the optimal policy π ⋆ and optimal action-value function Q ⋆, it must satisfy: TABLE IX: Literature that discusses theoretical aspects of the connection between MPC and RL.

<!-- chunk {"id": "body-0190", "role": "body", "section": "State-transition Model for Closed-Loop Optimality", "weight": 1.0} -->

| Ref. | Authors | Year | Contribution | where V 0 is a constant. While does not directly yield a system identification procedure, it provides insights into models minimizing. Such models prove optimal for deterministic MDPs and LQR problems. Local optimality can be established for tracking problems, set-point stabilization, and dissipative economic problems by bounding the conditional covariance of the state transition dynamics P given in and the curvature of the (locally smooth) optimal value function V ⋆. However, models minimizing may not yield optimal policies for problems with non-smooth cost functions or dynamics, nondissipative MDPs, or strong disturbances.

<!-- chunk {"id": "body-0191", "role": "body", "section": "State-transition Model for Closed-Loop Optimality", "weight": 1.0} -->

The authors of approach the problem of model design by formulating an equivalent expression to in terms of the Bellman equation, introducing the optimal model design (OMD) method for simultaneous learning of Q-functions and models. This connects to broader developments in RL, such as the learned hidden state dynamic models, which focus on capturing only the state information essential for optimal actions and rewards. While focus on the theoretical properties of models in MPC contexts, provides algorithmic tools for their construction.

<!-- chunk {"id": "body-0192", "role": "body", "section": "SOFTWARE TOOLS AND IMPLEMENTATION ASPECTS", "weight": 1.0} -->

This section highlights challenges in practical implementations and points to available software solutions for combining MPC and RL.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Integrating Software from Machine Learning and Numerical Optimization", "weight": 1.0} -->

The architectural combinations of NNs and MPCs described in Sect. VI and illustrated in Fig. 3 significantly influence the choice of optimization software, particularly for derivativebased MPC solvers. When objective or constraint functions are highly nonlinear, the resulting optimization problems become nonconvex and computationally challenging. Furthermore, the selected software must be compatible with machine learning libraries to enable seamless integration.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Integrating Software from Machine Learning and Numerical Optimization", "weight": 1.0} -->

To address these challenges, recent open-source tools have emerged. The package l4casadi enables the integration of NNs φ θ ( s, z ) within the automatic differentiation tool CasADi. Similarly, l4acados bridges learned models from PyTorch to acados, focusing on residual models based on GPs in an integrated approach ϕ = φ θ ( z; s ). While these tools address derivative-based optimization, sampling-based MPC solvers offer an alternative approach, as they are less sensitive to nonlinear functions and only require forward simulation.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Implementation Aspects", "weight": 1.0} -->

Besides the difficulty of solving an optimization problem that involves NNs with derivative-based solvers, several further issues arise when combining MPC and RL, and should be considered in the implementation.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Implementation Aspects", "weight": 1.0} -->

- 1) Differentiation: The MPC solver differentiation requires the computation of sensitivities - a process that is theoretically straightforward but demands existing solvers to

<!-- chunk {"id": "body-0197", "role": "body", "section": "Implementation Aspects", "weight": 1.0} -->

- provide an efficient implementation of the parametric sensitivity computations. This capability is currently ongoing work in acados and will be detailed in a future publication. - 2) Solver States: MPC solvers often introduce additional solver states that must be incorporated into an augmented MDP. Nonlinear optimization processes start from initial guesses and may converge to different local minima, making these initial guesses part of the state space. This becomes particularly relevant in the RTI scheme (cf. Sect. IV), where the solver tracks optima across iterations rather than achieving full convergence. These additional solver states increase the MDP's complexity. - 3) Computational Efficiency: Some RL algorithms, such as SAC, require random sampling from replay buffers during learning. Computing gradients for each sample necessitates multiple solutions to optimization problems, resulting in significant computational overhead. - 4) Hardware Utilization: While machine learning frameworks benefit from parallelizable architectures, MPC solvers typically target CPU-based embedded applications. Efforts to leverage GPUs or parallel CPU implementations represent an emerging research direction, with recent developments including GPU-based sampling MPC and multicore CPU implementations for derivative-based MPC in acados.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Implementation Aspects", "weight": 1.0} -->

Complementary to this survey, early-stage software development aims at addressing these aspects. The code is publicly available as Learning for Predictive Control (leap-c) 2, a tool for derivative-based closed-loop learning utilizing MPC policies with the acados solver as a numerical optimization backend. Similar software projects with a lower degree of integration with fast OCP solvers exist 3.

<!-- chunk {"id": "body-0199", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Model predictive control (MPC) and reinforcement learning (RL) each require extensive background knowledge, as detailed in Sect. III and Sect. IV, and possess complementary features as highlighted in Sect. V. The latter raises the question of how to effectively combine these approaches to leverage their respective strengths while mitigating their limitations. In Sect. VI, various possible combinations within the framework of solving Markov decision processes (MDPs) through actorcritic RL are demonstrated.

<!-- chunk {"id": "body-0200", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Within this framework, MPC can serve as an algorithmic part in multiple roles. One role is as a supervisory expert actor in imitation learning (IL) or guided policy search (GPS) frameworks as discussed in VII. This allows to include domain knowledge and other features to develop computationally efficient policies for online deployment.

<!-- chunk {"id": "body-0201", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Another role for MPC is as a part of the policy - the most prevalent approach in the literature as shown in Sect. VIII. The categorization becomes more intricate in this case. We distinguish between two main directions: MDP aligned approaches that aim at modifying the MPC to reflect the MDP structure in terms of cost and state transitions, and closed-loop optimal approaches that focus on the closedloop optimality of MPC. In both cases, the MPC enters the learning pipeline through an optimization layer that may be expensive to evaluate in the forward inference path or to differentiate in the backpropagation path in order to provide the respective gradients, cf. App. A. A challenge concerning the implementation is that the computation of gradients is often not provided by optimization solvers, despite recent implementations, e.g., acados and other software discussed in Sect. XI. It is possible to avoid the gradient computation of the MPC solution by integrating it into the environment (cf. Sect. VIII-B) such that its parameterization becomes part of the action space. The critic then evaluates the parameterization of the MPC as opposed to the actions provided by the MPC output.

<!-- chunk {"id": "body-0202", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Considering MPC as a part of the environment and evaluating the critic on the MPC parameterization can be viewed as an example of the second practical architecture that we emphasize, i.e., architectures that use the MPC solver within the forward path but do not require its differentiation. Other architectures that avoid differentiation the category of using an expert MPC (Sect. VII), using a fixed MPC critic ( Sect. IX) and on-policy learning of the model and the terminal value function in the MDP aligned structure (Sect. VIII-A) can be seen as variants that do not require differentiation but use MPC as part of the forward path. Still, the repeated solutions of optimization problems make learning iterations significantly more expensive, and implementation aspects and tailored software as outlined in Sect. XI should be considered.

<!-- chunk {"id": "body-0203", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

The last role of MPC in the RL framework is that of a critic, as discussed in IX, which is not as prominent in the literature but may have the advantage of building explainable value functions estimates and significantly improving the sample efficiency and avoidance of local minima of RL training. Again, repeated MPC evaluations increase the computational cost compared to other artificial neural network (NN) layers.

<!-- chunk {"id": "body-0204", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Beyond these categories, several variants exist in the literature where MPC is not used during RL training but where MPC is solely used in the final deployed policy. These include off-policy learning of the model and some algorithms that learn a terminal value function in the MDP aligned structure ( Sect. VIII-A) as well as pre- and post-processing components (Sect. VIII-C). In the latter, MPC can function as a safety filter to enhance trained policies with its inherent constraint satisfaction capabilities and as a reference provider ( VIII-C) - a role that may extend to the learning phase as well.

<!-- chunk {"id": "body-0205", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Yet another important design decision is the combination architecture of NNs and MPCs in Sect. VI for which we identified the integrated, hierarchical, parallel or parameterized approaches outlined in Fig. 3. NNs are usually highly nonlinear functions that deserve a distinction from moderately nonlinear functions used as part of derivative-based MPC. In Sect. VI, we contrast between using NNs outside the MPC, i.e., it does not depend on decision variables of the optimization problem, using NNs inside the MPC optimization problem or avoiding NNs and using parameters of simpler linear or quadratic functions.

<!-- chunk {"id": "body-0206", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

Many variants of classifying MPC and RL methods exist in the literature, with notable frameworks presented, and. We used an actor-critic perspective and categories within that setting, that allows us to give a broad classification of very diverse algorithms.

<!-- chunk {"id": "body-0207", "role": "body", "section": "CONCLUSION AND DISCUSSION", "weight": 1.5} -->

As indicated in this survey, the expectations for the superiority of MPC and RL combinations are high, but challenges remain. Theoretical work provided already a solid foundation, cf. Sect. X. Nonetheless, practical work that shows large improvements over various domains is still required. Most importantly, the practical work requires numerical solvers to align with machine learning frameworks and tools that allow fast MPC solvers to be embedded in learning frameworks, see Section XI. With the increased development of such tools, the outlook on the MPC and RL combination appears prosperous. In future work, we hope the community will investigate whether the control paradigm shifts from MDP aligned learning to closed-loop optimal learning and whether the sampling complexity and other challenges of RL can be improved by MPC optimization modules.
