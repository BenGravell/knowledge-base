<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Probabilistic Completeness of RRT for Geometric and Kinodynamic Planning with Forward Propagation

Topics include Probabilistic models, Sampling-based methods, Planning, Control, Sampling, Rapidly-exploring random tree, PC, Random tree, Motion planning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Rapidly-exploring Random Tree (RRT) algorithm has been one of the most prevalent and popular motion-planning techniques for two decades now. Surprisingly, in spite of its centrality, there has been an active debate under which conditions RRT is probabilistically complete. We provide two new proofs of probabilistic completeness (PC) of RRT with a reduced set of assumptions. The first one for the purely geometric setting, where we only require that the solution path has a certain clearance from the obstacles. For the kinodynamic case with forward propagation of random controls and duration, we only consider in addition mild Lipschitz-continuity conditions. These proofs fill a gap in the study of RRT itself. They also lay sound foundations for a variety of more recent and alternative sampling-based methods, whose PC property relies on that of RRT. Our original publication contains an error in the analysis of the case of the kinodynamic RRT. Here, we rectify the problem by modifying the proof of Theorem 2, which, in particular, necessitated a revision of Lemma 3. Briefly, the original (and erroneous) proof of Theorem 2 used a sequence of equal-size balls.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The correction uses a sequence of balls of increasing radii. We emphasize that the correction is in Lemma 3 and the proof of Theorem 2 only. The main results remain unchanged.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two decades ago LaValle and Kuffner presented the *Rapidly-exploring Random Tree* (RRT) method for sampling-based motion planning. Even though numerous alternatives for motion planning have been proposed since then, RRT remains one of the most widely used techniques today. This is due to its simplicity and practical efficiency, especially when combined with simple heuristics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

