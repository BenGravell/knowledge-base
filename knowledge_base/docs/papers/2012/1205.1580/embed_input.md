<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sharp Recovery Bounds for Convex Demixing, with Applications

Topics include Convex demixing, Signal separation, Conic geometry, Sparse recovery, Low-rank recovery, Random orientations, Statistical dimension.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes a broad convex demixing template for separating structured components from a superposition, using random orientation and incoherence assumptions to turn geometry into sharp phase-transition bounds. Its lasting contribution is the degrees-of-freedom accounting rule: demixing succeeds when the observation dimension exceeds the combined complexity of the constituent structures, with examples covering sparse-basis separation, error correction, and low-rank-plus-sparse decomposition.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Demixing refers to the challenge of identifying two structured signals given only the sum of the two signals and prior information about their structures. Examples include the problem of separating a signal that is sparse with respect to one basis from a signal that is sparse with respect to a second basis, and the problem of decomposing an observed matrix into a low-rank matrix plus a sparse matrix. This paper describes and analyzes a framework, based on convex optimization, for solving these demixing problems, and many others. This work introduces a randomized signal model which ensures that the two structures are incoherent, i.e., generically oriented. For an observation from this model, this approach identifies a summary statistic that reflects the complexity of a particular signal. The difficulty of separating two structured, incoherent signals depends only on the total complexity of the two structures. Some applications include (i) demixing two signals that are sparse in mutually incoherent bases; (ii) decoding spread-spectrum transmissions in the presence of impulsive errors; and (iii) removing sparse corruptions from a low-rank matrix. In each case, the theoretical analysis of the convex demixing method closely matches its empirical behavior.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In modern data-intensive science, it is common to observe a superposition of multiple information-bearing signals. *Demixing* refers to the challenge of separating out the constituent signals from the observation. A fundamental computational question is to understand when a tractable algorithm can successfully complete the demixing. Problems of this sort arise in fields as diverse as acoustics, astronomy, communications geophysics, image processing machine learning, and statistics. Some well-known examples of convex methods for demixing include morphological component analysis, robust principal component analysis and inpainting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work presents a general framework for demixing based on convex optimization. We study the geometry of the optimization problem, and we develop conditions that describe precisely when our method succeeds. Let us illustrate the major aspects of our approach through a concrete example.

<!-- chunk {"id": "body-0006", "role": "body", "section": "A first application: Morphological component analysis", "weight": 1.0} -->

Starck et al. use demixing to model the problem of distinguishing stars from galaxies in an astronomical image. This task requires hypotheses on the two types of objects. First, we must assume that stars and galaxies exhibit different kinds of structure: stars appear as localized bright points, while galaxies are wispy or filamented. Second, we must insist that the image is not so full of stars, nor of galaxies, that they obscure one another. These two properties are modeled by the notions of *incoherence* and *sparsity*. With these hypotheses, we can solve the demixing problem using a method known as morphological component analysis (MCA).

<!-- chunk {"id": "body-0007", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

The matrices $\mathbf{A}$ and $\mathbf{B}$ are known, while the vectors ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are unknown. Each column of $\mathbf{A}$ contains an elementary structure that might appear in the first signal; the columns of $\mathbf{B}$ reflect the structures in the second signal. The vector ${\mathbf{x}}_{0}$ selects the columns of $\mathbf{A}$ that appear in the first signal, e.g., stars in different locations, while ${\mathbf{y}}_{0}$ selects the columns of $\mathbf{B}$ that generate the second signal, e.g., galaxies in different locations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

*Incoherence* demands that the columns of $\mathbf{A}$ and $\mathbf{B}$ are weakly correlated, and *sparsity* requires that ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ have few nonzero elements.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

for a known orthogonal matrix $\mathbf{Q}$. The specialization to orthonormal bases is standard.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

Instead of restricting our attention to specific choices of $\mathbf{Q}$ that are incoherent with the identity matrix, we consider an idealized model for incoherence where $\mathbf{Q}$ is a uniformly random orthogonal matrix. This formulation ensures that the structures in the two signals are oriented generically with respect to each other. Other authors have also used this approach to study incoherence,.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

We quantify the sparsity of the two constituent signals by fixing parameters $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ in the interval $\lbrack 0,1\rbrack$ such that the unknown signals ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ satisfy

<!-- chunk {"id": "body-0012", "role": "body", "section": "The MCA signal model", "weight": 1.0} -->

where ${nnz}{({\mathbf{x}})}$ denotes the number of nonzero elements of $\mathbf{x}$.^‡‡^‡We prefer the notation ${nnz}{( \cdot )}$ over $\parallel \cdot \parallel_{\ell_{0}}$ because the number of nonzero elements in a vector is not a norm. In other words, $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ measure the proportion of nonzero entries in ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. These sparsity parameters emerge as the major factor that determines how hard it is to extract ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ from the observation ${\mathbf{z}}_{0}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The constrained MCA demixing procedure", "weight": 1.0} -->

The goal of morphological component analysis is to identify the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ of sparse vectors given the observation ${\mathbf{z}}_{0}$ and the matrix $\mathbf{Q}$. A natural technique for finding a sparse vector that satisfies certain conditions is to minimize the $\ell_{1}$ norm subject to these constraints, where the $\ell_{1}$ norm is defined as $\left. \parallel{\mathbf{x}}\parallel{}_{\ell_{1}}: = \sum_{i = 1}^{d}|x_{i}| \right.$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The constrained MCA demixing procedure", "weight": 1.0} -->

where the decision variables are ${{\mathbf{x}},{\mathbf{y}}} \in {\mathbb{R}}^{d}$. We call this optimization problem *constrained MCA*, and we say that it *succeeds* if $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is the unique optimal point of (1.1). Since (1.1) can be written as a linear program, constrained MCA offers a tractable procedure for attempting to identify the underlying components $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$, provided the observation ${\mathbf{z}}_{0}$, the orthogonal matrix $\mathbf{Q}$, and the side information $\alpha = {\|{\mathbf{y}}_{0}\|}_{\ell_{1}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The constrained MCA demixing procedure", "weight": 1.0} -->

Constrained MCA is closely related to the standard MCA procedure, which is a Lagrangian formulation of (1.1) that does not require the side information $\alpha$ \[71, Eq. \]. The constrained problem (1.1) is more powerful than the standard MCA procedure, so it provides hard limits on the effectiveness of the usual approach. In most cases, the two methods are equivalent, provided that we can choose the Lagrange multiplier correctly---a nontrivial task in itself. See Section 1.2.4 for more details.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Numerical and theoretical results for constrained MCA", "weight": 1.0} -->

This work establishes two theoretical results for constrained MCA. The first result provides a phase transition curve, parameterized by the sparsity $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$, for the probability that constrained MCA will demix a single pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0}$. This *weak bound* is marked by the green line in Figure 1. Observe that the green line coincides almost perfectly with the empirical phase transition.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Numerical and theoretical results for constrained MCA", "weight": 1.0} -->

Second, we establish a *strong bound*. For a fixed instantiation of the random orthogonal basis $\mathbf{Q}$, with high probability, constrained MCA (1.1) can identify *every* sufficiently sparse pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0}$. The blue curve in the bottom left corner of Figure 1 is a lower estimate for the sparsity pairs $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ where this uniform guarantee holds. Section 6.1 provides the details regarding the computation of the weak and strong bounds as well as a fully detailed description of our numerical experiment.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A recipe for demixing", "weight": 1.0} -->

This work is not primarily about MCA. We are interested in developing methods that apply to a whole spectrum of demixing problems. The following two sections describe how to construct a convex program that can separate two structured signals.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

The $\ell_{1}$ norm is a convex complexity measure that tends to be small near sparse vectors, so we can minimize the $\ell_{1}$ norm to promote sparsity. We now describe a method for building complexity measures that are appropriate for other types of structure. This construction was originally introduced in the nonlinear approximation literature,. The recent paper explains how to apply these ideas to solve signal processing problems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

In practice, we often encounter signals that are formed as a positive linear combination of a few elementary structures, called *atoms*, drawn from a fixed collection. For example, a sparse vector in ${\mathbb{R}}^{d}$ is a conic combination of a small number elements from the set $\{{{{\pm {\mathbf{e}}_{i}}:i = 1},{\ldots,d}}\}$ of signed standard basis vectors. We want to construct a function that reflects the complexity of an atomic signal.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

with the convention that ${f_{\mathcal{A}}{({\mathbf{x}})}} = {+ \infty}$ if the set is empty. Then $f_{\mathcal{A}}$ is a homogeneous convex function. The "unit ball" of $f_{\mathcal{A}}$ is $\overline{conv}{(\mathcal{A})}$, and the level sets of $f_{\mathcal{A}}$ are dilations of this unit ball. The atomic gauge $f_{\mathcal{A}}$ is a norm if and only if $\overline{conv}{(\mathcal{A})}$ is a bounded, symmetric set that contains zero in its interior.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

