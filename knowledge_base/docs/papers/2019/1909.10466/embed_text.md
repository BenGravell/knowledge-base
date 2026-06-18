## Introduction

The analysis of time-dependent phenomena is at the heart of investigation in a broad range of scientific research. Within these studies, the integration of data in the form of time-series has increased considerably. Therefore, the application of innovative algorithms is necessary to gain deep insights into the characteristics of data. In this paper, we address time-series analysis by Dynamic Mode Decomposition (DMD), which was first introduced by Schmid and Sesterhenn in 2008.

DMD is a data-driven and model-free algorithm extracting spatio-temporal patterns in the form of so-called DMD modes and DMD eigenvalues. As an efficient tool in fluid mechanics, DMD has gained much attention. DMD has been investigated on both practical and theoretical grounds. Nonetheless, the focus of these analyses was mainly a practical one. For example, various types of flow were considered, such as airflow around an airfoil, fuel flow in a combustion chamber, or heat conduction in various cases. Completely different fields of application comprise financial trading, video processing, epidemiology, neuroscience, and control theory.

In contrast, we focus on theoretical investigations. The paper is thus structured as follows: After discussing related work, we introduce the theoretical framework of DMD dealing with the background mechanisms. In this process, we define the so-called system matrix, which is pioneering for DMD and prove the following results: a characterization for the exactness and diagonalizability of the system matrix as well as the resulting reconstruction of data with its spectral components. These theorems are central for the following sections introducing the three common variants of DMD: The original formulation, the modification by a singular value decomposition, and Exact-Dynamic Mode Decomposition. In this context, a systematic advancement will be presented that clarifies precisely the interrelation of these algorithms. This especially includes algebraic identities as well as spectral-theoretic results leading, e.g., to a new approach for the extension to the most recent variant of DMD. In addition, the exact reconstruction property of DMD will be proven for each DMD variant that guarantees an error-free reconstruction of the data. To this end, a new variant of scaling factors is introduced involving a new concept of an error scaling for the reconstruction of the first snapshot. Some concluding remarks will be given in the last section.

## Related Work

Rowley et al. provided a first theoretical investigation for the fundamental version of DMD, here denoted as Companion Dynamic Mode Decomposition (CDMD). They dealt with the reconstruction property of CDMD, however, they did not take appropriate scaling factors into account. An algorithmic improvement through the singular value decomposition was achieved by Schmid resulting in another variant of DMD. We refer to this algorithm as Singular Value Decomposition Dynamic Mode Decomposition (SDMD). The reconstruction property of SDMD was mentioned by Chen et al. as well as further properties of CDMD. Tu et al. introduced the advancement of SDMD to Exact-Dynamic Mode Decomposition (EXDMD), which is the most recent version of DMD. They prove basic algebraic identities and show primarily spectral-theoretic connections between these two algorithms. We generalize and extend all results or derive them as a corollary. In addition, we present a new approach for the extension of SDMD to EXDMD characterizing precisely the connection between these two algorithms. Despite these theoretical investigations, the problem of an exact reconstruction is left open. However, Jovanovic et al. as well as Drmač et al. discussed efficient techniques for finding appropriate coefficients by solving certain (convex) minimization problems. We introduce a new variant of scaling factors that lead to an error-free reconstruction of the snapshots under appropriate conditions.

## Theoretical Framework

This section is dedicated to the basic theoretical background of DMD. In this context, the general setting will be presented as well as an intuitive interpretation of the principles of DMD. These are crucial for the precise understanding of DMD, forming the basis for the subsequent sections. In addition, basic notation will be formalized and consistently used in this paper.

The application of DMD starts with the availability of data that may stem either from empirical experiments or numerical simulations alike. The objective of DMD is to extract spatio-temporal patterns out of the data in the form of DMD modes, eigenvalues,and amplitudes. As the modes are related to spatial structures, the corresponding eigenvalues determine the temporal behavior of these. The amplitudes characterize the impact of individual modes on the whole system, i.e. the dominance structure.

