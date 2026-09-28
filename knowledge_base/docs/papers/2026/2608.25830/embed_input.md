<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Anytime Global Tensor Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Global Tensor Motion Planning (GTMP) solves motion planning with batched tensor operations over a layered multipartite graph. We generalize GTMP so that adjacent-layer edges are realized by any black-box local planner (e.g., linear interpolation, splines, sampling-based planning, trajectory optimization, or generative sampling). We provide two anytime policies on top of this generalization: Anytime GTMP with random restarts at a fixed budget, which covers every homotopy class almost surely, and AO-GTMP with informed expansion with growing budgets, which converges to the optimal cost. We prove that a single sampled graph covers every endpoint-fixed homotopy class admitting a \(δ\)-clear representative of bounded length. We also prove that additional samples per layer reduce the per-layer miss probability exponentially, whereas stronger local planners reduce the required layer count only sublinearly. On manipulation benchmarks the method matches state-of-the-art performance, and on 2D navigation it returns batches of topologically diverse solutions, while the informed baselines concentrate on one or two classes.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning in cluttered, high-dimensional spaces requires finding the connected components of the configuration space and connecting configurations within them. Classical sampling-based planners do both in one sequential search, which couples global exploration to local connection failure. When several routes exist, downstream applications need *topologically diverse* alternatives rather than one feasible path: navigation selects among routes around obstacles, manipulation exploits distinct approach paths, and task-level planning reasons over the alternatives. Existing topological planners reason about homotopy classes through sequential roadmap construction, without coverage guarantees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global Tensor Motion Planning (GTMP) recasts sampling-based planning as two batch-parallel operations, sampling the intermediate vertex layers and realizing all adjacent-layer edges, so many candidate paths are evaluated at once. We generalize GTMP with black-box *local planners* (LPs), admitting straight-line interpolation, sampling-based planners, trajectory optimizers, and generative samplers. We prove that this method covers *every* homotopy class admitting a $\delta$-clear representative of bounded length. Our key insight is that a tube of clearance $\delta$ around a reference path guarantees coverage: the layer samples explore globally, the local planner connects locally, and any path that stays inside the tube lies in the reference's homotopy class. Moreover, random restarts at a fixed budget achieves almost-sure class coverage (Anytime-GTMP), and informed expansion with growing budgets gives almost-sure cost convergence (AO-GTMP).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate multi-class coverage on 2D navigation benchmarks, where Anytime-GTMP returns batches of topologically diverse solutions while the baselines return one path per query. Fig. 1 contrasts the two modes: random restart explores new corridors, while asymptotic optimality concentrates samples in the shrinking informed set. On MotionBenchMaker with 6--8 degree-of-freedom (DoF) manipulators, our variants match state-of-the-art performance and attain the lowest mean path cost on 15 of 21 problems within 60 seconds. We release our code as open source at

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

A path $f$ is *$\delta$-clear* if $\operatorname{dist}(f(t),C_{\mathrm{coll}})\geq\delta$ for all $t\in$; equivalently, $N_{\delta}(\mathrm{Im}(f))\subset C_{\mathrm{free}}$. A homotopy class is *$\delta$-clear* if it admits a $\delta$-clear representative. A path is *rectifiable* if it has finite Euclidean length. We write $\mathrm{TV}(f)$ for that length.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Two paths $f,g:\to C_{\mathrm{free}}$ with the same endpoints are *homotopic relative to endpoints*, written $f\simeq g$, if there exists a continuous map $H:\times\to C_{\mathrm{free}}$ such that $H(\cdot,0)=f$, $H(\cdot,1)=g$, $H(0,s)=q_{0}$, and $H(1,s)=q_{g}$ for all $s\in$. The homotopy class of $f$ is denoted by $[f]$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Layered Sampling Model", "weight": 1.0} -->

Fix an integer $M\geq 0$ and define the uniform grid on $$ For each intermediate layer $m\in\{1,\dots,M\}$, let $C_{m}\subseteq C$ be the *sampling region* of that layer: a measurable set with nonempty interior and finite volume. Let $\pi_{m}$ be a probability measure on $C_{m}\cap C_{\mathrm{free}}$ with Lebesgue density at least $a_{m}>0$ there. Each of the $N$ layer-$m$ samples $X_{m,1},\dots,X_{m,N}$ is drawn by an independent fair coin: with probability $\tfrac{1}{2}$ from $\pi_{m}$, independently of everything else, and otherwise from any heuristic sampler, which may depend on the history.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Layered Sampling Model", "weight": 1.0} -->

