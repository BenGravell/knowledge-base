<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Averse Stochastic Shortest Path Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the stochastic shortest path planning problem in MDPs, i.e., the problem of designing policies that ensure reaching a goal state from a given initial state with minimum accrued cost. In order to account for rare but important realizations of the system, we consider a nested dynamic coherent risk total cost functional rather than the conventional risk-neutral total expected cost. Under some assumptions, we show that optimal, stationary, Markovian policies exist and can be found via a special Bellman's equation. We propose a computational technique based on difference convex programs (DCPs) to find the associated value functions and therefore the risk-averse policies. A rover navigation MDP is used to illustrate the proposed methodology with conditional-value-at-risk (CVaR) and entropic-value-at-risk (EVaR) coherent risk measures.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Shortest path problems, i.e., the problem of reaching a goal state form an initial state with minimum total cost, arise in several real-world applications, such as driving directions on web mapping websites like MapQuest or Google Maps and robotic path planning. In a shortest path problem, if transitions from one system state to another is subject to stochastic uncertainty, the problem is referred to as a stochastic shortest path (SSP) problem. In this case, we are interested in designing policies such that the total expected cost is minimized. Such planning under uncertainty problems are indeed equivalent to an undiscounted total cost Markov decision processes (MDPs) and can be solved efficiently via the dynamic programming method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, emerging applications in path planning, such as autonomous navigation in extreme environments, e.g., subterranean and extraterrestrial environments, not only require reaching a goal region, but also risk-awareness for mission success. Nonetheless, the conventional total expected cost is only meaningful if the law of large numbers can be invoked and it ignores important but rare system realizations. In addition, robust planning solutions may give rise to behavior that is extremely conservative.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Risk can be quantified in numerous ways. For example, mission risks can be mathematically characterized in terms of chance constraints, utility functions, and distributional robustness. Chance constraints often account for Boolean events (such as collision with an obstacle or reaching a goal set) and do not take into consideration the tail of the cost distribution. To account for the latter, risk measures have been advocated for planning and decision making tasks in robotic systems. The preference of one risk measure over another depends on factors such as sensitivity to rare events, ease of estimation from data, and computational tractability. Artzner et. al. characterized a set of natural properties that are desirable for a risk measure, called a coherent risk measure, and have henceforth obtained widespread acceptance in finance and operations research, among others. Coherent risk measures can be interpreted as a special form of distributional robustness, which will be leveraged later in this paper.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Conditional value-at-risk (CVaR) is an important coherent risk measure that has received significant attention in decision making problems, such as MDPs. General coherent risk measures for MDPs were studied, wherein it was further assumed the risk measure is *time consistent*, akin to the dynamic programming property. Following the footsteps of, proposed a sampling-based algorithm for MDPs with static and dynamic coherent risk measures using policy gradient and actor-critic methods, respectively (also, see a model predictive control technique for linear dynamical systems with coherent risk objectives ). A method based on stochastic reachability analysis was proposed in to estimate a CVaR-safe set of initial conditions via the solution to an MDP. A worst-case CVaR SSP planning method was proposed and solved via dynamic programming. Also, total cost undiscounted MDPs with static CVaR measures were studied in and solved via a surrogate MDP, whose solution approximates the optimal policy with arbitrary accuracy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a method for designing policies for SSP planning problems, such that the total accrued cost in terms of dynamic, coherent risk measures is minimized (a generalization of the problems considered in and to dynamic, coherent risk measures). We begin by showing that, under the assumption that the goal region is reachable in finite time with non-zero probability, the total accumulated risk cost is always bounded. We further show that, if the coherent risk measures satisfy a Markovian property, we can find optimal, stationary, Markovian risk-averse policies via solving a special Bellman's equation. We also propose a computational method based on difference convex programming to solve the Bellman's equation and therefore design risk-averse policies. We elucidate the proposed method via numerical examples involving a rover navigation MDP and CVaR and entropic-value-at-risk (EVaR) measures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In the next section, we review some definitions and properties used in the sequel. In Section III, we present the problem under study and show its well-posedness under an assumption. In Section IV, we present the main result of the paper, i.e., a special Bellman's equation for the risk-averse SSP problem. In Section V, we describe a computational method to find risk-averse policies. In Section VI, we illustrate the proposed method via a numerical example and finally, in Section VI, we conclude the paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: We denote by ${\mathbb{R}}^{n}$ the $n$-dimensional Euclidean space and ${\mathbb{N}}_{\geq 0}$ the set of non-negative integers. We use bold font to denote a vector and ${( \cdot )}^{\top}$ for its transpose, e.g., ${\mathbf{a}} = {(a_{1},\ldots,a_{n})}^{\top}$, with $n \in {\{ 1,2,\ldots\}}$. For a vector $\mathbf{a}$, we use ${\mathbf{a}} \succeq {{( \preceq )}\mathbf{0}}$ to denote element-wise non-negativity (non-positivity) and ${\mathbf{a}} \equiv \mathbf{0}$ to show all elements of $\mathbf{a}$ are zero.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a finite set $\mathcal{A}$, we denote its power set by $2^{\mathcal{A}}$, i.e., the set of all subsets of $\mathcal{A}$. For a probability space $(\Omega,\mathcal{F},{\mathbb{P}})$ and a constant $p \in {\lbrack 1,\infty)}$, $\mathcal{L}_{p}{(\Omega,\mathcal{F},{\mathbb{P}})}$ denotes the vector space of real valued random variables $c$ for which ${{\mathbb{E}}{|c|}^{p}} < \infty$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Superscripts are used to denote indices and subscripts are used to denote time steps (stages), e.g., for $s \in \mathcal{S}$, $s_{1}^{2}$ means the the value of $s^{2} \in \mathcal{S}$ at the $1$st stage.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Next, we formally describe the risk-averse SSP problem. We also demonstrate that, if the goal state is reachable in finite time, the risk-averse SSP problem is well-posed. Let $\pi = {\{\pi_{0},\pi_{1},\ldots\}}$ be an admissible policy.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Consider MDP $\mathcal{M}$ as described in Definition 1. Given an initial state $s_{0} \neq s^{g}$, we are interested in solving the following problem

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1", "weight": 1.0} -->