Now, consider data (snapshots) ${x_{0},x_{1},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with the following two quantities:

In the application areas of DMD such as fluid dynamics or non-linear dynamics, the connection between these variables is typically given by $n \gg m$, which means that the size of the data points is considerable larger than the number of snapshots. In this context, typical values are $n \approx 10^{6}$--$10^{12}$ (depending on whether we address 2D or 3D scenarios) and $m \approx 100$--$1000$. This basic setting is crucial for understanding the principles of DMD and will be assumed in the following derivation. However, DMD can also be mathematically formulated and applied without this assumption, as we will see later.

In short, DMD calculates the relevant dynamic information of a high-dimensional linear operator that connects the given data points $x_{0},x_{1},\ldots,x_{m}$ in a least square sense, without explicitly computing it. This is achieved by an eigenvalue decomposition of a low-dimensional representation. The corresponding eigenvectors will be embedded as DMD modes into the high-dimensional space endowed with appropriate scaling factors, the DMD amplitudes.

In order to obtain the high-dimensional matrix $A \in {\mathbb{C}}^{n \times n}$ connecting the data points, we consider the following (least-squares) minimization problem:

Note that the high dimensionality stems from the fact $n \gg m$. An explicit solution of $A$ is necessary to formulate an algorithmic approach. To this end, we rewrite the data into the matrices

obtaining the following equivalent minimization problem:

where ${\parallel \cdot \parallel}_{F}$ denotes the Frobenius norm of a matrix. An explicit solution is now given by

where $X^{+}$ denotes the Moore-Penrose pseudoinverse of $X$. Since the pseudoinverse always exists, the solution $A$ can be used for an algorithmic formulation.

Now, assuming the diagonalizability of the matrix $A$, i.e., $A = {V\LambdaV^{- 1}}$ with the matrices $\Lambda = {\text{diag}{(\lambda_{1},\ldots,\lambda_{n})}}$ and $V = \begin{bmatrix}
\end{bmatrix}$ containing the eigenvalues and eigenvectors respectively, we obtain the characteristic reconstruction property of the matrix $A$ by

for $k = {0,1,\ldots,m}$, where $b = {(b_{1},\ldots,b_{n})}^{T}$ are the coefficients of the linear combination of $x_{0}$ in the eigenvector basis, i.e. $b = {V^{- 1}x_{0}}$. Since the rank of $A$ is at most $\min{\{{\text{rank}{(X)}},{\text{rank}{(Y)}}\}}$ and consequently not more than $m$, there are at least $n - m$ eigenvalues of $A$ that are equal to zero. The dynamic behavior will be thus captured by at most $m$ components, which are considerable fewer components. Consequently, we obtain the following reconstruction of the data:

for $k = {1,\ldots,m}$, where $q_{0}$ is the resulting error arising from the missing $m - n$ components. In sum, we gain a reasonable low-dimensional decomposition of the data into the triples ${(\lambda_{j},v_{j},b_{j})} \in {{\mathbb{C}} \times {\mathbb{C}}^{n} \times {\mathbb{C}}}$, providing an instrument for diagnostic approaches as well as a tool for prediction, long-term analysis, and stability analysis.

The different versions of DMD presented in the subsequent sections are based on various techniques to produce a low-dimensional representation of the matrix $A$ in order to (approximately) compute its eigenvalues and eigenvectors as well as new appropriate scaling factors. These procedures yield similar triples that will be denoted by ${(\lambda_{j},\vartheta_{j},a_{j})} \in {{\mathbb{C}} \times {\mathbb{C}}^{n} \times {\mathbb{C}}}$ throughout the paper. These triples consist of the so-called DMD eigenvalues, DMD modes, and DMD amplitudes corresponding to a particular algorithm (see each section).

Before studying the variants of DMD, we first concentrate on an analysis of the high-dimensional structures involving the matrix $A$. Through a deeper understanding of the matrix $A$ representing the starting point of DMD, we obtain insights into the desired action of DMD. In particular, the success of an error-free reconstruction of DMD depends on the following two aspects:

The exactness of the matrix $A$, i.e., ${AX} = Y$.

The diagonalizability of the matrix $A$.

These two aspects will be examined throughout this section, however, before, the matrix $A$ will be captured in the following definition.

### Definition 3.1

For data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with associated matrices $X = \begin{bmatrix}
\end{bmatrix}$ and $Y = \begin{bmatrix}
\end{bmatrix}$, we call the matrix $A = {YX^{+}} \in {\mathbb{C}}^{n \times n}$ the system matrix to the data $x_{0},\ldots,x_{m}$.

First, we recall some well-known facts. The definition is well-defined, as the pseudoinverse always exists and is unique. Furthermore, the system matrix is the unique solution to the the minimization problem $\min_{A \in {\mathbb{C}}^{n \times n}}{\parallel AX - Y\parallel}_{F}^{2}$, if the rows of the matrix $X$ are linearly independent (or equivalently, if the matrix $X$ is surjective).

An important condition is the exactness of the system matrix, i.e., the equality ${AX} = Y$ or equivalently ${Ax_{j}} = x_{j + 1}$ for $j = {0,\ldots,{m - 1}}$. The following proposition characterizes this property on linear functionals.

### Proposition 3.2

Let the system matrix $A$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ as well as an arbitrary vector $w \in {\mathbb{C}}^{n}$. Then the following statements are equivalent:

${\text{ker}{(X)}} \subseteq {\text{ker}{({w^{\ast}Y})}}$, i.e., ${Xz} = 0\Longrightarrow{w^{\ast}Yz} = 0$ for all $z \in {\mathbb{C}}^{n}$.

The system matrix is exact on $w$, i.e. ${w^{\ast}AX} = {w^{\ast}Y}$.

### Proof

"${(i)}\Longrightarrow{({ii})}$". Consider the following equation

where $P_{X^{\ast}}$ is the orthogonal projection onto the image of $X^{\ast}$. Therefore $I - P_{X^{\ast}}$ is the orthogonal projection onto the kernel of $X$ and consequently the assertion follows by the assumption ${\text{ker}{(X)}} \subseteq {\text{ker}{({w^{\ast}Y})}}$.

"${({ii})}\Longrightarrow{(i)}$". Let $z \in {\text{ker}{(X)}}$, i.e., ${Xz} = 0$. This implies ${w^{\ast}AXz} = 0$, which is by assumption equivalent to ${w^{\ast}Yz} = 0$. Hence $z \in {\text{ker}{({w^{\ast}Y})}}$. ~□~

A simple consequence of this proposition is the following corollary \[10, Theorem 2\].

### Corollary 3.3

Let the system matrix $A$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then the following assertions are equivalent:

${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$.

The system matrix is exact, i.e. ${AX} = Y$.

In the case of linear independent data points $x_{0},\ldots,x_{m - 1}$, the system matrix is exact, since ${\text{ker}{(X)}} = {\{ 0\}}$ and hence condition $(i)$ of Corollary 3.3 is trivially satisfied. In this context, the condition $n \gg m$ (which is typical for the application areas of DMD) suggests the linear independence of the data. Consequently, the first aspect (exactness of the system matrix) is characterized. For a full reconstruction of the data, however, we still need the diagonalizability of the system matrix. To this end, we examine the inner structure of the system matrix, i.e., its kernel and image.

### Lemma 3.4

Let the system matrix $A$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$, where $x_{0},\ldots,x_{m - 1}$ and $x_{1},\ldots,x_{m}$ are linear independent, respectively. Then the dimension of the image and the kernel of $A$ is given by

### Proof

For the first assertion, we use the following rank inequality:

which implies ${\text{rank}{(A)}} = m$ or equivalently ${\text{dim}\text{im}{(A)}} = m$. Consequently, we obtain that ${\text{dim}\text{ker}{(A)}} = {n - {\text{dim}\text{im}{(A)}}} = {n - m}$. ~□~

### Corollary 3.5

Let the system matrix $A$ to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ be given, where $x_{0},\ldots,x_{m - 1}$ and $x_{1},\ldots,x_{m}$ are linear independent, respectively. If $A$ has $m$ non-zero distinct eigenvalues, then it is diagonalizable.

Regarding the reconstruction property of the system matrix, the final result will be stated in the following theorem, which deals with both sufficient and necessary conditions. For a simple notational handling of the proof, we define the Vandermonde matrix.

### Definition 3.6

For ${\lambda_{1},\ldots,\lambda_{m}} \in {\mathbb{C}}$ we define the $k$-$K$-Vandermonde matrix by

with ${\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}} = {\text{Vand}{(\lambda_{1},\ldots,\lambda_{m};1,m)}}$ for the usual Vandermonde matrix.

### Theorem 3.7 (Reconstruction-property system matrix)

Let the system matrix $A$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then the two following assertions are equivalent:

The system matrix $A$ has the following properties:

${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$.

$A$ is diagonalizable, where the non-zero eigenvalues are distinct.

There are distinct numbers ${0 \neq {\lambda_{1},\ldots}},{\lambda_{r_{1}} \in {\mathbb{C}}}$, coefficients ${0 \neq {b_{1},\ldots}},{b_{r_{2}} \in {\mathbb{C}}}$ and linearly independent vectors $v_{1},\ldots,v_{r_{2}}$ with $r_{1} \leq r_{2} \leq n$ and $r_{1} \leq m$ such that the following identities hold for $k = {1,\ldots,m}$:

In this case, the non-zero distinct numbers $\lambda_{1},\ldots,\lambda_{r_{1}}$ are the eigenvalues of the system matrix and the related (scaled) vectors $v_{1},\ldots,v_{r_{1}}$ are the corresponding eigenvectors. The remaining vectors $v_{r_{1} + 1},\ldots,v_{r_{2}}$ are eigenvectors of the system matrix to the eigenvalue zero.

### Proof

"${(i)}\Longrightarrow{({ii})}$". By condition $c)$, the system matrix has at most $r_{1}$ non-zero eigenvalues, because ${\text{rank}{(A)}} \leq {\min{\{{\text{rank}{(X^{+})}},{\text{rank}{(Y)}}\}}} \leq r_{1}$. As the system matrix is diagonalizable by assumption $b)$, there exist non-zero distinct eigenvalues $\lambda_{1},\ldots,\lambda_{r}$ with $r \leq r_{1}$ and zero eigenvalues $\lambda_{r + 1},\ldots,\lambda_{n}$ with corresponding eigenvectors $v_{1},\ldots,v_{r},v_{r + 1},\ldots,v_{n}$. Rewriting into matrices leads to ${W^{- 1}AW} = \Lambda$ for $W = \begin{bmatrix}
\end{bmatrix}$ and $\Lambda = {\text{diag}{(\lambda_{1},\ldots,\lambda_{n})}}$. By Corollary 3.3, the first assumption $a)$ is equivalent to ${AX} = Y$, which implies the identity

