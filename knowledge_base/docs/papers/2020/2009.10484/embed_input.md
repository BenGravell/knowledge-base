<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically Optimal Sampling-Based Motion Planning Methods

Topics include Survey, Robotics, Motion planning, Robot motion planning, Sampling-based planning, Optimal motion planning, Asymptotically optimal.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning is a fundamental problem in autonomous robotics that requires finding a path to a specified goal that avoids obstacles and takes into account a robot's limitations and constraints. It is often desirable for this path to also optimize a cost function, such as path length. Formal path-quality guarantees for continuously valued search spaces are an active area of research interest. Recent results have proven that some sampling-based planning methods probabilistically converge toward the optimal solution as computational effort approaches infinity. This article summarizes the assumptions behind these popular asymptotically optimal techniques and provides an introduction to the significant ongoing research on this topic.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Planning is an important task in a number of fields, including computer science and robotics. It consists of finding a sequence of valid states (i.e., a path) between specified positions (i.e., a start and goal) in a search space. Many problems have multiple *feasible* solutions and applications often seek the feasible path that optimizes a cost function (i.e., the *optimal* solution). A feasible solution in robot motion planning is a path that avoids hazards in the environment (i.e., obstacles) and can be followed by the robot (e.g., is kinodynamically feasible). The optimal solution minimizes a user-specified path cost, such as actuator effort or path length.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Optimal planning is difficult because there are often a large number of states to consider and it can be computationally expensive to evaluate them. Graph-search algorithms, such as A\*, can search discrete spaces (e.g., graphs) efficiently with strong formal guarantees. These techniques are guaranteed to find the optimal solution, if one exists, and otherwise return failure (i.e., they are *complete* and *optimal*). A\* is also guaranteed to expand no more states than any other optimal algorithm given the same information \i.e., it is *optimally efficient*;.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Robot motion planning search spaces are instead often continuously valued (i.e., infinite sets) since robots can be arbitrarily repositioned in the physical world. These spaces can be approximated with discrete representations and then searched with graph-search algorithms but the performance will depend on the chosen resolution. The resulting discrete solutions will only be resolution complete and resolution optimal relative to the continuous problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

It can be difficult to select a 'correct' a priori discrete approximation in many continuously valued problems. Excessively sparse approximations may preclude finding a (suitable) solution but excessively dense ones can be prohibitively expensive to construct and search. These difficulties are common in robot motion planning where search spaces are often poorly bounded (e.g., planning outdoors), high dimensional (e.g., planning for manipulation), or otherwise expensive to discretize (e.g., kinodynamic systems).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Sampling-based planning algorithms, such as Probabilistic Roadmap \[PRM; 2\], Expansive Space Tree \[EST; 3\], and Rapidly exploring Random Tree \[RRT; 4\], are designed to avoid a priori approximations of the search space. They instead use sampling to interleave aspects of approximation and search until a solution is found. This leads to better performance than graph-based methods on many problems but makes formal guarantees probabilistic and dependent on the sampling distribution. Given an appropriate distribution (e.g., uniform sampling), the probability that many of these techniques find a solution, if one exists, goes to one as the number of samples goes to infinity \i.e., they are *probabilistically complete*;. Until recently, there were no equivalent formal statements about the quality of these solutions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Karaman and Frazzoli present the first formal analysis of probabilistic solution quality in popular sampling-based planning algorithms. They prove that sampling potential states and statically connecting them to the nearest existing vertex, as in Rapidly exploring Random Tree (RRT), gives a zero probability of finding the optimal solution, even with an infinite number of samples. They prove that algorithms that consider a higher number of connections, such as simplified \[s-PRM; 5\], can have a unity probability of asymptotically converging to the optimal solution, if one exists, as the number of samples goes to infinity (i.e., they are *almost-surely asymptotically optimal*). They present a series of algorithms specifically designed to consider a sufficient number of connections to achieve almost-sure asymptotic optimality efficiently: almost-surely asymptotically optimal (PRM\*), Rapidly exploring Random Graph (RRG) and almost-surely asymptotically optimal (RRT\*).

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

These results have motivated significant recent work on quality guarantees for sampling-based planning algorithms. These include refining the conditions necessary for popular approaches to converge asymptotically to the optimum and designing novel algorithms that find better initial solutions and/or converge faster. This survey summarizes results and algorithms from the field to present an introduction to this exciting work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this survey is organized as follows. Section 2 introduces the asymptotically optimal planning problem with a focus on providing a common set of definitions and assumptions for the literature. Section 3 presents an introductory survey of work in the field, including important theoretical results and effective algorithms. Section 4 provides a closing summary that includes a discussion of ongoing areas of research interest.

<!-- chunk {"id": "body-0011", "role": "body", "section": "SAMPLING-BASED MOTION PLANNING", "weight": 1.0} -->

