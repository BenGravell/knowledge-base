## Introduction

Most signals of interest contain scant information relative to their ambient dimension, but the classical approach to signal acquisition ignores this fact. We usually collect a complete representation of the target signal and process this representation to sieve out the actionable information. Then we discard the rest. Contemplating this ugly inefficiency, one might ask if it is possible instead to acquire *compressive samples*. In other words, is there some type of measurement that automatically winnows out the information from a signal? Incredibly, the answer is sometimes yes.

*Compressive sampling* refers to the idea that, for certain types of signals, a small number of nonadaptive samples carries sufficient information to approximate the signal well. Research in this area has two major components:

: How many samples are necessary to reconstruct signals to a specified precision? What type of samples? How can these sampling schemes be implemented in practice?

: Given the compressive samples, what algorithms can efficiently construct a signal approximation?

The literature already contains a well-developed theory of sampling, which we summarize below. Although algorithmic work has been progressing, the state of knowledge is less than complete. We assert that a practical signal reconstruction algorithm should have all of the following properties.

It should accept samples from a variety of sampling schemes.

It should succeed using a minimal number of samples.

It should be robust when samples are contaminated with noise.

It should provide optimal error guarantees for every target signal.

It should offer provably efficient resource usage.

To our knowledge, no approach in the literature simultaneously accomplishes all five goals.

This paper presents and analyzes a novel signal reconstruction algorithm that achieves these desiderata. The algorithm is called CoSaMP, from the acrostic *Compressive Sampling Matching Pursuit*. As the name suggests, the new method is ultimately based on orthogonal matching pursuit (OMP), but it incorporates several other ideas from the literature to accelerate the algorithm and to provide strong guarantees that OMP cannot. Before we describe the algorithm, let us deliver an introduction to the theory of compressive sampling.

### Rudiments of Compressive Sampling

To enhance intuition, we focus on sparse and compressible signals. For vectors in ${\mathbb{C}}^{N}$, define the $\ell_{0}$ quasi-norm

We say that a signal $\mathbf{x}$ is *$s$-sparse* when $\left\| {\mathbf{x}} \right\|_{0} \leq s$. Sparse signals are an idealization that we do not encounter in applications, but real signals are quite often *compressible*, which means that their entries decay rapidly when sorted by magnitude. As a result, compressible signals are well approximated by sparse signals. We can also talk about signals that are compressible with respect to other orthonormal bases, such as a Fourier or wavelet basis. In this case, the sequence of coefficients in the orthogonal expansion decays quickly. It represents no loss of generality to focus on signals that are compressible with respect to the standard basis, and we do so without regret. For a more precise definition of compressibility, turn to Section 2.6.

In the theory of compressive sampling, a *sample* is a linear functional applied to a signal. The process of collecting multiple samples is best viewed as the action of a *sampling matrix* $\mathbf{\Phi}$ on the target signal. If we take $m$ samples, or *measurements*, of a signal in ${\mathbb{C}}^{N}$, then the sampling matrix $\mathbf{\Phi}$ has dimensions $m \times N$. A natural question now arises: How many measurements are necessary to acquire $s$-sparse signals?

The minimum number of measurements $m \geq {2s}$ on account of the following simple argument. The sampling matrix must not map two different $s$-sparse signals to the same set of samples. Therefore, each collection of $2s$ columns from the sampling matrix must be nonsingular. It is easy to see that certain Vandermonde matrices satisfy this property, but these matrices are not really suitable for signal acquisition because they contain square minors that are very badly conditioned. As a result, some sparse signals are mapped to very similar sets of samples, and it is unstable to invert the sampling process numerically.

Instead, Candès and Tao proposed the stronger condition that the geometry of sparse signals should be preserved under the action of the sampling matrix. To quantify this idea, they defined the $r$th *restricted isometry constant* of a matrix $\mathbf{\Phi}$ as the least number $\delta_{r}$ for which

We have written $\left. \parallel \cdot \parallel{}_{2} \right.$ for the $\ell_{2}$ vector norm. When $\delta_{r} < 1$, these inequalities imply that each collection of $r$ columns from $\mathbf{\Phi}$ is nonsingular, which is the minimum requirement for acquiring $({r/2})$-sparse signals. When $\delta_{r} \ll 1$, the sampling operator very nearly maintains the $\ell_{2}$ distance between each pair of $({r/2})$-sparse signals. In consequence, it is possible to invert the sampling process stably.

To acquire $s$-sparse signals, one therefore hopes to achieve a small restricted isometry constant $\delta_{2s}$ with as few samples as possible. A striking fact is that many types of random matrices have excellent restricted isometry behavior. For example, we can often obtain $\delta_{2s} \leq 0.1$ with

measurements, where $\alpha$ is a small integer. Unfortunately, no deterministic sampling matrix is known to satisfy a comparable bound. Even worse, it is computationally difficult to check the inequalities (1.1), so it may never be possible to exhibit an explicit example of a good sampling matrix.

As a result, it is important to understand how random sampling matrices behave. The two quintessential examples are Gaussian matrices and partial Fourier matrices.

: If the entries of $\sqrt{m}\mathbf{\Phi}$ are independent and identically distributed standard normal variables then

except with probability $e^{- {cm}}$. See for details.

Partial Fourier matrices:

: If $\sqrt{m}\mathbf{\Phi}$ is a uniformly random set of $m$ rows drawn from the $N \times N$ unitary discrete Fourier transform (DFT), then

except with probability $N^{- 1}$. See for the proof. Experts believe that the power on the first logarithm should be no greater than two.

Here and elsewhere, we follow the analyst's convention that upright letters ($c,C,\ldots$) refer to positive, universal constants that may change from appearance to appearance.

The Gaussian matrix is important because it has optimal restricted isometry behavior. Indeed, for any $m \times N$ matrix,

on account of profound geometric results of Kashin and Garnaev--Gluskin. Even though partial Fourier matrices may require additional samples to achieve a small restricted isometry constant, they are more interesting for the following reasons.

There are technologies that acquire random Fourier measurements at unit cost per sample.

The sampling matrix can be applied to a vector in time $O{({N{\log N}})}$.

The sampling matrix requires only $O{({m{\log N}})}$ storage.

Other types of sampling matrices, such as the *random demodulator*, enjoy similar qualities. These traits are essential for the translation of compressive sampling from theory into practice.

### Signal Recovery Algorithms

The major algorithmic challenge in compressive sampling is to approximate a signal given a vector of noisy samples. The literature describes a huge number of approaches to solving this problem. They fall into three rough categories:

: These methods build up an approximation one step at a time by making locally optimal choices at each step. Examples include OMP, stagewise OMP (StOMP), and regularized OMP (ROMP).

: These techniques solve a convex program whose minimizer is known to approximate the target signal. Many algorithms have been proposed to complete the optimization, including interior-point methods, projected gradient methods, and iterative thresholding.

: These methods acquire highly structured samples of the signal that support rapid reconstruction via group testing. This class includes Fourier sampling, chaining pursuit, and HHS pursuit, as well as some algorithms of Cormode--Muthukrishnan and Iwen.

At present, each type of algorithm has its native shortcomings. Many of the combinatorial algorithms are extremely fast---sublinear in the length of the target signal---but they require a large number of somewhat unusual samples that may not be easy to acquire. At the other extreme, convex relaxation algorithms succeed with a very small number of measurements, but they tend to be computationally burdensome. Greedy pursuits---in particular, the ROMP algorithm---are intermediate in their running time and sampling efficiency.

CoSaMP, the algorithm described in this paper, is at heart a greedy pursuit. It also incorporates ideas from the combinatorial algorithms to guarantee speed and to provide rigorous error bounds. The analysis is inspired by the work on ROMP and the work of Candès--Romberg--Tao on convex relaxation methods. In particular, we establish the following result.

### Theorem A (CoSaMP)