for $k = {0,1,\ldots,m}$, where $b = {(b_{1},\ldots,b_{n})}^{T}$ contains the coefficients of the linear combination of $x_{0}$ in the eigenvector basis, i.e., $b = {W^{- 1}x_{0}}$. Some of the coefficients $b_{j}$ may be zero, such that we obtain, after reordering, the identity

for $k = {1,\ldots,m}$ and ${b_{1},\ldots,b_{\overset{\sim}{r}}} \neq 0$ with $\overset{\sim}{r} \leq r \leq r_{1}$. Since the rank of $Y$ is $r_{1}$ by condition $c)$, the data points $x_{1},\ldots,x_{m}$ span an $r_{1}$-dimensional vector subspace. As the vectors $v_{1},\ldots,v_{\overset{\sim}{r}}$ are linearly independent, the sum have to has at least $r_{1}$ terms. Hence, $\overset{\sim}{r} = r = r_{1}$ and ${b_{1},\ldots,b_{r_{1}}} \neq 0$ as well as ${\lambda_{1},\ldots,\lambda_{r_{1}}} \neq 0$. Finally, the first data point can be expressed by the remaining non-zero coefficients $b_{1},\ldots,b_{r_{1}},b_{r_{1} + 1},\ldots,b_{r_{2}}$ through

"${({ii})}\Longrightarrow{(i)}$". First, we define the following matrices

Now, we can rewrite the data matrices $X$ and $Y$ with the above introduced notation by

Consider the linear operator $A_{\ast} = {W_{r_{1}}\Lambda_{r_{1} \times r_{2}}W_{r_{2}}^{+}} \in {\mathbb{C}}^{n \times n}$. This operator exactly connects the data, since

As a result, the system matrix $A = {YX^{+}}$ is exact, too, because it minimizes the problem ${\parallel{{AX} - Y}\parallel}_{F}$, i.e., ${AX} = Y$. By Corollary 3.3, the first assertion ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$ is proven.

The second claim, ${\text{rank}{(Y)}} = r_{1}$, follows from the application of simple rank inequalities onto $Y = {W_{r_{1}}K_{r_{1}}\Lambda_{r_{1}}M_{r_{1}}}$ together with the conditions in $({ii})$.

As a consequence, we have ${\text{rank}{(A)}} \leq r_{1}$, which implies that $A$ has at most $r_{1}$ non-zero eigenvalues. Now, if we prove that $\lambda_{1},\ldots,\lambda_{r_{1}}$ are these eigenvalues, then the proof is complete, since this implies the diagonalizability of the system matrix with distinct non-zero eigenvalues (Corollary 3.5). More precisely, we have to show that

Note that the column vectors of $W_{r_{1}}K_{r_{1}}$ (representing the eigenvectors) are already non-zero by assumption. To prove the equality we consider two cases:

1\. case: $r_{1} < m$. Defining the matrix ${\overset{\sim}{M}}_{r_{1}} = {\text{Vand}{(\lambda_{1},\ldots,\lambda_{r_{1}};2,m)}} \in {\mathbb{C}}^{{r_{1} \times m} - 1}$ (i.e., without the first column), then we obtain by the exactness of the system matrix

Since the eigenvalues are distinct and $r_{1} < m$, the matrix ${\overset{\sim}{M}}_{r_{1}}$ has a right inverse (which is given by the pseudoinverse), hence, we arrive at the desired assertion.

2\. case: $r_{1} = m$. From ${\text{rank}{(Y)}} = m$ follows ${\text{ker}{(Y)}} = {\{ 0\}}$ and, consequently, ${\text{ker}{(X)}} = {\{ 0\}}$ by the already proven condition $a)$. Hence, ${\text{rank}{(X)}} = m$, too and by Lemma 3.4, the system matrix has ${\text{rank}{(A)}} = m$ and ${\text{dim}\text{ker}{(A)}} = {n - m}$. As the second identity geometrically implies ${\text{im}{(Y)}} \subseteq {\langle v_{1},\ldots,v_{m}\rangle}$, we obtain the following relationship

Since ${\text{rank}{(A)}} = m$ and $v_{1},\ldots,v_{m}$ are linearly independent, it follows ${\text{im}{(A)}} = {\langle v_{1},\ldots,v_{m}\rangle}$. Consequently, the remaining linearly independent vectors $v_{m + 1},\ldots,v_{r_{2}}$ belong to the kernel of the system matrix $A$. Rewriting the matrix $X$ into $X = {{W_{r_{1}}K_{r_{1}}M_{r_{1}}} + {qe_{1}^{T}}}$ with $q = {\sum_{j = {m + 1}}^{r_{2}}{b_{j}v_{j}}}$ with the first standard basis vector $e_{1}$, we obtain

