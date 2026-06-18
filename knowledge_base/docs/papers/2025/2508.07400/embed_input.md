<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Reward Identification in Max Entropy Reinforcement Learning with Sparsity and Rank Priors

Topics include Rank minimization, Convex relaxation, Reinforcement learning, Accuracy, Optimization, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we consider the problem of recovering time-varying reward functions from either optimal policies or demonstrations coming from a max entropy reinforcement learning problem. This problem is highly ill-posed without additional assumptions on the underlying rewards. However, in many applications, the rewards are indeed parsimonious, and some prior information is available. We consider two such priors on the rewards: 1) rewards are mostly constant and they change infrequently, 2) rewards can be represented by a linear combination of a small number of feature functions. We first show that the reward identification problem with the former prior can be recast as a sparsification problem subject to linear constraints. Moreover, we give a polynomial-time algorithm that solves this sparsification problem exactly. Then, we show that identifying rewards representable with the minimum number of features can be recast as a rank minimization problem subject to linear constraints, for which convex relaxations of rank can be invoked. In both cases, these observations lead to efficient optimization-based reward identification algorithms. Several examples are given to demonstrate the accuracy of the recovered rewards as well as their generalizability.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Reward identification, or Inverse Reinforcement Learning (IRL), is the problem of learning rewards from data. The premise behind IRL is that the reward function serves as the most succinct representation of an agent's behavior. Learning a reward function from demonstrations allows agents to generalize beyond observed behaviors, infer underlying human intentions, and capture pairwise preferences. However, like many inverse problems, IRL is inherently ill-posed as there may be infinitely many reward functions consistent with the same observed behavior. For instance, suppose an agent moves from location $A$ to location $B$. One possible hypothesis is that the agent likes $B$, but another equally valid hypothesis is that the agent dislikes $A$. Both reward hypotheses are consistent with the observed behavior, highlighting the fundamental ambiguity in IRL.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To address this ambiguity, recent research has shifted toward learning the entire *set* of reward functions that can explain observed behaviors. However, there is generally no consensus on how to select a specific reward function from within this set. The choice is often guided by the requirements of the downstream task or heuristic considerations. For example, Linear Programming IRL and Max Margin IRL select the reward function that makes the demonstrated policy as optimal as possible relative to the next-best alternative, effectively maximizing the opportunity cost---a principle widely studied in economics, where rational agents seek to maximize the value of their chosen actions relative to foregone alternatives. Adversarial IRL aims to find a reward function that generalizes well across environments, often selecting a state-only reward that maximizes transferability. Maximum Entropy IRL selects the reward function that maximizes the likelihood of the observed demonstrations, assuming an entropy-regularized policy model. More recently, introduced a framework for quantitatively selecting the best reward---potentially outside the solution set---based on a given target application.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we study reward identification in finite-horizon settings with time-varying reward functions. This is an important generalization for real-world applications where rewards evolve over time due to changing preferences, environmental conditions, or task requirements. While most prior IRL methods assume static rewards, the dynamic setting makes IRL even more ill-posed, as reward ambiguity can now arise at every time step. Existing approaches for dynamic rewards either impose restrictive parametric assumptions (e.g., Gaussian random walks or generalized linear models ), limiting their expressiveness to predefined reward dynamics, or assume privileged knowledge on the number of underlying reward regimes. Relatedly, learning time-varying objective functions is also considered in the area of inverse optimal control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Building on prior work, we propose a principled framework that systematically incorporates structure-aware priors---such as minimal reward switches and shared feature bases---to resolve ambiguity in time-varying reward identification, enabling flexible yet interpretable reward identification without strong parametric assumptions. Our contributions include a polynomial-time algorithm for recovering minimally switching rewards, a convex relaxation for feature-based reward decomposition, and robustness guarantees under finite-sample policy estimates. Empirical results validate our approach in several gridworld environments, showing improved interpretability and transferability over existing methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Notation", "weight": 1.0} -->

$\mathbb{R}$ and $\mathbb{N}$ are the sets of real and natural numbers respectively. The identity matrix in ${\mathbb{R}}^{n \times n}$ is denoted by $\mathbf{I}_{n}$. The zero matrix in ${\mathbb{R}}^{m \times n}$ is denoted by $\mathbf{0}_{m \times n}$ ($m$ are $n$ are dropped sometimes when they are clear from context). $\mathbf{1}_{m}$ is the constant vector of ones in ${\mathbb{R}}^{m}$. ${\mathbb{I}}{({x \in X})}$ is the indicator function. Given a matrix $A$, ${rank}{(A)}\text{~and~}{colspan}{(A)}$ denote its rank and column span, respectively.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Notation", "weight": 1.0} -->

