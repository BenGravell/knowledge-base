<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-based Algorithms for Optimal Motion Planning

Topics include Motion planning, Asymptotically optimal, Probabilistically complete, Rapidly-exploring random tree star.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

During the last decade, sampling-based path planning algorithms, such as probabilistic roadmaps (PRM) and rapidly exploring random trees (RRT), have been shown to work well in practice and possess theoretical guarantees such as probabilistic completeness. However, little effort has been devoted to the formal analysis of the quality of the solution returned by such algorithms, e.g. as a function of the number of samples. The purpose of this paper is to fill this gap, by rigorously analyzing the asymptotic behavior of the cost of the solution returned by stochastic sampling-based algorithms as the number of samples increases. A number of negative results are provided, characterizing existing algorithms, e.g. showing that, under mild technical conditions, the cost of the solution returned by broadly used sampling-based algorithms converges almost surely to a non-optimal value. The main contribution of the paper is the introduction of new algorithms, namely, PRM* and RRT*, which are provably asymptotically optimal, i.e. such that the cost of the returned solution converges almost surely to the optimum.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, it is shown that the computational complexity of the new algorithms is within a constant factor of that of their probabilistically complete (but not asymptotically optimal) counterparts. The analysis in this paper hinges on novel connections between stochastic sampling-based path planning algorithms and the theory of random geometric graphs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The robotic motion planning problem has received a considerable amount of attention, especially over the last decade, as robots started becoming a vital part of modern industry as well as our daily life. Even though modern robots may possess significant differences in sensing, actuation, size, workspace, application, etc., the problem of navigating through a complex environment is embedded and essential in almost all robotics applications. Moreover, this problem is relevant to other disciplines such as verification, computational biology, and computer animation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set of goal states, the motion planning problem is to find a sequence of control inputs so as the drive the robot from its initial state to one of the goal states while obeying the rules of the environment, e.g., not colliding with the surrounding obstacles. An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and failure otherwise.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, the problem is known to be very hard from the computational point of view. For example, a basic version of the motion planning problem, called the generalized piano movers problem, is PSPACE-hard. In fact, while complete planning algorithms exist, their complexity makes them unsuitable for practical applications.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Practical planners came around with the development of cell decomposition methods and potential fields. These approaches, if properly implemented, relaxed the completeness requirement to, for instance, resolution completeness, i.e., the ability to return a valid solution, if one exists, if the resolution parameter of the algorithm is set fine enough. These planners demonstrated remarkable performance in accomplishing various tasks in complex environments within reasonable time bounds. However, their practical applications were mostly limited to state spaces with up to five dimensions, since decomposition-based methods suffered from large number of cells, and potential field methods from local minima. Important contributions towards broader applicability of these methods include navigation functions and randomization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above methods rely on an explicit representation of the obstacles in the configuration space, which is used directly to construct a solution. This may result in an excessive computational burden in high dimensions, and in environments described by a large number of obstacles. Avoiding such a representation is the main underlying idea leading to the development of sampling-based algorithms. See Lindemann and LaValle for a historical perspective. These algorithms proved to be very effective for motion planning in high-dimensional spaces, and attracted significant attention over the last decade, including very recent work. Instead of using an explicit representation of the environment, sampling-based algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and connect a set of points sampled from the obstacle-free space in order to build a graph (roadmap) of feasible trajectories. The roadmap is then used to construct the solution to the original motion-planning problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Informally speaking, sampling-based methods provide large amounts of computational savings by avoiding explicit construction of obstacles in the state space, as opposed to most complete motion planning algorithms. Even though these algorithms are not complete, they provide probabilistic completeness guarantees in the sense that the probability that the planner fails to return a solution, if one exists, decays to zero as the number of samples approaches infinity. Moreover, the rate of decay of the probability of failure is exponential, under the assumption that the environment has good "visibility" properties. More recently, the empirical success of sampling-based algorithms was argued to be strongly tied to the hypothesis that most practical robotic applications, even though involving robots with many degrees of freedom, feature environments with such good visibility properties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sampling-Based Algorithms", "weight": 1.0} -->

Arguably, the most influential sampling-based motion planning algorithms to date include Probabilistic RoadMaps (PRMs) and Rapidly-exploring Random Trees (RRTs). Even though the idea of connecting points sampled randomly from the state space is essential in both approaches, these two algorithms differ in the way that they construct a graph connecting these points.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sampling-Based Algorithms", "weight": 1.0} -->

The PRM algorithm and its variants are multiple-query methods that first construct a graph (the roadmap), which represents a rich set of collision-free trajectories, and then answer queries by computing a shortest path that connects the initial state with a final state through the roadmap. The PRM algorithm has been reported to perform well in high-dimensional state spaces. Furthermore, the PRM algorithm is probabilistically complete, and such that the probability of failure decays to zero exponentially with the number of samples used in the construction of the roadmap. During the last two decades, the PRM algorithm has been a focus of robotics research: several improvements were suggested by many authors and the reasons to why it performs well in many practical cases were better understood.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sampling-Based Algorithms", "weight": 1.0} -->

Even though multiple-query methods are valuable in highly structured environments, such as factory floors, most online planning problems do not require multiple queries, since, for instance, the robot moves from one environment to another, or the environment is not known a priori. Moreover, in some applications, computing a roadmap a priori may be computationally challenging or even infeasible. Tailored mainly for these applications, incremental sampling-based planning algorithms such as RRTs have emerged as an online, single-query counterpart to PRMs. The incremental nature of these algorithms avoids the necessity to set the number of samples a priori, and returns a solution as soon as the set of trajectories built by the algorithm is rich enough, enabling on-line implementations. Moreover, tree-based planners do not require connecting two states exactly and more easily handle systems with differential constraints. The RRT algorithm has been shown to be probabilistically complete, with an exponential rate of decay for the probability of failure. The basic version of the RRT algorithm has been extended in several directions, and found many applications in the robotics domain and elsewhere.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling-Based Algorithms", "weight": 1.0} -->

In particular, RRTs have been shown to work effectively for systems with differential constraints and nonlinear dynamics as well as purely discrete or hybrid systems. Moreover, the RRT algorithm was demonstrated in major robotics events on various experimental robotic platforms.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sampling-Based Algorithms", "weight": 1.0} -->

Other sampling-based planners of note include Expansive Space Trees (EST) and Sampling-based Roadmap of Trees (SRT). The latter combines the main features of multiple-query algorithms such as PRM with those of single-query algorithms such as RRT and EST.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimal Motion Planning", "weight": 1.0} -->

In most applications, the quality of the solution returned by a motion planning algorithm is important. For example, one may be interested in solution paths of minimum cost, with respect to a given cost functional, such as the length of a path, or the time required to execute it. The problem of computing optimal motion plans has been proven in Canny and Reif to be very challenging even in basic cases.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal Motion Planning", "weight": 1.0} -->

