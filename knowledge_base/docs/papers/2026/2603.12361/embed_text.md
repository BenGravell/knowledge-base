<!-- arxiv-full-text:v1 {"arxiv_id": "2603.12361", "source": "arxiv-html"} -->

## Introduction

Motion planning in cluttered environments is a fundamental problem in robotics. Among its open challenges, narrow passages stand out: in environments with tight doorways, narrow gaps, or double enclosures, the only feasible routes pass through regions occupying a vanishingly small fraction of the space, making their reliable discovery essential for any practical planner.

Sampling-based planners, including RRT\*, BIT\*, Informed RRT\* (iRRT\*), APT\*, and their variants, provide asymptotic optimality guarantees but face a dual challenge in narrow passages. First, the probability of randomly sampling inside a passage of width $\varepsilon$ scales as $\varepsilon^{d}$, so narrow gaps become exponentially harder to discover in higher dimensions. Second, even when a sample lands inside a narrow passage, the straight-line segments connecting it to neighboring samples run close to obstacle boundaries, complicating collision checking at finite resolution. These challenges compound, so denser sampling or finer collision checking yields diminishing returns.

Decomposition-based planners address both challenges structurally. By partitioning the free space $\mathcal{F}$ into convex cells and constructing a cell adjacency graph, every passage---no matter how narrow---is represented exactly as a cell boundary (portal), so no bottleneck region is missed. Moreover, any path within a convex cell is collision-free by definition, eliminating resolution-dependent collision checking entirely. The continuous planning problem thus reduces to a discrete corridor search followed by local path optimization within each corridor.

The principal limitation of decomposition-based approaches is the corridor selection problem: the number of distinct corridors from start to goal grows combinatorially with the number of cells. In environments with hundreds to thousands of cells, the $k$-shortest path search via Yen's algorithm needs accurate edge weights, yet the default centroid-distance heuristic $w(c_{i},c_{j})=\|z_{i}-z_{j}\|$ correlates poorly with actual path cost for elongated cells, narrow passages, or asymmetric obstacle layouts.

We address the corridor selection problem by training a GNN on the cell adjacency graph to predict portal-level scores. Each portal $p_{ij}$ (the shared boundary between adjacent cells $c_{i}$ and $c_{j}$) receives a score $s_{ij}\in$ indicating the probability that it lies on a near-optimal corridor. These scores modulate edge weights via $w(c_{i},c_{j})=d(c_{i},c_{j})\cdot\exp(-\beta\cdot s_{ij})$, concentrating the $k$-shortest path search on promising regions. Importantly, the modulation is continuous---no corridors are pruned---thereby preserving completeness while improving the quality of initial corridor candidates.

Fig. 1 illustrates the GNN-DIP ($\mathcal{G}$-DIP) pipeline on a labyrinth with 50 polygon obstacles: CDT produces 385 triangular cells, the GNN isolates a 73-cell corridor containing the near-optimal path (${\sim}81\%$ search-space reduction), parallel Funnel evaluation yields the initial solution in under 20 ms, and Phase 2 refines it within a shrinking informed ellipsoid.

Figure 1: GNN-DIP pipeline on a labyrinth with polygon obstacles. (a) Planning problem with start (⋆) and goal (∘). (b) CDT decomposes the free space into 385 triangular cells. (c) The GNN selects a corridor of 73 cells (light blue), and the Funnel algorithm computes the initial path (green) in parallel across corridor candidates. (d) Phase 2 refines the solution within a shrinking informed ellipsoid (orange dashed → red solid).

The contributions of this paper are: A GNN-based portal scoring framework on cell adjacency graphs, with engineered node/edge features and a training pipeline using focal loss and multi-label supervision (Section III).

A two-phase Decomposition-Informed Planner (DIP) that combines GNN-guided corridor search with an *adaptation of informed-set pruning* to the cell adjacency graph and Funnel-based corridor evaluation, with proofs of completeness and convergence (Section IV).

Comprehensive experiments spanning 2D (310 maps, 18 scenarios), 3D bottleneck environments (4 scenarios, 50 PDT runs each), and dynamic 2D environments (100 planning instances), demonstrating 2--280$\times$ speedup, 99--100% success rates, and collision safety by construction (Section V).

## Preliminaries and Related Work

### II-A Decomposition-Based Motion Planning

