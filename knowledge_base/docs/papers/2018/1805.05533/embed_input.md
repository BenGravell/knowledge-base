<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Discovering Transforms: A Tutorial on Circulant Matrices, Circular Convolution, and the Discrete Fourier Transform

Topics include Transforms, DFT, Discrete fourier transform, Fourier transform.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

How could the Fourier and other transforms be naturally discovered if one didn't know how to postulate them? In the case of the Discrete Fourier Transform (DFT), we show how it arises naturally out of analysis of circulant matrices. In particular, the DFT can be derived as the change of basis that simultaneously diagonalizes all circulant matrices. In this way, the DFT arises naturally from a linear algebra question about a set of matrices. Rather than thinking of the DFT as a signal transform, it is more natural to think of it as a single change of basis that renders an entire set of mutually-commuting matrices into simple, diagonal forms. The DFT can then be "discovered" by solving the eigenvalue/eigenvector problem for a special element in that set. A brief outline is given of how this line of thinking can be generalized to families of linear operators, leading to the discovery of the other common Fourier-type transforms, as well as its connections with group representations theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Fourier transform in all its forms is ubiquitous. Its many useful properties are introduced early on in Mathematics, Science and Engineering curricula. Typically, it is introduced as a transformation on functions or signals, and then its many useful properties are easily derived. Those properties are then shown to be remarkably effective in solving certain differential equations, or in analyzing the action of time-invariant linear dynamical systems, amongst many other uses. To the student, the effectiveness of the Fourier transform in solving these problems may seem magical at first, before familiarity eventually suppresses that initial sense of wonder. In this tutorial, I'd like to step back to before one is shown the Fourier transform, and ask the following question: How would one naturally discover the Fourier transform rather than have it be postulated?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above question is interesting for several reasons. First, it is more intellectually satisfying to introduce a new mathematical object from familiar and well-known objects rather than having it postulated "out of thin air". In this tutorial we demonstrate how the DFT arises naturally from the problem of simultaneous diagonalization of all circulant matrices, which share symmetry properties that enable this diagonalization. It should be noted that simultaneous diagonalization of any class of linear operators or matrices is the ultimate way to understand their actions, by reducing the entire class to the simplest form of linear operations (diagonal matrices) simultaneously. The same procedure can be applied to discover the other close relatives of the DFT, namely the Fourier Transform, the $z$-Transform and Fourier Series. All can be arrived at by simultaneously diagonalizing a respective class of linear operators that obey their respective symmetry rules.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make the point above, and to have a concrete discussion, in this tutorial we consider primarily the case of circulant matrices. This case is also particularly useful because it yields the DFT, which is the computational workhorse for all Fourier-type analysis. Given an $n$-vector $a:={(a_{0},\ldots,a_{n - 1})}$, define the associated matrix $C_{a}$ whose first column is made up of these numbers, and each subsequent column is obtained by a circular shift of the previous column

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that each row is also obtained from the pervious row by a circular shift. Thus the entire matrix is completely determined by any one of its rows or columns. Such matrices are called circulant. They are a subclass of Toeplitz matrices, and as mentioned, have very special properties due to their intimate relation to the Discrete Fourier Transform (DFT) and circular convolution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given an $n$-vector $a$ as above, its DFT $\hat{a}$ is another $n$-vector defined by

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A remarkable fact is that given a circulant matrix $C_{a}$, its eigenvalues are easily computed. They are precisely the set of complex numbers $\left\{ {\hat{a}}_{k} \right\}$, i.e. the DFT of the vector $a$ that defines the circulant matrix $C_{a}$. There are many ways to derive this conclusion and other properties of the DFT. Most treatments start with the definition Eq. 2 of the DFT, from which many of its seemingly magical properties are easily derived. To restate the goal of this tutorial, the question we ask here is: what if we didn't know the DFT? How can we arrive at it in a natural manner without needing someone to postulate Eq. 2 for us?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a natural way to think about this problem. Given a class of matrices or operators, one asks if there is a transformation, a change of basis, in which their matrix representations all have the same structure such as diagonal, block diagonal, or other special forms. The simplest such scenario is when a class of matrices can be simultaneously diagonalized with the same transformation. Since diagonalizing transformations are made up of eigenvectors of a matrix, then a set of matrices is simultaneously diagonalizable iff they share a full set of eigenvectors. An equivalent condition is that they each are diagonalizable, and they all mutually commute. Therefore given a mutually commuting set of matrices, by finding their shared eigenvectors, one finds that special transformation that simultaneously diagonalizes all of them. Thus, finding the "right transform" for a particular class of operators amounts to identifying the correct eigenvalue problem, and then calculating the eigenvectors, which then yield the transform.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative but complementary view of the above procedure involves describing the class of operators using some underlying common symmetry. For example, circulant matrices such as Eq. 1 have a shift invariance property with respect to circular shifts of vectors. This can also be described as having a shift-invariant action on vectors over ${\mathbb{Z}}_{n}$ (the integers modulo $n$), which is also equivalent to having a shift-invariant action on periodic functions (with period $n$). In more formal language, circulant matrices represent a class of mutually commuting operators that also commute with the action of the group ${\mathbb{Z}}_{n}$. A basic shift operator generates that group, and the eigenvalue problem for that shift operator yields the DFT. This approach has the advantage of being generalizable to more complex symmetries that can be encoded in the action of other, possibly non-commutative, groups. These techniques are part of the theory of group representations. However, we adopt here the approach described in the previous paragraph, which uses familiar Linear Algebra language and avoids the formalism of group representations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