because $q \in {\text{ker}{(A)}}$. Multiplying this equation by $M_{r_{1}}^{+}$ from the right side, we obtain the desired algebraic identity, since $M_{r_{1}}^{+}$ is a right inverse. ~□~

## Companion Dynamic Mode Decomposition (CDMD)

In 2008, Schmid and Sesterhenn presented the first version of DMD. This variant will be referred to as Companion Dynamic Mode Decomposition (CDMD). CDMD has been investigated by experimental and numerical data by Schmid. The first approaches of a theoretic analysis were performed by Rowley et al.. Before we discuss the derivation of CDMD, the companion matrix will be defined, which is eponymous for this variant of DMD.

### Definition 4.1

For a vector $c = {(c_{0},\ldots,c_{m - 1})}^{T} \in {\mathbb{C}}^{m}$, we define the matrix $C_{c} \in {\mathbb{C}}^{m \times m}$ of the form

as the companion matrix to the vector $c$.

For the derivation of CDMD, we consider a given data set ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Again, we rewrite the data points into the matrices $X = \begin{bmatrix}
\end{bmatrix}$ and $Y = \begin{bmatrix}
\end{bmatrix}$. Now, instead of using the system matrix $A$, which connects the matrices $X$ and $Y$ (from the left), i.e., ${AX} \approx Y$, another approach is to look for a right-hand multiplied matrix $C \in {\mathbb{C}}^{m \times m}$ such that $Y \approx {XC}$. By construction, we can choose $C$ as a companion matrix $C_{c}$ and, hence, the problem reduces to find a vector $c$ such that

with a minimal error $q \in {\mathbb{C}}^{n}$, where $e_{m}$ represent the last standard basis vector. Under the assumption $n \gg m$, the companion matrix $C_{c} \in {\mathbb{C}}^{m \times m}$ is substantially lower dimensional than the system matrix $A \in {\mathbb{C}}^{n \times n}$. In addition, with decreasing error $q$ the companion matrix approximates the spectral-theoretic properties of $A$. In fact, for an eigenvector $v$ of $C_{c}$ to the eigenvalue $\lambda$ the transformed eigenvector $\vartheta = {Xv}$ satisfies

In sum, the computation of $C_{c}$ is reduced to the calculation of the associated vector $c = {(c_{0},\ldots,c_{m - 1})}^{T}$. This vector minimizes the error $q = {x_{m} - {Xc}}$ and hence only need to solve the following minimization problem

which will be solved by $c = {X^{+}x_{m}}$. Consequently, we can formulate CDMD as an algorithm, however, before, we define the companion matrix to a given data set.

### Definition 4.2

For data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with associated matrix $X = \begin{bmatrix}
\end{bmatrix}$, we call the companion matrix $C_{c}$ to the vector $c = {X^{+}x_{m}} \in {\mathbb{C}}^{m}$ the companion matrix to the data $x_{0},\ldots,x_{m}$.

### Algorithm 4.3 (Companion Dynamic Mode Decomposition (CDMD))

Input: Data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$.\
Output: DMD eigenvalues ${\lambda_{1},\ldots,\lambda_{m}} \in {\mathbb{C}}$, DMD modes ${\vartheta_{1},\ldots,\vartheta_{m}} \in {\mathbb{C}}^{n}$, and DMD amplitudes ${a_{1},\ldots,a_{m}} \in {\mathbb{C}}$.

Define the matrices ${X:=\begin{bmatrix}
\end{bmatrix}},{Y:=\begin{bmatrix}
\end{bmatrix} \in {\mathbb{C}}^{n \times m}}$.

Compute the $c = {X^{+}x_{m}} \in {\mathbb{C}}^{m}$.

Construct the companion matrix $C_{c} \in {\mathbb{C}}^{m \times m}$ to the vector $c$.

Compute the DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and eigenvectors $W^{- 1} = \begin{bmatrix}
\end{bmatrix}$ of $C_{c}$ to the vector $c$.

Calculate DMD modes $\Theta = \begin{bmatrix}
\vartheta_{1} & \ldots & \vartheta_{m}
\end{bmatrix} = {XW^{- 1}} \in {\mathbb{C}}^{n \times m}$.

Compute the DMD amplitudes by $K = {\text{diag}{(a_{1},\ldots,a_{m})}} = {({\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}W^{- 1}})}^{+}$.

The algorithm described here differs from the standard literature as we introduce the necessary concept of DMD amplitudes. Note, that the matrix $K$ in step $6$, which defines the DMD amplitudes, may not be diagonal. However, if the eigenvalues are distinct, then $K$ is a diagonal matrix, as we will observe later. The current definition of the DMD amplitudes seems to be obscure and not very intuitive. Later on, we will show that these DMD amplitudes are the right scaling factors for an exact reconstruction. In addition, we will prove that this choice equals ${(a_{1},\ldots,a_{m})}^{T} = {\Theta^{+}x_{0}}$ under some further assumption.

For a theoretical investigation, we need a more compact representation of the companion matrix $C_{c}$ from Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"). To this end, consider the following minimization problem

which is closely related to the construction of the companion matrix. An explicit solution of the minimization problem is given by $C = {X^{+}Y} \in {\mathbb{C}}^{m \times m}$. This matrix will be captured in the following definition.

### Definition 4.4

For data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with associated matrices $X = \begin{bmatrix}
\end{bmatrix}$ and $Y = \begin{bmatrix}
\end{bmatrix}$, we call the matrix $C = {X^{+}Y} \in {\mathbb{C}}^{n \times n}$ the twisted system matrix to the data $x_{0},\ldots,x_{m}$.

### Remark 4.5

At first glance, the two approaches seems to be equivalent. However, note that the twisted system matrix $C$ and the companion matrix $C_{c}$ are not necessarily equal or similar. This fact can be observed by a rank truncation of the matrices $X$ and $Y$. In particular, the companion matrix $C_{c}$ has at least rank $m - 1$, because the first $m - 1$ columns are linearly independent. However, the rank of the matrix $C = {X^{+}Y}$ depends only on the matrices $X$ and $Y$ and therefore it may be less than $m - 1$, which implies a non-similarity in general.

The following lemma and corollary characterize the relations between the three objects $A,C$, and $C_{c}$.

### Lemma 4.6

Let the system matrix $A$, the twisted system matrix $C$, and the companion matrix $C_{c}$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ as well as the projections $P_{X} = {XX^{+}}$ and $P_{X^{\ast}} = {X^{+}X}$ onto ${\text{im}{(X)}} \subseteq {\mathbb{C}}^{n}$ and ${\text{im}{(X^{\ast})}} \subseteq {\mathbb{C}}^{m}$, respectively. Then the following assertions hold:

