<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Disciplined Multi-Convex Programming

Topics include Low-rank models, Matrix factorization, Convex optimization, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A multi-convex optimization problem is one in which the variables can be partitioned into sets over which the problem is convex when the other variables are fixed. Multi-convex problems are generally solved approximately using variations on alternating or cyclic minimization. Multi-convex problems arise in many applications, such as nonnegative matrix factorization, generalized low rank models, and structured control synthesis, to name just a few. In most applications to date the multi-convexity is simple to verify by hand. In this paper we study the automatic detection and verification of multi-convexity using the ideas of disciplined convex programming. We describe an implementation of our proposed method that detects and verifies multi-convexity, and then invokes one of the general solution methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A multi-convex optimization problem is one in which the variables can be partitioned into sets over which the problem is convex when the other variables are fixed. Multi-convex problems appear in domains such as machine learning, signal and information processing, communication, and control. Typical problems in these fields include nonnegative matrix factorization (NMF) and bilinear matrix inequality (BMI) problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general multi-convex problems are hard to solve globally, but several algorithms have been proposed as heuristic or local methods, and are widely used in applications. Most of these methods are variations on the block coordinate descent (BCD) method. The idea of optimizing over a single block of variables while holding the remaining variables fixed in each iteration dates back to. Convergence results were first discussed for strongly convex differentiable objective function, and then under various assumptions on the separability and regularity of the objective function. In, a two-block BCD method with proximal operator is used to minimize a nonconvex objective function which satisfies the Kurdyka-Lojasiewicz inequality. In the authors propose an inexact BCD approach which updates variable blocks by minimizing a sequence of approximations of the objective function, which can either be nondifferentiable or nonconvex.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A recent work uses BCD to solve multi-convex problems, where the objective is a sum of a differentiable multi-convex function and several extended-valued convex functions. In each step, updates with and without proximal operator and prox-linear operator are considered, and convergence analysis is established under certain assumptions. Gradient methods have also been proposed for multi-convex problems, where the objective is differentiable in each block of variables, and all variables are updated at once along their descent directions and then projected into a convex feasible set in every iteration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus of this paper is not on solution methods, but on a modeling framework for expressing multi-convex problems in a way that verifies the multi-convex structure, and can expose the structure to whatever solution algorithm is then used. Modeling frameworks have been developed for convex problems, e.g., CVX, YALMIP, CVXPY, and Convex.jl [UMZ + 14]. These frameworks provide a uniform method for specifying convex problems based on the idea of disciplined convex programming (DCP). This gives a simple method for verifying that a problem is convex, and for automatically canonicalizing to a standard generic form such as a cone program. The goal of DCP (and these software frameworks) is not to detect or determine feasibility of an arbitrary problem, but rather to give a very simple set of rules that can be used to construct convex problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we extend the idea of DCP to multi-convex problems. We propose a disciplined multi-convex programming (DMCP) rule set, an extension of the DCP rule set. Problem specifications that conform to the DMCP rule set can be verified as convex in a group of variables, for any fixed values of the other variables, using ideas that extend those in DCP. We describe an efficient algorithm that can carry out the analysis of convexity of problem when an arbitrary group of variables is fixed at any value. As with DCP, the goal of DMCP is not to analyze multi-convexity of an arbitrary problem, but rather to give a simple set of rules which if followed yields multi-convex problems. In applications to date, such as NMF, verification of multi-convexity is simple, and can be done by hand or just simple observation. With DMCP a far larger class of multi-convex problems can be constructed in an organized way.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We describe a software implementation of the ideas developed in this paper, called DMCP, a Python package that extends CVXPY. It implements the DMCP verification and analysis methods, and then heuristically solves a conforming problem via BCD type algorithms, which we extend for general use to include slack variables to handle infeasibility. A similar package, MultiConvex, has been developed for the Julia package Convex.jl. We illustrate the framework on a number of examples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In § 2 we carefully define multi-convexity of a function, constraint, and problem. We review block coordinate descent methods, introducing new variants with slack variables and generalized inequalities, in § 3. In § 4 we describe the main ideas of DMCP and an efficient algorithm for verifying that a problem specification conforms to DMCP. In § 5 we describe our implementation of the package DMCP. Finally, in § 6 we describe a number of numerical examples. Our goal there is not to show competitive results, in terms of solution quality or solve time, but rather to show the simplicity with which the problem is specified, along with results that are at least comparable to those obtained with custom solvers for the specific problem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

Fixing variables in a function. Consider a function f: R n → R ∪{∞}, and a partition of the variable x ∈ R n into blocks of variables so ∑ N i =1 n i = n. Throughout this paper we will use subsets of indices to refer to sets of the variables. Let F ⊆ { 1,..., N } denote an index set, with complement F c = { 1,..., N } \ F. By fixing the variables with indices in F of the function f at a given point ˆ x ∈ R n, we obtain a function over the remaining variables, with indices in F c, which we denote as ˜ f = fix(f, ˆ x, F). For i ∈ F c, x i is a variable of the function ˜ f; for i ∈ F, x i = ˆ x i. Informally we refer to ˜ f as ' f, with the variables x i for i ∈ F fi xed'.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