Suppose that $\mathbf{\Phi}$ is an $m \times N$ sampling matrix with restricted isometry constant $\delta_{2s} \leq c$. Let $\mathbf{u} = {{\mathbf{\Phi}\mathbf{x}} + \mathbf{e}}$ be a vector of samples of an arbitrary signal, contaminated with arbitrary noise. For a given precision parameter $\eta$, the algorithm CoSaMP produces a $2s$-sparse approximation $\mathbf{a}$ that satisfies

where $\mathbf{x}_{s}$ is a best $s$-sparse approximation to $\mathbf{x}$. The running time is $O{({\mathcal{L} \cdot {\log{({\left\| \mathbf{x} \right\|_{2}/\eta})}}})}$, where $\mathcal{L}$ bounds the cost of a matrix--vector multiply with $\mathbf{\Phi}$ or $\mathbf{\Phi}^{\ast}$. The working storage use is $O{(N)}$.

Let us expand on the statement of this result. First, recall that many types of random sampling matrices satisfy the restricted isometry hypothesis when the number of samples $m = {O{({s{\log^{\alpha}N}})}}$. Therefore, the theorem applies to a wide class of sampling schemes when the number of samples is proportional to the target sparsity and logarithmic in the ambient dimension of the signal space.

The algorithm produces a $2s$-sparse approximation whose $\ell_{2}$ error is comparable with the scaled $\ell_{1}$ error of the best $s$-sparse approximation to the signal. Of course, the algorithm cannot resolve the uncertainty due to the additive noise, so we also pay for the energy in the noise. This type of error bound is structurally optimal, as we discuss in Section 2.6. Some disparity in the sparsity levels (here, $2s$ versus $s$) seems to be necessary when the recovery algorithm is computationally efficient.

We can interpret the error guarantee as follows. In the absence of noise, the algorithm can recover an $s$-sparse signal to arbitrarily high precision. Performance degrades gracefully as the energy in the noise increases. Performance also degrades gracefully for compressible signals. The theorem is ultimately vacuous for signals that cannot be approximated by sparse signals, but compressive sampling is not an appropriate technique for this class.

The running time bound indicates that each matrix--vector multiplication reduces the error by a constant factor (if we amortize over the entire execution). That is, the algorithm has linear convergence^11^1Mathematicians sometimes refer to linear convergence as "exponential convergence.". We find that the total runtime is roughly proportional to (the negation of) the *reconstruction signal-to-noise ratio*

For compressible signals, one can show that $\left| \text{R-SNR} \right| = {O{({\log s})}}$. The runtime is also proportional to the cost of a matrix--vector multiply. For sampling matrices with a fast multiply, the algorithm is accelerated substantially. In particular, for the partial Fourier matrix, a matrix--vector multiply requires time $O{({N{\log N}})}$. It follows that the total runtime is $O{({N{\log{N \cdot \left| \text{R-SNR} \right|}}})}$. For most signals of interest, this cost is nearly linear in the signal length!

### Notation

Let us instate several pieces of notation that are carried throughout the paper. For $p \in {\lbrack 1,\infty\rbrack}$, we write $\left. \parallel \cdot \parallel{}_{p} \right.$ for the usual $\ell_{p}$ vector norm. We reserve the symbol $\left. \parallel \cdot \parallel \right.$ for the spectral norm, i.e., the natural norm on linear maps from $\ell_{2}$ to $\ell_{2}$.

Suppose that $\mathbf{x}$ is a signal in ${\mathbb{C}}^{N}$ and $r$ is a positive integer. We write ${\mathbf{x}}_{r}$ for the signal in ${\mathbb{C}}^{N}$ that is formed by restricting $\mathbf{x}$ to its $r$ largest-magnitude components. Ties are broken lexicographically. This signal is a best $r$-sparse approximation to $\mathbf{x}$ with respect to any $\ell_{p}$ norm. Suppose now that $T$ is a subset of $\{ 1,2,\ldots,N\}$. We define the restriction of the signal to the set $T$ as

We occasionally abuse the notation and treat ${{\mathbf{x}}|}_{T}$ as an element of the vector space ${\mathbb{C}}^{T}$. We also define the restriction $\mathbf{\Phi}_{T}$ of the sampling matrix $\mathbf{\Phi}$ as the column submatrix whose columns are listed in the set $T$.

Finally, we define the pseudoinverse of a tall, full-rank matrix $\mathbf{A}$ by the formula ${\mathbf{A}}^{\dagger} = {{({{\mathbf{A}}^{\ast}{\mathbf{A}}})}^{- 1}{\mathbf{A}}^{\ast}}$.

### Organization

The rest of the paper has the following structure. In Section 2 we introduce the CoSaMP algorithm, we state the major theorems in more detail, and we discuss implementation and resource requirements. Section 3 describes some consequences of the restricted isometry property that pervade our analysis. The central theorem is established for sparse signals in Sections 4 and 5. We extend this result to general signals in Section 6. Finally, Section 7 places the algorithm in the context of previous work. The first appendix presents variations on the algorithm. The second appendix contains a bound on the number of iterations required when the algorithm is implemented using exact arithmetic.

## The CoSaMP Algorithm

This section gives an overview of the algorithm, along with explicit pseudocode. It presents the major theorems on the performance of the algorithm. Then it covers details of implementation and bounds on resource requirements.

### Intuition

The most difficult part of signal reconstruction is to identify the locations of the largest components in the target signal. CoSaMP uses an approach inspired by the restricted isometry property. Suppose that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{s} \ll 1$. For an $s$-sparse signal $\mathbf{x}$, the vector ${\mathbf{y}} = {\mathbf{\Phi}^{\ast}\mathbf{\Phi}{\mathbf{x}}}$ can serve as a proxy for the signal because the energy in each set of $s$ components of $\mathbf{y}$ approximates the energy in the corresponding $s$ components of $\mathbf{x}$. In particular, the largest $s$ entries of the proxy $\mathbf{y}$ point toward the largest $s$ entries of the signal $\mathbf{x}$. Since the samples have the form ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$, we can obtain the proxy just by applying the matrix $\mathbf{\Phi}^{\ast}$ to the samples.

The algorithm invokes this idea iteratively to approximate the target signal. At each iteration, the current approximation induces a residual, the part of the target signal that has not been approximated. As the algorithm progresses, the samples are updated so that they reflect the current residual. These samples are used to construct a proxy for the residual, which permits us to identify the large components in the residual. This step yields a tentative support for the next approximation. We use the samples to estimate the approximation on this support set using least squares. This process is repeated until we have found the recoverable energy in the signal.

### Overview

As input, the CoSaMP algorithm requires four pieces of information:

Access to the sampling operator via matrix--vector multiplication.

A vector of (noisy) samples of the unknown signal.

The sparsity of the approximation to be produced.

The algorithm is initialized with a trivial signal approximation, which means that the initial residual equals the unknown target signal. During each iteration, CoSaMP performs five major steps:

Identification. The algorithm forms a proxy of the residual from the current samples and locates the largest components of the proxy.

Support Merger. The set of newly identified components is united with the set of components that appear in the current approximation.

Estimation. The algorithm solves a least-squares problem to approximate the target signal on the merged set of components.

Pruning. The algorithm produces a new approximation by retaining only the largest entries in this least-squares signal approximation.

Sample Update. Finally, the samples are updated so that they reflect the residual, the part of the signal that has not been approximated.

These steps are repeated until the halting criterion is triggered. In the body of this work, we concentrate on methods that use a fixed number of iterations. Appendix A discusses some other simple stopping rules that may also be useful in practice.

Pseudocode for CoSaMP appears as Algorithm 2.1. This code describes the version of the algorithm that we analyze in this paper. Nevertheless, there are several adjustable parameters that may improve performance: the number of components selected in the identification step and the number of components retained in the pruning step. For a brief discussion of other variations on the algorithm, turn to Appendix A.