Cell decomposition methods partition the free space into simple regions and plan over the resulting adjacency graph. Exact cell decomposition constructs cells whose union equals the free space, whereas approximate methods employ regular grids or adaptive subdivisions. Constrained Delaunay Triangulation (CDT) with parity-based face classification provides a well-studied 2D decomposition with robust implementations in CGAL. The Funnel algorithm computes the exact Euclidean shortest path through a sequence of adjacent convex polygons in $O(n)$ time, where $n$ is the total number of portal endpoints.

In 3D, exact convex decomposition of general polyhedral free space is computationally expensive. For environments with axis-aligned box (AABB) obstacles, a Slab decomposition exploits obstacle face alignment to produce an exact convex decomposition in near-linear time. Strub and Gammell introduced AIT\* and EIT\*, which integrate lazy search and informed sampling. Recent advances include tree-grafting bidirectional planners, estimated informed anytime search with adaptive sampling, and genetic programming heuristics for informed trees. The Planner Developer Tools (PDT) framework provides standardized benchmarking infrastructure for OMPL-compatible planners.

### II-B Relation to Graphs of Convex Sets

Closest to our decomposition-plus-adjacency-graph formulation is the Graphs of Convex Sets (GCS) framework, which also casts planning as a shortest-path problem over a graph whose vertices are convex free-space regions. Both reduce planning to selecting a sequence of convex sets, but differ in how that selection is resolved. GCS embeds the discrete selection and the continuous trajectory into a single mixed-integer convex program solved via a tight convex relaxation, achieving global optimality at the cost of a centralized optimization that scales with the graph. GNN-DIP instead *decouples* the two: a GNN gives learned, millisecond-scale guidance that biases the $k$-shortest corridor search (Sec. IV), and each corridor's path is recovered exactly (Funnel, 2D) or near-exactly (portal-face sampling, 3D). We trade GCS's global-optimality guarantee for far faster initial solutions, anytime refinement, completeness, and high-frequency replanning, while both inherit collision-safety-by-construction from the decomposition. Finally, for the narrow-passage regime we target, exact decomposition offers a further guarantee: every passage appears as a cell boundary, so none is missed. The convex regions underlying GCS, by contrast, are inflated from seed configurations and may fail to cover very thin passages, reintroducing at the region-generation stage the same seeding difficulty that exact decomposition eliminates.

### II-C Learning and GNNs for Motion Planning

Neural approaches to motion planning include learned samplers, conditional generative models, and reinforcement learning, all operating in continuous configuration space without exploiting cell decomposition structure. GNNs have been applied to roadmap graphs for collision prediction, neural planning, and edge cost learning. These operate on roadmap graphs (nodes = configurations, edges = local paths), whereas our GNN operates on the cell adjacency graph (nodes = free-space cells, edges = portals)---a fundamentally different and more compact representation. Informed approaches exploit ellipsoidal or zonotope subsets; our GNN guidance is complementary, biasing corridor search before any solution is found.

### II-D Problem Formulation

This section formalizes the key components of the proposed framework. Throughout, $\mathcal{W}\subseteq\mathbb{R}^{d}$ ($d\in\{2,3\}$) denotes the workspace.

### Definition 1 (Motion Planning Problem)

Given a workspace $\mathcal{W}$ with obstacles $\mathcal{O}=\{O_{1},\ldots,O_{m}\}$ (arbitrary simple polygons in 2D, axis-aligned boxes in 3D), the free space is $\mathcal{F}=\mathcal{W}\setminus\bigcup_{i=1}^{m}O_{i}$. Given start and goal configurations $q_{s},q_{g}\in\mathcal{F}$, the *optimal motion planning problem* seeks a continuous path $\sigma^{*}:\to\mathcal{F}$ with $\sigma=q_{s}$, $\sigma=q_{g}$, minimizing the path length $\ell(\sigma)=\int_{0}^{1}\|\dot{\sigma}(t)\|\,dt$:

### Definition 2 (Free-Space Decomposition)

A *free-space decomposition* of $\mathcal{F}$ is a finite collection of closed convex cells $\mathcal{C}=\{c_{1},\ldots,c_{n}\}$ such that (i) $\bigcup_{i=1}^{n}c_{i}=\overline{\mathcal{F}}$ (coverage), (ii) $\mathrm{int}(c_{i})\cap\mathrm{int}(c_{j})=\emptyset$ for $i\neq j$ (non-overlapping interiors), and (iii) each $c_{i}$ is convex. In 2D, we use Constrained Delaunay Triangulation (CDT) with obstacle edges as constraints and parity-based classification to identify free faces. In 3D with axis-aligned box obstacles, we employ a *Slab convex decomposition*: obstacle face coordinates define axis-aligned splitting planes; obstacle cells are removed and adjacent free cells are greedily merged, producing a compact set of convex boxes.

