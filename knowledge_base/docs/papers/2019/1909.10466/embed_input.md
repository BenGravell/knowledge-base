<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Mode Decomposition: Theory and Data Reconstruction

Topics include Dynamic mode decomposition, Data-driven, Data reconstruction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Tutorial and survey that presents theoretical analysis of DMD with a focus on data reconstruction from DMD modes, addressing the relationship between DMD approximations and the underlying dynamics of the system.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dynamic Mode Decomposition (DMD) is a data-driven decomposition technique extracting spatio-temporal patterns of time-dependent phenomena. In this paper, we perform a comprehensive theoretical analysis of various variants of DMD. We provide a systematic advancement of these and examine the interrelations. In addition, several results of each variant are proven. Our main result is the exact reconstruction property. To this end, a new modification of scaling factors is presented and a new concept of an error scaling is introduced to guarantee an error-free reconstruction of the data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The analysis of time-dependent phenomena is at the heart of investigation in a broad range of scientific research. Within these studies, the integration of data in the form of time-series has increased considerably. Therefore, the application of innovative algorithms is necessary to gain deep insights into the characteristics of data. In this paper, we address time-series analysis by Dynamic Mode Decomposition (DMD), which was first introduced by Schmid and Sesterhenn in 2008.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

DMD is a data-driven and model-free algorithm extracting spatio-temporal patterns in the form of so-called DMD modes and DMD eigenvalues. As an efficient tool in fluid mechanics, DMD has gained much attention. DMD has been investigated on both practical and theoretical grounds. Nonetheless, the focus of these analyses was mainly a practical one. For example, various types of flow were considered, such as airflow around an airfoil, fuel flow in a combustion chamber, or heat conduction in various cases. Completely different fields of application comprise financial trading, video processing, epidemiology, neuroscience, and control theory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, we focus on theoretical investigations. The paper is thus structured as follows: After discussing related work, we introduce the theoretical framework of DMD dealing with the background mechanisms. In this process, we define the so-called system matrix, which is pioneering for DMD and prove the following results: a characterization for the exactness and diagonalizability of the system matrix as well as the resulting reconstruction of data with its spectral components. These theorems are central for the following sections introducing the three common variants of DMD: The original formulation, the modification by a singular value decomposition, and Exact-Dynamic Mode Decomposition. In this context, a systematic advancement will be presented that clarifies precisely the interrelation of these algorithms. This especially includes algebraic identities as well as spectral-theoretic results leading, e.g., to a new approach for the extension to the most recent variant of DMD. In addition, the exact reconstruction property of DMD will be proven for each DMD variant that guarantees an error-free reconstruction of the data. To this end, a new variant of scaling factors is introduced involving a new concept of an error scaling for the reconstruction of the first snapshot. Some concluding remarks will be given in the last section.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

This section is dedicated to the basic theoretical background of DMD. In this context, the general setting will be presented as well as an intuitive interpretation of the principles of DMD. These are crucial for the precise understanding of DMD, forming the basis for the subsequent sections. In addition, basic notation will be formalized and consistently used in this paper.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

The application of DMD starts with the availability of data that may stem either from empirical experiments or numerical simulations alike. The objective of DMD is to extract spatio-temporal patterns out of the data in the form of DMD modes, eigenvalues,and amplitudes. As the modes are related to spatial structures, the corresponding eigenvalues determine the temporal behavior of these. The amplitudes characterize the impact of individual modes on the whole system, i.e. the dominance structure.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

