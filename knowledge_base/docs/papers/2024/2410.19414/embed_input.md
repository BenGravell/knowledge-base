<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning for Robotics: A Review for Sampling-based Planners

Topics include Survey, Motion planning, Robot motion planning, Sampling-based planning, Robotics, Benchmarking.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Reviews ten popular sampling-based motion planners for robotic applications, analyzing their theoretical properties and empirical performance across diverse planning scenarios to highlight ongoing research challenges in the field.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent advancements in robotics have transformed industries such as manufacturing, logistics, surgery, and planetary exploration. A key challenge is developing efficient motion planning algorithms that allow robots to navigate complex environments while avoiding collisions and optimizing metrics like path length, sweep area, execution time, and energy consumption. Among the available algorithms, sampling-based methods have gained the most traction in both research and industry due to their ability to handle complex environments, explore free space, and offer probabilistic completeness along with other formal guarantees. Despite their widespread application, significant challenges still remain. To advance future planning algorithms, it is essential to review the current state-of-the-art solutions and their limitations. In this context, this work aims to shed light on these challenges and assess the development and applicability of sampling-based methods. Furthermore, we aim to provide an in-depth analysis of the design and evaluation of ten of the most popular planners across various scenarios. Our findings highlight the strides made in sampling-based methods while underscoring persistent challenges. This work offers an overview of the important ongoing research in robotic motion planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, robotics technology has rapidly advanced across various industries, including manufacturing, logistics, robotic surgery, and planetary exploration, bringing profound changes. Among the challenges in robotics, developing efficient and effective motion planning algorithms that help robots navigate complex environments, avoid obstacles, and complete tasks with minimal energy consumption and time is a critical task. The core objective of motion planning is to find the optimal path from the starting point to the target location while considering various constraints, such as dynamic environments and non-holonomic motion restrictions. This issue has become a central research topic in the field of robotics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The state-of-the-art and most common algorithms related to solving the motion planning problem are shown in Fig.. Motion planning can be divided into global motion planning and local motion planning. Spatial partitioning approach within configuration space, graph-based search algorithms, sampling-based methods, Bio-inspired and meta-heuristic optimization methods belong to global motion planning. Methods like Artificial Potential Field (APF) and Dynamic Window Approach (DWA) belong to local motion planning for real-time and dynamic obstacle avoidance. Graph-based algorithms like Dijkstra, wavefront, A\* and D\* are resolution-complete but are computationally expensive for high dimensional complex problems. Bio-inspired and meta-heuristic optimization methods, such as Genetic Algorithm, Particle Swarm Optimization, and Ant Colony Optimization, are well-suited for solving multi-objective optimization problems. However, Like many other evolutionary methods, such as Simulated Annealing, Artificial Neural Networks, often face issues like getting stuck in local optima and having high computational costs. Additionally, they are highly sensitive to the size of the search space and the problem's data representation scheme.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The APF method's advantage is its real-time adaptability for obstacle avoidance, while its drawbacks include susceptibility to local minima and difficulty in navigating between closely spaced obstacles. Among the various methods developed to address this challenge, sampling-based algorithms have emerged as a powerful and versatile approach, particularly suitable for high-dimensional and complex environments, as illustrated in Fig..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based algorithms, such as the Probabilistic Roadmap, Expansive Space Trees (EST), and Rapidly-exploring Random Trees, have gained main attention due to their ability to efficiently handle the computational complexity associated with planning in high-dimensional spaces. These algorithms work by randomly sampling the configuration space of the robot and incrementally building a graph or tree that represents feasible paths. This approach contrasts with traditional deterministic methods, which often struggle with the curse of dimensionality and require comprehensive environment modeling. Additionally, these methods are highly adaptable and can be easily extended to accommodate various constraints and optimization criteria, making them suitable for a broad spectrum of robotic applications. The flexibility and efficiency of sampling-based approaches have led to extensive research and numerous enhancements, resulting in a rich body of literature that continues to evolve.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent decades, researchers in sampling-based motion planning have published numerous comprehensive review papers. An early exploration of the field's history, documented in the review by Latombe, discusses the advancements in motion planning, from the initial stages of basic collision detection to the current ability to handle multi-degree-of-freedom robots in complex environments, with non-robotic applications emerging as a key driver for future research. Lindemann and LaValle review the development of sampling-based motion planning during the early 2000's. The survey by Tsianos et al. focus on the application of sampling-based motion planning in realistic settings. Elbanhawi and Simic provide a comprehensive overview of various planners, along with a collection of common primitives applicable to a wide range of algorithms. Furthermore, Noreen et al. offer a detailed review of RRT\* based path planning approaches, Kingston et al. provide an overview and discuss the problem of motion planning with constraints, while Cai et al. focus on mobile robot motion planning in dynamic environments, Sanchez et al. focus on autonomous mobile robots. Respectively, Gammell and Strub present an extensive overview of asymptotically optimal planners.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Subsequently, Orthey et al. provide an excellent review of sampling-based motion planning. Recently, the paper reviews the research on RRT-based improved algorithms from 2021 to 2023, including theoretical improvements and application implementations. With the rapid advancement of sampling-based methods, conducting a survey on the current developments in sampling-based planners is highly valuable and relevant. By systematically reviewing the existing literature and identifying key trends and developments, this survey aims to serve as a valuable resource for researchers and practitioners seeking to understand and advance the capabilities of sampling-based motion planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This survey provides a comprehensive overview of the sampling-based motion planning algorithms. Section II introduces the motion planning problem and fundamental concepts. In Section III, we delve into a detailed analysis of traditional sampling-based motion planning algorithms. Section IV explores the various applications and limitations of these algorithms. In Section V, we evaluate the performance of ten popular planners across both simulated random scenarios and manipulation tasks in different dimensions. Finally, in Section VI we make a conclusion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