The optimal planning problem requires solving the underlying feasible problem (Figure 1). Section 2.1 presents formal definitions of the planning search space and the feasible and optimal problems. Section 2.2 presents definitions of formal performance guarantees for sampling-based planning algorithms in the form of probabilistic statements on finding solutions to the feasible and optimal motion planning problems. Section 2.3 summarizes common assumptions made to prove these properties for sampling-based planning algorithms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Planning problems are defined in a spatial representation of the system. There are a variety of common representations in robot motion planning, including actuator positions (i.e., configuration) and robot pose, possibly including dynamics (i.e., physical state). This survey refers to all robot representations, without loss of generality, as the search space, $X$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Search space, $X$The space in which the motion planning problem is posed, often a world or configuration space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

A subset of the search space may be invalid for use in a solution, $X_{invalid} \subset X$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Invalid states in robot motion planning include self collisions, collisions between the robot and the physical world, and other dangerous or undesirable outcomes. It is often easy to check these conditions for individual states but difficult to enumerate all invalid states, especially when evaluating validity requires mapping between the physical world and configuration space, as in manipulator arms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

The complement of the invalid states is the set of states permitted in a solution, $X_{free} ≔ {X \smallsetminus X_{invalid}}$, where $\smallsetminus$ is the set difference. A planning problem is defined by specifying a start state, $\mathbf{x}_{start} \in X_{free}$, and a goal state or region, $\mathbf{x}_{goal} \in X_{goal} \subset X_{free}$, in this free space. In robot motion planning, the start is the initial robot configuration and the goal may be either an individual state (e.g., a mobile robot pose) or set of states (e.g., the set of arm joint angles for a desired end-effector position).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Free space, $X_{free}$The permissible subset of the search space.\\entryStart state, $\mathbf{x}_{start}$The initial state of a motion planning problem.\\entryGoal region, $X_{goal}$The desired final state(s) of a motion planning problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

A path is a sequence of states through the search space that can be described by a continuous function with bounded variation (i.e., finite length),

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

where $T \in_{> 0}$ and ${TV}( \cdot )$ is the total variation of the function. The set of paths passing solely through the free space of a problem is the set of free paths,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

where $\Sigma$ is the set of all paths. The set of paths between the start and goal of a problem is the set of start-goal paths,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

The set of paths executable by the system is the set of followable paths, $\Sigma_{follow}$. This followable set is equivalent to the set of all paths for unconstrained holonomic systems. Robotic systems can be unconstrained or subject to a variety of constraints and dynamics, such as in kinodynamic systems (Section 2.3.4).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Path, $\sigma$A sequence of states through the search space that can be described by a continuous function with bounded variation.\\entryFeasible paths, $\Sigma_{feasible}$The set of all paths connecting the start to goal through free space that can be followed by the robot.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

A given problem has a solution if the set of feasible paths,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

