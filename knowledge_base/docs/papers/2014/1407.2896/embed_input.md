<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically Optimal Sampling-based Kinodynamic Planning

Topics include Kinodynamic planning, Asymptotic optimality, BVP-free, Sparse tree, SST.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

SST is a kinodynamic planner that requires no 2-point BVP solver or steering function, instead relying solely on forward propagation of control actions while maintaining a sparse sample set for computational efficiency.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based algorithms are viewed as practical solutions for high-dimensional motion planning. Recent progress has taken advantage of random geometric graph theory to show how asymptotic optimality can also be achieved with these methods. Achieving this desirable property for systems with dynamics requires solving a two-point boundary value problem (BVP) in the state space of the underlying dynamical system. It is difficult, however, if not impractical, to generate a BVP solver for a variety of important dynamical models of robots or physically simulated ones. Thus, an open challenge was whether it was even possible to achieve optimality guarantees when planning for systems without access to a BVP solver. This work resolves the above question and describes how to achieve asymptotic optimality for kinodynamic planning using incremental sampling-based planners by introducing a new rigorous framework. Two new methods, STABLE_SPARSE_RRT (SST) and SST*, result from this analysis, which are asymptotically near-optimal and optimal, respectively. The techniques are shown to converge fast to high-quality paths, while they maintain only a sparse set of samples, which makes them computationally efficient.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The good performance of the planners is confirmed by experimental results using dynamical systems benchmarks, as well as physically simulated robots.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kinodynamic Planning: For many interesting robots it is difficult to adapt a collision-free path into a feasible one given the underlying dynamics. This class of robots includes ground vehicles at high-velocities (Likhachev & Ferguson ), unmanned aerial vehicles, such as fixed-wing airplanes (Richter et al. ), or articulated robots with dynamics, including balancing and locomotion systems (Kuindersma et al. ). In principle, most robots controlled by the second-order derivative of their configuration (e.g., acceleration, torque) and which exhibit drift cannot be treated by a decoupled approach for trajectory planning given their controllability properties (Laumond et al.; Choset et al. ). To solve such challenges, the idea of *kinodynamic planning* has been proposed (Donald et al. ), which involves directly searching for a collision-free and feasible trajectory in the underlying system's state space. This is a harder problem than kinematic path planning, as it involves searching a higher-dimensional space and respecting the underlying flow that arises from the dynamics. Given its importance, however, it has attracted a lot of attention in the robotics community.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus in this work is on the properties of the popular sampling-based motion planners for kinodynamic challenges (Kavraki et al.; LaValle & Kuffner; Hsu et al.; Karaman & Frazzoli ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based Motion Planning: The sampling-based approach has been shown to be a practical solution for quickly finding feasible paths for relatively high-dimensional motion planning challenges (Kavraki et al.; LaValle & Kuffner; Hsu et al. ). The first popular methodology, the Probabilistic Roadmap Method (PRM) (Kavraki et al. ) focused on preprocessing the configuration space of a kinematic system so as to generate a roadmap that can be used to quickly answer multiple queries. Tree-based variants, such as RRT-Extend (LaValle & Kuffner ) and EST (Hsu et al. ), focused on addressing kinodynamic problems. For all these methods, the guarantee provided is relaxed to probabilistic completeness, i.e., the probability of finding a solution if one exists, converges to one (Kavraki et al.; Hsu et al.; Ladd & Kavraki ). This was seen as a sufficient objective in the community given the hardness of motion planning and the *curse of dimensionality*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, however, the focus has shifted from providing feasible solutions to achieving high-quality solutions. A milestone has been the identification of the conditions under which sampling-based algorithms are asymptotically optimal. These conditions relate to the connectivity of the underlying roadmap based on results on random geometric graphs (Karaman & Frazzoli ). This line of work provided asymptotically optimal algorithms for motion planning, such as PRM^∗^ and RRT^∗^ (Karaman & Frazzoli ).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lack of a BVP Solution: A requirement for the generation of a motion planning roadmap is the existence of a steering function. This function returns the optimum path between two states in the absence of obstacles. In the case of a dynamical system, the steering function corresponds to the solution of a two-point boundary value problem (BVP). Addressing this problem corresponds to solving a differential equation, while also satisfying certain boundary conditions. It is not easy, however, to produce a BVP solution for many interesting dynamical systems and this is the reason that roadmap planners, including the asymptotically optimal PRM^∗^, cannot by used for kinodynamic planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, RRT^∗^ also requires a steering function, as it reasons over an underlying roadmap even though it generates a tree data structure. While in certain cases it is sufficient to plan for a linearized version of the dynamics (Webb & van Den Berg ) or using a numerical approximation to the BVP problem, this approach is not a general solution. Furthermore, it does not easily address an important class of planning challenges, where the system is simulated using a physics engine. In this situation, the primitive available to the planning process is forward propagation of the dynamics using the physics engine. Thus, an open problem for the motion planning community was whether it was even possible to achieve optimality given access only to a forward propagation model of the dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Summary of Contribution: This paper introduces a new way to analyze the properties of incremental sampling-based algorithms that construct a tree data structure for a wide class of kinodynamic planning challenges. This analysis provides the conditions under which asymptotic optimality can be achieved when a planner has access only to a forward propagation model of the system's dynamics. The reasoning is based on a kinodynamic system's accessibility properties and probability theory to argue probabilistic completeness and asymptotic optimality for non-holonomic systems where *Chow's condition* holds, eliminating the requirement for a BVP solution.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A simplification of EST, which extends a tree data structure in a random way, referred to as NAIVE_RANDOM_TREE: It is shown to be asymptotically optimal but impractical as it does not have good convergence to high quality paths.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

An approach inspired by an existing variation of RRT, referred to as RRT-BestNear (Urmson & Simmons ), which promotes the propagation of reachable states with good path cost: It is shown to be asymptotically near-optimal and has a practical convergence rate to high quality paths but has a per iteration cost that is higher than that of RRT.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed algorithms STABLE_SPARSE_RRT (SST) and STABLE_SPARSE-RRT^∗^ (SST^∗^), which use the BestNear selection process. They apply a pruning operation to keep the number of nodes stored small: they are able to achieve asymptotic near-optimality and optimality respectively. They also have good convergence rate to high quality paths. SST has reduced per iteration cost relative to the suboptimal RRT given the pruning operation, which accelerates searching for nearest neighbors.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

