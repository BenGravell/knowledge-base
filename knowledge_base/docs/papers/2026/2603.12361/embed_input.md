<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning

Topics include Motion planning, Neural networks, Graph neural networks, Graphs, Benchmarks, Sampling-based methods, Planning, Sampling, GNN-DIP, Two-phase, Decomposition-informed, DIP, Delaunay triangulation, CDT.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning through narrow passages remains a core challenge: sampling-based planners rarely place samples inside these narrow but critical regions, and even when samples land inside a passage, the straight-line connections between them run close to obstacle boundaries and are frequently rejected by collision checking. Decomposition-based planners resolve both issues by partitioning free space into convex cells - every passage is captured exactly as a cell boundary, and any path within a cell is collision-free by construction. However, the number of candidate corridors through the cell graph grows combinatorially with environment complexity, creating a bottleneck in corridor selection. We present GNN-DIP, a framework that addresses this by integrating a Graph Neural Network (GNN) with a two-phase Decomposition-Informed Planner (DIP). The GNN predicts portal scores on the cell adjacency graph to bias corridor search toward near-optimal regions while preserving completeness. In 2D, Constrained Delaunay Triangulation (CDT) with the Funnel algorithm yields exact shortest paths within corridors; in 3D, Slab convex decomposition with portal-face sampling provides near-optimal path evaluation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Benchmarks on 2D narrow-passage scenarios, 3D bottleneck environments with up to 246 obstacles, and dynamic 2D settings show that GNN-DIP achieves 99-100% success rates with 2-280 times speedup over sampling-based baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning in cluttered environments is a fundamental problem in robotics. Among its open challenges, narrow passages stand out as both the hardest to solve and the most valuable to exploit: in environments with tight doorways, narrow gaps between obstacles, or double enclosures, the only feasible routes pass through regions that occupy a vanishingly small fraction of the configuration space, making their reliable discovery essential for any practical planner.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based planners, including RRT\*, BIT\*, InformedRRT\* (iRRT\*), and their variants, provide asymptotic optimality guarantees but face a dual challenge in narrow passages. First, the probability of randomly sampling inside a passage of width $\varepsilon$ scales as $\varepsilon^{d}$, so narrow gaps become exponentially harder to discover in higher dimensions. Second, even when a sample lands inside a narrow passage, the straight-line segments connecting it to neighboring samples run close to obstacle boundaries, complicating collision checking at finite resolution. These two challenges compound in environments with narrow gaps and double enclosures, where increasing sampling density or collision-checking resolution provides diminishing returns.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Decomposition-based planners address both challenges structurally. By partitioning the free space $\mathcal{F}$ into convex cells and constructing a cell adjacency graph, every passage---no matter how narrow---is represented exactly as a cell boundary (portal), so no bottleneck region is missed. Moreover, any path within a convex cell is collision-free by definition, eliminating resolution-dependent collision checking entirely. The continuous planning problem thus reduces to a discrete corridor search followed by local path optimization within each corridor. In 2D, exact shortest paths within a corridor of convex polygons can be computed in linear time using the Funnel algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The principal limitation of decomposition-based approaches is the corridor selection problem: the number of distinct corridors from start to goal grows combinatorially with the number of cells. In environments with hundreds to thousands of cells, the $k$-shortest path search via Yen's algorithm must be guided by accurate edge weights. The default centroid-distance heuristic $w(c_{i},c_{j})=\|z_{i}-z_{j}\|$ correlates poorly with actual path cost in environments with elongated cells, narrow passages, or asymmetric obstacle configurations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach. We address the corridor selection problem by training a GNN on the cell adjacency graph to predict portal-level scores. Each portal $p_{ij}$ (the shared boundary between adjacent cells $c_{i}$ and $c_{j}$) receives a score $s_{ij}\in$ indicating the probability that it lies on a near-optimal corridor. These scores modulate edge weights via $w(c_{i},c_{j})=d(c_{i},c_{j})\cdot\exp(-\beta\cdot s_{ij})$, concentrating the $k$-shortest path search on promising regions. Importantly, the modulation is continuous---no corridors are pruned---thereby preserving completeness while improving the quality of initial corridor candidates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1 illustrates the GNN-DIP ($\mathcal{G}$-DIP) pipeline on a labyrinth environment with 50 polygon obstacles of varying shapes. CDT produces 385 triangular cells (panel b), creating a combinatorial corridor search space that grows exponentially with cell count. The GNN identifies a narrow corridor of 73 cells (panel c, light blue) containing the near-optimal path, reducing the effective search space by ${\sim}81\%$. Parallel corridor evaluation via the Funnel algorithm then yields the initial solution in under 20 ms. Phase 2 refines the solution within a shrinking informed ellipsoid (panel d).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are: A GNN-based portal scoring framework on cell adjacency graphs, with feature engineering for node/edge representations and a training pipeline using focal loss, multi-label generation, and stratified train-validation splitting (Section III).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A two-phase Decomposition-Informed Planner (DIP) combining GNN-guided corridor search, informed ellipsoid pruning, and Funnel-based corridor evaluation, with proofs of completeness and convergence (Section IV).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive experiments spanning 2D (310 maps, 18 scenarios), 3D bottleneck environments (4 scenarios, 50 PDT runs each), and dynamic 2D environments (100 planning instances), demonstrating 2--280$\times$ speedup, 99--100% success rates, and collision safety by construction (Section V).

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Decomposition-Based Motion Planning", "weight": 1.0} -->