is the total risk functional for the admissible policy $\pi$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 1", "weight": 1.0} -->

In fact, we are interested in reaching the goal state $s^{g}$ such that the total risk cost is minimized^11^1An important class of SSP planning problems are concerned with minimum-time reachability. Indeed, our formulation also encapsulates minimum-time problems, in which for MDP $\mathcal{M}$, we have ${c{(s)}} = 1$, for all $s \in {\mathcal{S} \smallsetminus {\{ s^{g}\}}}$.. Note that the risk-averse deterministic shortest problem can be obtained as a special case when the transitions are deterministic. We define the optimal risk value function as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 1", "weight": 1.0} -->

We posit the following assumption, which implies that the goal state is reachable eventually under all policies.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1 (Goal is Reachable in Finite Time)", "weight": 1.0} -->

Regardless of the policy used and the initial state, there exists an integer $\tau$ such that there is a positive probability that the goal state $s^{g}$ is visited after no more than $\tau$ stages^22^2If instead of one goal state $s^{g}$, we were interested in a set of goal states $\mathcal{G} \subset \mathcal{S}$, it suffices to define $\tau = \inf{\{ t \mid {\mathbb{P}}{(s_{t} \in \mathcal{G} \mid s_{0} \in \mathcal{S} \smallsetminus \mathcal{G},\pi)} > 0\}}$. Then, all the paper's derivations can be applied. For the sake of simplicity of the presentation, we present the results for a single goal state..

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1 (Goal is Reachable in Finite Time)", "weight": 1.0} -->

We then have the following observation with respect to Problem 1^33^3Note that Problem 1 is ill-posed in general. For example, if the induced Markov chain for an admissible policy is periodic, then the limit in may not exist. This is in contrast to risk-averse discounted infinite-horizon MDPs, for which we only require non-negativity and boundedness of immediate costs..

