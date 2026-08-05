<!-- arxiv-full-text:v1 {"arxiv_id": "1111.0952", "source": "ar5iv"} -->

## Introduction

In the Nonnegative Matrix Factorization (NMF) problem we are given an $n \times m$ matrix $M$ with nonnegative real entries (such a matrix will be henceforth called "nonnegative") and an integer $r > 0$. Our goal is to express $M$ as $AW$ where $A$ and $W$ are nonnegative matrices of size $n \times r$ and $r \times m$ respectively. We refer to $r$ as the inner-dimension of the factorization and the smallest value of $r$ for which there is such a factorization as the nonnegative rank of $M$. An equivalent formulation is that our goal is to write $M$ as the sum of $r$ nonnegative rank-one matrices.^11^1It is a common misconception that since the real rank is the maximum number of linearly independent columns, the nonnegative rank must be the size of the largest set of columns in which no column can be written as a nonnegative combination of the rest. This is false, and has been the source of many incorrect proofs demonstrating a gap between rank and nonnegative rank. A correct proof finally follows from the results of Fiorini et al. We note that $r$ must be at least the rank of $M$ in order for such a factorization to exist. In some applications, it makes sense to instead ask for $AW$ to be a good approximation to $M$ in some suitable matrix norm. We refer to the problem of finding a nonnegative $A$ and $W$ of inner-dimension $r$ that (approximately) minimizes $\left. \parallel{M - {AW}}\parallel \right._{F}$ as Approximate NMF, where $\left. \parallel\parallel \right._{F}$ denotes the Frobenius norm. Without the restriction that $A$ and $W$ be nonnegative, the problem can be solved exactly via singular value decomposition.

NMF is a fundamental problem that has been independently introduced in a number of different contexts and applications. Many interesting heuristics and local search algorithms (including the familiar Expectation Maximization or EM) have been proposed to find such factorizations. One compelling family of applications is data analysis, where a nonnegative factorization is computed in order to extract certain latent relationships in the data and has been applied to image segmentation, information retrieval and document clustering. NMF also has applications in fields such as chemometrics (where the problem has a long history of study under the name self modeling curve resolution) and biology (e.g. in vision research ): in some cases, the underlying physical model for a system has natural restrictions that force a corresponding matrix factorization to be nonnegative. In demography (see e.g., ), NMF is used to model the dynamics of marriage through a mechanism similar to the chemical laws of mass action. In combinatorial optimization, Yannakakis characterized the number of extra variables needed to succinctly describe a given polytope as the nonnegative rank of an appropriate matrix (called the "slack matrix"). In communication complexity, Aho et al showed that the log of the nonnegative rank of a Boolean matrix is polynomially related to its deterministic communication complexity - and hence the famous Log-Rank Conjecture of Lovasz and Saks is equivalent to showing a quasi-polynomial relationship between real rank and nonnegative rank for Boolean matrices. In complexity theory, Nisan used nonnegative rank to prove lower bounds for non-commutative models of computation. Additionally, the 1993 paper of Cohen and Rothblum gives a long list of other applications in statistics and quantum mechanics. That paper also gives an exact algorithm that runs in exponential time.

### Question 1.1

Can a nonnegative matrix factorization be computed efficiently when the inner-dimension, $r$, is small?

Vavasis recently proved that the NMF problem is $NP$-hard when $r$ is large, but this only rules out an algorithm whose running time is polynomial in $n$, $m$ and $r$. Arguably, in most significant applications, $r$ is small. Usually the algorithm designer posits a two-level generative model for the data and uses NMF to compute "hidden" variables that explain the data. This explanation is only interesting when the number of hidden variables ($r$) is much smaller than the number of examples ($m$) or the number of observations per example ($n$). In information retrieval, we often take $M$ to be a "term-by-document" matrix where the ${(i,j)}^{th}$ entry in $M$ is the frequency of occurrence of the $i^{th}$ term in the $j^{th}$ document in the database. In this context, a NMF computes $r$ "topics" which are each a distribution on words (corresponding to the $r$ columns of $A$) and each document (a column in $M$) can be expressed as a distribution on topics given by the corresponding column of $W$. This example will be a useful metaphor for thinking about nonnegative factorization. In particular it justifies the assertion $r$ should be small -- the number of topics should be much smaller than the total number of documents in order for this representation to be meaningful. See Section A for more details.

Focusing on applications, and the overwhelming empirical evidence that heuristic algorithms do find good-enough factorizations in practice, motivates our next question.

### Question 1.2

Can we design very efficient algorithms for NMF if we make reasonable assumptions about $M$?

### Our Results

Here we largely resolve Question 1.1. We give both an algorithm for accomplishing this algorithmic task that runs in polynomial time for any constant value of $r$ and we complement this with an intractability result which states that assuming the Exponential Time Hypothesis no algorithm can solve the exact NMF problem in time ${({nm})}^{o{(r)}}$.

### Theorem 1.3

There is an algorithm for the Exact NMF problem (where $r$ is the target inner-dimension) that runs in time $O{({({nm})}^{r^{2}2^{r}})}$.

This result is based on algorithms for deciding the first order theory of the reals - roughly the goal is to express the decision question of whether or not the matrix $M$ has nonnegative rank at most $r$ as a system of polynomial equations and then to apply algorithms in algebraic geometry to determine if this semi-algebraic set is non-empty. The complexity of these procedures is dominated by the number of distinct variables occurring in the system of polynomial equations. In fact, the number of distinct variables plays an analogous role to VC-dimension, in a sense and the running time of algorithms for determining if a semi-algebraic set is non-empty depend exponentially on this quantity. Additionally these algorithms can compute successive approximations to a point in the set at the cost of an additional factor in the run time that is polynomial in the number of bits in the input and output. The naive formulation of the NMF decision problem as a non-emptiness problem is to use ${nr} + {mr}$ variables, one for each entry in $A$ or $W$. This would be unacceptable, since even for constant values of $r$, the associated algorithm would run in time exponential in $n$ and $m$.

At the heart of our algorithm is a structure theorem -- based on a novel method for reducing the number of variables needed to define the associated semi-algebraic set. We are able to express the decision problem for nonnegative matrix factorization using $r^{2}2^{r}$ distinct variables (and we make use of tools in geometry, such as the notion of a separable partition, to accomplish this ). Thus we obtain the algorithm quoted in the above theorem. All that was known prior to our work (for constant values for $r$) was an exponential time algorithm, and local search heuristics akin to the Expectation-Maximization (EM) Algorithm with unproved correctness or running time.

A natural requirement on $A$ is that its columns be linearly independent. In most applications, NMF is used to express a large number of observed variables using a small number of hidden variables. If the columns of $A$ are not linearly independent then Radon's Lemma implies that this expression can be far from unique. In the example from information retrieval, this translates to: there are candidate documents that can be expressed as a convex combination of one set of topics, or could alternatively be expressed as a convex combination of an entirely disjoint set of topics (see Section 2.1). When we add the requirement that the columns of $A$ be linearly independent, we refer to the associated problem as the Simplicial Factorization (SF) problem. In this case the doubly-exponential dependence on $r$ in the previous theorem can be improved to singly-exponential. Our algorithm is again based on the first order theory of the reals, but here the system of equations is much smaller so in practice one may be able to use heuristic approaches to solve this system (in which case, the validity solution can be easily checked).

### Theorem 1.4

There is an algorithm for the Exact SF problem (where $r$ is the target inner-dimension) that runs in time $O{({({nm})}^{r^{2}})}$.

We complement these algorithms with a fixed parameter intractability result. We make use of a recent result of Patrascu and Williams (and engineer low-dimensional gadgets inspired by the gadgets of Vavasis ) to show that under the Exponential Time Hypothesis, there is no exact algorithm for NMF that runs in time ${({nm})}^{o{(r)}}$. This intractability result holds also for the SF problem.

### Theorem 1.5

If there is an exact algorithm for the SF problem (or for the NMF problem) that runs in time $O{({({nm})}^{o{(r)}})}$ then $3$-SAT can be solved in $2^{o{(n)}}$ time on instances with $n$ variables.

Now we turn to Question 1.2. We consider the nonnegative matrix factorization problem under the "separability" assumption introduced by Donoho and Stodden in the context of image segmentation. Roughly, this assumption asserts that there are $r$ rows of $A$ that can be permuted to form the identity matrix. If we knew the names of these rows, then computing a nonnegative factorization would be easy. The challenge in this context, is to avoid brute-force search (which runs in time $n^{r}$) and to find these rows in time polynomial in $n$, $m$ and $r$. To the best of our knowledge the following is the first example of a polynomial-time algorithm that provably works under a non-trivial condition on the input.

### Theorem 1.6

There is an exact algorithm that can compute a separable, nonnegative factorization $M = {AW}$ (where $r$ is the inner-dimension) in time polynomial in $n$, $m$ and $r$ if such a factorization exists.

Donoho and Stodden argue that the separability condition is naturally met in the context of image segmentation. Additionally, Donoho and Stodden prove that separability in conjunction with some other conditions guarantees that the solution to the NMF problem is unique. Our theorem above is an algorithmic counterpart to their results, but requires only separability. Our algorithm can also be made noise tolerant, and hence works even when the separability condition only holds in an approximate sense. Indeed, an approximate separability condition is regarded as a fairly benign assumption and is believed to hold in many practical contexts in machine learning. For instance it is usually satisfied by model parameters fitted to various generative models (e.g. LDA in information retrieval). (We thank David Blei for this information.)

Lastly, we consider the case in which the given matrix $M$ does not have an exact low-rank NMF but rather can be approximated by a nonnegative factorization with small inner-dimension.

### Theorem 1.7

There is a $2^{{poly}{({r{\log{({1/\epsilon})}}})}}{poly}{(n,m)}$-time algorithm that, given a $M$ for which there is a nonnegative factorization $AW$ (of inner-dimension $r$) which is an $\epsilon$-approximation to $M$ in Frobenius norm, computes $A'$ and $W'$ satisfying The rest of the paper is organized as follows: In Section 2 we give an exact algorithm for the SF problem and in Section 3 we give an exact algorithm for the general NMF problem. In Section 4 we prove a fixed parameter intractability result for the SF problem. And in Section 5 and Section 6 we give algorithms for the separable and adversarial nonnegative fatorization problems. Throughout this paper, we will use the notation that $M_{i}$ and $M^{j}$ are the $i^{th}$ column and $j^{th}$ row of $M$ respectively.

## Simplicial Factorization

Here we consider the simplicial factorization problem, in which the target inner-dimension is $r$ and the matrix $M$ itself has rank $r$. Hence in any factorization $M = {AW}$ (where $r$ is the inner-dimension), $A$ must have full column rank and $M$ must have full row rank.

### Justification for Simplicial Factorization

We first argue that the extra restriction imposed in simplicial factorization is natural in many contexts: Through a re-scaling (see Section LABEL:sec:appendix:separable for more details), we can assume that the columns of $M$, $A$ and $W$ all have unit $\ell_{1}$ norm. The factorization $M = {AW}$ can be interpreted probabilistically: each column of $M$ can be expressed as a convex combination (given by the corresponding column of $W$) of columns in $A$. In the example in the introduction, columns of $M$ represent documents and the columns of $A$ represent "topics". Hence a nonnegative factorization is an "explanation": each document can be expressed as a convex combination of the topics.

But if $A$ does not have full column rank then this explanation is seriously deficient. This follows from a restatement of Radon's Lemma. Let $conv{(A_{U})}$ be the convex hull of the columns $A_{i}$ for $i \in U$.

### Observation 1

If $A$ is an $n \times r$ (with $n \geq r$) matrix and ${rank{(A)}} < r$, then there are two disjoint sets of columns ${U,V} \subset {\lbrack r\rbrack}$ so that ${{conv{(A_{U})}} \cap {conv{(A_{V})}}} \neq \varnothing$.

The observation implies that there is some candidate document $x$ that can be expressed as a convex combination of topics (in $U$), or instead can be expressed as a convex combination of an entirely disjoint set ($V$) of topics. The end goal of NMF is often to use the representation of documents as distributions on topics to perform various tasks, such as clustering or information retrieval. But if (even given the set of topics in a database) it is this ambiguous to determine how we should represent a given document as a convex combination of topics, then the topics we have extracted cannot be very useful for clustering! In fact, it seems unnatural to not require the columns of $A$ to be linearly independent!

Next, one should consider the process (probabilistic, presumably) that generates the datapoints, namley, columns of $M$. Any reasonable process for generating columns of $M$ from the columns of $A$ would almost surely result in a matrix $M$ whose rank equals the rank of $A$. But then $M$ has the same rank as $A$.

### Algorithm for Simplicial Factorization

In this Section we give an algorithm that solves the simplicial factorization problem in ${({nm})}^{O{(r)}}$ time. Let $L$ be the maximum bit complexity of any coefficient in the input.

### Theorem 2.1

