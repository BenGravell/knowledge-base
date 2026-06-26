## Introduction

Demixing refers to the problem of extracting multiple informative signals from a single, possibly noisy and undersampled, observation. One rather general model for a mixed observation ${\mathbf{z}}_{0} \in {\mathbb{R}}^{\gtrdot}$ takes the form where the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ are the unknown informative signals that we wish to find; the matrices ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ model the relative orientation of the constituent vectors; the operator ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ compresses the observation from $d$ dimensions to $m \leq d$ dimensions; and ${\mathbf{w}} \in {\mathbb{R}}$ is unstructured noise. We assume that all elements appearing in (1.1) are known except for the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ and the noise $\mathbf{w}$.

Numerous applications of the model (1.1) appear in modern data-intensive science. In imaging, for example, the informative signals can model features like stars and galaxies, while an undersampling operator accounts for known occlusions or missing data \[, \]. In graphical model selection, the data may consist of the sum of a sparse component that encodes causality structure and a confounding low-rank component that arises from unobserved latent variables. Similar mixed-signal models appear in robust statistics \[, \] and image processing \[PGW^+^12, \]. In every case, the question of interest is This work answers this question for a popular class of demixing procedures under a random model. The analysis reveals that each constituent possesses a degrees-of-freedom parameter, and that these demixing procedures can succeed with high probability if and only if the total number of measurements exceeds the total degrees of freedom.

In the next two subsections, we describe a well-known recipe that converts *a priori* structural information on the constituents ${\mathbf{x}}_{i}^{\natural}$ into an convex optimization program suited for demixing (1.1). Section 1.3 motivates a random model that we use to study demixing, and Section 1.4 defines the degrees-of-freedom parameter $\delta_{i}$. The main result appears in Section 1.5.

### Structured signals and convex penalties

In the absence of assumptions, it is impossible to reliably recover unknown vectors from a superposition of the form (1.1). In order to have any hope of success, we must make use of domain-specific knowledge about the types of constituents making up our observation. This knowledge often implies that our constituents belong to some set of highly-structured elements. Typical examples of these structured families include *sparse vectors* and *low-rank matrices*.: A sparse vector has many entries equal to zero. Sparse vectors regularly appear in modern signal and data processing applications for a variety of reasons. Bandlimited communications signals, for example, are engineered to be sparse in the frequency domain. The adjacency matrix of a sparse graph is sparse by definition. Piecewise smooth functions are nearly sparse in wavelet bases, so that many natural images exhibit sparsity in the wavelet domain \[, Sec. 9\].: A matrix has low rank if many of its singular values are equal to zero. Low-rank structure appears whenever the rows or columns of a matrix satisfy many nontrivial linear relationships. For example, strong correlations between predictors cause many statistical datasets to exhibit low-rank structure. Rank deficient matrices appear in a number of other areas, including control theory \[, Sec. 6\], video processing, and structured images \[PGW^+^12\].

Other types of structured families that appear in the literature include the family of sign vectors ${\{{\pm 1}\}}^{d} \subset {\mathbb{R}}$, nonnegative sparse vectors, block- and group-sparse vectors and matrices \[, MÇW03\], and orthogonal matrices.

In each of these cases, the structured family possesses an associated convex function that, roughly speaking, measures the amount of complexity of a signal with respect to the family \[\]. For sparse vectors and low-rank matrices, the natural penalty functions are the $\ell_{1}$ norm and the Schatten 1-norm: where $\sigma_{i}{({\mathbf{X}})}$ is the $i$th singular value of $\mathbf{X}$ and the wedge $\land$ denotes the minimum of two numbers. See \[, Sec. 2.2\] for additional examples as well as a principled approach to constructing convex penalty functions. These convex complexity measures form the building blocks of the demixing procedures that we study in this work.

### A generic demixing framework

Given an observation of the form (1.1), we desire a computational method for recovering the constituents ${\mathbf{x}}_{i}^{\natural}$. We now describe a well-known framework that combines convex complexity measures into a convex optimization program that demixes a signal. Specific instances of this recipe appear in numerous works \[ PGW^+^12\], and the general format described below is closely related to the work \[, \].