As an example consider f: R 4 → R ∪ {∞} defined as With ˆ x = and F = { 1, 3 }, the fixed function ˜ f = fix(f, ˆ x, { 1, 3 }) is given by ˜ f (x 2, x 4) = | x 2 + x 4 |.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

Multi-convex and multi-affine functions. Given an index set F ⊆ { 1,..., N }, we say that a function f: R n → R ∪ {∞} is convex (or affine ) with set F fi xed, if for any ˆ x ∈ R n the function fix( f, ˆ x, F ) is a convex (or affine) function. (In this definition, we consider a so-called improper function, which has the value ∞ everywhere, as convex or affine.) For example, the function f defined in is convex with the variables x 1 and x 3 fixed ( i.e., with index set F = { 1, 3 } ). A function is convex if and only if it is convex with F = ∅ fi xed, i.e., with none of its variables fixed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

We say the function f is multi-convex (or multi-affine), if there are index sets F 1,..., F K, such that for every k the function f is convex (or affine) with F k fixed, and ∩ K k =1 F k = ∅. The requirement that ∩ K k =1 F k = ∅ means that for every variable x i there is some F k with i ̸∈ F k. In particular, ˜ f = fix( f, ˆ x, { 1,..., N } \ { i } ) is convex in x i. For K = 2, we say that the function is bi-convex (or bi-affine ).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

As an example, the function f in is convex with { 1, 3 } fi xed and { 2, 4 } fi xed, so it is multi-convex. The choice of K, and the index sets, is not unique. The function f is also convex with { 2, 3, 4 } fi xed, { 1, 3, 4 } fi xed, { 1, 2, 4 } fi xed, and { 1, 2, 3 } fi xed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Multi-convex function", "weight": 1.0} -->

Minimal fixed sets. For a function f, we can consider the set of all index sets F for which fix( f, ˆ x, F ) is convex for all ˆ x; among these we are interested in the minimal fixed sets that render a function convex. A minimal fixed set is a set of variables that when fixed make the function convex; but if any variable is removed from the set, the function is not convex. A function is multi-convex if and only if the intersection of these minimal fixed index sets is empty.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Multi-convex problem", "weight": 1.0} -->

We now extend the idea of multi-convexity to the optimization problem with variable x ∈ R n partitioned into blocks as x = (x 1,..., x N), and functions f i: R n → R ∪ {∞} for i = 0,..., m and g i: R n → R for i = 1,..., p are proper.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multi-convex problem", "weight": 1.0} -->

Given an index set F ⊆ { 1,..., N }, problem is convex with set F fi xed, if for any ˆ x ∈ R n the problem is convex. In other words, problem is convex with F fi xed, if and only if functions f i for i = 0,..., m are convex with F fi xed, and functions g i for i = 1,..., p are affine with F fixed.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multi-convex problem", "weight": 1.0} -->

We say the problem is multi-convex, if there are sets F 1,..., F K, such that for every k problem is convex with set F k fixed, and ∩ K k =1 F k = ∅. A convex problem is multi-convex with K = 0 ( i.e., F = ∅ ). A bi-convex problem is multi-convex with K = 2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multi-convex problem", "weight": 1.0} -->

As an example the following problem is multi-convex: with variable x ∈ R 4. This is readily verfied with F 1 = { 1, 3 } and F 2 = { 2, 4 }. For a given problem we can consider the minimal variable index sets which make the problem convex. If the problem is convex, F = ∅ is the unique minimal set.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Block coordinate descent and variations", "weight": 1.0} -->

In this section we review, and extend, some generic methods for approximately solving the multi-convex problem, using BCD-type methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Block coordinate minimization with slack variables", "weight": 1.0} -->

Assume that sets F k, k = 1,..., K are index sets for which the problem with F k fixed is convex, with ∩ K k =1 F k = ∅. These could be the set of all minimal index sets, but any other set of index sets that verify multi-convexity could be used.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Block coordinate minimization with slack variables", "weight": 1.0} -->

The basic form of the proposed method is iterative. In each iteration, we fix the variables in one set F k and solve the following subproblem, where s i for i = 1,..., m + p and x i for i ∈ F c k are the variables, and µ > 0 is a parameter. Here the constant ˆ x inherits the value of x from the least iteration. This subproblem solved in each iteration is convex. The slack variables s i for i = 1,..., m + p ensure that the subproblem cannot be infeasible. The added terms in the objective are a so-called exact penalty, meaning that when some technical conditions hold, and µ is large enough, the solution satisfies s i = 0, when the subproblem without the slack variables is feasible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Block coordinate minimization with slack variables", "weight": 1.0} -->