### Definition 3 (Cell Adjacency Graph)

The *cell adjacency graph* $G=(\mathcal{C},\mathcal{P})$ is defined over the free-space cells of Definition 2. ‣ II-D Problem Formulation ‣ II Preliminaries and Related Work ‣ GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning"), with cells as nodes and portals as edges. A *portal* $p_{ij}\in\mathcal{P}$ exists between cells $c_{i}$ and $c_{j}$ if they share a $(d{-}1)$-dimensional face (an edge segment in 2D, a rectangular face in 3D). Each portal $p_{ij}$ is characterized by its geometric attributes: endpoints $\{a_{ij},b_{ij}\}$ and midpoint $m_{ij}$, with size measure $\lambda_{ij}$ defined as the segment length $\|a_{ij}-b_{ij}\|$ in 2D or the face area in 3D.

### Definition 4 (Corridor)

A *corridor* $\pi=(c_{i_{1}},c_{i_{2}},\ldots,c_{i_{L}})$ is a path in $G$ from the cell containing $q_{s}$ to the cell containing $q_{g}$. The corridor defines a connected region $\mathcal{R}_{\pi}=\bigcup_{\ell=1}^{L}c_{i_{\ell}}$ through which a collision-free path must pass. The *corridor cost* $\ell(\pi)$ is the length of the shortest path in $\mathcal{F}$ that traverses the cells of $\pi$ in order.

## GNN Portal Scoring

The corridor selection problem can be formulated as an edge classification task on the cell adjacency graph: for each portal $p_{ij}$, predict whether it lies on a near-optimal corridor. A GNN is trained for this task, and its scores bias edge weights in the corridor search.

### III-A Graph Representation and Feature Engineering

The graph $G=(\mathcal{C},\mathcal{P})$ is represented as directed with bidirectional edges (each portal appears twice); each cell $c_{i}$ carries node features $\mathbf{x}_{i}\in\mathbb{R}^{d_{n}}$ and each portal $p_{ij}$ edge features $\mathbf{e}_{ij}\in\mathbb{R}^{d_{e}}$.

### III-A1 Node Features ($d_{n}=11$ in 2D) and Edge Features ($d_{e}=9$ in 2D)

Table I and Edge Features (𝑑_𝑒=9 in 2D) ‣ III-A Graph Representation and Feature Engineering ‣ III GNN Portal Scoring ‣ GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning") lists the complete 2D feature set. Node features encode cell geometry (area, aspect ratio $\rho_{i}=e_{\max}/e_{\min}$), spatial relationships to the query (distances to start, goal, and the start--goal line $d_{\perp}$), and role indicators. Edge features encode portal geometry, spatial context, and inter-cell relationships. The relative angle $\theta_{ij}=\angle(p_{ij})-\angle(\overrightarrow{q_{s}q_{g}})$ captures alignment between the portal and the global query direction. For the 3D Slab decomposition, features are extended to $d_{n}{=}14$ and $d_{e}{=}13$ by adding volumetric cell descriptors (volume, size along each axis, clearance) and 3D portal attributes (face area, portal height, normal axis).

Start cell flag Cell–cell dist.

Goal cell flag TABLE I: GNN input features: node (cell) and edge (portal).

### III-B GNN Architecture

The architecture follows an encode--process--decode pattern. Raw node features are projected to hidden dimension $h=128$ via a linear layer with batch normalization (BN) and ReLU. In 2D, three GCN layers with symmetric normalization, BN, and dropout ($p{=}0.15$) process the node embeddings; layers 2--3 use two-layer-skip residual connections. For 3D, GCN is replaced by GATv2 (3 layers, 4 attention heads) to better capture the irregular connectivity of Slab cells; the remaining architecture is identical.

For each portal $p_{ij}$, the score is predicted by an MLP ($\mathbb{R}^{2h+d_{e}}\to h\to 32\to 1$, ReLU activations) on the concatenation of endpoint embeddings and edge features: where $\mathrm{sigm}(\cdot)=1/(1+e^{-x})$ is the sigmoid function (distinguished from path $\sigma$).

### III-C Training

### III-C1 Label Generation

