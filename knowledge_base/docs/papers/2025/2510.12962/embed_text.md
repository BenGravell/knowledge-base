## Introduction

The task of path planning for a solid 3D object is to find a feasible (collision-free) path in an environment with obstacles, which arises in many applications in robotics and other fields, such as autonomous car navigation, CAD design, and assembly. This leads to a search in six-dimensional configuration space, which can be solved using sampling-based approaches like Rapidly-exploring Random Trees (RRT) or Probabilistic Roadmaps (PRM). Sampling-based planners randomly sample the configuration space and maintain a graph structure (roadmap) of the collision-free samples. A solution (path) is found in the roadmap using a graph-based search. The narrow passage problem arises when the solution leads through a narrow collision-free region whose volume is significantly smaller than the volume of the whole configuration space. In such a case, the probability of placing samples into the narrow passage is low. Consequently, many samples must be drawn to find a solution through the narrow passage, which increases planning runtime. The narrow passage problem has been studied in many papers surveyed , resulting in various approaches to cope with the problem. Nevertheless, the planning for a solid 3D object in the presence of a narrow passage is still an open problem as both the success rate (of finding a feasible path) and the computational time of the existing methods are greatly affected, as shown in this paper.

In guided sampling, a guide (a path in the workspace or even in the configuration space) is used to generate the random samples along it. A guiding path in the configuration space can be found by solving a similar, yet simpler, problem. In scenarios requiring path planning for different objects in the same environment (e.g., in bin-picking ), computing the guiding paths prior to every planning would introduce a considerable overhead and slow the planning process.

This paper proposes a novel method named Rapidly-exploring Random Trees with a Library of Paths (RRT-LIB), shown in Figure 1. We aim to reuse the knowledge gained by previous planning and generalize it to different objects moving through the same environment. In the preparation phase, we compile a library containing paths for multiple object classes. The paths are generated using a planner that is able to quickly approximate paths through an environment with narrow passages. The planner then leverages this knowledge in the planning phase. When a path for a new object is required, we retrieve the paths of the most similar object in the library. We choose the most similar object using a state-of-the-art 3D shape similarity evaluation method. The relative transformation between the library and manipulated objects is computed using the Iterative Closest Point algorithm (ICP). The library paths are then transformed accordingly to be more relevant for the current planning task. Finally, these transformed paths serve as guiding paths, hinting at the possible paths through the environment.

Figure 1: RRT-LIB: Rapidly-exploring Random Trees with a Library of Paths — a novel algorithm for path planning in environments with narrow passages, consisting of the preparation phase (top) and the planning phase (bottom).

We demonstrate the effectiveness of our method on various environments and objects using a benchmarking tool inside the Open Motion Planning Library (OMPL). We show that RRT-LIB outperforms the existing methods in various environments containing multiple narrow passages, offering up to $85\%$ decrease in the time needed and often being the only planner able to find a solution in the given amount of time.

## Related Work

The most well-known sampling-based planners are Rapidly-exploring Random Trees (RRT) and Probabilistic Roadmaps (PRM). Several planners were derived from basic RRT and PRM, such as their asymptotically optimal variants RRT\* and PRM\*. We refer to the surveys about general variants of sampling-based planners. The survey focuses on sampling under constraints and surveys on optimal path planning.

Sampling-based planners can suffer from the well-known narrow passage problem, where a solution leads through a relatively small collision-free region of the configuration space. Due to its volume (relative to the volume of the whole configuration space), the probability of placing enough samples into the narrow passage is low. This increases the number of samples (and therefore the time) the planners need to find a solution.

Early attempts to cope with the narrow passages increase the probability of generating random samples around the obstacles. For example, the Gaussian PRM generates two close samples. If exactly one of them is collision-free, it is added to the roadmap, effectively increasing the density of the roadmap near the obstacles. The strategy was further extended in the Bridge-test PRM.