Many schemes can be used to choose k in each iteration, and to update the slack parameter µ. For example, we can cyclically choose k, or randomly choose k, or optimize over k = 1,..., K in rounds of K steps, in an order chosen by a random permutation in each round. Updating µ is typically done by increasing it by a factor ρ > 1 after each iteration, or after each round of K iterations. One variation on the algorithm sets the slack variables to zero ( i.e., removes them) once a feasible point is obtained ( i.e., a point is obtained with s i = 0). The algorithm is typically initialized with values specific to the particular application, or generic values.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Block coordinate minimization with slack variables", "weight": 1.0} -->

This algorithm differs from the basic BCD algorithm in the addition of the slack variables, and in the feature that a variable can appear in more than one set F c k, meaning that a variable can be updated in multiple iterations per round of K iterations. For example, if a problem has variables x 1, x 2, x 3 and is convex in ( x 1, x 2 ) and ( x 2, x 3 ), our method will update x 2 in each step.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Block coordinate minimization with slack variables", "weight": 1.0} -->

In the general case, very little can be said about the convergence of this method. One obvious observation is that, if µ is held fixed, the objective is nonincreasing and so convergences. See the references cited above for some convergence results for related algorithms, for special cases with strong assumptions such as strict convexity (when the variables are fixed) or differentiability. As a practical matter, similar algorithms have been found to be robust, and very useful in practice, despite a lack of strong theory establishing convergence in the general case.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Block coordinate proximal iteration", "weight": 1.0} -->

Avariation of subproblem is adds a proximal term, which renders the subproblems strongly convex: where x i for i ∈ F c k and s i for i = 1,..., m + p are variables, λ > 0 is the proximal parameter. The proximal term penalizes large changes in the variables being optimized, i.e., it introduces damping into the algorithm. In some cases it has been observed to yield better final points, i.e., points with smaller objective value, than those obtained without proximal regularization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Block coordinate proximal iteration", "weight": 1.0} -->

Yet another variation uses linearized proximal steps, when f is differentiable in the variables x i for i ∈ F c k. The subproblem solved in this case is where x i for i ∈ F c k and s i for i = 1,..., m + p are variables, and ∇ f (ˆ x i) is the partial gradient of f with respect to x i at the point ˆ x. The objective is equivalent to the minimization of which is the objective of a proximal gradient method.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Generalized inequality constraints", "weight": 1.0} -->

One useful extension is to generalize problem by allowing generalized inequality constraints. Suppose the functions f 0 and g i for i = 1,..., p are the same as in problem, but f i: R n → R d i ∪ {∞}. Consider the following program with generalized inequalities, where x = (x 1,..., x N) ∈ R n is the variable, and the generalized inequality constraints are with respect to proper cones K i ⊆ R d i, i = 1,..., m. The definitions of multi-convex program and minimal index set can be directly extended. Slack variables are added in the following way: where e i is a given positive element in cone K i for i = 1,..., m.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

Disciplined convex programming (DCP) is a methodology introduced by Grant et al. that imposes a set of conventions that must be followed when constructing (or specifying or defining) convex programs. Conforming problems are called disciplined convex programs. A disciplined convex program can be transformed into an equivalent cone program by replacing each function with its graph implementation. The convex optimization modeling systems YALMIP, CVX, CVXPY, and Convex.jl [UMZ + 14] use DCP to verify the convexity of a problem and automatically convert convex programs into cone programs, which can then be solved using generic solvers.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

The conventions of DCP restrict the set of functions that can appear in a problem and the way functions can be composed. Every function in a disciplined convex program must be formed as an expression involving constants or parameters, variables, and a dictionary of atomic functions. The dictionary consists of functions with known curvature and monotonicity, and a graph implementation, or representation as partial optimization over a cone program. Every composition of functions f ( g 1 ( x ),..., g p ( x )), where f: R p → R is convex and g 1,..., g p: R n → R, must satisfy the following composition rule, which ensures the composition is convex. Let ˜ f: R p → R ∪{∞} be the extended-value extension of f [, Chap. 3]. One of the following conditions must hold for each i = 1,...,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

- g i is convex and ˜ f is nondecreasing in argument i. - g i is concave and ˜ f is nonincreasing in argument i.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

The composition rule for concave functions is analogous.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

Signed DCP is an extension of DCP that keeps track of the signs of functions and expressions, using simple sign arithmetic. The monotonicity of functions in the atom library can then depend on the sign of their arguments. As a simple example, consider the expression y = (exp x ) 2, where x is a variable. The subexpression exp x is convex and (in signed DCP analysis) nonnegative. With DCP analysis, y cannot be verified as convex, since the square function is not nondecreasing. With signed DCP analysis, the square function is known to be nondecreasing for nonnegative arguments, which matches this case, so y is verified as convex using signed DCP analysis.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

