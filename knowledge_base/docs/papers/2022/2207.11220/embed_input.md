<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Algebraic Riccati Equations Are Almost as Easy as Deterministic Ones Theoretically

Topics include Optimal control, Control, Algebraic Riccati equation, Riccati equation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic algebraic Riccati equations, also known as rational algebraic Riccati equations, arising in linear-quadratic optimal control for stochastic linear time-invariant systems, were considered to be not easy to solve. The-state-of-art numerical methods most rely on differentiability or continuity, such as Newton-type method, LMI method, or homotopy method. In this paper, we will build a novel theoretical framework and reveal the intrinsic algebraic structure appearing in this kind of algebraic Riccati equations. This structure guarantees that to solve them is almost as easy as to solve deterministic/classical ones, which will shed light on the theoretical analysis and numerical algorithm design for this topic.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algebraic Riccati equations (AREs) arise in various models related to control theory, especially in linear-quadratic optimal control design. The deterministic/classical ones are considered for the deterministic linear time-invariant systems, including discrete-time algebraic Riccati equations (DAREs) and continuous-time algebraic Riccati equations (CAREs) During many years, people have developed rich theoretical results and numerical methods for the DAREs and CAREs. Readers are referred to to obtain an overview for both theories and algorithms. In comparison, the stochastic/rational ones are considered for the stochastic linear time-invariant systems, including stochastic discrete-time algebraic Riccati equations (SDAREs) and stochastic continuous-time algebraic Riccati equations (SCAREs) Here $r - 1$ is the number of stochastic processes involved in the stochastic systems dealt, and it is easy to check that for the case $r = 1$ SDAREs and SCAREs degenerate to DAREs and CAREs respectively. Due to the complicated forms, one may recognize it would be much more difficult to analyze their properties and obtain their solutions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are still literature, e.g. discussing the stochastic linear systems and the induced stochastic AREs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As we can see, the stochastic AREs are still algebraic, and it is quite natural to ask whether algebraic methods could be developed to solve them. However, limited by lack of clear algebraic structures, to the best of the authors' knowledge, nearly all of the existing algorithms are based on the differentiability or continuity of the equations, such as Newton's method, modified Newton's method, Lyapunov/Stein iterations, comparison theorem based method, LMI's (linear matrix inequality) method, and homotopy method.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key to the problem is the algebraic structures behind the equations. In this paper, we will build up a simple and clear algebraic interpretation of SDAREs and SCAREs with the help of the so-called left semi-tensor product. In the analysis we find out the Toeplitz structure and the symplectic structure appearing in the equations, and illustrate the fact that the fixed point iteration and the doubling iteration are also valid for them. The algebraic structures found here will shed light on the theoretical analysis and numerical algorithms design, and strongly imply that stochastic AREs are almost as easy as deterministic ones.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. First some notations and a brief description of the left semi-tensor product are given immediately. Section 2 and Section 3 are devoted to describe the algebraic structures in SDAREs and SCAREs respectively. At last some concluding remarks are given in Section 4.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Notations", "weight": 1.0} -->

In this paper, $\mathbb{R}$ is the set of all real numbers. ${\mathbb{R}}^{n \times m}$ is the set of all $n \times m$ real matrices, ${\mathbb{R}}^{n} = {\mathbb{R}}^{n \times 1}$, and ${\mathbb{R}} = {\mathbb{R}}^{1}$. $I_{n}$ (or simply $I$ if its dimension is clear from the context) is the $n \times n$ identity matrix. Given a matrix $X$, $X^{T}$, $\| X\|$, and $\rho{(X)}$ are its transpose, induced norm, and spectral radius respectively.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Notations", "weight": 1.0} -->

Given a linear operator $\mathcal{X}$, $\mathcal{X}^{\ast}$, $\|\mathcal{X}\|$, and $\rho{(\mathcal{X})}$ are its adjoint, norm, and spectral radius respectively. For a symmetric matrix $X$, $X \succ 0$ ($X \succeq 0$) indicates its positive (semi-)definiteness, and $X \prec 0$ ($X \preceq 0$) if ${- X} \succ 0$ (${- X} \succeq 0$).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notations", "weight": 1.0} -->

Some easy identities are given: Here is the Sherman-Morrison-Woodbury formula: The inverse sign in 1.3 and 1.4 indicates invertibility.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Left semi-tensor product", "weight": 1.0} -->

The left semi-tensor product, first defined in 2001, has many applications in system and control theory, such as Boolean networks and electrical systems. Please seek more information in the monograph.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Left semi-tensor product", "weight": 1.0} -->