Cell decomposition methods partition the free space into simple regions and plan over the resulting adjacency graph. Exact cell decomposition constructs cells whose union equals the free space, whereas approximate methods employ regular grids or adaptive subdivisions. Constrained Delaunay Triangulation (CDT) with parity-based face classification provides a well-studied 2D decomposition with robust implementations in CGAL. The Funnel algorithm computes the exact Euclidean shortest path through a sequence of adjacent convex polygons in $O(n)$ time, where $n$ is the total number of portal endpoints.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Decomposition-Based Motion Planning", "weight": 1.0} -->

In 3D, exact convex decomposition of general polyhedral free space is computationally expensive. For environments with axis-aligned box (AABB) obstacles, a Slab decomposition exploits obstacle face alignment to produce an exact convex decomposition in near-linear time. Strub and Gammell introduced AIT\* and EIT\*, which integrate lazy search and informed sampling. The Planner Developer Tools (PDT) framework provides standardized benchmarking infrastructure for OMPL-compatible planners.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Learning and GNNs for Motion Planning", "weight": 1.0} -->

Neural approaches to motion planning include learned samplers, conditional generative models, and reinforcement learning, all operating in continuous configuration space without exploiting cell decomposition structure. GNNs have been applied to roadmap graphs for collision prediction, neural planning, and edge cost learning. These operate on roadmap graphs (nodes = configurations, edges = local paths), whereas our GNN operates on the cell adjacency graph (nodes = free-space cells, edges = portals)---a fundamentally different and more compact representation. Informed approaches exploit ellipsoidal or zonotope subsets; our GNN guidance is complementary, biasing corridor search before any solution is found.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Problem Formulation", "weight": 1.0} -->

This section formalizes the key components of the proposed framework. Throughout, $\mathcal{W}\subseteq\mathbb{R}^{d}$ ($d\in\{2,3\}$) denotes the workspace.

<!-- chunk {"id": "body-0017", "role": "body", "section": "GNN Portal Scoring", "weight": 1.0} -->

The corridor selection problem can be formulated as an edge classification task on the cell adjacency graph: for each portal $p_{ij}$, predict whether it lies on a near-optimal corridor. A GNN is trained to solve this classification problem, and the predicted scores are used to bias edge weights in the corridor search.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Graph Representation and Feature Engineering", "weight": 1.0} -->