RRT is especially useful in single-query settings, as it focuses on finding a single trajectory moving a robot from an initial state to a goal state (or region), rather than exploring the full state space of the problem, as roadmap methods do, such as PRM. To achieve this objective, RRT grows a tree, rooted at an initial state, which is periodically extended towards random state samples until the goal is reached.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, RRT is well suited to complex motion planning tasks and, in particular, problems involving kinodynamic constraints. This is due to the fact that RRT can be implemented without a steering function, which is difficult to obtain for many systems with complex dynamics. (This function returns a path between two states in the absence of obstacles. It corresponds to solving a two-point boundary value problem (BVP), which may be a difficult task for many dynamical systems.) Moreover, RRT has low dependence on parameters and is easily extendable to a variety of domains (e.g., graspRRT for integrated motion and grasp planning ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since its introduction, numerous variations and extensions of RRT have been proposed (see, e.g., ), to allow improved performance. While RRT is not asymptotically optimal (AO) and provably does not converge to the optimal solution, it forms the basis of many AO planners, including RRT^∗^ and RRG. In particular, the probabilistic completeness (PC) of most of the aforementioned RRT-based algorithms is derived from the PC properties of RRT.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Surprisingly, it is not completely obvious under what conditions RRT is probabilistically complete, especially when using forward propagation of controls for the kinodynamic case. Indeed there has been some debate on this issue in the literature. This paper aims to address this gap.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

We provide two new proofs of PC of RRT. The first one for the purely geometric setting, where we only require that the solution path has a certain clearance from the obstacles. For the kinodynamic case with forward propagation of random controls and duration, we add mild Lipschitz-continuity conditions. This line of work lays sound foundations for arguing the probabilistic completeness of the variety of methods whose PC relies on that of RRT.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

Section II describes related work and Section III proceeds with the probabilistic completeness proof for the geometric case. Section IV gives a proof for the kinodynamic setting. A discussion on further research appears in Section V.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A PC of Kinodynamic RRT", "weight": 1.0} -->

LaValle and Kuffner discuss completeness of RRT in kinodynamic setting in one of the early works on the subject. While this work provides strong evidence for the PC of RRT, it only derives a proof sketch that does not fully addresses many of the complications that arise in analyzing sampling-based planners, be it a geometric or kinodynamic setting. For instance, the proofs in that paper assume the existence of "attraction sequences" and "basin regions", whose purpose is to lead the growth of the RRT tree toward the goal. It is not clear, however, whether such regions exist at all and for what types of robotic systems. It is also not clear whether the number of such regions is finite, and whether it is possible to produce samples in such regions with positive probability. Similar concerns were expressed by Caron et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A PC of Kinodynamic RRT", "weight": 1.0} -->

Indeed, in 2014, Kunz and Stilman showed that one of the variants of RRT mentioned in the original RRT paper is in fact not PC. In particular, they consider RRT which employs a fixed time step (rather than random propagation time which we use here) and a best-control input strategy, which picks the control input that yields the nearest state to the random sample. For this setting they describe a counterexample consisting of a specific robotic system for which RRT will have a success rate of $0$. The reason being that the state space reachable by this type of RRT is a strict subset of the actual reachable space of the robotic system. Completeness of the other variants was left as an open question.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A PC of Kinodynamic RRT", "weight": 1.0} -->

PC proofs of RRT under different steering functions and robot systems were presented in and. Specifically, Caron et al. consider state-based steering, which is different than forward propagation of random controls that we consider here. A setting similar to ours of random forward propagation was considered in and. It should be noted, however, that both papers consider a random-tree planner (and its extensions), which selects the next vertex to expand in a uniform and random manner among all its vertices, unlike RRT which expands the nearest neighbor toward a random sample point. Interestingly, the random tree is AO, in contrast to RRT which is not AO. Nevertheless, the selection process employed by RRT allows it to quickly explore the underlying state space when endowed with an appropriate metric.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Probabilistic completeness of RRT: The geometric case", "weight": 1.0} -->

We start by defining useful notation in Subsection III-A and then proceed to describe RRT for the geometric case. Then, in Subsection III-B, we provide the PC proof. We call the algorithm in this section GEOM-RRT to distinguish from the kinodynamic version. The geometric case, where a steering function exists and the dimension of the control space is identical to the dimension of the state space, can be considered as a special case of the kinodynamic setting. Thus, this section can be viewed as an introduction to the more involved kinodynamic setting, which is analyzed in the following section.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Let $\mathcal{X}$ be the state space, which is assumed to be ${\lbrack 0,1\rbrack}^{d}$ (a $d$-dimensional Euclidean hypercube), equipped with the standard Euclidean distance metric, whose norm we denote by $\parallel \cdot \parallel$. The free space is denoted by $\mathcal{F} \subseteq \mathcal{X}$. Given a subset $D \subseteq \mathcal{X}$ we denote by $|D|$ its Lebesgue measure. We will use $\mathcal{B}_{r}{(x)}$ to denote the ball of radius $r$ centered at $x \in {\mathbb{R}}^{d}$. Let $x_{\text{init}} \in \mathcal{F}$ denote the start state, and let $\mathcal{X}_{\text{goal}}$ be an open subset of $\mathcal{F}$ denoting the goal region.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

A motion-planning problem is implicitly defined by the triplet $(\mathcal{F},x_{\text{init}},\mathcal{X}_{\text{goal}})$. A solution to such a problem is a trajectory that moves the robot from the initial state to the goal region while avoiding collisions with obstacles. More formally, a valid trajectory is a continuous map $\pi:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow\mathcal{F}}$, such that ${\pi{}} = x_{\text{init}}$ and ${\pi{(t_{\pi})}} \in \mathcal{X}_{\text{goal}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

We describe in Algorithm 1 the (geometric) RRT algorithm, GEOM-RRT, based. The input for GEOM-RRT consists of an initial configuration $x_{\text{init}}$, goal region $\mathcal{X}_{\text{goal}}$, number of iterations $k$, and a steering parameter $\eta > 0$ used by the algorithm. GEOM-RRT constructs a tree $\mathcal{T}$ by preforming $k$ iterations of the following form. In each iteration, a new random sample $x_{\text{rand}}$ is returned from $\mathcal{X}$ uniformly by calling RANDOM_STATE. Then, the vertex $x_{\text{near}} \in \mathcal{T}$ that is nearest (according to $\parallel \cdot \parallel$) to $x_{\text{rand}}$ is found using NEAREST_NEIGHBOR.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

3: xrand← RANDOM_STATE 4: xnear ← NEAREST_NEIGHBOR (xrand, 𝒯) 5: xnew← NEW_STATE(xrand, xnear, η) 6: if COLLISION_FREE(xnear, xnew) then 7: 𝒯.add_vertex(xnew) 8: 𝒯.add_edge(xnear, xnew) Algorithm 1 GEOM-RRT(xinit, 𝒳goal, k, η) To retrieve a trajectory for the robot, the single path in $\mathcal{T}$ from the root state $x_{\text{init}}$ to the goal is found. It can then be translated to a feasible, collision-free trajectory for the robot by tracing the configurations along this path.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Probabilistic completeness proof", "weight": 1.0} -->

Next we devise a PC proof for GEOM-RRT. Throughout this section we will assume that there exists a valid trajectory $\pi:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow\mathcal{F}}$ with clearance $\delta_{\text{clear}} > 0$. Without loss of generality, assume that ${\pi{(t_{\pi})}} = x_{\text{goal}}$, i.e., the trajectory terminates at the center of the goal region. Denote by $L$ the (Euclidean) length of $\pi$. Also, let $\delta:={\min{\{\delta_{\text{clear}},\delta_{\text{goal}}\}}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Probabilistic completeness proof", "weight": 1.0} -->

Let $m = \frac{5L}{\nu}$, where $\nu = {\min{(\delta,\eta)}}$, and $\eta$ is the steering parameter of GEOM-RRT. Then, define a sequence of $m + 1$ points ${x_{0} = {x_{\text{init}},\ldots}},{x_{m} = x_{\text{goal}}}$ along $\pi$, such that the length of the sub-path between every two consecutive points is $\nu/5$. Therefore, ${\|{x_{i} - x_{i + 1}}\|} \leqslant {\nu/5}$ for every $0 \leqslant i < m$. Next, we define a set of $m + 1$ balls of radius $\nu/5$, centered at these points, and prove that with high probability GEOM-RRT will generate a path that goes through these balls.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Probabilistic completeness proof", "weight": 1.0} -->

We start by proving Lemma 1, which will be used in the proof of Theorem 1 and specifies a condition for successfully extending the tree to the goal.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Probabilistic completeness of RRT under differential constraints", "weight": 1.0} -->

We begin by formulating the kinodynamic problem. Our assumptions on the robotic system and the environment as well as the definitions appear in Subsection IV-A and are adapted from Li et al.. Next, we describe the modifications to RRT required for solving the kinodynamic problem. Finally, in Subsection IV-B, we devise a novel PC proof for the kinodynamic RRT.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Preliminaries", "weight": 1.0} -->

We adapt the problem attributes introduced in the previous section to accommodate the more involved structure of the kinodynamic case. The state space $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is a smooth $d$-dimensional manifold. Let $\mathcal{F} \subset \mathcal{X}$ denote the free state space. As before, we assume that there exist ${x_{\text{goal}} \in \mathcal{X}},{\delta_{\text{goal}} > 0}$, such that $\mathcal{X}_{\text{goal}} = {\mathcal{B}_{\delta_{\text{goal}}}{(x_{\text{goal}})}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Preliminaries", "weight": 1.0} -->

Let ${\mathbb{U}} \subseteq {\mathbb{R}}^{D}$ denote the space of control vectors. The given system has differential constraints of the following form: Trajectories under differential constraints are defined as follows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Probabilistic completeness proof", "weight": 1.0} -->

We prove that RRT for a system with dynamics satisfying the aforementioned characteristics is PC. To do so, we start by proving three lemmas. The following lemma, which is an extension of Theorem 15, bounds the distance between the endpoints of two trajectories with similar control inputs and initial positions, for the same duration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Discussion", "weight": 1.5} -->

Although our proofs assume uniform samples, they can be easily extended to samples generated using a Poisson point process, which is preferable in certain settings. An immediate extension of this work is to verify whether our proofs hold when other sampling distributions are considered, e.g., Halton sequences (see ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another possible direction is to further relax some of the assumptions made for kinodynamic systems, such as Lipschitz continuity. Additionally, the work raises the following challenging research question: Is it possible to extend these proofs that have a reduced set of assumptions to other sampling-based planners, or informed variants of RRT.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, we mention that the following variants of RRT are not addressed in the current paper, or in the work of Kunz and Stilman: (i) random time + best-control input; (ii) fixed time + random control; (iii) random time larger than a fixed threshold + random or best control. Whether these variants are indeed probabilistically complete remains as a question for future research.
