<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner

Topics include Motion planning, Sampling-based planning, Kinodynamic planning, Graphics processing unit, Parallelized, Real-time planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

GPU-native kinodynamic sampling-based planner that decomposes the traditionally serial RRT tree-growth process into three massively parallel subroutines. The design aligns with GPU execution hierarchies: independent threads, balanced workloads, low-latency shared memory.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based motion planners (SBMPs) are effective for planning with complex kinodynamic constraints in high-dimensional spaces, but they still struggle to achieve real-time performance, which is mainly due to their serial computation design. We present Kinodynamic Parallel Accelerated eXpansion (Kino-PAX), a novel highly parallel kinodynamic SBMP designed for parallel devices such as GPUs. Kino-PAX grows a tree of trajectory segments directly in parallel. Our key insight is how to decompose the iterative tree growth process into three massively parallel subroutines. Kino-PAX is designed to align with the parallel device execution hierarchies, through ensuring that threads are largely independent, share equal workloads, and take advantage of low-latency resources while minimizing high-latency data transfers and process synchronization. This design results in a very efficient GPU implementation. We prove that Kino-PAX is probabilistically complete and analyze its scalability with compute hardware improvements.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Empirical evaluations demonstrate solutions in the order of 10 ms on a desktop GPU and in the order of 100 ms on an embedded GPU, representing up to 1000× improvement compared to coarse-grained CPU parallelization of state-of-the-art sequential algorithms over a range of complex environments and systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robotic systems are increasingly deployed in dynamic environments, requiring fast, reactive motion planning that accounts for the robot's complex kinematics and dynamics. Solving the kinodynamic motion planning problem *quickly* is critical for ensuring both functionality and safety. Sampling-based motion planners (SBMPs) have proven effective for various difficult problems, such as complex dynamics, complex tasks, and stochastic dynamics. Nevertheless, they are typically designed for serial computation, limiting their speed to CPU clock rate. While recent methods can find solutions within seconds for simple systems and tens of seconds for complex ones, this is insufficient for *real-time* reactivity. Given the plateau in improvements to serial computation and CPU clock speeds, parallel devices like GPUs offer promising speedups. However, current SBMP algorithms are inherently sequential and inefficient when parallelized. In this work, we aim to enable real-time motion planning for complex and high-dimensional kinodynamical systems by exploiting the parallel architecture of GPU-like devices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce Kino-PAX, a highly parallel kinodynamic SBMP, designed to efficiently leverage parallel devices. Kino-PAX grows a tree of trajectory segments directly in parallel. Our key insight is that the iterative tree growth process can be decomposed into three massively parallel subroutines. We design Kino-PAX to align with the parallel execution hierarchy of these devices, ensuring that threads are largely independent, share equal workloads, and take advantage of low-latency resources while minimizing high-latency data transfers and process synchronizations. We provide an analysis of Kino-PAX, showing that it is probabilistically complete. We also demonstrate, through several benchmarks, that Kino-PAX is robust to changes in hyperparameters and scalable to large dimensional systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our contributions are four-fold: (i) Kino-PAX, a highly parallel kinodynamic SBMP designed to leverage the parallel architecture of GPU-like devices, (ii) a discussion of Kino-PAX's hyperparameters and its efficient application to highly parallel devices, (iii) a thorough analysis and proof of probabilistic completeness, and (iv) benchmarks showing the efficiency and efficacy of Kino-PAX for complex and high-dimensional dynamical systems. Our results show that Kino-PAX achieves up to three-orders-of-magnitude improvement in computation time compared to our baselines, which use CPU parallelization. In all evaluated problems, Kino-PAX finds solutions in the order of $10$ milliseconds, representing significant progress in enabling real-time kinodynamic motion planning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Geometric Motion Planning", "weight": 1.0} -->

SBMPs have a long-standing history in addressing the geometric motion planning problem, as established by foundational works such as Probabilistic RoadMaps (PRM), Expansive-Space Tree (EST), Rapidly-exploring Random Tree (RRT), etc. In general terms, SBMP techniques involve finding a path from a starting configuration to a goal region by constructing a graph or tree, where nodes represent geometric configurations and straight line edges represent transitions in the configuration space. Traditionally, these algorithms operate serially on CPU devices. However, the increasing demand for rapid replanning for complex systems in unknown and dynamic environments has driven the development of parallelization methods for geometric SBMPs. These parallelized approaches have been applied to both CPU-based planners and GPU-based implementations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Geometric Motion Planning", "weight": 1.0} -->

