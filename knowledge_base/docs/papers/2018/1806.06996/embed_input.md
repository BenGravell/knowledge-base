<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming

Topics include Polynomial optimization, Sum of squares, Semidefinite programming, DSOS, SDSOS, Nonnegative polynomials, Convex polynomials, Linear programming, Second-order cone programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies polynomial optimization through both classical SOS/SDP machinery and scalable alternatives based on DSOS and SDSOS certificates. The dissertation is valuable as a bridge between nonnegative-polynomial theory, convex-polynomial structure, and large-scale conic relaxations that trade SDP strength for LP/SOCP tractability.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The problem of optimizing over the cone of nonnegative polynomials is a fundamental problem in computational mathematics, with applications to polynomial optimization, control, machine learning, game theory, and combinatorics, among others. A number of breakthrough papers in the early 2000s showed that this problem, long thought to be out of reach, could be tackled by using sum of squares programming. This technique however has proved to be expensive for large-scale problems, as it involves solving large semidefinite programs (SDPs). In the first part of this thesis, we present two methods for approximately solving large-scale sum of squares programs that dispense altogether with semidefinite programming and only involve solving a sequence of linear or second order cone programs generated in an adaptive fashion. We then focus on the problem of finding tight lower bounds on polynomial optimization problems (POPs), a fundamental task in this area that is most commonly handled through the use of SDP-based sum of squares hierarchies (e.g., due to Lasserre and Parrilo).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In contrast to previous approaches, we provide the first theoretical framework for constructing converging hierarchies of lower bounds on POPs whose computation simply requires the ability to multiply certain fixed polynomials together and to check nonnegativity of the coefficients of their product. In the second part of this thesis, we focus on the theory and applications of the problem of optimizing over convex polynomials, a subcase of the problem of optimizing over nonnegative polynomials. (See manuscript for the rest of the abstract.)

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Semidefinite programming is a powerful tool in optimization that is used in many different contexts, perhaps most notably to obtain strong bounds on discrete optimization problems or nonconvex polynomial programs. One difficulty in applying semidefinite programming is that state-of-the-art general-purpose solvers often cannot solve very large instances reliably and in a reasonable amount of time. As a result, at relatively large scales, one has to resort either to specialized solution techniques and algorithms that employ problem structure, or to easier optimization problems that lead to weaker bounds. We will focus on the latter approach in this chapter.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

At a high level, our goal is to not solve semidefinite programs (SDPs) to optimality, but rather replace them with cheaper conic relaxations---*linear and second order cone relaxations* to be precise---that return useful bounds quickly. Throughout the chapter, we will aim to find lower bounds (for minimization problems); i.e., bounds that certify the distance of a candidate solution to optimality. Fast, good-quality lower bounds are especially important in the context of branch-and-bound schemes, where one needs to strike a delicate balance between the time spent on bounding and the time spent on branching, in order to keep the overall solution time low. Currently, in commercial integer programming solvers, almost all lower bounding approaches using branch-and-bound schemes exclusively produce linear inequalities. Even though semidefinite cuts are known to be stronger, they are often too expensive to be used even at the root node of a branch-and-bound tree.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of this, many high-performance solvers, e.g., IBM ILOG CPLEX and Gurobi, do not even provide an SDP solver and instead solely work with LP and SOCP relaxations. Our goal in this chapter is to offer some tools that exploit the power of SDP-based cuts, while staying entirely in the realm of LP and SOCP. We apply these tools to classical problems in both nonconvex polynomial optimization and discrete optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Techniques that provide lower bounds on minimization problems are precisely those that certify nonnegativity of objective functions on feasible sets. To see this, note that a scalar $\gamma$ is a lower bound on the minimum value of a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ on a set ${K \subseteq {\mathbb{R}}^{n}},$ if and only if ${{f{(x)}} - \gamma} \geq 0$ for all $x \in K$. As most discrete optimization problems (including those in the complexity class NP) can be written as polynomial optimization problems, the problem of certifying nonnegativity of polynomial functions, either globally or on basic semialgebraic sets, is a fundamental one.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A polynomial $p{(x)}: = p{(x_{1},\ldots,x_{n})}$ is said to be *nonnegative*, if ${p{(x)}} \geq 0$ for all $x \in {\mathbb{R}}^{n}$. Unfortunately, even in this unconstrained setting, the problem of testing nonnegativity of a polynomial $p$ is NP-hard even when its degree equals four. This is an immediate corollary of the fact that checking if a symmetric matrix $M$ is copositive---i.e., if ${{x^{T}Mx} \geq 0},{{\forall x} \geq 0}$---is NP-hard.^11^1Weak NP-hardness of testing matrix copositivity is originally proven by Murty and Kabadi; its strong NP-hardness is apparent from the work of de Klerk and Pasechnik.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite this computational complexity barrier, there has been great success in using sum of squares (SOS) programming to obtain certificates of nonnegativity of polynomials in practical settings. It is known from Artin's solution to Hilbert's 17th problem that a polynomial $p{(x)}$ is nonnegative if and only if

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

for some polynomials $q_{1},\ldots,q_{t},g_{1},\ldots,g_{r}$. When $p$ is a quadratic polynomial, then the polynomials $g_{i}$ are not needed and the polynomials $q_{i}$ can be assumed to be linear functions. In this case, by writing $p{(x)}$ as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $Q$ is an ${({n + 1})} \times {({n + 1})}$ symmetric matrix, checking nonnegativity of $p{(x)}$ reduces to checking the nonnegativity of the eigenvalues of $Q$; i.e., checking if $Q$ is positive semidefinite.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

More generally, if the degrees of $q_{i}$ and $g_{i}$ are fixed in (2.1), then checking for a representation of $p$ of the form in (2.1) reduces to solving an SDP, whose size depends on the dimension of $x$, and the degrees of $p,q_{i}$ and $g_{i}$. This insight has led to significant progress in certifying nonnegativity of polynomials arising in many areas. In practice, the "first level" of the SOS hierarchy is often the one used, where the polynomials $g_{i}$ are left out and one simply checks if $p$ is a sum of squares of other polynomials. In this case already, because of the numerical difficulty of solving large SDPs, the polynomials that can be certified to be nonnegative usually do not have very high degrees or very many variables.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, finding a sum of squares certificate that a given quartic polynomial over $n$ variables is nonnegative requires solving an SDP involving roughly $O{(n^{4})}$ constraints and a positive semidefinite matrix variable of size ${{O{(n^{2})}} \times O}{(n^{2})}$. Even for a handful of or a dozen variables, the underlying semidefinite constraints prove to be expensive. Indeed, in the absence of additional structure, most examples in the literature have less than 10 variables.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently other systematic approaches to certifying nonnegativity of polynomials have been proposed which lead to less expensive optimization problems than semidefinite programming problems. In particular, Ahmadi and Majumdar, introduce "DSOS and SDSOS" optimization techniques, which replace semidefinite programs arising in the nonnegativity certification problem by linear programs and second-order cone programs. Instead of optimizing over the cone of sum of squares polynomials, the authors optimize over two subsets which they call "diagonally dominant sum of squares" and "scaled diagonally dominant sum of squares" polynomials (see Section 3.2.1 for formal definitions). In the language of semidefinite programming, this translates to solving optimization problems over the cone of diagonally dominant matrices and scaled diagonally dominant matrices. These can be done by LP and SOCP respectively. The authors have had notable success with these techniques in different applications. For instance, they are able to run these relaxations for polynomial optimization problems of degree 4 in 70 variables in the order of a few minutes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

They have also used their techniques to push the size limits of some SOS problems in controls; examples include stabilizing a model of a humanoid robot with 30 state variables and 14 control inputs, or exploring the real-time applications of SOS techniques in problems such as collision-free autonomous motion planning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these results, our goal in this chapter is to start with DSOS and SDSOS techniques and improve on them. By exploiting ideas from column generation in large-scale linear programming, and by appropriately interpreting the DSOS and SDSOS constraints, we produce several iterative LP and SOCP-based algorithms that improve the quality of the bounds obtained from the DSOS and SDSOS relaxations. Geometrically, this amounts to optimizing over structured subsets of sum of squares polynomials that are larger than the sets of diagonally dominant or scaled diagonally dominant sum of squares polynomials. For semidefinite programming, this is equivalent to optimizing over structured subsets of the cone of positive semidefinite matrices. An important distinction to make between the DSOS/SDSOS/SOS approaches and our approach, is that our approximations iteratively get larger in the direction of the given objective function, unlike the DSOS, SDSOS, and SOS approaches which all try to inner approximate the set of nonnegative polynomials *irrespective* of any particular direction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

In related literature, Krishnan and Mitchell use linear programming techniques to approximately solve SDPs by taking a semi-infinite LP representation of the SDP and applying column generation. In addition, Kim and Kojima solve second order cone relaxations of SDPs which are closely related to the dual of an SDSOS program in the case of quadratic programming; see Section 2.3 for further discussion of these two papers.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The organization of the rest of the chapter is as follows. In the next section, we review relevant notation, and discuss the prior literature on DSOS and SDSOS programming. In Section 2.3, we give a high-level overview of our column generation approaches in the context of a general SDP. In Section 2.4, we describe an application of our ideas to nonconvex polynomial optimization and present computational experiments with certain column generation implementations. In Section 2.5, we apply our column generation approach to approximate a copositive program arising from a specific discrete optimization application (namely the stable set problem). All the work in these sections can be viewed as providing techniques to optimize over subsets of positive semidefinite matrices. We then conclude in Section 2.6 with some future directions, and discuss ideas for column generation which allow one to go beyond subsets of positive semidefinite matrices in the case of polynomial and copositive optimization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DSOS and SDSOS optimization", "weight": 1.0} -->

In order to alleviate the problem of scalability posed by the SDPs arising from sum of squares programs, Ahmadi and Majumdar, ^22^2The work in is currently in preparation for submission; the one in is a shorter conference version of which has already appeared. The presentation of the current chapter is meant to be self-contained. recently introduced similar-purpose LP and SOCP-based optimization problems that they refer to as *DSOS and SDSOS programs*. Since we will be building on these concepts, we briefly review their relevant aspects to make our chapter self-contained.

<!-- chunk {"id": "body-0021", "role": "body", "section": "DSOS and SDSOS optimization", "weight": 1.0} -->

The idea, is to replace the condition that the Gram matrix $Q$ be positive semidefinite with stronger but cheaper conditions in the hope of obtaining more efficient inner approximations to the cone $SOS_{n,d}$. Two such conditions come from the concepts of *diagonally dominant* and *scaled diagonally dominant* matrices in linear algebra. We recall these definitions below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Column generation for inner approximation of positive semidefinite cones", "weight": 1.0} -->

In this section, we describe a natural approach to apply techniques from the theory of column generation, in large-scale optimization to the problem of optimizing over nonnegative polynomials. Here is the rough idea: We can think of all SOS/SDSOS/DSOS approaches as ways of proving that a polynomial is nonnegative by writing it as a nonnegative linear combination of certain "atom" polynomials that are already known to be nonnegative. For SOS, these atoms are all the squares (there are infinitely many). For DSOS, there is actually a finite number of atoms corresponding to the extreme rays of the cone of diagonally dominant matrices (see Theorem 2.3.1. ‣ 2.3.1 LP-based column generation ‣ 2.3 Column generation for inner approximation of positive semidefinite cones ‣ Chapter 2 Optimization over Structured Subsets of Positive Semidefinite Matrices via Column Generation ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") below).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Column generation for inner approximation of positive semidefinite cones", "weight": 1.0} -->

For SDSOS, once again we have infinitely many atoms, but with a specific structure which is amenable to an SOCP representation. Now the column generation idea is to start with a certain "cheap" subset of atoms (columns) and only add new ones---one or a limited number in each iteration---if they improve our desired objective function. This results in a sequence of monotonically improving bounds; we stop the column generation procedure when we are happy with the quality of the bound, or when we have consumed a predetermined budget on time.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Column generation for inner approximation of positive semidefinite cones", "weight": 1.0} -->

In the LP case, after the addition of one or a few new atoms, one can obtain the new optimal solution from the previous solution in much less time than required to solve the new problem from scratch. However, as we show with some examples in this chapter, even if one were to resolve the problems from scratch after each iteration (as we do for all of our SOCPs and some of our LPs), the overall procedure is still relatively fast. This is because in each iteration, with the introduction of a constant number $k$ of new atoms, the problem size essentially increases only by $k$ new variables and/or $k$ new constraints. This is in contrast to other types of hierarchies---such as the rDSOS and rSDSOS hierarchies of Definition 3.2.2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Column generation for inner approximation of positive semidefinite cones", "weight": 1.0} -->

‣ 3.2.1 DSOS and SDSOS optimization ‣ 3.2 Preliminaries ‣ Chapter 3 Sum of Squares Basis Pursuit with Linear and Second Order Cone Programming ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")---that blow up in size by a factor that depends on the dimension in each iteration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Column generation for inner approximation of positive semidefinite cones", "weight": 1.0} -->

In the next two subsections we make this general idea more precise. While our focus in this section is on column generation for general SDPs, the next two sections show how the techniques are useful for approximation of SOS programs for polynomial optimization (Section 2.4), and copositive programs for discrete optimization (Section 2.5).

