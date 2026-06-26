<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Dynamic Mode Decomposition: Theory and Applications

Topics include Dynamic mode decomposition, Fluid dynamics, Data-driven methods, Koopman operator.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides rigorous theoretical foundations for DMD, introduces the exact DMD formulation with improved numerical accuracy, and analyzes convergence properties and connections to Koopman spectral analysis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Originally introduced in the fluid mechanics community, dynamic mode decomposition (DMD) has emerged as a powerful tool for analyzing the dynamics of nonlinear systems. However, existing DMD theory deals primarily with sequential time series for which the measurement dimension is much larger than the number of measurements taken. We present a theoretical framework in which we define DMD as the eigendecomposition of an approximating linear operator. This generalizes DMD to a larger class of datasets, including nonsequential time series. We demonstrate the utility of this approach by presenting novel sampling strategies that increase computational efficiency and mitigate the effects of noise, respectively. We also introduce the concept of linear consistency, which helps explain the potential pitfalls of applying DMD to rank-deficient datasets, illustrating with examples. Such computations are not considered in the existing literature, but can be understood using our more general framework. In addition, we show that our theory strengthens the connections between DMD and Koopman operator theory. It also establishes connections between DMD and other techniques, including the eigensystem realization algorithm (ERA), a system identification method, and linear inverse modeling (LIM), a method from climate science.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that under certain conditions, DMD is equivalent to LIM.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fluid flows often exhibit low-dimensional behavior, despite the fact that they are governed by infinite-dimensional partial differential equations (the Navier--Stokes equations). For instance, the main features of the laminar flow past a two-dimensional cylinder can be described using as few as three ordinary differential equations. To identify these low-order dynamics, such flows are often analyzed using *modal decomposition* techniques, including proper orthogonal decomposition (POD), balanced proper orthogonal decomposition (BPOD), and dynamic mode decomposition (DMD). Such methods describe the fluid state (typically the velocity or vorticity field) as a superposition of empirically computed basis vectors, or "modes." In practice, the number of modes necessary to capture the gross behavior of a flow is often many orders of magnitude smaller than the state dimension of the system (e.g., $\mathcal{O}{}$ compared to $\mathcal{O}{(10^{6})}$).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since it was first introduced, DMD has quickly gained popularity in the fluids community, primarily because it provides information about the *dynamics* of a flow, and is applicable even when those dynamics are *nonlinear*. A typical application involves collecting a time series of experimental or simulated velocity fields, and from them computing DMD modes and eigenvalues. The modes are spatial fields that often identify coherent structures in the flow. The corresponding eigenvalues define growth/decay rates and oscillation frequencies for each mode. Taken together, the DMD modes and eigenvalues describe the dynamics observed in the time series in terms of oscillatory components. In contrast, POD modes optimally reconstruct a dataset, with the modes ranked in terms of energy content. BPOD modes identify spatial structures that are important for capturing linear input-output dynamics, and can also be interpreted as an optimal decomposition of two (dual) datasets.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

