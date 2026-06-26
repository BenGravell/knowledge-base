<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Neural Informed RRT*: Learning-based Path Planning with Point Cloud State Representations under Admissible Ellipsoidal Constraints

Topics include Path planning, Robotics, Probabilistic models, Benchmarks, Sampling-based methods, Planning, Learning, Sampling, Sampling-based planning, Rapidly-exploring random tree, Point cloud.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based planning algorithms like Rapidly-exploring Random Tree (RRT) are versatile in solving path planning problems. RRT* offers asymptotic optimality but requires growing the tree uniformly over the free space, which leaves room for efficiency improvement. To accelerate convergence, rule-based informed approaches sample states in an admissible ellipsoidal subset of the space determined by the current path cost. Learning-based alternatives model the topology of the free space and infer the states close to the optimal path to guide planning. We propose Neural Informed RRT* to combine the strengths from both sides. We define point cloud representations of free states. We perform Neural Focus, which constrains the point cloud within the admissible ellipsoidal subset from Informed RRT*, and feeds into PointNet++ for refined guidance state inference. In addition, we introduce Neural Connect to build connectivity of the guidance state set and further boost performance in challenging planning problems. Our method surpasses previous works in path planning benchmarks while preserving probabilistic completeness and asymptotic optimality. We deploy our method on a mobile robot and demonstrate real world navigation around static obstacles and dynamic humans. Code is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path planning is the task of finding a path for a robot to traverse from a start to a goal safely and efficiently. An effective path planning algorithm should be complete and optimal: a solution is guaranteed to be found if one exists, and the optimal solution is guaranteed to be achieved with sufficient run time; efficient in optimal convergence: the solution should be quickly improved towards near optimal; and versatile and scalable: the implementation should be modified with minimal effort to generalize across different problems, environments, and robots.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multiple branches of planning algorithms have been developed to meet these requirements, including grid-based search, artificial potential field, and sampling-based algorithms. Sampling-based algorithms are popular due to their versatility, scalability, and formal properties of probabilistic completeness and asymptotic optimality. To accelerate convergence to the optimal path, various sampling strategies are introduced to replace the default uniform sampling. The rule-based informed strategy enforces sampling in an admissible ellipsoidal subset of states which are more promising to improve the current path solution. The learning-based methods harness grid-based neural networks to make inference of states close to the optimal path, and bias sampling towards these states, which we define as guidance states.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While these works improve performance, we observe three limitations. First, learning-based methods encode whole state space to generate guidance states without iterative improvement, where inference speed and accuracy are affected by modeling features of irrelevant region or obstacles. Second, rule-based informed sampling does not favor topologically critical states in the ellipsoidal subset (e.g., narrow corridors). Finally, learning-based methods do not consider connectivity of the guidance state set, which severely affects the convergence rate in complex planning problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Neural Informed RRT\* (NIRRT\*) to address these limitations (Figure 1). We represent free states with a point cloud, and apply PointNet++ to classify guidance states. Sampling from the guidance states is mixed with the random sampling step of Informed RRT\* (IRRT\*). Using a point cloud instead of an occupancy grid allows us to perform Neural Focus: constraining the point clouds by the admissible ellipsoidal subset of the free space, from which the critical states are inferred by PointNet++. The quality of the guidance states is continually improved during iteration, because the inference is always made on the informed subset created by an improved path cost. In addition, we build connectivity of the guidance state set by following a Neural Connect scheme similar to RRT-Connect, where the point-based network is called to solve a subproblem with a closer pair of start and goal states.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, our contributions are threefold: we use a Point-based Network (PointNet++) to directly take free states as point cloud input to generate multiple guidance states in one run; we present Neural Informed RRT\*, by introducing Neural Focus to integrate Point-based Network and Informed RRT\*; and we propose Neural Connect to address the connectivity issue of inferred guidance state set.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Problem Definition", "weight": 1.0} -->

We define the optimal path planning problem similar to related works. The state space is denoted as $X \subseteq {\mathbb{R}}^{d}$. The obstacle space and the free space are denoted as $X_{\text{obs}}$ and $X_{\text{free}}$. A path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow X_{\text{free}}}$ is a sequence of states. The set of paths is denoted as $\Sigma$. The optimal path planning problem is to find a path $\sigma^{*}$ which minimizes a given cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, connects a given start state $x_{\text{start}} \in X_{\text{free}}$ and a given goal state $x_{goal} \in X_{\text{free}}$, and has all states on the path in free space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-B Neural Informed RRT\\*", "weight": 1.0} -->

