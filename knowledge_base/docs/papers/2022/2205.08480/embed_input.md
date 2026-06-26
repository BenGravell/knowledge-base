<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Effort Informed Roadmaps (EIRM*): Efficient Asymptotically Optimal Multiquery Planning by Actively Reusing Validation Effort

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Multiquery planning algorithms find paths between various different starts and goals in a single search space. They are designed to do so efficiently by reusing information across planning queries. This information may be computed before or during the search and often includes knowledge of valid paths. Using known valid paths to solve an individual planning query takes less computational effort than finding a completely new solution. This allows multiquery algorithms, such as PRM*, to outperform single-query algorithms, such as RRT*, on many problems but their relative performance depends on how much information is reused. Despite this, few multiquery planners explicitly seek to maximize path reuse and, as a result, many do not consistently outperform single-query alternatives. This paper presents Effort Informed Roadmaps (EIRM*), an almost-surely asymptotically optimal multiquery planning algorithm that explicitly prioritizes reusing computational effort. EIRM* uses an asymmetric bidirectional search to identify existing paths that may help solve an individual planning query and then uses this information to order its search and reduce computational effort.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This allows it to find initial solutions up to an order-of-magnitude faster than state-of-the-art planning algorithms on the tested abstract and robotic multiquery planning problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A general-purpose path planner aims to find a path that connects a start to a goal, typically in a continuous space. The underlying structure of many environments is static and tends to pose repetitive problems, such as in home [faust2018prmrl], construction [funk2021learn2assemble,hartmann2020robust], or kitchen [lagriffoul2018platform] scenarios. Multiquery planners are designed to solve multiple different start-goal queries in static environments by exploiting this repetitiveness to reduce the computational time required to find a solution. A large component of this computational effort for an individual planning query is checking if a path is collision free, i.e., validation effort[hauser2015lazy,Solovey2020,sanchez2002]. This can be reduced in multiquery settings by reusing previously gained knowledge of valid edges to solve subsequent queries more efficiently.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many planners compute reusable information in advance. Probabilistic Roadmaps (PRM) [kavraki1996probabilistic] construct a roadmap and collision check all its edges during preprocessing. This roadmap is then used to simplify individual queries to a graph search over the roadmap, resulting in fast solution times.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

EIRM*, $t_\text{init} = 0.00437\text{s}$ LazyPRM*, $t_\text{init} = 2.481\text{s}$ An illustration of EIRM* finding the initial solution orders-of-magnitude faster than LazyPRM* for the 20$^\text{th}$ query of a multiquery problem. The green and red disks are the start and the goal, respectively. Edges that are collision checked in this query are yellow, and edges that are reused are dark grey. Light grey edges are valid edges that have been collision checked in previous queries. The time of the initial solution is $t_\text{init}$. EIRM* validates two edges to connect to the preexisting graph while LazyPRM* validates 81 edges.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the environment is not available in advance, reusable information needs to be calculated in parallel to solving queries. [bohlin00lazy] solves individual queries by optimistically assuming all edges and vertices in the roadmap are valid, and then only checking the edges and vertices of the solution that are not yet validated. It preserves the knowledge of validated and invalidated edges over multiple queries but does not activelyreuse previously invested effort, so any reuse of effort is by coincidence. [karaman2011sampling] and LazyPRM*[hauser2015lazy]extend these ideas to the optimal planning problem by continually adding more samples to their roadmaps to improve the approximation with additional computational time. This roadmap asymptotically contains the optimal solution with probability one, i.e., is almost-surely asymptotically optimal. While this graph growth improves solution quality, it can also increase initial solution times since new queries start from the previous approximation and searching large graphs can be prohibitively expensive.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents Effort Informed Roadmaps (EIRM*), an almost-surely asymptotically optimal anytime multiquery planner which seeks to to prioritize finding an initial solution by actively reusing effort from previous queries. EIRM* extends Effort Informed Trees (EIT*)[strub2021ait] to the challenges of solving multiquery problems quickly: (i) actively seeking to reuse computational effort, and (ii)managing graph size over multiple planning queries.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

