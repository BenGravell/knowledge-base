<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SnapVX: A Network-Based Convex Optimization Solver

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

SnapVX is a high-performance Python solver for convex optimization problems defined on networks. For these problems, it provides a fast and scalable solution with guaranteed global convergence. SnapVX combines the capabilities of two open source software packages: Snap.py and CVXPY. Snap.py is a large scale graph processing library, and CVXPY provides a general modeling framework for small-scale subproblems. SnapVX offers a customizable yet easy-to-use interface with out-of-the-box functionality. Based on the Alternating Direction Method of Multipliers (ADMM), it is able to efficiently store, analyze, and solve large optimization problems from a variety of different applications. Documentation, examples, and more can be found on the SnapVX website at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convex optimization is a widely used approach of modeling and solving problems in many different fields, as it offers well-established methods for finding globally optimal solutions. Numerous general-purpose optimization software packages exist, but they typically rely on algorithms that are difficult to scale, so many modern machine learning problems cannot be solved by these common, yet general, approaches. Instead, solving large scale examples often requires developing problem-specific solution methods, which can be very fast but require significant optimization expertise to build. Furthermore, they are limited in scope, as they must be fine-tuned to only one particular type of problem and thus are hard to generalize.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we build on the observation that many large convex optimization examples follow a common form in that they can often be split up into a series of subproblems using a network (graph) structure. Nodes are subproblems, representing anything from timestamps in a time-series data set to users in a social network. The edges then define the coupling, or relationships between the different nodes, and the combination of nodes and edges yields the original convex optimization problem. This representation can refer to problems defined on actual networks, such as social or transportation systems, or questions classically modeled in other ways, such as control theory or time-series analysis.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, we present SnapVX, a solver that is both scalable and general on optimization problems defined over networks. It combines the graph capabilities of Snap.py with the general modeling framework from CVXPY. We show how SnapVX works, present syntax and supported features, scale it to large problems, and describe how it can be used to solve convex optimization problems from a variety of different fields. The full version of our solver, which is released under the BSD Open-Source License, can be found at the project website, In addition to the source code, the download contains installation instructions, unit tests, documentation, and several examples to help users get started.

<!-- chunk {"id": "body-0006", "role": "body", "section": "SnapVX General Form", "weight": 1.0} -->

Variable $x_{i}$ is associated with node $i$, for $i = {1,\ldots,{|\mathcal{V}|}}$ (the size of $x_{i}$ can vary at each node). In problem, $f_{i}$ is the cost function at node $i$, and $g_{jk}$ is the cost associated with edge $(j,k)$. Constraints are represented by extended (infinite) values of $f_{i}$ and $g_{jk}$. Note that nodes and edges can also have local, private optimization variables (which can also vary in size). These remain confined to a single node or edge, though, whereas the $x_{i}$'s are shared between different parts of the network. We consider only convex objectives and constraints for $f_{i}$ and $g_{jk}$, so the entire problem is a convex optimization problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "SnapVX General Form", "weight": 1.0} -->

To solve problem, SnapVX uses a splitting algorithm based on the Alternating Direction Method of Multipliers (ADMM). With ADMM, each individual component of the graph solves its own subproblem, iteratively passing small messages over the network and eventually converging to an optimal solution. See the SnapVX developer documentation for more details on the underlying derivation. By splitting up the problem into a series of subproblems, SnapVX is able to solve much larger convex optimization examples than standard solvers, which solve the whole problem at once. ADMM also keeps the optimality benefits that general solvers enjoy: not only are we guaranteed to obtain an optimal solution, but we also are given a certificate of optimality in the form of primal and dual residuals; see.

<!-- chunk {"id": "body-0008", "role": "body", "section": "SnapVX General Form", "weight": 1.0} -->

SnapVX stores the network using a Snap.py graph structure. This allows fast traversal and easy manipulation, as well as efficient storage. On top of the standard graph, each node/edge is given convex objectives and constraints using CVXPY syntax. To find a global solution, SnapVX automatically splits up the problem and solves each subproblem using CVXPY, iteratively handling the ADMM message passing behind the scenes. Though wrapped in a Python layer, CVXPY uses ECOS and CVXOPT (two high-performance numerical optimization packages) as its primary underlying solvers, so the Python overhead is not significant and allows for easier interpretability and improved user interface. To parallelize the solver, a worker pool coordinates updates for the separate subproblems using Python's multiprocessing library. SnapVX is built to run on a single machine, parallelizing across multiple cores and allowing "out-of-the-box" functionality on machines ranging from standard laptops to large-memory servers.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