In the context of sampling-based motion planning algorithms, the importance of computing optimal solutions has been pointed out in early seminal papers. However, optimality properties of sampling-based motion planning algorithms have not been systematically investigated, and most of the relevant work relies on heuristics. For example, in many field implementations of sampling-based planning algorithms, it is often the case that since a feasible path is found quickly, additional available computation time is devoted to improving the solution with heuristics until the solution is executed. Urmson and Simmons proposed heuristics to bias the tree growth in RRT towards those regions that result in low-cost solutions. They have also shown experimental results evaluating the performance of different heuristics in terms of the quality of the solution returned. Ferguson and Stentz considered running the RRT algorithm multiple times in order to progressively improve the quality of the solution. They showed that each run of the algorithm results in a path with smaller cost, even though the procedure is not guaranteed to converge to an optimal solution. Criteria for restarting multiple RRT runs, in a different context, were also proposed in Wedge and Branicky.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimal Motion Planning", "weight": 1.0} -->

A more recent approach is the transition-based RRT (T-RRT) designed to combine rapid exploration properties of the RRT with stochastic global optimization methods.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal Motion Planning", "weight": 1.0} -->

A different approach that also offers optimality guarantees is based on graph search algorithms, such as A^∗^, applied over a finite discretization (based, e.g., on a grid, or a cell decomposition of the configuration space) that is generated offline. Recently, these algorithms received a large amount of attention. In particular, they were extended to run in an anytime fashion, deal with dynamic environments, and handle systems with differential constraints. These have also been successfully demonstrated on various robotic platforms. However, optimality guarantees of these algorithms are only ensured up to the grid resolution. Moreover, since the number of grid points grows exponentially with the dimensionality of the state space, so does the (worst-case) running time of these algorithms.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties of the major paradigms for sampling-based path planning algorithms, for multiple- or single-query applications, and introduces the first algorithms that are both asymptotically optimal and computationally efficient, with respect to other algorithms in this class. A summary of the contributions can be found below, and is shown in Table 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

As a first set of results, it is proven that the standard PRM and RRT algorithms are not asymptotically optimal, and that the "simplified" PRM algorithm is asymptotically optimal, but computationally expensive. Moreover, it is shown that the $k$-nearest variant of the (simplified) PRM algorithm is not necessarily probabilistically complete (e.g., it is not probabilistically complete for $k = 1$), and is not asymptotically optimal for any fixed $k$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

In order to address the limitations of sampling-based path planning algorithms available in the literature, new algorithms are proposed, i.e., PRM^∗^, RRG, and RRT^∗^, and proven to be probabilistically complete, asymptotically optimal, and computationally efficient. Of these, PRM^∗^ is a batch variable-radius PRM, applicable to multiple-query problems, in which the radius is scaled with the number of samples in a way that provably ensures both asymptotic optimality and computational efficiency. RRG is an incremental algorithm that builds a connected roadmap, providing similar performance to PRM^∗^ in a single-query setting, and in an anytime fashion (i.e., a first solution is provided quickly, and monotonically improved if more computation time is available). The RRT^∗^ algorithm is a variant of RRG that incrementally builds a tree, providing anytime solutions, provably converging to an optimal solution, with minimal computational and memory requirements.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

In this paper, the problem of planning a path through a connected bounded subset of a $d$-dimensional Euclidean space is considered. As in the early seminal papers on incremental sampling-based motion planning algorithms such as Kuffner and LaValle, no differential constraints are considered (i.e., the focus of the paper is on path planning problems), but our methods can be easily extended to planning in configuration spaces and applied to several practical problems of interest. The extension to systems with differential constraints is deferred to future work (see Karaman and Frazzoli for preliminary results).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

Finally, the results presented in this article, and the techniques used in the analysis of the algorithms, hinge on novel connections established between sampling-based path planning algorithms in robotics and the theory of random geometric graphs, which may be of independent interest.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

A preliminary version of this article has appeared in Karaman and Frazzoli. Since then a variety of new algorithms based on the the ideas behind PRM^∗^, RRG, and RRT^∗^ have been proposed in the literature. For instance, a probabilistically complete and probabilistically sound algorithm for solving a class of differential games has appeared in Karaman and Frazzoli. Algorithms based on the RRG were used to solve belief-space planning problems in Bry and Roy. The RRT^∗^ algorithm was used for anytime motion planning in Karaman et al., where it was also demonstrated experimentally on a full-size robotic fork truck. In Alterovitz et al., the analysis given in Karaman and Frazzoli was used to guarantee computational efficiency and asymptotic optimality of a new algorithm that can trade off between exploration and optimality during planning.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

A software library implementing the new algorithms introduced in this paper has been released as open-source software by the authors, and is currently available at

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

This paper is organized as follows. Section 2 lays the ground in terms of notation and problem formulation. Section 3 is devoted to the discussion of the algorithms that are considered in the paper: first, the main paradigms for sampling-based motion planning algorithms available in the literature are presented, together with their main variants. Then, the new proposed algorithms are presented and motivated. In Section 4 the properties of these algorithms are rigorously analyzed, formally establishing their probabilistic completeness and asymptotically optimality (or lack thereof), as well as their computational complexity as a function of the number of samples and of the number of obstacles in the environment. Experimental results are presented in Section 5, to illustrate and validate the theoretical findings. Finally, Section 6 contains conclusions and perspectives for future work. In order not to excessively disrupt the flow of the presentation, a summary of notation used throughout the paper, as well as lengthy proofs of important results are presented in the Appendix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Preliminary Material", "weight": 1.0} -->

This section contains some preliminary material that will be necessary for the discussion in the remainder of the paper. Namely, the problems of feasible and optimal motion planning is introduced, and some important results from the theory of random geometric graphs are summarized. The notation used in the paper is summarized in Appendix A.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this section, the feasible and optimal path planning problems are formalized.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathcal{X} = {}^{d}$ be the *configuration space*, where $d \in {\mathbb{N}}$, $d \geq 2$. Let $\mathcal{X}_{obs}$ be the obstacle region, such that $\mathcal{X} \smallsetminus \mathcal{X}_{obs}$ is an open set, and denote the obstacle-free space as $\mathcal{X}_{free} = {{cl}{({\mathcal{X} \smallsetminus \mathcal{X}_{obs}})}}$, where ${cl}{( \cdot )}$ denotes the closure of a set. The initial condition $x_{init}$ is an element of $\mathcal{X}_{free}$, and the goal region $\mathcal{X}_{goal}$ is an open subset of $\mathcal{X}_{free}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A path planning problem is defined by a triplet $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$; the total variation of $\sigma$ is defined as A function $\sigma$ with ${{TV}{(\sigma)}} < \infty$ is said to have bounded variation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Random Geometric Graphs", "weight": 1.0} -->

The objective of this section is to summarize some of the results on random geometric graphs that are available in the literature, and are relevant to the analysis of sampling-based path planning algorithms. In the remainder of this article, several connections are made between the theory of random geometric graphs and path-planning algorithms in robotics, providing insight on a number of issues, including, e.g., probabilistic completeness and asymptotic optimality, as well as technical tools to analyze the algorithms and establish their properties. In fact, it turns out that the data structures constructed by most sampling-based motion planning algorithms in the literature coincide, in the absence of obstacles, with standard models of random geometric graphs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Random Geometric Graphs", "weight": 1.0} -->

Random geometric graphs are in general defined as stochastic collections of points in a metric space, connected pairwise by edges if certain conditions (e.g., on the distance between the points) are satisfied. Such objects have been studied since their introduction by Gilbert; see, e.g., Penrose and Balister et al. for an overview of recent results. From the theoretical point of view, the study of random geometric graphs makes a connection between random graphs and percolation theory. On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithms", "weight": 1.0} -->