Now, consider data (snapshots) ${x_{0},x_{1},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ with the following two quantities: In the application areas of DMD such as fluid dynamics or non-linear dynamics, the connection between these variables is typically given by $n \gg m$, which means that the size of the data points is considerable larger than the number of snapshots. In this context, typical values are $n \approx 10^{6}$--$10^{12}$ (depending on whether we address 2D or 3D scenarios) and $m \approx 100$--$1000$. This basic setting is crucial for understanding the principles of DMD and will be assumed in the following derivation. However, DMD can also be mathematically formulated and applied without this assumption, as we will see later.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

In short, DMD calculates the relevant dynamic information of a high-dimensional linear operator that connects the given data points $x_{0},x_{1},\ldots,x_{m}$ in a least square sense, without explicitly computing it. This is achieved by an eigenvalue decomposition of a low-dimensional representation. The corresponding eigenvectors will be embedded as DMD modes into the high-dimensional space endowed with appropriate scaling factors, the DMD amplitudes.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

In order to obtain the high-dimensional matrix $A \in {\mathbb{C}}^{n \times n}$ connecting the data points, we consider the following (least-squares) minimization problem: Note that the high dimensionality stems from the fact $n \gg m$. An explicit solution of $A$ is necessary to formulate an algorithmic approach. To this end, we rewrite the data into the matrices obtaining the following equivalent minimization problem: where ${\parallel \cdot \parallel}_{F}$ denotes the Frobenius norm of a matrix. An explicit solution is now given by where $X^{+}$ denotes the Moore-Penrose pseudoinverse of $X$. Since the pseudoinverse always exists, the solution $A$ can be used for an algorithmic formulation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

Now, assuming the diagonalizability of the matrix $A$, i.e., $A = {V\LambdaV^{- 1}}$ with the matrices $\Lambda = {\text{diag}{(\lambda_{1},\ldots,\lambda_{n})}}$ and $V = \begin{bmatrix} \end{bmatrix}$ containing the eigenvalues and eigenvectors respectively, we obtain the characteristic reconstruction property of the matrix $A$ by for $k = {0,1,\ldots,m}$, where $b = {(b_{1},\ldots,b_{n})}^{T}$ are the coefficients of the linear combination of $x_{0}$ in the eigenvector basis, i.e. $b = {V^{- 1}x_{0}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

Since the rank of $A$ is at most $\min{\{{\text{rank}{(X)}},{\text{rank}{(Y)}}\}}$ and consequently not more than $m$, there are at least $n - m$ eigenvalues of $A$ that are equal to zero. The dynamic behavior will be thus captured by at most $m$ components, which are considerable fewer components. Consequently, we obtain the following reconstruction of the data: for $k = {1,\ldots,m}$, where $q_{0}$ is the resulting error arising from the missing $m - n$ components. In sum, we gain a reasonable low-dimensional decomposition of the data into the triples ${(\lambda_{j},v_{j},b_{j})} \in {{\mathbb{C}} \times {\mathbb{C}}^{n} \times {\mathbb{C}}}$, providing an instrument for diagnostic approaches as well as a tool for prediction, long-term analysis, and stability analysis.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

The different versions of DMD presented in the subsequent sections are based on various techniques to produce a low-dimensional representation of the matrix $A$ in order to (approximately) compute its eigenvalues and eigenvectors as well as new appropriate scaling factors. These procedures yield similar triples that will be denoted by ${(\lambda_{j},\vartheta_{j},a_{j})} \in {{\mathbb{C}} \times {\mathbb{C}}^{n} \times {\mathbb{C}}}$ throughout the paper. These triples consist of the so-called DMD eigenvalues, DMD modes, and DMD amplitudes corresponding to a particular algorithm (see each section).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

Before studying the variants of DMD, we first concentrate on an analysis of the high-dimensional structures involving the matrix $A$. Through a deeper understanding of the matrix $A$ representing the starting point of DMD, we obtain insights into the desired action of DMD. In particular, the success of an error-free reconstruction of DMD depends on the following two aspects: The exactness of the matrix $A$, i.e., ${AX} = Y$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Theoretical Framework", "weight": 1.0} -->

These two aspects will be examined throughout this section, however, before, the matrix $A$ will be captured in the following definition.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Companion Dynamic Mode Decomposition (CDMD)", "weight": 1.0} -->

In 2008, Schmid and Sesterhenn presented the first version of DMD. This variant will be referred to as Companion Dynamic Mode Decomposition (CDMD). CDMD has been investigated by experimental and numerical data by Schmid. The first approaches of a theoretic analysis were performed by Rowley et al.. Before we discuss the derivation of CDMD, the companion matrix will be defined, which is eponymous for this variant of DMD.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm 4.3 (Companion Dynamic Mode Decomposition (CDMD))", "weight": 1.0} -->

Construct the companion matrix $C_{c} \in {\mathbb{C}}^{m \times m}$ to the vector $c$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm 4.3 (Companion Dynamic Mode Decomposition (CDMD))", "weight": 1.0} -->

The algorithm described here differs from the standard literature as we introduce the necessary concept of DMD amplitudes. Note, that the matrix $K$ in step $6$, which defines the DMD amplitudes, may not be diagonal. However, if the eigenvalues are distinct, then $K$ is a diagonal matrix, as we will observe later. The current definition of the DMD amplitudes seems to be obscure and not very intuitive. Later, we will show that these DMD amplitudes are the right scaling factors for an exact reconstruction. In addition, we will prove that this choice equals ${(a_{1},\ldots,a_{m})}^{T} = {\Theta^{+}x_{0}}$ under some further assumption.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm 4.3 (Companion Dynamic Mode Decomposition (CDMD))", "weight": 1.0} -->

For a theoretical investigation, we need a more compact representation of the companion matrix $C_{c}$ from Algorithm 4.3). ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"). To this end, consider the following minimization problem which is closely related to the construction of the companion matrix. An explicit solution of the minimization problem is given by $C = {X^{+}Y} \in {\mathbb{C}}^{m \times m}$. This matrix will be captured in the following definition.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

At first glance, the two approaches seems to be equivalent. However, note that the twisted system matrix $C$ and the companion matrix $C_{c}$ are not necessarily equal or similar. This fact can be observed by a rank truncation of the matrices $X$ and $Y$. In particular, the companion matrix $C_{c}$ has at least rank $m - 1$, because the first $m - 1$ columns are linearly independent. However, the rank of the matrix $C = {X^{+}Y}$ depends only on the matrices $X$ and $Y$ and therefore it may be less than $m - 1$, which implies a non-similarity in general.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

The following lemma and corollary characterize the relations between the three objects $A,C$, and $C_{c}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "SVD-Dynamic Mode Decomposition (SDMD)", "weight": 1.0} -->