Firstly, we define the path-related parameters based on the formal definition provided by Karaman and Frazzoli. Let $\mathcal{X} = {}^{d}$ represent the configuration space, where $d \in {\mathbb{N}}$ and $d \geq 2$. Define $\mathcal{X}_{\text{not}}$ as the obstacle region, such that $\mathcal{X} \smallsetminus \mathcal{X}_{\text{not}}$ is an open set. The obstacle-free space is denoted as $\mathcal{X}_{\text{free}} = {\text{cl}{({\mathcal{X} \smallsetminus \mathcal{X}_{\text{not}}})}}$, where $\text{cl}{( \cdot )}$ denotes the closure of a set.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

Consider a function $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$ that represents a path in a $d$-dimensional configuration space. A path $\sigma$ is considered valid if it is continuous and its total variation, denoted by $TV{(\sigma)}$, is bounded. The collection of all such valid paths is denoted by $\Sigma$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

The total variation for a path $\sigma$, that is, $TV{(\sigma)}$, is defined as the supremum of the sum of Euclidean distances between successive points along the path. That is,

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

When ${TV{(\sigma)}} < \infty$, it indicates that the path $\sigma$ has bounded variation, making it a valid path belonging to the set $\Sigma$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

1\) Feasible Path Planning: This type of path planning focuses on identifying a route that effectively moves from a start point to a specified goal, ensuring that the path is achievable. For instance, the path must avoid obstacles or comply with constraints in the environment. There are often multiple possible solutions to a feasible path planning problem, but the primary objective is directly to reach the goal without concern for the path's quality or efficiency.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

2\) Optimal Path Planning: This type of path planning goes beyond simply finding a valid route by focusing on identifying the most efficient path according to specific criteria. The objective might be to minimize factors such as distance traveled, time taken, energy usage, or other relevant task-specific factors. Consequently, the optimal path planning problem seeks to determine the best possible solution among all feasible options.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

Definition 2 (The Optimal Path Planning Problem): Given a path planning problem $(\mathcal{X}_{\text{free}},x_{\text{start}},\mathcal{X}_{\text{goal}})$ and a cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, the task is to find a feasible path $\sigma^{\ast}$ such that

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Definition of Planning Problem", "weight": 1.0} -->

where ${\mathbb{R}}_{\geq 0}$ represents the set of non-negative real numbers. The cost of this optimal path is denoted as $c^{\ast}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Analysis of sampling-based planning", "weight": 1.0} -->

Probabilistic Completeness is an important property for sampling-based path planning algorithms, which means that if there exists a feasible path from the starting position to the target position, the probability that the algorithm finds this path approaches 1 as the number of samples increases infinitely.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Analysis of sampling-based planning", "weight": 1.0} -->

Definition 3 (Probabilistic Completeness): An algorithm is said to be probabilistically complete if the probability of finding a feasible path, assuming one exists, converges to 1 as the number of samples $q$ goes to infinity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Analysis of sampling-based planning", "weight": 1.0} -->

where $\Sigma_{q}$ is the set of feasible paths found using $q$ samples, and $P$ denotes probability

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Analysis of sampling-based planning", "weight": 1.0} -->

where $c{(\pi_{q})}$ is the cost of the path found with $q$ samples, $c^{\ast}$ is the cost of the optimal path, and $P$ denotes probability.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

To find the optimal path in the planning task, the Rapidly-exploring Random Tree star-based planner (RRT\*) is widely used. The workflow of RRT\* is shown in Algorithm 1. First, the search tree $\mathcal{T}$ is initialized with the root node $x_{\text{start}}$. Random sample points $x_{\text{rand}}$ are generated through the Sampling($\cdot$) function within the search space. Then, the Nearest($\cdot$) function identifies the nearest node $x_{\text{near}}$ in the tree $\mathcal{T}$ to the sample point $x_{\text{rand}}$. Next, the Steer($\cdot$) function moves from $x_{\text{near}}$ towards $x_{\text{rand}}$ by a defined step size to obtain a new node $x_{\text{new}}$ and creates the edge $(x_{\text{near}},x_{\text{new}})$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

After that, the CollisionFree($\cdot$) method checks whether this edge collides with any obstacles or boundaries in the map. If no collision is detected, the tree is expanded by adding $x_{\text{new}}$ to the set of vertices and the edge $(x_{\text{near}},x_{\text{new}})$ to the set of edges. If a collision is detected, the newly generated node is discarded, and the algorithm retries the sampling process. Once $x_{\text{new}}$ is added, the algorithm performs an Extend($\cdot$) operation by searching within a defined neighborhood around $x_{\text{new}}$ to identify a parent vertex that minimizes the overall cost from the initial state. A Heuristic($\cdot$) method is employed at this stage to estimate the cost-to-go from $x_{\text{new}}$ to the goal, allowing the algorithm to prioritize more promising nodes and improve convergence towards the optimal solution.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

Subsequently, a Rewire($\cdot$) step is conducted by checking neighboring vertices to see if their connection through $x_{\text{new}}$ reduces their path cost. If so, their parent vertices are updated accordingly to reflect the more efficient path.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

As the number of iterations increases, the sampling-based algorithm progressively generates paths that approach the optimal solution. Ultimately, the algorithm outputs a path that is refined with each iteration, ensuring it is close to the shortest possible path.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

Input: Start state xstart, goal region 𝒳goal
Output: Feasible tree 𝒯
4V ← xstart, E ← ⌀, 𝒯 = (V,E) ← RRT*(xstart)
7 xnearest ← nearest(𝒯,xrand)
8 xnew ← steer(xnearest,xrand)
9 if collisionFree (xnearest, xnew) then
10 Xnear ← near(𝒯, xnew, k or r)
11 $x_{min}\leftarrow{\arg{\min\limits_{x_{near} \in X_{near}}\left( {{\text{cost}{(x_{near})}} + {\|{x_{near} - x_{new}}\|}} \right)}}$
12 ⊳ heuristic for minimal path cost, ∥ ⋅ ∥ denote as L2 norm
14 rewire(𝒯,Xnear,xmin,xnew)
Algorithm 1 Rapidly Exploring Random Tree Star (RRT*)

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Sampling-based Planner Framework", "weight": 1.0} -->

