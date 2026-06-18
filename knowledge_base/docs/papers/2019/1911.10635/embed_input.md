<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms

Topics include Reinforcement learning, Multi-agent systems, Robotics, Autonomous driving, Learning, Multi-agent reinforcement learning, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent years have witnessed significant advances in reinforcement learning (RL), which has registered great success in solving various sequential decision-making problems in machine learning. Most of the successful RL applications, e.g., the games of Go and Poker, robotics, and autonomous driving, involve the participation of more than one single agent, which naturally fall into the realm of multi-agent RL (MARL), a domain with a relatively long history, and has recently re-emerged due to advances in single-agent RL techniques. Though empirically successful, theoretical foundations for MARL are relatively lacking in the literature. In this chapter, we provide a selective overview of MARL, with focus on algorithms backed by theoretical analysis. More specifically, we review the theoretical results of MARL algorithms mainly within two representative frameworks, Markov/stochastic games and extensive-form games, in accordance with the types of tasks they address, i.e., fully cooperative, fully competitive, and a mix of the two. We also introduce several significant but challenging applications of these algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Orthogonal to the existing reviews on MARL, we highlight several new angles and taxonomies of MARL theory, including learning in extensive-form games, decentralized MARL with networked agents, MARL in the mean-field regime, (non-)convergence of policy-based methods for learning in games, etc. Some of the new angles extrapolate from our own research endeavors and interests. Our overall goal with this chapter is, beyond providing an assessment of the current state of the field on the mark, to identify fruitful future research directions on theoretical studies of MARL. We expect this chapter to serve as continuing stimulus for researchers interested in working on this exciting while challenging topic.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed sensational advances of reinforcement learning (RL) in many prominent sequential decision-making problems, such as playing the game of Go, playing real-time strategy games, robotic control, playing card games, and autonomous driving, especially accompanied with the development of deep neural networks (DNNs) for function approximation. Intriguingly, most of the successful applications involve the participation of more than one single agent/player^11^1Hereafter, we will use *agent* and *player* interchangeably., which should be modeled systematically as multi-agent RL (MARL) problems. Specifically, MARL addresses the sequential decision-making problem of multiple autonomous agents that operate in a common environment, each of which aims to optimize its own long-term return by interacting with the environment and other agents. Besides the aforementioned popular ones, learning in multi-agent systems finds potential applications in other subareas, including cyber-physical systems, finance, sensor/communication networks, and social science.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Largely, MARL algorithms can be placed into three groups, *fully cooperative*, *fully competitive*, and *a mix of the two*, depending on the types of settings they address. In particular, in the cooperative setting, agents collaborate to optimize a common long-term return; while in the competitive setting, the return of agents usually sum up to zero. The mixed setting involves both cooperative and competitive agents, with general-sum returns. Modeling disparate MARL settings requires frameworks spanning from optimization theory, dynamic programming, game theory, and decentralized control, see §2.2 for more detailed discussions. In spite of these existing multiple frameworks, several challenges in MARL are in fact common across the different settings, especially for the theoretical analysis. Specifically, first, the learning goals in MARL are *multi-dimensional*, as the objectives of all agents are not necessarily aligned, which brings up the challenge of dealing with equilibrium points, as well as some additional performance criteria beyond return-optimization, such as the efficiency of communication/coordination, and robustness against potential adversarial agents.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, as all agents are improving their policies according to their own interests concurrently, the environment faced by each agent becomes *non-stationary*. This breaks or invalidates the basic framework of most theoretical analyses in the single-agent setting. Furthermore, the joint action space that increases exponentially with the number of agents may cause scalability issues, known as the *combinatorial nature* of MARL. Additionally, the information structure, i.e., *who knows what*, in MARL is more involved, as each agent has limited access to the observations of others, leading to possibly suboptimal decision rules locally. A detailed elaboration on the underlying challenges can be found in §3.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has in fact been no shortage of efforts attempting to address the above challenges. See for a comprehensive overview of earlier theories and algorithms on MARL. Recently, this domain has gained resurgence of interest due to the advances of single-agent RL techniques. Indeed, a huge volume of work on MARL has appeared lately, focusing on either identifying new learning criteria and/or setups, or developing new algorithms for existing setups, thanks to the development of deep learning, operations research, and multi-agent systems. Nevertheless, not all the efforts are placed under rigorous theoretical footings, partly due to the limited understanding of even single-agent deep RL theories, and partly due to the inherent challenges in multi-agent settings. As a consequence, it is imperative to review and organize the MARL algorithms with theoretical guarantees, in order to highlight the boundary of existing research endeavors, and stimulate potential future directions on this topic.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this chapter, we provide a selective overview of theories and algorithms in MARL, together with several significant while challenging applications. More specifically, we focus on two representative frameworks of MARL, namely, Markov/stochastic games and extensive-form games, in discrete-time settings as in standard single-agent RL. In conformity with the aforementioned three groups, we review and pay particular attention to MARL algorithms with convergence and complexity analysis, most of which are fairly recent. With this focus in mind, we note that our overview is by no means comprehensive. In fact, besides the classical reference, there are several other reviews on MARL that have appeared recently, due to the resurgence of MARL. We would like to emphasize that these reviews provide views and taxonomies that are complementary to ours: surveys the works that are specifically devised to address *opponent-induced non-stationarity*, one of the challenges we discuss in §3; are relatively more comprehensive, but with the focal point on *deep* MARL, a subarea with scarce theories thus far on the other hand, focuses on algorithms in the *cooperative* setting only, though the review within this setting is extensive.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we spotlight several new angles and taxonomies that are comparatively underexplored in the existing MARL reviews, primarily owing to our own research endeavors and interests. First, we discuss the framework of extensive-form games in MARL, in addition to the conventional one of Markov games, or even simplified repeated games; second, we summarize the progresses of a recently boosting subarea: decentralized MARL with *networked* agents, as an extrapolation of our early works on this; third, we bring about the *mean-field* regime into MARL, as a remedy for the case with an extremely large population of agents; fourth, we highlight some recent advances in optimization theory, which shed lights on the (non-)convergence of policy-based methods for MARL, especially zero-sum games. We have also reviewed some of the literature on MARL in partially observed settings, but without using deep RL as heuristic solutions. We expect these new angles to help identify fruitful future research directions, and more importantly, inspire researchers with interests in establishing rigorous theoretical foundations on MARL.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Roadmap. The remainder of this chapter is organized as follows. In §2, we introduce the background of MARL: standard algorithms for single-agent RL, and the frameworks of MARL. In §3, we summarize several challenges in developing MARL theory, in addition to the single-agent counterparts. A series of MARL algorithms, mostly with theoretical guarantees, are reviewed and organized in §4, according to the types of tasks they address. In §5, we briefly introduce a few recent successes of MARL driven by the algorithms mentioned, followed by conclusions and several open research directions outlined in §6.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Single-Agent RL", "weight": 1.0} -->