${P_{X^{\ast}}C_{c}P_{X^{\ast}}} = {CP_{X^{\ast}}} = {X^{+}AX}$.

### Proof

The identities are proven by simple algebraic manipulations. ~□~

A direct consequence of this lemma is that the twisted system matrix and the companion matrix are equal, if the first $m$ snapshots are linearly independent. In addition, in the case of $n \gg m$, it illustrates that the companion matrix $C_{c} \in {\mathbb{C}}^{m \times m}$ is a low-dimensional representation of the system matrix $A \in {\mathbb{C}}^{n \times n}$.

### Corollary 4.7

Let the system matrix $A$, the twisted system matrix $C$ and the companion matrix $C_{c}$ be given to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. If $x_{0},\ldots,x_{m - 1}$ are linearly independent, then the following assertions hold:

### Proof

Since $x_{0},\ldots,x_{m - 1}$ are linearly independent, the identity ${X^{+}X} = I$ holds, which implies the assertions by Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") ~□~

The property of a low-dimensional representation suggests that CDMD inherits the characteristic reconstruction of the system matrix. Indeed, the following theorem proves this fact using the new concept of DMD amplitudes from Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"). In the literature a similar theorem is known \[6, Theorem 1\] that does not account for amplitudes. Hence, the choice of the corresponding modes is not appropriate for the reconstruction as these are computed up to a scaling (since they stem from eigenvectors).

### Theorem 4.8 (Reconstruction-property of CDMD)

Let DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$, DMD amplitudes $a_{1},\ldots,a_{m}$, and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. If the DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ are distinct, then the following identities hold:

for $k = {0,\ldots,{m - 1}}$ and $q = {x_{m} - {Xc}}$.

### Proof

Since the eigenvalues are distinct, the companion matrix $C_{c}$ will be diagonalized by the Vandermonde matrix:

However, the eigenvectors $\begin{bmatrix}
\end{bmatrix} = {\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}^{- 1}}$ may not coincide with the eigenvectors $v_{1},\ldots,v_{m}$ of the companion matrix produced by Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"). As the eigenvalues are distinct, there exist scaling factors ${\alpha_{1},\ldots,\alpha_{m}} \in {\mathbb{C}}$ such that for $j = {1,\ldots,m}$:

For the eigenvectors $v_{1},\ldots,v_{m}$ and scaling factors $\alpha_{1},\ldots,\alpha_{m}$ we define the matrices $W^{- 1} = \begin{bmatrix}
\end{bmatrix}$ and $K = \text{diag}{(\alpha_{1},\ldots,\alpha_{m}}$), respectively. As a result, we get the following connection

Consequently, $K = {({\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}W^{- 1}})}^{- 1}$, which shows that $K$ equals the matrix in step $6$ of Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") consisting of the DMD amplitudes, i.e., $\alpha_{j} = a_{j}$ for $j = {1,\ldots,m}$. Multiplying the above equation by the matrix $X$, we obtain

By this notation the DMD modes $\Theta = \begin{bmatrix}
\vartheta_{1} & \ldots & \vartheta_{m}
\end{bmatrix}$ are given by $\Theta = {XW^{- 1}}$ and, therefore, the first assertions follows by rearranging the above equation to $X = {\ThetaK\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}}$. The second identity is a result of the following calculation

### Corollary 4.9

Let DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$, DMD amplitudes $a_{1},\ldots,a_{m}$, and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. If the DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ are distinct and $x_{0},\ldots,x_{m - 1}$ are linearly independent, then the DMD amplitudes $a = {(a_{1},\ldots,a_{m})}^{T}$ can be calculated by

### Proof

By Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain the relation $x_{0} = {\Thetaa}$, where $\Theta = \begin{bmatrix}
\vartheta_{1} & \ldots & \vartheta_{m}
\end{bmatrix} = {XW^{- 1}}$ with $W^{- 1} = \begin{bmatrix}
\end{bmatrix}$. Since the matrix $X$ and $W^{- 1}$ have full rank, the DMD modes will be linear independent and, consequently, there exist a left-inverse of $\Theta$, which is given by its pseudoinverse $\Theta^{+}$. Hence, $a = {\Theta^{+}x_{0}}$. ~□~

Even though, the method of CDMD is mathematically correct, a practical implementation leads to an ill-conditioned algorithm. The reason for this is the external computation of the vector $c$ (which define companion matrix $C_{c}$) that leads to unsatisfied approximation properties of the system matrix $A$. This problem can be tackled by using the robust singular value decomposition (SVD), and will be discussed in the next section.

## SVD-Dynamic Mode Decomposition (SDMD)

In 2010, the algorithm of DMD was modified radically by Schmid. He published a variant of DMD based on a reduced singular value decomposition. For this reason, we will denote this method by SVD-Dynamic Mode Decomposition (SDMD). The result was a robust and stable algorithm, which serves as a basis for the most modern version of DMD. We start this section by deducing this algorithm.

Let the system matrix $A$ to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ be given as well as the reduced singular value decomposition of $X$ with $r = {\text{rank}{(X)}}$ and $X = {U\SigmaV^{\ast}} \in {\mathbb{C}}^{n \times m}$, where $U \in {\mathbb{C}}^{n \times r}$, $V \in {\mathbb{C}}^{m \times r}$ and $\Sigma \in {\mathbb{R}}^{r \times r}$. Utilizing the transformation matrix $U$, we construct the low-dimensional representation $S$ of the system matrix $A$ by

For an explicit calculation of $S$, it is necessary to avoid the computation of the system matrix $A$. To this end, we calculate

Now, we compute the eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of the matrix $S$ and finally transform them by the matrix $U$ into

in order to obtain an approximation of the eigenvalues and eigenvectors of the system matrix:

Consequently, the algorithm can be formulated as follows.

### Algorithm 5.1

(SVD-Dynamic Mode Decomposition)\
Input: Data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$.\
Output: DMD eigenvalues ${\lambda_{1},\ldots,\lambda_{r}} \in {\mathbb{C}}$, DMD modes ${\vartheta_{1},\ldots,\vartheta_{r}} \in {\mathbb{C}}^{n}$, and DMD amplitudes ${a_{i},\ldots,a_{r}} \in {\mathbb{C}}$.

Define the matrices ${X:={(x_{0},\ldots,x_{m - 1})}},{Y:={(x_{1},\ldots,x_{m})} \in {\mathbb{C}}^{n \times m}}$.

Compute the reduced singular value decomposition $X = {U\SigmaV^{\ast}}$ with $r = {\text{rank}{(X)}}$.