Researchers have proposed various strategies to improve different components of the sampling-based planner framework, including the $\text{Sampling}{( \cdot )}$ function, $\text{Nearest}{( \cdot )}$ function, $\text{Steer}{( \cdot )}$ function, $\text{CollisionFree}{( \cdot )}$ method, $\text{Extend}{( \cdot )}$ operation, Heuristic($\cdot$) method and $\text{Rewire}{( \cdot )}$ step. Fig. provides a general overview of these technological advancements, which will be further detailed in the following sections.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

The Sampling($\cdot$) function generates an infinite sequence of sample points within the search space. Sampling functions are classified as Informed Set, Learning-based, Adaptive Sampling, Smart Biased Sampling and Kinodynamic.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

Informed Set, such as Informed RRT\*, which restricts the node sampling range by creating a hyper-ellipsoid subset for sampling and conducts direct sampling within this subset. By constraining the algorithm's sampling region, this subset increases the probability of selecting relevant nodes, thereby boosting the algorithm's efficiency. BIT\* builds on Informed RRT\*, with batch sampling in the hyper-ellipsoid subset, this leads to a further enhancement in the algorithm's efficiency. Respectively, Ding et al. propose the expanding path RRT\* (EP-RRT\*) based on heuristic sampling in the path expansion area. Another paper proposes a cylinder-based informed rapid exploration random tree (Cyl-iRRT\*) path planning algorithm, which biases the sampling of new candidate states into an admissible cylindrical subset around the centerline from start to goal positions via rejection sampling to quickly find the homotopy optimal path in a 3-D environment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

Learning-based Sampling, such as Neural RRT\* and Neural Informed RRT\*, guides the sampling direction by training neural networks, which are particularly effective in navigating narrow passages and complex environments. Another paper uses a conditional variational auto-encoder (CVAE) to learn sampling distributions, Molina et al. propose to use convolutional neural networks (CNNs) to identify critical regions for robot planning so that the sampling process can be biased to these regions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

Adaptive Sampling, as demonstrated in methods like the Rapidly-Exploring Adaptive Sampling Tree\* (RAST\*), Gaussian Mixture Regression Rapidly exploring Random Tree\* (GMR-RRT\*) and the similar works such as, leverages an adaptive sampling approach to prioritize information-dense regions. This strategy effectively reduces localization uncertainty by concentrating on areas with higher information gain.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

Smart Biased Sampling, like RRT\*-SMART, mRRT\*-Smart and RRT\*SMART-A\* employs intelligent sampling around key nodes from an initial path, accelerating convergence.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Advanced Sampling Approaches", "weight": 1.0} -->

Kinodynamics, Boeuf et al. present an incremental state-space sampling technique to avoid generating local trajectories that violate kinodynamic constraints. Other papers prioritize generating samples that maximize clearance, meaning the distance between the robot and its surroundings. This is typically done by sampling a feasible state and taking random steps to further increase the clearance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

The Nearest($\cdot$) function refers to a key step in the sampling-based algorithms where the nearest node in the tree is found for a randomly sampled point and used as the base to expand the tree towards that point.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

Traditional nearest-neighbor searches are computationally expensive due to their linear search nature. Techniques like KD trees address these challenges by employing advanced data structures and algorithms. KD trees partition the space recursively, enabling efficient multi-dimensional searches. This method improves the search process compared to a linear search, with an average time complexity of logarithmic order, making it highly suitable for large, high-dimensional datasets.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

In contrast, the k-nearest neighbor (k-NN) strategy in sampling-based algorithms can also be implemented using formulas that adaptively determine the number of neighbors $k$ for each node based on the number of samples $q$ and the dimensionality of the space $n$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

where $\eta > 1$ is a tuning parameter. This strategy ensures that the tree expands efficiently while maintaining good coverage of the space. Pan et al. propose a novel approach for rapid probabilistic collision checking aimed at boosting the efficiency of sampling-based motion planning. In this method, the k-NN strategy is employed to identify the closest prior query sample to the new query configuration. The results demonstrate that this integrated approach enhances the RRT-based path planner by speeding up local pathfinding and optimizing the search sequence on the roadmap. These findings have been validated on both rigid and articulated robots.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