The convex hull of an atomic set $\mathcal{A}$ tends to have sharp corners at atoms; see Figure 2. At these sharp points, most perturbations of the objective increase the value of the gauge, so the atomic gauge tends to take small values at atoms. Similar behavior occurs at a signal comprised of a relatively small number of atoms. This observation is a key reason that atomic gauges make good complexity measures for atomic signals. Some common atomic gauges include

<!-- chunk {"id": "body-0023", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

*The Schatten 1-norm.* The Schatten 1-norm on ${\mathbb{R}}^{m \times n}$ is the sum of the singular values of a matrix. It is the atomic gauge generated by the set of rank-one matrices in ${\mathbb{R}}^{m \times n}$ with unit Frobenius norm. Minimizing the Schatten 1-norm promotes low rank,.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

*The operator norm.* The operator norm returns the maximum singular value of a matrix. On the space ${\mathbb{R}}^{n \times n}$ of square matrices, the operator norm is the atomic gauge generated by the set $\mathsf{O}_{n}$ of orthogonal matrices. This norm can be used to search for orthogonal matrices \[15, Prop. 3.13\]

<!-- chunk {"id": "body-0025", "role": "body", "section": "Structured signals and atomic gauges", "weight": 1.0} -->

Our applications focus on these four instances, but a dizzying variety other structure-promoting atomic gauges are available. For example, there are atomic gauges for vectors that are sparse in a dictionary (also known as analysis-sparsity) block- and group-sparse vectors and low-rank tensors and probability measures \[15, Sec. 2\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

Demixing is hopeless when the structures in the constituent signals are too strongly aligned. As an extreme example, suppose we observe ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {\mathbf{y}}_{0}}$, where both ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are sparse. There is clearly no principled way to assign the nonzero elements of ${\mathbf{z}}_{0}$ correctly to ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

In contrast, if we observe ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {\mathbf{H}{\mathbf{y}}_{0}}}$, where $\mathbf{H}$ is a normalized Walsh--Hadamard transform and both ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are sparse, then the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is typically identifiable. The latter situation is more favorable than the former because the Walsh--Hadamard matrix and the identity matrix are incoherent; that is, their columns are weakly correlated.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

In order to avoid restricting our attention to special cases, such as the Walsh--Hadamard matrix, we model incoherence by assuming that the basis $\mathbf{Q}$ is drawn randomly from the invariant Haar measure on the set of all orthogonal matrices $\mathsf{O}_{d}$. We call this the *random basis model.* This idealized approach to incoherence guarantees that the structures in the two constituent signals are generically oriented. This model has precedents in the literature on sparse approximation and it is analogous to the assumption of a measurement operator with a uniformly random nullspace that appears in the context of compressed sensing,.

<!-- chunk {"id": "body-0029", "role": "body", "section": "A generic model for incoherence", "weight": 1.0} -->

We expect that the random basis model also sheds light on other highly incoherent problems, such as the case where ${\mathbf{Q}} = \mathbf{H}$ is the Walsh--Hadamard transform or ${\mathbf{Q}} = \mathbf{D}$ is the discrete cosine transform (DCT). Some limited numerical simulations suggest that both the Walsh--Hadamard and the DCT matrices behave qualitatively similar to the random matrix $\mathbf{Q}$ in the examples considered in this work. This observation is in line with the universality of phase transitions that appear in $\ell_{1}$ minimization for many classes of measurement matrices. However, more coherent situations may exhibit different behavior, and thus they fall outside the purview of this work.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Formulating a convex demixing method", "weight": 1.0} -->

We are ready to introduce a computational framework for demixing structured signals. This approach unifies several related procedures that appear in the literature. See, for example.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Formulating a convex demixing method", "weight": 1.0} -->

where $\mathbf{Q}$ is a known orthogonal matrix and the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is unknown. We include the matrix $\mathbf{Q}$ in the formalism because it allows us to model incoherence using the random basis model described in Section 1.2.2 above. Our goal is to demix the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the observation ${\mathbf{z}}_{0}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Formulating a convex demixing method", "weight": 1.0} -->