Training labels are generated from OMPL baselines (iRRT\*, AIT\*, BIT\*, RRT\*) run on each map with a sufficient time budget; portals on near-optimal corridors of the collected paths are labeled positive. Let $\sigma_{\text{ref}}$ denote the shortest path found across all baseline runs: where $\epsilon=0.1$ (10% suboptimality threshold). Since $\sigma_{\text{ref}}$ is the best solution found rather than the true optimum $\sigma^{*}$, label noise may arise when baselines have not converged; in practice, running four planners with a 10 s budget per map yields near-optimal references. This multi-label scheme assigns positive labels to portals on any near-optimal corridor, capturing the multiplicity of good solutions. The resulting label distribution is severely imbalanced: typically less than 5% of portals are positive.

### III-C2 Focal Loss

To address the extreme class imbalance, focal loss is adopted: where $p_{t}=\hat{s}\cdot y+(1-\hat{s})(1-y)$ is the model's estimated probability for the true class, $\alpha_{t}=\alpha y+(1-\alpha)(1-y)$ balances positive/negative contributions, and $\gamma$ is the focusing parameter. We use $\alpha=0.85$ and $\gamma=2.0$. The $(1-p_{t})^{\gamma}$ factor down-weights well-classified negatives, focusing gradient updates on hard positives---the critical portals that the model initially misclassifies.

### III-C3 Optimization

Training employs Adam (initial learning rate $10^{-3}$, weight decay $10^{-4}$) with cosine annealing and early stopping based on validation F1 score (patience 30 epochs). Data are split using stratified sampling (20% validation ratio). The model ($\sim$`<!-- -->`{=html}150K parameters) trains in under 5 minutes on a single GPU.

## Decomposition-Informed Planner

The Decomposition-Informed Planner (DIP) operates in two phases on the cell adjacency graph $G$. Phase 1 performs GNN-guided $k$-shortest corridor search with corridor evaluation; Phase 2 refines the search using an informed ellipsoid derived from the current best solution.

### IV-A GNN-Guided Edge Weight Integration

Given GNN-predicted portal scores $\{\hat{s}_{ij}\}$, we define modified edge weights: where $d(c_{i},c_{j})=\|z_{i}-z_{j}\|$ is the centroid distance and $\beta>0$ is a temperature parameter (we use $\beta=3.0$).

### Proposition 1 (Properties of GNN Edge Weights)

The weight is strictly positive and continuous; it recovers the centroid-distance baseline when $\hat{s}_{ij}=0$ (graceful degradation); and higher scores yield lower weights, concentrating the $k$-shortest search on predicted near-optimal portals.

### IV-B Phase 1: $k$-Shortest Corridor Search

Phase 1 applies Yen's algorithm to find $k$ shortest paths in $G$ from the start cell $c_{s}$ to the goal cell $c_{g}$, using edge weights $w_{\text{GNN}}$ when available and centroid distances $d(\cdot,\cdot)$ otherwise. Each corridor is evaluated using the Funnel algorithm (2D) or portal-face sampling with layered-graph DP (3D); the best solution provides an initial cost bound $c_{\text{best}}^{}$ that seeds Phase 2.

### IV-C Phase 2: Informed Ellipsoid Corridor Refinement

### Definition 5 (Informed Ellipsoid)

Given the current best cost $c_{\text{best}}$, the *informed ellipsoid* is: A portal $p_{ij}$ is *informative* if it intersects the ellipsoid, i.e., $p_{ij}\cap\mathcal{E}(c_{\text{best}})\neq\emptyset$, or equivalently $\min_{x\in p_{ij}}(\|x-q_{s}\|+\|x-q_{g}\|)\leq c_{\text{best}}$.

The set in Definition 5. ‣ IV-C Phase 2: Informed Ellipsoid Corridor Refinement ‣ IV Decomposition-Informed Planner ‣ GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning") is the admissible $L^{2}$ informed set of Informed RRT\*, and tightening it as $c_{\text{best}}$ decreases mirrors the informed pruning of AIT\*/EIT\*. Our contribution is not the informed set itself but its transfer to the decomposition setting: we prune *portals of the cell adjacency graph* rather than sample configurations directly, and combine it with GNN-scored corridors so refinement concentrates on the corridors the network favors---yielding deterministic anytime behavior on the discrete graph, unlike sampling-based informed methods that must still sample and connect within the set.

Phase 2 iteratively re-runs the $k$-shortest path search on $G$, restricted to portals inside $\mathcal{E}(c_{\text{best}})$. Only corridors not yet contained in the evaluated set $\mathcal{S}$ are passed to the corridor evaluator (Funnel in 2D, portal-face sampling in 3D). When a better corridor is found, the ellipsoid shrinks accordingly; otherwise, the corridor budget $k^{\prime}$ is doubled up to $4k$, after which the loop terminates.