A reinforcement learning agent is modeled to perform sequential decision-making by interacting with the environment. The environment is usually formulated as an infinite-horizon discounted Markov decision process (MDP), henceforth referred to as Markov decision process^22^2Note that there are several other standard formulations of MDPs, e.g., time-average-reward setting and finite-horizon episodic setting. Here, we only present the classical infinite-horizon discounted setting for ease of exposition., which is formally defined as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Value-based RL methods are devised to find a good estimate of the state-action value function, namely, the optimal Q-function $Q_{\pi^{\ast}}$. The (approximate) optimal policy can then be extracted by taking the greedy action of the Q-function estimate. One of the most popular value-based algorithms is Q-learning, where the agent maintains an estimate of the Q-value function $\hat{Q}{(s,a)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

where $\alpha > 0$ is the stepsize/learning rate. Under certain conditions on $\alpha$, Q-learning can be proved to converge to the optimal Q-value function almost surely, with finite state and action spaces. Moreover, when combined with neural networks for function approximation, deep Q-learning has achieved great empirical breakthroughs in human-level control applications. Another popular *on-policy* value-based method is SARSA, whose convergence was established in for finite-space settings.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

An alternative while popular value-based RL algorithm is Monte-Carlo tree search (MCTS), which estimates the optimal value function by constructing a search tree via Monte-Carlo simulations. Tree polices that judiciously select actions to balance exploration-exploitation are used to build and update the search tree. The most common tree policy is to apply the UCB1 (UCB stands for *upper confidence bound*) algorithm, which was originally devised for stochastic multi-arm bandit problems, to each node of the tree. This yields the popular UCT algorithm. Recent research endeavors on the non-asymptotic convergence of MCTS include.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Besides, another significant task regarding value functions in RL is to *estimate the value function associated with a given policy* (not only the optimal one). This task, usually referred to as *policy evaluation*, has been tackled by algorithms that follow a similar update as (2.1), named *temporal difference* (TD) learning. Some other common policy evaluation algorithms with convergence guarantees include gradient TD methods with linear, and nonlinear function approximations. See for a more detailed review on policy evaluation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Another type of RL algorithms directly searches over the policy space, which is usually estimated by parameterized function approximators like neural networks, namely, approximating $\pi{( \cdot |s)} \approx \pi_{\theta}{( \cdot |s)}$. As a consequence, the most straightforward idea, which is to update the parameter along the gradient direction of the long-term reward, has been instantiated by the policy gradient (PG) method. As a key premise for the idea, the closed-form of PG is given as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

where $J{(\theta)}$ and $Q_{\pi_{\theta}}$ are the expected return and Q-function under policy $\pi_{\theta}$, respectively, ${{\nabla\log}\pi_{\theta}}{(\left. a \middle| s \right.)}$ is the score function of the policy, and $\eta_{\pi_{\theta}}$ is the state occupancy measure, either discounted or ergodic, under policy $\pi_{\theta}$. Then, various policy gradient methods, including REINFORCE, G(PO)MDP, and actor-critic algorithms, have been proposed by estimating the gradient in different ways. A similar idea also applies to deterministic policies in continuous-action settings, whose PG form has been derived recently. Besides gradient-based ones, several other policy optimization methods have achieved state-of-the-art performance in many applications, including PPO, TRPO, soft actor-critic.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Compared with value-based RL methods, policy-based ones enjoy better convergence guarantees, especially with neural networks for function approximation, which can readily handle massive or even continuous state-action spaces. Besides the value- and policy-based methods, there also exist RL algorithms based on the linear program formulation of an MDP; see recent efforts.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multi-Agent RL Framework", "weight": 1.0} -->

In a similar vein, multi-agent RL also addresses sequential decision-making problems, but with more than one agent involved. In particular, both the evolution of the system state and the reward received by each agent are influenced by the joint actions of all agents. More intriguingly, each agent has its own long-term reward to optimize, which now becomes a function of the policies of all other agents. Such a general model finds broad applications in practice, see §5 for a detailed review of several prominent examples.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Multi-Agent RL Framework", "weight": 1.0} -->

In general, there exist two seemingly different but closely related theoretical frameworks for MARL, Markov/stochastic games and extensive-form games, as to be introduced next. Evolution of the systems under different frameworks are illustrated in Figure 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Markov/Stochastic Games", "weight": 1.0} -->

One direct generalization of MDP that captures the intertwinement of multiple agents is Markov games (MGs), also known as stochastic games. Originated from the seminal work, the framework of MGs^44^4Similar to the single-agent setting, here we only introduce the infinite-horizon discounted setting for simplicity, though other settings of MGs, e.g., time-average-reward setting and finite-horizon episodic setting, also exist. has long been used in the literature to develop MARL algorithms, see §4 for more details. We introduce the formal definition as below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Extensive-Form Games", "weight": 1.0} -->

Even though they constitute a classical formalism for MARL, Markov games can only handle the fully observed case, i.e., the agent has *perfect information* on the system state $s_{t}$ and the executed action $a_{t}$ at time $t$. Nonetheless, a plethora of MARL applications involve agents with only partial observability, i.e., *imperfect information* of the game. Extension of Markov games to partially observed case may be applicable, which, however, is challenging to solve, even under the cooperative setting.^66^6Partially observed Markov games under the cooperative setting are usually formulated as decentralized POMDP (Dec-POMDP) problems. See §4.1.3 for more discussions on this setting.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Extensive-Form Games", "weight": 1.0} -->

In contrast, another framework, named *extensive-form games*, can handily model imperfect information for multi-agent decision-making. This framework is rooted in computational game theory and has been shown to admit polynomial-time algorithms under mild conditions. We briefly introduce the framework of extensive-form games as follows.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2.6 (Other MARL Frameworks)", "weight": 1.0} -->

Several other theoretical frameworks for MARL also exist in the literature, e.g., normal-form and/or repeated games, and partially observed Markov games. However, the former framework can be viewed as a special case of MGs, with a singleton state; most early theories of MARL in this framework have been restricted to small scale problems only. MARL in the latter framework, on the other hand, is inherently challenging to address in general, leading to relatively scarce theories in the literature. Due to space limitation, we do not introduce these models here in any detail. We will briefly review MARL algorithms under some of these models, especially the partially observed setting, in §4, though. Interested readers are referred to the early review for more discussions on MARL in normal-form/repeated games.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Challenges in MARL Theory", "weight": 1.0} -->

Despite a general model that finds broad applications, MARL suffers from several challenges in theoretical analysis, in addition to those that arise in single-agent RL. We summarize below the challenges that we regard as fundamental in developing theories for MARL.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Non-Unique Learning Goals", "weight": 1.0} -->

Unlike single-agent RL, where the goal of the agent is to maximize the long-term return efficiently, the learning goals of MARL can be vague at times. In fact, as argued, the *unclarity* of the problems being addressed is the fundamental flaw in many early MARL works. Indeed, the goals that need to be considered in the analysis of MARL algorithms can be multi-dimensional. The most common goal, which has, however, been challenged, is the convergence to Nash equilibrium as defined in §2.2. By definition, NE characterizes the point that no agent will deviate, if any algorithm *finally* converges. This is undoubtedly a reasonable solution concept in game theory, under the assumption that the agents are all *rational*, and are capable of perfectly reasoning and infinite mutual modeling of agents. However, with *bounded rationality*, the agents may only be able to perform *finite* mutual modeling. As a result, the learning dynamics that are devised to converge to NE may not be justifiable for practical MARL agents.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Non-Unique Learning Goals", "weight": 1.0} -->

Instead, the goal may be focused on designing the best *learning strategy* for a given agent and *a fixed class of the other agents in the game.* In fact, these two goals are styled as *equilibrium agenda* and *AI agenda*.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Non-Unique Learning Goals", "weight": 1.0} -->

Besides, it has also been controversial that *convergence* (to the equilibrium point) is the dominant performance criterion for MARL algorithm analysis. In fact, it has been recognized in that value-based MARL algorithms fail to converge to the *stationary* NE of general-sum Markov games, which motivated the new solution concept of *cyclic equilibrium* therein, at which the agents cycle rigidly through a set of stationary policies, i.e., not converging to any NE policy. Alternatively, separate the learning goal into being both *stable* and *rational*, where the former ensures the algorithm to be convergent, given a predefined, targeted class of opponents' algorithms, while the latter requires the convergence to a best-response when the other agents remain stationary. If all agents are both stable and rational, convergence to NE naturally arises in this context. Moreover, the notion of *regret* introduces another angle to capture agents' rationality, which measures the performance of the algorithm compared to the best hindsight static strategy.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Non-Unique Learning Goals", "weight": 1.0} -->

No-regret algorithms with asymptotically zero average regret guarantee the convergence to the equilibria of certain games, which in essence guarantee that the agent is not *exploited* by others.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Non-Unique Learning Goals", "weight": 1.0} -->

In addition to the goals concerning optimizing the return, several other goals that are special to multi-agent systems have also drawn increasing attention. For example, investigate *learning to communicate*, in order for the agents to better coordinate. Such a concern on communication protocols has naturally inspired the recent studies on *communication-efficient* MARL. Other important goals include how to learn without over-fitting certain agents, and how to learn robustly with either malicious/adversarial or failed/dysfunctional learning agents. Still in their infancy, some works concerning aforementioned goals provide only empirical results, leaving plenty of room for theoretical studies.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Non-Stationarity", "weight": 1.0} -->

Another key challenge of MARL lies in the fact that multiple agents usually learn concurrently, causing the environment faced by each individual agent to be *non-stationary*. In particular, the action taken by one agent affects the reward of other opponent agents, and the evolution of the state. As a result, the learning agent is required to account for how the other agents behave and adapt to the *joint behavior* accordingly. This invalidates the stationarity assumption for establishing the convergence of single-agent RL algorithms, namely, the stationary Markovian property of the environment such that the individual reward and current state depend only on the previous state and action taken. This precludes the direct use of mathematical tools for single-agent RL analysis in MARL.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Non-Stationarity", "weight": 1.0} -->

Indeed, theoretically, if the agent ignores this issue and optimizes its own policy assuming a stationary environment, which is usually referred to as an *independent learner*, the algorithms may fail to converge, except for several special settings. Empirically, however, independent learning may achieve satisfiable performance in practice. As the most well-known issue in MARL, non-stationarity has long been recognized in the literature. A recent comprehensive survey peculiarly provides an overview on how it is modeled and addressed by state-of-the-art multi-agent learning algorithms. We thus do not include any further discussion on this challenge, and refer interested readers to.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Scalability Issue", "weight": 1.0} -->

To handle non-stationarity, each individual agent may need to account for the *joint action space*, whose dimension increases exponentially with the number of agents. This is also referred to as the *combinatorial nature* of MARL. Having a large number of agents complicates the theoretical analysis, especially the convergence analysis, of MARL. This argument is substantiated by the fact that theories on MARL for the two-player zero-sum setting are much more extensive and advanced than those for general-sum settings with more than two agents, see §4 for a detailed comparison. One possible remedy for the scalability issue is to assume additionally the *factorized* structures of either the value or reward functions with regard to the action dependence; see for the original heuristic ideas, and for recent empirical progress. Relevant theoretical analysis had not been established until recently, which considers a special dependence structure, and develops a provably convergent model-based algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Scalability Issue", "weight": 1.0} -->

Another theoretical challenge of MARL that is brought about independently of, but worsened, the scalability issue, is to build up theories for deep multi-agent RL. Particularly, scalability issues necessitate the use of function approximation, especially deep neural networks, in MARL. Though empirically successful, the theoretical analysis of deep MARL is an almost uncharted territory, with the currently limited understanding of deep learning theory, not alone the deep RL theory. This is included as one of the future research directions in §6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Various Information Structures", "weight": 1.0} -->

(b) Decentralized setting with networked agents
(c) Fully decentralized setting

<!-- chunk {"id": "body-0036", "role": "body", "section": "Various Information Structures", "weight": 1.0} -->

Compared to the single-agent case, the information structure of MARL, namely, *who knows what* at the training and execution, is more involved. For example, in the framework of Markov games, it suffices to observe the instantaneous state $s_{t}$, in order for each agent to make decisions, since the local policy $\pi^{i}$ mapping from $\mathcal{S}$ to $(\mathcal{A}^{i})$ contains the equilibrium policy. On the other hand, for extensive-form games, each agent may need to recall the history of past decisions, under the common perfect recall assumption. Furthermore, as self-interested agents, each agent can scarcely access either the *policy* or the rewards of the opponents, but at most the action samples taken by them. This partial information aggravates the issues caused by non-stationarity, as the samples can hardly recover the exact behavior of the opponents' underlying policies, which increases the non-stationarity viewed by individual agents.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Various Information Structures", "weight": 1.0} -->

The extreme case is the aforementioned *independent learning* scheme, which assumes the observability of only the local action and reward, and suffers from non-convergence in general.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Various Information Structures", "weight": 1.0} -->

Learning schemes resulting from various information structures lead to various levels of difficulty for theoretical analysis. Specifically, to mitigate the partial information issue above, a great deal of work assumes the existence of a *central controller* that can collect information such as joint actions, joint rewards, and joint observations, and even design policies for all agents. This structure gives birth to the popular learning scheme of *centralized-learning-decentralized-execution*, which stemmed from the works on planning for the partially observed setting, namely, Dec-POMDPs, and has been widely adopted in recent (deep) MARL works. For cooperative settings, this learning scheme greatly simplifies the analysis, allowing the use of tools for single-agent RL analysis. Though, for non-cooperative settings with heterogeneous agents, this scheme does not significantly simplify the analysis, as the learning goals of the agents are not aligned, see §3.1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Various Information Structures", "weight": 1.0} -->

Nonetheless, generally such a central controller does not exist in many applications, except the ones that can easily access a simulator, such as video games and robotics. As a consequence, a *fully decentralized* learning scheme is preferred, which includes the aforementioned independent learning scheme as a special case. To address the non-convergence issue in independent learning, agents are usually allowed to exchange/share local information with their neighbors over a communication network. We refer to this setting as *a decentralized one with networked agents*. Theoretical analysis for convergence is then made possible in this setting, the difficulty of which sits between that of single-agent RL and general MARL algorithms. Three different information structures are depicted in Figure 2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "MARL Algorithms with Theory", "weight": 1.0} -->

This section provides a selective review of MARL algorithms, and categorizes them according to the tasks to address. Exclusively, we review here the works that are focused on the theoretical studies only, which are mostly built upon the two representative MARL frameworks, fully observed Markov games and extensive-form games, introduced in §2.2. A brief summary on MARL for partially observed Markov games in *cooperative* settings, namely, the Dec-POMDP problems, is also provided below in §4.1, due to their relatively more mature theory than that of MARL for general partially observed Markov games.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

Cooperative MARL constitutes a great portion of MARL settings, where all agents collaborate with each other to achieve some shared goal. Most cooperative MARL algorithms backed by theoretical analysis are devised for the following more specific settings.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

A majority of cooperative MARL settings involve *homogeneous* agents with a *common* reward function that aligns all agents' interests. In the extreme case with large populations of agents, such a homogeneity also indicates that the agents play an *interchangeable* role in the system evolution, and can hardly be distinguished from each other. We elaborate more on homogeneity below.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

Consider a Markov game as in Definition 2.2 with $R^{1} = R^{2} = \cdots = R^{N} = R$, where the reward $R:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow R}$ is influenced by the joint action in $\mathcal{A} = {\mathcal{A}^{1} \times \cdots \times \mathcal{A}^{N}}$. As a result, the Q-function is identical for all agents. Hence, a straightforward algorithm proceeds by performing the standard Q-learning update (2.1) at each agent, but taking the $\max$ over the joint action space $a^{\prime} \in \mathcal{A}$. Convergence to the optimal/equilibrium Q-function has been established, when both state and action spaces are finite.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

However, convergence of the Q-function does not necessarily imply that of the equilibrium policy for the Markov team, as any combination of equilibrium policies extracted at each agent may not constitute an equilibrium policy, if the equilibrium policies are non-unique, and the agents fail to agree on which one to select. Hence, convergence to the NE policy is only guaranteed if either the equilibrium is assumed to be unique, or the agents are coordinated for equilibrium selection. The latter idea has first been validated in the cooperative repeated games setting, a special case of Markov teams with a singleton state, where the agents are joint-action learners (JAL), maintaining a Q-value for joint actions, and learning empirical models of all others. Convergence to equilibrium point is claimed, without a formal proof. For the actual Markov teams, this coordination has been exploited, which proposes *optimal adaptive learning* (OAL), the first MARL algorithm with provable convergence to the equilibrium policy. Specifically, OAL first learns the game structure, and constructs virtual games at each state that are *weakly acyclic* with respect to (w.r.t.) a biased set.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

OAL can be shown to converge to the NE, by introducing the biased adaptive play learning algorithm for the constructed weakly acyclic games, motivated.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

Apart from equilibrium selection, another subtlety special to Markov teams (compared to single-agent RL) is the necessity to address the scalability issue, see §3.3. As independent Q-learning may fail to converge, one early attempt toward developing scalable while convergent algorithms for MMDPs is, which advocates a distributed Q-learning algorithm that converges for *deterministic* finite MMDPs. Each agent maintains only a Q-table of state $s$ and local action $a^{i}$, and successively takes maximization over the joint action $a^{\prime}$. No other agent's actions and their histories can be acquired by each individual agent. Several other heuristics (with no theoretical backing) regarding either reward or value function factorization have been proposed to mitigate the scalability issue. Very recently, provides a rigorous characterization of conditions that justify this value factorization idea. Another recent theoretical work along this direction is, which imposes a special dependence structure, i.e., a one-directional tree, so that the (near-)optimal policy of the overall MMDP can be provably well-approximated by *local policies*.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

More recently, has studied common interest games, which includes Markov teams as an example, and develops a *decentralized* RL algorithm that relies on only states, local actions and rewards. With the same information structure as independent Q-learning, the algorithm is guaranteed to converge to *team optimal* equilibrium policies, and not just equilibrium policies. This is important as in general, a suboptimal equilibrium can perform arbitrarily worse than the optimal equilibrium.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

For policy-based methods, to our knowledge, the only convergence guarantee for this setting exists. The authors propose two-timescale actor-critic *fictitious play* algorithms, where at the slower timescale, the actor mixes the current policy and the best-response one w.r.t. the local Q-value estimate, while at the faster timescale the critic performs policy evaluation, as if all agents' policies are stationary. Convergence is established for *simultaneous move multistage games* with a common (also zero-sum, see §4.2.2) reward, a special Markov team with initial and absorbing states, and each state being visited only once.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