When $B$ is another matrix of compatible dimension, $\begin{bmatrix}
\end{bmatrix}$ denotes the horizontal concatenation of $A$ and $B$, and $A \otimes B$ denotes their Kronecker product. Given a vector space $V$ with a basis $B = {\{ v_{1},\cdots,v_{m}\}}$, ${\lbrack w\rbrack}_{B}$ is the vector representation of $w$ in $V$. For a set $S$, $\Delta{(S)}$ denotes the set of probability distributions over it, and $|S|$ denotes its cardinality.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

${r = {{(r_{t})}_{t = 0}^{T - 1}\text{~is a time-varying reward function where each~}r_{t}}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is the reward function at time step $t$; $\gamma \in {\lbrack 0,1\rbrack}$ is a discount factor; and $T \in {\mathbb{N}}$ is the non-negative time horizon.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

An MDP without a reward function, denoted $\mathcal{M} \smallsetminus r$, is called an *MDP model*. A policy $\pi_{t}:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ is a function that describes an agent's behavior at time step $t$ by specifying an action distribution at each state. We denote by $\pi = {(\pi_{t})}_{t = 0}^{T - 1}$ the *time-varying* stochastic policy throughout the entire horizon.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

A trajectory $\tau$ (of length $T$) is an alternating sequence of states and actions (ending with a state), i.e., $\tau = {(s_{0},a_{0},s_{1},a_{1},\ldots,s_{T - 1},a_{T - 1},s_{T})}$ with $s_{t} \in \mathcal{S}$ and $a_{t} \in \mathcal{A}$. Under a policy $\pi$, a trajectory $\tau$ occurs with probability

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

which depends on the distribution of initial states, the policy, and the Markov transition kernel.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

which is known to be unique up-to accessible states.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Markov Decision Processes", "weight": 1.0} -->

with $s \in \mathcal{S}$, $a \in \mathcal{A}$, for $t < {T - 1}$. $V_{t}^{\ast}$ is the optimal soft value function at time step $t$, which is also known as reward-to-go.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Inverse Reinforcement Learning", "weight": 1.0} -->

Inverse reinforcement learning is the problem of inferring a reward function given an agent's actions. Concretely, given an MDP model $\mathcal{M} \smallsetminus r$ and an expert's time-varying policy $\pi^{E}$, the goal is to find a reward function $r$ such that $\pi^{E}$ is the optimal policy for $r$, in other words $r$ *induces* $\pi^{E}$. However, this problem is ill-posed because multiple distinct reward functions can yield the same optimal policy, making reward inference inherently ambiguous. In the case of the Max Entropy RL objective, the set of reward functions that induce a given policy $\pi^{E}$ can be derived in closed form. We present the following result.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM STATEMENTS", "weight": 1.0} -->

By looking at the definition of $\mathcal{R}^{E}$, it should be clear from a simple dimension argument that there exists an infinite number of rewards inducing the same policy $\pi^{E}$. Indeed, the key insight from Lemma ‣ II-C Inverse Reinforcement Learning ‣ II PRELIMINARIES ‣ Efficient Reward Identification In Max Entropy Reinforcement Learning with Sparsity and Rank Priors") is that for any expert policy $\pi^{E}$, one can generate a valid inducing reward $r$ by selecting an appropriate time-dependent value function $\nu$ and computing $r$ via Equation ). Hence, recovering any reward function that induces $\pi^{E}$ is not particularly meaningful. Instead, we are interested in recovering reward functions consistent with prior knowledge we might have about the structure of the reward function. One such prior is to find the time-varying reward function inducing $\pi^{E}$ while having the minimum number of switches. This is particularly important in many real-world settings, where less erratic reward functions enhance interpretability and better reflect underlying task structures (Occam's razor).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given an MDP model $\mathcal{M} \smallsetminus r$ and a time-varying policy $\pi^{E}$, find the reward function $r$ inducing $\pi^{E}$ with the least number of switches, i.e. $r_{t} = r_{t + 1}$ for as many $t$'s as possible.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Another approach is to find a reward function that induces $\pi^{E}$, expressed in terms of a structured basis, commonly referred to in the IRL literature as featurization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 1", "weight": 1.0} -->