Define the DMD matrix $S:={U^{\ast}YV\Sigma^{- 1}} \in {\mathbb{C}}^{r \times r}$.

Compute the DMD eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of $S$.

Calculate the DMD modes $\vartheta_{i} = {Uv_{i}} \in {\mathbb{C}}^{n}$ and define $\Theta = {(\vartheta_{1},\ldots,\vartheta_{r})} \in {\mathbb{C}}^{n \times r}$.

Compute the DMD amplitudes $a = {\Theta^{+}x_{0}} \in {\mathbb{C}}^{r}$ with $a = {(a_{1},\ldots,a_{r})}^{T}$.

In Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), the DMD amplitudes will be defined intuitively by a best-fit linear combination of the first snapshots $x_{0}$ in the modes selection (compare Corollary 4.9 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")). For a deeper understanding of SDMD, we first characterize the connection to CDMD, which will be examined in the following lemma.

### Lemma 5.2

Let the companion matrix $C_{c}$ and the DMD matrix $S$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then the following identity holds:

In particular, if $x_{0},\ldots,x_{m - 1}$ are linearly independent, then the matrices $C_{c}$ and $S$ are similar.

### Proof

By Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and the reduced singular value decomposition $X = {U\SigmaV^{\ast}}$, we obtain

### Corollary 5.3

Let the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ be given. If $x_{0},\ldots,x_{m - 1}$ are linearly independent, then CDMD and SDMD produce the same DMD eigenvalues.

The corollary suggests that the reconstruction property of CDMD from Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") will be also transferred onto SDMD. In the case of distinct DMD eigenvalues, the DMD modes associated to equal eigenvalues only differ by a scaling factor. Therefore, the DMD modes of SDMD have to be rescaled for an exact reconstruction. The following theorem shows the reconstruction property of SDMD, where the scaling factors are given by the DMD amplitudes.

### Theorem 5.4 (Reconstruction-property SDMD)

Let DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$, DMD amplitudes $a_{1},\ldots,a_{m}$, and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$, where $x_{0},\ldots,x_{m - 1}$ are linearly independent. If the DMD eigenvalues are distinct, then the following identities hold:

for $k = {0,\ldots,{m - 1}}$ and $q = {x_{m} - {Xc}}$ with $c = {X^{+}x_{m}}$.

### Proof

By the notation of the proof of Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Lemma 5.2 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") we obtain

where the matrix $W^{- 1}$ contains the eigenvectors of $S$. Consider a scaling matrix $K = {\text{diag}{(\alpha_{1},\ldots,\alpha_{m})}}$ that satisfies the equation

Since the scaling matrix $K$ adjusts eigenvectors (in the same one-dimensional eigenspace), the scaling factors are ${\alpha_{1},\ldots,\alpha_{m}} \neq 0$ and, therefore, the matrix $K$ is invertible. By multiplying the above equation with $U$ from the left, we obtain

where $\Theta = {UW^{- 1}}$ are the DMD modes (by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")). In sum, we obtain

which shows the first identity concerning the scalings $\alpha_{1},\ldots,\alpha_{m}$. The second statement follows analogously by

It misses to show that the scaling factors $\alpha_{i}$ are given by the DMD amplitudes $a_{i}$. Rewriting $\alpha = {(\alpha_{1},\ldots,\alpha_{m})}^{T}$ and using the identity ${X\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}^{- 1}e} = x_{0}$ (from Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")), we obtain:

### Remark 5.5

SDMD is characterized by the robust singular value decomposition and the reconstruction property. However, the spectral-theoretical connection of SDMD to the system matrix is not clear. Therefore, let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then the following equation hold:

We observe that the eigenvalue equation is correct up to the projection $P_{X} = {XX^{+}} = {UU^{\ast}}$ onto the image of $X$.

The following proposition presents characterizations for the equality of the eigenvector equation of Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction").

### Proposition 5.6

Let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. In addition, let the error $q = {x_{m} - {Xc}}$ with $c = {X^{+}x_{m}}$ be given. Then the following assertions are equivalent:

The DMD mode $\vartheta_{i}$ is an eigenvector of the system matrix $A$ to the eigenvalue $\lambda_{i}$.

${A\vartheta_{i}} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$.

${{\langle e_{m},{X^{+}\vartheta_{i}}\rangle} \cdot q} = 0$.

$x_{m} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$ or ${\langle e_{m},{V\Sigma^{- 1}v_{i}}\rangle} = 0$.

### Proof

Let the companion matrix $C_{c}$ to the data $x_{0},\ldots,x_{m}$ be given.

${({iii})}\Longrightarrow{({ii})}$ By Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") we obtain the equality

which implies ${A\vartheta_{i}} \in {\text{im}{(X)}}$, i.e. ${A\vartheta_{i}} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$.

"${({ii})}\Longrightarrow{(i)}$" Let ${A\vartheta_{i}} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$. Then the (algebraic) eigenvalue equation is trivially satisfied, since the projection $P_{X}$ can be ignored in the equation of Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"). Furthermore, since the columns of $U$ are orthogonal and $v_{i} \neq 0$, the vector $\vartheta_{i} = {Uv_{i}}$ is non-zero and, therefore, an eigenvector of $A$.

"${(i)}\Longrightarrow{({iii})}$" By the preliminary Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), and assumption (i), we obtain

"${({iii})}\Leftrightarrow{({iv})}$" We reformulate the conditions by

A trivial consequence of the above proposition is the following corollary, which was first proven by Tu et al..

### Corollary 5.7

Let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. If $x_{m} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$, then the DMD modes and DMD eigenvalues are eigenvectors and eigenvalues of the system matrix $A$, respectively.

The previous statement implies ${\sigma{(S)}} \subseteq {\sigma{(A)}}$. However, the other inclusion is also true for all non-zero eigenvalues of the system matrix $A$.

### Proposition 5.8

Let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then all non-zero eigenvalues $\lambda \neq 0$ of $A$ will be calculated by DMD, i.e., it holds

### Proof

For an arbitrary eigenvector $z$ of $A$ to the eigenvalue $\lambda \neq 0$, we obtain by defining the vector $v:={U^{\ast}z}$:

Assume $v = 0$. Then ${U^{\ast}z} = 0$ and we obtain

As $z \neq 0$, it follows $\lambda = 0$, which contradicts the assumptions. ~□~

Consequently, under appropriate assumptions of the data, we obtain the spectral-theoretic relation

However, the condition $x_{m} \in {\langle x_{0},\ldots,x_{m - 1}\rangle}$ in Corollary 5.7 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") is actually never satisfied in the case of $n \gg m$ and, hence, not practically applicable.

This raises the question, whether the DMD modes can be modified such that we obtain eigenvectors of the system matrix without any assumptions. A solution to this problem is presented in the next theorem, which is inspired by the assertion $({iii})$ in Proposition 5.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction").

### Theorem 5.9

Let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. In addition, let the error $q = {x_{m} - {Xc}}$ with $c = {X^{+}x_{m}}$ be given. For $\lambda_{i} \neq 0$

is an eigenvector of the system matrix $A$ to the eigenvalue $\lambda_{i}$.

### Proof

By Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain the eigenvalue equation by

Assume $\zeta = 0$. Then we obtain

Since $v_{i} \neq 0$, it follows $\lambda = 0$, which contradicts the assumption. ~□~

The previous proposition characterizes exactly the spectral-theoretic relation between the DMD matrix $S$ and the system matrix $A$. In fact, it holds ${{\sigma{(A)}} \smallsetminus {\{ 0\}}} \subseteq {\sigma{(S)}} \subseteq {\sigma{(A)}}$ (without any assumption) and thus

Consequently, the dynamic behavior of the system matrix $A$ will be completely captured by the low-dimensional DMD matrix $S$. However, the DMD modes have to be modified according to Theorem 5.9 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") in order to get eigenvectors of the system matrix. This motivates the formulation of a new variant of DMD with modified DMD modes and possibly new DMD amplitudes such that the reconstruction property is preserved. In particular, as Theorem 5.9 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") states, only the non-zero eigenvalues can be used. Nevertheless, these eigenvalues are sufficient to capture the temporal evolution and consequently no dynamical information is lost.