Respectively, the r-nearest neighbor (r-NN) strategy used in the r-disc (i.e.,

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

where $\lambda{( \cdot )}$ denotes the Lebesgue measure, and $B_{1,n}$ is the $n$-dimensional unit ball, $\hat{\mathcal{X}}$ is defined as the informed set, this providing a way to scale the connection radius according to the sample distribution and the space's properties.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Nearest Neighbor Methods", "weight": 1.0} -->

In addition to the aforementioned r-disc strategy, Kleinbort et al. demonstrate that the r-disc approach can achieve superior performance compared to the k-nearest variant, though the connection radius $r{(q)}$ must be calibrated according to the characteristics of the state space. Properly tuning the connection radius for specific applications can improve search efficiency. Furthermore, faster-decreasing radii are presented by Janson et al. and Tsao et al., enabling the r-disc strategy to perform even better when handling varying dimensions and sampling densities.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Tree-based Expansion Strategies", "weight": 1.0} -->

Based on the step size constraint, from the nearest node, the Steer($\cdot$) function takes a small step in the direction of the random point, generating a new node, and creates the edge. Wang et al. present variant step size RRT, which adaptively changes the step size of the tree according to the location of obstacles. Similarly, another paper changes the step size adaptively according to the density of obstacles. Subsequently, Yang et al. present a novel Variable Step Size (VSS) strategy based on RRT\*. The VSS strategy adapts the expansion step size dynamically by considering both the direction of the vertex and the target point within the random tree, with the goal of accelerating the approach toward the target point. In another paper the gradient descent method is employed to adapt the step size, causing it to gradually decrease as the goal region is approached. Additionally, Li et al. present a gravity adaptive step size strategy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Tree-based Expansion Strategies", "weight": 1.0} -->

To quickly find a feasible path, the bidirectional expansion strategy for steering was developed. Bidirectional RRT, where two trees grow simultaneously from the start and goal points, seeking to connect with each other, as illustrated in Fig..

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-D Tree-based Expansion Strategies", "weight": 1.0} -->

Initial approach, like RRT-Connect is introduced by Kuffner and LaValle, establishes the foundational method of constructing two trees from start and goal points and connecting them, thereby greatly improving search efficiency. However, RRT-connect is not asymptotically optimal like RRT\*. To solve this, Akgun et al. present Bidirectional RRT\* (B-RRT\*), incorporate an existing bi-directional approach to search which decreases the time to find an initial path. Similarly, Jorden et al. present Optimal B-RRT\*, an asymptotically optimal bidirectional method that achieves an improved convergence rate by incorporating several heuristic techniques. While Qureshi et al. introduce a new variant called Intelligent Bidirectional-RRT\* (IB-RRT\*) which is an improved variant of the optimal RRT\* and bidirectional version of RRT\* (B-RRT\*) algorithms. IB-RRT\* utilizes the bidirectional trees approach and introduces an intelligent sample insertion heuristic for fast convergence to the optimal path solution using uniform sampling heuristics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-D Tree-based Expansion Strategies", "weight": 1.0} -->

Furthermore, Tahir et al. propose the Potentially Guided Intelligent Bi-directional RRT\* (PIB-RRT\*) and Potentially Guided Bi-directional RRT\* (PB-RRT\*), which are extensions of Bi-directional RRT\* (B-RRT\*) and Intelligent Bi-directional RRT\* (IB-RRT\*). These methods greatly enhance the convergence rate and utilize memory more efficiently in cluttered environments. Additionally, the BI^2^RRT\* algorithm builds upon the Informed RRT\* by implementing a bidirectional search strategy, which helps in finding initial solutions faster and allows more time for refinement. Subsequently, Yi et al. combine homotopy topological spaces with bidirectional trees in the Homotopy-aware RRT\*, increasing the probability of finding optimal paths by exploring different topological spaces. Moreover, Lin et al. propose the Bidirectional Homotopy-Guided RRT (BH-RRT), which uses obstacle contour information to guide tree growth, improving success rates.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-D Tree-based Expansion Strategies", "weight": 1.0} -->

Wang et al. introduced the Bidirectional-Unidirectional RRT Extend Function, which switches from bidirectional to unidirectional search to overcome complex boundary problems, enhancing search efficiency. Another paper present a goal-biased bidirectional RRT with curve smoothing, connecting tree parts with Bezier curves to meet kinematic constraints, thus achieving higher success rates and shorter search times. Recently, Peng et al. develop the Improved Bidirectional RRT\*, utilizing an artificial potential field to reduce randomness and inflection points, resulting in shorter and more efficient paths.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-E Collision Check Methods", "weight": 1.0} -->

After the Steer($\cdot$) function creates the edge, the CollisionFree($\cdot$) method involves verifying whether the path between two nodes intersects with any obstacles. This basic approach, as detailed in LaValle and Kuffner's 2001 seminal paper on Rapidly-exploring Random Trees (RRT), involves checking the line segment between the current node and the new node for collisions. Over time, various methods have been developed to enhance the efficiency of collision checking.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-E Collision Check Methods", "weight": 1.0} -->

Lazy Collision Checking, such as Lazy PRM and Fuzzy PRM, both initially assume the path is collision-free and perform collision checks only when necessary. If a collision is later detected, the path is re-evaluated and corrected. However, neither Lazy PRM nor Fuzzy PRM guarantees solution quality. To solve this, Hauser et al. present two novel motion planners, Lazy-PRM\* and Lazy-RRG\*, they are almost-surely asymptotically optimal algorithms that grow a network of feasible vertices connected by edges. Edges are not immediately checked for collision, but rather are checked only when a better path to the goal is found. This strategy avoids checking the vast majority of edges that have no chance of being on an optimal path. Another paper, Adaptive Lazy Collision Checking delays collision checking in regions likely to be free of obstacles while checking early in other regions to reduce optimistic thrashing, enhancing the planner's performance in complex environments. Most recently, Neural Network Collision Checking has been introduced by Kew et al. through ClearanceNet, a neural network-based heuristic that predicts collision clearance, facilitating parallel RRT processing and significantly accelerating the collision checking process.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-F Tree Extension Techniques", "weight": 1.0} -->

After $x_{\text{new}}$ is added, the algorithm executes an Extend($\cdot$) operation to determine the parent node of $x_{\text{new}}$, the node that results in the lowest cost from the starting point to $x_{\text{new}}$ is selected as its parent node.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-F Tree Extension Techniques", "weight": 1.0} -->

LaValle and Kuffner's paper "Rapidly-exploring Random Trees: Progress and Prospects" introduce the basic principles of the standard RRT algorithm and the Extend Tree process, laying the foundation for subsequent advancements. FMT\* (Fast Marching Tree) leverages the Fast Marching Method (FMM) to enhance the efficiency of RRT in high-dimensional spaces by integrating efficient sampling and searching strategies. Specifically, the FMT\* algorithm uses FMM to quickly evaluate the quality of nodes when building the tree structure, accelerating the convergence of the path planning process. This makes FMT\* particularly effective in complex, high-dimensional path planning problems. Subsequently, Qureshi et al. introduce the P-RRT\*, which integrates Artificial Potential Fields (APF) into the RRT\* framework to provide a more directed exploration and faster convergence. Another strategy is Quick-RRT\*, which uses triangular inequality for parent node selection.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-F Tree Extension Techniques", "weight": 1.0} -->

Extending these approaches, Li et al. propose the PQ-RRT\*, which combines the strengths of P-RRT\* and Quick-RRT\*, further enhancing the convergence speed by improving both the sampling strategy and the optimization procedures used in the tree expansion process. Moreover, Liao et al. present F-RRT\*, which improves path cost by generating a parent node for the random point rather than choosing one from the existing vertices. Similarly, another paper introduces Fast-RRT\*. In order to achieve a path with a lower cost compared to the RRT\* algorithm, the ancestors of the nearest node are taken into account up to the initial state when selecting a parent for the new node. Next, Armstrong et al. introduce the Assisting Metric RRT\* (AM-RRT\*). This algorithm incorporates an assisting metric that combines Euclidean distance with a novel metric to optimize tree growth, extension, and rewiring, thereby improving coverage and path quality. This approach not only considers distance but also factors such as path smoothness or traversability, resulting in higher quality paths while maintaining efficient search performance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-F Tree Extension Techniques", "weight": 1.0} -->

Respectively, Wanga et al. present an evaluation function for growth points based on the adaptive resolution octree map, which guides the generation of RRT paths towards a more intentional extension strategy. Additionally, the algorithm reselects parent nodes and candidate nodes, followed by a rewiring process. As a result, the improved RRT algorithm eliminates redundant bifurcations in the growth tree, reduces the number of sampling instances, and significantly improves growth efficiency.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-G Heuristic-guided Exploration Methods", "weight": 1.0} -->

While the tree is extending, the Heuristic($\cdot$) method is used to estimate the remaining cost from $x_{\text{new}}$ to the goal, enabling the algorithm to prioritize nodes that appear more promising and accelerate convergence toward an optimal solution.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-G Heuristic-guided Exploration Methods", "weight": 1.0} -->

Heuristic-guided sampling enhances the efficiency of path planning algorithms by biasing the extending process towards regions more likely to yield high-quality paths. The Heuristically Guided RRT (hRRT) algorithm proposed by Urmson and Simmons utilizes a heuristic cost function to evaluate the quality of different states, thereby optimizing the sampling process. This algorithm has improved performance but does not provide any guarantee on the quality of its solution. To solve this, Gammell et al. present Informed RRT\* enhances RRT\* by incorporating an admissible cost heuristic, ensuring that only states capable of improving the current solution are considered. This approach accelerates the convergence rate of RRT\* while preserving its asymptotic optimality with high probability. Following this, Gammell et al. develop the Batch Informed Trees (BIT\*), which compactly groups states into an implicit random geometric graph (RGG), employing step-wise search similar to Lifelong Planning A\* (LPA\*), based on expected solution quality.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-G Heuristic-guided Exploration Methods", "weight": 1.0} -->

This approach combines heuristic-guided search with batch sampling and heuristic sorting of the search process, ensuring rapid convergence to high-quality solutions in both low- and high-dimensional spaces. Next, the Adaptively Informed Trees (AIT\*), improves upon BIT\* by utilizing the same progressively denser RGG approximation, but it employs an asymmetric bidirectional search. This search calculates and leverages a more accurate cost heuristic tailored to each specific RGG approximation. Then, the Advanced BIT\* (ABIT\*) further improves performance by integrating advanced graph-search techniques, such as heuristic inflation and search truncation. Furthermore, the Greedy BIT\* (GBIT\*) extends ABIT\* by incorporating a greedy search policy inspired by RRT-Connect, which accelerates the discovery of initial solutions and enhances convergence speed, while maintaining the asymptotic optimality of the solution. Respectively, Effort Informed Trees (EIT\*) builds upon AIT\* by utilizing problem-specific information in a way that takes advantage of informative admissible cost heuristics when available, but still performs effectively in their absence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-G Heuristic-guided Exploration Methods", "weight": 1.0} -->

It achieves this by incorporating additional types of problem-specific data, such as the computational effort required to validate a path. This generalization extends asymptotically optimal informed path planning algorithms to a wider range of problems, including those without effective a priori cost heuristics. Moreover, Hartmann et al. present Effort Informed Roadmaps (EIRM\*), EIRM\* extends the EIT\* approach to efficiently handle multiquery problems by actively reusing computational effort and managing graph size over multiple planning queries, thereby improving both speed and efficiency in complex environments. Subsequently, Li et al. propose Symmetrical Bidirectional Optimal Path Planning with Adaptive Heuristic (BiAIT\*), in contrast to AIT\*, BiAIT\* utilizes a symmetric bidirectional search for both heuristic calculation and space exploration. This method allows BiAIT\* to find an initial solution faster than AIT\* and to update the heuristic more efficiently when a collision occurs.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-H Various Rewiring for Tree Optimization", "weight": 1.0} -->

Subsequently, a Rewire($\cdot$) step is performed by evaluating neighboring vertices to determine if connecting through $x_{\text{new}}$ would lower their overall path cost. If a more efficient route is found, the parent vertices of those neighboring nodes are updated accordingly to reflect the improved path.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-H Various Rewiring for Tree Optimization", "weight": 1.0} -->

Karaman and Frazzoli are the first to present the idea of using the rewiring method to ensure asymptotic optimality. Building on top of the RRT\* presented, RRT-sharp (RRT^\#^) employs a more efficient rewiring cascade that not only propagates reduced cost-to-goal information throughout the graph but also adjusts connections within local neighborhoods when even lower cost-to-goal values are achievable. Moreover, RRT^X^ introduces a rewiring strategy to adapt to changes in dynamic environments. This algorithm quickly recalculates paths when the environment changes for dynamic obstacles. Subsequently, Quick-RRT\* enhances the rewiring procedure by incorporating the ancestry of nearby vertices, instead of only checking if a new node can provide a better connection for its direct neighbors. This improves the path optimization process by generating straighter paths and reducing detours. Respectively, The Real-Time RRT\* (RT-RRT\*) algorithm, based on RRT\* and Informed RRT\*, introduces an online tree rewiring strategy for real-time path planning in dynamic environments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-H Various Rewiring for Tree Optimization", "weight": 1.0} -->

This method enables the tree to quickly adapt to changes, maintaining near-optimal paths without rebuilding the entire tree. Additionally, a triangular inequality-based rewiring method is applied to the RRT-Connect algorithm, demonstrating faster planning times and shorter path lengths compared to both RRT and RRT-Connect algorithms. Similarly, the Post Triangular Rewiring method further improves the optimality of paths generated by the RRT algorithm by leveraging the triangular inequality principle.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-I Hybrid Search Approaches", "weight": 1.0} -->

In sampling-based algorithms, hybrid methods combine multiple path planning strategies to enhance the algorithm's performance and adaptability in complex environments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-I Hybrid Search Approaches", "weight": 1.0} -->

Wei and Liu combine RRT with a variable-length genetic algorithm, enhancing smooth path generation by minimizing path length and curvature, maintaining diversity, and preventing premature convergence. Mashayekhi et al. propose Hybrid RRT, Hybrid RRT utilizes a dual-tree search, enabling it to find solutions more quickly than unidirectional searches. Afterward, it merges the start tree and goal tree from the dual-tree search into a single tree to perform informed sampling, optimizing the current solution. Additionally, Al-Ansarry et al. introduce an enhanced approach known as Hybrid RRT-A\*, designed to address the limitations of the original RRT, particularly its slow convergence and high cost. By integrating the heuristic function of the A\* algorithm with RRT, the method reduces tree expansion and directs the search towards the goal more efficiently, using fewer nodes and less time. Respectively, Kiani et al. integrate RRT with Grey Wolf Optimization (GWO), demonstrating the ability to efficiently find near-optimal paths in three-dimensional path planning.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-I Hybrid Search Approaches", "weight": 1.0} -->

Pohan et al. propose a hybridization of RRT\* and Ant Colony System (RRT-ACS)to generate optimal parking paths efficiently, outperforming other algorithms in common scenarios. Recently, Cao et al. integrate the advantages of RRT-Connect for global path planning, artificial potential field (APF) for local path planning, and cubic B-spline for curve smoothing to optimize the path of unmanned aerial vehicles (UAVs).

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Application 1: Dynamic Environments", "weight": 1.0} -->

Dynamic path planning involves determining a path from a starting position to a goal position in an environment that evolves over time. This may include changes caused by moving obstacles, such as individual pedestrians or crowds, alterations in the environment's structure, or other dynamic elements requiring real-time path updates. Various sampling-based algorithms have been developed to efficiently replan paths in such scenarios. One common approach is to use bidirectional search, which facilitates quicker updates. Another strategy focuses on continuously refining and adjusting the search process during execution. Furthermore, biased sampling has proven to be an effective method for improving planning efficiency. Additionally, incorporating human awareness and crowd dynamics into the sampling-based planning process further enhances the planner's performance.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B Application 2: Unknown Environments and Uncertainty Localization", "weight": 1.0} -->

Robot motion planning in unknown environments is challenging, as it requires navigating without prior knowledge of the surroundings. In such cases, robots rely on real-time sensor data (e.g., LiDAR, cameras, sonar) to detect obstacles, track changes, and build an on-the-fly map. This process involves continuous exploration, obstacle avoidance, and dynamic path adjustments. Sampling-based algorithms play a crucial role in exploration tasks, enabling efficient and adaptive navigation in uncertain environments.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B Application 2: Unknown Environments and Uncertainty Localization", "weight": 1.0} -->

In unknown environments, one effective method involves using sampling-based algorithms with a biased direction to optimize node generation and reduce computational load, allowing for more efficient real-time path planning. Other strategies include rolling planning combined with node screening and model predictive control to further enhance path optimization.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B Application 2: Unknown Environments and Uncertainty Localization", "weight": 1.0} -->

To address localization uncertainties, sampling-based algorithms integrated with the Extended Kalman Filter (EKF) and Simultaneous Localization and Mapping (SLAM) have been employed to improve navigation accuracy. Additionally, sampling-based methods that focus on generating robust trajectories and risk-bounded trajectories provide enhanced path-planning capabilities in uncertain environments. The Min-Max RRT\* further refines this process by minimizing the maximum state estimate uncertainty along a path, offering an alternative to traditional additive cost representations of uncertainty.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-C Application 3: Nonholonomic constraints", "weight": 1.0} -->

Nonholonomic constraints limit a robot's movement in certain directions due to its physical structure, such as wheeled robots that cannot move sideways. These constraints complicate motion planning, requiring algorithms that generate paths respecting the robot's kinematic properties. To handle these challenges, sampling-based planners are adapted using techniques like steering functions, and goal bias. Another approach combines RRT\* with the generalized velocity obstacles (GVO) model to reduce trajectory uncertainty. Similarly, the use of a distance function extends RRT\* to handle nonholonomic constraints effectively. S-BRRT\* further optimizes planning by combining the strengths of bidirectional RRT\* with pruning and smoothing strategies. It incorporates bidirectional trees to enhance search efficiency and employs Bezier curves for path smoothing, significantly improving path quality and exploration efficiency in both sparse and dense environments.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-D Application 4: Kinematics", "weight": 1.0} -->

Sampling-based motion planning with kinodynamic constraints considers both the robot's kinematics and dynamics, planning in the state space (including position and velocity). This approach requires generating time-parameterized, dynamically feasible trajectories, making the problem more complex.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-D Application 4: Kinematics", "weight": 1.0} -->

A wide variety of sampling-based algorithms for kinodynamic planning exist. For instance, using a fixed-final-state-free-final-time controller, neural network predictions of cost functions to achieve the cost/metric between two given states considering the nonlinear constraints, deep reinforcement learning to learn an obstacle-avoiding policy that maps a robot's sensor observations to actions, precomputed motion primitives, lazy-steering techniques and using a partial-final-state-free (PFF) optimal controller in kinodynamic RRT\* to reduce the dimensionality of the sampling space.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-E Application 5: Manifold constraints", "weight": 1.0} -->

Motion planning under manifold constraints in robotics involves finding paths or trajectories that not only guide the robot from start to goal but also satisfy specific constraints defining a "manifold." Manifolds are higher-dimensional spaces representing the set of valid configurations that the robot can assume under its constraints, such as non-holonomic constraints, geometric constraints, kinematic limitations, or contact constraints.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-E Application 5: Manifold constraints", "weight": 1.0} -->

Several sampling-based algorithms have been proposed to address these challenges, such as projection methods, continuation techniques, reparameterization-based and offline methods that construct an approximation of the constraint manifold offline.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-F Application 6: Multi-Robot", "weight": 1.0} -->

Multi-robot motion planning focuses on coordinating the movements of multiple robots to complete individual or collective tasks while avoiding collisions. This involves not only determining paths for each robot within a shared environment but also managing their interactions to optimize overall efficiency. Such planning is crucial in applications like warehouse automation, search and rescue missions, autonomous bio-inspired robot coordination, and robotic swarms.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-F Application 6: Multi-Robot", "weight": 1.0} -->

Research in sampling-based algorithms has extensively tackled the challenges inherent in multi-robot motion planning, proposing various modifications and enhancements to traditional methods for improved performance. One approach integrates both tightly-coupled and loosely-coupled strategies within its framework, allowing it to adapt to diverse multi-robot task scenarios. Another method utilizes a more efficient sampling strategy to enhance planning efficiency. Additionally, an optimization-based map exploration strategy equips multiple robots to actively explore their environment.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-F Application 6: Multi-Robot", "weight": 1.0} -->

To efficiently plan within composite spaces, sampling-based algorithms offer effective strategies, where constructing individual roadmaps for each robot and implicitly searching the tensor product of these structures is a common approach. For resolving inter-robot conflicts, sampling-based methods incorporate techniques like Prioritized Planning (SI-CPP) and Conflict-Based Search (SI-CCBS) to better coordinate the paths of multiple robots.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-G Limitation 1: Narrow passage", "weight": 1.0} -->

In robot motion planning, the narrow passage problem refers to the challenge robots face when navigating through tight or confined spaces within complex environments. Research on sampling-based algorithms has extensively explored the narrow passage problem. Various studies have proposed modifications and enhancements to the traditional sampling-based algorithms to improve their performance in these constrained environments. One approach focuses on optimizing the sampling process to enhance the accuracy and efficiency of path planning in narrow spaces. Another strategy involves incorporating an improved bridge test along with a novel search method based on local guidance to facilitate smoother navigation. Additionally, Szkandera et al. propose a method inspired by the exit points for cavities in protein models, incorporating this concept into sampling-based algorithms. Respectively, Wang et al. model the tree selection process as a multi-armed bandit problem and using a reinforcement learning algorithm with an enhanced $\varepsilon_{t}$-greedy strategy to address the narrow passage problem.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-H Limitation 2: Slow convergence and large memory required", "weight": 1.0} -->

Sampling-based algorithms face several limitations and challenges, particularly related to low convergence rates and high memory requirements. Low Convergence Rates: sampling-based algorithms can struggle with convergence speed, especially in high-dimensional spaces. The random sampling process, while effective for exploration, can lead to slow convergence towards optimal paths. This is a significant drawback when quick and efficient path planning is required. High Memory Requirements: sampling-based algorithms often require large amounts of memory to store the extensive tree structures generated during the planning process. This can become problematic in scenarios with limited computational resources or when dealing with very large state spaces.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-H Limitation 2: Slow convergence and large memory required", "weight": 1.0} -->

To improve the convergence speed and memory efficiency of sampling-based algorithms, researchers have introduced various advanced methods. These include smart sampling techniques, bidirectional search, lazy search strategies, and heuristic-based methods.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-I Comprehensive Comparison of Sampling-based Algorithms", "weight": 1.0} -->

This table provides a comprehensive comparison of various typical sampling-based algorithms proposed between 1998 and 2024, showcasing the evolution of path planning techniques over the years. The table lists key attributes for each algorithm, including probabilistic completeness, bidirectional approach, heuristic search, batch sampling, asymptotic optimality, anytime capability, lazy collision check, greedy strategy, learning-based planning, static path planning, and dynamic path planning. These attributes highlight each method's technical advancements and specific features, providing insight into how they address different path planning challenges.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiment", "weight": 1.0} -->

In this survey, we utilize the Planner-Arena benchmark database, the Planner Developer Tools (PDT), and Open Robotics Automation Virtual Environment (OpenRAVE) to benchmark proposed motion planner behaviors.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experiment", "weight": 1.0} -->

Ten popular algorithms, including various versions of RRT-Connect, RRT\*, RRT^\#^, Informed RRT\*, LazyPRM\*, BIT\*, ABIT\*, AIT\*, EIRM\*, and EIT\* from the Open Motion Planning Library (OMPL), were tested in both simulated random scenarios and manipulation tasks (Fig., Fig. ). The evaluations are implemented on a desktop with an Intel i5-12600k processor and 16GB memory, running Ubuntu 20.04. These comparisons were carried out in simulated environments ranging from ${\mathbb{R}}^{4}$ to ${\mathbb{R}}^{16}$, and for Manipulation tasks ranging from ${\mathbb{R}}^{7}$ and ${\mathbb{R}}^{14}$. The primary objective for the planners was to minimize path length (cost). The RGG constant $\eta$ was uniformly set to 1.001, and the rewire factor was set to 1.2 for all planners.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Experiment", "weight": 1.0} -->

For RRT-based algorithms, a 5% goal bias was used, with maximum edge lengths of 0.5, 1.1, 1.25, 2.4 and 3.0 in ${\mathbb{R}}^{4}$, ${\mathbb{R}}^{7}$, ${\mathbb{R}}^{8}$, ${\mathbb{R}}^{14}$,${\mathbb{R}}^{16}$. All batch-sorted planners sampled 100 states per batch, and informed planners defined the informed set $X_{\hat{f}}$ using the current best costs.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Simulation Experimental Tasks", "weight": 1.0} -->

Fig. shows the performance of all algorithms in the wall gap test benchmarks and ten random rectangle experiments conducted in ${\mathbb{R}}^{4}$, ${\mathbb{R}}^{8}$, and ${\mathbb{R}}^{16}$. EIT\* and EIRM\* perform efficiently in terms of both success rate and path cost across various scenarios. RRT\*, RRT^\#^, and Informed RRT\* do not perform as well in terms of both success rate and path cost across various scenarios. RRT\* and RRT^\#^ Informed RRT\* tend to struggle with convergence speed, often requiring more time to find feasible solutions. As shown in Table II, various path planning algorithms are compared across multiple benchmark scenarios. Among benchmarked planners, EIT\* stands out as the state-of-the-art (SOTA) algorithm, achieves the lowest initial solution time of 0.0056s in the $\text{WG} - {\mathbb{R}}^{4}$ scenario.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-A Simulation Experimental Tasks", "weight": 1.0} -->

This impressive performance highlights EIT\*'s efficiency in quickly finding feasible paths, outperforming other algorithms such as RRT-Connect, RRT\*, and Informed RRT\*, which exhibit longer initial solution times.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-A Simulation Experimental Tasks", "weight": 1.0} -->

In the $\text{RR} - {\mathbb{R}}^{4}$ scenario, BIT\* and ABIT\* achieve shorter initial times (0.1239s and 0.0947s, respectively), compared to the other methods, with BIT\* also yielding a lower final solution cost ($c_{\text{final}}^{\text{med}} = 2.0457$). Similarly, in $\text{RR} - {\mathbb{R}}^{16}$, ABIT\* outperforms other planners in terms of initial time (0.5259s), although EIT\* demonstrates a lower final cost. In higher-dimensional scenarios, EIT\* continues to demonstrate its competitive edge, with notable efficiency observed in both $\text{WG} - {\mathbb{R}}^{8}$ and $\text{WG} - {\mathbb{R}}^{16}$. The ability of EIT\* to maintain low initial solution times while achieving satisfactory final solution costs reinforces its status as a leading approach in path planning.

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-A Simulation Experimental Tasks", "weight": 1.0} -->

Overall, the table underscores the adaptability of sampling-based planners in high-dimensional spaces, achieving low initial solution times and final costs across various scenarios. ABIT\* and BIT\* excel in structured environments such as $\text{RR} - {\mathbb{R}}^{4}$ and $\text{RR} - {\mathbb{R}}^{16}$, effectively balancing initial time and solution cost. EIT\* and EIRM\* exhibit similarly low values for median initial solution time, median initial solution cost, and median solution cost over time. In contrast, RRT\*, RRT^\#^, and Informed RRT\* demonstrate higher median initial solution times, initial solution costs, and solution costs over time.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

Fig. shows the performance of all algorithms in the Single-Arm Manipulator Problem and in Dual-Arm Manipulator Problem. RRT-Connect and ABIT\* are faster than other algorithms but may result in higher costs, making them suitable for applications requiring quick solutions. On the other hand, Lazy PRM\*, BIT\* and AIT\* achieve lower costs but require more computation time, making them ideal for scenarios where path optimality is crucial. RRT\*, RRT^\#^, and Informed RRT\* do not perform as well in terms of both success rate and path cost. As illustrated in Table III, we compare various algorithms for manipulation tasks, focusing on both single-arm (SA) and dual-arm (DA) configurations in high-dimensional spaces.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

The performance metrics include median initial solution time ($t_{\text{init}}^{\text{med}}$), median initial solution cost ($c_{\text{init}}^{\text{med}}$), and median solution cost over time ($c_{\text{final}}^{\text{med}}$).

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

In the single-arm scenario ($\text{SA} - {\mathbb{R}}^{7}$), RRT-Connect demonstrates a relatively low initial solution time of 0.2260s, but its final solution cost remains high at 18.0909. Conversely, EIT\* offers a more competitive median initial solution time of 0.8493s while achieving a notably lower median solution cost of 16.3089, indicating its efficiency in path optimization.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

The dual-arm configuration ($\text{DA} - {\mathbb{R}}^{14}$) presents similar trends. EIT\* achieves an initial solution time of 0.6177s, which is comparable to other algorithms, while also has the minimal final solution cost at 12.4140. This positions EIT\* as a strong contender in both initial speed and long-term cost efficiency.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

Among the other algorithms, RRT\*, RRT^\#^, Informed RRT\* exhibit higher initial solution times, indicating less efficiency in quickly generating paths. LazyPRM\* shows slightly better final solution costs but suffers from higher initial costs and times compared to EIT\*.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-B Simulated Manipulation Tasks", "weight": 1.0} -->

Overall, these experiments demonstrate the performance of ten popular algorithms across various scenarios, solidifying their status as leading choices in high-dimensional manipulation path planning. The performance in both single-arm and dual-arm tasks highlights their feasibility and efficiency.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Sampling-based motion planning algorithms are highly effective for exploring continuously-valued spaces, which are commonly encountered in robotics. These algorithms rely on generating samples to approximate and explore the search space. Many sampling-based algorithms are probabilistically complete. But these algorithms do not provide any guarantee on the quality of its solution. In recent years, researchers have focused on addressing this issue. In this article, we have reviewed the progress made. We divide the traditional sampling-based algorithms framework into seven parts, Sampling($\cdot$), Nearest($\cdot$), Steer($\cdot$), CollisionFree($\cdot$), Extend($\cdot$) including Heuristic($\cdot$), Rewire($\cdot$). We conduct an extensive literature review on these seven aspects and provide a summary and analysis of the current research status. Furthermore, this paper tests the performance of ten popular planners in both simulated random scenarios and Manipulation tasks with different dimensions. The results suggest that planning algorithms are capable of solving a wide range of problems, including those with narrow passages and constraints. However, no single planner consistently outperforms others across all problem types.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Apart from the comparative evaluations, this review provides a comprehensive overview about applications and limitations, such as dynamic environments, Narrow passage and kinodynamic constraints. This helps researchers and practitioners to make better understanding sampling-based planners in different fields.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In summary, by systematically reviewing the state of the art and addressing the remaining challenges, this survey serves as a valuable resource for researchers and practitioners in the field of robotics. It offers a clear understanding of the current landscape of motion planning techniques and provides insights into the future directions of this rapidly evolving area of study.