An illustration of the proposed SST's performance for a kinematic point system is provided in Fig. 1. This is a simple challenge, where comparison with RRT^∗^ is possible. This is a problem where RRT typically does not return a path in the homotopic class of the optimum one. SST is able to do so, while also maintaining a sparse data structure. Fig. 2 describes the performance of different components of SST in searching the phase space of a pendulum system relative to RRT. No method is making use of a steering function for the pendulum system. A summary of the desirable properties of SST and SST^∗^ in relation to the efficient RRT and the asymptotically optimal RRT^∗^ is available in Table 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Probabilistically Complete (under conditions)
Probabilistically δ-Robust Complete / Probabilistically Complete

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Asymptotically δ-Robust Near-Optimal / Asymptotically Optimal

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single Propagation Per Iteration
Many Steering Calls Per Iteration
Single Propagation Per Iteration

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bounded Time Complexity Per Iteration / 1 Range Query + 1 NN Query

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Includes All Collision-Free Samples
Includes All Collision-Free Samples
Sparse Data Structure / Converges to All Collision-Free Samples

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Paper Overview: The following section provides a more comprehensive review of the literature and the relative contribution of this paper. Then, Section 3 identifies formally the considered problem and a set of assumptions under which the desired properties for the proposed algorithms hold. Section 4 first outlines how sampling-based algorithms need to be adapted so as to achieve asymptotic optimality and efficiency in the context of kinodynamic planning. Based on this outline, the description of SST and SST^∗^ is then provided, as well as an accompanying nearest neighbor data structure, which allows the removal of nodes to achieve a sparse tree. The description of the algorithms is followed by the comprehensive analysis of the described methods in Section 5. Simulation results on a series of systems, including kinematic ones, where comparison with RRT^∗^ is possible, as well as benchmarks with interesting dynamics are available in Section 6. A physically simulated system is also considered in the same section. Finally, the paper concludes with a discussion in Section 7.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

where ${x{(t)}} \in {\mathbb{X}} \subseteq R^{d}$ and ${u{(t)}} \in {\mathbb{U}} \subseteq R^{l}$. The collision-free subset of $\mathbb{X}$ is ${\mathbb{X}}_{f}$. Let $\mu{({\mathbb{X}})}$ denote the Lebesgue measure of $\mathbb{X}$. This work focuses on state space manifolds that are subsets of $d$-dimensional Euclidean spaces, which allow the definition of the ${\mathbb{L}}_{2}$ Euclidean norm $||.||$. The corresponding $r$-radius closed ball in $\mathbb{X}$ centered at $x$ will be $\mathcal{B}_{r}{(x)}$. In other words, the underlying state space needs to exhibit some smoothness properties and behave locally as a Euclidean space.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

*Chow's* condition of Small-time Locally Accessible (STLA) systems: For STLA systems, it is true that the reachable set of states $A{(x, \leq T)} \subset V$ from any state $x$ in time less than or equal to $T$ without exiting a neighborhood $V \subset {\mathbb{X}}$ of $x$, and for any such $V$, has the same dimensionality as $\mathbb{X}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

It is *Lipschitz continuous* for both of its arguments, i.e.,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

The assumption that $f$ satisfies *Chow's* condition implies there always exist $\delta$-similar trajectories for any trajectory $\pi$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 9", "weight": 1.0} -->

For a $\delta$-robust feasible motion planning problem, there exists a $\delta$-robust trajectory $\pi$ generated by a piecewise constant control function $\overline{\Upsilon}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 9", "weight": 1.0} -->

An incremental sampling-based algorithm, abbreviated here as $ALG$, typically extends a graph data structure of feasible trajectories over multiple iterations. This paper considers the following properties of such sampling-based planners.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 11", "weight": 1.0} -->

The cost function $cost{(\pi)}$ of a trajectory is assumed to be *Lipschitz continuous*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 11", "weight": 1.0} -->