The $\pi_{m}$ draws are mutually independent within and across layers, so a layer misses a measurable set $A$ with probability at most $(1-\tfrac{1}{2}\pi_{m}(A))^{N}$ whatever the heuristic does. Every result below uses only the $\pi_{m}$ half of the mixture. Define the layer vertex sets: The GTMP candidate graph contains all ordered pairs $(u,v)$ with $u\in V_{m}$ and $v\in V_{m+1}$ for some $m\in\{0,\dots,M\}$. The graph is complete between adjacent layers and contains no intra-layer or skip-layer edges.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Generalized GTMP Graph", "weight": 1.0} -->

A *local planner* (LP), denoted $\mathsf{LP}$, is a randomized procedure $\mathsf{LP}(x,y;s,\ell)$ that, given $x,y\in C_{\mathrm{free}}$, an effort budget $s\in\mathbb{N}$, and a limit $\ell>0$, either returns failure or returns a continuous collision-free path $\Gamma:\to C_{\mathrm{free}}$ with $\Gamma=x$, $\Gamma=y$, and image inside the *query ellipsoid* $\ell$ is computable from the query alone, is enforced by rejecting samples and edges outside ${\mathcal{E}}$, and is not restrictive: any path from $x$ to $y$ of length at most $\ell$ already lies in ${\mathcal{E}}$, the segment $[x,y]$ included. The corresponding graph is denoted by $G^{\mathsf{LP}}_{M,N,s}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Generalized GTMP Graph", "weight": 1.0} -->

An edge $(u,v)$ is present in $G^{\mathsf{LP}}_{M,N,s}$ if and only if the call succeeds; the edge holds the returned local path $\Gamma_{u,v}$ and its cost.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Generalized GTMP Graph", "weight": 1.0} -->

A *chain* in $G^{\mathsf{LP}}_{M,N,s}$ is a sequence of vertices: with $v_{m}\in V_{m}$ and each adjacent pair $(v_{m},v_{m+1})$ realized as an edge. If the realized edges carry local paths $\Gamma_{0},\dots,\Gamma_{M}$, then their concatenation $P=\Gamma_{0}*\cdots*\Gamma_{M}$ is a continuous collision-free path from $q_{0}$ to $q_{g}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Generalized GTMP Graph", "weight": 1.0} -->

Let $[f]$ be an endpoint-fixed homotopy class from $q_{0}$ to $q_{g}$. We say that $G^{\mathsf{LP}}_{M,N,s}$ *covers* $[f]$ if it contains a chain whose concatenated path $P$ satisfies $P\simeq f$. For a finite family of classes $\mathcal{F}=\{[f^{}],\dots,[f^{(K)}]\},$ we say that $G^{\mathsf{LP}}_{M,N,s}$ *covers $\mathcal{F}$* if it covers every class in the family, not necessarily via disjoint chains. Class membership of a returned path $P$ is recorded by a label $\kappa(P)$ that accumulates along the path, such as the h-signature or a persistent-homology descriptor; we write ${\mathcal{K}}$ for the finite set of labels realized by chains of a given graph.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

Two iteration policies run on the layered graph: Anytime-GTMP uses random restart with fixed budgets for homotopy-class diversity, and AO-GTMP grows budgets monotonically for asymptotic cost optimality. The local planner may be any point-to-point planner; the original GTMP is the straight-line special case.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Stagewise Graph Instantiation", "weight": 1.0} -->

At planning stage $\nu\in\mathbb{N}$, choose budgets $(M_{\nu},N_{\nu},s_{\nu})$ and instantiate the layered graph from Sec. III, yielding the realized graph $G^{\mathsf{LP}}_{\nu}$. Every call $\mathsf{LP}(u,v;s_{\nu},\ell)$ uses the edge-length limit $\ell=\ell_{M_{\nu}}(r)$ of Sec. V, and on success assigns edge cost $c_{\nu}(u,v)=\mathrm{cost}(\Gamma_{u,v})$; admissible costs are additive, at least path length, and Lipschitz in the endpoints of a straight-line edge (Thm. 3. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")), which includes path length and weighted length.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Stagewise Graph Instantiation", "weight": 1.0} -->

Per-stage cost is $\mathcal{O}(M_{\nu}N_{\nu}^{2})$ local planner calls, which dominates the search except for the $|{\mathcal{K}}|$ factor of the class-augmented sweep (Sec. IV-B).

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-B Graph Search on the Layered DAG", "weight": 1.0} -->

