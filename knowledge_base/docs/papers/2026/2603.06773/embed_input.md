<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stability-Guided Exploration for Diverse Motion Generation

Topics include Trajectory optimization, Robotics, Stability analysis, Deep learning, Datasets, Sampling-based methods, Search trees, Optimization, Learning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Scaling up datasets is highly effective in improving the performance of deep learning models, including in the field of robot learning. However, data collection still proves to be a bottleneck. Approaches relying on collecting human demonstrations are labor-intensive and inherently limited: they tend to be narrow, task-specific, and fail to adequately explore the full space of feasible states. Synthetic data generation could remedy this, but current techniques mostly rely on local trajectory optimization and fail to find diverse solutions. In this work, we propose a novel method capable of finding diverse long-horizon manipulations through black-box simulation. We achieve this by combining an RRT-style search with sampling-based MPC, together with a novel sampling scheme that guides the exploration toward stable configurations. Specifically, we sample from a manifold of stable states while growing a search tree directly through simulation, without restricting the planner to purely stable motions. We demonstrate the method's ability to discover diverse manipulation strategies, including pushing, grasping, pivoting, throwing, and tool use, across different robot morphologies, without task-specific guidance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

Recent advances in deep learning have demonstrated impressive capabilities for controlling robots. These developments emphasize the need for large-scale, diverse robotic datasets to enable further progress. However, compared to domains like vision and language, datasets for robotics are not as readily available. This has led to research efforts directed towards obtaining more data. For this purpose, several different approaches have been explored. One of the most prominent in the field of behavioral cloning is teleoperation, where a human operator controls a robot to solve a specific task. While this can lead to high quality real world data, it requires extensive work from human experts, which is both expensive and time consuming. For reference, current large scale robotic datasets contain around a few million demonstrations, whereas VLM datasets comprise billions of image-text pairs. An alternative approach is to extract data from human video demonstrations, by using computer vision to estimate the positions of humans directly from online videos. The motivation for this type of method is the large amount of human videos found on the internet. However, these techniques do not produce the necessary low-level information needed for training robots. Furthermore, they only focus on human-like approaches, neglecting the diversity of robot morphologies.