<!-- chunk {"id": "body-0027", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

Our goal is to inner approximate the feasible set of (2.2) by increasingly larger polyhedral sets. We consider LPs of the form

<!-- chunk {"id": "body-0028", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

Here, the matrices ${B_{1},\ldots,B_{t}} \in P_{n}$ are some fixed set of positive semidefinite matrices (our psd "atoms"). To expand our inner approximation, we will continually add to this list of matrices. This is done by considering the dual LP

<!-- chunk {"id": "body-0029", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

which in fact gives a polyhedral outer approximation (i.e., relaxation) of the spectrahedral feasible set of the SDP in (2.3). If the optimal solution $X^{\ast}$ of the LP in (2.5) is already psd, then we are done and have found the optimal value of our SDP. If not, we can use the violation of positive semidefiniteness to extract one (or more) new psd atoms $B_{j}$. Adding such atoms to (2.4) is called column generation, and the problem of finding such atoms is called the pricing subproblem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

(On the other hand, if one starts off with an LP of the form (2.5) as an approximation of (2.3), then the approach of adding inequalities to the LP iteratively that are violated by the current solution is called a cutting plane approach, and the associated problem of finding violated constraints is called the separation subproblem.) The simplest idea for pricing is to look at the eigenvectors $v_{j}$ of $X^{\ast}$ that correspond to negative eigenvalues. From each of them, one can generate a rank-one psd atom $B_{j} = {v_{j}v_{j}^{T}}$, which can be added with a new variable ("column") $\alpha_{j}$ to the primal LP in (2.4), and as a new constraint ("cut") to the dual LP in (2.5).

<!-- chunk {"id": "body-0031", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

The subproblem can then be defined as getting the most negative eigenvector, which is equivalent to minimizing the quadratic form $x^{T}X^{\ast}x$ over the unit sphere $\left. \{ x \middle| {{\| x\|} = 1}\} \right.$. Other possible strategies are discussed later in the chapter.

<!-- chunk {"id": "body-0032", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

This LP-based column generation idea is rather straightforward, but what does it have to do with DSOS optimization? The connection comes from the extreme-ray description of the cone of diagonally dominant matrices, which allows us to interpret a DSOS program as a particular and effective way of obtaining $n^{2}$ initial psd atoms.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LP-based column generation", "weight": 1.0} -->

Let $\mathcal{U}_{n,k}$ denote the set of vectors in ${\mathbb{R}}^{n}$ which have at most $k$ nonzero components, each equal to $\pm 1$, and define $U_{n,k} \subset S_{n}$ to be the set of matrices

<!-- chunk {"id": "body-0034", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

In a similar vein, we present an SOCP-based column generation algorithm that in our experience often does much better than the LP-based approach. The idea is once again to optimize over structured subsets of the positive semidefinite cone that are SOCP representable and that are larger than the set $SDD_{n}$ of scaled diagonally dominant matrices. This will be achieved by working with the following SOCP

<!-- chunk {"id": "body-0035", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

Here, the positive semidefiniteness constraints on the $2 \times 2$ matrices can be imposed via rotated quadratic cone constraints as explained in Section 3.2.1. The $n \times 2$ matrices $V_{i}$ are fixed for all $i = {1,\ldots,t}$. Note that this is a direct generalization of the LP in (2.4), in the case where the atoms $B_{i}$ are rank-one. To generate a new SOCP atom, we work with the dual of (2.6):

<!-- chunk {"id": "body-0036", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

Once again, if the optimal solution $X^{\ast}$ is psd, we have solved our SDP exactly; if not, we can use $X^{\ast}$ to produce new SOCP-based cuts. For example, by placing the two eigenvectors of $X^{\ast}$ corresponding to its two most negative eigenvalues as the columns of an $n \times 2$ matrix $V_{t + 1}$, we have produced a new useful atom. (Of course, we can also choose to add more pairs of eigenvectors and add multiple atoms.) As in the LP case, by construction, our bound can only improve in every iteration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

We will always be initializing our SOCP iterations with the SDSOS bound. It is not hard to see that this corresponds to the case where we have $\binom{n}{2}$ initial $n \times 2$ atoms $V_{i}$, which have zeros everywhere, except for a 1 in the first column in position $j$ and a 1 in the second column in position $k > j$. We denote the set of all such $n \times 2$ matrices by $\mathcal{V}_{n,2}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

The first step of our procedure is carried out already in for approximating solutions to QCQPs. Furthermore, the work in shows that for a particular class of QCQPs, its SDP relaxation and its SOCP relaxation (written respectively in the form of (2.3) and (2.7)) are exact.

<!-- chunk {"id": "body-0039", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

(a) LP starting with DSOS and adding 5 atoms.

<!-- chunk {"id": "body-0040", "role": "body", "section": "SOCP-based column generation", "weight": 1.0} -->

(b) SOCP starting with SDSOS and adding 5 atoms.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

In this section, we apply the ideas described in the previous section to sum of squares algorithms for nonconvex polynomial optimization. In particular, we consider the NP-hard problem of minimizing a form (of degree $\geq 4$) on the sphere. Recall that $z{(x,d)}$ is the vector of all monomials in $n$ variables with degree $d$. Let $p{(x)}$ be a form with $n$ variables and even degree $2d$, and let $\text{coef}{(p)}$ be the vector of its coefficients with the monomial ordering given by $z{(x,{2d})}$. Thus $p{(x)}$ can be viewed as $\text{coef}{(p)}^{T}z{(x,{2d})}$. Let $s{(x)}: = {(\sum_{i = 1}^{n}x_{i}^{2})}^{d}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

With this notation, the problem of minimizing a form $p$ on the unit sphere can be written as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

The sum of squares certificate is directly read from an eigenvalue decomposition of the solution $Y$ to the SDP above and has the form

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

where $Y = {\sum_{i}{u_{i}u_{i}^{T}}}$. Since all sos polynomials are nonnegative, the optimal value of the SDP in (2.4) is a lower bound to the optimal value of the optimization problem in (2.8). Unfortunately, before solving the SDP, we do not have access to the vectors $u_{i}$ in the decomposition of the optimal matrix $Y$. However, the fact that such vectors exist hints at how we should go about replacing $P_{n}$ by a polyhedral restriction in (2.4): If the constraint $Y \succeq 0$ is changed to

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

where $\mathcal{U}$ is a finite set, then (2.4) becomes an LP. This is one interpretation of Ahmadi and Majumdar's work in where they replace $P_{n}$ by $DD_{n}$. Indeed, this is equivalent to taking $\mathcal{U} = \mathcal{U}_{n,2}$ in (2.10), as shown in Theorem 2.3.1. ‣ 2.3.1 LP-based column generation ‣ 2.3 Column generation for inner approximation of positive semidefinite cones ‣ Chapter 2 Optimization over Structured Subsets of Positive Semidefinite Matrices via Column Generation ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming"). We are interested in extending their results by replacing $P_{n}$ by larger restrictions than $DD_{n}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nonconvex polynomial optimization", "weight": 1.0} -->

A natural candidate for example would be obtained by changing $\mathcal{U}_{n,2}$ to $\mathcal{U}_{n,3}$. However, although $\mathcal{U}_{n,3}$ is finite, it contains a very large set of vectors even for small values of $n$ and $d$. For instance, when $n = 30$ and $d = 4$, $\mathcal{U}_{n,3}$ has over 66 million elements. Therefore we use column generation ideas to iteratively expand $\mathcal{U}$ in a manageable fashion. To initialize our procedure, we would like to start with good enough atoms to have a feasible LP. The following result guarantees that replacing $Y \succeq 0$ with $Y \in {DD_{n}}$ always yields an initial feasible LP in the setting that we are interested.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments with a 10-variable quartic", "weight": 1.0} -->

We illustrate the behaviour of these different strategies on an example. Let $p{(x)}$ be a degree-four form defined on 10 variables, where the components of $\text{coef}{(p)}$ are drawn independently at random from the normal distribution $\mathcal{N}{}$. Thus $d = 2$ and $n = 10$, and the form $p{(x)}$ is 'fully dense' in the sense that $\text{coef}{(p)}$ has essentially all nonzero components. In Figure 2.2, we show how the lower bound on the optimal value of $p{(x)}$ over the unit sphere changes per iteration for different methods. The $x$-axis shows the number of iterations of the column generation algorithm, i.e., the number of times columns are added and the LP (or SOCP) is resolved. The $y$-axis shows the lower bound obtained from each LP or SOCP. Each curve represents one way of adding columns.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments with a 10-variable quartic", "weight": 1.0} -->

The three horizontal lines (from top to bottom) represent, respectively, the SDP bound, the 1SDSOS bound and the 1DSOS bound. The curve DSOS~k~ gives the bound obtained by solving LPs, where the first LP has $Y \in {DD_{n}}$ and subsequent columns are generated from a single eigenvector corresponding to the most negative eigenvalue of the dual optimal solution as described in Section 2.3.1. The LP triples curve also corresponds to an LP sequence, but this time the columns that are added are taken from $U_{n,3}$ and are more than one in each iteration (see the next subsection). This bound saturates when constraints coming from all elements of $U_{n,3}$ are satisfied. Finally, the curve SDSOS~k~ gives the bound obtained by SOCP-based column generation as explained just above.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

In this section, we consider larger problem instances ranging from 15 variables to 40 variables: these instances are again fully dense and generated in exactly the same way as the $n = 10$ example of the previous subsection. However, contrary to the previous subsection, we only apply our "triples" column generation strategy here. This is because the eigenvector-based column generation strategy is too computationally expensive for these problems as we discuss below.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

To solve the triples pricing subproblem with our partial enumeration strategy, we set $t_{1}$ to 300,000 and $t_{2}$ to 5000. Thus in each iteration, we find up to 300,000 violated triples, and add up to 5000 of them. In other words, we augment our LP by up to 5000 columns in each iteration. This is somewhat unusual as in practice at most a few dozen columns are added in each iteration. The logic for this is that primal simplex is very fast in reoptimizing an LP when a small number of additional columns are added to an LP whose optimal basis is known. However, in our context, we observed that the associated LPs are very hard for the simplex routines inside our LP solver (CPLEX 12.4) and take much more time than CPLEX's interior point solver. We therefore use CPLEX's interior point ("barrier") solver not only for the initial LP but for subsequent LPs after adding columns.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

Because interior point solvers do not benefit significantly from warm starts, each LP takes a similar amount of time to solve as the initial LP, and therefore it makes sense to add a large number of columns in each iteration to amortize the time for each expensive solve over many columns.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

Table 2.1 is taken from the work of Ahmadi and Majumdar, where they report lower bounds on the minimum value of fourth-degree forms on the unit sphere obtained using different methods, and the respective computing times (in seconds).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

Table 2.1: Comparison of optimal values in for lower bounding a quartic form on the sphere for varying dimension, along with run times (in seconds). These results are obtained on a 3.4 GHz Windows computer with 16 GB of memory.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

In Table 2.2, we give our bounds for the same problem instances. We report two bounds, obtained at two different times (if applicable). In the first case ( rows labeled R1), the time taken by 1SDSOS in Table 2.1 is taken as a limit, and we report the bound from the last column generation iteration occuring before this time limit; the 1SDSOS bound is the best non-SDP bound reported in the experiments of Ahmadi and Majumdar. In the rows labeled as R2, we take 600 seconds as a limit and report the last bound obtained before this limit. In a couple of instances ($n = 15$ and $n = 20$), our column generation algorithm terminates before the 600 second limit, and we report the termination time in this case.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

Table 2.2: Lower bounds on the optimal value of a form on the sphere for varying degrees of polynomials using Triples on a 2.33 GHz Linux machine with 32 GB of memory.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

We observe that in the same amount of time (and even on a slightly slower machine), we are able to consistently beat the 1SDSOS bound, which is the strongest non-SDP bound produced. We also experimented with the eigenvalue pricing subproblem in the LP case, with a time limit of 600 seconds. For $n = 25$, we obtain a bound of $- 23.46$ after adding only $33$ columns in 600 seconds. For $n = 40$, we are only able to add 6 columns and the lower bound obtained is $- 61.49$. Note that this bound is worse than the triples bound given in Table 2.2. The main reason for being able to add so few columns in the time limit is that each column is almost fully dense (the LPs for n=25 have 20,475 rows, and 123,410 rows for $n = 40$). Thus, the LPs obtained are very hard to solve after a few iterations and become harder with increasing $n$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Larger computational experiments", "weight": 1.0} -->

As a consequence, we did not experiment with the eigenvalue pricing subproblem in the SOCP case as it is likely to be even more computationally intensive.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

Semidefinite programming has been used extensively for approximation of NP-hard combinatorial optimization problems. One such example is finding the *stability number* of a graph. A stable set (or independent set) of a graph $G = {(V,E)}$ is a set of nodes of $G$, no two of which are adjacent. The size of the largest stable set of a graph $G$ is called the stability number (or independent set number) of $G$ and is denoted by ${\alpha{(G)}}.$ Throughout, $G$ is taken to be an undirected, unweighted graph on $n$ nodes. It is known that the problem of testing if $\alpha{(G)}$ is greater than a given integer $k$ is NP-hard. Furthermore, the stability number cannot be approximated to a factor of $n^{1 - \epsilon}$ for any $\epsilon > 0$ unless P$=$NP. The natural integer programming formulation of this problem is given by

<!-- chunk {"id": "body-0059", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

Although this optimization problem is intractable, there are several computationally-tractable relaxations that provide upper bounds on the stability number of a graph. For example, the obvious LP relaxation of (2.14)

<!-- chunk {"id": "body-0060", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

This bound can be improved upon by adding the so-called *clique inequalities* to the LP, which are of the form ${x_{i_{1}} + x_{i_{2}} + \ldots + x_{i_{k}}} \leq 1$ when nodes $(i_{1},i_{2},\ldots,i_{k})$ form a clique in $G$. Let $C_{k}$ be the set of all $k$-clique inequalities in $G$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

Notice that for ${k = 2},$ this simply corresponds to (2.15), in other words, ${LP_{2}{(G)}} = {LP{(G)}}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

In addition to LPs, there are also semidefinite programming (SDP) relaxations that provide upper bounds to the stability number.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

Here $J$ is the all-ones matrix and $I$ is the identity matrix of size $n$. The Lovász theta number is known to always give at least as good of an upper bound as the LP in (2.15), even with the addition of clique inequalities of all sizes (there are exponentially many); see, e.g., \[116, Section 6.5.2\] for a proof. In other words,

<!-- chunk {"id": "body-0064", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

An alternative SDP relaxation for stable set is due to de Klerk and Pasechnik. In, they show that the stability number can be obtained through a conic linear program over the set of copositive matrices. Namely,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

where $A$ is the adjacency matrix of $G$. Replacing $C_{n}$ by the restriction $P_{n} + N_{n}$, one obtains the aforementioned relaxation through the following SDP

<!-- chunk {"id": "body-0066", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

This latter SDP is more expensive to solve than the Lovász SDP (2.17), but the bound that it obtains is always at least as good (and sometimes strictly better). A proof of this statement is given in \[55, Lemma 5.2\], where it is shown that (2.19) is an equivalent formulation of an SDP of Schrijver, which produces stronger upper bounds than (2.17).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

Another reason for the interest in the copositive approach is that it allows for well-known SDP and LP hierarchies---developed respectively by Parrilo \[152, Section 5\] and de Klerk and Pasechnik ---that produce a sequence of improving bounds on the stability number. In fact, by appealing to Positivstellensatz results of Pólya, and Powers and Reznick, de Klerk and Pasechnik show that their LP hierarchy produces the exact stability number in $\alpha^{2}{(G)}$ number of steps \[55, Theorem 4.1\]. This immediately implies the same result for stronger hierarchies, such as the SDP hierarchy of Parrilo, or the rDSOS and rSDSOS hierarchies of Ahmadi and Majumdar.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

One notable difficulty with the use of copositivity-based SDP relaxations such as (2.19) in applications is scalibility. For example, it takes more than 5 hours to solve (2.19) when the input is a randomly generated Erdós-Renyi graph with 300 nodes and edge probability $p = 0.8$. ^33^3The solver in this case is MOSEK and the machine used has 3.4GHz speed and 16GB RAM; see Table 2.4 for more results. The solution time with the popular SDP solver SeDuMi e.g. would be several times larger. Hence, instead of using (2.19), we will solve a sequence of LPs/SOCPs generated in an iterative fashion. These easier optimization problems will provide upper bounds on the stability number in a more reasonable amount of time, though they will be weaker than the ones obtained via (2.19).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

We will derive both our LP and SOCP sequences from formulation (2.18) of the stability number. To obtain the first LP in the sequence, we replace $C_{n}$ by ${DD_{n}} + N_{n}$ (instead of replacing $C_{n}$ by $P_{n} + N_{n}$ as was done in (2.19)) and get

<!-- chunk {"id": "body-0070", "role": "body", "section": "Inner approximations of copositive programs and the maximum stable set problem", "weight": 1.0} -->

This is an LP whose optimal value is a valid upper bound on the stability number as ${DD_{n}} \subseteq P_{n}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

For many problems of discrete and polynomial optimization, there are hierarchies of SDP-based sum of squares algorithms that produce provably optimal bounds in the limit,. However, these hierarchies can often be expensive computationally. In this chapter, we were interested in problem sizes where even the first level of the hierarchy is too expensive, and hence we resorted to algorithms that replace the underlying SDPs with LPs or SOCPs. We built on the recent work of Ahmadi and Majumdar on DSOS and SDSOS optimization which serves exactly this purpose. We showed that by using ideas from linear programming column generation, the performance of their algorithms is improvable. We did this by iteratively optimizing over increasingly larger structured subsets of the cone of positive semidefinite matrices, without resorting to the more expensive rDSOS and rSDSOS hierarchies.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

There is certainly a lot of room to improve our column generation algorithms. In particular, we only experimented with a few types of pricing subproblems and particular strategies for solving them. The success of column generation often comes from good "engineering", which fine-tunes the algorithms to the problem at hand. Developing warm-start strategies for our iterative SOCPs for example, would be a very useful problem to work on in the future.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

Here is another interesting research direction, which for illustrative purposes we outline for the problem studied in Section 2.4; i.e., minimizing a form on the sphere. Recall that given a form $p$ of degree $2d$, we are trying to find the largest $\lambda$ such that ${p{(x)}} - {\lambda{({\sum_{i = 1}^{n}x_{i}^{2}})}^{d}}$ is a sum of squares. Instead of solving this sum of squares program, we looked for the largest $\lambda$ for which we could write ${p{(x)}} - \lambda$ as a conic combination of a certain set of nonnegative polynomials. These polynomials for us were always either a single square or a sum of squares of polynomials. There are polynomials, however, that are nonnegative but not representable as a sum of squares. Two classic examples, are the Motzkin polynomial

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

Either of these polynomials can be shown to be nonnegative using the arithmetic mean-geometric mean (am-gm) inequality, which states that if ${x_{1},\ldots,x_{k}} \in {\mathbb{R}}$, then

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

For example, in the case of the Motzkin polynomial, it is clear that the monomials $x^{6},{y^{4}z^{2}}$ and $y^{2}z^{4}$ are nonnegative for all ${x,y,z} \in {\mathbb{R}}$, and letting $x_{1},x_{2},x_{3}$ stand for these monomials respectively, the am-gm inequality implies that

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

These polynomials are known to be extreme in the cone of nonnegative polynomials and they cannot be written as a sum of squares (sos).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

It would be interesting to study the separation problems associated with using such non-sos polynomials in column generation. We briefly present one separation algorithm for a family of polynomials whose nonnegativity is provable through the am-gm inequality and includes the Motzkin and Choi-Lam polynomials. This will be a relatively easy-to-solve integer program in itself, whose goal is to find a polynomial $q$ amongst this family which is to be added as our new "nonnegative atom".

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

The family of $n$-variate polynomials under consideration consists of polynomials with only $k + 1$ nonzero coefficients, with $k$ of them equal to one, and one equal to $- k$. (Notice that the Motzkin and the Choi-Lam polynomials are of this form with $k$ equal to three and four respectively.) Let $m$ be the number of monomials in $p$. Given a dual vector $\mu$ of (2.4) of dimension $m$, one can check if there exists a nonnegative degree $2d$ polynomial $q{(x)}$ in our family such that ${{{\mu \cdot \text{coef}}{({q{(x)}})}} < 0}.$

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

Here, we have $\alpha_{i} \in {\mathbb{N}}^{n}$ and the variables $c_{i},y_{i}$ form the coefficients of the polynomial ${q{(x)}} = {{\sum_{i = 1}^{m}{c_{i}x^{\alpha_{i}}}} - {k{\sum_{i = 1}^{m}{y_{i}x^{\alpha_{i}}}}}}$. The above integer program has $2m$ variables, but only $n + 2$ constraints (not counting the integer constraints). If a polynomial $q{(x)}$ with a negative objective value is found, then one can add it as a new atom for column generation. In our specific randomly generated polynomial optimization examples, such polynomials did not seem to help in our preliminary experiments. Nevertheless, it would be interesting to consider other instances and problem structures.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusions and future research", "weight": 1.0} -->

Similarly, in the column generation approach to obtaining inner approximations of the copositive cone, one need not stick to positive semidefinite matrices. It is known that the $5 \times 5$ "Horn matrix" for example is extreme in the copositive cone but cannot be written as the sum of a nonnegative and a positive semidefinite matrix. One could define a separation problem for a family of Horn-like matrices and add them in a column generation approach. Exploring such strategies is left for future research.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, semidefinite programming and sum of squares optimization have proven to be powerful techniques for tackling a diverse set of problems in applied and computational mathematics. The reason for this, at a high level, is that several fundamental problems arising in discrete and polynomial optimization or the theory of dynamical systems can be cast as linear optimization problems over the cone of nonnegative polynomials. This observation puts forward the need for efficient conditions on the coefficients $c_{\alpha}: = c_{\alpha_{1},\ldots,\alpha_{n}}$ of a multivariate polynomial

<!-- chunk {"id": "body-0082", "role": "body", "section": "Introduction", "weight": 1.5} -->

being positive semidefinite and this constraint can be imposed by semidefinite programming. For higher degrees, however, imposing nonnegativity of polynomials is in general an intractable computational task. In fact, even checking if a given quartic polynomial is nonnegative is NP-hard.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Introduction", "weight": 1.5} -->

This condition is attractive for several reasons. From a computational perspective, for fixed-degree polynomials, a sum of squares decomposition can be checked (or imposed as a constraint) by solving a semidefinite program of size polynomial in the number of variables. From a representational perspective, such a decomposition *certifies* nonnegativity of $p$ in terms of an easily verifiable algebraic identity. From a practical perspective, the so-called "sum of squares relaxation" is well-known to produce powerful (often exact) bounds on optimization problems that involve nonnegative polynomials; see, e.g.,. The reason for this is that constructing examples of nonnegative polynomials that are not sums of squares in relatively low dimensions and degrees seems to be a difficult task^11^1See for explicit examples of nonnegative polynomials that are not sums of squares., especially when additional structure arising from applications is required.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have recently been interested in leveraging the attractive features of semidefinite programs (SDPs) and sum of squares (SOS) programs, while solving much simpler classes of convex optimization problems, namely *linear programs* (LPs) and *second order cone programs* (SOCPs). Such a research direction can potentially lead to a better understanding of the relative power of different classes of convex relaxations. It also has obvious practical motivations as simpler convex programs come with algorithms that have better scalability and improved numerical conditioning properties. This chapter is a step in this research direction. We present a scheme for solving a sequence of LPs or SOCPs that provide increasingly accurate approximations to the optimal value and the optimal solution of a semidefinite (or a sum of squares) program. With the algorithms that we propose, one can use one of many mature LP/SOCP solvers such as, including simplex-based LP solvers, to obtain reasonable approximations to the optimal values of these more difficult convex optimization problems.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Introduction", "weight": 1.5} -->

The intuition behind our approach is easy to describe with a contrived example. Suppose we would like to show that the degree-4 polynomial

<!-- chunk {"id": "body-0086", "role": "body", "section": "Introduction", "weight": 1.5} -->

has a sum of squares decomposition. One way to do this is to attempt to write $p$ as

<!-- chunk {"id": "body-0087", "role": "body", "section": "Introduction", "weight": 1.5} -->

is the standard (homogeneous) monomial basis of degree 2 and the matrix $Q$, often called the *Gram matrix*, is symmetric and positive semidefinite. The search for such a $Q$ can be done with semidefinite programming; one feasible solution e.g.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Introduction", "weight": 1.5} -->

Suppose now that instead of the basis $z$ in (3.1), we pick a different basis

<!-- chunk {"id": "body-0089", "role": "body", "section": "Introduction", "weight": 1.5} -->

With this new basis, we can get a sum of squares decomposition of $p$ by writing it as

<!-- chunk {"id": "body-0090", "role": "body", "section": "Introduction", "weight": 1.5} -->

In effect, by using a better basis, we have simplified the Gram matrix and made it diagonal. When the Gram matrix is diagonal, its positive semidefiniteness can be imposed as a *linear* constraint (diagonals should be nonnegative).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Introduction", "weight": 1.5} -->

Of course, the catch here is that we do not have access to the magic basis $\overset{\sim}{z}{(x)}$ in (3.2) a priori. Our goal will hence be to "pursue" this basis (or other good bases) by starting with an arbitrary basis (typically the standard monomial basis), and then iteratively improving it by solving a sequence of LPs or SOCPs and performing some efficient matrix decomposition tasks in the process. Unlike the intentionally simplified example we gave above, we will not ever require our Gram matrices to be diagonal. This requirement is too strong and would frequently lead to our LPs and SOCPs being infeasible. The underlying reason for this is that the cone of diagonal matrices is not full dimensional in the cone of positive semidefinite matrices. Instead, we will be after bases that allow the Gram matrix to be *diagonally dominant* or *scaled diagonally dominant* (see Definition 5.3.1). The use of these matrices in polynomial optimization has recently been proposed by Ahmadi and Majumdar. We will be building on and improving upon their results in this chapter.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Organization of this chapter", "weight": 1.0} -->

The organization of the rest of the chapter is as follows. In Section 3.2, we introduce some notation and briefly review the concepts of "dsos and sdsos polynomials" which are used later as the first step of an iterative algorithm that we propose in Section 3.3. In this section, we explain how we inner approximate semidefinite (Subsection 3.3.1) and sum of squares (Subsection 3.3.2) cones with LP and SOCP-based cones by iteratively changing bases. In Subsection 3.3.3, we give a different interpretation of our LPs in terms of their corner description as opposed to their facet description. Subsection 3.3.4 is about duality, which is useful for iteratively outer approximating semidefinite or sum of squares cones.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Organization of this chapter", "weight": 1.0} -->

In Section 3.4, we apply our algorithms to the Lovász semidefinite relaxation of the maximum stable set problem. It is shown numerically that our LPs and SOCPs converge to the SDP optimal value in very few iterations and outperform some other well-known LP relaxations on a family of randomly generated examples. In Section 3.5, we consider the partition problem from discrete optimization. As opposed to the stable set problem, the quality of our relaxations here is rather poor. In fact, even the sum of squares relaxation fails on some completely trivial instances. We show this empirically on random instances, and formally prove it on one representative example (Subsection 3.5.1). The reason for this failure is existence of a certain family of quartic polynomials that are nonnegative but not sums of squares.

<!-- chunk {"id": "body-0094", "role": "body", "section": "DSOS and SDSOS optimization", "weight": 1.0} -->

In recent work, Ahmadi and Majumdar introduce more scalable alternatives to SOS optimization that they refer to as *DSOS and SDSOS programs* ^22^2The work in is currently in preparation for submission; the one in is a shorter conference version of which has already appeared. The presentation of the current chapter is meant to be self-contained.. Instead of semidefinite programming, these optimization problems can be cast as linear and second order cone programs respectively. Since we will be building on these concepts, we briefly review their relevant aspects to make our chapter self-contained.

<!-- chunk {"id": "body-0095", "role": "body", "section": "DSOS and SDSOS optimization", "weight": 1.0} -->

The idea in is to replace the condition that the Gram matrix $Q$ be positive semidefinite with stronger but cheaper conditions in the hope of obtaining more efficient inner approximations to the cone $SOS_{n,d}$. Two such conditions come from the concepts of *diagonally dominant* and *scaled diagonally dominant* matrices in linear algebra. We recall these definitions below.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Pursuing improved bases", "weight": 1.0} -->

Throughout this section, we consider the standard SDP

<!-- chunk {"id": "body-0097", "role": "body", "section": "Pursuing improved bases", "weight": 1.0} -->

which we assume to have an optimal solution. We denote the optimal value by $SOS^{\ast}$ since we think of a semidefinite program as a sum of squares program over quadratic forms (recall that ${PSD_{n,2}} = {SOS_{n,2}}$). This is so we do not have to introduce additional notation to distinguish between degree-2 and higher degree SOS programs. The main goal of this section is to construct sequences of LPs and SOCPs that generate bounds on the optimal value of (3.4). Section 3.3.1 focuses on providing upper bounds on (3.4) while Section 3.3.4 focuses on lower bounds.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

To obtain upper bounds on (3.4), we need to replace the constraint $X \succeq 0$ by a stronger condition. In other words, we need to provide *inner approximations* to the set of psd matrices.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

First, let us define a family of cones

<!-- chunk {"id": "body-0100", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

parametrized by an $n \times n$ matrix $U$. Optimizing over the set $DD{(U)}$ is an LP since $U$ is fixed, and the defining constraints are linear in the coefficients of the two unknowns $M$ and $Q$. Furthermore, the matrices in $DD{(U)}$ are all psd; i.e., ${\forall U},$ ${DD{(U)}} \subseteq P_{n}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

To define the sequence $\{ U_{k}\}$, we assume that an optimal solution $X_{k}$ to (3.5) exists for every iteration. As it will become clear shortly, this assumption will be implied simply by assuming that only the first LP in the sequence is feasible. The sequence $\{ U_{k}\}$ is then given recursively by

<!-- chunk {"id": "body-0102", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

Note that the first LP in the sequence optimizes over the set of diagonally dominant matrices as in the work of Ahmadi and Majumdar. By defining $U_{k + 1}$ as a Cholesky factor of $X_{k}$, improvement of the optimal value is guaranteed in each iteration. Indeed, as $X_{k} = {U_{k + 1}^{T}IU_{k + 1}}$, and the identity matrix $I$ is diagonally dominant, we see that $X_{k} \in {DD{(U_{k + 1})}}$ and hence is feasible for iteration $k + 1$. This entails that the optimal value at iteration $k + 1$ is at least as good as the optimal value at the previous iteration; i.e., ${DSOS_{k + 1}} \leq {DSOS_{k}}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

Since the sequence $\{{DSOS_{k}}\}$ is lower bounded by $SOS^{\ast}$ and monotonic, it must converge to a limit ${DSOS^{\ast}} \geq {SOS^{\ast}}$. We have been unable to formally rule out the possibility that ${DSOS^{\ast}} > {SOS^{\ast}}$. In all of our numerical experiments, convergence to $SOS^{\ast}$ happens (i.e., ${DSOS^{\ast}} = {SOS^{\ast}}$), though the speed of convergence seems to be problem dependent (contrast e.g. the results of Section 3.4 with Section 3.5). What is easy to show, however, is that if $X_{k}$ is positive definite^33^3This would be the case whenever our inner approximation is not touching the boundary of the psd cone in the direction of the objective.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Inner approximations of the psd cone", "weight": 1.0} -->

As far as numerical computation is concerned, this is of course always the case., then the improvement from step $k$ to $k + 1$ is actually *strict*.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

A problem domain where inner approximations to semidefinite programs can be useful is in sum of squares programming. This is because the goal of SOS optimization is already to inner approximate the cone of nonnegative polynomials. So by further inner approximating the SOS cone, we will get bounds in the same direction as the SOS bounds.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

Let $z{(x)}$ be the vector of monomials of degree up to $d$. Define a family of cones of degree-$2d$ polynomials

<!-- chunk {"id": "body-0107", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

parameterized by an $n \times n$ matrix $U$. We can think of this set as the cone of polynomials that are dsos in the basis $Uz{(x)}$. If an SOS program has a constraint "$p$ sos", we will replace it iteratively by the constraint $p \in {DSOS{(U_{k})}}$. The sequence of matrices $\{ U_{k}\}$ is again defined recursively with

<!-- chunk {"id": "body-0108", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

where $Q_{k}$ is an optimal Gram matrix of iteration $k$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

This set can also be viewed as the set of polynomials that are sdsos in the basis $Uz{(x)}$. To construct a sequence of SOCPs that generate improving bounds on the sos optimal value, we replace the constraint $p$ sos by $p \in {SDSOS{(U_{k})}}$, where $U_{k}$ is defined as above.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

In Figure 3.3, we consider a parametric family of polynomials

<!-- chunk {"id": "body-0111", "role": "body", "section": "Inner approximations to the cone of nonnegative polynomials", "weight": 1.0} -->

The outermost set in both figures corresponds to the set of pairs $(a,b)$ for which $p_{a,b}$ is sos. As $p_{a,b}$ is a bivariate quartic, this set coincides with the set of $(a,b)$ for which $p_{a,b}$ is nonnegative. The innermost sets in the two subfigures correspond to $(a,b)$ for which $p_{a,b}$ is dsos (resp. sdsos). The thick blue lines illustrate the optimal points achieved when maximizing in all directions over the sets obtained from a single Cholesky decomposition. (The details of the procedure are exactly the same as Figure 3.2.) Once again, the inner approximations after one iteration improve substantially over the DSOS and SDSOS approximations.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Extreme-ray interpretation of the change of basis", "weight": 1.0} -->

In this section, we present an alternative but equivalent way of expressing the LP and SOCP-based sequences. This characterization is based on the extreme-ray description of the cone of diagonally dominant/scaled diagonally dominant matrices. It will be particularly useful when we consider outer approximations of the psd cone in Section 3.3.4.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

In Section 3.3.1, we considered inner approximations of the psd cone to obtain upper bounds on (3.4). In many applications, semidefinite programming is used as a "relaxation" to provide outer approximations to some nonconvex sets. This approach is commonly used for relaxing quadratic programs; see, e.g., Section 3.4, where we consider the problem of finding the largest stable set of a graph. In such scenarios, it does not make sense for us to inner approximate the psd cone: to have a valid relaxation, we need to outer approximate it. This can be easily achieved by working with the dual problems, which we will derive explicitly in this section.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

Since $P_{n} \subseteq {DD_{n}^{\ast}}$, the first iteration in our LP sequence for outer approximation will be

<!-- chunk {"id": "body-0115", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

By the description of the dual cone in (3.9), we know this can be equivalently written as

<!-- chunk {"id": "body-0116", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

where the $v_{i}$'s are the extreme rays of the set of diagonally dominant matrices as described in Section 3.3.3; namely, all vectors with at most two nonzero elements which are either $+ 1$ or $- 1$. Recall that when we were after inner approximations (Subsection 3.3.1), the next LP in our sequence was generated by replacing the vectors $v_{i}$ by $U^{T}v_{i}$, where the choice of $U$ was dictated by a Cholesky decomposition of an optimal solution of the previous iterate. In the outer approximation setting, we seemingly do not have access to a psd matrix that would provide us with a Cholesky decomposition. However, we can simply get this from the dual of (3.12)

<!-- chunk {"id": "body-0117", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

where $\{ U_{k}\}$ is a sequence of matrices defined recursively as

<!-- chunk {"id": "body-0118", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

This algorithm again strictly improves the objective value at each iteration. Indeed, from LP strong duality, we have

<!-- chunk {"id": "body-0119", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

and Theorem 3.3.1 applied to the dual problem states that

<!-- chunk {"id": "body-0120", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

where $V_{i}$'s are $n \times 2$ matrices containing exactly one 1 in each column, and $\{ U_{k}\}$ is a sequence of matrices defined as

<!-- chunk {"id": "body-0121", "role": "body", "section": "Outer approximations of the psd cone", "weight": 1.0} -->

where each $\Lambda_{i}$ is a $2 \times 2$ unknown symmetric matrix.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Remark 3.3.3", "weight": 1.0} -->

Let us end with some concluding remarks about our algorithm. There are other ways of improving the DSOS and SDSOS bounds. For example, Ahmadi and Majumdar propose the requirement that ${({\sum_{i = 1}^{n}x_{i}^{2}})}^{r}p{(x)}$ be dsos or sdsos as a sufficient condition for nonnegativity of $p$. As $r$ increases, the quality of approximation improves, although the problem size also increases very quickly. Such hierarchies are actually commonly used in the sum of squares optimization literature. But unlike our approach, they do not take into account a particular objective function and may improve the inner approximation to the PSD cone in directions that we do not care about. Nevertheless, these hierarchies have interesting theoretical implications. Under some assumptions, one can prove that as $r\rightarrow\infty$, the underlying convex programs succeed in optimizing over the entire set of nonnegative polynomials; see, e.g.,.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Remark 3.3.3", "weight": 1.0} -->

Another approach to improve on the DSOS and SDSOS bounds appears in Chapter LABEL:chap:bp. We show there how ideas from column generation in large-scale integer and linear programming can be used to iteratively improve inner approximations to semidefinite cones. The LPs and SOCPs proposed in that work take the objective function into account and increase the problem size after each iteration by a moderate amount. By contrast, the LPs and SOCPs coming from our Cholesky decompositions in this chapter have exactly the same size in each iteration. We should remark however that the LPs from iteration two and onwards are typically more dense than the initial LP (for DSOS) and slower to solve. A worthwhile future research direction would be to systematically compare the performance of the two approaches and to explore customized solvers for the LPs and the SOCPs that arise in our algorithms.

<!-- chunk {"id": "body-0124", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

A classic problem in discrete optimization is that of finding the stability number of a graph. The graphs under our consideration in this section are all undirected and unweighted. A *stable set* (or *independent set*) of a graph $G = {(V,E)}$ is a set of nodes of $G$ no two of which are adjacent. The stability number of $G$, often denoted by $\alpha{(G)}$, is the size of its maximum stable set(s). The problem of determining $\alpha$ has many applications in scheduling (see, e.g., ) and coding theory. As an example, the maximum number of final exams that can be scheduled on the same day at a university without requiring any student to take two exams is given by the stability number of a graph. This graph has courses IDs as nodes and an edge between two nodes if and only if there is at least one student registered in both courses. Unfortunately, the problem of testing whether $\alpha{(G)}$ is greater than a given integer $k$ is well known to be NP-complete.

<!-- chunk {"id": "body-0125", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Furthermore, the stability number cannot be approximated within a factor ${|V|}^{1 - \epsilon}$ for any $\epsilon > 0$ unless P$=$NP.

<!-- chunk {"id": "body-0126", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

A straightforward integer programming formulation of $\alpha{(G)}$ is given by

<!-- chunk {"id": "body-0127", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Solving this LP results in an upper bound on the stability number. The quality of this upper bound can be improved by adding the so-called *clique inequalities*. The set of $k$-clique inequalities, denoted by $C_{k}$, is the set of constraints of the type ${x_{i_{1}} + x_{i_{2}} + \ldots + x_{i_{k}}} \leq 1$, if $(i_{1},\ldots,i_{k})$ form a clique (i.e., a complete subgraph) of $G$. Observe that these inequalities must be satisfied for binary solutions to the above LP, but possibly not for fractional ones.

<!-- chunk {"id": "body-0128", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Note that ${LP} = {LP^{2}}$ by construction and ${\alpha{(G)}} \leq {LP^{k + 1}} \leq {LP^{k}}$ for all $k$. We will be comparing the bound obtained by some of these well-known LPs with those achieved via the new LPs that we propose further below.

<!-- chunk {"id": "body-0129", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

where $J$ here is the all ones matrix and $I$ is the identity matrix. The optimal value $\vartheta{(G)}$ is called the Lovász theta number of the graph. We have the following inequalities

<!-- chunk {"id": "body-0130", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

The fact that ${\alpha{(G)}} \leq {\vartheta{(G)}}$ is easily seen by noting that if $S$ is a stable set of maximum size and $1_{S}$ is its indicator vector, then the rank-one matrix $\frac{1}{|S|}1_{S}1_{S}^{T}$ is feasible to the SDP and gives the objective value $|S|$. The other inequality states that this SDP-based bound is stronger than the aforementioned LP bound even with all the clique inequalities added (there are exponentially many). A proof can be found e.g. in \[116, Section 6.5.2\].

<!-- chunk {"id": "body-0131", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Our goal here is to obtain LP and SOCP based sequences of upper bounds on the Lovász theta number. To do this, we construct a series of outer approximations of the set of psd matrices as described in Section 3.3.4.

<!-- chunk {"id": "body-0132", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

In view of (3.9), this LP can be equivalently written as

<!-- chunk {"id": "body-0133", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

where $v_{i}$ is a vector with at most two nonzero entries, each nonzero entry being either $+ 1$ or $- 1$. This LP is always feasible (e.g., with $X = {\frac{1}{n}I}$). Furthermore, it is bounded above. Indeed, the last constraints in (3.15) imply in particular that for all $i,j$, we must have

<!-- chunk {"id": "body-0134", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

This, together with the constraint ${I \cdot X} = 1$, implies that the objective $J \cdot X$ must remain bounded. As a result, the first LP in our iterative sequence will give a finite upper bound on $\alpha$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

To progress to the next iteration, we will proceed as described in Section 3.3.4. The new basis for solving the problem is obtained through the dual^44^4The reader should not be confused to see both the primal and the dual as maximization problems. We can make the dual a minimization problem by changing the sign of $y$. of (3.15):

<!-- chunk {"id": "body-0136", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

The second constraint in this problem is equivalent to requiring that ${{yI} + Y} - J$ be dd. We can define

<!-- chunk {"id": "body-0137", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

where $(y_{1}^{\ast},Y_{1}^{\ast})$ are optimal solutions to (3.16). We then solve

<!-- chunk {"id": "body-0138", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

to obtain our next iterate. The idea remains exactly the same for a general iterate $k$: We construct the dual

<!-- chunk {"id": "body-0139", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

where $(y_{k}^{\ast},Y_{k}^{\ast})$ is an optimal solution to the dual. The updated primal is then

<!-- chunk {"id": "body-0140", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

As stated in Section 3.3.4, the optimal values of (3.17) are guaranteed to strictly improve as a function of $k$. Note that to get the bounds, we can just work with the dual problems throughout.

<!-- chunk {"id": "body-0141", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

An analoguous technique can be used to obtain a sequence of SOCPs. For the initial iterate, instead of requiring that $X \in {DD^{\ast}}$ in (3.15), we require that $X \in {SDD^{\ast}}$. This problem must also be bounded and feasible as

<!-- chunk {"id": "body-0142", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Then, for a given iterate $k$, the algorithm consists of solving

<!-- chunk {"id": "body-0143", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

where as explained in Section 3.3.3 each $V_{i}$ is an $n \times 2$ matrix whose columns contain exactly one nonzero element which is equal to $1$. The matrix $U_{k}$ here is fixed and obtained by first constructing the dual SOCP

<!-- chunk {"id": "body-0144", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

(each $\Lambda_{i}$ is a symmetric $2 \times 2$ matrix decision variable) and then taking

<!-- chunk {"id": "body-0145", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Once again, one can just work with the dual problems to obtain the bounds.

<!-- chunk {"id": "body-0146", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

As our first example, we apply both techniques to the problem of finding the stability number of the complement of the Petersen graph (see Figure 3.4(a)). The exact stability number here is 2 and an example of a maximum stable set is illustrated by the two white nodes in Figure 3.4(a). The Lovász theta number is 2.5 and has been represented by the continuous line in Figure 3.4(b). The dashed lines represent the optimal values of the LP and SOCP-based sequences of approximations for 7 iterations. Notice that already within one iteration, the optimal values are within one unit of the true stability number, which is good enough for knowing the exact bound (the stability number is an integer). From the fifth iteration onwards, they differ from the Lovász theta number by only $10^{- 2}$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

(b) The Lovász theta number and iterative bounds bounds obtained by LP and SOCP

<!-- chunk {"id": "body-0148", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Finally, in Table 3.1, we have generated 100 instances of 20-node Erdös-Rényi graphs with edge probability $0.5$. For each instance, we compute the bounds from the Lovász SDP, the standard LP in (3.13), the standard LP with all 3-clique inequalities added ($LP^{3}$ in (3.14)), and our LP/SOCP iterative sequences. We focus here on iterations 3,4 and 5 because there is no need to go further. We compare our bounds with the standard LP and the standard LP with 3-clique inequalities because they are LPs of roughly the same size. If any of these bounds are within one unit of the true stable set number, we count this as a success and increment the counter. As can be seen in Table 3.1, the Lovász theta number is always within a unit of the stable set number, and so are our LP and SOCP sequences (${DSOS_{k}},{SDSOS_{k}}$) after four or at most five iterations.

<!-- chunk {"id": "body-0149", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

If we look just at the bound after 3 iterations, the success rate of SDSOS is noticeably higher than the success rate of DSOS. Also note that the standard LP with or without the three clique inequalities never succeeds in giving a bound within one unit of $\alpha{(G)}$.^55^5All numerical experiments in this chapter have been parsed using either SPOT or YAMIP and solved using the LP/SOCP/SDP solver of MOSEK.

<!-- chunk {"id": "body-0150", "role": "body", "section": "The maximum stable set problem", "weight": 1.0} -->

Table 3.1: Percentage of instances out of 100 where the bound obtained is less than a unit away from the stability number

<!-- chunk {"id": "body-0151", "role": "body", "section": "Partition", "weight": 1.0} -->

The partition problem is arguably the simplest NP-complete problem to state: Given a list of positive integers $a_{1},\ldots,a_{n}$, is it possible to split them into two sets with equal sums? We say that a partition instance is feasible if the answer is yes (e.g., {5,2,1,6,3,8,5,4,1,1,10}) and infeasible if the answer is no (e.g., {47,20,13,15,36,7,46}). The partition problem is NP-complete but only weakly. In fact, the problem admits a pseudopolynomial time algorithm based on dynamic programming that can deal with rather large problem sizes efficiently. This algorithm has polynomial running time on instances where the bit size of the integers $a_{i}$ are bounded by a polynomial in $\log n$. In this section, we investigate the performance and mostly limitations of algebraic techniques for refuting feasibility of partition instances.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Partition", "weight": 1.0} -->

Feasibility of a partition instance can always be certified by a short proof (the partition itself). However, unless P=co-NP, we do not expect to always have short certificates of infeasibility. Nevertheless, we can try to look for such a certificate through a sum of squares decomposition. Indeed, given an instance $a: = {\{ a_{1},\ldots,a_{n}\}}$, it is not hard to see^66^6 This equivalence is apparent in view of the zeros of the polynomial on the right hand side of (3.18) corresponding to a feasible partition.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Partition", "weight": 1.0} -->

So if for some $\epsilon > 0$ we could prove that ${p_{a}{(x)}} - \epsilon$ is nonnegative, we would have refuted the feasibility of our partition instance.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Failure of the sum of squares relaxation on trivial partition instances", "weight": 1.0} -->

For complexity reasons, one would expect there to be infeasible instances of partition that are not sos-refutable. What is surprising however is that the sos relaxation is failing on many instances that are totally trivial to refute as the sum of their input integers is odd. We present a proof of this phenomenon on an instance which is arguably the simplest one.^88^8If we were to instead consider the instance, sos would succeed in refuting it.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Open problems", "weight": 1.0} -->

We showed in the previous subsection that the infeasible partition instance $\{ 1,1,1,1,1\}$ was not sos-refutable. Many more randomly-generated partition instances that we knew to be infeasible (their sum being odd) also failed to be sos-refutable.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Open Problem 1", "weight": 1.0} -->

Characterize the set of partition instances $\{ a_{1},\ldots,a_{n}\}$ that have an odd sum but are not sos-refutable (see Definition 3.5.1).

<!-- chunk {"id": "body-0157", "role": "body", "section": "Open Problem 1", "weight": 1.0} -->

Our second open problem has to do with the power of higher order sos relaxations for refuting feasibility of partition instances.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Open Problem 2", "weight": 1.0} -->

For a positive integer $r$, let us call a partition instance $\{ a_{1},\ldots,a_{n}\}$ *$r$-sos-refutable* if ${\exists\epsilon} > 0$ such that ${({{p{(x)}} - \epsilon})}{({{\sum_{i}x_{i}^{2}} + 1})}^{r}$ is sos. Note that this is also a certificate of infeasibility of the instance. Even though the $\{ 1,1,1,1,1\}$ instance is not sos-refutable, it is $1$-sos-refutable. Furthermore, we have numerically observed that the instance $\{ 1,1,1,1,1,1,1\}$ (vector of all ones of length 7) is not sos-refutable or $1$-sos-refutable, but it is $2$-sos-refutable.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Open Problem 2", "weight": 1.0} -->

If we consider the instance consisting of $n$ ones with $n$ odd, and define $\overset{\sim}{r}$ to be the minimum $r$ such that $\{ 1,1,\ldots,1\}$ becomes $r$-sos-refutable, is it true that $\overset{\sim}{r}$ must grow with $n$?

<!-- chunk {"id": "body-0160", "role": "body", "section": "Introduction", "weight": 1.5} -->

A polynomial optimization problem (POP) is an optimization problem of the form

<!-- chunk {"id": "body-0161", "role": "body", "section": "Introduction", "weight": 1.5} -->

where ${{{p,g_{i},i} = 1},{\ldots,m}},$ are polynomial functions in $n$ variables $x: = {(x_{1},\ldots,x_{n})}$ and with real coefficients. It is well-known that polynomial optimization is a hard problem to solve in general. For example, simply testing whether the optimal value of problem (4.1) is smaller than or equal to some rational number $k$ is NP-hard already when the objective is quadratic and the constraints are linear. Nevertheless, these problems remain topical due to their numerous applications throughout engineering, operations research, and applied mathematics (see, e.g., ). In this chapter, we are interested in obtaining lower bounds on the optimal value of problem (4.1). We focus on a class of methods which construct hierarchies of tractable convex optimization problems whose optimal values are lowerbounds on the optimal value of (4.1), with convergence to it as the sequence progresses.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Introduction", "weight": 1.5} -->

This implies that even though the original POP is nonconvex, one can obtain increasingly accurate lower bounds on its optimal value by solving convex optimization problems. One method for constructing these hierarchies of optimization problems that has gained attention in recent years relies on the use of *Positivstellensätze* (see, e.g., for a survey). Positivstellensätze are algebraic identities that certify infeasibility of a set of polynomial inequalities, or equivalently^11^1Note that the set $\left. \{{x \in {\mathbb{R}}^{n}} \middle| {{{g_{1}{(x)}} \geq {0,\ldots}},{{g_{m}{(x)}} \geq 0}}\} \right.$ is empty if and only if ${- {g_{1}{(x)}}} > 0$ on the set $\left.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Introduction", "weight": 1.5} -->

\{{x \in {\mathbb{R}}^{n}} \middle| {{{g_{2}{(x)}} \geq {0,\ldots}},{{g_{m}{(x)}} \geq 0}}\} \right.$., positivity of a polynomial on a basic semialgebraic set. (Recall that a basic semialgebraic set is a set defined by finitely many polynomial inequalities.) These Positivstellensätze can be used to prove lowerbounds on POPs. Indeed, if we denote the feasible set of (4.1) by $S$, the optimal value of problem (4.1) is equivalent to

<!-- chunk {"id": "body-0164", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence if $\gamma$ is a strict lower bound on (4.1), we have that ${{p{(x)}} - \gamma} > 0$ on $S$, a fact that can be certified using Positivstellensätze. At a conceptual level, hierarchies that provide lower bounds on (4.1) are constructed thus: we fix the "size of the certificate" at each level of the hierarchy and search for the largest $\gamma$ such that the Positivstellensätze at hand can certify positivity of ${p{(x)}} - \gamma$ over $S$ with a certificate of this size. As the sequence progresses, we increase the size of the certificates allowed, hence obtaining increasingly accurate lower bounds on (4.1).

<!-- chunk {"id": "body-0165", "role": "body", "section": "Introduction", "weight": 1.5} -->

Below, we present three of the better-known Positivstellensätze, given respectively by Stengle, Schmüdgen, and Putinar. These all rely on sum of squares certificates. We recall that a polynomial is a *sum of squares* (sos) if it can be written as a sum of squares of other polynomials. We start with Stengle's Positivstellensatz, which certifies infeasibility of a set of polynomial inequalities. It is sometimes referred to as "the Positivstellensatz" in related literature as it requires no assumptions, contrarily to Schmüdgen and Putinar's theorems which can be viewed as refinements of Stengle's result under additional assumptions.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Outline of the chapter", "weight": 1.0} -->

The chapter is structured as follows. In Section 4.2, we show that if one can inner approximate the cone of positive definite forms arbitrarily well (with certain basic properties), then one can produce a converging hierarchy of lower bounds for POPs with compact feasible sets (Theorem 4.2.4). This relies on a reduction (Theorem 4.2.1) that reduces the problem of certifying a strict lower bound on a POP to that of proving positivity of a certain form. In Section 4.3, we see how this result can be used to derive semidefinite programming-based converging hierarchies (Theorems 4.3.2 and 4.3.4) from the Positivstellensätze by Artin (Theorem 6.4.2. ‣ 6.4.2 Sum of squares polynomials and semidefinite programming review ‣ 6.4 Semidefinite programming-based approximations of polynomial norms ‣ Chapter 6 Polynomials Norms ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")) and Reznick (Theorem 4.1.5.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Outline of the chapter", "weight": 1.0} -->

‣ 4.1 Introduction ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")). In Section 4.4, we derive an optimization-free hierarchy (Theorem 4.4.1) from the Positivstellensatz of Polyá (Theorem 4.1.6. ‣ 4.1 Introduction ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")) as well as LP and SOCP-based hierarchies which rely on dsos/sdsos polynomials (Corollary 4.4.8). We conclude with a few open problems in Section 4.5.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Constructing converging hierarchies for POP using global certificates of positivity", "weight": 1.0} -->

Consider the polynomial optimization problem in (4.1) and denote its optimal value by $p^{\ast}$. Let $d$ be such that $2d$ is the smallest even integer larger than or equal to the maximum degree of ${{p,g_{i},i} = 1},{\ldots,m}$. We denote the feasible set of our optimization problem by

<!-- chunk {"id": "body-0169", "role": "body", "section": "Constructing converging hierarchies for POP using global certificates of positivity", "weight": 1.0} -->

and assume that $S$ is contained within a ball of radius $R$. From this, it is easy to provide (possibly very loose) upper bounds on $g_{i}{(x)}$ over the set $S$: as $S$ is contained in a ball of radius $R$, we have ${|x_{i}|} \leq R$, for all $i = {1,\ldots,n}$. We then use this to upper bound each monomial in $g_{i}$ and consequently $g_{i}$ itself. We use the notation $\eta_{i}$ to denote these upper bounds, i.e., ${g_{i}{(x)}} \leq \eta_{i}$, for all $i = {1,\ldots,m}$ and for all $x \in S$. Similarly, we can provide an upperbound on $- {p{(x)}}$.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Constructing converging hierarchies for POP using global certificates of positivity", "weight": 1.0} -->

The goal of this section is to produce a method for constructing converging hierarchies of lower bounds for POPs if we have access to arbitrarily accurate inner approximations of the set of positive definite forms. The first theorem (Theorem 4.2.1) connects lower bounds on (4.1) to positive definiteness of a related form. The second theorem (Theorem 4.2.4) shows how this can be used to derive a hierarchy for POPs.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Remark 4.2.2", "weight": 1.0} -->

Note that Theorem 4.2.1 implies that testing feasibility of a set of polynomial inequalities is no harder than checking whether a homogeneous polynomial that is sos has a zero. Indeed, as mentioned before, the basic semialgebraic set

<!-- chunk {"id": "body-0172", "role": "body", "section": "Remark 4.2.2", "weight": 1.0} -->

is empty if and only if $\gamma = 0$ is a strict lower bound on the POP

<!-- chunk {"id": "body-0173", "role": "body", "section": "Remark 4.2.2", "weight": 1.0} -->

In principle, this reduction can open up new possibilities for algorithms for testing feasibility of a basic semialgebraic set. For example, the work in shows that positive definiteness of a form $f$ is equivalent to global asymptotic stability of the polynomial vector field ${\overset{˙}{x} = {- {{\nabla f}{(x)}}}}.$ One could as a consequence search for Lyapunov functions, as is done in \[2, Example 2.1.\], to certify positivity of forms. Conversely, simulating trajectories of the above vector field can be used to minimize $f$ and potentially find its nontrivial zeros, which, by our reduction, can be turned into a point that belongs to the basic semialgebraic set at hand.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Remark 4.2.2", "weight": 1.0} -->

We further remark that one can always take the degree of the sos form $f_{\gamma}$ in (4.3) whose positivity is under consideration to be equal to four. This can be done by changing the general POP in (4.1) to only have quadratic constraints and a quadratic objective via an iterative introduction of new variables and new constraints in the following fashion: $x_{ij} = {x_{i}x_{j}}$.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Remark 4.2.3 (Notational remark)", "weight": 1.0} -->

As a consequence of Theorem 4.2.1, we now know that certifying lower bounds on (4.1) is equivalent to proving positivity of the form $f_{\gamma}$ that appears in (4.3). To simplify notation, we take this form to have $n$ variables and be of degree $2d$ from now on (except for our Positivstellensätze in Corollaries 4.3.5. ‣ 4.3 Semidefinite programming-based hierarchies obtained from Artin’s and Reznick’s Positivstellensätze ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") and 4.4.5.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Remark 4.2.3 (Notational remark)", "weight": 1.0} -->

‣ 4.4.1 An optimization-free hierarchy of lower bounds for POPs ‣ 4.4 Polyá’s theorem and hierarchies for POPs that are optimization-free, LP-based, and SOCP-based ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") which stand on their own). To connect back to problem (4.1)

<!-- chunk {"id": "body-0177", "role": "body", "section": "Remark 4.2.3 (Notational remark)", "weight": 1.0} -->

Recall that $n$ was previously the dimension of the decision variable of problem (4.1), $d$ was such that $2d$ is the smallest even integer larger than or equal to the maximum degree of $g_{i}$ and $p$ in (4.1), and $m$ was the number of constraints of problem (4.1).

<!-- chunk {"id": "body-0178", "role": "body", "section": "Remark 4.2.3 (Notational remark)", "weight": 1.0} -->

Our next theorem shows that, modulo some technical assumptions, if one can inner approximate the set of positive definite forms arbitrarily well (conditions (a) and (b)), then one can construct a converging hierarchy for POPs.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Remark 4.2.5", "weight": 1.0} -->

Note that condition (d) is subsumed by the more natural condition that $K_{n,d}^{r}$ be a convex cone for any ${n,d},$ and $r$. However, there are interesting and relevant cones which we cannot prove to be convex though they trivially satisfy condition (d) (see Theorem 4.3.2 for an example).

<!-- chunk {"id": "body-0180", "role": "body", "section": "Semidefinite programming-based hierarchies obtained from Artin's and Reznick's Positivstellensätze", "weight": 1.0} -->

In this section, we construct two different semidefinite programming-based hierarchies for POPs using Positivstellensätze derived by Artin (Theorem 6.4.2. ‣ 6.4.2 Sum of squares polynomials and semidefinite programming review ‣ 6.4 Semidefinite programming-based approximations of polynomial norms ‣ Chapter 6 Polynomials Norms ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")) and Reznick (Theorem 4.1.5. ‣ 4.1 Introduction ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming")). To do this, we introduce two sets of cones that we call the Artin and Reznick cones.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Remark 4.3.3", "weight": 1.0} -->

To solve a fixed level $r$ of the hierarchy given in Theorem 4.3.2, one must proceed by *bisection* on $\gamma.$ Bisection here would produce a sequence of upper bounds $\{ U_{k}\}$ and lower bounds $\{ L_{k}\}$ on $l_{r}$ as follows. At iteration $k$, we test whether $\gamma = \frac{U_{k} + L_{k}}{2}$ is feasible for (4.7). If it is, then we take $L_{k + 1} = \frac{U_{k} + L_{k}}{2}$ and $U_{k + 1} = U_{k}$. If it is not, we take $U_{k + 1} = \frac{U_{k} + L_{k}}{2}$ and $L_{k + 1} = L_{k}$.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Remark 4.3.3", "weight": 1.0} -->

Hence, solving the $r^{th}$ level of this hierarchy using bisection can be done by semidefinite programming. Indeed, for a fixed $r$ and $\gamma$ given by the bisection algorithm, one simply needs to test membership of

<!-- chunk {"id": "body-0183", "role": "body", "section": "Remark 4.3.3", "weight": 1.0} -->

to the set of sum of squares polynomials. This amounts to solving a semidefinite program. We remark that all semidefinite programming-based hierarchies available only produce an approximate solution to the optimal value of the SDP solved at level $r$ in polynomial time. This is independent of whether they use bisection (e.g., such as the hierarchy given in Theorem 4.3.2 or the one based on Stengle's Positivstellensatz) or not (e.g., the Lasserre hierarchy).

<!-- chunk {"id": "body-0184", "role": "body", "section": "Remark 4.3.3", "weight": 1.0} -->

Our next theorem improves on our previous hierarchy by freeing the multiplier ${({\sum_{i = 1}^{n}z_{i}^{2}})}^{r}$ and taking advantage of our ability to search for an optimal multiplier using semidefinite programming.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Polyá's theorem and hierarchies for POPs that are optimization-free, LP-based, and SOCP-based", "weight": 1.0} -->

In this section, we use a result by Polyá on global positivity of even forms to obtain new hierarchies for polynomial optimization problems. In Section 4.4.1, we present a hierarchy that is *optimization-free*, in the sense that each level of the hierarchy only requires multiplication of two polynomials and checking if the coefficients of the resulting polynomial are nonnegative. In Section 4.4.2, we use the previous hierarchy to derive linear programming and second-order cone programming-based hierarchies with faster convergence. These rely on the recently developed concepts of dsos and sdsos polynomials (see Definition 4.4.7.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Polyá's theorem and hierarchies for POPs that are optimization-free, LP-based, and SOCP-based", "weight": 1.0} -->

‣ 4.4.2 Linear programming and second-order cone programming-based hierarchies for POPs ‣ 4.4 Polyá’s theorem and hierarchies for POPs that are optimization-free, LP-based, and SOCP-based ‣ Chapter 4 On the Construction of Converging Hierarchies for Polynomial Optimization Based on Certificates of Global Positivity ‣ Part I LP, SOCP, and Optimization-Free Approaches to Semidefinite and Sum of Squares Programming ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") and ), which are alternatives to sos polynomials that have been used in diverse applications to improve scalability; see \[9, Section 4\].

<!-- chunk {"id": "body-0187", "role": "body", "section": "Linear programming and second-order cone programming-based hierarchies for POPs", "weight": 1.0} -->

In this section, we present a linear programming and a second-order cone programming-based hierarchy for general POPs which by construction converge faster than the hierarchy presented in Section 4.4.1. These hierarchies are based on the recently-introduced concepts of dsos and sdsos polynomials which we briefly revisit below to keep the presentation self-contained.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Open problems", "weight": 1.0} -->

To conclude, we present two open problems spawned by the writing of this chapter. The first one concerns the assumptions needed to construct our hierarchies.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Open problem 1", "weight": 1.0} -->

Theorems 4.2.1 and 4.2.4 require that the feasible set $S$ of the POP given in (4.1) be contained in a ball of radius $R$. Can these theorems be extended to the case where there is no compactness assumption on $S$?

<!-- chunk {"id": "body-0190", "role": "body", "section": "Open problem 1", "weight": 1.0} -->

The second open problem is linked to the Artin and Reznick cones presented in Definition 4.3.1.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Open problem 2", "weight": 1.0} -->

As mentioned before, Reznick cones $R_{n,{2d}}^{r}$ are convex for all $r$. We are unable to prove however that Artin cones $A_{n,{2d}}^{r}$ are convex (even though they satisfy properties (a)-(d) of Theorem 4.2.4 like Reznick cones do). Are Artin cones convex for all $r$? We know that they are convex for $r = 0$ and for $r$ large enough as they give respectively the sos and psd cones (see for the latter claim). However, we do not know the answer already for $r = 1$.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Introduction", "weight": 1.5} -->

A difference of convex (dc) program is an optimization problem of the form

<!-- chunk {"id": "body-0193", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $f_{0},\ldots,f_{m}$ are difference of convex functions; i.e.,

<!-- chunk {"id": "body-0194", "role": "body", "section": "Introduction", "weight": 1.5} -->

and $g_{i}:{{\mathbb{R}}^{n}\rightarrow{{\mathbb{R}},h_{i}}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are convex functions. The class of functions that can be written as a difference of convex functions is very broad containing for instance all functions that are twice continuously differentiable,. Furthermore, any continuous function over a compact set is the uniform limit of a sequence of dc functions; see, e.g., reference where several properties of dc functions are discussed.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization problems that appear in dc form arise in a wide range of applications. Representative examples from the literature include machine learning and statistics (e.g., kernel selection, feature selection in support vector machines, sparse principal component analysis, and reinforcement learning ), operations research (e.g., packing problems and production-transportation problems ), communications and networks circuit design, finance and game theory, and computational chemistry. We also observe that dc programs can encode constraints of the type $x \in {\{ 0,1\}}$ by replacing them with the dc constraints ${0 \leq x \leq 1},{{x - x^{2}} \leq 0}$. This entails that any binary optimization problem can in theory be written as a dc program, but it also implies that dc problems are hard to solve in general.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Introduction", "weight": 1.5} -->

As described, there are essentially two schools of thought when it comes to solving dc programs. The first approach is global and generally consists of rewriting the original problem as a concave minimization problem (i.e., minimizing a concave function over a convex set; see, ) or as a reverse convex problem (i.e., a convex problem with a linear objective and one constraint of the type ${h{(x)}} \geq 0$ where $h$ is convex). We refer the reader to for an explanation on how one can convert a dc program to a reverse convex problem, and to for more general results on reverse convex programming. These problems are then solved using branch-and-bound or cutting plane techniques (see, e.g., or ). The goal of these approaches is to return global solutions but their main drawback is scalibility. The second approach by contrast aims for local solutions while still exploiting the dc structure of the problem by applying the tools of convex analysis to the two convex components of a dc decomposition.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Introduction", "weight": 1.5} -->

One such algorithm is the Difference of Convex Algorithm (DCA) introduced by Pham Dinh Tao in and expanded on by Le Thi Hoai An and Pham Dinh Tao. This algorithm exploits the duality theory of dc programming and is popular because of its ease of implementation, scalability, and ability to handle nonsmooth problems.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case where the functions $g_{i}$ and $h_{i}$ in (5.2) are differentiable, DCA reduces to another popular algorithm called the Convex-Concave Procedure (CCP). The idea of this technique is to simply replace the concave part of $f_{i}$ (i.e., $- h_{i}$) by a linear overestimator as described in Algorithm 1. By doing this, problem (5.1) becomes a convex optimization problem that can be solved using tools from convex analysis. The simplicity of CCP has made it an attractive algorithm in various areas of application. These include statistical physics (for minimizing Bethe and Kikuchi free energy functions ), machine learning and image processing, just to name a few. In addition, CCP enjoys two valuable features: (i) if one starts with a feasible solution, the solution produced after each iteration remains feasible, and (ii) the objective value improves in every iteration, i.e., the method is a descent algorithm.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proof of both claims readily comes out of the description of the algorithm and can be found, e.g., in \[123, Section 1.3.\], where several other properties of the method are also laid out. Like many iterative algorithms, CCP relies on a stopping criterion to end. This criterion can be chosen amongst a few alternatives. For example, one could stop if the value of the objective does not improve enough, or if the iterates are too close to one another, or if the norm of the gradient of $f_{0}$ gets small.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Introduction", "weight": 1.5} -->

3:while stopping criterion not satisfied do
5: Solve convex subroutine: min f0k (x), s.t. fik (x) ≤ 0, i = 1, …, m
6: $x_{k + 1}: = \underset{{f_{i}^{k}{(x)}}\leq 0}{\text{argmin}}f_{0}^{k}{(x)}$

<!-- chunk {"id": "body-0201", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convergence results for CCP can be derived from existing results found for DCA, since CCP is a subcase of DCA as mentioned earlier. But CCP can also be seen as a special case of the family of majorization-minimization (MM) algorithms. Indeed, the general concept of MM algorithms is to iteratively upperbound the objective by a convex function and then minimize this function, which is precisely what is done in CCP. This fact is exploited by Lanckriet and Sriperumbudur in and Salakhutdinov et al. in to obtain convergence results for the algorithm, showing, e.g., that under mild assumptions, CCP converges to a stationary point of the optimization problem (5.1).

<!-- chunk {"id": "body-0202", "role": "body", "section": "Motivation and organization of the chapter", "weight": 1.0} -->

Although a wide range of problems already appear in dc form (5.2), such a decomposition is not always available. In this situation, algorithms of dc programming, such as CCP, generally fail to be applicable. Hence, the question arises as to whether one can (efficiently) compute a difference of convex decomposition (dcd) of a given function. This challenge has been raised several times in the literature. For instance, Hiriart-Urruty states "All the proofs \[of existence of dc decompositions\] we know are "constructive" in the sense that they indeed yield \[$g_{i}$\] and \[$h_{i}$\] satisfying (5.2) but could hardly be carried over \[to\] computational aspects". As another example, Tuy writes: "The dc structure of a given problem is not always apparent or easy to disclose, and even when it is known explicitly, there remains for the problem solver the hard task of bringing this structure to a form amenable to computational analysis."

<!-- chunk {"id": "body-0203", "role": "body", "section": "Motivation and organization of the chapter", "weight": 1.0} -->

Ideally, we would like to have not just the ability to find one dc decomposition, but also to optimize over the set of valid dc decompositions. Indeed, dc decompositions are not unique: Given a decomposition $f = {g - h}$, one can produce infinitely many others by writing ${f = {{g + p} - {({h + p})}}},$ for any convex function $p$. This naturally raises the question whether some dc decompositions are better than others, for example for the purposes of CCP.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Motivation and organization of the chapter", "weight": 1.0} -->

In this chapter we consider these decomposition questions for multivariate polynomials. Since polynomial functions are finitely parameterized by their coefficients, they provide a convenient setting for a computational study of the dc decomposition questions. Moreover, in most practical applications, the class of polynomial functions is large enough for modeling purposes as polynomials can approximate any continuous function on compact sets with arbitrary accuracy. It could also be interesting for future research to explore the potential of dc programming techniques for solving the polynomial optimization problem. This is the problem of minimizing a multivariate polynomial subject to polynomial inequalities and is currently an active area of research with applications throughout engineering and applied mathematics. In the case of quadratic polynomial optimization problems, the dc decomposition approach has already been studied,.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Motivation and organization of the chapter", "weight": 1.0} -->

With these motivations in mind, we organize the chapter as follows. In Section 5.2, we start by showing that unlike the quadratic case, the problem of testing if two given polynomials $g,h$ form a valid dc decomposition of a third polynomial $f$ is NP-hard (Proposition 5.2.2). We then investigate a few candidate optimization problems for finding dc decompositions that speed up the convex-concave procedure. In particular, we extend the notion of an undominated dc decomposition from the quadratic case to higher order polynomials. We show that an undominated dcd always exists (Theorem 5.2.6) and can be found by minimizing a certain linear function of one of the two convex functions in the decomposition. However, this optimization problem is proved to be NP-hard for polynomials of degree four or larger (Proposition 5.2.7). To cope with intractability of finding optimal dc decompositions, we propose in Section 5.3 a class of algebraic relaxations that allow us to optimize over subsets of dcds.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Motivation and organization of the chapter", "weight": 1.0} -->

These relaxations will be based on the notions of *dsos-convex, sdsos-convex,* and *sos-convex* polynomials (see Definition 5.3.3), which respectively lend themselves to *linear, second order cone,* and *semidefinite programming*. In particular, we show that a dc decomposition can always be found by linear programming (Theorem 5.3.5). Finally, in Section 5.4, we perform some numerical experiments to compare the scalability and performance of our different algebraic relaxations.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Polynomial dc decompositions and their complexity", "weight": 1.0} -->

To study questions around dc decompositions of polynomials more formally, let us start by introducing some notation.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Polynomial dc decompositions and their complexity", "weight": 1.0} -->

where the sum is over $n$-tuples of nonnegative integers $\alpha_{i}$. The *degree* of a monomial $x^{\alpha}$ is equal to $\alpha_{1} + \cdots + \alpha_{n}$. The degree of a polynomial $p{(x)}$ is defined to be the highest degree of its component monomials. A simple counting argument shows that a polynomial of degree $d$ in $n$ variables has $\binom{n + d}{d}$ coefficients. A *homogeneous polynomial* (or a *form*) is a polynomial where all the monomials have the same degree. An $n$-variate form $p$ of degree $d$ has $\binom{{n + d} - 1}{d}$ coefficients. We denote the set of polynomials (resp. forms) of degree $2d$ in $n$ variables by ${\overset{\sim}{\mathcal{H}}}_{n,{2d}}$ (resp.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Polynomial dc decompositions and their complexity", "weight": 1.0} -->

Recall that a symmetric matrix $A$ is positive semidefinite (psd) if ${x^{T}Ax} \geq 0$ for all $x \in {\mathbb{R}}^{n}$; this will be denoted by the standard notation ${A \succeq 0}.$ Similarly, a polynomial $p{(x)}$ is said to be *nonnegative* or positive semidefinite if ${p{(x)}} \geq 0$ for all $x \in {\mathbb{R}}^{n}$. For a polynomial $p$, we denote its Hessian by $H_{p}$. The second order characterization of convexity states that $p$ is convex if and only if ${H_{p}{(x)}} \succeq 0$, ${{\forall x} \in {\mathbb{R}}^{n}}.$

<!-- chunk {"id": "body-0210", "role": "body", "section": "Alegbraic relaxations and more tractable subsets of the set of convex polynomials", "weight": 1.0} -->

We have just seen in the previous section that for polynomials with degree as low as four, some basic tasks related to dc decomposition are computationally intractable. In this section, we identify three subsets of the set of convex polynomials that lend themselves to polynomial-time algorithms. These are the sets of *sos-convex, sdsos-convex*, and *dsos-convex* polynomials, which will respectively lead to semidefinite, second order cone, and linear programs. The latter two concepts are to our knowledge new and are meant to serve as more scalable alternatives to sos-convexity. All three concepts certify convexity of polynomials via explicit algebraic identities, which is the reason why we refer to them as algebraic relaxations.

<!-- chunk {"id": "body-0211", "role": "body", "section": "DSOS-convexity, SDSOS-convexity, SOS-convexity", "weight": 1.0} -->

To present these three notions we need to introduce some notation and briefly review the concepts of sos, dsos, and sdsos polynomials.

<!-- chunk {"id": "body-0212", "role": "body", "section": "DSOS-convexity, SDSOS-convexity, SOS-convexity", "weight": 1.0} -->

${p{(x)}} = {z_{n,d}^{T}{(x)}Qz_{n,d}{(x)}}$), for some psd matrix $Q$,. The matrix $Q$ is generally called the Gram matrix of $p$. An SOS optimization problem is the problem of minimizing a linear function over the intersection of the convex cone $SOS_{n,d}$ with an affine subspace. The previous statement implies that SOS optimization problems can be cast as semidefinite programs.

<!-- chunk {"id": "body-0213", "role": "body", "section": "DSOS-convexity, SDSOS-convexity, SOS-convexity", "weight": 1.0} -->

We now define dsos and sdsos polynomials, which were recently proposed by Ahmadi and Majumdar, as more tractable subsets of sos polynomials. When working with dc decompositions of $n$-variate polynomials, we will end up needing to impose sum of squares conditions on polynomials that have $2n$ variables (see Definition 5.3.3). While in theory the SDPs arising from sos conditions are of polynomial size, in practice we rather quickly face a scalability challenge. For this reason, we also consider the class of dsos and sdsos polynomials, which while more restrictive than sos polynomials, are considerably more tractable. For example, Table 5.2 in Section 5.4.2 shows that when $n = 14$, dc decompositions using these concepts are about 250 times faster than an sos-based approach. At $n = 18$ variables, we are unable to run the sos-based approach on our machine. With this motivation in mind, let us start by recalling some concepts from linear algebra.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Existence of difference of s/d/sos-convex decompositions of polynomials", "weight": 1.0} -->

The reason we introduced the notions of s/d/sos-convexity is that in our optimization problems for finding dcds, we would like to replace the condition

<!-- chunk {"id": "body-0215", "role": "body", "section": "Existence of difference of s/d/sos-convex decompositions of polynomials", "weight": 1.0} -->

with the computationally tractable condition

<!-- chunk {"id": "body-0216", "role": "body", "section": "Existence of difference of s/d/sos-convex decompositions of polynomials", "weight": 1.0} -->

The first question that needs to be addressed is whether for any polynomial such a decomposition exists. In this section, we prove that this is indeed the case. This in particular implies that a dcd can be found efficiently.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Existence of difference of s/d/sos-convex decompositions of polynomials", "weight": 1.0} -->

We start by proving a lemma about cones.

<!-- chunk {"id": "body-0218", "role": "body", "section": "of Theorem 5.3.7", "weight": 1.0} -->

Let $p_{n,{2k}} \in \mathcal{H}_{n,{2k}}$ be the form constructed in the proof of Lemma 5.3.9 which is in the interior of ${\Sigma_{D}C_{n,{2k}}}.$ Let $Q_{k}$ denote the strictly diagonally dominant matrix which was constructed to satisfy

<!-- chunk {"id": "body-0219", "role": "body", "section": "Remark 5.3.10", "weight": 1.0} -->

If we had only been interested in showing that any polynomial in ${\overset{\sim}{\mathcal{H}}}_{n,{2d}}$ could be written as a difference of two sos-convex polynomials, this could have been easily done by showing that ${p{(x)}} = \left( {\sum_{i}x_{i}^{2}} \right)^{d} \in {int{({\SigmaC_{n,{2d}}})}}$. However, this form is not dsos-convex or sdsos-convex for all $n,d$ (e.g., for $n = 3$ and ${2d} = 8$). We have been unable to find a simpler proof for existence of sdsos-convex dcds that does not go through the proof of existence of dsos-convex dcds.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Remark 5.3.11", "weight": 1.0} -->

If we solve problem (5.6) with the convexity constraint replaced by a dsos-convexity (resp. sdsos-convexity, sos-convexity) requirement, the same arguments used in the proof of Theorem 5.2.6 now imply that the optimal solution $g^{\ast}$ is not dominated by any dsos-convex (resp. sdsos-convex, sos-convex) decomposition.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Numerical results", "weight": 1.0} -->

In this section, we present a few numerical results to show how our algebraic decomposition techniques affect the convex-concave procedure. The objective function $p \in {\overset{\sim}{\mathcal{H}}}_{n,{2d}}$ in all of our experiments is generated randomly following the ensemble of \[155, Section 5.1.\]. This means that

<!-- chunk {"id": "body-0222", "role": "body", "section": "Numerical results", "weight": 1.0} -->

where $g$ is a random polynomial of total degree $\leq {{2d} - 1}$ whose coefficients are random integers uniformly sampled from ${\lbrack{- 30},30\rbrack}.$ An advantage of polynomials generated in this fashion is that they are bounded below and that their minimum $p^{\ast}$ is achieved over ${\mathbb{R}}^{n}.$ We have intentionally restricted ourselves to polynomials of degree equal to $4$ in our experiments as this corresponds to the smallest degree for which the problem of finding a dc decomposition of $f$ is hard, without being too computationally expensive. Experimenting with higher degrees however would be a worthwhile pursuit in future work. The starting point of CCP was generated randomly from a zero-mean Gaussian distribution.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Numerical results", "weight": 1.0} -->

One nice feature of our decomposition techniques is that all the polynomials ${{f_{i}^{k},i} = 0},{\ldots,m}$ in line 4 of Algorithm 1 in the introduction are sos-convex. This allows us to solve the convex subroutine of CCP exactly via a single SDP \[53, Remark 3.4.\], \[110, Corollary 2.3.\]:

<!-- chunk {"id": "body-0224", "role": "body", "section": "Numerical results", "weight": 1.0} -->

The degree of $\sigma_{0}$ here is taken to be the maximum degree of $f_{0}^{k},\ldots,f_{m}^{k}$. We could have also solved these subproblems using standard descent algorithms for convex optimization. However, we are not so concerned with the method used to solve this convex problem as it is the same for all experiments. All of our numerical examples were done using MATLAB, the polynomial optimization library SPOT, and the solver MOSEK.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

In this subsection, we consider the problem of minimizing a random polynomial $f_{0} \in {\overset{\sim}{\mathcal{H}}}_{8,4}$ over a ball of radius $R$, where $R$ is a random integer in ${\lbrack 20,50\rbrack}.$ The goal is to compare the impact of the dc decomposition of the objective on the performance of CCP. To monitor this, we decompose the objective in 4 different ways and then run CCP using the resulting decompositions. These decompositions are obtained through different SDPs that are listed in Table 5.1.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

yT τ (x) y 777Here, τ (x) is an n × n matrix where each entry is in ${\overset{\sim}{\mathcal{H}}}_{n,{{2d} - 4}}$ sos

<!-- chunk {"id": "body-0227", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

Table 5.1: Different decomposition techniques using sos optimization

<!-- chunk {"id": "body-0228", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

The first SDP in Table 5.1 is simply a feasibility problem. The second SDP minimizes the largest eigenvalue of $H_{h}$ at the initial point $x_{0}$ inputed to CCP. The third minimizes the largest eigenvalue of $H_{h}$ over the ball $B$ of radius $R$. Indeed, let $f_{1}: = \sum_{i}x_{i}^{2} - R^{2}.$ Notice that ${\tau{(x)}} \succeq {0,{\forall x}}$ and if $x \in B$, then ${f_{1}{(x)}} \leq 0$. This implies that ${{{tI} \succeq {H_{h}{(x)}}},{{\forall x} \in B}}.$ The fourth SDP searches for an undominated dcd.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

Once $f_{0}$ has been decomposed, we start CCP. After $4$ mins of total runtime, the program is stopped and we recover the objective value of the last iteration. This procedure is repeated on 30 random instances of $f_{0}$ and $R$, and the average of the results is presented in Figure 5.2.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Picking a good dc decomposition for CCP", "weight": 1.0} -->

From the figure, we can see that the choice of the initial decomposition impacts the performance of CCP considerably, with the region formulation of $\lambda_{\max}$ and the undominated decomposition giving much better results than the other two. It is worth noting that all formulations have gone through roughly the same number of iterations of CCP (approx. 400). Furthermore, these results seem to confirm that it is best to pick an undominated decomposition when applying CCP.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

While solving the last optimization problem in Table 5.1 usually gives very good results, it relies on an sos-convex dc decomposition. However, this choice is only reasonable in cases where the number of variables and the degree of the polynomial that we want to decompose are low. When these become too high, obtaining an sos-convex dcd can be too time-consuming. The concepts of dsos-convexity and sdsos-convexity then become interesting alternatives to sos-convexity. This is illustrated in Table 5.2,

<!-- chunk {"id": "body-0232", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

In this case, $f$ is a random polynomial of degree $4$ in $n$ variables. We also report the optimal value of (5.28) (we know that (5.28) is always guaranteed to be feasible from Theorem 5.3.7).

<!-- chunk {"id": "body-0233", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

Table 5.2: Time and optimal value obtained when solving (5.28)

<!-- chunk {"id": "body-0234", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

Notice that for $n = 18$, it takes over 30 hours to obtain an sos-convex decomposition, whereas the run times for s/dsos-convex decompositions are still in the range of 10 seconds. This increased speed comes at a price, namely the quality of the decomposition. For example, when $n = 10$, the optimal value obtained using sos-convexity is nearly 10 times lower than that of sdsos-convexity.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

Now that we have a better quantitative understanding of this tradeoff, we propose a modification to CCP that leverages the speed of s/dsos-convex dcds for large $n$. The idea is to modify CCP in such a way that one would compute a new s/dsos-convex decomposition of the functions $f_{i}$ after each iteration. Instead of looking for dcds that would provide good global decompositions (such as undominated sos-convex dcds), we look for decompositions that perform well locally. From Section 5.2, candidate decomposition techniques for this task can come from formulations (5.4) and (5.5) that minimize the maximum eigenvalue of the Hessian of $h$ at a point or the trace of the Hessian of $h$ at a point. This modified version of CCP is described in detail in Algorithm 2. We will refer to it as *multiple decomposition CCP*.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

We compare the performance of CCP and multiple decomposition CCP on the problem of minimizing a polynomial $f$ of degree 4 in $n$ variables, for varying values of $n$. In Figure 5.3, we present the optimal value (averaged over 30 instances) obtained after 4 mins of total runtime. The "SDSOS" columns correspond to multiple decomposition CCP (Algorithm 2) with sdsos-convex decompositions at each iteration. The "SOS" columns correspond to classical CCP where the first and only decomposition is an undominated sos-convex dcd. From Figure 5.2, we know that this formulation performs well for small values of $n$. This is still the case here for $n = 8$ and $n = 10$. However, this approach performs poorly for $n = 12$ as the time taken to compute the initial decomposition is too long. In contrast, multiple decomposition CCP combined with sdsos-convex decompositions does slightly worse for $n = 8$ and $n = 10$, but significantly better for $n = 12$.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

3:while stopping criterion not satisfied do
4: Decompose: ∀i find gik, hik s/d/sos-convex that min. t, s.t. t I − Hhik (xk) s/dd888Here dd and sdd matrices refer to notions introduced in Definition 5.3.1. Note that any t which makes t I − A dd or sdd gives an upperbound on λmax (A). By formulating the problem this way (instead of requiring t I ≽ A) we obtain an LP or SOCP instead of an SDP.and fi = gik − hik
5: Convexify: fik(x): = gik(x) − (hik(xk)+∇hik(xk)T(x−xk)), i = 0, …, m
6: Solve convex subroutine: min f0k (x), s.t.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Scalibility of s/d/sos-convex dcds and the multiple decomposition CCP", "weight": 1.0} -->

In conclusion, our overall observation is that picking a good dc decomposition noticeably affects the perfomance of CCP. While optimizing over all dc decompositions is intractable for polynomials of degree greater or equal to $4$, the algebraic notions of sos-convexity, sdsos-convexity and dsos-convexity can provide valuable relaxations. The choice among these options depends on the number of variables and the degree of the polynomial at hand. Though these classes of polynomials only constitute subsets of the set of convex polynomials, we have shown that even the smallest subset of the three contains dcds for any polynomial.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some well-known examples of norms include the $1$-norm, ${f{(x)}} = {\sum_{i = 1}^{n}{|x_{i}|}}$, the $2$-norm, ${f{(x)}} = \sqrt{\sum_{i = 1}^{n}x_{i}^{2}}$, and the $\infty$-norm, ${{f{(x)}} = {\max_{i}{|x_{i}|}}}.$ Our focus throughout this chapter is on norms that can be derived from multivariate polynomials. More specifically, we are interested in establishing conditions under which the $d^{th}$ root of a homogeneous polynomial of degree $d$ is a norm, where $d$ is an even number. We refer to the norm obtained when these conditions are met as *a polynomial norm*. It is easy to see why we restrict ourselves to $d^{th}$ roots of degree-$d$ homogeneous polynomials.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, nonhomogeneous polynomials cannot hope to satisfy the homogeneity condition and homogeneous polynomials of degree $d > 1$ are not 1-homogeneous unless we take their $d^{th}$ root. The question of when the square root of a homogeneous quadratic polynomial is a norm (i.e., when $d = 2$) has a well-known answer (see, e.g., \[35, Appendix A\]): a function ${f{(x)}} = \sqrt{x^{T}Qx}$ is a norm if and only if the symmetric $n \times n$ matrix $Q$ is positive definite. In the particular case where $Q$ is the identity matrix, one recovers the $2$-norm. Positive definiteness of $Q$ can be checked in polynomial time using for example Sylvester's criterion (positivity of the $n$ leading principal minors of $Q$). This means that testing whether the square root of a quadratic form is a norm can be done in polynomial time.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Introduction", "weight": 1.5} -->

A similar characterization in terms of conditions on the coefficients are not known for polynomial norms generated by forms of degree greater than 2. In particular, it is not known whether one can efficiently test membership or optimize over the set of polynomial norms.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Outline and contributions", "weight": 1.0} -->

In this chapter, we study polynomial norms from a computational perspective. In Section 6.2, we give two different necessary and sufficient conditions under which the $d^{th}$ root of a degree-$d$ form $f$ will be a polynomial norm: namely, that $f$ be strictly convex (Theorem 6.2.2), or (equivalently) that $f$ be convex and postive definite (Theorem 6.2.1). Section 6.3 investigates the relationship between general norms and polynomial norms: while many norms are polynomial norms (including all $p$-norms with $p$ even), some norms are not (consider, e.g., the $1$-norm). We show, however, that any norm can be approximated to arbitrary precision by a polynomial norm (Theorem 6.3.1). In Section 6.4, we move on to complexity results and show that simply testing whether the $4^{th}$ root of a quartic form is a norm is strongly NP-hard (Theorem 6.4.1).

<!-- chunk {"id": "body-0243", "role": "body", "section": "Outline and contributions", "weight": 1.0} -->

We then provide a semidefinite programming-based test for checking whether the $d^{th}$ root of a degree $d$ form is a norm (Theorem 6.4.4) and a semidefinite programming-based hierarchy to optimize over a subset of the set of polynomial norms (Theorem 6.4.20). The latter is done by introducing the concept of $r$-sum of squares-convexity (see Definition 6.4.6). We show that any form with a positive definite Hessian is $r$-sos-convex for some value of $r$, and present a lower bound on that value (Theorem 6.4.7). We also show that the level $r$ of the semidefinite programming hierarchy cannot be bounded as a function of the number of variables and the degree only (Theorem 6.4.18). Finally, we cover a few applications of polynomial norms in statistics and dynamical systems in Section 6.5. In Section 6.5.1, we compute approximations of two different types of norms, polytopic gauge norms and $p$-norms with $p$ noneven, using polynomial norms.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Outline and contributions", "weight": 1.0} -->

The techniques described in this section can be applied to norm regression. In Section 6.5.2, we use polynomial norms to prove stability of a switched linear system, a task which is equivalent to computing an upperbound on the joint spectral radius of a family of matrices.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Two equivalent characterizations of polynomial norms", "weight": 1.0} -->

We start this section with two theorems that provide conditions under which the $d^{th}$ root of a degree-$d$ form is a norm. These will be useful in Section 6.4 to establish semidefinite programming-based approximations of polynomial norms. Note that throughout this chapter, $d$ is taken to be an even positive integer.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Approximating norms by polynomial norms", "weight": 1.0} -->

It is easy to see that not all norms are polynomial norms. For example, the 1-norm ${\| x\|}_{1} = {\sum_{i = 1}^{n}{|x_{i}|}}$ is not a polynomial norm. Indeed, all polynomial norms are differentiable at all but one point (the origin) whereas the 1-norm is nondifferentiable whenever one of the components of $x$ is equal to zero. In this section, we show that, though not every norm is a polynomial norm, any norm can be approximated to arbitrary precision by a polynomial norm (Theorem 6.3.1). The proof of this theorem is inspired from a proof by Ahmadi and Jungers. A related result is given by Barvinok. In that chapter, he shows that any norm can be approximated by the $d$-th root of a nonnegative degree-$d$ form, and quantifies the quality of the approximation as a function of $n$ and $d$. The form he obtains however is not shown to be convex.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Approximating norms by polynomial norms", "weight": 1.0} -->

In fact, in a later work \[25, Section 2.4\], Barvinok points out that it would be an interesting question to know whether any norm can be approximated by the $d^{th}$ root of a convex form with the same quality of approximation as for $d$-th roots of nonnegative forms. The result below is a step in that direction though no quantitative result on the quality of approximation is given. Throughout, $S^{n - 1}$ denotes the unit sphere in ${\mathbb{R}}^{n}.$

<!-- chunk {"id": "body-0248", "role": "body", "section": "Remark 6.3.3", "weight": 1.0} -->

We remark that the polynomial norm constructed in Theorem 6.3.1 is the $d^{th}$-root of an *sos-convex* polynomial. Hence, one can approximate any norm on ${\mathbb{R}}^{n}$ by searching for a polynomial norm using semidefinite programming. To see why the polynomial $f$ in (6.6) is sos-convex, observe that linear forms are sos-convex and that an even power of an sos-convex form is sos-convex.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Complexity", "weight": 1.0} -->

It is natural to ask whether testing if the $d^{th}$ root of a given degree-$d$ form is a norm can be done in polynomial time. In the next theorem, we show that, unless $P = {NP}$, this is not the case even when $d = 4$.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Sum of squares polynomials and semidefinite programming review", "weight": 1.0} -->

We start this section by reviewing the notion of *sum of squares polynomials* and related concepts such as *sum of squares-convexity*. We say that a polynomial $f$ is a *sum of squares* (sos) if ${f{(x)}} = {\sum_{i}{q_{i}^{2}{(x)}}}$, for some polynomials $q_{i}$. Being a sum of squares is a sufficient condition for being nonnegative. The converse however is not true, as is exemplified by the Motzkin polynomial

<!-- chunk {"id": "body-0251", "role": "body", "section": "Sum of squares polynomials and semidefinite programming review", "weight": 1.0} -->

which is nonnegative but not a sum of squares. The sum of squares condition is a popular surrogate for nonnegativity due to its tractability. Indeed, while testing nonnegativity of a polynomial of degree greater or equal to 4 is a hard problem, testing whether a polynomial is a sum of squares can be done using *semidefinite programming.* This comes from the fact that a polynomial $p$ of degree $d$ is a sum of squares if and only if there exists a positive semidefinite matrix $Q$ such that ${f{(x)}} = {z{(x)}^{T}Qz{(x)}}$, where $z{(x)}$ is the standard vector of monomials of degree up to $d$ (see, e.g., ). As a consequence, any optimization problem over the coefficients of a set of polynomials which includes a combination of affine constraints and sos constraints on these polynomials, together with a linear objective can be recast as a semidefinite program. These type of optimization problems are known as *sos programs*.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Sum of squares polynomials and semidefinite programming review", "weight": 1.0} -->

Though not all nonnegative polynomials can be written as sums of squares, the following theorem by Artin circumvents this problem using sos multipliers.

<!-- chunk {"id": "body-0253", "role": "body", "section": "A test for validity of polynomial norms", "weight": 1.0} -->

In this subsection, we assume that we are given a form $f$ of degree $d$ and we would like to test whether $f^{1/d}$ is a norm using semidefinite programming.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Remark 6.4.5", "weight": 1.0} -->

We remark that we are not imposing $c > 0$ in the semidefinite program above. This is because, in practice, especially if the semidefinite program is solved with interior point methods, the solution returned by the solver will be in the interior of the feasible set, and hence $c$ will automatically be positive. One can slightly modify (6.9) however to take the constraint $c > 0$ into consideration explicitely.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Remark 6.4.5", "weight": 1.0} -->

It is easy to check that (6.10) is feasible with $\gamma \geq 0$ if and only if the last constraint of (6.9) is feasible with $c > 0$. To see this, take $c = {1/\gamma}$ and note that $\gamma$ can never be zero.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Remark 6.4.5", "weight": 1.0} -->

To the best of our knowledge, we cannot use the approach described in Theorem 6.4.4 to optimize over the set of polynomial norms with a semidefinite program. This is because of the product of decision variables in the coefficients of $f$ and $q$. The next subsection will address this issue.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Optimizing over the set of polynomial norms", "weight": 1.0} -->

In this subsection, we consider the problem of optimizing over the set of polynomial norms. To do this, we introduce the concept of $r$-sos-convexity. Recall that the notation $H_{f}$ references the Hessian matrix of a form $f$.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Remark 6.4.8", "weight": 1.0} -->

Note that $\eta{(f)}$ can also be interpreted as

<!-- chunk {"id": "body-0259", "role": "body", "section": "Remark 6.4.9", "weight": 1.0} -->

Theorem 6.4.7 is a generalization of Theorem 6.4.3. ‣ 6.4.2 Sum of squares polynomials and semidefinite programming review ‣ 6.4 Semidefinite programming-based approximations of polynomial norms ‣ Chapter 6 Polynomials Norms ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") by Reznick. Note though that this is not an immediate generalization. First, $y^{T}H_{f}{(x)}y$ is not a positive definite form (consider, e.g., $y = 0$ and any nonzero $x$). Secondly, note that the multiplier is ${({\sum_{i}x_{i}^{2}})}^{r}$ and does not involve the $y$ variables. (As we will see in the proof, this is essentially because $y^{T}H_{f}{(x)}y$ is quadratic in $y$.)

<!-- chunk {"id": "body-0260", "role": "body", "section": "Remark 6.4.10", "weight": 1.0} -->

Theorem 6.4.7 can easily be adapted to biforms of the type $\sum_{j}{f_{j}{(x)}g_{j}{(y)}}$ where $f_{j}$'s are forms of degree $d$ in $x$ and $g_{j}$'s are forms of degree $\overset{\sim}{d}$ in $y$. In this case, there exist integers $s,r$ such that

<!-- chunk {"id": "body-0261", "role": "body", "section": "Remark 6.4.10", "weight": 1.0} -->

is sos. For the purposes of this chapter however and the connection to polynomial norms, we will show the result in the particular case where the biform of interest is ${y^{T}H_{f}{(x)}y}.$

<!-- chunk {"id": "body-0262", "role": "body", "section": "Remark 6.4.10", "weight": 1.0} -->

Our proof will follow the structure of the proof of Theorem 6.4.3. ‣ 6.4.2 Sum of squares polynomials and semidefinite programming review ‣ 6.4 Semidefinite programming-based approximations of polynomial norms ‣ Chapter 6 Polynomials Norms ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming") given in and reutilize some of the results given in the chapter which we quote here for clarity of exposition.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Remark 6.4.19", "weight": 1.0} -->

Any form $f$ with ${{H_{f}{(x)}} \succ 0},{{\forall x} \neq 0}$ is strictly convex but the converse is not true.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Remark 6.4.19", "weight": 1.0} -->

To see this, note that any form $f$ of degree $d$ with a positive definite Hessian is convex (as ${H_{f}{(x)}} \succeq {0,{\forall x}}$) and positive definite (as, from a recursive application of Euler's theorem on homogeneous functions, ${f{(x)}} = {\frac{1}{d{({d - 1})}}x^{T}H_{f}{(x)}x}$). From the proof of Theorem 6.2.2, this implies that $f$ is strictly convex.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Remark 6.4.19", "weight": 1.0} -->

To see that the converse statement is not true, consider the strictly convex form $f{(x_{1},x_{2})}: = x_{1}^{4} + x_{2}^{4}$. We have

<!-- chunk {"id": "body-0266", "role": "body", "section": "Remark 6.4.19", "weight": 1.0} -->

which is not positive definite e.g., when $x = {}^{T}$.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Optimizing over a subset of polynomial norms with $r$-sos-convexity", "weight": 1.0} -->

In the following theorem, we show how one can efficiently optimize over the set of forms $f$ with ${H_{f}{(x)}} \succ 0$, ${{\forall x} \neq 0}.$ Comparatively to Theorem 6.4.4, this theorem allows us to impose as a constraint that the $d^{th}$ root of a form be a norm, rather than simply testing whether it is. This comes at a cost however: in view of Remark 6.4.19 and Theorem 6.2.2, we are no longer considering all polynomial norms, but a subset of them whose $d^{th}$ power has a positive definite Hessian.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Remark 6.4.21", "weight": 1.0} -->

Note that we are not imposing $c > 0$ in the above semidefinite program. As mentioned in Section 6.4.3, this is because in practice the solution returned by interior point solvers will be in the interior of the feasible set.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Remark 6.4.21", "weight": 1.0} -->

In the special case where $f$ is completely free^22^2This is the case of our two applications in Section 6.5. (i.e., when there are no additional affine conditions on the coefficients of $f$), one can take $c \geq 1$ in (6.16) instead of $c \geq 0$. Indeed, if there exists $c > 0$, an integer $r$, and a polynomial $f$ such that $f - {c{({\sum_{i}x_{i}^{2}})}^{d/2}}$ is $r$-sos-convex, then $\frac{1}{c}f$ will be a solution to (6.16) with $c \geq 1$ replacing $c \geq 0$.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Norm approximation and regression", "weight": 1.0} -->

In this section, we study the problem of approximating a (non-polynomial) norm by a polynomial norm. We consider two different types of norms: $p$-norms with $p$ noneven (and greater than 1) and gauge norms with a polytopic unit ball. For $p$-norms, we use as an example ${\|{(x_{1},x_{2})}^{T}\|} = {({{|x_{1}|}^{7.5} + {|x_{2}|}^{7.5}})}^{1/7.5}$. For our polytopic gauge norm, we randomly generate an origin-symmetric polytope and produce a norm whose 1-sublevel corresponds to that polytope. This allows us to determine the value of the norm at any other point by homogeneity (see \[35, Exercise 3.34\] for more information on gauge norms, i.e., norms defined by convex, full-dimensional, origin-symmetric sets). To obtain our approximations, we proceed in the same way in both cases.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Norm approximation and regression", "weight": 1.0} -->

Problem (6.17) can be written as a semidefinite program as the objective is a convex quadratic in the coefficients of $f$ and the constraint has a semidefinite representation as discussed in Section 6.4.2. The solution $f$ returned is guaranteed to be convex. Moreover, any sos-convex form is sos (see \[89, Lemma 8\]), which implies that $f$ is nonnegative. One can numerically check to see if the optimal polynomial is in fact positive definite (for example, by checking the eigenvalues of the Gram matrix of a sum of squares decomposition of $f$). If that is the case, then, by Theorem 6.2.1, $f^{1/d}$ is a norm. Futhermore, note that we have

<!-- chunk {"id": "body-0272", "role": "body", "section": "Norm approximation and regression", "weight": 1.0} -->

where the first inequality is a consequence of concavity of $z\mapsto z^{1/d}$ and the second is a consequence of the inequality ${|{x - y}|}^{1/d} \geq {|{{|x|}^{1/d} - {|y|}^{1/d}}|}$. This implies that if the optimal value of (6.17) is equal to $\epsilon$, then the sum of the squared differences between $\| x_{i}\|$ and $f^{1/d}{(x_{i})}$ over the sample is less than or equal to $N \cdot {(\frac{\epsilon}{N})}^{1/d}$.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Norm approximation and regression", "weight": 1.0} -->

It is worth noting that in our example, we are actually searching over the entire space of polynomial norms of a given degree. Indeed, as $f$ is bivariate, it is convex if and only if it is sos-convex. In Figure 6.2, we have drawn the 1-level sets of the initial norm (either the $p$-norm or the polytopic gauge norm) and the optimal polynomial norm obtained via (6.17) with varying degrees $d$. Note that when $d$ increases, the approximation improves.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Norm approximation and regression", "weight": 1.0} -->

A similar method could be used for *norm regression*. In this case, we would have access to data points $x_{1},\ldots,x_{N}$ corresponding to noisy measurements of an underlying unknown norm function. We would then solve the same optimization problem as the one given in (6.17) to obtain a polynomial norm that most closely approximates the noisy data.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

As a second application, we revisit a result from Ahmadi and Jungers from on upperbounding the joint spectral radius of a finite set of matrices. We first review a few notions relating to dynamical systems and linear algebra. The spectral radius $\rho$ of a matrix $A$ is defined as

<!-- chunk {"id": "body-0276", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

The spectral radius happens to coincide with the eigenvalue of $A$ of largest magnitude. Consider now the discrete-time linear system $x_{k + 1} = {Ax_{k}}$, where $x_{k}$ is the $n \times 1$ state vector of the system at time $k$. This system is said to be *asymptotically stable* if for any initial starting state $x_{0} \in {\mathbb{R}}^{n}$, ${x_{k}\rightarrow 0},$ when ${k\rightarrow\infty}.$ A well-known result connecting the spectral radius of a matrix to the stability of a linear system states that the system $x_{k + 1} = {Ax_{k}}$ is asymptotically stable if and only if ${\rho{(A)}} < 1$.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

In 1960, Rota and Strang introduced a generalization of the spectral radius to a *set* of matrices. The *joint spectral radius (JSR)* of a set of matrices $\mathcal{A}: = {\{ A_{1},\ldots,A_{m}\}}$ is defined as

<!-- chunk {"id": "body-0278", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

Analogously to the case where we have just one matrix, the value of the joint spectral radius can be used to determine stability of a certain type of system, called *a switched linear system.* A switched linear system models an uncertain and time-varying linear system, i.e., a system described by the dynamics

<!-- chunk {"id": "body-0279", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

where the matrix $A_{k}$ varies at each iteration within the set $\mathcal{A}$. As done previously, we say that a switched linear system is asymptotically stable if $x_{k}\rightarrow\infty$ when $k\rightarrow\infty$, for any starting state $x_{0} \in {\mathbb{R}}^{n}$ and any sequence of products of matrices in $\mathcal{A}$. One can establish that the switched linear system $x_{k + 1} = {A_{k}x_{k}}$ is asymtotically stable if and only if ${\rho{(\mathcal{A})}} < 1$.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Joint spectral radius and stability of linear switched systems", "weight": 1.0} -->

Though they may seem similar on many points, a key difference between the spectral radius and the joint spectral radius lies in difficulty of computation: testing whether the spectral radius of a matrix $A$ is less than equal (or strictly less) than $1$ can be done in polynomial time. However, already when $m = 2$, the problem of testing whether ${\rho{(A_{1},A_{2})}} \leq 1$ is undecidable. An active area of research has consequently been to obtain sufficient conditions for the JSR to be strictly less than one, which, for example, can be checked using semidefinite programming. The theorem that we revisit below is a result of this type. We start first by recalling a Theorem linked to stability of a linear system.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Example 6.5.3", "weight": 1.0} -->

We consider a modification of Example 5.4. in as an illustration of the previous theorem. We would like to show that the joint spectral radius of the two matrices

<!-- chunk {"id": "body-0282", "role": "body", "section": "Example 6.5.3", "weight": 1.0} -->

To do this, we search for a nonzero form $f$ of degree $d$ such that

<!-- chunk {"id": "body-0283", "role": "body", "section": "Example 6.5.3", "weight": 1.0} -->

If problem (6.19) is feasible for some $d$, then ${\rho{(A_{1},A_{2})}} < 1$. A quick computation using the software package YALMIP and the SDP solver MOSEK reveals that, when $d = 2$ or $d = 4$, problem (6.19) is infeasible. When $d = 6$ however, the problem is feasible and we obtain a polynomial norm $V = f^{1/d}$ whose 1-sublevel set is the outer set plotted in Figure 6.3. We also plot on Figure 6.3 the images of this 1-sublevel set under $A_{1}$ and $A_{2}$. Note that both sets are included in the 1-sublevel set of $V$ as expected. From Theorem 6.5.2.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Example 6.5.3", "weight": 1.0} -->

‣ 6.5.2 Joint spectral radius and stability of linear switched systems ‣ 6.5 Applications ‣ Chapter 6 Polynomials Norms ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming"), the existence of a polynomial norm implies that ${\rho{(A_{1},A_{2})}} < 1$ and hence, the pair $\{ A_{1},A_{2}\}$ is asymptotically stable.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Remark 6.5.4", "weight": 1.0} -->

As mentioned previously, problem (6.19) is infeasible for $d = 4$. Instead of pushing the degree of $f$ up to 6, one could wonder whether the problem would have been feasible if we had asked that $f$ of degree $d = 4$ be $r$-sos-convex for some fixed $r \geq 1$. As mentioned before, in the particular case where $n = 2$ (which is the case at hand here), the notions of convexity and sos-convexity coincide; see. As a consequence, one can only hope to make problem (6.19) feasible by increasing the degree of $f$.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Future directions", "weight": 1.0} -->

In this chapter, we provided semidefinite programming-based conditions under which we could test whether the $d^{th}$ root of a degree-$d$ form is a polynomial norm (Section 6.4.3), and semidefinite programming-based conditions under which we could optimize over the set of forms with positive definite Hessians (Section 6.4.4). A clear gap emerged between forms which are strictly convex and those which have a positive definite Hessian, the latter being a sufficient (but not necessary) condition for the former. This leads us to consider the following two open problems.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Open Problem 6.6.1", "weight": 1.0} -->

We have given a semidefinite programming hierarchy for optimizing over a subset of polynomial norms. Is there a semidefinite programming hierarchy that optimizes over all polynomial norms?

<!-- chunk {"id": "body-0288", "role": "body", "section": "Open Problem 6.6.2", "weight": 1.0} -->

Helton and Nie have shown in that sublevel sets of forms that have positive definite Hessians are SDP-representable. This means that we can optimize linear functions over these sets using semidefinite programming. Is the same true for sublevel sets of all polynomial norms?

<!-- chunk {"id": "body-0289", "role": "body", "section": "Open Problem 6.6.2", "weight": 1.0} -->

On the application side, it might be interesting to investigate how one can use polynomial norms to design *regularizers* in machine learning applications. Indeed, a very popular use of norms in optimization is as regularizers, with the goal of imposing additional structure (e.g., sparsity or low-rankness) on optimal solutions. One could imagine using polynomial norms to design regularizers that are based on the data at hand in place of more generic regularizers such as the 1-norm. Regularizer design is a problem that has already been considered (see, e.g., ) but not using polynomial norms. This can be worth exploring as we have shown that polynomial norms can approximate any norm with arbitrary accuracy, while remaining differentiable everywhere (except at the origin), which can be beneficial for optimization purposes.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central problem in robotics, computer graphics, virtual and augmented reality (VR/AR), and many applications involving complex physics simulations is the accurate, real-time determination of proximity relationships between three-dimensional objects situated in a cluttered environment. In robot navigation and manipulation tasks, path planners need to compute a dynamically feasible trajectory connecting an initial state to a goal configuration while avoiding obstacles in the environment. In VR/AR applications, a human immersed in a virtual world may wish to touch computer generated objects that must respond to contacts in physically realistic ways. Likewise, when collisions are detected, 3D gaming engines and physics simulators (e.g., for molecular dynamics) need to activate appropriate directional forces on interacting entities. All of these applications require geometric notions of separation and penetration between representations of three-dimensional objects to be continuously monitored.

<!-- chunk {"id": "body-0291", "role": "body", "section": "Introduction", "weight": 1.5} -->

A rich class of computational geometry problems arises in this context, when 3D objects are outer approximated by convex or nonconvex bounding volumes. In the case where the bounding volumes are convex, the Euclidean distance between them can be computed very precisely, providing a reliable certificate of safety for the objects they enclose. In the case where the bounding volumes are nonconvex, distance computation can be done either approximately via convex decomposition heuristics which cover the volumes by a finite union of convex shapes, or exactly by using more elaborate algebraic optimization hierarchies that we discuss in this chapter. When 3D objects overlap, quantitative measures of degree of penetration are needed in order to optimally resolve collisions, e.g., by a gradient-based trajectory optimizer. Multiple such measures have been proposed in the literature. The penetration depth is the minimum magnitude translation that brings the overlapping objects out of collision. The growth distance is the minimum shrinkage of the two bodies required to reduce volume penetration down to merely surface touching. Efficient computation of penetration measures is also a problem of interest to this chapter.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Contributions and organization of the chapter", "weight": 1.0} -->

In this work, we propose to represent the geometry of a given 3D environment comprising multiple static or dynamic rigid bodies using sublevel sets of polynomials. The chapter is organized as follows: In Section 7.2, we provide an overview of the algebraic concepts of sum of squares (sos) and sum of squares-convex (sos-convex) polynomials as well as their relation to semidefinite programming and polynomial optimization. In Section 7.3, we consider the problem of containing a cloud of 3D points with tight-fitting convex or nearly convex sublevel sets of polynomials. In particular, we propose and justify a new volume minimization heuristic for these sublevel sets which empirically results in tighter fitting polynomials than previous proposals,. Additionally, we give a procedure for explicitly tuning the extent of convexity imposed on these sublevel set bounding volumes using sum of squares optimization techniques. If convexity is imposed, we refer to them as sos-convex bodies; if it is not, we term them simply as sos-bodies.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Contributions and organization of the chapter", "weight": 1.0} -->

(See Section 7.2 for a more formal definition.) We show that the bounding volumes we obtain are highly compact and adapt to the shape of the data in more flexible ways than canned convex primitives typically used in standard bounding volume hierarchies; see Table 7.1. The construction of our bounding volumes involves small-scale semidefinite programs (SDPs) that can fit, in an offline preprocessing phase, 3D meshes with tens of thousands of data points in a few seconds. In Section 7.4, we give sum of squares algorithms for measuring notions of separation or penetration, including Euclidean distance and growth distance, of two bounding volumes representing obstacles. We show that even when convexity is lacking, we can efficiently compute (often tight) lower bounds on these measures. In Section 7.5, we consider the problem of grouping several obstacles (i.e., bounding volumes) within one, with the idea of making a map of the 3D environment with a lower level of resolution. A semidefinite programming based algorithm for this purpose is proposed and demonstrated via an example.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

In this section, we briefly review the notions of *sum of squares polynomials*, *sum of squares-convexity,* and *polynomial optimization* which will all be central to the geometric problems we discuss later. We refer the reader to the recent monograph for a more detailed overview of the subject.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

Throughout, we will denote the set of $n \times n$ symmetric matrices by $S^{n \times n}$ and the set of degree-$2d$ polynomials with real coefficients by ${\mathbb{R}}_{2d}{\lbrack x\rbrack}$. We say that a polynomial ${p{(x_{1},\ldots,x_{n})}} \in {{\mathbb{R}}_{2d}{\lbrack x\rbrack}}$ is *nonnegative* if ${{p{(x_{1},\ldots,x_{n})}} \geq 0},{{\forall x} \in {\mathbb{R}}^{n}}$. In many applications (including polynomial optimization that we will cover later), one would like to constrain certain coefficients of a polynomial so as to make it nonnegative. Unfortunately, even testing whether a given polynomial (of degree ${2d} \geq 4$) is nonnegative is NP-hard.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

As a consequence, we would like to replace the intractable condition that $p$ be nonnegative by a sufficient condition for it that is more tractable. One such condition is for the polynomial to have a sum of squares decomposition. We say that a polynomial $p$ is a *sum of squares (sos)* if there exist polynomials $q_{i}$ such that $p = {\sum_{i}q_{i}^{2}}$. From this definition, it is clear that any sos polynomial is nonnegative, though not all nonnegative polynomials are sos; see, e.g. for some counterexamples.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

Furthermore, requiring that a polynomial $p$ be sos is a computationally tractable condition as a consequence of the following characterization: A polynomial $p$ of degree $2d$ is sos if and only if there exists a positive semidefinite matrix $Q$ such that ${{p{(x)}} = {z{(x)}^{T}Qz{(x)}}},$ where $z{(x)}$ is the vector of all monomials of degree up to $d$. The matrix $Q$ is sometimes called the Gram matrix of the sos decomposition and is of size $\binom{n + d}{d} \times \binom{n + d}{d}$.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

(Throughout the chapter, we let ${{N:} = \binom{n + d}{d}}.$) The task of finding a positive semidefinite matrix $Q$ that makes the coefficients of $p$ all equal to the coefficients of $z{(x)}^{T}Qz{(x)}$ is a semidefinite programming problem, which can be solved in polynomial time to arbitrary accuracy.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

The concept of sum of squares can also be used to define a sufficient condition for convexity of polynomials known as *sos-convexity*. We say that a polynomial $p$ is sos-convex if the polynomial $y^{T}{\nabla^{2}p}{(x)}y$ in $2n$ variables $x$ and $y$ is a sum of squares. Here, ${\nabla^{2}p}{(x)}$ denotes the Hessian of $p$, which is a symmetric matrix with polynomial entries. For a polynomial of degree $2d$ in $n$ variables, one can check that the dimension of the Gram matrix associated to the sos-convexity condition is ${\overset{\sim}{N}:} = {n \cdot \binom{{n + d} - 1}{d - 1}}$.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

It follows from the second order characterization of convexity that any sos-convex polynomial is convex, as $y^{T}{\nabla^{2}p}{(x)}y$ being sos implies that ${{{\nabla^{2}p}{(x)}} \succeq {0,{\forall x}}}.$ The converse however is not true, though convex but not sos-convex polynomials are hard to find in practice; see. Through its link to sum of squares, it is easy to see that testing whether a given polynomial is sos-convex is a semidefinite program. By contrast, testing whether a polynomial of degree ${2d} \geq 4$ is convex is NP-hard.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

A *polynomial optimization problem* is a problem of the form

<!-- chunk {"id": "body-0302", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

where the objective $p$ is a (multivariate) polynomial and the feasible set $K$ is a basic semialgebraic set; i.e.,

<!-- chunk {"id": "body-0303", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

It is straightforward to see that problem (7.1) can be equivalently formulated as that of finding the largest constant $\gamma$ such that ${{{{p{(x)}} - \gamma} \geq 0},{{\forall x} \in K}}.$ It is known that, under mild conditions (specifically, under the assumption that $K$ is Archimedean ), the condition ${{{p{(x)}} - \gamma} > 0},{{\forall x} \in K}$, is equivalent to the existence of sos polynomials $\sigma_{i}{(x)}$ such that ${{p{(x)}} - \gamma} = {{\sigma_{0}{(x)}} + {\sum_{i = 1}^{m}{\sigma_{i}{(x)}g_{i}{(x)}}}}$.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

Indeed, it is at least clear that if $x \in K$, i.e., ${g_{i}{(x)}} \geq 0$, then ${{\sigma_{0}{(x)}} + {\sum_{i = 1}^{m}{\sigma_{i}{(x)}g_{i}{(x)}}}} \geq 0$ which means that ${{p{(x)}} - \gamma} \geq 0$. The converse is less trivial and is a consequence of the Putinar Positivstellensatz. Using this result, problem (7.1) can be rewritten as

<!-- chunk {"id": "body-0305", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

For any fixed upper bound on the degrees of the polynomials $\sigma_{i}$, this is a semidefinite programming problem which produces a lower bound on the optimal value of (7.1). As the degrees of $\sigma_{i}$ increase, these lower bounds are guaranteed to converge to the true optimal value of (7.1). Note that we are making *no convexity assumptions* about the polynomial optimization problem and yet solving it *globally* through a sequence of semidefinite programs.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

Sum of squares and polynomial optimization in robotics. We remark that sum of squares techniques have recently found increasing applications to a whole host of problems in robotics, including constructing Lyapunov functions, locomotion planning, design and verification of provably safe controllers, grasping and manipulation, robot-world calibration, and inverse optimal control, among others.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Sum of squares and sos-convexity", "weight": 1.0} -->

We also remark that a different use of sum of squares optimization for finding minimum bounding volumes that contain semialgebraic sets has been considered in along with some interesting control applications (see Section 7.5 for a brief description).

<!-- chunk {"id": "body-0308", "role": "body", "section": "3D point cloud containment", "weight": 1.0} -->

Throughout this section, we are interested in finding a body of minimum volume, parametrized as the 1-sublevel set of a polynomial of degree $2d$, which encloses a set of given points $\{ x_{1},\ldots,x_{m}\}$ in ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Convex sublevel sets", "weight": 1.0} -->

We focus first on finding a *convex* bounding volume. Convexity is a common constraint in the bounding volume literature and it makes certain tasks (e.g., distance computation among the different bodies) simpler. In order to make a set of the form $\left. \{{x \in {\mathbb{R}}^{3}} \middle| {{p{(x)}} \leq 1}\} \right.$ convex, we will require the polynomial $p$ to be convex. (Note that this is a sufficient but not necessary condition.) Furthermore, to have a tractable formulation, we will replace the convexity condition with an sos-convexity condition as described previously. Even after these relaxations, the problem of minimizing the volume of our sublevel sets remains a difficult one. The remainder of this section discusses several heuristics for this task.

<!-- chunk {"id": "body-0310", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

where $w{(x,y)}$ is a vector of monomials in $x$ and $y$ of degree $1$ in $y$ and $d - 1$ in $x$. This problem outputs a polynomial $p$ whose 1-sublevel set corresponds to the bounding volume that we are interested.

<!-- chunk {"id": "body-0311", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

The last constraint simply ensures that all the data points are within the 1-sublevel set of $p$ as required.

<!-- chunk {"id": "body-0312", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

The second constraint imposes that $p$ be sos-convex. The matrix $H$ is the Gram matrix associated with the sos condition on $y^{T}{\nabla^{2}p}{(x)}y$.

<!-- chunk {"id": "body-0313", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

The first constraint requires that the polynomial $p$ be sos. This is a necessary condition for boundedness of (7.3) when $p$ is parametrized with affine terms. To see this, note that for any given positive semidefinite matrix $Q$, one can always pick the coefficients of the affine terms in such a way that the constraint ${p{(x_{i})}} \leq 1$ for $i = {1,\ldots,m}$ be trivially satisfied. Likewise one can pick the remaining coefficients of $p$ in such a way that the sos-convexity condition is satisfied. The restriction to sos polynomials, however, can be done without loss of generality. Indeed, suppose that the minimum volume sublevel set was given by $\left. \{ x \middle| {{p{(x)}} \leq 1}\} \right.$ where $p$ is an sos-convex polynomial.

<!-- chunk {"id": "body-0314", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

The objective function of the above formulation is motivated in part by the degree ${2d} = 2$ case. Indeed, when ${2d} = 2$, the sublevel sets of convex polynomials are ellipsoids of the form $\left. \{ x \middle| {{{x^{T}Px} + {b^{T}x} + c} \leq 1}\} \right.$ and their volume is given by ${\frac{4}{3}\pi} \cdot \sqrt{\det{(P^{- 1})}}$. Hence, by minimizing $- {\log{\det{(P)}}}$, we would exactly minimize volume. As the matrix $P$ above is none other than the Hessian of the quadratic polynomial ${x^{T}Px} + {b^{T}x} + c$ (up to a multiplicative constant), this partly justifies the formulation given. Another justification for this formulation is given in itself and relates to curvature of the polynomial $p$.

<!-- chunk {"id": "body-0315", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

Indeed, the curvature of $p$ at a point $x$ along a direction $y$ is proportional to $y^{T}{\nabla^{2}p}{(x)}y$. By imposing that ${{y^{T}{\nabla^{2}p}{(x)}y} = {w{(x,y)}^{T}Hw{(x,y)}}},$ with $H \succeq 0$, and then maximizing $\log{({\det{(H)}})}$, this formulation seeks to increase the curvature of $p$ along all directions so that its 1-sublevel set can get closer to the points $x_{i}$. Note that curvature maximization in all directions without regards to data distribution can be counterproductive in terms of tightness of fit, particularly in regions where the data geometry is flat (an example of this is given in Figure 7.3).

<!-- chunk {"id": "body-0316", "role": "body", "section": "The Hessian-based approach", "weight": 1.0} -->

A related minimum volume heuristic that we will also experiment with replaces the $\log\det$ objective with a linear one. More specifically, we introduce an extra decision variable $V \in S^{\overset{\sim}{N} \times \overset{\sim}{N}}$ and minimize $\text{trace}{(V)}$ while adding an additional constraint ${\begin{bmatrix}
\end{bmatrix} \succeq 0}.$ Using the Schur complement, the latter constraint can be rewritten as $V \succeq H^{- 1}$. As a consequence, this trace formulation minimizes the *sum* of the inverse of the eigenvalues of $H$ whereas the $\log\det$ formulation described in (7.3) minimizes the *product* of the inverse of the eigenvalues.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Our approach", "weight": 1.0} -->

We propose here an alternative heuristic for obtaining a tight-fitting convex body containing points in ${\mathbb{R}}^{n}.$ Empirically, we validate that it tends to consistently return convex bodies of smaller volume than the ones obtained with the methods described above (see Figure 7.3 below for an example). It also generates a relatively smaller convex optimization problem.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Our approach", "weight": 1.0} -->

One can also obtain a trace formulation of this problem by replacing the $\log\det$ objective by a trace one as it was done in the previous paragraph.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Our approach", "weight": 1.0} -->

Note that the main difference between (7.3) and (7.4) lies in the Gram matrix chosen for the objective function. In (7.3), the Gram matrix comes from the sos-convexity constraint, whereas in (7.4), the Gram matrix is generated by the sos constraint.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Our approach", "weight": 1.0} -->

In the case where the polynomial is quadratic and convex, we saw that the formulation (7.3) is exact as it finds the minimum volume ellipsoid containing the points. It so happens that the formulation given in (7.4) is also exact in the quadratic case, and, in fact, both formulations return the same optimal ellipsoid. As a consequence, the formulation given in (7.4) can also be viewed as a natural extension of the quadratic case.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Our approach", "weight": 1.0} -->

To provide more intuition as to why this formulation performs well, we interpret the 1-sublevel set

<!-- chunk {"id": "body-0322", "role": "body", "section": "Our approach", "weight": 1.0} -->

of $p$ as the preimage of some set whose volume is being minimized. More precisely, consider the set

<!-- chunk {"id": "body-0323", "role": "body", "section": "Our approach", "weight": 1.0} -->

which corresponds to the image of ${\mathbb{R}}^{n}$ under the monomial map $z{(x)}$ and the set

<!-- chunk {"id": "body-0324", "role": "body", "section": "Our approach", "weight": 1.0} -->

for a positive semidefinite matrix $P$ such that ${{p{(x)}} = {z{(x)}^{T}Pz{(x)}}}.$ Then, the set $S$ is simply the preimage of the intersection of $T_{1}$ and $T_{2}$ through the mapping $z$. Indeed, for any $x \in S$, we have ${p{(x)}} = {z{(x)}^{T}Pz{(x)}} \leq 1$. The hope is then that by minimizing the volume of $T_{2}$, we will minimize volume of the intersection $T_{1} \cap T_{2}$ and hence that of its preimage through $z$, i.e., the set $S.$

<!-- chunk {"id": "body-0325", "role": "body", "section": "Relaxing convexity", "weight": 1.0} -->

Though containing a set of points with a convex sublevel set has its advantages, it is sometimes necessary to have a tighter fit than the one provided by a convex body, particularly if the object of interest is highly nonconvex. One way of handling such scenarios is via convex decomposition methods, which would enable us to represent the object as a union of sos-convex bodies. Alternatively, one can aim for problem formulations where convexity of the sublevel sets is not imposed. In the remainder of this subsection, we first review a recent approach from the literature to do this and then present our own approach which allows for controlling the level of nonconvexity of the sublevel set.

<!-- chunk {"id": "body-0326", "role": "body", "section": "The inverse moment approach", "weight": 1.0} -->

In very recent work, Lasserre and Pauwels propose an approach for containing a cloud of points with sublevel sets of polynomials (with no convexity constraint). Given a set of data points ${x_{1},\ldots,x_{m}} \in {\mathbb{R}}^{n}$, it is observed in that paper that the sublevel sets of the degree $2d$ sos polynomial

<!-- chunk {"id": "body-0327", "role": "body", "section": "The inverse moment approach", "weight": 1.0} -->

tend to take the shape of the data accurately. Here, $z{(x)}$ is the vector of all monomials of degree up to $d$ and $M_{d}{({\mu{(x_{1},\ldots,x_{m})}})}$ is the moment matrix of degree $d$ associated with the empirical measure $\mu: = \frac{1}{m}\sum_{i = 1}^{m}\delta_{x_{i}}$ defined over the data. This is an $\binom{n + d}{d} \times \binom{n + d}{d}$ symmetric positive semidefinite matrix which can be cheaply constructed from the data ${x_{1},\ldots,x_{m}} \in {\mathbb{R}}^{n}$ (see for details).

<!-- chunk {"id": "body-0328", "role": "body", "section": "The inverse moment approach", "weight": 1.0} -->

One very nice feature of this method is that to construct the polynomial $p_{\mu,d}$ in (7.5) one only needs to invert a matrix (as opposed to solving a semidefinite program as our approach would require) after a single pass over the point cloud. The approach however does not a priori provide a particular sublevel set of $p_{\mu,d}$ that is guaranteed to contain all data points. Hence, once $p_{\mu,d}$ is constructed, one could slowly increase the value of a scalar $\gamma$ and check whether the $\gamma$-sublevel set of $p_{\mu,d}$ contains all points.

<!-- chunk {"id": "body-0329", "role": "body", "section": "Our approach and controlling convexity", "weight": 1.0} -->

An advantage of our proposed formulation (7.4) is that one can easily drop the sos-convexity assumption in the constraints and thereby obtain a sublevel set which is not necessarily convex. This is not an option for formulation (7.3) as the Gram matrix associated to the sos-convexity constraint intervenes in the objective.

<!-- chunk {"id": "body-0330", "role": "body", "section": "Our approach and controlling convexity", "weight": 1.0} -->

Note that in neither this formulation nor the inverse moment approach of Lasserre and Pauwels, does the optimizer have control over the shape of the sublevel sets produced, which may be convex or far from convex. For some applications, it is useful to control in some way the degree of convexity of the sublevel sets obtained by introducing a parameter which when increased or decreased would make the sets more or less convex.

<!-- chunk {"id": "body-0331", "role": "body", "section": "Our approach and controlling convexity", "weight": 1.0} -->

Note that when $c = 0$, the problem we are solving corresponds exactly to (7.4) and the sublevel set obtained is convex. When $c > 0$, we allow for nonconvexity of the sublevel sets. Note that this is a consequence of ${({\sum_{i}x_{i}^{2}})}^{d}$ being a strictly convex function, which can offset the nonconvexity of $p$. As we decrease $c$ towards zero, we obtain sublevel sets which get progressively more and more convex.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Bounding volume numerical experiments", "weight": 1.0} -->

In Table 7.1, we provide a comparison of various bounding volumes on Princeton Shape Benchmark datasets. It can be seen that sos-convex bodies generated by higher degree polynomials provide much tighter fits than spheres or axis-aligned bounding boxes (AABB) in general. The proposed minimum volume heuristic of our formulation in (7.4) works better than that proposed in (see (7.3)). In both formulations, typically, the log-determinant objective outperforms the trace objective. The convex hull is the tightest possible convex body. However, for smooth objects like the vase, the number of vertices describing the convex hull can be a substantial fraction of the original number of points in the point cloud. When convexity is relaxed, a degree-6 sos polynomial compactly described by just $84$ coefficients gives a tighter fit than the convex hull. For the same degree, solutions to our formulation (7.6) with a positive value of $c$ outperform the inverse moment construction of.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Bounding volume numerical experiments", "weight": 1.0} -->

The bounding volume construction times are shown in Figure 7.4 for sos-convex chair models. In comparison to the volume heuristics of, our heuristic runs noticeably faster as soon as degree exceeds $6$. We believe that this may come from the fact that the decision variable featuring in the objective in our case is a matrix of size $N \times N$, where $N = \binom{n + d}{d}$, whereas the decision variable featuring in the objective of is of size ${\overset{\sim}{N} \times \overset{\sim}{N}},$ where ${\overset{\sim}{N} = {n \cdot \binom{{n + d} - 1}{d - 1}} > N}.$ Our implementation uses YALMIP with the splitting conic solver (SCS) as its backend SDP solver (run for 2500 iterations). Note that the inverse moment approach of is the fastest as it does not involve any optimization and makes just one pass over the point cloud.

<!-- chunk {"id": "body-0334", "role": "body", "section": "Bounding volume numerical experiments", "weight": 1.0} -->

However, this approach is not guaranteed to return a convex body, and for nonconvex bodies, tighter fitting polynomials can be estimated using log-determinant or trace objectives on our problem (7.6).

<!-- chunk {"id": "body-0335", "role": "body", "section": "points/vertices in cvx hull", "weight": 1.0} -->

Table 7.1: Comparison of the volume of various bounding bodies obtained from different techniques

<!-- chunk {"id": "body-0336", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

In this section, we are interested in computing the Euclidean distance between two basic semialgebraic sets

<!-- chunk {"id": "body-0337", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

We will tackle this problem by applying the sos hierarchy described at the end of Section 7.2. This will take the form of the following hierarchy of semidefinite programs

<!-- chunk {"id": "body-0338", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

where in the $d$-th level of the hierarchy, the degree of all polynomials $\tau_{i}$ and $\xi_{j}$ is upper bounded by $d$. Observe that the optimal value of each SDP produces a *lower bound* on (7.7) and that when $d$ increases, this lower bound can only improve.

<!-- chunk {"id": "body-0339", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

Amazingly, in all examples we tried (independently of convexity of $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$), the 0-th level of the hierarchy was already exact (though we were unable to prove this). By this we mean that the optimal value of (7.8) exactly matched that of (7.7), already when the degree of the polynomials $\tau_{i}$ and $\xi_{j}$ was zero; i.e., when $\tau_{i}$ and $\xi_{j}$ were nonnegative scalars. An example of this phenomenon is given in Figure 7.5 where the green bodies are each a (highly nonconvex) sublevel set of a quartic polynomial.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

When our SDP relaxation is exact, we can recover the points $x^{\ast}$ and $y^{\ast}$ where the minimum distance between sets is achieved from the eigenvector corresponding to the zero eigenvalue of the Gram matrix associated with the first sos constraint in (7.8). This is what is done in Figure 7.5.

<!-- chunk {"id": "body-0341", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

The sos-convex case. One important special case where we know that the 0-th level of the sos hierarchy in (7.8) is *guaranteed* to be exact is when the defining polynomials $g_{i}$ and $h_{i}$ of $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ are *sos-convex*. This is a corollary of the fact that the 0-th level sos relaxation is known to be tight for the general polynomial optimization problem in (7.1) if the polynomials $p$ and $- g_{i}$ involved in the description of $K$ there are sos-convex; see. An example of the computation of the minimum distance between two degree-6 sos-convex bodies enclosing human and chair 3D point clouds is given below, together with the points achieving the minimum distance.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

Using MATLAB's fmincon active-set solver, the time required to compute the distance between two sos-convex bodies ranges from around 80 milliseconds to 340 milliseconds seconds as the degree is increased from $2$ to $8$; see Table 7.2. We believe that the execution time can be improved by an order of magnitude with more efficient polynomial representations, warm starts for repeated queries, and reduced convergence tolerance for lower-precision results.

<!-- chunk {"id": "body-0343", "role": "body", "section": "Euclidean distance", "weight": 1.0} -->

Table 7.2: Euclidean distance query times for sos-convex sets.

<!-- chunk {"id": "body-0344", "role": "body", "section": "Penetration measures for overlapping bodies", "weight": 1.0} -->

As another application of sos-convex polynomial optimization problems, we discuss a problem relevant to collision avoidance. Here, we assume that our two bodies $\mathcal{S}_{1}$, $\mathcal{S}_{2}$ are of the form $\mathcal{S}_{1}: = {\{ x|p_{1}{(x)} \leq 1\}}$ and $\mathcal{S}_{2}: = {\{ x|p_{2}{(x)} \leq 1\}},$ where $p_{1},p_{2}$ are sos-convex. As shown in Figure 7.1 (right), by varying the sublevel value, we can grow or shrink the sos representation of an object.

<!-- chunk {"id": "body-0345", "role": "body", "section": "Penetration measures for overlapping bodies", "weight": 1.0} -->

In other words, the sets $\left. \{ x \middle| {{p_{2}{(x)}} \leq 1}\} \right.$ and $\{ x|p_{1}{(x)} \leq d{(p_{1}||p_{2})}\}$ do not overlap. As a consequence, the optimal value of (7.9) gives us a measure of how much we need to shrink the level set defined by $p_{1}$ to eventually move out of contact of the set $\mathcal{S}_{2}$ assuming that the "seed point", i.e., the minimum of $p_{1}$, is outside $\mathcal{S}_{2}$. It is clear that,

<!-- chunk {"id": "body-0346", "role": "body", "section": "Penetration measures for overlapping bodies", "weight": 1.0} -->

These measures are closely related to the notion of growth models and growth distances. Note that similarly to what is described for the sos-convex case in Section 7.4.1, the optimal solution $d{(p_{1}||p_{2})}$ to (7.9) can be computed exactly using semidefinite programming, or using a generic convex optimizer. The two leftmost subfigures of Figure 7.7 show a chair and a human bounded by 1-sublevel sets of degree 6 sos-convex polynomials (in green). In both cases, we compute $d{(p_{1}||p_{2})}$ and $d{(p_{2}||p_{1})}$ and plot the corresponding minimizers. In the first subfigure, the level set of the chair needs to grow in order to touch the human and vice-versa, certifying separation. In the second subfigure, we translate the chair across the volume occupied by the human so that they overlap. In this case, the level sets need to contract.

<!-- chunk {"id": "body-0347", "role": "body", "section": "Penetration measures for overlapping bodies", "weight": 1.0} -->

In the third subfigure, we plot the optimal value of the problem in (7.9) as the chair is translated from left to right, showing how the growth distances dip upon penetration and rise upon separation. The final subfigure shows the time taken to solve (7.9) when warm started from the previous solution. The time taken is of the order of 150 milliseconds without warm starts to 10 milliseconds with warm starts.

<!-- chunk {"id": "body-0348", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

In this section, we show how the sum of squares machinery can be used in a straightforward manner to contain polynomial sublevel sets (as opposed to point clouds) with a convex polynomial level set. More specifically, we are interested in the following problem: Given a basic semialgebraic set

<!-- chunk {"id": "body-0349", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

find a convex polynomial $p$ of degree $2d$ such that

<!-- chunk {"id": "body-0350", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

Moreover, we typically want the unit sublevel set of $p$ to have small volume. Note that if we could address this question, then we could also handle a scenario where the unit sublevel set of $p$ is required to contain the union of several basic semialgebraic sets (simply by containing each set separately).

<!-- chunk {"id": "body-0351", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

Convexification: In some scenarios, one may have a nonconvex outer approximation of an obstacle (e.g., obtained by the computationally inexpensive inverse moment approach of Lasserre and Pauwels as described in Section 7.3.2) and be interested in containing it with a convex set. This would e.g. make the problem of computing distances among obstacles more tractable; cf. Section 7.4.

<!-- chunk {"id": "body-0352", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

Grouping multiple obstacles: For various navigational tasks involving autonomous agents, one may want to have a mapping of the obstacles in the environment in varying levels of resolution. A relevant problem here is therefore to group obstacles: this would lead to the problem of containing several polynomial sublevel sets with one.

<!-- chunk {"id": "body-0353", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

It is straightforward to see that constraints (7.13) and (7.14) imply the required set containment criterion in (7.11). As usual, the constraint in (7.12) ensures convexity of the unit sublevel set of $p$. The objective function attempts to minimize the volume of this set. A natural choice for the degree $2\hat{d}$ of the polynomials $\tau_{i}$ is ${2\hat{d}} = {{2d} - {{\min_{i}{deg}}{(g_{i})}}}$, though better results can be obtained by increasing this parameter.

<!-- chunk {"id": "body-0354", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

An analoguous problem is discussed in recent work by Dabbene, Henrion, and Lagoa. In the paper, the authors want to find a polynomial $p$ of degree $d$ whose 1-superlevel set $\left. \{ x \middle| {{p{(x)}} \geq 1}\} \right.$ contains a semialgebraic set $\mathcal{S}$ and has minimum volume. Assuming that one is given a set $B$ containing $\mathcal{S}$ and over which the integrals of polynomials can be efficiently computed, their method involves searching for a polynomial $p$ of degree $d$ which minimizes $\int_{B}{p{(x)}{dx}}$ while respecting the constraints ${p{(x)}} \geq 1$ on $\mathcal{S}$ and ${p{(x)}} \geq 0$ on $B$. Note that the objective is linear in the coefficients of $p$ and that these last two nonnegativity conditions can be made computationally tractable by using the sum of squares relaxation.

<!-- chunk {"id": "body-0355", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

The advantage of such a formulation lies in the fact that when the degree of the polynomial $p$ increases, the objective value of the problem converges to the true volume of the set $\mathcal{S}$.

<!-- chunk {"id": "body-0356", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

Example. In Figure 7.8, we have drawn in black three random ellipsoids and a degree-4 convex polynomial sublevel set (in yellow) containing the ellipsoids. This degree-4 polynomial was the output of the optimization problem described above where the sos multipliers $\tau_{i}{(x)}$ were chosen to have degree $2$.

<!-- chunk {"id": "body-0357", "role": "body", "section": "Containment of polynomial sublevel sets", "weight": 1.0} -->

We end by noting that the formulation proposed here is backed up theoretically by the following converse result.

<!-- chunk {"id": "body-0358", "role": "body", "section": "Chapter 8 Nonnegative polynomials and shape-constrained regression", "weight": 1.0} -->

Unlike the other chapters in this thesis, the paper on which this chapter is based is still in preparation. We recommend that future readers read the submitted version of this chapter if it is available at the time of reading.

<!-- chunk {"id": "body-0359", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regression is a key problem in statistics and machine learning. Its goal is to estimate relationships between an *explained variable* (e.g., the price of a second-hand car) and a *vector of explanatory variables* (e.g., the make, brand, mileage, power, or age of this car). In many applications, one can observe a monotonous dependency between the explained variable and the explanatory variables. Examples arise in many different areas, including medicine, e.g., loss of hippocampus gray matter with respect to age or survival rate with respect to white blood cell count in patients fighting leukemia; biology and environmental engineering, e.g., frequency of occurrence of a specific plant as a function of environment pollution; electrical and computer engineering, e.g., failure rate of software as a function of number of bugs; economics, e.g., production output of a competitive firm as a function of its inputs and civil engineering, e.g., total shaded area on the floor of a room as a function of length of a blind over the window in that room, to name a few.

<!-- chunk {"id": "body-0360", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition or in parallel to monotonicity, one may also wish to impose convexity or concavity constraints on the regressor. Examples where such a need arises are given, e.g.,. They include geometric programming, computed tomography, target reconstruction, circuit design, queuing theory, and utility function estimation in economics.

<!-- chunk {"id": "body-0361", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the following, we refer to the problem of fitting a convex or monotonous regressor to data as *shape-constrained regression*. As evidenced above, this problem appears ubiquitously in applications and has consequently been widely studied. We review prior literature on both monotone and convex regression below. We focus on *polynomial* regression as this will be the subject of interest throughout this chapter.

<!-- chunk {"id": "body-0362", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

Past work on monotonically-constrained polynomial regression has by and large focused on univariate polynomials. Methods that enforce monotonicity include specific parametrizations of polynomial families (see and ) or iterative algorithms that leverage geometric properties of univariate polynomials (in for example, the derivative of the polynomial is constrained to be zero at inflection points). Extensions to multivariate polynomials involve adding univariate polynomials together to get a (separable) multivariate polynomial, which ignores interactions between explanatory variables (see ). Furthermore, all the methods considered in this paragraph impose monotonicity of the regressor globally, as opposed to over a given set, which may be too restrictive.

<!-- chunk {"id": "body-0363", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

Another way of obtaining monotonous (but not necessarily polynomial) predictive models is via the use of artificial neural networks (ANNs). The easiest way to guarantee that an ANN outputs an increasing function with respect to all features is to keep the edge weights in the neural net nonnegative, see. However, it has been shown in that in order for a neural network with nonnegative weights to approximate any monotonically increasing function in $n$ features arbitrarily well, the ANN must have $n$ fully connected hidden layers, which can lead to computational limitations and requires a large training dataset.

<!-- chunk {"id": "body-0364", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

*Interpolated look-up tables* are another popular approach to monotone regression (see, e.g., ). Here, the feature space is discretized into different cells, and each point in the feature space $x$ is associated to a vector of linear interpolation weights $\phi{(x)}$, which reflects the distance of $x$ to each vertex of the specific cell it belongs to. The function we wish to learn is then given by a linear combination of $\phi{(x)}$, i.e., ${f{(x)}} = {\theta^{T}\phi{(x)}}$, and the parameter $\theta$ is obtained by solving ${\min_{\theta}l}{(y_{i},{\theta^{T}\phi{(x_{i})}})}$, where $l$ is a convex loss function. If the entries of $\theta$ satisfy some pairwise constraints, then the function $f$ is guaranteed to be monotonous.

<!-- chunk {"id": "body-0365", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

We remark that in this approach, the size of $\theta$, and so the number of variables, is exponential in the number of features.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

Finally, we mention two other research directions which also involve breaking down the feature domain into smaller subsets. These are *regression trees* and *isotonic regression*. In the first, the feature domain is recursively partitioned into smaller subdomains, where interactions between features are more manageable. On each subdomain, a fit to the data is computed, and to obtain a function over the whole domain, the subdomain fits are aggregated, via, e.g., gradient boosting; see. To obtain monotone regressors, one enforces monotonicity on each subregion, as aggregation maintains this structural property. In the second method, a piecewise constant function $f$ is fitted to the data in such a way that ${f{(x_{i})}} \leq {f{(x_{j})}}$ if $x_{i}$ and $x_{j}$ are breakpoints of the function and $x_{i} \succeq x_{j}$, where $\succeq$ is some partial or total ordering.

<!-- chunk {"id": "body-0367", "role": "body", "section": "Prior work on monotone regression", "weight": 1.0} -->

Both of these methods present some computational challenges in the sense that, much like interpolated look-up tables, they scale poorly in the number of features. In the case of the second method, the function produced also lacks some desirable analytic properties, such as smoothness and differentiability.

<!-- chunk {"id": "body-0368", "role": "body", "section": "Prior work on convex regression", "weight": 1.0} -->

The work by Magnani, Lall, and Boyd in is the closest to what is presented in this chapter. Similarly to what is done here, a sum of squares approach to impose convexity of their polynomial regressor is used in that reference. However, contrarily to us, convexity is imposed globally, and not locally. Furthermore, our focus in this chapter is on approximation results and computational complexity analysis, which is not a focus of their work. Other methods for computationally efficient convex regression involve fitting a piecewise linear model to data. This is done, e.g.,. Other related work in the area consider convex regression from a more statistical viewpoint. The reference in for example, studies maximum likelihood estimation for univariate convex regression whereas and more recently study the multivariate case. In particular, the first two papers show consistency of the maximum likelihood estimator whereas the latter paper provides a more efficient and scalable framework for its computation.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Outline", "weight": 1.0} -->

The outline of the chapter is as follows. In Section 8.2, we specify our problem formulation in more detail. In particular, we define the notion of monotonicity profile (which encodes how the polynomial regressor varies depending on each variable) in Definition 8.2.3. ‣ 8.2 Problem formulation ‣ Chapter 8 Nonnegative polynomials and shape-constrained regression ‣ Part II Optimizing over Convex Polynomials ‣ Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming"). In Section 8.3, we show that both the problem of testing whether a polynomial has a certain monotonicity profile over a box and the problem of testing whether a polynomial is convex over a box are NP-hard already for cubic polynomials (Theorems 8.3.1 and 8.3.2). This motivates our semidefinite programming-based relaxations for fitting a polynomial that is constrained to be monotone or convex to data. These are presented in Section 8.4. Among other things, we show that any monotone (resp. convex) function can be approximated to arbitrary accuracy by monotone (resp.

<!-- chunk {"id": "body-0370", "role": "body", "section": "Outline", "weight": 1.0} -->

convex) polynomials, with sum of squares certificates of these properties (Theorems 8.4.1 and 8.4.6). In Section 8.5, we show how our methods perform on synthetic regression problems as well as real-world problems (namely predicting interest rates for personal loans and predicting weekly wages). In particular, we show that in both real-world problems, the shape-constrained regressor provides a lower root mean squared error on testing data than the unconstrained regressor.

<!-- chunk {"id": "body-0371", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In this chapter, we consider the problem of *polynomial regression*, i.e., the problem of fitting a polynomial function $p:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ to data points $(x_{i},y_{i})$, $i = {1,\ldots,m}$. Here, $x_{i}$ is a vector in ${\mathbb{R}}^{n}$, often called the *feature vector* or *vector of explanatory variables*, and $y_{i}$ is a scalar corresponding to the response. To obtain our regressor $p$, we fix its degree and search for its coefficients such that $p$ minimizes some convex loss function. This could be, e.g., the *least squares error*,

<!-- chunk {"id": "body-0372", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

or, the *least absolute deviation error*,

<!-- chunk {"id": "body-0373", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In our setting, we would additionally like to add shape constraints to our regressor, such as monotonicity or convexity. More specifically, we consider the model we outline next. We assume that $y_{i}$ is a measurement of an underlying unknown (not necessarily polynomial) function $f:{{\mathbb{R}}^{n}\mapsto{\mathbb{R}}}$ at point $x_{i}$ corrupted by some noise $\epsilon_{i}$. In other words, we have

<!-- chunk {"id": "body-0374", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We further assume that we possess prior knowledge regarding the shape of $f$, e.g., increasing in variable $j$ or convex over a certain region. We would then like our regressor $p$ to have the same attributes. This is a very natural problem when considering applications such as those discussed in the introduction of this chapter.

<!-- chunk {"id": "body-0375", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Throughout the chapter, we assume that our feature vectors $x_{i}$ belong to a *box*

<!-- chunk {"id": "body-0376", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where $b_{1}^{-},b_{1}^{+},\ldots,b_{n}^{-},b_{n}^{+}$ are real numbers satisfying ${b_{i}^{-} \leq b_{i}^{+}},{{\forall i} = {1,\ldots,n}}$. In practice, this is often, if not always, the case, as features are generally known to lie within certain ranges. We would like to mention nevertheless that the techniques presented in this chapter can be extended to any feature domain that is *basic semialgebraic*, i.e., defined by a finite number of polynomial equalities and inequalities. The shape constraints we define next are assumed to hold over this box: they are, respectively, monotonicity over $B$ with respect to a feature and convexity over $B$.

<!-- chunk {"id": "body-0377", "role": "body", "section": "Computational complexity results", "weight": 1.0} -->

As mentioned previously, we would like to optimize some convex loss function over the set of polynomial regressors constrained to be convex or monotonous over a box $B$. In this section, we show that, unless P=NP, one has no hope of doing this in a tractable fashion as even the problem of testing if a given polynomial has these properties is NP-hard.

<!-- chunk {"id": "body-0378", "role": "body", "section": "Semidefinite programming-based relaxations", "weight": 1.0} -->

In light of the previous hardness results, we provide tractable relaxations of the previous concepts, i.e., monotonocity over a box and convexity over a box, involving semidefinite programming. These relaxations are based on the notion of *sum of squares* polynomials, which we provide a brief exposition of below.

<!-- chunk {"id": "body-0379", "role": "body", "section": "Review of sum of squares polynomials", "weight": 1.0} -->

A polynomial $p$ is a sum of squares (sos) if it can be written as a sum of squares of other polynomials, i.e., ${{p{(x)}} = {\sum_{i}{q_{i}{(x)}^{2}}}},$ where $q_{i}{(x)}$ are some polynomials. Being a sum of squares is obviously a sufficient condition for nonnegativity. It is not however necessary, as the Motzkin polynomial (which is nonnegative but not sos) can attest to. Sum of squares polynomials are widely used as a surrogate for nonnegative polynomials as one can optimize over the set of sos polynomials using semidefinite programming (SDP) contrarily to nonnegative polynomials, which form an intractable set to optimize over.

<!-- chunk {"id": "body-0380", "role": "body", "section": "Review of sum of squares polynomials", "weight": 1.0} -->

The fact that one can optimize over the set of sos polynomials using semidefinite programming is the consequence of the following theorem: a polynomial $p$ of degree $2d$ is a sum of squares if and only if there exists a positive semidefinite matrix $Q$ such that ${p{(x)}} = {z{(x)}^{T}Qz{(x)}}$, where ${z{(x)}} = {(1,x_{1},\ldots,x_{n},{x_{1}x_{2}\ldots},x_{n}^{d})}$ is the vector of standard monomials of degree $\leq d$.

<!-- chunk {"id": "body-0381", "role": "body", "section": "Review of sum of squares polynomials", "weight": 1.0} -->

We say that an $m \times m$ polynomial matrix $M{(x)}$ is an *sos-matrix* if there exists a polynomial matrix $V{(x)}$ of size $q \times m$, where $q$ is some integer, such that ${M{(x)}} = {V{(x)}^{T}V{(x)}}$. This is equivalent to the polynomial $y^{T}M{(x)}y$ in $2n$ variables $(x,y)$ being a sum of squares.

<!-- chunk {"id": "body-0382", "role": "body", "section": "Relaxations and approximation results", "weight": 1.0} -->

With no constraints on the regressor, this fit can be obtained by minimizing some convex loss function such as the least squares error ${\sum_{i = 1}^{m}{({{p{(x_{i})}} - y_{i}})}^{2}}.$ Here, we consider two different cases of constrained regression, corresponding to two shape constraints on the function $f$ in (8.9) that generates the data. For concreteness, we will throughout use the least squares error as our convex loss function, though our algorithms can be extended to hold for other convex loss functions such as the least absolute deviation function or any sos-convex polynomial loss function.

<!-- chunk {"id": "body-0383", "role": "body", "section": "Monotonically-constrained polynomial regression", "weight": 1.0} -->

We assume that the monotonicity profile $\rho$ of $f$ in (8.9) as well as a box $B$ which contains the feature vectors are given. We wish to fit a polynomial $p$ to data ${{{(x_{i},y_{i})},i} = 1},{\ldots,m}$ generated using $f$, such that $p$ also has monotonicity profile $\rho$ over $B$.

<!-- chunk {"id": "body-0384", "role": "body", "section": "Monotonically-constrained polynomial regression", "weight": 1.0} -->

Theorem 8.3.1 suggests that this problem cannot be solved efficiently unless $P = {NP}$. We present here a relaxation of this problem with some formal guarantees.

<!-- chunk {"id": "body-0385", "role": "body", "section": "Remark 8.4.4", "weight": 1.0} -->

The format of the sum of squares certificate of positivity of $p$ over the box $B$ depends on the representation that one uses to represent the box. If the box had been defined instead as

<!-- chunk {"id": "body-0386", "role": "body", "section": "Remark 8.4.4", "weight": 1.0} -->

satisfy the Archimdean property as well.

<!-- chunk {"id": "body-0387", "role": "body", "section": "Remark 8.4.4", "weight": 1.0} -->

We have chosen to use the formulation given in (8.12) rather than the one in (8.13) as one need only search for $n$ sos polynomials in (8.12) rather than $2n$, in (8.13).

<!-- chunk {"id": "body-0388", "role": "body", "section": "Polynomial regressors constrained to be convex", "weight": 1.0} -->

In this section, we assume that it is known that $f$ is convex over a box $B$, which is given to us. The goal is then to fit a polynomial $p$ to the data ${{{(x_{i},y_{i})},i} = 1},{\ldots,m}$ such that $p$ is also convex over $B$.

<!-- chunk {"id": "body-0389", "role": "body", "section": "Polynomial regressors constrained to be convex", "weight": 1.0} -->

Again, Theorem 8.3.2 suggests that this problem cannot be solved efficiently unless ${P = {NP}}.$

<!-- chunk {"id": "body-0390", "role": "body", "section": "Cases where the semidefinite programming-based relaxations are exact", "weight": 1.0} -->

In Corollaries 8.4.5 and 8.4.8, we have replaced the original problem of finding polynomial regressors which are convex or monotone over $B$ with sum of squares-based relaxations. In both cases, we have asymptotic guarantees on the quality of these relaxations, i.e., we are guaranteed to recover the solutions of (8.10) and (8.15) if the degree of the sos polynomials involved is arbitrarily high. (We remark that no explicit bound on this degree can be given as a function of the number of variables and the degree only.) In two particular cases (which we cover below), one can in fact come up with semidefinite programming-based relaxations which are *exact*: this means that the degree of the sum of squares polynomials needed to recover the true solution is explicitly known. Hence, one can write a semidefinite program that exactly solves (8.10) and (8.15). We review these two cases below.

<!-- chunk {"id": "body-0391", "role": "body", "section": "The quadratic case", "weight": 1.0} -->

In this particular case, we wish to solve (8.10) and (8.15) with $d = 2$.

<!-- chunk {"id": "body-0392", "role": "body", "section": "The quadratic case", "weight": 1.0} -->

We first consider the case where we would like to constrain $p$ to have a certain monotonicity profile, i.e., we would like to solve (8.10). As $p$ is quadratic, each of its partial derivatives is a linear function. Requiring that a linear function be nonnegative over a box can be done using the following lemma, which is a variant of the Farkas lemma.

<!-- chunk {"id": "body-0393", "role": "body", "section": "The separable case", "weight": 1.0} -->

Recall that a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is said to be separable if

<!-- chunk {"id": "body-0394", "role": "body", "section": "The separable case", "weight": 1.0} -->

We first consider the case where we would like to solve (8.10), assuming that $p$ is separable, i.e., ${p{(x)}} = {\sum_{i = 1}^{n}{p_{i}{(x_{i})}}}$. Note that we have

<!-- chunk {"id": "body-0395", "role": "body", "section": "The separable case", "weight": 1.0} -->

In other words, one can replace (8.10) by

<!-- chunk {"id": "body-0396", "role": "body", "section": "The separable case", "weight": 1.0} -->

where $x_{j}\mapsto{p_{j}^{\prime}{(x_{j})}}$ is a univariate polynomial. We then use the following lemma.

<!-- chunk {"id": "body-0397", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We now provide some illustrations of our methods on different datasets. In the first part of this section, we consider synthetic datasets. This will enable us to compare the advantages and limitations of our relaxations in terms of performance metrics such as training and testing accuracy, robustness, flexibility and scalability. In the second part of this section, we look at how our methods perform on real-life datasets.

<!-- chunk {"id": "body-0398", "role": "body", "section": "Synthetic regression problems", "weight": 1.0} -->

For the synthetic experiments, we analyze the performance of 4 different algorithms: UPR, which corresponds to unconstrained polynomial regression, MCPR, which corresponds to polynomial regression with monotonicity constraints, CCPR which corresponds to polynomial regression with convexity constraints, and MCPR+CCPR, which corresponds to polynomial regression with both monotonicity and convexity constraints. The underlying function for this experiment as described in (8.9)

<!-- chunk {"id": "body-0399", "role": "body", "section": "Synthetic regression problems", "weight": 1.0} -->

The function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is monotonically increasing in all directions, thus, it has a monotonicity profile $\rho_{i} = {1,{\forall i}}$. Furthermore, $f$ is convex.

<!-- chunk {"id": "body-0400", "role": "body", "section": "Data Generation", "weight": 1.0} -->

We denote by $X$ the feature matrix, i.e., the matrix obtained by concatenating the $m$ feature vectors $x_{i}$ of length $n$. Each column or $X$ corresponds to a feature and each row is an observation of all the $n$ features. Hence, $X$ is an $m \times n$ matrix. For our synthetic datasets, we generate each entry of $X$ uniformly at random in an interval $\lbrack b^{-},b^{+}\rbrack$, where $b^{-} = 0.5$ and $b^{+} = 2$. The feature domain in this case is taken to be

<!-- chunk {"id": "body-0401", "role": "body", "section": "Data Generation", "weight": 1.0} -->

We compute the response variable $y_{i}$ by evaluating $f$ at each column $x_{i}$ of $X$, which we corrupt by some noise, whose scaling $\epsilon$ we vary in order to test for robustness. As a consequence, if we denote by $y$ the $m \times 1$ vector containing $y_{1},\ldots,y_{m}$ and by $f{(X)}$ the $m \times 1$ vector obtained by applying $f$ to each row of $X$, we have ${y = {{f{(X)}} + \epsilon}},$ where $\epsilon$ is a vector with each entry taken to be iid and Gaussian of mean zero and standard deviation $\alpha\sqrt{var{({f{(X)}})}}$.

<!-- chunk {"id": "body-0402", "role": "body", "section": "Data Generation", "weight": 1.0} -->

Here $var{({f{(X)}})}$ is the variance of the set of random points obtained when varying the input $X$ to $f$ and $\alpha$ is a fixed constant, which we use to parametrize noise (e.g., $\alpha = 1$ is low noise, whereas $\alpha = 10$ is high noise).

<!-- chunk {"id": "body-0403", "role": "body", "section": "Data Generation", "weight": 1.0} -->

In the following, we wish to fit a polynomial $p$ of degree $d$ to the data, such that the mean squared error (which is a normalization of the least squared error)

<!-- chunk {"id": "body-0404", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

One of the biggest drawbacks of unconstrained polynomial regression is the algorithmic instability to noise. Here we want to compare the four algorithms listed above with respect to robustness to noise. To do this, we fit polynomials of varying degrees to the data in both high-noise ($\alpha = 10$ as described previously) and low-noise ($\alpha = 1$) settings. We then compare the Root Mean Squared Error (RMSE)

<!-- chunk {"id": "body-0405", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

on the testing and training samples. The results are given in Figure 8.5. Note that the thin light blue constant line listed as "Reference" is the reference RMSE, i.e., the value obtained when one computes the RMSE for the function $f$ itself.

<!-- chunk {"id": "body-0406", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(a) Comparison of RMSE on the training set in a low noise setting

<!-- chunk {"id": "body-0407", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(b) Comparison of RMSE on the testing set in a low noise setting

<!-- chunk {"id": "body-0408", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(c) Comparison of RMSE on the training set in a high noise setting

<!-- chunk {"id": "body-0409", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(d) Comparison of RMSE on the testing set in a high noise setting

<!-- chunk {"id": "body-0410", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

As expected, from Figure 8.5, we see that UPR tends to overfit. This can be observed by comparing the RMSE of UPR to the Reference RMSE: anything below the reference can be considered to be overfitting. Note that for both training sets, and particularly when the degree of the polynomials is high, the data points corresponding to UPR are well below those given by the Reference. Introducing monotonicity or convexity constraints improves both the accuracy on the test data as well as robustness to noise, in the sense that the RMSE of these algorithms remains moderate, even in high noise environments. When both monotonicity and convexity are imposed, the benefits compound. Indeed, MCPR+CCPR has similar performance for both the testing and the training data, and the RMSE obtained with this algorithm is the closest to the reference line. Note that MCPR+CCPR performs well both in low noise as well as high noise settings, which indicates the ability to robustly learn the true underlying distribution.

<!-- chunk {"id": "body-0411", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

Lastly we compare qualitatively the robustness of UCR, MCPR, CCPR, and MCPR+CCPR with respect to the true underlying function. The plots in Figure 8.6 are obtained by projecting the 4 fitted functions and the underlying function onto one of the features (this is done by fixing all the other features to some arbitrary values in their range). We consider the case where the polynomials are of degree $4$ and of degree $7$.

<!-- chunk {"id": "body-0412", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(a) Projections of degree 4 fits and the underlying function in a low noise setting

<!-- chunk {"id": "body-0413", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(b) Projections of degree 7 fits and the underlying function in a low noise setting

<!-- chunk {"id": "body-0414", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(c) Projections of degree 4 fits and the underlying function in a high noise setting

<!-- chunk {"id": "body-0415", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

(d) Projections of degree 7 fits and the underlying function in a high noise setting

<!-- chunk {"id": "body-0416", "role": "body", "section": "Comparative performance", "weight": 1.0} -->

The results obtained confirm our previous observations. First, UPR tends to overfit, particularly when the noise scaling factor is high and when the degree of the polynomial fit is large (this is because, as the degree increases, the polynomials gain in expressiveness). Having monotonicity and convexity constraints proves to be a very efficient way of regularizing the polynomial fit, even in high noise settings: the fits obtained are very close to the true function. Furthermore, though their performance does deteriorate slightly in the high noise and high degree regime, the overall shape of the projection stays close to that of the underlying function, and that of lower degrees. This in contrast to the unconstrained fit whose shape is very unstable when the degree and the noise varies.

<!-- chunk {"id": "body-0417", "role": "body", "section": "Applications to real regression problems", "weight": 1.0} -->

In this section we present two applications of our methods to real datasets. Our first example uses monotonically constrained polynomial regression (MPCR) to predict interest rates for personal loans. The second example is a hybrid regression setting with a mixture of monotonicity and convexity constraints which is used to predict weekly wages from a set of features.

<!-- chunk {"id": "body-0418", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

In this subsection, we study data for loans issued between the years 2007-2011 by Lending Club. We decided to focus on the particular category of home loans so as to avoid having to deal with categorical variables such as loan type. The updated dataset has $N = 3707$ observations and 32 numerical features. Though the MCPR algorithm has run time polynomial in the number of features, we encounter issues with memory for too large a number of features. Hence, some data preprocessing is necessary to reduce the number of features. This was done by eliminating highly correlated covariates and running some canonical feature selection procedures. In the end, we consider six features. The response variable in this case is the interest rate on home loans.

<!-- chunk {"id": "body-0419", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

dti:+1 - Ratio of the borrower's total monthly debt payments an the self-reported monthly income. A borrower with high dti is perceived to be riskier, which typically corresponds to higher interest rates.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

delinq_2yrs:+1 - The number of past-due delinquencies in the past 2 years. The interest rate is monotonically increasing with respect to the number of delinquencies.

<!-- chunk {"id": "body-0421", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

pub_rec:+1 - Number of derogatory public records. The interest rate is monotonically increasing with respect to this feature.

<!-- chunk {"id": "body-0422", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

out_prncp:+1 - Remaining outstanding principal. This feature has a monotonically increasing relationship with the interest rate.

<!-- chunk {"id": "body-0423", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

total_rec_prncp:-1 - Principal received to date with a monotonically decreasing dependency.

<!-- chunk {"id": "body-0424", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

total_rec_int:-1 - Interest received to date. The interest rate is monotonically decreasing with respect to this feature.

<!-- chunk {"id": "body-0425", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

We compute the average RMSE for testing and training sets through a 10-fold cross validation. We compare in Figure 8.7 the results for fitting polynomials of different degrees in both the unconstrained and monotonically constrained settings.

<!-- chunk {"id": "body-0426", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

(a) Values taken by the RMSE on training data

<!-- chunk {"id": "body-0427", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

(b) Values taken by the RMSE on testing data

<!-- chunk {"id": "body-0428", "role": "body", "section": "Predicting interest rates for personal loans", "weight": 1.0} -->

The best performance was achieved by a degree 4, monotonically constrained polynomial regression with average RMSE of $4.09$ and standard error of $0.20$. Already for degree $5$, the unconstrained regression runs into numerical problems as it becomes rank deficient, i.e., the number of coefficients that needs to be determined is larger than the number of data points. Therefore, monotonicity constraints can be an efficient way of ensuring robustness in settings where the number of datapoints is relatively small, but the relationship between the covariates is complex.

<!-- chunk {"id": "body-0429", "role": "body", "section": "Predicting weekly wages", "weight": 1.0} -->

In this section, we analyze data from the 1988 Current Population Survey. This data is freely available under the name ex1029 in the Sleuth2 R package. The data contains $N = 25361$ observations and 2 numerical features: years of experience and years of education. We expect wages to increase with respect to years of education and be concave with respect to years of experience. We compare the performance of this hybrid constrained regression problem with the unconstrained case, as well as the CAP algorithm proposed by Hannah. Similarly to the previous example we compute the RMSEs with 10-fold cross validation. In addition we time our algorithm in order to compare the runtimes with the CAP algorithm. The results are presented in Figure 8.8.

<!-- chunk {"id": "body-0430", "role": "body", "section": "Predicting weekly wages", "weight": 1.0} -->

(a) Values taken by the RMSE on training data

<!-- chunk {"id": "body-0431", "role": "body", "section": "Predicting weekly wages", "weight": 1.0} -->

(b) Values taken by the RMSE on testing data

<!-- chunk {"id": "body-0432", "role": "body", "section": "Predicting weekly wages", "weight": 1.0} -->

The best performing algorithm is the monotonically and convexly constrained degree 2 polynomial with average test RMSE: $250.0$ and standard error $39.2$. The algorithm with the smallest standard error, therefore the one with the most consistent performance is the degree 3 hybrid polynomial with test RMSE: $285.0 \pm 29.9$. In comparison, the CAP and Fast CAP algorithm have test RMSE: $385.7 \pm 20.8$. Our algorithm does not only perform better in terms of RMSE, it also has a better runtime performance. For the degree 2 hybrid regression, the run time is $0.24 \pm 0.01$ seconds, and for degree 3, the hybrid regresion runtime is $0.26 \pm 0.01$ seconds. In contrast, the CAP algorithm takes $12.8 \pm 0.8$ seconds and the Fast CAP algorithm takes $1.9 \pm 0.2$ seconds.