Let $f$ and $g$ be convex complexity measures---such as atomic gauges---associated with the structures we expect to find in ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. Suppose we have access to the additional side information $\alpha = {g{({\mathbf{y}}_{0})}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Formulating a convex demixing method", "weight": 1.0} -->

where the decision variables are ${{\mathbf{x}},{\mathbf{y}}} \in {\mathbb{R}}^{d}$. The display (1.2) describes a convex program because $f$ and $g$ are convex functions. We say that the convex demixing method (1.2) *succeeds at demixing $(\mathbf{x}_{0},\mathbf{y}_{0})$*, or simply *succeeds*, if $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is the unique optimal point of (1.2); otherwise, it *fails*. In this work, we develop conditions that describe when the convex demixing method (1.2) succeeds and when it fails.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Lagrangian counterpart", "weight": 1.0} -->

In practice, the value $\alpha = {g{({\mathbf{y}}_{0})}}$ may not be known. In this case, we may replace the convex demixing method (1.2) with its Lagrangian relative

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Lagrangian counterpart", "weight": 1.0} -->

where $\lambda > 0$ is a regularization parameter that must be specified. The constrained problem (1.2) is slightly more powerful than (1.3), so its performance dominates the Lagrangian formulation (1.3). It is well known that (1.2) and (1.3) are essentially equivalent when the regularization parameter $\lambda$ is chosen correctly and a mild regularity condition holds; see Appendix A for details. Thus, we can interpret our results as delineating the *best possible performance* of the Lagrange problem (1.3).

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Lagrangian counterpart", "weight": 1.0} -->

This type of best-case analysis has precedents in the literature on sparse approximation, e.g. yet the identification of optimal Lagrange parameters for demixing remains a significant open problem. Several works prove that specific demixing procedures succeed for specific choices of Lagrange parameters under incoherence assumptions but these conservative guarantees fail to identify phase transitions. Since this document was submitted, some additional theoretical guidance choosing Lagrange parameters has appeared. Nevertheless, a comprehensive theory describing the optimal choices of Lagrange parameters for (1.3) does not currently exist.

<!-- chunk {"id": "body-0037", "role": "body", "section": "One hammer, many nails", "weight": 1.0} -->

The convex demixing method (1.2) includes many interesting special cases. Our analysis provides detailed information about when (1.2) is able to separate two structured, incoherent signals. We now describe some applications of this machinery.

<!-- chunk {"id": "body-0038", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

Suppose we wish to securely transmit a binary message across a communications channel. We can obtain strong guarantees of security by modulating the message with a random rotation before transmission,. Our theory shows that decoding the message via demixing also makes this secure scheme perfectly robust to sparse corruptions such as erasures or malicious interference.

<!-- chunk {"id": "body-0039", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

Consider the following simple communications protocol. We model the binary message as a sign vector ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$. Choose a random orthogonal matrix ${\mathbf{Q}} \in \mathsf{O}_{d}$. The transmitter sends the scrambled message ${\mathbf{s}}_{0} = {{\mathbf{Q}}{\mathbf{m}}_{0}}$ across the channel, where it is corrupted by an unknown sparse vector ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$. The receiver must determine the original message given only the corrupted signal

<!-- chunk {"id": "body-0040", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

and knowledge of the scrambling matrix $\mathbf{Q}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

This signal model is perfectly suited to the demixing recipe of Section 1.2. The discussion in Section 1.2.1 indicates that the $\ell_{1}$ and $\ell_{\infty}$ norms are natural complexity measures for the structured signals ${\mathbf{c}}_{0}$ and ${\mathbf{m}}_{0}$. Since the message ${\mathbf{m}}_{0}$ is a sign vector, we also have the side information $\left\| {\mathbf{m}}_{0} \right\|_{\ell_{\infty}} = 1$. Our receiver then recovers the message with the convex demixing method

<!-- chunk {"id": "body-0042", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

In Section 6.2, we apply the general theory developed in this work to study this communications protocol. Before summarizing the results of this analysis, we fix some notation. Suppose the corruption ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$ is $\tau$-sparse; that is, ${{nnz}{({\mathbf{c}}_{0})}} = {\lceil{\taud}\rceil}$ for some $\tau \in {\lbrack 0,1\rbrack}$. We further distinguish between two types of corruption. A *benign* corruption ${\mathbf{c}}_{0}$ is independent of the scrambling matrix $\mathbf{Q}$. In contrast, an *adversarial* corruption may depend on both $\mathbf{Q}$ and ${\mathbf{m}}_{0}$. Adversarial corruptions also include nonlinear effects that are not necessarily malicious.

<!-- chunk {"id": "body-0043", "role": "body", "section": "A secure communications protocol that is robust to sparse errors", "weight": 1.0} -->

In the benign case, our theory shows that there exists a phase transition in the success probability of the convex demixing method (1.4) at sparsity level $\tau \approx 0.19$. The empirical $50\%$ failure threshold for benign corruptions closely matches this prediction. In the adversarial case, our results guarantee that with high probability, our protocol will tolerate all corruptions that affect no more than $1.8\%$ of the components in the received message ${\mathbf{z}}_{0}$. This bound is conservative for the type of adversarial corruption in the numerical experiment; this is not surprising because we may not have constructed the worst possible corruption.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Low-rank matrix recovery with generic sparse corruptions", "weight": 1.0} -->

Consider now the *matrix* observation ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}} \in {\mathbb{R}}^{n \times n}$, where ${\mathbf{X}}_{0}$ has low rank, ${\mathbf{Y}}_{0}$ is sparse, and $\mathcal{Q}$ is a random rotation on ${\mathbb{R}}^{n \times n}$. This type of signal provides a highly stylized model for applications such as latent variable selection, and robust principal component analysis. In these settings, ${\mathbf{X}}_{0}$ has low rank because the underlying data is drawn from a low-dimensional linear model, while $\mathcal{Q}{({\mathbf{Y}}_{0})}$ represents a corruption.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Low-rank matrix recovery with generic sparse corruptions", "weight": 1.0} -->

(Note, however, that this stylized model is not equivalent to pre- and post-multiplying ${\mathbf{Y}}_{0}$ by independent random rotations of ${\mathbb{R}}^{n}$.) We aim to discover the matrix ${\mathbf{X}}_{0}$ given the corrupted observation ${\mathbf{Z}}_{0}$ and the rotation $\mathcal{Q}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Low-rank matrix recovery with generic sparse corruptions", "weight": 1.0} -->

We follow the now-familiar pattern of Section 1.2. The Schatten 1-norm $\left. \parallel \cdot \parallel{}_{S_{1}} \right.$ serves as a natural complexity measure for the low-rank structure of ${\mathbf{X}}_{0}$, and the matrix $\ell_{1}$ norm $\left. \parallel \cdot \parallel{}_{\ell_{1}} \right.$ is appropriate for the sparse structure of ${\mathbf{Y}}_{0}$. We further assume the side information $\alpha = \left\| {\mathbf{Y}}_{0} \right\|_{\ell_{1}}$. We then solve

<!-- chunk {"id": "body-0047", "role": "body", "section": "Low-rank matrix recovery with generic sparse corruptions", "weight": 1.0} -->

This convex demixing method succeeds if $({\mathbf{X}}_{0},{\mathbf{Y}}_{0})$ is the unique solution to (1.5).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Low-rank matrix recovery with generic sparse corruptions", "weight": 1.0} -->

The results of this work show that, with high probability, program (1.5) succeeds so long as the pair $(\rho,\tau)$ lies below the green curve on Figure 4. When the rank parameter $\rho$ is small, our theoretical bound closely tracks the phase transition visible in the numerical experiment, although the bound appears loose when $\rho$ is larger. Section 6.3 provides further details.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Matrix demixing mix-and-match", "weight": 1.0} -->

Our results are not restricted to the convex demixing methods (1.1), (1.4) or (1.5). Let us mention a few other situations we can analyze using the theory developed in this work. With a tractable convex program, it is possible to demix

<!-- chunk {"id": "body-0050", "role": "body", "section": "Matrix demixing mix-and-match", "weight": 1.0} -->

An orthogonal matrix from a matrix that is sparse in a random orthogonal basis,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Matrix demixing mix-and-match", "weight": 1.0} -->

A randomly oriented sign matrix from a sufficiently low-rank matrix, and

<!-- chunk {"id": "body-0052", "role": "body", "section": "Matrix demixing mix-and-match", "weight": 1.0} -->

A randomly rotated low-rank matrix from an orthogonal matrix.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Matrix demixing mix-and-match", "weight": 1.0} -->

See Section 6.4 for the details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

Our approach reveals a number of theoretical insights.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

Design of convex demixing methods for incoherent structures.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

: In the incoherent regime we analyze, the parameters that determine when the convex demixing method (1.2) succeeds reflect the structures in the constituent signals and the associated complexity measures. These summary parameters are independent of the relationship between the two incoherent structures. We discuss this fact and its consequences for the design of demixing procedures in Section 4.2.1.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

Connection with linear inverse problems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

: The parameters that determine success of the convex demixing method (1.2) are closely related to number of random linear measurements required to identify a structured signal. In Section 5.2, we leverage this relationship to compute these parameters from Gaussian width bounds developed.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Theoretical insights", "weight": 1.0} -->

: Our theory indicates that there is often a phase transition in the behavior of the demixing method (1.2). See Section 4.2.2 for a discussion of this point.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Outline", "weight": 1.0} -->

This work begins with demixing in the deterministic setting. Section 2 describes the geometry of the convex demixing method (1.2) and provides a geometric characterization of successful demixing.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Outline", "weight": 1.0} -->

Section 3 presents a random model for incoherence along with some techniques from spherical integral geometry that allow us to analyze this model. In Section 4, these ideas yield theory that predicts success and failure regimes for the convex demixing method (1.2). Section 5 develops methods for computing the parameters necessary to apply the theorems of Section 4.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Outline", "weight": 1.0} -->

In Section 6, we analyze the application problems described in Sections 1.1 and 1.3. Section 7 concludes with a discussion of this work's place in the literature and future directions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The geometry of demixing", "weight": 1.0} -->

This short section lays the geometric foundation for the rest of this work. Section 2.1 describes the local behavior of convex functions in terms of special convex cones. In Section 2.2, this geometric view yields a concise characterization of successful demixing in terms of the configuration of two cones. The results in this section are deterministic, that is, they hold for any fixed basis $\mathbf{Q}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Feasible cones", "weight": 1.0} -->

The success of the convex demixing method (1.2) depends on the properties of the complexity measures $f$ and $g$ at the structured vectors ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. The following definition captures the local behavior of a convex function.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example 2.2 (The feasible cone of the $\\ell_{\\infty}$ norm at sign vectors)", "weight": 1.0} -->

The feasible cone is always a convex cone containing zero, but it is not necessarily closed. If $\mathcal{A}$ is a set of atoms and ${\mathbf{a}} \in \mathcal{A}$, the feasible cone $\mathcal{F}{(f_{\mathcal{A}},{\mathbf{a}})}$ of the atomic gauge $f_{\mathcal{A}}$ at the atom $\mathbf{a}$ tends to be small because the unit ball of $f_{\mathcal{A}}$ is the smallest convex set containing all of the atoms. See Figure 2 for an illustration. The positive homogeneity of atomic gauges further implies that the feasible cones of atomic gauges do not depend on the scaling of a vector, in the sense that

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

Definition 2.1. ‣ 2.1 Feasible cones ‣ 2 The geometry of demixing ‣ Sharp recovery bounds for convex demixing, with applications") is equivalent to the definition of the "tangent cone" appearing in \[15, Eq. \]. However, that definition differs slightly from the standard definition of a tangent cone; cf., \[66, Thm. 6.9\]. The cone of feasible directions \[62, p. 33\] is the closest relative of the feasible cone that we have identified in the literature, and this is the source of our terminology.

<!-- chunk {"id": "body-0067", "role": "body", "section": "A geometric characterization of optimality", "weight": 1.0} -->

The following lemma provides a geometric characterization for success in the convex demixing method (1.2) in terms of the configuration of two feasible cones. This is the main result of this section.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Spherical intrinsic volumes", "weight": 1.0} -->

We begin our introduction to integral geometry with fundamental geometric parameters known as spherical intrinsic volumes. Spherical intrinsic volumes quantify geometric properties of convex cones such as the fraction of space a cone consumes (a type of volume), the fraction of space taken by the corresponding dual cone, and quantities akin to surface area. The following characterization \[3, Proposition 4.4.6\] is convenient.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.4 (Extension to nonpolyhedral cones)", "weight": 1.0} -->

The definition of spherical intrinsic volumes extends to all closed convex cones by approximation with polyhedral cones, but note that the probabilistic characterization above *does not hold* for nonpolyhedral cones. The technical details involve continuity properties of the spherical intrinsic volumes under the spherical Hausdorff metric. This theory is developed,. See \[69, Ch. 6.5\] for a self-contained overview of spherical integral geometry developed via polyhedral approximation, or see \[3, Sec. 4\] for a development using tools from differential geometry.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Key facts from integral geometry", "weight": 1.0} -->

We now collect some of the properties of spherical intrinsic volumes that are required for our development. We start with some elementary facts.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Fact 3.5", "weight": 1.0} -->

Let $K \subset {\mathbb{R}}^{d}$ be a closed convex cone. Then

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fact 3.6 (Spherical kinematic formula \\[69, p. 261\\])", "weight": 1.0} -->

Let $K$ and $\overset{\sim}{K}$ be closed convex cones in ${\mathbb{R}}^{d}$, at least one of which is not a subspace, and let $\mathbf{Q}$ be a random basis. Then

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

Fact 3.6. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") is usually stated for random rotations drawn according to the Haar measure on the special orthogonal group ${\mathsf{S}\mathsf{O}}_{d}$, but the unitary invariance given by Fact 3.5.3 readily implies that the spherical kinematic formula holds for $\mathbf{Q}$ drawn from the Haar measure on the orthogonal group $\mathsf{O}_{d}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

The spherical Gauss--Bonnet formula (Fact B.2. ‣ B.1 Regions of failure: The proof of Theorem 4.3 ‣ Appendix B Regions of failure and uniform guarantees ‣ Sharp recovery bounds for convex demixing, with applications") in Appendix B.1) can be used to eliminate the apparent asymmetry between $K$ and $\overset{\sim}{K}$ in (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")). In particular, the identity

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

holds for any convex cones $K$ and $\overset{\sim}{K}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "High-dimensional decay of spherical intrinsic volumes", "weight": 1.0} -->

The spherical kinematic formula (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")), coupled with the geometric optimality conditions of Lemma 2.4, provides an exact expression for the probability that the demixing problem (1.2) succeeds. Nevertheless, the formula involves the spherical intrinsic volumes of two cones, and it is challenging to determine these quantities directly from the definition except in simple situations.

<!-- chunk {"id": "body-0077", "role": "body", "section": "High-dimensional decay of spherical intrinsic volumes", "weight": 1.0} -->

To confront this challenge, we seek summary statistics for the intrinsic volumes as the dimension $d\rightarrow\infty$. We motivate our approach with the orthant. In Figure 7, we see that the spherical intrinsic volumes of the orthant $v_{i}{({\mathbb{R}}_{+}^{d})}$ decay rapidly as $d\rightarrow\infty$ when the index $i$ falls outside of the region $i \approx {d/2}$. The intrinsic volumes with indices $i$ far away from $d/2$ will contribute very little to the sum (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")) appearing in the kinematic formula. This observation simplifies the application of the kinematic formula when one of the cones is congruent to the orthant.

<!-- chunk {"id": "body-0078", "role": "body", "section": "High-dimensional decay of spherical intrinsic volumes", "weight": 1.0} -->

In general, we might hope that for some sequence of cones $K^{(d)} \in {\mathbb{R}}^{d}$, the spherical intrinsic volumes $v_{i}{(K^{(d)})}$ decay rapidly as $d\rightarrow\infty$ for indices $i$ outside of some interval $\lbrack{\kappa_{\star}d},{\theta_{\star}d}\rbrack$. We codify this behavior with *decay thresholds* that indicate which intrinsic volumes are very small as the ambient dimension $d$ grows.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 3.10 (Nonuniqueness of decay thresholds)", "weight": 1.0} -->

The upper decay threshold $\theta_{\star}$ for an ensemble $\{ K^{(d)}\}$ defined above is not unique since any $\theta^{\prime} > \theta_{\star}$ is also a decay threshold for $\{ K^{(d)}\}$. An analogous comment holds for the lower decay threshold.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Examples of decay thresholds", "weight": 1.0} -->

Since the intrinsic volumes are positive and sum to one (Fact 3.5), not every intrinsic volume is exponentially small in the ambient dimension $d$. In particular, the inequality $\kappa_{\star} \leq \theta_{\star}$ between lower and upper decay thresholds always holds. In practice, however, we can often find decay thresholds that satisfy the equality $\kappa_{\star} = \theta_{\star}$, as the following examples demonstrate.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Success and failure", "weight": 1.0} -->

This section synthesizes the material from Sections 2 and 3 to determine whether the convex demixing method (1.2) succeeds, or fails, with high probability. Section 4.1 introduces the concept of a demixing ensemble. Our main results arrive in Section 4.2, where we find that the success and failure of the convex demixing method (1.2) are characterized by decay thresholds. Section 4.3 extends our methods to achieve uniform guarantees on the success of method (1.2).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Ensembles of demixing problems", "weight": 1.0} -->

A demixing ensemble is a collection of demixing problems that is indexed by the ambient dimension of the observation. We explain this idea in the context of MCA, and we develop the abstract definition in Section 4.1.2.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example: The MCA demixing ensemble", "weight": 1.0} -->

Recall from Section 1.1 that MCA seeks to demix a superposition of two sparse vectors. Let us fix sparsity levels $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ in $\lbrack 0,1\rbrack$. For each pair $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$, we construct an ensemble of demixing problems with one problem per dimension. For each $d \in {\mathbb{N}}$, let ${\mathbf{x}}_{0}^{(d)}$ and ${\mathbf{y}}_{0}^{(d)}$ be vectors in ${\mathbb{R}}^{d}$ with

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example: The MCA demixing ensemble", "weight": 1.0} -->

Together, these data define a demixing ensemble for MCA. We want to study when the MCA problem (1.2) succeeds with high probability for all members of the ensemble with $d$ sufficiently large.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Abstract demixing ensembles", "weight": 1.5} -->

It is straightforward to extend this idea to other demixing problems. Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices. A *demixing ensemble* consists of one problem per index. For each $d \in \mathcal{D}$, the data are

<!-- chunk {"id": "body-0086", "role": "body", "section": "Abstract demixing ensembles", "weight": 1.5} -->

A random basis ${\mathbf{Q}}^{(d)} \in \mathsf{O}_{d}$ that is statistically independent of the other ensemble data,

<!-- chunk {"id": "body-0087", "role": "body", "section": "Abstract demixing ensembles", "weight": 1.5} -->

Given such a demixing ensemble, we seek to determine conditions for which the convex demixing method

<!-- chunk {"id": "body-0088", "role": "body", "section": "Abstract demixing ensembles", "weight": 1.5} -->

succeeds with high probability when the dimension $d$ is large. When it does not cause confusion, we omit the superscript $d$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Abstract demixing ensembles", "weight": 1.5} -->

Our goal in this paper is to describe regions where the demixing program (4.1) succeeds, or fails, with high probability as the dimension $d\rightarrow\infty$. In order to avoid cumbersome repetition in our theorems, we make a shorthand definition.

<!-- chunk {"id": "body-0090", "role": "body", "section": "The main results", "weight": 1.0} -->

We are now in a position to state our main results. The first result shows that the upper decay threshold provides guarantees for the success of demixing under the model of Section 4.1.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Consequences for the choice of complexity functions", "weight": 1.0} -->

The complementary nature of Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") has striking implications. The success, or failure, of the convex demixing method (4.1) in high dimensions depends only on the sum of the decay thresholds. As a consequence, the upper and lower decay thresholds assess the quality of the complexity measures $f^{(d)}$ and $g^{(d)}$ in high dimensions.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Consequences for the choice of complexity functions", "weight": 1.0} -->

Since the decay thresholds are independent of any interrelationship between the structured vectors ${\mathbf{x}}_{0}^{(d)}$ and ${\mathbf{y}}_{0}^{(d)}$ in the superimposed observation ${\mathbf{z}}_{0}^{(d)}$, the quality of the complexity measure $f^{(d)}$ is independent of the choice $g^{(d)}$. This explains, for instance, the ubiquity of the use of the $\ell_{1}$ norm for inducing sparsity and the Schatten 1-norm as a complexity measure for rank. Simply put, when a complexity measure is good for one incoherent demixing problem, it is good for another.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Sharp phase transitions", "weight": 1.0} -->

Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") have an important consequence for phase transitions in the convex demixing method (4.1). Equality between the lower and upper decay thresholds holds in cases where we have access to exact formulas for the spherical intrinsic volumes. Proposition 3.11. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") shows that the upper and lower decay thresholds are equal for subspaces whose dimension is proportional to the ambient space, and Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") implies that the upper decay threshold is equal to the lower decay threshold for the ensemble of nonnegative orthants.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Sharp phase transitions", "weight": 1.0} -->