is not empty, i.e., $\Sigma_{feasible} \neq \varnothing$. The feasible motion planning problem is then formally defined as the search for a path from the feasible set (Definition 1. ‣ 2.1 Problem Definitions ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Definitions", "weight": 1.0} -->

Feasible motion planningThe search for a feasible path that connects the start and goal of a given problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Formal Analysis of Sampling-based Motion Planners", "weight": 1.0} -->

Sampling-based motion planners attempt to solve the feasible and optimal motion planning problems by sampling the search space. These samples are used to approximate and search the problem and can allow the algorithms to be applied to continuously valued spaces without a priori finite discretizations. They also make algorithm performance a function of the number and specific sequence of samples and weaken formal guarantees.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Formal Analysis of Sampling-based Motion Planners", "weight": 1.0} -->

It is common to evaluate sampling-based planning performance as a function of the number of samples probabilistically over all possible realizations of a chosen sampling distribution. Algorithms with a probability of solving feasible motion planning problems that goes to one with infinite samples are described as probabilistically complete (Definition 3. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")) in the sampling-based planning literature \e.g.,.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Formal Analysis of Sampling-based Motion Planners", "weight": 1.0} -->

Probabilistically completeThe probability of finding a solution goes to one as the number of samples approaches infinity.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumptions", "weight": 1.0} -->

Formal analysis of sampling-based planners requires making assumptions about the properties of the optimal motion planning problem. These commonly include aspects of the search space (Section 2.3.1), solutions (Section 2.3.2), and cost function (Section 2.3.3). These assumptions can also be modified and extended to provide formal analysis of planning performance for kinodynamic systems (Section 2.3.4).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Search space assumptions", "weight": 1.0} -->

The search space is assumed in to be Euclidean and an open unit $n$-dimensional (hyper)cube, $X ≔ ^{n}$, as in works by Kavraki et al. and others. Spaces that are not a unit cube and/or Euclidean must be scaled appropriately and/or behave locally as a Euclidean space. The free space is then taken as the closed complement of this search space and the invalid set, $X_{free} ≔ {{cl}\left( {X \smallsetminus X_{invalid}} \right)}$, where ${cl}( \cdot )$ denotes the closure of a set. The closed free set ensures that a feasible path exists with optimal cost for all feasible planning problems, i.e., ${\Sigma_{feasible} \neq \varnothing}\Leftrightarrow{\Sigma^{\ast} \neq \varnothing}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Search space assumptions", "weight": 1.0} -->

Janson et al. refine these assumptions for planning problems to a goal region to ensure that samples can be drawn near the goal boundary with a nonzero probability. A goal region is described as $\xi$-regular if its boundary, $\partial X_{goal}$, has bounded curvature everywhere. This is expressed by requiring that every state in the goal boundary also lies on the boundary of a $\xi$-radius subset of the goal region, ${B(\mathbf{y},\xi)} \subseteq X_{goal}$, where $\xi > 0$, i.e.,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Search space assumptions", "weight": 1.0} -->

is an $n$-dimensional ball of radius $r$ centred at $\mathbf{y}$ and $\partial$ denotes the boundary of the specified set.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

The probability of sampling a state that could belong to a feasible path is proportional to the measure of the set of all feasible paths relative to that of the sampling domain. A sufficient condition for this probability to be nonzero when sampling uniformly is for there to exist a feasible path that remains a finite distance from obstacles for its entire length (Figure 2a). Such paths are described as having strong $\delta$-clearance and the set of all such paths is given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

where $B\left( {\sigma(t)},\delta \right)$ is a $\delta$-radius ball centred at $\sigma(t)$ as defined by Equation 1. {marginnote}\\entryStrong $\delta$-clearance pathA path that is no closer than $\delta$ from invalid states.\\entryRobustly feasible problemA problem is robustly feasible if it has at least one solution with strong $\delta$-clearance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

A planning problem containing a feasible path with strong $\delta$-clearance is described as robustly feasible. Sampling-based motion planners have zero probability of solving problems where all solutions do not have strong $\delta$-clearance, i.e., problems that are not robustly feasible (Figure 2c).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

The set of optimal solutions has zero measure and therefore zero probability of being sampled in most practical problems, even if the problem is robustly feasible. Asymptotically optimal sampling-based planning algorithms instead converge towards an optimal solution from suboptimal paths (Figure 2b). Optimal solutions often pass infinitely close to obstacles and are described as having weak $\delta$-clearance if they are homotopic to a strong $\delta$-clearance path, i.e.,

<!-- chunk {"id": "body-0037", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

where $\sigma^{\ast} \in \Sigma_{free}$ is an optimal solution, $\sigma^{\prime} \in \Sigma_{\delta - {clear}}$ is a robustly feasible solution, and $H$ is a homotopic map between the two.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

Janson et al. note that this homotopy requirement can be "vacuously satisfied" (p. 886) and seek to refine the mathematical definition. They state the assumption as the existence of an infinite sequence of strong $\delta_{i}$-clearance paths, $\left( \sigma_{i} \right)_{i = 1}^{\infty}$, such that the limit of this sequence has optimal cost, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

A planning problem with at least one optimal solution that can be continuously transformed to a strong $\delta$-clearance path is referred to as robustly optimal or $\delta$-robustly feasible. Asymptotically optimal techniques cannot converge towards any other optima, i.e., cannot asymptotically solve optimal planning problems that are not robustly optimal or $\delta$-robustly feasible (Figure 2c).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

Solovey and colleagues define the robust optimum, $c_{\delta - {clear}}^{\ast}$, as the infimum of the $\delta$-clearance paths,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

This cost will be equivalent to the true optimum in problems that contain at least one optimal solution with weak $\delta$-clearance, i.e., one optimal solution that can be continuously transformed to a strong $\delta$-clearance path.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Solution assumptions", "weight": 1.0} -->

Weak $\delta$-clearance pathA path that can be continuously transformed through free space to be no closer than $\delta$ from invalid states.\\entryRobustly optimal problemA problem is robustly optimal if it has at least one optimal solution with weak $\delta$-clearance.\\entryRobust optimum, $c_{\delta - {clear}}^{\ast}$The best cost of all weak $\delta$-clearance solutions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Cost assumptions", "weight": 1.0} -->

Asymptotic convergence towards the optimum requires a well-behaved cost function. While a variety of assumptions are made about the function in subsequent analysis, the most basic assumption is that it is bounded for paths in free space and monotonic such that the cost of any path cannot be smaller than its subpaths,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Cost assumptions", "weight": 1.0} -->

where $|$ is the concatenation of two paths and is defined as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Cost assumptions", "weight": 1.0} -->

Monotonic costA path-cost function where the total cost of a path cannot be smaller than that of any of its constituent subpaths.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Kinodynamic Systems", "weight": 1.0} -->

The initial formal analysis of asymptotically optimal sampling-based motion planning algorithms focused on geometric motion planning in the absence of dynamics or constraints, i.e., $\Sigma_{follow} = \Sigma$. This analysis has been extended to consider the dynamic systems often found in robotics. These systems are often described by a dynamical equation that relates the evolution of the state to control inputs (i.e., kinodynamics). This limits the set of followable paths to those that satisfy the differential equation of motion,

<!-- chunk {"id": "body-0047", "role": "body", "section": "Kinodynamic Systems", "weight": 1.0} -->

where $f( \cdot, \cdot )$ defines a time-invariant dynamical system and $\Psi ≔ \left\{ \psi \right\}$ is the set of all control sequences, $\psi:{\lbrack 0,T\rbrack\rightarrow U}$, in the control space of the robot, $U \subseteq^{m}$. The path is fully defined by an initial state, ${\sigma} = \mathbf{x}_{start}$, and the control sequence, which makes kinodynamic motion planning the search for a sequence of controls, $\psi^{\prime} \in \Psi$, that solves the posed problem.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Kinodynamic Systems", "weight": 1.0} -->

Optimal kinodynamic motion planning problems often seek to minimize the cost of the path and control effort in the form,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Kinodynamic Systems", "weight": 1.0} -->

where the integrand, ${\mathfrak{c}}( \cdot, \cdot )$, is the *cost derivative* and maps from the search and control spaces to a cost,

<!-- chunk {"id": "body-0050", "role": "body", "section": "Kinodynamic Systems", "weight": 1.0} -->

Formally analyzing the asymptotic optimality of kinodynamic motion planning algorithms requires additional assumptions that are not summarized here. These include statements about the controllability of the dynamical system, the nature of the cost function, and other properties of the problem, including whether the dynamical equation can be solved analytically for arbitrary end conditions (i.e., the existence of a 'steering' function). Kinodynamic motion planning is often considered in the presence of kinodynamic constraints (Section 3.3.3).

<!-- chunk {"id": "body-0051", "role": "body", "section": "ASYMPTOTICALLY OPTIMAL SAMPLING-BASED MOTION PLANNING", "weight": 1.0} -->

Asymptotically optimal sampling-based motion planning is a popular research topic. This section presents an introductory survey of approximately half of the more than 300 academic articles published since 2010, as necessitated by the limits of this article. While many of these works address multiple questions, general areas of research include refining and extending formal analysis (Section 3.1), improving practical performance (Section 3.2), supporting constraints and specifications (Section 3.3), and applying algorithms to a variety of problems in robotics (Section 3.4).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Formal Analysis", "weight": 1.0} -->

A primary area of research interest is refining and extending the formal analysis of asymptotic optimality first presented. This includes tightening the bounds that guarantee asymptotic optimality almost surely or in probability (Section 3.1.1), developing relaxed bounds for asymptotic convergence to *near optimal* solutions (Section 3.1.2), and extending analysis to evaluate rates of convergence (Section 3.1.3).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Analytic Bounds", "weight": 1.0} -->

The almost-sure asymptotic optimality presented in is a result of considering multiple connections per sample. The number of connections necessary are presented as a function of state measure (e.g., volume), state dimension, and the number of existing vertices. These expressions define either the minimum number of nearest vertices (e.g., $k$-nearest) or the maximum distance to consider (e.g., $r$-disc) when adding new samples.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Analytic Bounds", "weight": 1.0} -->

The computational cost of sampling-based planning algorithms depends on the number of these connections required to be considered for each new sample. Significant research has worked to develop tighter bounds and/or alternative analysis for other algorithms to reduce the number of connections while maintaining asymptotic convergence to the optimum, sometimes by making more specific assumptions about the planning problem. Research has included addressing limitations in the original analysis, relaxing asymptotic optimality to convergence in probability, and developing alternative analysis and refined expressions for connectivity, including with different sampling and graph models. It has also investigated necessary conditions for asymptotic convergence when planning for kinodynamic systems, including in an augmented state-cost search space, and integrated task and motion planning problems. These bounds are often also investigated as part of work focused on other aspects of the planning problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Near Optimality", "weight": 1.0} -->

Asymptotically optimal algorithms converge towards an optimal solution as the number of samples increase but will almost surely not reach it in finite time \Lemma 28;. Asymptotically *near-optimal* sampling-based algorithms improve practical performance by instead converging towards a solution that is within a user-specified factor of the optimum. This relaxed theoretical guarantee reduces computational effort and can result in algorithms that find better solutions faster in finite time and use less computational resources than required to maintain strict asymptotic optimality.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Near Optimality", "weight": 1.0} -->

Asymptotic near optimality can be achieved in a variety of ways, including different connectivity expressions and lazily evaluating or removing connections during or after the search.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

Asymptotically optimal sampling-based planning algorithms converge with infinite samples but have no guarantees on their rate of convergence. Different rates can result in orders-of-magnitude differences in finite-time performance. Understanding the rates in different situations can help identify useful algorithms for practical problems and also design better planners.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

Research includes developing probabilistic bounds on the length of a solution as a function of finite samples for PRM\* and Fast Marching Tree \[FMT\*; 8\] with both random and deterministic sampling. It also includes convergence rates for asymptotically near-optimal kinodynamic planners and asymptotically optimal kinodynamic planners built on feasible planning in a state-cost space. It has also proven that naive RRT\* converges sublinearly (i.e., slower than linearly) in all possible problem or planner configurations when minimizing path length but that focused variants, such as Informed RRT\*, can have linear convergence in some situations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Practical Performance", "weight": 1.0} -->

Another primary area of research is improving the practical ability of asymptotically optimal planning algorithms to find initial solutions quickly and converge rapidly towards the optimum. This work is important for real robotic systems and may also include formal analysis of the algorithmic improvements. Research in this area is wide ranging and difficult to classify but includes work on sampling (Section 3.2.1), heuristic search (Section 3.2.2), lazy computations (Section 3.2.3), hybrid search techniques (Section 3.2.4), bidirectional search techniques (Section 3.2.5), and a variety of other approaches (Section 3.2.6).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Sampling", "weight": 1.0} -->

The performance of an individual instance of a sampling-based planning algorithm depends on the sequence of samples used in that specific run. Sequences may be deterministic or random but expected algorithm performance will depend on the underlying distribution. Many algorithms use a uniform distribution over the entire search space to ensure that all possible solutions can be found; however, performance can often be improved by increasing the likelihood of sampling (better) solutions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Sampling", "weight": 1.0} -->

Samples can be generated in a number of different ways that can reduce search effort, including sampling using motion primitives, subspaces or simplified abstractions, potential functions, and gradient descent. Performance can also be improved by biasing sampling around approximations of free space, with cross entropy, machine-learning methods, and existing solutions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Sampling", "weight": 1.0} -->

Existing solutions to a planning problem limit the search for improvements without loss of generality. The set of states that could belong to a better solution is the *omniscient set* and sampling it is a necessary condition to improve the solution for many algorithms \Lemma 5;. Knowledge of the omniscient set is equivalent to solving a problem and it is often approximated as an *informed set* whose sampling is also necessary for improvement \Lemma 12;. The utility of informed sets will depend on the precision and accuracy with which they approximate the omniscient set and they are often sampled approximately using heuristics and rejection sampling.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sampling", "weight": 1.0} -->

An informed set applicable to all problems seeking to minimize path length is an $n$-dimensional ellipse defined by the $L^{2}$ (i.e., Euclidean) norm. It has been shown that the probability of sampling this set with rejection sampling goes to zero factorially (i.e., faster than exponentially) as state dimension increases \Theorem 14;. This minimum-path-length curse of dimensionality can be avoided without loss of generality by directly sampling the $L^{2}$ informed set.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Heuristic Search", "weight": 1.0} -->

Graph-search algorithms use estimates of solution cost (i.e., heuristics) to order their search by potential solution quality. This allows them to prioritize high-quality solutions and avoid unnecessarily low-quality paths which improves both practical and theoretical performance. Heuristics can also be used to order asymptotically optimal sampling-based planning to find better initial solutions sooner, and converge towards the optimum faster, than uninformed approaches.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Heuristic Search", "weight": 1.0} -->

Heuristics can be used to order asymptotically optimal sampling-based planning probabilistically and directly. Batch Informed Trees \[BIT\*; 61\] separates approximation from search and uses heuristics to process batches of samples in order of potential solution quality. This not only searches problems quickly but also allows for extensions from the graph-search literature, including greedy searches, heuristic inflation and search truncation to balance exploration and exploitation, and an asymmetric bidirectional search to adaptively estimate and use problem-specific heuristics. Research into estimating heuristics for motion planning also includes work on kinodynamic systems.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Lazy Search", "weight": 1.0} -->

Sampling-based planning algorithms search problems by sampling the free subspace and connecting samples with edges. These edges must also pass solely through free space and be followable by the robot (i.e., they must be feasible) for the algorithm to find valid solutions. Evaluating edge feasibility can be expensive in many problems, especially in the presence of constraints or obstacles that are defined by a noninvertible function of state.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Lazy Search", "weight": 1.0} -->

Lazy algorithms reduce computational cost and improve real-time performance by delaying edge evaluations until necessary to find and/or improve a solution. Edges may be evaluated only when they belong to the best candidate solution, in order of potential solution quality, when necessary to satisfy optimality bounds, or to estimate heuristics. Lazy collision checking can also be adapted as collision information is gathered to reduce false negatives.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Hybrid Search", "weight": 1.0} -->

Asymptotically optimal sampling-based planning algorithms converge towards the global optimum but have a zero probability of finding it in finite time for most practical problems \Lemma 28;. Local search methods, such as path simplification or local optimization, may find local minima in finite time but provide no global guarantees. Hybrid search algorithms improve the global convergence of sampling-based planning algorithms by including local optimization in the search.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Hybrid Search", "weight": 1.0} -->

The balance between global search and local optimization varies across hybrid algorithms. Some techniques apply optimizers to improve connections between samples and/or minimize solutions during global search. Others are designed to use sampling-based exploration to explore homotopy classes as initial conditions for optimization methods.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Bidirectional Search", "weight": 1.0} -->

Probabilistically complete bidirectional sampling-based planning algorithms, such as RRT-Connect, are effective techniques for feasible planning problems. Bidirectional variants of asymptotically optimal algorithms apply similar approaches to the optimal planning problem. This often finds initial solutions faster but incorporating bidirectional search into asymptotic convergence to the optimum can be more complex.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Bidirectional Search", "weight": 1.0} -->

Bidirectional asymptotically optimal planning includes direct implementations of "RRT\*-Connect" and modifications to improve asymptotic convergence by limiting the 'Connect' heuristic and using informed sampling. They have also been used for manifold constraints, replanning in the presence of dynamic obstacles, and to estimate heuristics adaptively during search. A bidirectional Fast Marching Tree (FMT\*) also includes research on stopping conditions for bidirectional marching methods.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Other Search Improvements", "weight": 1.0} -->

Not all methods to improve the practical performance of asymptotically optimal sampling-based planning algorithms fit neatly into the previous descriptions. A variety of other techniques to improve asymptotically optimal planning include switching between nonasymptotically optimal and asymptotically optimal algorithms and more thoroughly exploiting sampled information. It also includes using computational resources more effectively, such as techniques designed for parallel computing.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Constrained Planning Problems", "weight": 1.0} -->

Robot motion planning problems often require solutions that not only avoid obstacles but also satisfy other platform and/or task constraints. These can include manifold (Section 3.3.1), nonholonomic (Section 3.3.2), and kinodynamic (Section 3.3.3) constraints and high-level task specifications (Section 3.3.4).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Manifold Constraints", "weight": 1.0} -->

Many robot motion planning problems require solutions to both avoid obstacles and satisfy geometric constraints, such as maintaining the orientation of a manipulator end effector. These kinematic or holonomic constraints are a function of state, e.g., ${g(\mathbf{x})} = 0$, and limit solutions to a lower dimensional manifold of the original problem. This manifold has zero measure and therefore zero probability of being sampled from the full search space. {marginnote}\\entryManifold constraintA constraint on the system state which restricts solutions to a lower dimensional manifold in the original search space.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Manifold Constraints", "weight": 1.0} -->

Problems that cannot be reparameterized onto the constraint manifold require planning techniques that can map their search to the implicit manifold. Research on asymptotically optimal algorithms to do so includes using continuation techniques and decomposition into finite subspaces. It also includes projection- and continuation-based methods that allow many types of general asymptotically optimal motion planners to be used directly on implicit manifold configuration spaces.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Nonholonomic Constraints", "weight": 1.0} -->

Many real-world robots have restrictions on their motion, such as skid-steer and Ackermann-steer wheeled robots that cannot move laterally. These nonholonomic constraints are an inseparable function of the state and its derivatives, e.g., ${g\left( \mathbf{x},\frac{d\mathbf{x}}{dt},\frac{d^{2}\mathbf{x}}{dt^{2}},\ldots \right)} = 0$, and limit the connectivity of the search space. These problems can often be solved by treating the nonholonomic constraints as additional obstacles but better planning performance can be achieved by actively incorporating the constraints into the search. Many of these systems must also consider kinodynamic constraints (Section 3.3.3). {marginnote}\\entryNonholonomic constraintA constraint coupling the system state and its derivatives which reduces the connectivity of the search space.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Nonholonomic Constraints", "weight": 1.0} -->

Research has developed distance functions for a variety of nonholonomic vehicles and a general framework to assess asymptotically optimal planning for driftless systems. It also includes work on asymptotically optimal feedback planning, planning in vector flow fields, and deterministic sampling for driftless systems.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

The motion of robots in the real world is governed by differential equations relating control inputs (e.g., forces) to accelerations (Section 2.3.4). These kinodynamics change the connectivity of the search space and any kinodynamic constraints that limit control inputs or rates of change, e.g., $\frac{d^{2}\mathbf{x}}{dt^{2}} < a_{\max}$, further reduce the set of feasible paths. This kinodynamic planning is further complicated for systems where the differential equations of motion cannot be solved in closed form for arbitrary end conditions. The absence of analytical solutions to these two-point boundary-value problems require additional considerations during asymptotically optimal planning, such as numerical approximations or shooting methods. Many of these systems must also consider nonholonomic constraints (Section 3.3.2). {marginnote}\\entryKinodynamic constraintA limit on the state derivatives or control inputs of a kinodynamic system which reduces the connectivity of the search space.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

This popular area of research includes analyzing kinodynamic asymptotic optimality and extending RRT\* to kinodynamic systems. A wide variety of kinodynamic planning techniques exist, including solving two-point BVPs with linear-quadratic regulators \[LQRs; 97, 98\], fixed-final-state free-final-time controllers, successive approximation, closed-loop prediction, and precomputed motion primitives. Other asymptotically optimal kinodynamic planning algorithms use sequential quadratic programming (SQP) with Batch Informed Trees (BIT\*) and analytic steering solutions and numerical approximations with marching methods. Kinodynamic techniques have also been accelerated with heuristics and informed sampling.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

Solving or approximating two-point BVPs is impractical or impossible in some problems. Research on these applications has extended RRT-style shooting methods to asymptotically optimal kinodynamic planning, including with an augmented state-cost search space that does not require rewiring. Two-point BVPs can also be avoided with generalized label correcting methods.

<!-- chunk {"id": "body-0081", "role": "body", "section": "High-level Task Specifications", "weight": 1.0} -->

Many motion planning problems require solutions to both avoid obstacles and satisfy a number of high-level or task-specific constraints. These may include the rules of the road for self-driving cars, a time-dependent sequence of tasks for a warehouse robot, or any number of other complex temporal relationships. These requirements are often defined in high-level specification languages and must be evaluated in parallel to searching for a collision-free path.

<!-- chunk {"id": "body-0082", "role": "body", "section": "High-level Task Specifications", "weight": 1.0} -->

A number of different specification languages have been used with asymptotically optimal sampling-based planners, including $\mu$-calculus, process algebra, Linear Temporal Logic \[LTL; 110, 111, 112\], finite Linear Temporal Logic (LTL), and Signal Temporal Logic \[STL; 114\]. This research allows for algorithms to find paths that satisfy high-level constraints and, when no satisfying solution exists, find paths that reach the goal while violating a minimum number of specifications.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Applications and Further Extensions", "weight": 1.0} -->

There are a number of interesting and challenging extensions of the motion planning problem in robotics. These include complex cost functions (Section 3.4.1) and planning for multirobot (Section 3.4.2) and multimodal (Section 3.4.3) systems. It also includes considering state and/or measurement uncertainty during planning (Section 3.4.4) and replanning when the environment changes or new information is available (Section 3.4.5).

<!-- chunk {"id": "body-0084", "role": "body", "section": "Applications and Further Extensions", "weight": 1.0} -->

Asymptotically optimal planning algorithms are also used in a variety of interesting applications. These include finding optimal solutions to the filtering and stochastic control problems and planning for a number of specific situations, including pursuit evasion games, simultaneous planning and execution, moving goals, operating in vector flow fields, autonomous driving at high speed, autonomous driving for passenger comfort, cable-suspended parallel robots, to reduce radioactive exposure, and very many more.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Different Cost Functions and Objectives", "weight": 1.0} -->

Many planning problems seek to optimize a more complex cost than path length, such as maximizing minimum clearance to obstacles, and objectives defined by cost maps or combinations of cost functions. These objective functions may not meet the assumptions used to first prove asymptotically optimality (Section 2.3) or the resulting refinements (Section 3.1.1).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Different Cost Functions and Objectives", "weight": 1.0} -->

Asymptotically optimal algorithms for these situations include planning on problems defined by cost maps, finding Pareto optimal solutions to multiobjective problems, and minimizing bottleneck (i.e., maximum state) cost. Specific applications include asymptotically optimal inspection in terms of path length and coverage and planning for groups of vehicles to optimize connectivity, surveillance, and path length.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Different Cost Functions and Objectives", "weight": 1.0} -->

A reoccurring complex planning objective in robotics is information maximization. Informative path planning problems require systems to measure their environment while navigating to any specified goals. Asymptotically optimal algorithms have been developed and demonstrated for this problem in environmental monitoring and mapping.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Multirobot Systems", "weight": 1.0} -->

The complexity of path planning is directly related to the dimensionality of the search space. This dimensionality increases quickly in systems consisting of multiple robots. These problems can often be solved naively by treating each robot independently but this may preclude solutions to some problems that require coordination.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Multirobot Systems", "weight": 1.0} -->

Research includes identifying conditions for multirobot asymptotic convergence and developing techniques to solve coupled multirobot problems with the tensor product of their individual spaces. Applications also include groups of vehicles optimizing complex cost functions, two-arm manipulation, and cooperative aerial transport.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Multimodal Systems", "weight": 1.0} -->

Some complex robotic systems have multiple configurations that are best represented as discrete modes (e.g., different legged-robot gaits). Planning problems for these multimodal systems have search spaces with both continuously valued and discrete dimensions. These problems can often be solved with general sampling-based planners but techniques designed to exploit the mixed nature of the search space can be more efficient.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Multimodal Systems", "weight": 1.0} -->

Work to develop better asymptotically optimal planning algorithms for these situations includes extending roadmap planners to the multimodal configuration space of robot and object manipulation. It also includes investigating the conditions for asymptotically optimal convergence in multimodal integrated task and motion planning problems and the application of multirobot techniques to this problem.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Uncertainty", "weight": 1.0} -->

Real-world robotic systems use noisy sensors to measure their environment. This creates uncertainty about their position relative to both obstacles and the goal and makes the feasible and optimal motion planning problems probabilistic. This *belief space planning* seeks a solution that safely reaches the goal with high probability given the system uncertainty.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Uncertainty", "weight": 1.0} -->

Asymptotically optimal algorithms in belief space find the minimum cost path for a noisy system and/or in an uncertain environment that has a bounded probability of collision \i.e., chance constraint; or is guaranteed to be safe. Research has also studied the conditions required for optimality in belief space and shown that this property cannot be achieved for several cost functions and investigated better distance functions to improve planning.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Unknown and/or Dynamic Environments", "weight": 1.0} -->

Real-world robotic systems often operate in environments where the known presence and position of obstacles can change over time as a result of moving objects or sensor range limits. These changes may invalidate previously feasible solutions and require the system to solve an updated version of the original planning problem. This problem can be solved more efficiently with planning algorithms that reuse the previous search effort.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Unknown and/or Dynamic Environments", "weight": 1.0} -->

Asymptotically optimal techniques to replan efficiently when new information becomes available include using a bidirectional search to facilitate updates and continuously refining and repairing a search during execution. Work has also investigated achievable notions of optimality specific to incrementally revealed environments that result in policies guaranteed to be collision free.

<!-- chunk {"id": "body-0096", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Sampling-based motion planning algorithms are powerful tools for searching continuously valued spaces, as often found in robotics. They use samples to approximate and search the space and many popular algorithms have a unity probability of finding a solution, if one exists, with an infinite number of samples (i.e., they are probabilistically complete; Definition 3. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")). The quality of the solutions returned by these algorithms remained an open question until recently.

<!-- chunk {"id": "body-0097", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Karaman and Frazzoli analyze the quality of solutions found by popular sampling-based algorithms and prove that most have zero probability of finding an optimal solution, even with infinite samples. They provide efficient versions of these popular algorithms that instead converge asymptotically to the optimal solution with infinite samples almost surely over all realizations of a sampling distribution (i.e., they are almost-surely asymptotically optimal; Definition 4. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")).

<!-- chunk {"id": "body-0098", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Most asymptotically optimal algorithms converge towards the optimal solution incrementally with additional samples. This anytime performance avoids the difficulties of approximating a continuously valued search space a priori to its search. The sampling instead interleaves approximation and search and the algorithms can be run for a given computational budget or until a suitable solution is found.

<!-- chunk {"id": "body-0099", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Extending asymptotically optimal planning has become an important and increasingly popular area of theoretical and practical research. Theoretical work has refined the necessary conditions for both asymptotic optimality almost surely and in probability (Definition 5. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")), investigated asymptotic near-optimality, and analyzed rates of convergence. Practical work has developed a wide-variety of techniques to find better initial solutions sooner and converge towards the optimum faster.

<!-- chunk {"id": "body-0100", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Asymptotically optimal motion planning algorithms have been adopted and used on a number of robotic systems and problems. These include mobile ground robots, multirotor and fixed wing aerial vehicles, manipulator systems, and many others. These systems may operate independently or as part of a coordinated group and they may be unconstrained or have manifold, nonholonomic, kinodynamic, or high-level task constraints. The planning algorithms may need to optimize complex cost functions and account for unknown environments, moving obstacles, and measurement uncertainty in their plans.

<!-- chunk {"id": "body-0101", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Ongoing research will likely continue to expand the applicability and performance of these popular motion planning algorithms. This will include additional theoretical results, including perhaps further refinement to the necessary conditions for asymptotic optimality and investigations on the convergence rate of the resulting algorithms. It will also continue to include wide ranging efforts to improve practical search performance and applicability to real-world robotic problems.

<!-- chunk {"id": "body-0102", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Asymptotically optimal sampling-based planning algorithms are applicable to many optimal motion planning problems with continuously valued search spaces.

<!-- chunk {"id": "body-0103", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

These algorithms asymptotically converge to the optimal solution as the number of samples goes to infinity almost surely or in probability over all realizations of an appropriate sampling distribution.

<!-- chunk {"id": "body-0104", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Many of these algorithms converge in an anytime manner that avoids the difficulty of selecting the correct approximation a priori to the search.

<!-- chunk {"id": "body-0105", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

These algorithms have been successfully applied to a number of important problems in robotics, including nonholonomic and kinodynamic systems, in unknown and dynamic environments, and in the presence of execution and measurement uncertainty.

<!-- chunk {"id": "body-0106", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Research continues to refine the conditions necessary for asymptotic optimality for a wide range of problems and cost functions.

<!-- chunk {"id": "body-0107", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

There is a large amount of interest in improving practical search performance by finding and improving solutions quickly.

<!-- chunk {"id": "body-0108", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Potential real-world applications continue to grow and include new challenging problems and environments.

<!-- chunk {"id": "body-0109", "role": "body", "section": "DISCLOSURE STATEMENT", "weight": 1.0} -->

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.