Because GTMP connects only adjacent layers, the realized graph is a directed acyclic graph ordered by layer index, so a shortest feasible chain follows from value iteration at cost $\mathcal{O}(M_{\nu}N_{\nu}^{2})$. Let $\mathcal{V}_{\nu,m}$ denote the vertices in layer $m$. Define the terminal cost-to-go by $J_{\nu,M_{\nu}+1}(q_{g})=0$, and for any vertex $u\in\mathcal{V}_{\nu,m}$, $m=M_{\nu},\dots,0$, Any absent edge is treated as having infinite cost.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Graph Search on the Layered DAG", "weight": 1.0} -->

Taking $\sigma_{\nu,m}(u)$ to be a minimizer above and applying it repeatedly from $q_{0}$ recovers one minimum-cost feasible chain $q_{0}\to v_{\nu,1}\to\cdots\to v_{\nu,M_{\nu}}\to q_{g}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Graph Search on the Layered DAG", "weight": 1.0} -->

Concatenating the local planner paths yields a continuous configuration-space path: Anytime-GTMP augments the state with the class label, $J_{\nu,m}(u,\chi)$ over $\mathcal{V}_{\nu,m}\times{\mathcal{K}}$, and sweeps the same recursion subject to $\chi=\kappa(\Gamma_{u,v})\cdot\chi^{\prime}$, which returns a minimum-cost chain in *every* realized class for $\Theta(M_{\nu}N_{\nu}^{2}|{\mathcal{K}}|)$ work whenever the label accumulates along concatenation and tells the classes apart, as the h-signature does (Prop. 1. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")). Each sweep is a single batched tensor contraction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-C Two Iteration Policies", "weight": 1.0} -->

The two policies differ only in the budget schedule: Anytime-GTMP holds $(M,N,s)$ fixed and targets class diversity, while AO-GTMP holds $s$ fixed, grows $(M_{\nu},N_{\nu})$ monotonically to infinity, and targets cost optimality. Both proceed in two phases. *Phase 1 (feasibility).* Run GTMP from $(M_{1},N_{1},s_{1})$ until one feasible chain is found, yielding $\sigma_{0}$ and the initial bound $c_{0}\leftarrow\mathrm{cost}(\sigma_{0})$; with a probabilistically complete local planner this phase inherits the probabilistic completeness of GTMP. *Phase 2 (anytime).* Iterate under the chosen policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-C Two Iteration Policies", "weight": 1.0} -->

Alg. 1 gives both policies and the shared gtmp$$ subroutine, which extends canonical GTMP with the local planner budget $s$ and optional warm-start inputs ${\bm{Q}}$ and ${\bm{V}}_{h}$. The first iteration returning a feasible path is Phase 1: it seeds the archive (Anytime-GTMP) or the cost bound $c_{\textup{min}}$ (AO-GTMP). Both policies cost $\Theta(M_{\nu}N_{\nu}^{2})$ per stage, the $2N_{\nu}+(M_{\nu}{-}1)N_{\nu}^{2}$ candidate edges being dominated by inter-layer pairs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-D Anytime-GTMP", "weight": 1.0} -->