At first glance, it may seem dubious that a nonlinear system could be described by superposition of modes whose dynamics are governed by eigenvalues. After all, one needs a linear operator in order to talk about eigenvalues. However, it was shown in that DMD is closely related to a spectral analysis of the Koopman operator. The Koopman operator is a linear but infinite-dimensional operator whose modes and eigenvalues capture the evolution of observables describing any (even nonlinear) dynamical system. The use of its spectral decomposition for data-based modal decomposition and model reduction was first proposed. DMD analysis can be considered to be a numerical approximation to Koopman spectral analysis, and it is in this sense that DMD is applicable to nonlinear systems. In fact, the terms "DMD mode" and "Koopman mode" are often used interchangably in the fluids literature.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Much of the recent work involving DMD has focused on its application to different flow configurations. For instance, DMD has been applied in the study of the wake behind a flexible membrane, the flow around high-speed trains, instabilities in annular liquid sheets, shockwave-turbulent boundary layer interactions, detonation waves, cavity flows, and various jets. There have also been a number of efforts regarding the numerics of the DMD algorithm, including the development of memory-efficient algorithms, an error analysis of DMD growth rates, and a method for selecting a sparse basis of DMD modes. Variants of the DMD algorithm have also been proposed, including optimized DMD and optimal mode decomposition. Theoretical work on DMD has centered mainly on exploring connections with other methods, such as Koopman spectral analysis, POD, and Fourier analysis. Theorems regarding the existence and uniqueness of DMD modes and eigenvalues can be found. For a review of the DMD literature, we refer the reader to.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many of the papers cited above mention the idea that DMD is able to characterize nonlinear dynamics through an analysis of some approximating linear system. In this work, we build on this notion. We present DMD as an analysis of *pairs* of $n$-dimensional data vectors $(x_{k},y_{k})$, in contrast to the sequential time series that are typically considered. From these data we construct a particular linear operator $A$ and define DMD as the eigendecomposition of that operator (see Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). We show that DMD modes satisfying this definition can be computed using a modification of the algorithm proposed. Both algorithms generate the same eigenvalues, with the modes differing by a projection (see Theorem 3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is of course no guarantee that analyzing this particular approximating operator is meaningful for data generated by nonlinear dynamics. To this end, we show that our definition strengthens the connections between DMD and Koopman operator theory, extending those connections to include more general sampling strategies. This is important, as it allows us to maintain the interpretion of DMD as an approximation to Koopman spectral analysis. We can then be confident that DMD is useful for characterizing nonlinear dynamics. Furthermore, we show that the connections between DMD and Koopman spectral analysis hold not only when the vectors $x_{k}$ are linearly independent, as assumed, but under a more general condition we refer to as linear consistency (see Definition 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). When the data are not linearly consistent, the Koopman analogy can break down and DMD analysis may produce either meaningful or misleading results. We show an example of each and explain the results using our approximating-operator definition of DMD.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

(For a more detailed investigation of how well DMD eigenvalues approximate Koopman eigenvalues, we refer the reader to.)

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The generality of our framework has important practical implications as well. To this end, we present examples demonstrating the benefits of applying DMD to nonsequential time series. For instance, we show that nonuniform temporal sampling can provide increased computational efficiency, with little effect on accuracy of the dominant DMD modes and eigenvalues. We also show that noise in experimental datasets can be dealt with by concatenating data from multiple runs of an experiment. The resulting DMD computation produces a spectrum with sharper, more isolated peaks, allowing us to identify higher-frequency modes that are obscured in a traditional DMD computation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, our framework highlights the connections between DMD and other well-known methods, specifically the eigensystem realization algorithm (ERA) and linear inverse modeling (LIM). The ERA is a control-theoretic method for system identification of linear systems. We show that when computed from the same data, DMD eigenvalues reduce to poles of an ERA model. This connection motivates the use of ERA-inspired strategies for dealing with certain limitations of DMD. LIM is a modeling procedure developed in the climate science community. We show that under certain conditions, DMD is equivalent to LIM. Thus it stands to reason that practioners of DMD could benefit from an awareness of related work in the climate science literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this work is organized as follows: in Section 2, we propose and discuss a new definition of DMD. We provide several different algorithms for computing DMD modes and eigenvalues that satisfy this new definition and show that these are closely related to the modes and eigenvalues computed using the currently accepted SVD-based DMD algorithm. A number of examples are presented in Section 3. These explore the application of DMD to rank-deficient datasets and nonsequential time series. Section 4 describes the connections between DMD and Koopman operator theory, the ERA, and LIM, respectively. We summarize our results in Section 5.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theory", "weight": 1.0} -->

Since its first appearance in 2008, DMD has been defined by an algorithm (the specifics of which are given in Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") below). Here, we present a more general, non-algorithmic definition of DMD. Our definition emphasizes data that are collected as a set of *pairs* ${\{{(x_{k},y_{k})}\}}_{k = 1}^{m}$, rather than as a sequential time series ${\{ z_{k}\}}_{k = 0}^{m}$. We show that our DMD definition and algorithm are closely related to the currently accepted algorithmic definition. In fact, the two approaches produce the same DMD eigenvalues; it is only the DMD modes that differ.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Standard definition", "weight": 1.0} -->

Originally, the DMD algorithm was formulated in terms of a companion matrix, which highlights its connections to the Arnoldi algorithm and to Koopman operator theory. The SVD-based algorithm presented in is more numerically stable, and is now generally accepted as the defining DMD algorithm; we describe this algorithm below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Standard definition", "weight": 1.0} -->

Consider a sequential set of data vectors $\{ z_{0},\ldots,z_{m}\}$, where each $z_{k} \in {\mathbb{R}}^{n}$. We assume that the data are generated by linear dynamics for some (unknown) matrix $A$. (Alternatively, the vectors $z_{k}$ can be sampled from a continuous evolution $z{(t)}$, in which case $z_{k} = {z{({k\Deltat})}}$ and a fixed sampling rate $\Deltat$ is assumed.) When DMD is applied to data generated by nonlinear dynamics, it is assumed that there exists an operator $A$ that approximates those dynamics. The DMD modes and eigenvalues are intended to approximate the eigenvectors and eigenvalues of $A$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm 1 (Standard DMD)", "weight": 1.0} -->

Arrange the data $\{ z_{0},\ldots,z_{m}\}$ into matrices Compute the (reduced) SVD of $X$ (see), writing where $U$ is $n \times r$, $\Sigma$ is diagonal and $r \times r$, $V$ is $m \times r$, and $r$ is the rank of $X$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm 1 (Standard DMD)", "weight": 1.0} -->

Define the matrix Compute eigenvalues and eigenvectors of $\overset{\sim}{A}$, writing The DMD mode corresponding to the DMD eigenvalue $\lambda$ is then given by If desired, the DMD modes can be scaled in a number of ways, as described in Appendix A.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm 1 (Standard DMD)", "weight": 1.0} -->

In this paper, we will refer to the modes produced by Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") as projected DMD modes, for reasons that will become apparent in Section 2.3 (in particular, see Theorem 3).

<!-- chunk {"id": "body-0021", "role": "body", "section": "New definition", "weight": 1.0} -->

The standard definition of DMD assumes a sequential set of data vectors $\{ z_{0},\ldots,z_{m}\}$ in which the order of vectors $z_{k}$ is critical. Furthermore, the vectors should (at least approximately) satisfy the relation. Here, we relax these restrictions on the data, and consider data *pairs* $\{{(x_{1},y_{1})},\ldots,{(x_{m},y_{m})}\}$. We then define DMD in terms of the $n \times m$ data matrices Note that the formulation (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) is a special case of, with $x_{k} = z_{k - 1}$ and $y_{k} = z_{k}$. In order to relate this method to the standard DMD procedure, we may assume that for some (unknown) matrix $\hat{A}$. However, the procedure here is applicable more generally.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The operator $A$ in (8. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) is the least-squares/minimum-norm solution to the potentially over- or under-constrained problem ${AX} = Y$. That is, if there is an exact solution to ${AX} = Y$ (which is always the case if the vectors $x_{k}$ are linearly independent), then the choice (8. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) minimizes ${\| A\|}_{F}$, where $\parallel A \parallel_{F} = {Tr}{(AA^{\ast})}^{1/2}$ denotes the Frobenius norm. If there is no $A$ that exactly satisfies ${AX} = Y$, then the choice (8.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) minimizes ${\|{{AX} - Y}\|}_{F}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

When $n$ is large, as is often the case with fluid flow data, it may be inefficient to compute the eigendecomposition of the $n \times n$ matrix $A$. In some cases, even storing $A$ in memory can be prohibitive. Using the following algorithm, the DMD modes and eigenvalues can be computed without an explicit representation or direct manipulations of $A$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm 2 (Exact DMD)", "weight": 1.0} -->

Compute the (reduced) SVD of $X$, writing $X = {U\SigmaV^{\ast}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm 2 (Exact DMD)", "weight": 1.0} -->

Compute eigenvalues and eigenvectors of $\overset{\sim}{A}$, writing ${\overset{\sim}{A}w} = {\lambdaw}$. Each nonzero eigenvalue $\lambda$ is a DMD eigenvalue.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm 2 (Exact DMD)", "weight": 1.0} -->

The DMD mode corresponding to $\lambda$ is then given by If desired, the DMD modes can be scaled in a number of ways, as described in Appendix A.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2", "weight": 1.0} -->

When $n \gg m$, the above algorithm can be modified to reduce computational costs. For instance, the SVD of $X$ can be computed efficiently using the method of snapshots. This involves computing the correlation matrix $X^{\ast}X$. The product $U^{\ast}Y$ required to form $\overset{\sim}{A}$ can be cast in terms of a product $X^{\ast}Y$, using (3. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) to substitute for $U$. If $X$ and $Y$ happen to share columns, as is the case for sequential time series, then $X^{\ast}Y$ will share elements with $X^{\ast}X$, reducing the number of new computations required. (See Section 3.1 for more on sequential versus nonsequential time series.)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Algorithm 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") is nearly identical to Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") (originally presented in ). In fact, the only difference is that the DMD modes are given by (9. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), whereas in Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), they are given by (6. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). This modification is subtle, but important, as we discuss in Section 2.3.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Though the original presentations of DMD assume $X$ and $Y$ of the form given by (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") does not make use of this structure. That is, the algorithm can be carried out for the general case of $X$ and $Y$ given. (This point has been noted previously,.)

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Algorithm 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") may also be used to find certain eigenvectors with $\lambda = 0$ (that is, in the nullspace of $A$). In particular, if ${\overset{\sim}{A}w} = 0$ and $\varphi = {YV\Sigma^{- 1}w} \neq 0$, then $\varphi$ is an eigenvector with $\lambda = 0$ (and is in the image of $Y$); if ${\overset{\sim}{A}w} = 0$ and ${YV\Sigma^{- 1}w} = 0$, then $\varphi = {Uw}$ is an eigenvector with $\lambda = 0$ (and is in the image of $X$). However, DMD modes corresponding to zero eigenvalues are usually not of interest, since they do not play a role in the dynamics.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Next, we characterize the conditions under which the operator $A$ defined by (8. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) satisfies $Y = {AX}$. We emphasize that this does not require that $Y$ is generated from $X$ through linear dynamics defined by $A$; we place no restrictions on the data pairs $(x_{k},y_{k})$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Comparing definitions", "weight": 1.0} -->

Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") (originally presented in) has come to dominate among DMD practioners due to its numerical stability. Effectively, it has become the working definition of DMD. As mentioned above, it differs from Algorithm 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") only in that the (projected) DMD modes are given by where $w$ is an eigenvector of $\overset{\sim}{A}$, while the exact modes DMD modes are given by (9. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) as Since $U$ contains left singular vectors of $X$, we see that the original modes defined by (6. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) lie in the image of $X$, while those defined by (9.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Comparing definitions", "weight": 1.0} -->

‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) lie in the image of $Y$. As a result, the modes $\hat{\varphi}$ are not eigenvectors of the approximating linear operator $A$. Are they related in any way to the eigenvectors of $A$? The following theorem establishes that they are, and motivates the terminology projected DMD modes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 5", "weight": 1.0} -->