In 2010, the algorithm of DMD was modified radically by Schmid. He published a variant of DMD based on a reduced singular value decomposition. For this reason, we will denote this method by SVD-Dynamic Mode Decomposition (SDMD). The result was a robust and stable algorithm, which serves as a basis for the most modern version of DMD. We start this section by deducing this algorithm.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SVD-Dynamic Mode Decomposition (SDMD)", "weight": 1.0} -->

Let the system matrix $A$ to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$ be given as well as the reduced singular value decomposition of $X$ with $r = {\text{rank}{(X)}}$ and $X = {U\SigmaV^{\ast}} \in {\mathbb{C}}^{n \times m}$, where $U \in {\mathbb{C}}^{n \times r}$, $V \in {\mathbb{C}}^{m \times r}$ and $\Sigma \in {\mathbb{R}}^{r \times r}$. Utilizing the transformation matrix $U$, we construct the low-dimensional representation $S$ of the system matrix $A$ by For an explicit calculation of $S$, it is necessary to avoid the computation of the system matrix $A$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SVD-Dynamic Mode Decomposition (SDMD)", "weight": 1.0} -->

To this end, we calculate Now, we compute the eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of the matrix $S$ and finally transform them by the matrix $U$ into in order to obtain an approximation of the eigenvalues and eigenvectors of the system matrix: Consequently, the algorithm can be formulated as follows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm 5.1", "weight": 1.0} -->