Assume that, for each constituent ${\mathbf{x}}_{i}^{\natural}$, we have determined an appropriate convex complexity function $f_{i}$. For example, if we suspect that the $i$th constituent ${\mathbf{x}}_{i}^{\natural}$ is sparse, we may choose the $\left. f_{i} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$, the $\ell_{1}$ norm. In the *Lagrange formulation* of the demixing procedure, we combine the regularizers into a single master penalty function $F_{\mathbf{λ}}:{({\mathbb{R}}\supsetneq^{\ltimes}\rightarrow{\mathbb{R}}}$ given by where the weights $\lambda_{i} > 0$. In this formulation, we minimize the master penalty $F_{\mathbf{λ}}$ plus a Euclidean-norm penalty constraint that ensures consistency with our observation: where $\left\| {\mathbf{x}} \right\|^{2}:={\langle{\mathbf{x}},{\mathbf{x}}\rangle}$ is the squared Euclidean norm. We include the Moore--Penrose pseudoinverse ${\mathbf{A}}^{\dagger}$ in the consistency term to ensure that our recovery procedure is independent of the conditioning of $\mathbf{A}$. This demixing procedure succeeds when an optimal point ${({\overset{\sim}{\mathbf{x}}}_{i})}_{i = 1}^{n}$ of (1.2) provides a good approximation for the true constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$.

Rather than restrict ourselves to specific choices of Lagrange parameters $\mathbf{λ}$, we study whether it is possible to demix the constituents of ${\mathbf{z}}_{0}$ using a method of the form (1.2) for the best choice of weights $\mathbf{λ}$. To study this setting, we focus our analysis on the more powerful *constrained formulation* of demixing: | | $\operatorname{minimize}\limits_{{\mathbf{x}}_{i} \in {\mathbb{R}}}$ | $\left\| {{\mathbf{A}}^{\dagger}\left({{{\mathbf{A}}{\sum_{i = 1}^{n}{{\mathbf{U}}_{i}{\mathbf{x}}_{i}}}} - {\mathbf{z}}_{0}} \right)} \right\|^{2}$ | | (1.3) | | | subject to | ${{{f_{i}{({\mathbf{x}}_{i})}} \leq {{f_{i}{({\mathbf{x}}_{i}^{\natural})}}\quad\text{for each}}}\quad{i = {1,\ldots,{n - 1},n}}}.$ | | | The theory of Lagrange multipliers indicates that solving the constrained demixing program (1.3) is essentially equivalent to solving the Lagrange problem (1.2) with the best choice of weights $\mathbf{λ}$. There are some subtle issues in this equivalence, notably the fact that (1.2) can have strictly more optimal points than the corresponding constrained problem (1.3). We refer to \[, Sec. 28\] for further details.

We wish to interrogate whether an optimal point ${({\hat{\mathbf{x}}}_{i})}_{i = 1}^{n}$ of (1.3) forms a good approximation for the true constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$. For this study, we distinguish two situations.: In the noiseless setting where ${\mathbf{w}} = \mathbf{0}$, can we guarantee that the constrained demixing program (1.3) recovers the constituents exactly?: For nonzero noise ${\mathbf{w}} \neq \mathbf{0}$, can we guarantee that any solution to the constrained demixing problem (1.3) provides a good approximation to the constituents ${\mathbf{x}}_{i}^{\natural}$?

The following definition makes these notions precise.

### Definition 1.1 (Exact and stable recovery)

We say that *exact recovery is achievable* in (1.3) if the tuple ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ is the unique optimal point of (1.3) when ${\mathbf{w}} = \mathbf{0}$. We say that *stable recovery is achievable* if there exists number $C > 0$, such that for any optimal point ${({\hat{\mathbf{x}}}_{i})}_{i = 1}^{n}$ of (1.3), we have The value of $C$ may depend on all problem parameters except $\mathbf{w}$.

The goal of this work is to describe when exact and stable recovery are achievable for the constrained demixing program (1.3).

### A generic model for incoherence

A necessary requirement to identify signals from a superimposed observation is that the constituent signals must look different. The superposition of two sparse vectors, for example, is still sparse; *a priori* knowledge that both vectors are sparse provides little guidance in determining how to allocate the nonzero elements between the two constituents. On the other hand, a sparse vector looks very different from a superposition of a small number of sinusoids. This structural diversity makes distinguishing spikes from sines tractable. We extend this idea to more general families by saying that structured vectors that look very different from one another are *incoherent*.

In this work, we follow \[, \] and model incoherence by assuming that the families are *randomly oriented* relative to one another. The set of all possible orientations on $\mathbb{R}$ is the *orthogonal group* $\mathsf{O}_{d}$ consisting of all $d \times d$ orthogonal matrices: The orthogonal group is a compact group, and so it possesses a unique invariant probability measure called the *Haar measure* \[, Ch. 44\]. We model incoherence among the constituents ${\mathbf{x}}_{i}^{\natural}$ by drawing the orientations ${\mathbf{U}}_{i}$ from the Haar measure.

### Definition 1.2 (Random orientation model)

We say that the matrices ${({\mathbf{U}}_{i})}_{i = 1}^{d}$ satisfy the *random orientation model* if the matrices ${\mathbf{U}}_{1},\ldots,{\mathbf{U}}_{n - 1},{\mathbf{U}}_{n}$ are drawn independently from the Haar measure on $\mathsf{O}_{d}$.

The random orientation model is analogous to random measurements models that appear in the compressed sensing literature \[, \]. In this work, however, we find that orienting the structures randomly through the rotations ${\mathbf{U}}_{i}$ provides sufficient randomness for the analysis. We have no need to assume that the measurement matrix $\mathbf{A}$ is random.

### Descent cones and the statistical dimension

Our study of the exact and stable recovery capabilities of the constrained demixing program (1.3) relies on a geometric analysis of the optimality conditions of the convex program (1.3). The key player in this analysis is the following cone that captures the local behavior of a convex function at a point (Figure 1).

Figure 1: Descent cone. [Left] The sublevel set S (shaded) of a convex function f (level lines) at a point x. [Right] The descent cone 𝒟 (f, x) (shaded) is the cone generated by S at x.

### Definition 1.3 (Descent cone)

The descent cone $\mathcal{D}{(f,{\mathbf{x}})}$ of a convex function $f$ at a point $\mathbf{x}$ is the cone generated by the perturbations about $\mathbf{x}$ that do not increase $f$: Intuitively, a convex penalty function $f$ will be more effective at finding a structured vector ${\mathbf{x}}^{\natural}$ if most perturbations around ${\mathbf{x}}^{\natural}$ increase the value of $f$, i.e., if the descent cone $\mathcal{D}{(f,{\mathbf{x}}^{\natural})}$ is small. Our next definition provides a summary parameter that lets us quantify the size of a convex cone.

### Definition 1.4 (Statistical dimension)

Let $C \subset {\mathbb{R}}$ be a closed convex cone, and define the Euclidean projection $\mathbf{\Pi}_{C}:{{\mathbb{R}}\rightarrow{\mathbb{C}}}$ onto $C$ by The *statistical dimension* $\delta{(C)}$ of $C$ is given by the average value where ${\mathbf{g}} \sim {N{(\mathbf{0},\mathbf{I})}}$ is a standard Gaussian vector.

The statistical dimension satisfies a number of properties that make it an appropriate measure of the "size" or "dimension" of a convex cone. It also extends a number of useful properties for the usual dimension of a linear subspace to convex cones \[, Sec. 4\]. Moreover, a number of calculations for the statistical dimension are available in the literature \[ \], which makes the statistical dimension an appealing parameter in practice.

The statistical dimension turns out to be the key parameter which determines the success and failure of demixing under the random orientation model. To shorten notation, we abbreviate the statistical dimensions of the descent cones $\mathcal{D}{(f_{i},{\mathbf{x}}_{i}^{\natural})}$: where the overline denotes the closure.

### Main result

We are now in a position to state our main result.

### Theorem A

With $\delta_{i}$ as in (1.7), define the total dimension $\Delta$ and the scale $\sigma$ by Choose a probability tolerance $\eta \in {}$, and define the transition width Suppose that the matrices ${(\mathbf{U}_{i})}_{i = 1}^{n}$ are drawn from the random orientation model and that the measurement operator $\mathbf{A} \in {\mathbb{R}}^{\gtrdot \times \ltimes}$ has full row rank. Then where we define exact and stable recovery in Definition 1.1. ‣ 1.2 A generic demixing framework ‣ 1 Introduction ‣ The achievable performance of convex demixing").

Theorem A provides detailed information about the capability of constrained demixing (1.3) under the random orientation model.: The capability of (1.3) changes rapidly when the number of measurements $m$ passes through the total statistical dimension $\Delta$. For $m$ somewhat less than $\Delta$, exact recovery is highly unlikely. On the other hand, when $m$ is a bit larger than $\Delta$, we have stable recovery with high probability. This justifies our heuristic that the number of measurements required for demixing is equal to the total statistical dimension.: Theorem A tightly controls the width of the transition region between success and failure. When the probability tolerance $\eta$ is independent of $d$ and $n$, the transition width satisfies The second equality follows from the observation that $\sigma^{2} \leq {nd}$ because the statistical dimension is never larger than the ambient dimension (cf. \[, Sec. 4\]). In many applications, the number $n$ of constituents is independent of the ambient dimension, so the transition between success and failure occurs over no more than $O{(\sqrt{d})}$ measurements as $d\rightarrow\infty$.

Strong probability bounds: Probability tolerances $\eta$ that decay rapidly with the ambient dimension $d$ can provide strong guarantees for demixing \[, Sec. 4.3\]. For example, when the number of measurements $m \geq {\Delta + {cd}}$ for some $c > 0$, Theorem A guarantees that Due to the estimate $\sigma^{2} \leq {nd}$ from above, the constant $c' > 0$ need depend only on $c$ and $n$. Such exponentially small failure probabilities lead to strong demixing bounds using union-bound arguments as in \[, Secs. 6.1.1 & 6.2.2\]. We omit the details for brevity.: How many constituents can we reliably demix? The answer is simple: Consider, for example, the fully observed case $m = d$, and fix a probability of success $\eta$ independent of $d$. Suppose that $\Delta \leq {{({1 - \varepsilon})}d}$ for some $\varepsilon > 0$. For demixing to succeed, by Theorem A, we only need where the equality is (1.12). Thus, the implication (1.10) remains nontrivial as $d\rightarrow\infty$ so long as $n \leq {cd}$ for some sufficiently small $c > 0$.

This growth regime is essentially optimal. It can be shown^11^1The fact that $\delta_{i} > {1/2}$ except in trivial cases follows because the statistical dimension of a ray is $0.5$, every nontrivial cone contains a ray, and the statistical dimension is increasing under set inclusion. that $\delta_{i} \geq {1/2}$ whenever ${\mathbf{x}}_{i}^{\natural}$ is not the unique global minimum of $f_{i}$. Thus, excepting trivial situations, we have $\Delta \geq {n/2}$, so that when $n{}2d$, demixing must fail with high probability by (1.11).

The proof of Theorem A is based on a geometric optimality condition for the constrained demixing program (1.3) that characterizes exact and stable recovery in terms of a configuration of randomly oriented convex cones. A new extension of the approximate kinematic formula lets us provide precise bounds on the probability that this geometric optimality condition holds under the random orientation model.

### Outline

Section 2 describes the related work on demixing. The proof of Theorem A appears in Section 3. Section 4 provides two simple numerical experiments that illustrate the accuracy of Theorem A, and we conclude in Section 5 with some open problems. The technical details in our development appear in the appendices.

### Notation and basic facts

Vectors appear in bold lowercase, while matrices are bold and capitalized. The range and nullspace of a matrix $\mathbf{X}$ are $\mathcal{R}{({\mathbf{X}})}$ and $\mathcal{N}{({\mathbf{X}})}$. The Minkowski sum of sets ${S_{1},S_{2}} \subset {\mathbb{R}}$ is $S_{1} + S_{2}$. When more than two sets are involved, we define the Minkowski sum $\sum_{i}S_{i}$ inductively. We write $- S$ for the reflection of $S$ about $\mathbf{0}$ and $\overline{S}$ for the closure of $S$.

A convex cone $C \subset {\mathbb{R}}$ is a convex set that is positive homogeneous: ${{\mathbf{x}},{\mathbf{y}}} \in C\Longrightarrow{\lambda{({{\mathbf{x}} + {\mathbf{y}}})}} \in C$ for all $\lambda > 0$. All cones in this work contain the origin $\mathbf{0}$. We write $\mathcal{C}_{d}$ for the set of all closed, convex cones in $\mathbb{R}$. For any cone $C \subset {\mathbb{R}}$, we define the polar cone $C^{\circ} \in \mathcal{C}_{d}$ by The bipolar formula states $C^{\circ \circ} = \overline{C}$. We measure the distance between two cones ${C,D} \subset {\mathbb{R}}$ by computing the maximal inner product It follows from the Cauchy--Schwarz inequality that ${{C},{D}} \leq 1$ for every pair of cones, while the equality conditions for Cauchy--Schwarz show that ${{C},{D}} = 1$ if and only if the intersection $\overline{C} \cap \overline{D}$ contains a ray.

We will refer to the following elementary properties of the statistical dimension. For any closed convex cones $C \in \mathcal{C}_{d}$ and $D \in \mathcal{C}_{d'}$, the statistical dimension reverses under polarity and splits under the Cartesian product Simple proofs of relations (1.15) and (1.16) appear in \[, Sec. 4\].

## Context and related work

This work is a successor to the author's earlier work on demixing with $n = 2$ components in the fully observed $m = d$ setting. The techniques used in this paper hail, which studied phase transitions in randomized optimization programs. While those two works are the closest in spirit to our development below, numerous works on demixing appear in the literature. This section provides an overview of the literature on demixing, from its origins in sparse approximation to recent developments towards a general theory.

### Demixing and sparse approximation

Early work on demixing methods used the $\ell_{1}$ norm to encourage sparsity. Taylor, Banks, & McCoy used (1.2) with $\left. f_{1} = f_{2} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$ to demix a sparse signal from sparse noise, with applications to geophysics. About ten years later, Donoho & Stark explained how uncertainty principles can guarantee the success of demixing signals that are sparse in frequency from those that are sparse in time using the $\ell_{1}$ norm.

The analysis of Donoho & Huo provided incoherence-based guarantees which demonstrate that exact recovery is possible under fairly generic conditions. This work motivated interest in *morphological component analysis* (MCA) for image processing \[ BSF^+^07\]. MCA posits that images are the superposition of a small number of signals from a known dictionary---such as pointillistic stars and wispy galaxies. Demixing with the $\ell_{1}$ norm provides a computational framework for decomposing these images into their constituent signals.

A number of recent papers provide theoretical guarantees for demixing with the $\ell_{1}$ norm. Wright & Ma showed that $\ell_{1}$-norm demixing can recovery a nearly dense vector from a sufficiently sparse corruption. Additional work along these lines appears in \[ \]. The phase transition for demixing two signals using the $\ell_{1}$-norm was first identified by the present authors. The very recent work recovers similar guarantees under a slightly different model, and it also provides stability guarantees.

### Demixing beyond sparsity

Applications for mixed signal model (1.1) when the constituents satisfy more general structural assumptions appear in a number of areas. The work of Chandrasekaran et al. \[ \] demonstrated that a demixing program of the form (1.2) can recover the superposition of a sparse and low-rank matrix. The independent work of Candès et al. uses this model for robust principal component analysis and image processing applications.

Modifications to the rank-sparsity model find applications in robust statistics \[ \] and its compressed variants \[, \], image processing \[, PGW^+^12\], and network analysis \[ \].

### A general theory takes shape

Recent work has started to unify the piecemeal results discussed above. Chandrasekaran et. al gave a general treatment of the $n = 1$ case using Gaussian width analysis. For the $n = 2$ and $m = d$ case, the present authors used tools from integral geometry to demonstrate numerically matching upper and lower exact recovery guarantees for demixing. The first fully rigorous account of phase transitions in demixing problems, for the $n = 2$ and $m = d$ case, appeared in work of Amelunxen et al..

In very recent work, Foygel & Mackey studied the $n = 2$ case with a linear undersampling model that differs slightly from the one we consider in this work. These empirically sharp results recover and extend some of the bounds, but they do not prove that a phase transition occurs. Notably, the work of Foygel & Mackey offers guidance on the choice of Lagrange parameters.

The only previous result for the demixing setup where the number of constituents $n$ is arbitrary appears in Wright et al.. Their results provide recovery guarantees for the Lagrange formulation of the undersampled demixing program (1.2) when sufficiently strong guarantees are available for the fully observed $m = d$ case. Their guarantees, however, do not identify the phase transition between success and failure.

## Proof of the main result

This section presents the arc of the argument leading to Theorem A, but it postpones the proof of intermediate results to the appendices. Section 3.1 describes deterministic conditions for exact and stable recovery. In Section 3.2, we provide simplifications for these deterministic conditions that hold almost surely under the random orientation model. These simplifications reduce the recovery conditions to a single geometric condition involving the intersection of (polars of) randomly oriented descent cones.

Our key tool, the *approximate kinematic formula*, appears in Section 3.3. This formula bounds the probability that an arbitrary number of randomly oriented cones intersect in terms of the statistical dimension. It extends and refines a result of Amelunxen et al. \[, Thm. 7.1\]. We complete the argument in Section 3.4 by applying the kinematic formula to our simplified geometric recovery condition.

### Deterministic recovery conditions

We begin the proof of Theorem A with deterministic conditions for exact recovery and stability for the constrained demixing problem (1.3). These conditions rephrase exact recovery and stability in terms of configurations of descent cones. In order to highlight the symmetries in these conditions, we first introduce some notation that we use throughout the proof. Define The *exact recovery condition* is the event In words, the exact recovery condition requires that no descent cone shares a ray with the sum of the other cones. The *stable recovery condition* strengthens (ERC) by requiring that the cones are separated by some positive angle: where we recall the definition (1.14) of the inner product between cones. These two conditions precisely characterize exact and stable recovery for constrained demixing (1.3).

### Lemma 3.1

Success is achievable in the noiseless case if and only if the exact recovery condition (ERC) holds. If the stable recovery condition condition (SRC) holds, then stability is achievable.

We prove Lemma 3.1 in Appendix A. The proof of exact recovery is based on a perturbative argument that extends the proof \[, Lem. 2.3\] of the recovery conditions for demixing two signals. The stable recovery result follows similar lines.

### Three simplifications

Our goal in this work is the analysis of demixing when the orientations are drawn independently from the Haar measure on the orthogonal group. In this section, we describe some simplifications that arise from the fact that this measure is *invariant* and *continuous*. In the end, we reduce the problem of studying the exact and stable recovery conditions (ERC) and (SRC) hold to the problem of studying a single geometric question: *What is the probability that $n + 1$ randomly oriented cones share a ray?* In Section 3.2.1, we show that we can replace the deterministic nullspace $\mathcal{N}{({\mathbf{A}})}$ with a randomly oriented $d - m$ dimensional subspace, which effectively randomizes the nullspace of the measurement operator $\mathbf{A}$. In Section 3.2.2, we find that (ERC) and (SRC) are equivalent under the random orientation model. Finally, we simplify the exact recovery condition (ERC) in Section 3.2.3.

### Randomizing the nullspace

In definition (3.1), we fix the rotation ${\mathbf{U}}_{i} = \mathbf{I}$ in order to make the statement of the exact and stable recovery conditions symmetric. However, this symmetry is broken by the random orientation model because only ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ are taken at random. The next result restores this symmetry.

### Lemma 3.2

Suppose that ${(\mathbf{U}_{i})}_{i = 1}^{n}$ are drawn from the random orientation model and fix $\mathbf{U}_{n + 1} = \mathbf{I}$. Let ${(\mathbf{Q}_{i})}_{i = 1}^{n + 1}$ be an $({n + 1})$-tuple of i.i.d. random rotations. Then | | ${\mathbb{P}}\left\{ {\text{~holds}} \right\}$ | $= {{\mathbb{P}}\left\{ {{\nmid\mathbf{\mathbb{Q}}_{\beth}{\mathbb{D}}_{\beth}} \cap {\sum_{\gimel \neq \beth}{\mathbf{\mathbb{Q}}_{\gimel}{\mathbb{D}}_{\gimel}\nleftrightarrow{\{\mathbf{\nvdash}\}}\text{~for each~}\beth\nleftrightarrow\nVdash\nparallel\ldots\nparallel\ltimes\nparallel\ltimes\nsupseteq\nVdash}}} \right\}\nmid}$ | | (3.2) | | Under the same conditions, | | | ${\mathbb{P}}\left\{ {\text{~holds}} \right\}$ | $= {{\mathbb{P}}\left\{ {\nmid\mathbf{\mathbb{Q}}_{\beth}{\mathbb{D}}_{\beth}\nparallel{\sum_{\gimel \neq \beth}{\mathbf{\mathbb{Q}}_{\gimel}{\mathbb{D}}_{\gimel}\nLeftrightarrow\nVdash\text{~for each~}\beth\nleftrightarrow\nVdash\nparallel\ldots\nparallel\ltimes\nparallel\ltimes\nsupseteq\nVdash}}} \right\}\nmid}$ | | (3.3) | The proof, which appears in Appendix B.1, requires only an elementary application of the rotation invariance of the Haar measure.

### Exchanging stable for exact recovery

Our second simplification shows that the stability condition (SRC) holds with the same probability that the recovery condition (ERC) holds.

### Lemma 3.3

The probabilities appearing in (3.2) and (3.3) are equal.

This result is immediate for closed cones: compactness arguments imply that two closed cones do not intersect if and only if the angle between the cones is strictly less than one. Hence, (ERC) is equivalent to (SRC) when all of the descent cones $D_{i}$ are closed. The proof of Lemma 3.3 in Appendix B.2 shows that this equivalence almost surely holds even when the cones are not closed.

### Polarizing the exact recovery condition

Our final simplification reduces the $n + 1$ intersections in (3.2) to a single intersection.

### Lemma 3.4

Suppose that $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i \in {\{ 1,\ldots,n,{n + 1}\}}$. Then where the matrices ${(\mathbf{Q}_{i})}_{i = 1}^{n}$ are drawn i.i.d. from the random orientation model.

The demonstration appears in Appendix B.3, but we describe main difficulty here. Let ${C,D} \subset {\mathbb{R}}$ be two cones such that ${{- C} \cap D} = {\{\mathbf{0}\}}$. The separating hyperplane theorem provides a nonzero ${\mathbf{w}} \in {\mathbb{R}}$ that weakly separates $- C$ and $D$: By definition of polar cones, we have ${\mathbf{w}} \in {C^{\circ} \cap D^{\circ}}$, so that polar cones intersect nontrivially.

On the other hand, reversing the argument above shows that any nonzero ${\mathbf{w}} \in {C^{\circ} \cap D^{\circ}} \neq {\{\mathbf{0}\}}$ weakly separates $- C$ from $D$. Unfortunately, weak separation is not enough to conclude the strong separation ${{- C} \cap D} = {\{\mathbf{0}\}}$. Proposition B.5 in Appendix B.3 shows that the event ${C^{\circ} \cap D^{\circ}} \neq {\{\mathbf{0}\}}$ almost surely implies the event ${{- C} \cap D} = {\{\mathbf{0}\}}$ when $C$ and $D$ are randomly oriented. The proof of Lemma 3.4 bootstraps this result to the multiple cone case.

### The approximate kinematic formula

The simplifications in Section 3.2 reduce the study of (ERC) and (SRC) to the question of computing the probability (3.4) that randomly oriented cones intersect. Remarkably, formulas for the probability that two randomly oriented cones share a ray appear in literature on stochastic geometry under the name *kinematic formulas* \[, \]. While exact, these formulas involve geometric parameters that are typically difficult to compute.

In recent work, the present authors and collaborators demonstrate that the classical kinematic formulas can be summarized using the statistical dimension \[, Thm. 7.1\]. The following result extends this formula to the intersection of an arbitrary number of randomly oriented cones.

### Theorem 3.5 (Approximate kinematic formula)

Let ${C_{1},\ldots,C_{n - 1},C_{n}} \in \mathcal{C}_{d}$ be closed, convex cones and $L \subset {\mathbb{R}}$ an $m$-dimensional linear subspace. Define the parameters Suppose that ${(\mathbf{Q}_{i})}_{i = 1}^{n + 1}$ are i.i.d. random rotations. Then for any $\lambda > 0$, The concentration function $p_{\theta}{(\lambda)}$ is defined for $\lambda > 0$ by The proof of this result forms the topic of Appendix C. The argument requires some background from conic integral geometry that we provide in Appendix C.1. The proof of Theorem 3.5. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing") appears in Appendix C.2.

### Completing the proof

At this point, we have presented all of the components needed to complete the proof of Theorem A. Let us summarize the progress. Lemma 3.1 shows that (ERC) and (SRC) characterize exact and stable recovery. Under the random orientation model, the probability that the stable recovery condition (SRC) holds is equal to the probability that the exact recovery condition (ERC) holds (Lemma 3.3). We have also seen that so long as $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i \in {\{ 1,\ldots,n,{n + 1}\}}$ (Lemmas 3.2 and 3.4).

To complete the proof of Theorem A, we use the approximate kinematic formula of Theorem 3.5. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing") to develop lower and upper bounds on the probability (3.9). This establishes the implications (1.10) and (1.11) when $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i$. We defer the degenerate case where $D_{i} = {\{\mathbf{0}\}}$ for all except (possibly) one index $i$ to Appendix D.

### Proof of Theorem A

We assume that $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i$. The polarity formula for the statistical dimension (1.15) implies where we use the fact that $\delta_{i} = {\delta{({\overline{D}}_{i})}}$ by definitions (1.7) and (3.1) of $\delta_{i}$ and $D_{i}$. For the same reason, we have where the width parameter $\sigma$ is defined in (1.8). Moreover, definition (3.1) shows that the cone $D_{n + 1}^{\circ}$ is a linear subspace with because ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ has full row rank by assumption.

Therefore, when $m \geq {\Delta + \lambda_{\ast}}$ the lower bound (3.7. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing")) of the approximate kinematic formula implies Similarly, when $m \leq {\Delta - \lambda_{\ast}}$, the upper bound (3.6. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing")) of the approximate kinematic formula provides In light of Lemmas 3.1, 3.2, 3.3, and 3.4, the inequalities (3.10) and (3.11) imply claims (1.10) and (1.11) once we verify that To verify (3.12), we invert the definition (3.8. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing")) of $p_{\sigma}$ and solve a quadratic equation to find where $L:={\log{({1/\eta})}}$. Since $\sqrt{a^{2} + b^{2}} \leq {a + b}$ for positive $a$ and $b$, we see Thus (3.12) holds for our choice $\lambda_{\ast}$, as claimed. This completes the proof in the case where $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i$. We complete the proof for the remaining case in Appendix D. ∎

## Numerical examples

In this section, we describe two simple numerical experiments that demonstrate the accuracy of Theorem A. In our first example, we consider demixing three components, two of them sparse, the third a sign vector. Our second example considers demixing two sparse vectors with undersampling. Technical details about the experiments are collected in Appendix E.

Figure 2: Demixing experiments from Section 4. The colormaps display the empirical probability of successful demixing, from complete success (white) to total failure (black). The transition region (gray) contains a mixture of successes and failures. Three contour lines indicate 95% (brown), 50% (red), and 5% (pink) empirical success lines. The yellow curve indicates where an approximation to the total statistical dimension Δ equals to the number of measurements m. [Left] Demixing two sparse vectors from a sign vector in dimension d = 200 with complete measurements. [Right] Demixing two sparse vectors in dimension d = 200 from m = 25, 50, 75, 100 measurements.

### Sparse, sparse, and sign

In our first experiment, we fix the ambient dimension $d = 200$ and generate a mixed observation of the form where ${\mathbf{x}}_{1}^{\natural}$ and ${\mathbf{x}}_{2}^{\natural}$ are sparse vectors, ${\mathbf{x}}_{3}^{\natural} \in {\{{\pm 1}\}}^{d}$ is a sign vector, and the tuple ${({\mathbf{U}}_{i})}_{i = 1}^{3}$ consists of i.i.d. random rotations. In order to demix this observation, we solve the constrained demixing program | | $\operatorname{minimize}\limits_{{\mathbf{x}}_{i} \in {\mathbb{R}}}$ | $\left\| {{{{\mathbf{U}}_{1}{\mathbf{x}}_{1}} + {{\mathbf{U}}_{2}{\mathbf{x}}_{2}} + {{\mathbf{U}}_{3}{\mathbf{x}}_{3}}} - {\mathbf{z}}_{0}} \right\|^{2}$ | | (4.1) | | | subject to | ${{\left\| {\mathbf{x}}_{1} \right\|_{\ell_{1}} \leq \left\| {\mathbf{x}}_{1}^{\natural} \right\|_{\ell_{1}}},{{\left\| {\mathbf{x}}_{2} \right\|_{\ell_{1}} \leq {\left\| {\mathbf{x}}_{2}^{\natural} \right\|_{\ell_{1}},\text{and}}}\quad{\left\| {\mathbf{x}}_{3} \right\|_{\ell_{\infty}} \leq \left\| {\mathbf{x}}_{3}^{\natural} \right\|_{\ell_{\infty}}}}},$ | | | where $\left\| {\mathbf{x}} \right\|_{\ell_{\infty}}:={\max_{i = {1,\ldots,d}}{|x_{i}|}}$ is the $\ell_{\infty}$ norm that is a convex penalty function associated to the binary sign vectors ${\{{\pm 1}\}}^{d}$.

Figure 2 \[left\] shows the results of this experiment as the sparsity of ${\mathbf{x}}_{1}^{\natural}$ and ${\mathbf{x}}_{2}^{\natural}$ vary. The colormap indicates the empirical probability of success over $35$ trials. The yellow curve uses provably accurate formulas from \[, Sec. 4\] to approximate the location where The agreement between the $50\%$ empirical success curve and the theoretical yellow curve is remarkable. See Appendix E for further details.

### Undersampled sparse and sparse

In our second experiment, we fix the ambient dimension $d = 200$ and consider demixing the observation where ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ has full row rank, the constituents ${\mathbf{x}}_{1}^{\natural}$ and ${\mathbf{x}}_{2}^{\natural}$ are sparse, and ${\mathbf{U}}_{1}$ and ${\mathbf{U}}_{2}$ are drawn from the random orientation model. We demix the observation by solving | | $\operatorname{minimize}\limits_{{\mathbf{x}}_{i} \in {\mathbb{R}}}$ | $\left\| {{\mathbf{A}}^{\dagger}\left({{{\mathbf{A}}{({{{\mathbf{U}}_{1}{\mathbf{x}}_{1}} + {{\mathbf{U}}_{2}{\mathbf{x}}_{2}}})}} - {\mathbf{z}}_{0}} \right)} \right\|^{2}$ | | (4.2) | | | subject to | ${\left\| {\mathbf{x}}_{1} \right\|_{\ell_{1}} \leq {\left\| {\mathbf{x}}_{1}^{\natural} \right\|_{\ell_{1}}\quad\text{and}}}\quad{\left\| {\mathbf{x}}_{2} \right\|_{\ell_{1}} \leq \left\| {\mathbf{x}}_{2}^{\natural} \right\|_{\ell_{1}}}$ | | | The results of this experiment with $m = {25,50,75}$ and $100$ appear in Figure 2 \[right\]. The colormaps indicate the empirical probability of success over $35$ trials as the sparsity of ${\mathbf{x}}_{1}^{\natural}$ and ${\mathbf{x}}_{2}^{\natural}$ varies. The yellow curve approximates the location where Once again, this yellow curve agrees very well with the red $50\%$ empirical success contour.

## Conclusions and open problems

This work unifies and resolves a number of theoretical questions regarding when it is possible to demix a superposition of incoherent signals. Under our random incoherence model, we find that demixing is possible if and only if the total number of measurements is greater than the total statistical dimension. While this result provides an intuitive and unifying theory for a large class of demixing problems, there are several important open problems that must be addressed before a complete "theory of demixing" emerges.: Most of the prior work on demixing provides guarantees under explicit choices of the Lagrange parameter for (1.2), yet to the best of our knowledge, the only work that demonstrates sharp recovery bounds with specified Lagrange parameters occur for the LASSO problem, where $n = 1$ and $\left. f_{1} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$. Very recent work of Stojnic achieves comparable guarantees using a different approach.

Explicit choices of Lagrange parameters appear. These choices provide near-optimal empirical performance, but currently there is no proof that their choice of parameters reaches the phase transition that we identify. It would be very interesting to provide provably optimal choices of Lagrange parameters for demixing.

Other random models: Our numerical experience indicates that the incoherence model considered in this work is predictive for highly incoherent situations. However, these results appear overly optimistic in more coherent situations. The difference between these situations appears, for example, in an application to calcium imaging \[, Fig. 3\]. Extending our results to other incoherence models will clarify where the phase transition in Theorem A predicts empirical performance, and where it does not.

Statistical dimension calculations: For practical applications of this work, we require accurate statistical dimension calculations. A recipe for these computations put forward has provable guarantees under some technical conditions (cf. \[, Sec. 4.4\] and \[, Prop. 1\]), but expressions for the statistical dimension of a number of important convex regularizers remains unknown. New statistical dimension computations immediately extend the reach of the methods used in this paper.
