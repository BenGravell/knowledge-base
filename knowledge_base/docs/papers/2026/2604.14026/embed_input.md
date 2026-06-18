<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning for Object Extraction

Topics include Bandits, Motion planning, Sampling-based methods, Planning, Sampling, MAB-RRT, Principal component analysis.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Object extraction tasks often occur in disassembly problems, where bolts, screws, or pins have to be removed from tight, narrow spaces. In such problems, the distance to the environment is often on the millimeter scale. Sampling-based planners can solve such problems and provide completeness guarantees. However, sampling becomes a bottleneck, since almost all motions will result in collisions with the environment. To overcome this problem, we propose a novel scale-invariant sampling strategy which explores the configuration space using a grow-shrink search to find useful, high-entropy sampling scales. Once a useful sampling scale has been found, our framework exploits this scale by using a principal components analysis (PCA) to find useful directions for object extraction. We embed this sampler into a multi-arm bandit rapidly-exploring random tree (MAB-RRT) planner and test it on eight challenging 3D object extraction scenarios, involving bolts, gears, rods, pins, and sockets. To evaluate our framework, we compare it with classical sampling strategies like uniform sampling, obstacle-based sampling, and narrow-passage sampling, and with modern strategies like mate vectors, physics-based planning, and disassembly breadth first search.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our experiments show that scale-invariant sampling improves success rate by one order of magnitude on 7 out of 8 scenarios. This demonstrates that scale-invariant sampling is an important concept for general purpose object extraction in disassembly tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Removing an object out of a tight, narrow passage is a fundamental skill for robot disassembly tasks in recycling \[asif2024robotic\], repair \[parker1998robotics\], and remanufacturing \[laili2022optimisation, das2025towards\]. Sampling-based methods \[Orthey2023AnnualReview\] can tackle such problems and provide completeness guarantees \[zickler2009efficient, aguinaga2008targetless, Ebinger2018MateVecTRRT, tian2022assemble\]. However, due to narrow passages, such problems often become intractable to solve \[Ebinger2018MateVecTRRT\]. This is often due to the large scale on which methods like rapidly exploring random tree (RRT) \[Kuffner2000\] operate, where motions out of narrow passages are almost always invalid.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To tackle this problem, we propose a novel scale-invariant sampling strategy. This strategy is based on the observation that scale is an important consideration for motion planning of object extraction tasks. For example, if a point robot is inside a narrow passage, and you sample points inside a large radius around it, then almost all of the points will be unreachable (the robot just bumps into the wall). In contrast, if we sample in an infinitesimal small radius, then almost all samples will be reachable. Those two scales have, however, a low information entropy \[jaynes2003probability\] and do not help a planner to make good decisions. What this implies, however, is that there is a scale, at which the information entropy is high, meaning samples are maximally useful for planning. Such a scale corresponds to situations where roughly half of the samples become reachable \[jaynes2003probability\]. This scale would not only have a high information entropy, but it would be an exceptional guidance to the planner.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To implement this insight, we devise two sampling strategies. One is a scale sampler, which explores different scales to find a high information entropy scale. The other is a principal component analysis (PCA) sampler, which exploits the principal components in the samples at the previously computed high information entropy scale. Both of those samplers are integrated into a multi-arm bandit RRT (MAB-RRT) \[faroni2023motion\]. An overview about this framework is shown in Fig. 1. We found scale-invariant sampling in MAB-RRT to be an effective planning strategy for disassembly tasks where bolts, pins, or gears have to be removed from a narrow passage.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a novel scale sampler which can autonomously find high information entropy scales for efficient sampling densities.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a PCA sampler to exploit a given high information entropy scale by biasing samples along a positive or negative principal component direction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Embedding both samplers into the MAB-RRT planner to combine it with other sampling strategies like uniform sampling.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide an implementation of samplers and MAB-RRT as an extension of the Open Motion Planning Library (OMPL) and provide a set of demos scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Eventually, this sampling strategy is tested against other classical sampling methods on eight challenging 3D scenarios involving realistic object extraction tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

