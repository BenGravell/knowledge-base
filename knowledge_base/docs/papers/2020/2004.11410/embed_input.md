<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Divide-and-Conquer Monte Carlo Tree Search for Goal-Directed Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Standard planners for sequential decision making (including Monte Carlo planning, tree search, dynamic programming, etc.) are constrained by an implicit sequential planning assumption: The order in which a plan is constructed is the same in which it is executed. We consider alternatives to this assumption for the class of goal-directed Reinforcement Learning (RL) problems. Instead of an environment transition model, we assume an imperfect, goal-directed policy. This low-level policy can be improved by a plan, consisting of an appropriate sequence of sub-goals that guide it from the start to the goal state. We propose a planning algorithm, Divide-and-Conquer Monte Carlo Tree Search (DC-MCTS), for approximating the optimal plan by means of proposing intermediate sub-goals which hierarchically partition the initial tasks into simpler ones that are then solved independently and recursively. The algorithm critically makes use of a learned sub-goal proposal for finding appropriate partitions trees of new tasks based on prior experience. Different strategies for learning sub-goal proposals give rise to different planning strategies that strictly generalize sequential planning. We show that this algorithmic flexibility over planning order leads to improved results in navigation tasks in grid-worlds as well as in challenging continuous control environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is the first sentence of this paper, but it was not the first one we wrote. In fact, the entire introduction section was actually one of the last sections to be added to this manuscript. The discrepancy between the order of inception of ideas and the order of their presentation in this paper probably does not come as a surprise to the reader. Nonetheless, it serves as a point for reflection that is central to the rest of this work, and that can be summarized as *"the order in which we construct a plan does not have to coincide with the order in which we execute it"*.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most standard planners for sequential decision making problems---including Monte Carlo planning, Monte Carlo Tree Search (MCTS) and dynamic programming---have a baked-in *sequential planning assumption* Browne et al.; Bertsekas et al.. These methods begin at either the initial or final state and then proceed to plan actions sequentially forward or backwards in time. However, this sequential approach faces two main challenges. (i) The transition model used for planning needs to be reliable over long horizons, which is often difficult to achieve when it has to be inferred from data. (ii) Credit assignment to each individual action is difficult: In a planning problem spanning a horizon of 100 steps, to assign credit to the first action, we have to compute the optimal cost-to-go for the remaining problem with a horizon of 99 steps, which is only slightly easier than solving the original problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome these two fundamental challenges, we consider alternatives to the basic assumptions of sequential planners in this work. To this end, we focus on goal-directed decision making problems where an agent should reach a goal state from a start state. Instead of a transition and reward model of the environment, we assume a given goal-directed policy (the "low-level" policy) and the associated value oracle that returns the success probability of the low-level policy on any given task. In general, a low-level policy will not be not optimal, e.g. it might be too "myopic" to reliably reach goal states that are far away from its current state. We now seek to improve the low-level policy via a suitable *sequence of sub-goals* that effectively guide it from the start to the final goal, thus maximizing the overall task success probability. This formulation of planning as finding good sub-goal sequences, makes learning of explicit environment models unnecessary, as they are replaced by low-level policies and their value functions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The sub-goal planning problem can still be solved by a conventional sequential planner that begins by searching for the first sub-goal to reach from the start state, then planning the next sub-goal in sequence, and so. Indeed, this is the approach taken in most hierarchical RL settings based on options or sub-goals. However, the credit assignment problem mentioned above still persists, as assessing if the first sub-goal is useful still requires evaluating the success probability of the remaining plan. Instead, it could be substantially easier to reason about the utility of a sub-goal "in the middle" of the plan, as this breaks the long-horizon problem into two sub-problems with much shorter horizons: how to get to the sub-goal and how to get from there to the final goal. Based on this intuition, we propose the Divide-and-Conquer MCTS (DC-MCTS) planner that searches for sub-goals to split the original task into two independent sub-tasks of comparable complexity and then recursively solves these, thereby drastically facilitating credit assignment.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To search the space of intermediate sub-goals efficiently, DC-MCTS uses a heuristic for proposing promising sub-goals that is learned from previous search results and agent experience.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is structured as follows. In Section 2, we formulate planning in terms of sub-goals instead of primitive actions. In Section 3, as our main contribution, we propose the novel Divide-and-Conquer Monte Carlo Tree Search algorithm for this planning problem. In Section 5, we show that it outperforms sequential planners both on grid world and continuous control navigation tasks, demonstrating the utility of constructing plans in a flexible order that can be different from their execution order.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Improving Goal-Directed Policies with Planning", "weight": 1.0} -->