for all $\pi_{1}$, $\pi_{2}$ with the same start state. Consider two trajectories $\pi_{1},\pi_{2}$ such that their concatenation is $\left. \pi_{1} \middle| \pi_{2} \right.$ (i.e.,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 11", "weight": 1.0} -->

Then, it is possible to relax the property of *asymptotic optimality* and allow some tolerance depending on the clearance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithms", "weight": 1.0} -->

This section provides sampling-based tree motion planners that achieve the properties of Definitions 10 and 12 for kinodynamic planning when there is no access to a BVP solver. First a general framework is described for this purpose, and then an instantiation of this framework is given (SST), which is extended to an asymptotically optimal algorithm (SST^∗^).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Traditional Approach: Given the difficulty of kinodynamic planning (Donald et al. ), the early but practical tree-based planners aimed for even and fast exploration of $\mathbb{X}$ even in challenging high-dimensional cases where greedy, heuristic expansion towards the goal would fail. Given that computing optimal trajectories corresponds to an even harder challenge, the focus was not on the quality of the returned trajectory in these early methods.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

3 xs e l e c t e d← Exploration_First_Selection(𝕍, 𝕏);
4 xn e w← Fixed_Duration_Prop(xs e l e c t e d, 𝕌, Tp r o p);
5 if CollisionFree$(\overline{x_{selected}\rightarrow x_{new}})$ then
7 ${\mathbb{E}}\leftarrow{{\mathbb{E}} \cup {\{\overline{x_{selected}\rightarrow x_{new}}\}}}$;
Algorithm 1 EXPLORATION_TREE(𝕏, 𝕌, x0, Tp r o p, N)

<!-- chunk {"id": "body-0034", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Algorithm 1 summarizes the high-level selection/propagation operation of these planners.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Selection: A reachable state along the tree, such as a node $x_{selected} \in V$, is selected. In some variants a state along an edge of the tree can also be selected. The selection process is designed so as to increase the probability of searching underexplored parts of $\mathbb{X}$. For instance, the RRT-Extend algorithm samples a random state $x_{rand}$ and then selects the closest node on the tree as $x_{selected}$. The objective is to achieve a ''Voronoi-bias'' that promotes exploration, i.e., nodes on the tree that correspond to the largest Voronoi regions of $\mathbb{X}$, given tree nodes as sites, have a higher probability of being selected ^11^1A tree-based planner without access to a BVP solver cannot guarantee a "Voronoi-bias" in general. If the distance function can correctly estimate the *cost-to-go* and if the propagation behaves similarly to the steering function, then the "Voronoi-bias" is achieved..

<!-- chunk {"id": "body-0036", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

In EST implementations, nodes store the local density of samples and those with low density are selected with higher probability to promote exploration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Propagation: The procedure for extending the tree has varied in the related literature but the scheme followed in RRT-Extend has been popular in most implementations. The approach is to select a control that drives the system towards the randomly sampled point, then forward propagate that control input for a fixed time duration. If the resulting trajectory $\overline{x_{selected}\rightarrow x_{new}}$ is collision-free, then it is added as an edge in the tree. It was recently shown that this propagation scheme actually makes RRT-Extend lose its probabilistic completeness guarantees. In EST, a randomized approach is employed where random controls are used. The analysis of the proposed methods shows that a randomized approach has benefits in terms of solution quality.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Challenge: Optimality has only recently become the focus of sampling-based motion planning, given the development of the asymptotically optimal RRT^∗^ and PRM^∗^. This great progress, however, does not address kinodynamic planning instances. Both planners are roadmap-based methods in the sense that they reason over (in the case of RRT^∗^) or explicitly construct (in the case of PRM^∗^) a graph that makes use of a steering function to connect states.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*Is it even possible to achieve asymptotic optimality guarantees in sampling-based kinodynamic planning?*

<!-- chunk {"id": "body-0040", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

This has been an open question in the algorithmic robotics community and resulted in many methods that aim to provide asymptotic optimality for systems with dynamics. The majority of these techniques, however, can address only specific classes of problems (e.g., systems with linear dynamics) and do not possess the generality of the original sampling-based tree planners.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Progress: The current work provides an answer to the above open question through a comprehensive, novel analysis of sampling-based processes for motion planning without access to a steering function, which departs from previous analysis efforts in this domain.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*It is possible to achieve asymptotic optimality in the rather general setting of this paper's problem setup with a sampling-based process that makes proper use of random forward propagation and a naïve selection strategy.*

<!-- chunk {"id": "body-0043", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*This method, however, is computationally impractical and does not have a good convergence rate to optimal solutions. Thus, the important question is whether there are planners with practical convergence to high-quality solutions.*

<!-- chunk {"id": "body-0044", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*Given this realization, this work describes a framework for computationally efficient sampling-based planners that achieve asymptotic near-optimality, which are then also extended to provide asymptotic optimality.*

<!-- chunk {"id": "body-0045", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Asymptotic Optimality from Random Primitives: To achieve these desirable properties it is necessary to clearly define the framework which sampling-based algorithms should adopt. In particular, it is possible to argue asymptotic optimality for the NAIVE_RANDOM_TREE process described in Algorithm 2. This algorithm follows the same selection/propagation scheme of sampling-based tree planners but applies uniform selection and calls the MonteCarlo-Prop procedure to extend the tree.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

The MonteCarlo-Prop procedure described in Algorithm 3 is different than the Fixed_Duration_Prop method that is frequently followed in implementations of sampling-based tree planners. The difference is that the duration of the propagation is randomly sampled between 0 and a maximum duration $T_{prop}$ instead of being fixed. The accompanying analysis (Section 5.1) shows that this random process provides asymptotic optimality when the only primitive to access the dynamics is forward propagation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Nevertheless, the NAIVE_RANDOM_TREE approach employs a naïve selection strategy, where a node $x_{selected}$ is selected uniformly at random. This has the effect that the resulting method does not have a good convergence rate in finding high-quality solutions as a function of iterations. It is not clear to the authors if a version of the NAIVE_RANDOM_TREE algorithm using an Exploration_First_Selection strategy is asymptotically optimal and most importantly *whether it has better convergence rate* properties, i.e., whether a method like EST or a version of RRT-Extend that employs MonteCarlo-Prop are asymptotically optimal with good convergence rate. The experimental indications for RRT-Extend with MonteCarlo-Prop are that it does not improve path quality quickly.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Improving Convergence Rate: A solution, however, has been identified to this issue. In particular, the authors propose the use of a Best_First_Selection strategy as a desirable alternative for node selection so as to achieve good convergence to high-quality paths. In this context, best-first means that the node $x_{selected}$ should be chosen so that the method prioritizes nodes that correspond to good quality paths, while also balancing exploration objectives. For instance, one way to achieve this in an RRT-like fashion (described in detail in the consecutive section) is shown in Figure 6, i.e., first sample a random state $x_{random}$ and then among all the nodes on the tree within a certain radius $\delta_{BN}$, select the one that has the best path cost from the root. A similar selection strategy has actually been proposed in the past as a variant of RRT that experimentally exhibited good behavior. This previous work, however, did not integrate this selection strategy with the MonteCarlo-Prop procedure and did not show any desirable properties for the resulting algorithm.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

The analysis shows that the consideration of a best first strategy together with the random propagation procedure leads to an asymptotically $\delta$-robust near-optimal solution with good convergence rate per iteration. This allows to observe improvement in solution paths over time in practice. Nevertheless, there are additional considerations to take into account when implementing a sampling-based planner. In particular, the asymptotically dominant operation computationally for these methods corresponds to nearest neighbor queries. The implementation of Best_First_Selection described above and in Figure 6 requires the use of a range query that is more expensive than the traditional closest neighbor query in RRT making the individual iteration cost of the proposed solution more expensive. Consequently, the challenge becomes whether this good convergence rate per iteration can be achieved, while also reducing the running time for each iteration.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Balancing Computation Cost with Optimality: The property achieved with the Best_First_Selection strategy is that of asymptotic $\delta$-robust near-optimality. This means that there should be an optimum trajectory $\pi^{\ast}$ in $\mathbb{X}$ which has $\delta$-robust clearance, as indicated in the problem setup. This property also implies that it is not necessary to keep all samples as nodes in the data structure so as to get arbitrarily close to $\pi^{\ast}$. It is sufficient to have nodes that are in the vicinity of the path that is defined by its robust clearance $\delta$. Thus, it is possible for a sparse data structure with a finite set of states to sufficiently represent $\mathbb{X}$ as long as it can return $\delta$-similar solutions to all possible optimal trajectories in $\mathbb{X}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

This allows for a pruning operation, where certain nodes can be forgotten. Which trajectories should a sampling-based planner maintain during its incremental operation and which ones should it prune? The idea is motivated by the same objectives as that of the Best_First_Selection strategy and is illustrated in Figures 7 and 8. The pruning operation should maintain nodes that correspond locally to good paths. For instance, it is possible to evaluate whether a node has the best cost in a local vicinity and prune neighbors with worse cost as long as they do not have children with good path costs in their local neighborhood. Nodes with high path cost in a local neighborhood do not need to be considered again for propagation. There are many different ways to define local neighborhoods. For instance, a grid-based discretization of the space could be defined. In the accompanying implementation and analysis, this work follows an incremental approach of defining visited regions of the state space space as described in Figure 8.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Note that, with high probability, the pruned high-cost nodes would not have been selected for propagation by the best first strategy anyway. In this manner, the pruning operation reinforces the properties of the Best_First_Selection procedure in terms of path quality. The accompanying analysis shows that the specific pruning operation is actually maintaining the convergence properties of the selection strategy. But it also provides significant computational benefits. Since the complexity of all the nearest neighbor queries depends on the number of points in the data structure, having a finite number of nodes, results in queries that have bounded time complexity per iteration. The benefits of sparsity in motion planning have been studied over the last few years by some of the authors and others. The discussion section of this paper describes the trade-offs that arise between computational efficiency and the type of guarantee achieved in relation to the requirement for the existence of $\delta$-robust trajectories.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

A New Framework: It is now possible to bring together the recommended changes to the original sampling-based tree planners and achieve a new framework for asymptotic near-optimality without a steering function in a computationally efficient way, both in terms of running time and memory requirements. Table 2 is summarizing the differences between the original methods (corresponding to the EXPLORATION_TREE procedure) and the proposed framework for kinodynamic sampling-based planning. The new framework is referred to as SPARSE_BEST_FIRST_TREE in Algorithm 4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

NAIVE_RANDOM_TREE
SPARSE_BEST_FIRST_TREE

<!-- chunk {"id": "body-0055", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Exploration_First_Selection
Best_First_Selection

<!-- chunk {"id": "body-0056", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

Probabilistically Complete (under conditions), Suboptimal but Computationally Efficient, Dense Data Structure
Asymptotically Optimal but Bad Convergence Rate and Impractical, Dense Data Structure
Asymptotically Near-Optimal with Good Convergence Rate and Computationally Efficient with a Sparse Data Structure

<!-- chunk {"id": "body-0057", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*Selection:* The new framework still promotes the selection of nodes in under-explored parts of $\mathbb{X}$, as in the original approaches, but within each local region only the nodes that correspond to the best path from the root are selected.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*Propagation:* The analysis accompanying this work emphasizes the need to employ a fully random propagation process both in terms of the selected control and duration of propagation, i.e., the MonteCarlo-Prop method, as in EST.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

*Pruning:* Nodes that are locally dominated in terms of path cost can be removed under certain conditions resulting in a sparse data structure instead of storing infinitely many points.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

3 xs e l e c t e d← Best_First_Selection( 𝕍, 𝕏);
6 if CollisionFree$(\overline{x_{selected}\rightarrow x_{new}})$ then
7 if Is_Node_Locally_the_Best( xn e w, 𝕍 ) then
9 ${\mathbb{E}}\leftarrow{{\mathbb{E}} \cup {\{\overline{x_{selected}\rightarrow x_{new}}\}}}$;
11 Prune_Dominated_Nodes( xn e w, G );
Algorithm 4 SPARSE_BEST_FIRST_TREE(𝕏f, 𝕌, x0, Tp r o p, N)

<!-- chunk {"id": "body-0061", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

The following section provides an efficient instantiation of the SPARSE_BEST_FIRST_TREE framework, which has been used both in the theoretical analysis and the experimental evaluation of this paper. This algorithm, called STABLE_SPARSE_RRT (SST), provides concrete implementations of the Best_First_Selection, Is_Node_Locally_the_Best and Prune_Dominated_Nodes procedures. The analysis shows that it is asymptotically near-optimal with a good convergence rate and computationally efficient.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Change in Algorithmic Paradigm", "weight": 1.0} -->

The near-optimality property stems from the consideration of $\delta$-robust optimal trajectories. The existence of at least weak $\delta$-robust clearance for optimal trajectories has been considered in the related literature that achieves asymptotic optimality in the kinematic case. To show asymptotic optimality for RRT^∗^, one can show that the requirement for the $\delta$ value reduces as the algorithm progresses. The true value $\delta$ depends on the specific problem to be solved and is typically not known beforehand. The way to address this issue is to first assume an arbitrary value for $\delta$ and then repeatedly shrink the value for answering motion planning queries. This is the approach considered here for extending SST into an asymptotically optimal approach SST^∗^.

<!-- chunk {"id": "body-0063", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

Algorithm 5 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning") provides a concrete implementation of the abstract framework of SPARSE_BEST_FIRST_TREE outlined in the previous section and corresponds to one of the proposed algorithms, STABLE_SPARSE_RRT (SST), which is analyzed in the next section.

<!-- chunk {"id": "body-0064", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

At a high-level, SST follows the abstract framework. For $N$ iterations, a selection/propagation/pruning procedure is followed. The selection follows the principle of the best first strategy to return an existing node on the tree $x_{selected}$ (line 5). Its concrete implementation is described in detail here. Then MonteCarlo-Prop is called (line 6), which samples a random control and a random duration and then integrates forward the system dynamics according to Eq. 1. If the path $\overline{x_{selected}\rightarrow x_{new}}$ is collision-free (line 7), the new node $x_{new}$ is evaluated on whether is the best node in terms of path cost in a local neighborhood (line 8). If $x_{new}$ is indeed better, it is added to the tree (lines 9-10) and any previous node in the same local vicinity that is dominated, is pruned (line 11).

<!-- chunk {"id": "body-0065", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

5 xs e l e c t e d←Best_First_Selection_SST( 𝕏, 𝕍a c t i v e, δB N);
8 if CollisionFree$(\overline{x_{selected}\rightarrow x_{new}})$ then
9 if Is_Node_Locally_the_Best_SST(xn e w, S, δs) then
11 ${\mathbb{E}}\leftarrow{{\mathbb{E}} \cup {\{\overline{x_{selected}\rightarrow x_{new}}\}}}$;
12 Prune_Dominated_Nodes_SST(xn e w, 𝕍a c t i v e, 𝕍i n a c t i v e, 𝔼 );
Algorithm 5 STABLE_SPARSE_RRT( 𝕏, 𝕌, x0, Tp r o p, N, δB N, δs)

<!-- chunk {"id": "body-0066", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

i\) SST requires an additional input parameter $\delta_{BN}$, used in the selection process of the Best_First_Selection_SST procedure shown in Alg. 6 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning"), inspired from previous work.

<!-- chunk {"id": "body-0067", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

ii\) SST requires an additional input parameter $\delta_{s}$, used to evaluate whether a newly generated node $x_{new}$ has locally the best path cost in the Is_Node_Locally_the_Best_SST procedure of Alg. 7 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning"), useful for pruning.

<!-- chunk {"id": "body-0068", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

iii\) SST splits the nodes of the tree $\mathbb{V}$ into two subsets: ${\mathbb{V}}_{active}$ and ${\mathbb{V}}_{inactive}$. The nodes in ${\mathbb{V}}_{active}$ correspond to nodes that in a local neighborhood have the best path cost from the root. The nodes ${\mathbb{V}}_{inactive}$ correspond to dominated nodes in terms of path cost but have children with good path cost in their local neighborhoods and for this reason are maintained on the tree for connectivity purposes. Lines 1 and 2 of Algorithm 5 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning") initialize the sets and the graph data structure $G{({\mathbb{V}},{\mathbb{E}})}$, which will be returned by the algorithm. Only nodes in ${\mathbb{V}}_{active}$ are considered for propagation and participate in the Best_First_Selection_SST procedure (line 5).

<!-- chunk {"id": "body-0069", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

These two sets are updated when a new state $x_{new}$ is generated that dominates its local neighborhood and pruning is performed (lines 9 and 11).

<!-- chunk {"id": "body-0070", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

iv\) In order to define local neighborhoods, SST uses an auxiliary set of states, called ''witnesses'' and denoted as $S$. The approach maintains the following invariant with respect to $S$: for every witness $s$ kept in $S$, a single node in the tree will represent that witness (stored in the field $s.{rep}$ of the corresponding witness), and that node will have the best path cost from the root within a $\delta_{s}$ distance of the witness $s$. All nodes generated within distance $\delta_{s}$ of the witness $s$ with a worse path cost then $s.{rep}$ are removed from ${\mathbb{V}}_{active}$, thereby resulting in a sparse data structure. Line 3 of Algorithm 5 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning") initializes the set $S$ to correspond to the root state of the tree, which becomes its own representative.

<!-- chunk {"id": "body-0071", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

The set $S$ is used by the Is_Node_Locally_the_Best_SST procedure to identify whether the newly generated sample $x_{new}$ is dominating the $\delta_{s}$-neighborhood of its closest witness $s \in S$. The same procedure is responsible for updating the set $S$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "STABLE_SPARSE_RRT (SST)", "weight": 1.0} -->

There are two input parameters to SST, $\delta_{BN}$ and $\delta_{s}$. $\delta_{BN}$ influences the number of nodes that are considered when selecting nodes to extend. The larger this parameter is, the more likely that exploration will be ignored and path quality will take precedent. For this reason, care must be taken to not make $\delta_{BN}$ too large. $\delta_{s}$ is the parameter responsible for performing pruning and providing a sparse data structure. As with $\delta_{BN}$, there is a tradeoff with $\delta_{s}$. The larger this parameter is, the more pruning will be performed, which helps computationally but then problems may not be solved if it is not possible to sample inside narrow passages.

<!-- chunk {"id": "body-0073", "role": "body", "section": "STABLE_SPARSE-RRT^∗^ (SST\\*)", "weight": 1.0} -->

SST is providing only asymptotic $\delta$-robust near-optimality. Asymptotic optimality cannot be achieved by SST directly primarily due to the fixed sized pruning operation employed. The solution to this is to slowly reduce the radii $\delta_{BN}$ and $\delta_{s}$ employed by the algorithm eventually converging to iterations that are similar to the NAIVE_RANDOM_TREE approach. The key to SST^∗^, which is provided in Algorithm 9 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning"), is to make sure that the rate of reducing the pruning is slow enough to achieve an anytime behavior, where initial solutions are found for large radii and then they are improved. As the radii decrease, the algorithm is able to discover new homotopic classes that correspond to narrow passages where solution trajectories have reduced clearance.

<!-- chunk {"id": "body-0074", "role": "body", "section": "STABLE_SPARSE-RRT^∗^ (SST\\*)", "weight": 1.0} -->

SST^∗^ provides a schedule for reducing the two radii parameters to SST, $\delta_{BN}$ and $\delta_{s}$ over time. It receives as input an additional parameter $\xi$, which is used to decrease the radii $\delta_{BN}$ and $\delta_{s}$ over consecutive calls to SST (note that $d$ and $l$ are the dimensionalities of the state and control spaces respectively). This, in effect, makes pruning more difficult to occur, turns the selection procedure more towards an exploration objective instead of a best-first strategy and increases the number of nodes in the data structure. As the number of iterations approaches infinity, pruning will no longer be performed, the selection process works in a uniformly at random manner and all collision-free states will be generated.

<!-- chunk {"id": "body-0075", "role": "body", "section": "STABLE_SPARSE-RRT^∗^ (SST\\*)", "weight": 1.0} -->

Alg. 9 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning") is a meta-algorithm that repeatedly calls SST as a building block. In the above call, SST is assumed to be operating on the same graph data structure $G$ over repeated calls. It is possible to take advantage of previously generated versions of the graph data structures with some additional considerations, e.g., instead of clearing out all states in $V_{active}$ from previous iterations, one can carefully modify the pruning procedure to take advantages of the existing $V_{active}$ set given the updated radii.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The implementation of SST imposes certain technical requirements from the underlying nearest neighbor data structure that are not typical for existing sampling-based motion planners. In particular, given the pruning operation, it is necessary to have an efficient implementation of deletion from the nearest neighbor data structure. In most nearest neighbor structures, a removal of a node will cause the entire data structure to be frequently rebuilt, severely increasing run times.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The goal here is to describe a simple idea for performing approximate nearest neighbor search using a graph structure $\mathbb{G}$ that stores the nodes of the tree and on its edges stores distances between them according to $d_{x}{( \cdot, \cdot )}$. This approach builds on top of ideas from random graph theory. Graphs are conducive to easy removal, but some overhead is placed in node addition to maintain this data structure incrementally.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The key operation is finding the closest node in a graph, which is performed by following a hill climbing approach shown in Algorithm 10. A random set of nodes is first sampled from the existing structure, proportional to $\sqrt{\|{\mathbb{V}}\|}$ (line 1). From this set of nodes, the closest node to the query node $v$ is determined by applying linear search according to $d_{x}{( \cdot, \cdot )}$ (line 2). From the closest node, a hill climbing process is performed by searching the local neighborhood of the closest node on the graph to identify whether there are nodes that are closer to the query one (line 3-6). Once no closer nodes can be found, the locally best node is returned (line 7).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

On top of this operation, it is also possible to define a way for approximately finding the $k$-closest nodes or the nodes that are within a certain radius $\delta$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The idea in both cases is to start from the closest node by calling Algorithm 10. Then, each corresponding method searches the local neighborhoods of the discovered nodes (initially just the closest node) for either the $k$-closest ones or those nodes that are within $\delta$ distance. The methods iterate by searching locally until there is no change in the list.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The process of adding nodes to the nearest neighbor data structure is shown in Algorithm 12. It is achieved by first finding the $k$ closest nodes and then adding edges to them. The number $k$ should be at least a logarithmic number of nodes as a function of the total number of nodes to ensure the graph is connected (similar to PRM^∗^).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Nearest Neighbor Data Structure", "weight": 1.0} -->

The reason for using a graph data structure for the nearest neighbor operations is the ease of removal shown in Algorithm 13. Most implementations of graph data structures provide such a primitive that is typically quite fast. This can be sped up even more if a link to the nearest neighbor graph node is kept with the tree node allowing for constant time removal.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section, arguments for the proposed framework are provided. Sec. 5.1 begins by discussing the requirements of MonteCarlo-Prop and what properties this primitive provides. Then, in Sec. 5.2, an analysis of the NAIVE_RANDOM_TREE approach is outlined, showing that this algorithm can achieve asymptotic optimality. To address the poor convergence rate of that approach, the properties of using the best-first selection strategy are detailed in Sec. 5.3. Finally, in order to introduce the pruning operation, properties of SST and SST^∗^ are studied in Sec. 5.4 and 5.5.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Properties of MonteCarlo-Prop", "weight": 1.0} -->

The MonteCarlo-Prop procedure is a simple primitive for generating random controls, but provides desirable properties in the context of achieving asymptotic optimality properties for systems without access to a steering function. This section aims to illustrate these desirable properties, given the assumptions from Section 3. Much of the following analysis will use these results to prove the probabilistic completeness and asymptotic near-optimality properties of SST and asymptotic optimality of SST^∗^. These algorithms are using MonteCarlo-Prop for generating random controls.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Properties of MonteCarlo-Prop", "weight": 1.0} -->

The analysis first considers a $\delta$-robust optimal path for a specific planning query, which is guaranteed to exist for the specified problem setup. For such a path, consider a covering ball sequence (an illustration is shown in Fig.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Naive Algorithm: Already Asymptotically Optimal", "weight": 1.0} -->

This section considers the impractical sampling-based tree algorithm outlined in Algorithm 2, which does not employ a steering function. Instead, it selects uniformly at random a reachable state in the existing tree and applies random propagation to extend it. The following discussion argues that this algorithm eventually generates trajectories $\delta$-similar to optimal ones. The general idea is to prove by induction that a sequence of trajectories between the covering balls of an optimal trajectory can be generated. This proof shows probabilistic completeness. Then, from the properties of MonteCarlo-Prop, the quality of the trajectory generated in this manner is examined. Finally, if the radius of the covering-ball sequence tends toward zero, asymptotic optimality is achieved.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Using BestNear: Improving Convergence Rate", "weight": 1.0} -->

A computationally efficient alternative to NAIVE_RANDOM_TREE for finding a path, if one exists, is referred to here as RRT-BestNear, which works like NAIVE_RANDOM_TREE but switches line 3 in Algorithm 2 with the procedure in Algorithm 6 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning"). An important observation from the complexity discussion for NAIVE_RANDOM_TREE is that the exponential term arises from the use of uniform random sampling for selection among the existing nodes. By not using any path cost information when performing selection, the likelihood of generating good trajectories becomes very low, even if it is still non-zero.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Using BestNear: Improving Convergence Rate", "weight": 1.0} -->

The analysis of RRT-BestNear involves similar event constructions as in the previous section: $A_{k}^{(n)}$ and $E_{k}^{(n)}$ are defined as in the previous section, except the endpoint of the trajectory segment generated must be in $\mathcal{B}_{\delta_{BN}}{(x_{k}^{\ast})}$. The propagation from MonteCarlo-Prop still has positive probability of occurring, but is different from $\rho_{\delta}$. The changed probability for MonteCarlo-Prop to generate such a trajectory is defined as $\rho_{\delta\rightarrow\delta_{BN}}$ The probabilities of these events will also change due to the new selection process and more constrained propagation requirements. It must be shown that nodes that have good quality should have a positive probability of selection. Consider the selection mechanism BestNear in the context of Figure 13.

<!-- chunk {"id": "body-0089", "role": "body", "section": "STABLE_SPARSE_RRT Analysis", "weight": 1.0} -->

This section argues that the introduction of the *pruning process* in SST does not compromise asymptotic $\delta$-robust optimality and improves the computational efficiency. Consider the selection mechanism used in SST.

<!-- chunk {"id": "body-0090", "role": "body", "section": "SST\\* Analysis", "weight": 1.0} -->

In SST, for given $\delta$, $\delta_{s}$, and $\delta_{BN}$ values, $\gamma_{sst}$ and $\rho_{\delta\rightarrow\delta_{c}}$ are two constants describing the probability of selecting a near-optimal state for propagation and of successfully propagating to the next ball region. Note that if $\delta_{BN}$ and $\delta_{s}$ are reduced over time, the related $\delta$ value can be smaller. This is the intuition behind why SST^∗^ provides asymptotic optimality. If after a sprint of iterations where $\delta_{BN}$ and $\delta_{s}$ are kept static, they are reduced slightly, this should allow for the generation of trajectories with smaller clearance, i.e., closer to the true optimum.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

2 Dim. State, 1 Dim. Control, No Damping

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

In order to evaluate the proposed method, a set of experiments involving several different systems have been conducted. The proposed algorithm SST is compared against RRT as a baseline and also with another algorithm: (a) if a steering function is available, a comparison with RRT^∗^ is conducted, (b) if RRT^∗^ cannot be used, a comparison with an alternative based on a ''shooting'' function is utilized. Different versions of RRT were evaluated depending on the benchmark. In the case where a steering function is available, RRT corresponds to RRT-Connect. When a steering function is not available, a version of RRT using MonteCarlo-Prop is used, which is similar to RRT-Extend.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

The overall results show that SST can provide consistently improving path quality given more iterations as RRT^∗^ does for kinematic systems, achieving running times equivalent (if not better than) RRT, and maintaining a small number of nodes, all while using a very simple random propagation primitive.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Kinematic Point. A simple system for a baseline comparison.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

3D Rigid Body. A free-flying rigid body. The state space is 6D $(x,y,z,\alpha,\beta,\gamma)$ signifying the space of SE and the control space is 6D $(\overset{˙}{x},\overset{˙}{y},\overset{˙}{z},\overset{˙}{\alpha},\overset{˙}{\beta},\overset{˙}{\gamma})$ representing the velocities of these degrees of freedom.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Simple Pendulum. A pendulum system typical in control literature.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Cart-Pole. Another typical control system where a block mass on a track has to balance a pendulum. The state space is 4D $(x,\theta,\overset{˙}{x},\overset{˙}{\theta})$ and the control space is 1D $(f)$ which is the force on the block mass. The dynamics are.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Two-link Acrobot. The two-link acrobot model with a passive root joint. The state space is 4D $(\theta_{1},\theta_{2},\overset{˙}{\theta_{1}},\overset{˙}{\theta_{2}})$ and the control space is 1D $(\tau)$ which is the torque on the active joint. The dynamics are.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Fixed-wing airplane. An airplane flying among cylinders. The state space is 9D $(x,y,z,v,\alpha,\beta,\theta,\omega,\tau)$, the control space is 3D $(\tau_{des},\alpha_{des},\beta_{des})$, and the dynamics are.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Quadrotor. A quadrotor flying through windows. The state space is 12D $(x,y,z,\alpha,\beta,\gamma,\overset{˙}{x},\overset{˙}{y},\overset{˙}{z},\overset{˙}{\alpha},\overset{˙}{\beta},\overset{˙}{\gamma})$, the control space is 4D $(w_{1},w_{2},w_{3},w_{4})$ corresponding to the rotor torques, and the dynamics are.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Quality of Solution Trajectories", "weight": 1.0} -->

In Figure 16 the average solution quality to nodes in each tree is shown. This average is a measure of the quality of trajectories generated to all reachable parts of the state space. In every case, SST is able to improve quality over time. By looking at all of the nodes in the tree as a whole, the global behavior of improving path costs can be observed. RRT will increase this average over time because it chooses suboptimal nodes and further propagates them, thus making those average values increase over time.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Quality of Solution Trajectories", "weight": 1.0} -->

It is interesting to note that the approach based on the shooting function had varying success in these scenarios. The systems with highly nonlinear dynamics (e.g., all the systems with a pendulum-like behavior) did not perform better than RRT. This could result from the choice of distance function for these scenarios or from the inaccuracy in the shooting method. Notably, SST does not have this problem for the same distance function and with random propagations and continues to provide good performance. The shooting method did perform well in the quadrotor environment, but failed to return solutions for most of the fixed-wing airplane runs and was therefore omitted.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Time Efficiency", "weight": 1.0} -->

SST has another advantage over other RRT variants. Due to the pruning operation, there is another criterion in addition to being collision-free that newly generated states must satisfy to be added to the tree. Any new state must both be collision-free and dominant in the region around the witness sample in $S$. Because of this, the collision check at Line 8 of Algorithm 5 ‣ 4 Algorithms ‣ Asymptotically Optimal Sampling-based Kinodynamic Planning") can be shifted to after Line 15. In the event that collision checking is more expensive than a nearest neighbor query in $S$, this can result in improved computational efficiency depending on the scenario. This strategy was not used in these experiments, but can be beneficial in domains where collision checking is the dominant computational factor.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Space Efficiency", "weight": 1.0} -->

One of the major gains of using SST is the smaller number of nodes that are needed in the data structure. Figure 18 shows the number of nodes stored by each of the algorithms. The number of nodes is significantly lower in SST, even when considering the witness set $S$. The sparse data structure of SST makes the memory requirements quite small, in contrast to RRT and RRT^∗^, which do not perform any pruning operations. In the case of shooting, sometimes the inaccuracy of the shooting primitive will cause collisions to occur in resimulated trees, pruning them from the data structure. This can lead to losing solution trajectories.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Space Efficiency", "weight": 1.0} -->

These results showcase the large efficiency gains when a sparse data structure can be generated. There is a tradeoff, however, between the sparseness of the data structure and allowing for a diverse set of paths to be generated. Path diversity can be helpful for discovering the homotopic class of the optimal solution in practice. In all of these scenarios, there is either only one homotopic class for solutions or the pruning radius $\delta_{s}$ is small enough to allow each homotopic class to be potentially explored. Even considering this, significant pruning can still be achieved.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Space Efficiency", "weight": 1.0} -->

One can draw parallels between SST and grid-based methods, as both methodologies end up maintaining a discrete set of witness states in the state space. One concern with grid-based approaches is that they have an exponential dependency in the dimensionality of the state space. In the worst case, SST shares the same property. At the same time, however, it has certain advantages. Typically, the discretization followed by grid-based methods corresponds to fixed witnesses defined before the problem is known. In SST the witnesses arise on the fly and are adaptive to the features of the state space. A benefit of following this approach is the capability to find solutions sooner in practice without explicitly constructing or reasoning over the entire grid, which has an exponential number of points. After an initial solution is found, witness nodes can be removed, improving space complexity even further, similar to branch-and-bound techniques.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Dependence on Parameters", "weight": 1.0} -->

Table 4 shows statistics for running SST with several different parameter choices. The problem setup is the simple case of the 2D kinematic point. Larger values for the pruning radius, $\delta_{s}$, result in initial solutions being discovered sooner. Larger values also restrict the convergence to better solutions. Larger values for the selection radius, $\delta_{BN}$, provide better solution cost for initial solutions, but requires more computational effort. These tradeoffs can be weighed for the application area depending on the importance of finding solutions early and the quality of those solutions.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Physically-simulated Car Evaluation", "weight": 1.0} -->

One of the more interesting applications of SST is in the domain of planning for physically-simulated systems. SST is able to provide improving path quality given enough time and keeps the number of forward propagations to one per iteration as shown in Figure 19. In this setup, the computational cost of propagation overtakes the cost of nearest neighbor queries. Nearest neighbor queries become the bottleneck in problems, such as the kinematic point, where propagation and collision checking are cheap. In the physically simulated case, however, these primitives are expensive, therefore focusing the motion planner on good quality paths is especially important. In this respect, SST is suited to plan for physically-simulated systems.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Physically-simulated Car Evaluation", "weight": 1.0} -->

This physically-simulated car is modeled through the use of a rectangular prism chassis, two wheel axles, and four wheels, creating a system with 7 rigid bodies. These rigid bodies are linked together with virtual joints in the Bullet physics engine. The front axle is permitted to rotate to simulate steering angle and thrust is simulated as a force on the chassis. The data provided in Figure 19 is generated by planning for the car in an open environment and attempting to reach a goal state denoted by x,y and heading.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Physically-simulated Car Evaluation", "weight": 1.0} -->

Using SST for a physically simulated system raises the question of whether this is a case where asymptotic optimality can be argued formally. Note, that in this case, contacts arise between the moving system and the plane. Such contacts typically violate the assumptions specified in the problem setup and in this manner the formal guarantees described in this work do not necessary apply. Nevertheless, it is encouraging that the algorithm is still exhibiting good performance, in terms of being able to improve the quality of the solution computed over time. This is probably because such real-world problems still exhibit a certain level of smoothness that allows the algorithm to prune suboptimal solutions. As described in the Discussion section of this paper, future research efforts will focus on generalizing the provided analysis and include interesting challenges where contacts arise, including dexterous manipulation and locomotion.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Graph-based Nearest Neighbor Structure", "weight": 1.0} -->

In order to evaluate the graph-based nearest neighbor structure, comparisons to two other alternatives are shown. First, a baseline comparison with a brute force search is provided. This provides the worst-case performance computationally that more intelligent search methods should be able to overcome. Next, an approximate nearest neighbor structure is used. This approach follows the popular kd-trees approach to space decomposition and nearest neighbor queries. In the following experiments, the same environments for the kinematic point and the airplane systems are used, and comparisons are made between RRT, RRT^∗^, and SST.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Graph-based Nearest Neighbor Structure", "weight": 1.0} -->

A comparison of the resulting solution quality between planners that use different nearest neighbor structures is shown in Figures 20 and 21. In the case of RRT, where the Voronoi bias heavily affects the expansion process, having an exact brute force metric actually provides small benefits in terms of quality. For RRT^∗^ and SST, small approximation errors when returning nearest neighbors can actually result in generating longer edges that help in path quality. This causes a small improvement in path quality for these algorithms.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Graph-based Nearest Neighbor Structure", "weight": 1.0} -->

In Figure 22, timing data for each of the nearest neighbor structures is shown. As expected in RRT and RRT^∗^, the brute force method is worse than either of the approximate structures. The graph-based structure slightly outperforms the alternative method. An interesting effect occurs in the case of SST however. Since SST maintains a small number of nodes for this problem instance, the brute force search can actually be competitive with the graph-based nearest neighbor. The alternative method that does not explicitly handle removal is much slower than the graph structure for SST, mainly due to having to rebuild its internal structure when too many nodes are removed.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Graph-based Nearest Neighbor Structure", "weight": 1.0} -->

Table 5 shows the accuracy of the graph-based method compared to the other methods. While resulting in some query errors, the number of errors is less than the comparison method.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Recently, the focus in sampling-based motion planning has moved to providing optimality guarantees, while balancing the computational efficiency of the related methods. Achieving this objective for systems with dynamics has generally required the generation of specialized steering functions. This work shows that a fully-random selection/propagation procedure can achieve asymptotic optimality under reasonable assumptions for kinodynamic systems. The same method, however, has a very slow convergence rate to finding high-quality solutions, which indicates that the focus should primarily be on the convergence rate of methods that provide path improvement over time.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

To address these issues, this work proposed a new framework for asymptotically optimal sampling-based motion planning. The departure from previous work is the utilization of best-first selection strategy and a pruning process, which allow for fast convergence to high-quality solutions and a sparse data structure. Experiments and analytical results show the running time and space requirements of a concrete implementation of this framework, i.e., the SST approach, are better even than that of the efficient but suboptimal RRT, while SST can still improve path quality over time. This performance increase is seen in many different scenarios, including in the case of a physically-simulated system.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Parameter Selection: The two parameters of SST, namely $\delta_{s}$ and $\delta_{BN}$, directly affect the performance of the algorithm. Since the $\delta_{s}$ radius controls how much pruning SST will perform, it is necessary that this parameter is not set too high because it can lead the algorithm not to discover paths through narrow passages. Practically, $\delta_{s}$ can be as large as the clearance of paths desired from a given problem instance. It is also helpful to choose this value to be smaller than the radius of the goal region, so as to allow the generation of a sample close to the goal.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

The parameter $\delta_{BN}$ should be larger than $\delta_{s}$ to allow the tree data structure to properly expand. A value for $\delta_{BN}$ that is too large will result in poor exploration of the state space since nodes closer to the root will be selected repetitively. Overall, a balance between the state space size, $\delta_{BN}$, and $\delta_{s}$ must be maintained to achieve good performance. The SST^∗^ approach allows to start the search using rather arbitrary large values for $\delta_{s}$ and $\delta_{BN}$, which then automatically decrease over time.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Finite-time Properties: Since SST maintains a relatively small data structure, and in bounded spaces it results in a finite size data structure, it is interesting to consider the finite-time properties that can be argued. This depends significantly on the rate at which the witness set $S$ can cover the free space. After this initial coverage, it may be possible to examine the quality of the existing paths.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Planning under Uncertainty: By removing the requirement of the steering function, SST can be applied to other problems where steering functions are difficult to construct. One of these areas is planning under uncertainty, where planning is performed in belief space. It is difficult to compute a steering function that connects two probability distributions in this domain, but forward propagation can update the corresponding beliefs. Some challenges in applying SST to this domain involve computing appropriate distance metrics for the best first and pruning operations, as well as the increased dimensionality of the problem. Some progress has been recently achieved in this direction, where it has been shown that in the context of the methods described in the current paper a suitable function based on the Earth Mover's distance can lead to efficient solutions when planning under uncertainty. This can lead eventually to the application of such solutions to important problems that involve significant uncertainty, such as kinodynamic and non-prehensile manipulation (e.g., pushing, throwing, pulling, etc).

<!-- chunk {"id": "body-0121", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Feedback-based Motion Planning: Another extension relates to feedback-based motion planning and the capability to argue that the computed trajectories are dynamically stable. The current work follows the majority of the literature in sampling-based kinodynamic planning and is providing only nominal trajectories and not feedback-based plans or policies. There has been work that takes advantage of sampling in the context of feedback-based motion planning, such as the work on LQR-trees. Nevertheless, it has been typically difficult to argue about the optimality of a feedback-based solution when it comes to realistic and relatively high-dimensional dynamical robotic systems. In this way, an interesting research direction is to identify the conditions under which it will be possible to provide such guarantees in the context of feedback-based planning.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Real-world Experiments and Applications: It is also important to evaluate the effectiveness of the approach on real systems with significant dynamics, especially aerial systems that perform aggressive maneuvers and systems modeled through the use of physics engines. For example, future planetary exploration missions may involve more capable rovers. They will have the capability to move at higher speeds in low gravity environments, potentially acquiring ballistic trajectories for small periods of time. Thus, reasoning about the dynamics becomes more important during the planning process. SST may be useful in this domain to optimize paths with respect to path length, energy expenditure, or the sensitivity of the sensor payload on-board.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Locomotion and Dexterous Manipulation: Other potential research domains where SST may be used include locomotion and dexterous manipulation. These challenges involve planning using models of contact between objects and physical considerations, such as balancing of a locomotion system or stability of a grasp for a manipulator. The use of a physics engine to model friction and mass effects can be useful here. As demonstrated above, SST provides control sequences that improve over time when a physics engine is used. Nevertheless, the presence of contacts introduces important complexities that are not currently handled by the presented analysis.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In particular, there are two critical assumptions which complicate the generalization of the provided results: (a) the system dynamics are expressed in the form of equation 1, which is a nonlinear ordinary differential equation, and (b) the manifolds in which the systems live are smooth subsets of a $d$-dimensional Euclidean space. These assumptions do not allow to consider models of rigid body dynamics and stick-slip friction, which are useful idealizations of locomotion and dexterous manipulation. Such systems exhibit jump-discontinuities and in general cannot be represented by expressions of the form in Equation 1. There is also a question of whether it is possible to address challenges in spaces, which are not locally Euclidean.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

It would be interesting to study manifolds generated by contact constraints. Such manifolds can be algebraic varieties, which need not be smooth. Furthermore, such manifolds can be of different dimensions, as finger gaiting and locomotion problems really don't live on varieties of a single dimension, but live on stratified sets in a higher-dimensional ambient state space. These issues motivate further research in the direction of providing general sampling-based algorithms that exhibit asymptotic optimality guarantees for proper models of dexterous manipulation and locomotion systems.