None the less, the two approaches are intimately linked. Perhaps the present approach can be thought of as a "gateway" treatment on a slippery slope to group representations if the reader is so inclined.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This tutorial follows the ideas described earlier. We first (Section 2) investigate the simultaneous diagonalization problem for matrices, which is of interest in itself, and show how it can be done constructively. We then (Section 3) introduce circulant matrices, explore their underlying geometric and symmetry properties, as well as their simple correspondence with circular convolutions. The general procedure for commuting matrices is then used (Section 4) for the particular case of circulant matrices to simultaneously diagonalize them. The traditionally defined DFT emerges naturally out of this procedure, as well as other equivalent transforms. The "big picture" for the DFT is then summarized (Section 5). A much larger context is briefly outlined in Section 6, where the close relatives of the DFT, namely the Fourier transform, the $z$-transform and Fourier series are discussed. Those can be arrived at naturally by simultaneously "diagonalizing" families of mutually commuting linear operators. In this case, diagonalization has to be interpreted in a more general sense of conversion to so-called multiplication operators.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally (Section 6.2), an example of a non-commutative case is given where not diagonalization, but rather simultaneous block-diagonalization is possible. This serves as a motivation for generalizing classical Fourier analysis to so-called non-commutative Fourier analysis which is very much the subject of group representations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Simultaneous Diagonalization of Commuting Matrices", "weight": 1.0} -->

The simplest matrices to study and understand are the diagonal matrices. They are basically uncoupled sets of scalar multiplications, essentially the simplest of all possible linear operations. When a matrix $M$ can be diagonalized with a similarity transformation (i.e. $\Lambda = {V^{- 1}MV}$, where $\Lambda$ is diagonal), then we have a change of basis in which the linear transformation has that simple diagonal matrix representation, and its properties can be easily understood.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Simultaneous Diagonalization of Commuting Matrices", "weight": 1.0} -->

Often one has to work with a set of transformations rather than a single one, and usually with sums and products of elements of that set. If we require a different similarity transformation for each member of that set, then sums and products will each require finding their own diagonalizing transformation, which is a lot of work. It is then natural to ask if there exists one basis in which all members of a set of transformations have diagonal forms. This is the simultaneous diagonalization problem. If such a basis exists, then the properties of the entire set, as well as all sums and products (i.e. the algebra generated by that set) can be easily deduced from their diagonal forms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The case of simple (non-repeated) eigenvalues", "weight": 1.0} -->

Now consider the problem of simultaneous diagonalization. It is clear from the above discussion that two matrices can be simultaneously diagonalized iff they share a full set of eigenvectors. Consider the converse of the argument Eq. 3, and assume that $A$ has (simple) non-repeated eigenvalues. This means that

<!-- chunk {"id": "body-0017", "role": "body", "section": "The case of simple (non-repeated) eigenvalues", "weight": 1.0} -->

Consider any matrix $B$ that commutes with $A$. Let $B$ act on each of the eigenvectors by $Bv_{i}$ and observe that

<!-- chunk {"id": "body-0018", "role": "body", "section": "The case of simple (non-repeated) eigenvalues", "weight": 1.0} -->

Thus $Bv_{i}$ is an eigenvector of $A$ with eigenvalue $\lambda_{i}$. Since those eigenvalues are distinct, and the corresponding eigenspace is one dimensional, $Bv_{i}$ must be a scalar multiple of $v_{i}$

<!-- chunk {"id": "body-0019", "role": "body", "section": "The case of simple (non-repeated) eigenvalues", "weight": 1.0} -->

Thus $v_{i}$ is an eigenvector of $B$, but possibly with an eigenvalue $\gamma_{i}$ different from $\lambda_{i}$. In other words, the eigenvectors of $B$ are exactly the unique (up to scalar multiples) eigenvectors of $A$. We summarize this next.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Structural Properties of Circulant Matrices", "weight": 1.0} -->

The structure of circulant matrices is most clearly expressed using modular arithmetic. In some sense, modular arithmetic "encods" the symmetry properties of circulant matrices. We begin with a geometric view of modular arithmetic by relating it to rotations of roots of unity. We then show the "rotation invariance" of the action of circulant matrices, and finally connect that with circular convolution.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

To understand the symmetry properties of circulant matrices, it is useful to first study and establish some simple properties of the set ${\mathbb{Z}}_{n}:=\left\{ 0,1,\cdots,{n - 1} \right\}$ of integers modulo $n$. The arithmetic in ${\mathbb{Z}}_{n}$ is modular arithmetic, that is, we say $k$ equals $l$ modulo $n$ if $k - l$ is an integer multiple of $n$. The following notation can be used to describe this formally