Object extraction is the task of separating two objects until the distance between them reaches a predefined threshold. Our interest is in tasks where the objects have to move along tight, narrow passages to achieve separation, a task which is often encountered in disassembly problems \[tian2022assemble\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

A main focus of research in this area is on fastener removal. For example, detecting screw types and using the correct tool for screw extraction \[zhang2023automatic\] or learning policies for single object extraction tasks with a robot manipulator \[serrano2023learning\]. Specialized systems exists for specific screw types like hexagonal screws \[li2020unfastening\]. Our work is complementary in that we tackle arbitrary objects, including bolts, nuts, or gears, for which a removal plan has first to be computed to achieve a separation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

Apart from fastener removal, research has also focused on cluttered extraction. This includes extracting boxes from piles without other boxes collapsing \[pathak2025collapse\], or carefully extracting objects from a pile without disturbing the other objects \[Motoda2023\].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

For object extraction in disassemblies, specialized planners have been developed. For example, the Targetless-RRT \[aguinaga2008targetless\] explores the space without a specified goal region, but instead tries to minimize its distance to a predefined exterior space which represents a disassembled state. This idea has later been combined with mating vectors in the Mating Vector and Targetless-RRT (MateVec-TRRT) \[Ebinger2018MateVecTRRT, tian2022assemble\]. MateVec-TRRT uses the concept of mating vectors, which are vectors which point into the direction of a separation between two objects. This is particularly advantageous when two objects are close by and just have to be pulled apart \[Ebinger2018MateVecTRRT\]. Another approach is to use physics-based separation vectors \[tian2022assemble, zickler2009efficient\]. This idea is based on the observation that nuts and bolts can be moved by an approximate force which has a component into the motion direction \[tian2022assemble\].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

This avoids costly computation of the exact motion direction. This can then be implemented in a planner like the Behavioral Kinodynamic Rapidly-Exploring Random Trees (BK-RRT) \[zickler2009efficient\], where the random physical forces are used as forward propagations to reach new states. A more dedicated planner is the disassembly breadth first search (BFS) \[tian2022assemble\], which uses physics-based force directions in combination with a breadth first search and state similarity checks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Object Extraction", "weight": 1.0} -->

Our work extends approaches like MateVec-TRRT \[Ebinger2018MateVecTRRT\], BK-RRT \[zickler2009efficient\], and BFS \[tian2022assemble\] in that we focus on general removal tasks in disassembly scenarios, where we add the concept of scale-invariant sampling to ensure that we progress along long elongated narrow passages. Additionally, instead of using a possibly costly physical simulation \[tian2022assemble\], we use purely geometrical arguments to find the direction of motion.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Biased Sampling", "weight": 1.0} -->

To circumnavigate narrow passages, most research has focused on biasing samples. Common approaches include Obstacle-based sampling \[Boor1999GaussianSampling\], where samples are biased towards obstacle boundaries, Bridge-based sampling \[Hsu2003BridgeTest\] where samples are biased towards narrow passages, Utility-based sampling \[burns2005toward\], where samples are drawn based upon their utility to improve the roadmap, and Dynamic-domain RRT \[yershova2005dynamic\], where the Voronoi bias of samples is adjusted based on their performance. Sample biases can also be learned from similar situations \[ichter2018learning, chamzas2021learning\] to improve sampling quality. Once paths are found, biasing can be used to improve the path quality by using informed sampling \[gammell2014informed\], where an admissible ellipsoid heuristic is used in RRT\* \[karaman2011sampling\] to bias samples towards paths with lower cost.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Biased Sampling", "weight": 1.0} -->

More recent approaches focus on selective densification \[huang2025selective\], where sparse regions are identified, and their resolution is changed so that more samples are produced in narrow passages. Our approach differs by concentrating on object extraction tasks while carefully finding trade-offs between uniform and scale-invariant sampling.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Biased Sampling", "weight": 1.0} -->

This trade-off is similar to the exploration/exploitation trade-off \[rickert2014balancing\], where an exploration step finds locally free configuration space regions, while an exploitation step uses this region to quickly find valid paths. We follow a similar approach, but see exploration as a search for high information entropy samples, while exploitation as the biasing operation along the high-information entropy samples.

<!-- chunk {"id": "body-0021", "role": "body", "section": "PCA-based sampling", "weight": 1.0} -->

A widely used sampling analysis tool in motion planning is Principal component analysis (PCA) \[pearson1901liii, jolliffe2011principal\]. PCA can extract a principal component from a set of samples, thereby showing a direction in which the samples are distributed. This is particularly useful to find directions to sample inside narrow passages.

<!-- chunk {"id": "body-0022", "role": "body", "section": "PCA-based sampling", "weight": 1.0} -->

One way to leverage PCA is to detect if samples are currently inside a narrow passage. For example, ADD-RRT \[cai2022add\] uses PCA to identify nodes which are likely in a narrow passages, and changes the sampling strategy accordingly in the immediate neighborhood. If regions of interests are available, like in manipulation tasks, PCA can be used to ensure sampling is better distributed in those regions \[rosell2013path\]. Another application of PCA in this context is to reduce the conformal states for protein folding \[teodoro2003understanding\] thereby reducing the effective dimensions of the problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "PCA-based sampling", "weight": 1.0} -->