Convexity verification of an expression formed from variables and constants (or parameters) in (signed) DCP first analyzes the signs of all subexpressions. Then it checks that the composition rule above holds for every subexpression, possibly relying on the known signs of subexpressions. If everything checks out the expression is verified to be constant, affine, convex, concave, or unknown (when the DCP rules do not hold). We make an observation that is critical for our work here: The DCP analysis does not use the values of any constants or parameters in the expression. The number 4.57 is simply treated as positive; if a parameter has been declared as positive, then it is treated as positive. It follows immediately that DCP analysis has verified not just that the specific expression is convex, but that it is convex for any other values of the constants and parameters, with the same signs as the given ones, if the sign matters.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

The following code snippet gives an example in CVXPY: x = Variable(n) mu = Parameter(sign = 'positive') expr = sum_squares(x) + mu*norm(x,1) In the first line we declare (or construct) a variable, and in the second line construct a paramater, i.e., a constant that is unknown, but positive. The curvature of the expression expr is verified to be convex, even though the value of parameter mu is unknown; DCP analysis uses only the fact that whatever the value of mu is, it must be positive.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

To determine that problem is multi-convex requires us to verify that functions fix( f i, ˆ x, F ) are convex, and if fix( g i, ˆ x, F ) are affine, for all ˆ x ∈ R n. We can use the idea of DCP, specifically with signed parameters, to carry this out, which gives us a practical method for multi-convexity verification.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

Multi-convex atoms. We start by generalizing the library of DCP atom functions to include multi-convex atomic functions. A function is a multi-convex atom if it has N arguments N > 1, and it reduces to a DCP atomic function, when and only when all but the i th arguments are constant for each i = 1,..., N. For example, the product of N variables is a multi-convex atom that extends the DCP atom of multiplication between one variable and constants.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

Given a description of problem under a library of DCP and multi-convex atomic functions, we say that it is disciplined convex programming with set F ⊆ { 1,..., N } fi xed, if the corresponding problem for any ˆ x ∈ R n conforms to the DCP rules with respect to the DCP atomic function set. When there is no confusion, we simply say that problem is DCP with F fi xed.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

To verify if a problem is DCP with F fi xed, a method first fixes the problem by replacing variables in F with parameters of the same signs and dimensions. Then it verifies DCP of the fixed problem with parameters according to the DCP ruleset. The parameter is the correct model for fixed variables, in that the DCP rules ensure that the verified curvature holds for any value of the parameter.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

Disciplined multi-convex program. Given a description of problem under a library of DCP and multi-convex atomic functions, it is disciplined multi-convex programming (DMCP), if there are sets F 1,..., F K such that problem with every F k fixed is DCP, ∩ K k =1 F k = ∅. We simply say that problem is DMCP if there is no confusion. A problem that is DMCP is guaranteed to be multi-convex, just as a problem that is DCP is guaranteed to be convex. Morever, when a BCD method is applied to a DMCP problem, each iteration involves the solution of a DCP problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

DMCP verification. A direct way of DMCP verification is to check if the problem is DCP with { i } c fixed for every i = 1,..., N. Expressions in DMCP inherit the tree structure from DCP, so such verification can be done in O ( MN ) time, where M is number of nodes in problem expression trees, and N is the number of distinct variables. To see why DMCP can be verified in this simple way, we have the following claim. The claim implies that every DMCP problem is DCP when all but one variable is fixed.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

Claim 4.1 For a problem consisting only of DCP atoms (or multi-convex atoms with all but one arguments constant), it is DCP with F fi xed, if and only if it is DCP with { i } c fixed for all i ∈ F c.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

To see why Claim 4.1 is correct, we first prove the direction that if a problem consisting only of DCP atoms is DCP with { i } c fixed for all i ∈ F c, then it is DCP with F fi xed. The proof begins with two observations for functions consisting only of DCP atoms.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

- The DCP curvature types have a hierarchy: Unknown is the base type, then it splits into convex and concave. Affine is a subtype of both convex and concave. Then constant is a subtype of everything. There is a similar hierarchy for sign information. The DCP type system is monotone in the curvature and sign hierarchies, meaning if the curvature or sign of an argument of a function is changed to be more specific, the type of the function will become more specific or stay the same. Fixing variables of a function makes the curvatures of some arguments more specific, while keeps all signs the same, so the curvature of the function can only get more specific or stay the same.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

- If a function is affine in x and y separately, then it is affine in ( x, y ). This is true because no multiplication of variables is allowed in DCP, and the function can only be in the form of Ax + By + c.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

Now suppose that a problem consisting of DCP atoms with only two variables x and y is not DCP, but it is DCP with x fi xed and with y fi xed. Then there must be some function that has a wrong curvature type in ( x, y ) but whose arguments all have known curvatures. Since the function has the right curvature type with x fi xed and y fi xed, there must be an argument that is convex or concave (not affine) in ( x, y ), but has a different curvature in x and y. According to the first observation, the argument must be affine in x and y. By the second observation, the argument is affine in ( x, y ), which is a contradiction. For the same reason, cases with more than two variables have the same conclusion.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Disciplined multi-convex programming", "weight": 1.0} -->

