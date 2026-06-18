## Introduction

Recovering sparse vectors and low-rank matrices from noisy linear measurements, with applications in compressed sensing and machine learning, has been the focus of much recent research. The Restricted Isometry Property (RIP) was introduced by Candès and Tao in and has played a major role in proving recoverability of sparse signals from compressed measurements. The first recovery algorithm that was analyzed using RIP was $\ell_{1}$ minimization in. Since then, many algorithms including GraDes, Reweighed $\ell_{1}$, and CoSaMP have been analyzed using RIP. Analogous to the vector case, RIP has also been used in the analysis of algorithms for *low rank matrix recovery*, for example Nuclear Norm Minimization, SVP, Reweighted Trace Minimization and AdMiRA. Other recovery conditions have also been proposed for recovery of both sparse vectors and low-rank matrices including the Null Space Property and the Spherical Section Property (also known as the 'almost Euclidean' property) for the nullspace. The first matrix RIP result was given in where it was shown that the RIP is sufficient for low rank recovery using nuclear norm minimization, and that it holds with high probability as long as number of measurements are sufficiently large. This analysis was improved in to require a minimal order of measurements. Recently, improved the RIP constants with a stronger analysis similar to.

In this paper, we show that if a set of conditions are sufficient for the robust recovery of sparse vectors with sparsity at most $k$, then the "extension" (defined later) of the same set of conditions are sufficient for the robust recovery of low rank matrices up to rank $k$.

While the recovery analysis in and (Theorem 2.4) is complicated and lengthy, our results (see "Main Theorem") are easily derived due to the use of a key singular value inequality (Lemma 1). Our results also apply to generic recovery conditions, one of which is RIP. As an example, $\delta_{k} < 0.307$, $\delta_{2k} < 0.472$ are two of the many RIP-based conditions (see also, ) that are known to be sufficient for sparse vector recovery using $\ell_{1}$ minimization. A simple consequence of this paper is the following: The RIP conditions ${\delta_{k} < 0.307},{\delta_{2k} < 0.472}$ (and all other RIP conditions that are sufficient for sparse vector recovery) are *also* sufficient for robust recovery of matrices with rank at most $k$ improving the previous best condition of $\delta_{2k} < 0.307$ in. Improving the RIP conditions is a direct consequence of our observation but is not the focus of this paper, although such improvements have been of independent interest (e.g., ).

Our results also apply to another recovery condition known as the Nullspace Spherical Section Property (SSP) and it easily follows from our main theorem that the spherical section constant $\Delta > {4k}$ is sufficient for the recovery of matrices up to rank $k$ as in the vector case. This approach not only simplifies the analysis in, but also gives a better condition (as compared to $\Delta > {6k}$ in ). Our final contribution is to give nullspace based conditions for recovery of low-rank matrices using Schatten-$p$ quasi-norm minimization, which is analogous to $\ell_{p}$ minimization with $0 < p < 1$ for vectors. These nonconvex surrogate functions have motivated algorithms such as IRLS that are empirically observed to improve on the recovery performance of $\ell_{1}$ and nuclear norm minimization.

## Basic Definitions and Notation

