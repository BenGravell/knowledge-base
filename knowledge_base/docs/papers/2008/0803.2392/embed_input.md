<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples

Topics include Compressed sensing, Sparse recovery, Greedy algorithms, Signal reconstruction, CoSaMP, Error bounds.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces CoSaMP, a greedy sparse-recovery algorithm with provable accuracy, stability, and runtime guarantees under standard compressed-sensing assumptions. It combines matching-pursuit style support identification with least-squares refinement and pruning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compressive sampling offers a new paradigm for acquiring signals that are compressible with respect to an orthonormal basis. The major algorithmic challenge in compressive sampling is to approximate a compressible signal from noisy samples. This paper describes a new iterative recovery algorithm called CoSaMP that delivers the same guarantees as the best optimization-based approaches. Moreover, this algorithm offers rigorous bounds on computational cost and storage. It is likely to be extremely efficient for practical problems because it requires only matrix-vector multiplies with the sampling matrix. For many cases of interest, the running time is just O(N*log^2(N)), where N is the length of the signal.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most signals of interest contain scant information relative to their ambient dimension, but the classical approach to signal acquisition ignores this fact. We usually collect a complete representation of the target signal and process this representation to sieve out the actionable information. Then we discard the rest. Contemplating this ugly inefficiency, one might ask if it is possible instead to acquire *compressive samples*. In other words, is there some type of measurement that automatically winnows out the information from a signal? Incredibly, the answer is sometimes yes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Compressive sampling* refers to the idea that, for certain types of signals, a small number of nonadaptive samples carries sufficient information to approximate the signal well. Research in this area has two major components:: How many samples are necessary to reconstruct signals to a specified precision? What type of samples? How can these sampling schemes be implemented in practice?: Given the compressive samples, what algorithms can efficiently construct a signal approximation?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The literature already contains a well-developed theory of sampling, which we summarize below. Although algorithmic work has been progressing, the state of knowledge is less than complete. We assert that a practical signal reconstruction algorithm should have all of the following properties.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should accept samples from a variety of sampling schemes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should succeed using a minimal number of samples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should be robust when samples are contaminated with noise.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should provide optimal error guarantees for every target signal.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should offer provably efficient resource usage.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To our knowledge, no approach in the literature simultaneously accomplishes all five goals.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents and analyzes a novel signal reconstruction algorithm that achieves these desiderata. The algorithm is called CoSaMP, from the acrostic *Compressive Sampling Matching Pursuit*. As the name suggests, the new method is ultimately based on orthogonal matching pursuit (OMP), but it incorporates several other ideas from the literature to accelerate the algorithm and to provide strong guarantees that OMP cannot. Before we describe the algorithm, let us deliver an introduction to the theory of compressive sampling.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

To enhance intuition, we focus on sparse and compressible signals. For vectors in ${\mathbb{C}}^{N}$, define the $\ell_{0}$ quasi-norm We say that a signal $\mathbf{x}$ is *$s$-sparse* when $\left\| {\mathbf{x}} \right\|_{0} \leq s$. Sparse signals are an idealization that we do not encounter in applications, but real signals are quite often *compressible*, which means that their entries decay rapidly when sorted by magnitude. As a result, compressible signals are well approximated by sparse signals. We can also talk about signals that are compressible with respect to other orthonormal bases, such as a Fourier or wavelet basis. In this case, the sequence of coefficients in the orthogonal expansion decays quickly. It represents no loss of generality to focus on signals that are compressible with respect to the standard basis, and we do so without regret. For a more precise definition of compressibility, turn to Section 2.6.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

In the theory of compressive sampling, a *sample* is a linear functional applied to a signal. The process of collecting multiple samples is best viewed as the action of a *sampling matrix* $\mathbf{\Phi}$ on the target signal. If we take $m$ samples, or *measurements*, of a signal in ${\mathbb{C}}^{N}$, then the sampling matrix $\mathbf{\Phi}$ has dimensions $m \times N$. A natural question now arises: How many measurements are necessary to acquire $s$-sparse signals?