Among the basic extensions of RRT to cope with the narrow passage problem is the bidirectional RRT, where two trees are built simultaneously or RRT with multiple trees. However, the above-mentioned planners do not utilize the knowledge of the workspace (e.g., shapes of the obstacles or information about the medial axis of the workspace).

Utilizing workspace knowledge can significantly improve planning performance. The XXL planner utilizes a decomposed workspace to generate samples for various control points on a many-DOF robot. The MAPRM approach retracts the samples towards the medial axis of the workspace. Similarly, the RRT-based planner utilizes the medial axis of the workspace. RRV uses collision-free and colliding samples to identify the type of local space (e.g., an entrance to a narrow passage). It uses PCA (Principal Component Analysis) to analyze the type of local space. In, a machine learning-based approach is used to estimate new relevant regions for sampling. The learning uses the samples and the information about collision detection and cost-to-go heuristics collected during the sampling.

A large family of methods utilizes the concept of guided-based planning, where the random samples are generated along a guide (path) instead of the whole configuration space. In case the environment contains a narrow passage and a guiding path going through the narrow passage is available, using the guide increases the probability of sampling in the narrow passage, thereby decreasing the time needed to find a solution. The simple guide can be represented as a path in the 2D workspace, a path in the 3D workspace, or a medial axis. The work utilizes multiple guides for motion planning of a mobile manipulator. One guiding path computed on the ground is used for generating samples for the mobile platform, and planning for the manipulator is guided using a 3D path generated in the workspace. The work uses bidirectional search to sample along waypoints of previously found paths.

The performance of sampling along a workspace-based guide decreases with the increasing dimension of the configuration space. Therefore, other techniques must be employed to obtain the guide for high-dimensional spaces. Researchers in proposed computing the guide directly in the configuration space. This is achieved by solving a similar but simpler (relaxed) problem. For example, collision constraints can be relaxed by scaling-down the robot (or obstacles) or by their thinning. After the approximate solution is found, the configuration space is sampled again with the original robot.

In a mostly static workspace (e.g., mobile robots used for shelf stacking in a warehouse), experience can enhance planning performance. The Experience-Driven Random Trees (ERT) method saves solution paths into a database as the robot completes various planning tasks. The path segments represent the robot's experience and are used to expand the search tree in subsequent planning tasks. In, the experience is a movement through a specific obstacle region (e.g., a robot's arm moving through a bookcase shelf). A standard sampling-based planner is used to find a path during the first interaction with a local obstacle region. This path is saved to a database, and when a similar obstacle region is encountered again, the database path is used to guide the planner. However, this approach requires an explicit model of the obstacles to create the local primitives. In both approaches, the experience depends on both the robot and the workspace. Therefore, the methods are suitable for situations where one robot repeatedly works in the same environment. In, a database of previously found paths for a robotic manipulator is used in parallel with planning-from-scratch. The path from the database is selected based on the distance of the start and goal configurations, and repaired if necessary. The repairing process identifies all valid segments of the path and attempts to connect them using bidirectional RRT. Simultaneously, planning from scratch aims to find new paths in the configuration space. A path found by either the database-based planner or by the planning-from-scratch is executed on the robot, and the database is updated if the new paths differ from the stored ones. The framework is further extended , but instead of storing whole paths, previous experience is stored in sparse roadmap spanners. Sparse roadmap spanners can represent known connectivity in large configuration spaces and are less memory demanding than storing all previously found paths. The solution database is also used ; each path is associated with a situation descriptor (e.g., information about start, goal, distance from obstacles, shape of obstacles around the path) and the descriptor is used to find a matching path from the database. The configuration space in is searched using bidirectional RRT with dense sampling along the waypoints of the matching path. Unlike our method proposed in this paper, the framework does not automatically decide if the newly found solution is stored in the database; it is decided by the user.

While guided-based planners and database-based approaches use stored paths to sample the configuration space (e.g., sampling along the paths), the approach uses the path database to compute the heuristic determining which nodes of the search tree should be expanded. Moreover, the database is updated during the search (and not only after a valid path is found as in ).