In this section, a number of sampling-based motion planning algorithms are introduced. First, some common primitive procedures are defined. Then, the PRM and the RRT algorithms are outlined, as they are representative of the major paradigms for sampling-based motion planning algorithms in the literature. Then, new algorithms, namely PRM^∗^ and RRT^∗^, are introduced, as asymptotically optimal and computationally efficient versions of their "standard" counterparts.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Primitive Procedures", "weight": 1.0} -->

Before discussing the algorithms, it is convenient to introduce the primitive procedures that they rely.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Nearest Neighbor", "weight": 1.0} -->

Given a graph $G = {(V,E)}$, where $V \subset \mathcal{X}$, a point $x \in \mathcal{X}$, the function ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}:{{(G,x)}\mapsto v \in V}$ returns the vertex in $V$ that is "closest" to $x$ in terms of a given distance function.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Nearest Neighbor", "weight": 1.0} -->

In this paper, the Euclidean distance is used (see, e.g., LaValle and Kuffner for alternative choices), and hence A set-valued version of this function is also considered, ${\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}:{{(G,x,k)}\mapsto{\{ v_{1},v_{2},\ldots,v_{k}\}}}$, returning the $k$ vertices in $V$ that are nearest to $x$, according to the same distance function as above. (By convention, if the cardinality of $V$ is less than $k$, then the function returns $V$.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Near Vertices", "weight": 1.0} -->

Given a graph $G = {(V,E)}$, where $V \subset \mathcal{X}$, a point $x \in \mathcal{X}$, and a positive real number $r \in {\mathbb{R}}_{> 0}$, the function ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}:{{(G,x,r)}\mapsto V' \subseteq V}$ returns the vertices in $V$ that are contained in a ball of radius $r$ centered at $x$, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Steering", "weight": 1.0} -->

Given two points ${x,y} \in \mathcal{X}$, the function ${\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}}:{{(x,y)}\mapsto z}$ returns a point $z \in \mathcal{X}$ such that $z$ is "closer" to $y$ than $x$ is. Throughout the paper, the point $z$ returned by the function $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ will be such that $z$ minimizes $\|{z - y}\|$ while at the same time maintaining ${\|{z - x}\|} \leq \eta$, for a prespecified $\eta > 0$,^11^1This steering procedure is used widely in the robotics literature, since its introduction in Kuffner and LaValle.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Steering", "weight": 1.0} -->

Our results also extend to the Rapidly-exploring Random Dense Trees, which are slightly modified versions of the RRTs that do not require tuning any prespecified parameters such as $\eta$ in this case. i.e.,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Existing Algorithms", "weight": 1.0} -->

Next, some of the sampling-based algorithms available in the literature are outlined. For convenience, inputs and outputs of the algorithms are not shown explicitly, but are as follows. All algorithms take as input a path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, an integer $n \in {\mathbb{N}}$, and a cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, if appropriate. These inputs are shared with functions and procedures called within the algorithms. All algorithms return a graph $G = {(V,E)}$, where $V \subset \mathcal{X}_{free}$, ${{card}(V)} \leq {n + 1}$, and $E \in {V \times V}$. The solution of the path planning problem can be easily computed from such a graph, e.g., using standard shortest-path algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

The Probabilistic RoadMaps algorithm is primarily aimed at multi-query applications. In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among $n$ randomly-sampled points in $\mathcal{X}_{free}$, and a query phase, in which paths connecting initial and final conditions through the roadmap are sought. "Expansion" heuristics for enhancing the roadmap's connectivity are available in the literature but have no impact on the analysis in this paper, and will not be discussed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

The pre-processing phase, outlined in Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), begins with an empty graph. At each iteration, a point $x_{rand} \in \mathcal{X}_{free}$ is sampled, and added to the vertex set $V$. Then, connections are attempted between $x_{rand}$ and other vertices in $V$ within a ball of radius $r$ centered at $x_{rand}$, in order of increasing distance from $x_{rand}$, using a simple local planner (e.g., straight-line connection). Successful (i.e., collision-free) connections result in the addition of a new edge to the edge set $E$. To avoid unnecessary computations (since the focus of the algorithm is establishing connectivity), connections between $x_{rand}$ and vertices in the same connected component are avoided. Hence, the roadmap constructed by PRM is a forest, i.e., a collection of trees.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

6 foreach u ∈ U, in order of increasing ∥u − xrand∥, do 7 if xrand and u are not in the same connected component of G = (V, E) then 8 if CollisionFree (xrand, u) then E ← E ∪ {(xrand, u), (u, xrand)}; Algorithm 1 PRM (preprocessing phase) Analysis results in the literature are only available for a "simplified" version of the PRM algorithm, referred to as sPRM in this paper. The simplified algorithm initializes the vertex set with the initial condition, samples $n$ points from $\mathcal{X}_{free}$, and then attempts to connect points within a distance $r$, i.e., using a similar logic as PRM, with the difference that connections between vertices in the same connected component are allowed. Notice that in the absence of obstacles, i.e., if $\mathcal{X}_{free} = \mathcal{X}$, the roadmap constructed in this way is a random $r$-disc graph.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

Practical implementation of the (s)PRM algorithm have often considered different choices for the set $U$ of vertices to which connections are attempted (i.e., line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") in Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), and line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") in Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")). In particular, the following criteria are of particular interest: $k$-Nearest (s)PRM: Choose the nearest $k$ neighbors to the vertex under consideration, for a given $k$ (a typical value is reported as $k = 15$).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

In other words, $U\leftarrow{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{({G = {{(V,E)},x_{rand},k}})}}$ in line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") and $U\leftarrow{{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{({G = {{(V,E)},v,k}})}} \smallsetminus {\{ v\}}}$ in line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion

<!-- chunk {"id": "body-0047", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

Planning") of Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"). The roadmap constructed in this way in an obstacle-free environment is a random $k$-nearest graph.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

Bounded-degree (s)PRM: For any fixed $r$, the average number of connections attempted at each iteration is proportional to the number of vertices in $V$, and can result in an excessive computational burden for large $n$. To address this, an upper bound $k$ can be imposed on the cardinality of the set $U$ (a typical value is reported as $k = 20$ ).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

In other words, $U\leftarrow{{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}{(G,x_{rand},r)}} \cap {{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{(G,x_{rand},k)}}}$ in line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), and $U\leftarrow{{({{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}{(G,v,r)}} \cap

<!-- chunk {"id": "body-0050", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{(G,v,k)}}})} \smallsetminus {\{ v\}}}$ in line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Probabilistic RoadMaps (PRM)", "weight": 1.0} -->

Variable-radius (s)PRM: Another option to maintain the degree of the vertices in the roadmap small is to make the connection radius $r$ a function of $n$, as opposed to a fixed parameter. However, there are no clear indications in the literature on the appropriate functional relationship between $r$ and $n$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Rapidly-exploring Random Trees (RRT)", "weight": 1.0} -->