For the other direction of Claim 4.1, we again use the observation that if a problem is DCP with F fi xed, then fixing additional variables only makes function curvatures more specific. The problem must then be DCP with { i } c fixed for all i ∈ F c, since F ⊆ { i } c.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Efficient search for minimal sets", "weight": 1.0} -->

A problem may have multiple collections of index sets for which it is DMCP. We propose several generic and efficient ways of choosing which collection to use when applying a BCD method to the problem. The simplest option is to always choose the collection { 1 } c,..., { N } c, in which case BCD optimizes over one variable at a time.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Efficient search for minimal sets", "weight": 1.0} -->

A more sophisticated approach is to reduce the collection { 1 } c,..., { N } c to minimal sets, which allows BCD to optimize over multiple variables each iteration. We find minimal sets by first determining which variables can be optimized together. Concretely, we construct a conflict graph ( V, E ), where V is the set of all variables, and i ∼ j ∈ E if and only if variables i and j appear in two different child trees of a multi-convex atom in the problem expression tree, which means the variables cannot be optimized together.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Efficient search for minimal sets", "weight": 1.0} -->

Constructing the conflict graph takes O ( N 2 M ) time. We simply do a depth-first traversal of the problem expression tree. At each leaf node, we initialize a linked list with the leaf variable. At each parent node, we join the linked lists of its children. At each multi-convex atom node, we also remove duplicates from each child's linked list and then iterate over the lists, adding an edge for every two variables appearing in different lists. The edges added at a given multi-convex node are all unique because a duplicate edge would mean the same variable appeared in two different child trees, which is not possible in a DMCP problem. Hence, iterating over the lists of variables takes at most N 2 operations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Efficient search for minimal sets", "weight": 1.0} -->

Given the conflict graph, for i = 1,..., N we find a maximal independent set F i containing i using a standard fast algorithm and replace { i } c with F c i. The final collection is all index sets F c i that are not supersets of another index set F c j. More generally, we can choose any collection of index sets F 1,..., F K such that F c 1,..., F c K are independent sets in the conflict graph.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Implementation", "weight": 1.0} -->

The methods of DMCP verification, searching for minimal sets to fix, and cyclic optimization with minimal sets fixed are implemented as an extension of CVXPY in a package DMCP that can be accessed. A Julia package with similar functionality, MultiConvex.jl, can be found, but we focus here on the Python package DMCP.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Some useful functions", "weight": 1.0} -->

Multi-convex atomic functions. In order to allow multi-convex functions, we extend the atomic function set of CVXPY. The following atoms are allowed to have non-constant expressions in both arguments, while in base CVXPY one of the arguments must be constant.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Some useful functions", "weight": 1.0} -->

- multiplication: expression1 * expression2 - elementwise multiplication: mul\_elemwise(expression1, expression2) - convolution: conv(expression1, expression2) Find minimal sets. Given a problem, the function find\_minimal\_sets(problem) runs the algorithm discussed in § 4.3 and returns a list of minimal sets of indices of variables. The indices are with respect to the list problem.variables, namely, the variable corresponding to index 0 is problem.variables.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Some useful functions", "weight": 1.0} -->

DMCP verification. Given a problem, the function returns a boolean indicating if it is a DMCP problem.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Some useful functions", "weight": 1.0} -->

Fix variables. The function fix(expression, fix\_vars) returns a new expression with the variables in the list fix\_vars replaced with parameters of the same signs and values. If expression is replaced with a CVXPY problem, then a fixed problem is returned by fixing every expression in its cost function and both sides of inequalities or equalities in constraints.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Some useful functions", "weight": 1.0} -->

Random initialization. It is suggested that users provide an initial point x 0 for the method such that functions fix( f i, x 0, F 1 ) are proper for i = 0,..., m, where F 1 is the first minimal set given by find\_minimal\_sets. If not, the function rand\_initial(problem) will be called to generate random values from the uniform distribution over the interval [0, 1) (( -1, 0]) for variables with non-negative (non-positive) sign, and from the standard normal distribution for variables with no sign. There is no guarantee that such a simple random initialization can always work for any problem.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Options on update and algorithm parameters", "weight": 1.0} -->

The solving method is to cyclically fix every minimal set found by find\_minimal\_sets and update the variables. Three ways of updating variables are implemented. The default one can be called by problem.solve(method = 'bcd', update = 'proximal'), which is to solve the subproblem with proximal operators, i.e., problem. To update by minimizing the subproblem without proximal operators, i.e., problem, the solve method is called with update = 'minimize'. To use the prox-linear operator in updates, i.e., problem, the solve method should be called with update = 'prox\_linear'.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Options on update and algorithm parameters", "weight": 1.0} -->

