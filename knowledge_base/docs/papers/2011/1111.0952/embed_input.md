<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Computing a Nonnegative Matrix Factorization - Provably

Topics include Nonnegative matrix factorization, Separable NMF, Provable algorithms, Matrix factorization, Polynomial time algorithm, Topic model, Computational complexity.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Identifies separability conditions under which nonnegative matrix factorization becomes tractable and gives polynomial-time algorithms for exact and approximate NMF in those regimes. The paper is important because it turns a widely used heuristic matrix factorization problem into a provable algorithmic setting connected to topics and mixture models.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the Nonnegative Matrix Factorization (NMF) problem we are given an n x m nonnegative matrix M and an integer r > 0. Our goal is to express M as A W where A and W are nonnegative matrices of size n x r and r x m respectively. In some applications, it makes sense to ask instead for the product AW to approximate M - i.e. (approximately) minimize normM - AW_F where norm{}_F denotes the Frobenius norm; we refer to this as Approximate NMF. This problem has a rich history spanning quantum mechanics, probability theory, data analysis, polyhedral combinatorics, communication complexity, demography, chemometrics, etc. In the past decade NMF has become enormously popular in machine learning, where A and W are computed using a variety of local search heuristics. Vavasis proved that this problem is NP-complete. We initiate a study of when this problem is solvable in polynomial time: 1. We give a polynomial-time algorithm for exact and approximate NMF for every constant r. Indeed NMF is most interesting in applications precisely when r is small.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

2. We complement this with a hardness result, that if exact NMF can be solved in time (nm)^(o)(r), 3-SAT has a sub-exponential time algorithm. This rules out substantial improvements to the above algorithm. 3. We give an algorithm that runs in time polynomial in n, m and r under the separablity condition identified by Donoho and Stodden in 2003. The algorithm may be practical since it is simple and noise tolerant (under benign assumptions). Separability is believed to hold in many practical settings. To the best of our knowledge, this last result is the first example of a polynomial-time algorithm that provably works under a non-trivial condition on the input and we believe that this will be an interesting and important direction for future work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the Nonnegative Matrix Factorization (NMF) problem we are given an $n \times m$ matrix $M$ with nonnegative real entries (such a matrix will be henceforth called "nonnegative") and an integer $r > 0$. Our goal is to express $M$ as $AW$ where $A$ and $W$ are nonnegative matrices of size $n \times r$ and $r \times m$ respectively. We refer to $r$ as the inner-dimension of the factorization and the smallest value of $r$ for which there is such a factorization as the nonnegative rank of $M$. An equivalent formulation is that our goal is to write $M$ as the sum of $r$ nonnegative rank-one matrices.^11^1It is a common misconception that since the real rank is the maximum number of linearly independent columns, the nonnegative rank must be the size of the largest set of columns in which no column can be written as a nonnegative combination of the rest. This is false, and has been the source of many incorrect proofs demonstrating a gap between rank and nonnegative rank.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A correct proof finally follows from the results of Fiorini et al. We note that $r$ must be at least the rank of $M$ in order for such a factorization to exist. In some applications, it makes sense to instead ask for $AW$ to be a good approximation to $M$ in some suitable matrix norm. We refer to the problem of finding a nonnegative $A$ and $W$ of inner-dimension $r$ that (approximately) minimizes $\left. \parallel{M - {AW}}\parallel \right._{F}$ as Approximate NMF, where $\left. \parallel\parallel \right._{F}$ denotes the Frobenius norm. Without the restriction that $A$ and $W$ be nonnegative, the problem can be solved exactly via singular value decomposition.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