From a game-theoretic perspective, a more general framework to embrace cooperation is *potential games*, where there exits some *potential* function shared by all agents, such that if any agent changes its policy unilaterally, the change in its reward equals (or proportions to) that in the potential function. Though most potential games are stateless, an extension named *Markov potential games* (MPGs) has gained increasing attention for modeling *sequential* decision-making, which includes Markovian states whose evolution is affected by the joint actions. Indeed, MMDPs/Markov teams constitute a particular case of MPGs, with the potential function being the common reward; such dynamic games can also be viewed as being strategically equivalent to Markov teams, using the terminology, e.g., \[164, Chapter $1$\]. Under this model, provides verifiable conditions for a Markov game to be an MPG, and shows the equivalence between finding closed-loop NE in MPG and solving a single-agent optimal control problem. Hence, single-agent RL algorithms are then enabled to solve this MARL problem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

Another idea toward tackling the scalability issue is to take the setting to the *mean-field* regime, with an extremely large number of homogeneous agents. Each agent's effect on the overall multi-agent system can thus become infinitesimal, resulting in all agents being interchangeable/indistinguishable. The interaction with other agents, however, is captured simply by some mean-field quantity, e.g., the average state, or the empirical distribution of states. Each agent only needs to find the best response to the mean-field, which considerably simplifies the analysis. This mean-field view of multi-agent systems has been approached by the mean-field games (MFGs) model, the team model with mean-field sharing, and the game model with mean-field actions.^77^7The difference between mean-field teams and mean-field games is mainly the solution concept: optimum versus equilibrium, as the difference between general dynamic team theory and game theory. Although the former can be viewed as a special case of the latter, related works are usually reviewed separately in the literature. We follow here this convention.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Homogeneous Agents", "weight": 1.0} -->

MARL in these models have not been explored until recently, mostly in the non-cooperative setting of MFGs, see §4.3 for a more detailed review. Regarding the cooperative setting, recent work studies RL for Markov teams with mean-field sharing. Compared to MFG, the model considers agents that share a common reward function depending only on the local state and the mean-field, which encourages cooperation among the agents. Also, the term mean-field refers to the *empirical average* for the states of *finite* population, in contrast to the *expectation* and *probability distribution* of *infinite* population in MFGs. Based on the dynamic programming decomposition for the specified model, several popular RL algorithms are easily translated to address this setting. More recently, approach the problem from a mean-field control (MFC) model, to model large-population of cooperative decision-makers. Policy gradient methods are proved to converge for linear quadratic MFCs, and mean-field Q-learning is then shown to converge for general MFCs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Cooperative agents in numerous practical multi-agent systems are not always homogeneous. Agents may have different preferences, i.e., reward functions, while they still form a team to maximize the return of the *team-average* reward $\overline{R}$, with ${\overline{R}{(s,a,s^{\prime})}} = {N^{- 1} \cdot {\sum_{i \in \mathcal{N}}{R^{i}{(s,a,s^{\prime})}}}}$. More subtly, the reward function is sometimes not sharable with others, as the preference is kept private to each agent. This setting finds broad applications in engineering systems as sensor networks, smart grid, intelligent transportation systems, and robotics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Covering the homogeneous setting in §4.1.1 as a special case, the specified one definitely requires more coordination, as, for example, the global value function cannot be estimated locally without knowing other agents' reward functions. With a central controller, most MARL algorithms reviewed in §4.1.1 directly apply, since the controller can collect and average the rewards, and distributes the information to all agents. Nonetheless, such a controller may not exist in most aforementioned applications, due to either cost, scalability, or robustness concerns. Instead, the agents may be able to share/exchange information with their neighbors over a possibly time-varying and sparse communication network, as illustrated in Figure 2 (b). Though MARL under this *decentralized/distributed*^88^8Note that hereafter we use *decentralized* and *distributed* interchangeably for describing this paradigm. paradigm is imperative, it is relatively less-investigated, in comparison to the extensive results on distributed/consensus algorithms that solve *static/one-stage* optimization problems, which, unlike RL, involves no system *dynamics*, and does not maximize the *long-term* objective as a *sequential-decision making* problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

The most significant goal is to learn the optimal joint policy, while each agent only accesses to local and neighboring information over the network. The idea of MARL with networked agents dates back to. To our knowledge, the first provably convergent MARL algorithm under this setting is due to, which incorporates the idea of *consensus $+$ innovation* to the standard Q-learning algorithm, yielding the *$\mathcal{Q}\mathcal{D}$-learning* algorithm with the following update

<!-- chunk {"id": "body-0055", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

where ${\alpha_{t,s,a},\beta_{t,s,a}} > 0$ are stepsizes, $\mathcal{N}_{t}^{i}$ denotes the set of neighboring agents of agent $i$, at time $t$. Compared to the Q-learning update (2.1), *$\mathcal{Q}\mathcal{D}$*-learning appends an innovation term that captures the difference of Q-value estimates from its neighbors. With certain conditions on the stepsizes, the algorithm is guaranteed to converge to the optimum Q-function for the tabular setting.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Due to the scalability issue, function approximation is vital in MARL, which necessitates the development of policy-based algorithms. Our work proposes actor-critic algorithms for this setting. Particularly, each agent parameterizes its own policy $\pi_{\theta^{i}}^{i}:{\mathcal{S}\rightarrow{(\mathcal{A}^{i})}}$ by some parameter $\theta^{i} \in R^{m^{i}}$, the policy gradient of the return is first derived as

<!-- chunk {"id": "body-0057", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

where $Q_{\theta}$ is the global value function corresponding to $\overline{R}$ under the joint policy $\pi_{\theta}$ that is defined as ${\pi_{\theta}{(\left. a \middle| s \right.)}}:={\prod_{i \in \mathcal{N}}{\pi_{\theta^{i}}^{i}{(\left. a^{i} \middle| s \right.)}}}$. As an analogy to (2.2), the policy gradient in (4.1) involves the expectation of the product between the local score function ${{\nabla_{\theta^{i}}\log}\pi_{\theta^{i}}^{i}}{(s,a^{i})}$ and the global Q-function $Q_{\theta}$. The latter, nonetheless, cannot be estimated individually at each agent.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

As a result, by parameterizing each local copy of $Q_{\theta}{( \cdot, \cdot )}$ as $Q_{\theta}{( \cdot, \cdot;\omega^{i})}$ for agent $i$, we propose the following consensus-based TD learning for the critic step, i.e.,

<!-- chunk {"id": "body-0059", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

where $\beta_{\omega,t} > 0$ is the stepsize, $\delta_{t}^{i}$ is the local TD-error calculated using $Q_{\theta}{( \cdot, \cdot;\omega^{i})}$. The first relation in (4.2) performs the standard TD update, followed by a weighted combination of the neighbors' estimates ${\overset{\sim}{\omega}}_{t}^{j}$. The weights here, $c_{t}{(i,j)}$, are dictated by the topology of the communication network, with non-zero values only if two agents $i$ and $j$ are connected at time $t$. They also need to satisfy the *doubly stochastic* property in expectation, so that $\omega_{t}^{i}$ reaches a *consensual* value for all $i \in \mathcal{N}$ if it converges.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Then, each agent $i$ updates its policy following stochastic policy gradient given by (4.1) in the actor step, using its own Q-function estimate $Q_{\theta}{( \cdot, \cdot;\omega_{t}^{i})}$. A variant algorithm is also introduced, relying on not the Q-function, but the state-value function approximation, to estimate the global advantage function.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

With these in mind, almost sure convergence is established in for these decentralized actor-critic algorithms, when linear functions are used for value function approximation. Similar ideas are also extended to the setting with continuous spaces, where deterministic policy gradient (DPG) method is usually used. Off-policy exploration, namely a stochastic behavior policy, is required for DPG, as the deterministic on-policy may not be explorative enough. However, in the multi-agent setting, as the policies of other agents are unknown, the common off-policy approach for DPG \[71, §4.2\] does not apply. Inspired by the expected policy gradient (EPG) method which unifies stochastic PG (SPG) and DPG, we develop an algorithm that remains on-policy, but reduces the variance of general SPG. In particular, we derive the multi-agent version of EPG, based on which we develop the actor step that can be implemented in a decentralized fashion, while the critic step still follows (4.2). Convergence of the algorithm is then also established when linear function approximation is used.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

In the same vein, considers the extension of to an off-policy setting, building upon the emphatic temporal differences (ETD) method for the critic. By incorporating the analysis of ETD($\lambda$) into, almost sure convergence guarantee has also been established. Another off-policy algorithm for the same setting is proposed concurrently, where agents do not share their estimates of value function. Instead, the agents aim to reach consensus over the global optimal policy estimation. Provable convergence is then established for the algorithm, with a local critic and a consensus actor.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

RL for decentralized networked agents has also been investigated in *multi-task*, in addition to the multi-agent, settings. In some sense, the former can be regarded as a simplified version of the latter, where each agent deals with an *independent MDP* that is not affected by other agents, while the goal is still to learn the optimal joint policy that accounts for the average reward of all agents. proposes a distributed actor-critic algorithm, assuming that the states, actions, and rewards are all local to each agent. Each agent performs a local TD-based critic step, followed by a consensus-based actor step that follows the gradient calculated using information exchanged from the neighbors. Gradient of the average return is then proved to converge to zero as the iteration goes to infinity. has developed *Diff-DAC*, another distributed actor-critic algorithm for this setting, from duality theory. The updates resemble those, but provide additional insights that actor-critic is actually an instance of the dual ascent method for solving a linear program.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Note that all the aforementioned convergence guarantees are *asymptotic*, i.e., the algorithms converge as the iteration numbers go to infinity, and are restricted to the case with linear function approximations. This fails to quantify the performance when finite iterations and/or samples are used, not to mention when nonlinear functions such as deep neural networks are utilized. As an initial step toward *finite-sample analyses* in this setting with more *general* function approximation, we consider in the *batch* RL algorithms, specifically, decentralized variants of the fitted-Q iteration (FQI). Note that we focus on FQI since it motivates the celebrated deep Q-learning algorithm when deep neural networks are used for function approximation. We study FQI variants for both the cooperative setting with networked agents, and the competitive setting with two teams of such networked agents (see §4.2.1 for more details). In the former setting, all agents cooperate to iteratively update the global Q-function estimate, by fitting nonlinear least squares with the target values as the responses.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

$i$'s Q-function estimate at iteration $t$. Then, all agents cooperate to find a common Q-function estimate by solving

<!-- chunk {"id": "body-0066", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Since $y_{j}^{i}$ is only known to agent $i$, the problem in (4.3) aligns with the formulation of *distributed/consensus optimization*, whose global optimal solution can be achieved by the algorithms therein, if $\mathcal{F}$ makes $\sum_{j = 1}^{n}{\lbrack{y_{j}^{i} - {f{(s_{j},a_{j}^{1},\cdots,a_{j}^{N})}}}\rbrack}^{2}$ convex for each $i$. This is indeed the case if $\mathcal{F}$ is a linear function class. Nevertheless, with only a finite iteration of distributed optimization algorithms (common in practice), agents may not reach exact consensus, leading to an error of each agent's Q-function estimate away from the actual optimum of (4.3). Such an error also exists when nonlinear function approximation is used.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Considering this error caused by decentralized computation, we follow the *error propagation* analysis stemming from single-agent batch RL, to establish the finite-sample performance of the proposed algorithms, i.e., how the accuracy of the algorithms output depends on the function class $\mathcal{F}$, the number of samples within each iteration $n$, and the number of iterations $t$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Aside from control, a series of algorithms in this setting focuses on the policy evaluation task only, namely, the critic step of the actor-critic algorithms. With the policy fixed, this task embraces a neater formulation, as the sampling distribution becomes stationary, and the objective becomes convex under linear function approximation. This facilitates the finite-time/sample analyses, in contrast to most control algorithms with only asymptotic guarantees. Specifically, under joint policy $\pi$, suppose each agent parameterizes the value function by a linear function class $\{{{V_{\omega}{(s)}}:={\phi^{\top}{(s)}\omega}}:{\omega \in R^{d}}\}$, where ${\phi{(s)}} \in R^{d}$ is the feature vector at $s \in \mathcal{S}$, and $\omega \in R^{d}$ is the vector of parameters.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

a \middle| s \right.)}P{(\left. s^{\prime} \middle| {s,a} \right.)}}}$. Then, the objective of all agents is to jointly minimize the mean square projected Bellman error (MSPBE) associated with the team-average reward, i.e.,

