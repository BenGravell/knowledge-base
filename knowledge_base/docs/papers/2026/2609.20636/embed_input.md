<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Complexity of Output Feedback Stabilization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that unless P = NP, there cannot be a polynomial-time (or even pseudo-polynomial-time) algorithm for output feedback stabilization of a linear dynamical system with a linear controller. This settles one of the best-known open problems in control theory. The result holds in both continuous and discrete time. We also present a family of stabilizable linear dynamical systems for which no polynomial-time algorithm can write down a stabilizing controller in its standard representation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A real matrix is *Hurwitz* if all its eigenvalues have negative real parts, and *Schur* if all its eigenvalues lie in the open unit disk in the complex plane. For matrices $A\in\mathbb{Q}^{N\times N}$, $B\in\mathbb{Q}^{N\times p}$, and $C\in\mathbb{Q}^{q\times N}$, the *output feedback stabilization* problem in continuous time (resp. discrete time) asks whether there exists some $K\in\mathbb{R}^{p\times q}$ that makes $A+BKC$ Hurwitz (resp. Schur). This amounts to asymptotically stabilizing the linear dynamical system $\dot{x}=Ax+Bu$, $y=Cx$, or its discrete-time analogue, using a static linear control law $u=Ky$ that maps the observed output $y$ of the system to the control $u$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

When the answer to this question is positive, one often also hopes to find a stabilizing "feedback gain" matrix $K$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In their 1995 survey, Blondel, Gevers, and Lindquist described output feedback stabilization as "the most often mentioned specific open problem" in systems and control theory. When $C$ is the identity matrix, the problem reduces to *state feedback stabilization* and admits an efficient test based on the stabilizability of the pair $(A,B)$, or a polynomial-size semidefinite programming formulation that can also recover the feedback gain matrix \[3, Section 7.2.1\]. In general, one can reformulate the output feedback stabilization problem as the problem of testing the feasibility of a system of polynomial inequalities^11^ 1 Such a formulation can be obtained, for example, by jointly searching for the controller matrix $K$ and a quadratic Lyapunov function for the closed-loop system, and then invoking Sylvester's criterion for matrix positive definiteness. and hence the problem admits exponential-time algorithms; see, e.g.,. However, no polynomial-time algorithm is known for output feedback stabilization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Blondel and Tsitsiklis proved NP-hardness when the entries of $K$ are constrained to prescribed intervals, but left the complexity of the unrestricted problem open. Chaudhry proved strong NP-hardness of the more general problem of deciding whether an affine subspace of matrices contains a Hurwitz (or a Schur) matrix. The affine subspaces in that reduction, however, do not have the specific form $\{A+BKC:K\in\mathbb{R}^{p\times q}\}$ required by output feedback stabilization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we prove that output feedback stabilization is strongly NP-hard. This result is established both in continuous time (Section 2) and in discrete time (Section 3). The implication of this result is that unless P=NP, there is no polynomial-time (or even pseudo-polynomial-time) algorithm for output feedback stabilization. In Section 4, we also establish, in both continuous and discrete time, a representation obstruction to polynomial-time algorithms that is independent of any complexity-theoretic assumption: even when the system is stabilizable, a polynomial-time algorithm cannot, in general, write down a stabilizing feedback gain matrix in its natural representation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

All results in this paper are in the Turing model of computation, where the input consists of the rational entries of the matrices $A,B,C$. Each entry is represented as $a/b$, where $a$ is a signed integer and $b$ is a positive integer. The input size $L$ is the total number of bits needed to encode these numerators and denominators in binary, including the signs. Let $M$ be the maximum of $|a|$ and $b$ over all entries of $A,B,C$. An algorithm is polynomial-time if its running time is bounded by a polynomial in $L$, and pseudo-polynomial-time if its running time is bounded by a polynomial in $M$ and the dimensions of $A,B,C$. In particular, every polynomial-time algorithm is also pseudo-polynomial-time, though the converse is not true as pseudo-polynomial time algorithms can take exponential time in $L$. Our reductions establish NP-hardness even when $M$ is polynomially bounded in the matrix dimensions. On these instances, any pseudo-polynomial-time bound becomes a polynomial-time bound.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, our NP-hardness results are in the strong sense and rule out pseudo-polynomial-time algorithms unless $\mathrm{P}=\mathrm{NP}$. See for more details on these notions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Continuous-time hardness", "weight": 1.0} -->

In this section, we prove the following theorem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Representation obstruction to polynomial-time algorithms", "weight": 1.0} -->

Independently of assumptions such as P$\neq$NP, we show in this section that there is a representation obstruction to polynomial-time controller synthesis: on some stabilizable instances, a polynomial-time algorithm cannot even write down a stabilizing controller (i.e. feedback gain matrix) in its standard representation. This also suggests that output feedback stabilization may not belong to NP, unless there is a polynomial-size certificate of stabilizability that avoids writing down the controller. The problem belongs to $\mathrm{PSPACE}$, however, since we have already argued that it can be reduced to testing the feasibility of polynomial inequalities.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Representation obstruction to polynomial-time algorithms", "weight": 1.0} -->

Observe that if a stabilizing controller exists, a rational one exists as well. Indeed, the sets of Hurwitz and Schur matrices are open, and $K\mapsto A+BKC$ is continuous. The set of stabilizing controllers is therefore open, and every nonempty open subset of a finite-dimensional real vector space contains a rational point.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Representation obstruction to polynomial-time algorithms", "weight": 1.0} -->

We encode an entry $a/b$ of $A,B,$ or $C$, with $a\in\mathbb{Z}$, $b\in\mathbb{Z}_{>0}$, and $\gcd(|a|,b)=1$, by writing its signed numerator and positive denominator explicitly in binary. Dense matrix encoding lists every entry, including zeros, which have constant encoding size. We use the elementary observation that for $a,b\in\mathbb{Z}_{>0}$ and $\varepsilon>0$, This follows from $a\geq 1$ and applies after cancellation, so reducing a fraction cannot invalidate this denominator bound.
