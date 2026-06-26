<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CAT-ORA: Collision-Aware Time-Optimal Formation Reshaping for Efficient Robot Coordination in 3D Environments

Topics include Robotics, Vehicles, CAT-ORA, Time-optimal, Formation reshaping, Collision avoidance.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we introduce an algorithm designed to address the problem of time-optimal formation reshaping in three-dimensional environments while preventing collisions between agents. The utility of the proposed approach is particularly evident in mobile robotics, where agents benefit from being organized and navigated in formation for a variety of real-world applications requiring frequent alterations in formation shape for efficient navigation or task completion. Given the constrained operational time inherent to battery-powered mobile robots, the time needed to complete the formation reshaping process is crucial for their efficient operation, especially in case of multi-rotor Unmanned Aerial Vehicles (UAVs). The proposed Collision-Aware Time-Optimal formation Reshaping Algorithm (CAT-ORA) builds upon the Hungarian algorithm for the solution of the robot-to-goal assignment implementing the inter-agent collision avoidance through direct constraints on mutually exclusive robot-goal pairs combined with a trajectory generation approach minimizing the duration of the reshaping process. Theoretical validations confirm the optimality of CAT-ORA, with its efficacy further showcased through simulations, and a real-world outdoor experiment involving 19 UAVs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Thorough numerical analysis shows the potential of CAT-ORA to decrease the time required to perform complex formation reshaping tasks by up to 49%, and 12% on average compared to commonly used methods in randomly generated scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

T EAMS of autonomous mobile robots have found practical applications in various real-world scenarios, including search and rescue operations -, environmental monitoring precision agriculture, and automated warehouse systems. In most cases, these teams consist of robots working together to achieve a common objective while independently navigating through the environment and Authors are with the Department of Cybernetics, Faculty of Electrical Engineering, Czech Technical University in Prague, Technicka 2, Prague 6, Czech Republic.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

∗ Corresponding author, { vit.kratky|penicrob|horynjir|stibipet |bacatoma|matej.petrlik|stepan|martin.saska } @fel.cvut.cz This work was partially funded by the CTU grant no. /177/OHK3/3T/13, by the Czech Science Foundation (GA ˇ CR) grant no. 23-06162M, and by the European Union under the project Robotics and advanced industrial production (reg. no. CZ.02.01.01/00/22 008/0004590).

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Fig. 1: Deployment of the introduced Collision-Aware Time-Optimal formation Reshaping Algorithm (CAT-ORA) in a small-scale drone visual performance with 19 UAVs. The images show the transition of UAVs guided by the CAT-ORA from a triangular shape (a) to a ring shape (b). This transition was performed within 7 seconds. The blue lines highlight the shape of the formation in top view images, while (c) captures the flying formation from the side. The red point represents a missing UAV that failed to start due to a HW failure. avoiding collisions. However, in certain applications, it is advantageous for mobile robots to be arranged in a specific formation to accomplish desired tasks, such as documenting historical buildings, monitoring wildfires, or creating drone light shows,. In these scenarios, the robots often need to adjust their positions relative to one another to achieve the required formation shape for the mission's execution. Considering the formation shape adaptation as part of a robotic mission, the time efficiency of this process becomes of great importance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This applies specifically to vehicles with operational time significantly constrained by battery endurance, such as multi-rotor Unmanned Aerial Vehicles (UAVs), especially in time critical missions such as search and rescue and applications requiring highly dynamic performance, such as drone light shows.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper tackles the Time-Optimal Formation Reshaping Problem (TOFREP) with collision avoidance guarantees. The problem involves finding the assignment of robots to goals coupled with the generation of minimum-time collision-free trajectories. From the robotics perspective, the formation reshaping problem is a specific instance of cooperative motion planning. However, instead of having specific goals assigned to individual robots, the group of robots is given a set of unassigned goals to visit. The algorithms for the solution of assignment problems have been widely tackled in literature. However, since robots are physical entities sharing an environment, mutual collision avoidance has to be considered during the assignment process. This consideration implies that, in general, the individual cost of assigning two robot-goal pairs in a matching depends on the other assigned pairs, preventing a direct use of algorithms for the solution of general assignment problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Previous works in the field of formation reshaping vary in the level of decentralization, complexity, dimensions of the environment, optimization criteria, and applied methodology -. Although the completion time of the reshaping process is a critical factor for algorithms deployed on robots with limited operational time, only a few works have taken the time criterion into account -. However, none has addressed the minimization of completion time while simultaneously accounting for mutual collision avoidance among robots and the kinematic constraints associated with robots as physical entities. Furthermore, these works lack guarantees regarding the solution completeness and quality, which is one aspect that limits the transfer of the algorithms to industrial applications where we observe a clear tendency to favour robotic systems with predictable and well-defined behavior guided by clear, understandable rules.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To this end, we address the problem of the time-efficient collision-free formation reshaping in 3D environments by introducing a centralized, deterministic Collision-Aware TimeOptimal formation Reshaping Algorithm (CAT-ORA) directly optimizing the completion time (the so-called makespan) of the formation reshaping process while providing guarantees on a minimum mutual distance of involved agents (inter-agent collision avoidance). The proposed approach comprises two key components designed together to allow us to provide theoretical guarantees of the overall complex robotic system's behavior: (i) an algorithm for optimal robot-to-goal assignment considering mutual collision avoidance among robots, and (ii) a computationally efficient trajectory generation approach minimizing the completion time of a set of trajectories. CAT-ORA builds upon the Hungarian algorithm, adapted to solve the robot-to-goal assignment as Linear Bottleneck Assignment Problem (LBAP) effectively managing potential collisions between assigned robot-goal pairs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The designed approach to the generation of a set of trajectories is based on a closed-form solution to the minimum-time single-trajectory generation problem adapted to generate a set of trajectories minimizing their makespan, while keeping collision-free properties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The optimality, efficiency, and other attributes of CAT-ORA have been confirmed through theoretical validation, statistical evaluation, and a real-world demonstration of a formation flight in a small-scale visual entertainment performance involving up to 19 UAVs (see Fig. 1). The results demonstrate the capability of CAT-ORA to solve the introduced problem in real time (within a few milliseconds for instances of up to 32 robots) while significantly decreasing the time required to perform formation reshaping tasks (up to 49% compared to Linear Sum Assignment Problem (LSAP)-based solution, ) and providing collision avoidance guarantees. This outcome holds significant value, especially for robots with limited operational time, and can be employed to enhance existing approaches or serve as a foundation for future research in formation reshaping, particularly concerning the autonomous deployment of cooperating multi-robot systems in real-world environments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- We present a lower bound on a minimum mutual distance of trajectories for the solution of the robot-to-goal assignment as LBAP along with its theoretical proof. - We introduce a deterministic, complete algorithm for solving the robot-to-goal assignment problem, minimizing the maximum length of the path among assigned robot-goal pairs while respecting constraints on mutually exclusive robot-goal pairs. - We provide a closed-form solution for generating a set of trajectories connecting given start and goal positions and minimizing the makespan while preserving the guarantees of collision-free properties. - We combine the contributions mentioned above to build CAT-ORA, the first known complete approach for the solution of the formation reshaping problem minimizing the makespan while providing collision avoidance guarantees in 3D environments. We provide verification of its properties through several proofs, numerical analysis, and a real-world experiment. - We provide a quantitative and theoretical analysis of the CAT-ORA solution compared to the LSAP-based solution in terms of the makespan of a reshaping process, showing its superior performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PROBLEM DEFINITION", "weight": 1.0} -->

The Time-Optimal Formation Reshaping Problem (TOFREP), tackled in this manuscript, is defined as follows. Given the set of initial configurations of n unlabeled robots S = { s 1, s 2,..., s n } and set of n goal configurations G = { g 1, g 2,..., g n }, find a set of collision-free trajectories T that guide the robots from S to G while minimizing the makespan of the reshaping process.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PROBLEM DEFINITION", "weight": 1.0} -->

Let us define the makespan of reshaping the formation F given the assignment φ: S → G as where tf (T (a, b)) represents the time required to reach position b from position a following trajectory T (a, b). Then, the TOFREP is defined as where T (·, t) represents a point on a trajectory T (·) corresponding to time t, te = max (tf (T (s i, g j)), tf (T (s k, g l))) is a maximum duration of examined trajectories, ∆ stands for the minimum acceptable mutual distance of robots, Φ is the set of all possible assignments from S to G, and T is a class of arbitrary trajectory generation functions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM DEFINITION", "weight": 1.0} -->