EIRM* quickly finds an initial solution to a planning query by using a search explicitly informed by validation effort. It then uses a cost-informed search to improve this solution by efficiently adding and searching more samples for as long as time allows for the current query. When a new planning query is posed, EIRM* prevents the complexity of this high-resolution graph from negatively affecting search performance by rewinding the approximation to the first batch of samples. It then reuses computational effort to solve this new query by both informing the initial search by validation effort and improving the solution by replaying the previous samples and reusing any previously validated edges. This allows EIRM* to find initial solutions to individual queries faster than other planners while almost-surely converging asymptotically to the same global optimum.=-1 EIRM* to other planners available in Open Motion Planning Library (OMPL)[sucan2012ompl] on several low-and high-dimensional abstract environments, and simulated robots. On these problems, it solves later queries of a problem up to an order-of-magnitude faster than the tested planners while performing the same on initial queries.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

EIRM* extends EIT* to the multiquery setting. EIT* is an almost-surely asymptotically optimal anytime sampling-based path planning algorithm that is based on an asymmetric search which simultaneously calculates and exploits problem-specific heuristics. Both EIT* and EIRM* sample batches of states, and view these states as a series of edge-implicit random geometric graphs (RGGs) [penrose2003random], as in BIT* [gammell\_ijrr20]. The edges in each RGG are processed in a reverse search informed by an a priori heuristic. The reverse search is computationally inexpensive since collisions are checked at a lower resolution than in the forward search, i.e., sparsely checked. The reverse search computes approximation-specific heuristic estimates of the cost and effort to reach the goal, and provides a lower bound on the resolution-optimal solution in the current RGG approximation. The forward search is guided by the cost and effort heuristics that are calculated in the reverse search.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

EIT* and EIRM* both compute a suboptimality bound by inflating the resolution-optimal solution cost and only consider edges that satisfy this suboptimality bound. During the forward search, edges are fully collision checked. For more details on EIT*, see[strub\_dphil21].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

In the multiquery setting, the RGG likely contains validated edges from solving previous queries that would require zero validation effort to reuse in a solution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

EIRM* leverages these zero-effort edges and avoids unbounded graph growth by modifying EIT*'s batch sampling (ssec:graph) and reverse search (ssec:rev) while using the same forward search (ssec:fwd). The batch sampling is modified to rewind the approximation of each query to the initial batch of samples. This approximation is then improved by replaying the same batches of samples as in previous queries in order to reuse effort.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

The reverse search of EIRM* differs from EIT* in that the search of each query is ordered by estimated validation effort until an initial solution is found. After finding an initial solution, EIRM* computes an admissible cost heuristic in its reverse search, and the forward search is ordered by cost. EIRM* is illustrated infig:illustration, and algorithmic details are presented in alg:eiprm,alg:expand,alg:get\_new\_sample,alg:best\_rev\_edge\_improve\_sol,alg:pop\_fwd\_full, with modifications compared to EIT* in orange.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Effort Informed Roadmaps (EIRM*)", "weight": 1.0} -->

EIRM* maintains the almost-sure asymptotic optimality and probabilistic completeness of EIT*. Initially only considering the first batch of samples and later adding previous samples to improve the cost results in the same behaviour as EIT* as the number of samples goes to infinity and does not alter formal properties. The full proof for almost-sure asymptotic optimality for EIT*, which implies probabilistic completeness, is presented in[strub\_dphil21].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Approximation", "weight": 1.0} -->

EIRM* incrementally adds batches of $m$ states to the RGG to build a discrete approximation of the search space (alg:eiprm, alg:add\_samples). Informed sampling [gammell2014informed]can be used to focus the approximation on the part of the space that can improve the solution once an initial solution to the current query has been found, if appropriate.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Approximation", "weight": 1.0} -->

EIRM* considers connections between each sample and its $k$-nearest neighbours or states within a distance $r$ as well as previously validated edges independent of their distance to the state currently under consideration (alg:expand, alg:add\_valid\_neighbours).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Approximation", "weight": 1.0} -->

If not handled explicitly, the size of the RGG will grow unbounded over the course of multiple queries.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Approximation", "weight": 1.0} -->

EIRM*manages the growth of the graph by rewinding the sampling-based approximation to the first batch to find the initial solution to each query and by pruning starts and goals from the graph to limit graph growth.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Batch Rewinding", "weight": 1.0} -->