### Remark 5.10

For the formulation of an efficient algorithm, we need a more compact representation of the modified DMD modes $\zeta_{i}$, which arises directly from transformations of the eigenvectors of $S$. By Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we rearrange the modified DMD modes by

Defining the DMD modes in this way, we obtain the most modern version of DMD, called Exact-Dynamic Mode Decomposition (EXDMD). In the following section, we will introduce this variant of DMD.

## Exact-Dynamic Mode Decomposition (EXDMD)

In 2014, Tu et. al. presented the most modern version of DMD, called Exact-Dynamic Mode Decomposition (EXDMD). However, the algorithm presented here differs from the standard literature as we use a different definition of the DMD amplitudes. In addition, we introduce a novel relevant variable: The error scaling.

### Algorithm 6.1 (Exact-Dynamic Mode Decomposition)

Input: Data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$.\
Output: DMD eigenvalues ${\lambda_{1},\ldots,\lambda_{r_{0}}} \in {\mathbb{C}}$, DMD modes ${\vartheta_{1},\ldots,\vartheta_{r_{0}}} \in {\mathbb{C}}^{n}$, DMD amplitudes ${a_{1},\ldots,a_{r_{0}}} \in {\mathbb{C}}$, and the error scaling $a_{0}$.

Define the matrices ${X:={(x_{0},\ldots,x_{m - 1})}},{Y:={(x_{1},\ldots,x_{m})} \in {\mathbb{C}}^{n \times m}}$.

Compute the reduced singular value decomposition $X = {U\SigmaV^{\ast}}$ with $r = {\text{rank}{(X)}}$.

Define the DMD matrix $S:={U^{\ast}YV\Sigma^{- 1}} \in {\mathbb{C}}^{r \times r}$.

Compute the DMD eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of $S$.

Calculate the DMD modes $\vartheta_{i} = {\frac{1}{\lambda_{i}}YV\Sigma^{- 1}v_{i}} \in {\mathbb{C}}^{n}$ and define $\Theta = {{(\vartheta_{1},\ldots,\vartheta_{r_{0}})}{\mathbb{C}}^{n \times r_{0}}}$.

Compute the DMD amplitudes $a = {\Lambda^{- 1}\Theta^{+}x_{1}} \in {\mathbb{C}}^{r}$ with $a = {(a_{1},\ldots,a_{r_{0}})}^{T}$.

Calculate the error scaling $a_{0} = {- {\sum_{j = 1}^{r_{0}}{\frac{1}{\lambda_{j}}{\prod_{\begin{matrix}
\end{matrix}}^{r_{0}}\frac{1}{\lambda_{j} - \lambda_{k}}}}}} \in {\mathbb{C}}$, if it exists.

The introduction of the error scaling $a_{0}$ and the fundamental change of the definition of the DMD amplitude will be justified by the subsequent theorem, which proves the reconstruction property of EXDMD. The reconstruction property of EXDMD, however, differs from the previous ones of CDMD (see Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")) and SDMD (see Theorem 5.4. ‣ 5 SVD-Dynamic Mode Decomposition (SDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")). The reason for this is the spectral-theoretic relation of EXDMD to the system matrix, as we will examine in the proof.

### Lemma 6.2

Let data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with associated matrices $X = \begin{bmatrix}
\end{bmatrix}$ and $Y = \begin{bmatrix}
\end{bmatrix}$ be given. If ${ker{(X)}} \subseteq {ker{(Y)}}$ and ${\text{ker}{(X)}} \neq {\{ 0\}}$, then $x_{m} \in {\text{im}{(X)}}$. In particular, it holds ${\text{im}{(X)}} \subseteq {\text{im}{(Y)}}$.

### Proof

Since the kernel of $X$ is non-trivial, there exist a vector $v = {(v_{1},\ldots,v_{m})}^{T} \neq 0 \in {\mathbb{C}}^{m}$ with ${Xv} = 0$. Since ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$, we obtain ${Yv} = 0$.

1\. case: $v_{m} \neq 0$. Then the equation ${{v_{1}x_{1}} + {\ldotsv_{m}x_{m}}} = 0$ implies

and hence the assertion is proven.

2\. case: $v_{m} = 0$. Then we obtain

By assumption ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$, we obtain

If $v_{m - 1} \neq 0$, then we get a representation of $x_{m}$ analogous to the firstcase. Otherwise, we repeat this steps as long as an entry $v_{j} \neq 0$ appears. As $v$ is non-zero, there exists such an entry $v_{j_{0}} \neq 0$. ~□~

### Theorem 6.3 (Reconstruction property EXDMD)