CoSaMP(Φ, u, s) Input: Sampling matrix Φ, noisy sample vector u, sparsity level s Output: An s-sparse approximation a of the target signal a0 ← 0 { Trivial initial approximation } v ← u { Current samples = input samples } k ← 0 repeat k ← k + 1 y ← Φ* v { Form signal proxy } Ω ← supp(y2 s) { Identify large components } T ← Ω ∪ supp(ak − 1) { Merge supports } b|T ← ΦT† u { Signal estimation by least-squares } b|Tc ← 0 ak ← bs { Prune to obtain next approximation } v ← u − Φ ak { Update current samples } until halting criterion true

Algorithm 2.1 CoSaMP Recovery Algorithm

### Performance Guarantees

This section describes our theoretical analysis of the behavior of CoSaMP. The next section covers the resource requirements of the algorithm. Afterward, Section 2.5 combines these materials to establish Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples").

Our results depend on a set of hypotheses that has become common in the compressive sampling literature. Let us frame the standing assumptions:

CoSaMP Hypotheses • The sparsity level $s$ is fixed. • The $m \times N$ sampling operator $\mathbf{\Phi}$ has restricted isometry constant $\delta_{4s} \leq 0.1$.\
• The signal ${\mathbf{x}} \in {\mathbb{C}}^{N}$ is arbitrary, except where noted. • The noise vector ${\mathbf{e}} \in {\mathbb{C}}^{m}$ is arbitrary. • The vector of samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$.

We also define the *unrecoverable energy* $\nu$ in the signal. This quantity measures the baseline error in our approximation that occurs because of noise in the samples or because the signal is not sparse.

$${\nu = {\left\| {{\mathbf{x}} - {\mathbf{x}}_{s}} \right\|_{2} + {\frac{1}{\sqrt{s}}\left\| {{\mathbf{x}} - {\mathbf{x}}_{s}} \right\|_{1}} + \left\| {\mathbf{e}} \right\|_{2}}}.$$ (2.1)

We postpone a more detailed discussion of the unrecoverable energy until Section 2.6.

Our key result is that CoSaMP makes significant progress during each iteration where the approximation error is large relative to the unrecoverable energy.

### Theorem 2.1 (Iteration Invariant)

For each iteration $k \geq 0$, the signal approximation $\mathbf{a}^{k}$ is $s$-sparse and

The proof of Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") will occupy us for most of this paper. In Section 4, we establish an analog for sparse signals. The version for general signals appears as a corollary in Section 6.

Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") has some immediate consequences for the quality of reconstruction with respect to standard signal metrics. In this setting, a sensible definition of the *signal-to-noise ratio* (SNR) is

The *reconstruction SNR* is defined as

Both quantities are measured in decibels. Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") implies that, after $k$ iterations, the reconstruction SNR satisfies

In words, each iteration reduces the reconstruction SNR by about 3 decibels until the error nears the noise floor. To reduce the error to its minimal value, the number of iterations is proportional to the SNR.

Let us consider a slightly different scenario. Suppose that the signal $\mathbf{x}$ is $s$-sparse, so the unrecoverable energy $\nu = \left\| {\mathbf{e}} \right\|_{2}$. Define the *dynamic range*

Assume moreover that the minimum nonzero component of the signal is at least $40\nu$. Using the fact that $\left\| {\mathbf{x}} \right\|_{2} \leq {\sqrt{s}\left\| {\mathbf{x}} \right\|_{\infty}}$, it is easy to check that $\left\| {{\mathbf{x}} - {\mathbf{a}}} \right\|_{2} \leq {\min\left| x_{i} \right|}$ as soon as the number $k$ of iterations satisfies

It follows that the support of the approximation $\mathbf{a}$ must contain every entry in the support of the signal $\mathbf{x}$.

This discussion suggests that the number of iterations might be substantial if we require a very low reconstruction SNR or if the signal has a very wide dynamic range. This initial impression is not entirely accurate. We have established that, when the algorithm performs arithmetic to high enough precision, then a fixed number of iterations suffices to reduce the approximation error to the same order as the unrecoverable energy. Here is a result for exact computations.

### Theorem 2.2 (Iteration Count)

Suppose that CoSaMP is implemented with exact arithmetic. After at most $6{({s + 1})}$ iterations, CoSaMP produces an $s$-sparse approximation $\mathbf{a}$ that satisfies

In fact, even more is true. The number of iterations depends significantly on the structure of the signal. The only situation where the algorithm needs $\Omega{(s)}$ iterations occurs when the entries of the signal decay exponentially. For signals whose largest entries are comparable, the number of iterations may be as small as $O{({\log s})}$. This claim is quantified in Appendix B, where we prove Theorem 2.2. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples").

If we solve the least-squares problems to high precision, an analogous result holds, but the approximation guarantee contains an extra term that comes from solving the least-squares problems imperfectly. In practice, it may be more efficient overall to solve the least-squares problems to low precision. The correct amount of care seems to depend on the relative costs of forming the signal proxy and solving the least-squares problem, which are the two most expensive steps in the algorithm. We discuss this point in the next section. Ultimately, the question is best settled with empirical studies.

### Remark 2.3

In the hypotheses, a bound on the restricted isometry constant $\delta_{2s}$ also suffices. Indeed, Corollary 3.4 of the sequel implies that $\delta_{4s} \leq 0.1$ holds whenever $\delta_{2s} \leq 0.025$.

### Remark 2.4

The expression (2.1) for the unrecoverable energy can be simplified using Lemma 7 from, which states that, for every signal ${\mathbf{y}} \in {\mathbb{C}}^{N}$ and every positive integer $t$, we have

Choosing ${\mathbf{y}} = {{\mathbf{x}} - {\mathbf{x}}_{s/2}}$ and $t = {s/2}$, we reach

In words, the unrecoverable energy is controlled by the scaled $\ell_{1}$ norm of the signal tail.

### Implementation and Resource Requirements

CoSaMP was designed to be a practical method for signal recovery. An efficient implementation of the algorithm requires some ideas from numerical linear algebra, as well as some basic techniques from the theory of algorithms. This section discusses the key issues and develops an analysis of the running time for the two most common scenarios.

We focus on the least-squares problem in the estimation step because it is the major obstacle to a fast implementation of the algorithm. The algorithm guarantees that the matrix $\mathbf{\Phi}_{T}$ never has more than $3s$ columns, so our assumption $\delta_{4s} \leq 0.1$ implies that the matrix $\mathbf{\Phi}_{T}$ is extremely well conditioned. As a result, we can apply the pseudoinverse $\mathbf{\Phi}_{T}^{\dagger} = {{({\mathbf{\Phi}_{T}^{\ast}\mathbf{\Phi}_{T}})}^{- 1}\mathbf{\Phi}_{T}^{\ast}}$ very quickly using an iterative method, such as Richardson's iteration \[1, Sec. 7.2.3\] or conjugate gradient \[1, Sec. 7.4\]. These techniques have the additional advantage that they only interact with the matrix $\mathbf{\Phi}_{T}$ through its action on vectors. It follows that the algorithm performs better when the sampling matrix has a fast matrix--vector multiply.

Section 5 contains an analysis of the performance of iterative least-squares algorithms in the context of CoSaMP. In summary, if we initialize the least-squares method with the current approximation ${\mathbf{a}}^{k - 1}$, then the cost of solving the least-squares problem is $O{(\mathcal{L})}$, where $\mathcal{L}$ bounds the cost of a matrix--vector multiply with $\mathbf{\Phi}_{T}$ or $\mathbf{\Phi}_{T}^{\ast}$. This implementation ensures that Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds at each iteration.

We emphasize that direct methods for least squares are likely to be extremely inefficient in this setting. The first reason is that each least-squares problem may contain substantially different sets of columns from $\mathbf{\Phi}$. As a result, it becomes necessary to perform a completely new QR or SVD factorization during each iteration at a cost of $O{({s^{2}m})}$. The second problem is that computing these factorizations typically requires direct access to the columns of the matrix, which is problematic when the matrix is accessed through its action on vectors. Third, direct methods have storage costs $O{({sm})}$, which may be deadly for large-scale problems.