There is an $O{({({nm})}^{O{(r^{2})}})}$ time algorithm for deciding if the simplicial factorization problem has a solution of inner-dimension at most $r$. Furthermore, we can compute a rational approximation to the solution up to accuracy $\delta$ in time ${poly}{(L,{({nm})}^{O{(r^{2})}},{\log{1/\delta}})}$.

The above theorem is proved by using Lemma 2.3. ‣ 2.2 Algorithm for Simplicial Factorization ‣ 2 Simplicial Factorization ‣ Computing a Nonnegative Matrix Factorization – Provably") below to reduce the problem of finding a simplicial factorization to finding a point inside a semi-algebraic set with $poly{(n)}$ constraints and $2r^{2}$ real-valued variables (or deciding that this set is empty). The decision problem can be solved using the well-known algorithm of Basu et. al. solves this problem in $n^{O{(r^{2})}}$ time. We can instead use the algorithm of Renegar (a bound of ${poly}{(L,{({nm})}^{O{(r^{2})}})}$ on the bit complexity of the coefficients in the solution due to Grigor'ev and Vorobjov ) to compute a rational approximation to the solution up to accuracy $\delta$ in time ${poly}{(L,{({nm})}^{O{(r^{2})}},{\log{1/\delta}})}$.

This reduction uses the fact that since $A,W$ have full rank they have "pseudo-inverses" $A^{+}$, $W^{+}$ which are $r \times n$ and $n \times r$ matrices respectively such that ${A^{+}A} = {WW^{+}} = I_{r \times r}$. Thus ${A^{+}M_{i}} = {A^{+}AW_{i}} = W_{i}$ and similarly ${M^{j}W^{+}} = A^{j}$.

### Definition 2.2

Let $C = \left\{ u_{1},u_{2},..u_{r} \right\}$ be a basis for the columns of $M$ in $\Re^{n}$, and let $R = \left\{ v_{1},v_{2},{\ldotsv_{r}} \right\}$ be a basis for the rows of $M$ in $\Re^{m}$.

Then $M_{C}$ (a size $r \times m$ matrix) denotes the columns of $M$ expressed in the basis $\mathcal{C}$, and similarly $M_{R}$ (a size $n \times r$ matrix) denotes the rows of $M$ expressed in the basis $\mathcal{R}$.

### Lemma 2.3 (Structure Lemma for Simplicial Factorization)

$M$ has a simplicial factorization rank $r$ iff for every basis $C$ for the columns and basis $B$ for the rows of $M$, there are $r \times r$ matrices $T_{C},T_{R}$ such that: (i) $T_{C}M_{C}$ and $M_{R}T_{R}$ are nonnegative matrices (ii) ${M_{R}T_{R}T_{C}M_{C}} = M$ Proof: ("if") Suppose the conditions in the theorem are met. Then set $A = {M_{R}T_{R}}$ and $W = {T_{C}M_{C}}$. These matrices are nonnegative and have size $n \times r$ and $r \times m$ respectively, and furthermore are a factorization for $M$. Since ${rank{(M)}} = r$, $A$ and $W$ are a simplicial factorization.

("only if") Conversely suppose that there is a simplicial factorization $M = {AW}$. Let $\mathcal{C} = \left\{ {\mathcal{u}}_{1},{\mathcal{u}}_{2},..{\mathcal{u}}_{\mathcal{r}} \right\}$ and $\mathcal{R} = \left\{ {\mathcal{v}}_{1},{\mathcal{v}}_{2},{\ldots{\mathcal{v}}_{\mathcal{r}}} \right\}$ be arbitrary bases for the columns and rows of $M$ respectively. Let $U$ and $V$ be the corresponding $n \times r$ and $m \times r$ matrices. Let $M_{C}$ and $M_{R}$ be $r \times m$ and $n \times r$ representations in this basis for the columns and rows of $M$ - i.e. ${UM_{C}} = M$ and ${M_{R}V^{T}} = M$.

Define $r \times r$ matrices $T_{C} = {A^{+}U}$ and $T_{R} = {V^{T}W^{+}}$ where $A^{+}$ and $W^{+}$ are the respective pseudoinverses of $A,W$. Let us check that this choice of $T_{C}$ and $T_{R}$ satisfies the conditions in the theorem.

We can re-write ${T_{C}M_{C}} = {A^{+}UM_{C}} = {A^{+}M} = W$ and hence the first condition in the theorem is satisfied. Similarly ${M_{R}T_{R}} = {M_{R}V^{T}W^{+}} = {MW^{+}} = A$ and hence the second and third condition are also satisfied. $\blacksquare$

## General NMF

Now we consider the NMF problem where the factor matrices $A,W$ need not have full rank.

### Theorem 3.1

There is a $O{({({nm})}^{cr^{2}2^{r}})}$ time deterministic algorithm that given an $n \times m$ nonnegative matrix $M$ outputs a factorization $AW$ of inner dimension $r$ if such a factorization exists.

As in the Simplicial case the main idea will again be a reduction to an existence question for a semi-algebraic set, but this reduction is significantly more complicated than Lemma 2.3. ‣ 2.2 Algorithm for Simplicial Factorization ‣ 2 Simplicial Factorization ‣ Computing a Nonnegative Matrix Factorization – Provably").

### General Structure Theorem: Minimality

Our goal is to re-cast nonnegative matrix factorization (for constant $r$) as a system of polynomial inequalities where the number of variables is constant, the maximum degree is constant and the number of constraints is polynomially bounded in $n$ and $m$. The main obstacle is that $A$ and $W$ are large - we cannot afford to introduce a new variable to represent each entry in these matrices. We will demonstrate there is always a "minimal" choice for $A$ and $W$ so that: there is a collection of linear transformations $T_{1},T_{2},{\ldotsT_{g{(r)}}}$ from the column-span of $M$ to $\Re^{r}$ and a choice function $\sigma_{W}:{{\lbrack m\rbrack}\rightarrow{\lbrack{g{(r)}}\rbrack}}$ and a collection of linear transformations $S_{1},S_{2},{\ldotsS_{g{(r)}}}$ from the row-span of $M$ to $\Re^{r}$ and a choice function $\sigma_{A}:{{\lbrack n\rbrack}\rightarrow{\lbrack{g{(r)}}\rbrack}}$ And these linear transformations and choice functions satisfy the conditions: for each $i \in {\lbrack n\rbrack}$, $W_{i} = {T_{\sigma_{W}{(i)}}M_{i}}$ and for each $j \in {\lbrack m\rbrack}$, $A^{j} = {M^{j}S_{\sigma_{A}{(j)}}}$.

Furthermore, the number of possible choice functions $\sigma_{W}$ is at most $m^{cr^{2}f{(r)}}$ and the number of possible choice functions for $\sigma_{A}$ is at most $n^{cr^{2}g{(r)}}$. These choice functions are based on the notion of a simplicial partition, which we introduce later. We then give an algorithm for enumerating all simplicial partitions (this is the primary bottleneck in the algorithm). Fixing the choice functions $\sigma_{W}$ and $\sigma_{A}$, the question of finding linear transformations $T_{1},T_{2},{\ldotsT_{g{(r)}}}$ and $S_{1},S_{2},{\ldotsS_{g{(r)}}}$ that satisfy the above constraints (and the constraint that $M = {AW}$, and $A$ and $W$ are nonnegative) is exactly a system of polynomial inequalities with a $O{({r^{2}g{(r)}})}$ variables (each matrix $T_{i}$ or $S_{j}$ is $r \times r$), degree at most four and furthermore there are at most $O{({mn})}$ polynomial constraints.

In this subsection, we will give a procedure (which given $A$ and $W$) generates a "minimal" choice for $A$ and $W$ (call this minimal choice $A'$ and $W'$), and we will later establish that this "minimal" choice satisfies the structural property stated informally above.

### Definition 3.2

Let ${\mathcal{C}{(A)}} \subset 2^{\lbrack r\rbrack}$ denote the subsets of $\lbrack r\rbrack$ corresponding to maximal independent sets of columns (of $A$). Similarly let ${\mathcal{R}{(W)}} \subset 2^{\lbrack r\rbrack}$ denote the subsets of $\lbrack r\rbrack$ corresponding to maximal independent sets of rows (of $W$).

A basic fact from linear algebra is that all maximal independent sets of columns of $A$ have exactly $rank{(A)}$ elements and all maximal independent sets of rows of $W$ similarly have exactly $rank{(W)}$ elements.

### Definition 3.3

Let $\succ_{s}$ be the total ordering on subsets of $\lbrack r\rbrack$ of size $s$ so that if $U$ and $V$ are both subsets of $\lbrack r\rbrack$ of size $s$, $U \prec_{s}V$ iff $U$ is lexicographically before $V$.

### Definition 3.4

Given a column $M_{i}$, we will call a subset $U \in {\mathcal{C}{(A)}}$ a minimal basis for $M_{i}$ (with respect to $A$) if $M_{i} \in {cone{(A_{U})}}$ and for all $V \in {\mathcal{C}{(A)}}$ such that $M_{i} \in {cone{(A_{V})}}$ we must have $U \prec_{s}V$.

### Claim 3.5

If $M_{i} \in {cone{(A)}}$, then there is some $U \in {\mathcal{C}{(A)}}$ such that $M_{i} \in {cone{(A_{U})}}$.

### Definition 3.6

