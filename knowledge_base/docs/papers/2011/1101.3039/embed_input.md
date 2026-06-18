<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Freedman's Inequality for Matrix Martingales

Topics include Matrix concentration, Martingales, Freedman inequality, Random matrices, Lieb theorem, Tail bounds, Probability inequalities.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives a sharp matrix-valued version of Freedman's martingale inequality using Lieb's concavity theorem rather than a more direct scalarization argument. The note is compact but important because it helped establish the modern matrix concentration toolkit for dependent matrix-valued processes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Freedman's inequality is a martingale counterpart to Bernstein's inequality. This result shows that the large-deviation behavior of a martingale is controlled by the predictable quadratic variation and a uniform upper bound for the martingale difference sequence. Oliveira has recently established a natural extension of Freedman's inequality that provides tail bounds for the maximum singular value of a matrix-valued martingale. This note describes a different proof of the matrix Freedman inequality that depends on a deep theorem of Lieb from matrix analysis. This argument delivers sharp constants in the matrix Freedman inequality, and it also yields tail bounds for other types of matrix martingales. The new techniques are adapted from recent work by the present author.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

Freedman's inequality is a martingale counterpart to Bernstein's inequality. This result shows that the large-deviation behavior of a martingale is controlled by the predictable quadratic variation and a uniform upper bound for the martingale difference sequence. Oliveira has recently established a natural extension of Freedman's inequality that provides tail bounds for the maximum singular value of a matrix-valued martingale. This note describes a different proof of the matrix Freedman inequality that depends on a deep theorem of Lieb from matrix analysis. This argument delivers sharp constants in the matrix Freedman inequality, and it also yields tail bounds for other types of matrix martingales. The new techniques are adapted from recent work by the present author.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Key words and phrases", "weight": 1.0} -->

Discrete-time martingale, large deviation, probability inequality, random matrix, sum of independent random variables

<!-- chunk {"id": "body-0006", "role": "body", "section": "Key words and phrases", "weight": 1.0} -->

2010 Mathematics Subject Classification. Primary: 60B20. Secondary: 60F10, 60G50, 60G42

<!-- chunk {"id": "body-0007", "role": "body", "section": "Key words and phrases", "weight": 1.0} -->

JAT is with Computing & Mathematical Sciences, MC 305-16, California Inst. Technology, Pasadena, CA 91125. E-mail: jtropp@acm.caltech.edu. Research supported by ONR award N00014-08-1-0883, DARPA award N66001-08-1-2065, and AFOSR award FA9550-09-1-0643.

<!-- chunk {"id": "body-0008", "role": "body", "section": "An Introduction to Freedman's Inequality", "weight": 1.0} -->

The Freedman inequality \[, Thm. (1.6)\] is a martingale extension of the Bernstein inequality. This result demonstrates that a martingale exhibits normal-type concentration near its mean value on a scale determined by the predictable quadratic variation, and the upper tail has Poisson-type decay on a scale determined by a uniform bound on the difference sequence.

<!-- chunk {"id": "body-0009", "role": "body", "section": "An Introduction to Freedman's Inequality", "weight": 1.0} -->

Oliveira \[, Thm. 1.2\] proves that Freedman's inequality extends, in a certain form, to the matrix setting. The purpose of this note is to demonstrate that the methods from the author's paper can be used to establish a sharper version of the matrix Freedman inequality. Furthermore, this approach offers a transparent way to obtain other probability inequalities for adapted sequences.

<!-- chunk {"id": "body-0010", "role": "body", "section": "An Introduction to Freedman's Inequality", "weight": 1.0} -->

Let us introduce some notation and background on martingales so that we can state Freedman's original result rigorously. Afterward, we continue with a statement of our main results and a presentation of the methods that we need to prove the matrix generalization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Martingales", "weight": 1.0} -->

Let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space, and let $\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \cdots \subset \mathcal{F}$ be a filtration of the master sigma algebra. We write ${\mathbb{E}}_{k}$ for the expectation conditioned on $\mathcal{F}_{k}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Martingales", "weight": 1.0} -->

Roughly, the present value of a martingale depends only on the past values, and the martingale has the status quo property: today, on average, is the same as yesterday.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Freedman's Inequality", "weight": 1.0} -->