Moreover, our computations in Appendix C suggest that equality between the upper and lower decay thresholds also holds for the ensemble of feasible cones of the $\ell_{1}$ norm at vectors with a fixed proportion of nonzero elements.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Sharp phase transitions", "weight": 1.0} -->

The equality of the upper and lower decay thresholds explains the close agreement between our theoretical bounds and the empirical experiments. For instance, consider Figure 1. For sparsity levels below the green curve, the sum of the upper decay thresholds is less than one, so Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that demixing succeeds with overwhelming probability in high dimensions. On the other hand, with sparsity levels above the green curve, the sum of the lower decay thresholds exceeds one, so demixing fails with overwhelming probability in high dimensions by Theorem 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"). (See Section 6.1 for the details of this calculation.)

<!-- chunk {"id": "body-0096", "role": "body", "section": "Sharp phase transitions", "weight": 1.0} -->

One may wonder whether the transition between success and failure is sharp in general. In work undertaken after the submission of this article, with collaborators, we have determined that the answer to this question is *yes* for a large class of demixing ensembles. In essence, the result \[5, Thm. 6.1\] indicates that the upper- and lower-decay thresholds for a sufficiently regular ensemble $\{{K^{(d)}:d \in \mathcal{D}}\}$ are equal.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Sharp phase transitions", "weight": 1.0} -->

For example, the fact that ${d^{- 1}W{({K^{(d)} \cap \mathsf{S}^{d - 1}})}^{2}}\rightarrow\rho \in {}$ as $d\rightarrow\infty$ is sufficient to guarantee that the upper- and lower-decay thresholds $\theta_{\star}$ and $\kappa_{\star}$ of the ensemble $\{{K^{(d)}:d \in \mathcal{D}}\}$ satisfy $\theta_{\star} = \kappa_{\star} = \rho$. (The function $W$ is the Gaussian width defined in Section 5.2.1.) We refer the reader to this newer work for details.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