High-resolution approximations often contain high-quality solutions, but are computationally expensive to search due to the computational cost of the nearest-neighbour lookup and the required depth of the search. When fast solution times are desired, low-resolution approximations are often better since the computational cost of these operations reduce with the number of samples.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Batch Rewinding", "weight": 1.0} -->

EIRM* stores all sampled states $x_i$ for the duration of the multiquery problem in a buffer, $\mathcal{B}=(x_1, x_2, \cdots, x_n)$, and a new batch of samples is added to the approximation from the buffer when refine\_approximation is called (alg:get\_new\_sample). If the buffer does not contain enough samples, new states are first sampled and added to the buffer (alg:get\_new\_sample, alg:sample\_uni). Samples from the buffer are only added to the batch if they can improve the current solution (alg:get\_new\_sample, alg:rejection). The current position in the buffer, $i_\text{buffer}$, is incremented as samples from the buffer are used (alg:get\_new\_sample, alg:increment), and is reset once a new planning query is considered (alg:eiprm, alg:clear).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Start/Goal Pruning", "weight": 1.0} -->

The size of the graph will grow unbounded with the number of queries if all starts and goals of every query are kept in the graph. Keeping all starts and goals in the graph may also result in a nonuniform distribution of states if the starts and goals are not uniformly distributed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Start/Goal Pruning", "weight": 1.0} -->

Forgetting all starts and goals prevents unbounded graph growth and maintains the state sampling distribution, but discards the effort spent validating associated edges. These conflicting behaviours are balanced by keeping the starts or goals in a buffer, $\mathcal{B}_\text{start/goal}$, if they satisfy a user-specified criterion (alg:eiprm, alg:add\_starts\_to\_buffer). The stored starts and goals are added to the RGG at the same time as the new start and goals of the current query (alg:eiprm, alg:add\_start\_goals) and the first batch of samples.=-1