The cell adjacency graph $G=(\mathcal{C},\mathcal{P})$ is represented as a directed graph with bidirectional edges (each portal appears as two directed edges). Each cell $c_{i}$ is associated with a node feature vector $\mathbf{x}_{i}\in\mathbb{R}^{d_{n}}$, and each portal $p_{ij}$ with an edge feature vector $\mathbf{e}_{ij}\in\mathbb{R}^{d_{e}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A1 Node Features ($d_{n}=11$ in 2D) and Edge Features ($d_{e}=9$ in 2D)", "weight": 1.0} -->

Table I and Edge Features (𝑑_𝑒=9 in 2D) ‣ III-A Graph Representation and Feature Engineering ‣ III GNN Portal Scoring ‣ GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning") lists the complete 2D feature set. Node features encode cell geometry (area, aspect ratio $\rho_{i}=e_{\max}/e_{\min}$), spatial relationships to the query (distances to start, goal, and the start--goal line $d_{\perp}$), and role indicators. Edge features encode portal geometry, spatial context, and inter-cell relationships. The relative angle $\theta_{ij}=\angle(p_{ij})-\angle(\overrightarrow{q_{s}q_{g}})$ captures alignment between the portal and the global query direction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A1 Node Features ($d_{n}=11$ in 2D) and Edge Features ($d_{e}=9$ in 2D)", "weight": 1.0} -->

For the 3D Slab decomposition, features are extended to $d_{n}{=}14$ and $d_{e}{=}13$ by adding volumetric cell descriptors (volume, size along each axis, clearance) and 3D portal attributes (face area, portal height, normal axis).

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A1 Node Features ($d_{n}=11$ in 2D) and Edge Features ($d_{e}=9$ in 2D)", "weight": 1.0} -->

Start cell flag Cell–cell dist.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A1 Node Features ($d_{n}=11$ in 2D) and Edge Features ($d_{e}=9$ in 2D)", "weight": 1.0} -->

Goal cell flag TABLE I: GNN input features: node (cell) and edge (portal).

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B GNN Architecture", "weight": 1.0} -->

The architecture follows an encode--process--decode pattern. Raw node features are projected to hidden dimension $h=128$ via a linear layer with batch normalization (BN) and ReLU. In 2D, three GCN layers with symmetric normalization, BN, and dropout ($p{=}0.15$) process the node embeddings; layers 2--3 use two-layer-skip residual connections. For 3D, GCN is replaced by GATv2 (3 layers, 4 attention heads) to better capture the irregular connectivity of Slab cells; the remaining architecture is identical.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B GNN Architecture", "weight": 1.0} -->

For each portal $p_{ij}$, the score is predicted by an MLP ($\mathbb{R}^{2h+d_{e}}\to h\to 32\to 1$, ReLU activations) on the concatenation of endpoint embeddings and edge features: where $\mathrm{sigm}(\cdot)=1/(1+e^{-x})$ is the sigmoid function (distinguished from path $\sigma$).

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C1 Label Generation", "weight": 1.0} -->

Training labels are generated from OMPL baseline planners (iRRT\*, AIT\*, BIT\*, RRT\*) run on each map with a sufficient time budget. All solution paths are collected and portals on near-optimal corridors are identified. Let $\sigma_{\text{ref}}$ denote the shortest path found across all baseline runs: where $\epsilon=0.1$ (10% suboptimality threshold). Since $\sigma_{\text{ref}}$ is the best solution found rather than the true optimum $\sigma^{*}$, label noise may arise when baselines have not converged; in practice, running four planners with a 10 s budget per map yields near-optimal references. This multi-label scheme assigns positive labels to portals on any near-optimal corridor, capturing the multiplicity of good solutions. The resulting label distribution is severely imbalanced: typically less than 5% of portals are positive.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C2 Focal Loss", "weight": 1.0} -->

To address the extreme class imbalance, focal loss is adopted: where $p_{t}=\hat{s}\cdot y+(1-\hat{s})(1-y)$ is the model's estimated probability for the true class, $\alpha_{t}=\alpha y+(1-\alpha)(1-y)$ balances positive/negative contributions, and $\gamma$ is the focusing parameter. We use $\alpha=0.85$ and $\gamma=2.0$. The $(1-p_{t})^{\gamma}$ factor down-weights well-classified negatives, focusing gradient updates on hard positives---the critical portals that the model initially misclassifies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C3 Optimization", "weight": 1.0} -->

Training employs Adam (initial learning rate $10^{-3}$, weight decay $10^{-4}$) with cosine annealing and early stopping based on validation F1 score (patience 30 epochs). Data are split using stratified sampling (20% validation ratio). The model contains approximately 150K parameters with hidden dimension $h=128$ and trains in under 5 minutes on a single GPU.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Decomposition-Informed Planner", "weight": 1.0} -->