In fact, the probability that randomly oriented convex cones strike is *equal* to the probability that their closures strike. This seemingly innocuous claim appears to have no simple proof from first principles. However, this fact readily follows from the discussion of touching probabilities in \[69, pp. 258--259\].

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 4.6 (Explicit dimensional dependence)", "weight": 1.0} -->

The methods above can provide explicit dependence between the sum of the decay thresholds $\theta_{x} + \theta_{y}$, the "sufficiently large" dimension and the probability decay rate $\varepsilon$ when detailed information about the intrinsic volumes is available. In the case of the orthant, for example, Stirling's formula with remainder \[59, Sec. 5.6.1\] may provide enough information. For the descent cones of the $\ell_{1}$ norm, it may be possible to achieve such explicit dependence using the approach of.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Uniform demixing guarantees", "weight": 1.0} -->

Suppose that $\mathbf{Q}$ is drawn at random and fixed. For example, in the MCA problem from Section 1.1, we may observe a number of different images, but the structures that we expect to find (encoded by $\mathbf{Q}$) are the same in each image. In this case, we ask whether (1.1) demix *every* sparse pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$, and thus successfully identify the structures in a large family of images.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Uniform demixing guarantees", "weight": 1.0} -->

More generally, we can study the probability that the generic demixing program (1.2) will demix every structured pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ with a random---but fixed---basis $\mathbf{Q}$. (These uniform guarantees go by the name of *strong bounds*.) By the geometric optimality condition of Lemma 2.4, this probability is equal to the probability of the event

<!-- chunk {"id": "body-0102", "role": "body", "section": "Uniform demixing guarantees", "weight": 1.0} -->

In this section, we control the probability of (4.4) by coupling the argument leading to Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") with a union bound. This approach does not necessarily limit our methods to a finite number of structured pairs $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$, however. In the case of a sparse vectors, for example, the set of feasible cones

<!-- chunk {"id": "body-0103", "role": "body", "section": "Uniform demixing guarantees", "weight": 1.0} -->

consists of $\binom{d}{k}2^{k}$ cones because the feasible cone $\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{x}}) \right.$ depends only on the sparsity and sign pattern, and not the magnitude, of the elements of $\mathbf{x}$. (See Section 6.1.1 for more details.) Thus, even the simple union bound can offer insight into the behavior of constrained MCA (1.1) for an *infinite* family of images.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Uniform demixing guarantees", "weight": 1.0} -->

Applying a union bound to a finite, but rather large, set of cones such as (4.5) requires stronger probabilistic information than provided by the decay thresholds. Therefore, we define an extension of the upper decay threshold that provides detailed information on the rate of decay of spherical intrinsic volumes.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Computing decay thresholds", "weight": 1.0} -->

Section 4.2 demonstrates that the decay thresholds provide a simple way to analyze demixing under the random basis model. This section describes several methods for computing decay thresholds. We begin by considering direct approaches, where precise formulas for the spherical intrinsic volumes give correspondingly precise thresholds.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Computing decay thresholds", "weight": 1.0} -->

The direct method is powerful, but its application is limited to regimes where we have access to formulas for spherical intrinsic volumes. In Section 5.2, we observe that known results on linear inverse problems imply bounds on decay thresholds. This observation allows us to study upper decay thresholds for several structural classes, including low-rank matrices.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Direct approach", "weight": 1.0} -->

There are several situations where the direct approach for calculating decay thresholds is feasible. Propositions 3.11. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") and 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") compute upper and lower decay thresholds for ensembles of subspaces and orthants directly from the definition of spherical intrinsic volumes. In Appendix C, we use the asymptotic polytope angle computations of to compute the decay threshold for ensembles of feasible cones of the $\ell_{1}$ norm at sparse vectors. The approach follows roughly the same lines as Propositions 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") and 4.9.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Direct approach", "weight": 1.0} -->

‣ 4.3 Uniform demixing guarantees ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), but the argument requires a good deal of background information that is tangential to this work.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

There is a useful link between the number of random linear measurements required to identify a structured signal with a convex complexity measure and the upper decay threshold of the associated feasible cone. Roughly speaking, the upper decay threshold is the ratio between the number of linear measurements required to identify a structured signal and the ambient dimension. This observation provides a powerful method for determining decay thresholds.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

Linear inverse problems are closely related to demixing problems. Suppose we observe the linear image ${\mathbf{z}}_{0} = {{\mathbf{A}}{\mathbf{x}}_{0}}$, where $\mathbf{A}$ is a known matrix and ${\mathbf{x}}_{0}$ is a structured vector. Given an associated convex complexity measure $f$, Chandrasekaran et al. study the convex optimization program

<!-- chunk {"id": "body-0111", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

These authors consider the question "Given the data ${\mathbf{z}}_{0} = {{\mathbf{A}}{\mathbf{x}}_{0}}$, when is ${\mathbf{x}}_{0}$ the unique optimal point of (5.1)?" The answer to this question is closely related to our demixing problem.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

To place the linear inverse problem in our asymptotic framework, we consider an ensemble of problems indexed by the ambient dimension $d$. Fix an undersampling parameter $\sigma \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

We attempt to identify ${\mathbf{x}}_{0}^{(d)}$ by solving the optimization problem

<!-- chunk {"id": "body-0114", "role": "body", "section": "Relationship to linear inverse problems", "weight": 1.0} -->

with decision variable ${\mathbf{x}} \in {\mathbb{R}}^{d}$. This method succeeds when ${\mathbf{x}}_{0}^{(d)}$ is the unique optimal point of (5.2). The following result shows that the problem of computing the number of random linear measurements needed to identify a structured vector is equivalent to determining an upper decay threshold.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

A counterpart to Lemma 5.1 that links the failure of linear inverse problems to the lower decay threshold $\kappa_{\star}$ is readily derivable with the techniques used in this work. This may enable the computation of lower decay thresholds through information-theoretic arguments.

<!-- chunk {"id": "body-0116", "role": "body", "section": "The upper decay threshold from the Gaussian width", "weight": 1.0} -->

Lemma 5.1 provides a powerful tool for computing upper decay thresholds. Define the *Gaussian width* of a cone $K \subset {\mathbb{R}}^{d}$ by the expression

<!-- chunk {"id": "body-0117", "role": "body", "section": "The upper decay threshold from the Gaussian width", "weight": 1.0} -->

where the random vector $\mathbf{ω}$ is drawn from the Gaussian distribution on ${\mathbb{R}}^{d}$. The following corollary lets us determine upper decay thresholds from Gaussian width bounds. As usual, $\mathcal{D}$ is an infinite subset of the natural numbers.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Remark 5.5", "weight": 1.0} -->

An asymptotically sharp upper bound for the Gaussian width in (5.4) is given by the solution to an implicit equation in \[60, Eq. \]. We use this asymptotically precise formula for computing the location of the green curve in Figure 4. See Section 6.3 for more details.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Experiments", "weight": 1.0} -->

We can tackle a variety of scenarios using the theory developed in Section 4 and the decay threshold calculations of Section 5.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Morphological component analysis", "weight": 1.0} -->

We return to the MCA model of Section 1.1. Our goal is to analyze when we can demix two signals that are sparse in incoherent bases. To apply our theoretical results, we consider the demixing ensemble from Section 4.1.1.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Morphological component analysis", "weight": 1.0} -->

The $\ell_{1}$ norm is a natural complexity measure for sparse vectors. Given the side information $\alpha = \left\| {\mathbf{y}}_{0} \right\|_{\ell_{1}}$, we pose the constrained MCA problem

<!-- chunk {"id": "body-0122", "role": "body", "section": "Morphological component analysis", "weight": 1.0} -->

Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that our demixing method (6.1) for sparse vectors succeeds with overwhelming probability in high dimensions so long as ${{\theta_{\ell_{1}}{(\tau_{\mathbf{x}})}} + {\theta_{\ell_{1}}{(\tau_{\mathbf{y}})}}} < 1$. The right panel of Figure 11 shows the level sets of the function ${\theta_{\ell_{1}}{(\tau_{\mathbf{x}})}} + {\theta_{\ell_{1}}{(\tau_{\mathbf{y}})}}$ for $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ on the unit square ${\lbrack 0,1\rbrack}^{2}$. The green curve is the level set

<!-- chunk {"id": "body-0123", "role": "body", "section": "Morphological component analysis", "weight": 1.0} -->

Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that program (6.1) succeeds with overwhelming probability when the joint sparsity $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ lies below the green curve.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Morphological component analysis", "weight": 1.0} -->

On the other hand, our computations show that the upper decay threshold $\theta_{\ell_{1}}{(\tau)}$ is numerically equal to the lower decay threshold $\kappa_{\ell_{1}}{(\tau)}$---see the discussion in Appendix C.2. Theorem 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that the sparse demixing method (6.1) fails with overwhelming probability for sparsity levels $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ in the region above the green curve. In other words, the green curve on the right panel of Figure 11 delineates a sharp transition between success and failure for constrained MCA (6.1). The green curve in Figure 11(b) is the same as the green curve in Figure 1.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

The theory of Section 4.3 allows us to provide a uniform recovery guarantee. For a fixed draw of the random basis, constrained MCA can demix all sufficiently sparse pairs of vectors with overwhelming probability in high dimensions.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

holds. Theorem 4.11 guarantees that the probability of event (6.2) is large when some associated decay thresholds are small enough; let us describe how to verify the required technical assumptions.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

First, the results in Appendix C allow us to compute upper decay threshold at levels $\psi \geq 0$ for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{w}}^{(d)}) \right.\}$ from Section 6.1 consisting of feasible cones for the $\ell_{1}$ norm at $\tau$-sparse vectors. We extend our earlier notation by writing this quantity as $\theta_{\ell_{1}}{(\tau,\psi)}$. This is the first element required to check the hypotheses of Theorem 4.11.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