Freedman uses a powerful stopping-time argument to establish the following theorem for scalar martingales \[, Thm. (1.6)\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Matrix Martingales", "weight": 1.0} -->

Matrix martingales are defined in much the same manner as scalar martingales. Consider a random process $\{{\mathbf{Y}}_{k}:{k = {0,1,2,\ldots}}\}$ whose values are matrices of finite dimension. We say that the process is a *matrix martingale* when

<!-- chunk {"id": "body-0015", "role": "body", "section": "Matrix Martingales", "weight": 1.0} -->

We write $\left. \parallel \cdot \parallel \right.$ for the *spectral norm*, which coincides with the operator norm between Hilbert spaces. As before, we assume that ${\mathbf{Y}}_{0} = \mathbf{0}$, and we define the difference sequence $\{{\mathbf{X}}_{k}:{k = {1,2,3,\ldots}}\}$ via the relation

<!-- chunk {"id": "body-0016", "role": "body", "section": "Matrix Martingales", "weight": 1.0} -->

A matrix-valued random process is a martingale if and only if we obtain a scalar martingale when we track each fixed coordinate in time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Freedman's Inequality for Matrices", "weight": 1.0} -->

In the elegant paper, Oliveira establishes that it is possible to extend Freedman's inequality to the matrix setting. He studies martingales that take self-adjoint matrix values, and he shows that the *maximum eigenvalue* of the martingale satisfies a result very similar to Freedman's inequality. The uniform bound $R$ and the predictable quadratic variation $\{ W_{k}\}$ are replaced by natural noncommutative extensions. As a consequence, these results have powerful applications in random matrix theory.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Freedman's Inequality for Matrices", "weight": 1.0} -->

In this note, we establish a sharper version of Oliveira's theorem \[, Thm. 1.2\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Tools and Techniques", "weight": 1.0} -->

In his paper, Oliveira describes a way to transport Freedman's stopping-time argument to the matrix setting. The main technical obstacle is to control the evolution of the moment generating function (mgf) of the matrix martingale. Oliveira accomplishes this task using an insightful variation on a idea due to Ahlswede and Winter \[, App.\]. This method, however, does not result in the sharpest bounds on the matrix mgf.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Tools and Techniques", "weight": 1.0} -->

This note demonstrates that the ideas allow us to obtain the sharp estimates for the mgf with minimal effort. Our main tool is a deep theorem \[, Thm. 6\] of Lieb.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Tail Bounds via Martingale Methods", "weight": 1.0} -->

In this section, we show that Freedman's techniques extend to the matrix setting with minor (but profound) changes. The key idea is to use Corollary 1.5. ‣ 1.5. Tools and Techniques ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") to control the evolution of a matrix version of the moment generating function. This argument culminates in a rather general theorem on the large deviation behavior of an adapted sequence of random matrices. In §3, we specialize this result to obtain Freedman's inequality.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Additional Terminology", "weight": 1.0} -->

We say that a sequence $\{{\mathbf{X}}_{k}\}$ of random matrices is *adapted* to the filtration when each ${\mathbf{X}}_{k}$ is measurable with respect to $\mathcal{F}_{k}$. Loosely speaking, an adapted sequence is one where the present depends only upon the past. We say that a sequence $\{{\mathbf{V}}_{k}\}$ of random matrices is *previsible* when each ${\mathbf{V}}_{k}$ is measurable with respect to $\mathcal{F}_{k - 1}$. In particular, the sequence $\{{{\mathbb{E}}_{k - 1}{\mathbf{X}}_{k}}\}$ of conditional expectations of an adapted sequence $\{{\mathbf{X}}_{k}\}$ is previsible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Additional Terminology", "weight": 1.0} -->

In words, we can determine if the stopping time has arrived from current and past experience.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

Consider an adapted random process $\{{\mathbf{X}}_{k}:{k = {1,2,3,\ldots}}\}$ and a previsible random process $\{{\mathbf{V}}_{k}:{k = {1,2,3,\ldots}}\}$ whose values are self-adjoing matrices with dimension $d$. Suppose that the two processes are connected through a relation of the form

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

where the function $g:{{(0,\infty)}\rightarrow{\lbrack 0,\infty\rbrack}}$. The left-hand side should be interpreted as a conditional cumulant generating function (cgf); see \[, Sec. 3.1\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

The random matrix ${\mathbf{W}}_{k}$ can be viewed as a measure of the total variability of the process $\{{\mathbf{X}}_{k}\}$ up to time $k$. The partial sum ${\mathbf{Y}}_{k}$ is unlikely to be large unless ${\mathbf{W}}_{k}$ is also large.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

To continue, we fix the function $g$ and a positive number $\theta$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

We use the function $G_{\theta}$ to construct a real-valued random process.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Large Deviation Supermartingale", "weight": 1.0} -->

This process is an evolving measure of the discrepancy between the partial sum process $\{{\mathbf{Y}}_{k}\}$ and the cumulant sum process $\{{\mathbf{W}}_{k}\}$. The following lemma describes the key properties of this random sequence. In particular, the average discrepancy decreases with time.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Tail Bound for Adapted Sequences", "weight": 1.0} -->

Our key theorem for adapted sequences provides a bound on the probability that the partial sum of a matrix-valued random process is large. In the next section, we apply this result to establish a stronger version of Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"). This result also allows us to develop other types of probability inequalities for adapted sequences of random matrices; see the technical report for additional details.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Demonstration of Theorem 3.1", "weight": 1.0} -->

We conclude with the proof of Theorem 3.1. The argument depends on the following estimate for the moment generating function of a zero-mean random matrix whose eigenvalues are uniformly bounded. See \[, Lem. 6.7\] for the proof.