Compute the reduced singular value decomposition $X = {U\SigmaV^{\ast}}$ with $r = {\text{rank}{(X)}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm 5.1", "weight": 1.0} -->

Compute the DMD eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of $S$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm 5.1", "weight": 1.0} -->

In Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), the DMD amplitudes will be defined intuitively by a best-fit linear combination of the first snapshots $x_{0}$ in the modes selection (compare Corollary 4.9 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")). For a deeper understanding of SDMD, we first characterize the connection to CDMD, which will be examined in the following lemma.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 5.5", "weight": 1.0} -->

SDMD is characterized by the robust singular value decomposition and the reconstruction property. However, the spectral-theoretical connection of SDMD to the system matrix is not clear. Therefore, let the system matrix $A$ as well as DMD eigenvalues $\lambda_{1},\ldots,\lambda_{m}$ and DMD modes $\vartheta_{1},\ldots,\vartheta_{m}$ be given by Algorithm 5.1 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") to the data ${x_{0},\ldots,x_{m}} \in {\mathbb{C}}^{n}$. Then the following equation hold: We observe that the eigenvalue equation is correct up to the projection $P_{X} = {XX^{+}} = {UU^{\ast}}$ onto the image of $X$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 5.5", "weight": 1.0} -->

The following proposition presents characterizations for the equality of the eigenvector equation of Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction").

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 5.10", "weight": 1.0} -->

For the formulation of an efficient algorithm, we need a more compact representation of the modified DMD modes $\zeta_{i}$, which arises directly from transformations of the eigenvectors of $S$. By Remark 5.5 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction") and Lemma 4.6 ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction"), we rearrange the modified DMD modes by Defining the DMD modes in this way, we obtain the most modern version of DMD, called Exact-Dynamic Mode Decomposition (EXDMD). In the following section, we will introduce this variant of DMD.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Exact-Dynamic Mode Decomposition (EXDMD)", "weight": 1.0} -->

In 2014, Tu et. al. presented the most modern version of DMD, called Exact-Dynamic Mode Decomposition (EXDMD). However, the algorithm presented here differs from the standard literature as we use a different definition of the DMD amplitudes. In addition, we introduce a novel relevant variable: The error scaling.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm 6.1 (Exact-Dynamic Mode Decomposition)", "weight": 1.0} -->

Compute the reduced singular value decomposition $X = {U\SigmaV^{\ast}}$ with $r = {\text{rank}{(X)}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm 6.1 (Exact-Dynamic Mode Decomposition)", "weight": 1.0} -->

Compute the DMD eigenvalues $\lambda_{i}$ and eigenvectors $v_{i}$ of $S$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Algorithm 6.1 (Exact-Dynamic Mode Decomposition)", "weight": 1.0} -->

The introduction of the error scaling $a_{0}$ and the fundamental change of the definition of the DMD amplitude will be justified by the subsequent theorem, which proves the reconstruction property of EXDMD. The reconstruction property of EXDMD, however, differs from the previous ones of CDMD (see Theorem 4.8. ‣ 4 Companion Dynamic Mode Decomposition (CDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")) and SDMD (see Theorem 5.4. ‣ 5 SVD-Dynamic Mode Decomposition (SDMD) ‣ Dynamic Mode Decomposition: Theory and Data Reconstruction")). The reason for this is the spectral-theoretic relation of EXDMD to the system matrix, as we will examine in the proof.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A comprehensive theoretical analysis of Dynamic Mode Decomposition has been developed that clarify the connection between different variants of DMD (CDMD, SDMD, and EXDMD) and demonstrates several features of them. One of these features is the reconstruction property, which was proven for all variants and the system matrix as well. To this end, different scaling factors were used and new ones introduced to ensure this property. Especially for EXDMD, it was shown that under appropriate conditions the algorithm calculates the dynamically relevant, high-dimensional structures of the system matrix with the help of low-dimensional, spectral-theoretical techniques. The new findings facilitate the application with DMD since precise reconstructions are obtained which lead to a clearer decomposition of the data into DMD eigenvalues, modes and amplitudes.