The Decomposition-Informed Planner (DIP) operates in two phases on the cell adjacency graph $G$. Phase 1 performs GNN-guided $k$-shortest corridor search with corridor evaluation; Phase 2 refines the search using an informed ellipsoid derived from the current best solution.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A GNN-Guided Edge Weight Integration", "weight": 1.0} -->

Given GNN-predicted portal scores $\{\hat{s}_{ij}\}$, we define modified edge weights: where $d(c_{i},c_{j})=\|z_{i}-z_{j}\|$ is the centroid distance and $\beta>0$ is a temperature parameter (we use $\beta=3.0$).

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Phase 1: $k$-Shortest Corridor Search", "weight": 1.0} -->

Phase 1 applies Yen's algorithm to find $k$ shortest paths in $G$ from the start cell $c_{s}$ to the goal cell $c_{g}$, using edge weights $w_{\text{GNN}}$ when available and centroid distances $d(\cdot,\cdot)$ otherwise. Each corridor is evaluated using the Funnel algorithm (2D) or portal-face sampling with layered-graph DP (3D).

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Phase 1: $k$-Shortest Corridor Search", "weight": 1.0} -->

The best solution from Phase 1 provides an initial cost bound $c_{\text{best}}^{}$ that seeds the refinement in Phase 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-E Corridor Evaluation", "weight": 1.0} -->

In 2D, the Funnel algorithm computes the exact shortest path through a corridor of $L$ convex polygons in $O(L)$ time via string-pulling. In 3D, we employ portal-face sampling: $N_{s}$ points are sampled uniformly on each portal face, forming a layered DAG from $q_{s}$ through portal samples to $q_{g}$. A forward DP sweep finds the shortest path in $O(L\cdot N_{s}^{2})$ time---collision-free by convexity. Adaptive Gaussian re-sampling refines the path for up to $r=3$ iterations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-F Complexity and System Design", "weight": 1.0} -->

Decomposition is $O(n\log n)$ (CDT in 2D) or $O(N_{x}N_{y}N_{z}+M)$ (Slab in 3D). Phase 1 runs Yen's $k$-shortest paths in $O(k\cdot|\mathcal{C}|\cdot(|\mathcal{P}|+|\mathcal{C}|\log|\mathcal{C}|))$; each Funnel evaluation is $O(L)$. Phase 2 operates on progressively smaller ellipsoid-filtered subgraphs. GNN inference is $O(L_{\text{GNN}}\cdot(|\mathcal{P}|\cdot h+|\mathcal{C}|\cdot h^{2}))$ with $L_{\text{GNN}}=3$, $h=128$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-F Complexity and System Design", "weight": 1.0} -->

The system comprises a C++ planning core ($\sim$`<!-- -->`{=html}5K LOC, OMPL-integrated ) and a Python GNN module (PyTorch + PyG, $\sim$`<!-- -->`{=html}150K parameters). GNN inference adds 10--50 ms latency. Default corridor budget: $k=8$ in 2D, $k=16$ ($\mathcal{G}$-DIP) or $k=32$ (unguided DIP) in 3D; 3D portal-face sampling uses $N_{s}=16$, refinement iterations $r=3$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

GNN-DIP is evaluated against unguided DIP and OMPL baselines (best result among iRRT\*, AIT\*, BIT\*, EIT\*, RRT\*) in both 2D and 3D environments. All experiments are executed on a single thread of an Intel i7 processor.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A 2D Evaluation", "weight": 1.0} -->

The 2D benchmark uses 310 polygon maps across 18 scenarios in four complexity tiers by CDT cell count: simple (14--74), medium (80--164), hard (280--672), and very hard (764--2372 cells). DIP uses $k=8$ with Funnel evaluation. DIP achieves an 89.5% win rate against OMPL at 10 ms on simple--hard maps but only 33% on very hard maps (1000+ cells) due to combinatorial corridor explosion. GNN guidance addresses this: on mega forest (1074 cells), unguided DIP fails while GNN-DIP succeeds with cost 1.295 (vs. 1.293 for OMPL); on tight labyrinth (1046 cells), both DIP methods achieve cost 1.737, outperforming OMPL's 1.799.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Decomposition Guarantees Full Reliability on 2D Narrow Passages", "weight": 1.0} -->