If the vectors $\{ y_{k}\}$ lie in the span of the vectors $\{ x_{k}\}$, then ${{\mathbb{P}}_{X}A} = A$, and the projected and exact DMD modes are identical. For instance, this is the case for a sequential time series (as in (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))) when the last vector $z_{m}$ is a linear combination of $\{ z_{0},\ldots,z_{m - 1}\}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 5", "weight": 1.0} -->

In addition to providing an improved algorithm, also explores the connection between (projected) DMD and POD. For data generated by linear dynamics $z_{k + 1} = {Az_{k}}$, derives the relation $\overset{\sim}{A} = {U^{\ast}AU}$ and notes that we can interpret $\overset{\sim}{A}$ as the correlation between the matrix of POD modes $U$ and the matrix of time-shifted POD modes $AU$. Of course, $\overset{\sim}{A}$ also determines the DMD eigenvalues. Exact DMD is based on the definition of $A$ as the least-squares/minimum-norm solution to ${AX} = Y$, but does not require that equation to be satisfied exactly. Even so, we can combine and to find that $\overset{\sim}{A} = {U^{\ast}AU}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Thus exact DMD preserves the interpretation of $\overset{\sim}{A}$ in terms of POD modes, extending it from sequential time series to generic data matrices, and without making any assumptions about the dynamics relating $X$ and $Y$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

Compute the (reduced) SVD of $X$, writing $X = {U\SigmaV^{\ast}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

Compute an orthonormal basis for the column space of $\begin{bmatrix} \end{bmatrix}$, stacking the basis vectors in a matrix $Q$ such that ${Q^{\ast}Q} = I$. For example, $Q$ can be computed by singular value decomposition of $\begin{bmatrix} \end{bmatrix}$, or by a $QR$ decomposition.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

The DMD mode corresponding to $\lambda$ is then given by If desired, the DMD modes can be scaled in a number of ways, as described in Appendix A.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

To see that $\varphi$ computed by Algorithm 3. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") is an exact DMD mode, we first observe that because the columns of $Q$ span the column space of $Y$, we can write $Y = {QQ^{\ast}Y}$, and thus $A = {QQ^{\ast}A}$. Then we find that We emphasize that because the above algorithm requires both an SVD of $X$ and a QR decomposition of the augmented matrix $\begin{bmatrix} \end{bmatrix}$, it is more costly than Algorithm 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), which should typically be used in practice. However, Algorithm 3. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") proves useful in showing how exact DMD can be interpreted as a simple extension of the standard algorithm for projected DMD (see Algorithm 1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). Recall that in projected DMD, one constructs the matrix $\overset{\sim}{A} = {U^{\ast}AU}$, where $U$ arises from the SVD of $X$. One then finds eigenvectors $w$ of $\overset{\sim}{A}$, and the projected DMD modes have the form $\hat{\varphi} = {Uw}$. Algorithm 3. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") is precisely analogous, with $U$ replaced by $Q$: one constructs ${\overset{\sim}{A}}_{Q} = {Q^{\ast}AQ}$, finds eigenvectors $v$ of ${\overset{\sim}{A}}_{Q}$, and the exact DMD modes have the form $\varphi = {Qw}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

In the case of a sequential time series, where $X$ and $Y$ are given by (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), projected DMD projects $A$ onto the space spanned by the first $m$ vectors $\{ z_{0},\ldots,z_{m - 1}\}$ (columns of $X$), while exact DMD projects $A$ onto the space spanned by all $m + 1$ vectors $\{ z_{0},\ldots,z_{m}\}$ (columns of $X$ and $Y$). In this sense, exact DMD is perhaps more natural, as it uses all of the data, rather than leaving out the last vector.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm 3 (Exact DMD, alternative method)", "weight": 1.0} -->

The case of a sequential time series is so common that it deserves special attention. For this case, we provide a variant of Algorithm 3. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") that is computationally advantageous.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Arrange the data $\{ z_{0},\ldots,z_{m}\}$ into matrices $X$ and $Y$, as in (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Compute the (reduced) SVD of $X$, writing $X = {U\SigmaV^{\ast}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Compute a vector $q$ such that the columns of form an orthonormal basis for $\{ z_{0},\ldots,z_{m}\}$. For instance, $q$ may be computed by one step of the Gram-Schmidt procedure applied to $z_{m}$: (If $p = 0$, then take $Q = U$; in this case, exact DMD is identical to projected DMD, as discussed in Remark 5.)

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Define the matrix $\overset{\sim}{A} \triangleq {U^{\ast}YV\Sigma^{- 1}}$, as in (4. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Compute eigenvalues and eigenvectors of $\overset{\sim}{A}$, writing ${\overset{\sim}{A}w} = {\lambdaw}$. Each nonzero eigenvalue $\lambda$ is a DMD eigenvalue.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

The DMD mode corresponding to $\lambda$ is then given by If desired, the DMD modes can be scaled in a number of ways, as described in Appendix A.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm 4 (Exact DMD, sequential time series)", "weight": 1.0} -->

Here, (16. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) is obtained from (9. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), noting that $B = {QQ^{\ast}B}$, so From Algorithm 4. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), we see that an exact DMD mode $\varphi$ can be viewed as a projected DMD mode $\hat{\varphi}$ (calculated from (6. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))) plus a correction (the last term in (16. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))) that lies in the nullspace of $A$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Applications", "weight": 1.0} -->

In this section we discuss the practical implications of a DMD framework based on Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"). Specifically, we extend DMD to nonsequential datasets using the fact that Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") places no constraints on the structure of the data matrices $X$ and $Y$. This allows for novel temporal sampling strategies that we show to increase computational efficiency and mitigate the effects of noise, respectively. We also present canonical examples that demonstrate the potential benefits and pitfalls of applying DMD to rank-deficient data. Such computations are not discussed in the existing DMD literature, but can be understood in our linear algebra-based framework.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Nonsequential sampling", "weight": 1.0} -->

In Section 2.2, there were no assumptions made on the data contained in $X$ and $Y$. However, DMD is typically applied to data that come from a dynamical system, for instance one whose evolution is given by with $z \in {\mathbb{R}}^{n}$. Often, the data consist of direct measurements of the state $z$. More generally, one could measure some function of the state $h{(z)}$ (see Section 4.1).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Nonsequential sampling", "weight": 1.0} -->

