<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CVXPY: A Python-Embedded Modeling Language for Convex Optimization

Topics include Convex optimization, Optimization, CVXPY.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

CVXPY is a domain-specific language for convex optimization embedded in Python. It allows the user to express convex optimization problems in a natural syntax that follows the math, rather than in the restrictive standard form required by solvers. CVXPY makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design. CVXPY is available at under the GPL license, along with documentation and examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convex optimization has many applications to fields as diverse as machine learning, control, finance, and signal and image processing. Using convex optimization in an application requires either developing a custom solver or converting the problem into a standard form. Both of these tasks require expertise, and are time-consuming and error prone. An alternative is to use a domain-specific language (DSL) for convex optimization, which allows the user to specify the problem in a natural way that follows the math; this specification is then automatically converted into the standard form required by generic solvers. CVX, YALMIP, QCML, PICOS, and Convex.jl are examples of such DSLs for convex optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

CVXPY is a new DSL for convex optimization. It is based on CVX, but introduces new features such as signed disciplined convex programming analysis and parameters. CVXPY is an ordinary Python library, which makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

CVXPY has been downloaded by thousands of users and used to teach multiple courses. Many tools have been built on top of CVXPY, such as an extension for stochastic optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "CVXPY Syntax", "weight": 1.0} -->

CVXPY has a simple, readable syntax inspired by CVX. The following code constructs and solves a least squares problem where the variable's entries are constrained to be between 0 and 1. The problem data $A \in \text{R}^{m \times n}$ and $b \in \text{R}^{m}$ could be encoded as NumPy ndarrays or one of several other common matrix representations in Python.

<!-- chunk {"id": "body-0007", "role": "body", "section": "CVXPY Syntax", "weight": 1.0} -->

## Construct the problem
objective = Minimize(sum_squares(A*x - b))
prob = Problem(objective, constraints)

<!-- chunk {"id": "body-0008", "role": "body", "section": "CVXPY Syntax", "weight": 1.0} -->

## The optimal objective is returned by prob.solve
result = prob.solve
## The optimal value for x is stored in x.value

<!-- chunk {"id": "body-0009", "role": "body", "section": "CVXPY Syntax", "weight": 1.0} -->

The variable, objective, and constraints are each constructed separately and combined in the final problem. In CVX, by contrast, these objects are created within the scope of a particular problem. Allowing variables and other objects to be created in isolation makes it easier to write high-level code that constructs problems (see §6).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Solvers", "weight": 1.0} -->

CVXPY converts problems into a standard form known as conic form, a generalization of a linear program. The conversion is done using graph implementations of convex functions. The resulting cone program is equivalent to the original problem, so by solving it we obtain a solution of the original problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Solvers", "weight": 1.0} -->

Solvers that handle conic form are known as cone solvers; each one can handle combinations of several types of cones. CVXPY interfaces with the open-source cone solvers CVXOPT, ECOS, and SCS, which are implemented in combinations of Python and C. These solvers have different characteristics, such as the types of cones they can handle and the type of algorithms employed. CVXOPT and ECOS are interior-point solvers, which reliably attain high accuracy for small and medium scale problems; SCS is a first-order solver, which uses OpenMP to target multiple cores and scales to large problems with modest accuracy.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Signed DCP", "weight": 1.0} -->

Like CVX, CVXPY uses disciplined convex programming (DCP) to verify problem convexity. In DCP, problems are constructed from a fixed library of functions with known curvature and monotonicity properties. Functions must be composed according to a simple set of rules such that the composition's curvature is known. For a visualization of the DCP rules, visit dcp.stanford.edu.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Signed DCP", "weight": 1.0} -->

CVXPY extends the DCP rules used in CVX by keeping track of the signs of expressions. The monotonicity of many functions depends on the sign of their argument, so keeping track of signs allows more compositions to be verified as convex. For example, the composition `square(square(x))` would not be verified as convex under standard DCP because the `square` function is nonmonotonic. But the composition is verified as convex under signed DCP because `square` is increasing for nonnegative arguments and `square(x)` is nonnegative.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Parameters", "weight": 1.0} -->