The remaining steps of the algorithm are standard. Let us estimate the operation counts.

: Forming the proxy is dominated by the cost of the matrix--vector multiply $\mathbf{\Phi}^{\ast}{\mathbf{v}}$.

: We can locate the largest $2s$ entries of a vector in time $O{(N)}$ using the approach in \[8, Ch. 9\]. In practice, it may be faster to sort the entries of the signal in decreasing order of magnitude at cost $O{({N{\log N}})}$ and then select the first $2s$ of them. The latter procedure can be accomplished with quicksort, mergesort, or heapsort \[8, Sec. II\]. To implement the algorithm to the letter, the sorting method needs to be stable because we stipulate that ties are broken lexicographically. This point is not important in practice.

: We can merge two sets of size $O{(s)}$ in expected time $O{(s)}$ using randomized hashing methods \[8, Ch. 11\]. One can also sort both sets first and use the elementary merge procedure \[8, p. 29\] for a total cost $O{({s{\log s}})}$.

: We use Richardson's iteration or conjugate gradient to compute $\mathbf{\Phi}_{T}^{\dagger}{\mathbf{u}}$. Initializing the least-squares algorithm requires a matrix--vector multiply with $\mathbf{\Phi}_{T}^{\ast}$. Each iteration of the least-squares method requires one matrix--vector multiply each with $\mathbf{\Phi}_{T}$ and $\mathbf{\Phi}_{T}^{\ast}$. Since $\mathbf{\Phi}_{T}$ is a submatrix of $\mathbf{\Phi}$, the matrix--vector multiplies can also be obtained from multiplication with the full matrix. We prove in Section 5 that a constant number of least-squares iterations suffices for Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") to hold.

: This step is similar to identification. Pruning can be implemented in time $O{(s)}$, but it may be preferable to sort the components of the vector by magnitude and then select the first $s$ at a cost of $O{({s{\log s}})}$.

: This step is dominated by the cost of the multiplication of $\mathbf{\Phi}$ with the $s$-sparse vector ${\mathbf{a}}^{k}$.

Table 1 summarizes this discussion in two particular cases. The first column shows what happens when the sampling matrix $\mathbf{\Phi}$ is applied to vectors in the standard way, but we have random access to submatrices. The second, column shows what happens when the sampling matrix $\mathbf{\Phi}$ and its adjoint $\mathbf{\Phi}^{\ast}$ both have a fast multiply with cost $\mathcal{L}$, where we assume that $\mathcal{L} \geq N$. A typical value is $\mathcal{L} = {O{({N{\log N}})}}$. In particular, a partial Fourier matrix satisfies this bound.

Total per iteration

Table 1. Operation count for CoSaMP. Big-O notation is omitted for legibility. The dimensions of the sampling matrix Φ are m × N; the sparsity level is s. The number ℒ bounds the cost of a matrix–vector multiply with Φ or Φ*.

Finally, we note that the storage requirements of the algorithm are also favorable. Aside from the storage required by the sampling matrix, the algorithm constructs only one vector of length $N$, the signal proxy. The sample vectors $\mathbf{u}$ and $\mathbf{v}$ have length $m$, so they require $O{(m)}$ storage. The signal approximations can be stored using sparse data structures, so they require at most $O{({s{\log N}})}$ storage. Similarly, the index sets that appear require only $O{({s{\log N}})}$ storage. The total storage is $O{(N)}$.

The following result summarizes this discussion.

### Theorem 2.5 (Resource Requirements)

Each iteration of CoSaMP requires $O{(\mathcal{L})}$ time, where $\mathcal{L}$ bounds the cost of a multiplication with the matrix $\mathbf{\Phi}$ or $\mathbf{\Phi}^{\ast}$. The algorithm uses storage $O{(N)}$.

### Remark 2.6

We have been able to show that Theorem 2.2. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds when the least-squares problems are solved iteratively with a delicately chosen stopping threshold. In this case, the total number of least-squares iterations performed over the entire execution of the algorithm is at most $O{({\log{({\left\| \mathbf{x} \right\|_{2}/\eta})}})}$ if we wish to achieve error $O{({\eta + \nu})}$. When the cost of forming the signal proxy is much higher than the cost of solving the least-squares problem, this analysis may yield a sharper result. For example, using standard matrix--vector multiplication, we have a runtime bound

The first term reflects the number of CoSaMP iterations times the cost of forming the signal proxy. The second term reflects the total cost of the least-squares iterations. Unless the relative precision $\left\| \mathbf{x} \right\|_{2}/\eta$ is superexponential in the signal length, we obtain running time $O{({smN})}$. This bound is comparable with the worst-case cost of OMP or ROMP. As we discuss in Appendix B, the number of CoSaMP iterations may be much smaller than $s$, which also improves the estimate.

### Proof of Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples")

We have now collected all the material we need to establish the main result. Fix a precision parameter $\eta$. After at most $O{({\log{({\left\| {\mathbf{x}} \right\|_{2}/\eta})}})}$ iterations, CoSaMP produces an $s$-sparse approximation $\mathbf{a}$ that satisfies

in consequence of Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). Apply inequality (2.2) to bound the unrecoverable energy $\nu$ in terms of the $\ell_{1}$ norm. We see that the approximation error satisfies

According to Theorem 2.5. ‣ 2.4. Implementation and Resource Requirements ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), each iteration of CoSaMP is completed in time $O{(\mathcal{L})}$, where $\mathcal{L}$ bounds the cost of a matrix--vector multiplication with $\mathbf{\Phi}$ or $\mathbf{\Phi}^{\ast}$. The total runtime, therefore, is $O{({\mathcal{L}{\log{({\left\| {\mathbf{x}} \right\|_{2}/\eta})}}})}$. The total storage is $O{(N)}$.

In the statement of the theorem, perform the substitution ${s/2}\mapsto s$. Finally, we replace $\delta_{8s}$ with $\delta_{2s}$ by means of Corollary 3.4, which states that $\delta_{cr} \leq {c \cdot \delta_{2r}}$ for any positive integers $c$ and $r$.

### The Unrecoverable Energy

Since the unrecoverable energy $\nu$ plays a central role in our analysis of CoSaMP, it merits some additional discussion. In particular, it is informative to examine the unrecoverable energy in a compressible signal. Let $p$ be a number in the interval $$. We say that $\mathbf{x}$ is *$p$-compressible* with magnitude $R$ if the sorted components of the signal decay at the rate

When $p = 1$, this definition implies that $\left\| {\mathbf{x}} \right\|_{1} \leq {R \cdot {({1 + {\log N}})}}$. Therefore, the unit ball of $1$-compressible signals is similar to the $\ell_{1}$ unit ball. When $p \approx 0$, this definition implies that $p$-compressible signals are very nearly sparse. In general, compressible signals are well approximated by sparse signals:

where $C_{p} = {({{1/p} - 1})}^{- 1}$ and $D_{p} = {({{2/p} - 1})}^{- {1/2}}$. These results follow by writing each norm as a sum and approximating the sum with an integral. We see that the unrecoverable energy (2.1) in a $p$-compressible signal is bounded as

When $p$ is small, the first term in the unrecoverable energy decays rapidly as the sparsity level $s$ increases. For the class of $p$-compressible signals, the bound (2.3) on the unrecoverable energy is sharp, modulo the exact values of the constants.

With these inequalities, we can see that CoSaMP recovers compressible signals efficiently. Let us calculate the number of iterations required to reduce the approximation error from $\left\| {\mathbf{x}} \right\|_{2}$ to the optimal level (2.3). For compressible signals, the energy $\left\| {\mathbf{x}} \right\|_{2} \leq {2R}$, so

Therefore, the number of iterations required to recover a generic $p$-compressible signal is $O{({\log s})}$, where the constant in the big-O notation depends on $p$.