1 \ALC@tlmInput: 𝒲, qs, qg, GNN model fθ, corridor budget k, timeout T 2 \ALC@tlmOutput: Best path σ* and cost c* 3 \ALC@tlm4 Decompose ℱ into cells; build G = (𝒞, 𝒫) 7 \ALC@tlm8 wij ← d(ci, cj) ⋅ exp (−β ⋅ ŝij), ∀ (ci, cj) ∈ 𝒫 11 \ALC@tlm12 Πk ← Yen(G, cs, cg, k, w) 13 \ALC@tlm14 for π ∈ Πk do 15 \ALC@tlm16 (ℓπ, σπ) ← Eval(π, qs, qg); 𝒮 ← 𝒮 ∪ {π} 24 \ALC@tlm25 while elapsed time < T do 26 \ALC@tlm27 𝒫′ ← {pij ∈ 𝒫: minx ∈ pij(∥x − qs∥+∥x − qg∥) ≤ c*} 28 \ALC@tlm29 Π′ ← Yen(G|𝒫′, cs, cg, k′, w) 30 \ALC@tlm31 improved ← false 32 \ALC@tlm33 for π ∈ Π′ \ 𝒮 do 34 \ALC@tlm35 (ℓπ, σπ) ← Eval(π, qs, qg); 𝒮 ← 𝒮 ∪ {π} 38 \ALC@tlm39 c* ← ℓπ; σ* ← σπ; improved ← true 40 \ALC@tlm41 if ¬ improved 42 \ALC@tlm43 k′ ← min (2k′, 4k) 46 \ALC@tlm47 break 48 \ALC@tlm49 return (σ*, c*) Algorithm 1: GNN-DIP: Decomposition-Informed Planner

### IV-D Theoretical Properties

### Theorem 1 (Completeness of DIP)

If a collision-free path from $q_{s}$ to $q_{g}$ exists in $\mathcal{F}$, and the decomposition $\mathcal{C}$ covers $\mathcal{F}$ with $q_{s},q_{g}$ contained in cells of $G$, then DIP (Algorithm 1) finds a solution path.

### Proof sketch

GNN weights preserve graph topology (all edges remain with positive weights), so Yen's algorithm can discover any reachable corridor. For Phase 2, any portal on an optimal corridor satisfies the ellipsoid condition by the triangle inequality, so it is never pruned. ∎

### Theorem 2 (Convergence of DIP)

The Phase 2 loop of Algorithm 1 terminates in finite iterations. Moreover, each iteration either discovers a strictly better corridor (decreasing $c^{*}$) or explores no new corridors.

### Proof sketch

The number of distinct corridors is finite; each is evaluated at most once. Each iteration either discovers a new corridor or triggers termination, so the loop terminates. ∎

### IV-E Corridor Evaluation

In 2D, the Funnel algorithm computes the exact shortest path through a corridor of $L$ convex polygons in $O(L)$ time via string-pulling. In 3D, we employ portal-face sampling: $N_{s}$ points are sampled uniformly on each portal face, forming a layered DAG from $q_{s}$ through portal samples to $q_{g}$. A forward DP sweep finds the shortest path in $O(L\cdot N_{s}^{2})$ time---collision-free by convexity. Adaptive Gaussian re-sampling refines the path for up to $r=3$ iterations.

### IV-F Complexity and System Design

Decomposition is $O(n\log n)$ (CDT in 2D) or $O(N_{x}N_{y}N_{z}+M)$ (Slab in 3D). Phase 1 runs Yen's $k$-shortest paths in $O(k\cdot|\mathcal{C}|\cdot(|\mathcal{P}|+|\mathcal{C}|\log|\mathcal{C}|))$; each Funnel evaluation is $O(L)$. Phase 2 operates on progressively smaller ellipsoid-filtered subgraphs. GNN inference is $O(L_{\text{GNN}}\cdot(|\mathcal{P}|\cdot h+|\mathcal{C}|\cdot h^{2}))$ with $L_{\text{GNN}}=3$, $h=128$.

The system comprises a C++ planning core ($\sim$`<!-- -->`{=html}5K LOC, OMPL-integrated ) and a Python GNN module (PyTorch + PyG, $\sim$`<!-- -->`{=html}150K parameters). GNN inference adds 10--50 ms latency. Default corridor budget: $k=8$ in 2D, $k=16$ ($\mathcal{G}$-DIP) or $k=32$ (unguided DIP) in 3D; 3D portal-face sampling uses $N_{s}=16$, refinement iterations $r=3$.