Learning-based approaches are also presented in the available literature. In Motion Planning Networks (MPNet), two neural networks are used to plan the path incrementally. The first network encodes the environment with obstacles into a latent space. The other network then takes this encoding, the current robot configuration, and the goal configuration and outputs the following configuration on the path. An optimal planner such as RRT\* is used to teach the PNet when the neural network cannot provide a feasible trajectory. The drawback is that the same robot needs to stay the same between the training and the online execution. In, a Convolutional Neural Network is trained to predict sampling distribution for RRT\*. The network is trained on more than $10^{6}$ examples of optimal trajectories computed by A\*. The approach is, however, limited only to 2D configuration spaces (as the input to the network is a 2D image of the workspace) and can work only for circular robots but not for general shapes as in our method. In, an autoencoding network is used to learn the latent space of the configuration space (the training data contains short feasible trajectories), and the planning is then realized using the latent space. The training requires many examples (authors use $10^{4}$ trajectories).

Such training by examples is similar to Learning from Demonstration, which leverages motions generated by a human expert when solving new problem instances (e.g., a robotic arm reproducing several tasks, such as grasping, placing, and releasing ).

The most relevant approaches for our method are. While these frameworks assume only one type of robot, we consider multiple types of robots (objects). After a matching (guiding) path is found in the database for a given robot (object), it is not directly used to sample the configuration space like , but it is first transformed according to the similarity between the object in the database and the current one. Similarly to the related works, our planner can update the library after discovering a new path. However, the library is updated only if the new path is distinct from already stored ones.

## Rapidly-exploring Random Trees with a Library of Paths

The proposed method aims to solve path planning for various (query) 3D objects moving in a set of $m$ environments. The objects are allowed to move and rotate in the environment --- therefore, their state is described by a configuration $q \in {SE{}}$. Instead of searching the configuration space for each object from scratch, we build a library of template paths for a set of $n$ template objects in each environment. Then, to find a path for a query object $\mathcal{O}_{q}$, the most similar object in the library is found first and the template paths for it are retrieved. These paths are considered as approximate solutions for the query object, and the configuration space is sampled densely along them. Let ${\mathcal{O}_{i},i} \in {\{ 1,\ldots,n\}}$ be the template objects and ${\mathcal{W}_{j},j} \in {\{ 1,\ldots,m\}}$ the environments each described by a 3D triangular mesh. To compute the template paths, a scaled-down version $o_{i}$ of the template object $\mathcal{O}_{i}$ is used in order to promote finding multiple approximate guiding paths, as discussed in and. Each pair of an object $o_{i}$ and an environment $\mathcal{W}_{j}$ forms its own configuration space $\mathcal{C}_{i,j}$. For the sake of simplicity, we denote the configuration space as $\mathcal{C}$ and its collision-free region as $\mathcal{C}_{\text{free}} \subseteq \mathcal{C}$. The library $\mathcal{L} = {({{\mathcal{O}_{i},\mathcal{W}_{j},P_{i,j}} \in \mathcal{C}_{\text{free}}})}$ contains $k_{i,j}$ template paths $P_{i,j} = {\{ p_{1},\ldots,p_{k_{i,j}}\}}$ for the scaled-down version $o_{i}$ of the $i$-th template object $\mathcal{O}_{i}$ in the $j$-th environment. The path ${p_{k} = {(q_{l})}},{q_{l} \in \mathcal{C}_{\text{free}}}$ is a sequence of collision-free waypoints. The ultimate goal of the method is to solve planning from the start towards the goal configuration in an environment $\mathcal{W}_{j}$. We assume that all template objects are collision-free when placed at both start and goal configurations in the environment $\mathcal{W}_{j}$. The proposed RRT-LIB method consists of two main phases: the preparation phase and the planning phase.

### Preparation phase