The term "unrecoverable energy" is justified by several facts. First, we must pay for the $\ell_{2}$ error contaminating the samples. To check this point, define $S = {{supp}{({\mathbf{x}}_{s})}}$. The matrix $\mathbf{\Phi}_{S}$ is nearly an isometry from $\ell_{2}^{S}$ to $\ell_{2}^{m}$, so an error in the large components of the signal induces an error of equivalent size in the samples. Clearly, we can never resolve this uncertainty.

The term $s^{- {1/2}}\left\| {{\mathbf{x}} - {\mathbf{x}}_{s}} \right\|_{1}$ is also required on account of classical results about the Gel'fand widths of the $\ell_{1}^{N}$ ball in $\ell_{2}^{N}$, due to Kashin and Garnaev--Gluskin. In the language of compressive sampling, their work has the following interpretation. Let $\mathbf{\Phi}$ be a fixed $m \times N$ sampling matrix. Suppose that, for every signal ${\mathbf{x}} \in {\mathbb{C}}^{N}$, there is an algorithm that uses the samples ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$ to construct an approximation $\mathbf{a}$ that achieves the error bound

Then the number $m$ of measurements must satisfy $m \geq {cs{\log{({N/s})}}}$.

## Restricted Isometry Consequences

When the sampling matrix satisfies the restricted isometry inequalities (1.1), it has several other properties that we require repeatedly in the proof that the CoSaMP algorithm is correct. Our first observation is a simple translation of (1.1) into other terms.

### Proposition 3.1

Suppose $\mathbf{\Phi}$ has restricted isometry constant $\delta_{r}$. Let $T$ be a set of $r$ indices or fewer. Then

where the last two statements contain an upper and lower bound, depending on the sign chosen.

### Proof

The restricted isometry inequalities (1.1) imply that the singular values of $\mathbf{\Phi}_{T}$ lie between $\sqrt{1 - \delta_{r}}$ and $\sqrt{1 + \delta_{r}}$. The bounds follow from standard relationships between the singular values of $\mathbf{\Phi}_{T}$ and the singular values of basic functions of $\mathbf{\Phi}_{T}$. ∎

A second consequence is that disjoint sets of columns from the sampling matrix span nearly orthogonal subspaces. The following result quantifies this observation.

### Proposition 3.2 (Approximate Orthogonality)

Suppose $\mathbf{\Phi}$ has restricted isometry constant $\delta_{r}$. Let $S$ and $T$ be disjoint sets of indices whose combined cardinality does not exceed $r$. Then

### Proof

Abbreviate $R = {S \cup T}$, and observe that $\mathbf{\Phi}_{S}^{\ast}\mathbf{\Phi}_{T}$ is a submatrix of ${\mathbf{\Phi}_{R}^{\ast}\mathbf{\Phi}_{R}} - \mathbf{I}$. The spectral norm of a submatrix never exceeds the norm of the entire matrix. We discern that

because the eigenvalues of $\mathbf{\Phi}_{R}^{\ast}\mathbf{\Phi}_{R}$ lie between $1 - \delta_{r}$ and $1 + \delta_{r}$. ∎

This result will be applied through the following corollary.

### Corollary 3.3

Suppose $\mathbf{\Phi}$ has restricted isometry constant $\delta_{r}$. Let $T$ be a set of indices, and let $\mathbf{x}$ be a vector. Provided that $r \geq \left| {T \cup {{supp}{(\mathbf{x})}}} \right|$,

### Proof

Define $S = {{{supp}{({\mathbf{x}})}} \smallsetminus T}$, so we have ${{\mathbf{x}}|}_{S} = {{\mathbf{x}}|}_{T^{c}}$. Thus,

owing to Proposition 3.2. ‣ 3. Restricted Isometry Consequences ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). ∎

As a second corollary, we show that $\delta_{2r}$ gives weak control over the higher restricted isometry constants.

### Corollary 3.4

Let $c$ and $r$ be positive integers. Then $\delta_{cr} \leq {c \cdot \delta_{2r}}$.

### Proof

The result is clearly true for ${c = {1,2}},$ so we assume $c \geq 3$. Let $S$ be an arbitrary index set of size $cr$, and let ${\mathbf{M}} = {{\mathbf{\Phi}_{S}^{\ast}\mathbf{\Phi}_{S}} - \mathbf{I}}$. It suffices to check that $\left\| {\mathbf{M}} \right\| \leq {c \cdot \delta_{2r}}$. To that end, we break the matrix $\mathbf{M}$ into $r \times r$ blocks, which we denote ${\mathbf{M}}_{ij}$. A block version of Gershgorin's theorem states that $\left\| {\mathbf{M}} \right\|$ satisfies at least one of the inequalities

The derivation is entirely analogous with the usual proof of Gershgorin's theorem, so we omit the details. For each diagonal block, we have $\left\| {\mathbf{M}}_{ii} \right\| \leq \delta_{r}$ because of the restricted isometry inequalities (1.1). For each off-diagonal block, we have $\left\| {\mathbf{M}}_{ij} \right\| \leq \delta_{2r}$ because of Proposition 3.2. ‣ 3. Restricted Isometry Consequences ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). Substitute these bounds into the block Gershgorin theorem and rearrange to complete the proof. ∎

Finally, we present a result that measures how much the sampling matrix inflates nonsparse vectors. This bound permits us to establish the major results for sparse signals and then transfer the conclusions to the general case.

### Proposition 3.5 (Energy Bound)

Suppose that $\mathbf{\Phi}$ verifies the upper inequality of (1.1), viz.

Then, for every signal $\mathbf{x}$,

### Proof

We repeat the geometric argument of Rudelson that is presented in.

First, observe that the hypothesis of the proposition can be regarded as a statement about the operator norm of $\mathbf{\Phi}$ as a map between two Banach spaces. For a set $I \subset {\{ 1,2,\ldots,N\}}$, write $B_{2}^{I}$ for the unit ball in $\ell_{2}{(I)}$. Define the convex body

and notice that, by hypothesis, the operator norm

Define a second convex body

and consider the operator norm

The content of the proposition is the claim that

To establish this point, it suffices to check that $K \subset S$.

Instead, we prove the reverse inclusion for the polars: $S^{\circ} \subset K^{\circ}$. The norm with unit ball $S^{\circ}$ is calculated as

Consider a vector $\mathbf{u}$ in the unit ball $S^{\circ}$, and let $I$ be a set of $r$ coordinates where $\mathbf{u}$ is largest in magnitude. We must have

or else $\left| u_{i} \right| > \frac{1}{\sqrt{r}}$ for each $i \in I$. But then $\left\| {\mathbf{u}} \right\|_{S^{\circ}} \geq \left. \left\| {\mathbf{u}}| \right._{I}\parallel \right._{2} > 1$, a contradiction. Therefore, we may write

where $B_{p}$ is the unit ball in $\ell_{p}^{N}$. But the set on the right-hand side is precisely the unit ball of $K^{\circ}$ since

In summary, $S^{\circ} \subset K^{\circ}$. ∎

## The Iteration Invariant: Sparse Case

We now commence the proof of Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). For the moment, let us assume that the signal is actually sparse. Section 6 removes this assumption.

The result states that each iteration of the algorithm reduces the approximation error by a constant factor, while adding a small multiple of the noise. As a consequence, when the approximation error is large in comparison with the noise, the algorithm makes substantial progress in identifying the unknown signal.

### Theorem 4.1 (Iteration Invariant: Sparse Case)

Assume that $\mathbf{x}$ is $s$-sparse. For each $k \geq 0$, the signal approximation $\mathbf{a}^{k}$ is $s$-sparse, and

The argument proceeds in a sequence of short lemmas, each corresponding to one step in the algorithm. Throughout this section, we retain the assumption that $\mathbf{x}$ is $s$-sparse.

### Approximations, Residuals, etc