<!-- chunk {"id": "body-0019", "role": "body", "section": "Risk-Averse SSP Planning", "weight": 1.0} -->

This section presents the paper's main result, which includes a special Bellman's equation for finding the risk value functions for Problem 1. Furthermore, assuming that the coherent risk measures satisfy a Markovian property, we show that the optimal risk-averse policies are stationary and Markovian.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Risk-Averse SSP Planning", "weight": 1.0} -->

To begin, note that at any time $t$, the value of $\rho_{t}$ is $\mathcal{F}_{t}$-measurable and is allowed to depend on the entire history of the process $\{ s_{0},s_{1},\ldots\}$ and we cannot expect to obtain a Markov optimal policy. In order to obtain Markov optimal policies for Problem 1, we need the following property \[39, Section 4\] of risk measures.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The one-step coherent risk measure $\rho_{t}$ is a Markov risk measure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We can now present the main result in the paper, a form of Bellman's equations for solving the risk-averse SSP problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "DCP Computational Approach", "weight": 1.0} -->

In this section, we propose a computational method based on DCPs to find the risk value functions and subsequently policies that minimize the accrued dynamic risk in the SSP planning. Before stating the DCP formulation, we show that the Bellman operator in is non-decreasing. Let

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A DCPs for Risk-Averse SSP Planning", "weight": 1.0} -->

Assumption 1 implies that each $\rho$ is a coherent, Markov risk measure. Hence, the mapping $v\mapsto{\sigma{(v, \cdot, \cdot )}}$ is convex (because $\sigma$ is also a coherent risk measure). We next show that optimization problem is in fact a DCP.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A DCPs for Risk-Averse SSP Planning", "weight": 1.0} -->

The above optimization problem is indeed a standard DCP. Many applications require solving DCPs, such as feature selection in machine learning and inverse covariance estimation in statistics. DCPs can be solved globally, e.g. using branch and bound algorithms. Yet, a locally optimal solution can be obtained based on techniques of nonlinear optimization more efficiently. In particular, in this work, we use a variant of the convex-concave procedure, wherein the concave terms are replaced by a convex upper bound and solved. In fact, the disciplined convex-concave programming (DCCP) technique linearizes DCP problems into a (disciplined) convex program (carried out automatically via the DCCP Python package ), which is then converted into an equivalent cone program by replacing each function with its graph implementation. Then, the cone program can be solved readily by available convex programming solvers, such as CVXPY.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A DCPs for Risk-Averse SSP Planning", "weight": 1.0} -->

In the Appendix, we present the specific DCPs required for risk-averse SSP planning for CVaR and EVaR risk measures used in our numerical experiments in the next section. Note that for the risk-neutral conditional expectation measure, optimization (V-A) becomes a linear program, since ${\sigma\left\{ {J{(s^{\prime})}},s,{T{(\left. s^{\prime} \middle| {s,\alpha} \right.)}} \right\}} = {\sum_{s^{\prime} \in \mathcal{S}}{T{(\left. s^{\prime} \middle| {s,\alpha} \right.)}J{(s^{\prime})}}}$ is linear in the decision variables $\mathbf{J}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we evaluate the proposed method for risk-averse SSP planning with a rover navigation MDP (also used in ). We consider the traditional total expectation as well as CVaR and EVaR. The experiments were carried out on a MacBook Pro with 2.8 GHz Quad-Core Intel Core i5 and 16 GB of RAM. The resultant linear programs and DCPs were solved using CVX with DCCP add-.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

