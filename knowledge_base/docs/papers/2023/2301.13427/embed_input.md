<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Disciplined Saddle Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider convex-concave saddle point problems, and more generally convex optimization problems we refer to as saddle problems, which include the partial supremum or infimum of convex-concave saddle functions. Saddle problems arise in a wide range of applications, including game theory, machine learning, and finance. It is well known that a saddle problem can be reduced to a single convex optimization problem by dualizing either the convex (min) or concave (max) objectives, reducing a min-max problem into a min-min (or max-max) problem. Carrying out this conversion by hand can be tedious and error prone. In this paper we introduce disciplined saddle programming (DSP), a domain specific language (DSL) for specifying saddle problems, for which the dualizing trick can be automated. The language and methods are based on recent work by Juditsky and Nemirovski arXiv:2102.01002 [math.OC], who developed the idea of conic-representable saddle point programs, and showed how to carry out the required dualization automatically using conic duality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Juditsky and Nemirovski's conic representation of saddle problems extends Nesterov and Nemirovski's earlier development of conic representable convex problems; DSP can be thought of as extending disciplined convex programming (DCP) to saddle problems. Just as DCP makes it easy for users to formulate and solve complex convex problems, DSP allows users to easily formulate and solve saddle problems. Our method is implemented in an open-source package, also called DSP.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider saddle problems, by which we mean convex-concave saddle point problems or, more generally, convex optimization problems that include the partial supremum or infimum of convex-concave saddle functions. Saddle problems arise in various fields such as game theory, robust and minimax optimization, machine learning, and finance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While there are algorithms specifically designed to solve some types of saddle point or minimax problems, another approach is to convert them into standard convex optimization problems using a trick based on duality that can be traced back to at least the 1920s. The idea is to express the infima or suprema that appear in the saddle problem via their duals, which converts them to suprema or infima, respectively. Roughly speaking, this turns a min-max problem into a min-min (or max-max) problem, which can then be solved by standard methods. Specific cases of this trick are well known; the classical example is converting a matrix game, a specific saddle point problem, into a linear program (LP). While the dualizing trick has been known and used for almost 100 years, it has always been done by hand, for specific problems. It can only be carried out by those who have a working knowledge of duality in convex optimization, and are aware of the trick.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose an automated method for carrying out the dualizing trick. Our method is based on the theory of conic representation of saddle point problems, developed recently by Juditsky and Nemirovski. Based on this development, we have designed a domain specific language (DSL) for describing saddle problems, which we refer to as disciplined saddle programming (DSP). When a problem description complies with the syntax rules, i.e., is DSP-compliant, it is easy to verify that it is a valid saddle problem, and more importantly, automatically carry out the dualizing trick. We have implemented the DSL in an open source software package, also called DSP, which works with CVXPY, a DSL for specifying and solving convex optimization problems. DSP makes it easy to specify and solve saddle problems, without any expertise in (or even knowledge of) convex duality. Even for those with the required expertise to carry out the dualizing trick by hand, DSP is less tedious and error prone.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

DSP is *disciplined*, meaning it is based on a small number of syntax rules that, if followed, guarantee that the specified problem is a valid saddle problem. It is analogous to disciplined convex programming (DCP), which is a DSL for specifying convex optimization problems. When a problem specification follows these syntax rules, i.e., is DCP-compliant, it is a valid convex optimization problem, and more importantly can be automatically converted to an equivalent cone program, and then solved. As a practical matter, DCP allows a large number of users to specify and solve even complex convex optimization problems, with no knowledge of the reduction to cone form. Indeed, most DCP users are blissfully unaware of how their problems are solved, i.e., a reduction to cone form. DCP was based on the theory of conic representations of convex functions and problems, pioneered by Nesterov and Nemirovski. Widely used implementations of DCP include CVXPY, Convex.jl \[Ude+14\], CVXR, YALMIP, and CVX.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Like DCP did for convex problems, DSP makes it easy to specify and solve saddle problems, with most users unaware of the dualization trick and reduction used to solve their problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

Studying saddle problems is a long-standing area of research, resulting in many theoretical insights, numerous algorithms for specific classes of problems, and a large number of applications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

Saddle problems are often studied in the context of minimax or maximin optimization, which, while dating back to the 1920s and the work of von Neumann and Morgenstern on game theory, continue to be active areas of research, with many recent advancements for example in machine learning \[Goo+14\]. A variety of methods have been developed for solving saddle point problems, including interior point methods, first-order methods, and second-order methods, where many of these methods are specialized to specific classes of saddle problems. Depending on the class of saddle problem, the methods differ in convergence rate. For example, for the subset of smooth minimax problems, an overview of rates for different curvature assumptions is given in \[The+19\]. Due to their close relation to Lagrange duality, saddle problems are commonly studied in the context of convex analysis (see, for example, \[, §5.4\], \[, §33--37\], \[, §11.J\], \[, §4.3\]), with an analysis via monotone operators given.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

The practical usefulness of saddle programming in many applications is also increasingly well known. Many applications of saddle programming are robust optimization problems. For example, in statistics, distributionally robust models can be used when the true distribution of the data generating process is not known. Another common area of application is in finance, with \[, §19.3--4\] describing a range of financial applications that can be characterized as saddle problems. Similarly, \[Boy+17 \] describe variations of the classical portfolio optimization problem as saddle problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

DCP is a grammar for constructing optimization problems that are provably convex, meaning that they can be solved globally, efficiently and accurately. It is based on the rule that the convexity of a function $f$ is preserved under composition if all inner expressions in arguments where $f$ is nondecreasing are convex, and all expressions where $f$ is nonincreasing are concave, and all other expressions are affine. A detailed description of the composition rule is given in \[, §3.2.4\]. Using this rule, functions can be composed from a small set of primitives, called atoms, where each atom has known curvature, sign, and monotonicity. Every function that can be constructed from these atoms according to the composition rule is convex, but the converse is not true. The DCP framework has been implemented in many programming languages, including MATLAB, Python, R, and Julia \[Ude+14\], and is used by researchers and practitioners in a wide range of fields.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Well-structured convex-concave saddle point problems", "weight": 1.0} -->

As mentioned earlier, disciplined saddle programming is based on Juditsky and Nemirovski's recent work on well-structured convex-concave saddle point problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We introduce disciplined saddle programming, a domain specific language for specifying and solving convex-concave saddle problems. To solve the saddle problems, automated dualization is applied to the conic representation of the problem. We extend the existing literature by deriving a procedure that returns both the convex and concave coordinates of the saddle point. This also guarantees that a valid saddle point was found without the need to check for technical conditions (such as compactness). These developments make the theory of conic representable saddle problems practically applicable for the first time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We specify and implement the first DSL that encodes sufficient conditions for conic representability of saddle problems. We develop an open-source Python package, also called DSP, providing a user-friendly interface for specifying and solving saddle problems. Using this implementation, we demonstrate the effectiveness of the framework by solving a variety of saddle problems from different application domains.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