where $U \in {\mathbb{R}}^{{mn} \times K}$ is a feature matrix, with each column corresponding to a feature function $u_{k}$, and ${\mathbf{α}}_{\mathbf{t}} = {\lbrack\alpha_{1,t},\ldots,\alpha_{K,t}\rbrack}^{\intercal}$ represents the corresponding feature weights. However, unlike standard IRL settings where the feature matrix $U$ is typically predefined, in our case, $U$ is unknown.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Both problems and can be extended to the setting when only a finite-sample estimate ${\hat{\pi}}^{\text{E}}$ of the expert policy is available, rather than the true policy $\pi^{\text{E}}$. In Section V, we address this practical scenario by introducing robust variants of $\mathcal{R}^{\text{E}}$ that accounts for estimation errors and provides probabilistic guarantees.

<!-- chunk {"id": "body-0021", "role": "body", "section": "METHODOLOGY", "weight": 1.0} -->

for some loss function $\ell:{{\{ r_{0},\cdots,r_{T - 1}\}}\rightarrow{\mathbb{R}}}$. Problem (P) serves as our unifying optimization framework, where domain-specific knowledge is systematically incorporated through tailored loss functions $\ell$, while the constraint ensures consistency with the expert policy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

Problem 1 can be reformulated naturally as a *sparsification problem*, where the objective is to maximize the number of zero entries in an appropriately defined vector-valued sequence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

and consider the sequence ${\{{\Deltar_{t}}\}}_{t = 0}^{T - 2}$. It should be clear that any non-zero element $\Deltar_{t}$ corresponds to a switch in the reward function $r$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

where ${\|{\{{\Deltar_{t}}\}}_{t = 0}^{T - 2}\|}_{0} \triangleq {|{\{ t\mid{{\|{\Deltar_{t}}\|} \neq 0}\}}|}$. While maximizing sparsity is a non-convex and hard to solve problem in general, there exist efficient convex relaxations based on variants of $\ell_{1}$-norm. Moreover, as we show next, thanks to the additional structure in $\mathcal{R}^{E}$, problem (P1) admits an *exact* polynomial-time solution.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

In what follows, we devise a greedy algorithm to solve problem (P1) and prove its correctness.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

Our strategy is to find intervals over which a time-invariant reward can explain the given policy while ensuring consistency with the overall policy. In particular, we do this by working backward in time and iteratively extending an interval until a time-invariant reward is not feasible over this interval and starting a new interval from that point. Algorithm implements this idea by following a bisection approach to find the time step where the time-invariant reward becomes infeasible.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Minimally Switching Rewards", "weight": 1.0} -->

1:Horizon: T, Transition Matrix: P, Policy π
2:Sequence of minimum number of switch times Z and corresponding reward functions R
8: Pick $\overline{r},\overline{\nu}$ from ℛj: τinv (Vτ)
12: Prepend u to Z and $\overline{r}$ to R
13: $V_{t}\leftarrow{{\overline{\nu}}_{t}{\forall t}} \in {\lbrack u,{\tau - 1}\rbrack}$
19:Prepend $\overline{r}$ to R and $V_{t}\leftarrow{{\overline{\nu}}_{t}{\forall t}} \in {\lbrack 0,{\tau - 1}\rbrack}$
Algorithm 1 Greedy Interval Partitioning

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Feature-Based Rewards", "weight": 1.0} -->

If the reward function at time step $t$ is expressed as $r_{t} = {U{\mathbf{α}}_{\mathbf{t}}}$, optimizing over both $U$ and ${\mathbf{α}}_{\mathbf{t}}$ leads to a bilinear optimization problem. Further, since the number of features is unknown, the dimension of $U$ is an additional decision variable. Bilinear programs are generally NP-hard due to their inherent non-convexity, and even checking local optimality can be computationally intractable. Our key insight to avoid solving a bilinear program is that featurization imposes a low-rank structure on the reward function, which remains consistent across the entire horizon. This means that while the reward at each time step may vary, it lies in a subspace spanned by a fixed set of basis functions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Feature-Based Rewards", "weight": 1.0} -->

Consequently, instead of independently optimizing $U$ and ${\mathbf{α}}_{\mathbf{t}}$, we can directly model the reward function as a low-rank matrix, where each column corresponds to the reward at a given time step. By enforcing a low-rank structure on this matrix, we transform the problem into one of recovering a structured representation of rewards rather than solving a bilinear optimization.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Feature-Based Rewards", "weight": 1.0} -->