The CPU-based methods in use coarse-grained parallelization, where threads independently construct trees and exchange search information. These methods offer straightforward implementation by leveraging existing serial SBMPs but they achieve limited improvements in planning rates, and are not applicable to many-core devices. More similar to our work, the approaches in focus on fine-grained parallelization to accelerate the construction of a single tree. Works introduce parallel RRT and RRT\* methods that leverage thread-safe atomic operations and a novel concurrent data structure for efficient nearest neighbor search. In contrast, decomposes core operations of geometric SBMPs into unconventional data layouts that enable parallelism without specialized hardware. While these works present promising fine-grained parallelization techniques, they are not easily adaptable to kinodynamic planning and are unsuitable for many-core technology due to high inter-thread communication costs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Geometric Motion Planning", "weight": 1.0} -->

Most similar to our work, leverages GPUs to solve the geometric path planning problem by adapting FMT\* for parallelized graph search. Their implementation achieves orders-of-magnitude performance improvements over its serial counterpart; however, it is strictly limited to geometric problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Kinodynamic Motion Planning", "weight": 1.0} -->

To provide dynamically feasible and collision-free trajectories for systems with complex dynamics, a kinodynamic motion planning algorithm is used, as seen in traditional serial solutions such as. The details of the kinodynamic motion planning problem are formally discussed in Section II; however, in general, these algorithms are tree-based and solve the problem by sequentially randomly extending trajectories until a path from a start state to a goal region satisfying all state constraints can be followed by a sequence of trajectory segments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Kinodynamic Motion Planning", "weight": 1.0} -->

To achieve fast planning times, works employ space discretization. Specifically, constructs a graph from discrete regions and uses it as a high-level planner to guide the motion tree. However, this approach can face the *state-explosion* problem as the dimensionality of state space increases. In contrast, avoids this issue by using the discrete regions to track spatial information about the sparsity of the motion tree without constructing a graph. In the design of Kino-PAX, we take inspirations from those planners, using discrete regions to guide the search. Similar to, we use these regions for spatial information to ensure scalability. However, unlike previous work, Kino-PAX performs these operations in parallel subroutines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Kinodynamic Motion Planning", "weight": 1.0} -->

In contrast to the parallelized geometric planning solutions discussed above, parallelization for planning under the constraints of general dynamical systems is relatively understudied in the field. An approach to parallelization for the kinodynamic problem is a coarse-grained method, where multiple trees of classical SBMPs are generated in parallel, and the first solution found is returned. This technique improves average-case performance, and is employed in Section VI to perform CPU-based parallelization as a baseline. However, the inherent sequential nature of these motion planners make them inefficient for massive parallelization. In this work, we propose a novel algorithm that enables efficient application to highly parallel devices.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a robotic system operating within a bounded workspace $W \subset {\mathbb{R}}^{d}$, where $d \in {\{ 2,3\}}$. This workspace contains a finite set of obstacles $\mathcal{O}$, where each obstacle $o \in \mathcal{O}$ is a closed subset of $W$, i.e., $o \subset W$. The dynamics of the robot's motion is given by where ${x{(t)}} \in X \subset {\mathbb{R}}^{n}$ and ${u{(t)}} \in U \subset {\mathbb{R}}^{N}$ are the robot's state and control at time $t$, respectively, and $f:{{X \times U}\rightarrow{\mathbb{R}}^{n}}$ is the vector field.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We assume that $f$ is a Lipschitz continuous function with respect to both arguments, i.e, there exist constants ${K_{x},K_{u}} > 0$ such that for all ${x,x'} \in X$ and ${u,u'} \in U$, In addition to motion constraints defined by the dynamics in and obstacles in $\mathcal{O}$, we consider state constraints, e.g., bound on the velocity. To this end, we define the set of valid states, i.e., states at which the robot does not violate its state constraints and does not collide with an obstacle, as the valid set and denote it by $X_{\text{valid}} \subseteq X$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In motion planning, the interest is to find a valid trajectory $\mathbf{x}$ that visits a given goal set $X_{\text{goal}} \subseteq X_{\text{valid}}$. Therefore, by following this trajectory, the robot is able to respect all of its motion (kinodynamic) constraints, avoid collisions with obstacles, and reach its goal. In this work, we focus on kinodynamic motion planning with an emphasis on computational efficiency through parallelism.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 1 (Kinodynamic Motion Planning)", "weight": 1.0} -->