In §2 we describe saddle programming, which includes the classical saddle point problem, as well as convex problems that include functions described via partial minimization or maximization of a saddle function. We describe some typical applications of saddle programming in §3. In §4 we describe disciplined saddle programming, which is a way to specify saddle programs in such a way that validity is easy to verify, and the reduction to an equivalent cone program can be automated. We describe our implementation in §5, showing how saddle functions, saddle extremum functions, saddle point problems, and saddle problems are specified. We present numerical examples in §6.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Saddle functions", "weight": 1.0} -->

A *saddle function* (also referred to as a convex-concave saddle function) $f:{{\mathcal{X} \times \mathcal{Y}}\rightarrow\text{𝐑}}$ is one for which $f{( \cdot,y)}$ is convex for any fixed $y \in \mathcal{Y}$, and $f{(x, \cdot )}$ is concave for any fixed $x \in \mathcal{X}$. The argument domains $\mathcal{X} \subseteq \text{𝐑}^{n}$ and $\mathcal{Y} \subseteq \text{𝐑}^{m}$ must be nonempty closed convex. We refer to $x$ as the convex variable, and $y$ as the concave variable, of the saddle function $f$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Examples", "weight": 1.0} -->

*Functions of $x$ or $y$ alone.* A convex function of $x$, or a concave function of $y$, are trivial examples of saddle functions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Examples", "weight": 1.0} -->

*Lagrangian of a convex optimization problem.* The convex optimization problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "Examples", "weight": 1.0} -->

for $\lambda \geq 0$ (elementwise). It is convex in $x$ and affine (and therefore also concave) in $y = {(\nu,\lambda)}$, so it is a saddle function with

<!-- chunk {"id": "body-0021", "role": "body", "section": "Examples", "weight": 1.0} -->

*Bi-affine function.* The function ${f{(x,y)}} = {{({{Ax} + b})}^{T}{({{Cy} + d})}}$, with $\mathcal{X} = \text{𝐑}^{p}$ and $\mathcal{Y} = \text{𝐑}^{q}$, is evidently a saddle function. The inner product $x^{T}y$ is a special case of a bi-affine function. For a bi-affine function, either variable can serve as the convex variable, with the other serving as the concave variable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Examples", "weight": 1.0} -->

*Convex-concave inner product.* The function ${f{(x,y)}} = {F{(x)}^{T}G{(y)}}$, where $F:{\text{𝐑}^{p}\rightarrow\text{𝐑}^{n}}$ is a nonnegative elementwise convex function and $G:{\text{𝐑}^{q}\rightarrow\text{𝐑}^{n}}$ is a nonnegative elementwise concave function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Examples", "weight": 1.0} -->

*Weighted $\ell_{2}$ norm.* The function

<!-- chunk {"id": "body-0024", "role": "body", "section": "Examples", "weight": 1.0} -->

*Quadratic form with quasi-semidefinite matrix.* The function

<!-- chunk {"id": "body-0025", "role": "body", "section": "Examples", "weight": 1.0} -->

where the matrix is quasi-semidefinite, i.e., $P \in \text{𝐒}_{+}^{n}$ (the set of symmetric positive semidefinite matrices) and ${- Q} \in \text{𝐒}_{+}^{n}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Examples", "weight": 1.0} -->

*Quadratic form.* The function ${f{(x,Y)}} = {x^{T}Yx}$, with $\mathcal{X} = \text{𝐑}^{n}$ and $\mathcal{Y} = \text{𝐒}_{+}^{n}$ (the set of symmetric positive semidefinite $n \times n$ matrices), is a saddle function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Combination rules", "weight": 1.0} -->

Saddle functions can be combined in several ways to yield saddle functions. For example the sum of two saddle functions is a saddle function, provided the domains have nonempty intersection. A saddle function scaled by a nonnegative scalar is a saddle function. Scaling a saddle function with a nonpositive scalar, and swapping its arguments, yields a saddle function: ${g{(x,y)}} = {- {f{(y,x)}}}$ is a saddle function provided $f$ is. Saddle functions are preserved by pre-composition of the convex and concave variables with an affine function, i.e., if $f$ is a saddle function, so is $f{({{Ax} + b},{{Cx} + d})}$. Indeed, the bi-affine function is just the inner product with an affine pre-composition for each of the convex and concave variables.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Saddle point problems", "weight": 1.0} -->

In other words, $x^{\star}$ minimizes $f{(x,y^{\star})}$ over $x \in \mathcal{X}$, and $y^{\star}$ maximizes $f{(x^{\star},y)}$ over $y \in \mathcal{Y}$. The basic *saddle point problem* is to find such a saddle point,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Saddle point problems", "weight": 1.0} -->

The value of the saddle point problem is $f{(x^{\star},y^{\star})}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Saddle point problems", "weight": 1.0} -->

Existence of a saddle point for a saddle function is guaranteed, provided some technical conditions hold. For example, Sion's theorem guarantees the existence of a saddle point when $\mathcal{Y}$ is compact. There are many other cases.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Examples", "weight": 1.0} -->

*Matrix game.* In a matrix game, player one chooses $i \in {\{ 1,\ldots,m\}}$, and player two chooses $j \in {\{ 1,\ldots,n\}}$, resulting in player one paying player two the amount $C_{ij}$. Player one wants to minimize this payment, while player two wishes to maximize it. In a mixed strategy, player one makes choices at random, from probabilities given by $x$ and player two makes independent choices with probabilities given by $y$. The expected payment from player one to player two is then ${f{(x,y)}} = {x^{T}Cy}$. With $\mathcal{X} = {\{ x\mid{{x \geq 0},{{\;1^{T}x} = 1}}\}}$, and similarly for $\mathcal{Y}$, a saddle point corresponds to an equilibrium, where no player can improve her position by changing (mixed) strategy.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Examples", "weight": 1.0} -->

The saddle point problem consists of finding a stable equilibrium, i.e., an optimal mixed strategy for each player.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Examples", "weight": 1.0} -->

*Lagrangian.* A saddle point of a Lagrangian of a convex optimization problem is a primal-dual optimal pair for the convex optimization problem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Saddle extremum functions", "weight": 1.0} -->

is called a *saddle max function*. Similarly, the function $H:{\mathcal{Y}\rightarrow{\text{𝐑} \cup {\{{- \infty}\}}}}$ defined by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Saddle extremum functions", "weight": 1.0} -->