Table II reports PDT results (100 runs, 2 s budget) on four very hard 2D scenarios. DIP and $\mathcal{G}$-DIP achieve 100% success on all scenarios. On Bottleneck, all four sampling-based baselines fall below 3% success; on Tight Labyrinth, only EIT\* reaches 47%. On Mega Forest, EIT\* attains 99% success but at a median cost of 1.51---17% higher than $\mathcal{G}$-DIP's 1.29.

<!-- chunk {"id": "body-0038", "role": "body", "section": "GNN Scoring Provides Targeted Speedup on Combinatorially Hard Maps", "weight": 1.0} -->

$\mathcal{G}$-DIP reduces initial solve time by 4.6$\times$ on Mega Forest (48 ms vs. 223 ms) and 3.3$\times$ on Bottleneck (158 ms vs. 516 ms). On Bottleneck, $\mathcal{G}$-DIP also reduces median cost from 1.52 to 1.33 (12.5%), indicating that GNN-selected corridors are closer to optimal. On Tight Labyrinth and Cluttered Field, where DIP already solves in 16 ms and 35 ms, $\mathcal{G}$-DIP matches both cost and latency.

<!-- chunk {"id": "body-0039", "role": "body", "section": "GNN Scoring Provides Targeted Speedup on Combinatorially Hard Maps", "weight": 1.0} -->

Success rate / median cost Time to first solution TABLE II: PDT benchmark. Top: SR/median cost. Bottom: time to first solution. 2D: 100 runs, 2 s; 3D: 50 runs, 20 s. D-BN = Dense Bottleneck. Bold = best; “—” = no solution.

<!-- chunk {"id": "body-0040", "role": "body", "section": "GNN Scoring Provides Targeted Speedup on Combinatorially Hard Maps", "weight": 1.0} -->

Fig. 2 shows the convergence plots.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

To stress-test narrow-passage planning in 3D, we design four bottleneck scenarios where all feasible paths traverse walls with a single narrow door (width 0.035--0.05 in a unit cube). The probability of hitting a passage of width $\varepsilon$ scales as $\varepsilon^{3}$, making sampling-based discovery exponentially harder. Slab cells exactly represent free space regardless of passage width, and paths within convex cells are collision-free by construction.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

Bottleneck Office: $4\!\times\!4$ rooms separated by walls with one narrow door each, a horizontal floor partition, and 30 clutter boxes (181--190 obstacles).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

Bottleneck Maze: Recursive-division maze with single-door walls, two vertical zones, one floor partition, and 25 clutter boxes (129--175 obstacles).

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

Bottleneck Layers: Three layers of $3\!\times\!3$ rooms with narrow doors and narrow floor holes (radius 0.04--0.05), plus 30 clutter boxes (239--246 obstacles).

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

Dense BN Office: BN Office augmented with 120 extra clutter boxes, yielding $\sim$`<!-- -->`{=html}600 cells and $\sim$`<!-- -->`{=html}1600 portals (vs. $\sim$`<!-- -->`{=html}200 cells originally)---a search space where unguided $k$-shortest enumeration becomes a bottleneck.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B 3D Bottleneck Benchmark", "weight": 1.0} -->

Six planners (DIP, $\mathcal{G}$-DIP, BIT\*, AIT\*, iRRT\*, EIT\*) are evaluated via PDT over 50 runs with a 20 s budget on the most challenging map per scenario.

<!-- chunk {"id": "body-0047", "role": "body", "section": "DIP Maintains Perfect Reliability Across All 3D Scenarios", "weight": 1.0} -->

Table II reports all results. DIP and $\mathcal{G}$-DIP maintain 100% success on all four scenarios, including the dense variant with $\sim$`<!-- -->`{=html}600 cells. AIT\* fails entirely on BN Layers and the dense variant (0%), iRRT\* drops to 78% on BN Layers, and BIT\* to 98% on BN Office. EIT\* sustains 100% across all scenarios but requires the full 20 s budget.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Speed--Quality Tradeoff Between DIP and Asymptotic Planners", "weight": 1.0} -->