We present NIRRT\* in Algorithm 1, where the unhighlighted part is from RRT\*, the blue part is from IRRT\*, and the red part is our contribution. We track the best path solution cost $c_{\text{best}}^{i}$ through each iteration, which is initialized as infinity (line 3). We initialize update cost $c_{\text{update}}$ with the value of $c_{\text{best}}^{0}$ (line 4). We call the neural network to infer an initial guidance state set $X_{\text{guide}}$ based on the complete free state space (line 5). As better solutions are found, the guidance state set $X_{\text{guide}}$ may be updated by the neural network calls depending on how much the path cost has been improved, and random samples $x_{\text{rand}}$ are sampled using both $X_{\text{guide}}$ and informed sampling (line 8).

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Neural Informed RRT\\*", "weight": 1.0} -->

5:Xguide ← 𝙿𝚘𝚒𝚗𝚝𝙽𝚎𝚝𝙶𝚞𝚒𝚍𝚎(xstart, xgoal, cbest0, Xfree); 7: cbesti ← minxsoln ∈ Xsoln{𝙲𝚘𝚜𝚝(xsoln)}; 8: xrand, Xguide, cupdate ← 𝙿𝚘𝚒𝚗𝚝𝙽𝚎𝚝𝙶𝚞𝚒𝚍𝚎𝚍𝚂𝚊𝚖𝚙𝚕𝚒𝚗𝚐 (Xguide, xstart, xgoal, cupdate, cbesti, Xfree); 10: xnew ← 𝚂𝚝𝚎𝚎𝚛(xnearest, xrand); 11: if 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎(xnearest, xnew) then 12: Xnear ← 𝙽𝚎𝚊𝚛(G = (V, E), xnew, rRRT*); 15: cmin ← 𝙲𝚘𝚜𝚝(xnearest) + c(𝙻𝚒𝚗𝚎(xnearest, xnew)); 16: for all xnear ∈ Xnear do 17: if ​𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎(xnear, xnew) ∧ 𝙲𝚘𝚜𝚝(xnear) +c(𝙻𝚒𝚗𝚎(xnear, xnew)) < cmin then 19: cmin ← 𝙲𝚘𝚜𝚝(xnear) + c(𝙻𝚒𝚗𝚎(xnear, xnew)); 23: for all xnear ∈ Xnear do 24: if

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Neural Informed RRT\\*", "weight": 1.0} -->

𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎(xnew, xnear) ∧ 𝙲𝚘𝚜𝚝(xnew) +c(𝙻𝚒𝚗𝚎(xnew, xnear)) < 𝙲𝚘𝚜𝚝(xnear) then 26: E ← (E ∖ {(xparent, xnear)}) ∪ {(xnew, xnear)}; 30: Xsoln ← Xsoln ∪ {xnew}; Algorithm 1 Neural Informed RRT* 1:if ccurr < αcupdate then 2: Xguide ← 𝙿𝚘𝚒𝚗𝚝𝙽𝚎𝚝𝙶𝚞𝚒𝚍𝚎(xstart, xgoal, ccurr, Xfree); 7: xrand ← 𝙸𝚗𝚏𝚘𝚛𝚖𝚎𝚍𝚂𝚊𝚖𝚙𝚕𝚒𝚗𝚐(xstart, xgoal, ccurr); 14:return xrand, Xguide, cupdate; Algorithm 2 𝙿𝚘𝚒𝚗𝚝𝙽𝚎𝚝𝙶𝚞𝚒𝚍𝚎𝚍𝚂𝚊𝚖𝚙𝚕𝚒𝚗𝚐(Xguide, xstart, xgoal, cupdate, ccurr, Xfree) PointNetGuidedSampling: When the current best path cost $c_{\text{curr}}$ is less than the path cost improvement ratio $\alpha \leq 1$ of $c_{\text{update}}$, the neural network is called to update

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Neural Informed RRT\\*", "weight": 1.0} -->

The random sample $x_{\text{rand}}$ is sampled with a mixed strategy: if a random number $\text{Rand} \in {}$ is smaller than 0.5, we use the sampling strategy of IRRT\* to sample $x_{\text{rand}}$; otherwise, we sample $x_{\text{rand}}$ uniformly from $X_{\text{guide}}$. Similar to, our mixed sampling strategy guarantees probabilistic completeness and asymptotic optimality by implementing the sampling procedure of IRRT\* with a non-zero probability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Neural Informed RRT\\*", "weight": 1.0} -->