is called a *saddle min function*. Saddle max functions are convex, and saddle min functions are concave. We will use the term *saddle extremum* (SE) functions to refer to saddle max or saddle min functions. Which is meant is clear from context, i.e., whether it is defined by minimization (infimum) or maximization (supremum), or its curvature (convex or concave). Note that in SE functions, we always maximize (or take supremum) over the concave variable, and minimize (or take infimum) over the convex variable. This means that evaluating $G{(x)}$ or $H{(y)}$ involves solving a convex optimization problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Examples", "weight": 1.0} -->

*Dual function.* Minimizing a Lagrangian $L{(x,\nu,\lambda)}$ over $x$ gives the dual function of the original convex optimization problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Examples", "weight": 1.0} -->

Maximizing a Lagrangian $L{(x,\nu,\lambda)}$ over $y = {(\nu,\lambda)}$ gives the objective function restricted to the feasible set.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Examples", "weight": 1.0} -->

*Conjugate of a convex function.* Suppose $f$ is convex. Then ${g{(x,y)}} = {{f{(x)}} - {x^{T}y}}$ is a saddle function, the Lagrangian of the problem of minimizing $f$ subject to $x = 0$. Its saddle min is the negative conjugate function: ${\inf_{x}{g{(x,y)}}} = {- {f^{*}{(y)}}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Saddle points via SE functions", "weight": 1.0} -->

A pair $(x^{\star},y^{\star})$ is a saddle point of a saddle function $f$ if and only if $x^{\star}$ minimizes the convex SE function $G$ in over $x \in \mathcal{X}$, and $y^{\star}$ maximizes the concave SE function $H$ defined in over $y \in \mathcal{Y}$. This means that we can find saddle points, i.e., solve the saddle point problem, by solving the convex optimization problem

<!-- chunk {"id": "body-0040", "role": "body", "section": "Saddle points via SE functions", "weight": 1.0} -->

with variable $x$, and the convex optimization problem

<!-- chunk {"id": "body-0041", "role": "body", "section": "Saddle points via SE functions", "weight": 1.0} -->

with variable $y$. The problem is called a minimax problem, since we are minimizing a function defined as the maximum over another variable. The problem is called a maximin problem.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Saddle points via SE functions", "weight": 1.0} -->

While the minimax problem and maximin problem are convex, they cannot be directly solved by conventional methods, since the objectives themselves are defined by maximization and minimization, respectively. There are solution methods specifically designed for minimax and maximin problems, but as we will see minimax problems involving SE functions can be transformed to equivalent forms that can be directly solved using conventional methods.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

In this paper we consider convex optimization problems that include SE functions in the objective or constraints, which we refer to as *saddle problems*. The convex problems that solve the basic saddle point problem and are special cases, where the objective is an SE function. As another example consider the problem of minimizing a convex function $\phi$ subject to the convex SE constraint ${H{(y)}} \leq 0$, which can be expressed as

<!-- chunk {"id": "body-0044", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

with variable $x$. The constraint here is called a *semi-infinite constraint*, since (when $\mathcal{Y}$ is not a singleton) it can be thought of as an infinite collection of convex constraints, one for each $y \in \mathcal{Y}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

Saddle problems include the minimax and maximin problems (that can be used to solve the saddle point problem), and semi-infinite problems that involve SE functions. There are many other examples of saddle problems, where SE functions can appear in expressions that define the objective and constraints.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

As a more specific example of a saddle problem consider the linear program with robust cost,

<!-- chunk {"id": "body-0047", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

with variable $x \in \text{𝐑}^{n}$, with $\mathcal{C} = {\{ c\mid{{Fc} \leq g}\}}$. This is an LP with worst case cost over the polyhedron $\mathcal{C}$. This is a saddle problem with convex variable $x$, concave variable $y$, and an objective which is a saddle max function.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Special cases with tractable analytical expressions", "weight": 1.0} -->

There are cases where an SE function can be worked out analytically. An example is the max of a linear function over a box,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Special cases with tractable analytical expressions", "weight": 1.0} -->

where the absolute value is elementwise. We will see other cases in our examples.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Subgradient methods", "weight": 1.0} -->

We can readily compute a subgradient of a saddle max function (or a supergradient of a saddle min function) at a given input, by simply maximizing over the concave variable (minimizing over the convex variable), which is itself a convex optimization problem, and then obtaining a subgradient (supergradient) at that maximizer (minimizer). We can then use any method to solve the saddle problem using these subgradients, e.g., subgradient-type methods, ellipsoid method, or localization methods such as the analytic center cutting plane method. In such an approach is used for general minimax problems.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Methods for specific forms", "weight": 1.0} -->

Many methods have been developed for finding saddle points of saddle functions with the special form

<!-- chunk {"id": "body-0052", "role": "body", "section": "Methods for specific forms", "weight": 1.0} -->

where $\phi$ is convex, $\psi$ is concave, and $K$ is a matrix. Beyond this example, there are many other special forms of saddle functions, with different methods adapted to properties such as smoothness, separability, and strong-convex-strong-concavity.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Dual reduction", "weight": 1.0} -->

A well-known trick can be used to transform a saddle point problem into an equivalent problem that does not contain SE functions. This method of transforming an inner minimization is not new; it has been used since the 1950s when Von Neumann proved the minimax theorem using strong duality in his work with Morgenstern on game theory. Using this observation, he showed that the minimax problem of a two player game is equivalent to an LP. Duality allows us to express the convex (concave) SE function as an infimum (supremum), which facilitates the use of standard convex optimization. We think of this as a reduction to an equivalent problem that removes the SE functions from the objective and constraints.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

We illustrate the dualization method for the robust cost LP. The key is to express the robust cost or saddle max function $\sup_{{Fc} \leq g}{c^{T}x}$ as an infimum. We first observe that this saddle max function is the optimal value of the LP

<!-- chunk {"id": "body-0055", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

with variable $\lambda$. With $\mathcal{C} = {\{ c\mid{{Fc} \leq g}\}}$, and assuming $\mathcal{C}$ is nonempty, this dual problem has the same optimal value as the primal, i.e.,

<!-- chunk {"id": "body-0056", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

Substituting this into we obtain the problem

<!-- chunk {"id": "body-0057", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

with variables $x$ and $\lambda$. This simple LP is equivalent to the original robust LP, in the sense that if $(x^{\star},\lambda^{\star})$ is a solution of, then $x^{\star}$ is a solution of the robust LP.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Robust cost LP", "weight": 1.0} -->

We will see this dualization trick in a far more general setting in §4.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Applications", "weight": 1.0} -->

In this section we describe a few applications of saddle programming.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We describe here a simplified version of the problem described in much more detail. Our goal is to construct a portfolio of $n$ bonds, giving by its holdings vector $h \in \text{𝐑}_{+}^{n}$, where $h_{i}$ is the number of bond $i$ held in the portfolio. Each bond produces a cash flow, i.e., a sequence of payments to the portfolio holder, up to some period $T$. Let $c_{i,t}$ be the payment from bond $i$ in time period $t$. Let $y \in \text{𝐑}^{T}$ be the yield curve, which gives the time value of cash: A payment of one dollar at time $t$ is worth $\exp{({- {ty_{t}}})}$ current dollars, assuming continuously compounded returns. The bond portfolio value, which is the present value of the total cash flow, can be expressed as

<!-- chunk {"id": "body-0061", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

This function is convex in the yields $y$ and concave (in fact, linear) in the holdings vector $h$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

Now suppose we do not know the yield curve, but instead have a convex set $\mathcal{Y}$ of possible values, with $y \in \mathcal{Y}$. The worst case value of the bond portfolio, over this set of possible yield curves, is

<!-- chunk {"id": "body-0063", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We recognize this as a saddle min function. (In this application, $y$ is the convex variable of the saddle function $V$, whereas elsewhere in this paper we use $y$ to denote the concave variable.)

<!-- chunk {"id": "body-0064", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We consider a robust bond portfolio construction problem of the form

<!-- chunk {"id": "body-0065", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

where $\phi$ is a convex objective, typically a measure of return and risk, $\mathcal{H}$ is a convex set of portfolio constraints (for example, imposing $h \geq 0$ and a total budget), and $V^{\lim}$ is a specified limit on worst case value of the portfolio over the yield curve set $\mathcal{Y}$, which has a saddle min as a constraint.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

For some simple choices of $\mathcal{Y}$ the worst case value can be found analytically. One example is when $\mathcal{Y}$ has a maximum element. In this special case, the maximum element is the minimizer of the value over $\mathcal{Y}$ (since $V$ is a monotone decreasing function of $y$). For other cases, however, we need to solve the saddle problem.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

We wish to fit a model parametrized by $\theta \in \Theta \subseteq \text{𝐑}^{n}$ to $m$ observed data points. We do this by minimizing a weighted loss over the observed data, plus a regularizer,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

where $\ell_{i}$ is the convex loss function for observed data point $i$, $r$ is a convex regularizer function, and the weights $w_{i}$ are nonnegative. The weights can be used to adjust a data sample that was not representative, as, or to ignore some of the data points (by taking $w_{i} = 0$), as. Evidently the weighted loss is a saddle function, with convex variable $\theta$ and concave variable $w$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

We consider the case when the weights are unknown, but lie in a convex set, $w \in \mathcal{W}$. The robust fitting problem is to choose $\theta$ to minimize the worst case loss over the set of possible weights, plus the regularizer,

<!-- chunk {"id": "body-0070", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

We recognize the first term, i.e., the worst case loss over the set of possible weights, as a saddle max function.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

For some simple choices of $\mathcal{W}$ the worst case loss can be expressed analytically. For example with

<!-- chunk {"id": "body-0072", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

(with $k \in {\lbrack 0,n\rbrack}$), the worst case loss is given by

<!-- chunk {"id": "body-0073", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

where $\phi$ is the sum-of-$k$-largest entries \[, §3.2.3\]. (Our choice of symbol $k$ suggests that $k$ is an integer, but it need not be.) In this case we judge the model parameter $\theta$ by its worst loss on any subset of $k$ of data points. Put another way, we judge $\theta$ by dropping the $m - k$ data points on which it does best (i.e., has the smallest loss).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

CVXPY directly supports the sum-of-$k$-largest function, so the robust fitting problem can be formulated and solved without using DSP. To support this function, CVXPY carries out a transformation very similar to the one that DSP does. The difference is that the transformation in CVXPY is specific to this one function, whereas the one carried out in DSP is general, and would work for other convex weight sets. One such case would be to constrain the Wasserstein distance of the weights to a nominal distribution.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Robust production problem with worst case prices", "weight": 1.0} -->

We consider the choice of a vector of quantities $q \in \mathcal{Q} \subseteq \text{𝐑}^{n}$. Positive entries indicate goods we buy, and negative quantities are goods we sell. The set of possible quantities $\mathcal{Q}$ is our production set, which is convex. In addition, we have a manufacturing cost associated with the choice $q$, given by $\phi{(q)}$, where $\phi$ is a convex function. The total cost is the manufacturing cost plus the cost of goods (which includes revenue), ${\phi{(q)}} + {p^{T}q}$, where $p \in \text{𝐑}^{n}$ is vector of prices.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Robust production problem with worst case prices", "weight": 1.0} -->

We consider the situation when we do not know the prices, but we have a convex set they lie, $p \in \mathcal{P}$. The worst case cost of the goods is $\max_{p \in \mathcal{P}}{p^{T}q}$. The robust production problem is

<!-- chunk {"id": "body-0077", "role": "body", "section": "Robust production problem with worst case prices", "weight": 1.0} -->

with variable $q$. Here too we can work out analytical expressions for simple choices of $\mathcal{P}$, such as a range for each component, in which case the worst case price is the upper limit for goods we buy, and the lower limit for goods we sell. In other cases, we solve the saddle problem.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

Markowitz portfolio construction chooses a set of weights (the fraction of the total portfolio value held in each asset) by solving the convex problem

<!-- chunk {"id": "body-0079", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

where the variable is the vector of portfolio weights $w \in \text{𝐑}^{n}$, $\mu \in \text{𝐑}^{n}$ is a forecast of the asset returns, $\gamma > 0$ is the risk aversion parameter, $\Sigma \in \text{𝐒}_{+ +}^{n}$ is a forecast of the asset return covariance matrix, and $\mathcal{W}$ is a convex set of feasible portfolios. The objective is called the risk adjusted (mean) return.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

Markowitz portfolio construction is known to be fairly sensitive to the (forecasts) $\mu$ and $\Sigma$, which have to be chosen with some care; see, e.g.,. One approach is to specify a convex uncertainty set $\mathcal{U}$ that $(\mu,\Sigma)$ must lie, and replace the objective with its worst case (smallest) value over this uncertainty set. This gives the robust Markowitz portfolio construction problem

<!-- chunk {"id": "body-0081", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

with variable $w$. This is described, e.g., \[Boy+17 \]. We observe that this is directly a saddle problem, with a saddle min objective, i.e., a maximin problem.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

For some simple versions of the problem we can work out the saddle min function explicitly. One example, given in \[Boy+17\], uses $\mathcal{U} = {\mathcal{M} \times \mathcal{S}}$, where

<!-- chunk {"id": "body-0083", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

where $\rho > 0$ is a vector of uncertainties in the forecast returns, and $\eta \in {}$ is a parameter that scales the perturbation to the forecast covariance matrix. (We interpret $\delta$ and $\Delta$ as perturbations of the nominal mean and covariance $\mu$ and $\Sigma$, respectively.) We can express the worst case risk adjusted return analytically as

<!-- chunk {"id": "body-0084", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

The first two terms are the nominal risk adjusted return; the last two terms (which are nonpositive) represent the cost of uncertainty.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conic representable saddle functions", "weight": 1.0} -->

Nemirovski and Juditsky propose a class of *conic representable* saddle functions which facilitate the automated dualization of saddle problems. We will first introduce some terminology and notation, and then describe the class of conic representable saddle functions.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conic representable saddle functions", "weight": 1.0} -->

Let $\mathcal{X}$ and $\mathcal{Y}$ be nonempty and possessing $\mathcal{K}$-representations

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conic representable saddle functions", "weight": 1.0} -->

A saddle function ${\phi{(x,y)}}:{{\mathcal{X} \times \mathcal{Y}}\rightarrow\text{𝐑}}$ is $\mathcal{K}$-representable if there exist constant matrices $P$, $Q$, $R$, constant vectors $p$ and $s$ and a cone $K \in \mathcal{K}$ such that for each $x \in \mathcal{X}$ and $y \in \mathcal{Y}$,

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conic representable saddle functions", "weight": 1.0} -->

Here $f$ is a vector of the same dimension as $y$, $t$ is a scalar, and $u$ is a vector. This definition generalizes simple class of bilinear saddle functions. See for much more detail.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

Suppose we have a $\mathcal{K}$-representable saddle function $\phi$ as above. The conic form allows us to derive a dualized representation of the saddle extremum function

<!-- chunk {"id": "body-0090", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

which again admits a tractable conic form, meaning that it can be represented in a DSL like CVXPY. Specifically,

<!-- chunk {"id": "body-0091", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

where in (4.2) we use Sion's minimax theorem to reverse the inf and sup, and in we invoke strong duality to replace the supremum over $y$ with an infimum over $\lambda$. Concretely, strong duality and the conic structure allow us to equate

<!-- chunk {"id": "body-0092", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

where $K^{*}$ is the dual cone of $K$. This is exactly the automated dualization made possible by the conic representable form of $\phi$ (which DSP provides). Given the conic representation of $\phi$, the dualized form is obtained via the explicit formula given.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

The final line implies a conic representation of the epigraph of $\Phi{(x)}$,

<!-- chunk {"id": "body-0094", "role": "body", "section": "Automated dualization", "weight": 1.0} -->

which is tractable and can be implemented in a DSL like CVXPY. This transformation is exact, and so there is no notion of approximation error or optimality gap arising from the dualization procedure.

<!-- chunk {"id": "body-0095", "role": "body", "section": "A mathematical nuance", "weight": 1.0} -->

Switching the $\inf$ and $\sup$ in (4.2) requires Sion's theorem to hold. A sufficient condition for Sion's theorem to hold is that the set $\mathcal{Y}$ is compact. However, the min and max can be exchanged even if $\mathcal{Y}$ is not compact. Then, due to the max-min inequality

<!-- chunk {"id": "body-0096", "role": "body", "section": "A mathematical nuance", "weight": 1.0} -->

the equality in is replaced with a less than or equal to, and we obtain a convex restriction. Thus, if a user creates a problem involving an SE function (as opposed to a saddle point problem only containing saddle functions in the objective), then DSP guarantees that the problem generated is a restriction. This means that the variables returned are feasible and the returned optimal value is an upper bound on the optimal value for the user's problem.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

One challenge that arises in transforming the mathematical concept of conic representable saddle functions into a practical implementation is that the automated dualization removes the concave variable from the problem. Additionally, the procedure relies on the technical conditions such as compactness, which we believe should not be exposed in a user interface. We now address these points.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

In our implementation, a saddle problem with an SE function in the objective is solved by applying the above automatic dualization to both the objective $\phi$ and $- \phi$ and then solving each resulting convex problem. Note that $\phi{(x,y)}$ is convex in $x$ and concave in $y$, while $- {\phi{(x,y)}}$ is concave in $x$ and convex in $y$. We do so in order to obtain both the convex and concave components of the saddle point, since the dualization removes the concave variable. To see this, note that contains $x$ but not $y$ (and the opposite holds for the negated problem). The saddle problem is only reported as solved if the optimal value of the problem with objective $\phi$, $u$, is within a numerical tolerance of the negated optimal value of the problem with objective $- \phi$, $- l$. If this holds, this actually implies that

<!-- chunk {"id": "body-0099", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

i.e., (4.2) was valid, even if for example $\mathcal{Y}$ is not compact. To see this, note that solving for $\phi$ as well as $- \phi$ results in an upper and a lower bound on the optimal value of the saddle point problem,

<!-- chunk {"id": "body-0100", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

Using symmetry and combining the above inequalities, we obtain

<!-- chunk {"id": "body-0101", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

Suppose now that $l = u$. Note that since

<!-- chunk {"id": "body-0102", "role": "body", "section": "Obtaining convex and concave saddle point coordinates", "weight": 1.0} -->

Thus, a user need not concern themselves with the compactness of $\mathcal{Y}$ (or any other sufficient condition for Sion's theorem) when using DSP to find a saddle point; if a saddle point problem is solved, then the saddle point property is guaranteed to hold. This mathematical insight extends the work of, which assumes compactness of $\mathcal{Y}$, allowing users who might be unfamiliar with this technical restriction to use DSP.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Implementation", "weight": 1.0} -->

In this section we describe our Python implementation of the concepts and methods described in §4, which we also call DSP. It can be accessed online under an open source license at DSP works with CVXPY, an implementation of a DSL for convex optimization based on DCP. We use the term DSP in two different ways. We use it to refer to the mathematical concept of disciplined saddle programming, and also our specific implementation; which is meant should be clear from the context. The term DSP-compliant refers to a function or expression that is constructed according to the DSP composition rules given in §5.2. It can also refer to a problem that is constructed according to these rules. In the code snippets below, we use the prefix cp--- to indicate functions and classes from CVXPY. (We give functions and classes from DSP without prefix, whereas they would likely have a prefix such as

<!-- chunk {"id": "body-0104", "role": "body", "section": "Atoms", "weight": 1.0} -->

Saddle functions in DSP are created from fundamental building blocks or atoms. These building blocks extend the atoms from CVXPY. In CVXPY, atoms are either jointly convex or concave in all their variables, but in DSP, atoms are (jointly) convex in a subset of the variables and (jointly) concave in the remaining variables. We describe some DSP atoms below. The listing is not exhaustive, and additional atoms can be added as necessary.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Inner product", "weight": 1.0} -->

The atom inner product $x^{T}y$. Since either $x$ or $y$ could represent the convex variable, we adopt the convention in DSP that the first argument of According to the DSP rules, both arguments to and the variables they depend on must be disjoint.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Saddle inner product", "weight": 1.0} -->

The atom where $F$ and $G$ are vectors of nonnegative and respectively elementwise convex and concave functions. It is DSP-compliant if $F$ is DCP convex and nonnegative and $G$ is DCP concave. If the function $G$ is not DCP nonnegative, then the DCP constraint This is analogous to how the DCP constraint expression As an example consider

<!-- chunk {"id": "body-0107", "role": "body", "section": "Saddle inner product", "weight": 1.0} -->

This represents the saddle function

<!-- chunk {"id": "body-0108", "role": "body", "section": "Saddle inner product", "weight": 1.0} -->

where $I$ is the $\{ 0,\infty\}$ indicator function of its argument.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Weighted $\\ell_{2}$ norm", "weight": 1.0} -->

The represents the saddle function $\left( {\sum_{i = 1}^{n}{y_{i}x_{i}^{2}}} \right)^{1/2}$, with $y \geq 0$. It is DSP-compliant if Here too, the constraint

<!-- chunk {"id": "body-0110", "role": "body", "section": "Weighted log-sum-exp", "weight": 1.0} -->

The represents the saddle function $\log\left( {\sum_{i = 1}^{n}{y_{i}{\exp x_{i}}}} \right)$, with $y \geq 0$. It is DSP-compliant if The constraint

<!-- chunk {"id": "body-0111", "role": "body", "section": "Quasi-semidefinite quadratic form", "weight": 1.0} -->

where the matrix is quasi-semidefinite, i.e., $P \in \text{𝐒}_{+}^{n}$ and ${- Q} \in \text{𝐒}_{+}^{n}$. It is DSP-compliant if $x$ is DCP affine and $y$ is DCP affine.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Quadratic form", "weight": 1.0} -->

The the function $x^{T}Yx$, where $Y$ is a PSD matrix. It is DSP-compliant if $x$ is DCP affine, and $Y$ is DCP PSD.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

The atoms can be combined according to the calculus described below to form expressions that are DSP-compliant. For example, saddle functions can be added or scaled. DCP-compliant convex and concave expressions are promoted to saddle functions with no concave or convex variables, respectively. For example, with variables the expression

<!-- chunk {"id": "body-0114", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

is DSP-compliant, with convex variable affine variable Calling the expression is DSP-compliant. The methods list the convex, concave, and affine variables, respectively. The convex variables are those that could only be convex, and similarly for concave variables. We refer to the convex variables as the unambiguously convex variables, and similarly for the concave variables. The three lists of variables gives a partition of all the variables the expression depends. For the expression above, and Note that the role of since it could be either a convex or concave variable.

<!-- chunk {"id": "body-0115", "role": "body", "section": "No mixing variables rule", "weight": 1.0} -->

The DSP rules prohibit mixing of convex and concave variables. For example if we add two saddle expressions, no variable can appear in both its convex and concave variable lists.

<!-- chunk {"id": "body-0116", "role": "body", "section": "DSP-compliance is sufficient but not necessary to be a saddle function", "weight": 1.0} -->

Recall that if an expression is DCP convex (concave), then it is convex (concave), but the converse is false. For example, the expression function $\sqrt{1 + x^{2}}$, but is not DCP. But we can express the same function as The same holds for DSP and saddle function: If an expression is DSP-compliant, then it represents a saddle function; but it can represent a saddle function and not be DSP-compliant. As with DCP, such an expression would need to be rewritten in DSP-compliant form, to use any of the other features of DSP (such as a solution method). As an example, the expression but is not DSP-compliant. The same function can be expressed as DSP-compliant. While this restrictive syntax is an inherent limitation of disciplined convex programming in general, it is required for any parser based on the DSP composition rules.

<!-- chunk {"id": "body-0117", "role": "body", "section": "DSP-compliance is sufficient but not necessary to be a saddle function", "weight": 1.0} -->

When there are affine variables in a DSP-compliant expression, it means that those variables could be considered either convex or concave; either way, the function is a saddle function.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Example", "weight": 1.0} -->

The code below defines the bi-linear saddle function ${f{(x,y)}} = {x^{T}Cy}$, the objective of a matrix game, with $x$ the convex variable and $y$ the concave variable.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Example", "weight": 1.0} -->

1from dsp import * # notational convenience
Creating a saddle function.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Example", "weight": 1.0} -->

Lines 1--3 import the necessary packages (which we will use but not show in the sequel). In lines 5--7, we create two CVXPY variables and a constant matrix. In line 9 we construct the saddle function the DSP atom so this matches the DSP rules. In line 11 we check if In lines 13--15 we call functions that return lists of the convex, concave, and affine variables, respectively. The results of lines 13--15 might seem odd, but recall that marks its first argument as convex and its second as concave.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Saddle point problem objective", "weight": 1.0} -->

To construct a saddle point problem, we first create an objective using

<!-- chunk {"id": "body-0122", "role": "body", "section": "Saddle point problem objective", "weight": 1.0} -->

where The objective This is analogous to the CVXPY contructors which create objectives from expressions.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

A saddle point problem is constructed using

<!-- chunk {"id": "body-0124", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

Here, of convex variables and The objective must be DSP-compliant for the problem to be DSP-compliant. We now describe the remaining conditions under which the constructed problem is DSP-compliant.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

Each constraint in the list must be DCP, and can only involve convex variables or concave variables; convex and concave variables cannot both appear in any one constraint. The list of convex and concave variables partitions all the variables that appear in the objective or the constraints. In cases where the role of a variable is unambiguous, it is inferred, and does not need to be in either list. For example with the objective

<!-- chunk {"id": "body-0126", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

concave variables, and so do not need to appear in the lists used to construct a saddle point problem. The variable concave variable, and so must appear in one of the lists.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

The role of a variable can also be inferred from the constraints: Any variable that appears in a constraint with convex (concave) variables must also be convex (concave). With the objective above, the constraint to the saddle point constructor, since the roles of all variables can be inferred. When the roles of all variables are unambiguous, the lists are optional.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Saddle point problem", "weight": 1.0} -->

The roles of the variables in a saddle point problem and is a partition of all the variables appearing in the objective or constraints. This is useful for debugging, to be sure that DSP agrees with you about the roles of all variables. A DSP-compliant saddle point problem must have an empty list of affine variables. (If it did not, the problem would be ambiguous.)

<!-- chunk {"id": "body-0129", "role": "body", "section": "Solving a saddle point problem", "weight": 1.0} -->

The checking the objective and constraints for DSP-compliance. The conic representation of the problem is obtained, which involves setting up an auxiliary problem and compiling it using CVXPY. Then, the dualization is carried out, which results in another CVXPY problem which is then solved to yield the objective value. This has the side effect of setting all convex variables' To also obtain the values of the concave variables, the saddle point problem is solved again with a negated objective and the roles of the minimization and maximization variables reversed. We emphasize that as DSP acts as a compiler, it does not implement any optimization algorithms itself, but rather relies on the solvers accessible through CVXPY.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Example", "weight": 1.0} -->

Here we create and solve a matrix game, continuing the example above where was defined. We do not need to pass in lists of variables since their roles can be inferred.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Example", "weight": 1.0} -->

2constraints = [x &gt;= 0, cp.sum(x) == 1, y &gt;= 0, cp.sum(y) == 1]
3prob = SaddlePointProblem(obj, constraints)
5prob.is_dsp # True
6prob.convex_variables # [x]
7prob.concave_variables # [y]
8prob.affine_variables #
10prob.solve # solves the problem
Creating and solving a matrix game.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Local variables", "weight": 1.0} -->

An SE function has one of the forms

<!-- chunk {"id": "body-0133", "role": "body", "section": "Local variables", "weight": 1.0} -->

where $f$ is a saddle function. Note that $y$ in the definition of $G$, and $x$ in the definition of $H$, are local or dummy variables, understood to have no connection to any other variable. Their scope extends only to the definition, and not beyond.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Local variables", "weight": 1.0} -->

To express this subtlety in DSP, we use the class The variables that are maximized over (in a saddle max function) or minimized over (in a saddle min function) must be declared using the Any appear in any other SE function.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

Here, a list of constraints. We now describe the rules for constructing a DSP-compliant SE function.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

If a and the function's concave variables, and all variables appearing in the list of constraints, must be variables must all be regular A similar rule applies for The list of constraints is used to specify the set over which the sup or inf is taken. Each constraint must be DCP-compliant, and can only contain With

<!-- chunk {"id": "body-0137", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zl8xID0gc2FkZGxlX21heChpbm5lcih4LCB5X2xvYykgKyB6LCBbeV9sb2MgPD0gMV0pCmZfMiA9IHNhZGRsZV9tYXgoaW5uZXIoeCwgeV9sb2MpICsgel9sb2MsIFt5X2xvYyA8PSAxLCB6X2xvYyA8PSAxXSk=){download=""}

<!-- chunk {"id": "body-0138", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

1f_1 = saddle_max(inner(x, y_loc) + z, \[y_loc \<= 1\])

<!-- chunk {"id": "body-0139", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zl8zID0gc2FkZGxlX21heChpbm5lcih4LCB5X2xvYykgKyB6LCBbeV9sb2MgPD0gMSwgeiA8PSAxXSkKZl80ID0gc2FkZGxlX21heChpbm5lcih4LCB5KSArIHpfbG9jLCBbeV9sb2MgPD0gMSwgel9sb2MgPD0gMV0p){download=""}

<!-- chunk {"id": "body-0140", "role": "body", "section": "Constructing SE functions", "weight": 1.0} -->

The first is not DSP-compliant because but appears in the constraints. The second is not DSP-compliant because the saddle function.

<!-- chunk {"id": "body-0141", "role": "body", "section": "SE functions are DCP", "weight": 1.0} -->

When they are DSP-compliant, a They can be used anywhere in CVXPY that a convex or concave function is appropriate. You can add them, compose them (in appropriate ways), use them in the objective or either side of constraints (in appropriate ways).

<!-- chunk {"id": "body-0142", "role": "body", "section": "Examples", "weight": 1.0} -->

Now we provide full examples demonstrating construction of a game described in §5.3 as a saddle problem involving an SE function.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Examples", "weight": 1.0} -->

4# Creating local variables
7# Convex in x, concave in y_loc
8f = saddle_inner(C @ x, y_loc)
10# maximizes over y_loc
11G = saddle_max(f, [y_loc &gt;= 0, cp.sum(y_loc) == 1])
Creating a saddle max.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Examples", "weight": 1.0} -->

Note that exactly the same way.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Saddle problems", "weight": 1.0} -->

A saddle problem is a convex problem that uses SE functions. To be DSP-compliant, the problem must be DCP (which implies all SE functions are DSP-compliant). When you call the solve method on a saddle problem involving SE functions, and the solve is successful, then all variables' with optimal values. This includes maximized or minimized over; they are assigned to the value of a particular maximizer or minimizer of the SE function at the value of the non-local variables, with no further guarantees.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Example", "weight": 1.0} -->

We continue our example from §5.4 and solve the matrix game using either a saddle max.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Example", "weight": 1.0} -->

1prob = cp.Problem(cp.Minimize(G), [x &gt;= 0, cp.sum(x) == 1])
3prob.is_dsp # True
5prob.solve # solving the problem
Creating and solving a saddle problem using a saddle max to solve the matrix game.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section we give numerical examples, taken from §3, showing how to create DSP-compliant problems. The specific problem instances we take are small, since our main point is to show how easily the problems can be specified in DSP. But DSP will scale to far larger problem instances. Again, code and data for these examples are available at

<!-- chunk {"id": "body-0149", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

Our first example is the robust bond portfolio construction problem described in §3.1. We consider portfolios of $n = 20$ bonds, over a period $T = 60$ half-years, i.e., $30$ years. The bonds are taken as representative ones in a global investment grade bond portfolio; for more detail, see. The payments from the bonds are given by $C \in \text{𝐑}^{20 \times 60}$, with cash flow of bond $i$ in period $t$ denoted $c_{i,t}$. The goal is to choose holdings $h \in \text{𝐑}_{+}^{20}$, with the portfolio constraint set $\mathcal{H}$ given by

<!-- chunk {"id": "body-0150", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

i.e., the investments must be nonnegative and have a total value (budget) $B$, which we take to be \$100. Here $p \in \text{𝐑}_{+}^{20}$ denotes the price of the bonds on September 12, 2022. The portfolio objective is

<!-- chunk {"id": "body-0151", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

where $h^{mkt} \in \text{𝐑}_{+}^{20}$ is the market portfolio scaled to a value of \$100, and $\circ$ denotes Hadamard or elementwise multiplication. This is called the turn-over distance, since it tells us how much we would need to buy and sell to convert our portfolio to the market portfolio.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

The yield curve set $\mathcal{Y}$ is described in terms of perturbations to the nominal or current yield curve $y^{nom} \in \text{𝐑}^{60}$, which is the yield curve on September 12, 2022. We take

<!-- chunk {"id": "body-0153", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We interpret $\delta \in \text{𝐑}^{60}$ as a shock to the yield curve, which we limit elementwise, in absolute sum, and in smoothness. The specific parameter values are given by

<!-- chunk {"id": "body-0154", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

In the robust bond portfolio problem we take $V^{\lim} = 90$, that is, the worst case value of the portfolio cannot drop below \$90 for any $y \in \mathcal{Y}$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We solve the problem using the following code, where we assume the cash flow matrix and the market portfolio

<!-- chunk {"id": "body-0156", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

1# Constants and parameters
3delta_max, kappa, omega = 0.02, 0.9, 1e-6
8h = cp.Variable(n, nonneg=True)
14phi = 0.5 * cp.norm1(cp.multiply(h, p) - cp.multiply(h_mkt, p))
16# Creating saddle min function
19 t_plus_1 = np.arange(T) + 1 # Account for zero-indexing
20 V += saddle_inner(cp.exp(cp.multiply(-t_plus_1, y)), h[i] * C[i])
23 cp.norm_inf(delta) &lt;= delta_max,
24 cp.norm1(delta) &lt;= kappa,
25 cp.sum_squares(delta - delta) &lt;= omega,
30# Creating and solving the problem
31problem = cp.Problem(cp.Minimize(phi), [h @ p == B, V_wc &gt;= V_lim])
Robust bond portfolio construction.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

We first define the constants and parameters in lines 2--5, before creating the variable for the holdings and the perturbation, in line 10. In line 11 we define and the perturbation The objective function is defined in line 14. Lines 17--20 define the saddle function The yield uncertainty set is defined in line 25 using We use the concave expression to create and solve a CVXPY problem in lines 31--32.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Robust bond portfolio construction", "weight": 1.0} -->

Table 1 summarizes the results. The nominal portfolio is the market portfolio, which has zero turn-over distance to the market portfolio, i.e., zero objective value. This nominal portfolio, however, does not satisfy the worst-case portfolio value constraint, since there are yield curves in $\mathcal{Y}$ that cause the portfolio value to drop to around \$87, less than our limit of \$90. The solution of the robust problem has turn-over distance \$15.32, and satisfies the constraint that the worst-case value be at least \$90.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

We consider an instance of the model fitting problem described in §3.2. We use the well known Titanic data set, which gives several attributes for each passenger on the ill-fated Titanic voyage, including whether they survived. A classifier is fit to predict survival based on the features sex, age (binned into three groups, 0--26, 26--53, and 53--80), and class ($1$, $2$, or $3$). These features are encoded as a Boolean vector $a_{i} \in \text{𝐑}^{7}$. The label $y_{i} = 1$ means passenger $i$ survived, and $y_{i} = {- 1}$ otherwise. There are 1046 examples, but we fit our model using only the $m = 50$ passengers who embarked from Queenstown, one of three ports of embarkation. This is a somewhat non-representative sample; for example, the survival rate among Queenstown departures is 26%, whereas the overall survival rate is 40.8%.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

This is a common situation in machine learning, where the distribution of labels in the training data does not match that of the test dataset (known as label shift), for which we seek a robust solution.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

The data is weighted to partially correct for the different survival rates for our training set (26%) and the whole data set (40.8%). To do this we set $w_{i} = z_{1}$ when $y_{i} = 1$ and $w_{i} = z_{2}$ when $y_{i} = {- 1}$. We require $w \geq 0$ and ${\mathbf{1}^{T}w} = 1$, and

<!-- chunk {"id": "body-0162", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

Thus $\mathcal{W}$ consists of weights on the Queenstown departure samples that correct the survival rate to within 5% of the overall survival rate.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

The code shown below solves this problem, where we assume the data matrix is already defined as is defined as of survival in the training set is defined as

<!-- chunk {"id": "body-0164", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

1# Constants and parameters
10weights = cp.Variable(m, nonneg=True)
11surv_weight_0 = cp.Variable
12surv_weight_1 = cp.Variable
14# Defining the loss function and the weight constraints
15y_hat = A_train @ theta + beta_0
16loss = cp.pos(1 - cp.multiply(y_train, y_hat))
17objective = MinimizeMaximize(saddle_inner(loss, weights)
18 + eta * cp.sum_squares(theta))
24 weights[inds_0] == surv_weight_0,
25 weights[inds_1] == surv_weight_1,
28# Creating and solving the problem
29problem = SaddlePointProblem(objective, constraints)
Model fitting robust to data weights.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

After defining the constants and parameters in lines 2--5, we specify the variables for the model coefficient and the weights in lines 8--9 and 10--12, respectively. The loss function and regularizer which make up the objective are defined next in lines 15--18. The weight constraints are defined in lines 20--26. The saddle point problem is created and solved in lines 29 and 30.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Model fitting robust to data weights", "weight": 1.0} -->

The results are shown in table 2. We report the test accuracy on all samples in the dataset with a different port of embarkation than Queenstown (996 samples). We see that while the robust classification model has slightly lower training accuracy than the nominal model, it achieves a higher test accuracy, generalizing from the non-representative training data better than the nominal classifier, which uses uniform weights.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

We consider the robust Markowitz portfolio construction problem described in §3.4. We take $n = 6$ assets, which are the (five) Fama-French factors plus a risk-free asset. The data is obtained from the Kenneth R. French data library, with monthly return data available from July 1963 to October 2022. The nominal return and risk are the empirical mean and covariance of the returns. (These obviously involve look-ahead, but the point of the example is how to specify and solve the problem with DSP, not the construction of a real portfolio.) We take parameters $\rho = 0.02$, $\eta = 0.2$, and risk aversion parameter $\gamma = 1$.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

In the code, we use for the mean and covariance estimates, respectively, and the parameters are denoted

<!-- chunk {"id": "body-0169", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

1# Constants and parameters 3rho, eta, gamma = 0.2, 0.2, 1 6w = cp.Variable(n, nonneg=True) 8delta_loc = LocalVariable(n) 9Sigma_perturbed = LocalVariable((n, n), PSD=True) 10Delta_loc = LocalVariable((n, n)) 12# Creating saddle min function 13f = w @ mu + saddle_inner(delta_loc, w) \ 14 - gamma * saddle_quad_form(w, Sigma_perturbed) 16Sigma_diag = Sigma.diagonal 18 cp.abs(delta_loc) &lt;= rho, Sigma_perturbed == Sigma + Delta_loc, 19 cp.abs(Delta_loc) &lt;= eta * np.sqrt(np.outer(Sigma_diag, Sigma_diag)) 22G = saddle_min(f, local_constraints) 24# Creating and solving the problem 25problem = cp.Problem(cp.Maximize(G),

<!-- chunk {"id": "body-0170", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

[cp.sum(w) == 1]) Robust Markowitz portfolio construction.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

We first define the constants and parameters, before creating the weights variable in line 6, and the local variables for the perturbations in lines 8--10. The saddle function for the objective is defined in line 13, followed by the constraints on the perturbations. Both are combined into the concave saddle min function, which is maximized over the portfolio constraints in lines 25--26.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Robust Markowitz portfolio construction", "weight": 1.0} -->

The results are shown in table 3. The robust portfolio yields a slightly lower risk adjusted return of 0.291 compared to the nominal optimal portfolio with 0.295. But the robust portfolio attains a higher worst-case risk adjusted return of 0.076, compared to the nominal optimal portfolio which attains 0.065.