- (A1) Both the robots and the goals are unlabeled (any robot can be assigned to an arbitrary goal location). - (A2) The robots are stationary in the initial and goal configurations. - (A3) The motion of the robots between the initial and goal configuration is limited to straight paths with mutually equivalent time parametrization. - (A4) The robots are considered to be spheres with radius R for the collision avoidance resolution.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM DEFINITION", "weight": 1.0} -->

- (A5) The minimum distance between the pairs of initial configurations and the pairs of goal configurations δ = min (i, j) ∈{ 1,..., n } 2, i = j min (|| s i -s j ||, || g i -g j ||) fulfills the condition δ ≥ η ∆ with η ≥ √ 2 being a constant parameter.

<!-- chunk {"id": "body-0018", "role": "body", "section": "(A6) The convex hull of S ∪ G is free of obstacles apart from the robots themselves", "weight": 1.0} -->

The assumptions (A1) - (A6) are necessary to guarantee the optimality of the proposed algorithm to the solution of TOFREP, as defined. However, in Section X, we show that the assumption (A2) is not strict and that the algorithm can also be used for reshaping moving formations, and further that the optimal solution considering assumption (A3) stays close to the theoretical lower bound of the optimal solution not considering (A3). The assumptions (A5) and especially (A6) impose significant limitations, but both (A5) and (A6) may be easily satisfied in most of the real-world scenarios discussed in Section I, making the proposed solution practical for realworld applications.

<!-- chunk {"id": "body-0019", "role": "body", "section": "OVERVIEW OF THE MAXIMUM MATCHING IN BIPARTITE GRAPHS AND THE HUNGARIAN METHOD", "weight": 1.0} -->

In this section, we overview key terms and definitions from graph theory applied in a further description of the proposed methodology and briefly describe the Hungarian method employed in the proposed algorithm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Maximum matching in bipartite graphs", "weight": 1.0} -->

- Bipartite graph: graph G = { V, E } = { Vx, Vy, E }, where the set of vertices V can be partitioned in two disjoint subsets Vx, Vy, such that the set of edges E does not contain any edge connecting vertices from the same partition. - Matching: subset of edges EM ⊂ E, such that every vertex in V is incident to at most one edge in EM. - Cardinality of the matching: number of edges in a matching CM = | EM |. The matching containing the maximum possible number of edges is called maximum cardinality matching. If CM = | Vx | = | Vy |, the matching is called perfect. - Matched edge: edge ei j is called matched if it is a part of the matching, unmatched otherwise. - Matched vertex: vertex v is matched if it is incident to an edge in matching EM, and unmatched otherwise. - Alternating path: path in a graph that starts with an unmatched vertex and alternates between edges that do not and do belong to the matching. - Augmenting path: an alternating path that ends with an unmatched vertex.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Maximum matching in bipartite graphs", "weight": 1.0} -->

- Minimum weight bipartite matching problem: given bipartite graph G = { Vx, Vy, E } and weight function w: E → R, find a maximum cardinality matching EM, such that ∑ ei j ∈ EM w (ei j) is minimum. - Dual problem of minimum weight bipartite matching problem: given bipartite graph G = { V, E } = { Vx, Vy, E }, weight function w: E → R, and vertex labeling function l f: V → R, find a feasible labeling of a maximum cost c (l f) = ∑ vx, i ∈ Vx l f (vx, i) + ∑ vy, j ∈ Vy l f (vy, j), where feasible labeling is a choice of labels such that l f (vx, i)+ l f (vy, j) ≤ w (ei j).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hungarian algorithm", "weight": 1.0} -->

The Hungarian algorithm, is widely applied for the solution of the assignment problem (which can also be represented as a minimum weight bipartite matching problem) with proven complexity O (n 3), where n is a number of matched entities. The input of the Hungarian algorithm is a square biadjacency matrix M d representing a weighted bipartite graph G with weight function w: E → R. The algorithm exploits the properties of the dual of minimum weight bipartite matching problem by using dual variables ui = l f (vx, i), v j = l f (vy, j), i, j ∈{ 0, 1,..., N }. These variables are updated during the run of the algorithm and used to determine the admissibility of edge ei j given by condition The Hungarian algorithm starts with an empty matching φ and repeatedly searches for augmenting paths in an equality subgraph formed by edges fulfilling condition. The search for an augmenting path is realized by building so-called Hungarian trees that are rooted in unmatched nodes.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hungarian algorithm", "weight": 1.0} -->

If the Hungarian tree formed by alternating paths in a graph G contains an augmenting path, the current matching is updated by flipping the matched and unmatched edges along the found path. This process always increases the cardinality of current matching by one in a single step of the algorithm. If the augmenting path is not found in a current equality subgraph, the values of dual variables are updated such that the dual task remains feasible and new edges are introduced into the equality subgraph. Then, the search for an augmenting path continues. The incremental increase of the cardinality of the matching ensures that the algorithm reaches a perfect matching for M d ∈ R n × n in n steps of a successful search for an augmenting path. We refer to for a detailed description of the algorithm and proofs of its properties.

<!-- chunk {"id": "body-0024", "role": "body", "section": "COLLISION-AWARE TIME-OPTIMAL FORMATION RESHAPING ALGORITHM - OVERVIEW", "weight": 1.0} -->

The introduced TOFREP consists of two problems: (i) the optimal assignment of initial configurations to goal configurations and (ii) the generation of collision-free minimumtime trajectories. In further description, we assume that these two problems are completely separable, and that holds for all assignments φ a, φ b from S to G. This means that the assignment minimizing the makespan corresponds to the assignment minimizing the maximum distance dmax between the assigned initial and goal configurations Fig. 2: Block diagram of the proposed Collision-Aware Time-Optimal formation Reshaping Algorithm (CAT-ORA). The colors of the trajectories in the image on the right encode the velocity profile of particular trajectories, with red being equal to zero velocity and yellow to maximum velocity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "COLLISION-AWARE TIME-OPTIMAL FORMATION RESHAPING ALGORITHM - OVERVIEW", "weight": 1.0} -->

This allows us to design Collision-Aware Time-Optimal formation Reshaping Algorithm (CAT-ORA) such that the robotto-goal assignment and generation of collision-free minimumtime trajectories are tackled in a decoupled way (see Fig. 2 for block diagram of CAT-ORA). The proof that the proposed decoupled approach does not influence the optimal solution and that is fulfilled within the proposed approach is provided in Section IX-A.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Minimum-weight robot-to-goal assignment", "weight": 1.0} -->

The task of assigning the goal configurations to particular robots can be defined as an integer linear program where w (ei j) is the cost of assignment of the goal configuration g j to initial configuration s i, and xi j = 1 if s i is assigned to g j, xi j = 0 otherwise. The problem is often referred to as Linear Sum Assignment Problem (LSAP) which can be efficiently solved by the Hungarian algorithm,. Using the squared Euclidean distances || s i -g j || 2 as costs w (ei j), the solution of was proved to guarantee the collision-free property of constant-velocity trajectories when δ ≥ √ 2 R, where R is the safety radius of robots.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Minimum-weight robot-to-goal assignment", "weight": 1.0} -->

In compliance, problem must be reformulated to minimize the length of the longest trajectory in the assignment for solving TOFREP: known as Linear Bottleneck Assignment Problem (LBAP). The specificity of the robot-to-goal assignment problem requires augmenting by including constraints on mutually colliding paths where C is a set of constraints represented by sets of mutually colliding edges, and idx (·) represents the indices of the corresponding edge.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Minimum-weight robot-to-goal assignment", "weight": 1.0} -->

Solving augmented by using standard optimization methods would require to compute the whole set of mutual collision constraints prior to the solution of the problem, which would require to check collisions among n 2 ( n -1 ) 2 2 pairs of edges, making it computationally intractable for large n. In this work, we propose a novel algorithm that combines the Hungarian algorithm, and its dynamic variant with fast collision checking. The collision checking is built on the analysis of theoretical guarantees on a minimum mutual distance of trajectories for an assignment provided as a solution of LBAP (detailed in Section VI). A thorough description of the robot-to-goal assignment component of CAT-ORA is provided in Section VII.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Minimum makespan collision-aware trajectory planning", "weight": 1.0} -->

