<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

When Simple Exploration Is Sample Efficient: Identifying Sufficient Conditions for Random Exploration to Yield PAC RL Algorithms

Topics include Reinforcement learning, Benchmarks, Sample complexity, Learning, Efficient.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Efficient exploration is one of the key challenges for reinforcement learning (RL) algorithms. Most traditional sample efficiency bounds require strategic exploration. Recently many deep RL algorithms with simple heuristic exploration strategies that have few formal guarantees, achieve surprising success in many domains. These results pose an important question about understanding these exploration strategies such as e-greedy, as well as understanding what characterize the difficulty of exploration in MDPs. In this work we propose problem specific sample complexity bounds of Q learning with random walk exploration that rely on several structural properties. We also link our theoretical results to some empirical benchmark domains, to illustrate if our bound gives polynomial sample complexity in these domains and how that is related with the empirical performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

An important challenge for reinforcement learning is to balance exploration and exploitation. There have been many strategic exploration algorithms, yet many of the recent successes in deep reinforcement learning rely on algorithms with simple exploration mechanisms. While some of these approaches also require many samples, this still highlights an important question: when is exploration easy? In particular, we consider when a simple approach of random exploration followed by greedy exploitation can enable a strong efficiency criteria, Probably Approximately Correct (PAC): that on all but a number of sample that scales as a polynomial function of the domain, the algorithm will take near-optimal actions. Random exploration followed by greedy exploitation approach is related to popular $e$-greedy methods: it can be viewed as a particular thresholding decay schedule in $e$-greedy methods: $e$ is initially set to 1, and then dropped to 0 after a fixed number of steps. This simplification enables us to focus on when random exploration can still be efficient, and there are many domains where having a fixed budget for exploration is reasonable where our analysis will directly apply. Most prior work on formal analysis of exploration before exploitation approach focused on strategic exploration during the exploration phase.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, to our knowledge our work is the first to consider under what conditions random action selection during the exploration phase might still be sufficient to enable provably sample efficient reinforcement learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some restrictions on the decision process are needed: there exist challenging Markov decision processes where relying on random exploration will require an exponential bound (in the MDP parameters) on the sample complexity, in contrast to the polynomial dependence required for the algorithm to be PAC. In some such domains, like the combination lock setting), any greedy actions will (for a very long time) cause the agent to undo productive exploration towards finding the optimal policy, and therefore $\epsilon$-greedy (for any $\epsilon$) will be no better and likely worse than random exploration, and therefore will also not have PAC performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rather than focusing on new algorithmic contributions, in this paper we seek to explore sufficient conditions on the domains that ensure that random exploration then exploitation methods will quickly lead to high performance, as formalized by satisfying the PAC criteria. Our work is related to recent work which considered structural properties of Markov decision processes that bound the loss when performing shallow planning: in contrast to their work, our work focused on the structural properties of MDPs that enable simple exploration to quickly enable good performance during learning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As our main contribution, we introduce new structural properties of MDPs, and prove that when these parameters scales with a polynomial function of the domain parameters, then a random explore then exploit approach is PAC. Our key properties are $\phi{(s)}$, a state's stationary occupancy distribution under random walk, and eigenvalues of a graph Laplacian. Though making an assumption of the occupancy distribution under a random walk might seem to be presuming the conclusion, we note that this assumption only applies to the asymptotic, stationary distribution but our result yields finite sample bounds. Our result relies on some key results about convergence of a lazy random walk on directed graph in Chung. We also show that if a domain exhibits a property we term locally symmetric actions then it immediately satisfies the desired stationary criteria. That basically means for any two states there is a symmetric bijection between actions leading to the other state. A number of common simulation domains or slight variants of, including grid worlds, 4 rooms, and Taxi, satisfy this criteria. Following from this property, our work also yields some insights into why certain popular Atari domains have been observed to be feasible with simple e-greedy exploration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some conditions that are known to enable efficient exploration under more strategic exploration algorithms, such as finite diameter domains, are not sufficient for a random exploration then exploit algorithm to be PAC, and we frame a classic domain, chain, as such an example. Our results also illustrate the difficulty of other similar "trapdoor" domains, including Montezuma's Revenge which has been notoriously challenging for many deep RL agents. We also discuss several other properties that have been proposed to help characterize the learning complexity of MDPs and their relation to our proposed criteria.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, our results help to characterize the properties of an environment that make exploration hard or easy, a critical problem in RL. We hope these properties might help guide practitioners in their algorithm selection, and also advance our understanding about whether and when strategic exploration is needed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