NMF is a fundamental problem that has been independently introduced in a number of different contexts and applications. Many interesting heuristics and local search algorithms (including the familiar Expectation Maximization or EM) have been proposed to find such factorizations. One compelling family of applications is data analysis, where a nonnegative factorization is computed in order to extract certain latent relationships in the data and has been applied to image segmentation, information retrieval and document clustering. NMF also has applications in fields such as chemometrics (where the problem has a long history of study under the name self modeling curve resolution) and biology (e.g. in vision research ): in some cases, the underlying physical model for a system has natural restrictions that force a corresponding matrix factorization to be nonnegative. In demography (see e.g., ), NMF is used to model the dynamics of marriage through a mechanism similar to the chemical laws of mass action. In combinatorial optimization, Yannakakis characterized the number of extra variables needed to succinctly describe a given polytope as the nonnegative rank of an appropriate matrix (called the "slack matrix").

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In communication complexity, Aho et al showed that the log of the nonnegative rank of a Boolean matrix is polynomially related to its deterministic communication complexity - and hence the famous Log-Rank Conjecture of Lovasz and Saks is equivalent to showing a quasi-polynomial relationship between real rank and nonnegative rank for Boolean matrices. In complexity theory, Nisan used nonnegative rank to prove lower bounds for non-commutative models of computation. Additionally, the 1993 paper of Cohen and Rothblum gives a long list of other applications in statistics and quantum mechanics. That paper also gives an exact algorithm that runs in exponential time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Question 1.1", "weight": 1.0} -->

Can a nonnegative matrix factorization be computed efficiently when the inner-dimension, $r$, is small?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Question 1.1", "weight": 1.0} -->

Vavasis recently proved that the NMF problem is $NP$-hard when $r$ is large, but this only rules out an algorithm whose running time is polynomial in $n$, $m$ and $r$. Arguably, in most significant applications, $r$ is small. Usually the algorithm designer posits a two-level generative model for the data and uses NMF to compute "hidden" variables that explain the data. This explanation is only interesting when the number of hidden variables ($r$) is much smaller than the number of examples ($m$) or the number of observations per example ($n$). In information retrieval, we often take $M$ to be a "term-by-document" matrix where the ${(i,j)}^{th}$ entry in $M$ is the frequency of occurrence of the $i^{th}$ term in the $j^{th}$ document in the database.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Question 1.1", "weight": 1.0} -->

In this context, a NMF computes $r$ "topics" which are each a distribution on words (corresponding to the $r$ columns of $A$) and each document (a column in $M$) can be expressed as a distribution on topics given by the corresponding column of $W$. This example will be a useful metaphor for thinking about nonnegative factorization. In particular it justifies the assertion $r$ should be small -- the number of topics should be much smaller than the total number of documents in order for this representation to be meaningful. See Section A for more details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Question 1.1", "weight": 1.0} -->

Focusing on applications, and the overwhelming empirical evidence that heuristic algorithms do find good-enough factorizations in practice, motivates our next question.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Question 1.2", "weight": 1.0} -->

Can we design very efficient algorithms for NMF if we make reasonable assumptions about $M$?

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Results", "weight": 1.0} -->