The generation of collision-free trajectories between pairs of matched initial and goal configurations that minimize the makespan of the formation reshaping process requires considering the generation of individual minimum-time trajectories. In compliance with assumption (A3), we consider a model with single-dimension point-mass dynamics ¨ p = a, with constraints on acceleration control inputs -amax ≤ a ≤ amax, and limits on velocity v = ˙ p, 0 ≤ v ≤ vmax. Although the individual minimum-time trajectories using this model would minimize the makespan, they do not preserve the guarantees on mutual collision avoidance. Exploiting the fact that the minimized makespan is influenced only by the length of the longest trajectory, we have proposed an approach for generating mutually collision-free minimum-time trajectories, preserving the theoretical guarantees on minimum mutual distance. The proposed approach, which is based on a closed-form solution of the minimum-time trajectory generation problem, is detailed in Section VIII, along with the proof of theoretical guarantees.

<!-- chunk {"id": "body-0030", "role": "body", "section": "THEORETICAL GUARANTEES OF LBAP SOLUTION", "weight": 1.0} -->

The solution of LSAP using squared Euclidean distances as costs has been proved to guarantee minimum distance between trajectories dmin equal to where δ = min (i, j) ∈{ 1,..., n } 2, i = j min (|| s i -s j ||, || g i -g j ||) is the minimum distance between any two initial and goal configurations. The detailed description of the proof is provided. In the following sections, similar properties are derived and proved for the application of LBAP to solve the same problem while minimizing the maximum distance between the assigned initial and goal configurations, thus minimizing the makespan.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

For the analysis of the guarantees on the minimum distance between trajectories, we consider the following scenario. Without loss of generality, we can assume fixed initial and goal positions s i, s j, g i with || s j -g i || = d, || s i -g i || = Md, M ∈ [ 0, 1 ) and an arbitrarily positioned goal position g j such that || s j -g i || ≥ || s i -g j || (see Fig. 3). For M ≥ 1, the LBAP solution coincides with the solution to LSAP, thus implicitly providing the same guarantees on minimum mutual distance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Fig. 3: An example problem consisting of two initial positions s i, s j and two goal locations g i, g j. Without loss of generality, the distance || s j -g i || is assumed to be equal to d and || s i -g i || = Md, where M ∈ [ 0, 1 ).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Considering the trajectories with constant velocity, the position of robot x i (t) at time t following the trajectory from initial position s i to goal position g i can be described as with α = t t d uniformly sampled, where td is the duration of the trajectory. Hence, the mutual distance between robots following trajectories Ti and Tj of the same duration td from s i to g i with velocity vi and s j to g j with velocity v j = vi, respectively, can be expressed as Using the notation introduced at the beginning of this section and notations the equation can be written in the following form Then, the squared distance is given by Remark: In the remainder of this manuscript, we exploit the monotonicity of the quadratic function in the positive domain to replace the search for minimum distance by search for minimum squared distance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Following the theorem, for notational convenience, we define: This enables us to simplify to From, the value of α minimizing the distance between trajectories of robots with indices i, j, can be found as By substituting the value of α ∗ i j, the minimum squared distance between trajectories Ti, Tj is given by The minimum squared distance was already proved to be greater than 1 2 δ i j for b ≥ 0, which is guaranteed for solutions provided by LSAP using quadratic costs since holds for all pairs s i, g i, and s j, g j being part of an optimal assignment. Considering following equality which holds for general vectors x, y condition can be rewritten to In contrast to the application of LSAP, the LBAP solution does not directly provide any guarantee on values a, b, c, (defined in), and thus the worst-case minimum distance between trajectories is zero. Given the guarantees || x i -x j || 2 min ≥ 1 2 δ i j for b ≥ 0, we further focus on analyzing the guarantees of specific case of the LBAP solutions with b < 0.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Without loss of generality, we assume c = ka, k ≥ 1, and || s i j || to be constant, leading to a = a 0 with some constant a 0 ∈ R +. Considering b = √ a √ c cos λ, where λ is an angle between vectors s i j and g i j, and the constraints a ≥ 0, a ≥ b, c ≥ b enforced by constraints on α ∈ and b < 0, we can rewrite the first part of to Since b < 0 = ⇒ cos λ < 0 and a is constant, the gradient of with respect to k is non-negative for all admissible values of k. Therefore, the squared distance is minimal if a = c, meaning that the distance between the two start configurations and distance between two goal configurations equal. Using the substitution, this result can be also interpreted as || s i j || = || g i j ||. For a = c, the equation is simplified to Since a is constant and a > 0, the minimum distance is achieved for minimum b, such that a = c.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Remark: The distance between two trajectories following line segments is minimal when the trajectories intersect, which means that they lie in the same plane. For each pair of line segments (q, r) in three-dimensional space, it holds that either q || r, and thus q and r lie in the same plane, or we can find a plane P such that q ∈ P and r || P. The projection r ′ of r into a parallel plane preserves the dimension of r and where p (t 0), r (t 0) and p (t f), r (t f) stand for the start and end points of the line segments, respectively, and κ is an independent variable. This allows us to solve the rest of the problem in two-dimensional space without the loss of generality.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Based on the definition, the value of b is given by where β = ∠ g i s j s i and γ = ∠ g j g i s j (see Fig. 4). Consider- Fig. 4: Illustration of the general case of an assignment problem with fixed points s i, s j, g i and variable point g j. ing and the limitations on the values of β and γ coming from M ∈ [0, 1), the distance is minimized for β + γ = ± π, resulting in the intersection of s i -g i and s j -g j, leading to a minimum mutual distance equal to zero. This implies that there are no theoretical guarantees on the limits for the minimum mutual distance of robots following trajectories T i, T j for a general case. Therefore, we further focus on analysis of the guarantees on minimum mutual distance depending on the value of M.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Given the condition we can state the following theorem: Theorem 1: If max (|| s i -g i ||, || s j -g j ||) max (|| s i -g j ||, || s j -g i ||) ≤ M, M ∈ [0, 1), then minimum mutual distance dij, min ≥ √ 1 -M 2 δ i j.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

Considering the assumption in Theorem 1 and, the mutual distance is minimized when which maximizes β + γ in range (0, π). This corresponds to a situation in which the positions s i, s j, g i, g j form vertices of an isosceles trapezoid. The detailed analysis of minimum mutual distance of robots following trajectories formed by diagonals of an isosceles trapezoid is provided in Appendix A, along with proof of Theorem 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Minimum mutual distance of two trajectories", "weight": 1.0} -->

As a consequence of Theorem 1, a pair of constant-velocity trajectories for which holds is guaranteed to be collisionfree under the condition Since we have analyzed the worst-case scenario, the resulting condition forms a lower bound on the minimum distance between a pair of trajectories that can be applied for an efficient mutual collisions check of robots following constantvelocity trajectories.