<!-- chunk {"id": "body-0070", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

where $n$ is the data size, $A_{j},C_{j}$ and $b_{j}^{i}$ are empirical estimates of $A,C$ and $b^{i}:={E{\lbrack{R^{i,\pi}{(s)}\phi{(s)}}\rbrack}}$, respectively, using sample $j$. Note that (4.5) is convex in $\omega$ and concave in ${\{\lambda^{i}\}}_{i \in \mathcal{N}}$. The use of MSPBE as an objective is standard in multi-agent policy evaluation, and the idea of saddle-point reformulation has been adopted. Note that, a variant of MSPBE, named H-truncated $\lambda$-weighted MSPBE, is advocated, in order to control the bias of the solution deviated from the actual mean square Bellman error minimizer.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

With the formulation (4.4) in mind, develops a distributed variant of the gradient TD-based method, with asymptotic convergence established using the ordinary differential equation (ODE) method. In, a double averaging scheme that combines the dynamic consensus and the SAG algorithm has been proposed to solve the saddle-point problem (4.5) with a linear rate. incorporates the idea of variance-reduction, specifically, AVRG, into gradient TD-based policy evaluation. Achieving the same linear rate as, three advantages are claimed: i) data-independent memory requirement; ii) use of eligibility traces; iii) no need for synchronization in sampling. More recently, standard TD learning, instead of gradient-TD, has been generalized to this MARL setting, with special focuses on finite-sample analyses. Distributed TD($0$) is first studied, using the proof techniques originated, which requires a projection on the iterates, and the data samples to be independent and identically distributed (i.i.d.). Furthermore, motivated by the recent progress, finite-time performance of the more general distributed TD($\lambda$) algorithm is provided, with neither projection nor i.i.d.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Policy evaluation for networked agents has also been investigated under the setting of *independent* agents interacting with *independent* MDPs. studies off-policy evaluation based on the importance sampling technique. With no coupling among MDPs, an agent does not need to know the actions of the other agents. Diffusion-based distributed GTD is then proposed, and is shown to convergence in the mean-square sense with a sublinear rate. In, two variants of the TD-learning, namely, GTD2 and TDC, have been designed for this setting, with weak convergence proved by the general stochastic approximation theory, when agents are connected by a time-varying communication network. Note that also considers the independent MDP setting, with the same results established as the actual MARL setting.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Several other learning goals have also been explored for decentralized MARL with networked agents. has considered the *optimal consensus* problem, where each agent over the network tracks the states of its neighbors' as well as a leader's, so that the consensus error is minimized by the joint policy. A policy iteration algorithm is then introduced, followed by a practical actor-critic algorithm using neural networks for function approximation. A similar consensus error objective is also adopted, under the name of *cooperative multi-agent graphical games*. A centralized-critic-decentralized-actor scheme is utilized for developing off-policy RL algorithms.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Decentralized Paradigm with Networked Agents", "weight": 1.0} -->

Communication efficiency, as a key ingredient in the algorithm design for this setting, has drawn increasing attention recently. Specifically, develops Lazily Aggregated Policy Gradient (LAPG), a distributed PG algorithm that can reduce the communication rounds between the agents and a central controller, by judiciously designing communication trigger rules. addresses the same policy evaluation problem as, and develops a hierarchical distributed algorithm by proposing a mixing matrix different from the doubly stochastic one used, which allows unidirectional information exchange among agents to save communication. In contrast, the distributed actor-critic algorithm in reduces the communication by transmitting only one scalar entry of its state vector at each iteration, while preserving provable convergence as.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Partially Observed Model", "weight": 1.0} -->

We complete the overview for cooperative settings by briefly introducing a class of significant but challenging models where agents are faced with partial observability. Though common in practice, theoretical analysis of MARL algorithms in this setting is still relatively scarce, in contrast to the aforementioned fully observed settings. In general, this setting can be modeled by a decentralized POMDP (Dec-POMDP), which shares almost all elements such as the reward function and the transition model, as the MMDP/Markov team model in §2.2.1, except that each agent now only has its local observations of the system state $s$. With no accessibility to other agents' observations, an individual agent cannot maintain a global belief state, the sufficient statistic for decision making in single-agent POMDPs. Hence, Dec-POMDPs have been known to be NEXP-complete, requiring super-exponential time to solve in the worst case.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Partially Observed Model", "weight": 1.0} -->

There is an increasing interest in developing planning/learning algorithms for Dec-POMDPs. Most of the algorithms are based on the *centralized-learning-decentralized-execution* scheme. In particular, the decentralized problem is first reformulated as a centralized one, which can be solved at a central controller with (a simulator that generates) the observation data of all agents. The policies are then optimized/learned using data, and distributed to all agents for execution. Finite-state controllers (FSCs) are commonly used to represent the local policy at each agent, which map local observation histories to actions. A Bayesian nonparametric approach is proposed in to determine the controller size of variable-size FSCs. To efficiently solve the centralized problem, a series of *top-down* algorithms have been proposed. In, the Dec-POMDP is converted to *non-observable MDP* (NOMDP), a kind of centralized sequential decision-making problem, which is then addressed by some heuristic tree search algorithms.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Partially Observed Model", "weight": 1.0} -->

As an extension of the NOMDP conversion, convert Dec-POMDPs to *occupancy-state* MDPs (oMDPs), where the occupancy-states are distributions over hidden states and joint histories of observations. As the value functions of oMDPs enjoy the piece-wise linearity and convexity, both tractable planning and value-based learning algorithms have been developed.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Partially Observed Model", "weight": 1.0} -->

To further improve computational efficiency, several sampling-based planning/learning algorithms have also been proposed. In particular, Monte-Carlo sampling with policy iteration and the expectation-maximization algorithm, are proposed in and, respectively. Furthermore, Monte-Carlo tree search has been applied to special classes of Dec-POMDPs, such as multi-agent POMDPs and multi-robot active perception. In addition, policy gradient-based algorithms can also be developed for this centralized learning scheme, with a centralized critic and a decentralized actor. Finite-sample analysis can also be established under this scheme, for tabular settings with finite state-action spaces.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Partially Observed Model", "weight": 1.0} -->

Several attempts have also been made to enable *decentralized learning* in Dec-POMDPs. When the agents share some common information/observations, proposes to reformulate the problem as a centralized POMDP, with the common information being the observations of a *virtual* central controller. This way, the centralized POMDP can be solved individually by each agent. In, the reformulated POMDP has been approximated by finite-state MDPs with exponentially decreasing approximation error, which are then solved by Q-learning. Very recently, has developed a tree-search based algorithm for solving this centralized POMDP, which, interestingly, echoes back the heuristics for solving Dec-POMDPs directly as, but with a more solid theoretical footing. Note that in both, a common random number generator is used for all agents, in order to avoid communication among agents and enable a decentralized learning scheme.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Competitive settings are usually modeled as *zero-sum* games. Computationally, there exists a great barrier between solving two-player and multi-player zero-sum games. In particular, even the simplest three-player matrix games, are known to be PPAD-complete. Thus, most existing results on competitive MARL focus on two-player zero-sum games, with $\mathcal{N} = {\{ 1,2\}}$ and ${R^{1} + R^{2}} = 0$ in Definitions 2.2 and 2.4. In the rest of this section, we review methods that provably find a Nash (equivalently, saddle-point) equilibrium in two-player Markov or extensive-form games. The existing algorithms can mainly be categorized into two classes: value-based and policy-based approaches, which are introduced separately in the sequel.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Similar as in single-agent MDPs, value-based methods aim to find an optimal value function from which the joint Nash equilibrium policy can be extracted. Moreover, the optimal value function is known to be the unique fixed point of a Bellman operator, which can be obtained via dynamic programming type methods.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Similar as the minimax theorem in normal-form/matrix zero-sum games, for two-player zero-sum Markov games with finite state and action spaces, one can define the optimal value function $V^{\ast}:{\mathcal{S}\rightarrow R}$ as