<!-- chunk {"id": "body-0024", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

EIRM*first tries to find a solution as quickly as possible, and then tries to decrease the cost as quickly as possible. The reverse search is therefore initially ordered on validation effort, and afterwards on cost.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The reverse search considers the best edge, starting at the source state, $x_\text{s}$, to the target state, $x_\text{t}$, from the edge-queue, $\mathcal{Q}_\mathcal{R}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The elements of the key are estimates of the total computational effort and the total solution cost of a path through an edge. Their ordering depends on whether the current query already has a solution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The edge with the lowest key is extracted (alg:eiprm, alg:if\_not\_fin,alg:k\_eiprm,alg:else\_not\_fin,alg:k\_eit) and collisions are checked sparsely at evenly distributed states along the edge (alg:eiprm, alg:no\_sparse\_coll). If no collision is found, the computed cost heuristics, $\bar{h}[\cdot]$ and $\hat{h}[\cdot]$, and the effort heuristic, $\bar{e}[\cdot]$, of the target state, $x_\text{t}$, are updated (alg:eiprm, alg:update\_inadmissible,alg:update\_heuristic,alg:update\_heuristic\_2). The target state is then expanded, and the edges to its neighbours are inserted into the reverse queue, (alg:eiprm, alg:expand\_rev) and the iteration restarts.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

If a collision was found, the edge is added to the set of invalid edges, $E_\text{invalid}$ (alg:eiprm, alg:add\_sparse\_invalid). The reverse search terminates when it is guaranteed to have found the resolution-optimal solution on the current RGG approximation or no solution is found, as in A* (alg:eiprm, alg:can\_improv\_rev), where $k^\text{effort}_{\mathcal{F}}$ and $k^\text{cost}_{\mathcal{F}}$are the lexicographical sortings of the forward search and are defined analogously to the respective reverse keys.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The forward search is based on anytime explicit estimation search (AEES) [thayer2012better]and is guided by the calculated heuristics to effectively find solutions to each query. This search completely checks edges for collision and is more computationally expensive than the reverse search.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The previously computed admissible cost heuristic provides a lower bound, $\hat{s}$, on the resolution-optimal solution in the current RGG, $$\hat{s} = \min_{(x_\text{s}, x_\text{t})\in\mathcal{Q}_\mathcal{F}} \left\{{g}_\mathcal{F}(x_\text{s}) + \hat{c}(x_\text{s}, x_\text{t}) + \hat{h}[x_\text{t}]\right\},$$ where ${g}_\mathcal{F}(x_\text{s})$ is the cost to come through the forward tree to the source state, $x_\text{s}$, and $Q_\mathcal{F}$ is the edge-queue of the forward search.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Forward Search", "weight": 1.0} -->

A potentially more accurate estimate of the resolution-optimal cost can be calculated with the inadmissible cost heuristic, $$\bar{s} = \min_{(x_\text{s}, x_\text{t})\in\mathcal{Q}_\mathcal{F}} \left\{{g}_\mathcal{F}(x_\text{s}) + \bar{c}(x_\text{s}, x_\text{t}) + \bar{h}[x_\text{t}]\right\}.$$ This possibly inadmissible estimate can be more accurate than its admissible counterpart since the inadmissible cost heuristic can use information that may overestimate the true cost.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The focal set, $\mathcal{S}$, is the set of edges that can possibly lead to a solution within the current suboptimality bound, $w\bar{s}$, $$\mathcal{S} = \left\{(x_\text{s}, x_\text{t}) \; |\; {g}_\mathcal{F}(x_\text{t}) + \bar{c}(x_\text{t}, x_\text{s}) + \bar{h}[x_\text{s}] \leq w\bar{s}\right\}.$$ EIRM* expands the next edge (alg:eiprm, alg:pop\_fwd, alg:pop\_fwd\_full) considering the focal set and fully collision checks the edge (alg:eiprm, alg:coll\_free). If the edge is found to be invalid, it is labeled as such (alg:eiprm, alg:add\_invalid) and the reverse search is restarted.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Forward Search", "weight": 1.0} -->

Edges are selected for expansion by first considering the minimum remaining validation effort in the focal set, $$\argmin_{(x_\text{s}, x_\text{t})\in \mathcal{S}} \left\{\bar{e}(x_\text{s}, x_\text{t}) + \bar{e}[x_\text{t}]\right\}.$$ If this edge can improve the solution, it is selected (alg:pop\_fwd\_full, alg:ret\_min\_effort). If not, the edge with the lowest inadmissible cost estimate is selected if it is estimated to lead to a solution within the current suboptimality bound (alg:pop\_fwd\_full, alg:ret\_min\_inad\_cost). Otherwise, the edge with the lowest admissible cost estimate is selected (alg:pop\_fwd\_full, alg:ret\_ad\_cost).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The forward search continues until it is known that the best edge in the forward queue can not improve the solution (alg:eiprm, alg:can\_improv\_fwd), or a solution is found. If a solution is found, the best achieved cost is updated (alg:eiprm, alg:1), the search is then ordered by cost by setting the suboptimality factor to one (alg:eiprm, alg:2), the approximation is refined (alg:eiprm, alg:add\_samples), and the loop restarts with the reverse search.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Forward Search", "weight": 1.0} -->

This search continues as long as time allows and almost-surely converges asymptotically to the optimal solution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

EIRM* on a set of simulated scenarios All experiments were run using OMPL 1.5, on a laptop with an Intel i7-4720HQ CPU @ 2.60GHz processor with 16GB RAM., and compared it to a selection of both single-and multiquery planners available in OMPL: PRM*, LazyPRM*, RRT-Connect, RRT*, and EIT*. The OMPL version of SPARS/SPARS2 was not included due to performance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

RRT* used a goal bias of 0.05. Both RRT-based planners used maximum edge lengths of 0.3, 0.5, 1.25, and 2.4 in $\mathbb{R}^2$, $\mathbb{R}^4$, $\mathbb{R}^8$, and $\mathbb{R}^{14}$, respectively. EIRM* and EIT* used the $k$-nearest neighbour method and sampled $100$ states per batch. The a priori heuristic for both admissible and inadmissible cost in EIRM* and EIT* was the Euclidean distance. The a priori heuristic for inadmissible effort between two states, i.e., $\bar{e}$, in EIT* and EIRM* was the Euclidean distance divided by the needed remaining collision checking resolution.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

In order to fully exploit the possibility of preexisting zero-effort edges, EIRM* used the zero heuristic for the inadmissible effort to come, i.e., $\bar{d}$.=-1 In order to limit the growth of the graph, EIRM* kept starts and goals after a query if the number of required collision checks, i.e., the validation effort, to reach the state from the closest existing neighbour was larger than [group-separator=,]50000and otherwise forgot them.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

An illustration of the abstract scenarios in $\mathbb{R}^2$ with the subregions from which starts (green) and goals (red) are drawn uniformly, (a), (b). An illustration of the bookshelf scenario where the two-armed robot simulates picking/placing objects from the bookshelf, (c). Two versions of the repeating rectangles problem were considered, one in which start-goal queries are drawn from the subregions and the other in which they are drawn uniformly from the whole space.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

The median initial solution times per query over 100 runs for the repeating rectangles with subregion starts and goals in $\mathbb{R}^4$, (a), globally sampled starts and goals in $\mathbb{R}^8$, (b), and the bookshelf scenario, (c). The solid line is the median initial solution time per query, and the shaded area is the nonparametric 99% confidence interval. Unsuccessful runs are treated as having infinite cost. For the bookshelf scenario, PRM* and RRT* were not run due to performance.=-1 Wall Gap in $\mathbb{R}^2$: Query 1 Wall Gap in $\mathbb{R}^2$: Query 50 The planner performance in two queries for the wall gap in $\mathbb{R}^2$. The success plots (top) show the percentage of successful runs over time. The cost evolution plots (bottom) show the median cost at a given time as a thick line, with the nonparametric 99% confidence interval as shaded area. The squares show the median initial solution time for the query and the corresponding median initial cost.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments & Results", "weight": 1.0} -->

The absence of a solution is treated as having an infinite cost.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Abstract Scenarios", "weight": 1.5} -->

We considered two abstract scenarios with different obstacle configurations in $\mathbb{R}^2$, $\mathbb{R}^4$, and $\mathbb{R}^8$ (fig:abstract\_scenarios). The scenario in fig:repeating\_rectangleswas tested with the starts and goals were sampled uniformly at random from both subregions and sampled uniformly at random over the whole search space. The subregion scenario often occurs in construction or warehouse settings where robots move between two regions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Abstract Scenarios", "weight": 1.5} -->

Each planner was run $100$ times with different pseudorandom seeds on a multiquery problem consisting of a sequence of $100$ different queries. The query sequence was defined for each problem by randomly sampling $100$ starts and goals, and the same random sequence was used for all $100$ runs of all planners. The maximum runtime per query was $0.5\text{s}$, $2\text{s}$, and $2\text{s}$ in $\mathbb{R}^2$, $\mathbb{R}^4$, and $\mathbb{R}^8$, respectively. The collision detection resolution was set to $5\cdot 10^{-6}$ in the abstract problems to imitate the computational cost of collision checking of the robotic experiment, as in [strub\_dphil21].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Abstract Scenarios", "weight": 1.5} -->

The median initial solution time per query along with confidence intervals for the repeating rectangles with subregion starts and goals in $\mathbb{R}^4$, and globally sampled starts and goals in $\mathbb{R}^8$ are shown in fig:main\_initial\_duration. tab:all\_summary summarizes both the cumulative median initial solution time across all queries (i.e., the integral of the plots shown infig:main\_initial\_duration), and the corresponding cumulative median initial cost along with the cumulative median final cost of all planners. The evolution of the cost for the 1$^\text{st}$ and the 50$^\text{th}$ query on the example of the wall gap in $\mathbb{R}^2$ is presented in fig:cost\_breakout.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Abstract Scenarios", "weight": 1.5} -->

The initial solution time achieved by EIRM* is faster than the time achieved by all the other planners. The initial cost for the subregion scenarios is comparable to RRT-Connect, while in the globally sampled setting the cost is higher than the cost of the other planners since they use more computational time to find a initial solution. In both the subregion and the globally sampled start-goal scenarios, EIRM*converges to a solution that is similar to the other optimizing planners when given the same amount of computational time.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Robotic Scenario", "weight": 1.0} -->

We considered a two-armed robot ($\mathbb{R}^{14}$) with the queries chosen such that they simulate rearranging objects on a bookshelf (fig:bookshelf). Each planner was run $100$ times with different pseudorandom seeds on a sequence of $50$ different queries and was run for $10\text{s}$ for each query. As for the abstract experiments, the sequence of random starts and goals was constant for all attempts. The Flexible Collision Library (FCL) [fcl] was used for collision checking, and the collision detection resolution was set to $0.036$ for the bookshelf scenario, as in [strub\_dphil21]. fig:bookshelf\_initial\_sol shows the initial solution time taken per query. tab:all\_summary again summarizes the cumulative initial solution time across all queries and the corresponding cumulative median initial and final costs. EIRM*achieves up to an order-of-magnitude faster initial solutions for some queries and is approximately twice as fast cumulatively compared to the other planners.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Initial Solutions", "weight": 1.0} -->

The relative benefits of explicitly reusing previous search effort and managing graph size are evaluated by limiting planners to only finding an initial solution. Not letting the planners run until convergence reduces the problems of unbounded graph growth for PRM* and LazyPRM*.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Initial Solutions", "weight": 1.0} -->

These experiments were run for the repeating rectangles scenario with subregion start-goal queries in $\mathbb{R}^8$and for the bookshelf experiment. The experimental setup is the same as previously for both scenarios, but with early stopping after finding a solution. fig:appendix\_non\_converged\_initial\_sol shows the initial-solution time plots for the experiments. EIRM*still achieves better median initial solution times in the bookshelf scenario and comparable times for the repeating rectangle scenario demonstrating the value of explicitly reusing information on more difficult problems.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Initial Solutions", "weight": 1.0} -->

Repeated rectangles (subregion) in $\mathbb{R}^8$ The success plot (top) and the median initial solution times per query (bottom) for two experiments when the planning process was stopped as soon as an initial solution was found. In the success plot, the line indicates the number of runs that have solved the query at the end of the given planning time. In the median initial solution plot, the solid line is the median initial solution time per query, and the shaded area is the nonparametric 99% confidence interval. Unsuccessful runs are treated as having infinite cost. For the bookshelf scenario, PRM* and RRT* were not run due to performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Initial Solutions", "weight": 1.0} -->

An illustration of the construction scenario showing the mobile manipulate picking up a brick with translucent bricks illustrating the target position of future bricks, (a). The associated planner performance, (b), shows the success (top) and median initial solution times per query (bottom) over 25 runs and the culmulative median initial times and culmulative initial and final costs are shown in Table (c). In the success plot, the line indicates the percentage of runs that have solved the query in the given planning time. In the median initial solution plot, the solid line is the median initial solution time per query and the shaded area is the nonparametric 99% confidence interval. Unsuccessful runs are treated as having infinite cost.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Construction Scenario", "weight": 1.0} -->

Task and Motion Planning (TAMP) problems often pose multiquery scenarios where the environments changes and existing edges in the roadmap may be invalidated. We demonstrate a basic modification of EIRM* in a simplified construction setting [21-hartmann-long] where a mobile manipulator ($\mathbb{R}^8$) stacks 36 bricks to build a wall(fig:wall\_stacking). The bricks that make up the wall are all the same, and are all picked up in the same location, simulating a conveyor belt that brings the bricks to the robot.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Construction Scenario", "weight": 1.0} -->

There are typically two planning problems in such a scenario. The first is picking up the bricks and stacking it on the wall, the second is returning to the pickup location. These two problems are often treated independently since the collision-checking envelope of the robot is different with and without a brick. We demonstrate the second scenario where the robot returns from placing a brick to pick up a new brick.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Construction Scenario", "weight": 1.0} -->

EIRM* was modified to remove the edges and vertices in its roadmap invalidated by newly placed bricks. It was not possible to efficiently make such modifications to PRM* and LazyPRM*, so EIRM* was only compared to the single-query planners which require no modifications, RRT-Connect and EIT*. The planners were run $25$ times with different pseudorandom seeds on a $36$ query sequence with $10$s for each query. FCL was used for collision checking.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Construction Scenario", "weight": 1.0} -->

The median initial time plot (fig:wall\_stacking) is promising. While the time needed by RRT-Connect increases as the wall is built and the environment becomes more complex, the time taken by EIRM* decreases with the number of queries. Future work will focus on fully adapting EIRM* to changing environments by developing more efficient ways to remove invalidated edges and vertices.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

EIRM* consistently outperforms all tested planners in the time necessary to find an initial solution. The difference to other planners is most pronounced when queries are between subregions, since the previous paths are more likely to be part of future solutions. An improvement of the initial query time can still be observed in problems with uniformly distributed starts and goals. The cost of the quick initial solution from EIRM*is usually higher than the cost of the paths from other planners but the final cost is similar to the cost of other almost-surely asymptotically optimal planners.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Initial Solution Time", "weight": 1.0} -->

fig:main\_initial\_duration and tab:all\_summary show that EIRM*finds initial solutions up to an order-of-magnitude faster than the other tested planners. It does this by explicitly seeking to reuse previous search effort and rewinding the approximation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Initial Solution Time", "weight": 1.0} -->

LazyPRM* fails to solve some of the tested problems reliably due to the growing graph size when improving solution cost. In the experiments where the planners were stopped when an initial solution is found to limit this growth, EIRM* still achieves similar or better results than LazyPRM* on initial solution time. EIRM* also needs fewer queries to benefit from previously invested effort compared to LazyPRM* since EIRM*explicitly tries to reuse validated edges.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Initial Solution Time", "weight": 1.0} -->

Rewinding the approximation of the environment to the first batch of samples makes the performance of the planner independent of the previous query's final resolution since every query starts from a coarse resolution. This may remove important paths that were found in later approximations, e.g., narrow passages. Future work could investigate promoting promising samples to earlier batches by ordering the samples in the buffer with an importancemetric. This could lead to both quicker and higher quality initial solutions. Similarly, pruning starts and goals too aggressively might lead to a loss of invested effort. In future work, we intend to investigate the start and goal pruning method.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Initial Solution Time", "weight": 1.0} -->

It might be beneficial to explore other heuristics for the possibly inadmissible effort, and the stopping conditions for the effort ordered reverse search. We noticed actively reducing validation effort means that in some experiments validation effort is no longer the main computational cost of This suggests that future work could include other time intensive steps of the algorithm in the effort heuristic, e.g., nearest neighbour lookups, which took up to 30%of the planning time in our setting. We currently run the reverse search until no solution candidate with a lower remaining validation effort exists. It might be faster overall to stop the reverse search earlier, and use an earlier solution candidate even if it may not be the path with the minimum remaining validation effort.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Objective Value", "weight": 1.0} -->

tab:all\_summary reports the initial and final costs of the solution. The initial path cost found by EIRM* is usually higher than LazyPRM*, but its final cost is within a few percentage points of the best found solution. In some cases, EIRM*appeared not to converge efficiently to the best solution when the optimal solution was close to the straight-line path. This may be due to rejection sampling from the sample buffer to obtain informed samples when refining the RGG. Future work may consider how to efficiently sample the informed set while maintaining the uniform distribution of samples in the buffer.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Objective Value", "weight": 1.0} -->

If a suboptimal solution is acceptable, it might be desirable to smoothly interpolate between an effort-ordered and a cost-ordered search to allow for more path reuse. This could be achieved with multi-objective A* The labels for the cost and effort would then not only depend on the state itself, but also on which path was taken to get to the state. It is future work to investigate how to best incorporate this approach in EIRM*.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Multiquery planners aim to efficiently solve multiple diverse motion planning problems in the same environment. This is generally achieved by keeping the approximation built during the previous queries. This can speed up the planning process, but few planners fully exploit the invested effort.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents EIRM*, a planner that explicitly aims to find paths with a low remaining validation effort. This is achieved by using an asymmetric search that calculates cost and effort heuristics in a computationally cheap reverse search. The heuristics are then used to guide the forward search, in which the edges are fully collision checked.=-1 EIRM* demonstrates that explicitly reusing computational effort and managing graph size between queries finds an initial solution quickly and then rapidly improves it. This is shown to outperform existing state-of-the-art planners on initial solution time while achieving similar solution quality on multiple different planning scenarios consisting of low- and high-dimensional abstract problems and robotic simulations. Information on the OMPL implementation of EIRM* is available at same