Consider a set of vectors $\{ z_{1},\ldots,z_{m}\}$. These vectors need not comprise a sequential time series; they do not even need to be sampled from the same dynamical trajectory. There is no constraint on how the vectors $z_{k}$ are sampled from the state space. We pair each vector $z_{k}$ with its image under the dynamics $f{(z_{k})}$. This yields a set of data pairs $\{{(z_{1},{f{(z_{1})}})},\ldots,{(z_{m},{f{(z_{m})}})}\}$. Arranging these vectors as in yields matrices with which we can perform either projected or exact DMD. The case of sequential time series, for which $z_{k + 1} = {f{(z_{k})}}$, is simply a special case.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 6", "weight": 1.0} -->

We observe that only the pairwise correspondence of the columns of $X$ and $Y$ is important, and not the overall ordering. That is, permuting the order of the columns of $X$ and $Y$ has no effect on the matrix $A = {YX^{+}}$, or on the subsequent computation of DMD modes and eigenvalues, so long as the same permutation is applied to the columns of both $X$ and $Y$. This is true even for data taken from a sequential time series (i.e., $X$ and $Y$ as given in (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Recall from Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") and Remark 1 that DMD can be interpreted as an analysis of the best-fit linear operator relating $X$ and $Y$. This operator relates the columns of $X$ to those of $Y$ in a pairwise fashion. For $X$ and $Y$ as, the columns of $X$ are mapped to those of $Y$ by the (generally) nonlinear map $f$. Regardless, DMD provides eigenvalues and eigenvectors of the linear map $A = {YX^{+}}$. Then we can interpret DMD as providing an analysis of the best-fit linear approximation to $f$. If $X$ and $Y$ are linearly consistent, we can also interpret DMD using the formalism of Koopman operator theory (see Section 4.1).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The use of in place of (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) certainly offers greater flexibility in the sampling strategies that can be employed for DMD (see Sections 3.2.3 and 3.2.4). However, it is important to note that for sequential time series, there exist memory-efficient variants of Algorithm 1. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"). These improved algorithms take advantage of the overlap in the columns of $X$ and $Y$ (when defined as in (2. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))) to avoid redundant computations; the same strategies can be applied to Algorithms 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), 3. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), and 4. ‣ 2.3. Comparing definitions ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications").

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 6", "weight": 1.0} -->

This is not possible for the more general definitions of $X$ and $Y$ given by and.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Examples", "weight": 1.0} -->

The following section presents examples demonstrating the utility of a DMD theory based on Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"). The first two examples consider DMD computations involving rank-deficient datasets, which are not treated in the existing DMD literature. We show that in some cases, DMD can still provide meaningful information about the underlying dynamical system, but in others, the results can be misleading. The second two examples use the generalized approach described in Section 3.1 to perform DMD analysis using nonsequential datasets. First, we use nonuniform sampling to dramatically increase the efficiency of DMD computations. Then, we concatenate time series taken from multiple runs of an experiment, reducing the effects of noise.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Stochastic dynamics", "weight": 1.0} -->

Consider a system with stochastic dynamics where each $z_{k} \in {\mathbb{R}}$. We choose a decay rate $\lambda = 0.5$ and let $n_{k}$ be white noise with variance $\sigma^{2} = 10$. (This system was first used as a test of DMD.) Figure 1 (left) shows a typical trajectory for an initial condition $z_{0} = 0$. If we apply DMD to this trajectory, we estimate a decay rate $\overset{\sim}{\lambda} = 0.55$. This is despite the fact that the nominal (noiseless) trajectory is simply given by $z_{k} = 0$; a global, linear analysis of the trajectory shown in Figure 1 (left) would identify a stationary process ($\overset{\sim}{\lambda} = 0$).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Stochastic dynamics", "weight": 1.0} -->

Because the existing DMD literature focuses on high-dimensional systems, existing DMD theory deals primarily with time series whose elements are linearly independent. As such, it cannot be applied to explain the ability of DMD to accurately estimate the dynamics underlying this noisy data (a rank-one time series). Recalling Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), we can interpret DMD in terms of a linear operator that relates the columns of a data matrix $X$ to those of $Y$, in column-wise pairs. Figure 1 (right) shows the time series from Figure 1 (left) plotted in this pairwise fashion. We see that though the data are noisy, there is clear evidence of a linear relationship between $z_{k}$ and $z_{k + 1}$. For rank-deficient data, DMD approximates the dynamics relating $X$ and $Y$ through a least-squares fit, and so it is no surprise that we can accurately estimate $\lambda$ from this time series.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Standing waves", "weight": 1.0} -->

Because each DMD mode has a corresponding DMD eigenvalue (and thus a corresponding growth rate and frequency), DMD is often used to analyze oscillatory behavior, whether the underlying dynamics are linear or nonlinear. Consider data describing a standing wave: where $q$ is a fixed vector in ${\mathbb{R}}^{n}$. For instance, such data can arise from the linear system where ${(u_{k},v_{k})} \in {\mathbb{R}}^{2n}$. If we measure only the state $u_{k}$, then we observe the standing wave. Such behavior can also arise in nonlinear systems, for instance by measuring only one component of a multi-dimensional limit cycle.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Standing waves", "weight": 1.0} -->

Suppose we compute DMD modes and eigenvalues from data satisfying. By construction, the columns of the data matrix $X$ will be spanned by the single vector $q$. As such, the SVD of $X$ will generate a matrix $U$ with a single column, and the matrix $\overset{\sim}{A}$ will be $1 \times 1$. Then there will be precisely one DMD eigenvalue $\lambda$. Since $z$ is real-valued, then so is $\lambda$, meaning it captures only exponential growth/decay, and no oscillations. This is despite the fact that the original data are known to oscillate with a fixed frequency.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Standing waves", "weight": 1.0} -->

What has gone wrong? It turns out that, in this example, the data are not linearly consistent (see Definition 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). To see this, let $x$ and $y$ be vectors with components $x_{k} = {\cos{({k\theta})}}$ and $y_{k} = {\cos{({{({k + 1})}\theta})}}$ (for $k = {0,\ldots,{m - 1}}$), so the data matrices become Then $X$ and $Y$ are not linearly consistent unless $\theta$ is a multiple of $\pi$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Standing waves", "weight": 1.0} -->

For instance, the vector $a = {({- {\cos\theta}},1,0,\ldots,0)}$ is in $\mathcal{N}{(X)}$, since ${x^{T}a} = 0$. However, ${y^{\ast}a} = {{- {\cos^{2}\theta}} + {\cos{2\theta}}} = {\sin^{2}\theta}$, so $a \notin {\mathcal{N}{(Y)}}$ unless $\theta = {j\pi}$. Also, note that if $\theta = \pi$, then the columns of $X$ simply alternate sign, and in this case DMD yields the (correct) eigenvalue $- 1$. As such, even though the data in this example arise from the linear system, there is no $A$ such that $Y = {AX}$ (by Theorem 2), and DMD fails to capture the correct dynamics. This example underscores the importance of linear consistency.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Standing waves", "weight": 1.0} -->