Consider a robot with dynamics in in workspace $W$ consisting of obstacle set $\mathcal{O}$. Given an initial state $x_{\text{init}} \in X_{\text{valid}} \subseteq X$ and goal region $X_{\text{goal}} \subseteq X_{\text{valid}}$, *efficiently* find a control trajectory $\mathbf{u}:{{\lbrack 0,t_{f}\rbrack}\rightarrow U}$ such that its induced trajectory $\mathbf{x}$ through is valid and reaches goal, i.e., ${\mathbf{x}{}} = x_{\text{init}}$ and Note that this is a challenging problem. The simpler problem of geometric motion planning (by ignoring dynamics) is already PSPACE-complete, and the addition of kinodynamic constraints makes finding a solution considerably more difficult due to the increase in search space dimension and dynamic complexities.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 1 (Kinodynamic Motion Planning)", "weight": 1.0} -->

Existing algorithms find solutions in the order of seconds for simple (e.g., linear) systems and tens of seconds for more complex non-linear systems on standard benchmark problems. When combined with the need for fast replanning, e.g., unknown and changing environments, finding solutions in real-time (milliseconds) becomes crucial for ensuring the functionality and safety of autonomous systems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 1 (Kinodynamic Motion Planning)", "weight": 1.0} -->

With the availability of onboard GPUs, parallel computation provides a promising approach for finding solutions quickly. Hence, in our approach, we focus on achieving efficiency through a highly parallelizable algorithm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Kino-PAX", "weight": 1.0} -->

Our approach to Problem 1. ‣ II Problem Formulation ‣ Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner") is a highly parallel algorithm that is able to exploit the many-core architecture of GPU-like processors. To achieve efficient performance on these high-throughput devices, it is crucial that our algorithm complements the execution hierarchy of such processors to optimize resource utilization. For the development of this algorithm, we follow the guidance of and base our development on three key principles: (i) *thread independence*, the ability for each thread in a program to execute without being dependent on the state or result of other threads; (ii) *even workloads across threads*, each thread is assigned an equal or nearly equal number of operations throughout its execution; (iii) *utilization of low-latency memory*, groups of threads utilize low-latency memory to share information and reduce the number of higher-latency global memory accesses.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Kino-PAX", "weight": 1.0} -->

With these principles in mind, we introduce *Kinodynamic Parallel Accelerated eXpansion* (Kino-PAX), a highly parallel kinodynamic SBMP. Kino-PAX grows a tree of trajectory segments in parallel. This is achieved by decomposing the iterative tree growth process, i.e., selection of nodes, extension, validity checking, and adding new nodes to the tree, into three massively parallel subroutines. Each subroutine follows the key principles of *thread independence*, *balanced workloads*, and *low-latency memory utilization*. Additionally, to ensure fast and efficient planning iterations, we minimize the communication needed in the synchronization steps between subroutines, e.g., CPU-GPU communication.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Kino-PAX", "weight": 1.0} -->

At each iteration of Kino-PAX, a set of nodes in the tree is expanded in parallel. Each sample is extended multiple times through random sampling of controls, also in parallel. We dynamically adjust the number of extensions in each iteration to maintain an effective tree growth rate, ensuring efficient usage of the device's throughput. After extension, a new set of nodes are selected independently to be propagated in the next iteration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Kino-PAX", "weight": 1.0} -->

To guide the search process, Kino-PAX, similar to, employs a high-level space decomposition approach. We designed this method to be well-suited for parallel computation. This decomposition estimates exploration progress in each region, allowing threads to act independently when adding new nodes to the tree and identifying promising nodes for extension. As more trajectory segment data becomes available, the estimate of promising space regions is improved, allowing Kino-PAX to focus on propagating a large number of favorable nodes into less explored areas of the space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Core Algorithm", "weight": 1.0} -->

Here, we present a detailed description of Kino-PAX. Pseudocode of Kino-PAX is presented in Alg. 1, with subroutines Algs. 2, 3, and 4, and a full planning iteration is illustrated in Fig. 1. Kino-PAX organizes samples into three distinct sets: $V_{U},V_{O},V_{E}$. The set $V_{U}$ consists of newly generated promising samples that have not yet been added to the tree. The set $V_{O}$ includes tree nodes that are not currently considered for expansion; intuitively, these nodes are located in densely populated or frequently invalid regions of the search space. Finally, $V_{E}$ comprises the set of nodes that are flagged for parallel expansion. Further, Kino-PAX maintains the spatial search progress information using a partition of the state space denoted by $\mathcal{R}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Core Algorithm", "weight": 1.0} -->