We now present usage of SnapVX on a simple example. Complete documentation and more examples are available on the SnapVX website. Consider two nodes with an edge between them. We solve for a problem where each node has an unknown variable $x_{i} \in {\mathbb{R}}^{1}$. The first node's objective is to minimize $x_{1}^{2}$ subject to $x_{1} \leq 0$, the second's is to minimize $|{x_{2} + 3}|$, and the edge objective penalizes the square norm difference between the two variables, ${\|{x_{1} - x_{2}}\|}_{2}^{2}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBzbmFwdnggaW1wb3J0ICoKZ3Z4ID0gVEdyYXBoVlgoKSAjQ3JlYXRlIGEgbmV3IGdyYXBoCngxID0gVmFyaWFibGUoMSwgbmFtZT0neDEnKSAjQ3JlYXRlIGEgdmFyaWFibGUgZm9yIG5vZGUgMQpndnguQWRkTm9kZSgxLCBPYmplY3RpdmU9c3F1YXJlKHgxKSwgQ29uc3RyYWludHM9W3gxIDw9IDBdKSAjQWRkIG5ldyBub2RlCngyID0gVmFyaWFibGUoMSwgbmFtZT0neDInKSAjUmVwZWF0IGZvciBub2RlIDIKZ3Z4LkFkZE5vZGUoMiwgYWJzKHgyICsgMyksIFtdKQpndnguQWRkRWRnZSgxLCAyLCBPYmplY3RpdmU9c3F1YXJlKG5vcm0oeDEgLSB4MikpLCBDb25zdHJhaW50cz1bXSkgI0FkZCBlZGdlIGJldHdlZW4gbm9kZXMKZ3Z4LlNvbHZlKCkgI1NvbHZlIHRoZSBwcm9ibGVtCmd2eC5QcmludFNvbHV0aW9uKCkgI1ByaW50IHRoZSBzb2x1dGlvbiBvbiBhIG5vZGUtYnktbm9kZSBiYXNpcw==){download=""}

<!-- chunk {"id": "body-0011", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

gvx = TGraphVX #Create a new graph

<!-- chunk {"id": "body-0012", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

x1 = Variable(1, name='x1') #Create a variable for node 1

<!-- chunk {"id": "body-0013", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

gvx.AddNode(1, Objective=square(x1), Constraints=\[x1 \<= 0\]) #Add new node

<!-- chunk {"id": "body-0014", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

x2 = Variable(1, name='x2') #Repeat for node 2

<!-- chunk {"id": "body-0015", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

gvx.AddEdge(1, 2, Objective=square(norm(x1 - x2)), Constraints=) #Add edge between nodes

<!-- chunk {"id": "body-0016", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

gvx.Solve #Solve the problem

<!-- chunk {"id": "body-0017", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

gvx.PrintSolution #Print the solution on a node-by-node basis

<!-- chunk {"id": "body-0018", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

As SnapVX is meant to be a general-purpose solver, it has many customizable options to help easily and efficiently solve a wide range of convex optimization problems. These include ADMM iteration limits, verbose mode (to list intermediate steps at each iteration), and defining customized convergence thresholds.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

Bulk Loading - Often, the objectives and constraints at each node or edge will share a common form. For example, all the nodes could be trying to minimize ${\|{x - a_{i}}\|}_{2}$ for different values of $a_{i}$. Rather than requiring users to manually input each of these values, SnapVX allows for "bulk loading" of data. The functions AddNodeObjectives and AddEdgeObjectives allow the user to specify the general form of the objectives and an external file with separate data, and SnapVX fills in the details. This functionality makes practical and significantly speeds up the loading of very large data sets.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Syntax and Supported Features", "weight": 1.0} -->

ADMM $\rho$-update - The convergence time of ADMM depends on the value of the penalty parameter $\rho$, as it affects the tradeoff between primal and dual convergence, both of which need to be obtained for the overall problem to be solved. SnapVX users are not only able to select the value of $\rho$ (it defaults to $\rho = 1$), but can also define a function to update $\rho$ after each iteration based on the primal and dual residual values.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scalability", "weight": 1.0} -->

One of the biggest benefits of SnapVX is that it allows us to solve large problems very efficiently. It does so by automatically parallelizing the ADMM updates across multiple cores of a single machine using Python's multiprocessing class. Note that SnapVX is meant to be run on a single machine, rather than in a distributed computing environment. Convergence time depends on the problem complexity, but we empirically observe that it scales approximately linearly with problem size. We compare SnapVX and a general solver for a problem on a 3-regular graph. Each node solves for an unknown variable in ${\mathbb{R}}^{9000}$, where the node objectives are sum-of-Huber penalties and edges have network lasso penalties. By varying the number of nodes, we can span a wide range of problem sizes. The time required for SnapVX to converge, on a 40-core CPU where the entire problem can fit into memory, is shown in Table 1. Figure 1 displays a comparison to a general-purpose solver (ECOS, via CVXPY) in log-log scale.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Scalability", "weight": 1.0} -->

## of Unknowns
SnapVX Solution Time (Minutes)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Applications", "weight": 1.0} -->

SnapVX was created to allow users without significant optimization expertise to solve large network-based convex optimization problems by taking advantage of the powerful and scalable ADMM algorithm. Common examples from many different fields can be formulated in a SnapVX-friendly manner. Our software has been used to solve machine learning problems ranging from housing price prediction to ride-sharing analysis to high-dimensional regression, often significantly outperforming other commonly used approaches. Examples in the SnapVX download package and on the project website --- including financial modeling, network inference, PageRank, and time-series analysis --- guide users towards applying the software to a variety of applications. Both user and developer documentation help new users get started and, if they are interested, contribute to the code base. A robust set of unit tests ensures that the software has been properly downloaded and that the code is functioning as expected. Overall, our open-source software provides an easy-to-use ADMM solver that can scale to large problems and apply to a wide variety of examples. With an active user base and rising interest from a range of scientific and engineering fields, we hope that SnapVX can become a useful tool for convex optimization problems, both in research and industry.
