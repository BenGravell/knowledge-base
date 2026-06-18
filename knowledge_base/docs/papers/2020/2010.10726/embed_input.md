MINVO Basis: Finding Simplexes with Minimum Volume Enclosing Polynomial Curves

Topics include MINVO basis, Sum-of-squares programming, SOS.

This paper studies the polynomial basis that generates the smallest n-simplex enclosing a given n^(th)-degree polynomial curve in R^(n). Although the Bernstein and B-Spline polynomial bases provide feasible solutions to this problem, the simplexes obtained by these bases are not the smallest possible, which leads to overly conservative results in many CAD (computer-aided design) applications. We first prove that the polynomial basis that solves this problem (MINVO basis) also solves for the n^(th)-degree polynomial curve with largest convex hull enclosed in a given n-simplex. Then, we present a formulation that is independent of the n-simplex or n^(th)-degree polynomial curve given. By using Sum-Of-Squares (SOS) programming, branch and bound, and moment relaxations, we obtain high-quality feasible solutions for any ninmathbbN, and prove (numerical) global optimality for n = 1, 2, 3 and (numerical) local optimality for n = 4....

## Introduction

Polyhedral enclosures of a given polynomial curve have a crucial role in a large number of CAD algorithms to compute curve intersections, perform ray tracing, or obtain minimum distances between convex shapes. These polyhedral enclosures are also used in rasterization, mesh generation, path planning for numerical control machines, and trajectory optimization for robots. Many of these works leverage the convex hull property of the Bernstein basis (polynomial basis used by Bézier curves) to obtain these polyhedral enclosures, although some works use the B-Spline basis instead.

Although both the Bernstein basis and B-Spline basis have many useful properties, they are not designed to generate the smallest $n$-simplex that encloses a given $n^{\text{th}}$-degree polynomial curve in ${\mathbb{R}}^{n}$. This directly translates into undesirably conservative results in many of the aforementioned applications. Polyhedral enclosures with more than $n + 1$ vertices (i.e., not simplexes) can provide tighter volume approximations, but at the expense of a larger number of vertices, which can eventually increase the computation time in real-time applications. The main focus of this paper is therefore on simplex enclosures.

Is the global optimum of Problem 4 the same as the global optimum of Problem 3? I.e., are we losing optimality by imposing the specific structure on λi (t)? On a similar note, is it possible to obtain for any n a bound on the distance between the objective value obtained by the model proposed in Section 6.2, and the global minimum of Problem 3?
Does there exist a recursive formula to obtain the solution of Problem 3 for a specific n = q given the previous solutions for n = 1, …, q − 1? Would this recursive formula allow to obtain the globally optimal solutions for all n ∈ ℕ of Problem 3?

Finally, the way polynomials are scaled (to impose AT 1 = e) in Section 6.2 can suffer from numerical instabilities when the degree is very high (n &gt; 30). This is expected, since the monomial basis used to compute A is known to be numerically unstable. A more numerically-stable scaling, potentially avoiding the use of the monomial basis, could therefore be beneficial for higher degrees.

### Equivalent Formulation for Problems 1 and 2

## Problems definition