The purpose of the preparation phase is to create a library of paths $\mathcal{L} = {\{ P_{i,j}\}}$, where $P_{i,j}$ is a set of distinct paths for a template object $\mathcal{O}_{i}$ and an environment $\mathcal{W}_{j}$. The preparation phase is depicted in Figure 2. This phase simulates a process of collecting plans from the past planning experience, when an entirely new type of manipulated object is introduced to the planning and the user decides it is worth creating a new template object instead of using the templates already available in the database. Alternatively, the library $\mathcal{L}$ can be updated during the planning phase every time a new path distinct from the already stored ones is found. Based on the similarity metric, the algorithm can even automatically decide to create a new template object. These possible extensions are discussed in section 5. A naive approach to creating the library would be to employ a standard sampling-based planner (such as RRT) and repeatedly find various paths. However, sampling-based planners usually prefer to find easily achievable paths, and repeated planning from $q_{\text{start}}$ to $q_{\text{goal}}$ might result in similar paths with the same homotopy (i.e., paths that can be continuously deformed from one to the other without passing through the obstacle region).

To promote finding non-similar paths, we employ the RRT-IR (RRT with Inhibited Regions) planner, that is able to find multiple distinct paths in the environment. RRT-IR repeatedly searches the configuration space, and in each planning trial attempts to discover a new path. The configuration space is sampled uniformly, but the planner avoids certain "prohibited" regions $\mathcal{R} \subset \mathcal{C}$. In the beginning, the whole configuration space can be searched (i.e., $\mathcal{R} = \varnothing$). After a path is found, its waypoints are added into $\mathcal{R}$, so that the subsequent search will avoid sampling along the previously found paths. The preparation phase of RRT-LIB is presented in algorithm 1.

Figure 2: The preparation phase of the proposed RRT-LIB algorithm. The planner iteratively finds multiple paths through the environment. Using the already-found paths as input to the planner increases the probability of finding distinct paths. After enough distinct paths are found, the planning is terminated, and the paths are saved in the library.

Input: Template object 𝒪i and its scaled-down variant oi, workspace 𝒲j, start and goal configuration qstart, qgoal ∈ 𝒞free in the configuration space formed by oi and 𝒲j, library of paths ℒ
Params: Minimal similarity of paths dmin, Diversity patience ndiversity_patience, safe distance dsafe,
Output: Library of paths ℒ updated by new paths Pi, j
// Successive non-distinct paths found
// Avoid the inhibited regions (Alg. 2 in )
6 pk = RRT-IR(qstart, qgoal, 𝒢 = ⌀, ℛ);
// Add pk to Pi, j only if distinct enough
// Update the inhibited regions with a subset of pk
15 ℛ = ℛ ∪ {q ∈ pk|𝜚q (q,qstart) &gt; dsafe ∧ 𝜚q (q,qgoal) &gt; dsafe};
// Update the library
Algorithm 1 RRT-LIB preparation phase: finding paths for template object 𝒪i in environment 𝒲j

The original RRT-IR can find multiple similar paths, which could decrease the efficiency of the library since we want to store only distinct paths. There is also no clear indication when we should stop searching for new paths, and input from the user (i.e., the number of iterations) is required. However, the number of iterations needed is hard to predict for complex environments. We extend the original RRT-IR with path diversity tracking to solve this issue. The distance between a pair of paths $\varrho_{p}$($p_{1},p_{2}$) is measured as

where $\varrho_{q}{(q_{1},q_{2})}$ is a metric function on $SE{}$, i.e., $\varrho_{q}:{{{{SE{}} \times S}E{}}\rightarrow{\mathbb{R}}}$. The distance of a path $p$ from a set containing multiple paths $P = {\{ p_{1},\ldots,p_{n}\}}$ is then computed as

In order for a path to be considered distinct from the paths already found, its distance to the set containing the paths needs to be higher than a specified threshold $d_{\text{min}}$.