A proper chain $(A,W,A',W')$ is a set of nonnegative matrices for which $M = {AW}$, $M = {AW'}$ and $M = {A'W'}$ (the inner dimension of these factorizations is $r$) and functions $\sigma_{W'}:{{\lbrack m\rbrack}\rightarrow{\mathcal{C}{(A)}}}$ and $\sigma_{A'}:{{\lbrack n\rbrack}\rightarrow{\mathcal{R}{(W')}}}$ such that for all $i \in {\lbrack m\rbrack}$, ${AW_{i}'} = M_{i}$, ${supp{(W_{i}')}} \subset {\sigma_{W'}{(i)}}$ and $\sigma_{W'}{(i)}$ is a minimal basis with respect to $A$ for $M_{i}$ for all $j \in {\lbrack n\rbrack}$, ${A_{j}'W'} = M^{j}$, ${supp{(A^{j})}} \subset {\sigma_{A'}{(j)}}$ and $\sigma_{A'}{(j)}$ is a minimal basis with respect to $W'$ for $M^{j}$.

Note that the extra conditions on $W'$ (i.e. the minimal basis constraint) is with respect to $A$ and the extra conditions on $A'$ are with respect to $W'$. This simplifies the proof that there is always some proper chain, since we can compute a $W'$ that satisfies the above conditions with respect to $A$ and then find an $A'$ that satisfies the conditions with respect to $W'$.

### Lemma 3.7

If there is a nonnegative factorization $M = {AW}$ (of inner-dimension $r$), then there is a choice of nonnegative $A',W'$ of inner-dimension $r$ and functions $\sigma_{W'}:{{\lbrack m\rbrack}\rightarrow{\mathcal{C}{(A)}}}$ and $\sigma_{A'}:{{\lbrack n\rbrack}\rightarrow{\mathcal{R}{(W')}}}$ such that $(A,W,A',W')$ and $\sigma_{W'}$, $\sigma_{A'}$ form a proper chain.

Proof: The condition that there is some nonnegative $W$ for which $M = {AW}$ is just the condition that for all $i \in {\lbrack m\rbrack}$, $M_{i} \in {cone{(A)}}$. Hence, for each vector $M_{i}$, we can choose a minimal basis $U \in {\mathcal{C}{(A)}}$ using Claim 3.5. Then $M_{i} \in {cone{(A_{U})}}$ so there is some nonnegative vector $W_{i}'$ supported on $U$ such ${AW_{i}'} = M_{i}$ and we can set ${\sigma_{W'}{(i)}} = U$. Repeating this procedure for each column $M_{i}$, results in a nonnegative matrix $W'$ that satisfies the condition $M = {AW'}$ and for each $i \in {\lbrack m\rbrack}$, by design ${supp{(W_{i}')}} \subset {\sigma_{W'}{(i)}}$ and $\sigma_{W'}{(i)}$ is a minimal basis with respect to $A$ for $M_{i}$.

We can re-use this argument above, setting $M^{T} = {{(W^{'T})}A^{T}}$ and this interchanges the role of $A$ and $W$. Hence we obtain a nonnegative matrix $A'$ which satisfies $M = {A'W'}$ and for each $j \in {\lbrack n\rbrack}$, again by design we have that ${supp{(A^{j})}} \subset {\sigma_{A'}{(j)}}$ and $\sigma_{A'}{(j)}$ is a minimal basis with respect to $W$ for $M^{j}$. $\blacksquare$

### Definition 3.8

Let $\Pi{(A,U)}$ (for $U \in {\mathcal{C}{(A)}}$) denote the $r \times n$ linear transformation that is zero on all rows not in $U$ (i.e. ${\Pi{(A,U)}^{j}} = \overset{\rightarrow}{0}$ for $j \notin U$) and restricted to $U$ is ${\Pi{(A,U)}^{U}} = {(A_{U})}^{+}$ (where the $+$ operation denotes the Moore-Penrose pseudoinverse).

### Lemma 3.9

Let $(A,W,A',W')$ and $\sigma_{W'}$ and $\sigma_{A'}$ form a proper chain. For any index $i \in {\lbrack m\rbrack}$, let $U_{i} = {\sigma_{W'}{(i)}}$ and for any index $j \in {\lbrack n\rbrack}$ let $V_{j} = {\sigma_{A'}{(j)}}$. Then $W_{i}' = {\Pi{(A,U_{i})}M_{i}}$ and $A^{'j} = {M^{j}\Pi{(W^{'T},V_{j})}^{T}}$.

Notice that in the above lemma, the linear transformation that recovers the columns of $W'$ is based on column subsets of $A$, while the linear transformation to recover the rows of $A'$ is based on the row subsets of $W'$ (not $W$).

Proof: Since $(A,W,A',W')$ and $\sigma_{W'}$ and $\sigma_{A'}$ form a proper chain we have that ${AW'} = M$. Also ${supp{(W_{i}')}} \subset U_{i} = {\sigma_{W'}{(i)}}$. Consider the quantity $\Pi{(A,U_{i})}M_{i}$. For any $j \notin U_{i}$, ${({\Pi{(A,U_{i})}M_{i}})}_{j} = 0$. So consider where the last equality follows from the condition ${supp{(W_{i}')}} \subset U_{i}$. Since $U_{i} \in {\mathcal{C}{(A)}}$ we have that ${(A_{U_{i}})}^{+}A_{U_{i}}$ is the ${|U_{i}|} \times {|U_{i}|}$ identity matrix. Hence $W_{i}' = {\Pi{(A,U_{i})}M_{i}}$. An identical argument with $W'$ replaced with $A'$ and with $A$ replaced by $W^{'T}$ (and $i$ and $U_{i}$ replaced with $j$ and $V_{j}$) respectively implies that $A^{'j} = {M^{j}\Pi{(W^{'T},V_{j})}^{T}}$ too. $\blacksquare$ Note that there are at most ${|{\mathcal{C}{(A)}}|} \leq 2^{r}$ linear trasformations of the form $\Pi{(A,U_{i})}$ and hence the columns of $W'$ can be recovered by a constant number of linear transformations of the column span of $M$, and similarly the rows of $A'$ can also be recovered.

The remaining technical issue is we need to demonstrate that there are not too many (only polynomially many, for constant $r$) choice functions $\sigma_{W'}$ and $\sigma_{A'}$ and that we can enumerate over this set efficiently. In principle, even if say $\mathcal{C}{(A)}$ is just two sets, there are exponentially many choices of which (of the two) linear transformation to use for each column of $M$. However, when we use lexicographic ordering to tie break (as in the definition of a minimal basis), the number of choice functions is polynomially bounded. We will demonstrate that the choice function $\sigma_{W'}:{{\lbrack m\rbrack}\rightarrow{\mathcal{C}{(A)}}}$ arising in the definition of a proper chain can be embedded in a restricted type of geometric partitioning of $M$ which we call a simplicial partition.

### General Structure Theorem: Simplicial Partitions

Here, we establish that the choice functions $\sigma_{W'}$ and $\sigma_{A'}$ in a proper chain are combinatorially simple. The choice function $\sigma_{W'}$ can be regarded as a partition of the columns of $M$ into $|{\mathcal{C}{(A)}}|$ sets, and similarly the choice function $\sigma_{A'}$ is a partition of the rows of $M$ into $\mathcal{R}{(W')}$ sets. Here we define a geometric type of partitioning scheme which we call a simplicial partition, which has the property that there are not too many simplicial partitions (by virtue of this class having small VC-dimension), and we show that the partition functions $\sigma_{W'}$ and $\sigma_{A'}$ arising in the definition of a proper chain are realizable as (small) simplicial partitions.

### Definition 3.10

A $(k,s)$-simplicial partition of the columns of $M$ is generated by a collection of $k$ sets of $s$ hyperplanes Let $Q_{i} = {\{{{{i'\text{~s.t. for all~}j} \in {\lbrack s\rbrack}},{{h_{j}^{i} \cdot M_{i'}} \geq 0}}\}}$. Then this collection of sets of hyperplanes results in the partition $P_{k + 1} = {{\lbrack m\rbrack} - P_{1} - {P_{2}\ldots} - P_{k}}$ If ${rank{(A)}} = s$, we will be interested in a $(\binom{r}{s},s)$-simplicial partition.

### Lemma 3.11

Let $(A,W,A',W')$ and $\sigma_{W'}$ and $\sigma_{A'}$ form a proper chain. Then the partitions corresponding to $\sigma_{W'}$ and to $\sigma_{A'}$ (of columns and rows of $M$ respectively) are a $(\binom{r}{s},s)$-simplicial partition and a $(\binom{r}{t},t)$-simplicial partition respectively, where ${rank{(A)}} = s$ and ${rank{(W')}} = t$.

Proof: Order the sets in $\mathcal{C}{(A)}$ according to the lexicographic ordering $\succ_{s}$, so that $V_{1} \prec_{s}V_{2} \prec_{s}{\ldotsV_{k}}$ for $k = {|{\mathcal{C}{(A)}}|}$. Then for each $j$, let $\mathcal{H}^{j}$ be the rows of the matrix ${(A_{V_{j}})}^{+}$. Note that there are exactly ${rank{(A)}} = s$ rows, hence this defines a $(k,s)$-simplicial partition.

### Claim 3.12

${\sigma_{W'}{(i)}} = j$ if and only if $M_{i} \in P_{j}$ in the $(k,s)$-simplicial partition generated by $\mathcal{H}^{1},\mathcal{H}^{2},{\ldots\mathcal{H}^{k}}$.

Proof: Since $(A,W,A',W')$ and $\sigma_{W'}$ and $\sigma_{A'}$ forms a proper chain, we have that $M = {AW'}$. Consider a column $i$ and the corresponding set $V_{i} = {\sigma_{W'}{(i)}}$. Recall that $V_{j}$ is the $j^{th}$ set in $\mathcal{C}{(A)}$ according to the lexicographic ordering $\succ_{s}$. Also from the definition of a proper chain $V_{i}$ is a minimal basis for $M_{i}$ with respect to $A$. Consider any set $V_{j'} \in {\mathcal{C}{(A)}}$ with $j' < j$. Then from the definition of a minimal basis we must have that $M_{i} \notin {cone{(A_{V_{j'}})}}$. Since $V_{j'} \in {\mathcal{C}{(A)}}$, we have that the transformation ${(A_{V_{j'}})}{(A_{V_{j'}})}^{+}$ is a projection onto $span{(A)}$ which contains $span{(M)}$. Hence ${{(A_{V_{j'}})}{(A_{V_{j'}})}^{+}M_{i}} = M_{i}$, but $M_{i} \notin {cone{(A_{V_{j'}})}}$ so ${(A_{V_{j'}})}^{+}M_{i}$ cannot be a nonnegative vector. Hence $M_{i}$ is not in $P_{j'}$ for any $j' < j$. Furthermore, $M_{i}$ is in $Q_{j}$: using Lemma 3.9 we have ${\Pi{(A,V_{j})}M_{i}} = {\Pi{(A,V_{j})}AW_{i}'} = W_{i}' \geq \overset{\rightarrow}{0}$ and so ${{(A_{V_{j}})}^{+}M_{i}} = {({\Pi{(A,V_{j})}M_{i}})}_{V_{j}} \geq \overset{\rightarrow}{0}$. $\blacksquare$ We can repeat the above replacing $A$ with $W^{'T}$ and $W'$ with $A'$, and this implies the lemma. $\blacksquare$

### Enumerating Simplicial Partitions

Here we give an algorithm for enumerating all $(k,s)$-simplicial partitions (of, say, the columns of $M$) that runs in time $O{(m^{ks{({r + 1})}})}$. An important observation is that the problem of enumerating all simplicial partitions can be reduced to enumerating all partitions that arise from a single hyperplane. Indeed, we can over-specify a simplicial partition by specifying the partition (of the columns of $M$) that results from each hyperplane in the set of $ks$ total hyperplanes that generates the simplicial partition. From this set of partitions, we can recover exactly the simplicial partition.

A number of results are known in this domain, but surprisingly we are not aware of any algorithm that enumerates all partitions of the columns of $M$ (by a single hyperplane) that runs in polynomial time (for ${dim{(M)}} \leq r$ and $r$ is constant) without some assumption on $M$. For example, the VC-dimension of a hyperplane in $r$ dimensions is $r + 1$ and hence the Sauer-Shelah lemma implies that there are at most $O{(m^{r + 1})}$ distinct partitions of the columns of $M$ by a hyperplane. In fact, a classic result of Harding gives a tight upper bound of $O{(m^{r})}$. Yet these bounds do not yield an algorithm for efficiently enumerating this structured set of partitions without checking all partitions of the data.

A recent result of Hwang and Rothblum comes close to our intended application. A separable partition into $p$ parts is a partition of the columns of $M$ into $p$ sets so that the convex hulls of these sets are disjoint. Setting $p = 2$, the number of separable partitions is exactly the number of distinct hyperplane partitions. Under the condition that $M$ is in general position (i.e. there are no $t$ columns of $M$ lying on a dimension $t - 2$ subspace where $t = {{rank{(M)}} - 1}$), Hwang and Rothblum give an algorithm for efficiently enumerating all distinct hyperplane partitions.

Here we give an improvement on this line of work, by removing any conditions on $M$ (although our algorithm will be slightly slower). The idea is to encode each hyperplane partition by a choice of not too many data points. To do this, we will define a slight generalization of a hyperplane partition that we will call a hyperplane separation:

### Definition 3.13

A hyperplane $h$ defines a mapping (which we call a hyperplane separation) from columns of $M$ to $\{{- 1},0,1\}$ depending on the sign of $h \cdot M_{i}$ (where the sign function is $1$ for positive values, $- 1$ for negative values and $0$ for zero).

A hyperplane partition can be regarded as a mapping from columns of $M$ to $\{{- 1},1\}$ where we adopt the convention that $M_{i}$ such that $h \circ M_{i}$ is mapped to $1$.

### Definition 3.14

A hyperplane partition (defined by $h$) is an extension of a hyperplane separation (defined by $g$) if for all $i$, ${g{(M_{i})}} \neq 0\Rightarrow{g{(M_{i})}} = {h{(M_{i})}}$.

### Lemma 3.15

Let ${rank{(M)}} = s$, then for any hyperplane partition (defined by $h$), there is a hyperplane $g$ that contains $s$ affinely independent columns of $M$ and for which $h$ (as a partition) is an extension of $g$ (as a separation).

Proof: After an appropriate linear transformation (of the columns of $M$ and the hyperplanes), we can assume that $M$ is full rank. If the $h$ already contains $s$ affinely independent columns of $M$, then we can choose $g = h$. If not we can perturb $h$ in some direction so that for any column with ${h{(M_{i})}} = 0$, we maintain the invariant that $M_{i}$ is contained on the perturbed hyperplane $h'$. Since ${rank{(M)}} = s$ this perturbation has non-zero inner product with some column in $M$ and so this hyperplane $h'$ will eventually contain a new column from $M$ (without changing the sign of $h{(M_{i})}$ for any other column). We can continue this argument until the hyperplane contains $s$ affinely independent columns of $M$ and by design on all remaining columns agrees in sign with $h$. $\blacksquare$

### Lemma 3.16

Let ${rank{(M)}} = s$. For any hyperplane $h$ (which defines a partition), there is a collection of $k \leq s$ sets of (at most $s$) columns of $M$, $S_{1},S_{2},..S_{k}$ so that any hyperplanes $g_{1},g_{2},..g_{k}$ which contain $S_{1},S_{2},{\ldotsS_{k}}$ respectively satisfy: For all $i$, $h{(M_{i})}$ (as a partition) is equal to the value of $g_{j}{(M_{i})}$, where $j$ is the smallest index for which ${g_{j}{(M_{i})}} \neq 0$. Furthermore these subsets are nested: $S_{1} \supset S_{2} \supset \ldots \supset S_{k}$.

Proof: We can apply Lemma 3.15 repeatedly. When we initially apply the lemma, we obtain a hyperplane $g_{1}$ that can be extended (as a separation) to the partition corresponding to $h$. In the above function (defined implicitly in the lemma) this fixes the partition of the columns except those contained in $g_{1}$. So we can then choose $M'$ to be the columns of $M$ that are contained in $g_{1}$, and recurse. If $S_{2}$ is the largest set of columns output from the recursive call, we can add columns of $M$ contained in $g_{1}$ to this set until we obtain a set of $s + 1$ affinely independent columns contained in $g_{1}$, and we can output this set (as $S_{1}$). $\blacksquare$

### Theorem 3.17

Let ${rank{(M)}} = s$. There is an algorithm that runs in time $O{({m^{s}{({s + 2})}^{s}})}$ time to enumerate all hyperplane partitions of the columns of $M$.

Proof: We can apply Lemma 3.16 and instead enumerate the sets of points $S_{1},S_{2},{\ldotsS_{s}}$. Since these sets are nested, we can enumerate all choices as follows: choose at most $s$ columns corresponding to the set $S_{1}$ initialize an active set $T = S_{1}$ until $T$ is empty either choose a column to be removed from the active set or indicate that the current active set represents the next set $S_{i}$ and choose the sign of the corresponding hyperplane There are at most $O{({m^{s}{({s + 2})}^{s}})}$ such choices, and for each choice we can then run a linear program to determine if there is a corresponding hyperplane partition. (In fact, all partitions that result from the above procedure will indeed correspond to a hyperplane partition). The correctness of this algorithm follows from Lemma 3.16. $\blacksquare$ This immediately implies:

### Corollary 3.18

There is an algorithm that runs in time $O{(m^{ks^{2})})}$ that enumerates a set of partitions of the columns of $M$ that contains the set of all $(k,s)$-simplicial partitions (of the columns of $M$).

### Solving Systems of Polynomial Inequalities

The results of Basu et al give an algorithm for finding a point in a semi-algebraic set defined by $O{({mn})}$ constraints on polynomials of total degree at most $d$, and $f{(r)}$ variables in time $O{({({mnd})}^{cf{(r)}})}$. Using our structure theorem for nonnegative matrix factorization, we will re-cast the decision problem of whether a nonnegative matrix $M$ has nonnegative rank $r$ as an existence question for a semi-algebraic set.

### Theorem 3.19

There is an algorithm for deciding if a $n \times m$ nonnegative matrix $M$ has nonnegative rank $r$ that runs in time $O{({({nm})}^{O{({r^{2}2^{r}})}})}$. Furthermore, we can compute a rational approximation to the solution up to accuracy $\delta$ in time ${poly}{(L,{({nm})}^{O{({r^{2}2^{r}})}},{\log{1/\delta}})}$.

We first prove the first part of this theorem using the algorithm of Basu et al, and we instead use the algorithm of Renegar to compute a rational approximation to the solution up to accuracy $\delta$ in time ${poly}{(L,{({nm})}^{O{({r^{2}2^{r}})}},{\log{1/\delta}})}$.

Proof: Suppose there is such a factorization. Using Lemma 3.7, there is also a proper chain. We can apply Lemma 3.11 and using the algorithm in Theorem 3.17 we can enumerate over a superset of simplicial partitions. Hence, at least one of those partitions will result in the choice functions $\sigma_{W'}$ and $\sigma_{A'}$ in the proper chain decomposition for $M = {AW}$.

Using Lemma 3.9 there is a set of at most $2^{r}$ linear transformations $T_{1},T_{2},{\ldotsT_{2^{r}}}$ which recover columns of $W'$ given columns of $M$, and similarly there is a set of at most $2^{r}$ linear transformations $S_{1},S_{2},{\ldotsS_{2^{r}}}$ which recover the rows of $A'$ given rows of $M$. Note that these linear transformations are from the column-span and row-span of $M$ respectively, and hence are from subspaces of dimension at most $r$. So apply a linear transformation to columns of $M$ and one to rows of $M$ to to recover matrices $M_{C}$ and $M_{R}$ respectively (which are no longer necessarily nonnegative) but which are dimension $r \times m$ and $n \times r$ respectively. There will still be a collection of at most $2^{r}$ linear transformations from columns of $M_{C}$ to columns of $W'$, and similarly for $M_{R}$ and $A'$.

We will choose $r^{2}$ variables for each linear transformation, so there are $2 \ast r^{2} \ast 2^{r}$ variables in total. Then we can write a set of $m$ linear constraints to enforce that for each column of ${(M_{C})}_{i}$, the transformation corresponding to $\sigma_{W'}{(i)}$ recovers a nonnegative vector. Similarly we can define a set of $n$ constraints based on rows in $M_{R}$.

Lastly we can define a set of constraints that enforce that we do recover a factorization for $M$: For all ${i \in {\lbrack m\rbrack}},{j \in {\lbrack n\rbrack}}$, let $i' = {\sigma_{W'}{(i)}}$ and $j' = {\sigma_{A'}{(j)}}$. Then we write the constraint ${{(M_{C})}^{j}S_{j'}T_{i'}{(M_{R})}_{i}} = M_{i}^{j}$. This constraint has degree at two in the variables corresponding to the linear transformations. Lemma 3.7 implies that there is some choice of these transformations that will satisfy these constraints (when we formulate these constraints using the correct choice functions in the proper chain decomposition). Furthermore, any set of transformations that satisfies these constraints does define a nonnegative matrix factorization of inner dimension $r$ for $M$.

And of course, if there is no inner dimension $r$ nonnegative factorization, then all calls to the algorithm of Basu et al will fail and we can return that there is no such factorization. $\blacksquare$ The result in Basu et. al. is a quantifier elimination algorithm in the Blum, Shub and Smale (BSS) model of computation. The BSS model is a model for real number computation and it is natural to ask what is the bit complexity of finding a rational approximation of the solutions. There has been a long line of research on the decision problem for first order theory of reals: given a quantified predicate over polynomial inequalities of reals, determine whether it is true or false. What we need for our algorithm is actually a special case of this problem: given a set of polynomial inequalities over real variables, determine whether there exists a set of values for the variables so that all polynomial inequalities are satisfied. In particular, all variables in our problem are quantified by existential quantifier and there are no alternations. For this kind of problem Grigor'ev and Vorobjov first gave a singly-exponential time algorithm that runs in ${({nd})}^{O{({f{(r)}^{2}})}}$ where $n$ is the number of polynomial inequalities, $d$ is the maximum degree of the polynomials and $f{(r)}$ is the number of variables. The bit complexity of the algorithm is ${poly}{(L,{({nd})}^{O{({f{(r)}^{2}})}})}$ where $L$ is the maximum length of the coefficients in the input. Moreover, their algorithm also gives an upperbound of ${poly}{(L,{({nd})}^{O{({f{(r)}})}})}$ on the number of bits required to represent the solutions. Renegar gave a better algorithm that for the special case we are interested in takes time ${({nd})}^{O{({f{(r)}})}}$. Using his algorithm with binary search (with search range bounded by Grigor'ev et.al.), we can find rational approximations to the solutions with accuracy up to $\delta$ in time ${poly}{(L,{({nm})}^{O{({f{(r)}})}},{\log{1/\delta}})}$.

We note that our results on the SF problem are actually a special case of the theorem above (because our structural lemma for simplicial factorization is a special case of our general structure theorem):

### Corollary 3.20

There is an algorithm for determining whether the positive rank of a nonnegative $n \times m$ matrix $M$ equals the rank and this algorithm runs in time $O{({({nm})}^{cr^{2}})}$.

Proof: If ${rank{(M)}} = r$, then we know that both $A$ and $W$ must be full rank. Hence $\mathcal{C}{(A)}$ and $\mathcal{R}{(W)}$ are both just the set $\{ 1,2,{\ldotsr}\}$. Hence we can circumvent the simplicial partition machinery, and set up a system of polynomial constraints in at most $2r^{2}$ variables. $\blacksquare$

## Strong Intractability of Simplicial Factorization

Here we give evidence that finding a simplicial factorization of dimension $r$ probably cannot be solved in ${({nm})}^{o{(r)}}$ time, unless $3$-SAT can be solved in $2^{o{(n)}}$ time (in other words, if the Exponential Time Hypothesis of is true). Surprisingly, even the $NP$-hardness of the problem for general $r$ was only proved quite recently by Vavasis. That reduction is the inspiration for our result, though unfortunately we were unable to use it directly to get low-dimensional instances. Instead we give a new reduction using the $d$-SUM Problem.

### Definition 4.1 ($d$-SUM)

In the $d$-SUM problem we are given a set of $N$ values $\{ s_{1},s_{2},{\ldotss_{N}}\}$ each in the range $\lbrack 0,1\rbrack$, and the goal is to determine if there is a set of $d$ numbers (not necessarily distinct) that sum to exactly $d/2$.

This definition for the $d$-SUM Problem is slightly unconventional in that here we allow repetition (i.e. the choice of $d$ numbers need not be distinct). Patrascu and Williams recently proved that if $d$-SUM can be solved in $N^{o{(d)}}$ time then $3$-SAT has a sub-exponential time algorithm. In fact, in the instances constructed in we can allow repetition of numbers without affecting the reduction since in these instances choosing any number more than once will never result in a sum that is exactly $d/2$. Hence we can re-state the results in for our (slightly unconventional definition for) $d$-SUM.

### Theorem 4.2

If $d < N^{0.99}$ and if $d$-SUM instances of $N$ distinct numbers each of $O{({d{\log N}})}$ bits can be solved in $N^{o{(d)}}$ time then $3$-SAT on $n$ variables can be solved in time $2^{o{(n)}}$.

Given an instance of the $d$-SUM, we will reduce to an instance of the Intermediate Simplex problem defined .

### Definition 4.3 (Intermediate Simplex)

Given a polyhedron $P = {\{{x \in \Re^{r - 1}}:{{Hx} \geq b}\}}$ where $H$ is an $n \times {({r - 1})}$ size matrix and $b \in \Re^{n}$ such that the matrix $\lbrack H,b\rbrack$ has rank $r$ and a set $S$ of $m$ points in $\Re^{r - 1}$, the goal of the Intermediate Simplex Problem is to find a set of points $T$ that form a simplex (i.e. $T$ is a set of $r$ affinely independent points) each in $P$ such that the convex hull of $T$ contains the points in $S$.

Vavasis proved that Intermediate Simplex is equivalent to the Simplicial Factorization problem.

### Theorem 4.4

There is a polynomial time reduction from Intermediate Simplex problem to Simplicial Factorization problem and vice versa and furthermore both reductions preserve the value of $r$.

Interestingly, an immediate consequence of this theorem is that Simplicial Factorization is easy in the case in which ${rank{(M)}} = 2$ because mapping these instances to instances of intermediate simplex results in a one dimensional problem - i.e. the polyhedron $P$ is an interval.

### The Gadget

Given the universe $U = {\{ s_{1},s_{2},\ldots,s_{N}\}}$ for the $d$-SUM problem, we construct a two dimensional Intermediate Simplex instance as shown in Figure 1. We will show that the Intermediate Simplex instance has exactly $N$ solutions, each representing a choice of $s_{i}$. Later in the reduction we use $d$ such gadgets to represent the choice of $d$ numbers in the set $U$.

Figure 1: The Gadget Recall for a two dimensional Intermediate Simplex problem, the input consists of a polygon $\mathcal{P}$ (which is the hexagon $ABCDEF$ in Figure 1) and a set of points $S = {\{ I_{1},I_{2},\ldots,I_{3N}\}}$ inside $\mathcal{P}$ (which are the dots, except for $M$). A solution to this two dimensional Intermediate Simplex instance will be a triangle inside $\mathcal{P}$ such that all the points in $S$ are contained in the triangle (in Figure 1 $ACE$ is a valid solution).

We first specify the polygon $\mathcal{P}$ for the Intermediate Simplex instance. The polygon $\mathcal{P}$ is just the hexagon $ABCDEF$ inscribed in a circle with center $M$. All angles in the hexagon are ${2\pi}/3$, the edges ${AB} = {CD} = {EF} = \epsilon$ where $\epsilon$ is a small constant depending on $N$, $d$ that we determine later. The other 3 edges also have equal lengths ${BC} = {DE} = {FA}$.

We use $y{(A)}$ and $z{(A)}$ to denote the $y$ and $z$ coordinates for the point $A$ (and similarly for all other points in the gadget). The hexagon is placed so that ${y{(A)}} = {y{(B)}} = 0$, ${y{(D)}} = {y{(E)}} = 1$.

Now we specify the set $S$ of $3N$ points for the Intermediate Simplex instance. To get these points first take $N$ points in each of the 3 segements $AB$, $CD$, $EF$. On $AB$ these $N$ points are called $A_{1}$, $A_{2}$,..., $A_{N}$, and ${|{AA_{i}}|} = {\epsilons_{i}}$. Similarly we have points $C_{i}$'s on $CD$ and $E_{i}$'s on $EF$, ${|{CC_{i}}|} = {|{EE_{i}}|} = {\epsilons_{i}}$. Now we have $N$ triangles $A_{i}C_{i}E_{i}$ (the thin lines in Figure 1). We claim (see Lemma 4.5 below) that the intersection of these triangles is a polygon with $3N$ vertices. The points in $S$ are just the vertices of this intersection.

### Lemma 4.5

When $\epsilon < {1/50}$, the points $\{ A_{i}\}$, $\{ C_{i}\}$, $\{ E_{i}\}$ are on $AB$, $CD$, $EF$ respectively and ${AA_{i}} = {CC_{i}} = {EE_{i}} = {\epsilons_{i}}$, the intersection of the $N$ triangles $\{{A_{i}C_{i}E_{i}}\}$ is a polygon with $3N$ vertices.

Proof: Since the intersection of $N$ triangles $A_{i}C_{i}E_{i}$ is the intersection of $3N$ halfplanes, it has at most $3N$ vertices. Therefore we only need to prove every edge in the triangles has a segment remaining in the intersection. Notice that the gadget is symmetric with respect to rotations of ${2\pi}/3$ around the center $M$. By symmetry we only need to look at edges $A_{i}C_{i}$. The situation here is illustrated in Figure 2.

Since all the halfplanes that come from triangles $A_{i}C_{i}E_{i}$ contain the center $M$, later when talking about halfplanes we will only specify the boundary line. For example, the halfplane with boundary $A_{i}C_{i}$ and contains $E_{i}$ (as well as $M$) is called halfplane $A_{i}C_{i}$.

Figure 2: Proof of Lemma 4.5 The two thick lines in Figure 2 are extensions of $AB$ and $CD$, now they are rotated so that they are $z = {\pm {\sqrt{3}y}}$. The two thin lines are two possible lines $A_{i}C_{i}$ and $A_{j}C_{j}$. The differences between $y$ coordinates of $A_{i}$ and $C_{i}$ are the same for all $i$ (here normalized to 1) by the construction of the points $A_{i}$'s and $C_{i}$'s. Assume the coordinates for $A_{i}$, $A_{j}$ are $(y_{i},{- {\sqrt{3}y_{i}}})$ and $(y_{j},{- {\sqrt{3}y_{j}}})$ respectively. Then the coordinates for the intersection is $({y_{i} + y_{j} + 1},{\sqrt{3}{({1 + y_{i} + y_{j} + {2y_{i}y_{j}}})}})$. This means if we have $N$ segments with $y_{1} < y_{2} < \ldots < y_{N}$, segment $i$ will be the highest one when $y$ is in range $({y_{i - 1} + y_{i} + 1},{y_{i} + y_{i + 1} + 1})$ (indeed, the lines with $j > i$ have higher slope and will win when $y > {y_{i} + y_{j} + 1} \geq {y_{i} + y_{i + 1} + 1}$; the lines with $j < i$ have lower slope and will win when $y < {y_{i} + y_{j} + 1} \leq {y_{i} + y_{i - 1} + 1}$).

We also want to make sure that all these intersection points are inside the halfplanes $C_{i}E_{i}$'s and $E_{i}A_{i}$'s. Since $\epsilon < {1/50}$, all the $y_{i}$'s are within $\lbrack{{- {1/2}} - {1/20}},{{- {1/2}} + {1/20}}\rbrack$. Hence the intersection point is always close to the point $(0,{\sqrt{3}/2})$, the distance is at most $1/5$. At the same time, since $\epsilon$ is small, the distances of this point $(0,{\sqrt{3}/2})$ to all the $C_{i}E_{i}$'s and $E_{i}A_{i}$'s are all larger than $1/4$. Therefore all the intersection points are inside the other $2N$ halfplanes and the segments will indeed remain in the intersection. The intersection has $3N$ edges and $3N$ vertices. $\blacksquare$ The Intermediate Simplex instance has $N$ obvious solutions: the triangles $A_{i}C_{i}E_{i}$, each one corresponds to a value $s_{i}$ for the $d$-SUM problem. In the following Lemma we show that these are the only possible solutions.

### Lemma 4.6

When $\epsilon < {1/1000}$, if the solution of the Intermediate Simplex problem is $PQR$, then $PQR$ must be one of the $A_{i}C_{i}E_{i}$'s.

Proof: Suppose $PQR$ is a solution of the Intermediate Simplex problem, since $M$ is in the convex hull of $\{ I_{1},I_{2},\ldots,I_{3N}\}$, it must be in $PQR$. Thus one of the angles $\anglePMQ$, $\angleQMR$, $\angleRMP$ must be at least ${2\pi}/3$ (their sum is $2\pi$). Without loss of generality we assume this angle is $\anglePMQ$ and by symmetry assume $P$ is either on $AB$ or $BC$. We shall show in either of the two cases, when $P$ is not one of the $A_{i}$'s, there will be some $I_{k}$ that is not in the halfplane $PQ$ (recall the halfplanes we are interested in always contain $M$ so we don't specify the direction).

When $P$ is on $AB$, since ${\anglePMQ} \geq {{2\pi}/3}$, we have ${CQ} \geq {AP}$ (by symmetry when ${CQ} = {AP}$ the angle is exactly ${2\pi}/3$). This means we can move $Q$ to $Q'$ such that ${CQ'} = {AP}$. The intersection of halfplane $PQ'$ and the hexagon $ABCDEF$ is at least as large as the intersection of halfplane $PQ$ and the hexagon. However, if $P$ is not any of the points $\{ A_{i}\}$ (that is, ${{|{PQ'}|}/\epsilon} \notin {\{ s_{1},s_{2},\ldots,s_{N}\}}$), then $PQ'$ can be viewed as $A_{N + 1}C_{N + 1}$ if we add $s_{N + 1} = {{|{AP}|}/\epsilon}$ to the set $U$. By Lemma 4.5 introducing $PQ'$ must increase the number of vertices. One of the original vertices $I_{k}$ is not in the hyperplane $PQ'$, and hence not in $PQR$. Therefore when $P$ is on $AB$ it must coincide with one of the $A_{i}$'s, by symmetry $PQR$ must be one of $A_{i}C_{i}E_{i}$'s.

When $P$ is on $BC$, there are two cases as shown in Figure 3.

Figure 3: Proof of Lemma 4.6 First observe that if we take $U' = {U \cup {\{{1 - s_{1}},{1 - s_{2}},\ldots,{1 - s_{N}}\}}}$, and generate the set $S = {\{ I_{1},I_{2},\ldots,I_{6N}\}}$ according to $U'$, then the gadget is further symmetric with respect to flipping along the perpendicular bisector of $BC$. Now without loss of generality ${BP} \leq {{BC}/2}$. Since every $I_{k}$ is now in the intersection of $2N$ triangles, in particular they are also in the intersection of the original $N$ triangles, it suffices to show one of $I_{k}$ ($k \in {\lbrack{6N}\rbrack}$) is outside halfplane $PQ$.

The first case (left part of Figure 3) is when ${BP} < \epsilon$. In this case we extend $PQ$ to get intersection on $AB$ ($P'$) and intersection on $CD$ ($Q'$). Again since ${\anglePMQ} \geq {{2\pi}/3}$, we have ${DQ} \geq {BP}$. At the same time we know ${\angleDQQ'} \geq {\angleP'PB}$, so ${DQ'} > {BP'}$. Similar to the previous case, we take $Q^{\operatorname{\prime\prime}}$ so that ${CQ^{\operatorname{\prime\prime}}} = {AP'}$. The intersection of hyperplane $P'Q^{\operatorname{\prime\prime}}$ and the hexagon $ABCDEF$ is at least as large as the intersection of halfplane $PQ$ and the hexagon. When $\epsilon < {1/1000}$, we can check ${AP'} < {2\epsilon} \ll {1/50}$, therefore we can still view $P'Q^{\operatorname{\prime\prime}}$ as some $A_{{2N} + 1}C_{{2N} + 1}$ for $s_{{2N} + 1} < 2$. Now Lemma 4.5 shows there is some vertex $I_{k}$ not in halfplane $P'Q^{\operatorname{\prime\prime}}$ (and hence not in halfplane $PQ$).

The final case (right part of Figure 3) is when ${BP} \geq \epsilon$. In this case we notice the triangle with 3 edges $AD$, $BE$, $CF$ (the shaded triangle in the figure) is contained in every $A_{i}C_{i}E_{i}$, thus it must also be in $PQR$. However, since ${{BC}/2} \geq {BP} \geq \epsilon$, we know ${AR} \leq \epsilon$ and ${DQ} \leq \epsilon$. In this case $PQR$ does not even contain the center $M$. $\blacksquare$

### The Reduction

Suppose we are given an instance of the $d$-SUM Problem with $N$ values $\{ s_{1},s_{2},{\ldotss_{N}}\}$. We will give a reduction to an instance of Intermediate Simplex in dimension ${r - 1} = {{3d} + 1}$.

To encode the choice of $d$ numbers in the set $\{ s_{1},s_{2},\ldots,s_{N}\}$, we use $d$ gadgets defined in Section 4.1. The final solution of the Intermediate Simplex instance we constructed will include solutions to each gadget. As the solution of a gadget always corresponds to a number in $\{ s_{1},s_{2},\ldots,s_{N}\}$ (Lemma 4.6) we can decode the solution and get $d$ numbers, and we use an extra dimension $w$ that "computes" the sum of these numbers and ensures the sum is equal to $d/2$.

We use three variables $\{ x_{i},y_{i},z_{i}\}$ for the $i^{th}$ gadget.

### Variables 1

We will use ${3d} + 1$ variables: sets $\{ x_{i},y_{i},z_{i}\}$ for $i \in {\lbrack d\rbrack}$ and $w$.

### Constraints 1 (Box)

For all $i \in {\lbrack d\rbrack}$, ${x_{i},y_{i}} \in {\lbrack 0,1\rbrack}$, $z_{i} \in {\lbrack 0,2\rbrack}$ and also $w \in {\lbrack 0,1\rbrack}$.

### Definition 4.7

Let $G \subset \Re^{2}$ be the hexagon ABCDEF in the two-dimensional gadget given in the Section 4.1.Let $H \subset \Re^{3}$ be the set $conv{(\left. \{{{(x_{i},y_{i},z_{i})} \in \Re^{3}} \middle| {{{(y_{i},z_{i})} \in G},{x_{i} = 1}}\} \right.,\overset{\rightarrow}{0})}$. $H$ is a tilted-cone that has a hexagonal base $G$ and has an apex at the origin.

### Definition 4.8

Let $R$ be a $7 \times 3$ matrix and $b \in \Re^{7}$ so that $\left. \{ x \middle| {{Rx} \geq b}\} \right. = H$.

We will use these gadgets to define (some of the) constraints on the polyhedron $P$ in an instance of intermediate simplex:

### Constraints 2 (Gadget)

For each $i \in {\lbrack d\rbrack}$, ${R{(x_{i},y_{i},z_{i})}} \geq b$.

Hence when restricted to dimensions $x_{i}$, $y_{i}$, $z_{i}$ the $i^{th}$ gadget $G$ is on the plane $x_{i} = 1$.

We hope that in a gadget, if we choose three points corresponding to the triangle for some value $s_{i}$, that of these three points only the point on the $AB$ line will have a non-zero value for $w$ and that this value will be $s_{i}$. The points on the lines $CD$ or $EF$ will hopefully have a value close to zero. We add constraints to enforce these conditions:

### Constraints 3 (CE)

For all $i \in {\lbrack d\rbrack}$, $w \leq {{1 - y_{i}} + {({1 - x_{i}})}}$ These constraints make sure that points on $CD$ or $EF$ cannot have large $w$ value.

Recall that we use $z{(A)}$ to denote the $z$ coordinate of $A$ in the gadget in Section 4.1.

### Constraints 4 (AB)

For all $i \in {\lbrack d\rbrack}$: $w \in \left\lbrack {\frac{({z_{i} - {z{(A)}x_{i}}})}{\epsilon} \pm {({{\frac{10}{\epsilon}y_{i}} + {({1 - x_{i}})}})}} \right\rbrack$ Theses constraints make sure that points on $AB$ have values in $\{ s_{1},s_{2},\ldots,s_{N}\}$.

The $AB$ and $CE$ constraints all have the property that when $x_{i} < 1$ (i.e. the corresponding point is off of the gadget on the plane $x_{i} = 1$) then these constraints gradually become relaxed.

To make sure the gadget still works, we don't want the extra constraints on $w$ to rule out some possible values for $x_{i}$, $y_{i}$, $z_{i}$'s. Indeed we show the following claim.

### Claim 4.9

For all points in ${(x_{i},y_{i},z_{i})} \in H$, there is some choice of $w \in {\lbrack 0,1\rbrack}$ so that $x_{i},y_{i},z_{i}$ and $w$ satisfy the $CE$ and $AB$ Constraints.

The proof is by observing that Constraints $AB$ have almost no effect when $y > 0$ and Constraints $CE$ have no effect when $y = 0$.

Constraints 1 to 4 define a polyhedron $P$ in ${3d} + 1$-dimensional space and furthermore the set of constraints that define $P$ have full rank (in fact even the inequalities in the Box Constraints have full rank). Thus this polyhedron is a valid polyhedron for the Intermediate Simplex problem.

Next we specify the points in $S$ for the Intermediate Simplex problem(each of which will be contained in the polyhedron $P$). Let $I_{k}$ (for $k \in {\lbrack{3N}\rbrack}$) be the set $S$ in the gadget in Section 4.1. As before, let $z{(I_{k})}$ and $y{(I_{k})}$ be the $z$ and $y$ coordinates of $I_{k}$ respectively.

### Definition 4.10 ($w$-$\max{(I_{k})}$)

Let $w$-$\max{(I_{k})}$ be the maximum possible $w$-value of any point $I$ with $x_{i} = 1$, $y_{i} = {y{(I_{k})}}$, $z_{i} = {z{(I_{k})}}$ and ${x_{j},y_{j},z_{j}} = 0$ for all $j \neq i$ so that $I$ is still contained in $P$.

### Definition 4.11 ($O,W,I_{k}^{i},Q$)

The set $S$ of points for the Intermediate Simplex problem is: $O$ point: For all $i \in {\lbrack d\rbrack}$, ${x_{i},y_{i},z_{i}} = 0$ and $w = 0$: $W$ point: For all $i \in {\lbrack d\rbrack}$, ${x_{i},y_{i},z_{i}} = 0$ and $w = 1$: $I_{k}^{i}$ points: For each $i \in {\lbrack d\rbrack}$, for each $k \in {\lbrack{3N}\rbrack}$ set $x_{i} = {1/4}$, $y_{i} = {{1/4}y{(I_{k})}}$, $z_{i} = {{1/4}z{(I_{k})}}$ and for $j \neq i$ set ${x_{j},y_{j},z_{j}} = 0$. Also set $w$ to be the ${1/4} \times w$-$\max{(I_{k})}$.: $Q$ point: For each $i \in {\lbrack d\rbrack}$, $x_{i} = {1/d}$, $y_{i} = {{y{(M)}}/d}$, $z_{i} = {{z{(M)}}/d}$ and $w = {1/6}$ This completes the reduction of $3$-SUM to intermediate simplex, and next we establish the COMPLETENESS and SOUNDNESS of this reduction.

### Completeness and Soundness

The completeness part is straight forward: for $i^{th}$ gadget we just select the triangle that corresponds to $s_{k_{i}}$.

### Lemma 4.12

If there is a set $\{ s_{k_{1}},s_{k_{2}},{\ldotss_{k_{d}}}\}$ of $d$ values (not necessarily distinct) such that ${\sum_{i \in {\lbrack d\rbrack}}s_{k_{i}}} = {d/2}$ then there is a solution to the corresponding Intermediate Simplex Problem.

Proof: We will choose a set of ${3d} + 2$ points $T$: We will include the $O$ and $W$ points, and for each $s_{k_{i}}$, we will choose the triangle corresponding to the value $s_{k_{i}}$ in the $i^{th}$ gadget. Recall the triangle is $A_{k_{i}}C_{k_{i}}E_{k_{i}}$ in the gadget defined in Section 4.1. The points we choose have $x_{i} = 1$ and $y_{i}$, $z_{i}$ equal to the corresponding point in the gadget. We will set $w$ to be $s_{k_{i}}$ for the point on the line $AB$ and we will set $w$ to be zero for the other two points not contained in the line $AB$. The rest of the dimensions are all set to 0.

Next we prove that the convex hull of this set of points $T$ contains all the points in $S$: The points $O$ and $W$ are clearly contained in the convex hull of $T$ (and are in fact in $T$!). Next consider some point $I_{k}^{i}$ in $S$ corresponding to some intersection point $I_{k}$ in the gadget $G$. Since $I_{k}$ is in the convex hull of the triangle corresponding to $s_{k_{i}}$ in the gadget $G$, there is a convex combination of the these three points $A_{k_{i}},C_{k_{i}},E_{k_{i}}$ in $T$ (which we call $J$) so that ${1/4}J$ matches $I_{k}^{i}$ on all coordinates except possibly the $w$-coordinate. Furthermore the point $J$ has some value in the coordinate corresponding to $w$ and this must be at most the corresponding value in $I_{k}^{i}$ (because we chose the $w$-value in $I_{k}^{i}$ to be ${1/4} \times w$-$\max{(I_{k})}$). Hence we can distribute the remaining $3/4$ weight among the $O$ and $W$ points to recover $I_{k}^{i}$ exactly on all coordinates.

Lastly, we observe that if we equally weight all points in $T$ (except $O$ and $W$) we recover the point $Q$. In particular, the $w$ coordinate of $Q$ should be ${\frac{1}{3d}{\sum_{i = 1}^{d}s_{k_{i}}}} = {1/6}$. $\blacksquare$ Next we prove SOUNDNESS for our reduction. Suppose the solution is $T$, which is a set of ${3d} + 2$ points in the polyhedron $P$ and the convex hull of points in $T$ contains all the $O$, $W$, $I_{k}^{i}$, $Q$ points (in Definition 4.11. ‣ 4.2 The Reduction ‣ 4 Strong Intractability of Simplicial Factorization ‣ Computing a Nonnegative Matrix Factorization – Provably")).

### Claim 4.13

The points $O$ and $W$ must be in the set $T$.

Proof: The points $O$ and $W$ are vertices of the polyhedron $P$ and hence cannot be expressed as a convex combination of any other set of points in $P$. $\blacksquare$ Now we want to prove the rest of the $3d$ points in set $T$ is partitioned into $d$ triples, each triple belongs to one gadget. Set $T' = {T - {\{ O\}} - {\{ W\}}}$.

### Definition 4.14

For $i \in {\lbrack d\rbrack}$, let

### Claim 4.15

The sets $T_{i}'$ partition $T'$ and each contain exactly $3$ nodes.

Proof: The sets $T_{i}'$ are disjoint, and additionally each set $T_{i}'$ must contain at least $3$ nodes (otherwise the convex hull of $T_{i}'$ even restricted to $x_{i},y_{i},z_{i}$ cannot contain the points $I_{k}^{i}$). This implies the Claim. $\blacksquare$ Recall the gadget in Section 4.1 is a two dimensional object, but it is represented as a three dimensional cone in our construction. We would like to apply Lemma 4.6 to points on the plane $x_{i} = 1$ (in this plane the coordinates $y_{i}$,$z_{i}$ act the same as $y$, $z$ in the gadget).

### Definition 4.16

For each point $Z \in T_{i}'$, let ${ext{(Z)}} \in \Re^{3}$ be the intersection of the line connecting the origin and $({x_{i}{(Z)}},{y_{i}{(Z)}},{z_{i}{(Z)}})$ with the $x_{i} = 1$ base of the set $\left. \{{(x_{i},y_{i},z_{i})} \middle| {{R{(x_{i},y_{i},z_{i})}} \geq b}\} \right.$. Let $ext{(T_{i}')}$ be the point-wise $ext$ operation applied to each point in $T_{i}'$.

Since the points $I_{k}^{i}$ are in the affine hull of $T_{i}'$ when restricted to $x_{i},y_{i},z_{i}$, we know $ext{(I_{k}^{i})}$ must be in the convex hull of $ext{(T_{i}')}$. Using Lemma 4.6 in Section 4.1, we get:

### Corollary 4.17

$ext{(T_{i}')}$ must correspond to some triangle $A_{k_{i}}C_{k_{i}}E_{k_{i}}$ for some value $s_{k_{i}}$.

Now we know how to decode the solution $T$ and get the numbers $s_{k_{i}}$. We will abuse notation and call the 3 points in $T_{i}'$ $A_{k_{i}}$, $C_{k_{i}}$, $E_{k_{i}}$ (they were used to denote the corresponding points in the 2-d gadget in Section 4.1).We still want to make sure the $w$ coordinate correctly "computes" the sum of these numbers. As a first step we want to show that the $x_{i}$ of all points in $T_{i}'$ must be 1 (we need this because the Constraints AB and CE are only strict when $x_{i} = 1$).

### Lemma 4.18

For each point $Z \in T_{i}'$, ${x_{i}{(Z)}} = 1$ Proof: Suppose, for the sake of contradiction, that ${x_{i}{(Z)}} < 1$ (for $Z \in T_{i}'$). Then consider the point $Q$. Since ${\sum_{i \in {\lbrack d\rbrack}}{x_{i}{(Q)}}} = 1$, and for any point in $T$ ${\sum_{i \in {\lbrack d\rbrack}}x_{i}} \leq 1$, there is no convex combination of points in $T$ that places non-zero weight on $Z$ and equals $Q$.

Let $T_{i}^{\operatorname{\prime\prime}}$ be $T_{i}'\backslash{\{ Z\}}$, we observe that the points in $T_{i}^{\operatorname{\prime\prime}}$ are the only points in $T$ that have any contribution to $(x_{i},y_{i},z_{i})$ when we want to represent $Q$ (using a convex combination). For now we restrict our attention to these three dimensions.When trying to represent $Q$ we must have $1/d$ weight in the set $T_{i}^{\operatorname{\prime\prime}}$ (because of the contribution in $x_{i}$ coordinate). The $y_{i}$, $z_{i}$ coordinates of $Q$ are ${y{(M)}}/d$, ${z{(M)}}/d$ respectively. This means if we take projection to $y_{i},z_{i}$ plane $M$ must be in the convex hull of $T_{i}^{\operatorname{\prime\prime}}$. However that is impossible because no two points in $A_{k}C_{k}E_{k}$ contain $M$ in their convex hull. This contradiction implies the Lemma. $\blacksquare$

### Lemma 4.19

Any convex combination of points in $T$ that equals the point $Q$ must place equal weight on all points in $T'$.

Proof: Using Lemma 4.18, we conclude that the total weight on points in $T_{i}'$ is exactly $1/d$, and there is a unique convex combination of the points $T_{i}'$ (restricted to $y_{i},z_{i}$) that recover the point $M$ which is the ${1/3},{1/3},{1/3}$ combination. This implies the Lemma. $\blacksquare$ Now we are ready to compute the $w$ value of the point $Q$ and show the sum of $s_{k_{i}}$ is indeed $d/2$.

### Lemma 4.20 (Soundness)

When $\epsilon < N^{- {Cd}}$ for some large enough constant $C$, if there is a solution to the Intermediate Simplex instance, then there is a choice of $d$ values that sum up to exactly $d/2$.

Proof: As we showed in previous Lemmas, the solution to the Intermediate Simplex problem must contain $O$, $W$, and for each gadget $i$ the solution has 3 points $T_{i}'$ that correspond to one of the solutions of the gadget. Suppose for gadget $i$ the triangle we choose is $A_{k_{i}}C_{k_{i}}E_{k_{i}}$. By Constraints $AB$ we know ${w{(A_{k_{i}})}} = s_{k_{i}}$, by Constraints $CE$ we know ${w{(C_{k_{i}})}} \leq \epsilon$ and ${w{(E_{k_{i}})}} \leq \epsilon$.

By Lemma 4.19 there is only one way to represent $Q$, and ${w{(Q)}} = {\frac{1}{3d}{\sum_{i = 1}^{d}{\lbrack{{w{(A_{k_{i}})}} + {w{(C_{k_{i}})}} + {w{(E_{k_{i}})}}}\rbrack}}} = {1/6}$.

Since $w{(C_{k_{i}})}$ and $w{(E_{k_{i}})}$'s are small, we have ${\sum_{i = 1}^{d}s_{k_{i}}} \in {\lbrack{{d/2} - {2d\epsilon}},{d/2}\rbrack}$. However the numbers only have $O{({d{\log N}})}$ bits and $\epsilon$ is so small, the only valid value in the range is $d/2$. Hence the sum $\sum_{i = 1}^{d}s_{k_{i}}$ must be equal to $d/2$. $\blacksquare$

## Fully-Efficient Factorization under Separability

Earlier, we gave algorithms for NMF, and presented evidence that no ${({nm})}^{o{(r)}}$ time algorithm exists for determining if a matrix $M$ has nonnegative rank at most $r$. Here we consider conditions on the input that allow the factorization to be found in time polynomial in $n$, $m$ and $r$. (In Section 5.1, we give a noise-tolerant version of this algorithm). To the best of our knowledge this is the first example of an algorithm (that runs in time poly$(n,m,r)$) and provably works under a non-trivial condition on the input. Donoho and Stodden in a widely-cited paper identified sufficient conditions for the factorization to be unique (motivated by applications of NMF to a database of images) but gave no algorithm for this task. We give an algorithm that runs in time poly$(n,m,r)$ and assumes only one of their conditions is met (separability). We note that this separability condition is quite natural in its own right, since it is usually satisfied by model parameters fitted to various generative models (e.g. LDA in information retrieval).

### Definition 5.1 (Separability)

A nonnegative factorization $M = {AW}$ is called separable if for each $i$ there is some row $f{(i)}$ of $A$ that has a single nonzero entry and this entry is in the $i^{th}$ column.

Let us understand this condition at an intuitive level in context of clustering documents by topic, which was discussed in the introduction. Recall that there a column of $M$ corresponds to a document. Each column of $A$ represents a topic and its entries specify the probability that a word occurs in that topic. The NMF thus "explains" the $i^{th}$ document as $AW_{i}$ where the column vector $W_{i}$ has (nonnegative) coordinates summing to one---in other words, $W_{i}$ represents a convex combination of topics. In practice, the total number of words $n$ may number in the thousands or tens of thousands, and the number of topics in the dozens. Thus it is not unusual to find factorizations in which each topic is flagged by a word that appears only in that topic and not in the other topics. The separability condition asserts that this happens for every topic^11^1More realistically, the word may appear in other topics only with negligible property instead of zero probability. This is allowed in our noise-tolerant algorithm later..

For simplicity we assume without loss of generality that the rows of $M$ are normalized to have unit $\ell_{1}$-norm. After normalizing $M$, we can still normalize $W$ (while preserving the factorization) by re-writing the factorization as $M = {AW} = {{({AD})}{({D^{- 1}W})}}$ for some $r \times r$ nonnegative matrix $D$. By setting $D_{i,i} = \left. \parallel W^{i}\parallel \right._{1}$ the rows of $D^{- 1}W$ will all have $l_{1}$ norm 1. When rows of $M$ and $W$ are all normalized the rows of $A$ must also have unit $\ell_{1}$-norm because The third equality uses the nonnegativity of $W$. Notice that after this normalization, if a row of $A$ has a unique nonzero entry (the rows in Separability), that particular entry must be one.

We also assume $W$ is a simplicial matrix defined as below.

### Definition 5.2 (simplicial matrix)

A nonnegative matrix $W$ is simplicial if no row in $W$ can be represented in the convex hull of the remaining rows in $W$.

The next lemma shows that without loss of generality we may assume $W$ is simplicial.

### Lemma 5.3

If a nonnegative matrix $M$ has a separable factorization $AW$ of inner-dimension at most $r$ then there is one in which $W$ is simplicial.

Proof: Suppose $W$ is not simplicial, and let the $j^{th}$ row $W^{j}$ be in the convex hull of the remaining rows. Then we can represent $W^{j} = {{\overset{\rightarrow}{u}}^{T}W}$ where $\overset{\rightarrow}{u}$ is a nonnegative vector with ${|\overset{\rightarrow}{u}|}_{1} = 1$ and the $j^{th}$ coordinate is 0.

Now modify $A$ as follows. For each row $A^{j'}$ in $A$ that has a non-zero $j^{th}$ coordinate, we zero out the $j^{th}$ coordinate and add $A_{j}^{j'}\overset{\rightarrow}{u}$ to the row $A^{j'}$. At the end the matrix is still nonnegative but whose $j^{th}$ column is all zeros. So delete the $j^{th}$ column and let the resulting $n \times {({r - 1})}$ matrix be $A'$. Let $W'$ be the matrix obtained by deleting the $j^{th}$ row of $W$. Then by construction we have $M = {A'W'}$. Now we claim $A'$ is separable.

Since $A$ was originally separable, for each column index $i$ there is some row, say the $f{(i)}^{th}$ row, that has a non-zero entry in the $i^{th}$ column and zeros everywhere else. If $i \neq j$ then by definition the above operation does not change the $f{(i)}^{th}$ row of $A$. If $i = j$ the $j^{th}$ index is deleted at the end. In either case the final matrix $A'$ satisfies the separability condition.

Repeating the above operation for all violations of the simplicial condition we end with a separable factorization of $M$ (again with inner-dimension at most $r$) where $W$ is simplicial. $\blacksquare$

### Theorem 5.4

There is an algorithm that runs in time polynomial in $n$, $m$ and $r$ and given a matrix $M$ outputs a separable factorization with inner-dimension at most $r$ (if one exists).

Proof: We can apply Lemma 5.3 and assume without loss of generality that there is a factorization $M = {AW}$ where $A$ is separable and $W$ is simplicial. The separability condition implies that every row of $W$ appears among the rows of $M$. Thus $W$ is hiding in plain sight in $M$; we now show how to find it.

Say a row $M^{j}$ is a loner if (ignoring other rows that are copies of $M^{j}$) it is not in the convex hull of the remaining rows. The simplicial condition implies that the rows of $M$ that correspond to rows of $W$ are loners.

### Claim 5.5

A row $M^{j}$ is a loner iff $M^{j}$ is equal to some row $W^{i}$ Proof: Suppose (for contradiction) that a row in $M^{j}$ is not a loner and but it is equal to some row $W^{i}$. Then there is a set $S$ of rows of $M$ so that $M^{j}$ is in their convex hull and furthermore for all $j' \in S$, $M^{j'}$ is not equal to $M^{j}$. Thus there is a nonnegative vector $u \in \Re^{n}$ that is 0 at the $j^{th}$ coordinate and positive on indices in $S$ such that ${u^{T}M} = M^{j}$.

Hence ${u^{T}AW} = M^{j} = W^{i}$, but $u^{T}A$ must have unit $\ell_{1}$-norm (because $\left. \parallel u\parallel \right._{1} = 1$, all rows of $A$ have unit $\ell_{1}$-norm and are all nonnegative), also $u^{T}A$ is non-zero at position $j'$. Consequently $W^{i}$ is in the convex hull of the other rows of $W$, which yields a contradiction.

Conversely if a row $M^{j}$ is not equal to any row in $W$, we conclude that $M^{j}$ is in the convex hull of the rows of $W$. Each row of $W$ appears as a row of $A$ (due to the separability condition). Hence $M^{j}$ is not a loner because $M^{j}$ is in the convex hull of rows of $M$ that are equivalent to $M^{j}$ itself. $\blacksquare$ Using linear programming, we can determine which rows $M^{j}$ are loners. Due to separability there will be exactly $r$ different loner rows, each corresponds to one of the $W^{i}$. Thus we are able to recover $W'$ that is equal to $W$ after permutation over rows.We can compute a nonnegative $A'$ such that ${A'W'} = M$, and such solution $A'$ is necessarily separable (since it is just equal to $A$ after permutation over columns). $\blacksquare$

### Adding Noise

In any practical setting the data matrix $M$ will not have an exact NMF of low inner dimension since its entries are invariably subject to noise. Here we consider how to extend our separability-based algorithm to work in presence of noise. We assume that the input matrix $M'$ is obtained by perturbing each row of $M$ by adding a vector of $\ell_{1}$-norm at most $\epsilon$, where $M$ has a separable factorization of inner-dimension $r$. Alternatively, $\left. \parallel{M^{'i} - M^{i}}\parallel \right._{1} \leq \epsilon$ for all $i$. Notice that the case in which the separability condition is only approximately satisfied is a subcase of this: If for each column there is some row in which that column's entry is at least $1 - \epsilon$ and the sum of the other row entries is less than $\epsilon$ then the matrix $M'$ will satisfy the condition stated above. (Note that $M,A,W$ have been scaled as discussed above.)

Our algorithm will require one more condition -- namely, we require the unknown matrix $W$ to be "robustly" simplicial instead of just simplicial.

### Definition 5.6 ($\alpha$-robust simplicial)

We call $W$ $\alpha$-robust simplicial if no row in $W$ has $\ell_{1}$ distance smaller than $\alpha$ to the convex hull of the remaining rows in $W$. (Here all rows have unit $\ell_{1}$-norm.)

Recall from Lemma 5.3 that the simplicial condition can be assumed without loss of generality under separability. In general $\alpha$-robust simplicial condition does not follow from separability. However, any reasonable generative model would surely posit that the matrix $W$ ---whose columns after all represents distributions---satisfies the condition above. For instance, if columns of $W$ are picked randomly from the unit $\ell_{1}$ ball then after normalization $\alpha$ is more than $1/10$. Regardless of whether or not one self-identifies as a bayesian, it seems reasonable that any suitably generic way of picking column vectors would tend to satisfy the $\alpha$-robust-simplicial property.

### Theorem 5.7

Suppose $M = {AW}$ where $A$ is separable and $W$ is $\alpha$-robust simplicial. Let $\epsilon$ satisfy ${{{20\epsilon}/\alpha} + {13\epsilon}} < \alpha$. Then there is a polynomial time algorithm that given $M'$ such that for all rows $\left. \parallel{M^{'i} - M^{i}}\parallel \right._{1} < \epsilon$, finds a nonnegative matrix factorization $A'W'$ of the same inner dimension such that the $\ell_{1}$ norm of each row of $M' - {A'W'}$ is at most ${{10\epsilon}/\alpha} + {7\epsilon}$.

Proof: Separability implies that for any column index $i$ there is a row $f{(i)}$ in $A$ whose only nonzero entry is in the $i^{th}$ column. Then $M^{f{(i)}} = W^{i}$ and consequently $\left. \parallel{M^{'{f{(i)}}} - W^{i}}\parallel \right._{1} < \epsilon$. Let us call these rows $M^{'{f{(i)}}}$ for all $i$ the canonical rows. From the above description the following claim is clear since the rows of $M$ can be expressed as a convex combination of $W^{i}$'s.

### Claim 5.8

Every row $M^{'j}$ has $\ell_{1}$-distance at most $2\epsilon$ to the convex hull of canonical rows. and we can bound the right hand side by $2\epsilon$. $\blacksquare$ Next, we show how to find the canonical rows. For a row $M^{'j}$, we call it a robust-loner if upon ignoring rows whose $\ell_{1}$ distance to $M^{'j}$ is less than $d = {{{5\epsilon}/\alpha} + {2\epsilon}}$, the $\ell_{1}$-distance of $M^{'j}$ to the convex hull of the remaining rows is more than $2\epsilon$. Note that we can identify robust-loner rows using linear programming.

The following two claims establish that a row of $M^{'j}$ is a robust-loner if and only if it is close to some row $W^{i}$.

### Claim 5.9

If $M^{'j}$ has distance more than $d + \epsilon$ to all of the $W^{i}$'s, then it cannot be a robust loner.

Proof: Such an $M^{'j}$ has distance at least $d$ to each of the canonical rows. The previous claim shows $M^{'j}$ is close to the convex hull of the canonical rows and thus by definition it cannot be a robust-loner. $\blacksquare$

### Claim 5.10

All canonical rows are robust-loners.

Proof: Since $\left. \parallel{M^{'{f{(i)}}} - W^{i}}\parallel \right._{1} \leq \epsilon$, when we check if $M^{'{f{(i)}}}$ is a robust-loner (using linear programming), we leave out of consideration all rows that have $\ell_{1}$-distance at most ${{5\epsilon}/\alpha} + \epsilon$ to $W^{i}$. In particular, this omits any row $M^{'j}$ such that $M^{j} = {\sum_{k = 1}^{r}{A_{j,k}W^{k}}}$ and $A_{j,i} \geq {1 - {{5\epsilon}/\alpha}}$. All remaining rows have $A_{j,i} \leq {1 - {{5\epsilon}/\alpha}}$, and hence the $\ell_{1}$ distance of $W^{i}$ to $conv{({W\backslash W^{i}})}$ is at least $\alpha$ (by the $\alpha$-robust simplicial property), we conclude that the distance between $W^{i}$ and the convex hull of remaining $M^{j}$'s must be at least ${{{5\epsilon}/\alpha} \ast \alpha} = {5\epsilon}$. Since $M'$ is close to $M$ the $\ell_{1}$-distance between $M^{'{f{(i)}}}$ and the convex hull of remaining rows $M^{'j}$'s must be at least ${{5\epsilon} - {2\epsilon}} = {3\epsilon}$. Therefore $M^{'{f{(i)}}}$ is a robust-loner. $\blacksquare$ The previous claim implies that each robust-loner row is within $\ell_{1}$-distance $d + \epsilon$ to some $W^{i}$ and conversely, for every $W^{i}$ there is at least one robust-loner row that is close to it. Since the $\ell_{1}$-distances between $W^{i}$'s are at least $4{({d + \epsilon})}$, we can apply distance based clustering on the robust-loner rows: place two robust-loner rows into the same cluster if and only if these rows are within $\ell_{1}$-distance at most $2{({d + \epsilon})}$. Clearly we will obtain $r$ clusters, one corresponding to each of the $W^{i}$'s. Choose one row from each of the cluster, and using similar argument as Claim 5.8 we deduce that every row of $M'$ is within ${{2{({d + \epsilon})}} + \epsilon} = {{{10\epsilon}/\alpha} + {7\epsilon}}$ to the convex hull of the rows we selected. Therefore these rows form a nonnegative $W'$ and we can find $A'$ so that $\left. \parallel{M^{'j} - {({A'W'})}^{j}}\parallel \right._{1} \leq {{{10\epsilon}/\alpha} + {7\epsilon}}$ for all $j$. $\blacksquare$

## Approximate Nonnegative Matrix Factorization

Here we consider the case in which the given matrix does not have an exact low-rank NMF but rather can be approximated by a nonnegative factorization with small inner-dimension. We refer to this as Approximate NMF. Unlike the algorithm in Theorem 5.7, the algorithm here works with general nonnegative matrix factorization: we do not make any assumptions on matrices $A$ and $W$. Throughout this section we will use $\left. \parallel\parallel \right._{F}$ to denote the Froebenius norm, $\left. \parallel\parallel \right._{2}$ to denote the spectral norm and $\left. \parallel\parallel \right.$ applied to a vector will denote the standard Euclidean norm.

### Theorem 6.1

Let $M$ be an $n \times m$ nonnegative matrix such that there is a factorization $AW$ satisfying $\left. \parallel{M - {AW}}\parallel \right._{F} \leq {\epsilon\left. \parallel M\parallel \right._{F}}$, where $A$ and $W$ are nonnegative and have inner-dimension $r$. There is an algorithm that computes $A'$ and $W'$ satisfying in time $2^{{poly}{({r{\log{({1/\epsilon})}}})}}{poly}{(n,m)}$.

Note that the matrix $M$ need not have low rank, but we will be able to assume $M$ has rank at most $r$ without loss of generality: Let $M'$ be the best rank at most $r$ approximation (in terms of Frobenius norm) to $M$. This can be computed using a truncated singular value decomposition (see e.g. ). Since $A$ and $W$ have inner-dimension $r$, we get:

### Claim 6.2

$\left. \parallel{M' - M}\parallel \right._{F} \leq \left. \parallel{M - {AW}}\parallel \right._{F}$ Throughout this section, we will assume that the input matrix $M$ has rank at most $r$ - since otherwise we can compute $M'$ and solve the problem for $M'$. Then using the triangle inequality, any good approximation to $M'$ will also be a good approximation to $M$.

Throughout this section, we will use the notation $A_{t}$ to denote the $t^{th}$ column of $A$ and $W^{t}$ to denote the $t^{th}$ row of $W$. Note that $W^{t}$ is a row vector so we will frequently use $A_{t}W^{t}$ to denote an outer-product. Next, we apply a simple re-normalization that will allow us to state the main steps in our algorithm in a more friendly notation.

### Lemma 6.3

We can assume without loss of generality that for all $t$ and furthermore $\left. \parallel A\parallel \right._{F} \leq {{({1 + \epsilon})}\left. \parallel M\parallel \right._{F}}$.

Proof: We can write ${{AW} = {\sum_{t = 1}^{r}{A_{t}W^{t}}}}.$ So we may scale $A_{t},W^{t}$ to ensure that $\left. \parallel W^{t}\parallel \right. = 1$. Next, since $A$ and $W$ are nonnegative we have $\left. \parallel{AW}\parallel \right._{F} \geq \left. \parallel{A_{t}W^{t}}\parallel \right._{F} = {\left. \parallel A_{t}\parallel \right.\left. \parallel W^{t}\parallel \right.}$ and $\left. \parallel{AW}\parallel \right._{F} \leq {{({1 + \epsilon})}\left. \parallel M\parallel \right._{F}}$ and this implies the first condition in the lemma. where the inequality follows because all entries in $A$ and $W$ are nonnegative, and the last equality follows because $\left. \parallel W^{t}\parallel \right. = 1$. $\blacksquare$ Note that this lemma immediately implies that $\left. \parallel W\parallel \right._{F} \leq \sqrt{r}$.

The intuition behind our algorithm is to decompose the unknown matrix $W$ as the sum of two parts: $W = {W_{0} + W_{1}}$. The first part $W_{0}$ is responsible for how good $AW$ is as an approximation to $M$ (i.e., $\left. \parallel{M - {AW_{0}}}\parallel \right._{F}$ is small) but could be negative; the second part $W_{1}$ has little effect on the approximation but is important in ensuring the sum $W_{0} + W_{1}$ is nonnegative. The algorithm will find good approximations to $W_{0},W_{1}$.

What are $W_{0},W_{1}$? Since removing $W_{1}$ has little effect on how good $AW$ is as an approximation to $M$, this matrix should be roughly the projection of $W$ onto the "less significant" singular vectors of $A$. Namely, let the singular value decomposition of $A$ be and suppose that $\sigma_{1} \geq \sigma_{2}\ldots. \geq \sigma_{r}$. Let $t_{0}$ be the largest $t$ for which ${|\sigma_{t}|} \geq {\delta\left. \parallel M\parallel \right._{F}}$ (where $\delta$ is a constant that is polynomially related to $r$ and $\epsilon$ and will be specified later). Then set

### Lemma 6.4

$\left. \parallel{M - {AW_{0}}}\parallel \right._{F} \leq {{\epsilon\left. \parallel M\parallel \right._{F}} + {\delta\sqrt{r}\left. \parallel M\parallel \right._{F}}}$ Proof: By the triangle inequality $\left. \parallel{M - {AW_{0}}}\parallel \right._{F} \leq {\left. \parallel{M - {AW}}\parallel \right._{F} + \left. \parallel{AW_{1}}\parallel \right._{F}}$. Also ${AW_{1}} = {\sum_{t = {t_{0} + 1}}^{r}{\sigma_{t}{({u_{t}v_{t}^{T}})}W}}$, so we have where the last inequality follows because $\left. \parallel W\parallel \right._{F} \leq \sqrt{r}$ and the spectral norm of $\sum_{t = {t_{0} + 1}}^{r}{({u_{t}v_{t}^{T}})}$ is one. $\blacksquare$ Next, we establish a lemma that will be useful when searching for (an approximation to) $W_{0}$:

### Lemma 6.5

There is an $r \times m$ matrix $W_{0}'$ such that each row is in the span of the rows of $M$ and which satisfies ${\left. \parallel{W_{0}' - W_{0}}\parallel \right._{F} \leq {{2\epsilon}/\delta}}.$ Proof: Consider the matrix $A^{+} = {\sum_{t = 1}^{t_{0}}{\frac{1}{\sigma_{t}}v_{t}u_{t}^{T}}}$. Thus $A^{+}$ is a pseudo-inverse of the truncated SVD of $A$. Note that $W_{0} = {A^{+}AW}$ and the spectral norm $\left. \parallel A^{+}\parallel \right._{2}$ is at most $1/{({\delta\left. \parallel M\parallel \right._{F}})}$. Then we can choose $W_{0}' = {A^{+}M}$. Clearly, each row of $W_{0}'$ is in the span of the rows of $M$. Furthermore, we have

### Lemma 6.6

There is an algorithm that in time $2^{{poly}{({r{\log{({1/\epsilon})}}})}}{poly}{(n,m)}$ finds $W_{0}^{\operatorname{\prime\prime}},W_{1}'$ and $A'$ such that ${W_{0}^{\operatorname{\prime\prime}} + W_{1}'} \geq 0$, $A' \geq 0$ and Proof: We use exhaustive enumeration to find a close approximation to the matrix $W_{0}'$ of Lemma 6.5, and then we use convex programming to find $W_{1}',A'$: The exhaustive enumeration is simple: try all vectors that lie in some $\epsilon_{1}$-net in the span of the rows of $M$, where $\epsilon_{1} = {\epsilon/\delta}$. Such an $\epsilon_{1}$-net is easily enumerated in the provided time since the row vectors are smaller than $\left. \parallel W\parallel \right._{F} = \sqrt{r}$ and their span is $r$-dimensional. Contained in this net there must an $W_{0}^{\operatorname{\prime\prime}}$ such that $\left. \parallel{{A^{+}M} - W_{0}^{\operatorname{\prime\prime}}}\parallel \right._{F} \leq \epsilon_{1}$. Using Lemma 6.5, ${\left. \parallel{W_{0} - W_{0}'}\parallel \right._{2} \leq {{2\epsilon}/\delta}},$ so the triangle inequality implies $\left. \parallel{W_{0} - W_{0}^{\operatorname{\prime\prime}}}\parallel \right._{F} \leq {{{2\epsilon}/\delta} + \epsilon_{1}} \leq {{4\epsilon}/\delta}$.

Next, we give a method to find suitable substitutes $W_{1}',A'$ for $W_{1},A$ respectively so that ${W_{0}' + W_{1}'} \geq 0$ and $A'{({W_{0}' + W_{1}'})}$ is a good approximation to $M$.

Let us assume we know the vectors $v_{i}$ appearing in the SVD expression and $\left. \parallel A\parallel \right._{F}$. This is easy to guarantee since we can enumerate over all choices of the $v_{i}$'s (which are unit vectors in $\Re^{r}$) using a suitable $\epsilon_{2}$-net where $\epsilon_{2} = {\min{\{\frac{\epsilon}{\deltar},0.1\}}}$. Also, $\left. \parallel A\parallel \right._{F}$ is a scalar value that can be easily guessed within multiplicative factor $1.01$.

Let $W_{1}' = Z$ be the optimal solution to the following convex program: This is optimization problem is convex since the constraints are linear and the objective function is quadratic but convex. (In fact this optimization problem can be separated into $m$ smaller convex programs because the constraints between different columns of $W_{1}'$ are independent).

When the vectors we enumerated (denoted as $\{ v_{i}'\}$) are close enough to the true values $\{ v_{i}\}$, that is, when ${\sum_{i = 1}^{r}\left. \parallel{v_{i}' - v_{i}}\parallel \right.^{2}} \leq {\min{\{\frac{\epsilon^{2}}{\delta^{2}r},0.01\}}}$, the value of the objective function after substituting $v$ by $v'$ can only change by at most $O{({{\frac{\epsilon^{2}}{\delta^{2}}\left. \parallel A\parallel \right._{F}^{2}} + {r\delta^{2}\left. \parallel M\parallel \right._{F}^{2}}})}$. From now on we work with the true values of $\{ v_{i}\}$. The Claim below and arguments after will still be true although the vectors are not exact.

### Claim 6.7

The optimal value of this convex program is at most $O{({{\frac{\epsilon^{2}}{\delta^{2}}\left. \parallel A\parallel \right._{F}^{2}} + {r\delta^{2}\left. \parallel M\parallel \right._{F}^{2}}})}$.

Proof: We prove that $W_{1}' = {W - W_{0}^{\operatorname{\prime\prime}}} = {{({W_{0} - W_{0}^{\operatorname{\prime\prime}}})} + W_{1}}$ is a feasible solution and that the objective value of this solution is the value claimed in the lemma.

Since $W_{1} = {\sum_{t = {t_{0} + 1}}^{r}{{({v_{t}v_{t}^{T}})}W}}$ only contributes to the second term of the objective function, we can upper bound the objective as The proof is completed because $\left. \parallel{W_{0} - W_{0}^{\operatorname{\prime\prime}}}\parallel \right._{F} = {O{(\frac{\epsilon}{\delta})}}$ and $\left. \parallel W_{1}\parallel \right._{F} \leq \left. \parallel W\parallel \right._{F} = \sqrt{r}$. $\blacksquare$ After solving the convex program, we obtaine a candidate $W_{1}'$. Let $W' = {W_{0}^{\operatorname{\prime\prime}} + W_{1}'}$. To get the right $A'$ (since $W'$ is fixed) we can find the $A'$ that minimizes $\left. \parallel{M - {A'W'}}\parallel \right._{F}^{2}$ by solving a least-squares problem. Clearly such an $A'$ satisfies $\left. \parallel{M - {A'{({W_{0}^{\operatorname{\prime\prime}} + W_{1}'})}}}\parallel \right._{F} \leq \left. \parallel{M - {A{({W_{0}^{\operatorname{\prime\prime}} + W_{1}'})}}}\parallel \right._{F}$ and the latter quantity is bounded by ${\left. \parallel{M - {AW_{0}}}\parallel \right._{F} + \left. \parallel{A{({W_{0} - W_{0}^{\operatorname{\prime\prime}}})}}\parallel \right._{F} + \left. \parallel{AW_{1}'}\parallel \right._{F}}.$ Lemma 6.4 bounds the first term and Lemma 6.5 bounds the second term. The square of the last term is bounded by the objective function of the convex program. $\blacksquare$ Finally, by choosing $\delta = \frac{\sqrt{\epsilon}}{r^{1/4}}$ we get $A'$, $W' = {W_{0}^{\operatorname{\prime\prime}} + W_{1}'}$ such that $\left. \parallel{M - {A'W'}}\parallel \right._{F} \leq {O{({\epsilon^{1/2}r^{1/4}})}\left. \parallel M\parallel \right._{F}}$.

## Concluding Remarks

Here, we initiated a rigorous study of nonnegative matrix factorization. Our hardness result rules out significant improvements over our worst-case results for fixed inner-dimension $r$. We believe that our $\text{poly}{(m,n,r)}$-time algorithm for finding separable factorizations may point the way for future work. What other plausible conditions can one impose on the factors in real-life applications? We also hope our work promotes further theoretical study of nonnegative rank.

This work is part of a broader agenda of bringing greater rigor to the analysis of algorithms used in machine learning. Currently, heuristic approaches are popular because the solution concepts are believed to be intractable. Our results, for example our algorithm for NMF under the separability condition, raise hope that sometimes the solution concepts may not be intractable after all.
