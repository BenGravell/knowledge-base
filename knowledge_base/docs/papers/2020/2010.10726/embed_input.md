<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MINVO Basis: Finding Simplexes with Minimum Volume Enclosing Polynomial Curves

Topics include MINVO basis, Sum-of-squares programming, SOS.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper studies the polynomial basis that generates the smallest n-simplex enclosing a given n^(th)-degree polynomial curve in R^(n). Although the Bernstein and B-Spline polynomial bases provide feasible solutions to this problem, the simplexes obtained by these bases are not the smallest possible, which leads to overly conservative results in many CAD (computer-aided design) applications. We first prove that the polynomial basis that solves this problem (MINVO basis) also solves for the n^(th)-degree polynomial curve with largest convex hull enclosed in a given n-simplex. Then, we present a formulation that is independent of the n-simplex or n^(th)-degree polynomial curve given. By using Sum-Of-Squares (SOS) programming, branch and bound, and moment relaxations, we obtain high-quality feasible solutions for any ninmathbbN, and prove (numerical) global optimality for n = 1, 2, 3 and (numerical) local optimality for n = 4.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results obtained for n = 3 show that, for any given 3^(rd)-degree polynomial curve in R^, the MINVO basis is able to obtain an enclosing simplex whose volume is 2.36 and 254.9 times smaller than the ones obtained by the Bernstein and B-Spline bases, respectively. When n = 7, these ratios increase to 902.7 and 2.997*10^, respectively.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Polyhedral enclosures of a given polynomial curve have a crucial role in a large number of CAD algorithms to compute curve intersections, perform ray tracing, or obtain minimum distances between convex shapes. These polyhedral enclosures are also used in rasterization, mesh generation, path planning for numerical control machines, and trajectory optimization for robots. Many of these works leverage the convex hull property of the Bernstein basis (polynomial basis used by Bézier curves) to obtain these polyhedral enclosures, although some works use the B-Spline basis instead.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although both the Bernstein basis and B-Spline basis have many useful properties, they are not designed to generate the smallest $n$-simplex that encloses a given $n^{\text{th}}$-degree polynomial curve in ${\mathbb{R}}^{n}$. This directly translates into undesirably conservative results in many of the aforementioned applications. Polyhedral enclosures with more than $n + 1$ vertices (i.e., not simplexes) can provide tighter volume approximations, but at the expense of a larger number of vertices, which can eventually increase the computation time in real-time applications. The main focus of this paper is therefore on simplex enclosures.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, and rather than designing an iterative algorithm that needs to be run for each different curve to obtain the smallest simplex enclosure, this paper studies a novel polynomial basis that is designed by construction to minimize the volume of this simplex. Compared to an iterative algorithm, this basis benefits from the properties of *linearity* (the simplex is a linear transformation of the coefficient matrix of the curve, avoiding therefore the need of expensive iterative algorithms) and *independence with respect to the curve* (the matrix that defines this linear transformation is the same one for all the curves of the same degree). These two properties are highly desirable in real-time computing and/or when used in an optimization problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, this paper studies the polynomial basis that generates the $n$-simplex with minimum volume enclosing a given $n^{\text{th}}$-degree polynomial curve. Additionally, we also investigate the related problem of obtaining the $n^{\text{th}}$-degree polynomial curve with largest convex hull enclosed in a given $n$-simplex.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formulation of the optimization problem whose minimizer is the polynomial basis that generates the smallest $n$-simplex that encloses any given $n^{\text{th}}$-degree polynomial curve. We show that this basis also obtains the $n^{\text{th}}$-degree polynomial curve with largest convex hull enclosed in any given $n$-simplex. Another formulation that imposes a specific structure on the polynomials of the basis is also presented.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive high-quality feasible solutions for any $n \in {\mathbb{N}}$, obtaining simplexes that, for $n = 3$, are $2.36$ and $254.9$ times smaller than the ones obtained using the Bernstein and B-Spline bases respectively. For $n = 7$, these values increase to 902.7 and $2.997 \cdot 10^{21}$, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerical global optimality (with respect to the volume) is proven for $n = {1,2,3}$ using SOS, branch and bound, and moment relaxations. Numerical local optimality is proven for $n = 4$, and feasibility is guaranteed for $n \geq 5$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extension to polynomial curves embedded in subspaces of higher dimensions, and to some rational curves.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Volume of the Convex Hull of a Polynomial Curve", "weight": 1.0} -->

Note that, as the curve $P$ satisfies $n = m = k$ (see Section 3.1), the volume of its convex hull is nonzero and therefore $\left| {\mathbf{P}}_{{:,0}:{n - 1}} \right| \neq 0$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problems definition", "weight": 1.0} -->