<!-- chunk {"id": "body-0004", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

Overall, human generated data is inherently limited, as it may not be optimal and can fail to capture the full range of solutions accessible to robots. In contrast, algorithmically generated synthetic data can provide a broader set of valid solutions. Consequently, in this work, we are interested in the use of simulators to directly create high-quality and diverse data on tasks involving complex robot-object interactions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

Sampling-based Model Predictive Control (MPC) has recently shown promising results in generating dynamic motions by directly interacting with the simulator, both in locomotion and manipulation. However, these techniques mostly rely on local exploration in the control space, and are therefore prone to local minima. In contrast, sampling-based planners have a long history of relying on state space sampling to explore globally. We aim to combine both approaches to generate diverse, dynamic and contact-rich manipulations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Sampling-based MPC", "weight": 1.0} -->

MPC defines a controller as the solution to an optimal control problem. While MPC in robotics has historically relied on gradient-based optimization techniques, recent advances in parallel computing have enabled the successful deployment of gradient-free techniques in MPC on robots. In practice, most techniques currently used in robotics rely on some form of iterative procedure where samples following a Gaussian distribution are used to evaluate the function around the current guess in order to find a descent direction. For instance, Predictive Sampling simply picks the best sample to be the new guess around which the next Gaussian samples are drawn. MPPI uses a softmax weighting of the samples to compute an update direction. CMA-ES relies on a weighted average of the $k$-best samples (and also iteratively updates the covariance matrix).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Sampling-based MPC", "weight": 1.0} -->

The main strength of these techniques is that they can find interesting robot motions simply by interacting with the simulator. However, these approaches are inherently local. In many MPC and trajectory optimization methods, sampling is performed in the control space, often using single-shooting formulations, as handling constraints directly in gradient-free optimization is difficult. In contrast, graph-based motion planning methods sample in the state space and can offer theoretical guarantees such as probabilistic completeness.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Sampling Based Motion Planning", "weight": 1.0} -->

Sampling-based motion planners solve motion planning problems using probabilistic methods. They are commonly divided into two categories: single-query motion planning, with the most prominent approach being Rapidly-exploring Random Trees (RRTs), and multi-query motion planning, which is typically addressed using probabilistic roadmaps (PRMs). RRTs incrementally build a tree by sampling random states and extending the nearest node in the tree toward each sample. In contrast, PRMs build a graph by sampling points in the configuration space and attempting to connect nearby samples. This roadmap can then be reused to efficiently answer motion planning queries online. These algorithms are probabilistically complete under mild assumptions, meaning that they find a solution, if it exists, as the number of samples tends to infinity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Sampling Based Motion Planning", "weight": 1.0} -->

These methods have proven effective in many domains and have led to various extensions being developed. In the context of our work, an important extension is manifold RRTs. When constraints imposed on the system define a manifold of lower dimension than the ambient space, the probability of finding feasible points through uniform sampling in the ambient space approaches zero. Manifold RRTs address this issue by projecting sampled points onto the manifold and modifying the extend step to ensure that the tree grows along it.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sampling Based Motion Planning", "weight": 1.0} -->

In our work, we use the manifold of stable configurations to guide the search. Similarly to manifold RRT, we consider points projected onto a manifold as targets for extension; however, we do not restrict the paths to remain within the manifold. In that sense, our method is guided by a manifold of stable states while still being able to explore unstable states outside of it. This enables us to find diverse non-prehensile manipulations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Kinodynamic planning", "weight": 1.0} -->

Kinodynamic planning aims to solve problems involving both kinematics and dynamic constraints. The most direct approach is to use trajectory optimization; however, similarly to sampling-based MPC, it is subject to local minima and therefore cannot solve tasks involving long horizons. Another approach is to use Task and Motion Planning (TAMP); however, this implies a tedious manual definition of predicates. Alternatively, one could use sampling-based planners. For instance, RRTs can naturally be used for kino-dynamic planning by modifying the extend step to select a control input, typically by sampling multiple candidates and keeping the one that yields a next state closest to the target. Some works \[6: a framework to integrate local information into optimal path planning"), 33\] combined trajectory optimization and RRTs; however, they rely on gradient based optimization, which limits their application to problems involving complex contact interactions. In the context of manipulation, combined RRT and motion primitives to perform non-prehensile manipulation. In contacts are used for guiding motion planning, but is restricted to quasidynamic manipulation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Kinodynamic planning", "weight": 1.0} -->

Conceptually similar to our work, uses stability to guide a kino-dynamic RRT; however, they only consider non-prehensile manipulations on a $2$-dimensional plane. Furthermore, the authors enforce that the system ends up in a stable state after each action, while our approach allows the robots to execute multiple actions without intermittent stability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-C Contributions", "weight": 1.0} -->

We introduce StaGE, a novel algorithm to find complex and diverse long-horizon manipulations without motion priors. We achieve this by using our novel sampling scheme, Stability-Guidance, to guide a kino-dynamic RRT that directly interacts with black-box simulation. In addition, we provide a set of extensions to kino-dynamic RRT to encourage the generation of diverse behaviors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-C Contributions", "weight": 1.0} -->

Evaluations in multiple challenging environments with different robot morphologies qualitatively demonstrate the nature of the manipulations found by our approach.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-C Contributions", "weight": 1.0} -->

Importantly, the proposed method is task-agnostic. All the obtained motions naturally emerge and do not rely on manually tuned cost functions. To the best of our knowledge, this is the first generic method applying RRT with black-box simulation to non-prehensile manipulation without the use of hand-crafted motion primitives or analytical constraints.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

The aim of our method is to find diverse, contact-rich manipulations in any scene, independent of any task. To that end, we consider a hierarchy of subspaces $\mathcal{C}_{stable} \subset \mathcal{C}_{feasible}$, where $\mathcal{C}_{feasible}$ describes the space of all reachable states in a given black-box simulation, and $\mathcal{C}_{stable}$ additionally imposes that the state is stable, i.e., all objects are in equilibrium. Our method is divided into two stages. First, we sample states from $\mathcal{C}_{stable}$ using a diverse constraint solver. In the second stage, we use an RRT-style planner to find diverse paths between states. Importantly, the sampled random states are only used to guide the search; that is to say, the RRT-style planner is free to evolve through non-stable regions to enable dynamic manipulation. We provide a visual intuition for this approach in Fig. 1. The pseudo-code for StaGE can be seen in Alg. 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

In the first stage of our algorithm, we sample a set of fixed stable states $\mathcal{C}_{s} \subset \mathcal{C}_{stable}$ to guide the search later. To that end, we follow the constrained sampling method introduced, which generates states by solving a non-linear program. We briefly explain the method here and refer the reader to for more details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

The method first samples contact variables $c_{ij} \in {\{ 0,1\}}$, indicating whether the $i$-th and $j$-th frames in our scene are in contact. For scenes with one underactuated object (scenes (a), (b), and (d) in Fig. 2), we sample $1$ to $3$ support frames. If the scene contains multiple objects (scene (c) in Fig. 2), we sample uniformly from the set of up to three contacts, where each contact includes at least one underactuated object. Then, for each active contact, we add a point of attack $p_{ij}$, constrained to lie on both surfaces, as well as a force $f_{ij}$ acting on the frames, constrained to be within a predefined friction cone. Each underactuated object is constrained to be in a quasi-static equilibrium, i.e. the sum of all forces and moments acting on it through the contacts and gravity is zero. Lastly, we constrain the state to be collision-free.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

We then try to find a state $x$ satisfying these constraints by uniformly sampling a random initial state $\overline{x}$ formulating the optimization problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

which we solve using an augmented Lagrangian method. This formulation can be understood as a random projection onto the manifold $\mathcal{C}_{stable}$. Some examples of the resulting states can be seen in Fig. 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

While this method works well for the simple contact dynamics in the first two scenes in Fig. 2, it can struggle with the more complex meshes of the robotic arm introduced in scenes (c) and (d). That is to say, the optimizer may not find a solution that satisfies the constraint. If so, we sample a random initial state $\overline{x}$ again and try to solve it until success or a given number of trials is reached. In practice, in the PandaHook scene, we achieve a $100\%$ success rate in finding a stable state within $100$ attempts when both objects remain in contact with the table. However, imposing a grasp constraint (i.e., enforcing contact between an object and both finger frames of the gripper) reduces performance. The success rate drops to $15.1\%$ when attempting to grasp the cube and to only $1.4\%$ for grasping the hook. To remedy that, we first sort the contacts into high-level abstractions (namely contact with table, with panda or grasps) and then filter our stable states to have roughly equal numbers for each class.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Sampling Physically Stable States", "weight": 1.0} -->

We note that another way to circumvent this problem would be to handle these interactions by using specialized (grasp) samplers. However, this is beyond the scope of this work.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

To achieve our goal of finding diverse interactions, we build upon kinodynamic RRT. In its most basic version, kinodynamic RRT grows a tree rooted at a starting state by uniformly sampling a state and extending the closest node of the tree towards it. The extension works by selecting an action and simulating its effect for a fixed time-step. The end-state of that roll-out is then added as a new leaf of the tree. One possible scheme to select the action is to evaluate random actions through a physical engine and take the action that results in a state minimizing the distance to the sampled target state, as proposed. In this work, we refer to this approach as RRT-sim.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

While being generic, this approach is insufficient for our use-case. Intuitively, sampling directly in the configuration space will lead to too many uninteresting or irrelevant configurations (e.g., the tool flying in the air). To circumvent this issue, we propose stability-guidance, which means that instead of uniformly sampling from the space $\mathcal{C}_{feasible}$, we only sample from the embedded manifold $\mathcal{C}_{stable}$. Sampling from this manifold is expensive due to the complex, contact-rich interactions. Therefore, we first generate a set of fixed stable states $\mathcal{C}_{s}$, as described in section˜II-A, from which we draw a point to extend the tree towards. To compute the state to extend from and the action selected for extension, we use the weighted mean squared error as a metric, weighing the position error of non-actuated objects higher than the joint-state error of the robot.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

Furthermore, our goal is to find many diverse paths between multiple nodes in a dynamic, underactuated system with complex non-prehensile interactions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

Sampling from the $K$-Nearest Neighbors Instead of taking the node closest to the sampled stable state, we uniformly choose one of its $k$-nearest neighbors. This enables us to grow the tree (and consequently find more paths), even if the closest node is already within the minimum distance to the target state. To efficiently compute the $k$-nearest nodes for each stable state, we exploit the fact that the stable states are fixed: each stable state keeps a record of its $k$-nearest nodes, which we update each time we add a new node to our tree.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

This allows us to execute all the k-nearest neighbor searches and updates during the $N_{\max}$ iterations of the algorithm with $m = {|\mathcal{C}_{s}|}$ stable states in $\mathcal{O}{({N_{max}m{\log k}})}$ instead of $\mathcal{O}{({N_{max}{({{\log N_{max}} + k})}})}$ when using approximate nearest neighbors.^11^1in our implementation, the selection step is constant, while the update step costs $\mathcal{O}{({m{\log k}})}$ when using a max-heap to save the nearest nodes for each iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

Using approximate nearest neighbors one could achieve an expected runtime of $\mathcal{O}{({{\log i} + k})}$ in the $i$-th iteration, leading to the overall runtime $\mathcal{O}{({N_{max}{({{\log N_{max}} + k})}})}$. Since $N_{max} \gg m$, we use our (exact) implementation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

$N$-Best Actions Selecting the $n$-best actions that reduce the distance to the sampled target state, instead of only choosing the single best one, results in greater diversity in the paths found by our method.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

Node Rejection If a node fails to expand the tree towards any of the target stable states, we consider it to have a high likelihood of being a dead-end and therefore do not try to expand it further. Our environments contain unrecoverable states. For example, if the sphere falls off the ramp in scene (a) from Fig 2 or if the cube is pushed out of reach in (d). We believe that dead-ends act as a task-agnostic proxy for such states.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

Input: Maximum number of nodes Nmax, number of stable configurations m, nearest neighbors k, number of best actions n, minimal path difference dm i n
Output: Set of feasible paths 𝒫

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Connecting States", "weight": 1.0} -->

𝒳near ← KNearest (𝒯,xtarget,k);
(𝒜n,𝒳n) ← OptimizeActions (xnear,xtarget,n);

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Extracting Paths", "weight": 1.0} -->

We create paths from the tree grown in the second stage by selecting all nodes $x$ that fall within a certain minimum distance $\varepsilon$ to any of the stable states and extracting the path from $x_{0}$ to $x$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Extracting Paths", "weight": 1.0} -->

Afterwards, we filter out redundant paths for each goal state by iterating through the paths in random order and greedily taking a path if its distance to all previously taken paths is greater than a minimum threshold. We compute the distance between paths (given as sets $P,Q$) using the (undirected) Hausdorff-distance

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our method across four challenging environments. We provide baselines and perform ablations of all major algorithmic contributions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Environments", "weight": 1.0} -->

We use four distinct environments in our experiments, each using different robot morphologies and highlighting different challenges. The environments are depicted in Fig. 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Environments", "weight": 1.0} -->

SpheresRamp The environment consists of a single robot (blue) with a three-dimensional translational joint, manipulating an object (orange) on a ramp with two walls on the sides; a task similar to, but on a sloped surface. This environment enforces non-prehensile manipulation, since grasps are not possible. Furthermore, it contains non-recoverable states when the ball falls off the ramp.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Environments", "weight": 1.0} -->

SpheresCube This environment contains two robots (blue), each with three-dimensional translational joints, manipulating a cube. The environment contains two walls. This allows for diverse manipulations, where the cube can be pushed, grasped, thrown, or pivoted using the walls and floor. Additionally, the environment also forces the method to find manipulations that change the orientation of the cube.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Environments", "weight": 1.0} -->

PandaHook The environment contains a single Franka Emika Panda robotic arm, as provided, together with a cuboid and a hook. This environment enables more complex interaction where, for example, the robot can use the hook to reach and manipulate the cube. This environment motivates tool use and demonstrates sequential manipulation planning, where long horizon multi-step manipulations are needed.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Environments", "weight": 1.0} -->

PandasCube The environment contains two panda robot arms in a bi-manual setup with a cuboid. This environment encourages collaboration, like throwing the cuboid from one arm to the other.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

We evaluate our baselines and method on four different metrics intended to capture the quantity and diversity of the resulting data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

Path Count The total number of diverse paths returned by our method.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

Coverage The percentage of stable states sampled at the initial stage, which were reached by at least one node.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

Entropy The entropy of the states visited by the paths, calculated using the Kozachenko--Leonenko estimator. This estimator approximates the entropy based on the distance of the $k$-th nearest neighbor. We sample $100$ states^22^2We use a fixed number of states, since the KL-estimator depends on it and the number of visited states varies by multiple orders of magnitude between the methods we compare. from all visited states and calculate the entropy using $k = 10$. We repeat this process $10$ times and report the average.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

Average Hausdorff The average pairwise (undirected) Hausdorff distance between paths with the same stable state as the endpoint, averaged over all stable end states with at least two paths connecting to it.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Evaluation Metrics", "weight": 1.0} -->

For evaluation, we fix the set of stable states for each environment. We evaluate all baselines and ablations using $10$ randomly drawn starting states and average the results. We only report the entropy if the paths returned by the method add up to at least $100$ nodes, and we only report the average Hausdorff-distance if a stable state is reached by at least two paths.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Baselines", "weight": 1.0} -->

We compare our method against kinodynamic RRT through black-box simulation (RRT-sim) introduced in sec. II-B. We modify it by adding a bias towards sampling stable states with 20% probability, which corresponds to goal-bias in kinodynamic RRTs.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Baselines", "weight": 1.0} -->

Additionally, we evaluate the impact of our proposed extensions with ablations. For these, we take the number of selected actions $n \in {\{ 1,16\}}$ and the number of nearest neighbors $k \in {\{ 1,16\}}$. We also perform an ablation with only a 20% chance of sampling stable states, the rest of the samples being uniform. We give a budget of 2,500 tree expansions for the SpheresRamp and SpheresCube environments and a budget of 10,000 tree expansions for the PandaHook and PandasCube environments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C Baselines", "weight": 1.0} -->

Furthermore, we also consider as a baseline sampling-based MPC with predictive sampling. We rely on the implementation provided in Hydrax on the first (simplest) environment.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

Table I shows the results of our experiments. Our method performs the best in terms of coverage and paths found for all environments except PandasCube. We hypothesize that the improvement of StaGE w/o node rejection over StaGE is due to the high dimension of the action space (two $8$-DOF robotic arms). Since many actions (e.g. null-space movements or movements of the arm not in contact with the box) will not improve the state cost, it is reasonable to assume that the size of the set of actions improving our state is small. Therefore, even on a previously unsuccessful node, actions improving the distance can be sampled in subsequent iterations. Future work could investigate alternative sampling schemes for sampling actions, in order to improve their the chances of success. Fig. 4 more clearly shows the ability of our method to explore the space of feasible actions in the SpheresRamp environment compared to the RRT-sim baseline. Fig. 3 shows some examples of the trajectories found by StaGE.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

The results demonstrate that taking the $n$-best actions instead of only the best-performing one leads to the biggest improvement in performance. To further investigate the effects of this parameter and the $k$-nearest neighbor parameter we performed the ablations shown in Fig. 5. Additionally, we performed an ablation on the effects of the number of stable states sampled in the first stage of our method as shown in Table II. Notice that the coverage metric is highly dependent on the amount of stable states.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

Generating the trajectories on an AMD Ryzen 9 9900X CPU takes 4 seconds per trajectory for the SpheresRamp scenario, 1 minute per trajectory for SpheresCube, 8 minutes per trajectory on PandaHook, and 30 seconds per trajectory on PandasCube. Significant speedups are possible by parallelizing the simulation using a GPU, which is beyond the scope of this work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our method bears resemblance to the PRM paradigm in the sense that we also first sample points (stable configurations), which we then connect using local planners. However, PRMs usually aim to connect nearest neighbors or nodes within a certain distance. In comparison, we aim to find all possible paths since our focus is on diverse data instead of solving motion planning queries efficiently. Furthermore, for the considered problem, the construction of a PRM is not trivial. Indeed, in the case of manipulation, building a PRM would involve solving a two-point boundary value problem with non-differentiable dynamics. One could rely on gradient-free optimization. However, this can be costly and can fail in more complex environments.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

The action sampling step of the kino-dynamic RRT (and consequently, our method) can be seen as an iteration of predictive sampling to directly connect stable configuration pairs. It would be interesting to use multiple iterations or more sophisticated gradient-free techniques. However, this is beyond the scope of this paper.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we employed physically stable states to guide the search for diverse manipulations, motivated by the relative simplicity of generating such states. However, future research should explore extending the set of guidance states to include more generally informative states. For instance, states corresponding to moments of impact between the robot and an object could provide richer structural cues for exploration. Furthermore, improving the smoothness of the generated trajectories remains an important direction for future work.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduced StaGE, a novel method for diverse motion generation in complex non-prehensile manipulation scenarios. We demonstrated that our approach generalizes to a wide range of novel environments without requiring task-specific guidance, showing that pure exploration alone can yield long-horizon sequential manipulation behaviors. Even in the absence of motion priors, the method discovers highly complex skills such as throwing, grasping, pivoting, pushing, handovers, and tool use, relying solely on stable states as guidance.