Let DMD eigenvalues $\lambda_{1},\ldots,\lambda_{r}$, DMD amplitudes $a_{1},\ldots,a_{r}$, DMD modes $\vartheta_{1},\ldots,\vartheta_{r}$, and the error scaling $a_{0}$ be given by Algorithm 6.1. ‣ 6 Exact-Dynamic Mode Decomposition (EXDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. If ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$ and the DMD eigenvalues are distinct, then the following identities hold:

for $k = {1,\ldots,m}$ and a vector $q_{0}$ with

### Proof

By Theorem 5.9 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Remark 5.10 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain that the DMD eigenvalues $\lambda_{i}$ and modes $\vartheta_{i}$ are eigenvalues and eigenvectors of the system matrix $A$ for $i = {1,\ldots,m}$. Since ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$, we obtain the relation

In addition, the condition ${\text{im}{(A)}} \subseteq {\text{im}{(Y)}}$ implies ${\text{rank}{(A)}} \leq {\text{rank}{(Y)}}$ and consequently $r \leq {\text{rank}{(Y)}}$, because $A$ has $r$ non-zeros distinct eigenvalues. Hence, ${\text{rank}{(Y)}} = r$ and the system matrix $A$ is diagonalizable by $r$ non-zero distinct eigenvalues. Therefore, the assumptions of Theorem 3.7. ‣ 3 Theoretical Framework ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") are satisfied such that there exist scaling factors ${\alpha_{1},\ldots,\alpha_{r}} \in {\mathbb{C}}$ and an error $q_{0} \in {\mathbb{C}}^{n}$ such that

for $k = {1,\ldots,m}$. Using the notation of Theorem 3.7. ‣ 3 Theoretical Framework ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain the equation

where $K = {\text{diag}{(\alpha_{1},\ldots,\alpha_{m})}}$ is the scaling matrix. Since the DMD modes (which are eigenvectors of the system matrix) are related to distinct eigenvalues, they are linearly independent and, consequently, the following calculation

shows that the scaling factors $\alpha_{k}$ coincide with the DMD amplitude $a_{k}$. Hence, the two identities are proven. For the additional statement, we consider two cases:

1\. case: $r = m$. Consider $Y = {{XC_{c}} + {qe_{m}^{T}}}$ and rearrange this equation by using the inverse of $C_{c}$ (which exists since $r = m$):

By Lemma 5.2 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and relation $C_{c} = {{({\SigmaV^{\ast}})}S{({\SigmaV^{\ast}})}^{- 1}}$, we obtain the identity

and, therefore, it follows

Now, we examine the remaining term ${\langle e_{m},{C_{c}^{- 1}e_{1}}\rangle} \cdot q$. To this end, we represent the companion matrix $C_{c}$ by its eigenvectors and eigenvalues

The inverse of the transposed Vandermonde matrix $\text{Vand}{(\lambda_{1},\ldots,\lambda_{m})}^{T}$ is given by a LU-decomposition, i.e., there exist a lower triangle matrix $L$ and a upper triangle matrix $U$ with

More precisely, these matrices are given by

This factor equals the error scaling $a_{0}$, which completes the proof for the first case.

2\. case: $r \neq m$. Hence, $\text{ker}{(X)}$ is non-trivial, i.e., ${\text{ker}{(X)}} \neq {\{ 0\}}$. By Lemma 6.2 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain ${\text{im}{(X)}} \subseteq {\text{im}{(Y)}}$ and, therefore, it holds

because ${\text{im}{(A)}} \subseteq {\text{im}{(Y)}}$. Hence, $x_{0}$ is in the span of $\vartheta_{1},\ldots,\vartheta_{r}$ and therefore $q_{0} \in {\text{im}{(A)}}$, especially. However, by the proof of Theorem 3.7. ‣ 3 Theoretical Framework ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we obtain that the vector $q_{0} \in {\text{ker}{(A)}}$. Consequently, we obtain $q_{0} = 0$. ~□~

Theorem 6.3. ‣ 6 Exact-Dynamic Mode Decomposition (EXDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") clearly demonstrates the functionality of EXDMD. Via a reduced singular value decomposition, the dynamicly relevant properties of the system matrix were extracted, i.e., the eigenvectors to non-zero eigenvalues. As a result, the eigenvectors (or DMD modes) do not not generate a basis anymore and consequently the first snapshot $x_{0}$ will be reconstructed with an error. However, Theorem 6.3. ‣ 6 Exact-Dynamic Mode Decomposition (EXDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") gives us an exact representation of the error. The subsequent corollary illustrates the connection between the DMD amplitudes and the coefficients of the first snapshot in the eigenvector basis of the system matrix.

### Corollary 6.4

Let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{r}$, DMD modes $\vartheta_{1},\ldots,\vartheta_{r}$, DMD amplitudes $a_{1},\ldots,a_{r}$ be given by Algorithm 6.1. ‣ 6 Exact-Dynamic Mode Decomposition (EXDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. In addition, let the eigenvalues $\lambda_{1},\ldots,\lambda_{r},\lambda_{r + 1},\ldots,\lambda_{n}$ and eigenvectors $\vartheta_{1},\ldots,\vartheta_{r},v_{r + 1},\ldots,v_{n}$ of the system matrix as well as the coefficient vector $b = {(b_{1},\ldots,b_{n})}^{T} = {W^{- 1}x_{0}}$ with $W = {(\vartheta_{1},\ldots,\vartheta_{r},v_{r + 1},\ldots,v_{m})}$ be given. If ${\text{ker}{(X)}} \subseteq {\text{ker}{(Y)}}$, ${\text{rank}{(Y)}} = r$, and the (DMD) eigenvalues $\lambda_{1},\ldots,\lambda_{r}$ are distinct, then the DMD amplitudes coincide with the coefficients:

### Proof

The assumptions of Theorem 6.3. ‣ 6 Exact-Dynamic Mode Decomposition (EXDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Theorem 3.7. ‣ 3 Theoretical Framework ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") are satisfied, because the system matrix $A$ is diagonalizable by the $r$ distinct eigenvalues. Hence we receive

Since the eigenvectors (to distinct eigenvalues) are linear independent and the eigenvalues are non-zero, the coefficients have to match. ~□~

## Conclusion

A comprehensive theoretical analysis of Dynamic Mode Decomposition has been developed that clarify the connection between different variants of DMD (CDMD, SDMD, and EXDMD) and demonstrates several features of them. One of these features is the reconstruction property, which was proven for all variants and the system matrix as well. To this end, different scaling factors were used and new ones introduced to ensure this property. Especially for EXDMD, it was shown that under appropriate conditions the algorithm calculates the dynamically relevant, high-dimensional structures of the system matrix with the help of low-dimensional, spectral-theoretical techniques. The new findings facilitate the application with DMD since precise reconstructions are obtained which lead to a clearer decomposition of the data into DMD eigenvalues, modes and amplitudes.