The optimality of the greedy policy in various settings has been previously studied for significantly more restricted settings. Bastani et al. prove that a greedy policy can achieve the optimal asymptotic regret for a two-armed contextual bandit, which could be viewed as a special case of episodic reinforcement learning, as long as the contexts are i.i.d. and the distribution of contexts are diverse enough. That implies a case in contextual bandit where the greedy strategy is enough to solve the exploration problem. Karush and Dear shows that under MDP structures, a greedy strategy is optimal, eliminating the need to plan ahead. Our work focuses on the random walk side of explore-greedy and yields a polynomial sample complexity bound under more mild assumptions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Similarly, if the $Q$-functions are initialized extremely optimistically, $O{(\frac{V_{\max}}{\Pi_{i = 1}^{T}{({1 - \alpha_{i}})}})}$ where $\alpha_{i}$ is learning rate and $T$ is the samples we need to learn a near optimal $Q$ function, then greedy-only $Q$-learning is PAC. However, such a high optimism value (far higher than the possible achieve value) will result in an extremely aggressive exploration, further amplifying the problem of theoretically-motivated optimistic approaches in practice.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Maillard et al. propose a notion of hardness for MDPs named as environmental norm. It measures how varied the value function is at the possible next states and on the distribution over next states. They show how this property provides a tighter regret bound for UCRL algorithm. In the settings we consider random walk exploration is not driven by any reward/value observation, but purely depends on transition dynamics. Thus in this work we mainly consider transition-only parameters. In addition, in contrast to their work, we are focused on how structural properties of the MDP enable explore-greedy to be efficient, rather than improving the analysis of strategic exploration algorithms.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our proposed properties, stationary distribution and Laplacian eigenvalues, are related to a couple of other domain properties that have been previously considered. The first is diameter. Finite diameter is assumed for several strategic exploration algorithms such as optimism under uncertainty approaches and PAC analysis. However, in the context of simple random exploration, a diameter that is polynomial with the MDP parameters is necessary but not sufficient. This is illustrated later in our chain example in which the diameter is finite, because there does exist a policy that could traverse between the start and end state in time linear in the state space, but under random walk the number of samples needed to be likely to reach a later state scales exponentially with later states. Our bound use stationary distribution to measure the asymptotic occupancy instead of direct reachability, which is measured by diameter. The second is proto-value functions Mahadevan and Maggioni, which use spectral properties of MDP to design a representation-based policy learning algorithm. Mixing time for MDPs is also a property that is closely related with stationary distribution and our bounds. Previous work about mixing time in MDPs aims at designing strategic exploration algorithm and bounding the complexity of it by mixing time.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

Mixing time for MDPs is a property that is closely related with our bound. Previous work about mixing time in MDPs Kearns and Singh; Brafman and Tennenholtz aim at designing strategic exploration algorithm and bounding the complexity of it by mixing time. Our bound focus on how the simple exploration method works, and we bound this variant of mixing time by other basic parameters as well as stationary distribution and eigenvalues. Our work is also related to classic results about cover time in Markov chains. Some bounds on $\epsilon$-mixing time and relaxation time can also induce a bound on cover time by stationary distribution and Laplacian eigenvalues, but they all focus on reversible chains, which our Theorem 3 does not need.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Covering Length Bound", "weight": 1.0} -->

In this section, we will bound the covering length by the stationary distribution over states for random walk and Laplacian eigenvalues. The stationary distribution characterizes the asymptotic occupancy of states, and reflects asymptotically how good exploration will be. The smallest non-trivial eigenvalue of the Laplacian, is bounded by a geometric property named the Cheeger constant that intuitively measures the bottleneck of stationary random walk flow. These two parameters are both related to the asymptotic behavior of random walk. One natural question is that if we are given that asymptotically random walk can explore well, can we achieve polynomial sample complexity bound for finite sample exploration, and we show that through the following theorem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Covering Length Bound", "weight": 1.0} -->

Given the random walk policy $\pi_{RW}$, we have a transition matrix under this policy, $P_{RW}^{\pi}$, and we can view it as a transition matrix for a directed weighted graph, denoted as $G{(P_{RW}^{\pi})}$. If ${P_{RW}^{\pi}{(u,v)}} > 0$ we say there is an edge from $u$ to $v$ with weight $P_{RW}^{\pi}{(u,v)}$ in $G$. For the rest of this section, we use $G$ and $P$ to refer to this graph and its transition matrix. It is known that for the transition matrix $P$, there is a unique left eigenvector $\phi$ such that ${\phi{(s)}} > 0$ for any $s$ and ${\phiP} = \phi$, ${\|\phi\|}_{1} = 1$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Covering Length Bound", "weight": 1.0} -->

