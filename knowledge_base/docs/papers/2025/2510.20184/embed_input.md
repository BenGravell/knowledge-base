<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Unified and Scalable Method for Optimization over Graphs of Convex Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A Graph of Convex Sets (GCS) is a graph in which vertices are associated with convex programs and edges couple pairs of programs through additional convex costs and constraints. Any optimization problem over an ordinary weighted graph (e.g., the shortest-path, the traveling-salesman, and the minimum-spanning-tree problems) can be naturally generalized to a GCS, yielding a new class of problems at the interface of combinatorial and convex optimization with numerous applications. In this paper, we introduce a unified method for solving any such problem. Starting from an integer linear program that models an optimization problem over a weighted graph, our method automatically produces an efficient mixed-integer convex formulation of the corresponding GCS problem. This formulation is based on homogenization (perspective) transformations, and the resulting program is solved to global optimality using off-the-shelf branch-and-bound solvers. We implement this framework in GCSOPT, an open-source and easy-to-use Python library designed for fast prototyping. We illustrate the versatility and scalability of our approach through multiple numerical examples and comparisons.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, in the Shortest-Path Problem (SPP), the set $\mathcal{H}$ of admissible subgraphs consists of all paths between two fixed vertices in $G$. In the Traveling-Salesman Problem (TSP), $\mathcal{H}$ consists of all cycles that visit each vertex exactly once. In the Minimum-Spanning-Tree Problem (MSTP), $\mathcal{H}$ is the set of all trees that reach every vertex. This paper addresses a generalization of problem where the weighted graph is replaced by a Graph of Convex Sets (GCS).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A GCS is a graph in which each vertex is paired with a convex program, defined by a continuous variable, a convex constraint set, and a convex objective function. The edges of a GCS link pairs of these programs through additional convex costs and constraints. Any discrete optimization problem of the form is naturally generalized to a GCS. Indeed, if we fix the continuous variables of the GCS, we obtain a weighted graph over which we can solve problem. The challenge in a GCS problem is to optimize the continuous variables so that the resulting discrete problem achieves the smallest optimal value. This leads to a new class of problems at the interface of combinatorial and convex optimization with many applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The GCS framework has been recently introduced in marcucci2024shortest with a focus on the SPP, and has since been applied to a wide range of real-world robotics problems marcucci2023motion; kurtz2023temporal; cohn2024non; graesdal2024towards; philip2024mixed; morozov2024multi; natarajan2024implicit; morozov2025mixed; wei2025hierarchical; lin2025towards. The first contribution of this paper is to extend the approach presented in marcucci2024shortest for solving the SPP in GCS to any GCS problem. The input of our method is the formulation of problem as an Integer Linear Program (ILP). These ILPs have been deeply studied, and are readily available in combinatorial-optimization textbooks schrijver2003combinatorial; korte2018combinatorial; papadimitriou1998combinatorial; nemhauser1999integer; conforti2014integer. They typically have one binary variable for each vertex and edge in the graph.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The role of these variables is to take unit value if the corresponding vertex or edge is part of the subgraph $H$, and evaluate to zero otherwise. Our method translates this ILP into an efficient Mixed-Integer Convex Program (MICP) that models the corresponding GCS problem. This translation is based on homogenization transformations (also known as perspective formulations): a popular tool in mixed-integer programming ceria1999convex; stubbs1999branch; frangioni2006perspective; gunluk2010perspective; moehle2015perspective that allows us to activate and deactivate the convex costs and constraints in a GCS using the ILP binary variables.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our MICPs are reliably solved with standard branch-and-bound solvers, which either return a globally optimal solution or certify infeasibility. This process is facilitated by the small number of variables and constraints in our programs, and is especially effective when the original ILP is well approximated by its convex relaxation, since this property is typically inherited by our MICP.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our second contribution is GCSOPT, an open-source Python library for formulating and solving GCS problems, designed for ease of use and fast prototyping. GCSOPT provides a high-level interface for defining GCS vertices and connecting them with edges. Convex sets and functions are specified using the syntax of CVXPY diamond2016cvxpy: a popular Python library for convex optimization. Internally, these sets and functions are translated into conic form, enabling a straightforward computation of their homogenization. The MICP is constructed automatically and shipped to state-of-the-art solvers (e.g., Gurobi, Mosek, or CPLEX), then the GCS variables are populated with their optimal value. Thanks to this automation, users of GCSOPT do not need any significant expertise in mixed-integer programming: a basic familiarity with graphs and convex optimization is sufficient to model and solve complex GCS problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the broad applicability of our framework through a wide range of numerical examples. We also show that our method consistently outperforms alternative approaches for solving GCS problems globally.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related works", "weight": 1.0} -->

The GCS framework is closely related to several well-studied problems in graph theory and combinatorial optimization. Here we review these connections, emphasizing similarities and key differences.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Graph-structured convex optimization", "weight": 1.0} -->

When the only admissible subgraph is the entire graph, $\mathcal{H} = {\{ G\}}$, a GCS problem reduces to a purely continuous convex program with graph structure. Such programs are the focus of the software libraries SnapVX hallac2017snapvx and Plasmo.jl jalving2022graph. The former is a solver based on the alternating-direction method of multipliers, and the latter is a modeling and solution framework. In this paper, we add an extra layer of complexity by posing combinatorial questions on top of these graph-structured convex programs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Graph problems with neighborhoods", "weight": 1.0} -->

Variants of classical graph optimization problems, in which vertices can be selected within prescribed continuous sets, are known in the literature as problems *with neighborhoods*. Examples are the TSP arkin1994approximation; gudmundsson1999fast; dumitrescu2003approximation; de2005tsp; gentilini2013travelling; puerto2024hampered, the MSTP yang2007minimum; disser2014rectilinear; dorrigiv2015minimum; blanco2017minimum; blanco2025fixed, the SPP disser2014rectilinear, the Facility-Location Problem (FLP) blanco2019ordered; brimberg2002locating, and matching problems espejo2022minimum with neighborhoods.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Graph problems with neighborhoods", "weight": 1.0} -->

These problems have been approached either through approximation algorithms arkin1994approximation; mata1995approximation; dumitrescu2003approximation; fourney2024mobile or by formulating them as Mixed-Integer Nonconvex Programs (MINCP) that can be solved exactly gentilini2013travelling; blanco2017minimum; fourney2024mobile. However, the former algorithms are typically limited to planar neighborhoods with simple shape (e.g., lines, circles, or rectangles), while the latter rely on spatial branch-and-bound algorithms, which have significantly improved in recent years, but still struggle with large-scale problems (see also the comparison in Section 8.5).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Graph problems with neighborhoods", "weight": 1.0} -->

GCS problems generalize most common graph problems with neighborhoods, since our objective functions and constraints need only be convex. As already shown by the many robotics applications of the SPP in GCS, our MICPs can scale to large graphs and high-dimensional spaces. For instance, the motion-planning problems in marcucci2023motion involve up to $2,500$ vertices, $5,000$ edges, and vertex variables in $70$ dimensions. Additionally, the method proposed in this paper is unified and can solve any GCS problem, as opposed to the works above that are tailored to a specific graph problem with neighborhoods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Generalized network-design and Steiner problems", "weight": 1.0} -->

Generalized network-design problems feremans2003generalized; pop2012generalized and generalized Steiner problems dror2000generalizedsteiner can be viewed as discrete versions of graph problems with neighborhoods. The vertex set is divided into clusters, and the constraints are enforced at the cluster level rather than on individual vertices. For example, the generalized TSP has been studied in noon1993efficient; fischetti1995symmetric, the MSTP in myung1995generalized; dror2000generalizedspanning; feremans2004generalized, the SPP in li1995shortest, the vehicle routing problem in ghiani2000efficient, and graph coloring in li2000partition; demange2015some. GCS problems admit a natural discretization as graph problems with clusters. However, this approximation quickly becomes impractical in high dimensions, where dense sampling is infeasible, or in problems where equality constraints make the feasible set lower-dimensional and difficult to discretize.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

This paper is organized as follows. In Section 2, we give a formal statement of the GCS problem. Section 3 contains background material on ILP formulations of discrete optimization problems over graphs. Our MICP formulation is introduced in Section 4 and further refined in Section 5. Section 6 illustrates multiple examples of GCS problems along with their MICP formulations. Section 7 describes how some simplifying assumptions made in the previous sections can be relaxed. All numerical examples and comparisons are presented in Section 8, while the Python library GCSOPT is described in Section 9. Finally, Section 10 presents concluding remarks and directions for future work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Let $G = {(\mathcal{V},\mathcal{E})}$ be a weighted graph, either directed or undirected, with vertex set $\mathcal{V}$ and edge set $\mathcal{E} \subset \mathcal{V}^{2}$. Let $c_{v} \in {\mathbb{R}}$ and $c_{e} \in {\mathbb{R}}$ denote the weights of vertex $v \in \mathcal{V}$ and edge $e \in \mathcal{E}$, respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Here the variable is the subgraph $H$, which has vertex set $\mathcal{W} \subseteq \mathcal{V}$ and edge set $\mathcal{F} \subseteq {\mathcal{W}^{2} \cap \mathcal{E}}$. As, the set $\mathcal{H}$ consists of the admissible subgraphs of $G$ (e.g., paths, tours, or spanning trees). The objective function is equal to the total weight of $H$, i.e., the sum of its vertex and edge weights.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem statement", "weight": 1.0} -->

A GCS is a generalization of an ordinary weighted graph. Each vertex $v \in \mathcal{V}$ of a GCS is paired with a convex program, which is defined by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Each edge $e = {\lbrack v,w\rbrack} \in \mathcal{E}$ in a GCS (we use square brackets for edges that may be directed or undirected) couples the convex programs of vertices $v$ and $w$ through

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Additional assumptions on these sets and functions will be made in different sections of the paper. A simple sufficient condition under which all our results apply is that the sets $\mathcal{X}_{v}$ are bounded for all $v \in \mathcal{V}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Here the variables are both the discrete subgraph $H$ and the continuous vectors ${\mathbf{x}}_{v}$ for $v \in \mathcal{W}$. The first constraint is inherited from the graph optimization problem. The second and third enforce the vertex and edge constraints for the selected subgraph $H$. The objective function is equal to the total cost of $H$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

Integer programming offers a unified framework for solving graph optimization problems: once problem is cast as an ILP, it can be reliably solved to global optimality with highly effective branch-and-bound solvers. In this section, we examine some important properties of these ILPs that will play a central role in formulating the GCS problem as an MICP.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

The first step in formulating problem as an ILP is to parameterize the subgraph $H = {(\mathcal{W},\mathcal{F})}$ through its incidence (or characteristic) vector