While Problem (P2) is still a difficult non-convex problem, several heuristics have been developed to handle it, e.g., see. Notably, it has been established that the nuclear norm, under some regularity assumptions, serves as the tightest convex approximation for the rank function, generalizing $\ell_{1}$-norm based relaxation of the $\ell_{o}$-quasinorm to the rank function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Feature-Based Rewards", "weight": 1.0} -->

where for a given matrix $A \in {\mathbb{R}}^{m \times n}$, its nuclear norm ${\| A\|}_{\ast} = {\sum_{i = 1}^{\min{(m,n)}}{\sigma_{i}{(A)}}}$ with $\sigma_{i}$ denoting the singular values of $A$. To get a better approximation of the rank function, nuclear norm relaxation can be further refined by considering an iterative reweighted variant. While we tried this variant in our experiments, the results remained identical to those obtained with the nuclear norm formulation, which was sufficiently accurate for our problem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Given Demonstrations", "weight": 1.0} -->

The set $\mathcal{R}^{E}$ depends on the expert policy through $\Xi^{E}$. However, in practice, the true expert policy $\pi^{E}$ is typically unknown and a finite-sample estimate ${\hat{\pi}}^{E}$ must be used instead. We use the following lemma to motivate our approach in this case.

<!-- chunk {"id": "body-0033", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

How well can our frameworks recover the ground-truth time-varying rewards?

<!-- chunk {"id": "body-0034", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Can our recovered rewards transfer to novel environments?

<!-- chunk {"id": "body-0035", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To answer Q1, we evaluate Problems (P1) and (P2-approx) in the 5x5 gridworld shown in Figure 1(a). Each cell of the gridworld represents a state of the MDP. The actions available for the agent in each state are: $\{{up},{down},{left},{right},{stay}\}$. Upon taking an action, the agent transitions to the desired cell with a probability $1 - p_{w}$, and transitions to a neighboring cell in one of the cardinal directions with a probability $p_{w}$, representing the wind probability. The MDP has two important landmarks: a home state (called $s_{home}$) at the top left, and a water state (called $s_{water}$) in the bottom middle. For example, an agent with high reward at the home state tries to reach the home as fast as possible. An agent with a uniform reward everywhere tries to explore the environment equally. By varying the rewards over time, we can capture and model a multitude of complex behaviors. For example, the agent might want to explore the environment at first.

<!-- chunk {"id": "body-0036", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

During exploration it gets "thirsty", and thus the reward switches to reach the water state as fast as possible. Eventually, the agent wants to go back to the home state. A horizon of $50$ timesteps is used in all our experiments. Our frameworks improve over other baselines in qualitatively recovering the ground-truth weights and feature functions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To answer Q2, we evaluate our frameworks in a transfer learning setting, where the reward function is learned in the gridworld of Figure 1(a), but optimized in a different gridworld with different dynamics, shown in Figures 1(b) and 1(c). The difference in the dynamics is characterized by adding blockings, shown as a dashed line, and adding "sticky" states, shown in yellow, where all actions result in staying in that state with a probability $0.8$. We show that rewards learned with our algorithms still produce optimal or near-optimal behaviors, while baseline methods produce either lower quality policies or rewards that generalize poorly.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Experiment 1: Minimally Switching Rewards", "weight": 1.0} -->

In this experiment, we evaluate the performance of Algorithm. We construct tasks by dividing the time horizon into $k + 1$ intervals, where $k = 5$ switch points are chosen uniformly at random. These switch points correspond to time steps where ${\Deltar_{t}} \neq 0$. We begin with a time-invariant reward function, with values sampled uniformly between 0 and 1, for the first interval. For each interval, we generate a time-invariant reward function by perturbing the previous interval's reward using a uniformly sampled perturbation from ${\lbrack 0,\beta\rbrack}^{mn}$. We vary $\beta$ from 0.1 to 0.4 for each subsequent interval to induce reward changes of increasing magnitudes.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-A Experiment 1: Minimally Switching Rewards", "weight": 1.0} -->

To evaluate the accuracy of the inferred switch times, we consider the resulting intervals as clusters. The predicted intervals are evaluated against the true interval partitioning using the Adjusted Rand Index (ARI), as defined in Equation 5 of. The ARI is a widely used measure for comparing two clusterings: it equals 1 when they agree perfectly and has an expected value of 0 under random labeling (with possible negative values if agreement is worse than chance).

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Experiment 1: Minimally Switching Rewards", "weight": 1.0} -->

To study the impact of using a finite-sample estimate of the policy $\pi^{E}$, we compute the ARI scores of the switch times identified by Algorithm when run on estimates of $\pi^{E}$ obtained from varying numbers of trajectories. The experiment is repeated with 10 different reward functions. We report the mean and standard deviation of the ARI scores for each setting in Table I. As seen in Table I, increasing the number of trajectories leads to higher ARI scores and reduced variance. Our algorithm eventually recovers the true switching times. It is important to observe that the number of switches our algorithm identifies is always less than or equal to the true number of switches, hence our algorithm is able to explain the data with a simpler reward model when there is more uncertainty in the low-data regime.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Experiment 2: Feature-Based Rewards", "weight": 1.0} -->

For this experiment, we generated two ground-truth feature functions ${u_{1},u_{2}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ representing the home state and water state positions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Experiment 2: Feature-Based Rewards", "weight": 1.0} -->

where $u_{1}{(s,.)} = 1$ if $s = s_{home}$, and $0$ otherwise. Similarly, $u_{2}{(s,.)} = 1$ if $s = s_{water}$, and $0$ otherwise. We generate the time-varying weights ${\mathbf{α}}_{\mathbf{t}}$ following a Gaussian random walk as. After finding the expert policy $\pi^{E}$, we solve (P2-approx) to find both the feature functions and the weights. The recovered time-varying weights are shown in Figure, which also includes results with policies esimated from demonstrations. The recovered feature functions^11^1Since the feature vectors are ${|\mathcal{S}|} \times {|\mathcal{A}|}$ dimensional vectors, we only show the first $|\mathcal{S}|$ components, which correspond to the first action. The plots are the same for the remaining actions. are shown in Figures and. As a benchmark, we implemented the dynamic IRL method.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Experiment 2: Feature-Based Rewards", "weight": 1.0} -->

We note that the number of demonstrations fed to the method is much fewer than what our method used due to scalability issues with the former. Since the reward decomposition in (IV-B) is not unique, there exists infinitely many valid choices of basis vectors $U$, leading to different recovered parameters for each basis choice. Thus, to qualitatively compare the ground-truth and recovered weights, and generate meaningful visualizations, we apply a two-step post-processing approach. First, we identify a basis $U$ that satisfies the condition in (IV-B). We then perform a projection step to align this basis with the ground-truth feature vectors, yielding a transformed basis $U^{\prime}$. Next, we express the recovered weights relative to $B^{\prime}$ and apply a standardization step to eliminate trivial invariances due to shifting and scaling. This ensures that the recovered weights are comparable to the ground-truth while preserving their relative structure. Figures and compare our recovered feature mapping with that of. By enforcing a low-rank decomposition in the objective function, our method successfully recovers the true feature functions, whereas dynamic IRL produces a reasonable but noisier approximation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Experiment 2: Feature-Based Rewards", "weight": 1.0} -->

For our transferability experiments, we implemented an additional baseline: the finite-horizon MaxEnt IRL of, which recovers a time-invariant reward. To assess transferability, we first solve for the reward function using different methods/baselines with the optimal ground-truth policy in the Open Gridworld as input. We then compute the optimal policies of these recovered rewards in the novel environments, namely the Blocked Gridworld and the Sticky Gridworld. We report the negative log-likelihood of a sample trajectory set, generated from the optimal policy for the ground-truth reward, for each of the computed policies. We report these log-likelihoods in Table II. Our algorithm achieves near-optimal performance in both novel environments, attaining the best transferability performance among all methods. It is worth mentioning that the Gaussian random walk structure of the weights is embedded in the learning algorithm of, which we do not assume in our approach. Also, finite-horizon MaxEnt IRL baseline is given the true feature function. Finally, both and produce state-only reward functions, which are usually more suited for transferability tasks.

<!-- chunk {"id": "body-0045", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we addressed the challenge of reward identification in finite-horizon, time-varying settings by introducing a unifying framework that incorporates sparsity and rank priors. Our approach efficiently recovers minimally switching rewards through a greedy interval partitioning algorithm and leverages low-rank matrix approximations to identify structured feature-based rewards. Empirical results on several gridworld environments demonstrate robustness to policy estimation noise and superior transferability compared to existing methods.