<!-- chunk {"id": "body-0016", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

The minimum number of measurements $m \geq {2s}$ on account of the following simple argument. The sampling matrix must not map two different $s$-sparse signals to the same set of samples. Therefore, each collection of $2s$ columns from the sampling matrix must be nonsingular. It is easy to see that certain Vandermonde matrices satisfy this property, but these matrices are not really suitable for signal acquisition because they contain square minors that are very badly conditioned. As a result, some sparse signals are mapped to very similar sets of samples, and it is unstable to invert the sampling process numerically.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

Instead, Candès and Tao proposed the stronger condition that the geometry of sparse signals should be preserved under the action of the sampling matrix. To quantify this idea, they defined the $r$th *restricted isometry constant* of a matrix $\mathbf{\Phi}$ as the least number $\delta_{r}$ for which We have written $\left. \parallel \cdot \parallel{}_{2} \right.$ for the $\ell_{2}$ vector norm. When $\delta_{r} < 1$, these inequalities imply that each collection of $r$ columns from $\mathbf{\Phi}$ is nonsingular, which is the minimum requirement for acquiring $({r/2})$-sparse signals. When $\delta_{r} \ll 1$, the sampling operator very nearly maintains the $\ell_{2}$ distance between each pair of $({r/2})$-sparse signals. In consequence, it is possible to invert the sampling process stably.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

To acquire $s$-sparse signals, one therefore hopes to achieve a small restricted isometry constant $\delta_{2s}$ with as few samples as possible. A striking fact is that many types of random matrices have excellent restricted isometry behavior. For example, we can often obtain $\delta_{2s} \leq 0.1$ with measurements, where $\alpha$ is a small integer. Unfortunately, no deterministic sampling matrix is known to satisfy a comparable bound. Even worse, it is computationally difficult to check the inequalities (1.1), so it may never be possible to exhibit an explicit example of a good sampling matrix.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

As a result, it is important to understand how random sampling matrices behave. The two quintessential examples are Gaussian matrices and partial Fourier matrices.: If the entries of $\sqrt{m}\mathbf{\Phi}$ are independent and identically distributed standard normal variables then except with probability $e^{- {cm}}$. See for details.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

Partial Fourier matrices:: If $\sqrt{m}\mathbf{\Phi}$ is a uniformly random set of $m$ rows drawn from the $N \times N$ unitary discrete Fourier transform (DFT), then except with probability $N^{- 1}$. See for the proof. Experts believe that the power on the first logarithm should be no greater than two.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

Here and elsewhere, we follow the analyst's convention that upright letters ($c,C,\ldots$) refer to positive, universal constants that may change from appearance to appearance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

The Gaussian matrix is important because it has optimal restricted isometry behavior. Indeed, for any $m \times N$ matrix, on account of profound geometric results of Kashin and Garnaev--Gluskin. Even though partial Fourier matrices may require additional samples to achieve a small restricted isometry constant, they are more interesting for the following reasons.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

There are technologies that acquire random Fourier measurements at unit cost per sample.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

The sampling matrix can be applied to a vector in time $O{({N{\log N}})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

The sampling matrix requires only $O{({m{\log N}})}$ storage.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Rudiments of Compressive Sampling", "weight": 1.0} -->

Other types of sampling matrices, such as the *random demodulator*, enjoy similar qualities. These traits are essential for the translation of compressive sampling from theory into practice.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Signal Recovery Algorithms", "weight": 1.0} -->

The major algorithmic challenge in compressive sampling is to approximate a signal given a vector of noisy samples. The literature describes a huge number of approaches to solving this problem. They fall into three rough categories:: These methods build up an approximation one step at a time by making locally optimal choices at each step. Examples include OMP, stagewise OMP (StOMP), and regularized OMP (ROMP).: These techniques solve a convex program whose minimizer is known to approximate the target signal. Many algorithms have been proposed to complete the optimization, including interior-point methods, projected gradient methods, and iterative thresholding.: These methods acquire highly structured samples of the signal that support rapid reconstruction via group testing. This class includes Fourier sampling, chaining pursuit, and HHS pursuit, as well as some algorithms of Cormode--Muthukrishnan and Iwen.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Signal Recovery Algorithms", "weight": 1.0} -->

At present, each type of algorithm has its native shortcomings. Many of the combinatorial algorithms are extremely fast---sublinear in the length of the target signal---but they require a large number of somewhat unusual samples that may not be easy to acquire. At the other extreme, convex relaxation algorithms succeed with a very small number of measurements, but they tend to be computationally burdensome. Greedy pursuits---in particular, the ROMP algorithm---are intermediate in their running time and sampling efficiency.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Signal Recovery Algorithms", "weight": 1.0} -->

CoSaMP, the algorithm described in this paper, is at heart a greedy pursuit. It also incorporates ideas from the combinatorial algorithms to guarantee speed and to provide rigorous error bounds. The analysis is inspired by the work on ROMP and the work of Candès--Romberg--Tao on convex relaxation methods. In particular, we establish the following result.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Organization", "weight": 1.0} -->

The rest of the paper has the following structure. In Section 2 we introduce the CoSaMP algorithm, we state the major theorems in more detail, and we discuss implementation and resource requirements. Section 3 describes some consequences of the restricted isometry property that pervade our analysis. The central theorem is established for sparse signals in Sections 4 and 5. We extend this result to general signals in Section 6. Finally, Section 7 places the algorithm in the context of previous work. The first appendix presents variations on the algorithm. The second appendix contains a bound on the number of iterations required when the algorithm is implemented using exact arithmetic.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The CoSaMP Algorithm", "weight": 1.0} -->

This section gives an overview of the algorithm, along with explicit pseudocode. It presents the major theorems on the performance of the algorithm. Then it covers details of implementation and bounds on resource requirements.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Intuition", "weight": 1.0} -->

The most difficult part of signal reconstruction is to identify the locations of the largest components in the target signal. CoSaMP uses an approach inspired by the restricted isometry property. Suppose that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{s} \ll 1$. For an $s$-sparse signal $\mathbf{x}$, the vector ${\mathbf{y}} = {\mathbf{\Phi}^{\ast}\mathbf{\Phi}{\mathbf{x}}}$ can serve as a proxy for the signal because the energy in each set of $s$ components of $\mathbf{y}$ approximates the energy in the corresponding $s$ components of $\mathbf{x}$. In particular, the largest $s$ entries of the proxy $\mathbf{y}$ point toward the largest $s$ entries of the signal $\mathbf{x}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Intuition", "weight": 1.0} -->

Since the samples have the form ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$, we can obtain the proxy just by applying the matrix $\mathbf{\Phi}^{\ast}$ to the samples.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Intuition", "weight": 1.0} -->

The algorithm invokes this idea iteratively to approximate the target signal. At each iteration, the current approximation induces a residual, the part of the target signal that has not been approximated. As the algorithm progresses, the samples are updated so that they reflect the current residual. These samples are used to construct a proxy for the residual, which permits us to identify the large components in the residual. This step yields a tentative support for the next approximation. We use the samples to estimate the approximation on this support set using least squares. This process is repeated until we have found the recoverable energy in the signal.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Overview", "weight": 1.0} -->

As input, the CoSaMP algorithm requires four pieces of information: Access to the sampling operator via matrix--vector multiplication.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Overview", "weight": 1.0} -->

A vector of (noisy) samples of the unknown signal.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Overview", "weight": 1.0} -->

The sparsity of the approximation to be produced.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Overview", "weight": 1.0} -->

The algorithm is initialized with a trivial signal approximation, which means that the initial residual equals the unknown target signal. During each iteration, CoSaMP performs five major steps: Identification. The algorithm forms a proxy of the residual from the current samples and locates the largest components of the proxy.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Overview", "weight": 1.0} -->

Support Merger. The set of newly identified components is united with the set of components that appear in the current approximation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Overview", "weight": 1.0} -->

Estimation. The algorithm solves a least-squares problem to approximate the target signal on the merged set of components.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Overview", "weight": 1.0} -->

Pruning. The algorithm produces a new approximation by retaining only the largest entries in this least-squares signal approximation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Overview", "weight": 1.0} -->

Sample Update. Finally, the samples are updated so that they reflect the residual, the part of the signal that has not been approximated.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Overview", "weight": 1.0} -->

These steps are repeated until the halting criterion is triggered. In the body of this work, we concentrate on methods that use a fixed number of iterations. Appendix A discusses some other simple stopping rules that may also be useful in practice.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Overview", "weight": 1.0} -->

Pseudocode for CoSaMP appears as Algorithm 2.1. This code describes the version of the algorithm that we analyze in this paper. Nevertheless, there are several adjustable parameters that may improve performance: the number of components selected in the identification step and the number of components retained in the pruning step. For a brief discussion of other variations on the algorithm, turn to Appendix A.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Overview", "weight": 1.0} -->

CoSaMP(Φ, u, s) Input: Sampling matrix Φ, noisy sample vector u, sparsity level s Output: An s-sparse approximation a of the target signal a0 ← 0 { Trivial initial approximation } v ← u { Current samples = input samples } k ← 0 repeat k ← k + 1 y ← Φ* v { Form signal proxy } Ω ← supp(y2 s) { Identify large components } T ← Ω ∪ supp(ak − 1) { Merge supports } b|T ← ΦT† u { Signal estimation by least-squares } b|Tc ← 0 ak ← bs { Prune to obtain next approximation } v ← u − Φ ak { Update current samples } until halting criterion true Algorithm 2.1 CoSaMP Recovery Algorithm

<!-- chunk {"id": "body-0046", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

This section describes our theoretical analysis of the behavior of CoSaMP. The next section covers the resource requirements of the algorithm. Afterward, Section 2.5 combines these materials to establish Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples").

<!-- chunk {"id": "body-0047", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Our results depend on a set of hypotheses that has become common in the compressive sampling literature. Let us frame the standing assumptions: CoSaMP Hypotheses • The sparsity level $s$ is fixed. • The $m \times N$ sampling operator $\mathbf{\Phi}$ has restricted isometry constant $\delta_{4s} \leq 0.1$.\• The signal ${\mathbf{x}} \in {\mathbb{C}}^{N}$ is arbitrary, except where noted. • The noise vector ${\mathbf{e}} \in {\mathbb{C}}^{m}$ is arbitrary. • The vector of samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

We also define the *unrecoverable energy* $\nu$ in the signal. This quantity measures the baseline error in our approximation that occurs because of noise in the samples or because the signal is not sparse.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Our key result is that CoSaMP makes significant progress during each iteration where the approximation error is large relative to the unrecoverable energy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

In the hypotheses, a bound on the restricted isometry constant $\delta_{2s}$ also suffices. Indeed, Corollary 3.4 of the sequel implies that $\delta_{4s} \leq 0.1$ holds whenever $\delta_{2s} \leq 0.025$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2.4", "weight": 1.0} -->

The expression (2.1) for the unrecoverable energy can be simplified using Lemma 7, which states that, for every signal ${\mathbf{y}} \in {\mathbb{C}}^{N}$ and every positive integer $t$, we have Choosing ${\mathbf{y}} = {{\mathbf{x}} - {\mathbf{x}}_{s/2}}$ and $t = {s/2}$, we reach In words, the unrecoverable energy is controlled by the scaled $\ell_{1}$ norm of the signal tail.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

CoSaMP was designed to be a practical method for signal recovery. An efficient implementation of the algorithm requires some ideas from numerical linear algebra, as well as some basic techniques from the theory of algorithms. This section discusses the key issues and develops an analysis of the running time for the two most common scenarios.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

We focus on the least-squares problem in the estimation step because it is the major obstacle to a fast implementation of the algorithm. The algorithm guarantees that the matrix $\mathbf{\Phi}_{T}$ never has more than $3s$ columns, so our assumption $\delta_{4s} \leq 0.1$ implies that the matrix $\mathbf{\Phi}_{T}$ is extremely well conditioned. As a result, we can apply the pseudoinverse $\mathbf{\Phi}_{T}^{\dagger} = {{({\mathbf{\Phi}_{T}^{\ast}\mathbf{\Phi}_{T}})}^{- 1}\mathbf{\Phi}_{T}^{\ast}}$ very quickly using an iterative method, such as Richardson's iteration \[1, Sec. 7.2.3\] or conjugate gradient \[1, Sec. 7.4\].

<!-- chunk {"id": "body-0054", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

These techniques have the additional advantage that they only interact with the matrix $\mathbf{\Phi}_{T}$ through its action on vectors. It follows that the algorithm performs better when the sampling matrix has a fast matrix--vector multiply.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

Section 5 contains an analysis of the performance of iterative least-squares algorithms in the context of CoSaMP. In summary, if we initialize the least-squares method with the current approximation ${\mathbf{a}}^{k - 1}$, then the cost of solving the least-squares problem is $O{(\mathcal{L})}$, where $\mathcal{L}$ bounds the cost of a matrix--vector multiply with $\mathbf{\Phi}_{T}$ or $\mathbf{\Phi}_{T}^{\ast}$. This implementation ensures that Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds at each iteration.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

We emphasize that direct methods for least squares are likely to be extremely inefficient in this setting. The first reason is that each least-squares problem may contain substantially different sets of columns from $\mathbf{\Phi}$. As a result, it becomes necessary to perform a completely new QR or SVD factorization during each iteration at a cost of $O{({s^{2}m})}$. The second problem is that computing these factorizations typically requires direct access to the columns of the matrix, which is problematic when the matrix is accessed through its action on vectors. Third, direct methods have storage costs $O{({sm})}$, which may be deadly for large-scale problems.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

The remaining steps of the algorithm are standard. Let us estimate the operation counts.: Forming the proxy is dominated by the cost of the matrix--vector multiply $\mathbf{\Phi}^{\ast}{\mathbf{v}}$.: We can locate the largest $2s$ entries of a vector in time $O{(N)}$ using the approach in \[8, Ch. 9\]. In practice, it may be faster to sort the entries of the signal in decreasing order of magnitude at cost $O{({N{\log N}})}$ and then select the first $2s$ of them. The latter procedure can be accomplished with quicksort, mergesort, or heapsort \[8, Sec. II\]. To implement the algorithm to the letter, the sorting method needs to be stable because we stipulate that ties are broken lexicographically. This point is not important in practice.: We can merge two sets of size $O{(s)}$ in expected time $O{(s)}$ using randomized hashing methods \[8, Ch. 11\].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

One can also sort both sets first and use the elementary merge procedure \[8, p. 29\] for a total cost $O{({s{\log s}})}$.: We use Richardson's iteration or conjugate gradient to compute $\mathbf{\Phi}_{T}^{\dagger}{\mathbf{u}}$. Initializing the least-squares algorithm requires a matrix--vector multiply with $\mathbf{\Phi}_{T}^{\ast}$. Each iteration of the least-squares method requires one matrix--vector multiply each with $\mathbf{\Phi}_{T}$ and $\mathbf{\Phi}_{T}^{\ast}$. Since $\mathbf{\Phi}_{T}$ is a submatrix of $\mathbf{\Phi}$, the matrix--vector multiplies can also be obtained from multiplication with the full matrix. We prove in Section 5 that a constant number of least-squares iterations suffices for Theorem 2.1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") to hold.: This step is similar to identification. Pruning can be implemented in time $O{(s)}$, but it may be preferable to sort the components of the vector by magnitude and then select the first $s$ at a cost of $O{({s{\log s}})}$.: This step is dominated by the cost of the multiplication of $\mathbf{\Phi}$ with the $s$-sparse vector ${\mathbf{a}}^{k}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

Table 1 summarizes this discussion in two particular cases. The first column shows what happens when the sampling matrix $\mathbf{\Phi}$ is applied to vectors in the standard way, but we have random access to submatrices. The second, column shows what happens when the sampling matrix $\mathbf{\Phi}$ and its adjoint $\mathbf{\Phi}^{\ast}$ both have a fast multiply with cost $\mathcal{L}$, where we assume that $\mathcal{L} \geq N$. A typical value is $\mathcal{L} = {O{({N{\log N}})}}$. In particular, a partial Fourier matrix satisfies this bound.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

Total per iteration Table 1. Operation count for CoSaMP. Big-O notation is omitted for legibility. The dimensions of the sampling matrix Φ are m × N; the sparsity level is s. The number ℒ bounds the cost of a matrix–vector multiply with Φ or Φ*.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

Finally, we note that the storage requirements of the algorithm are also favorable. Aside from the storage required by the sampling matrix, the algorithm constructs only one vector of length $N$, the signal proxy. The sample vectors $\mathbf{u}$ and $\mathbf{v}$ have length $m$, so they require $O{(m)}$ storage. The signal approximations can be stored using sparse data structures, so they require at most $O{({s{\log N}})}$ storage. Similarly, the index sets that appear require only $O{({s{\log N}})}$ storage. The total storage is $O{(N)}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Implementation and Resource Requirements", "weight": 1.0} -->

The following result summarizes this discussion.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 2.6", "weight": 1.0} -->

We have been able to show that Theorem 2.2. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds when the least-squares problems are solved iteratively with a delicately chosen stopping threshold. In this case, the total number of least-squares iterations performed over the entire execution of the algorithm is at most $O{({\log{({\left\| \mathbf{x} \right\|_{2}/\eta})}})}$ if we wish to achieve error $O{({\eta + \nu})}$. When the cost of forming the signal proxy is much higher than the cost of solving the least-squares problem, this analysis may yield a sharper result. For example, using standard matrix--vector multiplication, we have a runtime bound The first term reflects the number of CoSaMP iterations times the cost of forming the signal proxy. The second term reflects the total cost of the least-squares iterations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 2.6", "weight": 1.0} -->

Unless the relative precision $\left\| \mathbf{x} \right\|_{2}/\eta$ is superexponential in the signal length, we obtain running time $O{({smN})}$. This bound is comparable with the worst-case cost of OMP or ROMP. As we discuss in Appendix B, the number of CoSaMP iterations may be much smaller than $s$, which also improves the estimate.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

Since the unrecoverable energy $\nu$ plays a central role in our analysis of CoSaMP, it merits some additional discussion. In particular, it is informative to examine the unrecoverable energy in a compressible signal. Let $p$ be a number in the interval $$. We say that $\mathbf{x}$ is *$p$-compressible* with magnitude $R$ if the sorted components of the signal decay at the rate When $p = 1$, this definition implies that $\left\| {\mathbf{x}} \right\|_{1} \leq {R \cdot {({1 + {\log N}})}}$. Therefore, the unit ball of $1$-compressible signals is similar to the $\ell_{1}$ unit ball. When $p \approx 0$, this definition implies that $p$-compressible signals are very nearly sparse.

<!-- chunk {"id": "body-0067", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

In general, compressible signals are well approximated by sparse signals: where $C_{p} = {({{1/p} - 1})}^{- 1}$ and $D_{p} = {({{2/p} - 1})}^{- {1/2}}$. These results follow by writing each norm as a sum and approximating the sum with an integral. We see that the unrecoverable energy (2.1) in a $p$-compressible signal is bounded as When $p$ is small, the first term in the unrecoverable energy decays rapidly as the sparsity level $s$ increases. For the class of $p$-compressible signals, the bound (2.3) on the unrecoverable energy is sharp, modulo the exact values of the constants.

<!-- chunk {"id": "body-0068", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

With these inequalities, we can see that CoSaMP recovers compressible signals efficiently. Let us calculate the number of iterations required to reduce the approximation error from $\left\| {\mathbf{x}} \right\|_{2}$ to the optimal level (2.3). For compressible signals, the energy $\left\| {\mathbf{x}} \right\|_{2} \leq {2R}$, so Therefore, the number of iterations required to recover a generic $p$-compressible signal is $O{({\log s})}$, where the constant in the big-O notation depends on $p$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

The term "unrecoverable energy" is justified by several facts. First, we must pay for the $\ell_{2}$ error contaminating the samples. To check this point, define $S = {{supp}{({\mathbf{x}}_{s})}}$. The matrix $\mathbf{\Phi}_{S}$ is nearly an isometry from $\ell_{2}^{S}$ to $\ell_{2}^{m}$, so an error in the large components of the signal induces an error of equivalent size in the samples. Clearly, we can never resolve this uncertainty.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

The term $s^{- {1/2}}\left\| {{\mathbf{x}} - {\mathbf{x}}_{s}} \right\|_{1}$ is also required on account of classical results about the Gel'fand widths of the $\ell_{1}^{N}$ ball in $\ell_{2}^{N}$, due to Kashin and Garnaev--Gluskin. In the language of compressive sampling, their work has the following interpretation. Let $\mathbf{\Phi}$ be a fixed $m \times N$ sampling matrix.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The Unrecoverable Energy", "weight": 1.0} -->

Suppose that, for every signal ${\mathbf{x}} \in {\mathbb{C}}^{N}$, there is an algorithm that uses the samples ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$ to construct an approximation $\mathbf{a}$ that achieves the error bound Then the number $m$ of measurements must satisfy $m \geq {cs{\log{({N/s})}}}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Restricted Isometry Consequences", "weight": 1.0} -->

When the sampling matrix satisfies the restricted isometry inequalities (1.1), it has several other properties that we require repeatedly in the proof that the CoSaMP algorithm is correct. Our first observation is a simple translation of (1.1) into other terms.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Iteration Invariant: Sparse Case", "weight": 1.0} -->

We now commence the proof of Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). For the moment, let us assume that the signal is actually sparse. Section 6 removes this assumption.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Iteration Invariant: Sparse Case", "weight": 1.0} -->

The result states that each iteration of the algorithm reduces the approximation error by a constant factor, while adding a small multiple of the noise. As a consequence, when the approximation error is large in comparison with the noise, the algorithm makes substantial progress in identifying the unknown signal.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Approximations, Residuals, etc", "weight": 1.0} -->

Fix an iteration $k \geq 1$. We write ${\mathbf{a}} = {\mathbf{a}}^{k - 1}$ for the signal approximation at the beginning of the iteration. Define the residual ${\mathbf{r}} = {{\mathbf{x}} - {\mathbf{a}}}$, which we interpret as the part of the signal we have not yet recovered. Since the approximation $\mathbf{a}$ is always $s$-sparse, the residual $\mathbf{r}$ must be $2s$-sparse.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Identification", "weight": 1.0} -->

The identification phase produces a set of components where the residual signal still has a lot of energy.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Support Merger", "weight": 1.0} -->

The next step of the algorithm merges the support of the current signal approximation $\mathbf{a}$ with the newly identified set of components. The following result shows that components of the signal $\mathbf{x}$ outside this set have very little energy.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Estimation", "weight": 1.0} -->

The estimation step of the algorithm solves a least-squares problem to obtain values for the coefficients in the set $T$. We need a bound on the error of this approximation.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Pruning", "weight": 1.0} -->

The final step of each iteration is to prune the intermediate approximation to its largest $s$ terms. The following lemma provides a bound on the error in the pruned approximation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Analysis of Iterative Least-squares", "weight": 1.0} -->

To develop an efficient implementation of CoSaMP, it is critical to use an iterative method when we solve the least-squares problem in the estimation step. The two natural choices are Richardson's iteration and conjugate gradient. The efficacy of these methods rests on the assumption that the sampling operator has small restricted isometry constants. Indeed, since the set $T$ constructed in the support merger step contains at most $3s$ components, the hypothesis $\delta_{4s} \leq 0.1$ ensures that the condition number This condition number is closely connected with the performance of Richardson's iteration and conjugate gradient. In this section, we show that Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds if we perform a constant number of iterations of either least-squares algorithm.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Richardson's Iteration", "weight": 1.0} -->

For completeness, let us explain how Richardson's iteration can be applied to solve the least-squares problems that arise in CoSaMP. Suppose we wish to compute ${\mathbf{A}}^{\dagger}{\mathbf{u}}$ where $\mathbf{A}$ is a tall, full-rank matrix. Recalling the definition of the pseudoinverse, we realize that this amounts to solving a linear system of the form This problem can be approached by *splitting* the Gram matrix: where ${\mathbf{M}} = {{{\mathbf{A}}^{\ast}{\mathbf{A}}} - \mathbf{I}}$. Given an initial iterate ${\mathbf{z}}^{0}$, Richardon's method produces the subsequent iterates via the formula Evidently, this iteration requires only matrix--vector multiplies with $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Richardson's Iteration", "weight": 1.0} -->

It is worth noting that Richardson's method can be accelerated \[1, Sec. 7.2.5\], but we omit the details.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Richardson's Iteration", "weight": 1.0} -->

It is quite easy to analyze Richardson's iteration \[1, Sec. 7.2.1\]. Observe that This recursion delivers In words, the iteration converges linearly.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Richardson's Iteration", "weight": 1.0} -->

In our setting, ${\mathbf{A}} = \mathbf{\Phi}_{T}$ where $T$ is a set of at most $3s$ indices. Therefore, the restricted isometry inequalities (1.1) imply that We have assumed that $\delta_{3s} \leq \delta_{4s} \leq 0.1$, which means that the iteration converges quite fast. Once again, the restricted isometry behavior of the sampling matrix plays an essential role in the performance of the CoSaMP algorithm.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Richardson's Iteration", "weight": 1.0} -->

Conjugate gradient provides even better guarantees for solving the least-squares problem, but it is somewhat more complicated to describe and rather more difficult to analyze. We refer the reader to \[1, Sec. 7.4\] for more information. The following lemma summarizes the behavior of both Richardson's iteration and conjugate gradient in our setting.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Initialization", "weight": 1.0} -->

Iterative least-squares algorithms must be seeded with an initial iterate, and their performance depends heavily on a wise selection thereof. CoSaMP offers a natural choice for the initializer: the current signal approximation. As the algorithm progresses, the current signal approximation provides an increasingly good starting point for solving the least-squares problem.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Iteration Count", "weight": 1.0} -->

We need to determine how many iterations of the least-squares algorithm are required to ensure that the approximation produced is sufficiently good to support the performance of CoSaMP.

<!-- chunk {"id": "body-0088", "role": "body", "section": "CoSaMP with Iterative least-squares", "weight": 1.0} -->

Finally, we need to check that the sparse iteration invariant, Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") still holds when we use an iterative least-squares algorithm.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Extension to General Signals", "weight": 1.0} -->

In this section, we finally complete the proof of the main result for CoSaMP, Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). The remaining challenge is to remove the hypothesis that the target signal is sparse, which we framed in Theorems 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") and 5.4. ‣ 5.4. CoSaMP with Iterative least-squares ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). Although this difficulty might seem large, the solution is simple and elegant. It turns out that we can view the noisy samples of a general signal as samples of a sparse signal contaminated with a different noise vector that implicitly reflects the tail of the original signal.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

CoSaMP draws on both algorithmic ideas and analytic techniques that have appeared before. This section describes the other major signal recovery algorithms, and it compares them with CoSaMP. It also attempts to trace the key ideas in the algorithm back to their sources.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

We begin with a short discussion of the major algorithmic approaches to signal recovery from compressive samples. We focus on provably correct methods, although we acknowledge that some *ad hoc* techniques provide excellent empirical results.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

The initial discovery works on compressive sampling proposed to perform signal recovery by solving a convex optimization problem. Given a sampling matrix $\mathbf{\Phi}$ and a noisy vector of samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$, consider the mathematical program In words, we look for a signal reconstruction that is consistent with the samples but has minimal $\ell_{1}$ norm. The intuition behind this approach is that minimizing the $\ell_{1}$ norm promotes sparsity, so allows the approximate recovery of compressible signals. Candès, Romberg, and Tao established in that a minimizer $\mathbf{a}$ of (7.1) satisfies provided that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{4s} \leq 0.2$. In, the hypothesis on the restricted isometry constant is sharpened to $\delta_{2s} \leq {\sqrt{2} - 1}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

The error bound for CoSaMP is equivalent, modulo the exact value of the constants.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

The literature describes a huge variety of algorithms for solving the optimization problem (7.1). The most common approaches involve interior-point methods, projected gradient methods, or iterative thresholding The interior-point methods are guaranteed to solve the problem to a fixed precision in time $O{({m^{2}N^{1.5}})}$, where $m$ is the number of measurements and $N$ is the signal length. Note that the constant in the big-O notation depends on some of the problem data. The other convex relaxation algorithms, while sometimes faster in practice, do not currently offer rigorous guarantees. CoSaMP provides rigorous bounds on the runtime that are much better than the available results for interior-point methods.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Tropp and Gilbert proposed the use of a greedy iterative algorithm called *orthogonal matching pursuit* (OMP) for signal recovery. The algorithm initializes the current sample vector ${\mathbf{v}} = {\mathbf{u}}$. In each iteration, it forms the signal proxy ${\mathbf{y}} = {\mathbf{\Phi}^{\ast}{\mathbf{v}}}$ and identifies a component of the proxy with largest magnitude. It adds the new component to the set $T$ of previously identified components. Then OMP forms a new signal approximation by solving a least-squares problem: ${\mathbf{a}} = {\mathbf{\Phi}_{T}^{\dagger}{\mathbf{u}}}$. Finally, it updates the samples ${\mathbf{v}} = {{\mathbf{u}} - {\mathbf{\Phi}{\mathbf{a}}}}$. These steps are repeated until a halting criterion is satisfied.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Tropp and Gilbert were able to prove a weak result for the performance of OMP. Suppose that $\mathbf{x}$ is a fixed, $s$-sparse signal, and let $m = {Cs{\log N}}$. Draw an $m \times N$ sampling matrix $\mathbf{\Phi}$ whose entries are independent, zero-mean subgaussian^22^2A subgaussian random variable $Z$ satisfies ${{\mathbb{P}}\left\{ {|Z| > t} \right\}} \leq {ce}^{- {ct^{2}}}$ for all $t > 0$. random variables with equal variances. Given noiseless measurements ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$, OMP reconstructs $\mathbf{x}$ after $s$ iterations, except with probability $N^{- 1}$. In this setting, OMP must fail for some sparse signals, so it does not provide the same uniform guarantees as convex relaxation.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

It is unknown whether OMP succeeds for compressible signals or whether it succeeds when the samples are contaminated with noise.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Donoho et al. invented another greedy iterative method called *stagewise OMP*, or StOMP. This algorithm uses the signal proxy to select multiple components at each step, using a rule inspired by ideas from wireless communications. The algorithm is faster than OMP because of the selection rule, and it sometimes provides good performance, although parameter tuning can be difficult. There are no rigorous results available for StOMP.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Very recently, Needell and Vershynin developed and analyzed another greedy approach, called *regularized OMP*, or ROMP. This algorithm is similar to OMP but uses a more sophisticated selection rule. Among the $s$ largest entries of the signal proxy, it identifies the largest subset whose entries differ in magnitude by at most a factor of two. The work on ROMP represents an advance because the authors establish under restricted isometry hypotheses that their algorithm can approximately recover any compressible signal from noisy samples. More precisely, suppose that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{8s} \leq {0.01/\sqrt{\log s}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Given noisy samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$, ROMP produces a $2s$-sparse signal approximation $\mathbf{a}$ that satisfies This result is comparable with the result for convex relaxation, aside from the extra logarithmic factor in the restricted isometry hypothesis and the error bound. The results for CoSaMP show that it does not suffer these parasitic factors, so its performance is essentially optimal.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

After we initially presented this work, Dai and Milenkovic developed an algorithm called Subspace Pursuit that is very similar to CoSaMP. They established that their algorithm offers performance guarantees analogous with those for CoSaMP. See for details.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

Finally, we note that there is a class of sublinear algorithms for signal reconstruction from compressive samples. A sublinear algorithm uses time and space resources that are asymptotically smaller than the length of the signal. One of the earliest such techniques is the Fourier sampling algorithm of Gilbert et al.. This algorithm uses random (but structured) time samples to recover signals that are compressible with respect to the discrete Fourier basis. Given $s{\operatorname{polylog}{(N)}}$ samples^33^3The term $\operatorname{polylog}$ indicates a function that is dominated by a polynomial in the logarithm of its argument., Fourier sampling produces a signal approximation $\mathbf{a}$ that satisfies except with probability $N^{- 1}$. The result for Fourier sampling holds for each signal (rather than for all). Later, Gilbert et al. developed two other sublinear algorithms, chaining pursuit and HHS pursuit, that offer uniform guarantees for all signals. Chaining pursuit has an error bound which is somewhat worse than (7.2). HHS pursuit achieves the error bound (7.2).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

These methods all require more measurements than the linear and superlinear algorithms (by logarithmic factors), and these measurements must be highly structured. As a result, the sublinear algorithms may not be useful in practice.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Algorithms for Compressive Sampling", "weight": 1.0} -->

The sublinear algorithms are all combinatorial in nature. They use ideas from group testing to identify the support of the signal quickly. There are several other combinatorial signal recovery methods due to Cormode--Muthukrishnan and Iwen. These algorithms have drawbacks similar to the sublinear approaches.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Relative Performance", "weight": 1.0} -->

Table 2 summarizes the relative behavior of these algorithms in terms of the following criteria.: Does the algorithm work for a variety of sampling schemes? Or does it require structured samples? The designation "RIP" means that a bound on a restricted isometry constant suffices. "Subgauss." means that the algorithm succeeds for the class of subgaussian sampling matrices.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Relative Performance", "weight": 1.0} -->

Optimal number of samples:: Can the algorithm recover $s$ sparse signals from $O{({s{\log N}})}$ measurements? Or are its sampling requirements higher (by logarithmic factors)?: Does the algorithm recover all signals given a fixed sampling matrix? Or do the results require a sampling matrix to be drawn at random for each signal?: Does the algorithm succeed when (a) the signal is compressible but not sparse and (b) when the samples are contaminated with noise? In most cases, stable algorithms have error bounds similar to (7.2). See the discussion above for details.: What is the worst-case cost of the algorithm to recover a real-valued $s$-sparse signal to a fixed relative precision, given a sampling matrix with no special structure? The designation LP($N$, $m$) indicates the cost of solving a linear program with $N$ variables and $m$ constraints, which is $O{({m^{2}N^{1.5}})}$ for an interior-point method.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Relative Performance", "weight": 1.0} -->

Note that most of the algorithms can also take advantage of fast matrix--vector multiplies to obtain better running times.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Relative Performance", "weight": 1.0} -->

Of the linear and superlinear algorithms, CoSaMP achieves the best performance on all these metrics. Although CoSaMP is slower than the sublinear algorithms, it makes up for this shortcoming by allowing more general sampling matrices and requiring fewer samples.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Relative Performance", "weight": 1.0} -->

Table 2. Comparison of several signal recovery algorithms. The notation s refers to the sparsity level; m refers the number of measurements; N refers to the signal length. See the text for comments on specific designations.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

We conclude with a historical overview of the ideas that inform the CoSaMP algorithm and its analysis.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

The overall greedy iterative structure of CoSaMP has a long history. The idea of approaching sparse approximation problems in this manner dates to the earliest algorithms. In particular, methods for variable selection in regression, such as forward selection and its relatives, all take this form. Temlyakov's survey describes the historical role of greedy algorithms in nonlinear approximation. Mallat and Zhang introduced greedy algorithms into the signal processing literature and proposed the name *matching pursuit*. Gilbert, Strauss, and their collaborators showed how to incorporate greedy iterative strategies into fast algorithms for sparse approximation problems, and they established the first rigorous guarantees for greedy methods. Tropp provided a new theoretical analysis of OMP in his work. Subsequently, Tropp and Gilbert proved that OMP was effective for compressive sampling.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

Unlike the simplest greedy algorithms, CoSaMP identifies many components during each iteration, which allows the algorithm to run faster for many types of signals. It is not entirely clear where this idea first appeared. Several early algorithms of Gilbert et al. incorporate this approach, and it is an essential feature of the Fourier sampling algorithm. More recent compressive sampling recovery algorithms also select multiple indices, including chaining pursuit, HHS pursuit, StOMP, and ROMP.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

CoSaMP uses the restricted isometry properties of the sampling matrix to ensure that the identification step is successful. Candès and Tao isolated the restricted isometry conditions in their work on convex relaxation methods for compressive sampling. The observation that restricted isometries can also be used to ensure the success of greedy methods is relatively new. This idea plays a role in HHS pursuit, but it is expressed more completely in the analysis of ROMP.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

The pruning step of CoSaMP is essential to maintain the sparsity of the approximation, which is what permits us to use restricted isometries in the analysis of the algorithm. It also has significant ramifications for the running time because it impacts the speed of the iterative least-squares algorithms. This technique originally appeared in HHS pursuit.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

The iteration invariant, Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), states that if the error is large then CoSaMP makes substantial progress. This approach to the overall analysis echoes the analysis of other greedy iterative algorithms, including the Fourier sampling method and HHS Pursuit.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Key Ideas", "weight": 1.0} -->

Finally, mixed-norm error bounds, such as that in Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), have become an important feature of the compressive sampling literature. This idea appears in the work of Candès--Romberg--Tao on convex relaxation; it is used in the analysis of HHS pursuit; it also plays a role in the theoretical treatment of Cohen--Dahmen--DeVore.