Here we largely resolve Question 1.1. We give both an algorithm for accomplishing this algorithmic task that runs in polynomial time for any constant value of $r$ and we complement this with an intractability result which states that assuming the Exponential Time Hypothesis no algorithm can solve the exact NMF problem in time ${({nm})}^{o{(r)}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Simplicial Factorization", "weight": 1.0} -->

Here we consider the simplicial factorization problem, in which the target inner-dimension is $r$ and the matrix $M$ itself has rank $r$. Hence in any factorization $M = {AW}$ (where $r$ is the inner-dimension), $A$ must have full column rank and $M$ must have full row rank.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Justification for Simplicial Factorization", "weight": 1.0} -->

We first argue that the extra restriction imposed in simplicial factorization is natural in many contexts: Through a re-scaling (see Section LABEL:sec:appendix:separable for more details), we can assume that the columns of $M$, $A$ and $W$ all have unit $\ell_{1}$ norm. The factorization $M = {AW}$ can be interpreted probabilistically: each column of $M$ can be expressed as a convex combination (given by the corresponding column of $W$) of columns in $A$. In the example in the introduction, columns of $M$ represent documents and the columns of $A$ represent "topics". Hence a nonnegative factorization is an "explanation": each document can be expressed as a convex combination of the topics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Justification for Simplicial Factorization", "weight": 1.0} -->

But if $A$ does not have full column rank then this explanation is seriously deficient. This follows from a restatement of Radon's Lemma. Let $conv{(A_{U})}$ be the convex hull of the columns $A_{i}$ for $i \in U$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Observation 1", "weight": 1.0} -->

The observation implies that there is some candidate document $x$ that can be expressed as a convex combination of topics (in $U$), or instead can be expressed as a convex combination of an entirely disjoint set ($V$) of topics. The end goal of NMF is often to use the representation of documents as distributions on topics to perform various tasks, such as clustering or information retrieval. But if (even given the set of topics in a database) it is this ambiguous to determine how we should represent a given document as a convex combination of topics, then the topics we have extracted cannot be very useful for clustering! In fact, it seems unnatural to not require the columns of $A$ to be linearly independent!

<!-- chunk {"id": "body-0019", "role": "body", "section": "Observation 1", "weight": 1.0} -->

Next, one should consider the process (probabilistic, presumably) that generates the datapoints, namley, columns of $M$. Any reasonable process for generating columns of $M$ from the columns of $A$ would almost surely result in a matrix $M$ whose rank equals the rank of $A$. But then $M$ has the same rank as $A$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm for Simplicial Factorization", "weight": 1.0} -->

In this Section we give an algorithm that solves the simplicial factorization problem in ${({nm})}^{O{(r)}}$ time. Let $L$ be the maximum bit complexity of any coefficient in the input.

<!-- chunk {"id": "body-0021", "role": "body", "section": "General NMF", "weight": 1.0} -->

Now we consider the NMF problem where the factor matrices $A,W$ need not have full rank.

<!-- chunk {"id": "body-0022", "role": "body", "section": "General Structure Theorem: Minimality", "weight": 1.0} -->

Our goal is to re-cast nonnegative matrix factorization (for constant $r$) as a system of polynomial inequalities where the number of variables is constant, the maximum degree is constant and the number of constraints is polynomially bounded in $n$ and $m$. The main obstacle is that $A$ and $W$ are large - we cannot afford to introduce a new variable to represent each entry in these matrices.

<!-- chunk {"id": "body-0023", "role": "body", "section": "General Structure Theorem: Minimality", "weight": 1.0} -->

Furthermore, the number of possible choice functions $\sigma_{W}$ is at most $m^{cr^{2}f{(r)}}$ and the number of possible choice functions for $\sigma_{A}$ is at most $n^{cr^{2}g{(r)}}$. These choice functions are based on the notion of a simplicial partition, which we introduce later. We then give an algorithm for enumerating all simplicial partitions (this is the primary bottleneck in the algorithm).

<!-- chunk {"id": "body-0024", "role": "body", "section": "General Structure Theorem: Minimality", "weight": 1.0} -->

Fixing the choice functions $\sigma_{W}$ and $\sigma_{A}$, the question of finding linear transformations $T_{1},T_{2},{\ldotsT_{g{(r)}}}$ and $S_{1},S_{2},{\ldotsS_{g{(r)}}}$ that satisfy the above constraints (and the constraint that $M = {AW}$, and $A$ and $W$ are nonnegative) is exactly a system of polynomial inequalities with a $O{({r^{2}g{(r)}})}$ variables (each matrix $T_{i}$ or $S_{j}$ is $r \times r$), degree at most four and furthermore there are at most $O{({mn})}$ polynomial constraints.

<!-- chunk {"id": "body-0025", "role": "body", "section": "General Structure Theorem: Minimality", "weight": 1.0} -->

In this subsection, we will give a procedure (which given $A$ and $W$) generates a "minimal" choice for $A$ and $W$ (call this minimal choice $A^{\prime}$ and $W^{\prime}$), and we will later establish that this "minimal" choice satisfies the structural property stated informally above.

<!-- chunk {"id": "body-0026", "role": "body", "section": "General Structure Theorem: Simplicial Partitions", "weight": 1.0} -->

Here, we establish that the choice functions $\sigma_{W^{\prime}}$ and $\sigma_{A^{\prime}}$ in a proper chain are combinatorially simple. The choice function $\sigma_{W^{\prime}}$ can be regarded as a partition of the columns of $M$ into $|{\mathcal{C}{(A)}}|$ sets, and similarly the choice function $\sigma_{A^{\prime}}$ is a partition of the rows of $M$ into $\mathcal{R}{(W^{\prime})}$ sets. Here we define a geometric type of partitioning scheme which we call a simplicial partition, which has the property that there are not too many simplicial partitions (by virtue of this class having small VC-dimension), and we show that the partition functions $\sigma_{W^{\prime}}$ and $\sigma_{A^{\prime}}$ arising in the definition of a proper chain are realizable as (small) simplicial partitions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Claim 3.12", "weight": 1.0} -->

We can repeat the above replacing $A$ with $W^{\prime T}$ and $W^{\prime}$ with $A^{\prime}$, and this implies the lemma. $\blacksquare$

<!-- chunk {"id": "body-0028", "role": "body", "section": "Enumerating Simplicial Partitions", "weight": 1.0} -->

Here we give an algorithm for enumerating all $(k,s)$-simplicial partitions (of, say, the columns of $M$) that runs in time $O{(m^{ks{({r + 1})}})}$. An important observation is that the problem of enumerating all simplicial partitions can be reduced to enumerating all partitions that arise from a single hyperplane. Indeed, we can over-specify a simplicial partition by specifying the partition (of the columns of $M$) that results from each hyperplane in the set of $ks$ total hyperplanes that generates the simplicial partition. From this set of partitions, we can recover exactly the simplicial partition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Enumerating Simplicial Partitions", "weight": 1.0} -->

A number of results are known in this domain, but surprisingly we are not aware of any algorithm that enumerates all partitions of the columns of $M$ (by a single hyperplane) that runs in polynomial time (for ${dim{(M)}} \leq r$ and $r$ is constant) without some assumption on $M$. For example, the VC-dimension of a hyperplane in $r$ dimensions is $r + 1$ and hence the Sauer-Shelah lemma implies that there are at most $O{(m^{r + 1})}$ distinct partitions of the columns of $M$ by a hyperplane. In fact, a classic result of Harding gives a tight upper bound of $O{(m^{r})}$. Yet these bounds do not yield an algorithm for efficiently enumerating this structured set of partitions without checking all partitions of the data.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Enumerating Simplicial Partitions", "weight": 1.0} -->

A recent result of Hwang and Rothblum comes close to our intended application. A separable partition into $p$ parts is a partition of the columns of $M$ into $p$ sets so that the convex hulls of these sets are disjoint. Setting $p = 2$, the number of separable partitions is exactly the number of distinct hyperplane partitions. Under the condition that $M$ is in general position (i.e. there are no $t$ columns of $M$ lying on a dimension $t - 2$ subspace where $t = {{rank{(M)}} - 1}$), Hwang and Rothblum give an algorithm for efficiently enumerating all distinct hyperplane partitions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Enumerating Simplicial Partitions", "weight": 1.0} -->

Here we give an improvement on this line of work, by removing any conditions on $M$ (although our algorithm will be slightly slower). The idea is to encode each hyperplane partition by a choice of not too many data points.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Solving Systems of Polynomial Inequalities", "weight": 1.0} -->

The results of Basu et al give an algorithm for finding a point in a semi-algebraic set defined by $O{({mn})}$ constraints on polynomials of total degree at most $d$, and $f{(r)}$ variables in time $O{({({mnd})}^{cf{(r)}})}$. Using our structure theorem for nonnegative matrix factorization, we will re-cast the decision problem of whether a nonnegative matrix $M$ has nonnegative rank $r$ as an existence question for a semi-algebraic set.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Strong Intractability of Simplicial Factorization", "weight": 1.0} -->

Here we give evidence that finding a simplicial factorization of dimension $r$ probably cannot be solved in ${({nm})}^{o{(r)}}$ time, unless $3$-SAT can be solved in $2^{o{(n)}}$ time (in other words, if the Exponential Time Hypothesis of is true). Surprisingly, even the $NP$-hardness of the problem for general $r$ was only proved quite recently by Vavasis. That reduction is the inspiration for our result, though unfortunately we were unable to use it directly to get low-dimensional instances. Instead we give a new reduction using the $d$-SUM Problem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Gadget", "weight": 1.0} -->

Given the universe $U = {\{ s_{1},s_{2},\ldots,s_{N}\}}$ for the $d$-SUM problem, we construct a two dimensional Intermediate Simplex instance as shown in Figure 1. We will show that the Intermediate Simplex instance has exactly $N$ solutions, each representing a choice of $s_{i}$. Later in the reduction we use $d$ such gadgets to represent the choice of $d$ numbers in the set $U$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Gadget", "weight": 1.0} -->

Recall for a two dimensional Intermediate Simplex problem, the input consists of a polygon $\mathcal{P}$ (which is the hexagon $ABCDEF$ in Figure 1) and a set of points $S = {\{ I_{1},I_{2},\ldots,I_{3N}\}}$ inside $\mathcal{P}$ (which are the dots, except for $M$). A solution to this two dimensional Intermediate Simplex instance will be a triangle inside $\mathcal{P}$ such that all the points in $S$ are contained in the triangle (in Figure 1 $ACE$ is a valid solution).

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Gadget", "weight": 1.0} -->

We first specify the polygon $\mathcal{P}$ for the Intermediate Simplex instance. The polygon $\mathcal{P}$ is just the hexagon $ABCDEF$ inscribed in a circle with center $M$. All angles in the hexagon are ${2\pi}/3$, the edges ${AB} = {CD} = {EF} = \epsilon$ where $\epsilon$ is a small constant depending on $N$, $d$ that we determine later. The other 3 edges also have equal lengths ${BC} = {DE} = {FA}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Gadget", "weight": 1.0} -->

Now we specify the set $S$ of $3N$ points for the Intermediate Simplex instance. To get these points first take $N$ points in each of the 3 segements $AB$, $CD$, $EF$. On $AB$ these $N$ points are called $A_{1}$, $A_{2}$,..., $A_{N}$, and ${|{AA_{i}}|} = {\epsilons_{i}}$. Similarly we have points $C_{i}$'s on $CD$ and $E_{i}$'s on $EF$, ${|{CC_{i}}|} = {|{EE_{i}}|} = {\epsilons_{i}}$. Now we have $N$ triangles $A_{i}C_{i}E_{i}$ (the thin lines in Figure 1). We claim (see Lemma 4.5 below) that the intersection of these triangles is a polygon with $3N$ vertices.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Gadget", "weight": 1.0} -->

The points in $S$ are just the vertices of this intersection.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Reduction", "weight": 1.0} -->

Suppose we are given an instance of the $d$-SUM Problem with $N$ values $\{ s_{1},s_{2},{\ldotss_{N}}\}$. We will give a reduction to an instance of Intermediate Simplex in dimension ${r - 1} = {{3d} + 1}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Reduction", "weight": 1.0} -->

To encode the choice of $d$ numbers in the set $\{ s_{1},s_{2},\ldots,s_{N}\}$, we use $d$ gadgets defined in Section 4.1. The final solution of the Intermediate Simplex instance we constructed will include solutions to each gadget. As the solution of a gadget always corresponds to a number in $\{ s_{1},s_{2},\ldots,s_{N}\}$ (Lemma 4.6) we can decode the solution and get $d$ numbers, and we use an extra dimension $w$ that "computes" the sum of these numbers and ensures the sum is equal to $d/2$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Constraints 2 (Gadget)", "weight": 1.0} -->

We hope that in a gadget, if we choose three points corresponding to the triangle for some value $s_{i}$, that of these three points only the point on the $AB$ line will have a non-zero value for $w$ and that this value will be $s_{i}$. The points on the lines $CD$ or $EF$ will hopefully have a value close to zero.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Constraints 3 (CE)", "weight": 1.0} -->

These constraints make sure that points on $CD$ or $EF$ cannot have large $w$ value.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Constraints 3 (CE)", "weight": 1.0} -->

Recall that we use $z{(A)}$ to denote the $z$ coordinate of $A$ in the gadget in Section 4.1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Constraints 4 (AB)", "weight": 1.0} -->

Theses constraints make sure that points on $AB$ have values in $\{ s_{1},s_{2},\ldots,s_{N}\}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Constraints 4 (AB)", "weight": 1.0} -->

The $AB$ and $CE$ constraints all have the property that when $x_{i} < 1$ (i.e. the corresponding point is off of the gadget on the plane $x_{i} = 1$) then these constraints gradually become relaxed.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Constraints 4 (AB)", "weight": 1.0} -->

To make sure the gadget still works, we don't want the extra constraints on $w$ to rule out some possible values for $x_{i}$, $y_{i}$, $z_{i}$'s. Indeed we show the following claim.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Claim 4.9", "weight": 1.0} -->

The proof is by observing that Constraints $AB$ have almost no effect when $y > 0$ and Constraints $CE$ have no effect when $y = 0$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Claim 4.9", "weight": 1.0} -->

Constraints 1 to 4 define a polyhedron $P$ in ${3d} + 1$-dimensional space and furthermore the set of constraints that define $P$ have full rank (in fact even the inequalities in the Box Constraints have full rank). Thus this polyhedron is a valid polyhedron for the Intermediate Simplex problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Claim 4.9", "weight": 1.0} -->

Next we specify the points in $S$ for the Intermediate Simplex problem(each of which will be contained in the polyhedron $P$). Let $I_{k}$ (for $k \in {\lbrack{3N}\rbrack}$) be the set $S$ in the gadget in Section 4.1. As before, let $z{(I_{k})}$ and $y{(I_{k})}$ be the $z$ and $y$ coordinates of $I_{k}$ respectively.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Completeness and Soundness", "weight": 1.0} -->

The completeness part is straight forward: for $i^{th}$ gadget we just select the triangle that corresponds to $s_{k_{i}}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Claim 4.13", "weight": 1.0} -->

The points $O$ and $W$ must be in the set $T$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Claim 4.13", "weight": 1.0} -->

Proof: The points $O$ and $W$ are vertices of the polyhedron $P$ and hence cannot be expressed as a convex combination of any other set of points in $P$. $\blacksquare$

<!-- chunk {"id": "body-0053", "role": "body", "section": "Claim 4.13", "weight": 1.0} -->

Now we want to prove the rest of the $3d$ points in set $T$ is partitioned into $d$ triples, each triple belongs to one gadget. Set $T^{\prime} = {T - {\{ O\}} - {\{ W\}}}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Claim 4.15", "weight": 1.0} -->

Proof: The sets $T_{i}^{\prime}$ are disjoint, and additionally each set $T_{i}^{\prime}$ must contain at least $3$ nodes (otherwise the convex hull of $T_{i}^{\prime}$ even restricted to $x_{i},y_{i},z_{i}$ cannot contain the points $I_{k}^{i}$). This implies the Claim. $\blacksquare$

<!-- chunk {"id": "body-0055", "role": "body", "section": "Claim 4.15", "weight": 1.0} -->

Recall the gadget in Section 4.1 is a two dimensional object, but it is represented as a three dimensional cone in our construction. We would like to apply Lemma 4.6 to points on the plane $x_{i} = 1$ (in this plane the coordinates $y_{i}$,$z_{i}$ act the same as $y$, $z$ in the gadget).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Fully-Efficient Factorization under Separability", "weight": 1.0} -->

Earlier, we gave algorithms for NMF, and presented evidence that no ${({nm})}^{o{(r)}}$ time algorithm exists for determining if a matrix $M$ has nonnegative rank at most $r$. Here we consider conditions on the input that allow the factorization to be found in time polynomial in $n$, $m$ and $r$. (In Section 5.1, we give a noise-tolerant version of this algorithm). To the best of our knowledge this is the first example of an algorithm (that runs in time poly$(n,m,r)$) and provably works under a non-trivial condition on the input. Donoho and Stodden in a widely-cited paper identified sufficient conditions for the factorization to be unique (motivated by applications of NMF to a database of images) but gave no algorithm for this task. We give an algorithm that runs in time poly$(n,m,r)$ and assumes only one of their conditions is met (separability).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Fully-Efficient Factorization under Separability", "weight": 1.0} -->

We note that this separability condition is quite natural in its own right, since it is usually satisfied by model parameters fitted to various generative models (e.g. LDA in information retrieval).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Claim 5.5", "weight": 1.0} -->

Proof: Suppose (for contradiction) that a row in $M^{j}$ is not a loner and but it is equal to some row $W^{i}$. Then there is a set $S$ of rows of $M$ so that $M^{j}$ is in their convex hull and furthermore for all $j^{\prime} \in S$, $M^{j^{\prime}}$ is not equal to $M^{j}$. Thus there is a nonnegative vector $u \in \Re^{n}$ that is 0 at the $j^{th}$ coordinate and positive on indices in $S$ such that ${u^{T}M} = M^{j}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Claim 5.5", "weight": 1.0} -->

Hence ${u^{T}AW} = M^{j} = W^{i}$, but $u^{T}A$ must have unit $\ell_{1}$-norm (because $\left. \parallel u\parallel \right._{1} = 1$, all rows of $A$ have unit $\ell_{1}$-norm and are all nonnegative), also $u^{T}A$ is non-zero at position $j^{\prime}$. Consequently $W^{i}$ is in the convex hull of the other rows of $W$, which yields a contradiction.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Claim 5.5", "weight": 1.0} -->

Conversely if a row $M^{j}$ is not equal to any row in $W$, we conclude that $M^{j}$ is in the convex hull of the rows of $W$. Each row of $W$ appears as a row of $A$ (due to the separability condition). Hence $M^{j}$ is not a loner because $M^{j}$ is in the convex hull of rows of $M$ that are equivalent to $M^{j}$ itself. $\blacksquare$

<!-- chunk {"id": "body-0061", "role": "body", "section": "Claim 5.5", "weight": 1.0} -->

Using linear programming, we can determine which rows $M^{j}$ are loners. Due to separability there will be exactly $r$ different loner rows, each corresponds to one of the $W^{i}$. Thus we are able to recover $W^{\prime}$ that is equal to $W$ after permutation over rows.We can compute a nonnegative $A^{\prime}$ such that ${A^{\prime}W^{\prime}} = M$, and such solution $A^{\prime}$ is necessarily separable (since it is just equal to $A$ after permutation over columns). $\blacksquare$

<!-- chunk {"id": "body-0062", "role": "body", "section": "Adding Noise", "weight": 1.0} -->

In any practical setting the data matrix $M$ will not have an exact NMF of low inner dimension since its entries are invariably subject to noise. Here we consider how to extend our separability-based algorithm to work in presence of noise. We assume that the input matrix $M^{\prime}$ is obtained by perturbing each row of $M$ by adding a vector of $\ell_{1}$-norm at most $\epsilon$, where $M$ has a separable factorization of inner-dimension $r$. Alternatively, $\left. \parallel{M^{\prime i} - M^{i}}\parallel \right._{1} \leq \epsilon$ for all $i$. Notice that the case in which the separability condition is only approximately satisfied is a subcase of this: If for each column there is some row in which that column's entry is at least $1 - \epsilon$ and the sum of the other row entries is less than $\epsilon$ then the matrix $M^{\prime}$ will satisfy the condition stated above.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Adding Noise", "weight": 1.0} -->

(Note that $M,A,W$ have been scaled as discussed above.)

<!-- chunk {"id": "body-0064", "role": "body", "section": "Adding Noise", "weight": 1.0} -->

Our algorithm will require one more condition -- namely, we require the unknown matrix $W$ to be "robustly" simplicial instead of just simplicial.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Claim 5.8", "weight": 1.0} -->

Every row $M^{\prime j}$ has $\ell_{1}$-distance at most $2\epsilon$ to the convex hull of canonical rows.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Claim 5.8", "weight": 1.0} -->

and we can bound the right hand side by $2\epsilon$. $\blacksquare$

<!-- chunk {"id": "body-0067", "role": "body", "section": "Claim 5.8", "weight": 1.0} -->

Next, we show how to find the canonical rows. For a row $M^{\prime j}$, we call it a robust-loner if upon ignoring rows whose $\ell_{1}$ distance to $M^{\prime j}$ is less than $d = {{{5\epsilon}/\alpha} + {2\epsilon}}$, the $\ell_{1}$-distance of $M^{\prime j}$ to the convex hull of the remaining rows is more than $2\epsilon$. Note that we can identify robust-loner rows using linear programming.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Claim 5.8", "weight": 1.0} -->

The following two claims establish that a row of $M^{\prime j}$ is a robust-loner if and only if it is close to some row $W^{i}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Claim 5.9", "weight": 1.0} -->

If $M^{\prime j}$ has distance more than $d + \epsilon$ to all of the $W^{i}$'s, then it cannot be a robust loner.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Claim 5.9", "weight": 1.0} -->

Proof: Such an $M^{\prime j}$ has distance at least $d$ to each of the canonical rows. The previous claim shows $M^{\prime j}$ is close to the convex hull of the canonical rows and thus by definition it cannot be a robust-loner. $\blacksquare$

<!-- chunk {"id": "body-0071", "role": "body", "section": "Claim 5.10", "weight": 1.0} -->

All canonical rows are robust-loners.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Claim 5.10", "weight": 1.0} -->

The previous claim implies that each robust-loner row is within $\ell_{1}$-distance $d + \epsilon$ to some $W^{i}$ and conversely, for every $W^{i}$ there is at least one robust-loner row that is close to it. Since the $\ell_{1}$-distances between $W^{i}$'s are at least $4{({d + \epsilon})}$, we can apply distance based clustering on the robust-loner rows: place two robust-loner rows into the same cluster if and only if these rows are within $\ell_{1}$-distance at most $2{({d + \epsilon})}$. Clearly we will obtain $r$ clusters, one corresponding to each of the $W^{i}$'s.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Claim 5.10", "weight": 1.0} -->

Choose one row from each of the cluster, and using similar argument as Claim 5.8 we deduce that every row of $M^{\prime}$ is within ${{2{({d + \epsilon})}} + \epsilon} = {{{10\epsilon}/\alpha} + {7\epsilon}}$ to the convex hull of the rows we selected. Therefore these rows form a nonnegative $W^{\prime}$ and we can find $A^{\prime}$ so that $\left. \parallel{M^{\prime j} - {({A^{\prime}W^{\prime}})}^{j}}\parallel \right._{1} \leq {{{10\epsilon}/\alpha} + {7\epsilon}}$ for all $j$. $\blacksquare$

<!-- chunk {"id": "body-0074", "role": "body", "section": "Approximate Nonnegative Matrix Factorization", "weight": 1.0} -->

Here we consider the case in which the given matrix does not have an exact low-rank NMF but rather can be approximated by a nonnegative factorization with small inner-dimension. We refer to this as Approximate NMF. Unlike the algorithm in Theorem 5.7, the algorithm here works with general nonnegative matrix factorization: we do not make any assumptions on matrices $A$ and $W$. Throughout this section we will use $\left. \parallel\parallel \right._{F}$ to denote the Froebenius norm, $\left. \parallel\parallel \right._{2}$ to denote the spectral norm and $\left. \parallel\parallel \right.$ applied to a vector will denote the standard Euclidean norm.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Claim 6.2", "weight": 1.0} -->

Throughout this section, we will assume that the input matrix $M$ has rank at most $r$ - since otherwise we can compute $M^{\prime}$ and solve the problem for $M^{\prime}$. Then using the triangle inequality, any good approximation to $M^{\prime}$ will also be a good approximation to $M$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Claim 6.2", "weight": 1.0} -->

Throughout this section, we will use the notation $A_{t}$ to denote the $t^{th}$ column of $A$ and $W^{t}$ to denote the $t^{th}$ row of $W$. Note that $W^{t}$ is a row vector so we will frequently use $A_{t}W^{t}$ to denote an outer-product. Next, we apply a simple re-normalization that will allow us to state the main steps in our algorithm in a more friendly notation.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Claim 6.7", "weight": 1.0} -->

Proof: We prove that $W_{1}^{\prime} = {W - W_{0}^{\operatorname{\prime\prime}}} = {{({W_{0} - W_{0}^{\operatorname{\prime\prime}}})} + W_{1}}$ is a feasible solution and that the objective value of this solution is the value claimed in the lemma.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Claim 6.7", "weight": 1.0} -->

Lemma 6.4 bounds the first term and Lemma 6.5 bounds the second term. The square of the last term is bounded by the objective function of the convex program. $\blacksquare$

<!-- chunk {"id": "body-0079", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Here, we initiated a rigorous study of nonnegative matrix factorization. Our hardness result rules out significant improvements over our worst-case results for fixed inner-dimension $r$. We believe that our $\text{poly}{(m,n,r)}$-time algorithm for finding separable factorizations may point the way for future work. What other plausible conditions can one impose on the factors in real-life applications? We also hope our work promotes further theoretical study of nonnegative rank.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This work is part of a broader agenda of bringing greater rigor to the analysis of algorithms used in machine learning. Currently, heuristic approaches are popular because the solution concepts are believed to be intractable. Our results, for example our algorithm for NMF under the separability condition, raise hope that sometimes the solution concepts may not be intractable after all.