Note the frequency of calling neural networks for guidance state inference is controlled by the path cost improvement ratio $\alpha$. If we do not update $X_{\text{guide}}$ after initial inference, and remove IRRT\* components, NIRRT\* is reduced to NRRT\*. While NIRRT\* is generic in that any neural network that infers guidance states can fit into the framework, we emphasize the use of a point-based network. In the next subsection, we discuss the details of Point-based Network Guidance (PNG), and explain the preference of point representations over grid representations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

Point-based Network. We represent the state space by a point cloud $X_{\text{input}} = {\{ x_{1},x_{2},\ldots,x_{N}\}} \subset X_{\text{free}}$. The density of point cloud should allow a reasonable amount of neighbors around each point in radius of step size $\eta$. We oversample points uniformly from $X_{\text{free}}$, and perform minimum distance downsampling to obtain the point cloud with even distribution. We create a one-hot vector for each point, indicating whether the point is within radius $\eta$ of $x_{\text{start}}$ or $x_{\text{goal}}$. We concatenate the one-hot vectors with normalized point coordinates to generate point cloud representations of the free states. The processed point cloud ${\overline{X}}_{\text{input}}$ is fed into a point-based network $f$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

The network $f$ maps each point to a probability $p_{i} \in {\lbrack 0,1\rbrack}$, where the points with probability greater than 0.5 form the set of guidance states $X_{\text{guide}}$. Formally, We implement PointNet++ as the model architecture of the point-based network. Since PointNet++ is originally designed for 3D point cloud, we set $z$ coordinates as zero for 2D problems. We collect 4,000 2D random worlds as the training dataset. For each random world, we run A\* in pixel space with step size of unit pixel and clearance of 3 pixels to generate the pixel-wise optimal path. We generate a point cloud of number $N = 2048$, and generate guidance state labels by checking whether each point is around any point of the pixel-wise optimal path in radius of $\eta$, which is set as 10 pixels. We train PointNet++ by Adam optimizer with an initial learning rate of 0.001 and batch size of 16 for 100 epochs. We use the trained model across all types of 2D planning problems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

For 3D random world problems, we follow a similar scheme, but the clearance is set as 2 voxels.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

Neural Focus. Informed RRT\* outperforms RRT\* by proposing a heuristic ellipsoidal subset of the planning domain $X_{\text{focus}}$ in terms of the current best solution cost $c_{\text{curr}}$, in order to sample $x_{\text{rand}}$ which is more likely to improve the current solution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

The reasoning behind this sampling strategy is that for any state $x_{\text{rejected}}$ from $X\backslash X_{\text{focus}}$, the minimum cost of a feasible path from $x_{\text{start}}$ to $x_{\text{goal}}$ through $x_{\text{rejected}}$ is greater than $c_{\text{curr}}$: Neural Focus is to constrain the point cloud input to the point-based network inside the $X_{\text{focus}}$, which is equivalent as changing the domain of oversampling from $X_{\text{free}}$ to $X_{\text{focus}} \cap X_{\text{free}}$. Since we normalize point coordinates when processing point cloud inputs, the trained point-based network can handle point clouds sampled from domains at different scales. With the same number of points $N$, a smaller volume of $X_{\text{focus}}$ leads to a denser point cloud, which describes important regions with finer details.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

For example, Figure 3(b) shows that Neural Focus fills the narrow passage with a large number of points, which is captured by the point-based network to produce more effective inference on guidance states compared to Figure 3(a).

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

Neural Connect. The points close to $x_{\text{start}}$ or $x_{\text{goal}}$ are usually classified as guidance states with greater probabilities than the points around midway of the path (e.g., Figure 3(d)). When the distance between $x_{\text{start}}$ and $x_{\text{goal}}$ gets longer, the guidance state set $X_{\text{guide}}$ is more likely to be separated into disconnected "blobs". This phenomenon of probability polarization is reported in NRRT\* work. Our experiments show lack of connectivity limits the performance in large and complex planning problems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