## Experiments

GNN-DIP is evaluated against unguided DIP and OMPL baselines (best of iRRT\*, AIT\*, BIT\*, EIT\*, RRT\*) in 2D and 3D, on a single thread of an Intel i7 processor.

### V-A 2D Evaluation

The 2D benchmark uses 310 polygon maps across 18 scenarios in four complexity tiers by CDT cell count: simple (14--74), medium (80--164), hard (280--672), and very hard (764--2372 cells). With $k{=}8$ and Funnel evaluation, DIP achieves an 89.5% win rate against OMPL at 10 ms on simple--hard maps but only 33% on very hard maps (1000+ cells) due to combinatorial corridor explosion. GNN guidance addresses this: on mega forest (1074 cells), unguided DIP fails while GNN-DIP succeeds with cost 1.295 (vs. 1.293 for OMPL); on tight labyrinth (1046 cells), both DIP methods achieve cost 1.737, outperforming OMPL's 1.799.

### Decomposition Guarantees Full Reliability on 2D Narrow Passages

Table II reports PDT results (100 runs, 2 s budget) on four very hard 2D scenarios. DIP and $\mathcal{G}$-DIP achieve 100% success on all scenarios. On Bottleneck, all four sampling-based baselines fall below 3% success; on Tight Labyrinth, only EIT\* reaches 47%. On Mega Forest, EIT\* attains 99% success but at a median cost of 1.51---17% higher than $\mathcal{G}$-DIP's 1.29.

### GNN Scoring Provides Targeted Speedup on Combinatorially Hard Maps

$\mathcal{G}$-DIP reduces initial solve time by 4.6$\times$ on Mega Forest (48 ms vs. 223 ms) and 3.3$\times$ on Bottleneck (158 ms vs. 516 ms). On Bottleneck, $\mathcal{G}$-DIP also reduces median cost from 1.52 to 1.33 (12.5%), indicating that GNN-selected corridors are closer to optimal. On Tight Labyrinth and Cluttered Field, where DIP already solves in 16 ms and 35 ms, $\mathcal{G}$-DIP matches both cost and latency.

Success rate / median cost Time to first solution TABLE II: PDT benchmark. Top: SR/median cost. Bottom: time to first solution. 2D: 100 runs, 2 s; 3D: 50 runs, 20 s. D-BN = Dense Bottleneck. Bold = best; “—” = no solution.

Fig. 2 shows the convergence plots.

### V-B 3D Bottleneck Benchmark

To stress-test narrow-passage planning in 3D, we design four bottleneck scenarios where all feasible paths traverse walls with a single narrow door (width 0.035--0.05 in a unit cube)---a regime where the $\varepsilon^{3}$ hit probability makes sampling-based discovery exponentially hard, while Slab cells capture every door exactly. *Bottleneck Office*: $4{\times}4$ rooms with one narrow door per wall, a floor partition, and 30 clutter boxes (181--190 obstacles); *Bottleneck Maze*: a recursive-division maze with single-door walls, two vertical zones, one floor partition, and 25 clutter boxes (129--175); *Bottleneck Layers*: three layers of $3{\times}3$ rooms with narrow doors and floor holes (radius 0.04--0.05), plus 30 clutter boxes (239--246); *Dense BN Office*: BN Office with 120 extra clutter boxes, yielding $\sim$`<!-- -->`{=html}600 cells and $\sim$`<!-- -->`{=html}1600 portals (vs. $\sim$`<!-- -->`{=html}200 originally), where unguided $k$-shortest enumeration becomes the bottleneck.

All six planners are evaluated via PDT (50 runs, 20 s budget) on the most challenging map per scenario.

### DIP Maintains Perfect Reliability Across All 3D Scenarios

Table II reports all results. DIP and $\mathcal{G}$-DIP maintain 100% success on all four scenarios, including the dense variant with $\sim$`<!-- -->`{=html}600 cells. AIT\* fails entirely on BN Layers and the dense variant (0%), iRRT\* drops to 78% on BN Layers, and BIT\* to 98% on BN Office. EIT\* sustains 100% across all scenarios but requires the full 20 s budget.

### Speed--Quality Tradeoff Between DIP and Asymptotic Planners