Another improvement in CVXPY is the introduction of parameters. Parameters are constants whose symbolic properties (e.g., dimensions and sign) are fixed but whose numeric value can change. A problem involving parameters can be solved repeatedly for different values of the parameters without redoing computations that do not depend on the parameter values. Parameters are an old idea in DSLs for optimization, appearing in AMPL.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Parameters", "weight": 1.0} -->

A common use case for parameters is computing a trade-off curve. The following code constructs a LASSO problem where the positive parameter $\gamma$ trades off the sum of squares error and the regularization term. The problem data are $A \in \text{R}^{m \times n}$ and $b \in \text{R}^{m}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Parameters", "weight": 1.0} -->

gamma = Parameter(sign="positive") # Must be positive due to DCP rules.
error = sum_squares(A*x - b)
prob = Problem(Minimize(error + gamma*regularization))

<!-- chunk {"id": "body-0017", "role": "body", "section": "Parameters", "weight": 1.0} -->

Computing a trade-off curve is trivially parallelizable, since each problem can be solved independently. CVXPY can be combined with Python multiprocessing (or any other parallelism library) to distribute the trade-off curve computation across many processes.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Parameters", "weight": 1.0} -->

## Assign a value to gamma and find the optimal x
def get_x(gamma_value):
gamma.value = gamma_value
result = prob.solve

<!-- chunk {"id": "body-0019", "role": "body", "section": "Parameters", "weight": 1.0} -->

## Get a range of gamma values with NumPy
gamma_vals = numpy.logspace(-4, 6)
## Do parallel computation with multiprocessing
pool = multiprocessing.Pool(processes = N)
x_values = pool.map(get_x, gamma_vals)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

CVXPY enables an object-oriented approach to constructing optimization problems. As an example, consider an optimal flow problem on a directed graph $G = {(V,E)}$ with vertex set $V$ and (directed) edge set $E$. Each edge $e \in E$ carries a flow $f_{e} \in \text{R}$, and each vertex $v \in V$ has an internal source that generates $s_{v} \in \text{R}$ flow. (Negative values correspond to flow in the opposite direction, or a sink at a vertex.) The (single commodity) flow problem is (with variables $f_{e}$ and $s_{v}$)

<!-- chunk {"id": "body-0021", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

where the $\phi_{e}$ and $\psi_{v}$ are convex cost functions and $I{(v)}$ and $O{(v)}$ give vertex $v$'s incoming and outgoing edges, respectively.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

To express the problem in CVXPY, we construct vertex and edge objects, which store local information such as optimization variables, constraints, and an associated objective term. These are exported as a CVXPY problem for each vertex and each edge.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

class Vertex(object):
def __init__(self, cost):
self.source = Variable
self.cost = cost(self.source)
self.edge_flows =

<!-- chunk {"id": "body-0024", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

def prob(self):
net_flow = sum(self.edge_flows) + self.source
return Problem(Minimize(self.cost), [net_flow == 0])

<!-- chunk {"id": "body-0025", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

class Edge(object):
def __init__(self, cost):
self.flow = Variable
self.cost = cost(self.flow)

<!-- chunk {"id": "body-0026", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

def connect(self, in_vertex, out_vertex):
in_vertex.edge_flows.append(-self.flow)
out_vertex.edge_flows.append(self.flow)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

def prob(self):
return Problem(Minimize(self.cost))

<!-- chunk {"id": "body-0028", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

The vertex and edge objects are composed into a graph using the edges' `connect` method. To construct the single commodity flow problem, we sum the vertices and edges' local problems. (Addition of problems is overloaded in CVXPY to add the objectives together and concatenate the constraints.)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Object-Oriented Convex Optimization", "weight": 1.0} -->

prob = sum([object.prob for object in vertices + edges])
prob.solve # Solve the single commodity flow problem.