We also require information on the total number of feasible cones under consideration. Let

<!-- chunk {"id": "body-0129", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

where the unions take place over all $\lceil{\tau_{\mathbf{x}}d}\rceil$-sparse ${\mathbf{x}}_{0} \in {\mathbb{R}}^{d}$ and all $\lceil{\tau_{\mathbf{y}}d}\rceil$-sparse ${\mathbf{y}}_{0} \in {\mathbb{R}}^{d}$. There are exactly $2^{k}\binom{d}{k}$ different---but congruent---feasible cones of the $\ell_{1}$ norm at vectors in ${\mathbb{R}}^{d}$ with $k$ nonzero entries, one for each sign/sparsity pattern. This corresponds to the number of $({k - 1})$-dimensional faces of the crosspolytope; see, e.g., \[25, Sec. 3.3\].

<!-- chunk {"id": "body-0130", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

With $k = {\lceil{\taud}\rceil}$, it follows from the proof of Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") that

<!-- chunk {"id": "body-0131", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

uniformly as $d\rightarrow\infty$. By continuity of the exponential, for every $\eta > 0$ and all sufficiently large $d$, the number of feasible cones is bounded above by

<!-- chunk {"id": "body-0132", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

We have now collected enough information to apply our theory. By Theorem 4.11, the event (6.2) holds with overwhelming probability in high dimensions so long as

<!-- chunk {"id": "body-0133", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

The blue curve appearing in Figure 1 on page 1 shows the level set

<!-- chunk {"id": "body-0134", "role": "body", "section": "Strong guarantees", "weight": 1.0} -->

When the sparsity level $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ lies below the blue curve, inequality (6.4) holds, so that the demixing method (6.1) succeeds at demixing *every* pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ of $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$-sparse vectors with overwhelming probability in high dimensions.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Numerical experiment for constrained MCA", "weight": 1.0} -->

The following numerical experiment illustrates the accuracy of these theoretical results. We fix the dimension $d = 100$. For each pair ${(k_{\mathbf{x}},k_{\mathbf{y}})} \in {\{ 0,1,\ldots,100\}}^{2}$, we repeat the following procedure $25$ times.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Numerical experiment for constrained MCA", "weight": 1.0} -->

Draw ${{\mathbf{x}}_{0},{\mathbf{y}}_{0}} \in {\mathbb{R}}^{d}$ with $k_{\mathbf{x}}$ or $k_{\mathbf{y}}$ nonzero elements, respectively. The locations of the nonzero elements are chosen at random, and these elements are equally likely to be $+ 1$ or $- 1$.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Numerical experiment for constrained MCA", "weight": 1.0} -->

Generate a random basis ${\mathbf{Q}} \in \mathsf{O}_{d}$; see Remark 6.1 below.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Numerical experiment for constrained MCA", "weight": 1.0} -->

Solve (6.1) for the optimal point $({\mathbf{x}}_{\star},{\mathbf{y}}_{\star})$ with the numerical optimization software CVX,.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Numerical experiment for constrained MCA", "weight": 1.0} -->

The background of Figure 1 shows the results of this experiment as a function of $\tau_{\mathbf{x}} = {k_{\mathbf{x}}/d}$ and $\tau_{\mathbf{y}} = {k_{\mathbf{y}}/d}$. The yellow curve marks the empirical $50\%$ success line, and we note that it tracks the green theoretical curve closely. It emerges that $d = 100$ is already large enough to see the high dimensional behavior described by our theoretical results.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Remark 6.1", "weight": 1.0} -->

A random basis in ${\mathbf{Q}} \in \mathsf{O}_{d}$ is often defined through a conceptually simple two-step operation. First, draw a square $d \times d$ Gaussian matrix; second, orthogonalize the columns of this matrix via the Gram--Schmidt procedure. Although this definition has the flavor of a numerical algorithm, the conceptual process is not numerically stable. Moreover, standard procedures for stabilizing the orthogonalization do not preserve the Haar measure. For a straightforward, numerically stable approach to generating random bases, see.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Secure and robust channel coding", "weight": 1.0} -->

Next, we study the secure channel coding scheme of Section 1.3.1. We want to analyze when the receiver can decode a transmitted message that is subject to a sparse corruption. The difficulty depends on the sparsity level $\tau$ of the corruption, where $\tau \in {\lbrack 0,1\rbrack}$. Let us introduce an ensemble of demixing problems. In each dimension $d \in {\mathbb{N}}$, choose a $d$-bit message ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$ and a corruption ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$ with ${{nnz}{({\mathbf{c}}_{0})}} = {\lceil{\taud}\rceil}$. Draw a random basis $\mathbf{Q}$ known to both the receiver and transmitter.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Secure and robust channel coding", "weight": 1.0} -->

The natural complexity measure for the sparse corruption ${\mathbf{c}}_{0}$ is the $\ell_{1}$ norm, while the $\ell_{\infty}$ norm is the appropriate complexity measure for the sign vector ${\mathbf{m}}_{0}$. Note that $\left\| {\mathbf{m}}_{0} \right\|_{\ell_{\infty}} = 1$. To recover the original message, the receiver solves the problem

<!-- chunk {"id": "body-0143", "role": "body", "section": "Secure and robust channel coding", "weight": 1.0} -->

This approach succeeds when $({\mathbf{m}}_{0},{\mathbf{c}}_{0})$ is the unique optimal point of (6.5).

<!-- chunk {"id": "body-0144", "role": "body", "section": "Secure and robust channel coding", "weight": 1.0} -->

We consider two types of corruptions. *Benign* corruptions are taken in any manner that is independent of $\mathbf{Q}$---this would happen, for instance, when the corruption is generated by an adversary with no knowledge of $\mathbf{Q}$ or the transmission ${\mathbf{Q}}{\mathbf{m}}_{0}$. *Adversarial* corruptions are worst-case sparse corruptions; these corruptions may model malicious interference or an erasure channel that sets some of the coordinates of ${\mathbf{z}}_{0}$ to zero. We first consider with the benign corruption, and then consider the adversarial case in Section 6.2.2.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Benign corruptions", "weight": 1.0} -->

Since the corruption is chosen independently of the basis $\mathbf{Q}$, the convex demixing method (6.5) succeeds if it can identify the single pair $({\mathbf{c}}_{0},{\mathbf{m}}_{0})$. Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") describe where procedure succeeds, or fails, with overwhelming probability in high dimensions, but we must first determine some decay thresholds.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Benign corruptions", "weight": 1.0} -->

The feasible cone of the $\ell_{\infty}$ norm at a sign vector is congruent to an orthant (Example 2.2. ‣ 2.1 Feasible cones ‣ 2 The geometry of demixing ‣ Sharp recovery bounds for convex demixing, with applications")). From Table 1, we see that the sequence $\{{{\mathbb{R}}_{+}^{d}:d \in {\mathbb{N}}}\}$ of orthants has an upper decay threshold of $\theta_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$ and a matching lower decay threshold $\kappa_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$. Appendix C defines an upper decay threshold $\theta_{\ell_{1}}{(\tau)}$ for the sequence of feasible cones of the $\ell_{1}$ norm at $\tau$-sparse vectors.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Benign corruptions", "weight": 1.0} -->

With these thresholds in hand, Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") guarantees that (6.5) succeeds with overwhelming probability in high dimensions provided that ${\theta_{{\mathbb{R}}_{+}^{d}} + {\theta_{\ell_{1}}{(\tau)}}} < 1$, or, equivalently, provided that ${{\theta_{\ell_{1}}{(\tau)}} < \frac{1}{2}}.$ On the other hand, Theorem 4.3.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Benign corruptions", "weight": 1.0} -->

‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") shows that (6.5) fails with overwhelming probability in high dimensions if the corresponding upper decay threshold satisfies ${{{\kappa_{\ell_{1}}{(\tau)}} + \kappa_{{\mathbb{R}}_{+}^{d}}} > 1}.$ This condition holds when ${\kappa_{\ell_{1}}{(\tau)}} > \frac{1}{2}$.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Benign corruptions", "weight": 1.0} -->

Numerically, we find that ${\theta_{\ell_{1}}{(\tau)}} < \frac{1}{2}$ when the sparsity level $\tau \lesssim 0.193$; see the left panel of Figure 11. The fact that ${\kappa_{\ell_{1}}{(\tau)}} = {\theta_{\ell_{1}}{(\tau)}}$ to numerical precision implies that ${\kappa_{\ell_{1}}{(\tau)}} > \frac{1}{2}$ for $\tau \gtrsim 0.193$. In other words, if fewer than $19\%$ of the entries of ${\mathbf{c}}_{0}$ are nonzero, the scheme (6.5) succeeds with overwhelming probability in high dimensions; otherwise, it fails with overwhelming probability in high dimensions. This sharp transition corresponds to the location of the dashed line in Figure 3.

<!-- chunk {"id": "body-0150", "role": "body", "section": "The adversarial case", "weight": 1.0} -->

In the adversarial case, the corruptions are sparse but may depend on the basis $\mathbf{Q}$ and the message ${\mathbf{m}}_{0}$. To ensure that no corruption with $\lceil{\taud}\rceil$ nonzero entries can cause (6.5) to fail, we must verify that (6.5) succeeds at identifying $({\mathbf{c}}_{0},{\mathbf{m}}_{0})$ for *every* $\lceil{\taud}\rceil$-sparse vector ${\mathbf{c}}_{0}$. From Lemma 2.4, this is equivalent to the event

<!-- chunk {"id": "body-0151", "role": "body", "section": "The adversarial case", "weight": 1.0} -->

We can use Theorem 4.11 to verify that event (6.6) holds with overwhelming probability in high dimensions. Let us collect the additional information required to verify the technical assumptions of this theorem.

<!-- chunk {"id": "body-0152", "role": "body", "section": "The adversarial case", "weight": 1.0} -->

for any $\eta > 0$ and all sufficiently large $d$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "The adversarial case", "weight": 1.0} -->

Since $\mathcal{K}_{\mathbf{m}}^{(d)}$ is a singleton, Theorem 4.11 implies that event (6.6) holds with overwhelming probability in high dimensions whenever

<!-- chunk {"id": "body-0154", "role": "body", "section": "The adversarial case", "weight": 1.0} -->

Computing $\theta_{\ell_{1}}{(\tau,\psi)}$ and $\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}$ numerically, we find that for all $\tau \lesssim 0.0186$, inequality (6.7) holds. We conclude that our channel coding scheme is robust to all adversarial corruptions so long as the corruptions have no more than about $1.8\%$ nonzero entries. This computation is illustrated in Figure 12.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