By $A \otimes B$ denote the Kronecker product of the matrices $A$ and $B$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Left semi-tensor product", "weight": 1.0} -->

For ${A \in {\mathbb{R}}^{m \times n}},{B \in {\mathbb{R}}^{p \times q}}$, define the left semi-tensor product of $A$ and $B$: This product satisfies: ${{({A \ltimes B})} \ltimes C} = {A \ltimes {({B \ltimes C})}}$ (so the parenthesis can be omitted); ${{{({A + B})} \ltimes C} = {{A \ltimes C} + {B \ltimes C}}},{{A \ltimes {({B + C})}} = {{A \ltimes B} + {A \ltimes C}}}$; \end{bmatrix} \ltimes \begin{bmatrix} \end{bmatrix}} = \begin{bmatrix} The left semi-tensor product, which satisfies the same arithmetic laws as the classical matrix product, can

<!-- chunk {"id": "body-0014", "role": "body", "section": "Left semi-tensor product", "weight": 1.0} -->

be treated as the matrix product in the following sections. Briefly, we write $A^{\ltimes k} = \underset{k}{\underbrace{A\ltimes A\ltimes\cdots\ltimes A}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "SDARE", "weight": 1.0} -->

Consider the SDARE 1.1 where ${A_{i},Q} \in {\mathbb{R}}^{n \times n}$, $B_{i} \in {\mathbb{R}}^{n \times m}$, $L \in {\mathbb{R}}^{n \times m}$ and $R \in {\mathbb{R}}^{m \times m}$ with $\begin{bmatrix} \end{bmatrix} \succeq 0$. It is easy to see that $X$ is a solution if and only if $X^{T}$ is a solution. In control theory, usually only symmetric solutions to 1.1 are needed. Hence in the paper, we only consider the symmetric solutions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "SDARE", "weight": 1.0} -->

It is known that if the assumption above holds, then 1.1 has a unique positive semi-definite stabilizing solution $X_{\star}$, see, e.g., \[10, Theorem 5.14\]. Here, $X$ is called a stabilizing solution if $\mathcal{S}_{F_{X}}$ is exponentially stable with In fact, $X_{\star}$ is a stabilizing solution if and only if the zero equilibrium of the closed-loop system is strongly exponentially stable in the mean square \[10, Remark 5.11\], where $F_{\star} = F_{X_{\star}}$ is as in 2.3 with $X = X_{\star}$. Moreover, the cost functional 2.2 has an optimal control $u_{t} = {F_{\star}x_{t}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Fixed point iteration and Toeplitz structure", "weight": 1.0} -->

Encouraging by the theory of DARE, one may solve the SDARE 2.6 by the fixed point iteration: Theorem 2.1. ‣ 2.1 Fixed point iteration and Toeplitz structure ‣ 2 SDARE ‣ Stochastic algebraic Riccati equations are almost as easy as deterministic ones theoretically") analyzes the convergence of the fixed point iteration 2.7.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Symplectic structure and doubling iteration", "weight": 1.0} -->

The fixed point iteration $\{ X_{t}\}$ from 2.7, or equivalently 2.11. ‣ 2.1 Fixed point iteration and Toeplitz structure ‣ 2 SDARE ‣ Stochastic algebraic Riccati equations are almost as easy as deterministic ones theoretically"), converges to the unique positive semi-definite stabilizing solution $X_{\star}$ linearly. As the doubling iteration is an acceleration of the fixed point iteration for DAREs and CAREs in the sense that the doubling iteration only computes the terms $X_{1},X_{2},X_{4},\ldots,X_{2^{k}},\ldots$ generated by the fixed point iteration, we will show the same acceleration is also valid for SDAREs 2.6.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Symplectic structure and doubling iteration", "weight": 1.0} -->

As the symplectic structure plays a fundamental role in the theory of doubling iteration for DAREs, the symplectic-like structure is also necessary for SDAREs, of which the related concepts are defined in the beginning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SCARE", "weight": 1.0} -->

Consider the SCARE 1.2 where ${A_{i},Q} \in {\mathbb{R}}^{n \times n}$, $B_{i} \in {\mathbb{R}}^{n \times m}$, $L \in {\mathbb{R}}^{n \times m}$ and $R \in {\mathbb{R}}^{m \times m}$ with $\begin{bmatrix} \end{bmatrix} \succeq 0$. It is easy to see that $X$ is a solution if and only if $X^{T}$ is a solution. In control theory, usually only symmetric solutions to 1.2 are needed. Hence in the paper, we only consider the symmetric solutions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SCARE", "weight": 1.0} -->