We note that in practice, we observe the same deficiency when the data do not satisfy exactly, so long as the dynamics are dominated by such behavior (a standing wave). Thus the presence of random noise, which may increase the rank of the dataset, does not alleviate the problem. This is not surprising, as the addition of random noise should not enlarge the subspace in which the oscillation occurs. However, if we append the measurement with a time-shifted value, i.e., performing DMD on a sequence of vectors $\begin{bmatrix} \end{bmatrix}^{T}$, then the data matrices $X$ and $Y$ become linearly consistent, and we are able to identify the correct oscillation frequency. (See Section 4.2 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications") for an alternative motivation for this approach.)

<!-- chunk {"id": "body-0067", "role": "body", "section": "Nonuniform sampling", "weight": 1.0} -->

Systems with a wide range of time scales can be challenging to analyze. If data are collected too slowly, dynamics on the fastest time scales will not be captured. On the other hand, uniform sampling at a high frequency can yield an overabundance of data, which can prove challenging to deal with numerically. Such a situation can be handled using the following sampling strategy: where we again assume dynamics of the form $z_{k + 1} = {f{(z_{k})}}$. The columns of $X$ and $Y$ are separated by a single iteration of $f$, capturing its fastest dynamics. However, the tuning parameter $P$ allows for a separation of time scales between the flow map iteration and the rate of data collection.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Nonuniform sampling", "weight": 1.0} -->

We demonstrate this strategy using a flow control example. Consider the flow past a two-dimensional cylinder, which is governed by the incompressible Navier--Stokes equations. We simulate the dynamics using the fast immersed boundary projection method detailed. The (non-dimensionalized) equations of motion are where $\overset{\rightarrow}{u}$ is the velocity, $p$ is the pressure, and $\overset{\rightarrow}{x}$ is the spatial coordinate. The Reynolds number $\text{Re} \triangleq {{U_{\infty}D}/\nu}$ is a nondimensional paramter defined by the freestream velocity $U_{\infty}$, the cylinder diameter $D$, and the kinematic viscosity $\nu$. $\partial\mathcal{B}$ is the union of the boundaries of any bodies in the flow. $\overset{\rightarrow}{f}$ is a boundary force that can be thought of a Lagrange multiplier used to enforce the no-slip boundary condition.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Nonuniform sampling", "weight": 1.0} -->

$\delta$ is the Dirac delta function.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Nonuniform sampling", "weight": 1.0} -->

We consider a cylinder with diameter $D = 1$ placed at the origin, in a flow with freestream velocity $U_{\infty} = 1$ and Reynolds number $\text{Re} = 100$. Convergence tests show that our simulations are accurate for an inner-most domain with ${(x,y)} \in {{\lbrack 15,15\rbrack} \times {\lbrack{- 5},5\rbrack}}$ and a $1500 \times 500$ mesh of uniformly-spaced points. At this Reynolds number, the flow is globally unstable. As a step towards computing a reduced-order model using BPOD, we restrict the linearized dynamics to their stable subspace. The system is actuated using a disk of vertical velocity downstream of the cylinder and sensed using localized measurements of vertical velocity placed along the flow centerline. This setup is based on flow control benchmark proposed in and is illustrated in Figure 2 (left).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Nonuniform sampling", "weight": 1.0} -->

The impulse response of this system is shown in Figure 2 (right). We see that from $t = 200$ to $t = 500$, the dynamics exhibit both a fast and slow oscillation. Suppose we want to identify the underlying frequencies and corresponding modes using DMD. For instance, this would allow us to implement the more efficient and more accurate analytic tail variant of BPOD. In order to capture the fast frequency, we must sample the system every 50 timesteps, with each timestep corresponding to ${\Deltat} = 0.02$. (This is in order to satisfy the Nyquist--Shannon sampling criterion.) As such, we let $z_{k} = {z{({50k\Deltat})}}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

DMD is often applied to experimental data, which are typically noisy. While filtering or phase averaging can be done to eliminate noise prior to DMD analysis, this is not always desirable, as it may remove features of the true dynamics. In POD analysis, the effects of noise can be averaged out by combining multiple trajectories in a single POD computation. We can take the same approach in DMD analysis using.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

Row order corresponds to decreasing mode norm.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

Table 1. Comparison of DMD eigenvalues∗ Figure 4. Comparison of dominant DMD modes computed from the impulse response shown in Figure 2 (right), illustrated using contours of vorticity. For each of the dominant frequencies, modes computed using nonuniform sampling (nonsequential DMD; bottom row) match those computed using uniform sampling (sequential DMD; top row). (For brevity, only the real part of each mode is shown; similar agreement is observed in the imaginary parts.) (a) f = 0.118, uniform sampling; (b) f = 0.127, uniform sampling; (c) f = 0.118, nonuniform sampling; (d) f = 0.127, nonuniform sampling.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

Consider multiple dynamic trajectories, indexed by $j$: ${\{ z_{k}^{j}\}}_{k = 0}^{m_{j}}$. These could be multiple runs of an experiment, or particular slices of a single, long trajectory. (The latter might be useful in trying to isolate the dynamics of a recurring dynamic event.) Suppose there are a total of $J$ trajectories. DMD can be applied to the entire ensemble of trajectories by defining We demonstrate this approach using experimental data from a bluff-body wake experiment. A finite-thickness flat plate with an elliptical leading edge is placed in a uniform oncoming flow. Figure 5 shows a schematic of the experimental setup. We capture snapshots of the velocity field in the wake behind the body using a time-resolved particle image velocimetry (PIV) system. (For details on the PIV data acquisition, see.) Multiple experimental runs are conducted, with approximately 1,400 velocity fields captured in each run. This corresponds to the maximum amount of data that can be collected per run.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

Due to the high Reynolds number ($\text{Re} = {50,000}$), the flow is turbulent. As such, though we observe a standard von Kármán vortex street (see Figure 6), the familiar vortical structures are contaminated by turbulent fluctuations. Figure 7 (left) shows a DMD spectrum computed using PIV data from a single experimental run.^11^1Instead of simply plotting the mode norms against their corresponding frequencies, as is generally done, we first scale the mode norms by $\lambda^{m}$. This reduces the height of spectral peaks corresponding to modes with large norm but quickly decaying eigenvalues. For dynamics known to lie on an attractor, such peaks can be misleading; they do not contribute to the long-time evolution of the system. The spectrum is characterized by a harmonic set of peaks, with the dominant peak corresponding to the wake shedding frequency. The corresponding modes are shown in Figure 8 (a--c). We see that the first pair of modes (see Figure 8 (a)) exhibits approximate top-bottom symmetry, with respect to the centerline of the body.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

The second pair of modes (see Figure 8 (b)) shows something close to top-bottom antisymmetry, though variations in the vorticity contours make this antisymmetry inexact. The third pair of modes (see Figure 8 (c)) also shows approximate top-bottom symmetry, with structures that are roughly spatial harmonics of those seen in the first mode pair.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Combining multiple trajectories", "weight": 1.0} -->

These modal features are to be expected, based on two-dimensional computations of a similar flow configuration. However, when computed from noise-free simulation data, the symmetry/antisymmetry of the modes is more exact. Figures 7 (right) and 8 (d--g) show that when five experimental runs are used, the experimental DMD results improve, more closely matching computational results. In the DMD spectrum (see Figure 7 (right)), we again observe harmonic peaks, with a fundamental frequency corresponding to the shedding frequency. The peaks are more isolated than those in Figure 7 (left); in fact, we observe a fourth frequency peak, which is not observed in the single-run computation. The modal structures, shown in Figure 8 (d--g), display more obvious symmetry and antisymmetry, respectively. The structures are also smoother and more elliptical.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Connections to other methods", "weight": 1.0} -->

In this section we discuss how DMD relates to other methods. First, we show that our definition of DMD preserves, and even strengthens, the connections between DMD and Koopman operator theory. Without these connections, the use of DMD to analyze nonlinear dynamics appears dubious, since there seems to be an underlying assumption of (approximately) linear dynamics (see Section 3.1), as. One might well question whether such an approximation would characterize a nonlinear system in a meaningful way. However, so long as DMD can be interpreted as an approximation to Koopman spectral analysis, there is a firm theoretical foundation for applying DMD in analyzing nonlinear dynamics.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Connections to other methods", "weight": 1.0} -->

Second, we explore the links between DMD and the eigensystem realization algorithm (ERA). The close relationship between the two methods provides motivation for the use of strategies from the ERA in DMD computations where rank is a problem. Finally, we show that under certain assumptions, DMD is equivalent to linear inverse modeling (LIM), a method developed in the climate science community decades ago. The link between the two methods suggests that practitioners of DMD may benefit from an awareness of the LIM literature, and vice versa.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

We briefly introduce the concepts of Koopman operator theory below and discuss how they relate to the theory outlined in Section 2. The connections between Koopman operator theory and projected DMD were first explored, but only in the context of sequential time series. Here, we extend those results to more general datasets, doing so using exact DMD (defined in Section 2.2).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

Consider a discrete-time dynamical system where $z$ is an element of a finite-dimensional manifold $M$. The Koopman operator $\mathcal{K}$ acts on scalar functions $g:{M\rightarrow{\mathbb{R}}}$ or $\mathbb{C}$, mapping $g$ to a new function $\mathcal{K}g$ given by Thus the Koopman operator is simply a composition or pull-back operator. We observe that $\mathcal{K}$ acts linearly on functions $g$, even though the dynamics defined by $f$ may be nonlinear.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

(We assume each component of $h$ lies in the span of the eigenfunctions.) We refer to the vectors ${\overset{\sim}{\varphi}}_{j}$ as *Koopman modes* (after). | Applying the Koopman operator, we find that For a sequential time series, we can repeatedly apply the Koopman operator (see and) to find A set of modes $\{{\overset{\sim}{\varphi}}_{j}\}$ and eigenvalues $\{\lambda_{j}\}$ must satisfy in order to be considered Koopman modes and eigenvalues.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

Now consider a set of arbitrary initial states $\{ z_{0},z_{1},\ldots,z_{m - 1}\}$ (not necessarily a trajectory of the dynamical system), and let As before, construct data matrices $X$ and $Y$, whose columns are $x_{k}$ and $y_{k}$. This is similar to, except that here we measure an observable, rather than the state itself. As long as the data matrices $X$ and $Y$ are linearly consistent (see Definition 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), we can determine a relationship between DMD modes and Koopman modes, as follows.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

Suppose we compute DMD modes from $X$ and $Y$, giving us eigenvectors and eigenvalues that satisfy where $A = {YX^{+}}$. If the matrix $A$ has a full set of eigenvectors, then we can expand each column $x_{k}$ of $X$ as | for some constants $c_{jk}$. For linearly consistent data, we have ${Ax_{k}} = y_{k}$, by Theorem 2, so | Comparing to, we see that in the case of linearly consistent data matrices (and diagonalizable $A$), the DMD modes correspond to Koopman modes, and the DMD eigenvalues to Koopman eigenvalues, where the constants $c_{jk}$ are given by $c_{jk} = {\theta_{j}{(z_{k})}}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

(We note, however, that we typically do not know the states $z_{k}$, nor do we know the Koopman eigenfunctions $\theta_{j}$.) If the data arise from a sequential time series, we can scale the modes to subsume the constants $c_{jk}$, following. (For more details see Appendix A.)

<!-- chunk {"id": "body-0087", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

The relationship between Koopman modes and DMD modes is similar to that established in (and discussed further in ), but the present result differs in some important respects. First, the result in uses projected DMD modes (see Section 2.1) and requires a sequential time series; here, we use exact DMD modes (see Section 2.2) and do not require a sequential time series. Furthermore, assumes the vectors $x_{k}$ are linearly independent; here, we impose the weaker requirement of linear consistency.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

We note that when $n$ is large, it may be impractical to compute all of the DMD modes. For instance, when $n \gg m$, $A$ will have a large nullspace, and one might use Algorithm 2. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") to compute only those DMD modes with nonzero eigenvalues. Suppose the rank of $A$ is $r$ and we write | where the first sum contains only DMD modes with nonzero eigenvalues. We still have | since all modes in the second sum have zero eigenvalues. As such, those modes don't contribute to the dynamics, and we can neglect those vectors as an error term that gets projected out by the dynamics. Contrast this with the DMD reconstruction of a sequential time series using projected DMD, where the residual instead appears at the end of the time series (see 3.13--3.14 in).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Koopman spectral analysis", "weight": 1.0} -->

Though the Koopman analogy provides a firm mathematical foundation for applying DMD to data generated by nonlinear systems, it is limited by the fact that it relies. The derivation of this equation requires making a number of assumptions, namely that the data are linearly consistent and that the matrix $A$ has a full set of eigenvectors (e.g., this holds when the eigenvalues of $A$ are distinct). When these assumptions do not hold, there is no guarantee that DMD modes will closely approximate Koopman modes. For instance, in some systems DMD modes and eigenvalues closely approximate those of the Koopman operator near an attractor, but not far from it. DMD may also perform poorly when applied to dynamics whose Koopman spectral decomposition contains Jordan blocks. In contrast, an understanding of DMD built on Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") holds even when these conditions break down.

<!-- chunk {"id": "body-0090", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

The ERA is a control-theoretic method for system identification and model reduction. Applicable to linear systems, the ERA takes input-output data and from them computes a minimal realization of the underlying dynamics. In this section, we show that while DMD and the ERA were developed in different contexts, they are closely related: the low-order linear operators central to each method are related by a similarity transform. This connection suggests that strategies used in ERA computations could be leveraged for gain in DMD computations. Specifically, it provides a motivation for appending the data matrices $X$ and $Y$ with time-shifted data to overcome rank problems (as suggested in Section 3.2.2).

<!-- chunk {"id": "body-0091", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

Consider the linear, time-invariant system where $x \in {\mathbb{R}}^{n}$, $u \in {\mathbb{R}}^{p}$, and $y \in {\mathbb{R}}^{q}$. (The matrix $A$ defined here is not necessarily related to the one defined in Section 2.) We refer to $x$ as the state of the system, $u$ as the input, and $y$ as the output.

<!-- chunk {"id": "body-0092", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

The goal of the ERA is to identify the dynamics of the system (30 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) from a time history of $y$. Specifically, in the ERA we sample outputs from the impulse response of the system. We collect the sampled outputs in two sets where we sample the impulse response every $P$ steps. The elements of $\mathcal{H}$ and $\mathcal{H}'$ are commonly referred to as Markov parameters of the system (30 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")).

<!-- chunk {"id": "body-0093", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

We then form the Hankel matrix by stacking the elements of $\mathcal{H}$ as where $m_{c}$ and $m_{o}$ can be chosen arbitrarily, subject to ${m_{c} + m_{o}} = {m - 1}$. The time-shifted Hankel matrix is built from the elements of $\mathcal{H}'$ in the same way: Next, we compute the (reduced) SVD of $H$, giving us Let $U_{r}$ consist of the first $r$ columns of $U$. Similarly, let $\Sigma_{r}$ be the upper left $r \times r$ submatrix of $\Sigma$ and let $V_{r}$ contain the first $r$ columns of $V$. Then the $r$-dimensional ERA approximation of (30 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) is given by the reduced-order system Now, suppose we use $H$ and $H'$ to compute DMD modes and eigenvalues as in Algorithm 2.

<!-- chunk {"id": "body-0094", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"), with $X = H$ and $Y = H'$. Recall from (5. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) that the DMD eigenvalues and modes are determined by the eigendecomposition of the operator with $U$, $\Sigma$, and $V$ defined as above. Comparing with (34 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")), we see that if one keeps all of the modes from ERA (i.e., choosing $r$ equal to the rank of $H$), then $A_{r}$ and $\overset{\sim}{A}$ are related by a similarity transform, with so $A_{r}$ and ${\overset{\sim}{A}}_{r}$ have the same eigenvalues.

<!-- chunk {"id": "body-0095", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

Furthermore, if $v$ is an eigenvector of $A_{r}$, with then $w = {\Sigma^{1/2}v}$ is an eigenvector of $\overset{\sim}{A}$, since Then $w$ can be used to construct either the exact or projected DMD modes (see (9. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")) and (6. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))).

<!-- chunk {"id": "body-0096", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

We see that algorithmically, the ERA and DMD are closely related: given two matrices $H$ and $H'$, applying the ERA produces a reduced-order operator $A_{r}$ that can be used to compute DMD modes and eigenvalues. However, the ERA was originally developed to characterize linear input-output systems, for which (33 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) approximates (30 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")). (In practice, it is often applied to experimental data, for which the underlying dynamics may be only approximately linear.) On the other hand, DMD is designed to analyze data generated by any dynamical system; the system can be nonlinear and may have inputs (e.g., $x_{k + 1} = {f{(x_{k},u_{k})}}$) or not (e.g., $x_{k + 1} = {f{(x_{k})}}$).

<!-- chunk {"id": "body-0097", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

We note that in the ERA, we collect two sets of data $\mathcal{H}$ and $\mathcal{H}'$, then arrange that data in matrices $H$ and $H'$. In doing so we are free to choose the values of $m_{c}$ and $m_{o}$, which determine the shapes of $H$ and $H'$ in (31 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) and (32 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")). Interpreting DMD using the Koopman formalism of Section 4.1, each column of $H$ corresponds to a particular value of an observable, where the observable function is a vector of outputs at $m_{o} + 1$ different timesteps. Each column of the matrix $H'$ then contains the value of this observable at the next timestep. A more typical application of DMD would use $m_{o} = 0$ and $m_{c} = {m - 1}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "The eigensystem realization algorithm (ERA)", "weight": 1.0} -->

Allowing for $m_{o} > 0$ is equivalent to appending the data matrices with rows of time-shifted Markov parameters. Doing so can enlarge the rank of $H$ and $H'$, increasing the accuracy of the reduced-order system (33 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) for the ERA. For DMD, it can overcome the rank limitations that prevent the correct characterization of standing waves (as suggested in Section 3.2.2).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Linear inverse modeling (LIM)", "weight": 1.0} -->

In this section, we investigate the connections between DMD and LIM. To set up this discussion, we briefly introduce and define a number of terms used in the climate science literature. This is followed by a more in-depth description of LIM. Finally, we show that under certain conditions, LIM and DMD are equivalent.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Nomenclature", "weight": 1.0} -->

*Empirical orthogonal functions* (EOFs) were first introduced in 1956 by Lorenz. Unique to the climate science literature, EOFs simply arise from the application of principal component analysis (PCA) to meteorological data. As a result, EOF analysis is equivalent to PCA, and thus also to POD and SVD. (We note that in PCA and and EOF analysis, the data mean is always subtracted, so that the results can be interpreted in terms of variances; this is often done for POD as well.)

<!-- chunk {"id": "body-0101", "role": "body", "section": "Nomenclature", "weight": 1.0} -->

In practice, EOFs are often used as a particular choice of *principal interaction patterns* (PIPs), a concept introduced in 1988 by Hasselmann. The following discussion uses notation similar to that found, which provides a nice review of PIP concepts. Consider a dynamical system with a high-dimensional state ${x{(t)}} \in {\mathbb{R}}^{n}$. In some cases, such a system may be approximately driven by a lower-dimensional system with state ${z{(t)}} \in {\mathbb{R}}^{r}$, where $r < n$. To be precise, we say that $x$ and $z$ are related as follows: where $\alpha$ is a vector of parameters. From this we see that given a knowledge of $z$ and its dynamics, $x$ is completely specified by the static map $P$, aside from the effects of noise.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Nomenclature", "weight": 1.0} -->

Though in general $P$ cannot be inverted, given a measurement of $x$, we can approximate $z$ using a least-squares fit: In climate science, the general approach of modeling the dynamics of a high-dimensional variable $x$ through a lower-dimensional variable $z$ is referred to as *inverse modeling*. The inverse model described above requires definitions of $F$, $P$, and $\alpha$. Generally, $F$ is chosen based on physical intuition. Once that choice is made, $P$ and $\alpha$ are fitted simultaneously. The PIPs are the columns of $P$ for the choice of $P$ (and $\alpha$) that minimizes the error where $E$ is the expected value operator. In general, the choice of $P$ is not unique.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Nomenclature", "weight": 1.0} -->

Hasselmann also introduced the notion of *principal oscillation patterns* (POPs) in his 1988 paper. Again, we use the notation found. Consider a system with unknown dynamics. We assume that we can approximate these dynamics with a linear system If we multiply both sides by $x_{k}^{T}$ and take expected values, we can solve for $A$ as The eigenvectors of $A$ are referred to as POPs. That is, POPs are eigenvectors of a particular linear approximation of otherwise unknown dynamics.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Nomenclature", "weight": 1.0} -->

Even within the climate science literature, there is some confusion between PIPs and POPs. This is due to the fact that POPs can be considered a special case of PIPs. In general, PIPs are basis vectors spanning a low-dimensional subspace useful for reduced-order modeling. Suppose we model our dynamics with the linear approximation described above, and do not reduce the order of the state. If we then express the model in its eigenvector basis, we are choosing our PIPs to be POPs.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Linear Markov models/linear inverse modeling (LIM)", "weight": 1.0} -->

In 1989, Penland derived a method for computing a linear, discrete-time system that approximates the trajectory of a stochastic, continuous-time, linear system, which he referred to as a linear Markov model. We describe this method, which came to be known as LIM, using the notation found. Consider an $n$-dimensional Markov process where $\xi{(t)}$ is white noise with covariance We assume the mean of the process has been removed. The covariance of $x$ is given by One can show that the following must hold: (See for details.)

<!-- chunk {"id": "body-0106", "role": "body", "section": "Linear Markov models/linear inverse modeling (LIM)", "weight": 1.0} -->

Defining the Green's function we can say that given a state $x{(t)}$, the most probable state time $\tau$ later is The operator $G{(\tau)}$ is computed from snapshots of the continuous-time system and has the same form as the linear approximation used in POP analysis (see (35 ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications"))). We note that we arrive at the same model if we apply linear stochastic estimation to snapshots of the state $x$, taking $x{(t)}$ and $x{({t + \tau})}$ to be the unconditional and conditional variables, respectively. (This was done in to identify a model for the evolution of POD coefficients in a fluid flow.)

<!-- chunk {"id": "body-0107", "role": "body", "section": "Linear Markov models/linear inverse modeling (LIM)", "weight": 1.0} -->

When this approach is applied to a nonlinear system, it can be shown that $G{(\tau)}$ is equivalent to a weighted average of the nonlinear dynamics, evaluated over an ensemble of snapshots. This is in contrast to a typical linearization, which involves evaluating the Jacobian of the dynamics at a fixed point. If the true dynamics are nearly linear, these two approaches will yield nearly the same model. However, if nonlinear effects are significant, $G{(\tau)}$ will be closer to the ensemble average, and arguably a better model than a traditional linearization.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Linear Markov models/linear inverse modeling (LIM)", "weight": 1.0} -->

In, this method was applied to compute a linear Markov model in the space of EOF coefficients. This is an example of inverse modeling (equivalently, PIP analysis); a high-dimensional variable is modeled via a projection onto a lower-dimensional EOF subspace. Due to the assumption of linear dynamics, this approach came to be known as *linear inverse modeling*. The combination of PIP and POP concepts in this early work has contributed to the continuing confusion between PIPs and POPs in the climate science literature today.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

In both exact and projected DMD, the DMD eigenvalues are given by the eigenvalues of the projected linear operator $\overset{\sim}{A}$ (see (4. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))). The projected DMD modes are computed by lifting the eigenvectors of $\overset{\sim}{A}$ to the original space via the left singular vectors $U$ (see (6. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications"))). In, the eigendecomposition of a low-order linear model $G{(\tau)}$ is computed and the low-order eigenvectors lifted to the original space via EOFs, in the same way as in projected DMD. The similarity in these two approaches is obvious. Recall that left singular vectors and EOFs are equivalent, so long as they are computed from the same data.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

Then to prove that LIM-based eigenvector analysis is equivalent to projected DMD, we simply have to show the equivalence of $G{(\tau)}$ and $\overset{\sim}{A}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

Consider two $n \times m$ data matrices $X$ and $Y$, with columns $x_{j} = x{(t_{j}}$) and $y_{j} = {x{({t_{j} + \tau})}}$, respectively. $X$ and $Y$ may or may not share columns. As in (3. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), we assume that the EOFs to be used for LIM are computed from $X$ alone, giving us where the columns of $U$ are the EOFs. The EOF coefficients of $X$ and $Y$ are given by whose columns we donote by ${\hat{x}}_{j}$ and ${\hat{y}}_{j}$, respectively.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

In order to show that $G{(\tau)}$ and $\overset{\sim}{A}$ are equivalent, we must reduce (4.3.2 ‣ 4.3. Linear inverse modeling (LIM) ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) to (4. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")). Because we are interested in the equivalence of LIM and projected DMD when the former is performed in the space of EOF coefficients, we replace all instances of $x$ in (36 ‣ 4.3. Linear inverse modeling (LIM) ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) and (4.3.2 ‣ 4.3. Linear inverse modeling (LIM) ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) with $\hat{x}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

Recall that the expected value of $a$, for an ensemble ${\{ a_{j}\}}_{j = 0}^{m - 1}$, is given by Then we can rewrite (36 ‣ 4.3. Linear inverse modeling (LIM) ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) as using the fact that ${XX^{\ast}U} = {U\Sigma^{2}}$, by the definition of left singular vectors. This result, along with (3. ‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), allows us to rewrite (4.3.2 ‣ 4.3. Linear inverse modeling (LIM) ‣ 4. Connections to other methods ‣ On dynamic mode decomposition: theory and applications")) as (Recall that ${x{({t_{j} + \tau})}} = y_{j}$, and ${x{(t_{j})}} = x_{j}$.) From (4.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

‣ 2.1. Standard definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications")), we then have ${G{(\tau)}} = \overset{\sim}{A}$, and we see that DMD and LIM are built on the same low-dimensional, approximating linear dynamics.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

We emphasize that this equivalence relies on a number of assumptions. First, we assume that we perform LIM in the space of EOF coefficients. Second, we assume that the EOFs are computed from $X$ alone. This may not be an intuitive choice if $X$ and $Y$ are completely distinct, but for a sequential snapshot sequence where $X$ and $Y$ differ by a single column, this is not a significant difference.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Equivalence to projected DMD", "weight": 1.0} -->

Given these assumptions, the equivalence of projected DMD and LIM gives us yet another way to interpret DMD analysis. If the data mean is removed, then the low-order map that generates the DMD eigenvalues and eigenvectors is simply the one that yields the statistically most likely state in the future. (This is the case for both exact and projected DMD, as both are built on the same low-order linear map.) In a small sense, the DMD framework is more general, as the intrepretation provided by Definition 1. ‣ 2.2. New definition ‣ 2. Theory ‣ On dynamic mode decomposition: theory and applications") holds even for data that are not mean-subtracted. Then again, in LIM the computation of the EOFs is completely divorced from the modeling procedure, allowing for a computation using both $X$ and $Y$. Nevertheless, the similarities between the two methods suggests that practitioners of DMD would be well-served in studying and learning from the climate science/LIM literature.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have presented a new definition in which DMD is defined to be the eigendecomposition of an approximating linear operator. Whereas existing DMD theory focuses on full-rank, sequential time series, our theory applies more generally to pairs of data vectors. At the same time, our DMD algorithm is only a slight modification of the commonly used, SVD-based DMD algorithm. It also preserves, and even strengthens, the links between DMD and Koopman operator theory. Thus our framework can be considered to be an extension of existing DMD theory to a more general class of datasets.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conclusions", "weight": 1.0} -->

For instance, when analyzing data generated by a dynamical system, we require only that the columns of the data matrices $X$ and $Y$ be related by the dynamics of interest, in a pairwise fashion. Unlike existing DMD algorithms, we do not require that the data come from uniform sampling of a single time series, nor do we require that the columns of $X$ and $Y$ overlap. We demonstrated the utility of this approach using two numerical examples. In the first, we sampled a trajectory nonuniformly, significantly reducing computational costs. In the second, we concatenated multiple datasets in a single DMD computation, effectively averaging out the effects of noise. Our generalized interpretation of DMD also proved useful in explaining the results of DMD computations involving rank-deficient datasets. Such computations may provide either meaningful or misleading information, depending on the dataset, and are not treated in the existing DMD literature.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, we showed that DMD is closely related to both the eigensystem realization algorithm (ERA) and linear inverse modeling (LIM). In fact, under certain conditions DMD and LIM are equivalent. We used the connection between DMD and the ERA to motivate a strategy for dealing with the inability of DMD to correctly characterize standing waves. An interesting future direction would be to explore whether or not lessons learned from past applications of LIM can similarly inform strategies for future applications of DMD.