DIP produces initial solutions in 18--48 ms, compared to 110--470 ms for BIT\* (4--26$\times$ slower) and 73--100 ms for EIT\*. EIT\* achieves lower median costs (1.78--1.90 vs. DIP's 2.02--2.34) through asymptotic refinement; DIP trades this for immediate availability. On the dense variant, $\mathcal{G}$-DIP solves in 0.12 s---2.2$\times$ faster than DIP (0.26 s) and 3.6$\times$ faster than BIT\* (0.43 s); convergence plots (Fig. 2) confirm $\mathcal{G}$-DIP converges 2$\times$ faster on this variant.

### Neural Corridor Scoring Reduces the Effective Branching Factor

A $k$-sweep ablation on Dense BN Office (5 maps $\times$ 5 seeds) confirms that $\mathcal{G}$-DIP at $k{=}8$ matches DIP at $k{=}32$ (2.346; 419 ms; 6940 ms): a 1.0% cost increase buys a 3.5$\times$ total and 6.5$\times$ initialization speedup, showing that GNN scores cut the number of corridors that must be enumerated by ${\sim}4\times$.

Figure 2: PDT convergence plots: success rate (top) and median cost (bottom) vs. time. Top row: 2D very hard scenarios (100 runs, 2 s). Bottom row: 3D bottleneck scenarios (50 runs, 20 s) and Dense BN Office (∼600 cells).

### V-C Cross-Scenario Generalization

To evaluate whether GNN portal scoring generalizes beyond its training distribution, we conduct two transfer experiments on seven 3D bottleneck scenarios---the four from Sec. V-B plus Dense BN Maze ($\sim$`<!-- -->`{=html}450 cells) and two individual unseen maps (BN Office #15, BN Maze #20). Each is tested with 50 runs and a 20 s budget.

### Leave-One-Type-Out (LOTO)

Training data spans four scenario families: office, maze, layers, and warehouse (261 samples across 14 subtypes). For each family $f$, we train a LOTO model $\mathcal{G}_{\neg f}$ on all data *excluding* family $f$ and evaluate it on scenarios from $f$.

### Simple-to-Complex Transfer

A model $\mathcal{G}_{\text{sim}}$ is trained exclusively on four basic scenario types (forest, narrow passage, multi-room, cluttered)---none containing bottleneck structures---and tested on all complex bottleneck scenarios.

Time to first solution TABLE III: Cross-scenario generalization. LOTO¬f: trained excluding the test scenario’s family f. 𝒢sim: trained on basic scenarios only. All methods achieve 100% SR. (50 runs, 20 s.)

Table III shows that LOTO models match the full model within 0.1% cost in 6 of 7 scenarios with equivalent or faster solve times. The single degradation, Dense BN Maze (+13% when maze data is excluded), is attributable to maze-specific structure. $\mathcal{G}_{\text{sim}}$ matches or improves DIP solve times on all bottleneck scenarios (up to 2.3$\times$ speedup on dense variants) despite never encountering bottleneck structures during training, confirming that spatial features (distance, clearance, connectivity) transfer effectively to complex layouts.

### V-D Dynamic 2D Evaluation

We evaluate GNN-DIP for high-frequency replanning in dynamic 2D environments. Ten scenarios each consist of 10 time steps (100 instances total), with $\sim$`<!-- -->`{=html}50% static, 30% moving, and 20% toggling obstacles (15--58 per step, 96--358 CDT cells). GNN-DIP executes the full pipeline (CDT + GNN + DIP) per step; OMPL runs five planners and selects the best valid result. Both use a 0.5 s budget. OMPL paths are post-validated via dense collision checking (200 samples/unit); only collision-free paths count as successes.

### GNN-DIP Dominates Dynamic Replanning in Reliability, Latency, and Cost

GNN-DIP achieves 99% success (99/100; the single failure is genuinely unsolvable) vs. OMPL's 40% after collision post-validation, solving each step in 1.8--44 ms (50--280$\times$ speedup) including the pipeline overhead (CDT $\sim$`<!-- -->`{=html}10 ms + GNN $\sim$`<!-- -->`{=html}5 ms). Fig. 3 shows consistently lower path costs on all 10 scenarios, with the largest margins (6--8%) on multi-room environments.

Figure 3: Dynamic 2D benchmark across 10 scenarios: (a) average path cost, (b) average solve time (GNN-DIP 1.8–44 ms vs. OMPL’s 0.5 s budget), (c) success rate after collision post-validation (99% vs. 40%).

### Collision Safety by Construction

The success gap reflects a fundamental architectural difference. To quantify this, we measure OMPL's pre-validation success rate (planner finds *any* path) and post-validation rate (path survives dense collision checking) at two motion-validation resolutions: the default (${\sim}1\%$ of space extent) and $2{\times}$ ($0.5\%$, which doubles the per-edge checking cost). Within the same 0.5 s budget, pre-validation success is unchanged (489/500 vs. 488/500 individual planner runs), confirming that the planning algorithms succeed and the overhead is negligible. However, post-validation success rises from 36% to 79%---yet 21% of steps still contain paths that penetrate thin walls. Raising resolution further would reduce violations at the cost of exploring fewer edges per budget. DIP needs no such tuning: CDT cells partition free space along obstacle boundaries, so corridor paths are collision-free by construction.

## Discussion and Conclusion

DIP exploits geometric structure for deterministic, fast initial solutions, while sampling-based planners offer asymptotic optimality at reduced reliability in narrow passages. GNN guidance matters most as complexity grows: the benefit is modest at $\sim$`<!-- -->`{=html}200 cells but reaches a $4\times$ branching-factor reduction at $\sim$`<!-- -->`{=html}600+ cells, and cross-scenario generalization (Table III) confirms the learned features are not layout-specific.

### VI-A Extension: CBF-Guarded Execution

DIP produces collision-free *point* paths; for a disk robot of radius $r$, wall clearance must be enforced at runtime. Rather than inflating obstacles (requiring re-decomposition) or shrinking portals (over-conservative), we define a CBF on each corridor wall with endpoints $(w_{1},w_{2})$: where $\{q:h(q)\geq 0\}$ is the safe region. The corridor structure suits CBF integration for two reasons: (i) *sparse constraints*---only walls of the current and neighboring corridor cells are monitored (${\leq}\,4$ per step), far fewer than whole-space formulations; (ii) *mostly-passive monitoring*---in a typical cell the path stays in the convex interior where $h(q)\gg 0$ and the nominal controller runs unmodified (Fig. 4a), with intervention only in the few narrow cells where $h\approx r$ (Fig. 4b). The filter clamps forward speed to $v\leq\gamma h/|a|$ when heading toward a wall, preserving forward invariance without a QP solver.

Figure 4: CBF behavior within CDT cells. (a) Typical cell: path traverses the convex interior far from the wall, h(q) ≫ 0, CBF inactive. (b) Narrow cell near a bottleneck: path forced close to wall, h ≈ r, CBF activates to enforce clearance.

### VI-B Limitations and Scope

*Workspace vs. configuration space.* GNN-DIP operates in the low-dimensional workspace $\mathcal{W}\subseteq\mathbb{R}^{d}$ ($d\in\{2,3\}$) for point/disk robots, and its guarantees rest on an *exact* convex decomposition of free space. This does not lift directly to the high-dimensional C-spaces of articulated systems (e.g., 6--7-DOF arms): C-space obstacles are curved and non-convex, no exact convex decomposition is known, and the cell count grows rapidly with dimension. The method thus targets low-DOF holonomic and workspace planning. To lift it to configuration space, we plan to follow the Graphs of Convex Sets line of work and replace the exact decomposition with an *approximate convex covering*: we adopt the region-inflation algorithm IRIS ---more precisely, its extension to configuration spaces with nonconvex obstacles (IRIS-NP) ---to generate a sparse set of large, possibly overlapping convex regions directly in C-space, on which our GNN portal scoring then guides the shortest-path search over the resulting region graph. This trades the constructive completeness of an exact decomposition for scalability, pairing GCS-style regions with learned corridor selection.

*3D obstacle geometry.* Slab decomposition is exact only for axis-aligned box (AABB) obstacles, so general polyhedral, curved, or non-convex geometries are unsupported and the 3D results should be read under this restriction; the 2D CDT pipeline already admits arbitrary simple polygons. A general 3D pipeline could substitute an approximate convex decomposition (e.g., V-HACD ), splitting each obstacle into convex pieces on which the same graph, portal features, and GNN scoring apply. The trade-offs are a larger, geometry-dependent cell count, general convex-polygon portals in place of rectangular faces, and loss of exactness where curved boundaries are approximated.

### VI-C Concluding Remarks

GNN-DIP integrates GNN portal scoring with a two-phase decomposition-informed planner, with formal completeness and convergence guarantees. Across static 2D (310 maps), 3D bottleneck (129--246 obstacles), and dynamic 2D benchmarks, it achieves 99--100% success with 2--280$\times$ speedups over sampling-based baselines, and GNN guidance matches unguided search quality at a $4\times$ smaller corridor budget.

Future work will address gradient-based 3D path refinement within convex corridors, the C-space and general-geometry extensions outlined in Sec. VI-B, C++/ONNX integration for sub-millisecond inference, and experimental validation of the CBF execution layer.