DIP produces initial solutions in 18--48 ms, compared to 110--470 ms for BIT\* (4--26$\times$ slower) and 73--100 ms for EIT\*. EIT\* achieves lower median costs (1.78--1.90 vs. DIP's 2.02--2.34) through asymptotic refinement; DIP trades this for immediate availability. On the dense variant, $\mathcal{G}$-DIP solves in 0.12 s---2.2$\times$ faster than DIP (0.26 s) and 3.6$\times$ faster than BIT\* (0.43 s); convergence plots (Fig. 2) confirm $\mathcal{G}$-DIP converges 2$\times$ faster on this variant.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Neural Corridor Scoring Reduces the Effective Branching Factor", "weight": 1.0} -->

The $k$-sweep ablation (Table III) confirms that $\mathcal{G}$-DIP at $k{=}8$ achieves cost 2.369, closely matching DIP $k{=}32$ at 2.346---a 3.5$\times$ total speedup at only 1.0% cost increase. The initialization gap is even larger: 64 ms vs. 419 ms (6.5$\times$), showing that GNN scores reduce the number of corridors that must be enumerated by a factor of four.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Neural Corridor Scoring Reduces the Effective Branching Factor", "weight": 1.0} -->

Fig. 2 presents the convergence plots.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Cross-Scenario Generalization", "weight": 1.0} -->

To evaluate whether GNN portal scoring generalizes beyond its training distribution, we conduct two transfer experiments on seven 3D bottleneck scenarios---the four from Sec. V-B plus Dense BN Maze ($\sim$`<!-- -->`{=html}450 cells) and two individual unseen maps (BN Office #15, BN Maze #20). Each is tested with 50 runs and a 20 s budget.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Leave-One-Type-Out (LOTO)", "weight": 1.0} -->

Training data spans four scenario families: office, maze, layers, and warehouse (261 samples across 14 subtypes). For each family $f$, we train a LOTO model $\mathcal{G}_{\neg f}$ on all data *excluding* family $f$ and evaluate it on scenarios from $f$. This directly measures cross-family transfer.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simple-to-Complex Transfer", "weight": 1.0} -->

A model $\mathcal{G}_{\text{sim}}$ is trained exclusively on four basic scenario types (forest, narrow passage, multi-room, cluttered)---none containing bottleneck structures---and tested on all complex bottleneck scenarios.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simple-to-Complex Transfer", "weight": 1.0} -->

Time to first solution TABLE IV: Cross-scenario generalization. LOTO¬f: trained excluding the test scenario’s family f. 𝒢sim: trained on basic scenarios only. All methods achieve 100% SR. (50 runs, 20 s.)

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simple-to-Complex Transfer", "weight": 1.0} -->

Table IV shows that LOTO models match the full model within 0.1% cost in 6 of 7 scenarios with equivalent or faster solve times. The single degradation is Dense BN Maze (+13% cost when maze data is excluded), localizable to maze-specific structural knowledge. $\mathcal{G}_{\text{sim}}$ matches or improves DIP solve times on all bottleneck scenarios (up to 2.3$\times$ speedup on dense variants) despite never encountering bottleneck structures during training, confirming that spatial features (distance, clearance, connectivity) transfer effectively to complex layouts.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Dynamic 2D Evaluation", "weight": 1.0} -->

We evaluate GNN-DIP for high-frequency replanning in dynamic 2D environments. Ten scenarios each consist of 10 time steps (100 instances total), with $\sim$`<!-- -->`{=html}50% static, 30% moving, and 20% toggling obstacles (15--58 per step, 96--358 CDT cells). GNN-DIP executes the full pipeline (CDT + GNN + DIP) per step; OMPL runs five planners and selects the best valid result. Both use a 0.5 s budget. OMPL paths are post-validated via dense collision checking (200 samples/unit); only collision-free paths count as successes.

<!-- chunk {"id": "body-0057", "role": "body", "section": "GNN-DIP Dominates Dynamic Replanning in Reliability, Latency, and Cost", "weight": 1.0} -->

GNN-DIP achieves 99% success (99/100, with the single failure being genuinely unsolvable) compared to OMPL's 40% after collision post-validation. GNN-DIP solves each step in 1.8--44 ms (50--280$\times$ speedup). Fig. 3 shows consistently lower path costs across all 10 scenarios, with the largest margins on multi-room environments (6--8% reduction), and solve times under 50 ms including the pipeline overhead (CDT $\sim$`<!-- -->`{=html}10 ms + GNN $\sim$`<!-- -->`{=html}5 ms).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Collision Safety by Construction", "weight": 1.0} -->

The success gap reflects a fundamental architectural difference. To quantify this, we measure OMPL's pre-validation success rate (planner finds *any* path) and post-validation rate (path survives dense collision checking) at two motion-validation resolutions: the default (${\sim}1\%$ of space extent) and $2{\times}$ ($0.5\%$, which doubles the per-edge checking cost). Within the same 0.5 s budget, pre-validation success is unchanged (489/500 vs. 488/500 individual planner runs), confirming that the planning algorithms succeed and the overhead is negligible. However, post-validation success rises from 36% to 79%---yet 21% of steps still contain paths that penetrate thin walls. Further increasing resolution would continue to reduce violations at the cost of exploring fewer edges per time budget. In contrast, DIP's collision safety is an *architectural guarantee*: CDT cells exactly partition free space along obstacle boundaries, so any path within a corridor is collision-free by construction, independent of resolution parameters.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

DIP exploits geometric structure for deterministic, fast initial solutions with 100% success on all scenarios, while sampling-based planners offer asymptotic optimality but suffer reduced reliability in narrow passages ($\varepsilon^{3}$ sampling probability in 3D). GNN guidance bridges the speed--quality gap: on small decompositions ($\sim$`<!-- -->`{=html}200 cells) the benefit is modest, but as complexity grows ($\sim$`<!-- -->`{=html}600+ cells) GNN scoring reduces the effective branching factor by $4\times$. Cross-scenario generalization (Table IV) confirms that learned spatial features transfer across scenario families and from simple to complex environments. Python-based inference adds 10--50 ms; ONNX Runtime integration would reduce this to sub-millisecond levels.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Extension: CBF-Guarded Execution", "weight": 1.0} -->

DIP produces collision-free *point* paths; for a disk robot of radius $r$, wall clearance must be enforced at runtime. Rather than inflating obstacles (requiring re-decomposition) or shrinking portals (over-conservative), we define a CBF on each corridor wall with endpoints $(w_{1},w_{2})$: where $\{q:h(q)\geq 0\}$ is the safe region. The DIP corridor structure is naturally suited for CBF integration because of two properties. First, *sparse constraints*: the filter monitors only walls of the current and neighboring corridor cells (${\leq}\,4$ constraints per step), far fewer than whole-space CBF formulations that check all obstacle boundaries. Second, *mostly-passive monitoring*: as Fig. 4(a) illustrates, in a typical CDT cell the path traverses a convex interior where $h(q)\gg 0$---the CBF constraint is trivially satisfied and the nominal controller runs unmodified.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Extension: CBF-Guarded Execution", "weight": 1.0} -->

CBF intervention activates only in the few narrow cells near bottlenecks where $h\approx r$ (Fig. 4(b)), making the filter effectively a lightweight *portal guard*. The resulting filter clamps forward speed to $v\leq\gamma h/|a|$ when heading toward a wall, preserving forward invariance without a QP solver.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-B Concluding Remarks", "weight": 1.0} -->

GNN-DIP integrates GNN portal scoring with a two-phase decomposition-informed planner, with formal completeness and convergence guarantees. Key findings: DIP achieves 89.5% win rate over OMPL at 10 ms in 2D, with GNN guidance solving tight labyrinths in under 20 ms; in 3D bottleneck environments (129--246 obstacles, narrow doors of width 0.035--0.05), DIP achieves 100% success vs. 0--100% for sampling-based planners, with 3--20$\times$ speed advantage over BIT\*; $\mathcal{G}$-DIP at $k{=}8$ matches DIP $k{=}32$ at 3.5$\times$ speedup on dense 3D ($\sim$`<!-- -->`{=html}600 cells); in dynamic 2D, GNN-DIP achieves 99% vs. 40% success with 50--280$\times$ speedup.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B Concluding Remarks", "weight": 1.0} -->

Future work will address improving 3D path quality via gradient-based refinement within convex corridors, extending Slab decomposition to non-axis-aligned obstacles, C++ GNN integration via ONNX Runtime for sub-millisecond inference, and experimental validation of the CBF execution layer for finite-size robots navigating narrow passages.