Fix an iteration $k \geq 1$. We write ${\mathbf{a}} = {\mathbf{a}}^{k - 1}$ for the signal approximation at the beginning of the iteration. Define the residual ${\mathbf{r}} = {{\mathbf{x}} - {\mathbf{a}}}$, which we interpret as the part of the signal we have not yet recovered. Since the approximation $\mathbf{a}$ is always $s$-sparse, the residual $\mathbf{r}$ must be $2s$-sparse. Notice that the vector $\mathbf{v}$ of updated samples can be viewed as noisy samples of the residual:

### Identification

The identification phase produces a set of components where the residual signal still has a lot of energy.

### Lemma 4.2 (Identification)

The set $\Omega = {{supp}{(\mathbf{y}_{2s})}}$ contains at most $2s$ indices, and

### Proof

The identification phase forms a proxy ${\mathbf{y}} = {\mathbf{\Phi}^{\ast}{\mathbf{v}}}$ for the residual signal. The algorithm then selects a set $\Omega$ of $2s$ components from $\mathbf{y}$ that have the largest magnitudes. The goal of the proof is to show that the energy in the residual on the set $\Omega^{c}$ is small in comparison with the total energy in the residual.

Define the set $R = {{supp}{({\mathbf{r}})}}$. Since $R$ contains at most $2s$ elements, our choice of $\Omega$ ensures that $\left. \left\| {\mathbf{y}}| \right._{R}\parallel \right._{2} \leq \left. \left\| {\mathbf{y}}| \right._{\Omega}\parallel \right._{2}$. By squaring this inequality and canceling the terms in $R \cap \Omega$, we discover that

Since the coordinate subsets here contain few elements, we can use the restricted isometry constants to provide bounds on both sides.

First, observe that the set $\Omega \smallsetminus R$ contains at most $2s$ elements. Therefore, we may apply Proposition 3.1 and Corollary 3.3 to obtain

Likewise, the set $R \smallsetminus \Omega$ contains $2s$ elements or fewer, so Proposition 3.1 and Corollary 3.3 yield

Since the residual is supported on $R$, we can rewrite ${{\mathbf{r}}|}_{R \smallsetminus \Omega} = {{\mathbf{r}}|}_{\Omega^{c}}$. Finally, combine the last three inequalities and rearrange to obtain

Invoke the numerical hypothesis that $\delta_{2s} \leq \delta_{4s} \leq 0.1$ to complete the argument. ∎

### Support Merger

The next step of the algorithm merges the support of the current signal approximation $\mathbf{a}$ with the newly identified set of components. The following result shows that components of the signal $\mathbf{x}$ outside this set have very little energy.

### Lemma 4.3 (Support Merger)

Let $\Omega$ be a set of at most $2s$ indices. The set $T = {\Omega \cup {{supp}{(\mathbf{a})}}}$ contains at most $3s$ indices, and

### Proof

Since ${{supp}{({\mathbf{a}})}} \subset T$, we find that

where the inequality follows from the containment $T^{c} \subset \Omega^{c}$. ∎

### Estimation

The estimation step of the algorithm solves a least-squares problem to obtain values for the coefficients in the set $T$. We need a bound on the error of this approximation.

### Lemma 4.4 (Estimation)

Let $T$ be a set of at most $3s$ indices, and define the least-squares signal estimate $\mathbf{b}$ by the formulae

This result assumes that we solve the least-squares problem in infinite precision. In practice, the right-hand side of the bound contains an extra term owing to the error from the iterative least-squares solver. In Section 5, we study how many iterations of the least-squares solver are required to make the least-squares error negligible in the present argument.

### Proof

Note first that

Using the expression ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$ and the fact ${\mathbf{\Phi}_{T}^{\dagger}\mathbf{\Phi}_{T}} = \mathbf{I}_{T}$, we calculate that

The cardinality of $T$ is at most $3s$, and $\mathbf{x}$ is $s$-sparse, so Proposition 3.1 and Corollary 3.3 imply that

Combine the bounds to reach

Finally, invoke the hypothesis that $\delta_{3s} \leq \delta_{4s} \leq 0.1$. ∎

### Pruning

The final step of each iteration is to prune the intermediate approximation to its largest $s$ terms. The following lemma provides a bound on the error in the pruned approximation.

### Lemma 4.5 (Pruning)

The pruned approximation $\mathbf{b}_{s}$ satisfies

### Proof

The intuition is that ${\mathbf{b}}_{s}$ is close to $\mathbf{b}$, which is close to $\mathbf{x}$. Rigorously,

The second inequality holds because ${\mathbf{b}}_{s}$ is the best $s$-sparse approximation to $\mathbf{b}$. In particular, the $s$-sparse vector $\mathbf{x}$ is a worse approximation. ∎

### Proof of Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples")

We now complete the proof of the iteration invariant for sparse signals, Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). At the end of an iteration, the algorithm forms a new approximation ${\mathbf{a}}^{k} = {\mathbf{b}}_{s}$, which is evidently $s$-sparse. Applying the lemmas we have established, we easily bound the error:

To obtain the second bound in Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), simply solve the error recursion and note that

This point completes the argument.

## Analysis of Iterative Least-squares

To develop an efficient implementation of CoSaMP, it is critical to use an iterative method when we solve the least-squares problem in the estimation step. The two natural choices are Richardson's iteration and conjugate gradient. The efficacy of these methods rests on the assumption that the sampling operator has small restricted isometry constants. Indeed, since the set $T$ constructed in the support merger step contains at most $3s$ components, the hypothesis $\delta_{4s} \leq 0.1$ ensures that the condition number

This condition number is closely connected with the performance of Richardson's iteration and conjugate gradient. In this section, we show that Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") holds if we perform a constant number of iterations of either least-squares algorithm.

### Richardson's Iteration

For completeness, let us explain how Richardson's iteration can be applied to solve the least-squares problems that arise in CoSaMP. Suppose we wish to compute ${\mathbf{A}}^{\dagger}{\mathbf{u}}$ where $\mathbf{A}$ is a tall, full-rank matrix. Recalling the definition of the pseudoinverse, we realize that this amounts to solving a linear system of the form

This problem can be approached by *splitting* the Gram matrix:

where ${\mathbf{M}} = {{{\mathbf{A}}^{\ast}{\mathbf{A}}} - \mathbf{I}}$. Given an initial iterate ${\mathbf{z}}^{0}$, Richardon's method produces the subsequent iterates via the formula

Evidently, this iteration requires only matrix--vector multiplies with $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$. It is worth noting that Richardson's method can be accelerated \[1, Sec. 7.2.5\], but we omit the details.

It is quite easy to analyze Richardson's iteration \[1, Sec. 7.2.1\]. Observe that

This recursion delivers

In words, the iteration converges linearly.

In our setting, ${\mathbf{A}} = \mathbf{\Phi}_{T}$ where $T$ is a set of at most $3s$ indices. Therefore, the restricted isometry inequalities (1.1) imply that

We have assumed that $\delta_{3s} \leq \delta_{4s} \leq 0.1$, which means that the iteration converges quite fast. Once again, the restricted isometry behavior of the sampling matrix plays an essential role in the performance of the CoSaMP algorithm.

Conjugate gradient provides even better guarantees for solving the least-squares problem, but it is somewhat more complicated to describe and rather more difficult to analyze. We refer the reader to \[1, Sec. 7.4\] for more information. The following lemma summarizes the behavior of both Richardson's iteration and conjugate gradient in our setting.

### Lemma 5.1 (Error Bound for LS)

Richardson's iteration produces a sequence $\{\mathbf{z}^{\ell}\}$ of iterates that satisfy

Conjugate gradient produces a sequence of iterates that satisfy

### Initialization

Iterative least-squares algorithms must be seeded with an initial iterate, and their performance depends heavily on a wise selection thereof. CoSaMP offers a natural choice for the initializer: the current signal approximation. As the algorithm progresses, the current signal approximation provides an increasingly good starting point for solving the least-squares problem.