<!-- chunk {"id": "body-0083", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Then (4.6) implies that $V_{\pi^{1, \ast},\pi^{2, \ast}}^{1}$ coincides with $V^{\ast}$ and any pair of policies $\pi^{1}$ and $\pi^{2}$ that attains the supremum and infimum in (4.7) constitutes a Nash equilibrium. Moreover, similar to MDPs, shows that $V^{\ast}$ is the unique solution of a Bellman equation and a Nash equilibrium can be constructed based on $V^{\ast}$. Specifically, for any $V:{\mathcal{S}\rightarrow R}$ and any $s \in \mathcal{S}$, we define

<!-- chunk {"id": "body-0084", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

where $Q_{V}{(s, \cdot, \cdot )}$ can be regarded as a matrix in $R^{{|\mathcal{A}^{1}|} \times {|\mathcal{A}^{2}|}}$. Then we define the Bellman operator $\mathcal{T}^{\ast}$ by solving a matrix zero-sum game regarding $Q_{V}{(s, \cdot, \cdot )}$ as the payoff matrix, i.e., for any $s \in \mathcal{S}$, one can define

<!-- chunk {"id": "body-0085", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

where we use $\text{Value}{( \cdot )}$ to denote the optimal value of a matrix zero-sum game, which can be obtained by solving a linear program. Thus, the Bellman operator $\mathcal{T}^{\ast}$ is $\gamma$-contractive in the $\ell_{\infty}$-norm and $V^{\ast}$ in (4.7) is the unique solution to the Bellman equation $V = {\mathcal{T}^{\ast}V}$. Moreover, letting ${p_{1}{(V)}},{p_{2}{(V)}}$ be any solution to the optimization problem in (4.9), we have that $\pi^{\ast} = {({p_{1}{(V^{\ast})}},{p_{2}{(V^{\ast})}})}$ is a Nash equilibrium specified by Definition 2.3.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Thus, based on the Bellman operator $\mathcal{T}^{\ast}$, proposes the value iteration algorithm, which creates a sequence of value functions ${\{ V_{t}\}}_{t \geq 1}$ satisfying $V_{t + 1} = {\mathcal{T}^{\ast}V_{t}}$ that converges to $V^{\ast}$ with a linear rate. Specifically, we have

<!-- chunk {"id": "body-0087", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

In addition, a value iteration update can be decomposed into the two steps. In particular, letting $\pi^{1}$ be any policy of player $1$ and $V$ be any value function, we define Bellman operator $\mathcal{T}^{\pi^{1}}$ by

<!-- chunk {"id": "body-0088", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

where $Q_{V}$ is defined in (4.8). Then we can equivalently write a value iteration update as

<!-- chunk {"id": "body-0089", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Such a decomposition motivates the policy iteration algorithm for two-player zero-sum games, which has been studied, e.g. for different variants of such Markov games. In particular, from the perspective of player $1$, policy iteration creates a sequence ${\{\mu_{t},V_{t}\}}_{t \geq 0}$ satisfying

<!-- chunk {"id": "body-0090", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

i.e., $V_{t + 1}$ is the fixed point of $\mathcal{T}^{\mu_{t + 1}}$. The updates for player $2$ can be similarly constructed. By the definition in (4.10), the Bellman operator $\mathcal{T}^{\mu_{t + 1}}$ is $\gamma$-contractive and its fixed point corresponds to the value function associated with $(\mu_{t + 1},{\text{Br}{(\mu_{t + 1})}})$, where $\text{Br}{(\mu_{t + 1})}$ is the best response policy of player $2$ when player $1$ adopts $\mu_{t + 1}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Hence, in each step of policy iteration, the player first finds an improved policy $\mu_{t + 1}$ based on the current function $V_{t}$, and then obtains a conservative value function by assuming that the opponent plays the best counter policy $\text{Br}{(\mu_{t + 1})}$. It has been shown in that the value function sequence ${\{ V_{t}\}}_{t \geq 0}$ monotonically increases to $V^{\ast}$ with a linear rate of convergence for turn-based zero-sum Markov games.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Notice that both the value and policy iteration algorithms are model-based due to the need of computing the Bellman operator $\mathcal{T}^{\mu_{t + 1}}$ in (4.11) and (4.12). By estimating the Bellman operator via data-driven approximation, has proposed minimax-Q learning, which extends the well-known Q-learning algorithm for MDPs to zero-sum Markov games. In particular, minimax-Q learning is an online, off-policy, and tabular method which updates the action-value function $Q:{{\mathcal{S} \times \mathcal{A}}\rightarrow R}$ based on transition data ${\{{(s_{t},a_{t},r_{t},s_{t}^{\prime})}\}}_{t \geq 0}$, where $s_{t}^{\prime}$ is the next state following $(s_{t},a_{t})$ and $r_{t}$ is the reward.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

In the $t$-th iteration, it only updates the value of $Q{(s_{t},a_{t})}$ and keeps other entries of $Q$ unchanged. Specifically, we have

<!-- chunk {"id": "body-0094", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

where $\alpha_{t} \in {}$ is the stepsize. As shown, under conditions similar to those for single-agent Q-learning, function $Q$ generated by (4.13) converges to the optimal action-value function $Q^{\ast} = Q_{V^{\ast}}$ defined by combining (4.7) and (4.8). Moreover, with a slight abuse of notation, if we define the Bellman operator $\mathcal{T}^{\ast}$ for action-value functions by

<!-- chunk {"id": "body-0095", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

then we have $Q^{\ast}$ as the unique fixed point of $\mathcal{T}^{\ast}$. Since the target value $r_{t} + {{\gamma \cdot \text{Value}}{\lbrack{Q{(s_{t}^{\prime}, \cdot, \cdot )}}\rbrack}}$ in (4.13) is an estimator of ${({\mathcal{T}^{\ast}Q})}{(s_{t},a_{t}^{1},a_{t}^{2})}$, minimax-Q learning can be viewed as a stochastic approximation algorithm for computing the fixed point of $\mathcal{T}^{\ast}$. Following, minimax-Q learning has been further extended to the function approximation setting where $Q$ in (4.13) is approximated by a class of parametrized functions. However, convergence guarantees for this minimax-Q learning with even linear function approximation have not been well understood.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Such a linear value function approximation also applies to a significant class of zero-sum MG instances with continuous state-action spaces, i.e., linear quadratic (LQ) zero-sum games, where the reward function is quadratic with respect to the states and actions, while the transition model follows linear dynamics. In this setting, Q-learning based algorithm can be guaranteed to converge to the NE.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

To embrace general function classes, the framework of batch RL can be adapted to the multi-agent settings, as in the recent works. As mentioned in §4.1.2 for cooperative batch MARL, each agent iteratively updates the Q-function by fitting least-squares using the target values. Specifically, let $\mathcal{F}$ be the function class of interest and let ${\{{(s_{i},a_{i}^{1},a_{i}^{2},r_{i},s_{i}^{\prime})}\}}_{i \in {\lbrack n\rbrack}}$ be the dataset.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

In such a two-player zero-sum Markov game setting, a finite-sample error bound on the Q-function estimate is established.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Regarding other finite-sample analyses, very recently, has studied zero-sum turn-based stochastic games (TBSG), a simplified zero-sum MG when the transition model is embedded in some feature space and a generative model is available. Two Q-learning based algorithms have been proposed and analyzed for this setting. has proposed algorithms that achieve near-optimal sample complexity for general zero-sum TBSGs with a generative model, by extending the previous near-optimal Q-learning algorithm for MDPs. In the online setting, where the learner controls only one of the players that plays against an arbitrary opponent, has proposed UCSG, an algorithm for the *average-reward* zero-sum MGs, using the principle of optimism in the face of uncertainty. UCSG is shown to achieve a sublinear regret compared to the game value when competing with an arbitrary opponent, and also achieve $\overset{\sim}{O}{({\text{poly}{({1/\epsilon})}})}$ sample complexity if the opponent plays an optimistic best response.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Value-Based Methods", "weight": 1.0} -->

Furthermore, when it comes to zero-sum games with imperfect information, have proposed to transform extensive-form games into normal-form games using the sequence form representation, which enables equilibrium finding via linear programming. In addition, by lifting the state space to the space of belief states, have applied dynamic programming methods to zero-sum stochastic games. Both of these approaches guarantee finding of a Nash equilibrium but are only efficient for small-scale problems. Finally, MCTS with UCB-type action selection rule can also be applied to two-player turn-based games with incomplete information, which lays the foundation for the recent success of deep RL for the game of Go. Moreover, these methods are shown to converge to the minimax solution of the game, thus can be viewed as a counterpart of minimax-Q learning with Monte-Carlo sampling.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Policy-based reinforcement learning methods introduced in §2.1.2 can also be extended to the multi-agent setting. Instead of finding the fixed point of the Bellman operator, a fair amount of methods only focus on a single agent and aim to maximize the expected return of that agent, disregarding the other agents' policies. Specifically, from the perspective of a single agent, the environment is time-varying as the other agents also adjust their policies. Policy based methods aim to achieve the optimal performance when other agents play arbitrarily by minimizing the (external) regret, that is, find a sequence of actions that perform nearly as well as the optimal fixed policy in hindsight. An algorithm with negligible average overall regret is called no-regret or Hannan consistent. Any Hannan consistent algorithm is known to have the following two desired properties in repeated normal-form games. First, when other agents adopt stationary policies, the time-average policy constructed by the algorithm converges to the best response policy (against the ones used by the other agents).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Second, more interestingly, in two-player zero-sum games, when both players adopt Hannan consistent algorithms and both their average overall regrets are no more than $\epsilon$, their time-average policies constitute a $2\epsilon$-approximate Nash equilibrium. Thus, any Hannan consistent single-agent reinforcement learning algorithm can be applied to find the Nash equilibria of two-player zero-sum games via *self-play*. Most of these methods belong to one of the following two families: fictitious play, and counterfactual regret minimization, which will be summarized below.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Fictitious play is a classic algorithm studied in game theory, where the players play the game repeatedly and each player adopts a policy that best responds to the average policy of the other agents. This method was originally proposed for solving normal-form games, which are a simplification of the Markov games defined in Definition 2.2 with $\mathcal{S}$ being a singleton and $\gamma = 0$. In particular, for any joint policy $\pi \in {(\mathcal{A})}$ of the $N$ agents, we let $\pi^{- i}$ be the marginal policy of all players except player $i$. For any $t \geq 1$, suppose the agents have played $\{ a_{\tau}:\}$ in the first $t$ stages.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Here, for any $\epsilon > 0$ and any $\pi \in {(\mathcal{A})}$, we denote by $\text{Br}_{\epsilon}{(\pi^{- i})}$ the $\epsilon$-best response policy of player $i$, which satisfies

<!-- chunk {"id": "body-0105", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

As $t\rightarrow\infty$, the updates in (4.17) can be approximately characterized by a differential inclusion

<!-- chunk {"id": "body-0106", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

which is known as the continuous-time fictitious play. Although it is well known that the discrete-time fictitious play in (4.17) is not Hannan consistent, it is shown in that the continuous-time fictitious play in (4.18) is Hannan consistent. Moreover, using tools from stochastic approximation, various modifications of discrete-time fictitious play based on techniques such as smoothing or stochastic perturbations have been shown to converge to the continuous-time fictitious play and are thus Hannan consistent. As a result, applying these methods with self-play provably finds a Nash equilibrium of a two-player zero-sum normal form game.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Furthermore, fictitious play methods have also been extended to RL settings without the model knowledge. Specifically, using sequence-form representation, has proposed the first fictitious play algorithm for extensive-form games which is realization-equivalent to the generalized weakened fictitious play for normal-form games. The pivotal insight is that a convex combination of normal-form policies can be written as a weighted convex combination of behavioral policies using realization probabilities. Specifically, recall that the set of information states of agent $i$ was denoted by $\mathcal{S}^{i}$. When the game has perfect-recall, each $s^{i} \in \mathcal{S}^{i}$ uniquely defines a sequence $\sigma_{s^{i}}$ of actions played by agent $i$ for reaching state $s^{i}$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Using the notation of realization probability, for any two behavioral policies $\pi$ and $\overset{\sim}{\pi}$ of agent $i$, the sum

<!-- chunk {"id": "body-0109", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

is the mixture policy of $\pi$ and $\overset{\sim}{\pi}$ with weights $\lambda \in {}$ and $1 - \lambda$, respectively. Then, combining (4.16) and (4.19), the fictitious play algorithm in computes a sequence of policies ${\{\pi_{t}\}}_{t \geq 1}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Here, both $\epsilon_{t}$ and $\alpha_{t}$ are taken to converge to zero as $t$ goes to infinity, and we further have ${\sum_{t \geq 1}\alpha_{t}} = \infty$. We note, however, that although such a method provably converges to a Nash equilibrium of a zero-sum game via self-play, it suffers from the curse of dimensionality due to the need to iterate all states of the game in each iteration. For computational efficiency, has also proposed a data-drive fictitious self-play framework where the best-response is computed via fitted Q-iteration for the single-agent RL problem, with the policy mixture being learned through supervised learning. This framework was later adopted by to incorporate other single RL methods such as deep Q-network and Monte-Carlo tree search. Moreover, in a more recent work, has proposed a smooth fictitious play algorithm for zero-sum multi-stage games with simultaneous moves (a special case of zero-sum stochastic games).

<!-- chunk {"id": "body-0111", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Their algorithm combines the actor-critic framework with fictitious self-play, and infers the opponent's policy implicitly via policy evaluation. Specifically, when the two players adopt a joint policy $\pi = {(\pi^{1},\pi^{2})}$, from the perspective of player $1$, it infers $\pi^{2}$ implicitly by estimating ${\overline{Q}}_{\pi^{1},\pi^{2}}$ via temporal-difference learning, where ${\overline{Q}}_{\pi^{1},\pi^{2}}:{{\mathcal{S} \times \mathcal{A}^{1}}\rightarrow R}$ is defined as

<!-- chunk {"id": "body-0112", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

which is the action-value function of player $1$ marginalized by $\pi^{2}$. Besides, the best response policy is obtained by taking the soft-greedy policy with respect to ${\overline{Q}}_{\pi^{1},\pi^{2}}$, i.e.,

<!-- chunk {"id": "body-0113", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

where $\eta > 0$ is the smoothing parameter. Finally, the algorithm is obtained by performing both policy evaluation and policy update in (4.20) simultaneously using two-timescale updates, which ensure that the policy updates, when using self-play, can be characterized by an ordinary differential equation whose asymptotically stable solution is a smooth Nash equilibrium of the game.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Another family of popular policy-based methods is based on the idea of counterfactural regret minimization (CFR), first proposed, which has been a breakthrough in the effort to solve large-scale extensive-form games. Moreover, from a theoretical perspective, compared with fictitious play algorithms whose convergence is analyzed asymptotically via stochastic approximation, explicit regret bounds can be established using tools from online learning, which yield rates of convergence to the Nash equilibrium. Specifically, when $N$ agents play the extensive-form game for $T$ rounds with $\{\pi_{t}:{1 \leq t \leq T}\}$, the regret of player $i$ is defined as

<!-- chunk {"id": "body-0115", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

where the maximum is taken over all possible policies of player $i$. In the following, before we define the notion of counterfactual regret, we first introduce a few notations. Recall that we had defined the reach probability $\eta_{\pi}{(h)}$ in (2.4), which can be factorized into the product of each agent's contribution.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Moreover, as shown in Theorem 3 of, counterfactual regrets defined in (4.23) provide an upper bound for the total regret in (4.21):

<!-- chunk {"id": "body-0117", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

where we let $x^{+}$ denote $\max{\{ x,0\}}$ for any $x \in R$. This bound lays the foundation of counterfactual regret minimization algorithms. Specifically, to minimize the total regret in (4.21), it suffices to minimize the counterfactual regret for each information state, which can be obtained by any online learning algorithm, such as EXP3, Hedge, and regret matching. All these methods ensure that the counterfactual regret is $\mathcal{O}{(\sqrt{T})}$ for all $s \in \mathcal{S}^{i}$, which leads to an $\mathcal{O}{(\sqrt{T})}$ upper bound of the total regret. Thus, applying CFR-type methods with self-play to a zero-sum two-play extensive-form game, the average policy is an $\mathcal{O}{(\sqrt{1/T})}$-approximate Nash equilibrium after $T$ steps.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

In particular, the vanilla CFR algorithm updates the policies via regret matching, which yields that ${\text{Reg}_{T}^{i}{(s)}} \leq {R_{\max}^{i} \cdot \sqrt{A^{i} \cdot T}}$ for all $s \in \mathcal{S}^{i}$, where we have introduced

<!-- chunk {"id": "body-0119", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

One drawback of vanilla CFR is that the entire game tree needs to be traversed in each iteration, which can be computationally prohibitive. A number of CFR variants have been proposed since the pioneering work for improving computational efficiency. For example, combine CFR with Monte-Carlo sampling; propose to estimate the counterfactual value functions via regression; improve the computational efficiency by pruning suboptimal paths in the game tree; analyze the performance of a modification named $\text{CFR}^{+}$, and proposes lazy updates with a near-optimal regret upper bound.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Furthermore, it has been shown recently in that CFR is closely related to policy gradient methods. To see this, for any joint policy $\pi$ and any $i \in \mathcal{N}$, we define the action-value function of agent $i$, denoted by $Q_{\pi}^{i}$, as

<!-- chunk {"id": "body-0121", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

As a result, the advantage actor-critic (A2C) algorithm is equivalent to a particular CFR algorithm, where the policy update rule is specified by the generalized infinitesimal gradient ascent algorithm. Thus, proves that the regret of the tabular A2C algorithm is bounded by ${{|\mathcal{S}^{i}|} \cdot {\lbrack{1 + {A^{i} \cdot {(R_{\max}^{i})}^{2}}}\rbrack} \cdot \sqrt{T}}.$ Following this work, shows that A2C where the policy is tabular and is parametrized by a softmax function is equivalent to CFR that uses Hedge to update the policy. Moreover, proposes a policy optimization method known as exploitability descent, where the policy is updated using actor-critic, assuming the opponent plays the best counter-policy. This method is equivalent to the CFR-BR algorithm with Hedge. Thus, show that actor-critic and policy gradient methods for MARL can be formulated as CFR methods and thus convergence to a Nash equilibrium of a zero-sum extensive-form game is guaranteed.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

In addition, besides fictitious play and CFR methods introduced above, multiple policy optimization methods have been proposed for special classes of two-player zero-sum stochastic games or extensive form games. For example, Monte-Carlo tree search methods have been proposed for perfect-information extensive games with simultaneous moves. It has been shown in that the MCTS methods with UCB-type action selection rules, introduced in §4.2.1, fail to converge to a Nash equilibrium in simultaneous-move games, as UCB does not take into consideration the possibly adversarial moves of the opponent. To remedy this issue, have proposed to adopt stochastic policies and using Hannan consistent methods such as EXP3 and regret matching to update the policies. With self-play, shows that the average policy obtained by MCTS with any $\epsilon$-Hannan consistent policy update method converges to an $\mathcal{O}{({D^{2} \cdot \epsilon})}$-Nash equilibrium, where $D$ is the maximal depth.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Finally, there are surging interests in investigating policy gradient-based methods in *continuous* games, i.e., the games with continuous state-action spaces. With policy parameterization, finding the NE of zero-sum Markov games becomes a nonconvex-nonconcave saddle-point problem in general. This hardness is inherent, even in the simplest linear quadratic setting with linear function approximation. As a consequence, most of the convergence results are *local*, in the sense that they address the convergence behavior around local NE points. Still, it has been shown that the vanilla gradient-descent-ascent (GDA) update, which is equivalent to the policy gradient update in MARL, fails to converge to local NEs, for either the non-convergent behaviors such as limit cycling, or the existence of non-Nash stable limit points for the GDA dynamics. Consensus optimization, symplectic gradient adjustment, and extragradient method have been advocated to mitigate the oscillatory behaviors around the equilibria; while exploit the curvature information so that all the stable limit points of the proposed updates are local NEs.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

Going beyond Nash equilibria, consider gradient-based learning for *Stackelberg equilibria*, which correspond to only the one-sided equilibrium solution in zero-sum games, i.e., either minimax or maximin, as the order of which player acts first is vital in nonconvex-nonconcave problems. introduces the concept of *local minimax* point as the solution, and shows that GDA converges to local minimax points under mild conditions. proposes a two-timescale algorithm where the follower uses a gradient-play update rule, instead of an exact best response strategy, which has been shown to converge to the Stackelberg equilibria. Under a stronger assumption of *gradient dominance*, have shown that nested gradient descent methods converge to the stationary points of the outer-loop, i.e., minimax, problem at a sublinear rate.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Policy-Based Methods", "weight": 1.0} -->

We note that these convergence results have been developed for *general* continuous games with *agnostic* cost/reward functions, meaning that the functions may have various forms, so long as they are *differentiable*, sometimes even *(Lipschitz) smooth*, w.r.t. each agent's policy parameter. For MARL, this is equivalent to requiring differentiability/smoothness of the long-term *return*, which relies on the properties of the game, as well as of the policy parameterization. Such an assumption is generally very restrictive. For example, the Lipschitz smoothness assumption fails to hold globally for LQ games, a special type of MGs. Fortunately, thanks to the special structure of the LQ setting, has proposed several projected nested policy gradient methods that are guaranteed to have *global* convergence to the NE, with convergence rates established. This appears to be the first-of-its-kind result in MARL. The results have then been improved by the techniques in a subsequent work of the authors, which can remove the projection step in the updates, for a more general class of such games. Very recently, also improves the results in independently, with different techniques.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

In stark contrast with the fully collaborative and fully competitive settings, the mixed setting is notoriously challenging and thus rather less well understood. Even in the simplest case of a two-player general sum normal-form game, finding a Nash equilibrium is PPAD-complete. Moreover, has proved that value-iteration methods fail to find stationary Nash or correlated equilibria for general-sum Markov games. Recently, it is shown that vanilla policy-gradient methods avoid a non-negligible subset of Nash equilibria in general-sum continuous games, including the LQ general-sum games. Thus, additional structures on either the games or the algorithms need to be exploited, to ascertain provably convergent MARL in the mixed setting.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

Under relatively stringent assumptions, several value-based methods that extend Q-learning to the mixed setting are guaranteed to find an equilibrium. In particular, has proposed the Nash-Q learning algorithm for general-sum Markov games, where one maintains $N$ action-value functions ${Q_{\mathcal{N}} = {(Q^{1},\ldots,Q^{N})}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow R^{N}}$ for all $N$ agents, which are updated using sample-based estimator of a Bellman operator.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

where $\text{Nash}{\lbrack{Q_{\mathcal{N}}{(s^{\prime}, \cdot )}}\rbrack}$ is the objective value of the Nash equilibrium of the stage game with rewards ${\{{Q_{\mathcal{N}}{(s^{\prime},a)}}\}}_{a \in \mathcal{A}}$. For zero-sum games, we have $Q^{1} = {- Q^{2}}$ and thus the Bellman operator defined in (4.26) is equivalent to the one in (4.14) used by minimax-Q learning. Moreover, establishes convergence to Nash equilibrium under the restrictive assumption that $\text{Nash}{\lbrack{Q_{\mathcal{N}}{(s^{\prime}, \cdot )}}\rbrack}$ in each iteration of the algorithm has unique Nash equilibrium.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

In addition, has proposed the Friend-or-Foe Q-learning algorithm where each agent views the other agent as either a "friend" or a "foe". In this case, $\text{Nash}{\lbrack{Q_{\mathcal{N}}{(s^{\prime}, \cdot )}}\rbrack}$ can be efficiently computed via linear programming. This algorithm can be viewed as a generalization of minimax-Q learning, and Nash equilibrium convergence is guaranteed for two-player zero-sum games and coordination games with a unique equilibrium. Furthermore, has proposed correlated Q-learning, which replaces $\text{Nash}{\lbrack{Q_{\mathcal{N}}{(s^{\prime}, \cdot )}}\rbrack}$ in (4.26) by computing a correlated equilibrium, a more general equilibrium concept than Nash equilibrium. In a recent work, has proposed a batch RL method to find an approximate Nash equilibrium via Bellman residue minimization.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

They have proved that the global minimizer of the empirical Bellman residue is an approximate Nash equilibrium, followed by the error propagation analysis for the algorithm. Also in the batch RL regime, has considered a simplified mixed setting for decentralized MARL: two teams of cooperative networked agents compete in a zero-sum Markov game. A decentralized variant of FQI, where the agents within one team cooperate to solve (4.3) while the two teams essentially solve (4.15), is proposed. Finite-sample error bounds have then been established for the proposed algorithm.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

To address the scalability issue, independent learning is preferred, which, however, fails to converge in general. has proposed *decentralized Q-learning*, a two timescale modification of Q-learning, that is guaranteed to converge to the equilibrium for *weakly acyclic Markov games* almost surely. Each agent therein only observes local action and reward, and neither observes nor keeps track of others' actions. All agents are instructed to use the same stationary *baseline policy* for many consecutive stages, named *exploration phase*. At the end of the *exploration phase*, all agents are *synchronized* to update their baseline policies, which makes the environment stationary for long enough, and enables the convergence of Q-learning based methods. Note that these algorithms can also be applied to the cooperative setting, as these games include Markov teams as a special case.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

For continuous games, due to the general negative results therein, introduces a new class of games, *Morse-Smale games*, for which the gradient dynamics correspond to gradient-like flows. Then, definitive statements on almost sure convergence of PG methods to either limit cycles, Nash equilibria, or non-Nash fixed points can be made, using tools from dynamical systems theory. Moreover, have studied the second-order structure of game dynamics, by decomposing it into two components.The first one, named symmetric component, relates to potential games, which yields gradient descent on some implicit function; the second one, named antisymmetric component, relates to *Hamiltonian games* that follows some conservation law, motivated by classical mechanical systems analysis. The fact that gradient descent converges to the Nash equilibrium of both types of games motivates the development of the Symplectic Gradient Adjustment algorithm that finds *stable fixed points* of the game, which constitute all local Nash equilibria for zero-sum games, and only a subset of local NE for general-sum games.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

provides finite-time local convergence guarantees to a neighborhood of a *stable* local Nash equilibrium of continuous games, in both deterministic setting, with exact PG, and stochastic setting, with unbiased PG estimates. Additionally, has also explored the effects of *non-uniform* learning rates on the learning dynamics and convergence rates. has also considered *general-sum* Stackelberg games, and shown that the same two-timescale algorithm update as in the zero-sum case now converges almost surely to the stable attractors only. It has also established finite-time performance for local convergence to a neighborhood of a stable Stackelberg equilibrium. In complete analogy to the zero-sum class, these convergence results for continuous games do not apply to MARL in Markov games directly, as they are built upon the differentiability/smoothness of the long-term return, which may not hold for general MGs, for example, LQ games. Moreover, most of these convergence results are local instead of global.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

Other than continuous games, the policy-based methods summarized in §4.2.2 can also be applied to the mixed setting via self-play. The validity of such an approach is based a fundamental connection between game theory and online learning -- If the external regret of each agent is no more than $\epsilon$, then their average policies constitute an $\epsilon$-approximate coarse correlated equilibrium of the general-sum normal-form games. Thus, although in general we are unable to find a Nash equilibrium, policy optimization with self-play guarantees to find a coarse correlated equilibrium in these normal-form games.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

The scalability issue in the non-cooperative setting can also be alleviated in the mean-field regime, as the cooperative setting discussed in §4.1.1. For general-sum games, has proposed a modification of the Nash-Q learning algorithm where the actions of other agents are approximated by their empirical average. That is, the action value function of each agent $i$ is parametrized by $Q^{i}{(s,a^{i},\mu_{a^{- i}})}$, where $\mu_{a^{- i}}$ is the empirical distribution of $\{ a_{j}:{ji}\}$. Asymptotic convergence of this mean-field Nash-Q learning algorithm has also been established.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

Besides, most mean-field RL algorithms are focused on addressing the mean-field game model. In mean-field games, each agent $i$ has a local state $s^{i} \in \mathcal{S}$ and a local action $a^{i} \in \mathcal{A}$, and the interaction among other agents is captured by an aggregated effect $\mu$, also known as the *mean-field term*, which is a functional of the empirical distribution of the local states and actions of the agents.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

Specifically, at the $t$-th time step, when agent $i$ takes action $a_{t}^{i}$ at state $s_{t}^{i}$ and the mean-field term is $\mu_{t}$, it receives an immediate reward $R{(s_{t}^{i},a_{t}^{i},\mu_{t})}$ and its local state evolves into $s_{t + 1}^{i} \sim \mathcal{P}{( \cdot |s_{t}^{i},a_{t}^{i},\mu_{t})} \in {(\mathcal{S})}$. Thus, from the perspective of agent $i$, instead of participating in a multi-agent game, it is faced with a time-varying MDP parameterized by the sequence of mean-field terms ${\{\mu_{t}\}}_{t \geq 0}$, which in turn is determined by the states and actions of all agents.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

The solution concept in MFGs is the *mean-field equilibrium*, which is a sequence of *pairs* of policy and mean-field terms ${\{\pi_{t}^{\ast},\mu_{t}^{\ast}\}}_{t \geq 0}$ that satisfy the following two conditions: $\pi^{\ast} = {\{\pi_{t}^{\ast}\}}_{t \geq 0}$ is the optimal policy for the time-varying MDP specified by $\mu^{\ast} = {\{\mu_{t}^{\ast}\}}_{t \geq 0}$, and $\mu^{\ast}$ is generated when each agent follows policy $\pi^{\ast}$. The existence of the mean-field equilibrium for discrete-time MFGs has been studied in and their constructive proofs exhibit that the mean-field equilibrium can be obtained via a fixed-point iteration.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

Specifically, one can construct a sequence of policies and mean-field terms ${\{\pi^{(i)}\}}_{i \geq 0}$ and ${\{\mu^{(i)}\}}_{i \geq 0}$ such that ${\{\pi^{(i)}\}}_{t \geq 0}$ solves the time-varying MDP specified by $\mu^{(i)}$, and $\mu^{({i + 1})}$ is generated when all players adopt policy $\pi^{(i)}$. Following this agenda, various model-free RL methods are proposed for solving MFGs where ${\{\pi^{(i)}\}}_{i \geq 0}$ is approximately solved via single-agent RL such as Q-learning and policy-based methods, with ${\{\mu^{(i)}\}}_{i \geq 0}$ being estimated via sampling.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Mixed Setting", "weight": 1.0} -->

In addition, recently propose fictitious play updates for the mean-field state where we have $\mu^{({i + 1})} = {{{({1 - \alpha^{(i)}})} \cdot \mu^{(i)}} + {\alpha^{(i)} \cdot {\hat{\mu}}^{({i + 1})}}}$, with $\alpha^{(i)}$ being the learning rate and ${\hat{\mu}}^{({i + 1})}$ being the mean-field term generated by policy $\pi^{(i)}$. Note that the aforementioned works focus on the settings with either *finite* horizon or *stationary* mean-field equilibria only. Instead, recent works consider possibly non-stationary mean-field equilibrium in infinite-horizon settings, and develop equilibrium computation algorithms that have laid foundations for model-free RL algorithms.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Application Highlights", "weight": 1.0} -->

In this section, we briefly review the recent empirical successes of MARL driven by the methods introduced in the previous section. In the following, we focus on the three MARL settings reviewed in §4 and highlight four representative and practical applications in each setting, as illustrated in Figure 3.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

One prominent application of MARL is the control of practical multi-agent systems, most of which are cooperative and decentralized. Examples of the scenarios include robot team navigation, smart grid operation, and control of mobile sensor networks. Here we choose unmanned aerial vehicles (UAVs), a recently surging application scenario of multi-agent autonomous systems, as one representative example. Specifically, a team of UAVs are deployed to accomplish a cooperation task, usually without the coordination of any central controller, i.e., in a decentralized fashion. Each UAV is normally equipped with communication devices, so that they can exchange information with some of their teammates, provided that they are inside its sensing and coverage range. As a consequence, this application naturally fits in the decentralized paradigm with networked agents we advocated in §4.1.2, which is also illustrated in Figure 2 (b). Due to the high-mobility of UAVs, the communication links among agents are indeed *time-varying* and fragile, making (online) cooperation extremely challenging. Various challenges thus arise in the context of cooperative UAVs, some of which have recently been addressed by MARL.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

In, the UAVs' optimal links discovery and selection problem is considered. Each UAV $u \in \mathcal{U}$, where $\mathcal{U}$ is the set of all UAVs, has the capability to perceive the local available channels and select a connected link over a common channel shared by another agent $v \in \mathcal{U}$. Each UAV $u$ has its local set of channels $\mathcal{C}_{u}$ with $\mathcal{C}_{u}{\bigcap{\mathcal{C}_{v}\varnothing}}$ for any $u,v$, and a connected link between two adjacent UAVs is built if they announce their messages on the same channel simultaneously.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

Each UAV's local state is whether the previous message has been successfully sent, and its action is to choose a pair $(v,{ch_{u}})$, with $v \in \mathcal{T}_{u}$ and ${ch_{u}} \in \mathcal{C}_{u}$, where $\mathcal{T}_{u}$ is the set of teammates that agent $u$ can reach. The availability of local channels ${ch_{u}} \in \mathcal{C}_{u}$ is modeled as probabilistic, and the reward $\mathcal{R}^{u}$ is calculated by the number of messages that are successfully sent. Essentially, the algorithm in is based on independent Q-learning, but with two heuristics to improve the tractability and convergence performance: by *fractional slicing*, it treats each dimension (fraction) of the action space independently, and estimates the actual Q-value by the average of that for all fractions; by *mutual sampling*, it shares both state-action pairs and a mutual Q-function parameter.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

addresses the problem of *field coverage*, where the UAVs aim to provide a full coverage of an unknown field, while minimizing the overlapping sections among their field of views. Modeled as a Markov team, the overall state $s$ is the concatenation of all local states $s_{i}$, which are defined as its $3$-D position coordinates in the environment. Each agent chooses to either head different directions, or go up and down, yielding $6$ possible actions. A multi-agent Q-learning over the *joint* action space is developed, with linear function approximation. In contrast, focuses on spectrum sharing among a network of UAVs. Under a remote sensing task, the UAVs are categorized into two clusters: the relaying ones that provide relay services and the other ones that gain spectrum access for the remaining ones, which perform the sensing task. Such a problem can be modeled as a *deterministic* MMDP, which can thus be solved by distributed Q-learning proposed, with optimality guaranteed. Moreover, considers the problem of *simultaneous* target-assignment and path-planning for multiple UAVs.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

In particular, a team of UAVs $U_{i} \in \text{U}$, with each $U_{i}$'s position at time $t$ given by $({x_{i}^{U}{(t)}},{y_{i}^{U}{(t)}})$, aim to cover all the targets $T_{j} \in \text{T}$ without collision with the threat areas $D_{i} \in \text{D}$, as well as with other UAVs.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

For each $U_{i}$, a path $P_{i}$ is planned as $P_{i} = {\{{({x_{i}^{U}{}},{y_{i}^{U}{}},\cdots,{x_{i}^{U}{(n)}},{y_{i}^{U}{(n)}})}\}}$, and the length of $P_{i}$ is denoted by $d_{i}$. Thus, the goal is to minimize $\sum_{i}d_{i}$ while the collision-free constraints are satisfied. By penalizing the collision in the reward function, such a problem can be characterized as one with a mixed MARL setting that contains both cooperative and competitive agents. Hence, the MADDPG algorithm proposed in is adopted, with centralized-learning-decentralized-execution.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

Two other tasks that can be tackled by MARL include resource allocation in UAV-enabled communication networks, using Q-learning based method, aerial surveillance and base defense in UAV fleet control, using policy optimization method in a purely centralized fashion.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

Another application of cooperative MARL aims to foster communication and coordination among a team of agents without explicit human supervision. Such a type of problems is usually formulated as a Dec-POMDP involving $N$ agents, which is similar to the Markov game introduced in Definition 2.2 except that each agent cannot observe the state $s \in \mathcal{S}$ and that each agent has the same reward function $\mathcal{R}$. More specifically, we assume that each agent $i \in \mathcal{N}$ receives observations from set $\mathcal{Y}^{i}$ via a noisy observation channel $\mathcal{O}^{i}:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{Y}_{i})}}}$ such that agent $i$ observes a random variable $y^{i} \sim \mathcal{O}^{i}{( \cdot |s)}$ when the environment is at state $s$.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

Note that this model can be viewed as a POMDP when there is a central planner that collects the observations of each agent and decides the actions for each agent. Due to the noisy observation channels, in such a model the agents need to communicate with each other so as to better infer the underlying state and make decisions that maximize the expected return shared by all agents. Let $\mathcal{N}_{t}^{i} \subseteq \mathcal{N}$ be the neighbors of agent $i$ at the $t$-th time step, that is, agent $i$ is able to receive a message $m_{t}^{j\rightarrow i}$ from any agent $j \in \mathcal{N}_{t}^{i}$ at time $t$. Let $I_{t}^{i}$ denote the information agent $i$ collects up to time $t$, which is defined as

<!-- chunk {"id": "body-0151", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

which contains its history collected in previous time steps and the observation received at time $t$. With the information $I_{t}^{i}$, agent $i$ takes an action $a_{t}^{i} \in \mathcal{A}^{i}$ and also broadcasts messages $m_{t}^{i\rightarrow j}$ to all agents $j$ with $i \in \mathcal{N}_{t}^{j}$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

To handle the memory issue, it is common to first embed $I_{t}^{i}$ in a fixed latent space via recurrent neural network (RNN) or Long Short-Term Memory (LSTM) and define the value and policy functions on top of the embedded features. Moreover, most existing works in this line of research adopt the paradigm of centralized learning and utilize techniques such as weight-sharing or attention mechanism to increase computational efficiency. With centralized learning, single-agent RL algorithms such as Q-learning and actor-critic are readily applicable.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Cooperative Setting", "weight": 1.0} -->

In particular, first proposes to tackle the problem of learning to communicate via deep Q-learning. They propose to use two Q networks that govern taking action $a^{i} \in \mathcal{A}$ and producing messages separately. Their training algorithm is an extension of the deep recurrent Q-learning (DRQN), which combines RNN and deep Q-learning. Following, various works have proposed a variety of neural network architectures to foster communication among agents. These works combine single-agent RL methods with novel developments in deep learning, and demonstrate their performance via empirical studies. Among these works, have reported the emergence of computational communication protocols among the agents when the RL algorithm is trained from scratch with text or image inputs. We remark that the algorithms used in these works are more akin to single-agent RL due to centralized learning. For more details overviews of multi-agent communication, we refer the interested readers to Section 6 of and Section 3 of.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Regarding the competitive setting, in the following, we highlight the recent applications of MARL to *the game of Go* and *Texas hold'em poker*, which are archetypal instances of two-player perfect-information and partial-information extensive-form games, respectively.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

The game of Go is a board game played by two competing players, with the goal of surrounding more territory on the board than the opponent. These two players have access to white or black stones respectively, and take turns placing their stones on a $19 \times 19$ board, representing their territories. In each move, a player can place a stone to any of the total $361$ positions on the board that is not already taken by a stone. Once placed on the board, the stones cannot be moved. But the stones will be removed from the board when completely surrounded by opposing stones. The game terminates when neither of the players is unwilling or unable to make a further move, and the winner is determined by counting the area of the territory and the number of stones captured by the players.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

The game of Go can be viewed as a two-player zero-sum Markov game with deterministic state transitions, and the reward only appears at the end of the game. The state of this Markov game is the current configuration of the board and the reward is either one or minus one, representing either a win or a loss, respectively. Specifically, we have ${{r^{1}{(s)}} + {r^{2}{(s)}}} = 0$ for any state $s \in \mathcal{S}$, and ${{r^{1}{(s)}},{r^{2}{(s)}}} \in {\{ 1,{- 1}\}}$ when $s$ is a terminating state, and ${r^{1}{(s)}} = {r^{2}{(s)}} = 0$ otherwise. Let $V_{\ast}^{i}{(s)}$ denote the optimal value function of player $i \in {\{ 1,2\}}$.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Thus, in this case, ${\lbrack{1 + {V^{i}{(s)}}}\rbrack}/2$ is the probability of player $i \in {\{ 1,2\}}$ winning the game when the current state is $s$ and both players follow the Nash equilibrium policies thereafter. Moreover, as this Markov game is turn-based, it is known that the Nash equilibrium policies of the two players are deterministic. Furthermore, since each configuration of the board can be constructed from a sequence of moves of the two players due to deterministic transitions, we can also view the game of Go as an extensive-form game with perfect information. This problem is notoriously challenging due to the gigantic state space. It is estimated in that the size of state space exceeds $10^{360}$, which forbids the usage of any traditional reinforcement learning or searching algorithms.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

A significant breakthrough has been made by the *AlphaGo* introduced, which is the first computer Go program that defeats a human professional player on a full-sized board. AlphaGo integrates a variety of ideas from deep learning and reinforcement learning, and tackles the challenge of huge state space by representing the policy and value functions using deep convolutional neural networks (CNN). Specifically, both the policy and value networks are $13$-layer CNNs with the same architecture, and a board configuration is represented by $48$ features. Thus, both the policy and value networks take inputs of size $19 \times 19 \times 48$. These two networks are trained through a novel combination of supervised learning from human expert data and reinforcement learning from Monte-Carlo tree search (MCTS) and self-play. Specifically, in the first stage, the policy network is trained by supervised learning to predict the actions made by the human players, where the dataset consists of $30$ million positions from the KGS Go server.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

That is, for any state-action pair $(s,a)$ in the dataset, the action $a$ is treated as the response variable and the state $s$ is regarded as the covariate. The weights of the policy network is trained via stochastic gradient ascent to maximize the likelihood function. After initializing the policy network via supervised learning, in the second stage of the pipeline, both the policy and value networks are trained via reinforcement learning and self-play. In particular, new data are generated by games played between the current policy network and a random previous iteration of the policy network. Moreover, the policy network is updated following policy gradient, and the value network aims to find the value function associated with the policy network and is updated by minimizing the mean-squared prediction error. Finally, when playing the game, the current iterates of the policy and value networks are combined to produce an improved policy by lookahead search via MCTS. The actual action taken by AlphaGo is determined by such an MCTS policy. Moreover, to improve computational efficiency, AlphaGo uses an asynchronous and distributed version of MCTS to speed up simulation.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Since the advent of AlphaGo, an improved version, known as AlphaGo Zero, has been proposed. Compared with the vanilla AlphaGo, AlphaGo Zero does not use supervised learning to initialize the policy network. Instead, both the policy and value networks are trained from scratch solely via reinforcement learning and self-play. Besides, instead of having separate policy and value functions share the same network architecture, in AlphaGo Zero, these two networks are aggregated into a single neural network structure.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Specifically, the policy and value functions are represented by ${({p{(s)}},{V{(s)}})} = {f_{\theta}{(s)}}$, where $s \in \mathcal{S}$ is the state which represents the current board, $f_{\theta}$ is a deep CNN with parameter $\theta$, $V{(s)}$ is a scalar that corresponds to the value function, and $p{(s)}$ is a vector which represents the policy, i.e., for each entry $a \in \mathcal{A}$, $p_{a}{(s)}$ is the probability of taking action $a$ at state $s$. Thus, under such a network structure, the policy and value networks automatically share the same low-level representations of the states. Moreover, the parameter $\theta$ of network $f_{\theta}$ is trained via self-play and MCTS.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Specifically, at each time-step $t$, based on the policy $p$ and value $V$ given by $f_{\theta_{t}}$, an MCTS policy $\pi_{t}$ can be obtained and a move is executed following policy $\pi_{t}{(s_{t})}$. Such a simulation procedure continues until the current game terminates. Then the outcome of the $t$-th time-step, $z_{t} \in {\{ 1,{- 1}\}}$, is recorded, according to the perspective of the player at time-step $t$. Then the parameter $\theta$ is updated by following a stochastic gradient step on a loss function $\ell_{t}$, which is defined as

<!-- chunk {"id": "body-0163", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Thus, $\ell_{t}$ is the sum of the mean-squared prediction error of the value function, cross-entropy loss between the policy network and the MCTS policy, and a weight-decay term for regularization. It is reported that AlphaGo Zero has defeated the strongest versions of the previous AlphaGo and that it also has demonstrated non-standard Go strategies that had not been discovered before. Finally, the techniques adopted in AlphaGo Zero has been generalized to other challenging board games. Specifically, proposes the AlphaZero program that is trained by self-play and reinforcement learning with zero human knowledge, and achieves superhuman performance in the games of chess, shogi, and Go.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Another remarkable applicational achievement of MARL in the competitive setting focuses on developing artificial intelligence in the Texas hold'em poker, which is one of the most popular variations of the poker. Texas hold'em is usually played by a group of two or more players, where each player is first dealt with two *private cards* face down. Then five *community cards* are dealt face up in three rounds. In each round. each player has four possible actions -- *check*, *call*, *raise*, and *fold*. After all the cards are dealt, each player who has not folded have seven cards in total, consisting of five community cards and two private cards. Each of these players then finds the best five-card poker hand out of all combinations of the seven cards. The player with the best hand is the winner and wins all the money that the players wager for that hand, which is also known as the *pot*. Note that each hand of Texas hold'em terminates after three rounds, and the payoffs of the player are only known after the hand ends. Also notice that each player is unaware of the private cards of the rest of the players.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Thus, Texas hold'em is an instance of multi-player extensive-form game with incomplete information. The game is called *heads-up* when there are only two players. When both the bet sizes and the amount of allowed raises are fixed, the game is called *limit hold'em*. In the no-limit hold'em, however, each player may bet or raise any amount up to all of the money the player has at the table, as long as it exceeds the previous bet or raise.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

There has been quest for developing superhuman computer poker programs for over two decades. Various methods have been shown successful for simple variations of poker such as Kuhn poker and Leduc hold'em. However, the full-fledged Texas hold'em is much more challenging and several breakthroughs have been achieved only recently. The simplest version of Texas hold'em is *heads-up limit hold'em* (HULHE), which has $3.9 \times 10^{14}$ information sets in total, where a player is required to take an action at each information set. has for the first time reported solving HULHE to approximate Nash equilibrium via $\text{CFR}^{+}$, a variant of counterfactual regret minimization. Subsequently, other methods such as Neural Fictitious Self-Play and Monte-Carlo tree search with self-play have also been adopted to successfully solve HULHE.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Despite these breakthroughs, solving *heads-up no-limit hold'em* (HUNL) with artificial intelligence has remained open until recently, which has more than $6 \times 10^{161}$ information sets, an astronomical number. Thus, in HUNL, it is impossible (in today's computational power) to traverse all information sets, making it inviable to apply $\text{CFR}^{+}$ as. Ground-breaking achievements have recently been made by *DeepStack* and *Libratus*, two computer poker programs developed independently, which defeat human professional poker players in HUNL for the first time. Both of these programs adopt CFR as the backbone of their algorithmic frameworks, but adopt different strategies for handling the gigantic size of the game. In particular, DeepStack applies deep learning to learn good representations of the game and proposes *deep counterfactual value networks* to integrate deep learning and CFR.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Moreover, DeepStack adopts limited depth lookahead planning to reduce the gigantic $6 \times 10^{161}$ information sets to no more than $10^{17}$ information sets, thus making it possible to enumerate all information sets. In contrast, *Libratus* does not utilize any deep learning techniques. Instead, it reduces the size of the game by computation of an abstraction of the game, which is possible since many of the information sets are very similar. Moreover, it further reduces the complexity by using the sub-game decomposition technique for imperfect-information games and by constructing fine-grained abstractions of the sub-games. When the abstractions are constructed, an improved version of the Monte-Carlo CFR is utilized to compute the policy. Furthermore, very recently, based upon *Libratus*, has proposed *Pluribus*, a computer poker program that has been shown to be stronger than top human professionals in no-limit Texas hold'em poker with six players.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

The success of Pluribus is attributed to the following techniques that have appeared in the literature: abstraction and sub-game decomposition for large-scale imperfect-information games, Monte-Carlo CFR, self-play, and depth-limited search.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Competitive Setting", "weight": 1.0} -->

Furthermore, another popular testbed of MARL is the StarCraft II, which is an immensely popular multi-player real-strategy computer game. This game can be formulated as a multi-agent Markov game with partial observation, where each player has only limited information of the game state. Designing reinforcement learning systems for StarCraft II is extremely challenging due to the needs to make decisions under uncertainty and incomplete information, to consider the optimal strategy in the long-run, and to design good reward functions that elicit learning. Since released, both the full-game and sub-game versions of StarCraft II have gained tremendous research interest. A breakthrough in this game was achieved by *AlphaStar*, recently proposed, which has demonstrated superhuman performance in zero-sum two-player full-game StarCraft II. Its reinforcement learning algorithm combines LSTM for the parametrization of policy and value functions, asynchronous actor-critic for policy updates, and Neural Fictitious Self-play for equilibrium finding.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Mixed Settings", "weight": 1.0} -->

Compared to the cooperative and competitive settings, research on MARL under the mixed setting is rather less explored. One application in this setting is multi-player poker. As we have mentioned in §5.2, Pluribus introduced in has demonstrated superhuman performance in six-player no-limit Texas hold'em. In addition, as an extension of the problem of learning to communicate, introduced in §5.1, there is a line of research that aims to apply MARL to tackle learning social dilemmas, which is usually formulated as a multi-agent stochastic game with partial information. Thus, most of the algorithms proposed under these settings incorporate RNN or LSTM for learning representations of the histories experienced by the agent, and the performance of these algorithms are usually exhibited using experimental results; see, e.g. and the references therein.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Mixed Settings", "weight": 1.0} -->

Moreover, another example of the mixed setting is the case where the agents are divided into two opposing teams that play zero-sum games. The reward of a team is shared by each player within this team. Compared with two-player zero-sum games, this setting is more challenging in that both cooperation among teammates and competition against the opposing team need to be taken into consideration. A prominent testbed of this case is the *Dota 2* video game, where each of the two teams, each with five players, aims to conquer the base of the other team and defend its own base. Each player independently controls a powerful character known as the *hero*, and only observes the state of the game via the video output on the screen. Thus, Dota 2 is a zero-sum Markov game played by two teams, with each agent having imperfect information of the game. For this challenging problem, in 2018, *OpenAI* has proposed the *OpenAI Five* AI system, which enjoys superhuman performance and has defeated human world champions in an e-sports game. The algorithmic framework integrates LSTM for learning good representations and proximal policy optimization with self-play for policy learning.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Mixed Settings", "weight": 1.0} -->

Moreover, to balance between effective coordination and communication cost, instead of having explicit communication channels among the teams, OpenAI Five utilizes reward shaping by having a hyperparameter, named "team spirit", to balance the relative importance between each hero's individual reward function and the average of the team's reward function.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Multi-agent RL has long been an active and significant research area in reinforcement learning, in view of the ubiquity of sequential decision-making with multiple agents coupled in their actions and information. In stark contrast to its great empirical success, theoretical understanding of MARL algorithms is well recognized to be challenging and relatively lacking in the literature. Indeed, establishing an encompassing theory for MARL requires tools spanning dynamic programming, game theory, optimization theory, and statistics, which are non-trivial to unify and investigate within one context.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

In this chapter, we have provided a selective overview of mostly recent MARL algorithms, backed by theoretical analysis, followed by several high-profile but challenging applications that have been addressed lately. Following the classical overview, we have categorized the algorithms into three groups: those solving problems that are fully cooperative, fully competitive, and a mix of the two. Orthogonal to the existing reviews on MARL, this chapter has laid emphasis on several new angles and taxonomies of MARL theory, some of which have been drawn from our own research endeavors and interests. We note that our overview should not be viewed as a comprehensive one, but instead as a focused one dictated by our own interests and expertise, which should appeal to researchers of similar interests, and provide a stimulus for future research directions in this general topical area. Accordingly, we have identified the following paramount while open avenues for future research on MARL theory.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Partially observed settings: Partial observability of the system states and the actions of other agents is quintessential and inevitable in many practical MARL applications. In general, these settings can be modeled as a partially observed stochastic game (POSG), which includes the cooperative setting with a common reward function, i.e., the Dec-POMDP model, as a special case. Nevertheless, as pointed out in §4.1.3, even the cooperative task is NEXP-complete and difficult to solve. In fact, the information state for optimal decision-making in POSGs can be very complicated and involve belief generation over the opponents' policies, compared to that in POMDPs, which requires belief on only states. This difficulty essentially stems from the heterogenous beliefs of agents resulting from their own observations obtained from the model, an inherent challenge of MARL mentioned in §3 due to various information structures. It might be possible to start by generalizing the centralized-learning-decentralized-execution scheme for solving Dec-POMDPs to solving POSGs.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Deep MARL theory: As mentioned in §3.3, using deep neural networks for function approximation can address the scalability issue in MARL. In fact, most of the recent empirical successes in MARL result from the use of DNNs. Nonetheless, because of lack of theoretical backings, we have not included details of these algorithms in this chapter. Very recently, a few attempts have been made to understand the global convergence of several single-agent deep RL algorithms, such as neural TD learning and neural policy optimization, when overparameterized neural networks are used. It is thus promising to extend these results to multi-agent settings, as initial steps toward theoretical understanding of deep MARL.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Model-based MARL: It may be slightly surprising that very few MARL algorithms in the literature are *model-based*, in the sense that the MARL model is first estimated, and then used as a nominal one to design algorithms. To the best of our knowledge, the only existing model-based MARL algorithms include the early one in that solves single-controller-stochastic games, a special zero-sum MG; and the later improved one, named R-MAX, for zero-sum MGs. These algorithms are also built upon the principle of optimism in the face of uncertainty, as several aforementioned model-free ones. Considering recent progresses in model-based RL, especially its provable advantages over model-free ones in certain regimes, it is worth generalizing these results to MARL to improve its sample efficiency.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Convergence of policy gradient methods: As mentioned in §4.3, the convergence result of vanilla policy gradient method in general MARL is mostly negative, i.e., it may avoid even the local NE points in many cases. This is essentially related to the challenge of non-stationarity in MARL, see §3.2. Even though some remedies have been advocated to stabilize the convergence in *general continuous* games, these assumptions are not easily verified/satisfied in MARL, e.g., even in the simplest LQ setting, as they depend not only on the model, but also on the policy parameterization. Due to this subtlety, it may be interesting to explore the (global) convergence of policy-based methods for MARL, probably starting with the simple LQ setting, i.e., general-sum LQ games, in analogy to that for the zero-sum counterpart. Such an exploration may also benefit from the recent advances of nonconvex-(non)concave optimization.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

MARL with robustness/safety concerns: Concerning the challenge of non-unique learning goals in MARL (see §3.1), we believe it is of merit to consider robustness and/or safety constraints in MARL. To the best of our knowledge, this is still a relatively uncharted territory. In fact, safe RL has been recognized as one of the most significant challenges in the single-agent setting. With more than one agents that may have conflicted objectives, guaranteeing safety becomes more involved, as the safety requirement now concerns the coupling of all agents. One straightforward model is constrained multi-agent MDPs/Markov games, with the constraints characterizing the safety requirement. Learning with provably safety guarantees in this setting is non-trivial, but necessary for some safety-critical MARL applications as autonomous driving and robotics. In addition, it is also natural to think of robustness against adversarial agents, especially in the decentralized/distributed cooperative MARL settings as, where the adversary may disturb the learning process in an anonymous way -- a common scenario in distributed systems. Recent development of robust distributed supervised-learning against Byzantine adversaries may be useful in this context.