For a vector $\mathbf{x} \in {\mathbb{R}}^{n}$, $\parallel \cdot \parallel_{0}$ denotes its cardinality or the number of nonzero elements. $\overline{\mathbf{x}}$ denotes the vector obtained by decreasingly sorting the absolute values of the entries of $\mathbf{x}$, and $\mathbf{x}^{k}$ denotes the vector obtained by restricting $\mathbf{x}$ to its $k$ largest elements (in absolute value). Let ${\text{diag}{( \cdot )}}:{{\mathbb{R}}^{n \times n}\rightarrow{\mathbb{R}}^{n}}$ return the vector of diagonal entries of a matrix, and ${\text{diag}{( \cdot )}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$ return a diagonal matrix with the entries of the input vector on the diagonal. Let $n_{1} \leq n_{2}$. We denote rank of a matrix $X \in {\mathbb{R}}^{n_{1} \times n_{2}}$ by ${rank}{(X)}$, and its $i$th largest singular value by $\sigma_{i}{(X)}$. Let ${\Sigma{(X)}} = {\lbrack{\sigma_{1}{(X)}},\ldots,{\sigma_{n_{1}}{(X)}}\rbrack}^{T}$ be vector of decreasingly sorted singular values of $X$. $X^{k}$ denotes the matrix obtained by taking the first $k$ terms in the singular value decomposition of $X$. The nuclear norm of $X$ is denoted by ${\| X\|}_{\star} = {\sum_{i = 1}^{n_{1}}{\sigma_{i}{(X)}}}$, and its Frobenius norm by ${\| X\|}_{F} = \sqrt{\sum_{i = 1}^{n_{1}}{\sigma_{i}^{2}{(X)}}}$. Let $\Sigma_{X} = {\text{diag}{({\Sigma{(X)}})}} \in {\mathbb{R}}^{n_{1} \times n_{1}}$. We call $(U,V)$ a unitary pair if ${U^{T}U} = {UU^{T}} = {V^{T}V} = I$. In this paper, we'll use the following singular value decomposition of $X$: $X = {U\Sigma_{X}V^{T}}$ where $(U,V)$ is a unitary pair. Clearly ${U \in {\mathbb{R}}^{n_{1} \times n_{1}}},{V \in {\mathbb{R}}^{n_{2} \times n_{1}}}$. Notice that the set of matrices $UDV^{T}$, where $D$ is diagonal, form an $n_{1}$ dimensional subspace. Denote this space by $S{(U,V)}$. Let ${\mathcal{A}{( \cdot )}}:{R^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ be a linear operator. ${\mathcal{A}_{U,V}{( \cdot )}}:{{\mathbb{R}}^{n_{1}}\rightarrow{\mathbb{R}}^{m}}$ is called the restriction of $\mathcal{A}$ to unitary pair $(U,V)$ if we have ${\mathcal{A}_{U,V}{(\mathbf{x})}} = {\mathcal{A}{({U\text{diag}{(\mathbf{x})}V^{T}})}}$ for all $\mathbf{x} \in {\mathbb{R}}^{n_{1}}$. In particular, $\mathcal{A}_{U,V}{( \cdot )}$ can be represented by a matrix $A_{U,V}$.

Consider the problem of recovering the desired vector $\mathbf{x}_{0} \in {\mathbb{R}}^{n}$ with ${\|\mathbf{x}_{0}\|}_{1} = k$ from corrupted measurements $\mathbf{y} = {{A\mathbf{x}_{0}} + \mathbf{z}}$, with ${\|\mathbf{z}\|}_{2} \leq \epsilon$ where $\epsilon$ denotes the noise level, and $A \in {\mathbb{R}}^{m \times n}$ denotes the measurement matrix. Under certain conditions, $\mathbf{x}_{0}$ can be found under certain conditions by solving the following convex problem,

where recovery is known to be robust to noise as well as imperfect sparsity. We say $\mathbf{x}^{\ast}$ is *as good as* $\mathbf{x}_{0}$ w.r.t $\mathbf{y}$ if ${\|{{A\mathbf{x}^{\ast}} - \mathbf{y}}\|}_{2} \leq \epsilon$ and ${\|\mathbf{x}^{\ast}\|}_{1} \leq {\|\mathbf{x}_{0}\|}_{1}$. In particular, the optimal solution of the problem 3 is as good as $\mathbf{x}_{0}$.

Similarly, consider the case where the desired signal to be recovered is a low-rank matrix denoted by $X_{0} \in {\mathbb{R}}^{n_{1} \times n_{2}}$, with $n = n_{1} \leq n_{2}$. Let $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ be the measurement operator. We observe corrupted measurements $\mathbf{y} = {{\mathcal{A}{(X_{0})}} + \mathbf{z}}$ with ${\|\mathbf{z}\|}_{2} \leq \epsilon$.

Similar to the vector case, we say that $X^{\ast}$ is *as good as* $X_{0}$ w.r.t $\mathbf{y}$ if ${\|{{\mathcal{A}{(X^{\ast})}} - \mathbf{y}}\|}_{2} \leq \epsilon$ and ${\| X^{\ast}\|}_{\star} \leq {\| X_{0}\|}_{\star}$. In particular the optimal solution to *problem* 4 is as good as $X_{0}$. We now give the definitions for certain recovery conditions on the measurement map, the Restricted Isometry Property and the Spherical Section Property.

### Definition: Restricted Isometry Constant (RIC)

The RIC of a matrix $A$ is the smallest constant $\delta_{k}$ for which

holds for all vectors $\mathbf{x}$ with ${\|\mathbf{x}\|}_{0} \leq k$.

The RIC for linear operators, $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ is defined similarly, with $X$ instead of $\mathbf{x}$, $\mathcal{A}$ instead of $A$ and ${{rank}{(X)}} \leq k$ instead of ${\|\mathbf{x}\|}_{0} \leq k$, and ${\| X\|}_{F}$ instead of ${\|\mathbf{x}\|}_{2}$.

### Definition: Restricted Orthogonality Constant (ROC)

The ROC of a matrix $A$ is the smallest constant $\theta_{k,k^{\prime}}$ for which

holds for all vectors $\mathbf{x},\mathbf{x}^{\prime}$ with disjoint supports and ${\|\mathbf{x}\|}_{0} \leq k$ and ${\|\mathbf{x}^{\prime}\|}_{0} \leq k^{\prime}$.\

Our definition of ROC for linear operators, $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ is slightly looser than the one given in. For a linear operator $\mathcal{A}$, ROC is the smallest constant $\theta_{k,k^{\prime}}$ for which

holds for all matrices $X,X^{\prime}$ such that ${{rank}{(X)}} \leq k$, ${rank}{(X)}^{\prime} \leq k^{\prime}$ and both column and row spaces of $X,X^{\prime}$ are orthogonal, i.e., in a suitable basis we can write $X = \begin{bmatrix}
\end{bmatrix}$ and $X^{\prime} = \begin{bmatrix}

We say that the matrix $A$ (or operator $\mathcal{A}$) satisfies RIP if the corresponding RIC and ROC constants are sufficiently small to ensure recovery of sparse vectors (low rank matrices). As one example if a matrix $A$ satisfies $\delta_{k} < 0.307$ or $\delta_{2k} < 0.472$, then we say $A$ satisfies RIP, since these conditions are sufficient for recovery of $k$-sparse vectors using $\ell_{1}$ minimization.

### Definition: Spherical Section Property (SSP)

The Spherical Section constant of a linear operator $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ is defined as

and we say $\mathcal{A}$ satisfies the $\Delta$-Spherical Section Property if ${\Delta{(\mathcal{A})}} \geq \Delta$.

The definition of SSP for a matrix $A \in {\mathbb{R}}^{n \times m}$ for analyzing recovery of sparse vectors is analogous to the above definition. Another way to describe this property is to note that a large $\Delta$ implies the nullspace is an *almost Euclidean* subspace, whose elements cannot have a small ratio of $\ell_{1}$ (nuclear norm) to $\ell_{2}$ (Frobenius norm), and therefore the subspace cannot include sparse (low-rank) elements.\
In the subsequent sections, we give our main results relating vector recovery to matrix recovery.

## Key Observations

Throughout this note, many of the proofs involving matrices apply the following useful Lemma which enables us to "vectorize" matrices when dealing with matrix norm inequalities.

### Lemma 1

() (Key Lemma) For any ${X,Y} \in {\mathbb{R}}^{n_{1} \times n_{2}}$, we have

We now give an application of Lemma 1.

### Lemma 2

Given $W$ with singular value decomposition $U\Sigma_{W}V^{T}$, if there is an $X_{0}$ for which ${\|{X_{0} + W}\|}_{\star} \leq {\| X_{0}\|}_{\star}$ then there exists $X_{1} \in {S{(U,V)}}$ with $\Sigma_{X_{1}} = \Sigma_{X_{0}}$ such that ${\|{X_{1} + W}\|}_{\star} \leq {\| X_{1}\|}_{\star}$. In particular this is true for $X_{1} = {- {U\Sigma_{X_{0}}V^{T}}}$.

### Proof

From Lemma 1 we have

On the other hand, for $X_{1} = {{- {U\Sigma_{X_{0}}V^{T}}},W}$ we have

Then from and it follows

Although Lemma 2 is easy to show, it proves helpful in Theorem 1 to connect vector recovery (on restricted subpaces $S{(U,V)}$) to matrix recovery over all space ${\mathbb{R}}^{n_{1} \times n_{2}}$.

To further illustrate the similarity between sparse and low rank recovery, we state the null space conditions for noiseless recovery.

### Lemma 3

() Null space condition for sparse recovery\
Let $A \in {\mathbb{R}}^{m \times n}$ be a measurement matrix. Assume $\epsilon = 0$ then one can perfectly recover all vectors $\mathbf{x}_{0}$ with ${\|\mathbf{x}_{0}\|}_{0} \leq k$ via program 3 if and only if for any $\mathbf{w} \in {\mathcal{N}{(A)}}$ we have

where ${\overline{w}}_{i}$ is the $i$th entry of $\overline{\mathbf{w}}$ defined previously in section II.

The use of the above condition has a long history; it was stated in (see also ) for matrices made from concatenation of two bases, and studied in in a general setting.

### Lemma 4

() Null space condition for low-rank recovery Let $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ be a linear measurement operator. Assume $\epsilon = 0$ then one can recover all matrices $X_{0}$ with ${{rank}{(X_{0})}} \leq k$ via program 4 if and only if for any $W \in {\mathcal{N}{(\mathcal{A})}}$ we have

## Main Result

In this section, we state our main result which enables us to seamlessly translate results for vector recovery to matrix recovery. Our main theorem assumes that operator $\mathcal{A}$ satisfies an extension property, defined below.

### Definition: Extension

Let $\mathbf{P}$ be a property defined for matrices, $A \in {\mathbb{R}}^{m \times n}$. We say that a linear operator, $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ satisfies the extension property, $\mathbf{P}^{e}$ if all its restrictions $A_{U,V}$ have property $\mathbf{P}$.

RIP and SSP are two examples of property $\mathbf{P}$ that are of interest in this paper. We show later that the main theorem can be applied to these properties.

Let $\parallel \cdot \parallel_{v}$ be an arbitrary norm on ${\mathbb{R}}^{n}$ with ${\|\mathbf{x}\|}_{v} = {\|\overline{\mathbf{x}}\|}_{v}$ for all $\mathbf{x}$. Let $\parallel \cdot \parallel_{m}$ be the corresponding unitarily invariant matrix norm on ${\mathbb{R}}^{n_{1} \times n_{2}}$ such that ${\| X\|}_{m} = {\|{\Sigma{(X)}}\|}_{v}$. For the sake of clarity, we use the following shorthand notation in the main theorem for statements regarding recovery of vectors:

$V_{1}$: A matrix $A:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ satisfies a property $\mathbf{P}$.

$V_{2}$: In program 3, for any $\mathbf{x}_{0}$, ${\|\mathbf{z}\|}_{2} \leq \epsilon$, $\mathbf{y} = {{A\mathbf{x}_{0}} + z}$ and any $\mathbf{x}^{\ast}$ as good as $\mathbf{x}_{0}$ we have,

$V_{3}$: For any $\mathbf{w} \in {\mathcal{N}{(A)}}$, $\mathbf{w}$ satisfies a property $\mathbf{Q}$.

We also use the following shorthand for statements regarding recovery of matrices:

$M_{1}$: A linear operator $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ satisfies the extension property $\mathbf{P}^{e}$.

$M_{2}$: In program 4, for any $X_{0}$, ${\|\mathbf{z}\|}_{2} \leq \epsilon$, $\mathbf{y} = {{\mathcal{A}{(X_{0})}} + \mathbf{z}}$ and any $X^{\ast}$ as good as $X_{0}$ we have,

$M_{3}$: For any $W \in {\mathcal{N}{(\mathcal{A})}}$, $\Sigma{(W)}$ satisfies property $\mathbf{Q}$.

### Theorem 1

For a given $\mathbf{P}$, the following implications hold true:\

### Proof

${({V_{1}\Longrightarrow V_{2}})}\Longrightarrow{({M_{1}\Longrightarrow M_{2}})}$.\
Assume $V_{1}\Longrightarrow V_{2}$ and that $M_{1}$ holds. Consider program 4 where measurements are $\mathbf{y}_{0} = {{\mathcal{A}{(X_{0})}} + \mathbf{z}_{0}}$ with ${\|\mathbf{z}_{0}\|}_{2} \leq \epsilon$. We would like to show that for any $X^{\ast}$ that is as good as $X_{0}$ w.r.t $\mathbf{y}_{0}$, it holds that ${\|{X^{\ast} - X_{0}}\|}_{m} \leq {h{({\Sigma{(X_{0})}},\epsilon)}}$. Consider any such $X^{\ast}$ and let $W = {X^{\ast} - X_{0}}$. This implies that ${\|{X_{0} + W}\|}_{\star} \leq {\| X_{0}\|}_{\star}$ and ${\|{{\mathcal{A}{({X_{0} + W})}} - \mathbf{y}_{0}}\|}_{2} \leq \epsilon$. Then, from Lemma 2 for $X_{1} = {- {U\Sigma_{X_{0}}V^{T}}}$ (where $W$ has SVD $U\Sigma_{W}V^{T}$) we have ${\|{X_{1} + W}\|}_{\star} \leq {\| X_{1}\|}_{\star}$. Now, let $\mathbf{y}_{1} = {{\mathcal{A}{(X_{1})}} + z_{0}}$. Clearly

and hence $X_{1} + W$ is as good as $X_{1}$ w.r.t $\mathbf{y}_{1}$. Now consider program 1 with $A_{U,V}$ as measurement matrix, $\mathbf{y}_{1}$ as measurements, $\mathbf{x}_{1} = {- \Sigma_{X_{0}}}$ as unknown vector and $\mathbf{w} = \Sigma_{W}$ as the perturbation. Notice that $\mathbf{x}_{1} + \mathbf{w}$ is as good as $\mathbf{x}_{1}$ w.r.t $\mathbf{y}_{1}$. Also since $\mathcal{A}$ has $\mathbf{P}^{e}$, $A_{U,V}$ has $\mathbf{P}$ and thus $V_{1}$ holds for $A = A_{U,V}$. Using $V_{1}\Longrightarrow V_{2}$ we conclude

It thus holds that $M_{1}\Longrightarrow M_{2}$.

Using similar arguments, we now show that ${({V_{1}\Longrightarrow V_{3}})}\Longrightarrow{({M_{1}\Longrightarrow M_{3}})}$.\
Assume $V_{1}\Longrightarrow V_{3}$ and that $M_{1}$ holds. Consider any $W \in {\mathcal{N}{(\mathcal{A})}}$ with SVD of $W = {U\Sigma_{W}V^{T}}$. Then, ${\mathcal{A}{(W)}} = {A_{U,V}\Sigma{(W)}} = 0$. Also $A_{U,V}$ satisfies $\mathbf{P}$ and hence $V_{1}$ holds for $A = A_{U,V}$. Using $V_{1}\Longrightarrow V_{3}$, we find $\Sigma{(W)}$ satisfies $\mathbf{Q}$. Hence $M_{1}\Longrightarrow M_{3}$.

As can be seen from the Main Theorem, throughout the paper, we are dealing with a *strong* notion of recovery. By strong we mean $\mathbf{P}$ guarantees recovery for all $\mathbf{x}_{0}$ ($X_{0}$) with sparsity (rank) at most $k$ instead of for just a particular $\mathbf{x}_{0}$ ($X_{0}$). For example, results for the matrix completion problem in the literature don't have a *strong* recovery guarantee. On the other hand it is known that (good) RIP or SSP conditions guarantee recoverability for all vectors and yield *strong* recovery results.

In the next section, we show that the main theorem can be applied to RIP and SSP based recovery and thus the corresponding recovery results for matrix recovery easily follow.

### IV-A Application of Main Theorem to RIP based recovery

We say that ${f{(\delta_{i_{1}},\ldots,\delta_{i_{m}},\theta_{j_{1},j_{1}^{\prime}},\ldots,\theta_{j_{n},j_{n}^{\prime}})}} \leq c$ is an RIP inequality where $c \geq 0$ is a constant and $f{( \cdot )}$ is an increasing function of its parameters (RIC and ROC) and ${f{(0,\ldots,0)}} = 0$. Let $\mathcal{F}$ be a set of RIP inequalities namely $f_{1},\ldots,f_{N}$ where $k$'th inequality is of the form:

### Lemma 5

If $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ satisfies a set of (matrix) RIP and ROC inequalities $\mathcal{F}$, then for all unitary pairs $(U,V)$, $A_{U,V}$ will satisfy the same inequalities.

### Proof

Let $\delta_{k}^{\prime},\theta_{k,k^{\prime}}^{\prime}$ denote RIC and ROC of of $A_{U,V}$ and $\delta_{k},\theta_{k,k^{\prime}}$ denote RIC and ROC of $\mathcal{A}{( \cdot )}$. Then we claim: $\delta_{k}^{\prime} \leq \delta_{k}$ and $\theta_{k,k^{\prime}}^{\prime} \leq \theta_{k,k^{\prime}}$. For any $\mathbf{x}$ of ${\|\mathbf{x}\|}_{0} \leq k$, let $X = {U\text{diag}{(\mathbf{x})}V^{T}}$. Using ${\|\mathbf{x}\|}_{2} = {\| X\|}_{F}$ and ${A_{U,V}\mathbf{x}} = {\mathcal{A}{(X)}}$ we have:

Hence $\delta_{k}^{\prime} \leq \delta_{k}$. Similarly let $\mathbf{x},\mathbf{x}^{\prime}$ have disjoint supports with sparsity at most $k,k^{\prime}$ respectively. Then obviously $X = {U\text{diag}{(\mathbf{x})}V^{T}}$ and $X^{\prime} = {U\text{diag}{(\mathbf{x}^{\prime})}V^{T}}$ satisfies the condition in ROC definition. Hence:

Hence $\theta_{k,k^{\prime}}^{\prime} \leq \theta_{k,k^{\prime}}$. Thus, $A_{U,V}$ satisfies the set of inequalities $\mathcal{F}$ as $f_{i}{( \cdot )}$'s are increasing function of $\delta_{k}$'s and $\theta_{k,k^{\prime}}$'s.

We can thus combine Lemma 5 and the main theorem to smoothly translate any implication of RIP for vector recovery to corresponding implication for matrix recovery. In particular, some typical RIP implications are as follows.

### RIP implications for $k$-sparse recovery

() Suppose $A:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ satisfies, a set of RIP inequalities $\mathcal{F}$. Then for all $\mathbf{x}_{0}$, ${\|\mathbf{z}\|}_{2} \leq \epsilon$ and $\mathbf{x}^{\ast}$ as good as $\mathbf{x}_{0}$ we have the following $\ell_{2}$ and $\ell_{1}$ robustness results,

for some constants ${C_{1},C_{2},C_{3}} > 0$.

Now, using Lemma 5 and Theorem 1, we have the following implications for matrix recovery.

### Lemma 6

Suppose $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ satisfies the same inequalities $\mathcal{F}$ as in. Then for all $X_{0}$, ${\|\mathbf{z}\|}_{2} \leq \epsilon$ and $X^{\ast}$ as good as $X_{0}$ we have the following Frobenius norm and nuclear norm robustness results,

### IV-B Application of Main theorem to SSP based recovery

### Lemma 7

Let $\Delta > 0$. If $\mathcal{A}:{{\mathbb{R}}^{n_{1} \times n_{2}}\rightarrow{\mathbb{R}}^{m}}$ satisfies $\Delta$-SSP, then for all unitary pairs $(U,V)$, $A_{U,V}$ satisfies $\Delta$-SSP.

### Proof

Consider any $\mathbf{w} \in {\mathcal{N}{(\mathcal{A}_{U,V})}}$. Then, ${\mathcal{A}{({U\text{diag}{(\mathbf{w})}V^{T}})}} = 0$ and therefore $W = {U\text{diag}{(\mathbf{w})}V^{T}} \in {\mathcal{N}{(\mathcal{A})}}$. Since $\mathcal{A}$ satisfies $\Delta$-SSP, we have $\frac{{\| W\|}_{\ast}}{{\| W\|}_{F}} = \frac{{\|\mathbf{w}\|}_{1}}{{\|\mathbf{w}\|}_{2}} \geq \sqrt{\Delta}$. Thus $A_{U,V}$ satisfies $\Delta$-SSP.

Now we give the following SSP based result for matrices as an application of main theorem.

### Theorem 2

Consider program 4 with $\mathbf{z} = 0$, $\mathbf{y} = {\mathcal{A}{(X_{0})}}$. Let $X^{\ast}$ be as good as $X_{0}$. Then if $\mathcal{A}$ satisfies $\Delta$-SSP with $\Delta > {4k}$, it holds that

where $C = \frac{2}{1 - {2\sqrt{k/\Delta}}}$.

Note that the use of main theorem and *Key Lemma* simplifies the recovery analysis in and also improves the sufficient condition of $k < \frac{\Delta}{6}$ in to $k < \frac{\Delta}{4}$. This improved sufficient condition matches the sufficient condition given in for the sparse vector recovery problem.

## Simplified Robustness Conditions

We show that various robustness conditions are equivalent to simple conditions on the measurement operator. The case of noiseless and perfectly sparse signals, is already given in Lemmas 3 and 4. Such simple conditions might be useful for analysis of nuclear norm minimization in later works. We state the conditions for matrices only; however, vector and matrix conditions will be identical (similar to Lemmas 3, 4) as one can expect from Theorem 1. The proofs follow from simple algebraic manipulations with the help of Lemma 1.

### Lemma 8

(Nuclear Norm Robustness for Matrices)\
Assume $\epsilon = 0$ (no noise). Let $C > 1$ be constant. Then for any $X_{0}$ and any $X^{\ast}$ as good as $X_{0}$ we are guaranteed to have:

if and only if for all $W \in {\mathcal{N}{(\mathcal{A})}}$ we have:

### Lemma 9

(Frobenius Norm Robustness for Matrices)\
Let $\epsilon = 0$. Then for any $X_{0}$ and $X^{\ast}$ as good as $X_{0}$,

if and only if for all $W \in {\mathcal{N}{(\mathcal{A})}}$,

### Lemma 10

(Matrix Noise Robustness) For any $X_{0}$ with ${r{(X_{0})}} \leq k$, any ${\|\mathbf{z}\|}_{2} \leq \epsilon$ and any $X^{\ast}$ as good as $X_{0}$,

if and only if for any $W$ with ${\| W^{k}\|}_{\star} \geq {\|{W - W^{k}}\|}_{\star}$,

## Null space based recovery result for Schatten-$p$ quasi-norm minimization

In the previous sections, we stated the main theorem and considered its applications on RIP and SSP based conditions to show that results for recovery of sparse vectors can be analogously extended to recovery of low-rank matrices without making the recovery conditions stronger. In this section, we consider extending results from vectors to matrices using an algorithm different from $\ell_{1}$ minimization or nuclear norm minimization.

The $\ell_{p}$ quasi-norm (with $0 < p < 1$) is given by ${\| x\|}_{p}^{p} = {\sum_{i = 1}^{n}{|x|}_{i}^{p}}$. Note that for $p = 0$, this is nothing but the cardinality function. Thus it is natural to consider the minimization of the $\ell_{p}$ quasi-norm (as a surrogate for minimizing the cardinality function). Indeed, $\ell_{p}$ minimization has been a starting point for algorithms including Iterative Reweighted Least Squares and Iterative Reweighted $\ell_{1}$ minimization. Note that although $\ell_{1}$ minimization is convex, $\ell_{p}$ minimization with $0 < p < 1$ is *non-convex*. However empirically, $\ell_{p}$ minimization based algorithms with $0 < p < 1$ have a better recovery performance as compared to $\ell_{1}$ minimization (see e.g.,). The recovery analysis of these algorithms has mostly been based on RIP. However Null space based recovery conditions analogous to those for $\ell_{1}$ minimization have been given for $\ell_{p}$ minimization (see e.g. ).

Let ${Tr}|A|^{p} = {Tr}{(A^{T}A)}^{\frac{p}{2}} = \sum_{i = 1}^{n}\sigma_{i}^{p}{(A)}$ denote the *Schatten-$p$ quasi norm* with $0 < p < 1$. Analogous to the vector case, one can consider the minimization of the Schatten-$p$ quasi-norm for the recovery of low-rank matrices,

where $y = {\mathcal{A}{(X_{0})}}$ with $X_{0}$ being the low-rank solution we wish to recover. IRLS-$p$ has been proposed as an algorithm to find a local minimum to in. However no null-space based recovery condition has been given for the recovery analysis of Schatten-$p$ quasi norm minimization. We give such a condition below, after mentioning a few useful inequalities.

### Lemma 11 (\[28\])

For any two matrices ${A,B} \in {\mathbb{R}}^{m \times n}$ it holds that ${\sum_{i = 1}^{k}{({{\sigma_{i}^{p}{(A)}} - {\sigma_{i}^{p}{(B)}}})}} \leq {\sum_{i = 1}^{k}{\sigma_{i}^{p}{({A - B})}}}$ for all $k = {1,2,\ldots,n}$.

Note that the $p$ quasi-norm of a vector satisfies the triangle inequality (${x,y} \in {\mathbb{R}}^{n}$, ${\sum_{i = 1}^{n}{|{x_{i} + y_{i}}|}^{p}} \leq {{\sum_{i = 1}^{n}{|x_{i}|}^{p}} + {\sum_{i = 1}^{n}{|y_{i}|}^{p}}}$). Lemma 11. ‣ VI Null space based recovery result for Schatten-𝑝 quasi-norm minimization ‣ A Simplified Approach to Recovery Conditions for Low Rank Matrices") generalizes this result to matrices.

### Lemma 12 (\[19\])

For any two matrices $A,B$ it holds that

where ${{{t + s} - 1} \leq {n,t}},{s \geq 0}$.

The following lemma easily follows as a consequence.

### Lemma 13

For any two matrices, $A,B$ with $B$ of rank $k$ and any $p > 0$,

### Theorem 3

Let *rank*${(X_{0})} = k$ and let $\overline{X}$ denote the global minimizer of. A sufficient condition for $\overline{X} = X_{0}$ is that ${\sum_{i = 1}^{2k}{\sigma_{i}^{p}{(W)}}} \leq {\sum_{i = {{2k} + 1}}^{n}{\sigma_{i}^{p}{(W)}}}$ for all $W \in {\mathcal{N}{(\mathcal{A})}}$. A necessary condition for $\overline{X} = X_{0}$ is that ${\sum_{i = 1}^{k}{\sigma_{i}^{p}{(W)}}} \leq {\sum_{i = {k + 1}}^{n}{\sigma_{i}^{p}{(W)}}}$ for all $W \in {\mathcal{N}{(\mathcal{A})}}$.

### Proof

($\Rightarrow$) For any $W \in {{\mathcal{N}{(\mathcal{A})}}\backslash{\{ 0\}}}$,

where the first inequality follows from Lemma 11. ‣ VI Null space based recovery result for Schatten-𝑝 quasi-norm minimization ‣ A Simplified Approach to Recovery Conditions for Low Rank Matrices") and Lemma 13. The necessary condition is easy to show analgous to the results for nuclear norm minimization.

Note that there is a gap between the necessary and sufficient conditions. We observe through numerical experiments that a better inequality such as ${\sum\limits_{i = 1}^{n}{\sigma_{i}^{p}{({A - B})}}} \geq {\sum\limits_{i = 1}^{n}{|{{\sigma_{i}^{p}{(A)}} - {\sigma_{i}^{p}{(B)}}}|}}$ seems to hold for any two matrices $A,B$. Note that this is in particular true for $p = 1$ (Lemma 1) and $p = 0$. If this inequality is proven true for all $0 < p < 1$, then we could bridge the gap between necessity and sufficiency in Theorem 3. Thus we have that singular value inequalities including those in Lemma 1 and Lemma 13, 11. ‣ VI Null space based recovery result for Schatten-𝑝 quasi-norm minimization ‣ A Simplified Approach to Recovery Conditions for Low Rank Matrices") play a fundamental role in extending recovery results from vectors to matrices. Although, our condition is not tight, we can still use the Theorems 1 and 3 to conclude the following:

### Lemma 14

Assume property $\mathbf{S}$ on matrices ${\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}$ implies perfect recovery of all vectors with sparsity at most $2k$ via $\ell_{p}$ quasi-norm minimization where $0 < p < 1$. Then $\mathbf{S}^{e}$ implies perfect recovery of all matrices with rank at most $k$ via Schatten-$p$ quasi-norm minimization.

*Proof Idea:* Since $\mathbf{S}$ implies perfect recovery of all vectors with sparsity at most $2k$, it necessarily implies a *null space property* (call it $\mathbf{Q}$) similar to the one given in Lemma 3, but with $p$ in the exponent (see e.g. ) and $k$ replaced by $2k$. Now the main theorem combined with Theorem 3 implies that $\mathbf{S}^{e}$ is sufficient for perfect revovery of rank $k$ matrices.\
In particular, using Lemma 14, we can conclude, any set of RIP conditions that are sufficient for recovery of vectors of sparsity up to $2k$ via $\ell_{p}$ minimization, are also sufficient for recovery of matrices of rank up to $k$ via Schatten-$p$ minimization. As an immediate consequence it follows that the results in can be easily extended.

## Conclusions

We presented a general result stating that the extension of any sufficient condition for the recovery of sparse vectors using $\ell_{1}$ minimization is also sufficient for the recovery of low-rank matrices using nuclear norm minimization. Consequently, we have that the best known RIP-based recovery conditions of $\delta_{k} < 0.307$ (and $\delta_{2k} < 0.472$) for sparse vector recovery are also sufficient for low-rank matrix recovery. Note that our result shows there is no "gap" between the recovery conditions for vectors and matrices, and we do not lose a factor of 2 in the rank of matrices that can be recovered, as might be suggested by existing analysis (e.g. ).

We showed that a Null-space based sufficient condition (Spherical Section Property) given in easily extends to the matrix case, tightening the existing conditions for low-rank matrix recovery. Finally, we gave null-space based conditions for recovery using Schatten-$p$ quasi-norm minimization and showed that RIP based conditions for $\ell_{p}$ minimization extend to the matrix case. We note that all of these results rely on the ability to "vectorize" matrices through the use of key singular value inequalities including Lemma 1, 11. ‣ VI Null space based recovery result for Schatten-𝑝 quasi-norm minimization ‣ A Simplified Approach to Recovery Conditions for Low Rank Matrices").