PCA can also be used globally to shape the sampling distributions around an existing configuration. The pioneering work by Dalibard et al. \[dalibard2009control, dalibard2011linear\] uses PCA to locally adjust the sampling radius around a node proportional to the Eigenvalues along each principal component. To make this more efficient, later work \[lee2012sr\] used a bridge test \[Hsu2003BridgeTest\] to identify narrow passages before running PCA on the samples. This reduces the calls to PCA to relevant regions of the configuration space. For dynamical systems, PCA can also be used to learn the bias stemming from the dynamics \[li2010balancing\] to make sampling more efficient.

<!-- chunk {"id": "body-0024", "role": "body", "section": "PCA-based sampling", "weight": 1.0} -->

Our work differs in that we do not consider PCA as a global tool for efficient sampling \[dalibard2011linear\], but instead leverage PCA as a local object extraction tool to exploit samples at high information entropy scales.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Multi-Arm Bandit", "weight": 1.0} -->

While novel sampling methods are important to better explore the space, it is also important to decide when to use which sampling method. A convenient framework to make this decision is the multi-arm bandit (MAB) \[auer2002finite, bubeck2012regret, slivkins2019introduction\]. MABs have been used in motion planning for different purposes, for example to select the best path from a set of candidate paths \[koval2015robust\], to select from different grasp strategies \[eppner2017visual\], and to run multiple trees with different sampling strategies, then select the best performing tree \[Lai2022RRF\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-Arm Bandit", "weight": 1.0} -->

A major work in this area is the MAB-RRT \[faroni2023motion, faroni2024online\], which is an RRT \[Kuffner2000\] with a MAB replacing the uniform sampling strategy. In the original MAB-RRT \[faroni2023motion\], each arm is used to select a particular region of the state space to sample. However, MAB-RRT is a general purpose planner which can take as input any set of sampling strategies if the MAB is clearly defined. Our work is complementary in that we treat MABs, similar Faroni et al. \[faroni2023motion\], as our global decision framework. However, while we leverage MAB-RRT as our framework, we differ by tackling a different application (object extraction) while using different sampling strategies and reward functions in the MAB.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning", "weight": 1.0} -->

Input: start configuration q0
Parameters: initial radius r0; optimal validity rate interval [αmin, αmax]; shrink factor s; growth factor g; min radius rmin; batch size b, max steps S
Output: final radius r⋆, valid samples V
$\alpha\leftarrow\frac{|V_{\text{new}}|}{|\mathcal{Q}|}$
8 if α ∈ [αmin, αmax] then
11 else if α &lt; αmin then
Algorithm 1 Finding High Information Entropy Scale

<!-- chunk {"id": "body-0028", "role": "body", "section": "Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning", "weight": 1.0} -->

Input: Normalized PCA axis a0, direction d ∈ {0, 1}, cylinder height interval [hmin, hmax], extension δ, radius R
Output: sample configuration q
// Sample random height vector
// Sample random direction in (N-1)-dimensional ball
// Account for volume density
// Assemble vector to get final sample
Algorithm 2 Sample from PCA-Aligned Cylinder

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning", "weight": 1.0} -->

Input: Start state xstart, goal region Xgoal
Output: Path π or failure
// Principal escape direction
5 S ← {Uniform, PC-Positive (a,r⋆), PC-Negative (a,r⋆)}
7while Not Terminate do
// Cylinder extension from r⋆
// UCB arm selection
9 xsample ← Sample (s,hext)
10 xnear ← Nearest (T,xsample)
11 xnew ← Steer (xnear,xsample)
12 valid ← CollisionFree (xnear,xnew)
// Accumulate valid samples
20 return ExtractPath(T, xnew)
Algorithm 3 Scale-Invariant MAB-RRT

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning", "weight": 1.0} -->

We propose a new sampling scheme which consists of three interconnected methods: Scale sampling to find high information entropy scales, directional sampling to exploit those scales, and a multi-arm bandit planner to integrate those samplers with classical sampling strategies. Each method is further detailed below.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exploration: Finding High Information Entropy Scales", "weight": 1.0} -->

The scale sampler is an adaptive sampling strategy designed to identify radii at which sampling yields a high information content. In particular, it aims to find a sampling scale at which the fraction of valid samples lies within a given target interval. This interval specifies a desired range of validity rates that characterizes informative sampling scales.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Exploration: Finding High Information Entropy Scales", "weight": 1.0} -->

The algorithm is depicted in Alg. 1. At each iteration, the scale sampler draws a fixed-size batch of quasi-random samples from a sphere (see below) of the current radius and evaluates their validity (Line 3,4). Based on the observed validity rate, the radius is increased or decreased (Line 6--12). This process continues until a radius is found whose validity rate falls within the target interval (Line 6--7), or until a predefined computational budget of $S$ steps is exhausted. In that case, we check if the radius is smaller than the minimal radius, in which case we clip it (Line 14--15). Afterwards, the best radius so far is returned (Line 16).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Exploration: Finding High Information Entropy Scales", "weight": 1.0} -->

Importantly, the scale sampler does not attempt to compute an optimal radius. Instead, it performs a feasibility-driven search whose goal is to find any radius that yields informative samples under noisy evaluation with finite samples. Our method is thereby robust to stochastic variability in validity estimates and avoids the need for strong assumptions such as deterministic monotonicity of validity with respect to scale.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sphere Sampling", "weight": 1.0} -->

An important aspect of our algorithm is the sphere sampling scheme. When using uniform sampling, we often face clustering of points on the sphere, which negatively impacts the validity rate, which requires a more uniform coverage of samples. To achieve this, we employ a dual sampling scheme, where alternate between uniform sampling and a jittered Fibonacci lattice sampling scheme. The Fibonacci lattice provides low-discrepancy samples \[Niederreiter1992, lavalle2006planning\] which guarantee a better coverage that avoids clustering. Without jitter, the lattice would place samples at identical positions across radii, making coverage entirely dependent on the uniform component. This jitter is controlled by the parameter $p_{\text{fibo-jitter}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Exploitation: Principal Components Sampling", "weight": 1.0} -->

Once a high-information entropy radius has been found, our planner should exploit it. A common way to better understand the valid sample distribution at the chosen scale is to run a principal component analysis (PCA). A PCA is a linear transformation of the data onto a new coordinate system, such that the (first) principal component (or principal axis) captures the largest variation in the data \[bishop2006pattern\]. PCA is a staple of many scientific software packages, and can be implemented with tools like Eigen \[eigenweb\].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Exploitation: Principal Components Sampling", "weight": 1.0} -->

However, to exploit the principal component for biased sampling requires a dedicated sampler. One possibility is to create a hyper-cylinder from the principal component and sample around it. This is depicted in Alg. 2. Our algorithm proceeds in three stages. First, we sample a random height from the axis $a_{0}$ to obtain a vector $a$ (Line 1--2). Second, we create an $({N - 1})$-dimensional ball around $a$, which is orthogonal to $a$ itself. To achieve this, we first sample directly in an $({N - 1})$-dimensional ball by getting a random distance variable $u$ (Line 3) and a random direction $t$ (Line 4). We then compute the radius $p$ by accounting for the volume density of the ball in $N - 1$ dimensions (there is more density further out). We then take $p$ and use it to compute the final direction $b$ in the $N - 1$ ball. Third, we assemble the final sample by projecting $b$ into the null-space of $a$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Exploitation: Principal Components Sampling", "weight": 1.0} -->

This is achieved by getting an orthonormal basis $Q$ \[axler2024linear\] and projecting $b$ into it. The final result $a + {Q \cdot b}$ (Line 8) gives a uniform distributed sample inside the cylinder of radius $R$ around the principal component as desired.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Integration of Samplers into Multi-Arm Bandit RRT", "weight": 1.0} -->

To decide when to use which sampler and to integrate them with other sampling strategies, we utilize a geometric version of the multi-arm bandit RRT (MAB-RRT) \[faroni2023motion\]. The algorithm itself is depicted in Alg. 3. This planner is similar to RRT \[Kuffner2000\], but uses in each iteration a possibly different sampling function as decided by the multi-arm bandit framework. This algorithm gets as input a start state $x_{\text{start}}$, a goal region $X_{\text{goal}}$, and outputs a path $\pi$ or a failure. We start by searching for a useful (high-information entropy) scale (Line 1) using the grow-shrink algorithm (Alg. 1). The outcome is a radius $r^{\star}$ and valid nodes and edges $V$. The nodes and edges are added to the initial tree at $x_{\text{start}}$ (Line 2). PCA is then computed on $V$ to obtain the principal escape direction (Line 3).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Integration of Samplers into Multi-Arm Bandit RRT", "weight": 1.0} -->

Afterwards, we define the set of samplers (Line 4), which includes a uniform sampler and the two principal component samplers, one for the positive and one for the negative direction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Integration of Samplers into Multi-Arm Bandit RRT", "weight": 1.0} -->

After those initialization steps, we start the inner loop while a terminate condition is not met. At each iteration, a cylinder extension height $h_{\text{ext}}$ is computed from the current best radius $r^{\star}$, allowing the principal component samplers to sample beyond the initial scale (see below). This inner loop starts with the selection of one sampler using the sliding window UCB policy denoted below. The remainder of the loop continues as in the original RRT by sampling a state, computing the nearest tree node, steering from this node to the sampled configuration, and checking if the connection is valid. If the connection is valid, we add it to the tree. For principal component samples, three additional updates occur: the valid sample is accumulated, the principal escape direction is recomputed online from all accumulated valid samples (see Online Recalibration below), and $r^{\star}$ is updated if the sample was drawn at a radius exceeding the current best, where $r_{\text{sample}}$ denotes the radius at which the cylinder sampler generated the point (see Cylinder Extension below).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Integration of Samplers into Multi-Arm Bandit RRT", "weight": 1.0} -->

If both the connection is valid and the last added configuration belongs to the goal region, we extract the path from the tree through backward search and return it. If no solution has been found yet, we update the bandit rewards and restart the loop. If no solution has been found when the terminate condition becomes true, we end the loop and return a failure.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Multi-Arm Bandit Dynamics", "weight": 1.0} -->

The multi-arm bandit algorithm selects samplers upon the Upper Confidence Bound (UCB) algorithm while each arm is updated via a reward function computed from the validity of a sample.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Arm Selection", "weight": 1.0} -->

where $b \in B$ are the bandit arms, ${\hat{\mu}}_{b}$ is the empirical mean rewards, $n_{b}$ is the recent count of arm $b$, $\beta$ is the exploration coefficient balancing exploitation against exploration, and $n_{c}$ is the count of the last $N_{\text{sliding-window}}$ arm iterations. The window ensures that arm selection reflects recent performance, which is crucial in an object extraction task where the geometry changes as object parts separate. In practice, we scale uniform and sphere-based rewards by constants $c_{u}$ and $c_{s}$, which tune the trade-off between outward tree growth and narrow-passage exploration.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reward function", "weight": 1.0} -->

Rewards are computed with respect to the last pulled arm, and the resulting value is propagated to all bandits along the decision path. Uniform samples are rewarded proportionally to their distance from the origin, encouraging outward tree expansion. Scale invariant samples (Positive and negative principal component) are rewarded inversely to their distance, prioritizing informative moves in narrow passages and down-weighting redundant samples once free space is reached. Invalid samples yield zero reward. Since the sliding-window UCB policy guarantees that each arm is selected infinitely often, and the uniform arm is itself probabilistically complete, the overall planner retains probabilistic completeness.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Online Recalibration", "weight": 1.0} -->

During the planning loop, the principal component axis is not fixed to the initial estimate from the scale search. Each time a principal component sampler produces a valid sample, the principal component is recomputed. To prevent axis flipping due to the sign ambiguity of PCA, the new axis is checked for consistency with the previous axis via their dot product. This online recalibration allows the escape direction to adapt as the planner discovers more of the local geometry beyond the initial radius.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cylinder Extension and Radius Growth", "weight": 1.0} -->

The principal component samplers update their sampling region through an integrated growth mechanism. Instead of setting the cylinder height to $r^{\star}$, an extension height of $h_{\text{ext}} = {\delta \cdot r^{\star}}$ with $\delta \geq 0$ being the extension factor. With $\delta = 0$, no extension occurs and samples are drawn at exactly $r^{\star}$ along the axis. Each principal component sampler samples along its respective direction within the range $\lbrack r^{\star},{r^{\star} + h_{\text{ext}}}\rbrack$ from the origin along the axis. Importantly, $r^{\star}$ is not fixed after the scale search: whenever a valid principal component sample is generated at a radius exceeding the current $r^{\star}$, the radius is updated. Since $h_{\text{ext}}$ is recomputed from $r^{\star}$, the escape direction is further increased for subsequent iterations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Open Source Software Implementation", "weight": 1.0} -->

The samplers and the multi-arm bandit RRT have been implemented as an extension of the open motion planning library (OMPL) \[sucan2012the-open-motion-planning-library\]. This code is open source and available on Github^11^1Link: We added a MAB-RRT planner demo, which can run on arbitrary occupancy maps in 2D.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example: Tunnel Environment", "weight": 1.0} -->

To showcase scale-invariant sampling with MAB-RRT, we created three toy scenarios as shown in Fig. 2. Those three scenarios are tunnel environments, where a point robot has to move from the origin (green point) to a goal configuration (red point). The scenarios differ by the size of a tunnel obstacle (black bars), where two bars restrict the start configuration from above and below. The distance between the bars differ for each scenario (5 units, 10 units, and 15 units).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example: Tunnel Environment", "weight": 1.0} -->

For each scenario, we visualize different properties of scale-invariant sampling. First, we show the final burn-in radius (high information entropy), at which roughly half of the samples are valid and half invalid. Furthermore, we show the search trees and the way the samples have been obtained. This includes uniform sampling (blue), positive principal component (green), and negative principal component (magenta). It can be seen that the high information entropy radius gives a good insight into where to move in each scenario, which leads to an efficient exploration of the configuration space.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate our scale-invariant sampler on $8$ environments involving multiple tight narrow passage scenarios inspired by realistic disassembly problems. The eight environments are shown in Fig. 3 and represent a diverse set of disassembly tasks adopted from an existing dataset \[tian2022assemble\].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

All experiments were conducted on a laptop running Ubuntu 20.04.6 LTS with an Intel Core i7-5820K CPU (3.30GHz, 12 cores) and 32GB RAM. In each scenario, we compare MAB-RRT using scale-invariant sampling with six alternative sampling strategies. This includes two sets of planners. First a set of classical sampling strategies integrated into RRT \[Kuffner2000\], namely RRT + bridge sampling \[Hsu2003BridgeTest\], RRT + Gaussian sampling \[Boor1999GaussianSampling\], and RRT + obstacle-based sampling \[Amato1998ObstacleBased\].

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Second, a set of modern strategies, including mating vectors (MateVec-TRRT) \[Ebinger2018MateVecTRRT\], physical simulation using behavioral kinodynamic RRT (BK-RRT) \[zickler2009efficient, tian2022assemble\], and physical simulation using similarity checks and disassembly breadth first search (BFS) \[tian2022assemble\]. For each scenario, we run each planner for a total of $10$ runs with a timeout of $100$ seconds.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Hardware and Parameters", "weight": 1.0} -->

For MAB-RRT, we use the following parameter values. For scale-invariant sampling, we use a Fibonacci jitter $p_{\text{fibo-jitter}} = \frac{\pi}{8}$, initial radius $r_{0} = 1.0$, min radius $r_{\text{min}} = {1{e{- 6}}}$, max radius $r_{\text{max}} = 25.0$, batch size $b = 64$, growth factor $g = {\exp{({- 0.7})}}$, shrink factor $s = {\exp{(0.9)}}$, max steps $S = 50$, and validity rates $\alpha_{\text{min}} = 0.1$ and $\alpha_{\text{max}} = 0.5$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Hardware and Parameters", "weight": 1.0} -->

For the Multi-arm bandit, we use a sliding window of $N_{\text{sliding-window}} = 256$, an UCB exploration coefficient $\beta = \sqrt{2}$, and constants for the uniform rewards of $c_{u} = {1{e8}}$ and PCA samplers as $c_{s} = 5.0$. For the classical sampling strategies, we use the default parameters as specified in OMPL \[sucan2012the-open-motion-planning-library, moll2015benchmarking-motion-planning-algorithms\].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hardware and Parameters", "weight": 1.0} -->

To show the results, we plot the success rate from zero to one hundred percent over time in log scale, as shown in Fig. 4. It can be seen that MAB-RRT solves all eight scenarios with $100$% success rate, meaning that MAB-RRT found a solution in every single run. In the Socket environment, MAB-RRT reaches $100$ percent with over one order of magnitude (OoM) better runtime compared to the next best planners (RRT + Obstacle Sampling and RRT + Bridge Sampling). In the Eye Bolt scenario, MAB-RRT and BFS reach $100$ percent success rate, with MAB-RRT outperforming BFS by over 1 OoM. In the U-Bolt environment, only MAB-RRT reaches $100$ percent, while BFS only reaches $30$ percent success rate until the timeout. In Motor Flange, the situation is similar with MAB-RRT reaching $100$ percent and BFS reaching $30$ percent.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Hardware and Parameters", "weight": 1.0} -->

In Gear Reducer, only MAB-RRT reaches $100$ percent, while planners RRT + Gaussian Sampling reaches $50$ percent, RRT + Bridge Sampling reaches $40$ percent, and RRT + Obstacle Sampling reaches $20$ percent. In the T-Bolt and Ring Bolt scenarios, MAB-RRT is the only planner reaching $100$ percent, each time with a runtime below $10^{1}$, which is 1 OoM below timeout. Finally, in Cross-Pin Connector, MAB-RRT, MateVec-TRRT, and BK-RRT reach $100$, while BFS and RRT + Obstacle Sampling reach $70$, RRT + Gaussian Sampling reaches $40$, and RRT + Bridge Sampling reaches $30$ percent. Again MAB-RRT outperforms the next best planner (BK-RRT) by 1 OoM. In terms of runtime, MAB-RRT outperforms the next best planner or the timeout by at least 1 OoM on seven out of eight scenarios, with the exception of the U-Bolt scenario.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Multi-Arm Bandit Dynamics", "weight": 1.0} -->

To verify that the multi-arm bandit correctly changes between arms over time, we run it on the T-Bolt experiment from Fig. 3. We plot both the UCB scores over time and the cumulative rewards per arm. This is depicted in Fig. 6. We can see that the cumulative rewards stays zero for uniform sampling, capturing the fact that uniform samples lead to direct collision. The reward for PCA positive is growing over time which reflects the fact that the robot can escape into only one direction from the tunnel. Once the robot has escaped (around iteration 85), there is a sharp uptick in reward for the uniform sampler, which reflects the growing of the tree into the open, free space.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Multi-Arm Bandit Dynamics", "weight": 1.0} -->

The UCB scores closely follow this trend. In the beginning, there is a sharp decrease in UCB score for uniform sampling, reflecting the invalidity of the samples. Over time, the UCB scores for uniform and PCA negative tend towards similar values ($\sim 1.0$--2.0), so that uniform samples are still occasionally tried to verify that the tree has not yet reached the open space. Finally, at iteration 85, the UCB score has a sharp increase reflecting the switch to the uniform sampling scheme.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Robustness of Scale-Invariant Sampling", "weight": 1.0} -->

Another important aspect of our framework is the grow-shrink algorithm to find a useful high-information entropy scale. In this section, we like to show that this algorithm is robust against different initial radii. For this, we created three environments as depicted in Fig. 5. Each row shows one environment, whereby the left image shows a starting radius of $1{e{- 6}}$ and the right image shows an initial radius of 25. For each scenario, we showcase the initial radius (violet circle) and the final radius after applying grow-shrink (orange circle). It can be seen that both initial radii faithfully converge to a similar radius at which roughly half of the samples are reachable. We also showcase the resulting trees with start (light green) and goal (red), where we show valid samples from uniform sampling (blue), samples from the principal component sampler with positive (green) and negative (magenta) direction, and initial samples from grow-shrink (light green).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We presented scale-invariant sampling, a novel sampling strategy for object extraction from tight, narrow passages. Our sampling strategy is based upon two methods. First, we explore the local space around an object's start position to find a scale where the information entropy is largest. This scale is maximally useful to find valuable samples. By using a grow-shrink method, we can robustly and quickly find such a scale. Second, we exploit the computed scale by leveraging the principal direction in the data, thereby finding a sampling bias which is helpful to robustly extract objects by finding the right directions inside a narrow passage. Finally, the samplers are integrated into a multi-arm bandit RRT (MAB-RRT) \[faroni2023motion\] which switches between different sampling strategies depending on the rewards obtained.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

The results show that scale-invariant MAB-RRT can successfully solve complex disassembly tasks. This involves sockets, gears, multiple bolt types, and connector pins. In our experiments, scale-invariant MAB-RRT outperforms similar biased sampling approaches and is the only planner which can reach a 100% success rate on all scenarios.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

While the results are promising, there are still some open questions. First, while PCA could be used for arbitrary spaces and objects, we have not yet demonstrated this. It would be important to verify that this works also on challenging scenarios where objects have to be rotated (e.g. screws, keys), where longer narrow passages are present (e.g. pipes, rods, axles), where objects are deformable (e.g. pulling out cables), or where narrow passages are non-linear (e.g. buzz wire game \[dorussen2021learning\]). Second, we believe it would be important to analyze the convergence properties of the high information entropy scale search. While the planners work robustly, there is currently no guarantee that it will converge in every situation. Third, it is important to integrate our algorithm into a larger system for disassembly tasks \[tian2025fabrica\], so that we can show that this can be used in combination with a real robot for complex object extraction tasks.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Despite limitations, scale-invariant MAB-RRT is a probabilistically complete and efficient planner which works reliably for complex object extraction tasks. We believe it is therefore an important component of a larger task and motion planning system \[Bayraktar2023RAL\] for automatic object disassembly.