### Lemma 5.2 (Initial Iterate for LS)

Let $\mathbf{x}$ be an $s$-sparse signal with noisy samples $\mathbf{u} = {{\mathbf{\Phi}\mathbf{x}} + \mathbf{e}}$. Let $\mathbf{a}^{k - 1}$ be the signal approximation at the end of the $({k - 1})$th iteration, and let $T$ be the set of components identified by the support merger. Then

### Proof

By construction of $T$, the approximation ${\mathbf{a}}^{k - 1}$ is supported inside $T$, so

Using Lemma 4.4. ‣ 4.4. Estimation ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), we may calculate how far ${\mathbf{a}}^{k - 1}$ lies from the solution to the least-squares problem.

Roughly, the error in the initial iterate is controlled by the current approximation error. ∎

### Iteration Count

We need to determine how many iterations of the least-squares algorithm are required to ensure that the approximation produced is sufficiently good to support the performance of CoSaMP.

### Corollary 5.3 (Estimation by Iterative LS)

Suppose that we initialize the LS algorithm with $\mathbf{z}^{0} = \mathbf{a}^{k - 1}$. After at most three iterations, both Richardson's iteration and conjugate gradient produce a signal estimate $\mathbf{b}$ that satisfies

### Proof

Combine Lemma 5.1. ‣ 5.1. Richardson’s Iteration ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") and Lemma 5.2. ‣ 5.2. Initialization ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") to see that three iterations of Richardson's method yield

The bound for conjugate gradient is slightly better. Let ${{\mathbf{b}}|}_{T} = {\mathbf{z}}^{3}$. According to the estimation result, Lemma 4.4. ‣ 4.4. Estimation ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), we have

An application of the triangle inequality completes the argument. ∎

### CoSaMP with Iterative least-squares

Finally, we need to check that the sparse iteration invariant, Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") still holds when we use an iterative least-squares algorithm.

### Theorem 5.4 (Sparse Iteration Invariant with Iterative LS)

Suppose that we use Richardson's iteration or conjugate gradient for the estimation step, initializing the LS algorithm with the current approximation $\mathbf{a}^{k - 1}$ and performing three LS iterations. Then Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") still holds.

### Proof

We repeat the calculation in Section 4.6 using Corollary 5.3. ‣ 5.3. Iteration Count ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") instead of the simple estimation lemma. To that end, recall that the residual ${\mathbf{r}} = {{\mathbf{x}} - {\mathbf{a}}^{k - 1}}$. Then

This bound is precisely what is required for the theorem to hold. ∎

## Extension to General Signals

In this section, we finally complete the proof of the main result for CoSaMP, Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). The remaining challenge is to remove the hypothesis that the target signal is sparse, which we framed in Theorems 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") and 5.4. ‣ 5.4. CoSaMP with Iterative least-squares ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). Although this difficulty might seem large, the solution is simple and elegant. It turns out that we can view the noisy samples of a general signal as samples of a sparse signal contaminated with a different noise vector that implicitly reflects the tail of the original signal.

### Lemma 6.1 (Reduction to Sparse Case)

Let $\mathbf{x}$ be an arbitrary vector in ${\mathbb{C}}^{N}$. The sample vector $\mathbf{u} = {{\mathbf{\Phi}\mathbf{x}} + \mathbf{e}}$ can also be expressed as $\mathbf{u} = {{\mathbf{\Phi}\mathbf{x}_{s}} + \overset{\sim}{\mathbf{e}}}$ where

### Proof

Decompose ${\mathbf{x}} = {{\mathbf{x}}_{s} + {({{\mathbf{x}} - {\mathbf{x}}_{s}})}}$ to obtain ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}_{s}} + \overset{\sim}{\mathbf{e}}}$ where $\overset{\sim}{\mathbf{e}} = {{\mathbf{\Phi}{({{\mathbf{x}} - {\mathbf{x}}_{s}})}} + {\mathbf{e}}}$. To compute the size of the error term, we simply apply the triangle inequality and Proposition 3.5. ‣ 3. Restricted Isometry Consequences ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"):

Finally, invoke the fact that $\delta_{s} \leq \delta_{4s} \leq 0.1$ to obtain $\sqrt{1 + \delta_{s}} \leq 1.05$. ∎

This lemma is just the tool we require to complete the remaining argument.

### Proof of Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples")

Let $\mathbf{x}$ be a general signal, and use Lemma 6.1. ‣ 6. Extension to General Signals ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples") to write the noisy vector of samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}_{s}} + \overset{\sim}{\mathbf{e}}}$. Apply the sparse iteration invariant, Theorem 4.1. ‣ 4. The Iteration Invariant: Sparse Case ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), or the analog for iterative least-squares, Theorem 5.4. ‣ 5.4. CoSaMP with Iterative least-squares ‣ 5. Analysis of Iterative Least-squares ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"). We obtain

Invoke the lower and upper triangle inequalities to obtain

Finally, recall the estimate for $\left\| \overset{\sim}{\mathbf{e}} \right\|_{2}$ from Lemma 6.1. ‣ 6. Extension to General Signals ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), and simplify to reach

where $\nu$ is the unrecoverable energy (2.1). ∎

## Discussion and Related Work

CoSaMP draws on both algorithmic ideas and analytic techniques that have appeared before. This section describes the other major signal recovery algorithms, and it compares them with CoSaMP. It also attempts to trace the key ideas in the algorithm back to their sources.

### Algorithms for Compressive Sampling

We begin with a short discussion of the major algorithmic approaches to signal recovery from compressive samples. We focus on provably correct methods, although we acknowledge that some *ad hoc* techniques provide excellent empirical results.

The initial discovery works on compressive sampling proposed to perform signal recovery by solving a convex optimization problem. Given a sampling matrix $\mathbf{\Phi}$ and a noisy vector of samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$, consider the mathematical program

In words, we look for a signal reconstruction that is consistent with the samples but has minimal $\ell_{1}$ norm. The intuition behind this approach is that minimizing the $\ell_{1}$ norm promotes sparsity, so allows the approximate recovery of compressible signals. Candès, Romberg, and Tao established in that a minimizer $\mathbf{a}$ of (7.1) satisfies

provided that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{4s} \leq 0.2$. In, the hypothesis on the restricted isometry constant is sharpened to $\delta_{2s} \leq {\sqrt{2} - 1}$. The error bound for CoSaMP is equivalent, modulo the exact value of the constants.

The literature describes a huge variety of algorithms for solving the optimization problem (7.1). The most common approaches involve interior-point methods, projected gradient methods, or iterative thresholding The interior-point methods are guaranteed to solve the problem to a fixed precision in time $O{({m^{2}N^{1.5}})}$, where $m$ is the number of measurements and $N$ is the signal length. Note that the constant in the big-O notation depends on some of the problem data. The other convex relaxation algorithms, while sometimes faster in practice, do not currently offer rigorous guarantees. CoSaMP provides rigorous bounds on the runtime that are much better than the available results for interior-point methods.

Tropp and Gilbert proposed the use of a greedy iterative algorithm called *orthogonal matching pursuit* (OMP) for signal recovery. The algorithm initializes the current sample vector ${\mathbf{v}} = {\mathbf{u}}$. In each iteration, it forms the signal proxy ${\mathbf{y}} = {\mathbf{\Phi}^{\ast}{\mathbf{v}}}$ and identifies a component of the proxy with largest magnitude. It adds the new component to the set $T$ of previously identified components. Then OMP forms a new signal approximation by solving a least-squares problem: ${\mathbf{a}} = {\mathbf{\Phi}_{T}^{\dagger}{\mathbf{u}}}$. Finally, it updates the samples ${\mathbf{v}} = {{\mathbf{u}} - {\mathbf{\Phi}{\mathbf{a}}}}$. These steps are repeated until a halting criterion is satisfied.