The parameter µ is update in every cycle by µ t +1 = min( ρµ t, µ max ). The algorithm parameters are ρ, µ 0, µ max, λ, and the maximum number of iterations. They can be set by passing values of the parameters rho, mu\_0, mu\_max, lambd, and max\_iter, respectively, to the solve method.

<!-- chunk {"id": "body-0060", "role": "body", "section": "One basic example", "weight": 1.0} -->

Problem description. The first example is problem, which has appeared throughout this paper to explain definitions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "One basic example", "weight": 1.0} -->

DMCP specification. The code written in DMCP for this example is as follows.

<!-- chunk {"id": "body-0062", "role": "body", "section": "One basic example", "weight": 1.0} -->

To find all minimal sets, the following line is typed in and the output is. Note that index i corresponds to variable prob.variables[i] for i = 0,..., 3. To verify if it is DMCP, the function Numerical result. Random initial values are set for all variables. The solve method with default setting finds a feasible point with objective value 0, which solves the problem globally.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Fractional optimization", "weight": 1.0} -->

Problem description. In this example we evaluate DMCP on some fractional optimization problems. Consider the following problem where x ∈ R n is the variable, X is a convex set, p is a convex function, and q is concave. The objective function is set to + ∞ unless p (x) ≥ 0, q (x) > 0. Such a problem is quasi-convex, and can be globally solved [, § 4.2.5], or even have analytical solutions, so the aim here is just to evaluate the effectiveness of the method.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Fractional optimization", "weight": 1.0} -->

There are several ways of specifying problem as DMCP. One way is via the following problem. where x and y are variables. Another way is via the following. where α ∈ R + and x are variables. Both of them are biconvex.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Fractional optimization", "weight": 1.0} -->

DMCP specification. Suppose that X = R n. The code for the formulation in is as the following. x = Variable(n) y = Variable(n) # specify p and q here prob = Problem(Minimize(inv_pos(q)*p), [x == y]) Expressions p and q are to be specified. The code for problem is as follows. alpha = Variable(1, sign = 'Positive') x = Variable(n) # specify p and q here prob = Problem(Minimize(alpha), [p <= q*alpha]) Numerical result. Take an example of p (x) = x 2 +1 and q (y) = √ y +0. 5. The code for specifying p and q is as the follows.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Fractional optimization", "weight": 1.0} -->

The global optimal value of the objective function is approximately 1. 217. With random initial points, DMCP finds the global optimum for problem and.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Linear transceiver design", "weight": 1.0} -->

Problem description. Suppose that a signal x ∈ R n passes through a linear pre-coder A ∈ R n × n, and is transmitted as Ax. Denote the channel matrix as C ∈ R m × n and the additive noise as e ∈ R m, then the received signal is y = CAx + e. The received signal passing through an equalizer B ∈ R n × m is decoded as By. The problem of determining A and B is called transceiver deign.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Linear transceiver design", "weight": 1.0} -->

In this example, we assume that the signal x is binary and follows IID Bernoulli distribution, and the noise e ∼ N (0, σ 2 e I). Given the channel matrix C, the aim is to design A Figure 1: Linear transceiver design. and B such that the mean squared error E ‖ x -By ‖ 2 2, where the mean is taken over x and e, is minimized, and the transmission power is constrained.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Linear transceiver design", "weight": 1.0} -->

An optimization problem is formulated as the following where B and A are the variables. The problem is biconvex.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Linear transceiver design", "weight": 1.0} -->

DMCP specification. The code can be written as the following.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Linear transceiver design", "weight": 1.0} -->

A = Variable(n,n) B = Variable(n,m) sigma_e = Parameter cost = square(norm(B*C*A-I,'fro'))/2+square(sigma_e)*square(norm(B,'fro')) prob = Problem(Minmize(cost), [norm(A, 'fro') <= p]) prob.solve(method = 'bcd') Numerical result. In an experiment, n = 10, m = 15, p = 10, and the channel matrix C is a random matrix with IID normal distribution. The signal to noise ratio varies, and for each value of σ e, we try to solve the problem to get a design of A and B. Each design is tested by 1000 trials with random signal x and noise e generated from the same distributions as the ones in the design. The method is run without proximal operator and with initial point generated from the SVD of the channel matrix C. The mean squared error and the averaged bit error rate are in Figure 1.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Sparse dictionary learning", "weight": 1.0} -->

Problem description. The aim is to find a dictionary D ∈ R m × n under which the data matrix X ∈ R m × T can be approximated by sparse coefficients, i.e., X ≈ DY where Y ∈ R n × T is a sparse matrix.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Sparse dictionary learning", "weight": 1.0} -->

The optimization problem can be formulated as where the variables are Y and D, and α > 0 is a parameter. The problem is biconvex.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Sparse dictionary learning", "weight": 1.0} -->