The Rapidly-exploring Random Tree algorithm is primarily aimed at single-query applications. In its basic version, the algorithm incrementally builds a tree of feasible trajectories, rooted at the initial condition. An outline of the algorithm is given in Algorithm 3: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"). The algorithm is initialized with a graph that includes the initial state as its single vertex, and no edges. At each iteration, a point $x_{rand} \in \mathcal{X}_{free}$ is sampled. An attempt is made to connect the nearest vertex $v \in V$ in the tree to the new sample. If such a connection is successful, $x_{rand}$ is added to the vertex set, and $(v,x_{rand})$ is added to the edge set. In the original version of this algorithm, the iteration is stopped as soon as the tree contains a node in the goal region. In this paper, for consistency with the other algorithms (e.g., PRM), the iteration is performed $n$ times.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Rapidly-exploring Random Trees (RRT)", "weight": 1.0} -->

In the absence of obstacles, i.e., if $\mathcal{X}_{free} = \mathcal{X}$, the tree constructed in this way is an online nearest neighbor graph.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Rapidly-exploring Random Trees (RRT)", "weight": 1.0} -->

4 xnearest ← Nearest (G = (V, E), xrand); 5 xnew ← Steer (xnearest, xrand); 6 if ObtacleFree (xnearest, xnew) then 7 V ← V ∪ {xnew}; E ← E ∪ {(xnearest, xnew)}; A variant of RRT consists of growing two trees, respectively rooted at the initial state, and at a state in the goal set. To highlight the fact that the sampling procedure must not necessarily be stochastic, the algorithm is also referred to as Rapidly-exploring Dense Trees (RDT).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Proposed algorithms", "weight": 1.0} -->

In this section, the new algorithms considered in this paper are presented. These algorithms are proposed as asymptotically optimal and computationally efficient versions of their "standard" counterparts, as will be made clear through the analysis in the next section. Input and output data are the same as in the algorithms introduced in Section 3.2.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

In the standard PRM algorithm, as well as in its simplified "batch" version considered in this paper, connections are attempted between roadmap vertices that are within a fixed radius $r$ from one another. The constant $r$ is thus a parameter of PRM.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

The proposed algorithm---shown in Algorithm 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")---is similar to sPRM, with the only difference being that the connection radius $r$ is chosen as a function of $n$, i.e., $r = {r{(n)}}:={\gamma_{PRM}{({{\log{(n)}}/n})}^{1/d}}$, where $\gamma_{PRM} > \gamma_{PRM}^{\ast} = {2{({1 + {1/d}})}^{1/d}\left( {{\mu{(\mathcal{X}_{free})}}/\zeta_{d}} \right)^{1/d}}$, $d$ is the dimension of the space $\mathcal{X}$, $\mu{(\mathcal{X}_{free})}$ denotes the Lebesgue measure (i.e., volume) of the