The SCARE 1.2 arises from the stochastic time-invariant control system in continue-time subject to multiplicative white noise, whose dynamics is described as below: in which ${x{(t)}},{u{(t)}}$ and $z{(t)}$ are state, input, measurement, respectively, and ${w{(t)}} = \begin{bmatrix} \end{bmatrix}^{T}$ is a standard Wiener process satisfying that each $w_{i}{(t)}$ is a standard Brownian motion and the $\sigma$-algebras ${{{\sigma\left({{{w_{i}{(t)}},t} \in {\lbrack t_{0},\infty)}} \right)},i} = 1},{\ldots,{r - 1}}$ are independent.

<!-- chunk {"id": "body-0022", "role": "body", "section": "SCARE", "weight": 1.0} -->

Considering the cost functional with respect to the control $u{(t)}$ with the given initial $x_{0}$: where $x_{t_{0},x_{0};u}{(t)}$ is the solution of the system 3.1 corresponding to the input $u{(t)}$ and having the initial ${x_{t_{0},x_{0};u}{(t_{0})}} = x_{0}$, one goal in stochastic control is to minimize the cost functional 3.2 and compute an optimal control. Such an optimization problem is also called the first linear-quadratic optimization problem \[11, Section 6.2\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "SCARE", "weight": 1.0} -->

It is known that if the assumption above holds, then 1.2 has a unique positive semi-definite stabilizing solution $X_{\star}$, see, e.g., \[11, Theorem 5.6.15\]. Here, $X$ is a stabilizing solution if the system $({A_{0} + {B_{0}F_{X}}},{A_{1} + {B_{1}F_{X}}},\cdots,{A_{r - 1} + {B_{r - 1}F_{X}}})$ is stable with or equivalently, $\mathcal{L}_{F_{\star}}$ is exponentially stable with the associated $F_{\star} = F_{X_{\star}}$ taking the feedback control specified in 3.3 with $X = X_{\star}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SCARE", "weight": 1.0} -->

In fact, $X_{\star}$ is a stabilizing solution if and only if the zero equilibrium of the closed-loop system is strongly exponentially stable in the mean square \[11, Chapter 5\]. Furthermore, the cost functional 3.2 has an optimal control ${u{(t)}} = {F_{\star}x_{t_{0},x_{0}}{(t)}}$ where $x_{t_{0},x_{0}}{(t)}$ is the solution to the corresponding closed-loop system 3.4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Standard form and symplectic structure", "weight": 1.0} -->

As we have done for SDAREs, first we make an equivalent reformulation for 1.2 for the sake of simplicity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Standard form and symplectic structure", "weight": 1.0} -->

As continuous-time algebraic Riccati equations can be transformed to discrete-time ones by Möbius transformation and then symplectic systems are attained, stochastic continuous-time algebraic Riccati equations can also be transformed to stochastic discrete-time ones, which is clarified in the following.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Standard form and symplectic structure", "weight": 1.0} -->

To apply the doubling transformation to the $\ltimes$-symplectic pair $(M,L)$, it is necessary to simplify it to a simpler form, say, $\ltimes$-SSF1 pair, whose existence is guaranteed by Lemma 3.1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper we demonstrate that the stochastic AREs are essentially the deterministic AREs in the sense that all the matrix products are understood as the left semi-tensor products. As a by-product, the fixed point iteration and the doubling iteration would play a role in acquiring the approximations to the solutions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

However, the two iterations could not be straightforwardly used as mature numerical methods to solve the equations, because the left semi-tensor products make the size of involving matrices grow twice-exponentially ($r^{2^{k}}n$ in fact), which makes the storage an impossible task. Take the doubling iteration 2.15 or 3.17 as an example: if ${n = 1},{r = 2}$, then the numbers of rows of first several terms $A_{k}$ or $E_{k}$ (also the number of rows/columns of $G_{k}$) are $2,4,16,256,65536$. Hence more work needs to be done on developing practical algorithms, though the algebraic structure is revealed as clearly as the deterministic AREs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Anyway, as we can see, many parallel theoretical results and numerical methods for DAREs and CAREs can probably be generalized to SDAREs and SCAREs. Plenty of results are ready to be examined, and of course a lot of gaps are still needed to be filled. We believe that there must be efficient algorithms proposed under the philosophy of this paper, and we leave it for future work.