An agent (e.g. a rover) must autonomously navigate a 2-dimensional terrain map (e.g. Mars surface) represented by an $M \times N$ grid with $0.25MN$ obstacles. Thus, the state space is given by $\mathcal{S} = \left. \{ s^{i} \middle| {{i = {x + y}},{{x \in {\{ 1,\ldots,M\}}},{y \in {\{ 1,\ldots,N\}}}}}\} \right.$ with ${x = 1},{y = 0}$ being the leftmost bottom grid. Since the rover can move from cell to cell, its action set is ${Act} = {\{ E,W,N,S\}}$. The actions move the robot from its current cell to a neighboring cell, with some uncertainty. The state transition probabilities for various cell types are shown for actions $E$ (East) and $N$ (North) in Figure 2. Other actions lead to similar transitions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Hitting an obstacle incurs the immediate cost of $5$, while the goal grid region has zero immediate cost. Any other grid has a cost of $1$ to represent fuel consumption.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Once the policies are calculated, as a robustness test similar to, we included a set of single grid obstacles that are perturbed in a random direction to one of the neighboring grid cells with probability $0.2$ to represent uncertainty in the terrain map. For each risk measure, we run $100$ Monte Carlo simulations with the calculated policies and count the number of runs ending in a collision.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In the experiments, we considered three grid-world sizes of $4 \times 5$, $10 \times 10$, and $10 \times 20$ corresponding to $20$, $100$, and $200$ states, respectively. We allocated 2, 4, and 8 uncertain (single-cell) obstacles for the $4 \times 5$, $10 \times 10$, and $10 \times 20$ grids, respectively. In each case, we solve DCP (linear program in the case of total expectation) with ${{|\mathcal{S}|}{|{Act}|}} = {{MN} \times 4} = {4MN}$ constraints and ${MN} + 1$ variables (the risk value functions $J$'s and $\zeta$ for CVaR and EVaR as discussed in the Appendix). In these experiments, we set the confidence levels to $\varepsilon = 0.3$ (more risk-averse) and $\varepsilon = 0.7$ (less risk-averse) for both CVaR and EVaR coherent risk measures.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The initial condition was chosen as $s_{0} = s^{1}$, i.e., the agent starts at the leftmost grid at the bottom, and the goal state was selected as $s^{g} = s^{MN}$, i.e., the rightmost grid at the top.

<!-- chunk {"id": "body-0033", "role": "body", "section": "U.O", "weight": 1.0} -->

A summary of our numerical experiments is provided in Table 1. Note the computed values of Problem 1 satisfy ${{\mathbb{E}}{(c)}} \leq {{CVaR}_{\varepsilon}{(c)}} \leq {{EVaR}_{\varepsilon}{(c)}}$. This is in accordance with the theory that EVaR is a more conservative coherent risk measure than CVaR (see also our work on EVaR-based model predictive control for dynamically moving obstacles ). Furthermore, the total accrued risk cost is higher for $\varepsilon = 0.3$, since this leads to more risk-averse policies.

<!-- chunk {"id": "body-0034", "role": "body", "section": "U.O", "weight": 1.0} -->

For total expectation coherent risk measure, the calculations took significantly less time, since they are the result of solving a set of linear programs. For CVaR and EVaR, a set of DCPs were solved. EVaR calculations were the most computationally involved, since they require solving exponential cone programs. Note that these calculations can be carried out offline for policy synthesis and then the policy can be applied for risk-averse robot path planning.

<!-- chunk {"id": "body-0035", "role": "body", "section": "U.O", "weight": 1.0} -->

The table also outlines the failure ratios of each risk measure. In this case, EVaR outperformed both CVaR and total expectation in terms of robustness, which is consistent with the fact that EVaR is a more conservative risk measure. Lower failure/collision rates were observed for $\varepsilon = 0.3$, which correspond to more risk-averse policies. In addition, these results suggest that, although total expectation can be used as a measure of performance in high number of Monte Carlo simulations, it may not be practical to use it for real-world planning under uncertainty scenarios. CVaR and EVaR seem to be a more efficient metric for performance in shortest path planning under uncertainty.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We proposed a method based on dynamic programming for designing risk-averse policies for the SSP problem. We presented a computational approach in terms of difference convex programs for finding the associated risk value functions and hence the risk-averse policies. Future research will extend to risk-averse MDPs with average costs and risk-averse MDPs with linear temporal logic specifications, where the former problem is cast as a special case of the risk-averse SSP problem. In this work, we assumed the states are fully observable, we will study the SSP problems with partial state observation in the future, as well.