<!-- chunk {"id": "body-0058", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

obstacle-free space, and $\zeta_{d}$ is the volume of the unit ball in the $d$-dimensional Euclidean space.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

Clearly, the connection radius decreases with the number of samples. The rate of decay is such that the average number of connections attempted from a roadmap vertex is proportional to $\log{(n)}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

Note that in the discussion of variable-radius PRM in LaValle, it is suggested that the radius be chosen as a function of sample dispersion. (Recall that the dispersion of a point set contained in a bounded set $\mathcal{S} \subset {\mathbb{R}}^{d}$ is the radius of the largest empty ball centered in $\mathcal{S}$.) Indeed, the dispersion of a set of $n$ random points sampled uniformly and independently in a bounded set is $O{({({{\log{(n)}}/n})}^{1/d})}$, which is precisely the rate at which the connection radius is scaled in the PRM^∗^ algorithm.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

3 U ← Near (G = (V, E), v, γPRM (log (n)/n)1/d) ∖ {v}; Another version of the algorithm, called $k$-nearest PRM^∗^, can be considered, motivated by the $k$-nearest PRM implementation previously mentioned, whereby the number $k$ of nearest neighbors to be considered is not a constant, but is chosen as a function of the cardinality of the roadmap $n$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

More precisely, ${k{(n)}}:={k_{PRM}{\log{(n)}}}$, where $k_{PRM} > k_{PRM}^{\ast} = {e{({1 + {1/d}})}}$, and $U\leftarrow{{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{({G = {{(V,E)},v,{k_{PRM}{\log{(n)}}}}})}} \smallsetminus {\{ v\}}}$ in line 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

<!-- chunk {"id": "body-0063", "role": "body", "section": "Optimal Probabilistic RoadMaps (PRM^∗^)", "weight": 1.0} -->

Note that $k_{PRM}^{\ast}$ is a constant that only depends on $d$, and does not otherwise depend on the problem instance, unlike $\gamma_{PRM}^{\ast}$. Moreover, $k_{PRM} = {2e}$ is a valid choice for all problem instances.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Rapidly-exploring Random Graph (RRG)", "weight": 1.0} -->

The Rapidly-exploring Random Graph algorithm was introduced as an incremental (as opposed to batch) algorithm to build a connected roadmap, possibly containing cycles. The RRG algorithm is similar to RRT in that it first attempts to connect the nearest node to the new sample. If the connection attempt is successful, the new node is added to the vertex set. However, RRG has the following difference.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Rapidly-exploring Random Graph (RRG)", "weight": 1.0} -->

Every time a new point $x_{new}$ is added to the vertex set $V$, then connections are attempted from all other vertices in $V$ that are within a ball of radius ${r{({{card}(V)})}} = {\min{\{{\gamma_{RRG}{({{\log{({{card}(V)})}}/{{card}(V)}})}^{1/d}},\eta\}}}$, where $\eta$ is the constant appearing in the definition of the local steering function, and $\gamma_{RRG} > \gamma_{RRG}^{\ast} = {2{({1 + {1/d}})}^{1/d}\left( {{\mu{(\mathcal{X}_{free})}}/\zeta_{d}} \right)^{1/d}}$. For each successful connection, a new edge is added to the edge set $E$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Rapidly-exploring Random Graph (RRG)", "weight": 1.0} -->

Hence, it is clear that, for the same sampling sequence, the RRT graph (a directed tree) is a subgraph of the RRG graph (an undirected graph, possibly containing cycles). In particular, the two graphs share the same vertex set, and the edge set of the RRT graph is a subset of that of the RRG graph.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Rapidly-exploring Random Graph (RRG)", "weight": 1.0} -->

4 xnearest ← Nearest (G = (V, E), xrand); 5 xnew ← Steer (xnearest, xrand); 6 if ObtacleFree (xnearest, xnew) then 7 Xnear ← Near (G = (V, E), xnew, min {γRRG (log (card(V))/card(V))1/d, η}); 8 V ← V ∪ {xnew}; E ← E ∪ {(xnearest, xnew), (xnew, xnearest)}; 9 foreach xnear ∈ Xnear do 10 if CollisionFree (xnear, xnew) then E ← E ∪ {(xnear, xnew), (xnew, xnear)} Another version of the algorithm, called $k$-nearest RRG, can be considered, in which connections are sought to $k$ nearest neighbors, with $k =

<!-- chunk {"id": "body-0068", "role": "body", "section": "Rapidly-exploring Random Graph (RRG)", "weight": 1.0} -->

Note that $k_{RRG}^{\ast}$ is a constant that depends only on $d$, and does not depend otherwise on the problem instance, unlike $\gamma_{RRG}^{\ast}$. Moreover, $k_{RRG} = {2e}$ is a valid choice for all problem instances.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

Maintaining a tree structure rather than a graph is not only economical in terms of memory requirements, but may also be advantageous in some applications, due to, for instance, relatively easy extensions to motion planning problems with differential constraints, or to cope with modeling errors. The RRT^∗^ algorithm is obtained by modifying RRG in such a way that formation of cycles is avoided, by removing "redundant" edges, i.e., edges that are not part of a shortest path from the root of the tree (i.e., the initial state) to a vertex. Since the RRT and RRT^∗^ graphs are directed trees with the same root and vertex set, and edge sets that are subsets of that of RRG, this amounts to a "rewiring" of the RRT tree, ensuring that vertices are reached through a minimum-cost path.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

4 xnearest ← Nearest (G = (V, E), xrand); 5 xnew ← Steer (xnearest, xrand); 6 if ObtacleFree (xnearest, xnew) then 7 Xnear ← Near (G = (V, E), xnew, min {γRRT* (log (card(V))/card(V))1/d, η}); 9 xmin ← xnearest; cmin ← Cost (xnearest) + c (Line (xnearest, xnew)); 10 foreach xnear ∈ Xnear do // Connect along a minimum-cost path 11 if CollisionFree (xnear, xnew) ∧ Cost (xnear) + c (Line (xnear, xnew)) < cmin then 12 xmin ← xnear; cmin ← Cost (xnear) + c (Line (xnear, xnew)) 15 foreach xnear ∈ Xnear do // Rewire the tree 16 if CollisionFree (xnew, xnear) ∧ Cost

<!-- chunk {"id": "body-0071", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

(xnew) + c (Line (xnew, xnear)) < Cost (xnear) then xparent ← Parent (xnear); 17 E ← (E ∖ {(xparent, xnear)}) ∪ {(xnew, xnear)} The RRT^∗^ algorithm, shown in Algorithm 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), adds points to the vertex set $V$ in the same way as RRT and RRG.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

It also considers connections from the new vertex $x_{new}$ to vertices in $X_{near}$, i.e., other vertices that are within distance ${r{({{card}(V)})}} = {\min{\{{\gamma_{{RRT}^{\ast}}{({{\log{({{card}(V)})}}/{{card}(V)}})}^{1/d}},\eta\}}}$ from $x_{new}$. However, not all feasible connections result in new edges being inserted in the edge set $E$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

In particular, (i) an edge is created from the vertex in $X_{near}$ that can be connected to $x_{new}$ along a path with minimum cost, and (ii) new edges are created from $x_{new}$ to vertices in $X_{near}$, if the path through $x_{new}$ has lower cost than the path through the current parent; in this case, the edge linking the vertex to its current parent is deleted, to maintain the tree structure.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Optimal RRT (RRT^∗^)", "weight": 1.0} -->

Another version of the algorithm, called $k$-nearest RRT^∗^, can be considered, in which connections are sought to $k$ nearest neighbors, with ${k{({{card}(V)})}} = {k_{RRG}{\log{({{card}(V)})}}}$, and $X_{near}\leftarrow{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{({G = {{(V,E)},x_{new},{k_{RRG}{\log{(i)}}}}})}}$, in line 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

<!-- chunk {"id": "body-0075", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section, a number of results concerning the probabilistic completeness, asymptotic optimality, and complexity of the algorithms in Section 3 are presented.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Analysis", "weight": 1.0} -->

The return value of Algorithms 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")-6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") is a graph. Since the sampling procedure $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ is stochastic, the returned graph is in fact a random variable.^22^2We will not address the case in which the sampling procedure is deterministic, but refer the reader to LaValle et al., which contains an in-depth discussion of the relative merits of randomness and determinism in sampling-based motion planning algorithms. Since the sampling procedure is modeled as a map from the sample space $\Omega$ to infinite sequences in $\mathcal{X}$, sets of vertices and edges of the graphs maintained by the algorithms can be defined as functions from the sample space $\Omega$ to appropriate sets.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Analysis", "weight": 1.0} -->

More precisely, let $ALG$ be a label indicating one of the algorithms in Section 3, and let ${\{{V_{i}^{ALG}{(\omega)}}\}}_{i \in {\mathbb{N}}}$ and ${\{{E_{i}^{ALG}{(\omega)}}\}}_{i \in {\mathbb{N}}}$ be, respectively, the sets of vertices and edges in the graph returned by algorithm $ALG$, indexed by the number of samples, for a particular realization of the sample sequence. (In other words, these are sequences of functions defined from $\Omega$ into finite subsets of $\mathcal{X}_{free}$ or $\mathcal{X}_{free} \times \mathcal{X}_{free}$.) Similarly, let $G_{i}^{ALG} = {(V_{i}^{ALG},E_{i}^{ALG})}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Analysis", "weight": 1.0} -->

(The label $ALG$ will be at times omitted when the algorithm being used is clear from the context.)

<!-- chunk {"id": "body-0079", "role": "body", "section": "Analysis", "weight": 1.0} -->

All algorithms considered in the paper are sound, in the sense that they only return graphs with vertices and edges representing points and paths in $\mathcal{X}_{free}$.This statement can be easily verified by inspection of the algorithms in Section 3.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Probabilistic Completeness", "weight": 1.0} -->

In this section, the feasibility problem is considered, and the (probabilistic) completeness properties of the algorithms in Section 3 are analyzed. First, some preliminary definitions are given, followed by a definition of probabilistic completeness. Then, completeness properties of various sampling-based motion planning algorithms are stated.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Probabilistic Completeness", "weight": 1.0} -->

In other words, the $\delta$-interior of $\mathcal{X}_{free}$ is the set of all states that are at least a distance $\delta$ away from any point in the obstacle set (see Figure 1). A collision-free path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}_{free}}$ is said to have strong $\delta$-clearance, if $\sigma$ lies entirely inside the $\delta$-interior of $\mathcal{X}_{free}$, i.e., ${\sigma{(\tau)}} \in {{int}_{\delta}{(\mathcal{X}_{free})}}$ for all $\tau \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Probabilistic Completeness", "weight": 1.0} -->

A path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$ is said to be robustly feasible if there exists a path with strong $\delta$-clearance, for some $\delta > 0$, that solves it. In terms of the notation used in this paper, the notion of probabilistic completeness can be stated as follows.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

In this section, the optimality problem of path planning is considered. The algorithms presented in Section 3 are analyzed, in terms of their ability to return solutions whose cost converge to the global optimum. First, a definition of asymptotic optimality is provided as almost-sure convergence to optimal paths. Second, it is shown that the RRT algorithm lacks the asymptotic optimality property. Third, the PRM^∗^, RRG, and RRT^∗^ algorithms, as well as their $k$-nearest implementations, are shown to be asymptotically optimal.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

Recall from Section 4.1 that an algorithm is probabilistically complete if the algorithm finds with high probability a solution to path planning problems that are robustly feasible, i.e., for which feasible path exists with strong $\delta$-clearance. A similar approach is used to define asymptotic optimality, relying on a notion of weak $\delta$-clearance and on a continuity property for the cost of paths, which will be introduced below.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

Let ${\sigma_{1},\sigma_{2}} \in \Sigma_{free}$ be two collision-free paths with the same end points. A path $\sigma_{1}$ is said to be homotopic to $\sigma_{2}$, if there exists a continuous function $\psi:{{\lbrack 0,1\rbrack}\rightarrow\Sigma_{free}}$, called the homotopy, such that ${\psi{}} = \sigma_{1}$, ${\psi{}} = \sigma_{2}$, and $\psi{(\tau)}$ is a collision-free path in for all $\tau \in {\lbrack 0,1\rbrack}$. Intuitively, a path that is homotopic to $\sigma$ can be continuously transformed to $\sigma$ through $\mathcal{X}_{free}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