<!-- chunk {"id": "body-0022", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

Thus for example $n \equiv_{n}0$, and ${n + 1} \equiv_{n}1$ and so. There are two equivalent ways to define (and think) about ${\mathbb{Z}}_{n}$, one mathematically formal and the other graphical. The first is to consider the set of all integers $\mathbb{Z}$ and regard any two integers $k$ and $l$ such that $k - l$ is a multiple of $n$ as equivalent, or more precisely as members of the same equivalence class. The infinite set of integers $\mathbb{Z}$ becomes a finite set of equivalence classes with this equivalence relation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

This is illustrated in Fig. 1a where elements of ${\mathbb{Z}}_{n}$ are arranged in "vertical bins" which are the equivalence classes. Each equivalence class can be identified with any of its members. One choice is to identify the first one with the element $0$, the second one with $1$, and so on up to the $n$'th class identified with the integer $n - 1$. Fig. 1c also shows how elements of ${\mathbb{Z}}_{n}$ can be arranged on a discrete circle so that the arithmetic in ${\mathbb{Z}}_{n}$ is identified with angle addition. One more useful isomorphism is between ${\mathbb{Z}}_{n}$ and the $n$th roots of unity $\rho_{m}:=e^{i\frac{2\pi}{n}m}$, $m = {0,\ldots,{n - 1}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

The complex numbers $\left\{ \rho_{m} \right\}$ lie on the unit circle each at a corresponding angle of $\frac{2\pi}{n}m$ counter-clockwise from the real axis (Fig. 1d). Complex multiplication on $\left\{ \rho_{m} \right\}$ corresponds to addition of their corresponding angles, and the mapping $\rho_{m}\rightarrow m$ is an isomorphism from complex multiplication on $\left\{ \rho_{m} \right\}$ to modular arithmetic in ${\mathbb{Z}}_{n}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

Using modular arithmetic, we can write down the definition of a circulant matrix Eq. 1 by specifying the $kl$'th entry^11^1Here, and in this entire tutorial, matrix rows and columns are indexed from $0$ to $n - 1$ rather than the more traditional $1$ through $n$ indexing. This alternative indexing significantly simplifies notation, and corresponds more directly to modular arithmetic. of the matrix $C_{a}$ as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

where we use (mod $n$) arithmetic for computing $k - l$. It is clear that with this definition, the first column of $C_{a}$ is just the sequence $a_{0},a_{1},\cdots,a_{n - 1}$. The second column is given by the sequence $\left\{ a_{k - 1} \right\}$ and is thus $a_{- 1},a_{0},\cdots,a_{n - 2}$, which is exactly the sequence $a_{n - 1},a_{0},\cdots,a_{n - 2}$, i.e. a circular shift of the first column. Similarly each subsequent column is a circular shift of the column preceding it.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

Finally, it is useful to visualize an $n$-vector $x:={(x_{0},\ldots,x_{n - 1})}$ as a set of numbers arranged at equidistant points along a circle, or equivalently as a function on the discrete circle. This is illustrated in Fig. 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

Note the difference between this figure and Fig. 1, which depicts the elements of ${\mathbb{Z}}_{n}$ and modular arithmetic. Fig. 2 instead depicts vectors as a set of numbers arranged in a discrete circle, or as functions on ${\mathbb{Z}}_{n}$. A function on ${\mathbb{Z}}_{n}$ can also be thought of as a periodic function (with period $n$) on the set of integers $\mathbb{Z}$ (Fig. 2.c). In this case, periodicity of the function is expressed by the condition

<!-- chunk {"id": "body-0029", "role": "body", "section": "Modular Arithmetic, ${\\mathbb{Z}}_{n}$, and Circular Shifts", "weight": 1.0} -->

It is however more natural to view periodic functions on $\mathbb{Z}$ as just functions on ${\mathbb{Z}}_{n}$. In this case, periodicity of the function is simply "encoded" in the modular arithmetic of ${\mathbb{Z}}_{n}$, and condition Eq. 24 does not need to be explicitly stated.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

Amongst all circulant matrices, there is a special one. Let $S$ and its adjoint $S^{\ast}$ be the circular shift operators defined by the following action on vectors

<!-- chunk {"id": "body-0031", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

$S$ is therefore called the circular right-shift operator while $S^{\ast}$ is the circular left-shift operator. It is clear that $S^{\ast}$ is the inverse of $S$, and it is easy to show that it is the adjoint of $S$. The latter fact also becomes clear upon examining the matrix representations of $S$ and $S^{\ast}$

<!-- chunk {"id": "body-0032", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

which shows that $S^{\ast}$ is indeed the transpose (and therefore the adjoint) of $S$. Note that both matrix representations are circulant matrices since $S = C_{(0,1,0,\ldots,0)}$ and $S^{\ast} = C_{(0,\ldots,0,1)}$ in the notation of Eq. 1. The actions of $S$ and $S^{\ast}$ expressed in terms of vector indices are

<!-- chunk {"id": "body-0033", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

where modular arithmetic is used for computing vector indices. For example $\left( {Sx} \right)_{0} = x_{0 - 1} \equiv_{n}x_{n\text{-}1}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

An important property of $S$ is that it commutes with any circulant matrix. One way to see this is to observe the for any matrix $M$, left (right) multiplication by $S$ amounts to row (column) circular permutation. A brief look at the circulant structure in Eq. 1 shows that a row circular permutation gives the same matrix as a column circular permutation. Therefore, for any circulant matrix $C_{a}$, we have ${SC_{a}} = {C_{a}S}$. A more detailed argument is as follows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

To see this, note that the matrix representation of $S$ implies its $ij$'th entry is given by $(S)_{ij} = \delta_{i - j - 1}$. Now let $C_{a}$ be any circulant matrix, and observe that

<!-- chunk {"id": "body-0036", "role": "body", "section": "Symmetry Properties of Circulant Matrices", "weight": 1.0} -->

where Eq. 23 is used for the entries of $C_{a}$. Thus $S$ commutes with any circulant matrix. The converse is also true (see Exercise Section A.1), and we state these conclusions in the next lemma.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Circular Convolution", "weight": 1.0} -->

We will start with examining the matrix-vector product when the matrix is circulant. By analyzing this product, we will obtain the circular convolution of two vectors. Let $C_{a}$ by some circulant matrix, and examine the action of such a matrix on any vector $x = \left( x_{0},x_{1},\cdots,x_{n - 1} \right)$. The matrix-vector multiplication $y = {C_{a}x}$ in detail reads

<!-- chunk {"id": "body-0038", "role": "body", "section": "Circular Convolution", "weight": 1.0} -->

Using $\left( C_{a} \right)_{kl} = a_{k - l}$, this matrix-vector multiplication can be rewritten as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Circular Convolution", "weight": 1.0} -->

This can be viewed as an operation on the two vectors $a$ and $x$ to yield the vector $y$, and allows us to reinterpret the matrix-vector product of a circulant matrix as follows.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simultaneous Diagonalization of all Circulant Matrices Yields the DFT", "weight": 1.0} -->

In this section, we will derive the DFT as a byproduct of diagonalizing circulant matrices. Since all circulant matrices mutually commute, we recall Lemma 2.2 eigenvalues ‣ 2 Simultaneous Diagonalization of Commuting Matrices ‣ Discovering Transforms: A Tutorial on Circulant Matrices, Circular Convolution, and the Discrete Fourier Transform") and look for a circulant matrix that has simple eigenvalues. The eigenvectors of that matrix will then give the simultaneously diagonalizing transformation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simultaneous Diagonalization of all Circulant Matrices Yields the DFT", "weight": 1.0} -->

The shift operator is in some sense the most fundamental circulant matrix, and is therefore a good candidate for an eigenvector/eigenvalue decomposition. The eigenvalue problem for $S$ will turn out to be the simplest one. Note that we have two options. To find eigenvectors of $S$ or alternatively of $S^{\ast}$. We begin with $S^{\ast}$ since this will end up yielding the classically defined DFT.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

Let $w$ be an eigenvector (with eigenvalue $\lambda$) of the shift operator $S^{\ast}$. Note that it is also an eigenvector (with eigenvalue $\lambda^{l}$) of any power ${(S^{\ast})}^{l}$ of $S^{\ast}$. Applying the definition Eq. 25 to the relation ${S^{\ast}w} = {\lambdaw}$ will reveal that an eigenvector $w$ has a very special structure

<!-- chunk {"id": "body-0043", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

i.e. each entry $w_{k + 1}$ of $w$ is equal to the previous entry $w_{k}$ multiplied by the eigenvalue $\lambda$. These relations can be used to compute all eigenvectors/eigenvalues of $S^{\ast}$. First, observe that although Eq. 30 is valid for all $l \in {\mathbb{Z}}$, this relation "repeats" for $l \geq n$. In particular, for $l = n$ we have for each index $k$

<!-- chunk {"id": "body-0044", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

since ${k + n} \equiv_{n}k$. Now since the vector $w \neq 0$, then for at least one index $k$, $w_{k} \neq 0$, and the last equality implies that ${\lambda^{n} = 1},$ i.e. any eigenvalue of $S$ must be an $n$th root of unity

<!-- chunk {"id": "body-0045", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

Thus we have discovered that the $n$ eigenvalues of $S^{\ast}$ are precisely the $n$ distinct $n$th roots of unity $\left\{ {{{\rho_{m},m} = 0},{\ldots,{n - 1}}} \right\}$. Note that any of the $n$th roots of unity can be expressed as a power of the first $n$th root: $\rho_{m} = \rho_{1}^{m}$ (recall Fig. 1d).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

Now fix $m \in {\mathbb{Z}}_{n}$ and compute $w^{(m)}$, the eigenvector corresponding to the eigenvalue $\rho_{m}$. Apply the last relation in Eq. 30 $w_{k + l} = {\lambda^{l}w_{k}}$, and use it to express the entries of the eigenvector $w^{(m)}$ in terms of the first entry ($k = 0$)

<!-- chunk {"id": "body-0047", "role": "body", "section": "Construction of Eigenvectors/Eigenvalues of $S^{\\ast}$", "weight": 1.0} -->

Note that $w_{0}$ is a scalar, and since eigenvectors are only unique up to multiplication by a scalar, we can set $w_{0} = 1$ for a more compact expression for the eigenvector. In addition, $\rho_{m}$ in Eq. 32 could be any of the $n$th roots of unity, and thus that expression applies to all of them, yielding the $n$ eigenvectors. We summarize the previous derivations in the following statement.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

Now that we have calculated all the eigenvectors of the shift operator in Lemma 4.1, we can use them to find the eigenvalues of any circulant matrix $C_{a}$. Recall that since any circulant matrix commutes with $S^{\ast}$, and $S^{\ast}$ has distinct eigenvalues, then $C_{a}$ has the same eigenvectors as those Eq. 33 previously found for $S^{\ast}$ (by Lemma 2.2 eigenvalues ‣ 2 Simultaneous Diagonalization of Commuting Matrices ‣ Discovering Transforms: A Tutorial on Circulant Matrices, Circular Convolution, and the Discrete Fourier Transform")). Thus we have the relation

<!-- chunk {"id": "body-0049", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

where $\{\lambda_{m}\}$ are the eigenvalues of $C_{a}$ (not the eigenvalues of $S^{\ast}$ found in the previous section). Each row of the above equation represent essentially the same equation (but multiplied by a power of $\rho_{m}$). The first row is the easiest equation to work with

<!-- chunk {"id": "body-0050", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

which is precisely the classically-defined DFT Eq. 2 of the vector $a$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

We therefore conclude that any circulant matrix $C_{a}$ is diagonalizable by the basis Eq. 33. Its $n$ eigenvalues are given by $\left( {\hat{a}}_{0},{\hat{a}}_{1},\ldots,{\hat{a}}_{n - 1} \right)$ from Eq. 35, which is the DFT of the vector $\left( a_{0},a_{1},\ldots,a_{n - 1} \right)$. In this way, the DFT arises from a formula for computing the eigenvalues of any circulant matrix.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

One might ask what the conclusion would have been if the eigenvectors of $S$ have been used instead of those of $S^{\ast}$. A repetition of the previous steps but now for the case of $S$ would yield that the eigenvalues of a circulant matrix $C_{a}$ are given by

<!-- chunk {"id": "body-0053", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

While the expressions Eq. 35 and Eq. 36 may at first appear different, the sets of numbers $\left\{ \lambda_{m} \right\}$ and $\left\{ \mu_{k} \right\}$ are actually equal. So in fact, the expression Eq. 36 gives the same set of eigenvalues as Eq. 35 but arranged in a different order since $\mu_{k} = \lambda_{- k}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Eigenvalues Calculation of a Circulant Matrix Yields the DFT", "weight": 1.0} -->

Along with the two choices of $S$ and $S^{\ast}$, there are also other possibilities. Let $p$ be any number that is coprime with $n$. It is easy to show (Exercise Section A.2) that a $n \times n$ matrix is circulant iff it commutes with $S^{p}$. In addition, the eigenvalues of $S^{p}$ are distinct (see Fig. 5). Therefore the eigenvectors of $S^{p}$ (rather than those of $S$) can be used to simultaneously diagonalize all circulant matrices. This would yield yet another transform distinct from the two transforms Eq. 35 or Eq. 36. However, the set of numbers produced from that transform will still be the same as those computed from the previous two transforms, but arranged in a different ordering.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

Let $C_{a}$ be a circulant matrix made from a vector $a$ as in Eq. 1. If we use the eigenvectors Eq. 33 of $S^{\ast}$ as columns of a matrix $W$, the $n$ eigenvalue/eigenvector relationships Eq. 34 ${C_{a}w^{(m)}} = {\lambda_{m}w^{(m)}}$ can be written as a single matrix equation as follows

<!-- chunk {"id": "body-0056", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

where we have used the fact Eq. 35 that the eigenvalues of $C_{a}$ are precisely $\left\{ {\hat{a}}_{m} \right\}$, the elements of the DFT of the vector $a$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

It is easy to verify that the columns of $W$ are mutually orthogonal^22^2 This also follows from the fact that the columns of $W$ are the eigenvectors of $S^{\ast}$, and since $S^{\ast}$ is a normal matrix, it has mutually orthogonal eigenvectors., and thus $W$ is a unitary matrix (up to a rescaling) ${W^{\ast}W} = {WW^{\ast}} = {nI}$, or equivalently $W^{- 1} = {\frac{1}{n}W^{\ast}}$. Since the matrix $W$ is made up of the eigenvectors of $S^{\ast}$, which in turn are made up of various powers of the roots of unity Eq. 33, it has some special structure which is worth examining

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

The matrix $W$ is symmetric, $W^{\ast}$ is thus the matrix $W$ with each entry replaced by its complex conjugate. Furthermore, since for each root of unity $\left( \rho^{k} \right)^{\ast} = \rho^{- k}$, we can therefore write

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

Also observe that multiplying a vector by $W^{\ast}$ is exactly taking its DFT. Indeed the $m$'th row of $W^{\ast}x$ is

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

which is exactly the definition Eq. 2 of the DFT. Similarly, multiplication by $\frac{1}{n}W$ is taking the inverse DFT

<!-- chunk {"id": "body-0061", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

Multiplying both sides of Eq. 37 from the right by $W^{- 1}$ gives the diagonalization of $C_{a}$ which can be written in several equivalent forms

<!-- chunk {"id": "body-0062", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

The diagonalization Eq. 38 can be interpreted as follows in terms of the action of a circulant matrix $C_{a}$ on any vector $x$

<!-- chunk {"id": "body-0063", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

Thus the action of $C_{a}$ on $x$, or equivalently the circular convolution of $a$ with $x$, can be performed by first taking the DFT of $x$, then multiplying the resulting vector component-wise by $\hat{a}$ (the DFT of the vector $a$ defining the matrix $C_{a}$), and then taking an inverse DFT. In other words, the diagonalization of a circulant matrix is equivalent to converting circular convolution to component-wise vector multiplication through the DFT. This is illustrated in Fig. 6.

<!-- chunk {"id": "body-0064", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

Note that in the literature there is an alternative form for the DFT and its inverse

<!-- chunk {"id": "body-0065", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

which is sometimes preferred due to its symmetry (and is also truly unitary since with this definition ${\| x\|}_{2} = {\|\hat{x}\|}_{2}$). This "unitary" DFT corresponds to the last diagonalization given in Eq. 38. We do not adopt this unitary DFT definition here since it complicates^33^3If the unitary DFT is adopted, the equivalent statement would be that the eigenvalues of $C_{a}$ are the elements of the entries of $\sqrt{n}\hat{a}$. the statement that the eigenvalues of $C_{a}$ are precisely the entries of $\hat{a}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The Big Picture", "weight": 1.0} -->

We summarize the algebraic aspects of the big picture in the following theorem.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Further Comments and Generalizations", "weight": 1.0} -->

We end by briefly sketching two different ways in which the procedures described in this tutorial can be generalized. The first is generalizations to families of mutually commuting infinite matrices and linear operators. These families are characterized by commuting with shifts of functions defined on "time-axes" which can be identified with groups or semi-groups. This yields the familiar Fourier transform, Fourier series, and the z-transform. A second line of generalization is to families of matrices that do not commute. In this case we can no longer demand simultaneous diagonalization, but rather simultaneous block diagonalization whenever possible. This is the subject of group representations, but we will only touch on the simplest of examples by way of illustration. The discussions in this section are meant to be brief sketches to motivate the interested reader into further exploration of the literature.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Fourier Transform, Fourier Series, and the z-Transform", "weight": 1.0} -->

First we recap what these classical transforms are. They are summarized in Table 1. In a Signals and Systems course, these concepts are usually introduced as transforms on temporal signals, so we will use that language to refer to the independent variable as time, although it can have any other interpretation. As is the theme of this tutorial, the starting point should not be the signal transform, but rather the systems, or operators, that act on them and their respective invariance properties. We now formalize these properties.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Fourier Transform, Fourier Series, and the z-Transform", "weight": 1.0} -->

The time axes are the integers $\mathbb{Z}$ for discrete time and the reals $\mathbb{R}$ for continuous time. Moreover, the discrete circle ${\mathbb{Z}}_{n}$ and the continuous circle $\mathbb{T}$ are the time axes for discrete and continuous-time periodic signals respectively. A common feature of the time axes $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{T}$ and ${\mathbb{Z}}_{n}$ is that they all are commutative groups. In fact, they are the basic commutative groups. All other (so-called locally compact) commutative groups are made up of group products of those basic four.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Fourier Transform, Fourier Series, and the z-Transform", "weight": 1.0} -->

which is the right shift (delay) of $f$ by $T$ time units. All that is needed to make sense of this operation is that for ${t,T} \in {\mathbb{G}}$, we have ${t - T} \in {\mathbb{G}}$, and that is guaranteed by the group structure for any of those four time sets. Now consider a linear operator $A:{{\mathbb{C}}^{\mathbb{G}}\longrightarrow{\mathbb{C}}^{\mathbb{G}}}$ acting on the vector space ${\mathbb{C}}^{\mathbb{G}}$ of all scalar-valued functions on $\mathbb{G}$, which can be any of the four time sets. We call such an operator time invariant (or shift invariant) if it commutes with all possible time-shift operations Eq. 39, i.e.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Fourier Transform, Fourier Series, and the z-Transform", "weight": 1.0} -->

To conform with traditional terminology, we refer to such shift-invariant linear operators as Linear Time-Invariant (LTI) systems. They are normally described as differential or difference equations with a forcing term, or as convolutions of signals amongst other representations. However, only the shift-invariance property Eq. 40, and not the details of those representations, is what's important in discovering the appropriate transform that simultaneously diagonalizes such operators.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fourier Transform, Fourier Series, and the z-Transform", "weight": 1.0} -->

There are additional technicalities in generalizing the previous techniques to sets of linear operators on infinite dimensional spaces rather than matrices. The procedure however is very similar. We identify the class of operators to be analyzed. This involves a shift (time) invariance property, which then implies that they all mutually commute. The "eigenvectors" of the shift operators give the simultaneously diagonalizing transform. The complication here is that eigenvectors may not exists in the classical sense (they do in the case of Fourier series, but not in the other cases). In addition, diagonalization will not necessarily correspond to finding a new basis of the vector space. In both the Fourier and z-transforms, the number of "linearly independent eigenfunctions" is not even countable, so they can't be thought of as forming a basis. Fortunately, it is easy to circumvent these difficulties by generalizing the concept of diagonal matrices to multiplication operators. For linear operators on infinite-dimensional spaces, these play the same role as the diagonal matrices do on finite-dimensional spaces.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

The simplest example of a non-commutative group of transformations is the so-called symmetric group ${\mathbb{S}}_{3}$ of all permutations of ordered $3$-tuples. Consider the ordered $3$-tuple $$ and the following "circular shift" and "swap" operations on it

<!-- chunk {"id": "body-0074", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

where $I$ is the identity (no permutation) operation, and $s_{ij}$ is the operation of swapping the $i$ and $j$ elements. The group operation is the composition of permutations. Note that the first three permutations $\left\{ I,c,c^{2} \right\}$ are isomorphic to ${\mathbb{Z}}_{2}$ as a group and thus mutually commute. The swap and shift operations in general do not mutually commute. A little investigation shows that the six elements

<!-- chunk {"id": "body-0075", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

do indeed form the group of all permutations of a $3$-tuple.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

A representation of a group is an isomorphism between the group and a set of matrices (or linear operators) with the composition operation between them being standard matrix multiplication. With a slight abuse of notation (where we use the same symbol for the group element and its representer) we have the following representation of ${\mathbb{S}}_{3}$ as linear operators on ${\mathbb{R}}^{3}$ (i.e. as matrices on $3$-vectors)

<!-- chunk {"id": "body-0077", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

Those matrices acting on a vector $\left( x_{0},x_{1},x_{2} \right)$ will permute the elements of that vector according to Eq. 41.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

Now we ask the question: can the set of matrices in ${\mathbb{S}}_{3}$ (identified as Eq. 42) be simultaneously diagonalized? Recall that commutativity is a necessary condition for simultaneous diagonalizability, and since this set is not commutative, the answer is no. The failure of commutativity can be seen from the following easily established relation between shifts and swaps

<!-- chunk {"id": "body-0079", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

(i.e. the arithmetic for $k + 1$ and $l + 1$ should be done in ${\mathbb{Z}}_{2}$).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

The lack of commutativity precludes simultaneous diagonalizability. However, it is possible to simultaneously block-diagonalize all elements of ${\mathbb{S}}_{3}$ so they all have the following block-diagonal form

<!-- chunk {"id": "body-0081", "role": "body", "section": "Simultaneous Block-Diagonalization and Group Representations", "weight": 1.0} -->

In some sense, this the simplest form one can hope for when analyzing all members of ${\mathbb{S}}_{3}$ (and the algebra generated by it). This block diagonalization does indeed reduce the complexity of analyzing a set of $3 \times 3$ matrices to analyzing sets of at most $2 \times 2$ matrices. While this might not seem significant at first, it can be immensely useful in certain cases. Imagine for example doing symbolic calculations with $3 \times 3$ matrices. This typically yields unwieldy formulas. A reduction to symbolic calculations for $2 \times 2$ matrices can give significant simplifications. Another case is when infinite-dimensional operators can be block diagonalized with finite-dimensional blocks. This is the case when one uses Spherical Harmonics to represent rotationally invariant differential operators. In that case the representation has finite-dimensional blocks, though with increasing size.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Block Diagonalization and Invariant Subspaces", "weight": 1.0} -->

Let's first examine how block diagonalization can be interpreted geometrically. Given an operator $A:{\mathcal{V}\longrightarrow\mathcal{V}}$ on a vector space, we say that a subspace $\mathcal{V}_{o} \subseteq \mathcal{V}$ is $A$-invariant if ${A\mathcal{V}_{o}} \subseteq \mathcal{V}_{o}$ (i.e. for any $v \in \mathcal{V}_{o}$, ${Av} \in \mathcal{V}_{o}$). Note that the span of any eigenvector of $A$ (the so-called eigenspace) is an invariant subspace of dimension 1. Finding invariant subspaces is equivalent to block triangularization.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Block Diagonalization and Invariant Subspaces", "weight": 1.0} -->

Note that in general, the complement subspace will not be $A$-invariant. If it were, then $A_{12} = 0$ above, and that form of $A$ would be block diagonal. Thus block diagonalization amounts to finding an $A$-invariant subspace $\mathcal{V}_{o}$, as well as a complement $\mathcal{V}_{1}$ of it such that $\mathcal{V}_{1}$ is also $A$-invariant.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Block Diagonalization and Invariant Subspaces", "weight": 1.0} -->

Now observe the following facts which are immediately obvious (at least for matrices) from the the form Eq. 44. If $A$ is invertible, then $\mathcal{V}_{o}$ is also $A^{- 1}$-invariant since the inverse of an upper-block-triangular matrix is also upper-block-triangular. If we choose $\mathcal{V}_{1} = \mathcal{V}_{o}^{\perp}$, the orthogonal complement of $\mathcal{V}_{o}$, then $\mathcal{V}_{o}$ is $A$-invariant iff $\mathcal{V}_{o}^{\perp}$ is $A^{\ast}$-invariant (this can be seen from Eq. 44 by observing that $A^{\ast}$ is block-lower-triangular).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Block Diagonalization and Invariant Subspaces", "weight": 1.0} -->

Finally, in the special case that $A$ is unitary (i.e. ${AA^{\ast}} = {A^{\ast}A} = I$, and therefore $A^{- 1} = A^{\ast}$), it follows from the previous two observations that for a unitary $A$, any $A$-invariant subspace $\mathcal{V}_{o}$ is such that its orthogonal complement $\mathcal{V}_{o}^{\perp}$ is automatically $A$-invariant. Therefore, for unitary matrices, block triangularization is equivalent to block diagonalization, which can be done by finding invariant subspaces and their orthogonal complements.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

Now we return to the matrices of ${\mathbb{S}}_{3}$ Eq. 43 and show how they can be simultaneously block diagonalized. Note that all the matrices are unitary, and therefore once all the common invariant subspaces are found, they are guaranteed to be mutually orthogonal. The easiest one to find is the vector $$. Note that it is an eigenvector of all members of ${\mathbb{S}}_{3}$ with eigenvalue $1$ (since obviously any permutation of the elements of this vector produce the same vector again). This is an eigenspace of dimension $1$. There is not another shared eigenspace of dimension $1$ since then we would have simultaneous diagonalizability, and we know that is precluded by the lack of commutativity. We thus have to simply find the 2-dimensional orthogonal complement of the span of $$. There are several choices for its basis. One of them is as follows

<!-- chunk {"id": "body-0087", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

Notice that the vectors $\{ v_{i}\}$ are mutually orthogonal, which simplifies calculations that finally give the elements of ${\mathbb{S}}_{3}$ in this new basis as

<!-- chunk {"id": "body-0088", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

which are all indeed of the form Eq. 43.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

It is more common in the literature to perform the above analysis in the language of group representations, specifically as decomposing a given representation into its component irreducible representations. Block diagonalization is then an observation about the matrix form that the representation takes after that decomposition. For the student proficient in linear algebra, but perhaps not as familiar with group theory, a more natural motivation is to start as done above from the block-diagonalization problem as the goal, and then use group representations as a tool to arrive at that goal.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

What has been done above can be restated using group representations as follows. A representation of a group $\mathbb{G}$ is a group homomorphism $\rho:{{\mathbb{G}}\longrightarrow{{GL}{(V)}}}$ into the group ${GL}{(V)}$ of invertible linear transformations of a vector space $V$. Assume for simplicity that $\mathbb{G}$ is finite, $\rho$ is injective, $V$ is finite dimensional, and that all transformations $\rho{({\mathbb{G}})}$ are unitary. The matrices Eq. 42 of ${\mathbb{S}}_{3}$ are in fact the images of an injective, unitary homomorphism $\rho:{{\mathbb{S}}_{3}\longrightarrow{{GL}{}}}$ into the group of all non-singular transformations of ${\mathbb{R}}^{3}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

A representation is said to be irreducible if there are no non-trivial invariant subspaces common to all transformations $\rho{({\mathbb{G}})}$. In other words, all elements of $\rho{({\mathbb{G}})}$ cannot be simultaneously block diagonalized. As we demonstrated, Eq. 42 is indeed reducible. More formally, let $\rho_{i}:{{\mathbb{G}}\longrightarrow{{GL}{(V_{i})}}}$, $i = {1,2}$ be two given representations. Their direct sum ${\rho_{1} \oplus \rho_{2}}:{{\mathbb{G}}\longrightarrow{{GL}{({V_{1} \oplus V_{2}})}}}$ is the representation formed by the "block diagonal" operator

<!-- chunk {"id": "body-0092", "role": "body", "section": "Block Diagonalization of ${\\mathbb{S}}_{3}$", "weight": 1.0} -->

with the obvious generalization to more than two representations. If a representation is reducible, then the existence of a common invariant subspace means that it can be written as the direct sum of so-called "subrepresentations" as in Eq. 46. Thus simultaneous block-diagonalization into the smallest dimension blocks is equivalent to the decomposition of a given representation into the direct sum of irreducible representations. This is what we have done for the representation Eq. 42 of ${\mathbb{S}}_{3}$ by finding the two common invariant subspaces (which contain no proper further subspaces that are invariant) and thus brining all of them into the block diagonal form Eq. 45. In general, it is a fact that any representation of a finite group (more generally, of a compact group) can be decomposed as the direct sum of irreducible representations.