Fix $(M,N,s)$ throughout. Each stage $\nu$ draws a fresh layered sample set, realizes edges with $\mathsf{LP}_{s}$, runs the class-augmented DP search, and inserts every solution into a class-indexed archive $\mathcal{A}_{\nu}$ that holds the lowest-cost path per homotopy class, updated: with $\mathcal{A}_{0}\equiv\emptyset$, and the anytime output is the lowest-cost path across all classes. Any positive per-stage coverage probability yields almost-sure eventual class coverage (Thm. 2. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")).

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-E AO-GTMP", "weight": 1.0} -->

Fix $s$ throughout; grow $(M_{\nu},N_{\nu})$ monotonically. This instantiates the AO-x meta-algorithm on the layered DAG. Let $c_{\nu}$ be the best cost found through stage $\nu$ and let $\mathcal{X}_{f}(c)=\{x\in C\mid\|x-q_{0}\|+\|x-q_{g}\|\leq c\}$ be the informed set at cost bound $c$, the ellipsoid with foci $q_{0},q_{g}$, meeting $C_{\mathrm{free}}$ in the query ellipsoid ${\mathcal{E}}(q_{0},q_{g};c)$ of Sec. III.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-E AO-GTMP", "weight": 1.0} -->

Stage $\nu$ samples against the bound available on entry, $c_{\nu-1}$, taking $\pi_{\nu,m}$ of Sec. III to be the uniform measure on $\mathcal{X}_{f}(c_{\nu-1})\cap C_{\nu,m}\cap C_{\mathrm{free}}$, and the heuristic half of the mixture to be the midpoints of the closest layer-$(m{-}1)$ and layer-$(m{+}1)$ sample pairs. Because the uniform grid shifts when $M$ grows, AO-GTMP runs in *epochs*: within an epoch $M$ is fixed and $N_{\nu}$ increases until the per-layer hit probability saturates (the sample schedule of Thm. 3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-E AO-GTMP", "weight": 1.0} -->

‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")); a new epoch begins at larger $M$ when triggered by the layer schedule: where the *reach* $\Lambda_{s}(\tau)=\sup\{\ell>0\mid q_{s}(\ell)\geq 1-\tau\}$ is the longest edge the local planner solves with probability at least $1-\tau$, for the success profile $q_{s}$ of Asm. 1. ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning"). Cost convergence $c_{\nu}\to c^{*}$ a.s. follows from Thm. 3. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

We use the fact that a chain inside a tube of radius $\delta$ around a reference path is homotopic to that reference. Coverage then reduces to two questions: did every layer sample near the reference, and did the local planner connect consecutive samples.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Fix a reference path $f:\to C_{\mathrm{free}}$ from $q_{0}$ to $q_{g}$, rectifiable, parameterized at constant speed, of length $L=\mathrm{TV}(f)$ and clearance $\delta>0$, so $N_{\delta}(\mathrm{Im}(f))\subset C_{\mathrm{free}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Consecutive waypoints are joined inside the tube by going in to the reference, along it, and back out, a path of length at most $L/(M+1)+2r$ with clearance at least $\delta-r$, so the local planner is called with the length limit: for a fixed margin $\varsigma>0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1 (Local planner success profile)", "weight": 1.0} -->

Fix a clearance level $\rho>0$. For each budget $s$ there is a non-increasing $q_{s}:(0,\infty)\to$ with $q_{s}(\ell)\to 1$ as $s\to\infty$ such that, whenever $x,y$ admit a $\rho$-clear path of length at most $\ell-\varsigma$, the call $\mathsf{LP}(x,y;s,\ell)$ succeeds with probability at least $q_{s}(\ell)$, conditionally on the sampling history and on the other calls.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1 (Local planner success profile)", "weight": 1.0} -->

The assumption asks only for success, since the length limit of Sec. III already confines the path to the query ellipsoid; the clearance level, $\rho=\delta-r$ below, is what keeps it meaningful, as no planner holds a uniform success rate over corridors of vanishing width. RRT-Connect confined to that ellipsoid qualifies, with failure decaying as $\exp(-\beta s\eta/\ell)$ for the planner step $\eta$ and a constant $\beta>0$, and is *short-range exact*: it tries the straight line first, so any collision-free straight-line edge is returned deterministically.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Anytime Policies", "weight": 1.0} -->

Coverage puts a chain of the target class in the graph; the search of Sec. IV-B then returns a minimum-cost chain in every realized class at once.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Fig. 2: Success rate eCDFs on a 60 second budget, log scale. Anytime-GTMP SEV iterates fast and a low local planner budget leaves room for global exploration.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experiments ran on an AMD Ryzen Threadripper PRO 5965WX 24-core CPU with 32 GB of RAM and an NVIDIA RTX 4090. We run each policy with two local planners: straight-line edges with collision checking (SEV) and RRT-Connect (RRTC). table under pick TABLE I: Planner performance on the MotionBenchMaker (MBM) suite. Each planner is evaluated on 7 problems for the Panda, UR5, and Fetch robots. For every (planner, problem) pair, success rate and mean simplified path length (in paranthesis) is reported. As planners differ in which trials they solve, path cost is aggregated only over trials solved by every reference planner (FCIT, AORRTC, and GTMP) in that column, so reported costs compare planners on a common set of problem instances. A dash (−) in the cost position indicates that the planner did not solve that whole common set, leaving no comparable cost. Each rate is over 100 trials per (planner, problem) pair. Within each robot block the highest success rate in a column is shown in bold. For path cost we bold the lowest mean cost together with every planner.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

On cost, AO-GTMP is bold on 5/7 Panda, 7/7 UR5, and 5/7 Fetch problems, and Anytime-GTMP on 4/7, 3/7, and 1/7, against 6/7, 3/7, and 3/7 for the strongest baseline, AORRTC.

<!-- chunk {"id": "body-0035", "role": "body", "section": "VI-A Feasibility and Cost", "weight": 1.0} -->

We validate feasibility and cost on MotionBenchMaker (Tables I and 2). GTMP variants are not the fastest to a first solution: within one second AORRTC and FCIT succeed often, BIT\* stays below $10\%$, and GTMP variants rarely return, which we attribute to the overhead of layered graph construction and local planner evaluation. Over the full time budget, Anytime-GTMP (SEV) matches FCIT's final success rate of approximately $85\%$. On the common set solved by every reference planner, the variants match or beat the lowest mean path cost most often: AO-GTMP on $5/7$ Panda, $7/7$ UR5, and $5/7$ Fetch problems, and Anytime-GTMP on $4/7$, $3/7$, and $1/7$, against $6/7$, $3/7$, and $3/7$ for AORRTC.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A Feasibility and Cost", "weight": 1.0} -->

Sec. V-A predicts that a strong enough local planner collapses the graph to a single call: fixing $M=6$ layers, $N=100$ samples per layer, and an AORRTC budget of 1000 iterations, a complete start-to-goal path emerges near 250 iterations and approaches the optimal chain by 1000, as the graph approaches the connectivity of the continuous configuration space.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A Feasibility and Cost", "weight": 1.0} -->

Fig. 3: Per-edge local planner budget against (a) best path cost and (b) time to first solution, for Anytime-GTMP (yellow) and AO-GTMP (brown). Budget 1 is a straight-line local planner; 100–1000 are maximum RRT-Connect iterations per edge. Bands are means over solved problems with SEM.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Feasibility and Cost", "weight": 1.0} -->

Sweeping the per-edge budget in Fig. 3 shows diminishing returns: path cost improves until roughly 400 to 600 RRT-Connect iterations and then flattens, so under a fixed planning budget moderate local effort with more global sampling dominates heavy local effort.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-B Topological Diversity", "weight": 1.0} -->

Fig. 4: Homotopy-class coverage across the 2D maps: aggregate coverage (left) and per-planner classes on the Sydney map (right). Random restart keeps sampling new corridors, so Anytime-GTMP reaches the most distinct classes, whereas AO-GTMP concentrates samples in the shrinking informed set.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-B Topological Diversity", "weight": 1.0} -->

We evaluate topological diversity (Figs. 5 and 4) on 2D street-view heightmaps from Sturtevant's database, whose homotopy classes are visually verifiable; the baselines return one path per query and do not target class coverage. Over a 60 s budget we record a path event whenever a planner explores a start-to-goal path, returned or not, label each event with a homotopy invariant, and pre-cluster with Dynamic Time Warping, itself not a homotopy invariant. Anytime-GTMP covers the highest average number of classes, while aggressive cost bounding concentrates informed planners on a few near-optimal ones: on the Sydney map, AO-GTMP (RRTC) and FCIT each identify a single class.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Topological Diversity", "weight": 1.0} -->

Fig. 5: As AO-GTMP’s cost bound shrinks, so does the sampling volume, and the diversity of new samples falls as search narrows to near optimal.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Topological Diversity", "weight": 1.0} -->

Fig. 5 plots the diversity of new AO-GTMP samples, the complement of mean cosine similarity, against the normalized cost bound: it spikes to $0.6$ just after the first feasible solution, when the informed set is still large, then falls as $c_{\nu}$ tightens and ${\mathcal{X}}_{f}(c_{\nu})$ contracts. The trade-off is empirical as well as theoretical: repetition gives diversity, and a shrinking informed set gives optimality.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have generalized GTMP so that adjacent-layer edges are realized by any black-box local planner. We prove that one sampled graph covers each $\delta$-clear homotopy class with high probability (Thm. 1. ‣ V-A Coverage from One Sampled Graph ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")), and every such class of bounded length simultaneously; that the longest edge a local planner connects reliably grows only sublinearly in its budget, while each additional sample per layer cuts the miss probability exponentially; and that two iteration policies yield distinct guarantees: random restart at a fixed budget achieves almost-sure class coverage (Thm. 2. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")), while informed expansion with growing budgets drives cost to the optimum (Thm. 3. ‣ V-B Anytime Policies ‣ V Theoretical Analysis ‣ Anytime Global Tensor Motion Planning")).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Empirically, the variants match FCIT's success rate at competitive path cost on 6--8 DoF manipulation, and on 2D navigation Anytime-GTMP covers the most homotopy classes while AO-GTMP concentrates on near-optimal ones---the random-restart versus informed-expansion trade-off in practice.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work includes lazy variants that realize only a subset of adjacent-layer pairs, scheduling that adapts $(M_{\nu},N_{\nu},s_{\nu})$ online from the measured local planner profile, dynamically-aware local planners that extend the same guarantees to dynamically feasible trajectories, and evaluating topological coverage on high-DoF manipulation, where homotopy classes are harder to verify than in the 2D navigation studied here.
