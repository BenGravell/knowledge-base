<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Achievable Performance of Convex Demixing

Topics include Convex demixing, Conic geometry, Statistical dimension, Signal separation, Phase transitions, Noisy observations, Structured recovery.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Generalizes convex demixing analysis to superimposed, undersampled, and noisy observations, emphasizing the achievable limits of convex programs under generic incoherence. The central takeaway is geometric: each structure contributes an intrinsic degrees-of-freedom term, and convex demixing succeeds essentially when the measurement dimension exceeds the sum of those terms, giving a precise benchmark for what convex separation can and cannot recover.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Demixing is the problem of identifying multiple structured signals from a superimposed, undersampled, and noisy observation. This work analyzes a general framework, based on convex optimization, for solving demixing problems. When the constituent signals follow a generic incoherence model, this analysis leads to precise recovery guarantees. These results admit an attractive interpretation: each signal possesses an intrinsic degrees-of-freedom parameter, and demixing can succeed if and only if the dimension of the observation exceeds the total degrees of freedom present in the observation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Demixing refers to the problem of extracting multiple informative signals from a single, possibly noisy and undersampled, observation. One rather general model for a mixed observation ${\mathbf{z}}_{0} \in {\mathbb{R}}^{\gtrdot}$ takes the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ are the unknown informative signals that we wish to find; the matrices ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ model the relative orientation of the constituent vectors; the operator ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ compresses the observation from $d$ dimensions to $m \leq d$ dimensions; and ${\mathbf{w}} \in {\mathbb{R}}$ is unstructured noise. We assume that all elements appearing in (1.1) are known except for the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ and the noise $\mathbf{w}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerous applications of the model (1.1) appear in modern data-intensive science. In imaging, for example, the informative signals can model features like stars and galaxies, while an undersampling operator accounts for known occlusions or missing data. In graphical model selection, the data may consist of the sum of a sparse component that encodes causality structure and a confounding low-rank component that arises from unobserved latent variables. Similar mixed-signal models appear in robust statistics and image processing \[PGW^+^12, \]. In every case, the question of interest is

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work answers this question for a popular class of demixing procedures under a random model. The analysis reveals that each constituent possesses a degrees-of-freedom parameter, and that these demixing procedures can succeed with high probability if and only if the total number of measurements exceeds the total degrees of freedom.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the next two subsections, we describe a well-known recipe that converts *a priori* structural information on the constituents ${\mathbf{x}}_{i}^{\natural}$ into an convex optimization program suited for demixing (1.1). Section 1.3 motivates a random model that we use to study demixing, and Section 1.4 defines the degrees-of-freedom parameter $\delta_{i}$. The main result appears in Section 1.5.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

In the absence of assumptions, it is impossible to reliably recover unknown vectors from a superposition of the form (1.1). In order to have any hope of success, we must make use of domain-specific knowledge about the types of constituents making up our observation. This knowledge often implies that our constituents belong to some set of highly-structured elements. Typical examples of these structured families include *sparse vectors* and *low-rank matrices*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

: A sparse vector has many entries equal to zero. Sparse vectors regularly appear in modern signal and data processing applications for a variety of reasons. Bandlimited communications signals, for example, are engineered to be sparse in the frequency domain. The adjacency matrix of a sparse graph is sparse by definition. Piecewise smooth functions are nearly sparse in wavelet bases, so that many natural images exhibit sparsity in the wavelet domain \[, Sec. 9\].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