<!-- chunk {"id": "body-0025", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

The entries of this vector are indexed by the elements of the set $\mathcal{V} \cup \mathcal{E}$, and have value

<!-- chunk {"id": "body-0026", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

denote the set of incidence vectors that represent an admissible subgraph.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

Using the shorthand notation $\mathcal{Y}^{bin} = {\mathcal{Y} \cap {\{ 0,1\}}^{\mathcal{V} \cup \mathcal{E}}}$ for the binary elements of $\mathcal{Y}$, problem can be rewritten as the ILP

<!-- chunk {"id": "body-0028", "role": "body", "section": "Graph optimization problems as integer linear programs", "weight": 1.0} -->

The decision variable is the incidence vector $\mathbf{y}$, with the superscript $H$ omitted for simplicity. The binary variables in the objective select the weights of the vertices and edges included in the subgraph. This ILP has the same optimal value as problem, and its optimal solutions $\mathbf{y}$ are the incidence vectors of the optimal subgraphs $H$. The ILP convex relaxation is obtained simply by replacing the polytope $\mathcal{Y}^{bin}$ with $\mathcal{Y}$ in (5b).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Compact versus strong formulations", "weight": 1.0} -->

How do we choose the polytope $\mathcal{Y}$ in practice? For any family $\mathcal{H}$ of subgraphs, there are infinitely many polytopes $\mathcal{Y}$ satisfying the incidence condition. Among these, we seek one that has few facets and for which the inclusion

<!-- chunk {"id": "body-0030", "role": "body", "section": "Compact versus strong formulations", "weight": 1.0} -->

is sufficiently tight, where $conv$ denotes the convex hull. A polytope $\mathcal{Y}$ with few facets yields a computationally light ILP, which we refer to as a *compact* formulation. While, when the inclusion is tight, the ILP is well approximated by its convex relaxation and the branch-and-bound process converges quickly. In this case, the formulation is said to be *strong*. Furthermore, if the inclusion holds with equality (i.e., is perfectly tight), then the ILP can be solved exactly through its convex relaxation, and the formulation is said to be *perfect*.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Compact versus strong formulations", "weight": 1.0} -->

Designing an ILP that is both compact and strong is sometimes impossible, as tightening the inclusion might require adding many facets to $\mathcal{Y}$. This trade-off is well understood for most graph optimization problems, and efficient ILP formulations can be found in standard textbooks schrijver2003combinatorial; korte2018combinatorial; papadimitriou1998combinatorial; nemhauser1999integer; conforti2014integer (see also Section 6 for a variety of examples).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Nonnegative weights", "weight": 1.0} -->

When the weights $c_{v}$ for $v \in \mathcal{V}$ and $c_{e}$ for $e \in \mathcal{E}$ are nonnegative, the incidence condition can be relaxed to

<!-- chunk {"id": "body-0033", "role": "body", "section": "Nonnegative weights", "weight": 1.0} -->

where ${\mathbb{Z}}_{\geq 0}$ is the set of nonnegative integers and the plus symbols denote Minkowski sums. In words, we ignore any difference that the sets $\mathcal{Y}^{bin}$ and $\mathcal{Y}_{\mathcal{H}}$ might have in the positive directions, and ask only that the two sets have equal minimal elements (with respect to the partial order $\leq$). Indeed, if the ILP is feasible, one of these minimal elements is necessarily optimal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Nonnegative weights", "weight": 1.0} -->

where ${\mathbb{R}}_{\geq 0}$ are the nonnegative reals. If this inclusion is tight or holds with equality, the ILP formulation is again said to be *strong* or *perfect*, respectively.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Subgraph polytope", "weight": 1.0} -->

Although the polytope $\mathcal{Y}$ is problem dependent, the incidence vector $\mathbf{y}$ must always represent a subgraph $H$ of $G$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Subgraph polytope", "weight": 1.0} -->

where $\delta_{v}$ is the set of edges incident with vertex $v$. The inequality $y_{v} \geq y_{e}$ ensures that if a vertex $v$ is excluded from the subgraph $H$, so are its incident edges $e$. Equivalently, if an edge $e = {\lbrack v,w\rbrack}$ is included in the subgraph $H$, so are the vertices $v$ and $w$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Base mixed-integer convex formulation of the GCS problem", "weight": 1.0} -->

This section presents an initial MICP formulation that applies to any GCS problem. Our construction extends the one proposed in marcucci2024shortest for the SPP in GCS. First, we transform the ILP into an MINCP that models the corresponding GCS problem, but is impractical to solve due to the nonconvexity of its constraints. Second, we design a convex relaxation that yields an equivalent, but easier to solve, MICP. In Section 5, we will show how this base MICP can be automatically tailored to specific classes of GCS problems to improve its computational efficiency.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Base mixed-integer convex formulation of the GCS problem", "weight": 1.0} -->

We will make two main simplifying assumptions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2 (Linear objectives)", "weight": 1.0} -->

While not essential, these assumptions simplify the exposition and avoid multiple technical subtleties. In Section 7, we will show how our MICP formulation can be extended to unbounded sets and nonlinear objective functions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Homogenization", "weight": 1.0} -->

The following operation is at the core of our method. It allows us to switch on and off convex constraints using binary variables.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 2", "weight": 1.0} -->

The homogenization $\overset{\sim}{\mathcal{X}}$ is easily verified to be a closed convex cone. In fact, it could be equivalently defined as the cone generated by the points $({\mathbf{x}},1)$ with ${\mathbf{x}} \in \mathcal{X}$. Especially important for us are the observations that ${({\mathbf{x}},1)} \in \overset{\sim}{\mathcal{X}}$ is equivalent to ${\mathbf{x}} \in \mathcal{X}$ and ${({\mathbf{x}},0)} \in \overset{\sim}{\mathcal{X}}$ is equivalent to ${\mathbf{x}} = \mathbf{0}$ (since ${0\mathcal{X}} = {\{\mathbf{0}\}}$).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 2", "weight": 1.0} -->

In Section 7.1, we will extend Definition 1 ‣ 4.1 Homogenization ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") to unbounded sets, and, in Section 9.4, we will show how homogenization transformations are well suited for numerical computations and amenable to standard conic-optimization solvers.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The term homogenization is not fully standard. It is used, for example, in (ziegler2012lectures Definition 1.13). The same operation is called *conic hull* in (ben2001lectures Section 3.3), while it is commonly named *perspective* when applied to functions (see, e.g., (hiriart2013convex Section IV.2.2) or (boyd2004convex Section 2.3.3)). The same construction appears frequently in (rockafellar1970convex Section 8), but is used without an explicit name.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

Here the decision variables are both the binary variables $\mathbf{y}$ and the continuous variables ${\mathbf{x}}_{v}$ for $v \in \mathcal{V}$. The objective uses the binary variables to activate and deactivate the cost contributions of the GCS vertices and edges, which are linear functions by Assumption 2 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."). The first constraint comes from the ILP, and forces $\mathbf{y}$ to be the incidence vector of an admissible subgraph.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

The equivalence of problem and the GCS problem is easily established, provided that the polytope $\mathcal{Y}$ satisfies the incidence condition or, when the objective functions $f_{v}$ for $v \in \mathcal{V}$ and $f_{e}$ for $e \in \mathcal{E}$ are nonnegative, the relaxed incidence condition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

We rewrite problem in an equivalent form to simplify the upcoming derivations. First, observe that the objective (11a) as well as the constraints (11c) and (11d) are nonconvex due to products between binary and continuous variables.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

The first equality is equivalent to (12b) after a reindexing. The second and the third equalities follow from and (12a), respectively.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

Collecting all the modifications, problem is reformulated as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

The objective, the second constraint, and the third constraint are the result of substituting the new variables in the original problem. The last constraint is taken, and is equivalent to (12b). We omitted the constraint ${\mathbf{z}}_{v} = {y_{v}{\mathbf{x}}_{v}}$ from (12a) since the variables ${\mathbf{x}}_{v}$ would appear only in this constraint, and the fact that ${\mathbf{z}}_{v} = \mathbf{0}$ when $y_{v} = 0$ is already implied by (14c). Therefore, we can solve the problem without constraint (12a) and, afterwards, define ${\mathbf{x}}_{v} = {\mathbf{z}}_{v}$ if $y_{v} = 1$ or leave ${\mathbf{x}}_{v}$ undefined if $y_{v} = 0$, for all $v \in \mathcal{V}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Mixed-integer nonconvex formulation", "weight": 1.0} -->

Constraint (14e) is nonconvex and makes problem an MINCP. This MINCP is akin to existing ones for graph problems with neighborhoods gentilini2013travelling; blanco2017minimum; fourney2024mobile, but applies to any GCS problem, uses homogenization transformations, and includes edge constraints. Although MINCP solvers have improved substantially in recent years, their scalability remains limited: our next step is to transform problem into a more tractable MICP by leveraging the bilinear structure of constraint (14e).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

We obtain our MICP by replacing the bilinear constraint (14e) with a family of convex constraints.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

Be equivalent to the bilinear constraint when the vector $\mathbf{y}$ has binary entries, resulting in a *correct* MICP formulation of the GCS problem.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

Envelop the bilinear constraint tightly when the vector $\mathbf{y}$ has fractional entries, resulting in a *strong* MICP formulation.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

Be few in number, resulting in a *compact* MICP formulation.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

Below, we present the approach that, in our experience, best balances these competing objectives. Section 8.5 reports a numerical comparison with a simpler formulation based on McCormick envelopes mccormick1976computability.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Convex relaxation of the bilinear constraint", "weight": 1.0} -->

The next lemma parallels (marcucci2024shortest Lemma 5.4), and gives us an algorithmic way of enveloping the bilinear equality (14e) with convex constraints. Recall that a constraint is *valid* for a set if it is satisfied by all points in the set, and *valid* for an optimization problem if it is valid for the problem's feasible set.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Automatic tailoring of the mixed-integer convex program", "weight": 1.0} -->

We now describe how the base MICP (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) can be automatically tailored to specific classes of GCS problems. First, we discuss a few variations and extensions of our constraint-generation procedure. Second, we present the algorithm that performs the automatic tailoring. Finally, we provide a qualitative comparison of our method with alternative relaxation techniques.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Variations and extensions of the constraint-generation procedure", "weight": 1.0} -->

Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") is easily specialized to equality constraints.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

The base MICP (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) is constructed leveraging only the linear inequalities that are valid for the subgraph polytope. However, knowing the specific class of GCS problems and the corresponding polytope $\mathcal{Y}$, allows us to generate additional convex constraints and strengthen the MICP.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Ideally, to fully exploit the structure of a given polytope $\mathcal{Y}$ and maximize the MICP strength, we would proceed as follows. For each vertex $v \in \mathcal{V}$, let $\mathcal{Y}_{v}^{bin}$ denote the orthogonal projection of $\mathcal{Y}^{bin}$ onto the subspace of $y_{v}$ and $y_{e}$ for $e \in \delta_{v}$. Find a minimal set of linear constraints that are valid for $\mathcal{Y}_{v}^{bin}$ and imply all other valid linear constraints (i.e., the extreme rays of the dual cone of $\mathcal{Y}_{v}^{bin}$).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Replace (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) and (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) with the convex constraints derived from these linear constraints using Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") (for inequalities) or Corollary 1 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and

<!-- chunk {"id": "body-0062", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") (for equalities).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Since $\mathcal{Y} \subseteq \mathcal{Y}_{sub}$, the linear constraints imply the subgraph inequalities $y_{v} \geq y_{e} \geq 0$ for $e \in \delta_{v}$, and the derived convex constraints imply (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) and (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) by Proposition 1 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in

<!-- chunk {"id": "body-0064", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

this paper is partially based on the author’s PhD thesis marcucci2024graphs.").

<!-- chunk {"id": "body-0065", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Hence, the resulting MICP is correct by Theorem 4.1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.").

<!-- chunk {"id": "body-0066", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

In practice, however, computing the projection $\mathcal{Y}_{v}^{bin}$ is generally intractable. Therefore, we construct our MICP in a more conservative way. For all $v \in \mathcal{V}$, we select the constraints that define $\mathcal{Y}$ and involve only the variables $y_{v}$ and $y_{e}$ for $e \in \delta_{v}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

If a selected constraint is linear, we apply Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") or Corollary 1 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."), and add the resulting convex constraint to the MICP (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

If a constraint is affine, we linearize it using Lemma 2 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") (for inequalities) or Corollary 2 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") (for equalities), add the constraint $y_{v} = 1$ to the MICP when appropriate, and proceed as in the linear case.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Finally, if the linear and linearized constraints associated with vertex $v$ imply a subgraph inequality $y_{e} \geq 0$ or $y_{v} \geq y_{e}$ for some $e \in \delta_{v}$, we remove the corresponding constraint from (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) or (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) since it is redundant.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

The resulting MICP is again correct by Theorem 4.1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.").

<!-- chunk {"id": "body-0071", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Algorithm 1 summarizes the steps just described. In the algorithm, $\mathcal{L}_{v}$ represents the set of linear and linearized constraints associated with vertex $v$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Inputs: GCS and polytope 𝒴
Output: tailored MICP
initialize empty set of linear constraints ℒv
foreach constraint defining 𝒴 do
if constraint involves only variables yv and ye for e ∈ δv then
if constraint is affine then
linearize constraint using Lemma 2 or Corollary 2
add constraint yv = 1 to MICP if appropriate

<!-- chunk {"id": "body-0073", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

add linear constraint to set ℒv
add convex constraint generated by Lemma 1 or Corollary 1 to MICP

<!-- chunk {"id": "body-0074", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

if constraints in ℒv imply ye ≥ 0 or yv ≥ ye then
remove constraint generated by implied inequality from (17c) or (17d)

<!-- chunk {"id": "body-0075", "role": "body", "section": "Tailoring algorithm", "weight": 1.0} -->

Algorithm 1 Tailoring of base MICP to a specific GCS problem

<!-- chunk {"id": "body-0076", "role": "body", "section": "Alternative relaxation techniques", "weight": 1.0} -->

The steps leading to our MICP generalize those presented in (marcucci2024shortest Section 5) for the SPP in GCS, with key improvements that exploit the structure of the subgraph polytope. Specifically, our constraint-generation procedure focuses on linear constraints, in contrast to (marcucci2024shortest Lemma 5.4) which applies to affine constraints of the form considered in Lemma 2 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.").

<!-- chunk {"id": "body-0077", "role": "body", "section": "Alternative relaxation techniques", "weight": 1.0} -->

While our procedure can easily be extended to affine constraints (see (marcucci2024graphs Lemma 5.1)), this is unnecessary since any affine constraint other than $y_{v} \leq 1$ or $y_{v} = 1$ reduces to a linear constraint that is at least as tight (see Lemma 2 ‣ 5.1 Variations and extensions of the constraint-generation procedure ‣ 5 Automatic tailoring of the mixed-integer convex program ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")). In addition, the valid convex constraints generated from $y_{v} \leq 1$ and $y_{v} = 1$ via (marcucci2024graphs Lemma 5.1) are easily seen to be redundant for our MICP. This observation streamlines the formulation of our MICPs by preventing the generation of redundant convex constraints, which are manually identified and eliminated in (marcucci2024shortest Section 5.3).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Alternative relaxation techniques", "weight": 1.0} -->

Our procedure can also be extended to constraints involving all binary variables, and not just those related to a common vertex. However, this requires introducing new variables that represent all possible products between a binary and a continuous variable. In our experience, the resulting MICPs are stronger but much slower to solve than ours due to their larger size.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Alternative relaxation techniques", "weight": 1.0} -->

Finally, the core idea behind Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") can be extended to a wide class of bilinear constraints, as shown in (marcucci2024shortest Section 7). The same reference highlights the close connections between our technique and the Lovász-Schrijver hierarchy lovasz1991cones, as well as other classical relaxation hierarchies sherali1990hierarchy; parrilo2000structured; parrilo2003semidefinite; lasserre2001global.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Some GCS problems and their mixed-integer convex formulations", "weight": 1.0} -->

This section presents several examples of GCS problems together with their MICP formulations. For each problem, we recall the ILP formulation of the associated graph optimization problem and apply Algorithm 1 to tailor the base MICP (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Some GCS problems and their mixed-integer convex formulations", "weight": 1.0} -->

The problems below admit several variants (e.g., directed versus undirected graphs or nonnegative versus sign-indefinite weights) and multiple ILP formulations. For brevity, we present only one variant and formulation per problem, even though our techniques apply to the others as well.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Shortest path", "weight": 1.0} -->

We begin with the SPP in GCS. The MICP we derive here is the same as that of marcucci2024shortest but is obtained in a simpler and more direct manner.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Shortest path", "weight": 1.0} -->

In the discrete SPP, we consider a directed weighted graph $G = {(\mathcal{V},\mathcal{E})}$ with nonnegative vertex and edge weights. We seek a minimum-weight path (i.e., a sequence of distinct vertices connected by edges) that starts at a source vertex $\sigma \in \mathcal{V}$ and ends at a target vertex $\tau \in \mathcal{V}$. The SPP can be solved in polynomial time using, e.g., Dijkstra's algorithm dijkstra1959note. It is a special case of problem, where the set $\mathcal{H}$ of admissible subgraphs is replaced with the set $\mathcal{H}_{path}$ of all paths from $\sigma$ to $\tau$ in $G$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Shortest path", "weight": 1.0} -->

Here the sets $\delta_{v}^{-}$ and $\delta_{v}^{+}$ contain the edges that are incoming and outgoing a vertex $v \in \mathcal{V}$, and, without loss of generality, we assume that $\delta_{\sigma}^{-} = \delta_{\tau}^{+} = \varnothing$. The first two conditions enforce bounds on the binary variables. The third ensures that the selected path contains the source $\sigma$ and the target $\tau$. The last two require that every vertex in the path has exactly one incoming and one outgoing edge, except for the source and target.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Shortest path", "weight": 1.0} -->

The polytope $\mathcal{Y}_{path}$ does not meet the incidence condition, since its binary elements represent a path together with disjoint cycles. However, it meets the relaxed incidence condition, which is sufficient for the validity of the ILP when the weights are nonnegative. In addition, $\mathcal{Y}_{path}$ also satisfies condition with equality, yielding a perfect ILP formulation and allowing the SPP with nonnegative weights to be solved through a linear program (see, e.g., (schrijver2003combinatorial Section 13.1)).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Shortest path", "weight": 1.0} -->

The SPP in GCS is obtained by replacing $\mathcal{H}$ with $\mathcal{H}_{path}$ in problem. The nonnegativity of the weights is translated into the nonnegativity of the objective functions $f_{v}$ for $v \in \mathcal{V}$ and $f_{e}$ for $e \in \mathcal{E}$. Although the SPP is solvable in polynomial time, the SPP in GCS is NP-hard (marcucci2024shortest Section 3).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Shortest path", "weight": 1.0} -->

The base MICP (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) is adapted to the SPP in GCS by following the steps in Algorithm 1. The inequality (18a) is mapped by our constraint-generation procedure to the valid convex constraint (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")). While the equalities (18d) and (18e) give us the valid linear equalities

<!-- chunk {"id": "body-0088", "role": "body", "section": "Shortest path", "weight": 1.0} -->

The resulting MICP formulation of the SPP in GCS is then

<!-- chunk {"id": "body-0089", "role": "body", "section": "Shortest path", "weight": 1.0} -->

${minimize}\quad$ objective (17a ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) (20a)
${{subject}{to}}\quad$ ${{\mathbf{y}} \in \mathcal{Y}_{path}^{bin}},$ (20b)
${\text{constraints~(}\text{),~(}\text{),~(}\text{)}}.$ (20c)

<!-- chunk {"id": "body-0090", "role": "body", "section": "Shortest path", "weight": 1.0} -->

Constraint (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) is omitted since, for each $v \in \mathcal{V}$, the constraints in involving only the variables $y_{v}$ and $y_{e}$ for $e \in \delta_{v}$ already imply the subgraph inequalities $y_{v} \geq y_{e}$ for $e \in \delta_{v}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

The TSP is one of the most famous NP-complete problems karp1972reducibility. Given an undirected weighted graph $G = {(\mathcal{V},\mathcal{E})}$, the goal is to find a minimum-weight tour, i.e., a cycle that visits every vertex. The TSP is a special case of the graph optimization problem where the set $\mathcal{H}$ is replaced with the set $\mathcal{H}_{tour}$ of all tours in $G$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

A classical ILP formulation of the TSP is due to Dantzig, Fulkerson, and Johnson dantzig1954solution. It is obtained by substituting the set $\mathcal{Y}$ in with the polytope $\mathcal{Y}_{tour}$ defined by the conditions

<!-- chunk {"id": "body-0093", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

The first condition enforces usual bounds, the second forces the tour to visit every vertex, and the third requires that each vertex has two incident edges. The last condition is a *subtour-elimination constraint*. The set $\mathcal{E}_{\mathcal{U}}$ on the left-hand side consists of all edges that have both ends in $\mathcal{U}$. If $\mathcal{U}$ is the vertex set of a subtour (i.e., a cycle not covering every vertex), then the left-hand side equals $|\mathcal{U}|$ and the constraint is violated. These subtour-elimination constraints are exponential in number and typically enforced as *lazy constraints*: they are not included in the ILP from the beginning but are added only if a candidate solution violates them during branch and bound. Despite its exponential size, the ILP formulation is not be perfect (see (korte2018combinatorial Section 21.4) for a simple counterexample).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

The TSP in GCS corresponds to problem with $\mathcal{H} = \mathcal{H}_{tour}$. It is NP-hard since it generalizes the ordinary TSP. Following Algorithm 1, constraint (21a) is linearized as $y_{v} \geq y_{e} \geq 0$, and yields the valid constraints (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) and (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

Our MICP formulation of the TSP in GCS is then

<!-- chunk {"id": "body-0096", "role": "body", "section": "Traveling salesman", "weight": 1.0} -->

${minimize}\quad$ objective (17a ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) (23a)
${{subject}{to}}\quad$ ${{\mathbf{y}} \in \mathcal{Y}_{tour}^{bin}},$ (23b)
${\text{constraints~(}\text{),~(}\text{),~(}\text{),~(}\text{)}}.$ (23c)

<!-- chunk {"id": "body-0097", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

As a third example, we consider the Minimum Spanning Arborescence Problem (MSAP) in GCS, which is the directed version of the MSTP in GCS illustrated in Figure 1(c). (The analysis of the MSTP is similar to the one of the TSP.) In the ordinary MSAP, we are given a directed graph $G = {(\mathcal{V},\mathcal{E})}$ with a root vertex $r \in \mathcal{V}$, and we seek a minimum-weight spanning arborescence in $G$, i.e., an acyclic subgraph where every vertex can be reached from the root through a unique path. This problem is solvable in polynomial time chu1965shortest; edmonds1967optimum, and is a special case of the graph optimization problem where $\mathcal{H} = \mathcal{H}_{arb}$ is the set of all spanning arborescences in $G$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

Without loss of generality, this formulation assumes that the root has no incoming edges: $\delta_{r}^{-} = \varnothing$. The first condition is as usual, the second ensures that every vertex is reached, and the third requires that every vertex has one incoming edge, except for the root. The last condition is a *cutset constraint* that guarantees connectivity by requiring that every subset $\mathcal{U}$ of vertices, that does not include the root, has at least one incoming edge. (We denote by $\delta_{\mathcal{U}}^{-}$ the set of edges $(v,w)$ with $w \in \mathcal{U}$.) Like the subtour-elimination constraints, the cutset constraints are exponential in number and enforced as lazy constraints in practice. Contrarily to the TSP, this exponential-size formulation of the MSAP is perfect (see, e.g., (schrijver2003combinatorial Corollary 52.3b)).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

The MSAP in GCS is obtained from problem by letting $\mathcal{H} = \mathcal{H}_{arb}$. It is NP-hard as it generalizes the NP-hard MSTP with neighborhoods analyzed in (yang2007minimum Theorem 1). As already noted, our constraint-generation procedure maps constraint (24a) to (17c ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")). While the affine constraint (24c) is mapped to the linear constraint

<!-- chunk {"id": "body-0100", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

Our MICP formulation of the MSAP in GCS is then

<!-- chunk {"id": "body-0101", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

${minimize}\quad$ objective (17a ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) (26a) ${{subject}{to}}\quad$ ${{\mathbf{y}} \in \mathcal{Y}_{arb}^{bin}},$ (26b) ${\text{constraints~(}\text{),~(}\text{),~(}\text{)}},$ (26c) ${{({{\mathbf{z}}_{v} - {\mathbf{z}}_{v}^{e}},{1 - y_{e}})} \in {\overset{\sim}{\mathcal{X}}}_{v}},$ ${e = {(v,w)} \in

<!-- chunk {"id": "body-0102", "role": "body", "section": "Minimum spanning arborescence", "weight": 1.0} -->

The last constraint of this MICP is part of (17d ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")). It is kept by Algorithm 1 since the constraints in associated with a vertex $v \in \mathcal{V}$ do not imply the subgraph inequality $y_{v} \geq y_{e}$ for $e \in \delta_{v}^{+}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Facility location", "weight": 1.0} -->

In the Facility-Location Problem (FLP) we are given a weighted graph $G$ that is undirected and bipartite. The vertices $\mathcal{V}$ are composed by two subsets, the facilities $\mathcal{B}$ and the clients $\mathcal{C}$. Every edge connects a facility and a client. We seek a minimum-weight assignment of each client to a facility, i.e., a subgraph where each client in $\mathcal{C}$ has exactly one incident edge. The FLP is NP-hard (korte2018combinatorial Proposition 22.1), and is a special case of problem where the set $\mathcal{H} = \mathcal{H}_{assig}$ consists of all assignments in $G$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Facility location", "weight": 1.0} -->

The ILP models the FLP when the polytope $\mathcal{Y} = \mathcal{Y}_{assig}$ enforces

<!-- chunk {"id": "body-0105", "role": "body", "section": "Facility location", "weight": 1.0} -->

The first condition is a standard subgraph constraint and the second ensures that each client is assigned to exactly one facility. This ILP formulation is compact but can be weak (as expected, given the problem hardness).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Facility location", "weight": 1.0} -->

The FLP in GCS corresponds to problem with $\mathcal{H} = \mathcal{H}_{assig}$. It is NP-hard since the FLP is NP-hard. As seen already, constraint (27a) yields

<!-- chunk {"id": "body-0107", "role": "body", "section": "Facility location", "weight": 1.0} -->

The MICP resulting from Algorithm 1 is then

<!-- chunk {"id": "body-0108", "role": "body", "section": "Facility location", "weight": 1.0} -->

${minimize}\quad$ objective (17a ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) (30a)
${{subject}{to}}\quad$ ${{\mathbf{y}} \in \mathcal{Y}_{assig}^{bin}},$ (30b)
${\text{constraints~(}\text{),~(}\text{),~(}\text{)}}.$ (30c)

<!-- chunk {"id": "body-0109", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

The Bipartite-Matching Problem (BMP) is a special case of the FLP in which the number of facilities $\mathcal{B}$ and clients $\mathcal{C}$ is equal, and each facility must be matched with exactly one client.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

This formulation is perfect (see, e.g., (schrijver2003combinatorial Theorem 18.1)) and the BMP is solvable in polynomial time.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

The BMP in GCS is also efficiently solvable, as it reduces to the ordinary BMP. To show this, we fix a matching in the GCS and consider one of its edges $e = {\{ v,w\}} \in \mathcal{E}$. The optimal values of ${\mathbf{x}}_{v}$ and ${\mathbf{x}}_{w}$ are independent of the other continuous variables, and can be computed via the convex program

<!-- chunk {"id": "body-0112", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

where the objective is linear by Assumption 2 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."). We then consider the weighted graph obtained by setting the weight of each edge $e$ in the GCS to the optimal value of problem, and all vertex weights to zero. A matching in this weighted graph is optimal if and only if it is optimal in the original GCS.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

Since the BMP in GCS is reducible to the ordinary BMP via $|\mathcal{E}|$ small convex programs, mixed-integer programming is not a practical way of solving this problem. Nevertheless, it is noteworthy that our MICP formulation is perfect for this problem, and allows us to solve the BMP in GCS via a single convex program. Through the usual steps, our MICP is given by

<!-- chunk {"id": "body-0114", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

${minimize}\quad$ objective (17a ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) (33a)
${{subject}{to}}\quad$ ${{\mathbf{y}} \in \mathcal{Y}_{match}^{bin}},$ (33b)
${\text{constraints~(}\text{),~(}\text{)}},$ (33c)
${{\mathbf{z}}_{v} = {\sum\limits_{e \in \delta_{v}}{\mathbf{z}}_{v}^{e}}},$ ${v \in \mathcal{V}},$ (33d)

<!-- chunk {"id": "body-0115", "role": "body", "section": "Bipartite matching", "weight": 1.0} -->

where the last constraint is generated from (31b).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Unbounded constraint sets and nonlinear objective functions", "weight": 1.0} -->

The techniques in the previous sections rely on Assumptions 1 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") and 2 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."), which require the GCS constraint sets and objective functions to be bounded and linear, respectively. Here we show that the same techniques continue to apply under the weaker assumption below.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Assumption 3 (Superlinear vertex objectives)", "weight": 1.0} -->

Note that this assumption is trivially satisfied if the sets $\mathcal{X}_{v}$ are bounded, since the only recession direction of a bounded set is zero. We also highlight that the analysis of the SPP in GCS in marcucci2024shortest relies on this stronger boundedness assumption, which is relaxed here.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Homogenization of unbounded sets", "weight": 1.0} -->

Dropping Assumptions 1 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") and 2 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") requires extending the homogenization operation to unbounded sets.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Example 3", "weight": 1.0} -->

Consider the unbounded interval $\mathcal{X} = {\lbrack 1,\infty)} \subset {\mathbb{R}}$. Its homogenization is the closure of the set ${\{{(x,y)}:{0 < y \leq x}\}} \cup {\{{}\}}$. Taking the closure includes the positive $x$-axis (i.e., the recession cone $\mathcal{X}^{\infty}$), yielding the set $\overset{\sim}{\mathcal{X}} = {\{{(x,y)}:{0 \leq y \leq x}\}}$ shown in Figure 3.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Example 3", "weight": 1.0} -->

The homogenization $\overset{\sim}{\mathcal{X}}$ of an unbounded set is still a closed convex cone, and we also still have that ${({\mathbf{x}},1)} \in \overset{\sim}{\mathcal{X}}$ if and only if ${\mathbf{x}} \in \mathcal{X}$. However, the condition ${({\mathbf{x}},0)} \in \overset{\sim}{\mathcal{X}}$ is not equivalent to ${\mathbf{x}} = \mathbf{0}$ in the unbounded case, but holds if and only if $\mathbf{x}$ is a recession direction of $\mathcal{X}$, i.e., ${\mathbf{x}} \in \mathcal{X}^{\infty}$ (rockafellar1970convex Theorem 8.2).

<!-- chunk {"id": "body-0121", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

We handle nonlinear GCS objective functions by working with their epigraphs, so that the only difficulty is the unboundedness of the GCS constraint sets. The latter is addressed by retracing the steps from Section 4 and adapting the proofs that rely on the boundedness assumption.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

Observe that, in terms of these new sets, Assumption 3 ‣ 7 Unbounded constraint sets and nonlinear objective functions ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") states that any recession direction $({\mathbf{x}}_{v},s_{v})$ of $\mathcal{X}_{v}^{\prime}$ must be such that ${\mathbf{x}}_{v} = \mathbf{0}$ and $s_{v} \geq 0$.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

The only difference between this problem and the one considered in Section 4 is that the new sets $\mathcal{X}_{v}^{\prime}$ and $\mathcal{X}_{e}^{\prime}$ are unbounded, and violate Assumption 1 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.").

<!-- chunk {"id": "body-0124", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

Assumption 1 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") was first used to omit the constraint ${\mathbf{z}}_{v} = {y_{v}{\mathbf{x}}_{v}}$ from the MINCP. In particular, it ensured that, if $y_{v} = 0$, then the constraint ${({\mathbf{z}}_{v},y_{v})} \in {\overset{\sim}{\mathcal{X}}}_{v}$ enforces ${\mathbf{z}}_{v} = \mathbf{0}$, and the objective contribution of vertex $v$ is zero.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

To show that the same holds under Assumption 3 ‣ 7 Unbounded constraint sets and nonlinear objective functions ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."),

<!-- chunk {"id": "body-0126", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

where we introduced the auxiliary variables $t_{v} = {y_{v}s_{v}}$ for $v \in \mathcal{V}$ and $t_{e} = {y_{e}s_{e}}$ for $e \in \mathcal{E}$. When $y_{v} = 0$, the second constraint forces $({\mathbf{z}}_{v},t_{v})$ to be a recession direction of $\mathcal{X}_{v}^{\prime}$. As noted above, this implies that ${\mathbf{z}}_{v} = \mathbf{0}$ and $t_{v} \geq 0$. Since $t_{v}$ does not appear in other constraints and is minimized by the objective, its optimal value is zero as desired.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

The constraint-generation procedure in Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") is easily adapted to the MINCP. The valid convex constraint (16 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) is now

<!-- chunk {"id": "body-0128", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

where $t_{v}^{e} = {y_{e}s_{v}}$ for all $v \in \mathcal{V}$ and $e \in \delta_{v}$. This leads us to the following MICP formulation of problem, which parallels (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")):

<!-- chunk {"id": "body-0129", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

The second use of Assumption 1 ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") was in the proof of Theorem 4.1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."), where we showed that the valid convex constraints imply the original bilinear constraint. The proof that constraints (37c) and (37d) imply ${\mathbf{z}}_{v}^{e} = {y_{e}{\mathbf{z}}_{v}}$ for all $v \in \mathcal{V}$ and $e \in \delta_{v}$ is essentially unchanged.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

However, we must now also verify that the bilinear constraint $t_{v}^{e} = {y_{e}t_{v}}$ holds at optimality of the MICP.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Epigraph formulation of the GCS problem", "weight": 1.0} -->

The variants of the constraint-generation procedure in Section 5.1 and the multiple MICPs in Section 6 are easily adapted to the weaker assumptions of this section, analogously to how Lemma 1 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.") is adapted.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

We present multiple numerical examples of the GCS problems introduced in Section 6, as well as a comparison between our MICP and alternative approaches for solving GCS problems globally. The results can be reproduced using the GCSOPT library described in Section 9 below. The computer used for the experiments is a laptop with processor 2.4 GHz 8-Core Intel Core i9 and memory 64 GB 2667 MHz DDR4. The MICP solver is Gurobi 12.0.3.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

We consider a solar-powered helicopter that flies between two islands of an archipelago in minimum time. When the battery runs low, the helicopter can take a recharging break on any island, at the cost of increasing the flight time.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

The archipelago is shown in the top of Figure 4 and composed of $I = 300$ islands. For $i = {1,\ldots,I}$, each island is a circle $\mathcal{C}_{i} \subset {\mathbb{R}}^{2}$ with center ${\mathbf{c}}_{i}$ and radius $r_{i}$ drawn uniformly from the intervals $\lbrack{},{}\rbrack$ and $\lbrack 0.02,0.1\rbrack$, respectively. A sampled island is rejected if it intersects with existing islands. The start island is in the bottom left (labeled with $i = 1$) and the goal island is in the top right (labeled with $i = I$). The flight speed is constant and equal to $s = 1$. The battery level over time is described by the function $b:{{\mathbb{R}}\rightarrow{\lbrack 0,1\rbrack}}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

It decreases at rate $\alpha = 5$ when the helicopter is flying, and increases at rate $\beta = 1$ during a recharging break. Initially, the battery is fully charged.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

We formulate the problem as an SPP in GCS. Our GCS has one vertex per island, $\mathcal{V} = {\{ 1,\ldots,I\}}$. The source vertex $\sigma = 1$ is paired with the start island, and the target vertex $\tau = I$ with the goal island. Each vertex $i = {1,\ldots,I}$ has continuous variable ${\mathbf{x}}_{i} = {({\mathbf{p}}_{i},{\mathbf{b}}_{i})} \in {\mathbb{R}}^{4}$: the vector ${\mathbf{p}}_{i} \in {\mathbb{R}}^{2}$ represents the recharge point if the helicopter stops on the $i$th island, and ${\mathbf{b}}_{i} \in {\mathbb{R}}^{2}$ contains the battery level before and after the stop.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

(The variables $b_{1,1}$ and $b_{I,2}$ are actually redundant, but simplify the notation.) The recharging time on the $i$th island is a linear function of the battery levels, $t_{i} = {{({b_{i,2} - b_{i,1}})}/\beta}$. The convex set $\mathcal{X}_{i}$ forces the recharge point to lie on the island, ${\mathbf{p}}_{i} \in \mathcal{C}_{i}$, the battery levels to not exceed their limits, ${\mathbf{b}}_{i} \in {\lbrack 0,1\rbrack}^{2}$, and the recharging time to be nonnegative, $t_{i} \geq 0$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

The set $\mathcal{X}_{1}$ paired with the start island also ensures that the battery is fully charged at the beginning of the flight, $b_{1,2} = 1$. The objective function of each vertex $i$ is equal to the recharging time $t_{i}$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

We connect two islands with an edge if the helicopter can fly between them starting with full battery. Specifically, for ${{i,j} = 1},{\ldots,I}$, we have ${(i,j)} \in \mathcal{E}$ if only if $i \neq j$ and ${{\|{{\mathbf{c}}_{j} - {\mathbf{c}}_{i}}\|}_{2} - {({r_{i} + r_{j}})}} \leq {s/\alpha}$. This leads to a graph with ${|\mathcal{E}|} = 2146$ edges. The cost of edge $(i,j)$ is equal to the flight time between islands $i$ and $j$, which is computed from the battery levels as $t_{ij} = {{({b_{i,2} - b_{j,1}})}/\alpha}$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

The edge constraints require that this value is not smaller than the flight distance divided by the speed: $t_{ij} \geq {{\|{{\mathbf{q}}_{j} - {\mathbf{q}}_{i}}\|}_{2}/s}$. (Although we would like to enforce this constraint as a nonconvex equality, the convex inequality is sufficient since it is always tight at optimality.)

<!-- chunk {"id": "body-0141", "role": "body", "section": "Minimum-time flight of a solar-powered helicopter", "weight": 1.0} -->

The problem is automatically translated into the MICP and solved with Gurobi. The homogenization of the quadratic vertex and edge constraints leads to a Mixed-Integer Second-Order-Cone Program (MISOCP), as discussed in Section 9.4 below. The convex relaxation of this MISOCP nearly preserves the exactness of the ordinary SPP relaxation: its optimal value is $29.96$ and the relaxation gap is only $0.2\%$. The MISOCP solution time is $23.5$ s.^11^1For this problem, we set the parameter PreMIQCPForm to $1$, which forces Gurobi to handle the model as an MISOCP. With the default setting, the convex relaxation would instead be solved through a sequence of linear programs, and the quadratic terms linearized during branch and bound. Although this linearization can be beneficial when many iterations are needed, it is counterproductive in our case, where the convex relaxation is essentially exact.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Optimal school-bus tour", "weight": 1.0} -->

It is the end of summer in Manhattan, and the local school is planning the route of the bus that will pick up the kids every morning. Due to heavy traffic, the school decides to optimize the pick-up points and have the children walk a few blocks to meet the bus.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Optimal school-bus tour", "weight": 1.0} -->

The school is located at the intersection of the $45$th street and the $7$th avenue: ${\mathbf{p}}_{0}:={}$. The number of kids is $I = 18$, and the house of each kid has integer position ${\mathbf{p}}_{i}$ drawn uniformly at random between $$ and $$ for $i = {1,\ldots,I}$. The goal is to find integer pick-up points ${\mathbf{x}}_{i}$, for $i = {1,\ldots,I}$, that minimize the sum of the distances traveled by the school bus and the kids (distances are measured using the $\mathcal{L}_{1}$ norm). The parents do not want the kids to walk for more than $d_{\max} = 3$ blocks. Figure 6 shows the optimal solution of this problem.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Optimal school-bus tour", "weight": 1.0} -->

We solve the problem as a TSP in GCS. We construct an undirected graph $G = {(\mathcal{V},\mathcal{E})}$ with ${|\mathcal{V}|} = {I + 1} = 19$ vertices. One vertex represents the school and the others represent the kids. The school vertex is labeled as zero and has continuous variable ${\mathbf{x}}_{0}$. The set $\mathcal{X}_{0}$ enforces the equality ${\mathbf{x}}_{0} = {\mathbf{p}}_{0}$, and the objective function $f_{0}$ is zero. The kid's vertices are labeled as $i = {1,\ldots,I}$, and have variables ${\mathbf{x}}_{i} \in {\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Optimal school-bus tour", "weight": 1.0} -->

Each edge $e = {\{ i,j\}}$ has objective function equal to the distance traveled by the bus, ${f_{e}{({\mathbf{x}}_{i},{\mathbf{x}}_{j})}} = {\|{{\mathbf{x}}_{j} - {\mathbf{x}}_{i}}\|}_{1}$. Although this GCS allows the pick-up points ${\mathbf{x}}_{i}$ to be fractional, it can be verified that there always exists an optimal solution with integral pick-up points, thanks to the $\mathcal{L}_{1}$ metric and the integral home positions ${\mathbf{p}}_{i}$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Optimal school-bus tour", "weight": 1.0} -->

Since the homogenization of a polyhedral set is a polyhedral cone (see Section 9.4 below), the MICP is a Mixed-Integer Linear Program (MILP) in this case. The subtour-elimination constraints (21d) are added as lazy constraints: every time an integer solution is found, we check if it contains subtours and, if it does, we eliminate a subtour with the smallest number of edges. The problem has optimal value equal to $79.0$ and the solver runtime is $18.7$ s. The MICP convex relaxation, without the subtour-elimination constraints, has optimal value $57.1$, yielding a relaxation gap of $27.7\%$. This relatively large relaxation gap reflects the weakness of the ILP formulation of the ordinary TSP, that our MICP builds upon.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Camera positioning with visibility constraints", "weight": 1.0} -->

As an example of the MSAP in GCS, we consider the problem of positioning surveillance cameras in a floor with many rooms. A camera is to be installed in each room, as close as possible to the room center. Each camera must be visible to at least another camera, ensuring that any attempt to disable it is recorded by a neighboring device. Furthermore, starting from any camera and tracing back through the camera that sees it, one must eventually reach the camera located in the main room of the building, where the central alarm system is located. In other words, the visibility graph of the cameras must form a spanning arborescence rooted at the main room, such that every room is connected to the main room through a visibility path. (This problem is similar in spirit to classical problems in computational geometry such as the art-gallery and watchman-route problems o1987art; chin1986optimum.)

<!-- chunk {"id": "body-0148", "role": "body", "section": "Camera positioning with visibility constraints", "weight": 1.0} -->

The rooms are axis-aligned rectangles arranged on a uniform grid of size $I = 60$ by $J = 15$, for a total of ${IJ} = 900$ rooms. The room centers have coordinates $(i,j)$ for $i = {1,\ldots,I}$ and $j = {1,\ldots,J}$. If $i + j$ is even (respectively, odd), the room centered at $(i,j)$ has horizontal and vertical (respectively, vertical and horizontal) sides drawn uniformly from the intervals $\lbrack{4/3},2\rbrack$ and $\lbrack{2/3},1\rbrack$. This ensures that the room intersects only with the four neighboring rooms, centered at $({i \pm 1},j)$ and $(i,{j \pm 1})$. The main room (i.e., the room that all rooms should be connected to) has center $$.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Camera positioning with visibility constraints", "weight": 1.0} -->

We model the problem via a directed GCS with one vertex per room, ${|\mathcal{V}|} = 900$. For each $v \in \mathcal{V}$, the variable ${\mathbf{x}}_{v} \in {\mathbb{R}}^{2}$ represents the camera position, and the set $\mathcal{X}_{v}$ constrains it to lie within the room boundaries. The objective function $f_{v}$ is a weighted $\mathcal{L}_{\infty}$ norm that evaluates to zero at the room center and $0.1$ at the room walls. We connect every pair of adjacent rooms with two directed edges, yielding a total of ${|\mathcal{E}|} = 3448$ edges. The edge objective functions are zero.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Camera positioning with visibility constraints", "weight": 1.0} -->

To capture visibility relations, the edge constraints must ensure that there is direct line of sight between ${\mathbf{x}}_{v}$ and ${\mathbf{x}}_{w}$ whenever edge $e = {(v,w)} \in \mathcal{E}$ is selected. Enforcing this relation exactly would require the nonconvex constraint ${{{({1 - \lambda})}{\mathbf{x}}_{v}} + {\lambda{\mathbf{x}}_{w}}} \in {\mathcal{X}_{v} \cup \mathcal{X}_{w}}$ for all $\lambda \in {\lbrack 0,1\rbrack}$. Instead, we enforce a simple sufficient condition: if edge $e$ is selected, then ${\mathbf{x}}_{w}$ must lie in $\mathcal{X}_{v} \cap \mathcal{X}_{w}$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Camera positioning with visibility constraints", "weight": 1.0} -->

The MICP is an MILP, with the cutset constraints (24d) enforced as lazy constraints. For this problem, we found it more effective to eliminate all minimum-length cycles at each callback, rather than just one of them. The problem has optimal value $25.5$ and the solver runtime is $54.6$ s. Without the cutset constraints, the convex relaxation has optimal value $24.2$, i.e., the relaxation gap is only $5.0\%$. This low relaxation gap is due to the strength of the original ILP formulation of the discrete MSAP. The branch-and-bound progress is shown in Figure 9: the lower bound is almost exact from the start and the solver converges immediately after finding a feasible solution.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

Collision checking is a fundamental operation in physics engines for robotic simulation. Given the angle of each joint, we must ensure that the robot does not collide with the environment or with itself. Exact collision checks are often intractable, since robot links can have complex curved geometry. A common workaround is to enclose each link with a set of simple shapes, typically spheres. We formulate this approximation problem as an FLP in GCS.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

We consider the simple two-dimensional robot link shown in Figure 10. This is described by a mesh with $I = 17$ triangles, $\mathcal{T}_{i} \subset {\mathbb{R}}^{2}$ for $i = {1,\ldots,I}$. We seek a collection of circles $\mathcal{C}_{j} \subset {\mathbb{R}}^{2}$, with $j = {1,\ldots,J}$, such that each triangle $\mathcal{T}_{i}$ is contained in at least one circle $\mathcal{C}_{j}$. We denote by ${\mathbf{c}}_{j}$ and $r_{j}$ the center and the radius of the circle $\mathcal{C}_{j}$. Among all possible solutions, we want one that minimizes the sum of the circle areas. We impose a budget of at most $J = 5$ circles, but allow the solution to use fewer circles if advantageous.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

The optimal solution is shown in Figure 10, and uses the whole budget of five circles to cover the triangular mesh.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

We formulate an FLP in GCS where the mesh triangles are clients, $\mathcal{C} = {\{ 1,\ldots,I\}}$, and the cover circles are facilities, $\mathcal{B} = {\{ 1,\ldots,J\}}$. The total number of vertices is ${|\mathcal{V}|} = {I + J} = 22$. The clients do not need continuous variables but, to comply with our problem statement, we assign them an auxiliary continuous variable which we constrain to be zero. Also the client objective functions are zero.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

Each facility $j \in \mathcal{B}$ is paired with the vector ${\mathbf{x}}_{j} = {({\mathbf{c}}_{j},r_{j})} \in {\mathbb{R}}^{3}$, and has objective function equal to the circle area ${f_{j}{({\mathbf{x}}_{j})}} = {\pir_{j}^{2}}$. The set $\mathcal{X}_{j}$ forces the center ${\mathbf{c}}_{j}$ to lie in the smallest axis-aligned rectangle that contains the whole mesh, and lower bounds the radius $r_{j}$ with the radius of the smallest circle enclosing the smallest triangle in the mesh.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

We do not enforce an upper bound on the radius $r_{j}$ (recall that, according to Assumption 3 ‣ 7 Unbounded constraint sets and nonlinear objective functions ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."), the superlinear growth of the objective $f_{j}$ with $r_{j}$ is sufficient for the validity of our MICP).

<!-- chunk {"id": "body-0158", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

The GCS has ${|\mathcal{E}|} = {IJ} = 85$ edges, all with zero cost. For each edge $e = {\{ i,j\}}$, the set $\mathcal{X}_{e}$ constrains the vertices of the triangle $\mathcal{T}_{i}$ to lie in the circle $\mathcal{C}_{j}$, ensuring that the solution of the FLP in GCS covers the whole mesh.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Circle cover of two-dimensional robot link", "weight": 1.0} -->

The quadratic objective and constraints make the MICP an MISOCP. The optimal value of this problem and its convex relaxation are $62.1$ and $22.2$, yielding a relaxation gap of $64\%$. The relatively loose relaxation is this case inherited from ILP formulation of the ordinary FLP. Despite this, the problem size is moderate, and the solver converges in $23.4$ s.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

A direct solution of the MINCP using the spatial branch-and-bound algorithm available in Gurobi 12. This algorithm has seen significant improvements in this solver release, and can handle nonconvex quadratic constraints. This approach is representative of existing MINCP formulations for graph problems with neighborhoods (although, as noted in Section 4.2, our MINCP improves upon them in multiple directions).

<!-- chunk {"id": "body-0161", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

A basic MICP formulation based on McCormick envelopes mccormick1976computability and solved with Gurobi 12. For all vertices $v \in \mathcal{V}$, we assume that the set $\mathcal{X}_{v}$ is bounded and denote by $\mathcal{B}_{v} \supseteq \mathcal{X}_{v}$ be the smallest bounding box that contains it. Using homogenization transformations, the standard McCormick envelope of the bilinear constraints can be written as

<!-- chunk {"id": "body-0162", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

Replacing (14e) with these constraints yields a correct MICP formulation of the GCS problem, which, however, is easily seen to be weaker than (17 ‣ 4.3 Convex relaxation of the bilinear constraint ‣ 4 Base mixed-integer convex formulation of the GCS problem ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs.")) and our tailored MICPs.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

The helicopter-flight problem from Section 8.1 (SPP in GCS), where we let the number of islands vary from $30$ to $300$ at increments of $30$. In parallel, we increment the horizontal size of the archipelago from $0.5$ to $5$ at increments of $0.5$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

The school-bus problem from Section 8.2 (TSP in GCS), where we let the number of kids vary from $2$ to $18$ at increments of $2$.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Comparison with alternative global solution methods", "weight": 1.0} -->

The camera-positioning problem from Section 8.3 (MSAP in GCS), where we vary the number of rooms in each row of the grid from $I_{\min} = 5$ to $I_{\max} = 60$ at increments of $5$, and we keep the number of rooms in each column equal to $J = 15$. Hence, the total number of rooms varies from ${I_{\min}J} = 75$ to ${I_{\max}J} = 900$.

<!-- chunk {"id": "body-0166", "role": "body", "section": "The GCSOPT Python library", "weight": 1.0} -->

This section presents GCSOPT: a Python library for formulating and solving GCS problems. We illustrate the high-level goals of GCSOPT, its usage, and the operations it performs behind the scenes. The library is freely available at

<!-- chunk {"id": "body-0167", "role": "body", "section": "The GCSOPT Python library", "weight": 1.0} -->

and can be installed via PyPI by running the following command in a terminal.

<!-- chunk {"id": "body-0168", "role": "body", "section": "The GCSOPT Python library", "weight": 1.0} -->

[⬇](data:text/plain;base64,cGlwIGluc3RhbGwgZ2Nzb3B0){download=""}

<!-- chunk {"id": "body-0169", "role": "body", "section": "High-level goals", "weight": 1.0} -->

The primary goal of GCSOPT is to provide a simple framework for modeling and solving GCS problems, with emphasis on ease of use and fast prototyping. The library offers a high-level interface that abstracts away most of the technical details discussed in this paper. Users can define a GCS through a simple graph modeling interface combined with the syntax of CVXPY diamond2016cvxpy, a widely used Python library for convex optimization. All low-level operations (such as constructing the MICP, sending it to a solver, and retrieving the solution) are handled automatically behind the scenes. By building on CVXPY, our library supports the definition of virtually any convex set and function, and is compatible with state-of-the-art solvers for mixed-integer optimization (such as Gurobi, Mosek, and CPLEX).

<!-- chunk {"id": "body-0170", "role": "body", "section": "High-level goals", "weight": 1.0} -->

We emphasize that, although GCSOPT is open source, most mixed-integer solvers are not, and need to be installed separately. For instance, the solver Gurobi, used in the experiments in Section 8, is freely available only for academic use. Nonetheless, competitive open-source mixed-integer conic solvers have begun to emerge (e.g., Pajarito coey2020outer ), and these will be automatically accessible in GCSOPT as soon as a CVXPY interface becomes available.

<!-- chunk {"id": "body-0171", "role": "body", "section": "High-level goals", "weight": 1.0} -->

We also mention that a fast implementation of the SPP in GCS is available in the open-source software Drake tedrake2019drake. Compared to Drake, GCSOPT offers a lighter code base, a simpler and more efficient translation of GCS problems into MICPs, and can solve virtually any GCS problem.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

As a basic example of the usage of GCSOPT, we illustrate the Python code necessary to solve the SPP in GCS in Figure 1(a).

<!-- chunk {"id": "body-0173", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

We start by importing the libraries GCSOPT and CVXPY. The latter is used to define the convex sets and functions in our problem.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,aW1wb3J0IGdjc29wdAppbXBvcnQgY3Z4cHk=){download=""}

<!-- chunk {"id": "body-0175", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,RyA9IGdjc29wdC5HcmFwaE9mQ29udmV4U2V0cyhkaXJlY3RlZD1UcnVlKQ==){download=""}

<!-- chunk {"id": "body-0176", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

We add ${|\mathcal{V}|} = 9$ vertices to the GCS, arranged on a square grid with side length $l = 3$. The vertex variables ${\mathbf{x}}_{v}$ are constrained by the convex sets $\mathcal{X}_{v}$ to lie within a circle of radius $r = 0.3$ centered at ${\mathbf{c}}_{v} = {(i,j)}$, for ${{i,j} = 0},{\ldots,{s - 1}}$ (note that Python uses zero-based indexing). In GCSOPT, every vertex must be assigned a name which, for example, can be used to retrieve the vertex from the graph instance. Here, we name each vertex after its center ${\mathbf{c}}_{v}$.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,bCA9IDMgIyBHcmlkIHNpZGUgbGVuZ3RoLgpyID0gMC4zICMgQ2lyY2xlIHJhZGl1cy4KZm9yIGkgaW4gcmFuZ2UobCk6CiAgZm9yIGogaW4gcmFuZ2UobCk6CiAgICBjdiA9IChpLCBqKSAjIENpcmNsZSBjZW50ZXIgYW5kIHZlcnRleCBuYW1lLgogICAgdiA9IEcuYWRkX3ZlcnRleChjdikgIyBWZXJ0ZXggd2l0aCBuYW1lIGN2LgogICAgeHYgPSB2LmFkZF92YXJpYWJsZSgyKSAjIENvbnRpbnVvdXMgdmFyaWFibGUgb2YgZGltZW5zaW9uIDIuCiAgICB2LmFkZF9jb25zdHJhaW50KGN2eHB5Lm5vcm0yKHh2IC0gY3YpIDw9IHIpICMgUG9pbnQgaW4gY2lyY2xlLg==){download=""}

<!-- chunk {"id": "body-0178", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

cv = (i, j) \# Circle center and vertex name.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

v = G.add_vertex(cv) \# Vertex with name cv.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

xv = v.add_variable \# Continuous variable of dimension 2.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

v.add_constraint(cvxpy.norm2(xv - cv) \<= r) \# Point in circle.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Next, we connect the vertices in the grid with directed edges. The first two for loops below move through the grid, and retrieve each vertex $v$ using its name. The variables associated with each vertex are stored in a list: to retrieve ${\mathbf{x}}_{v}$ we select the zeroth and only element in that list. In the third for loop, we connect vertex $v$ with the neighboring vertices $w$ on its right or above it. Each edge $e = {(v,w)}$ has objective function ${f_{e}{({\mathbf{x}}_{v},{\mathbf{x}}_{w})}} = {\|{{\mathbf{x}}_{w} - {\mathbf{x}}_{v}}\|}_{2}$.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zm9yIGkgaW4gcmFuZ2UobCk6CiAgZm9yIGogaW4gcmFuZ2UobCk6CiAgICBjdiA9IChpLCBqKSAjIE5hbWUgb2YgdmVydGV4IHYuCiAgICB2ID0gRy5nZXRfdmVydGV4KGN2KSAjIFJldHJpZXZlIHZlcnRleCB2IGZyb20gZ3JhcGguCiAgICB4diA9IHYudmFyaWFibGVzWzBdICMgR2V0IHplcm90aCB2YXJpYWJsZSBwYWlyZWQgd2l0aCB2LgogICAgbmVpZ2hib3JfbmFtZXMgPSBbKGkgKyAxLCBqKSwgKGksIGogKyAxKV0gIyBOZWlnaGJvcnMgb2Ygdi4KICAgIGZvciBjdyBpbiBuZWlnaGJvcl9uYW1lczoKICAgICAgaWYgRy5oYXNfdmVydGV4KGN3KTogIyBDb250aW51ZSBpZiBhIHZlcnRleCBpcyBuYW1lZCBjdy4KICAgICAgICB3ID0gRy5nZXRfdmVydGV4KGN3KSAjIFJldHJpZXZlIHZlcnRleCB3IGZyb20gZ3JhcGguCiAgICAgICAgeHcgPSB3LnZhcmlhYmxlc1swXSAjIEdldCB6ZXJvdGggdmFyaWFibGUgcGFpcmVkIHdpdGggdy4KICAgICAgICBlID0gRy5hZGRfZWRnZSh2LCB3KSAjIENvbm5lY3QgdiBhbmQgdy4KICAgICAgICBlLmFkZF9jb3N0KGN2eHB5Lm5vcm0yKHh3IC0geHYpKSAjIE9iamVjdGl2ZSBvZiBlZGdlIGUu){download=""}

<!-- chunk {"id": "body-0184", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

v = G.get_vertex(cv) \# Retrieve vertex v from graph.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

xv = v.variables \# Get zeroth variable paired with v.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

if G.has_vertex(cw): \# Continue if a vertex is named cw.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

w = G.get_vertex(cw) \# Retrieve vertex w from graph.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

xw = w.variables \# Get zeroth variable paired with w.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

e.add_cost(cvxpy.norm2(xw - xv)) \# Objective of edge e.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Now the GCS is fully specified, and we can solve the SPP through the MICP. This is formulated and solved automatically with the method solve_shortest_path. The parameters of this method are the source vertex $\sigma$ and target vertex $\tau$: the source is in the bottom left and has center ${\mathbf{c}}_{\sigma} = {}$, while the target is in the top right and has center ${\mathbf{c}}_{\tau} = {({l - 1},{l - 1})}$.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y3MgPSAoMCwgMCkgIyBTb3VyY2UgbmFtZS4KY3QgPSAobCAtIDEsIGwgLSAxKSAjIFRhcmdldCBuYW1lLgpzID0gRy5nZXRfdmVydGV4KGNzKSAjIFJldHJpZXZlIHNvdXJjZSB2ZXJ0ZXggZnJvbSBncmFwaC4KdCA9IEcuZ2V0X3ZlcnRleChjdCkgIyBSZXRyaWV2ZSB0YXJnZXQgdmVydGV4IGZyb20gZ3JhcGguCkcuc29sdmVfc2hvcnRlc3RfcGF0aChzLCB0KQ==){download=""}

<!-- chunk {"id": "body-0192", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

s = G.get_vertex(cs) \# Retrieve source vertex from graph.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

t = G.get_vertex(ct) \# Retrieve target vertex from graph.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

After solving a GCS problem, GCSOPT automatically populates the graph with the problem result. Below we print the optimal values of the problem and the variables paired with the vertices named $$ and $$.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,cHJpbnQoIlByb2JsZW0gb3B0aW1hbCB2YWx1ZToiLCBHLnZhbHVlKQpwcmludCgiVmFyaWFibGUgb3B0aW1hbCB2YWx1ZXM6IikKdmVydGV4X25hbWVzID0gWygwLCAxKSwgKDEsIDApXQpmb3IgY3YgaW4gdmVydGV4X25hbWVzOgogIHYgPSBHLmdldF92ZXJ0ZXgoY3YpCiAgeHYgPSB2LnZhcmlhYmxlc1swXQogIHByaW50KGN2LCB4di52YWx1ZSk=){download=""}

<!-- chunk {"id": "body-0196", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

print(\"Problem optimal value:\", G.value)

<!-- chunk {"id": "body-0197", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

The last code snippet results in the following terminal output. Observe that the second variable has no value since its vertex is not part of the optimal subgraph $H$ in Figure 1(a).

<!-- chunk {"id": "body-0198", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,UHJvYmxlbSBvcHRpbWFsIHZhbHVlOiAyLjQ1NjE2MjI0NzgyNzA2NzcKVmFyaWFibGUgb3B0aW1hbCB2YWx1ZXM6CigwLCAxKSBbMC4yNDQxMzU2MyAwLjgyNTY1MDM3XQooMSwgMCkgTm9uZQ==){download=""}

<!-- chunk {"id": "body-0199", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

GCSOPT also provides basic plotting functions for visualizing a GCS and the solution of a problem. These rely on the Python library Matplotlib and are limited to two-dimensional problems. The following code generates Figure 1(a).

<!-- chunk {"id": "body-0200", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

[⬇](data:text/plain;base64,aW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdCAjIEltcG9ydCBsaWJyYXJ5LgpwbHQuZmlndXJlKCkgIyBJbml0aWFsaXplIGVtcHR5IGZpZ3VyZS4KRy5wbG90XzJkKCkgIyBQbG90IEdDUy4KRy5wbG90XzJkX3NvbHV0aW9uKCkgIyBQbG90IG9wdGltYWwgc29sdXRpb24uCnBsdC5zaG93KCkgIyBTaG93IGZpZ3VyZS4=){download=""}

<!-- chunk {"id": "body-0201", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

import matplotlib.pyplot as plt \# Import library.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

plt.figure \# Initialize empty figure.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

G.plot_2d_solution \# Plot optimal solution.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

GCSOPT provides built-in functions for solving common GCS problems such as the SPP, TSP, MSTP, MSAP, and FLP. Moreover, leveraging Algorithm 1, it also allows the user to solve any nonstandard GCS problem of the form just by specifying a GCS and a polytope $\mathcal{Y}$. As an example, let us show how the SPP in GCS illustrated above can be solved without using the method solve_shortest_path.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

Starting from the graph G defined above, we initialize an empty list of affine ILP constraints that represent the polytope $\mathcal{Y}_{path}$. Then we add to this list a nonnegativity constraint for each edge binary variable, as in (18a).

<!-- chunk {"id": "body-0206", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

[⬇](data:text/plain;base64,aWxwID0gW10gIyBJbml0aWFsaXplIGVtcHR5IGxpc3Qgb2YgSUxQIGNvbnN0cmFpbnRzLgpmb3IgZSBpbiBHLmVkZ2VzOgogIHllID0gZS5iaW5hcnlfdmFyaWFibGUgIyBSZXRyaWV2ZSBlZGdlIGJpbmFyeSB2YXJpYWJsZS4KICBpbHAuYXBwZW5kKHllID49IDApICMgQWRkIGNvbnN0cmFpbnQgKDE4YSku){download=""}

<!-- chunk {"id": "body-0207", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

ilp = \# Initialize empty list of ILP constraints.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

ye = e.binary_variable \# Retrieve edge binary variable.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

Below are the other constraints defining the polytope $\mathcal{Y}_{path}$, from (18b) to (18e). The vertices s and t are the source and the target defined above.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zm9yIHYgaW4gRy52ZXJ0aWNlczoKICB5diA9IHYuYmluYXJ5X3ZhcmlhYmxlICMgUmV0cmlldmUgdmVydGV4IGJpbmFyeSB2YXJpYWJsZS4KICBpZiB2IGluIFtzLCB0XToKICAgIGlscC5hcHBlbmQoeXYgPT0gMSkgIyBDb25zdHJhaW50ICgxOGMpLgogIGVsc2U6CiAgICBpbHAuYXBwZW5kKHl2IDw9IDEpICMgQ29uc3RyYWludCAoMThiKS4KICBpZiB2ICE9IHM6CiAgICAjIFN1bSBiaW5hcnkgdmFyaWFibGVzIG9mIGVkZ2VzIGluY29taW5nIHZlcnRleCB2LgogICAgeWVfaW5jID0gc3VtKGUuYmluYXJ5X3ZhcmlhYmxlIGZvciBlIGluIEcuaW5jb21pbmdfZWRnZXModikpCiAgICBpbHAuYXBwZW5kKHl2ID09IHllX2luYykgIyBDb25zdHJhaW50ICgxOGQpLgogIGlmIHYgIT0gdDoKICAgICMgU3VtIGJpbmFyeSB2YXJpYWJsZXMgb2YgZWRnZXMgb3V0Z29pbmcgdmVydGV4IHYuCiAgICB5ZV9vdXQgPSBzdW0oZS5iaW5hcnlfdmFyaWFibGUgZm9yIGUgaW4gRy5vdXRnb2luZ19lZGdlcyh2KSkKICAgIGlscC5hcHBlbmQoeXYgPT0geWVfb3V0KSAjIENvbnN0cmFpbnQgKDE4ZSku){download=""}

<!-- chunk {"id": "body-0211", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

yv = v.binary_variable \# Retrieve vertex binary variable.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

\# Sum binary variables of edges incoming vertex v.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

ye_inc = sum(e.binary_variable for e in G.incoming_edges(v))

<!-- chunk {"id": "body-0214", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

\# Sum binary variables of edges outgoing vertex v.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

ye_out = sum(e.binary_variable for e in G.outgoing_edges(v))

<!-- chunk {"id": "body-0216", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

The method solve_from_ilp in the following code snippet applies Algorithm 1 to the list ilp of affine constraints. This automatically produces the MICP, including all the constraints tailored to the SPP in GCS. The problem is then solved, and the same optimal value as above is printed.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

[⬇](data:text/plain;base64,Ry5zb2x2ZV9mcm9tX2lscChpbHApICMgU29sdmUgTUlDUCBjb25zdHJ1Y3RlZCBieSBBbGdvcml0aG0gMS4KcHJpbnQoIlByb2JsZW0gb3B0aW1hbCB2YWx1ZToiLCBHLnZhbHVlKQ==){download=""}

<!-- chunk {"id": "body-0218", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

G.solve_from_ilp(ilp) \# Solve MICP constructed by Algorithm 1.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

print(\"Problem optimal value:\", G.value)

<!-- chunk {"id": "body-0220", "role": "body", "section": "Solving any GCS problem", "weight": 1.0} -->

The workflow just described allows the users of GCSOPT to easily solve complex GCS problems. For instance, Figure 13 shows the optimal solution of an inspection problem, where we seek a continuous closed curve of minimum Euclidean length that connects a set of designated rooms in a floor plan. The designated rooms are red, while the other rooms are green. Solid and dotted lines represent walls and open doors, respectively. The optimal curve is in dashed blue. The inspection problem can be formulated as a combination of an SPP and a TSP in GCS. The SPP component allows us to compute minimum-length curves around obstacles as explained in marcucci2023motion. The TSP component ensures that every designated room is visited at least once. This mix of SPP and TSP constraints can be described in approximately $50$ lines of code and passed to the method solve_from_ilp, which produces the curve shown in Figure 13. Note that this modeling effort is negligible and far less error prone than directly formulating the inspection problem as an MICP.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Automatic formulation of the MICP", "weight": 1.0} -->

At the core of GCSOPT is the observation that, as noted in (moehle2015perspective Section 2), computing the homogenization of a set in conic form is particularly simple. Recall that a closed convex set $\mathcal{X} \subseteq {\mathbb{R}}^{n}$ is described in *conic form* if we are given a matrix ${\mathbf{C}} \in {\mathbb{R}}^{m \times n}$, a vector ${\mathbf{d}} \in {\mathbb{R}}^{m}$, and a closed convex cone $\mathcal{K} \subseteq {\mathbb{R}}^{m}$ such that

<!-- chunk {"id": "body-0222", "role": "body", "section": "Automatic formulation of the MICP", "weight": 1.0} -->

For example, polyhedra, ellipsoids, and spectrahedra can all be described in conic from for appropriate choices of the cone $\mathcal{K}$. The homogenization of a closed convex set $\mathcal{X}$ in conic form is simply

<!-- chunk {"id": "body-0223", "role": "body", "section": "Automatic formulation of the MICP", "weight": 1.0} -->

(Note that here we do not take the closure as in Definition 3 ‣ 7.1 Homogenization of unbounded sets ‣ 7 Unbounded constraint sets and nonlinear objective functions ‣ A Unified and Scalable Method for Optimization over Graphs of Convex Sets The material presented in this paper is partially based on the author’s PhD thesis marcucci2024graphs."), since $\{{\mathbf{x}}:{{{\mathbf{C}}{\mathbf{x}}} \in \mathcal{K}}\}$ is exactly the recession cone $\mathcal{X}^{\infty}$.) Note also that this formula implies that, if we can efficiently optimize over a set $\mathcal{X}$ in conic form, then we can also efficiently optimize over its homogenization $\overset{\sim}{\mathcal{X}}$.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Automatic formulation of the MICP", "weight": 1.0} -->

Using the formula, the MICPs presented in this paper can be implemented in only a few tens of lines of code. Following the steps in Section 7, we add a slack variable per vertex and edge to make all GCS objective functions linear. Using CVXPY reductions and the disciplined-convex-programming rule set grant2006disciplined, vertex and edge constraint sets are automatically converted to conic form. This allows us to easily enforce any constraint of the form, produced by our constraint-generation technique, as well as the edge constraint (37e).

<!-- chunk {"id": "body-0225", "role": "body", "section": "Modeling guidelines for strong formulations", "weight": 1.0} -->

GCSOPT provides a high-level interface for defining GCS problems that shields the user from the complexity of formulating an efficient MICP. However, given the hardness of most GCS problems, and the worst-case exponential runtime of branch and bound, it is unavoidable that some of the user's modeling choices can have a noticeable effect on the solution times. Below are simple guidelines that can help the user make the underlying MICP more efficient.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Modeling guidelines for strong formulations", "weight": 1.0} -->

A first guideline is to keep the sets $\mathcal{X}_{v}$ for $v \in \mathcal{V}$ and $\mathcal{X}_{e}$ for $e \in \mathcal{E}$ as small as possible. Adding vertex and edge constraints that cut unnecessary portions of these sets (but do not alter the MICP optimal value and are computationally light) can tighten the convex relaxation and accelerate the branch and bound. For example, in the circle-cover problem in Section 8.4, our sets $\mathcal{X}_{v}$ constrain each circle to be no smaller than the minimum enclosing circle of the smallest mesh triangle. A simpler constraint would only require the radii to be nonnegative, but this would slow down the MICP solve by roughly $30\%$.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Modeling guidelines for strong formulations", "weight": 1.0} -->

When solving nonstandard GCS problems via the method solve_from_ilp, it is important to recall that Algorithm 1 strengthens the MICP only through ILP constraints whose variables are associated with a common vertex. Accordingly, whenever possible, it is more effective to express ILP constraints in this form rather than as "global" constraints involving larger groups of binary variables. We also note that linear constraints that are redundant for the ILP can still strengthen the MICP, although they are not required for its correctness. For example, for an MSAP with nonnegative weights, the ILP constraint (24c) is redundant. Hence, omitting it still produces a correct MICP if the GCS objective functions are nonnegative. However, including it, together with the corresponding implied constraint, reduces the solve time of the camera-positioning problem in Section 8.3 by a factor of six.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Edge variables", "weight": 1.0} -->

To simplify the definition of certain constraints and objective functions, GCSOPT allows each edge $e \in \mathcal{E}$ to be associated with auxiliary variables ${\mathbf{x}}_{e} \in {\mathbb{R}}^{n_{e}}$. The edge constraint set and objective function are then $\mathcal{X}_{e} \subseteq {\mathbb{R}}^{n_{v} + n_{w} + n_{e}}$ and $f_{e}:{{\mathbb{R}}^{n_{v} + n_{w} + n_{e}}\rightarrow{\mathbb{R}}}$. Although this can simplify the implementation, the resulting GCS problem is mathematically equivalent to the one in Section 2.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Edge variables", "weight": 1.0} -->

Indeed, we can define an equivalent edge constraint set as the projection of $\mathcal{X}_{e}$ onto the subspace of the variables ${\mathbf{x}}_{v}$ and ${\mathbf{x}}_{w}$, and an equivalent edge objective function as the partial minimization of $f_{e}$ over the extra variable ${\mathbf{x}}_{e}$. These sets and functions satisfy all convexity, closure, and boundedness assumptions required by our framework (see, e.g., (boyd2004convex Section 3.2.5) for convexity). Thus, they can replace $\mathcal{X}_{e}$ and $f_{e}$, eliminating the extra variables ${\mathbf{x}}_{e}$.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Conclusions and future works", "weight": 1.0} -->

This paper introduces a unified methodology for solving GCS problems, extending the ideas from marcucci2024shortest beyond the SPP. Given an ILP that models an optimization problem over a weighted graph, our method automatically constructs an efficient MICP formulation for the corresponding GCS problem. We have implemented this framework in the Python library GCSOPT and demonstrated its applicability through a wide range of numerical examples.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Conclusions and future works", "weight": 1.0} -->

Our experiments show that the proposed MICPs often retain the strength of the ILP formulations that they build upon. For problems such as the SPP and MSAP in GCS, the convex relaxations of our MICPs provide tight lower bounds, and the branch-and-bound solver converges in a few iterations.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Conclusions and future works", "weight": 1.0} -->

As future work, we highlight that our library currently relies on general-purpose branch-and-bound solvers. We expect that specialized optimization algorithms designed to exploit the graph structure underlying our problems could be substantially faster. Furthermore, although already broadly applicable, the framework proposed in this paper admits several natural extensions. It could be adapted to incorporate extended formulations conforti2010extended or semidefinite formulations of graph optimization problems. It could also be extended to hypergraphs, i.e., graphs where edges can connect more than two vertices. Beyond graphs, analogous methodologies may be developed for other classes of discrete optimization problems, such as Boolean satisfiability or equilibrium problems arising in game theory.