<!-- chunk {"id": "body-0041", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

As previously stated in Section V, neither the Hungarian algorithm nor its adaptations for LBAP can be used to directly solve the LBAP with constraints on mutually colliding trajectories. Using the results obtained in Section VI, we introduce an optimal algorithm for the solution of with additional constraints. The algorithm which forms the first component of the proposed CAT-ORA is outlined in Algorithm 1, illustrated in Fig. 5, and detailed in the following sections.

<!-- chunk {"id": "body-0042", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

Fig. 5: Simplified diagram illustrating succession of individual steps of the algorithm for robot-to-goal assignment considering mutual collision constraints. The green and red arrows indicate the branching based on positive and negative results, respectively. The detailed description of individual steps is provided in Section VII.

<!-- chunk {"id": "body-0043", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

Algorithm 1: Algorithm for robot-to-goal assignment considering mutual collision constraints Input: sets of initial and goal configurations S, G Output: complete, collision-free assignment φ from S to G, minimizing the length of the trajectories 1 Md, Sd, Gd: = preprocessData(S, G) 2 t lb: = getThresholdLowerBound(Md) 3 T, tc: = initializeThresholds(Md, t lb) 4 B: = initializeBoundedMatrix(Md, tc) 5 u, v: = initializeDualVariables(Md, B) 6 φ: = fi ndInitialAssignment(Md, B) 7 done:= false 8 while not done do 9 φ: = internalHungarian(φ, Md, B, u, v) 10 valid: = isComplete(φ) 11 if valid then 12 c edges: = getCollidingEdges(φ, Md, Sd, Gd, S, G) 13 if c edges = None then 14 done:= true 15 else 16 φ: = branchSolution(φ, Md, B, u, v) 17 valid: =

<!-- chunk {"id": "body-0044", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

isComplete(φ) 18 if not valid then 19 tc: = updateThreshold(T) 20 B, e u: = updateBoundedMatrix(tc) 21 u, v: = updateMatchingAndDuals(φ, Md, e u, u, v) A. Algorithm for robot-to-goal assignment considering mutual collision constraints To simplify the description of the proposed robot-to-goal assignment algorithm (Algorithm 1), we assume sets of initial and goal configurations S and G to be of the same size | S | = | G | = N, even though this is not strictly required.

<!-- chunk {"id": "body-0045", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

The algorithm begins with data preprocessing to get the weighted biadjacency matrix M d ∈ R N × N, mij = || s i -g j || 2 and the distance matrices S d ∈ R N × N, si j = || s i -s j || 2, G d ∈ R N × N, gij = || g i -g j || 2 that store the squared distances of particular start and goal locations for efficient collision checking.

<!-- chunk {"id": "body-0046", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

Further steps initialize several variables. First, the lower bound t lb for a threshold of elements in M d that determines whether edges ei j can be part of the solution is found as an element of M d Next, the list of thresholds T is formed as a sorted list of elements mij in M d which are greater than t lb. The current threshold tc = t lb is also applied in initialization of a bounding matrix B ∈ { 0, 1 } N × N, where The bounding matrix B is used and updated throughout the whole algorithm to limit the maximum cost of an admissible edge and also to exclude the restricted edges, being part of the collision, from the assignment.

<!-- chunk {"id": "body-0047", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

As the next step, the vectors of row and column dual variables u = { u 1,..., uN } and v = { v 1,..., vN } are initialized according to the following rule: This initialization ensures that at least one admissible edge is present in each row and column at the beginning of the algorithm. The final step preceding the main loop of the algorithm finds an initial assignment by a sequential search for an arbitrary admissible edge that lies in a yet unassigned row and column. This step is not necessary since the algorithm can start with a valid matching of arbitrary cardinality (including the empty matching), but it decreases the number of required steps in the initial phase of the algorithm.

<!-- chunk {"id": "body-0048", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

With the completed initialization, the main loop of the algorithm begins with the internalHungarian procedure (line 9 of Algorithm 1) detailed in Algorithm 2. This procedure starts by searching for an augmenting path through growing the Hungarian trees rooted at the unmatched nodes in a current equality subgraph. If an augmenting path P is found, the matching at step k, φ k is updated by path P as Otherwise, the dual variables are updated using the set of nodes encountered in the grown Hungarian trees according to the formula and H r, H c are sets of nodes' indices encountered within the Hungarian trees corresponding to the rows and columns of M d, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "ALGORITHM FOR SOLUTION OF LBAP WITH GUARANTEES ON MINIMUM DISTANCE AND COLLISION-FREE TRAJECTORIES", "weight": 1.0} -->

Up to this part, the internalHungarian procedure (Algorithm 2) matches the internal part of the original Hungarian algorithm with the only difference in which excludes the edges restricted by the bounding matrix B. However, this modification can result in an undefined value of θ, indicating that the assignment problem does not have a solution with the current threshold tc (line 5 in Algorithm 2). In such a case, the internalHungarian procedure is aborted while keeping the incomplete assignment φ and updating the values of dual

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

Input: matching φ, matrix of squared distances Md, bounding matrix B marking the elements exceeding current threshold tc, row and column dual variables u, v Output: updated assignment φ with non-decreased cardinality, updated row and column dual variables u, v 1 while not isComplete (φ) do 2 Th: = growHungarianTrees (φ, B, u, v) 3 P: = fi ndAugmentingPath (Th) 4 if P = None then 5 if isUpdateFeasible (Th, B) then 6 updateDualVariables (Th, u, v) 7 else 8 break 9 else 10 φ: = augmentPath variables u, v for later processing inside the main loop of Algorithm 1.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

Once the matching from the internalHungarian procedure is obtained, its completeness is verified (line 10 of Algorithm 1). If the matching is not complete, meaning that its cardinality card ( φ ) < N, the threshold tc and bounding matrix B are updated. As a result of the Hungarian algorithm on an incomplete graph, the last found matching φ has the maximum cardinality on a graph excluding edges bounded by B. Thus, the matching cannot be completed without adding at least K = N -card ( φ ) new edges. Based on this observation, the current threshold tc is updated to the lowest value in T that decreases the number of bounded elements in B by at least K.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

The change of the elements in matrix B corresponds to the modifications of values in the original cost matrix M d, which requires updating the dual variables to maintain the dual task feasible. For this purpose, we have adapted the method for updating dual variables in a dynamic (cost-changing) variant of the task assignment problem proposed. The updateMatchingAndDuals procedure applied within the proposed algorithm (line 21 of Algorithm 1) is outlined in Algorithm 3. After the adaptation of dual variables, the algorithm proceeds to the next run of the internalHungarian procedure (line 9 of Algorithm 1), starting with the matching of cardinality card ( φ k ) ≥ card ( φ k -1 ) and a decreased number of bounded elements.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

If the matching found by internalHungarian procedure is perfect, it is tested for the existence of colliding edges using a combination of the results derived in Section VI for evaluation of the majority of the potential collisions, and the precise collision checking using. The collision check is done over all pairs of edges in the perfect matching φ. The collision check of edges ei j, ekl ∈ φ starts with the evaluation of

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

- Algorithm 3: updateMatchingAndDuals(φ, Md, e u, u, v) Input: matching φ, matrix of squared distances Md, set of updated edges e u, row and column dual variables u, v Output: updated assignment φ, updated row and column dual variables u, v }} 1 for ei j ∈ e u do 2 if mij < ui + v j then 3 ui = min k ∈{ 1,..., N } mik -vk 4 if ei j / ∈ φ then 5 φ: = φ \{ eik, k ∈ { 1,..., N 6 else 7 φ: = φ \ ei j where the value of M is set based on the value of δ and the minimum allowed mutual distance ∆ using. The first part of the condition rejects the risk of potential collision by detecting the equivalence with the LSAP solution with proven guarantees on the minimum distance of trajectories while the second part eliminates the collisions using Theorem 1.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

Since the condition from Theorem 1 represents the lower bound on a minimum mutual distance, we further apply the exact computation of a minimum distance to avoid false positive detections of collisions if collide ( ei j, ekl ) = true. Thus, if the condition is not met, equation is applied for an exact computation of the minimum mutual distance of the trajectories being compared to the minimum acceptable distance ∆. In the case that there is no pair of colliding edges in a perfect matching φ, the algorithm terminates and returns φ as a complete assignment from S to G, minimizing the maximum length of the trajectory while fulfilling the condition on collision-free assignment with constant-velocity trajectories (line 14 of Algorithm 1).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

If a collision is detected, the branchSolution procedure (Algorithm 4) is started to ensure that the algorithm explores all possibly collision-free matchings for a current threshold tc before increasing its value and making new elements of M d feasible (line 16 of Algorithm 1). The proposed method is based on the depth-first search algorithm performed on a binary tree graph formed by nodes defined by matching φ, pair of colliding edges e c, and vectors of row and column dual variables u, v. Note that, the branchSolution method is used to find any collision-free solution with current threshold tc that defines the optimal value. Thus, the non-optimality of the depth-first search does not influence the optimality of the presented algorithm.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

The binary tree, rooted at a node corresponding to initial perfect matching, is iteratively built during the depth-first search by expanding the parent node according to the following expansion rule. The parent node Np = { φ p, ei j, u p, v p } with a maximum matching φ p, restricted edge ei j, and dual variables u p, v p is, in the case of detected colliding edges e c = { ekl, eop }, expanded into two child nodes derived from the task assignment problem of the parent node by adding a single bounded edge and updating dual variables correspondingly. Thus, the expansion of a node Np results in new nodes given by Note that, the matching and dual variables of particular nodes are always updated during the internalHungarian procedure before the child nodes are derived from them.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

In every iteration of the branchSolution procedure, a node n c = { φ c, ei j, u c, v c } is dequeued from the Last In First Out (LIFO) queue, the bounding matrix B is updated with the newly restricted edge ei j and the corresponding dual variables and matching are updated using updateMatchingAndDuals (Algorithm 3). After that, the internalHungarian is run to find a perfect matching for an updated assignment problem (line 8 of Algorithm 4). Since the newly restricted edge ei j is always part of an initial parent matching, the cardinality of the matching φ after an update is always card ( φ ) = N -1. As mentioned earlier, given the matching of cardinality N -1 and the corresponding dual variables, the internal Hungarian algorithm terminates after a single step with either a perfect matching (if an augmenting path exists) or an incomplete matching. This fact is important for keeping the computational complexity of the proposed algorithm low.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

If a perfect matching is not found by the internalHungarian method, the solution to an assignment problem with a set of bounded edges given by B does not exist. Consequently, it is easy to show that this situation cannot be improved by restricting additional edges. Hence, we cannot get a valid solution by expanding such a node and can proceed to the next iteration. If the computed solution is a perfect matching, it has to be examined whether it is collision-free. In case a pair of colliding edges is not found, the perfect matching is returned as a valid collision-free solution to the main loop of Algorithm 1. Otherwise, the node is expanded according to the expansion rule, inserted into the queue, and the algorithm proceeds to the next iteration (line 14 of Algorithm 4). In case all branches of the tree were explored without finding a valid, complete solution, the procedure returns to the main loop of Algorithm 1, where the value of the current threshold is updated (line 19), and the search for a solution continues. In the main loop, the algorithm repeats the above-described steps until a valid, complete solution is found. The valid solution is guaranteed to exist under the assumptions specified in Section III.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Algorithm 2: internalHungarian( φ, Md, B, u, v )", "weight": 1.0} -->

Since the introduced algorithm iteratively increases the threshold on bounded edges, the number of bounded edges decreases and the problem becomes less restricted. In a worstcase scenario, the algorithm reaches a point where none of the edges are bounded, meaning that also none of the edges from solution φ LSAP minimizing the sum of squared costs are bounded. Then, φ LSAP is an output of the internal Hungarian algorithm. Since the φ LSAP solution is guaranteed to be collisionfree with given assumptions, a valid collision-free matching is always found.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Algorithm 4: branchSolution( e c, φ, Md, B, u, v, S, G, S d, G d )", "weight": 1.0} -->

Input: colliding edges e c, matching φ, matrix of squared distances Md, bounding matrix B, row and column dual variables u, v, initial and goal configurations S, G, matrices with squared distances of initial and goal configurations S d, G d Output: complete collision-free assignment φ new if it exists, original assignment otherwise 1 O l: = Ø // Last in first out queue 2 Node root: = { φ, e c, u, v } 3 O l ← expand (root, φ, e c) 4 while O l = Ø do 5 n c: = dequeue (O l) 6 updateRestrictedNodes (Md, B, n c) 7 updateMatchingAndDuals (n c. φ, Md, n c. ei j, u, v) 8 φ new: = internalHungarian (n c.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Algorithm 4: branchSolution( e c, φ, Md, B, u, v, S, G, S d, G d )", "weight": 1.0} -->

φ, Md, B, u, v) 9 if isComplete (φ new) then 10 e c: = getCollidingEdges (φ new, Md, Sd, Gd, S, G) 11 if e c = None then 12 return φ new // solution found 13 else 14 O l ← expand (n c, φ new, e c) 15 return φ // solution not found

<!-- chunk {"id": "body-0063", "role": "body", "section": "MINIMUM-MAKESPAN TRAJECTORY GENERATION", "weight": 1.0} -->

The algorithm designed for the solution of the LBAP introduced in Section VII-A guarantees to solve part of TOFREP by finding an assignment minimizing the length of the longest path with additional guarantees on the collision-free property of the constant-velocity trajectories. In this section, we describe a second component of CAT-ORA that allows us to generate a set of trajectories connecting the pairs of assigned positions, while minimizing the makespan of the reshaping process and preserving the conditions on the collision-free property derived in Section VI.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Minimum-time trajectory generation", "weight": 1.0} -->

The time-optimal control of a model with single-dimension point-mass dynamics and constraints on maximum velocity results in a control policy of form where t 3 = t ∗ is the overall minimized time of trajectory following. The control policy leads to trajectories that are described by equations with velocities vi and positions pi, i ∈ { 0, 1, 2, 3 }. With the known initial and final conditions of p 0, v 0, p 3, v 3, the maximum acceleration amax, and the assumption on reachability of the maximum velocity v 1 = vmax, the number of equations matches the number of unknown variables (t 1, t 2, t 3, p 1, p 2, v 2), and has a closed-form solution. By the addition of an assumption that v 0 = v 3 = 0 and its consequence t 1 = t 3 -t 2, can be modified to With an additional seventh equation, the modified set of equations allows for relaxing the condition v 1 = vmax to v 1 ≤ vmax, thus providing a single closed-form solution valid even when maximum velocity cannot be reached, and the optimal control policy reduces to bang-bang control.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

By applying time optimal control policy, the time necessary for following the trajectory is directly proportional to the length of the trajectory. Thus, the makespan of the formation reshaping process is equal to the time tm of following the trajectory Tm corresponding to the longest path Pm obtained in the assignment φ From the solution of for the longest path Pm, we obtain the duration t m 1, t m 2 and t m 3 of acceleration, constant speed, and deceleration segments, respectively. Considering the duration of particular segments t 1, t 2, t 3 to be constant and equal to t m 1, t m 2, t m 3 for all trajectories, can be applied for the generation of the rest of trajectories with defined t 1, t 2, t 3, but varying | ai | ≤ amax and v 1 ≤ vmax. Such an approach results in trajectories defined by parametrization: where Vm and Am stand for maximum applied velocity and maximum applied acceleration of Tm, respectively, and s = t t m with t being time elapsed from start of the trajectory. Trajectories generated according to parametrization are illustrated in Fig. 6.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

Fig. 6: Acceleration and velocity profiles and position progress along the path for trajectory Tj with length Dj = Dm generated using time-optimal control policy (red), and for trajectory Ti with length Di ≤ Dm generated according to parametrization (blue). The background color distinguishes the acceleration (green), constant speed (white), and deceleration (red) segments of the trajectories.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

Let us define the progress ratio at time t > 0 for a pair of trajectories Ti, Tj of lengths Di > 0, Dj > 0, as where pi (t), pj (t) are the distances traveled along the trajectories Ti, Tj till time t.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

Theorem 2: If the progress ratios PRa = PR (Ti, a, Tj, a) and PRb = PR (Ti, b, Tj, b) of two parametrizations a and b of a single pair of paths are constant for all t and PRa = PRb, the following relation holds: Proof. The assumption PRa = PRb = const. in Theorem 2 can be reformulated to equation where ta and tb are the duration of trajectories Ti, a, Tj, a and Ti, b, Tj, b, respectively, and sa, sb are independent variables. Equation can be simplified to From, it follows that for an arbitrary pi, a (sa) with associated point pj, a (sa), it holds that Thus, the set of corresponding points on particular trajectories is equal for both pairs of trajectories, and their minimum distances are equal.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

By applying Theorem 2, it can be shown that the progress ratio of trajectories with a constant velocity and minimum-time trajectories defined by are equal and constant for all parts of parametrization. It follows that the minimum-time trajectories defined by have the same properties that were derived for trajectories with constant velocity. Thus, the pair of minimum-time trajectories are guaranteed to be collision-free if δ ≥ √ 1 -M 2 1 -M 2 ∆ and the CAT-ORA consisting of application of Algorithm 1 together with the trajectory generation approach provides a set of minimumtime collision-free trajectories as a solution to TOFREP.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Trajectories for minimum-time formation reshaping", "weight": 1.0} -->

Remark: The presented methodology and Theorem 2 are not limited to time-optimal control of a simplified single-dimension point-mass dynamics as presented in this section. The set of trajectories with constant progress ratios (thus collision-free for assignment based on Algorithm 1) can be generated for an arbitrary single trajectory generation approach with arbitrary complex motion model, including, e.g., focus on minimumenergy trajectory generation.

<!-- chunk {"id": "body-0071", "role": "body", "section": "THEORETICAL AND STATISTICAL ANALYSIS", "weight": 1.0} -->

In this section, we provide proof of the optimality of the proposed algorithm and state and prove several theorems that highlight the significant benefits of the proposed approach, and support the adequacy of the stated assumptions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "THEORETICAL AND STATISTICAL ANALYSIS", "weight": 1.0} -->

A. The independence of robot-to-goal assignment on trajectory generation approach The proposed decoupled solution to TOFREP is optimal under an assumption that the robot-to-goal assignment problem and minimum-time trajectory generation are separable. If holds for all assignments and trajectories generated as described in Section VIII, then the duration of trajectories can be replaced by Euclidean distances in the computation of robot-to-goal assignment without compromising the optimality of the solution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "THEORETICAL AND STATISTICAL ANALYSIS", "weight": 1.0} -->

The proof of follows directly, and properties of applied control policy. Based on the duration of all trajectories for a single assignment depends only on the length of the longest path in the assignment. Given the assumptions on stationary initial and goal configurations (A2), the generated trajectories have identical initial and final velocities. In such a case, the duration of trajectories generated using time-optimal control policy is a monotonic, increasing function of path length, ensuring the validity of assumption.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

- (B1) The Hungarian algorithm, and thus also the internalHungarian procedure, is optimal (proved in). - (B2) The dynamic variant of the Hungarian algorithm is optimal (proved in). - (B3) The bounding of elements mij > tc of a cost matrix M d by bounding matrix B is equivalent to substituting constant Q = ∑ mij ∈ M d [mij ≤ tc] mij for all elements mij > tc. - (B4) If an element mij used in updating dual variables is bounded, all unbounded elements of Md are already admissible, and the cardinality of the current matching cannot be increased without using bounded elements (comes from the properties of the Hungarian algorithm). - (B5) By the addition of k edges, the cardinality of the maximum matching φ can be increased by at most k. Thus, the matching φ cannot be completed without the addition of at least k = N -card (φ) new edges (comes from the properties of the Hungarian algorithm).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

- (B6) The robot-to-goal assignment algorithm checks all complete solutions for collisions using a combination of an efficient analytical method and an exact analytical method (both derived in Section VI). This approach ensures that any complete solution provided by the algorithm is collision-free with no false positives.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

The proof of completeness follows directly from (B1) and (B2). By omitting procedures that do not change any variables in the main loop of Algorithm 1, the algorithm reduces to a dynamic variant of the Hungarian algorithm, solving the assignment problem with iterative change of costs caused by updates of threshold tc. Based on (B3), bounded elements only influence the update of duals once they are smaller than tc. The threshold is updated until a valid collision-free solution is found, eventually ending with bij = 0 ∀ ( i, j ) ∈ { 1,..., N } 2. If no elements of Md are bounded, the solution exists according to assumption (A5). Then, in compliance with (B2), the solution is found, proving the algorithm's completeness.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

The proof of optimality is built using the fact that bounded values cannot be part of the solution, and thus the optimal value of the solution is bounded by tc. Therefore, given guarantees of exact collision checking (B6), it is sufficient to show that the threshold tc is increased only if no valid solution exists with the current threshold. In Algorithm 1, the initial threshold is set to the maximum of the minimum elements across particular rows and columns. Since the perfect matching must include at least one element from each row and column, the initial lower bound does not exceed the optimal value. Further, we branch the proof into two cases: (i) Algorithm 1 never detects a colliding edge or (ii) Algorithm 1 detects a colliding edge.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

In case (i), the algorithm alternates between applying the internalHungarian procedure and updating the threshold tc. Based on (B1) and (B4), the internalHungarian procedure always finds a maximum matching with respect to the current bounded matrix. If a perfect matching is found with the current threshold, then the optimal solution has been achieved; otherwise, tc is updated. According to (B5), increasing tc to the lowest value that decreases the number of bounded elements in B by k = N -card ( φ ), cannot increase the threshold above the value of the optimal solution. Then, for case (i), the procedure mirrors the dynamic Hungarian algorithm with the costs changed by updates of tc. Therefore, the optimality guarantees for case (i) follow from (B2) and the validity of threshold updates given by (B5).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

In case (ii), we have to prove that the branchSolution procedure is complete. The constraint on mutually colliding edges restricts edges er, es so that only one can be included in the solution. The branchSolution procedure exploits this constraint by creating a binary search tree where each branch is derived from a parent node by restricting exactly one edge from the colliding pair. This effectively splits the original problem into two instances: one where solutions exclude er, and the second where solutions exclude es, ensuring no valid solution is missed. During the search for the solution, each node represented by the instance of an assignment problem is evaluated using the internalHungarian and potentially getCollidingEdges procedure. For each node, the evaluation can yield three outcomes depending on corresponding set of restricted edges: (i) the found matching is not perfect; (ii) the found matching is perfect, but contains colliding edges; or (iii) the found matching is perfect and collision-free.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

If a perfect matching is not found, it is guaranteed not to exist ((B1), (B2)), and thus this branch of the solution does not have to be explored further since the restriction of an additional edge cannot lead to an increase in maximum cardinality. If a perfect matching is found and it contains a pair of colliding edges, the node is split into two and further explored. If the found matching is perfect and does not contain any colliding edge, it is bounded by tc, and is thus optimal with respect to,.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Optimality of the robot-to-goal assignment of CAT-ORA", "weight": 1.0} -->

Since we have proven the optimality of the algorithm for the solution of LBAP with mutual collision constraints, along with the independence of robot-to-goal assignment on minimumtime trajectory generation approach, it can be concluded that the CAT-ORA is an optimal algorithm for the solution of TOFREP.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

The superior performance of the LBAP-based approach to robot-to-goal assignment in terms of the length of the longest path is evident from the LSAP and LBAP problem formulation. With Theorem 3 introduced and proven in this section, we provide an insight into the significance of this phenomenon, and thus also the benefit of solving robot-to-goal assignment as LBAP instead of LSAP. The theorem shows that the LSAP solution can produce an up to 1. 7-times longer longest path compared to the LBAP solution already for small instances of 3 robots. This ratio further grows with the squared root of a number of robots, reaching a ratio of 10 for instances with 100 robots.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

Theorem 3: The upper bound on the ratio between the maximum length of the path in LSAP assignment φ s and LBAP assignment φ b is √ N, where N is the number of goals. The lower bound on this ratio equals 1. Thus, the following equation holds Proof. The proof of the first inequality directly follows from the optimization criterion and properties of LBAP. The LBAP solution directly minimizes the maximum length of the path in the assignment, hence max (i, j) ∈ φ b || s i -g j || ≤ max (i, j) ∈ φ a || s i -g j || holds for optimal solution to LBAP represented by assignment φ b and any valid solution optimizing arbitrary criteria (including LSAP) represented by assignment φ a, thus, 1 ≤ max (i, j) ∈ φ s || s i -g j || max (i, j) ∈ φ b || s i -g j ||.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

The lower bound is achievable since if no edge can be removed from the LSAP solution without rendering the problem unfeasible, the solutions of LSAP and LBAP coincide and thus max (i, j) ∈ φ b || s i -g j || = max (i, j) ∈ φ s || s i -g j ||.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

The second inequality can be proved by finding a solution to the optimization problem where is a necessary condition for a validity of LSAP solution coming from its formulation. Given the independence of the expressions in the numerator and denominator, the maximum of can be found by independent maximization of numerator and minimization of denominator while considering constraint.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

- i. The paths shorter than max (i, j) ∈ φ s || s i -g j || do not influence the value of numerator, but increase the value of the left side of. In the extreme case, this leads to a set of paths with zero length except for a single path in the set. - ii. The paths shorter than max (i, j) ∈ φ b || s i -g j || do not influence the value of the denominator, but increase the value of the right side of. In the extreme case, this leads to a set of paths with equal lengths.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Comparison of LBAP and LSAP in terms of maximum path length", "weight": 1.0} -->

The least constrained form can be further reformulated to which directly forms the upper bound on the examined quantity. The achievability of the upper bound can be proved by construction. The representative example for which the equality in for arbitrary N holds is formed by a scenario where S = { v 0,..., v N } ⊂ V, G = { v 1,..., v N + 1 } ⊂ V with V = { v 0,..., v N + 1 } being set of vertices of a closed polygonal chain for which holds: Given an environment with unconstrained dimensions, the introduced scenario can be constructed for arbitrary N.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Study on suboptimality of the solution to TOFREP neglecting assumption on straight paths", "weight": 1.0} -->

The optimality of the CAT-ORA for the solution of TOFREP is proved in Section IX-B. However, the assumption (A3) discriminates the use of collision resolution techniques, such as time delays and geometric modifications of paths,. Although the use of such techniques mostly leads to a significant increase in the computational complexity of the algorithm, they can resolve some collisions that are unsolvable by the proposed algorithm without increasing the threshold tc. Thus, neglecting the assumption (A3) can change the optimum value of TOFREP.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Study on suboptimality of the solution to TOFREP neglecting assumption on straight paths", "weight": 1.0} -->

We compare the achieved optimum value of the proposed algorithm with a theoretical lower bound of TOFREP (see Theorem 4) to analyze the gap between the optimum value of the solution while both considering and not considering assumption (A3). The results presented in Fig. 7 show that the CAT-ORA yields an optimal solution equal to the theoretical lower bound (neglecting assumption (A3)) in over 95% of instances in dense environments with an average suboptimality savg = 1. 0008 and maximum suboptimality smax = 1. 16.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Study on suboptimality of the solution to TOFREP neglecting assumption on straight paths", "weight": 1.0} -->

Theorem 4: The lower bound on the solution of TOFREP without limitations imposed by assumption (A3) is given by the duration of the minimum-time trajectory that corresponds to the longest path in the robot-to-goal assignment, as obtained by the solution of LBAP without considering mutual collisions.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Study on suboptimality of the solution to TOFREP neglecting assumption on straight paths", "weight": 1.0} -->

Proof. Considering an assumption on static initial and goal configuration, the optimum value of TOFREP equals the duration of minimum-time trajectory along the longest path among all reshaping paths. Thus, minimizing the length of the longest path among all reshaping paths optimizes the original problem. By applying any technique to resolve the collisions among trajectories, the optimum value remains the same or increases. Thus, the solution of LBAP together with the minimum-time trajectory generation forms a lower bound to TOFREP.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Study on suboptimality of the solution to TOFREP neglecting assumption on straight paths", "weight": 1.0} -->

Fig. 7: Quantitative analysis of the suboptimality of the CAT-ORA to TOFREP omitting assumption (A3). The presented results are generated using 10 5 instances with a density of the environment dr = 0. 1 for every number of robots. Qx stands for corresponding quantiles and µ stands for the mean value. The curve of Q 1. 0 is associated with the values on the right axis.

<!-- chunk {"id": "body-0093", "role": "body", "section": "NUMERICAL AND EXPERIMENTAL RESULTS", "weight": 1.0} -->

In this section, numerical and experimental results are presented to demonstrate the performance indicators of the proposed approach. All results were evaluated in scenarios with varying numbers and densities of the robots randomly generated in a 3D environment. The density of robots in the environment of volume Ve is defined as where Vr stands for the volume occupied by particular robots. All evaluations were performed on a computer with a 4core Intel (R) Core(TM) i7-10510U CPU with base frequency 1.80 GHz.

<!-- chunk {"id": "body-0094", "role": "body", "section": "The effect on length of the path", "weight": 1.0} -->

Although the presented approach is focused on minimizing the makespan of the formation reshaping process, the comparison based on the duration of the trajectories would depend on the choice of kinematic constraints. Thus, it would not yield fair results. Therefore, we compare the solutions provided by our algorithm for robot-to-goal assignment in terms of maximum length of the path with the solutions of LSAP used by several state-of-the-art works, -. The results show that, on average, the CAT-ORA produces a set of paths with a maximum length 11% shorter than the LSAP approach. This highlights the significant benefit of using CAT-ORA instead of LSAP-based approaches, especially for battery-constrained robots or time-constrained applications. The detailed results for various numbers of robots and densities of the environment are presented in Fig. 8. In compliance with Theorem 3, a more significant effect is observed for instances with more robots.

<!-- chunk {"id": "body-0095", "role": "body", "section": "The effect on length of the path", "weight": 1.0} -->

Fig. 8: The ratio between the maximum length of the set of paths produced by CAT-ORA Dm, CAT -ORA and by the LSAP approach Dm, LSAP for a varying number of robots and density of robots in the environment dr. The results are generated using 10 5 instances for each presented number of robots.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computational time", "weight": 1.0} -->

The introduced procedures and checks guaranteeing the optimality of the CAT-ORA come at the cost of higher computational times in comparison to the original Hungarian algorithm. A major increase in the computational burden may potentially come from the branchSolution method. However, reaching its theoretical asymptotic complexity would mean that all LBAP solution edges mutually collide. The probability of this situation is limited by the assumption (A5) and by solving the LBAP as an LSAP with restrictions on certain edges. This brings the advantage that any pair of edges ei, j, ek, l is guaranteed to be collision-free if ei, l ≤ tc and ek, j ≤ tc. Thus, in practice, the branchSolution method is responsible for 4. 7% of the total computational time on average among 10 5 randomly generated instances with high density.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Computational time", "weight": 1.0} -->

A detailed analysis has shown that the main part of the additional time required by CAT-ORA is not consumed by the collision resolution part, but by the search for a correct threshold for the feasible solution. Since some algorithms for the solution of LBAP have lower theoretical complexity than those for the solution of LSAP, they can be used to increase the efficiency of a search for the threshold tc. However, their application in Algorithm 1 is limited by the crucial role of dual variables that would require running the algorithm from its initial phase after the threshold is found. Therefore, such an approach is efficient only for instances with a high number of robots and an inaccurate initial estimate of threshold t lb.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Computational time", "weight": 1.0} -->

The detailed comparison of computational times of the algorithm is shown in Fig. 9. Although the ratio between the maximum computational times of the Hungarian algorithm, applied for the solution of LSAP and CAT-ORA is significant, the absolute maximum difference in times does not exceed a few milliseconds for the instances with up to 32 robots. This keeps the computational demands sufficiently low for using CAT-ORA in applications that require real-time computations. The ratio between computational times decreases with an increasing number of robots since it mitigates the effect of the more demanding initialization phase.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Computational time", "weight": 1.0} -->

Fig. 9: Comparison of computational demands of the LSAP approach and CAT-ORA approach for varying numbers of robots in an environment. The presented results are generated using 10 5 instances with varying densities of the environment.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Formation reshaping", "weight": 1.0} -->

We benchmark the CAT-ORA by comparing the achieved results with the LSAP and LBAP algorithms coupled with minimum-time trajectories. Similarly to the detailed results in the previous section, the algorithms were evaluated on a set of 10 5 instances representing formation reshaping tasks with various numbers and densities of robots in an environment. While the comparison results can be easily inferred from the characteristics of the individual algorithms, the presented results, as detailed in Table I, quantitatively demonstrate the expected outcomes. The LBAP-based consistently yields solutions with shorter maximum path lengths compared to other methods, resulting in a reduced makespan. However, the generated trajectories lead to collisions in more than 6% of instances. The CAT-ORA and LSAP-based approach provide collisionfree trajectories for all instances. Yet, while the LSAP-based solution leads to an average increase of 12% in makespan and 15% in maximum path length compared to LBAP-based approach, the CAT-ORA only marginally extends the duration of reshaping process by an average of 0. 06% compared to LBAP-based approach.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Formation reshaping", "weight": 1.0} -->

The advantage of the CAT-ORA over the LSAP-based algorithm is showcased in a scenario requiring 200 robots initially arranged in a rectangular formation to sequentially adapt the formation shape to represent the letters C, T, and U. Guided by the CAT-ORA, the entire formation reshaping task is completed in 36.6 s, which is 5.4 s faster than the solution provided by the LSAP-based approach, while the increase in computation time is 0. 9s. A detailed presentation of a specific formation reshaping instance is provided in Fig. 10.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Integration with cooperative motion planning algorithm", "weight": 1.0} -->

The applicability of the proposed algorithm in the distributed scenarios is validated by integrating the robot-to-goal assignment algorithm of CAT-ORA with a distributed cooperative motion planning algorithm MADER. The results, presented in Table II, show that complete CAT-ORA reduces the makespan by 45% on average when compared to MADER combined with the robot-to-goal assignment part of CAT-ORA only. This is caused mainly by the MADER's approach to collision resolution, which reacts to the identified risk of collision in advance, including situations where the collision would not happen. Thus, hindering full exploitation of kinematic constraints to minimize the makespan. Such an approach is very reasonable and practical in many scenarios, but at the same time, it leads to unnecessary extension of the reshaping process, which underlines the advantage of centralized algorithms in scenarios focused on minimizing the makespan.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Integration with cooperative motion planning algorithm", "weight": 1.0} -->

Further, we evaluate the performance of the MADER in combination with three different robot-to-goal assignment methods - LSAP-based, LBAP-based and CAT-ORA-based. The MADER algorithm provides collision-free solutions in combination with all examined assignments. However, although the LBAP-based solution provides the shortest paths among all assignments, the results show that the needed collision avoidance maneuvers prolong the makespan of the formation reshaping, and on average LBAP-based solution provides worse performance than both collision-free assignments. The best average performance over all instances was achieved with the assignment provided by CAT-ORA, which reduces the number of avoidance maneuvers by considering the collisions during the robot-to-goal assignment phase while minimizing the length of the longest path. The results highlight the importance of the robot-to-goal assignment for efficient formation reshaping and consideration of the collisions during the robotto-goal assignment, even in the case of the application of advanced collision-resolution techniques and algorithms. The detailed results are provided in Table II.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Integration with cooperative motion planning algorithm", "weight": 1.0} -->

| Approach | Success rate | Makespan PDB [%] | Makespan PDB [%] | Max. length PDB [%] | Max. length PDB [%] | Total length PDB [%] | Total length PDB [%] | Comp. time PDB [%] | Comp. time PDB [%] | Fig. 10: A qualitative comparison of the formation reshaping process applying CAT-ORA and approach applying LSAP solution coupled with minimum-time trajectory generation. The formation consists of 200 robots that are initially organized in a rectangular formation and are consequently required to adapt the shape of the formation to represent letters C, T, and U. The applied kinematic constraints are vmax = 4ms -1, and amax = 2ms -2. The height of each letter is 100 m and the scale of the axes is equivalent. The gray lines represent the reshaping paths, and the colored points represent positions of robots at corresponding times. The color encodes the velocity of particular robots, with red being equal to zero velocity and yellow to vmax.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Integration with cooperative motion planning algorithm", "weight": 1.0} -->

| Approach | Success rate [%] | Makespan mean [s] | Makespan PDB [%] | Makespan PDB [%] | Remark: For the methods applying MADER, the individual instances were rotated according to the result of the assignment such that the longest assigned path points in the diagonal direction of xy coordinate frame and thus the speed in this direction is not limited by the per-axis velocity and acceleration constraints applied by MADER.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Real-world experiment", "weight": 1.0} -->

In the real-world experiment, the CAT-ORA was applied in a scenario simulating a small-scale drone performance. The scenario requires a set of robots to perform 19 transitions between formations of diverse shapes (both 2D and 3D) and sizes, while the center of the formation continuously moves through the environment. Each formation F i = { r 1,..., r N } is defined by a set of desired relative positions to the center of the formation r j ∈ R 3 defined in the orthogonal coordinate system H that coincides with the position and orientation of the center of the formation. Since the requirement on continuous movement contradicts the assumption (A2) on robots being stationary in the initial and goal configurations, CAT-ORA cannot be directly applied to compute trajectories between the robots' configurations defined in the world coordinate frame W.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Real-world experiment", "weight": 1.0} -->

However, the definition of relative positions in an orthogonal coordinate system ensures independence of mutual distances between desired relative positions on the motion of the formation. Therefore, we apply CAT-ORA to compute the trajectories in the space of relative positions considering consecutive formations F i, F i + 1 as initial and goal configurations, respectively. The generated trajectories then define the time evolution of r j, leading to continuous adaptation of the formation shape. The trajectories in the world coordinate frame are then defined by p j ( t ) = T H, W r j ( t ), t ∈ ( t 0, t f ), where T H, W is a transformation matrix from formation frame H to world coordinate frame W. This approach shows that the assumption (A2) is not a strict requirement for the applicability of CAT-ORA to solve TOFREP.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Real-world experiment", "weight": 1.0} -->

However, the superposition of the generated trajectories to the trajectory of the center of the formation requires adapting the kinematic constraints for the generation of formation reshaping trajectories, such that the resulting trajectories p j ( t ), j ∈ { 1, 2,..., N }, t ∈ ( t 0, t f ) do not violate the kinematic constraints. Thus, (A3) is a necessary assumption for guaranteeing the optimality of the solution.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Real-world experiment", "weight": 1.0} -->

Fig. 11: Snapshots from a real-world experiment showing the transition between a 3D spiral and a pyramid shape. The transition was completed within 10 seconds during continual rotation of the formation. The red point represents a missing UA V that failed to start due to a HW failure. Blue lines highlight the shape of the formation. Since the images show a 3D formation, the measuring scale is approximate.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Real-world experiment", "weight": 1.0} -->

The real-world experiment was performed with 19 multirotor helicopters, using the MRS UAV system for low-level control and trajectory tracking. The time required for the whole performance was 294.80 s with the total time of reshaping 214.8 s and an overall computational time of 60 ms. Snapshots from the experiment are shown in Fig. 11 and Fig. 1.

<!-- chunk {"id": "body-0111", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The proposed CAT-ORA provides a significant reduction (up to 49%) of the reshaping time at the cost of an increase in computational time. Even though the computational time is, on average, approximately 3 times longer than for LSAP-based solutions, the low absolute computation times maintain the practicality of the proposed approach for real-time applications involving formations of tens of robots.

<!-- chunk {"id": "body-0112", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The primary drawback of the proposed method is its high theoretical asymptotic complexity which lies especially in the search for all potentially valid solutions during solution branching. However, while this complexity does not allow us to provide guaranteed bounds on computation time, it rarely causes problems in practical use (as supported by data presented in Fig. 9). The only notable deviations in computation time outside the distribution presented in Fig. 9 were observed for a few instances with more than 200 equally spaced robots, resulting in a large number of equivalent values in a distance matrix representing distances between individual start and goal configurations.

<!-- chunk {"id": "body-0113", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

Although the algorithm is centralized, its expected applications are not limited to scenarios requiring offline computation of trajectories for a large number of robots or other elements (e.g., droplets on lab-on-chip devices), where the minimization of the makespan of the reshaping process is of interest. Thanks to low computational demands, the algorithm can be used also as a part of distributed systems where it can provide efficient initial robot-to-goal assignment (similarly as LSAP-based solution is used ) for on-demand or emergent formation reshaping tasks. These scenarios assume a relatively low number of robots (usually less than one hundred) and often show high interest in minimizing the makespan. This combination of requirements makes the proposed algorithm well-suited for these real-time scenarios.

<!-- chunk {"id": "body-0114", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

This paper introduces an algorithm named CAT-ORA (Collision-Aware Time-Optimal formation Reshaping Algorithm) to address the time-optimal formation reshaping problem while considering mutual collision avoidance among robots. It showcases superior performance in terms of the makespan of the formation reshaping process, while maintaining computational demands at a level suitable for realtime deployment, even in formations comprising up to one hundred robots. The properties of the proposed algorithm have been evaluated by thorough numerical and theoretical analysis, including the proof of optimality, and the applicability of the algorithm in practical scenarios was demonstrated through simulations and real-world experiments.

<!-- chunk {"id": "body-0115", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Notably, the results highlight a significant advantage of the robot-to-goal assignment aspect within CAT-ORA. It reduces the maximum length of the assigned path by up to 49% compared to the LSAP-based methods utilized by state-of-theart approaches in cooperative motion planning and formation control. This finding holds particular significance for aerial vehicles with constrained operational time, as it enhances their performance during a real-world deployment. Moreover, this outcome has potential implications for future research on formation reshaping focused on deploying autonomous robots in general environments as it forms the lower bound on the optimal solution of the introduced problem in environments with obstacles.