A collision-free path $\sigma:{{\lbrack 0,s\rbrack}\rightarrow\mathcal{X}_{free}}$ is said to have weak $\delta$-clearance, if there exists a path $\sigma'$ that has strong $\delta$-clearance and there exist a homotopy $\psi$, with ${\psi{}} = \sigma$, ${\psi{}} = \sigma'$, and for all $\alpha \in {(0,1\rbrack}$ there exists $\delta_{\alpha} > 0$ such that $\psi{(\alpha)}$ has strong $\delta_{\alpha}$-clearance. See Figure 2 for an illustration of the weak $\delta$-clearance property. A path that violates the weak $\delta$-clearance property is shown in Figure 3. Weak $\delta$-clearance does not require points along a path to be at least a distance $\delta$ away from the obstacles (see Figure 4).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

In fact, a collision-free path with uncountably many points lying on the boundary of an obstacle can still have weak $\delta$-clearance.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

Next, the set of all paths with bounded length is introduced as a normed space, which allows taking the limit of a sequence of paths. Recall that $\Sigma$ is the set of all paths, and $TV{(\cdot)}$ denotes the total variation, i.e., the length, of a path (see Section 2.1).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

Given a path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ and a scalar $\alpha \in {\mathbb{R}}$, the multiplication by a scalar operation is defined as ${{({\alpha\sigma})}{(\tau)}}:={\alpha\sigma{(\tau)}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. With these addition and multiplication by a scalar operations, the function space $\Sigma$ is, in fact, a vector space.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

A feasible path $\sigma^{\ast} \in \mathcal{X}_{free}$ that solves the optimality problem (Problem 3 ‣ 2.1 Problem Formulation ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning")) is said to be a robustly optimal solution if it has weak $\delta$-clearance and, for any sequence of collision-free paths ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$, $\sigma_{n} \in \mathcal{X}_{free}$, ${\forall n} \in {\mathbb{N}}$, such that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$, ${\lim_{n\rightarrow\infty}{c{(\sigma_{n})}}} = {c{(\sigma^{\ast})}}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

Clearly, a path planning problem that has a robustly optimal solution is necessarily robustly feasible. Let $c^{\ast} = {c{(\sigma^{\ast})}}$ be the cost of an optimal path, and let $Y_{n}^{ALG}$ be the extended random variable corresponding to the cost of the minimum-cost solution included in the graph returned by $ALG$ at the end of iteration $n$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Assumption 27 (Zero-measure Optimal Paths)", "weight": 1.0} -->

The set of all points traversed by an optimal trajectory has measure zero, i.e., ${\mu\left( \mathcal{X}_{opt} \right)} = 0$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Assumption 27 (Zero-measure Optimal Paths)", "weight": 1.0} -->

Most cost functions and problem instances of interest satisfy this assumption, including, e.g., the Euclidean length of the path when the goal region is convex. This assumption does not imply that there is a single optimal path; indeed, there are problem instances with uncountably many optimal paths, for which Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") holds. (A simple example is the motion planning problem in three dimensional Euclidean space where a ball shaped obstacle is placed between the initial state and the goal region.) Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") implies that no sampling-based planning algorithm can find a solution to the optimality problem in a finite number of iterations.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Existing algorithms", "weight": 1.0} -->

The algorithms in Section 3.2 were originally introduced to efficiently solve the feasibility problem, relaxing the completeness requirement to probabilistic completeness. Nevertheless, it is of interest to establish whether these algorithms are asymptotically optimal in addition to being probabilistically complete. (The first two results in this section rely on results that will be proven in Section 4.2.2, i.e., the fact that the RRT algorithm is not asymptotically optimal, and the PRM^∗^ algorithm is asymptotically optimal) First, consider the PRM algorithm and its variants. The PRM algorithm, in its original form, is not asymptotically optimal.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Rapidly-exploring Random Trees", "weight": 1.0} -->

In this section, it is shown that the minimum-cost path in the RRT algorithm converges to a certain random variable, however, under mild technical assumptions, this random variable is not equal to the optimal cost, with probability one.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Proposed algorithms", "weight": 1.0} -->

In this section, the proposed algorithms are analyzed for asymptotic optimality, i.e., almost sure convergence to optimal solutions. It is shown that the PRM^∗^, RRG, and RRT^∗^ algorithms, as well as their $k$-nearest implementations, are all asymptotically optimal. The proofs of the following theorems are quite lengthy, and will be provided in the appendix.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Proposed algorithms", "weight": 1.0} -->

Recall that $d$ denotes the dimensionality of the configuration space, $\mu{(\mathcal{X}_{free})}$ denotes the Lebesgue measure of the obstacle-free space, and $\zeta_{d}$ denotes the volume of the unit ball in the $d$-dimensional Euclidean space. Proofs of the following theorems can be found in Appendices C ‣ Sampling-based Algorithms for Optimal Motion Planning")--G ‣ Sampling-based Algorithms for Optimal Motion Planning").

<!-- chunk {"id": "body-0098", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

The objective of this section is to compare the computational complexity of the algorithms provided in Section 3. First, each algorithm is analyzed in terms of the number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure. Second, the computational complexity of certain primitive procedures such as $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ and $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ (see Section 3.1) are analyzed. Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number of simple operations, such as comparisons, additions, multiplications.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

An analysis of the computational complexity of the query phase, i.e., the complexity of extracting the optimal solution from the graph returned by these algorithms, is also provided.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Number of calls to the $\\mathtt{C}\\mathtt{o}\\mathtt{l}\\mathtt{l}\\mathtt{i}\\mathtt{s}\\mathtt{i}\\mathtt{o}\\mathtt{n}\\mathtt{F}\\mathtt{r}\\mathtt{e}\\mathtt{e}$ procedure", "weight": 1.0} -->

First, lower-bounds are established for the PRM and sPRM algorithms.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Complexity of the $\\mathtt{C}\\mathtt{o}\\mathtt{l}\\mathtt{l}\\mathtt{i}\\mathtt{s}\\mathtt{i}\\mathtt{o}\\mathtt{n}\\mathtt{F}\\mathtt{r}\\mathtt{e}\\mathtt{e}$ procedure", "weight": 1.0} -->

In this section, complexity of the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure in terms of the number of obstacles in the environment is analyzed, which is a widely-studied problem in the literature (see, e.g., Lin and Manocha for a survey). The main result is based on Six and Wood, which shows that checking collision with $m$ obstacles can be executed in $O{({\log^{d}m})}$ time using data structures based on spatial trees.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}\\mathtt{e}\\mathtt{s}\\mathtt{t}$ procedure", "weight": 1.0} -->

The nearest neighbor search problem has been widely studied in the literature, since it has many applications, e.g., computer graphics, database systems, image processing, data mining, pattern recognition, etc.. Clearly, a brute-force algorithm that examines every vertex runs in $O{(n)}$ time and requires $O{}$ space. However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., in $O{({\log n})}$ time, especially for anytime algorithms that provide better solutions as the number of iterations increase.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}\\mathtt{e}\\mathtt{s}\\mathtt{t}$ procedure", "weight": 1.0} -->