: A matrix has low rank if many of its singular values are equal to zero. Low-rank structure appears whenever the rows or columns of a matrix satisfy many nontrivial linear relationships. For example, strong correlations between predictors cause many statistical datasets to exhibit low-rank structure. Rank deficient matrices appear in a number of other areas, including control theory \[, Sec. 6\], video processing, and structured images \[PGW^+^12\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

Other types of structured families that appear in the literature include the family of sign vectors ${\{{\pm 1}\}}^{d} \subset {\mathbb{R}}$, nonnegative sparse vectors, block- and group-sparse vectors and matrices \[, MÇW03\], and orthogonal matrices.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

In each of these cases, the structured family possesses an associated convex function that, roughly speaking, measures the amount of complexity of a signal with respect to the family.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Structured signals and convex penalties", "weight": 1.0} -->

where $\sigma_{i}{({\mathbf{X}})}$ is the $i$th singular value of $\mathbf{X}$ and the wedge $\land$ denotes the minimum of two numbers. See \[, Sec. 2.2\] for additional examples as well as a principled approach to constructing convex penalty functions. These convex complexity measures form the building blocks of the demixing procedures that we study in this work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

Given an observation of the form (1.1), we desire a computational method for recovering the constituents ${\mathbf{x}}_{i}^{\natural}$. We now describe a well-known framework that combines convex complexity measures into a convex optimization program that demixes a signal. Specific instances of this recipe appear in numerous works \[ PGW^+^12\], and the general format described below is closely related to the work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

Assume that, for each constituent ${\mathbf{x}}_{i}^{\natural}$, we have determined an appropriate convex complexity function $f_{i}$. For example, if we suspect that the $i$th constituent ${\mathbf{x}}_{i}^{\natural}$ is sparse, we may choose the $\left. f_{i} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$, the $\ell_{1}$ norm. In the *Lagrange formulation* of the demixing procedure, we combine the regularizers into a single master penalty function $F_{\mathbf{λ}}:{({\mathbb{R}}\supsetneq^{\ltimes}\rightarrow{\mathbb{R}}}$ given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

where $\left\| {\mathbf{x}} \right\|^{2}:={\langle{\mathbf{x}},{\mathbf{x}}\rangle}$ is the squared Euclidean norm. We include the Moore--Penrose pseudoinverse ${\mathbf{A}}^{\dagger}$ in the consistency term to ensure that our recovery procedure is independent of the conditioning of $\mathbf{A}$. This demixing procedure succeeds when an optimal point ${({\overset{\sim}{\mathbf{x}}}_{i})}_{i = 1}^{n}$ of (1.2) provides a good approximation for the true constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

Rather than restrict ourselves to specific choices of Lagrange parameters $\mathbf{λ}$, we study whether it is possible to demix the constituents of ${\mathbf{z}}_{0}$ using a method of the form (1.2) for the best choice of weights $\mathbf{λ}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

The theory of Lagrange multipliers indicates that solving the constrained demixing program (1.3) is essentially equivalent to solving the Lagrange problem (1.2) with the best choice of weights $\mathbf{λ}$. There are some subtle issues in this equivalence, notably the fact that (1.2) can have strictly more optimal points than the corresponding constrained problem (1.3). We refer to \[, Sec. 28\] for further details.

<!-- chunk {"id": "body-0020", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

We wish to interrogate whether an optimal point ${({\hat{\mathbf{x}}}_{i})}_{i = 1}^{n}$ of (1.3) forms a good approximation for the true constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$. For this study, we distinguish two situations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

: In the noiseless setting where ${\mathbf{w}} = \mathbf{0}$, can we guarantee that the constrained demixing program (1.3) recovers the constituents exactly?

<!-- chunk {"id": "body-0022", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

: For nonzero noise ${\mathbf{w}} \neq \mathbf{0}$, can we guarantee that any solution to the constrained demixing problem (1.3) provides a good approximation to the constituents ${\mathbf{x}}_{i}^{\natural}$?

<!-- chunk {"id": "body-0023", "role": "body", "section": "A generic demixing framework", "weight": 1.0} -->

The following definition makes these notions precise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

A necessary requirement to identify signals from a superimposed observation is that the constituent signals must look different. The superposition of two sparse vectors, for example, is still sparse; *a priori* knowledge that both vectors are sparse provides little guidance in determining how to allocate the nonzero elements between the two constituents. On the other hand, a sparse vector looks very different from a superposition of a small number of sinusoids. This structural diversity makes distinguishing spikes from sines tractable. We extend this idea to more general families by saying that structured vectors that look very different from one another are *incoherent*.

<!-- chunk {"id": "body-0025", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

In this work, we follow and model incoherence by assuming that the families are *randomly oriented* relative to one another.

<!-- chunk {"id": "body-0026", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

The orthogonal group is a compact group, and so it possesses a unique invariant probability measure called the *Haar measure* \[, Ch. 44\]. We model incoherence among the constituents ${\mathbf{x}}_{i}^{\natural}$ by drawing the orientations ${\mathbf{U}}_{i}$ from the Haar measure.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Descent cones and the statistical dimension", "weight": 1.0} -->

Our study of the exact and stable recovery capabilities of the constrained demixing program (1.3) relies on a geometric analysis of the optimality conditions of the convex program (1.3). The key player in this analysis is the following cone that captures the local behavior of a convex function at a point (Figure 1).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main result", "weight": 1.0} -->

We are now in a position to state our main result.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Outline", "weight": 1.0} -->

Section 2 describes the related work on demixing. The proof of Theorem A appears in Section 3. Section 4 provides two simple numerical experiments that illustrate the accuracy of Theorem A, and we conclude in Section 5 with some open problems. The technical details in our development appear in the appendices.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Context and related work", "weight": 1.0} -->

This work is a successor to the author's earlier work on demixing with $n = 2$ components in the fully observed $m = d$ setting. The techniques used in this paper hail, which studied phase transitions in randomized optimization programs. While those two works are the closest in spirit to our development below, numerous works on demixing appear in the literature. This section provides an overview of the literature on demixing, from its origins in sparse approximation to recent developments towards a general theory.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Demixing and sparse approximation", "weight": 1.0} -->

Early work on demixing methods used the $\ell_{1}$ norm to encourage sparsity. Taylor, Banks, & McCoy used (1.2) with $\left. f_{1} = f_{2} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$ to demix a sparse signal from sparse noise, with applications to geophysics. About ten years later, Donoho & Stark explained how uncertainty principles can guarantee the success of demixing signals that are sparse in frequency from those that are sparse in time using the $\ell_{1}$ norm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Demixing and sparse approximation", "weight": 1.0} -->

The analysis of Donoho & Huo provided incoherence-based guarantees which demonstrate that exact recovery is possible under fairly generic conditions. This work motivated interest in *morphological component analysis* (MCA) for image processing \[ BSF^+^07\]. MCA posits that images are the superposition of a small number of signals from a known dictionary---such as pointillistic stars and wispy galaxies. Demixing with the $\ell_{1}$ norm provides a computational framework for decomposing these images into their constituent signals.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Demixing and sparse approximation", "weight": 1.0} -->

A number of recent papers provide theoretical guarantees for demixing with the $\ell_{1}$ norm. Wright & Ma showed that $\ell_{1}$-norm demixing can recovery a nearly dense vector from a sufficiently sparse corruption. Additional work along these lines appears. The phase transition for demixing two signals using the $\ell_{1}$-norm was first identified by the present authors. The very recent work recovers similar guarantees under a slightly different model, and it also provides stability guarantees.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Demixing beyond sparsity", "weight": 1.0} -->

Applications for mixed signal model (1.1) when the constituents satisfy more general structural assumptions appear in a number of areas. The work of Chandrasekaran et al. demonstrated that a demixing program of the form (1.2) can recover the superposition of a sparse and low-rank matrix. The independent work of Candès et al. uses this model for robust principal component analysis and image processing applications.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Demixing beyond sparsity", "weight": 1.0} -->

Modifications to the rank-sparsity model find applications in robust statistics and its compressed variants, image processing \[, PGW^+^12\], and network analysis.

<!-- chunk {"id": "body-0036", "role": "body", "section": "A general theory takes shape", "weight": 1.0} -->

Recent work has started to unify the piecemeal results discussed above. Chandrasekaran et. al gave a general treatment of the $n = 1$ case using Gaussian width analysis. For the $n = 2$ and $m = d$ case, the present authors used tools from integral geometry to demonstrate numerically matching upper and lower exact recovery guarantees for demixing. The first fully rigorous account of phase transitions in demixing problems, for the $n = 2$ and $m = d$ case, appeared in work of Amelunxen et al..

<!-- chunk {"id": "body-0037", "role": "body", "section": "A general theory takes shape", "weight": 1.0} -->

In very recent work, Foygel & Mackey studied the $n = 2$ case with a linear undersampling model that differs slightly from the one we consider in this work. These empirically sharp results recover and extend some of the bounds, but they do not prove that a phase transition occurs. Notably, the work of Foygel & Mackey offers guidance on the choice of Lagrange parameters.

<!-- chunk {"id": "body-0038", "role": "body", "section": "A general theory takes shape", "weight": 1.0} -->

The only previous result for the demixing setup where the number of constituents $n$ is arbitrary appears in Wright et al.. Their results provide recovery guarantees for the Lagrange formulation of the undersampled demixing program (1.2) when sufficiently strong guarantees are available for the fully observed $m = d$ case. Their guarantees, however, do not identify the phase transition between success and failure.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deterministic recovery conditions", "weight": 1.0} -->

We begin the proof of Theorem A with deterministic conditions for exact recovery and stability for the constrained demixing problem (1.3). These conditions rephrase exact recovery and stability in terms of configurations of descent cones. In order to highlight the symmetries in these conditions, we first introduce some notation that we use throughout the proof. Define

<!-- chunk {"id": "body-0040", "role": "body", "section": "Deterministic recovery conditions", "weight": 1.0} -->

The *exact recovery condition* is the event

<!-- chunk {"id": "body-0041", "role": "body", "section": "Deterministic recovery conditions", "weight": 1.0} -->

In words, the exact recovery condition requires that no descent cone shares a ray with the sum of the other cones.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Deterministic recovery conditions", "weight": 1.0} -->

where we recall the definition (1.14) of the inner product between cones. These two conditions precisely characterize exact and stable recovery for constrained demixing (1.3).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Three simplifications", "weight": 1.0} -->

Our goal in this work is the analysis of demixing when the orientations are drawn independently from the Haar measure on the orthogonal group. In this section, we describe some simplifications that arise from the fact that this measure is *invariant* and *continuous*. In the end, we reduce the problem of studying the exact and stable recovery conditions (ERC) and (SRC) hold to the problem of studying a single geometric question: *What is the probability that $n + 1$ randomly oriented cones share a ray?*

<!-- chunk {"id": "body-0044", "role": "body", "section": "Three simplifications", "weight": 1.0} -->

In Section 3.2.1, we show that we can replace the deterministic nullspace $\mathcal{N}{({\mathbf{A}})}$ with a randomly oriented $d - m$ dimensional subspace, which effectively randomizes the nullspace of the measurement operator $\mathbf{A}$. In Section 3.2.2, we find that (ERC) and (SRC) are equivalent under the random orientation model. Finally, we simplify the exact recovery condition (ERC) in Section 3.2.3.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Randomizing the nullspace", "weight": 1.0} -->

In definition (3.1), we fix the rotation ${\mathbf{U}}_{i} = \mathbf{I}$ in order to make the statement of the exact and stable recovery conditions symmetric. However, this symmetry is broken by the random orientation model because only ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ are taken at random. The next result restores this symmetry.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Exchanging stable for exact recovery", "weight": 1.0} -->

Our second simplification shows that the stability condition (SRC) holds with the same probability that the recovery condition (ERC) holds.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Polarizing the exact recovery condition", "weight": 1.0} -->

Our final simplification reduces the $n + 1$ intersections in (3.2) to a single intersection.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The approximate kinematic formula", "weight": 1.0} -->

The simplifications in Section 3.2 reduce the study of (ERC) and (SRC) to the question of computing the probability (3.4) that randomly oriented cones intersect. Remarkably, formulas for the probability that two randomly oriented cones share a ray appear in literature on stochastic geometry under the name *kinematic formulas*. While exact, these formulas involve geometric parameters that are typically difficult to compute.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The approximate kinematic formula", "weight": 1.0} -->

In recent work, the present authors and collaborators demonstrate that the classical kinematic formulas can be summarized using the statistical dimension \[, Thm. 7.1\]. The following result extends this formula to the intersection of an arbitrary number of randomly oriented cones.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Completing the proof", "weight": 1.0} -->

At this point, we have presented all of the components needed to complete the proof of Theorem A. Let us summarize the progress. Lemma 3.1 shows that (ERC) and (SRC) characterize exact and stable recovery. Under the random orientation model, the probability that the stable recovery condition (SRC) holds is equal to the probability that the exact recovery condition (ERC) holds (Lemma 3.3). We have also seen that

<!-- chunk {"id": "body-0051", "role": "body", "section": "Completing the proof", "weight": 1.0} -->

To complete the proof of Theorem A, we use the approximate kinematic formula of Theorem 3.5. ‣ 3.3 The approximate kinematic formula ‣ 3 Proof of the main result ‣ The achievable performance of convex demixing") to develop lower and upper bounds on the probability (3.9). This establishes the implications (1.10) and (1.11) when $D_{i} \neq {\{\mathbf{0}\}}$ for at least two indices $i$. We defer the degenerate case where $D_{i} = {\{\mathbf{0}\}}$ for all except (possibly) one index $i$ to Appendix D.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In this section, we describe two simple numerical experiments that demonstrate the accuracy of Theorem A. In our first example, we consider demixing three components, two of them sparse, the third a sign vector. Our second example considers demixing two sparse vectors with undersampling. Technical details about the experiments are collected in Appendix E.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sparse, sparse, and sign", "weight": 1.0} -->

In our first experiment, we fix the ambient dimension $d = 200$ and generate a mixed observation of the form

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sparse, sparse, and sign", "weight": 1.0} -->

The agreement between the $50\%$ empirical success curve and the theoretical yellow curve is remarkable. See Appendix E for further details.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Undersampled sparse and sparse", "weight": 1.0} -->

In our second experiment, we fix the ambient dimension $d = 200$ and consider demixing the observation

<!-- chunk {"id": "body-0056", "role": "body", "section": "Undersampled sparse and sparse", "weight": 1.0} -->

The results of this experiment with $m = {25,50,75}$ and $100$ appear in Figure 2 \[right\]. The colormaps indicate the empirical probability of success over $35$ trials as the sparsity of ${\mathbf{x}}_{1}^{\natural}$ and ${\mathbf{x}}_{2}^{\natural}$ varies. The yellow curve approximates the location where

<!-- chunk {"id": "body-0057", "role": "body", "section": "Undersampled sparse and sparse", "weight": 1.0} -->

Once again, this yellow curve agrees very well with the red $50\%$ empirical success contour.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions and open problems", "weight": 1.0} -->

This work unifies and resolves a number of theoretical questions regarding when it is possible to demix a superposition of incoherent signals. Under our random incoherence model, we find that demixing is possible if and only if the total number of measurements is greater than the total statistical dimension. While this result provides an intuitive and unifying theory for a large class of demixing problems, there are several important open problems that must be addressed before a complete "theory of demixing" emerges.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions and open problems", "weight": 1.0} -->

: Most of the prior work on demixing provides guarantees under explicit choices of the Lagrange parameter for (1.2), yet to the best of our knowledge, the only work that demonstrates sharp recovery bounds with specified Lagrange parameters occur for the LASSO problem, where $n = 1$ and $\left. f_{1} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$. Very recent work of Stojnic achieves comparable guarantees using a different approach.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions and open problems", "weight": 1.0} -->

Explicit choices of Lagrange parameters appear. These choices provide near-optimal empirical performance, but currently there is no proof that their choice of parameters reaches the phase transition that we identify. It would be very interesting to provide provably optimal choices of Lagrange parameters for demixing.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusions and open problems", "weight": 1.0} -->

: Our numerical experience indicates that the incoherence model considered in this work is predictive for highly incoherent situations. However, these results appear overly optimistic in more coherent situations. The difference between these situations appears, for example, in an application to calcium imaging \[, Fig. 3\]. Extending our results to other incoherence models will clarify where the phase transition in Theorem A predicts empirical performance, and where it does not.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions and open problems", "weight": 1.0} -->

: For practical applications of this work, we require accurate statistical dimension calculations. A recipe for these computations put forward has provable guarantees under some technical conditions (cf. \[, Sec. 4.4\] and \[, Prop. 1\]), but expressions for the statistical dimension of a number of important convex regularizers remains unknown. New statistical dimension computations immediately extend the reach of the methods used in this paper.