As explained in Section 1, the goal of this paper is to find the smallest simplex $S \in \mathcal{S}^{n}$ enclosing a given polynomial curve $P \in \mathcal{P}^{n}$, and to find the polynomial curve $P \in \mathcal{P}^{n}$ with largest convex hull enclosed in a given simplex $S \in \mathcal{S}^{n}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Given $P \\in \\mathcal{P}^{n}$, find $S \\in \\mathcal{S}^{n}$", "weight": 1.0} -->

For $n = 2$, Problem 1 tries to find the triangle with the smallest area that contains a planar $2^{\text{nd}}$-degree polynomial curve. For $n = 3$, it tries to find the tetrahedron with the smallest volume that contains a $3^{\text{rd}}$-degree polynomial curve in 3D. Similar geometric interpretations apply for higher $n$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Given $P \\in \\mathcal{P}^{n}$, find $S \\in \\mathcal{S}^{n}$", "weight": 1.0} -->

Letting $f_{1}$ denote the objective function of this problem, we have that $f_{1}:={\text{vol}{(S)}} \propto {\text{abs}\left( \left| \begin{bmatrix}
\end{bmatrix} \right| \right)}$. Note that, as the volume of the convex hull of $P$ is nonzero (see Section 3.2), then it is guaranteed that $\left| \begin{bmatrix}
\end{bmatrix} \right| \neq 0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Given $S \\in \\mathcal{S}^{n}$, find $P \\in \\mathcal{P}^{n}$", "weight": 1.0} -->

By the definition of a simplex (see Section 3.1), its vertices are affinely independent and therefore the matrix of vertices of the given simplex $S$ satisfies $\left| \begin{bmatrix}
\end{bmatrix} \right| \neq 0$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Given $S \\in \\mathcal{S}^{n}$, find $P \\in \\mathcal{P}^{n}$", "weight": 1.0} -->

Now note that the optimal solution for this problem is guaranteed to satisfy $\left| {\mathbf{P}}_{{:,0}:{n - 1}} \right| \neq 0$, which can be easily proven by noting that we are maximizing the absolute value of $\left| {\mathbf{P}}_{{:,0}:{n - 1}} \right|$, and that there exists at least one feasible solution (for example the Bézier curve whose control points are the vertices of $S$) with $\left| {\mathbf{P}}_{{:,0}:{n - 1}} \right| \neq 0$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Equivalent Formulation", "weight": 1.0} -->

Let us now study the constraints and the objective functions of Problems 1 and 2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Constraints of Problems 1 and 2", "weight": 1.0} -->