DMCP specification. The code can be written as follows.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Sparse dictionary learning", "weight": 1.0} -->

D = Variable(m,n) Y = Variable(n,T) alpha = Parameter(sign = 'Positive') cost = square(norm(D*Y-X,'fro'))/2+alpha*norm(Y,1) prob = Problem(Minimize(cost), [norm(D,'fro') <= 1]) prob.solve(method = 'bcd') Numerical result. In an experiment, X is a random normal matrix with m = 10, n = 20, and T = 20. The parameter α is swept from 10 -5 to 1. For each value of α, the method is called with random initialization, and the relative approximation error and the cardinality of Y are shown as a blue dot in Figure 2.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Sparse feedback matrix design", "weight": 1.0} -->

Problem description. To design a sparse linear constant output feedback control u = Ky for the system which results in a decay rate r no less than a given threshold θ > 0 in the closed-loop system, we consider the following optimization problem where K, P, and r are variables, and A, B, C, and θ are given. The notation P ⪰ I means that P -I is semidefinite. The problem is biconvex with minimal sets of variables to fix { P } and { K,r }.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Sparse feedback matrix design", "weight": 1.0} -->

DMCP specification. The code can be the following.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Sparse feedback matrix design", "weight": 1.0} -->

P = Variable(n,n) K = Variable(m1,m2) r = Variable cost = norm(K,1) constr = [np.eye(n) << P, r >= theta] constr += [(A+B*K*C).T*P+P*(A+B*K*C) << -P*r*2] prob = Problem(Minimize(cost), constr) prob.solve(method = 'bcd') Numerical result. An example with n = m 1 = 5, m 2 = 4, θ = 0. 01, and the following data matrices is tested.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Sparse feedback matrix design", "weight": 1.0} -->

The initial value P 0 is an identity matrix, r 0 = 1, and K 0 is an matrix with all zeros. The result is that r = 0. 01 and which is sparse. The three nonzero entries are in the second column, so only the second output needs to be fed back. In the work with decay rate no less than 0. 35 another sparse feedback matrix is found with the same cardinality 3.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Bilinear control", "weight": 1.0} -->

Problem description. A discrete time m -input bilinear control system is of the following form where u t = [u 1 t,..., u m t] ∈ Ω ⊆ R m is the input, and x t ∈ R d is the system state at time t. In an optimal control problem with fixed initial state, given system matrices A, B i ∈ R n × n and convex objective functions f and g, an optimization problem can be formulated as where x t and u t are variables, and Ω is a given convex set describing bounds on u t and x t. The problem is multi-convex.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Bilinear control", "weight": 1.0} -->

As a special case, a standard model of D.C.-motor is a bilinear system of the following form where the derivative is with respect to time, and The correspondence between model and physical variables is that, x 1 is the armature current, x 2 is the speed of rotation, u is the field current, and v is the armature voltage. For nominal operation, A control problem is the braking with short-circuited armature (v t = 0). The field current u is controlled such that the rotation speed decreases to zero as fast as possible, and that the armature current is not excessively large. By discretizing over time and taking 10 samples per second, the problem can be formulated in the following form where u ∈ R n -1 and x t = [x 1 t, x 2 t] ∈ R 2 for t = 1,..., n are variables, and the notation x i = [x i 1,..., x i n], i = 1, 2. The problem is biconvex if we consider x = [x 1,..., x n] ∈ R 2 × n as one variable.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Bilinear control", "weight": 1.0} -->

DMCP specification. The code is as the following. x = Variable(2,n) u = Variable(n-1) constr = [x == 1, max_entries(abs(x)) <= M] for t in range(n-1): constr += [x[:,t+1]-x[:,t] == 0.1*(A0*x[:,t]+A1*x[:,t]*u[t])] prob = Problem(Minimize(norm(x)), constr) prob.solve(method = 'bcd') Numerical result. We take an example with n = 100 and M = 8. The initial value of x is zero and of u is a vector linearly decreasing from 0. 5 to 0. The result is shown in Fig. 3, where the braking is faster than that in a linear control system shown.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Resistance estimation", "weight": 1.0} -->

Problem description. A problem in direct current (DC) circuit is to estimate the values of resistors such that certain constraints on currents and voltages can be satisfied. The topology of the circuit is given, and several observations on currents and voltages are known. A general problem of estimating the resistance to fit the topology and the observations can be written as the following where u ∈ R n, i ∈ R m, and r ∈ R d + are variables representing voltages, currents, and resistance, respectively. The convex functions f and g penalize deviations from the observations. The first constraint corresponds to the Ohm's law, where the mapping A is linear and depends on the topology of the circuit. The sets U, I, and R are convex, and they may describe the Kirchhoff's circuit laws. The problem is multi-convex due to the first constraint. A simple example is shown in the following circuit diagram.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Resistance estimation", "weight": 1.0} -->