We perform two numerical experiments to complement our theory, one for the benign corruptions and the other for a specific type of malicious erasure.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

For dimensions $d = 100$ and $d = 300$ and for each of $70$ equally spaced values of $\tau \in {\lbrack 0,0.35\rbrack}$,

<!-- chunk {"id": "body-0157", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

Choose a corruption ${\mathbf{c}}_{0}$ with $k = {\lbrack{\taud}\rbrack}$ nonzero elements; the support of ${\mathbf{c}}_{0}$ is random, and the nonzero elements are taken to be $\pm 1$ with equal probability.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

Generate a random basis ${\mathbf{Q}} \in \mathsf{O}_{d}$; see Remark 6.1.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

The second experiment incorporates a malicious erasure. As in the benign case, the experiment is run for dimensions $d = 100$ and $d = 300$ and for $70$ equally spaced values of $\tau$ between zero and one.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

The curves in Figure 3 show the results of these experiments. For benign corruptions, the empirical $50\%$ success rate occurs very near the predicted sparsity value $\tau = 0.193$, and the transition region is more narrow for larger $d$. Thus, the experiment closely match our prediction for the location of the asymptotic phase transition.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

The empirical evidence suggests that our adversarial guarantees are conservative for the type of malicious corruption used in the experiment. This is expected, as we have no reason to believe that such erasures correspond to the worst-case corruption. However, the empirical transition between success and failure near $\tau \approx 0.05$ suggests that our adversarial bound lies within a factor of two or three of the best possible guarantee.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Low-rank matrices under sparse corruptions", "weight": 1.0} -->

To promote low-rank, we use the Schatten 1-norm, and to promote sparsity, we use the matrix $\ell_{1}$ norm. Given the side information $\alpha = \left\| {\mathbf{Y}}_{0} \right\|_{\ell_{1}}$, we pose the convex demixing method

<!-- chunk {"id": "body-0163", "role": "body", "section": "Low-rank matrices under sparse corruptions", "weight": 1.0} -->

We study when $({\mathbf{X}}_{0},{\mathbf{Y}}_{0})$ is the unique solution to (6.8) with overwhelming probability in high dimensions.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Low-rank matrices under sparse corruptions", "weight": 1.0} -->

By Proposition 5.4, we see that $\theta_{S_{1}}{(\rho)}: = 6\rho - 3\rho^{2}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{S_{1}},{\mathbf{X}}_{0}) \right.\}$ of feasible cones, indexed by the ambient dimension. However, a smaller upper decay threshold ${\overset{\sim}{\theta}}_{S_{1}}{(\rho)}$ is available using the results of ---see Remark 5.5. The green line in Figure 4 is the level set

<!-- chunk {"id": "body-0165", "role": "body", "section": "Low-rank matrices under sparse corruptions", "weight": 1.0} -->

where the ${\overset{\sim}{\theta}}_{S_{1}}{(\rho)}$ is given by the asymptotic upper bound on the Gaussian width given implicitly in \[60, Eq. \].^§§^§Our actual computation uses the simpler, but equivalent, formula given in \[5, Prop. 4.9\]. For $(\rho,\tau)$ pairs lying below the curve, Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that our demixing method (6.8) succeeds with overwhelming probability in high dimensions.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

Let us summarize the experiment in Figure 4.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

Generate a random matrix ${\mathbf{Y}}_{0} \in {\mathbb{R}}^{n \times n}$ with $\lbrack{\taun^{2}}\rbrack$ nonzero entries; the nonzero entries in ${\mathbf{Y}}_{0}$ take the values $+ 1$ or $- 1$ with equal probability.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

From Figure 4, we see that the theoretical bound closely matches the empirical success curve throughout the entire regime.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Assorted matrix demixing problems", "weight": 1.0} -->

We conclude this section with some other combinations of structured square matrices that we can separate using the convex demixing method (1.2). In each of these applications, we observe a superposition of the form ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}} \in {\mathbb{R}}^{n \times n}$, where $\mathcal{Q}$ is a random basis for the matrix space ${\mathbb{R}}^{n \times n}$. We consider various structures for ${\mathbf{X}}_{0}$ and ${\mathbf{Y}}_{0}$---either low rank, orthogonal, sparse, or sign matrices---and we show that our theory quickly identifies a regime where an appropriate convex demixing method succeeds with overwhelming probability in high dimensions. While we know of no concrete applications for these particular demixing programs, the analysis below illustrates the ease with which our theory extends to new settings.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Orthogonal and sparse matrices", "weight": 1.0} -->

The interchange of the objective and constraint as compared with (1.2) poses no difficulty because the optimality conditions of Lemma 2.4 are symmetric with respect to the objective and constraint.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Orthogonal and sparse matrices", "weight": 1.0} -->

By Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), the convex demixing method (6.9) succeeds with overwhelming probability in high dimensions so long as

<!-- chunk {"id": "body-0172", "role": "body", "section": "Orthogonal and sparse matrices", "weight": 1.0} -->

where $\theta_{\ell_{1}}{(\tau)}$, defined in Appendix C, is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{Y}}_{0}) \right.\}$ and $\theta_{Op} = \frac{3}{4}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{Op},{\mathbf{X}}_{0}) \right.\}$ by Proposition 5.6. Therefore, program (6.9) succeeds with overwhelming probability in high dimensions whenever

<!-- chunk {"id": "body-0173", "role": "body", "section": "Orthogonal and sparse matrices", "weight": 1.0} -->

This occurs for $\tau < 0.06$; see the left panel of Figure 11. We conclude that (6.9) demixes an orthogonal matrix ${\mathbf{X}}_{0}$ from a matrix sparse in a random basis $\mathcal{Q}{({\mathbf{Y}}_{0})}$ with high probability when no more than about $6\%$ of the elements of ${\mathbf{Y}}_{0}$ are nonzero.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Low-rank and sign matrices", "weight": 1.0} -->

We invoke Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") to see that (6.10) succeeds with overwhelming probability in high dimensions whenever ${{\theta_{S_{1}}{(\rho)}} + \theta_{{\mathbb{R}}_{+}^{d}}} < 1$. Here, $\theta_{S_{1}}{(\rho)}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{S_{1}},{\mathbf{X}}_{0}) \right.\}$ of feasible cones, and $\theta_{{\mathbb{R}}_{+}^{d}}$ is an upper decay threshold for the ensemble of nonnegative orthants. By Proposition 3.12.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Low-rank and sign matrices", "weight": 1.0} -->

‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), we have $\theta_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$, while Proposition 5.4 gives ${\theta_{S_{1}}{(\rho)}} = {{6\rho} - {5\rho^{2}}}$. Therefore, the convex demixing method (6.10) succeeds with overwhelming probability in high dimensions so long as