We address this issue by introducing Neural Connect, which is inspired by RRT-Connect. We initialize $X_{\text{guide}}$ as an empty set, $x_{\text{start}}^{1}$ as $x_{\text{start}}$, and $x_{\text{goal}}^{1}$ as $x_{\text{goal}}$. During iteration, we first call the point-based network with $x_{\text{start}}^{i}$ and $x_{\text{goal}}^{i}$ as start and goal, and add inferred guidance states to $X_{\text{guide}}$. Second, We run Breadth First Search (BFS) from $x_{\text{start}}$ to $x_{\text{goal}}$ through the guidance states in $X_{\text{guide}}$. The neighbor radius of BFS is set as $\eta$, and no collision check is performed.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

After BFS is finished, connectivity of $X_{\text{guide}}$ is confirmed if $x_{\text{goal}}$ is reached. Otherwise, we find the boundary points $X_{\text{bound}}$ of the states visited by BFS by checking whether any points in $X_{\text{input}}\backslash X_{\text{guide}}$ are around the visited state of radius $\eta/2$. We select $x_{\text{start}}^{i + 1}$ from $X_{\text{bound}}$ which is one of the states heuristically the furthest from $x_{\text{start}}$ and one of the states to reach $x_{\text{goal}}$ with minimum total heuristic cost. Third, we perform the same operation as the second step, with the start of BFS as $x_{\text{goal}}$, and the goal of BFS as $x_{\text{start}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

We obtain $x_{\text{goal}}^{i + 1}$ if connectivity is negative. We perform the iteration until connectivity is built or the limit of iteration $n_{\text{guide}}$ is reached, which we set as 5 in practice. We illustrate Neural Connect in Figure 3(c-h). Note the orange path found by BFS in Figure 3(h) does not go through collision check, so the path is not a feasible solution but a visual demonstration on the connectivity of $X_{\text{guide}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

PointNetGuide: We apply both Neural Focus and Neural Connect to the point-based network, and obtain the complete module of Point-based Network Guidance, which is presented in Algorithm 3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

connectivity, xgoalj + 1 ← 𝙱𝙵𝚂(Xguide, xgoal, xstart, η); Algorithm 3 𝙿𝚘𝚒𝚗𝚝𝙽𝚎𝚝𝙶𝚞𝚒𝚍𝚎(xstart, xgoal, ccurr, Xfree) Point versus Grid.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Point-based Network Guidance", "weight": 1.0} -->

We prefer using points over grids to represent state space due to compatibility with geometric constraints and convenience of extension to different problems. To apply Neural Focus to a CNN, grid representations require masking of the complement set of the ellipsoidal subset, where the mask quality depends on grid resolution. CNN also has to process the irrelevant masked region within the rectangular/box grid input. In contrast, point representations naturally confine states within arbitrary geometry by modifying the sampling domain, and the point-based network only needs to model free states. Moreover, while the point-based network just needs adjustment of the input format to extend to different dimensions, changing input dimensions usually requires redesign of CNN architecture.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

Planning Problems. We conduct simulation experiments on 2D center block, 2D narrow passage, 2D random world, and 3D random world problems. The center block and the narrow passage problems are defined similar to IRRT\* work (Figure 4). The center block problem examines the efficiency of planners to sample states relevant to the problem in a wide free space. The narrow passage problem studies the capability of planners to focus sampling in topologically critical area. The random world problems evaluate versatility and scalability of planners.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

In the center block problems, we specify 5 different map sizes with respect to a fixed start-goal distance, and set the block width randomly for 100 independent runs. In the narrow passage problems, we specify 5 different gap heights, and set random positions of the passage for 100 independent runs. We generate 500 random worlds for each 2D and 3D cases for evaluation. Note we use clearance of 3 pixels for 2D random world, zero clearance for 2D center block and 2D narrow passage, and 2 voxels for 3D random world. The default size of 2D planning problems is $224 \times 224$, and the default size of 3D planning problems is $50 \times 50 \times 50$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

Metrics. For the center block problems, we measure the number of iterations to reach within a path cost threshold, which is some percentage above the optimal cost. For the narrow passage problems, we measure the number of iterations to find a path through the passage. For the random world problems, we examine the iterations each planner spends on finding the initial solution, and path cost improvement after certain numbers of iterations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

Baselines. We compare NIRRT\* to RRT\*, IRRT\*, NRRT\*-GNG, and variants of our method across the experiments. NIRRT\*-PNG(FC) is our complete algorithm, where F is Neural Focus and C is Neural Connect. NIRRT\*-PNG(F) removes Neural Connect from the complete version. NRRT\*-PNG is Neural RRT\* with the point-based network. NRRT\*-PNG(C) uses Neural Connect in addition to NRRT\*-PNG. We train a U-Net with pretrained weights for NRRT\*-GNG for 2D problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

Experiment Results. The center block experiments show in Figure 5(b) that NIRRT\*-PNG(FC) outperforms IRRT\* in terms of the speed to find near-optimal paths across different problem sizes. The point-based network is able to infer guidance states from the informed subset which are the most promising to converge the path solution to optimum. Both Figure 5(a)(c) show that NIRRT\*-PNG(FC) and NIRRT\*-PNG(F) have similar performance. The informed subset effectively constrains the region of the point cloud to be around the center block, and significantly simplifies the task of guidance state inference. Therefore, the point-based network performs well even without Neural Connect. Similar to the claim by that initial path solution cost of NRRT\* is better than RRT\*, we see in Figure 5(c) that NRRT\*-PNG and NRRT\*-PNG(C) are faster than RRT\* in terms of reaching within a more relaxed threshold above optimal cost such as 7-10%.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

However, the convergence speeds of NRRT\* variants tend to be slow and are often worse than RRT\* when approaching a tighter bound such as 2-4%. In contrast, NIRRT\* variants work consistently better than IRRT\* across thresholds of optimal cost, since the informed subset allows the point-based network to provide finer distribution of the guidance states to continuously refine the path towards the optimal solution.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

In the narrow passage setting, NIRRT\*-PNG(FC) finds a difficult path through the passage faster and more frequently than IRRT\*, as represented in Figure 5(f). The convergence speed of NIRRT\*-PNG(FC) outperforms all baselines as shown in Figure 5(e). NIRRT\*-PNG(F) performance is similar to IRRT\* because the guidance state set usually ends up separated on left and right sides of the gap without Neural Connect, whereas NIRRT\*-PNG(FC) is able to connect the guidance state set together through the gap, which helps sampling critical states inside the gap. Both NRRT\*-GNG and NRRT\*-PNG are worse than RRT\*, but NRRT\*-PNG(C) works consistently better than RRT\*, which indicates the effectiveness of Neural Connect in planning problems with critical states. Note we collect the training dataset for point-based network with optimal paths which requires clearance of 3 pixels, which is equivalent to 7 pixels of the gap height.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

Figure 5(e) demonstrates that our point-based network generalizes well to planning problems with clearances tighter than training distribution by Neural Focus and Neural Connect, while the CNN model is sensitive to clearance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Simulation Experiments", "weight": 1.0} -->

For each random world problem, we record the cost of path solution at certain number of iterations after the initial solution is found, and plot these costs relative to the cost of the initial path solution from RRT\*. The 2D and 3D results are presented in Figure 5(g) and (d) respectively, and planning in 3D random worlds are visualized in Figure 6. We observe NRRT\*-GNG has the best initial solution in 2D since the grid representations are denser than point representations in terms of the whole state space. However, NIRRT\* variants converge faster due to continuous improvement of the guidance states. We find that both Neural Connect and Neural Focus contribute to improvement of convergence speed in both 2D and 3D cases. Figure 5(h) shows that NIRRT\*-PNG(FC) is faster than IRRT\* in terms of finding initial path solution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Real World Deployment", "weight": 1.0} -->

We deploy our method and the model trained in 2D random world to a TurtleBot 2i. The demonstration of real world navigation with static obstacles and dynamic humans is available at

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We present Neural Informed RRT\* approach to accelerate optimal path planning by incorporating a point-based network into Informed RRT\* for guidance state inference. We introduce Neural Focus to naturally bridge the point-based network and the informed sampling strategy with point cloud representations of free states. We propose Neural Connect to improve quality of the inferred guidance state set by enforcing connectivity. Our simulation experiments show that Neural Informed RRT\* outperforms RRT\*, Informed RRT\*, and Neural RRT\* in terms of convergence rate towards optimal solutions in planning problems with varying sizes, critical states, and randomized complicated patterns.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In future work, we want to study how to further improve our algorithm when the planning problem sizes are significantly different from the training distribution. We would like to explore the effectiveness of our work in higher-dimensional problems. It is also interesting to study if we can denoise the guidance state set inferred by the point-based network to offer an end-to-end option for generating feasible and near-optimal paths.