Input: xinit, Xgoal, tmax Output: Solution trajectory x 3𝒯← Initialize tree with root node xinit 5 Initialize ℛ with Paccept(ℛi) = 1 for each ℛi ∈ ℛ 7while ElapsedTime < tmax do 12 if x ≠ null then return x;

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A1 Initialization", "weight": 1.0} -->

In Alg. 1, Kino-PAX takes as input the initial state $x_{\text{init}}$, a goal region $X_{\text{goal}}$, and a maximum execution time $t_{max}$. In Lines 1-2, a tree $\mathcal{T}$ is initialized with $x_{\text{init}}$ at its root. Additionally, the set $V_{E}$ is initialized with the state $x_{\text{init}}$ and the sets $V_{U}$ and $V_{O}$ are initialized as empty. In Line 3, the space decomposition $\mathcal{R}$ is initialized in the state space, where the decomposition consists of non-overlapping regions, such that: where Int$(\mathcal{R}_{i})$ is the interior of $\mathcal{R}_{i}$. Each $\mathcal{R}_{i}$ is then further partitioned to a set of finer regions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A1 Initialization", "weight": 1.0} -->

We denote the $k$-th sub-region of $\mathcal{R}_{i}$ by $\mathcal{R}_{i}^{k}$, i.e., $\mathcal{R}_{i} = {\cup_{k = 1}^{n'}\mathcal{R}_{i}^{k}}$. For each region $\mathcal{R}_{i} \in \mathcal{R}$, several metrics are calculated to assess the exploration progress of the tree. These metrics, adapted, are designed to be effective in identifying promising regions for systems with complex dynamics and are well suited for parallelism.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A1 Initialization", "weight": 1.0} -->

Specifically, Kino-PAX updates the following metrics for each region, $\mathcal{R}_{i}$, after each iteration of parallel propagation to continually guide the search process: $Cov{(\mathcal{R}_{i})}$: estimates the progress made by the tree planner in covering $\mathcal{R}_{i}$; $FreeVol{(\mathcal{R}_{i})}$: estimates the free volume of $\mathcal{R}_{i}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A1 Initialization", "weight": 1.0} -->

The exact expressions for $Cov{(\mathcal{R}_{i})}$ and $FreeVol{(\mathcal{R}_{i})}$ are the same as, which we also show in Sec. III-A3.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A1 Initialization", "weight": 1.0} -->

These metrics determine a score value, $Score{(\mathcal{R}_{i})}$ and subsequently a probability $P_{accept}{(\mathcal{R}_{i})}$, which aid Kino-PAX in adding favorable samples to $\mathcal{T}$ and assessing if an existing node should be extended. During initialization, all $P_{accept}{(\mathcal{R}_{i})}$ values are set to 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A2 Node Extension", "weight": 1.0} -->

3 Randomly sample u and dt; 7 if the trajectory from x to x′ is valid then 9 if ℛik unvisited or with Paccept(ℛi) then After initialization, the main loop of the algorithm begins (Alg. 1, Lines 4--8). In each iteration, the Propagate (Alg. 2) function is called to propagate the set $V_{E}$ in parallel (Alg. 1, Line 5, Fig. 1(b)). Each node $x \in V_{E}$ is expanded $\lambda \in {\mathbb{N}}^{+}$ times using $\lambda$ threads, where each thread handles one expansion of $x$ (Alg. 2, Lines 1--2).

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A2 Node Extension", "weight": 1.0} -->

For each thread, a control $u \in U$ and a time duration ${dt} \in {(0,T_{prop}\rbrack}$, where $T_{prop}$ is a user-defined constant that sets the maximum propagation time, are randomly sampled, and the node's continuous state $x$ is propagated using dynamics in to generate a new sample state $x'$ (Alg. 2, Lines 3--4). Next, the corresponding region of $x'$, $\mathcal{R}_{i}^{k}$, is calculated (Alg. 2, Line 5). Then, in Line 6, the trajectory segment from $x$ to $x'$ is checked for validity, i.e., if it is in $X_{\text{valid}}$. Throughout the trajectory segment, a user-defined collision check is performed (our implementation uses a coarse-phase bounding volume hierarchies method discussed in). If the extended segment is valid, we increment the total number of valid samples in $\mathcal{R}_{i}$ (Alg.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A2 Node Extension", "weight": 1.0} -->

2, Line 7). Next, $x'$ is added to the set $V_{U}$ if its corresponding region $\mathcal{R}_{i}^{k}$ is unvisited; if $\mathcal{R}_{i}^{k}$ already contains a node, then $x'$ is added to $V_{U}$ with probability $P_{accept}{(\mathcal{R}_{i})}$, which favors promising samples (Alg. 2, Lines 8-9, Fig. 1(c)). Alternatively, if the trajectory segment is invalid, we increment the count of invalid samples in $\mathcal{R}_{i}$, as shown in Line 11. This information guides future propagation iterations away from regions that are frequently invalid, improving search efficiency.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A2 Node Extension", "weight": 1.0} -->

Output: Updated estimates for each region ℛi

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

After all samples in $V_{E}$ have been expanded, the UpdateEstimates (Alg. 3) subroutine is called (Alg. 1, Line 6). In this subroutine, metrics for each visited region (i.e., a region with a node $x \in \mathcal{T}$), denoted by $\mathcal{R}_{avail}$, are updated in parallel, with a thread handling a unique region $\mathcal{R}_{i} \in \mathcal{R}_{avail}$, calculating $Cov{(\mathcal{R}_{i})}$ and $FreeVol{(\mathcal{R}_{i})}$ (Alg. 3, Lines 1-3).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

For each thread, $Cov{(\mathcal{R}_{i})}$ is set to the number of visited sub-regions within $\mathcal{R}_{i}$, and $FreeVol{(\mathcal{R}_{i})}$ is calculated as where $\delta > 0$ is a small constant, and $vol{(\mathcal{R}_{i})}$ represents the mapped workspace volume of the region $\mathcal{R}_{i}$. Subsequently, on Line 4 of Alg. 3, each thread calculates its corresponding $Score{(\mathcal{R}_{i})}$ value with which prioritizes regions that are less visited and have a high free volume and low coverage.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

Once all score values have been updated, each visited region's $P_{accept}{(\mathcal{R}_{i})}$ probability is refined (Alg. 3, Lines 5-6, Fig. 1(c)). This process, again, is done in parallel with a thread being designated to a unique $\mathcal{R}_{i} \in \mathcal{R}_{avail}$ and $P_{accept}{(\mathcal{R}_{i})}$ being set by where $0 < \epsilon \ll 1$ is a constant and $\mathcal{R}_{avail} \in \mathcal{R}$ represents the set of regions that contain a node in $\mathcal{T}$. We note that the expressions for the metrics in - are taken.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

Once the $P_{accept}{(\mathcal{R}_{i})}$ probabilities have been updated for all available regions, the UpdateNodeSets subroutine is called (Alg. 1, Line $7$, Fig. 1(d)). In Lines $1 - 3$ of Alg. 4, we remove samples from the expansion set $V_{E}$ randomly with probability $1 - {P_{accept}{(\mathcal{R}_{i})}}$, ensuring that promising samples remain in $V_{E}$. Then, we move the newly generated samples, $V_{U}$, to $\mathcal{T}$ and add them to the expansion set $V_{E}$. If any newly generated nodes satisfy goal criteria, we return the valid trajectory $\mathbf{x}$ (Alg. 4, Lines 4-6). Finally, we move inactive samples in $V_{O}$ to the expansion set if deemed promising with the updated search information (Alg. 4, Lines 7-9).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

Kino-PAX repeats the main loop of Propagate, UpdateEstimates and UpdateNodeSets until a solution trajectory $\mathbf{x}$ that solves Problem 1. ‣ II Problem Formulation ‣ Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner") is returned, or a user-defined time limit $t_{max}$ is surpassed.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A3 Node Selection", "weight": 1.0} -->

Output: Trajectory if a goal is found, otherwise null 4 Move x to VO with probability 1 − Paccept(ℛi); 6 Move x from VU to VE and 𝒯; 7 if x ∈ X then return Trajectory xinit to x; 11 Move x to VE with probability Paccept(ℛi);

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tuning and Performance Discussion", "weight": 1.0} -->

In this section, we discuss how Kino-PAX can be tuned to match a problem's difficulty, and present the properties of Kino-PAX that enable efficient parallelism.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Tuning Parameter", "weight": 1.0} -->

In practice, due to the limitations of device memory and the high cost of vector resizing operations, we predefine the maximum size of the tree rather than constraining the runtime, similar to the approach taken in PRM. This introduces a hyperparameter for Kino-PAX, denoted as $t_{e}$, which we refer to as the expected tree size. Specifically, $t_{e}$ corresponds to the maximum number of nodes in Kino-PAX and should be tuned according to the difficulty of the problem at hand.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Tuning Parameter", "weight": 1.0} -->

Varying, $t_{e}$ has two main effects on the performance of Kino-PAX. Firstly, an increase in $t_{e}$ increases the branching factor $\lambda$ which is updated for each iteration of parallel propagation and is set according to where $\lambda_{max}$ is the user-defined maximum branching factor and $|\mathcal{T}|$ and $|V_{E}|$ are the numbers of nodes in $\mathcal{T}$ and $V_{E}$, respectively. Eq. ensures that in the early iterations, when $|\mathcal{T}|$ is much smaller than $t_{e}$, a larger $\lambda$ is used. This approach effectively uses available throughput and accelerates the initial stages of tree propagation. As $|\mathcal{T}|$ approaches $t_{e}$ and $|V_{E}|$ grows large, a smaller $\lambda$ is used to stabilize the growth rate of $\mathcal{T}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Tuning Parameter", "weight": 1.0} -->

Secondly, $t_{e}$ affects the number of nodes that can be included in $\mathcal{T}$. As the problem difficulty increases, such as with a system's state dimension, a larger $t_{e}$ is recommended to sufficiently explore the space. Kino-PAX's search characteristics make finding a suitable $t_{e}$ relatively straightforward for a given system, as the tree expands in all accessible free space areas. We demonstrate this in Sec. VI, where systems with the same state dimension utilize a constant $t_{e}$ value across all testing environments. In Sec. VI, we also show that as $t_{e}$ increases, the success rate of Kino-PAX converges to 100%.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The maximum tree size can be made adaptive by increasing $t_{e}$ by a constant multiple if a solution is not found after the tree size nears its threshold. However, this introduces vector resizing operations on high latency device memory, slowing down the search.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Decomposition Tuning", "weight": 1.0} -->

The search efficiency of Kino-PAX is dependent on the choice of space decomposition. An improper decomposition, e.g., one that is too coarse or too fine, can lead to inefficiencies. A decomposition that is too fine may cause slower updates due to the large number of regions. On the other hand, a decomposition that is too coarse may lead to poor approximation of promising space regions. For instance, if a region frequently generates invalid trajectories but contains critical space for finding a solution, Kino-PAX may experience inefficient search. A method to mitigate this is to use a free-space-obeying decomposition, as proposed. Nonetheless, Kino-PAX remains probabilistically complete with any valid decomposition.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Efficient Application to Highly Parallel Devices", "weight": 1.0} -->

Kino-PAX's propagation subroutine implementation is well-suited for parallelism due to three main factors. First, we utilize *low-latency memory* by distributing commonly used data to groups of nearby threads. Specifically, the state $x \in V_{E}$ is shared via on-chip memory to all $\lambda$ threads assigned to expand the node. Second, we *balance workloads* across threads by having each thread create a single trajectory segment, minimizing thread divergence---i.e., variations in execution paths that force threads into serial execution. Third, the acceptance of new samples and their addition to $V_{U}$ is achieved with *thread independence*, using and unique thread identifiers.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Efficient Application to Highly Parallel Devices", "weight": 1.0} -->

Kino-PAX maintains its space decomposition in a parallel-friendly manner through the metrics - that can be calculated independently of other regions and by ensuring that each region's calculations have an equal number of operations. Further, we avoid the need for serial data structures when choosing expansion nodes by adding samples to $V_{E}$ independently via the acceptance probability.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Efficient Application to Highly Parallel Devices", "weight": 1.0} -->

Furthermore, the organization of samples into three disjoint sets, ${V_{U},V_{O}},$ and $V_{E}$, enables a straightforward and memory-efficient representation. In Kino-PAX, we do this via a boolean-mask representation that is thoroughly discussed.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Efficient Application to Highly Parallel Devices", "weight": 1.0} -->

Lastly, Kino-PAX reduces latency between its subroutines by pre-allocating a large memory chunk on the GPU to accommodate $t_{e}$ nodes. This allows Kino-PAX to construct its tree directly on the GPU, avoiding the transfer of large data structures between devices.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Analysis", "weight": 1.0} -->

Here, we show that Kino-PAX is probabilistically complete for Problem 1. ‣ II Problem Formulation ‣ Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner") and analyze its scalability.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-A Probabilistic Completeness", "weight": 1.0} -->

We begin with a definition of probabilistic completeness for algorithms that solve Problem 1. ‣ II Problem Formulation ‣ Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner").

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Scalability", "weight": 1.0} -->

Here, we discuss the scalability of Kino-PAX. Firstly, Kino-PAX's scalability increases as the number of cores in the parallel device increases. Since Kino-PAX supports adaptive tuning of the branching factor $\lambda$ through varying $t_{e}$, an increased number of cores can be leveraged by increasing $t_{e}$ and setting a higher $\lambda_{max}$. This results in computation time improvements as the number of cores increase, allowing Kino-PAX to scale as parallel hardware computation power improves.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Scalability", "weight": 1.0} -->

Secondly, as the problem becomes more complex, i.e., requiring a larger tree (more nodes) to find a solution, traditional tree-based SBMPs suffer. That is, they slow down significantly as the number of nodes increases due to the sequential nature of those algorithms. However, Kino-PAX does not struggle with increasing number of nodes, unless the tree size nears its threshold and a resizing operation is needed. This property makes Kino-PAX particularly more advantageous for planning for systems with large dimensional state spaces since they often require large trees to sufficiently search the space.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

We demonstrate the performance of Kino-PAX in planning for various dynamical systems across three 3D environments shown in Fig. 2. The considered systems are: (i) 6D double integrator, (ii) 6D Dubins airplane, and (iii) 12D highly nonlinear quadcopter.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

Environment LABEL:sub@fig:trees Environment LABEL:sub@fig:narrowPassage Environment LABEL:sub@fig:house 12D Non Linear Quadcopter Table I: Benchmark results over 50 trials with a 60-second maximum planning time. CPU-based algorithms used coarse-grained parallelization, growing multiple trees in parallel and utilizing all available cores, denoted by “Par” before the algorithm name.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

For each pair of dynamical system and environment, we benchmark the performance and scalability of Kino-PAX against four traditional SBMPs: RRT, EST, PDST and SyCLoP. To ensure fairness, for these comparison planners, we used a coarse-grained CPU parallelization method where multiple trees grow in parallel as suggested. Each tree is managed by a separate thread, and the planner returns the first solution found.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

We implemented Kino-PAX in CUDA C and performed benchmarks on two GPUs with different capabilities. We used an NVIDIA RTX 4090 as a baseline, which has 16,384 CUDA cores and 24 GB of RAM. Further, to test the efficiency of Kino-PAX on an embedded GPU, we ran benchmarks on an NVIDIA Jetson Orin Nano, which has 1,024 cores and 8 GB of RAM. The comparison algorithms, are implemented in C++ using OMPL and executed on an Intel Core i9-14900K CPU with 24 cores, a base clock speed of 4.4 GHz, and 128 GB of RAM. Our implementation of Kino-PAX is publicly available: We followed the standard setup configurations for all comparison algorithms as recommended by the OMPL documentation. All algorithms, including Kino-PAX, were configured to use the same methods for state propagation, state validity checking and space decomposition. For all experiments, a grid-based decomposition was used with the dimensionality of the grid equal to the system's state-space dimension.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments", "weight": 1.0} -->

For Kino-PAX's hyperparameters, $\lambda_{max}$ was set to $32$ and $t_{e}$ was set to $2 \times 10^{5}$ for all 6D systems and $4 \times 10^{5}$ for the 12D system. For each combination of algorithm, dynamic model, and workspace, we performed 50 queries, each with a maximum runtime of 60 seconds.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Benchmark Results", "weight": 1.0} -->

Table I shows the mean runtime, the speed ratio relative to the desktop GPU implementation of Kino-PAX, and the success rate within the allotted planning time for each combination of algorithm, environment, and dynamics.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Benchmark Results", "weight": 1.0} -->

For both 6D systems, Kino-PAX finds a solution trajectory in less than $8$ ms across all testing environments. For the 6D Double Integrator, Kino-PAX is on average $85 \times$, $287 \times$, $433 \times$ faster in Environments LABEL:sub@fig:trees, LABEL:sub@fig:narrowPassage, LABEL:sub@fig:house, respectively, compared to the baseline algorithms. For the Dubins Airplane system, the performance gap of Kino-PAX widens further.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-A Benchmark Results", "weight": 1.0} -->

For instance, in Environment LABEL:sub@fig:house, Kino-PAX experiences a slowdown of less than $1.3 \times$ ($\sim$`<!-- -->`{=html}2 ms) compared to RRT's $22 \times$ ($\sim$`<!-- -->`{=html}20,000 ms), EST's $1.8 \times$ ($\sim$`<!-- -->`{=html}4,000 ms), PDST's $8.9 \times$ ($\sim$`<!-- -->`{=html}16,000 ms), and SyCLoP's $22 \times$ ($\sim$`<!-- -->`{=html}24,000 ms). Additionally, the embedded GPU implementation of Kino-PAX outperforms all serial baseline methods, finding valid trajectories for all 6D problems in under $115$ ms.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-A Benchmark Results", "weight": 1.0} -->

When dealing with the more challenging 12D nonlinear quadcopter problem, Kino-PAX finds solutions in less than $25$ ms across all environments. On average, this marks an improvement of *three orders of magnitude* over all reference serial solutions. In the most challenging environment (Environment LABEL:sub@fig:house), the best-performing baseline algorithm (EST) is $1720 \times$ slower than the desktop implementation of Kino-PAX and $44 \times$ slower than the embedded GPU implementation.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A Benchmark Results", "weight": 1.0} -->

As evident from the results, Kino-PAX outperforms baseline algorithms more significantly as the problem becomes more challenging; in other words, the performance gap significantly widens in favor of Kino-PAX. This is due to two main factors. First, as the dimensionality of the search space increases, exponentially more trajectory segments are required to find a valid solution. This suits Kino-PAX particularly well, as it is designed to propagate a massive number of nodes efficiently in parallel. Second, as the problem difficulty increases, the efficiency of Kino-PAX becomes more prominent. This is because unlike traditional tree-based SBMPs that slow down as the number of samples increases, Kino-PAX does not suffer as much with the size of the tree.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B Effects Of Tuning Parameter $t_{e}$", "weight": 1.0} -->

To support the point made in Sec. IV that Kino-PAX's hyperparameter $t_{e}$ is easy to tune and that Kino-PAX remains efficient across a wide range of values, we present a numerical experiment showing that as Kino-PAX is provided with a sufficiently large $t_{e}$, its failure rate converges to zero. We also examine the impact on runtime as $t_{e}$ increases. Fig. 3 presents the results for planning with the 12D nonlinear quadcopter system in Environment LABEL:sub@fig:trees.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-B Effects Of Tuning Parameter $t_{e}$", "weight": 1.0} -->

As shown in Fig. 3(a), for small values of $t_{e}$, Kino-PAX is unable to find solutions, indicating that the number of samples required exceeds $t_{e}$. As $t_{e}$ increases beyond $2.8 \times 10^{5}$, Kino-PAX achieves a 100% success rate, demonstrating that $t_{e}$ is not a sensitive tuning parameter with respect to finding solutions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Effects Of Tuning Parameter $t_{e}$", "weight": 1.0} -->

Fig. 3(b) shows an increase in the hyperparameter $t_{e}$ also increases the runtime. This can be attributed to two main factors. First, as $t_{e}$ increases, Kino-PAX typically uses a larger branching factor $\lambda$, resulting in a tree with more nodes. In this experiment, the number of nodes in the tree increases by approximately $1 \times 10^{5}$ for every $2 \times 10^{5}$ increase in $t_{e}$. Specifically, we observed $3.1 \times 10^{5}$ nodes when $t_{e} = {4 \times 10^{5}}$ and $6.1 \times 10^{5}$ nodes when $t_{e} = {10 \times 10^{5}}$. Second, the larger $t_{e}$ demands more memory, leading to more frequent cache misses in the implementation of Kino-PAX, which causes data to be fetched from slower global memory more often.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced a novel motion planning algorithm for kinodynamic systems that enables a significant parallelization of a process previously considered inherently sequential. Our algorithm is well suited to exploit the recent advancements of modern computing devices and is equipped to scale as hardware continues to improve. Benchmark results show planning times of less than $8$ ms for 6-dimensional systems and less than $25$ ms for a 12-dimensional nonlinear system, representing an improvement of up to three orders of magnitude compared to traditional motion planning algorithms. For future work, we plan to make the hyperparameter $t_{e}$ dynamic (adaptive) and extend Kino-PAX to a near-optimal planner.
