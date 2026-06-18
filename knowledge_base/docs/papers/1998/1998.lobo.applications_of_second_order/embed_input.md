<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Applications of Second-order Cone Programming

Topics include Second-order cone programming, Convex optimization, Interior-point methods, Robust estimation, Engineering design, Quadratic cones, Primal-dual methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys second-order cone programming as a tractable convex optimization class between linear programming and semidefinite programming, then demonstrates applications in engineering design and robust estimation. The paper also presents an efficient primal-dual interior-point method, helping establish SOCP as a practical modeling tool.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In a second-order cone program (SOCP) a linear function is minimized over the intersection of an affine set and the product of second-order (quadratic) cones. SOCPs are nonlinear convex problems that include linear and convex quadratic programs as special cases, and arise in many engineering problems, such as filter design, antenna array weight design, truss design, robust estimation, and problems involving friction, for example robot grasp. In this paper we describe the basic theory of SOCPs, a variety of engineering applications, and an efficient primal-dual interior-point method for solving SOCPs. The algorithm we describe shares many of the features of primal-dual interior-point methods for linear programming (LP): Worst-case theoretical analysis shows that the number of iterations required to solve a problem grows at most as the square root of the problem size, while numerical experiments indicate that the typical number of iterations ranges between 5 and 50, almost independent of the problem size.