Tropp and Gilbert were able to prove a weak result for the performance of OMP. Suppose that $\mathbf{x}$ is a fixed, $s$-sparse signal, and let $m = {Cs{\log N}}$. Draw an $m \times N$ sampling matrix $\mathbf{\Phi}$ whose entries are independent, zero-mean subgaussian^22^2A subgaussian random variable $Z$ satisfies ${{\mathbb{P}}\left\{ {|Z| > t} \right\}} \leq {ce}^{- {ct^{2}}}$ for all $t > 0$. random variables with equal variances. Given noiseless measurements ${\mathbf{u}} = {\mathbf{\Phi}{\mathbf{x}}}$, OMP reconstructs $\mathbf{x}$ after $s$ iterations, except with probability $N^{- 1}$. In this setting, OMP must fail for some sparse signals, so it does not provide the same uniform guarantees as convex relaxation. It is unknown whether OMP succeeds for compressible signals or whether it succeeds when the samples are contaminated with noise.

Donoho et al. invented another greedy iterative method called *stagewise OMP*, or StOMP. This algorithm uses the signal proxy to select multiple components at each step, using a rule inspired by ideas from wireless communications. The algorithm is faster than OMP because of the selection rule, and it sometimes provides good performance, although parameter tuning can be difficult. There are no rigorous results available for StOMP.

Very recently, Needell and Vershynin developed and analyzed another greedy approach, called *regularized OMP*, or ROMP. This algorithm is similar to OMP but uses a more sophisticated selection rule. Among the $s$ largest entries of the signal proxy, it identifies the largest subset whose entries differ in magnitude by at most a factor of two. The work on ROMP represents an advance because the authors establish under restricted isometry hypotheses that their algorithm can approximately recover any compressible signal from noisy samples. More precisely, suppose that the sampling matrix $\mathbf{\Phi}$ has restricted isometry constant $\delta_{8s} \leq {0.01/\sqrt{\log s}}$. Given noisy samples ${\mathbf{u}} = {{\mathbf{\Phi}{\mathbf{x}}} + {\mathbf{e}}}$, ROMP produces a $2s$-sparse signal approximation $\mathbf{a}$ that satisfies

This result is comparable with the result for convex relaxation, aside from the extra logarithmic factor in the restricted isometry hypothesis and the error bound. The results for CoSaMP show that it does not suffer these parasitic factors, so its performance is essentially optimal.

After we initially presented this work, Dai and Milenkovic developed an algorithm called Subspace Pursuit that is very similar to CoSaMP. They established that their algorithm offers performance guarantees analogous with those for CoSaMP. See for details.

Finally, we note that there is a class of sublinear algorithms for signal reconstruction from compressive samples. A sublinear algorithm uses time and space resources that are asymptotically smaller than the length of the signal. One of the earliest such techniques is the Fourier sampling algorithm of Gilbert et al.. This algorithm uses random (but structured) time samples to recover signals that are compressible with respect to the discrete Fourier basis. Given $s{\operatorname{polylog}{(N)}}$ samples^33^3The term $\operatorname{polylog}$ indicates a function that is dominated by a polynomial in the logarithm of its argument., Fourier sampling produces a signal approximation $\mathbf{a}$ that satisfies

except with probability $N^{- 1}$. The result for Fourier sampling holds for each signal (rather than for all). Later, Gilbert et al. developed two other sublinear algorithms, chaining pursuit and HHS pursuit, that offer uniform guarantees for all signals. Chaining pursuit has an error bound

which is somewhat worse than (7.2). HHS pursuit achieves the error bound (7.2). These methods all require more measurements than the linear and superlinear algorithms (by logarithmic factors), and these measurements must be highly structured. As a result, the sublinear algorithms may not be useful in practice.

The sublinear algorithms are all combinatorial in nature. They use ideas from group testing to identify the support of the signal quickly. There are several other combinatorial signal recovery methods due to Cormode--Muthukrishnan and Iwen. These algorithms have drawbacks similar to the sublinear approaches.

### Relative Performance

Table 2 summarizes the relative behavior of these algorithms in terms of the following criteria.

: Does the algorithm work for a variety of sampling schemes? Or does it require structured samples? The designation "RIP" means that a bound on a restricted isometry constant suffices. "Subgauss." means that the algorithm succeeds for the class of subgaussian sampling matrices.

Optimal number of samples:

: Can the algorithm recover $s$ sparse signals from $O{({s{\log N}})}$ measurements? Or are its sampling requirements higher (by logarithmic factors)?

: Does the algorithm recover all signals given a fixed sampling matrix? Or do the results require a sampling matrix to be drawn at random for each signal?

: Does the algorithm succeed when (a) the signal is compressible but not sparse and (b) when the samples are contaminated with noise? In most cases, stable algorithms have error bounds similar to (7.2). See the discussion above for details.

: What is the worst-case cost of the algorithm to recover a real-valued $s$-sparse signal to a fixed relative precision, given a sampling matrix with no special structure? The designation LP($N$, $m$) indicates the cost of solving a linear program with $N$ variables and $m$ constraints, which is $O{({m^{2}N^{1.5}})}$ for an interior-point method. Note that most of the algorithms can also take advantage of fast matrix--vector multiplies to obtain better running times.

Of the linear and superlinear algorithms, CoSaMP achieves the best performance on all these metrics. Although CoSaMP is slower than the sublinear algorithms, it makes up for this shortcoming by allowing more general sampling matrices and requiring fewer samples.

Table 2. Comparison of several signal recovery algorithms. The notation s refers to the sparsity level; m refers the number of measurements; N refers to the signal length. See the text for comments on specific designations.

### Key Ideas

We conclude with a historical overview of the ideas that inform the CoSaMP algorithm and its analysis.

The overall greedy iterative structure of CoSaMP has a long history. The idea of approaching sparse approximation problems in this manner dates to the earliest algorithms. In particular, methods for variable selection in regression, such as forward selection and its relatives, all take this form. Temlyakov's survey describes the historical role of greedy algorithms in nonlinear approximation. Mallat and Zhang introduced greedy algorithms into the signal processing literature and proposed the name *matching pursuit*. Gilbert, Strauss, and their collaborators showed how to incorporate greedy iterative strategies into fast algorithms for sparse approximation problems, and they established the first rigorous guarantees for greedy methods. Tropp provided a new theoretical analysis of OMP in his work. Subsequently, Tropp and Gilbert proved that OMP was effective for compressive sampling.

Unlike the simplest greedy algorithms, CoSaMP identifies many components during each iteration, which allows the algorithm to run faster for many types of signals. It is not entirely clear where this idea first appeared. Several early algorithms of Gilbert et al. incorporate this approach, and it is an essential feature of the Fourier sampling algorithm. More recent compressive sampling recovery algorithms also select multiple indices, including chaining pursuit, HHS pursuit, StOMP, and ROMP.

CoSaMP uses the restricted isometry properties of the sampling matrix to ensure that the identification step is successful. Candès and Tao isolated the restricted isometry conditions in their work on convex relaxation methods for compressive sampling. The observation that restricted isometries can also be used to ensure the success of greedy methods is relatively new. This idea plays a role in HHS pursuit, but it is expressed more completely in the analysis of ROMP.

The pruning step of CoSaMP is essential to maintain the sparsity of the approximation, which is what permits us to use restricted isometries in the analysis of the algorithm. It also has significant ramifications for the running time because it impacts the speed of the iterative least-squares algorithms. This technique originally appeared in HHS pursuit.

The iteration invariant, Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), states that if the error is large then CoSaMP makes substantial progress. This approach to the overall analysis echoes the analysis of other greedy iterative algorithms, including the Fourier sampling method and HHS Pursuit.

Finally, mixed-norm error bounds, such as that in Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), have become an important feature of the compressive sampling literature. This idea appears in the work of Candès--Romberg--Tao on convex relaxation; it is used in the analysis of HHS pursuit; it also plays a role in the theoretical treatment of Cohen--Dahmen--DeVore.