Both problems share the same constraint $P \subset S$ (i.e.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Constraints of Problems 1 and 2", "weight": 1.0} -->

Hence, $\lambda_{i}{(t)}$ represents the ratio between the distance from the point ${\mathbf{p}}{(t)}$ of the curve to the hyperplane ${\mathbf{π}}_{i}$ and the distance from ${\mathbf{v}}_{i}$ to that hyperplane ${\mathbf{π}}_{i}$ (see Figure 1 for the case $n = 3$)^11^1Note that multiplying numerator and denominator of Eq. 2 by the area of the facet that lies on the plane ${\mathbf{π}}_{i}$, each $\lambda_{i}{(t)}$ can also be defined as a ratio of volumes, as..

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constraints of Problems 1 and 2", "weight": 1.0} -->

Note that $\mathbf{A}$ is a ${({n + 1})} \times {({n + 1})}$ matrix whose $i^{\text{th}}$ row contains the coefficients of the polynomial $\lambda_{i}{(t)}$ in decreasing order. The second and third constraints of Eq. 1 can be rewritten as ${{\mathbf{A}}^{T}\mathbf{1}} = {\mathbf{e}}$ and ${{\mathbf{A}}{\mathbf{t}}} \geq {0{\forall t}} \in {\lbrack{- 1},1\rbrack}$ respectively. We conclude therefore that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Objective Function of Problem 1", "weight": 1.0} -->

Using the constraints in Eq. 3, and noting that the matrix $\mathbf{A}$ is invertible (as proven in B), we can write

<!-- chunk {"id": "body-0023", "role": "body", "section": "Objective Function of Problem 1", "weight": 1.0} -->

where we have used the fact that everything inside $\begin{bmatrix}
\end{bmatrix}$ is given (i.e., not a decision variable of the optimization problem), and the fact that $|{\mathbf{A}}| = {|{\mathbf{A}}^{T}|}$. We can therefore minimize $- {\text{abs}\left( |{\mathbf{A}}| \right)}$. Note that now the objective function $f_{1}$ is independent of the given curve $P$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Objective Function of Problem 2", "weight": 1.0} -->

Similar to the previous subsection, and noting that $\mathbf{V}$ is given in Problem 2, we have that

<!-- chunk {"id": "body-0025", "role": "body", "section": "Objective Function of Problem 2", "weight": 1.0} -->

and therefore the objective function $f_{2}$ is now independent of the given simplex $S$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

Note that now the dependence on the given polynomial curve (for Problem 1) or on the given simplex (for Problem 2) appears only in the constraint ${\mathbf{P}} = {{\mathbf{V}}{\mathbf{A}}}$. As $\mathbf{A}$ is invertible (see B), we can safely remove this constraint from the optimization, leaving $\mathbf{A}$ as the only decision variable, and then use ${\mathbf{P}} = {{\mathbf{V}}{\mathbf{A}}}$ to obtain $\mathbf{V}$ (for Problem 1) or $\mathbf{P}$ (for Problem 2). We end up therefore with the following optimization problem^22^2Note that in the objective function of Problem 3 the $\text{abs}{( \cdot )}$ is not necessary, since any permutation of the rows of $\mathbf{A}$ will change the sign of $|{\mathbf{A}}|$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

We keep it simply for consistency purposes, since later in the solutions we will show a specific order of the rows of $\mathbf{A}$ for which (for some $n$) $|{\mathbf{A}}| < 0$, but that allows us to highlight the similarities and differences between this matrix and the ones the Bernstein and B-Spline bases use.:

<!-- chunk {"id": "body-0028", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

*Remark:* As detailed above, Problem 3 does not depend on the specific given $n^{\text{th}}$-degree polynomial curve (for Problem 1) or on the specific given $n$-simplex (for Problem 2). Hence, its optimal solution ${\mathbf{A}}^{\ast}$ for a specific $n$ can be applied to obtain the optimal solution of Problem 1 for any given polynomial curve $P \in \mathcal{P}^{n}$ (by using ${\mathbf{V}}^{\ast} = {{\mathbf{P}}\left( {\mathbf{A}}^{\ast} \right)^{- 1}}$) and to obtain the optimal solution of Problem 2 for any given simplex $S \in \mathcal{S}^{n}$ (by using ${\mathbf{P}}^{\ast} = {{\mathbf{V}}{\mathbf{A}}^{\ast}}$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

As the objective function of Problem 3 is the determinant of the nonsymmetric matrix $\mathbf{A}$, it is clearly a nonconvex problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

Note that the *if and only if* condition applies because $\lambda_{i}{(t)}$ is a univariate polynomial. The decisions variables would be the positive semidefinite matrices ${\mathbf{W}}_{i}$ and ${\mathbf{V}}_{i}$, $i = {0,\ldots,n}$. Another option is to use the Markov--Lukács Theorem (\[54, Theorem 1.21.1\],\[55, Theorem 2.2\],):

<!-- chunk {"id": "body-0031", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

‣ 9 Final Remarks ‣ 8 Comparison with SLEFEs ‣ 7.2 Rational Curves ‣ 7 MINVO basis applied to other curves ‣ 6.2 Results for 𝑛>7 ‣ Table 5 ‣ 6.1 Results for 𝑛={1,2,…,7} ‣ 6 Results ‣ MINVO Basis: Finding Simplexes with Minimum Volume Enclosing Polynomial Curves") we derive the Karush--Kuhn--Tucker (KKT) conditions of Problem 3 using this theorem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

Regardless of the choice of the representation of the constraint ${{\mathbf{A}}{\mathbf{t}}} \geq {\mathbf{0}{\forall t}} \in {\lbrack{- 1},1\rbrack}$ (SOS or the Markov--Lukács Theorem), no generality has been lost so far. However, these formulations easily become intractable for large $n$ due to the high number of decision variables. We can reduce the number of decision variables of Problem 3 by imposing a structure in $\lambda_{i}{(t)}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

As Problem 1 is trying to minimize the volume of the simplex, we can impose that the facets of the $n$-simplex be tangent to several internal points ${\mathbf{p}}{(t)}$ of the curve (with $t \in {({- 1},1)}$), and in contact with the first and last points of the curve (${\mathbf{p}}{({- 1})}$ and ${\mathbf{p}}{}$). Using the geometric interpretation of the $\lambda_{i}{(t)}$ given in Section 5.1, this means that each $\lambda_{i}{(t)}$ should have either real double roots in $t \in {({- 1},1)}$ (where the curve is tangent to a facet), and/or roots at $t \in {\{{- 1},1\}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

These conditions, together with an additional symmetry condition between different $\lambda_{i}{(t)}$, translate into the formulation shown in Problem 4, in which the decisions variables are the roots of $\lambda_{i}{(t)}$ and the coefficients $b_{i}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

Letting $f_{i}$ denote the objective function of Problem $i$, the relationship between Problems 1, 2, 3 and 4 is given in Figure 2. First note that the constraints and structure imposed on $\lambda_{i}{(t)}$ in Problem 4 guarantee that they are nonnegative for $t \in {\lbrack{- 1},1\rbrack}$ and that they sum up to 1. Hence the feasible set of Problem 4 is contained in the feasible set of Problem 3, and therefore, $f_{3}^{\ast} \leq f_{4}^{\ast}$ holds.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Equivalent Formulation for Problems 1 and 2", "weight": 1.0} -->

The matrix $\mathbf{A}$ found in Problem 3 or 4 can be used to find the vertices of the simplex in Problem 1 (by simply using ${\mathbf{V}} = {{\mathbf{P}}({\mathbf{A}})^{- 1}}$, where $\mathbf{P}$ is the coefficient matrix of the polynomial curve given), or to find the coefficient matrix of the polynomial curve in Problem 2 (by using ${\mathbf{P}} = {{\mathbf{V}}{\mathbf{A}}}$, where $\mathbf{V}$ contains the vertices of the given simplex).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Using the nonconvex solvers *fmincon* and *SNOPT* (with the *YALMIP* interface ), we were able to find NLO solutions for Problem 4 for $n = {1,2,\ldots,7}$, and the same NLO solutions were found in Problem 3 for $n = {1,2,3,4}$. Problem 3 and 4 become intractable for $n \geq 5$ and $n \geq 8$ respectively. The optimal matrices $\mathbf{A}$ found are shown in Table 3, and are denoted as ${\mathbf{A}}_{\text{MV}}$^33^3Note that any permutation in the rows of ${\mathbf{A}}_{\text{MV}}$ will not change the objective value, since only the sign of the determinant is affected.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Despite this multiplicity of solutions, we will refer to any matrix shown in Table 3 as, e.g., the optimal solution ${\mathbf{A}}_{\text{MV}}$, the feasible solution ${\mathbf{A}}_{\text{MV}}$, etc.. Their determinants $\left| {\mathbf{A}}_{\text{MV}} \right|$ are also compared with the one of the Bernstein and B-Spline matrices (denoted as ${\mathbf{A}}_{\text{Be}}$ and ${\mathbf{A}}_{\text{BS}}$ respectively). The corresponding plots of the MINVO basis functions are shown in Figure 3, together with the Bernstein, B-Spline and Lagrange bases for comparison.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

All of these bases satisfy ${\sum_{i = 0}^{n}{\lambda_{i}{(t)}}} = 1$, and the MINVO, Bernstein, and B-Spline bases also satisfy ${\lambda_{i}{(t)}} \geq {0{\forall t}} \in {\lbrack{- 1},1\rbrack}$. The roots of each of the MINVO basis functions $\lambda_{i}{(t)}$ for $n = {1,\ldots,7}$ are shown in Table 2 and plotted in Figure 9.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(a) For any given curve P ∈ 𝒫2, the MINVO basis finds an enclosing 2-simplex that is 1.3 and 5.2 times smaller than the one found by the Bernstein and B-Spline bases respectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(b) For any given 2-simplex, the MINVO basis finds a curve P ∈ 𝒫2 inscribed in the simplex, and whose convex hull is 1.3 and 5.2 times larger than the one found by the Bernstein and B-Spline bases respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(a) For any given 3rd-degree polynomial curve, the MINVO basis finds an enclosing 3-simplex that is 2.36 and 254.9 times smaller than the one found by the Bernstein and B-Spline bases respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(b) For any given 3-simplex, the MINVO basis finds a 3rd-degree polynomial curve inscribed in the simplex, and whose convex hull is 2.36 and 254.9 times larger than the one found by the Bernstein and B-Spline bases respectively.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

One natural question to ask is whether the basis found constitutes a global minimizer for either Problem 3 or Problem 4. To answer this, first note that both Problem 3 and Problem 4 are polynomial optimization problems. Therefore, we can make use of Lasserre's moment method, and increase the order of the moment relaxation to find tighter lower bounds of the original nonconvex polynomial optimization problem. Using this technique, we were able to obtain, for $n = {1,2,3}$ and for Problem 4, the same objective value as the NLO solutions found before, proving therefore numerical global optimality for these cases. For Problem 3, the moment relaxation technique becomes intractable due to the high number of variables. Hence, to prove numerical global optimality in Problem 3 we instead use the branch-and-bound algorithm, which proves global optimality by reducing to zero the gap between the upper bounds found by a nonconvex solver and the lower bounds found using convex relaxations. This technique proved to be tractable for cases $n = {1,2,3}$ in Problem 3, and zero optimality gap was obtained.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(a) Simplexes found by the MINVO basis for four different given 3rd-degree polynomial curves (Problem 1).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

(b) Polynomial curves (and their convex hulls in blue) obtained using the MINVO basis for four different given 3-simplexes (Problem 2).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

The matrices ${\mathbf{A}}_{\text{MV}}$ found for $n = {1,2,3}$ are (numerical) global optima of both Problem 3 and Problem 4.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

The matrix ${\mathbf{A}}_{\text{MV}}$ found for $n = 4$ is at least a (numerical) local optimum of both Problem 3 and Problem 4.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

The matrices ${\mathbf{A}}_{\text{MV}}$ found for $n = {5,6,7}$ are at least (numerical) local optima for Problem 4, and are at least feasible solutions for Problem 3.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

The geometric interpretation of Problem 3 (for $n = 2$) is shown in Figure 4. The rows of $\mathbf{A}$ are vectors that lie in the cone of the polynomials that are nonnegative in $t \in {\lbrack{- 1},1\rbrack}$ (and whose frontier is shown in orange in the figure). As Problem 3 is maximizing the volume of the parallelepiped spanned by these vectors, the optimal minimizer is obtained in the frontier of the cone, while guaranteeing that the sum of these vectors is $\begin{bmatrix}

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

In Figure 5 we check that the centroids of each of the facets of the simplex belongs to $\text{conv}(P)$, which is a necessary condition for that simplex to be minimal. Note also that $\text{conv}(P)$ is tangent to the simplex along four lines (in blue in the figure), and that the contact points of the curve with the simplex happen at the roots of the MINVO basis functions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

When the polynomial curve is given (i.e., Problem 1), the ratio between the volume of the simplex $S_{\alpha}$ obtained by a basis $\alpha$ and the volume of the simplex $S_{\beta}$ obtained by a basis $\beta$ (${\alpha,\beta} \in {\{\text{MV},\text{Be},\text{BS}\}}$) is given by

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Similarly, when the simplex is given (i.e., Problem 2), the ratio between the volume of the convex hull of the polynomial curve $P_{\alpha}$ found by a basis $\alpha$ and the volume of the convex hull of the polynomial curve $P_{\beta}$ found by a basis $\beta$ (${\alpha,\beta} \in {\{\text{MV},\text{Be},\text{BS}\}}$) is given by

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For $n = 3$, the MINVO basis finds a simplex that has a volume (a polynomial curve whose convex hull has a volume) $\approx 2.36$ and $\approx 254.9$ times smaller (larger) than the one the Bernstein and B-Spline bases find respectively.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For $n = 7$, the MINVO basis finds a simplex that has a volume (a polynomial curve whose convex hull has a volume) $\approx 902.7$ and $\approx {2.997 \cdot 10^{21}}$ times smaller (larger) than the one the Bernstein and B-Spline bases find respectively.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

An analogous reasoning applies to the volume ratios of other $n$. These comparisons are shown in Figure 7 (for $n = 2$), and in Figure 7 (for $n = 3$). More examples of the MINVO bases applied to different polynomial curves and simplexes are shown in Figure 8.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

In all the cases (and for any m): there are n + 1 control points, and conv(control points) is a polyhedron ⊂ ℳ ⊆ ℝk that encloses the curve and that has at most n + 1 vertices.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

In and below the diagonal: When n = m, the polyhedron is an n-simplex embedded in ℝk that is at least numerically globally optimal (NGO), numerically locally optimal (NLO), or feasible (F).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

In Section 6.1, we obtained the results for n = 1, …, 7 by using the optimization problems. However, solving these problems becomes intractable when n &gt; 7. To address this problem, we present a model that finds high-quality feasible solutions by extrapolating for n &gt; 7 the pattern found for the roots of the MINVO basis (see the cases n = 1, …, 7 in Figure 9). Specifically, and noting that the double roots for a degree n tend to be distributed in n clusters, we found that the MINVO double roots in the interval (−1,1) for the degree n can be approximated by

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

where $s_{j,n}:=\left\lfloor \frac{n + {\text{odd}(j,n)}}{2} \right\rfloor$ models the number of roots per cluster j ∈ {0, …, (n−1)}, and k ∈ {0, …, (sj, n−1)} is the index of the root inside a specific cluster444The intuition behind the design of Eq. 4 is as follows: The $\sin\left( \frac{\cdot}{n + \cdot} \right)$ forces every root to be in [−1, 1], and makes the centers of the clusters more densely distributed near the extremes t ∈ {−1, 1}, and less around t = 0. The numerator inside the sin (⋅) is a weighted sum of the index of the root inside the cluster (centered around $\frac{s_{j,n} - 1}{2}$), and the index of the cluster (centered around $\frac{n - 1}{2}$).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Finally, note that, by construction, this formula enforces symmetry with respect to t = 0.. Here, c0 ≈ 0.2735, c1 ≈ 3.0385, and c2 ≈ 0.4779 were found by optimizing the associated nonlinear least-squares problem. This proposed model, with only three parameters, is able to obtain a least-square residual of 5.02 ⋅ 10−3 with respect to the MINVO roots lying in (−1,1) found for n = 2, …, 7. The distribution of roots generated by this proposed model (n ≥ 8) is shown in Figure 9. Each root can then be assigned to a polynomial i of the basis by simply following the same assignment pattern found for n = 1, …, 7. Then, and by solving a linear system, the polynomials can be scaled to enforce ${\sum_{i = 0}^{n}{\lambda_{i}{(t)}}} = {1{\forall t}}$ (or equivalently, AT 1 = e). Note that this proposed model, although not guaranteed to be optimal, is guaranteed to be feasible by construction.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Some examples of the MINVO basis functions are shown in Figure 10. The comparison of |AMV| between the proposed model and the optimization results of Section 6.1 is shown in Table 4. For n = 1, …, 7, the relative error between the objective value obtained using the optimization and the one obtained using the proposed model is always &lt; 9.2 ⋅ 10−3. The proposed model also produces much smaller simplexes than the Bernstein and B-Spline bases.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

7 MINVO basis applied to other curves
7.1 Polynomial curves of degree n, dimension k, and embedded in a subspace ℳ of dimension m
So far we have studied the case of n = m = k (i.e., a polynomial curve of degree n and dimension k = n and for which n is also the dimension of ℳ, see Section 3.1). The most general case would be any k, n and m, as shown in Table 5. In all these cases, and using the (n+1) × (n+1) matrix AMV, we can still apply the equation Vk × (n+1) = Pk × (n+1) AMV−1 to obtain all the n + 1 MINVO control points in ℝk of the given curve (columns of the matrix V). The convex hull of the control points is a polyhedron that is guaranteed to contain the curve because the curve is a convex combination of the control points. Note also that, when n = m, all the cases below the diagonal of Table 5 have the same optimality properties (NGO/NLO/Feasible) as the diagonal element that has the same n.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For k = 3, Figure 11 shows a cubic curve embedded in a two-dimensional subspace (m = 2, n = 3), a segment embedded in a one-dimensional subspace (m = n = 1) and a quadratic curve embedded in a two-dimensional subspace (m = n = 2). For k = m = 2, the comparison between the area of the convex hull of the MINVO control points (AreaMV) and the area of the convex hull of the Bézier control points (AreaBe) is shown in Figure 13. Note that this ratio is constant for any polynomial curve for the case n = 2, but depends on the given curve for the cases n &gt; 2. To generate the boxplots of Figure 13, we used a total of 104 polynomial curves passing through n + 1 points randomly sampled from the square [−1, 1]2. Although it is not guaranteed that AreaMV &lt; AreaBe for any polynomial with n &gt; 2, the Monte Carlo analysis performed using these random polynomial curves shows that AreaMV &lt; AreaBe holds for the great majority of them, with improvements up to ≈ 200 times for the case n = 7.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Similarly, the results for k = m = 3 are shown in Figure 13, where we used a total of 104 polynomial curves passing through n + 1 points randomly sampled from the cube [−1, 1]3. Again, it is not guaranteed that VolMV &lt; VolBe for any polynomial with n &gt; 3, but the Monte Carlo results obtained show that this is true in most of these random polynomials. For the case n = 7, the MINVO basis obtains convex hulls up to ≈ 550 times smaller than the Bézier basis. Qualitatively, and for the comparisons shown above, the MINVO enclosures are much smaller than the Bézier enclosures when used in “tangled” curves. In these curves, the Bézier control points tend to be spread out and far from the curve, leading therefore to large and conservative Bézier enclosures.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Finally, we compare in Figure 14 how these polyhedral convex hulls, obtained by either the MINVO or Bézier control points, approximate conv (P), which is the convex hull of the curve P. Similar to the previous cases, here we used a total of 103 polynomial curves passing through n + 1 points randomly sampled from the cube [−1, 1]k. The error in the MINVO outer polyhedral approximation is approximately linear as n increases, but it is exponential for the Bézier basis. For instance, when n = 7 and k = 3, the Bézier control points generate a polyhedral outer approximation that is ≈ 1010 times larger than the volume of conv (P), while the polyhedral outer approximation obtained by the MINVO control points is only ≈ 3.9 times larger.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Via projections, the MINVO basis is also able to obtain the smallest simplex that encloses some rational curves, which are curves whose coordinates are the quotients of two polynomials. For instance, given the n-simplex obtained by the MINVO basis for a given nth-degree polynomial curve P, we can project every point p (t) of the curve via a perspective projection, using a vertex as the viewpoint, and the opposite facet as the projection plane. Note that this perspective projection of the polynomial curve will be a rational curve. If the n-simplex is the smallest one enclosing the polynomial curve, then each facet is also the smallest (n−1)-simplex that encloses the projection. This can be easily proven by contradiction, since if the facet were not a minimal (n−1)-simplex for the projected curve, then the n-simplex would not be minimal for the original 3D curve (see for instance).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Let us define $\begin{bmatrix}
{\mathbf{v}}_{0} &amp; \ldots &amp; {\mathbf{v}}_{n}
\end{bmatrix}:=\begin{bmatrix}
\mathbf{0} &amp; {\mathbf{I}}_{n}
\end{bmatrix}$, and let πi denote the plane that passes though the vertices {v0, v1, …, vn} ∖ {vi}.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

This projection can also be applied successively from ℝi to ℝj (i &gt; j ≥ 1). Figure 15 shows the case ℝ3 → ℝ2 (for all the four possible projections), and some projections of the cases ℝ6 → ℝ2, ℝ10 → ℝ2, ℝ5 → ℝ3, and ℝ12 → ℝ3.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

MINVO: The curve is divided into s subintervals, and then the MINVO enclosure for each of the subintervals is computed.
Bézier: The curve is divided into s subintervals, and then the Bézier enclosure for each of the subintervals is computed.
SLEFE: The curve is divided into s subintervals, and the SLEFE (subdividable linear efficient function enclosure ) is obtained using h breakpoints555As an example, if the time subinterval is [0.6, 1], then three uniformly-distributed breakpoints would be {0.6,0.8,1}, and the SLEFE for that subinterval will consist of a convex enclosure for the part of the curve in t ∈ [0.6, 0.8], and another convex enclosure for the part of the curve in t ∈ [0.8, 1]. per subinterval (i.e., h − 1 linear segments per subinterval). A SLEFE obtained with h breakpoints per subinterval will be denoted as SLh.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Note that s = 1 corresponds to the case where no subdivision is performed. When s &gt; 1, the subintervals of the curve are obtained by evenly splitting the time interval. Moreover, SL2 (i.e., h = 2) corresponds to a SLEFE with only one linear segment (i.e., two breakpoints) per subinterval.
We compare the width, the union, and the convex hull (defined in F) for the different enclosures. The comparison of the width of the enclosures produced is available in G. The comparison of the area and number of vertices of the union and the convex hull is available in H. In I, we compare MINVO and SLEFE in terms of runtime and simplicity of their implementation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Compared to SL2, MINVO achieves a smaller area for most of the n–s combinations tested, and sometimes using only half of the vertices needed by SL2. Compared to SLh (h ∈ ), MINVO typically achieves a smaller area for the cases where either s is small or the degree n is high, and it usually does so using fewer number of vertices than SLh. On the other hand, SLh tends to achieve a smaller area when either s is large or the degree n is small, but it usually requires more vertices than MINVO. Hence, MINVO is advantageous with respect to SLh in applications where having a small number of vertices is crucial. For example, a smaller number of vertices can substantially reduce the total computation time in algorithms that, after finding the enclosure, need to iterate through all of the vertices found to impose a constraint or perform a specific operation/check for each of them. If the number of vertices is not important for the specific application, then SLh (h ≥ 4) should be chosen, since it typically achieves a smaller area of the union and area of the convex hull.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Compared to Bézier, MINVO also achieves a smaller union and hull area for the cases where either s is small or the degree n is high, and, when n ∈, it does so using only up to 1.3 times the number of vertices of Bézier. In terms of the width of the enclosure (G), SLEFE performs better than MINVO. The use of SLEFE is hence desirable in the cases where the width of the enclosure is more important for the specific application. For any of the techniques, operations like the union, the convex hull, or the outer boundaries computation for SLEFE are typically either not possible or computationally expensive in the applications where the curve itself is a decision variable of an optimization problem (as, e.g., ). Instead, we can use the raw points of the enclosure, which in 2D can be defined as the unique control points of each subinterval (for MINVO and Bézier), and as the unique vertices of each of the rectangles generated per breakpoint of each subinterval (for SLh).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

The number of these raw points for a general 2D curve is n s + s for MINVO, n s + 1 for Bézier, and 4 h s for SLh. The comparison of these raw points is shown in Figure 16. The MINVO enclosures have fewer raw points than all SLh (h ∈ ) for n ∈. Compared to Bézier, the MINVO enclosure has s − 1 additional raw points, but achieves areas that are up to 30 times smaller (see Figure 23). As noted, SLEFE depends pseudo-linearly on the coefficients of the polynomial curve (i.e., linearly except for a min/max operation). In contrast, the MINVO or Bézier enclosures depend linearly on the coefficients of the polynomial curve. This makes the MINVO and Bézier enclosures more suitable for time-critical optimization problems in which the coefficients of the curve are decision variables.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

9.1 Conversion between MINVO, Bernstein, and B-Spline
Given a curve P ∈ 𝒫n, the control points (i.e., the vertices of the n-simplex that encloses that curve) using a basis α can be obtained from the control points of a different basis β (α, β ∈ {MV, Be, BS}) using the formula

<!-- chunk {"id": "body-0076", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For instance, to obtain the Bernstein control points from the MINVO control points we can use VBe = VMV AMV ABe−1. The matrices AMV are the ones shown in Table 3, while the matrices ABe and ABS are available. Note that all the matrices need to be expressed in the same interval (t ∈ [−1, 1] in this paper), and that the inverses of these matrices can be easily precomputed offline. 9.2 Tighter volumes for Problem 1 via subdivision
As shown in Section 8, and at the expense of adding more vertices, tighter polyhedral solutions for Problem 1 can be obtained by dividing the polynomial curve into several subintervals and then computing the convex hull of the MINVO enclosure of each subinterval. To subdivide the curve, one can do it first in Bézier form (leveraging therefore the properties of De Casteljau’s algorithm), and then compute the MINVO control points as linear functions of the Bézier control points of that subinterval using Eq. 5.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Alternatively, one can also tabulate (offline) the inverse of the matrices AMV, expressed in the subinterval desired, and then simply compute the MINVO control points of that subinterval as VMV = P AMV−1. Several examples for n = 3 are shown in Figure 17, where the original curve P ∈ 𝒫3 is split into 5 subintervals (i.e., s = 5), and the resulting convex hull is a polyhedron with 20 vertices that is 1.19 times smaller than the smallest 3-simplex that encloses the whole curve (i.e., the simplex found by applying the MINVO basis to the whole curve). Depending on the specific application, one might also be interested in obtaining a sequence of overlapping polyhedra whose union (a nonconvex set in general) completely encloses the curve. This can be obtained by simply computing the MINVO enclosure for every subinterval of the curve. 9.3 When should each basis be used? The Bernstein (Bézier) and B-Spline bases have many useful properties that are not shared by the MINVO basis.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For example, a polynomial curve passes through the first and last Bézier control points, the derivative of a Bézier curve can be easily computed from the difference of the Bézier control points, and the B-Spline basis has built-in smoothness in curves with several segments. Hence, it may be desirable to use the Bézier or B-Spline control points to design and model the curve, and then convert the control points of every interval to the MINVO control points (using the simple linear transformation given in Section 9.1) to perform collision/intersection checks, or to impose collision-avoidance constraints in an optimization problem. This approach benefits from the properties of the Bernstein/B-Spline bases, while also exploiting the enclosures obtained by the MINVO basis. 10 Conclusions and Future Work
This work derived and presented the MINVO basis. The key feature of this basis is that it finds the smallest n-simplex that encloses a given nth-degree polynomial curve (Problem 1), and also finds the nth-degree polynomial curve with largest convex hull enclosed in a given n-simplex (Problem 2).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

For n = 3, the ratios of the improvement in the volume achieved by the MINVO basis with respect to the Bernstein and B-Spline bases are 2.36 and 254.9 respectively. When n = 7, these improvement ratios increase to 902.7 and 2.997 ⋅ 1021 respectively. Numerical global optimality was proven for n = 1, 2, 3, numerical local optimality was proven for n = 4, and high-quality feasible solutions for all n ≥ 5 were obtained. Finally, the MINVO basis was also applied to polynomial curves with different n, k and m (achieving improvements ratios of up to ≈ 550), and to some rational curves.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Is the global optimum of Problem 4 the same as the global optimum of Problem 3? I.e., are we losing optimality by imposing the specific structure on λi (t)? On a similar note, is it possible to obtain for any n a bound on the distance between the objective value obtained by the model proposed in Section 6.2, and the global minimum of Problem 3?
Does there exist a recursive formula to obtain the solution of Problem 3 for a specific n = q given the previous solutions for n = 1, …, q − 1? Would this recursive formula allow to obtain the globally optimal solutions for all n ∈ ℕ of Problem 3?

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results for $n = {1,2,\\ldots,7}$", "weight": 1.0} -->

Finally, the way polynomials are scaled (to impose AT 1 = e) in Section 6.2 can suffer from numerical instabilities when the degree is very high (n &gt; 30). This is expected, since the monomial basis used to compute A is known to be numerically unstable. A more numerically-stable scaling, potentially avoiding the use of the monomial basis, could therefore be beneficial for higher degrees.