Fortunately, existing algorithms for computing an "approximate" nearest neighbor, if not an exact one, are computationally very efficient. In the sequel, a vertex $y$ is said to be an $\varepsilon$-approximate nearest neighbor of a point $x$ if ${\|{y - x}\|} \leq {{({1 + \varepsilon})}{\|{z - x}\|}}$, where $z$ is the true nearest neighbor of $x$. An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves $O{({c_{d,\varepsilon}{\log n}})}$ query time using $O{({dn})}$ space, where $c_{d,\varepsilon} \leq {d{\lceil{1 + {{6d}/\varepsilon}}\rceil}^{d}}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}\\mathtt{e}\\mathtt{s}\\mathtt{t}$ procedure", "weight": 1.0} -->

This algorithm is computationally optimal in fixed dimensions, since it closely matches a lower bound for algorithms that use a tree structure stored in roughly linear space. Using approximate nearest neighbor computation in the context of both PRMs and RRTs was discussed very recently in Yershova and LaValle; Plaku and Kavraki.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}\\mathtt{e}\\mathtt{s}\\mathtt{t}$ procedure", "weight": 1.0} -->

Let $G = {(V,E)}$ be a graph with $V \subseteq \mathcal{X}$ and let $x \in \mathcal{X}$. The discussion above implies that the number of simple operations executed by the ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}{(G,x)}$ procedure is $\Theta{({\log{|V|}})}$ in fixed dimensions, if the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ procedure is implemented using a tree structure that is stored in linear space.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}$ procedure", "weight": 1.0} -->

Problems similar to that solved by the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure are also widely-studied in the literature, generally under the name of range search problems, as they have many applications, for instance, computer graphics and spatial database systems. In the worst case and in fixed dimensions, computing the exact set of vertices that reside in a ball of radius $r_{n}$ centered at a query point $x$ takes $O{({n^{1 - {1/d}} + m})}$ time using $k$-d trees, where $m$ is the number of vertices returned by the search (see also Chanzy et al. for an analysis of the average case).

<!-- chunk {"id": "body-0107", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}$ procedure", "weight": 1.0} -->

Similar to the nearest neighbor search, computing approximate solutions to the range search problem is computationally easier. A range search algorithm is said to be $\varepsilon$-approximate if it returns all vertices that reside in the ball of size $r_{n}$ and no vertices outside a ball of radius ${({1 + \varepsilon})}r_{n}$, but may or may not return the vertices that lie outside the former ball and inside the latter ball. Computing $\varepsilon$-approximate solutions using BBD-trees requires $O{({{2^{d}{\log n}} + {d^{2}{({{3\sqrt{d}}/\varepsilon})}^{d - 1}}})}$ time when using $O{({dn})}$ space, in the worst case.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}$ procedure", "weight": 1.0} -->

Thus, in fixed dimensions, the complexity of this algorithm is $O{({{\log n} + {({1/\varepsilon})}^{d - 1}})}$, which is known to be optimal, closely matching a lower bound. More recently, algorithms that can provide trade-offs between time and space were also proposed.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Complexity of the $\\mathtt{N}\\mathtt{e}\\mathtt{a}\\mathtt{r}$ procedure", "weight": 1.0} -->

Note that the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure can be implemented as an approximate range search while maintaining the asymptotic optimality guarantee. Notice that the expected number of vertices returned by the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure also does not change, except by a constant factor. Hence, the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure can be implemented to run in order $\log n$ expected time in the limit and linear space in fixed dimensions.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Time complexity of the processing phase", "weight": 1.0} -->

The following results characterize the asymptotic computational complexity of various sampling-based algorithms in terms of the number of simple operations such as comparisons, additions, and multiplications.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Time complexity of the processing phase", "weight": 1.0} -->

Let $n$ denote the total number of iterations (or, alternatively, the number of samples), and $m$ denote the number of obstacles in the environment. Then, by Lemmas 40 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") and 41 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"), ${N_{n}^{PRM},N_{n}^{sPRM}} \in {\Omega{({n^{2}{\log^{d}m}})}}$. In the $k$-nearest sPRM and RRT algorithms, $\Omega{({\log n})}$ time is spent on finding the ($k$-)nearest neighbor(s) and $\Omega{({\log^{d}m})}$ time is spent on collision checking at each iteration.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Time complexity of the query phase", "weight": 1.0} -->

After algorithm $ALG$ returns the graph $G_{n}^{ALG}$, the optimal path must be extracted from this graph using, e.g., Dijkstra's shortest path algorithm. In this section, the complexity of this operation, called the query phase, is discussed.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Time complexity of the query phase", "weight": 1.0} -->

The following lemma yields the asymptotic computational complexity of computing shortest paths. Let $G = {(V,E)}$ be a graph. A length function $l:{E\rightarrow{\mathbb{R}}_{> 0}}$ is a function that assigns each edge in $E$ a positive length. Given a vertex $v \in V$, the shortest paths tree for $G$, $l$, and $v$ is a graph $G' = {(V,E')}$, where $E' \subseteq E$ such that for any $v' \in {V \smallsetminus {\{ v\}}}$, there exists a unique path in $G$ that starts from $v$ and reaches $v'$, moreover, this path is the optimal such path in $G$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Space complexity", "weight": 1.0} -->

Space complexity of an algorithm $ALG$ is defined as the amount of memory that is used by $ALG$ to compute the graph $G_{n}^{ALG} = {(V_{n}^{ALG},E_{n}^{ALG})}$. Clearly, in all algorithms discussed in this paper, the space complexity is the size of $G_{n}^{ALG}$, i.e., ${|V_{n}^{ALG}|} + {|E_{n}^{ALG}|}$. Since the number of edges is at least as much as the number of vertices in $G_{n}^{ALG}$ for all algorithms discussed in this paper, the space complexity of an algorithm, in this context, is the number edges in the graph that it returns, which was determined in the previous section.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This section is devoted to an experimental study of the algorithms considered in the paper. All algorithms were implemented in C and run on a computer with 2.66 GHz processor and 4GB RAM running the Linux operating system. Unless otherwise noted, total variation of a path is its cost.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