This eigenvector $\phi$ is also the stationary state distribution under the random walk policy. We follow the definition of graph Laplacian for a directed graph $G$ proposed by Chung: where $\Phi$ is a diagonal matrix with entries ${\Phi{(s,s)}} = {\phi{(s)}}$. Usually the graph Laplacian is only defined on undirected graph, and the intuition in is that take the average of transition matrix $P$ and its transpose to define an undirected graph, then normalized the transition matrix, to introduce the Laplacian for weighted directed graph. The smallest eigenvalue of Laplacian $\mathcal{L}$ is zero. Let $\lambda$ be the smallest non-zero eigenvalue. In the following theorem, we will bound the covering time of random walk policy by the eigenvalues of $\mathcal{L}$ and the stationary distribution $\phi$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Our investigation was inspired by the recent empirical successes of deep reinforcement learning which relied on simple exploration mechanisms, and we hope that our theoretical analysis will both predict the hardness of domains that have been specifically constructed to require strategic exploration, as well add further insight into the hardness of other domains. In this section, we illustrate how our approach can explain some of the ease of exploration in some popular domains, as well as the hardness of exploration in others.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Grid World: Grid world is a group of navigation domains where we need to control an agent to walk in a grid world, collect reward, avoid walls and holes. Most grid worlds with deterministic or other typical action settings have locally symmetric actions. Under this condition, random walk over the grid world is equivalent to a random walk on an undirected graph. Thus ${1/\phi_{\min}} = {O{({SA})}}$ and it is a polynomial function of MDP parameters.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Taxi: Taxi is a 5x5 gridworld. A passenger starts at one of the 4 locations marked in a grid world, and its destination is randomly chosen from one of the 4 locations. The taxi starts randomly on any square, and the goal is to pickup or dropoff the passenger. This domain, as well as the two room example we discussed previously, are widely used testing domains in the hierarchical RL literature, since options/modular policy are expected to achieve more efficient exploration than primitive actions. It is also equivalent with undirected graphs following from the property of locally symmetric actions, if picking up/dropping off are not invertible actions. In that case, our bounds implies that random walk could learn the optimal value function of these domains efficiently.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Pong: Pong is one of the Atari games that is relatively easy for DQN with $e$-greedy. In this domain, one plays pong with a computer player by moving the padder in $y$ axis, hitting the ball back. Interestingly, we can approximately view Pong as satisfying the property of locally symmetric actions by considering a state abstraction. In Pong, the angle of reflection is a bijection function of the hitting position on the paddle, not of angle of incidence, which implies that we could achieve any possible reflection angle in the possible angle domain by proper action. Consider a game state abstraction that consists only of the last ball incidence angle $\theta$ to the agent's paddle. That means, we view all frames after the ball leaves paddle until another hitting as the same state. This makes several notable simplifications, ignoring: the ball's velocity, boundary^22^2Actually the boundary case could be treated by mirror reflection transformation. We would view the whole game as a mirror version of playing in the extended space, after hitting the boundary..

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Since we are playing in a boundless field, it is reasonable to view balls with different $y$ coordinates of hitting position as the same state. For simplicity we also assume the agent's opponent executes a deterministic policy that only depends on incidence angle, so that the mapping from incidence angle to reflection angle is a bijection, denoted as $f$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Under these settings, we can show Pong has the locally symmetric actions. For any state $\theta_{1}$, if we execute an action $a_{1}$ so that the reflection angle is $\theta_{1}^{'}$, then the next state, which is the angle after the computer opponent takes an action would be $\theta_{2} = {f{(\theta_{1}^{'})}}$. For this state, there exist an action $a_{2}$ such that the reflection angle is $f^{- 1}{(\theta_{1})}$. Since the mapping from action to reflection angle and $f$ are both bijection, the mapping between $a_{1}$ and $a_{2}$ is also bijection. Thus we could say random walk in a proper abstracted state space of Pong is equivalent with random walk on an undirected graph, and then yields polynomial sample complexity. That may intuitively explain the success of $e$-greedy in this domain.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Chain MDP: The chain MDP has been previously introduced to motivated the need for strategic exploration. The MDP has n+1 states, the start state is the leftmost state $s_{0}$, and at each state $s_{i}$ there are 2 deterministic actions, one is going right to $s_{i + 1}$ (except the right end states $s_{n}$ which has a self loop action) and the other is going back to $s_{0}$. $Q$ learning with $e$-greedy or random walk does poorly in this example. It takes $\Theta{(2^{n})}$ samples in expectation to visit the right end state for one time, resulting in an exponential sample complexity. That matches what we can learn from our bound: The stationary distribution of random walk on state $s_{i}$ is $\Theta{(\frac{1}{2^{i}})}$, and $1/\phi_{\min}$ is $\Theta{(2^{S})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical Bounds and Links to Empirical Results", "weight": 1.0} -->

Montezuma's Revenge: Montezuma's Revenge is a relatively hard game among different Atari 2600 games for DQN with $e$-greedy exploration. This game requires the player to navigate the explorer through several rooms. The explorer may die on the way of traps are triggered. We note that Montezuma's Revenge has a mechanism which brings one back to the start point after death. At a high level, that "trapdoor" structure is captured by the chain MDP example, and will result in an exponentially small stationary distribution of the end point. Game domains, even at a high level, may have more than one chain, but $\phi_{\min}$ could still be exponential in the maximum chain length. Note that some games like Pong or Enduro also have the restart mechanism, but that restart point is distributed more uniformly over the whole state space. This breaks the chain property and will not result in an exponentially small stationary distribution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we present several structural properties of MDPs that give upper bound on the sample complexity of $Q$ learning with random exploration followed by exploitation. We also link these properties to some conceptual testing domains as well as empirical benchmark domains, towards understanding the recent empirical success. We hope the knowledge of these properties might help guide practitioners in selecting exploration strategy, and understanding whether and when strategic exploration is necessary.