<!-- chunk {"id": "body-0176", "role": "body", "section": "Low-rank and sign matrices", "weight": 1.0} -->

This bound is valid when $\rho \leq 0.09$. We conclude that (6.10) can demix a low-rank matrix from a sign matrix in a random basis with overwhelming probability if ${{rank}{({\mathbf{X}}_{0})}} \leq {0.09n}$, where $n$ is side length of ${\mathbf{X}}_{0}$.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Low-rank and orthogonal matrices", "weight": 1.0} -->

Let $\rho \in {\lbrack 0,1\rbrack}$ be a proportional rank parameter. For each side length $n \in {\mathbb{N}}$, choose a low-rank matrix ${\mathbf{X}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{rank}{({\mathbf{X}}_{0})}} = {\lceil{\rhon}\rceil}$ and an orthogonal matrix ${\mathbf{Y}}_{0} \in \mathsf{O}_{n}$. With the usual choice of complexity measures, the convex demixing method is

<!-- chunk {"id": "body-0178", "role": "body", "section": "Low-rank and orthogonal matrices", "weight": 1.0} -->

By Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), program (6.11) succeeds with overwhelming probability in high dimensions so long as ${{\theta_{S_{1}}{(\rho)}} + \theta_{Op}} < 1$. Propositions 5.4 and 5.6 imply that this occurs whenever

<!-- chunk {"id": "body-0179", "role": "body", "section": "Low-rank and orthogonal matrices", "weight": 1.0} -->

For instance, it suffices that $\rho \leq 0.04$. Therefore, the convex demixing method (6.11) can identify a superposition of a low-rank matrix and an orthogonal matrix with overwhelming probability in high dimensions so long as ${{rank}{({\mathbf{X}}_{0})}} \leq {0.04n}$, where $n$ is the side length of ${\mathbf{X}}_{0}$.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Prior art and future directions", "weight": 1.0} -->

This work occupies a unique place in the literature on demixing. The analysis is highly general and applies to many problems. At the same time, the results are sharp or nearly sharp. This final section offers a wide-angle view of the field of demixing, from applications to analytical techniques, with a focus on methods based on convex optimization. We conclude by discussing some extensions of our current approach in the hope of encouraging further development in this field.

<!-- chunk {"id": "body-0181", "role": "body", "section": "A short history of convex demixing and incoherence", "weight": 1.0} -->

The use of convex optimization for signal demixing has a long history. Early predecessors to morphological component analysis come from the work of Claerbout & Muir and Taylor et al., where $\ell_{1}$ minimization is used to identify sparse spike trains from an observed seismic trace.

<!-- chunk {"id": "body-0182", "role": "body", "section": "A short history of convex demixing and incoherence", "weight": 1.0} -->

Demixing methods based on $\ell_{1}$ minimization were put on a rigorous footing in the 1980s with the work of Santosa & Symes and Donoho & Stark. These results, either implicitly or explicitly, rely on incoherence in the form of an uncertainty principle. The work of Donoho & Huo formalizes the notion of incoherence. Incoherent models, both random and deterministic, now pervade the sparse demixing literature.

<!-- chunk {"id": "body-0183", "role": "body", "section": "A short history of convex demixing and incoherence", "weight": 1.0} -->

In the last decade, new classes of convex regularizers have been introduced for solving inverse problems in signal processing. In particular, the Schatten 1-norm is used for problems involving low-rank matrices,. Demixing methods that involve the Schatten 1-norm include robust principal component analysis and latent variable selection. Rigorous theoretical results for these techniques typically involve a spectral incoherence assumption, but no previous work in this area identifies phase transition behavior.

<!-- chunk {"id": "body-0184", "role": "body", "section": "The neighborhood of this work", "weight": 1.0} -->

We take much of our inspiration from the geometric analysis of linear inverse problems. Indeed, the geometric optimality condition (Lemma 2.4) is a direct generalization of a geometric result \[15, Prop. 2.1\] for linear inverse problems. Moreover, the Gaussian width bounds from that work prove useful for computing the decay thresholds in this research.

<!-- chunk {"id": "body-0185", "role": "body", "section": "The neighborhood of this work", "weight": 1.0} -->

A related line of work, due to Negahban et al. is based on the concept of restricted strong convexity. The results in these papers are sharp within constant factors, but they do not yield bounds as precise as ours. Another general approach to demixing appears in of, where a deterministic incoherence condition leads to recovery guarantees, even in nonconvex settings. The recovery bounds available through this method are not competitive with the guarantees we provide.

<!-- chunk {"id": "body-0186", "role": "body", "section": "The neighborhood of this work", "weight": 1.0} -->

Several works also consider demixing two sparse vectors. The works, show that a nearly dense vector could be demixed from a sufficiently sparse vector, but they do not identify phase transition behavior. Recent work also offers demixing guarantees for demixing sparse vectors when the sparsity is mildly sublinear in the dimension. Their model is similar to our MCA formulation in Section 1.1, but again the results do not identify the phase transition between success and failure.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Random geometry and convex optimization", "weight": 1.0} -->

We now trace the use of methods from integral geometry for understanding randomized convex optimization programs. Vershik & Sporyshev use an asymptotic analysis of polytope angles to analyze the average-case behavior of the simplex method for linear programming. The underlying formulas have their roots in the results of Ruben, although some of the ideas apparently go back to the work Schläfli from the mid-nineteenth century---see Ruben's paper for a discussion.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Random geometry and convex optimization", "weight": 1.0} -->

The analysis of Vershik & Sporyshev fed a line of investigation on the expected face counts of randomly projected polytopes a topic of theoretical interest in combinatorial geometry. These computations resurfaced in convex optimization in the line of work of Donoho & Tanner. These articles characterize the behavior of convex optimization methods for solving several linear inverse problems under a random measurement model. In Appendix C, we leverage the asymptotic polytope angle calculations of Donoho & Tanner to compute decay threshold for the $\ell_{1}$ norm at sparse vectors.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Random geometry and convex optimization", "weight": 1.0} -->

This asymptotic polytope angle approach also yields stability guarantees for basis pursuit. Furthermore, it has been used to establish that iteratively reweighted basis pursuit can provide strictly stronger guarantees than standard basis pursuit.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Random geometry and convex optimization", "weight": 1.0} -->

Our approach to random geometry differs from these earlier works because it starts with the modern theory of spherical integral geometry. Previous research was based on an older theory of polytope angles. Spherical integral geometry reached its current state of development in the dissertation,. Chapter 6.5 of and the notes therein summarize this research. We also draw on insights from the thesis.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

The results in this work demonstrate the power of spherical integral geometry in the context of demixing. Our bounds are often tight, and they are broadly applicable. This approach raises many questions worth further attention. We conclude with a list of directions for future work. During the period that our original manuscript was under review, several of these areas have seen significant progress. We augment our original list of open problems with a summary of progress made in the interim.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

Tight results for Lagrangian demixing.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

: The Lagrange penalized demixing method (1.3) is important because it requires less knowledge about the unobserved vectors $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ than the corresponding constrained method (1.2). The results in this work give information regarding the potential, and the limits of, the penalized demixing approach (1.2). Nevertheless, a precise analysis of the penalized problem (1.3) and its dependence on the penalty parameter $\lambda$ would have real practical value.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

*While a sharp phase transition characterization for the Lagrange demixing problem (1.3) remains open, the recent work offers theoretical guarantees and explicit choices of Lagrange parameters.*

<!-- chunk {"id": "body-0195", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

: It would be interesting to study demixing problems involving more than two structured vectors.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

*A study of this problem appears. The present authors provide sharp phase transition characterizations for demixing an arbitrary number of signals.*

<!-- chunk {"id": "body-0197", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

Spherical intrinsic volumes for more cones.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

: Computation of additional decay thresholds will provide new bounds for convex demixing methods. The sharpest decay thresholds appear to require formulas for spherical intrinsic volumes. For instance, an asymptotic analysis of the spherical intrinsic volumes for feasible cones of the Schatten 1-norm would provide sharp recovery results for low-rank matrix demixing problems. Amelunxen & Bürgisser have made some recent progress in this direction by developing a formula for the spherical intrinsic volumes for the semidefinite cone.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

: Bürgisser & Amelunxen \[10, Conj. 2.19\] conjecture that the sequence of spherical intrinsic volumes is log-concave. This conjecture is closely related to the question of whether the upper and lower decay thresholds match.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

*In recent work by the present authors and collaborators, the intrinsic volumes are shown to have a nontrivial log-concave upper bound \[5, Sec. 6.1\]. While this result implies that the upper and lower decay thresholds are often equal (Section 4.2.2), the log-concavity conjecture remains open.*

<!-- chunk {"id": "body-0201", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

Extensions to more general probability measures.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

: The analysis in this work focuses on a specific random model. It would be interesting to incorporate more general probability measures into our framework. This may be a difficult problem; by the results of Section 5.2, this question is closely related to the observed universality phenomenon in basis pursuit.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

*Bayati et al. provide a rigorous version the universality property for basis pursuit observed. It remains unclear whether their methods adapt to demixing problems considered here.*