A first set of experiments were run to illustrate the different performance of $k$-nearest PRM and of PRM^∗^. The $k$-nearest PRM and the PRM^∗^ algorithms were run alongside in two dimensional configuration-space and the cost of the best path in both algorithms is plotted versus the number of iterations in Figure 10. The $k$-nearest PRM does not converge to optimal solutions, unlike PRM^∗^. The performance of the PRM^∗^ algorithm is also shown in configuration spaces of dimensions up to five in Figure 11.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The main bulk of the experiments were aimed at demonstrating the performance of the RRT^∗^ algorithm, especially in comparison with its "standard" counterpart, i.e., RRT. Three problem instances were considered. In the first two, the cost function is the Euclidean path length.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The first scenario includes no obstacles. Both algorithms are run in a square environment. The trees maintained by the algorithms are shown in Figure 12 at several stages. The figure illustrates that, in this case, the RRT algorithm does not improve the feasible solution to converge to an optimum solution. On the other hand, running the RRT^∗^ algorithm further improves the paths in the tree to lower cost ones. The convergence properties of the two algorithms are also investigated in Monte-Carlo runs. Both algorithms were run for 20,000 iterations 500 times and the cost of the best path in the trees were averaged for each iteration. The results are shown in Figure 13, which shows that in the limit the RRT algorithm has cost very close to a $\sqrt{2}$ factor the optimal solution (see LaValle and Kuffner for a similar result in a deterministic setting), whereas the RRT^∗^ converges to the optimal solution. Moreover, the variance over different RRT runs approaches 2.5, while that of the RRT^∗^ approaches zero. Hence, almost all RRT^∗^ runs have the property of convergence to an optimal solution, as expected.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In the second scenario, both algorithms are run in an environment in presence of obstacles. In Figure 14, the trees maintained by the algorithms are shown after 20,000 iterations. The tree maintained by the RRT^∗^ algorithm is also shown in Figure 15 in different stages. It can be observed that the RRT^∗^ first rapidly explores the state space just like the RRT. Moreover, as the number of samples increase, the RRT^∗^ improves its tree to include paths with smaller cost and eventually discovers a path in a different homotopy class, which reduces the cost of reaching the target considerably. Results of a Monte-Carlo study for this scenario is presented in Figure 16. Both algorithms were run alongside up until 20,000 iterations 500 times and cost of the best path in the trees were averaged for each iteration. The figures illustrate that all runs of the RRT^∗^ algorithm converges to the optimum, whereas the RRT algorithm is about 1.5 of the optimal solution on average. The high variance in solutions returned by the RRT algorithm stems from the fact that there are two different homotopy classes of paths that reach the goal.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

If the RRT luckily converges to a path of the homotopy class that contains an optimum solution, then the resulting path is relatively closer to the optimum than it is on average. If, on the other hand, the RRT first explores a path of the second homotopy class, which is often the case for this particular scenario, then the solution that RRT converges to is generally around twice the optimum.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Finally, in the third scenario, where no obstacles are present, the cost function is selected to be the line integral of a function, which evaluates to 2 in the high cost region, 1/2 in the low cost region, and 1 everywhere else. The tree maintained by the RRT^∗^ algorithm is shown after 20,000 iterations in Figure 17. Notice that the tree either avoids the high cost region or crosses it quickly, and vice-versa for the low-cost region. (Incidentally, this behavior corresponds to the well known Snell-Descartes law for refraction of light, see Rowe and Alexander for a path-planning application.)

<!-- chunk {"id": "body-0122", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To compare the running time, both algorithms were run alongside in an environment with no obstacles for up to one million iterations. Figure 18, shows the ratio of the running time of RRT^∗^ and that of RRT versus the number of iterations averaged over 50 runs. As expected from the complexity analysis of Section 4.3, this ratio converges to a constant value. A similar figure is produced for the second scenario and provided in Figure 19.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The RRT^∗^ algorithm was also run in a 5-dimensional state space. The number of iterations versus the cost of the best path averaged over 100 trials is shown in Figure 20. A comparison with the RRT algorithm is provided in the same figure. The ratio of the running times of the RRT^∗^ and the RRT algorithms is provided in Figure 21. The same experiment is carried out for a 10-dimensional configuration space. The results are shown in Figure 22.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented the results of a thorough analysis of sampling-based algorithms for optimal path planning. It is shown that broadly used algorithms from the literature, while probabilistically complete, are not asymptotically optimal, i.e., they will return a solution to the path planning problem with high probability if one exists, but the cost of the solution returned by the algorithm will not converge to the optimal cost as the number of samples increases. In particular, it is proven that the PRM and RRT algorithms are not asymptotically optimal. A simplified version of PRM is asymptotically optimal, but is computationally expensive. In addition, it is shown that certain heuristic versions of PRM are not only not asymptotically complete, but also not necessarily complete.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in this class. In other words, asymptotic optimality imposes only a constant factor increase in complexity with respect to probabilistic completeness. The first algorithm, called PRM^∗^, is a variant of PRM, with a variable connection radius that scales as ${\log{(n)}}/n$, where $n$ is the number of samples. In other words, the average number of connections made at each iteration is proportional to $\log{(n)}$. The second new algorithm, called RRG, incrementally builds a connected roadmap, augmenting the RRT algorithm with connections within a ball scaling as ${\log{(n)}}/n$. The third new algorithm, called RRT^∗^, is a version of RRG that incrementally builds a tree. Experimental evidence that demonstrate the effectiveness of the algorithms proposed and support the theoretical claims were also provided.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A common theme in the paper is that, in order to ensure both asymptotic optimality and computational efficiency, connections between samples should be sought within balls of radius scaling as ${\log{(n)}}/n$. If these balls shrink faster as $n$ increases, the algorithms are not asymptotically optimal (but may still be probabilistically complete); on the other hand, if these balls shrink slower, the complexity of the algorithms will suffer. On average, the proposed scaling laws will result in an average number of connections per iteration that is proportional to $\log{(n)}$. Hence, it is natural to consider variants of these algorithms that make connections to $k{\log{(n)}}$ neighbors surely. Indeed, it is shown that these algorithms do share the same asymptotic optimality and computational efficiency properties of their counterparts, as long as $k$ is no smaller than a constant $k_{RRG}^{\ast}$. It is remarkable that this constant only depends on the dimension of the space, and is otherwise independent from the problem instance.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The analysis of the results in the paper relies on techniques used to analyze random geometric graphs. Indeed, the algorithms considered in this paper build graphs that have many characteristics in common with well known classes of random geometric graphs. Interestingly, such geometric graphs exhibit phase transition phenomena, including percolation and connectivity, for thresholds matching those found for probabilistic completeness and asymptotic optimality of sampling-based algorithms. This leads to a natural conjecture that a sampling-based path planning algorithm is probabilistically complete if and only if the underlying random geometric graph percolates, and is asymptotically optimal if and only if the underlying random geometric graph is connected.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The work presented in this paper can be extended in numerous directions. First of all, it would be of interest to establish broader connections between sampling-based path planning algorithms and random geometric graphs, e.g., by proving or disproving the conjecture above, and by possibly improving on current algorithms through a better understanding of the underlying mathematical objects. Similar analysis techniques can also be used to analyze other sampling-based path planning algorithms that were not analyzed in this paper, such as EST. In addition, it is of interest to investigate deterministic sampling-based algorithms, in which samples are generated using deterministic dense sequences of points, e.g., low dispersion, as opposed to random sequences.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Second, it is of great practical interest to address motion planning problems subject to more complex constraints. For example, motion planning problems for mobile robots should consider the robot's dynamics, and hence differential constraints on the feasible trajectories (these are also called kino-dynamic planning problems). In addition, it is of interest to consider optimal planning problems in the presence of temporal/logic constraints on the trajectories, e.g., expressed using formal specification languages such as Linear Temporal Logic, or the $\mu$-calculus. Such constraints correspond to, e.g., rules of the road constraints for autonomous ground vehicles, mission specifications for autonomous robots, and rules of engagement in military applications. Ultimately, incremental sampling-based algorithms with asymptotic optimality properties may provide the basic elements for the on-line solution of differential games, as those arising when planning in the presence of dynamic obstacles.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, it is noted that the proposed algorithms may have applications outside of the robotic motion planning domain. In fact, the class of sampling-based algorithm described in this paper can be readily extended to deal with problems described by partial differential equations, such as the eikonal equation and the Hamilton-Jacobi-Bellman equation.