Tracking the diversity of the guiding paths comes with two advantages. Adding a nondistinct path to the set of guiding paths would not give us any new information. Removing such paths results in fewer guiding paths while preserving diversity. This improves the speed of the second phase, where the guiding paths are used to guide the path search. However, the nondistinct path is still added to the inhibited regions to enforce searching for new, distinct paths. The second advantage comes from the fact that searching for new guiding paths can be automatically stopped when the path diversity reaches a plateau, in contrast to having to manually specify the number of guiding paths prior to the search phase. In reality, stopping as soon as the first nondistinct path is found could lead to missing more complicated paths. Therefore, the search is terminated once no distinct path has been found in the last $n_{\text{diversity\_patience}}$ steps.

### Planning phase

The aim of the planning phase is to find a path from $q_{\text{start}}$ to $q_{\text{goal}}$ for a given query object as fast as possible, which is achieved by guided sampling along a suitable path from the library (depicted in Figure 3). First, the most similar template object $\mathcal{O}_{i}$ to the query object $\mathcal{O}_{q}$ is found in the library $\mathcal{L}$. We use a method presented in which utilizes genetic algorithms to find the correspondence map between two meshes, minimizing the Average Isometric Distortion (summary presented in the SHREC'19 contest paper ). From the library, we select the object that minimizes this metric to the query object and retrieve the paths $p_{k} \in P_{i,j}$ computed for the template object along with correspondences $\mathcal{S}_{q,i}$ between the query and the template object (pairs of mesh points, visualized in Figure 4).

Figure 3: The planning phase of the proposed RRT-LIB algorithm. The input consists of a manipulated object and an environment. Based on the inputs, paths computed for the most similar object in the library are loaded. After transforming the paths to account for possibly different positions of the manipulated object and the object from the library, we gain paths hinting at the possible paths through the environment. Increasing the sampling rate along these guiding paths should increase the probability of finding a solution.

It can be expected that the query object $\mathcal{O}_{q}$ and the template object $\mathcal{O}_{i}$ do not share the same pose (e.g., a query desk object can be rotated, while the template desk object is not rotated, as in Figure 5). In such a case, the approximate paths $P_{i,j}$ are not able to guide the search for the query objects. Therefore, the relative transformation of the query object to the template object is found using the Iterative Closest Point method (ICP). The results of ICP are the relative translation $t$ and rotation $R$. Then, the approximate solutions $P_{i,j}$ are transformed accordingly, i.e., all the waypoints are rotated and translated (Figure 5). ICP is primarily used for correcting small transformations, and it is recommended to provide the algorithm with an initial guess of the correspondences. For that, we extend the original algorithm by using the correspondences $\mathcal{S}_{q,i}$ retrieved during the similarity evaluation. These correspondences are computed using the method , which identifies geometric similarities between meshes and can successfully establish matches even under large transformations between the query and the objects in the library. This initial estimate then enables the ICP algorithm to efficiently find a transformation between the objects. The extended ICP algorithm is outlined in algorithm 2. By adding the ICP transformation into the planner, we get the RRT-LIB planning phase outlined in algorithm 3.

Figure 4: For every query object (left on each image), the most similar object from the library is selected (right on each image). The correspondences between the objects (illustrated by the colored lines) are used as the initial guess in the ICP algorithm.

(b) Mutual pose transformation found by ICP.

(d) After the transformation is applied.

Figure 5: When the mutual position and rotation of the guiding object (red) and the similar object (blue) are not taken into account, the guiding paths become useless because they guide the similar object through the wall instead of the middle window (Figure 5c). After the guiding paths are transformed using the transformation obtained from ICP, planning along them becomes viable (Figure 5d).

Input: Source mesh A = (a1,a2,…,an),
Initial correspondences S = ((as1,bs1),(as2,bs2),…,(asl,bsl))
Params: Maximum iterations K, Minimal error εmin
Output: Rotation matrix R*, Translation vector t*
7 for i = 1, …, n do // Nearest vertex to
// each vertex in source
Algorithm 2 ICP with an initial guess

Input: Query object 𝒪q, Workspace 𝒲j, Configurations qstart, qgoal ∈ 𝒞free in the configuration space formed by 𝒪q and 𝒲j, Library of paths ℒ
Output: Path τ from qstart to qgoal or empty list
// Identify guiding object from ℒ
// Compute mutual transformation (algorithm 2)
// Transform the library paths
// Plan along guiding paths 𝒢 (Alg. 2 in )
7 τ = RRT-IR(qstart, qgoal, 𝒢, ℛ = ⌀);
Algorithm 3 RRT-LIB planning phase

## Results

To compare the performance of our RRT-LIB planner with other planners, the Open Motion Planning Library (OMPL) and its benchmarking suite were used. The compared algorithms are listed in Table 1. The parameter settings for our RRT-LIB planner are listed in Table 2, with the default configuration used for all other planners. For each object and map pair, a benchmark test is performed, consisting of 50 runs with a 2-minute time limit each. Our primary criterion for comparison is the time required to find a solution --- therefore, each run is stopped as soon as a feasible solution is found. The calculations are carried out on a computing grid MetaCentrum^11^1 Each node runs a system with one thread on CPU Intel Xeon Gold 5120 and 8 GB of RAM.

RRT with a Library of Paths

Rapidly-Exploring Random Trees

Lazy vertex and edge evaluation RRT

Lazy vertex and edge evaluation PRM

Kinematic Planning by Interior-Exterior Cell Exploration

Lazy vertex and edge evaluation KPIECE

Expansive Space Trees

Single-query Bi-directional Lazy collision checking planner

Search Tree with Resolution Independent Density Estimation

Table 1: Planners used in the benchmark.

Table 2: RRT-LIB planner parameter values

### Preparation phase

All implemented methods are tested using objects from the PSB dataset and manually created maps. Objects and maps are represented as triangulated meshes (each mesh has a few thousand triangles). To make the results comparable, each object is scaled so that its bounding box fits into a cube with an edge size of 2 map units. Scaling the objects does not affect our method of selecting the guiding object and correspondences, as shown in Appendix A. Three object categories (desks, chairs, and teddy bears) and two maps (map~1~ and map~2~) were chosen for the benchmarks. These maps were selected because they offer multiple distinct paths through the wall, and the window dimensions are designed to make the problem challenging enough but still solvable.

From each object category (desk, chair, and teddy), one object is selected as the template. For scaled-down^22^2Objects were scaled-down to 40% of their original size. versions of the objects, the template paths are computed in the two maps and saved to the library (visualized in Figure 6). Our proposed method of generating template paths is able to find distinct paths quite well. However, no path was found through the smallest window in Figure 6b and the middle window in Figure 6f. The template path generation takes approximately 20 seconds per object and map.

(a) chair2 &amp; map1

(b) desk1 &amp; map1

(c) teddy1 &amp; map1

(d) chair2 &amp; map2

(e) desk1 &amp; map2

(f) teddy1 &amp; map2

Figure 6: Guiding paths for the three guiding objects and two maps. Generated as a part of the RRT-LIB preparation phase.

### Computational comparison with the baseline algorithms

In each benchmark scenario, a query object and a map are given as inputs to the planners. At first, our method selects the most similar object from the library and computes the mutual correspondences. The selection of the most similar object takes, on average, one second per object in the library --- therefore, in our case, it adds approximately 3 seconds to each planning task. In all cases, the shape correspondence algorithm successfully selected the template object belonging to the same class as the query object (Figure 4). The paths computed for the template object are retrieved from the library, and a transformation between the template object and the query object is found by ICP to ensure the objects have a similar position and rotation. Finding the transformation using ICP is not time demanding, and it takes $140$ ms on average to compute for our data and computers used. After the transformation is applied to the paths from the library, they are used as the guiding paths for the planner. If no solution is found after two minutes (this time includes the similarity evaluation and ICP for our RRT-LIB planner), the run is terminated.

A representative subset of the benchmark results is presented in Figure 7 and Figure 9, with a bar graph representing the success rate of each planner (in how many of the ten runs a path was successfully found) and a box graph containing the time needed to find a solution (capped at the 2-minute threshold). In the easier (i.e., the objects can pass through multiple windows and do not require complex maneuvers to do so) benchmarks (Figure 7), our planner achieves a 100% success rate, along with some other planners. However, considering the time added by generating the template paths in the preparation phase (not included in the timing), selecting the template object from the library, and finding the mutual transformation using ICP in the planning phase ($\sim$`<!-- -->`{=html}3 s, included in the timing), using one of the other planners would still be faster in some cases. A detailed view of the results is shown in Figure 8. In the first test, our planner solves the task in $3.5$ s on average, whereas the RRT and RRTConnect need $2.2$ s and $1.4$ s on average, respectively. Here, the main contribution to the time needed by the RRT-LIB planner is the similarity evaluation ($\sim$`<!-- -->`{=html}3 s). In the second and third tests, the advantage of retrieving the guiding paths for a similar object and transforming them for the given task starts to show. In the second test, the average runtime of our RRT-LIB planner is $3.4$ s --- a $50$% improvement over the second best algorithm in the test (RRTConnect with an average of $6.8$ s). In the third test, the average runtime of our RRT-LIB planner is $3.6$ s --- an approximately $85$% improvement over the second best algorithm in the test (RRT with an average of $24.3$ s).

(a) Query object, map and guiding paths

(d) Query object, map and guiding paths

(g) Query object, map and guiding paths

Figure 7: Easier benchmarks results

Figure 8: Detailed view of three benchmark results with median values shown. The runtime of our RRT-LIB planner is compared to the standard RRT and its bidirectional variant (RRTConnect).

Tests depicted in Figure 9 are substantially more challenging (i.e., the objects can only pass through one of the windows, and complex maneuvering is needed) and show the real advantage of using the guiding paths retrieved from the library and transformed to respect the manipulated object. Our planner is still able to find a solution in most of the runs, while the other planners fail every time. Specifically, in the first and third scenario, our RRT-LIB planner retains the $100$% success rate, finding a solution in $3.8$ s and $10.2$ s on average, respectively. In the third scenario, our planner failed to find a solution in two of the 50 runs, while the other planners were unable to provide any solution. The fact that none of the other tested planners produced a solution within the 2-minute time limit (in 50 trials) demonstrates the superior performance of the proposed RRT-LIB, which achieves a 96 % success rate. A higher success rate could potentially be obtained by either increasing the allowed time limit or tuning the parameters, but this is beyond the scope of this paper.

(a) Query object, map and guiding paths

(d) Query object, map and guiding paths

(g) Query object, map and guiding paths

Figure 9: Challenging benchmarks results

To demonstrate the transferability of the information contained in the library, we concluded another experiment with a much larger object. The object's minimal 3D bounding box is considerably larger than any of the windows, and a precise manipulation is needed to pass the narrow passage, as shown in Figure 10. Our RRT-LIB planner is still able to solve such problem with a 100% success rate in the imposed 2-minute limit, while the other planners fail every time.

(a) Query object and its minimal bounding box

(d) RRT-LIB solution: Entry

(e) RRT-LIB solution: Narrow Passage

(f) RRT-LIB solution: Exit

Figure 10: The proposed RRT-LIB planner is able to efficiently solve a problem where passing through the narrow passage requires precise manipulation.

## Discussion

The overhead introduced by the various steps in the pipeline (i.e., computing similarity between objects, finding their transformation using ICP, and planning) must be considered when evaluating the usefulness of the RRT-LIB planner for a specific task. The most time-consuming part of each query is the computation of similarity between the query and the objects in the library, which is performed using the method in and takes approximately 1 s per object (the objects used in the experiments are described by thousands of triangles). The evaluation of similarity can be accelerated by employing alternative shape-matching methods, possibly combined with mesh simplification. Mesh simplification would also speed up the ICP step; however, in our experiments, ICP takes only 140 ms per query, which is negligible compared to the time required for computing the similarity.

When the planning problem is easy to solve, the time required to select the template object and compute the mutual transformation can be considerably longer than the planning itself. Although the planner finds the solution almost immediately using the guiding paths, no significant time is saved compared to a standard RRT planner. Therefore, applying RRT-LIB in simple scenarios (e.g., convex robots navigating among widely spaced obstacles without narrow passages) provides little to no advantage.

In contrast, the benefit of using guiding paths computed for similar objects becomes apparent in challenging scenarios, where narrow passages and complex obstacles make planning significantly more difficult. In these cases, RRT-LIB substantially accelerates the search. Moreover, it successfully finds paths even when the other planners fail. However, the library needs to contain computed paths, and the computation of guiding paths in the RRT-LIB preparation phase requires a considerable amount of time. This requirement is similar to the learning-based path-planning approaches, which require significant training time. Making such an effort is reasonable only when planning for similar objects in the same environment repeatedly. Suppose that we know that the planning will be performed multiple times with a defined set of static environments and object classes. In that case, we can reuse the experience gained by prior planning, and devoting the time to compute paths to store in the library will prove advantageous in the long run. However, when the planning task is unique and will not be repeated, one should also consider other approaches when choosing the right planner.

Alternatively, RRT-LIB could be used even with an empty database $\mathcal{L}$ and update the database after new paths are found. In such a case, the planner (Alg. 3) would start with no guiding paths ($\mathcal{G} = \varnothing$) and would perform a standard RRT search. After finding a path, the planner would store the object as a template and the path as a guiding path in the database. During subsequent planning tasks, each newly found path would be stored only if it was distinct enough from the already stored paths (as in Alg. 1, line 1). Updating the library by the latest plan is common also in related works. However, these works assume only one type of robot, so the new paths are simply added to the library. In RRT-LIB, multiple objects (robots) are assumed --- if the object was deemed too different (which could be implemented trivially by thresholding the similarity metric used for similarity evaluation), a new template object would be created instead.

## Conclusion

This work presented RRT-LIB, an algorithm that aims to improve the efficiency of sampling-based planners by creating a library with already computed paths in an environment with narrow passages. We generate distinct paths for multiple object classes using Rapidly-Exploring Random Trees with Inhibited Regions (RRT-IR). These paths are filtered based on their similarity using our proposed method, and a diverse subset is saved in the library. During a query, the object most similar to the given manipulated object is found in the library using shape-matching methods based on Genetic Algorithms. To ensure that the library object and the manipulated object are positioned similarly in the coordinate frame, a transformation between them is found by the ICP algorithm. Finally, the transformed paths are used to guide the planner through the narrow passages contained in the environment.

We compared our planner to other state-of-the-art path planning methods using an open-source planning library OMPL. The benchmarks demonstrated that having multiple precomputed paths through the environment for a template object can substantially decrease the time needed when planning for a new similarly-shaped object. Our RRT-LIB planner was able to outperform the other state-of-the-art planners, with a 50 % and 85 % lower runtime in two of our tests compared to the second-best planner in each test. More importantly, our planner is able to find paths even in cases where the other planners fail. This was shown in three test scenarios, where the other planners were unable to find any solution in 50 test runs, while our algorithm found the solution in $100$ % runs in two of the tests and in $96$ % runs in another test scenario.

Future work includes implementing a more complex path-filtering method since even two homotopic paths can be declared distinct (when using the average distance between them) if they are far enough in the free space. Among the more advanced methods for filtering paths based on their path through the environment is topological clustering or Maximal Path Diversity Pruning. This could lead to improved results in more types of environments.