Let $\mathcal{S}$ and $\mathcal{A}$ be finite sets of states and actions. We consider a multi-task setting, where for each episode the agent has to solve a new task consisting of a new Markov Decision Process (MDP) $\mathcal{M}$ over $\mathcal{S}$ and $\mathcal{A}$. Each $\mathcal{M}$ has a single start state $s_{0}$ and a special absorbing state $s_{\infty}$, also termed the goal state. If the agent transitions into $s_{\infty}$ at any time it receives a reward of 1 and the episode terminates; otherwise the reward is 0. We assume that the agent observes the start and goal states $(s_{0},s_{\infty})$ at the beginning of each episode, as well as an encoding vector $c_{\mathcal{M}} \in {\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Improving Goal-Directed Policies with Planning", "weight": 1.0} -->

This vector provides the agent with additional information about the MDP $\mathcal{M}$ of the current episode and will be key to transfer learning across tasks in the multi-task setting. A stochastic, goal-directed policy $\pi$ is a mapping from $\mathcal{S} \times \mathcal{S} \times {\mathbb{R}}^{d}$ into distributions over $\mathcal{A}$, where $\pi{(\left. a \middle| {s,s_{\infty},c_{\mathcal{M}}} \right.)}$ denotes the probability of taking action $a$ in state $s$ in order to get to goal $s_{\infty}$. For a fixed goal $s_{\infty}$, we can interpret $\pi$ as a regular policy, here denoted as $\pi_{s_{\infty}}$, mapping states to action probabilities.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Improving Goal-Directed Policies with Planning", "weight": 1.0} -->

We denote the value of $\pi$ in state $s$ for goal $s_{\infty}$ as $v^{\pi}{(s,\left. s_{\infty} \middle| c_{\mathcal{M}} \right.)}$; we assume no discounting $\gamma = 1$. Under the above definition of the reward, the value is equal to the success probability of $\pi$ on the task, i.e. the absorption probability of the stochastic process starting in $s_{0}$ defined by running $\pi_{s_{\infty}}$: where $\tau_{s_{0}}^{\pi_{s}_{\infty}}$ is the trajectory generated by running $\pi_{s}_{\infty}$ from state $s_{0}$ ^11^1We assume MDPs with multiple absorbing states such that this probability is not trivially equal to 1 for most policies, e.g. uniform policy. In experiments, we used a finite episode length..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Improving Goal-Directed Policies with Planning", "weight": 1.0} -->

To keep the notation compact, we will omit the explicit dependence on $c_{\mathcal{M}}$ and abbreviate tasks with pairs of states in $\mathcal{S} \times \mathcal{S}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Planning over Sub-Goal Sequences", "weight": 1.0} -->

Assume a given goal-directed policy $\pi$, which we also refer to as the low-level policy. If $\pi$ is not already the optimal policy, then we can potentially improve it by planning: If $\pi$ has a low probability of directly reaching $s_{\infty}$ from the initial state $s_{0}$, i.e. ${v^{\pi}{(s_{0},s_{\infty})}} \approx 0$, we will try to find a *plan* consisting of a sequence of intermediate sub-goals such that they guide $\pi$ from the start $s_{0}$ to the goal state $s_{\infty}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Planning over Sub-Goal Sequences", "weight": 1.0} -->

To execute a plan $\sigma$, we construct a policy $\pi_{\sigma}$ by conditioning the low-level policy $\pi$ on each of the sub-goals in order: Starting with $n = 1$, we feed sub-goal $\sigma_{n + 1}$ to $\pi$, i.e. we run $\pi_{\sigma_{n + 1}}$; if $\sigma_{n + 1}$ is reached, we will execute $\pi_{\sigma_{n + 2}}$ and so. We now wish to do *open-loop planning*, i.e. find the plan with the highest success probability $P{({s_{\infty} \in \tau_{s_{0}}^{\pi_{\sigma}}})}$ of reaching $s_{\infty}$. However, this success probability depends on the transition kernels of the underlying MPDs, which might not be known.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Planning over Sub-Goal Sequences", "weight": 1.0} -->

We can instead define planning as maximizing the following lower bound of the success probability, that can be expressed in terms of the low-level value $v^{\pi}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

In the following we cast the planning problem into a representation amenable to efficient search. To this end, we use the natural compositionality of plans: We can concatenate, a plan $\sigma$ for the task $(s,s')$ and a plan $\hat{\sigma}$ for the task $(s',s^{\operatorname{\prime\prime}})$ into a plan $\sigma \circ \hat{\sigma}$ for the task $(s,s^{\operatorname{\prime\prime}})$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

Conversely, we can decompose any given plan $\sigma$ for task $(s_{0},s_{\infty})$ by splitting it at any sub-goal $s \in \sigma$ into $\sigma = {\sigma^{l} \circ \sigma^{r}}$, where $\sigma^{l}$ is the "left" sub-plan for task $(s_{0},s)$, and $\sigma^{r}$ is the "right" sub-plan for task $(s,s_{\infty})$. For an illustration see Figure 1. Trivially, the planning objective and the optimal high-level value factorize wrt. to this decomposition: This allows us to recursively reformulate planning as: The above equations are the Bellman equations and the Bellman optimality equations for the classical single pair shortest path problem in graphs, where the edge weights are given by $- {{\log v^{\pi}}{(s,s')}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

We can represent this planning problem by an AND/OR search tree consisting of alternating levels of OR and AND nodes. An OR node, also termed an *action node*, is labeled by a task ${(s,s^{\operatorname{\prime\prime}})} \in {\mathcal{S} \times \mathcal{S}}$; the root of the search tree is an OR node labeled by the original task $(s_{0},s_{\infty})$. A terminal OR node $(s,s^{\operatorname{\prime\prime}})$ has a value $v^{\pi}{(s,s^{\operatorname{\prime\prime}})}$ attached to it, which reflects the success probability of $\pi_{s^{\operatorname{\prime\prime}}}$ for completing the sub-task $(s,s^{\operatorname{\prime\prime}})$. Each non-terminal OR node has $|\mathcal{S}| + 1$ AND nodes as children.

<!-- chunk {"id": "body-0019", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

Each of these is labeled by a triple $(s,s',s^{\operatorname{\prime\prime}})$ for $s' \in \overline{\mathcal{S}}$, which correspond to inserting a sub-goal $s'$ into the overall plan, or not inserting one in case of $s = \varnothing$. Every AND node $(s,s',s^{\operatorname{\prime\prime}})$, which we will also refer to as a *conjunction node*, has two OR children, the "left" sub-task $(s,s')$ and the "right" sub-task $(s',s^{\operatorname{\prime\prime}})$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

In this representation, plans are induced by *solution trees*. A solution tree $\mathcal{T}_{\sigma}$ is a sub-tree of the complete AND/OR search tree, with the properties that (i) the root ${(s_{0},s_{\infty})} \in \mathcal{T}_{\sigma}$, (ii) each OR node in $\mathcal{T}_{\sigma}$ has at most one child in $\mathcal{T}_{\sigma}$ and (iii) each AND node in $\mathcal{T}_{\sigma}$ as two children in $\mathcal{T}_{\sigma}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "AND/OR Search Tree Representation", "weight": 1.0} -->

The plan $\sigma$ and its objective $L{(\sigma)}$ can be computed from $\mathcal{T}_{\sigma}$ by a depth-first traversal of $\mathcal{T}_{\sigma}$, see Figure 1. The correspondence of sub-trees to plans is many-to-one, as $\mathcal{T}_{\sigma}$, in addition to the plan itself, contains *the order* in which the plan was constructed. Figure 6 in the Appendix shows a example for a search and solution tree. Below we will discuss how to construct a favourable search order heuristic.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Best-First AND/OR Planning", "weight": 1.0} -->

1:Global low-level value oracle vπ 2:Global high-level value function v 3:Global policy prior p 4:Global search tree 𝒯 6:procedure Traverse(OR node (s, s'')) 9: return max (vπ (s, s''), v (s, s'')) ⊳ bootstrap 12: if s′ = ⌀ or max-depth reached then 14: else⊳ AND node 20: G ← max (G, vπ (s, s'')) ⊳ threshold the return Algorithm 1 Divide-and-Conquer MCTS procedures The planning problem from Definition 1. ‣ 2.1 Planning over Sub-Goal Sequences ‣ 2 Improving Goal-Directed Policies with Planning") can be solved exactly by formulating it as shortest path problem from $s_{0}$ to $s_{\infty}$ on a fully connected graph with vertex set $\mathcal{S}$ with non-negative edge weights given by $- {\log v^{\pi}}$ and applying a classical Single Source or All Pairs Shortest Path (SSSP / APSP) planner.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Best-First AND/OR Planning", "weight": 1.0} -->

This approach is appropriate if one wants to solve all goal-directed tasks in a *single* MDP. Here, we focus however on the multi-task setting described above, where the agent is given a new MDP wit a single task $(s_{0},s_{\infty})$ *every* episode. In this case, solving the SSSP / APSP problem is not feasible: Tabulating all graphs weights $- {{\log v^{\pi}}{(s,s')}}$ would require $|\mathcal{S}|^{2}$ evaluations of $v^{\pi}{(s,s')}$ for all pairs $(s,s')$. In practice, approximate evaluations of $v^{\pi}$ could be implemented by e.g. actually running the policy $\pi$, or by calls to a powerful function approximator, both of which are often too costly to exhaustively evaluate for large state-spaces $\mathcal{S}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Best-First AND/OR Planning", "weight": 1.0} -->

Instead, we tailor an algorithm for *approximate planning* to the multi-task setting, which we call Divide-and-Conquer MCTS (DC-MCTS). To evaluate $v^{\pi}$ as sparsely as possible, DC-MCTS critically makes use of two learned search heuristics that transfer knowledge from previously encountered MDPs / tasks to new problem instance: (i) a distribution $p{(\left. s' \middle| {s,s^{\operatorname{\prime\prime}}} \right.)}$, called the policy prior, for proposing promising intermediate sub-goals $s'$ for a task $(s,s^{\operatorname{\prime\prime}})$; and (ii) a learned approximation $v$ to the high-level value $v^{\ast}$ for bootstrap evaluation of partial plans. In the following we present DC-MCTS and discuss design choices and training for the two search heuristics.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Divide-and-Conquer Monte Carlo Tree Search", "weight": 1.0} -->

The input to the DC-MCTS planner is an MDP encoding $c_{\mathcal{M}}$, a task $(s_{0},s_{\infty})$ as well as a planning budget, i.e. a maximum number $B \in {\mathbb{N}}$ of $v^{\pi}$ oracle evaluations. At each stage, DC-MCTS maintains a (partial) AND/OR search tree $\mathcal{T}$ whose root is the OR node $(s_{0},s_{\infty})$ corresponding to the original task. Every OR node ${(s,s^{\operatorname{\prime\prime}})} \in \mathcal{T}$ maintains an estimate ${V{(s,s^{\operatorname{\prime\prime}})}} \approx {v^{\ast}{(s,s^{\operatorname{\prime\prime}})}}$ of its high-level value.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Divide-and-Conquer Monte Carlo Tree Search", "weight": 1.0} -->

DC-MCTS searches for a plan by iteratively constructing the search tree $\mathcal{T}$ with Traverse until the budget is exhausted, see Algorithm 1. During each traversal, if a leaf node of $\mathcal{T}$ is reached, it is expanded, followed by a recursive bottom-up backup to update the value estimates $V$ of all OR nodes visited in this traversal. After this search phase, the currently best plan is extracted from $\mathcal{T}$ by ExtractPlan (essentially depth-first traversal, see Algorithm 2 in the Appendix). In the following we briefly describe the main methods of the search.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Traverse and Select", "weight": 1.0} -->

$\mathcal{T}$ is traversed from the root $(s_{0},s_{\infty})$ to find a promising node to expand. At an OR node $(s,s^{\operatorname{\prime\prime}})$, Select chooses one of its children $s' \in \overline{\mathcal{S}}$ to next traverse into, including $s = \varnothing$ for not inserting any further sub-goals into this branch. We implemented Select by the pUCT Rosin rule, which consists of picking the next node $s' \in \overline{\mathcal{S}}$ based on maximizing the following score: where $N{(s,s')}$, $N{(s,s',s^{\operatorname{\prime\prime}})}$ are the visit counts of the OR node $(s,s')$, AND node $(s,s',s^{\operatorname{\prime\prime}})$ respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Traverse and Select", "weight": 1.0} -->

The first term is the *exploitation* component, guiding the search to sub-goals that currently look promising, i.e. have high estimated value. The second term is the *exploration* term favoring nodes with low visit counts. Crucially, it is explicitly scaled by the policy prior $p{(\left. s' \middle| {s,s^{\operatorname{\prime\prime}}} \right.)}$ to guide exploration. At an AND node $(s,s',s^{\operatorname{\prime\prime}})$, Traverse traverses into both the left $(s,s')$ and right child $(s',s^{\operatorname{\prime\prime}})$.^22^2It is possible to traverse into a single node at the time, we describe several plausible heuristics in Appendix A.3 As the two sub-problems are solved independently, computation from there on can be carried out in parallel. All nodes visited in a single traversal form a solution tree denoted here as $\mathcal{T}_{\sigma}$ with plan $\sigma$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Expand", "weight": 1.0} -->

If a leaf OR node $(s,s^{\operatorname{\prime\prime}})$ is reached during the traversal and its depth is smaller than a given maximum depth, it is expanded by evaluating the high- and low-level values $v{(s,s^{\operatorname{\prime\prime}})}$, $v^{\pi}{(s,s^{\operatorname{\prime\prime}})}$. The initial value of the node is defined as $\max$ of both values, as by definition $v^{\ast} \geq v^{\pi}$, i.e. further planning should only increase the success probability on a sub-task. We also evaluate the policy prior $p{(\left. s' \middle| {s,s^{\operatorname{\prime\prime}}} \right.)}$ for all $s'$, yielding the proposal distribution over sub-goals used in SELECT. Each node expansion costs one unit of budget $B$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Backup and Update", "weight": 1.0} -->

We define the return $G_{\sigma}$ of the traversal tree $\mathcal{T}_{\sigma}$ as follows. Let a refinement $\mathcal{T}_{\sigma}^{+}$ of $\mathcal{T}_{\sigma}$ be a solution tree such that $\mathcal{T}_{\sigma} \subseteq \mathcal{T}_{\sigma}^{+}$, thus representing a plan $\sigma^{+}$ that has all sub-goals of $\sigma$ with additional inserted sub-goals. $G_{\sigma}$ is now defined as the value of the objective $L{(\sigma^{+})}$ of the *optimal* refinement of $\mathcal{T}_{\sigma}$, i.e. it reflects how well one could do on task $(s_{0},s_{\infty})$ by starting from the plan $\sigma$ and refining it.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Backup and Update", "weight": 1.0} -->

It can be computed by a simple back-up on the tree $\mathcal{T}_{\sigma}$ that uses the bootstrap value $v \approx v^{\ast}$ at the leafs. As ${v^{\ast}{(s_{0},s_{\infty})}} \geq G_{\sigma} \geq {L{(\sigma)}}$ and $G_{\sigma^{\ast}} = {v^{\ast}{(s_{0},s_{\infty})}}$ for the optimal plan $\sigma^{\ast}$, we can use $G_{\sigma}$ to update the value estimate $V$. Like in other MCTS variants, we employ a running average operation (line 17-18 in Traverse).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Designing and Training Search Heuristics", "weight": 1.0} -->

Search results and experience from previous tasks can be used to improve DC-MCTS on new problem instances via adapting the search heuristics, i.e. the policy prior $p$ and the approximate value function $v$, in the following way.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Bootstrap Value Function", "weight": 1.0} -->

We parametrize ${v{(s,\left. s' \middle| c_{\mathcal{M}} \right.)}} \approx {v^{\ast}{(s,\left. s' \middle| c_{\mathcal{M}} \right.)}}$ as a neural network that takes as inputs the current task consisting of $(s,s')$ and the MDP encoding $c_{\mathcal{M}}$. A straight-forward approach to train $v$ is to regress it towards the non-parametric value estimates $V$ computed by DC-MCTS on previous problem instances. However, initial results indicated that this leads to $v$ being overly optimistic, an observation also made in Kaelbling. We therefore used more conservative training targets, that are computed by backing the low-level values $v^{\pi}$ up the solution tree $\mathcal{T}_{\sigma}$ of the plan $\sigma$ return by DC-MCTS. Details can be found in Appendix B.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Prior", "weight": 1.0} -->

Best-first search guided by a policy prior $p$ can be understood as policy improvement of $p$ as described in Silver et al.. Therefore, a straight-forward way of training $p$ is to distill the search results back into into the policy prior, e.g. by behavioral cloning. When applying this to DC-MCTS in our setting, we found empirically that this yielded very slow improvement when starting from an untrained, uniform prior $p$. This is due to plans with non-zero success probability $L > 0$ being very sparse in $\mathcal{S}^{\ast}$, equivalent to the sparse reward setting in regular MDPs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Prior", "weight": 1.0} -->

To address this issue, we propose to apply Hindsight Experience Replay (HER, Andrychowicz et al. ): Instead of training $p$ exclusively on search results, we additionally execute plans $\sigma$ in the environment and collect the resulting trajectories, i.e. the sequence of visited states, $\tau_{s_{0}}^{\pi_{\sigma}} = {(s_{0},s_{1},\ldots,s_{T})}$. HER then proceeds with *hindsight relabeling*, i.e. taking $\tau_{s_{0}}^{\pi_{\sigma}}$ as an approximately optimal plan for the "fictional" task $(s_{0},s_{T})$ that is likely different from the actual task $(s_{0},s_{\infty})$. In standard HER, these fictitious expert demonstrations are used for imitation learning of goal-directed policies, thereby circumventing the sparse reward problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Prior", "weight": 1.0} -->

We have considerable freedom in choosing which triplets to extract from data and use as supervision, which we can characterize in the following way. Given a task $(s_{0},s_{\infty})$, the policy prior $p$ defines a distribution over binary partition trees of the task via recursive application (until the terminal symbol $\varnothing$ closes a branch). A sample $\mathcal{T}_{\sigma}$ from this distribution implies a plan $\sigma$ as described above; but furthermore it also contains the order in which the task was partitioned. Therefore, $p$ not only implies a distribution over plans, but also a *search order*: Trees with high probability under $p$ will be discovered earlier in the search with DC-MCTS. For generating training targets for supervised training of $p$, we need to *parse* a given sequence $\tau_{s_{0}}^{\pi_{\sigma}} = {(s_{0},s_{1},\ldots,s_{T})}$ into a binary tree.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Prior", "weight": 1.0} -->

Therefore, when applying HER we are free to chose any deterministic or probabilistic parser that generates a solution tree $\mathcal{T}_{\tau_{s_{0}}^{\pi_{\sigma}}}$ from re-label HER data $\tau_{s_{0}}^{\pi_{\sigma}}$. The particular choice of HER-parser will shape the search strategy defined by $p$. Possible choices include: Left-first parsing creates triplets $(s_{t},s_{t + 1},s_{T})$. The resulting policy prior will then preferentially propose sub-goals close to the start state, mimicking standard forward planning. Analogously right-first parsing results in approximate backward planning; Temporally balanced parsing creates triplets $(s_{t},s_{t + {\Delta/2}},s_{t + \Delta})$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Prior", "weight": 1.0} -->

The resulting policy prior will then preferentially propose sub-goals "in the middle" of the task; Weight-balanced parsing creates triplets $(s,s',s^{\operatorname{\prime\prime}})$ such that $v{(s,s')} \approx v{(s's,^{\operatorname{\prime\prime}})}$ or $v^{\pi}{(s,s')} \approx v^{\pi}{(s's,^{\operatorname{\prime\prime}})}$. The resulting policy prior will attempt to propose sub-goals such that the resulting sub-tasks are equally difficult.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the proposed DC-MCTS algorithm on navigation in grid-world mazes as well as on a challenging continuous control version of the same problem. In our experiments, we compared DC-MCTS to standard sequential MCTS (in sub-goal space) based on the fraction of "solved" mazes by executing their plans. The MCTS baseline was implemented by restricting the DC-MCTS algorithm to only expand the "right" sub-problem in line 11 of Algorithm 1; all remaining parameters and design choice were the same for both planners except where explicitly mentioned otherwise. Videos of results can be found at

<!-- chunk {"id": "body-0040", "role": "body", "section": "Grid-World Mazes", "weight": 1.0} -->

In this domain, each task consists of a new, procedurally generated maze on a 21 $\times$ 21 grid with start and goal locations ${(s_{0},s_{\infty})} \in {\{ 1,\ldots,21\}}^{2}$, see Figure 2. Task difficulty was controlled by the density of walls $d$ (under connectedness constraint), where the easiest setting $d = 0.0$ corresponds to no walls and the most difficult one $d = 1.0$ implies so-called perfect or singly-connected mazes. The task embedding $c_{\mathcal{M}}$ was given as the maze layout and $(s_{0},s_{\infty})$ encoded together as a feature map of 21 $\times$ 21 categorical variables with 4 categories each (empty, wall, start and goal location). The underlying MDPs have 5 primitive actions: up, down, left, right and NOOP.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Grid-World Mazes", "weight": 1.0} -->

For sake of simplicity, we first tested our proposed approach by hard-coding a low-level policy $\pi^{0}$ as well as its value oracle $v^{\pi^{0}}$ in the following way. If in state $s$ and conditioned on a goal $s'$, and if $s$ is adjacent to $s'$, $\pi_{s'}^{0}$ successfully reaches $s'$ with probability 1 in one step, i.e. ${v^{\pi^{0}}{(s,s')}} = 1$; otherwise ${v^{\pi^{0}}{(s,s')}} = 0$. If $\pi_{s'}^{0}$ is nevertheless executed, the agent moves to a random empty tile adjacent to $s$. Therefore, $\pi^{0}$ is the "most myopic" goal-directed policy that can still navigate everywhere.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Grid-World Mazes", "weight": 1.0} -->

For each maze, MCTS and DC-MCTS were given a search budget of 200 calls to the low-level value oracle $v^{\pi^{0}}$. We implemented the search heuristics, i.e. policy prior $p$ and high-level value function $v$, as convolutional neural networks which operate on input $c_{\mathcal{M}}$; details for the network architectures are given in Appendix B.3. With untrained networks, both planners were unable to solve the task (\<2% success probability), as shown in Figure 3. This illustrates that a search budget of 200 evaluations of $v^{\pi^{0}}$ is insufficient for unguided planners to find a feasible path in most mazes. This is consistent with standard exhaustive SSSP / APSP graph planners requiring $21^{4} > 10^{5} \gg 200$ evaluations for optimal planning in the worst case on these tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Grid-World Mazes", "weight": 1.0} -->

Next, we trained both search heuristics $v$ and $p$ as detailed in Section 3.2. In particular, the sub-goal proposal $p$ was also trained on hindsight-relabeled experience data, where for DC-MCTS we used the temporally balanced parser and for MCTS the corresponding left-first parser. Training of the heuristics greatly improved the performance of both planners. Figure 3 shows learning curves for mazes with wall density $d = 0.75$. DC-MCTS exhibits substantially improved performance compared to MCTS, and when compared at equal performance levels, DC-MCTS requires $5$ to $10$-times fewer training episodes than MCTS. The learned sub-goal proposal $p$ for DC-MCTS is visualized for two example tasks in Figure 2 (further examples are given in the Appendix in Figure 8). Probability mass concentrates on promising sub-goals that are far from both start and goal, approximately partitioning the task into equally hard sub-tasks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Continuous Control Mazes", "weight": 1.0} -->

Next, we investigated the performance of both MCTS and DC-MCTS in challenging continuous control environments with non-trivial low-level policies. To this end, we embedded the navigation in grid-world mazes described above into a physical 3D environment simulated by MuJoCo, where each grid-world cell is rendered as 4m$\times$`<!-- -->`{=html}4m cell in physical space. The agent is embodied by a quadruped "ant" body; for illustration see Figure 4. For the low-level policy $\pi^{m}$, we pre-trained a goal-directed neural network controller that gets as inputs proprioceptive features (e.g. some joint angles and velocities) of the ant body as well as a 3D-vector pointing from its current position to a target position. $\pi^{m}$ was trained to navigate to targets randomly placed less than 1.5 m away in an open area (no walls), using MPO Abdolmaleki et al.. See Appendix B.4 for more details.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Continuous Control Mazes", "weight": 1.0} -->

If unobstructed, $\pi^{m}$ can walk in a straight line towards its current goal. However, this policy receives no visual input and thus can only avoid walls when guided with appropriate sub-goals. In order to establish an interface between the low-level $\pi^{m}$ and the planners, we used another convolutional neural network to approximate the low-level value oracle $v^{\pi^{m}}{(s_{0},\left. s_{\infty} \middle| c_{\mathcal{M}} \right.)}$: It was trained to predict whether $\pi^{m}$ will succeed in solving the navigation tasks ${(s_{0},s_{\infty})},c_{\mathcal{M}}$. Its input is given by the corresponding discrete grid-world representation $c_{\mathcal{M}}$ of the maze ($21 \times 21$ feature map of categoricals as described above, detail in Appendix).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Continuous Control Mazes", "weight": 1.0} -->

Note that this setting is still a difficult environment: In initial experiments we verified that a model-free baseline (also based on MPO) with access to state abstraction and low-level controller, only solved about 10% of the mazes after 100 million episodes due to the extremely sparse rewards.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Continuous Control Mazes", "weight": 1.0} -->

We applied the MCTS and DC-MCTS planners to this problem to find symbolic plans consisting of sub-goals in ${\{ 1,\ldots,21\}}^{2}$. The high-level heuristics $p$ and $v$ were trained for 65k episodes, exactly as described in Section 5.1, except using $v^{\pi^{m}}$ instead of $v^{\pi^{0}}$. We again observed that DC-MCTS outperforms by a wide margin the vanilla MCTS planner: Figure 5 shows performance of both (with fully trained search heuristics) as a function of the search budget for the most difficult mazes with wall density $d = 1.0$. Performance of DC-MCTS with the MuJoCo low-level controller was comparable to that with the hard-coded low-level policy from the grid-world experiment (with same wall density), showing that the abstraction of planning over low-level sub-goals successfully isolates high-level planning from low-level execution. We did not manage to successfully train the MCTS planner on MuJoCo navigation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Continuous Control Mazes", "weight": 1.0} -->

This was likely due to the fact that HER training, which we found --- in ablation studies --- essential for training DC-MCTS on both problem versions and MCTS on the grid-world problem, was not appropriate for MCTS on MuJoCo navigation: Left-first parsing for selecting sub-goals for HER training consistently biased the MCTS search prior $p$ to propose next sub-goals too close to the previous sub-goal. This lead the MCTS planner to \"micro-manage\" the low-level policy too much, in particular in long corridors that $\pi^{m}$ can solve by itself. DC-MCTS, by recursively partitioning, found an appropriate length scale of sub-goals, leading to drastically improved performance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Visualizing MCTS and DC-MCTS", "weight": 1.0} -->

To further illustrate the difference between DC-MCTS and MCTS planning we can look at an example search tree from each method in Figure 6. Light blue nodes are part of the final plan: note how in the case of DC-MCTS, the plan is distributed across a sub-tree within the search tree, while for the standard MCTS the plan is a single chain. The first 'actionable' sub-goal, i.e. the first sub-goal that can be passed to the low-level policy, is the left-most leaf in DC-MCTS and the first dark node from the root for MCTS.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

To enable guided, divide-and-conquer style planning, we made a few strong assumptions. Sub-goal based planning requires a universal value function oracle of the low-level policy. In many applications, this will have to be approximated from data. Overly optimistic approximations are likely be exploited by the planner, leading to "delusional" plans. Joint learning of the high and low-level components can potentially address this issue. A further limitation of sub-goal planning is that, at least in its current naive implementation, the \"action space\" for the planner is the whole state space of the underlying MDPs. Therefore, the search space will have a large branching factor in large state spaces. A solution to this problem likely lies in using learned state abstractions for sub-goal specifications, which is a fundamental open research question. We also implicitly made the assumption that low-level skills afforded by the low-level policy need to be "universal", i.e. if there are states that it cannot reach, no amount of high level search will lead to successful planning outcomes.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

In spite of these assumptions and open challenges, we showed that non-sequential sub-goal planning has some fundamental advantages over the standard approach of search over primitive actions: (i) Abstraction and dynamic allocation:Sub-goals automatically support temporal abstraction as the high-level planner does not need to specify the exact time horizon required to achieve a sub-goal. Plans are generated from coarse to fine, and additional planning is dynamically allocated to those parts of the plan that require more compute. (ii) Closed & open-loop:The approach combines advantages of both open- and closed loop planning: The closed-loop low-level policies can recover from failures or unexpected transitions in stochastic environments, while at the same time the high-level planner can avoid costly closed-loop planning. (iii) Long horizon credit assignment:Sub-goal abstractions open up new algorithmic possibilities for planning --- as exemplified by DC-MCTS --- that can facilitate credit assignment and therefore reduce planning complexity.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

(iv) Parallelization:Like other divide-and-conquer algorithms, DC-MCTS lends itself to parallel execution by leveraging problem decomposition made explicit by the independence of the \"left\" and \"right\" sub-problems of an AND node. (v) Reuse of cached search:DC-MCTS is highly amenable to transposition tables, by caching and reusing values for sub-problems solved in other branches of the search tree. (vi) Generality:DC-MCTS is strictly more general than both forward and backward goal-directed planning, both of which can be seen as special cases.