The known quantities are the current source I 0 and the voltage level u 0. It is observed that v k -v k +1 ≈ δ for k = 1,..., n -1, so the optimization problem is where x, y, i, j ∈ R n, z ∈ R n -1 are variables for currents, a, b ∈ R n +, c ∈ R n -1 + are the variables for resistance, and v ∈ R n is the variable for voltages. The problem is multiconvex, and the minimal sets to fix are not obvious.

<!-- chunk {"id": "body-0085", "role": "body", "section": "DMCP specification. The code can be as the following", "weight": 1.0} -->

x = Variable(n) y = Variable(n) z = Variable(n-1) i = Variable(n) j = Variable(n) a = Variable(n, sign = 'Positive') b = Variable(n, sign = 'Positive') c = Variable(n-1, sign = 'Positive') v = Variable(n) constr = [x == y+z, x[n-1]+z[n-2] == y[n-1]] constr += [i == x, j == y, i[n-1] == -I0, j[n-1] == -I0] cost = 0 for k in range(n-2): constr += [x[k+1]+z[k] == y[k+1]+z[k+1]] for k in range(n): constr += [x[k]*a[k] == u0 - v[k], y[k]*b[k] == v[k]] for k in

<!-- chunk {"id": "body-0086", "role": "body", "section": "DMCP specification. The code can be as the following", "weight": 1.0} -->

range(n-1): cost += square(v[k]-v[k+1]-delta) constr += [z[k]*c[k] == v[k]-v[k+1]] constr += [i[k+1]== i[k]+x[k+1], j[k+1] == j[k]+y[k+1]] prob = Problem(Minimize(cost), constr) prob.solve(method = 'bcd') The find\_minimal\_sets function returns where indices 1, 3, 5, 6, 7, 8 correspond to variables z, a, c, b, y, x respectively.

<!-- chunk {"id": "body-0087", "role": "body", "section": "DMCP specification. The code can be as the following", "weight": 1.0} -->

Numerical result. We set n = 10, I 0 = -100, δ = 1, u 0 = 12, and all variables are set with initial value 1. The method finds a feasible point with objective value 0 which solves the problem globally, and the solution is shown in the following table.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Steady state of Markov chain", "weight": 1.0} -->

Problem description. Suppose that P 1,..., P n ∈ R m × m are n transition matrices of Markov chains, then it is known that any convex combination P = ∑ n i =1 θ i P i for θ i ≥ 0 and ∑ n i =1 θ i = 1 is also a transition matrix of a Markov chain. Given P i for i = 1,..., n and a convex function f: R m → R, the problem is to find such a convex combination, so that the Markov chain with respect to P has a steady state vector x ∈ R m that achieves the minimum of f.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Steady state of Markov chain", "weight": 1.0} -->

The problem can be formulated as where x, P, and θ are variables. The problem is biconvex.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Steady state of Markov chain", "weight": 1.0} -->

As an example, f ( x ) = ‖ x -x 0 ‖ 2, so the goal is to generate a transition matrix so that the steady state vector is close to a given distribution x 0.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Steady state of Markov chain", "weight": 1.0} -->

DMCP specification. The code is as follows. cost = norm(x-x0) constr = [theta >= 0, sum_entries(theta) == 1, x >= 0, sum_entries(x) == 1] right = 0 for i in range(n): right += theta[i]*P0[i] constr += [P == right, P.T*x == x] prob = Problem(Minimize(cost), constr) prob.solve(method = 'bcd') Numerical result. An example with n = 4, m = 3, randomly generated P i, and is tested. The initial values are random. The result gives which achieves the targeted steady state vector.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Blind deconvolution", "weight": 1.0} -->

Problem description. Blind deconvolution is an inverse problem commonly encountered in many practical applications such as image restoration, system identification, and channel estimation. The problem is to find two vectors with some priors, such that their convolution approximates the given data.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Blind deconvolution", "weight": 1.0} -->

Suppose that the data d ∈ R m + n -1 is the convolution of an unknown sparse vector x 0 ∈ R n and an unknown vector y 0 ∈ R m. A problem can be formulated as the following where x ∈ R n and y ∈ R m are variables, and α > 0 is a parameter. The problem is biconvex. For any x ∗ y = d and a positive scalar k the convolution of kx and y/k is also d, so the constraint ‖ y ‖ ∞ ≤ M is needed to exclude a trivial solution x ≈ 0.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Blind deconvolution", "weight": 1.0} -->

DMCP specification. The code can be written as the following. y = Variable(m) x = Variable(n) cost = norm(conv(y,x)-d,2) + alpha*norm(x,1) prob = Problem(Minimize(cost), [norm(y,'inf') <= M]) prob.solve(method = 'bcd') Numerical result. In an example, m = 100, n = 40, M = 10, α = 0. 28, and the initial value of every variable is a vector of all ones. The result is in Figure 4.
