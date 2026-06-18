## Introduction

In modern data-intensive science, it is common to observe a superposition of multiple information-bearing signals. *Demixing* refers to the challenge of separating out the constituent signals from the observation. A fundamental computational question is to understand when a tractable algorithm can successfully complete the demixing. Problems of this sort arise in fields as diverse as acoustics, astronomy, communications geophysics, image processing machine learning, and statistics. Some well-known examples of convex methods for demixing include morphological component analysis, robust principal component analysis and inpainting.

This work presents a general framework for demixing based on convex optimization. We study the geometry of the optimization problem, and we develop conditions that describe precisely when our method succeeds. Let us illustrate the major aspects of our approach through a concrete example.

### A first application: Morphological component analysis

Starck et al. use demixing to model the problem of distinguishing stars from galaxies in an astronomical image. This task requires hypotheses on the two types of objects. First, we must assume that stars and galaxies exhibit different kinds of structure: stars appear as localized bright points, while galaxies are wispy or filamented. Second, we must insist that the image is not so full of stars, nor of galaxies, that they obscure one another. These two properties are modeled by the notions of *incoherence* and *sparsity*. With these hypotheses, we can solve the demixing problem using a method known as morphological component analysis (MCA).

### The MCA signal model

We model the observation ${\mathbf{z}}_{0} \in {\mathbb{R}}^{d}$ as the superposition of two structured signals:

The matrices $\mathbf{A}$ and $\mathbf{B}$ are known, while the vectors ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are unknown. Each column of $\mathbf{A}$ contains an elementary structure that might appear in the first signal; the columns of $\mathbf{B}$ reflect the structures in the second signal. The vector ${\mathbf{x}}_{0}$ selects the columns of $\mathbf{A}$ that appear in the first signal, e.g., stars in different locations, while ${\mathbf{y}}_{0}$ selects the columns of $\mathbf{B}$ that generate the second signal, e.g., galaxies in different locations. *Incoherence* demands that the columns of $\mathbf{A}$ and $\mathbf{B}$ are weakly correlated, and *sparsity* requires that ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ have few nonzero elements.

For simplicity, we assume that $\mathbf{A}$ and $\mathbf{B}$ are orthonormal bases. By changing coordinates, we may take ${\mathbf{A}} = \mathbf{I}$, the identity matrix. The observation then has the form

for a known orthogonal matrix $\mathbf{Q}$. The specialization to orthonormal bases is standard.

Instead of restricting our attention to specific choices of $\mathbf{Q}$ that are incoherent with the identity matrix, we consider an idealized model for incoherence where $\mathbf{Q}$ is a uniformly random orthogonal matrix. This formulation ensures that the structures in the two signals are oriented generically with respect to each other. Other authors have also used this approach to study incoherence,.

We quantify the sparsity of the two constituent signals by fixing parameters $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ in the interval $\lbrack 0,1\rbrack$ such that the unknown signals ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ satisfy

where ${nnz}{({\mathbf{x}})}$ denotes the number of nonzero elements of $\mathbf{x}$.^‡‡^‡We prefer the notation ${nnz}{( \cdot )}$ over $\parallel \cdot \parallel_{\ell_{0}}$ because the number of nonzero elements in a vector is not a norm. In other words, $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ measure the proportion of nonzero entries in ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. These sparsity parameters emerge as the major factor that determines how hard it is to extract ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ from the observation ${\mathbf{z}}_{0}$.

### The constrained MCA demixing procedure

The goal of morphological component analysis is to identify the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ of sparse vectors given the observation ${\mathbf{z}}_{0}$ and the matrix $\mathbf{Q}$. A natural technique for finding a sparse vector that satisfies certain conditions is to minimize the $\ell_{1}$ norm subject to these constraints, where the $\ell_{1}$ norm is defined as $\left. \parallel{\mathbf{x}}\parallel{}_{\ell_{1}}: = \sum_{i = 1}^{d}|x_{i}| \right.$.

Assume that we have access to side information $\alpha = {\|{\mathbf{y}}_{0}\|}_{\ell_{1}}$. Then the intuition above leads us to frame the following convex optimization problem for demixing:

where the decision variables are ${{\mathbf{x}},{\mathbf{y}}} \in {\mathbb{R}}^{d}$. We call this optimization problem *constrained MCA*, and we say that it *succeeds* if $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is the unique optimal point of (1.1). Since (1.1) can be written as a linear program, constrained MCA offers a tractable procedure for attempting to identify the underlying components $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$, provided the observation ${\mathbf{z}}_{0}$, the orthogonal matrix $\mathbf{Q}$, and the side information $\alpha = {\|{\mathbf{y}}_{0}\|}_{\ell_{1}}$.

Constrained MCA is closely related to the standard MCA procedure, which is a Lagrangian formulation of (1.1) that does not require the side information $\alpha$ \[71, Eq. \]. The constrained problem (1.1) is more powerful than the standard MCA procedure, so it provides hard limits on the effectiveness of the usual approach. In most cases, the two methods are equivalent, provided that we can choose the Lagrange multiplier correctly---a nontrivial task in itself. See Section 1.2.4 for more details.

Figure 1: Performance of constrained MCA. The variables τx and τy on the axes represent the fraction of components in x0 and y0 that are nonzero. The background shading indicates the empirical probability that the constrained MCA problem (1.1) identifies the pair (x0,y0) from the observation z0 = x0 + Q y0, where Q is a random orthogonal basis. The yellow curve marks the empirical 50% success threshold. The green curve locates the theoretical phase transition for demixing a single pair (x0,y0). For sparsity levels below the blue curve, constrained MCA (1.1) provably recovers all (τx,τy)-sparse pairs with high probability in the dimension. Further details are available in Section 1.1.3 and Section 6.1.

### Numerical and theoretical results for constrained MCA

Figure 1 displays the result of a numerical experiment on constrained MCA. We fix the dimension $d = 100$. For sparsity levels $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ varying over the unit square ${\lbrack 0,1\rbrack}^{2}$, we form vectors ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ with sparsity levels ${{nnz}{({\mathbf{x}}_{0})}} = {\lceil{\tau_{\mathbf{x}}d}\rceil}$ and ${{nnz}{({\mathbf{y}}_{0})}} = {\lceil{\tau_{\mathbf{y}}d}\rceil}$. (The manner in which we choose the nonzero entries is irrelevant.) We draw a random orthogonal matrix $\mathbf{Q}$ and construct the observation ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$. Then we solve the constrained MCA problem (1.1) to identify the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$. The background of the figure shows the empirical probability of success over the randomness in $\mathbf{Q}$; dark areas denote low probability of success, while light areas denote high success rates. The yellow curve marks the $50\%$ success threshold.

This work establishes two theoretical results for constrained MCA. The first result provides a phase transition curve, parameterized by the sparsity $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$, for the probability that constrained MCA will demix a single pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0}$. This *weak bound* is marked by the green line in Figure 1. Observe that the green line coincides almost perfectly with the empirical phase transition.

Second, we establish a *strong bound*. For a fixed instantiation of the random orthogonal basis $\mathbf{Q}$, with high probability, constrained MCA (1.1) can identify *every* sufficiently sparse pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0}$. The blue curve in the bottom left corner of Figure 1 is a lower estimate for the sparsity pairs $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ where this uniform guarantee holds. Section 6.1 provides the details regarding the computation of the weak and strong bounds as well as a fully detailed description of our numerical experiment.

### A recipe for demixing

This work is not primarily about MCA. We are interested in developing methods that apply to a whole spectrum of demixing problems. The following two sections describe how to construct a convex program that can separate two structured signals.

### Structured signals and atomic gauges

Figure 2: Atomic gauge. [Left] Let 𝒜 be an atomic set consisting of five atoms (stars). The “unit ball” of the atomic gauge f𝒜 is the closed convex hull of 𝒜 (heavy line). Other level sets (dashed lines) of f𝒜 are dilations of the unit ball. [Right] At an atom (star), the unit ball of f𝒜 tends to have sharp corners. Most perturbations away from this atom increase the value of f𝒜, so the atomic gauge is an effective measure of the complexity of an atomic signal.

The $\ell_{1}$ norm is a convex complexity measure that tends to be small near sparse vectors, so we can minimize the $\ell_{1}$ norm to promote sparsity. We now describe a method for building complexity measures that are appropriate for other types of structure. This construction was originally introduced in the nonlinear approximation literature,. The recent paper explains how to apply these ideas to solve signal processing problems.

In practice, we often encounter signals that are formed as a positive linear combination of a few elementary structures, called *atoms*, drawn from a fixed collection. For example, a sparse vector in ${\mathbb{R}}^{d}$ is a conic combination of a small number elements from the set $\{{{{\pm {\mathbf{e}}_{i}}:i = 1},{\ldots,d}}\}$ of signed standard basis vectors. We want to construct a function that reflects the complexity of an atomic signal.

We define the *atomic gauge* of a vector ${\mathbf{x}} \in {\mathbb{R}}^{d}$ with respect to a set $\mathcal{A} \subset {\mathbb{R}}^{d}$ of atoms by

with the convention that ${f_{\mathcal{A}}{({\mathbf{x}})}} = {+ \infty}$ if the set is empty. Then $f_{\mathcal{A}}$ is a homogeneous convex function. The "unit ball" of $f_{\mathcal{A}}$ is $\overline{conv}{(\mathcal{A})}$, and the level sets of $f_{\mathcal{A}}$ are dilations of this unit ball. The atomic gauge $f_{\mathcal{A}}$ is a norm if and only if $\overline{conv}{(\mathcal{A})}$ is a bounded, symmetric set that contains zero in its interior.

The convex hull of an atomic set $\mathcal{A}$ tends to have sharp corners at atoms; see Figure 2. At these sharp points, most perturbations of the objective increase the value of the gauge, so the atomic gauge tends to take small values at atoms. Similar behavior occurs at a signal comprised of a relatively small number of atoms. This observation is a key reason that atomic gauges make good complexity measures for atomic signals. Some common atomic gauges include

*The $\ell_{1}$ norm.* The $\ell_{1}$ norm on ${\mathbb{R}}^{d}$ is the atomic gauge generated by the set $\mathcal{A} = {\{ \pm {\mathbf{e}}_{i}:i = 1,\ldots,d\}}$ of signed standard basis vectors. This norm is widely used to promote sparsity. The $\ell_{1}$ norm may also be defined for matrices via the formula $\left\| {\mathbf{X}} \right\|_{\ell_{1}} = {\sum_{i,j}{|X_{ij}|}}$. In this context, the $\ell_{1}$ norm reflects the sparsity of matrices.

*The $\ell_{\infty}$ norm.* The $\ell_{\infty}$ norm on ${\mathbb{R}}^{d}$, given by $\left\| {\mathbf{x}} \right\|_{\ell_{\infty}} = {\max_{i = {1,\ldots,d}}{|x_{i}|}}$, is the atomic gauge generated by the set $\mathcal{A} = {\{{\pm 1}\}}^{d} \subset {\mathbb{R}}^{d}$ of all $2^{d}$ sign vectors. We use this norm to demix binary codewords. See also. For matrices, the $\ell_{\infty}$ norm returns $\left\| {\mathbf{X}} \right\|_{\ell_{\infty}} = {\max_{i,j}{|X_{ij}|}}$; this function is the atomic gauge generated by the set of sign matrices.

*The Schatten 1-norm.* The Schatten 1-norm on ${\mathbb{R}}^{m \times n}$ is the sum of the singular values of a matrix. It is the atomic gauge generated by the set of rank-one matrices in ${\mathbb{R}}^{m \times n}$ with unit Frobenius norm. Minimizing the Schatten 1-norm promotes low rank,.

*The operator norm.* The operator norm returns the maximum singular value of a matrix. On the space ${\mathbb{R}}^{n \times n}$ of square matrices, the operator norm is the atomic gauge generated by the set $\mathsf{O}_{n}$ of orthogonal matrices. This norm can be used to search for orthogonal matrices \[15, Prop. 3.13\]

Our applications focus on these four instances, but a dizzying variety other structure-promoting atomic gauges are available. For example, there are atomic gauges for vectors that are sparse in a dictionary (also known as analysis-sparsity) block- and group-sparse vectors and low-rank tensors and probability measures \[15, Sec. 2\].

### A generic model for incoherence

Demixing is hopeless when the structures in the constituent signals are too strongly aligned. As an extreme example, suppose we observe ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {\mathbf{y}}_{0}}$, where both ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are sparse. There is clearly no principled way to assign the nonzero elements of ${\mathbf{z}}_{0}$ correctly to ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. In contrast, if we observe ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {\mathbf{H}{\mathbf{y}}_{0}}}$, where $\mathbf{H}$ is a normalized Walsh--Hadamard transform and both ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ are sparse, then the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is typically identifiable. The latter situation is more favorable than the former because the Walsh--Hadamard matrix and the identity matrix are incoherent; that is, their columns are weakly correlated.

In order to avoid restricting our attention to special cases, such as the Walsh--Hadamard matrix, we model incoherence by assuming that the basis $\mathbf{Q}$ is drawn randomly from the invariant Haar measure on the set of all orthogonal matrices $\mathsf{O}_{d}$. We call this the *random basis model.* This idealized approach to incoherence guarantees that the structures in the two constituent signals are generically oriented. This model has precedents in the literature on sparse approximation and it is analogous to the assumption of a measurement operator with a uniformly random nullspace that appears in the context of compressed sensing,.

We expect that the random basis model also sheds light on other highly incoherent problems, such as the case where ${\mathbf{Q}} = \mathbf{H}$ is the Walsh--Hadamard transform or ${\mathbf{Q}} = \mathbf{D}$ is the discrete cosine transform (DCT). Some limited numerical simulations suggest that both the Walsh--Hadamard and the DCT matrices behave qualitatively similar to the random matrix $\mathbf{Q}$ in the examples considered in this work. This observation is in line with the universality of phase transitions that appear in $\ell_{1}$ minimization for many classes of measurement matrices. However, more coherent situations may exhibit different behavior, and thus they fall outside the purview of this work.

### Formulating a convex demixing method

We are ready to introduce a computational framework for demixing structured signals. This approach unifies several related procedures that appear in the literature. See, for example.

Assume we observe the superposition of two structured signals:

where $\mathbf{Q}$ is a known orthogonal matrix and the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is unknown. We include the matrix $\mathbf{Q}$ in the formalism because it allows us to model incoherence using the random basis model described in Section 1.2.2 above. Our goal is to demix the pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the observation ${\mathbf{z}}_{0}$.

Let $f$ and $g$ be convex complexity measures---such as atomic gauges---associated with the structures we expect to find in ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. Suppose we have access to the additional side information $\alpha = {g{({\mathbf{y}}_{0})}}$. We combine these ingredients to reach the following convex demixing method:

where the decision variables are ${{\mathbf{x}},{\mathbf{y}}} \in {\mathbb{R}}^{d}$. The display (1.2) describes a convex program because $f$ and $g$ are convex functions. We say that the convex demixing method (1.2) *succeeds at demixing $(\mathbf{x}_{0},\mathbf{y}_{0})$*, or simply *succeeds*, if $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is the unique optimal point of (1.2); otherwise, it *fails*. In this work, we develop conditions that describe when the convex demixing method (1.2) succeeds and when it fails.

### The Lagrangian counterpart

In practice, the value $\alpha = {g{({\mathbf{y}}_{0})}}$ may not be known. In this case, we may replace the convex demixing method (1.2) with its Lagrangian relative

where $\lambda > 0$ is a regularization parameter that must be specified. The constrained problem (1.2) is slightly more powerful than (1.3), so its performance dominates the Lagrangian formulation (1.3). It is well known that (1.2) and (1.3) are essentially equivalent when the regularization parameter $\lambda$ is chosen correctly and a mild regularity condition holds; see Appendix A for details. Thus, we can interpret our results as delineating the *best possible performance* of the Lagrange problem (1.3).

This type of best-case analysis has precedents in the literature on sparse approximation, e.g. yet the identification of optimal Lagrange parameters for demixing remains a significant open problem. Several works prove that specific demixing procedures succeed for specific choices of Lagrange parameters under incoherence assumptions but these conservative guarantees fail to identify phase transitions. Since this document was submitted, some additional theoretical guidance choosing Lagrange parameters has appeared. Nevertheless, a comprehensive theory describing the optimal choices of Lagrange parameters for (1.3) does not currently exist.

### One hammer, many nails

The convex demixing method (1.2) includes many interesting special cases. Our analysis provides detailed information about when (1.2) is able to separate two structured, incoherent signals. We now describe some applications of this machinery.

### A secure communications protocol that is robust to sparse errors

Figure 3: Performance of the robust communication protocol. The heavy curves indicate the empirical probability that problem (1.4) decodes a d-bit message m0 ∈ {±1}d from the observation z0 = Q m0 + c0, where Q is a random orthogonal matrix. The variable τ on the horizontal axis measures the proportion of nonzero entries in the corruption c0. A benign corruption is independent of Q, while an adversarial erasure zeros out the [τ d] largest components of the transmitted message. The vertical line at τ ≈ 0.19 marks the theoretical phase transition for successful decoding under a benign corruption. The vertical line at τ ≈ 0.018 provides a uniform guarantee applicable to adversarial corruptions. For τ ≲ 0.018, with high probability, our protocol will decode a message subject to any τ-sparse corruption whatsoever. See Section 1.3.1 and Section 6.2 for more details.

Suppose we wish to securely transmit a binary message across a communications channel. We can obtain strong guarantees of security by modulating the message with a random rotation before transmission,. Our theory shows that decoding the message via demixing also makes this secure scheme perfectly robust to sparse corruptions such as erasures or malicious interference.

Consider the following simple communications protocol. We model the binary message as a sign vector ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$. Choose a random orthogonal matrix ${\mathbf{Q}} \in \mathsf{O}_{d}$. The transmitter sends the scrambled message ${\mathbf{s}}_{0} = {{\mathbf{Q}}{\mathbf{m}}_{0}}$ across the channel, where it is corrupted by an unknown sparse vector ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$. The receiver must determine the original message given only the corrupted signal

and knowledge of the scrambling matrix $\mathbf{Q}$.

This signal model is perfectly suited to the demixing recipe of Section 1.2. The discussion in Section 1.2.1 indicates that the $\ell_{1}$ and $\ell_{\infty}$ norms are natural complexity measures for the structured signals ${\mathbf{c}}_{0}$ and ${\mathbf{m}}_{0}$. Since the message ${\mathbf{m}}_{0}$ is a sign vector, we also have the side information $\left\| {\mathbf{m}}_{0} \right\|_{\ell_{\infty}} = 1$. Our receiver then recovers the message with the convex demixing method

where the decision variables are ${{\mathbf{c}},{\mathbf{m}}} \in {\mathbb{R}}^{d}$. This method succeeds if $({\mathbf{c}}_{0},{\mathbf{m}}_{0})$ is the unique optimal point of (1.4).

In Section 6.2, we apply the general theory developed in this work to study this communications protocol. Before summarizing the results of this analysis, we fix some notation. Suppose the corruption ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$ is $\tau$-sparse; that is, ${{nnz}{({\mathbf{c}}_{0})}} = {\lceil{\taud}\rceil}$ for some $\tau \in {\lbrack 0,1\rbrack}$. We further distinguish between two types of corruption. A *benign* corruption ${\mathbf{c}}_{0}$ is independent of the scrambling matrix $\mathbf{Q}$. In contrast, an *adversarial* corruption may depend on both $\mathbf{Q}$ and ${\mathbf{m}}_{0}$. Adversarial corruptions also include nonlinear effects that are not necessarily malicious. For example, we can model an erasure at the $i$th time instant by taking ${({\mathbf{c}}_{0})}_{i} = {- {({{\mathbf{Q}}{\mathbf{m}}_{0}})}_{i}}$.

Figure 3 presents the results of a numerical experiment on this communications protocol; the complete experimental procedure is detailed in Section 6.2.3. Briefly, we consider messages of length $d = 100$ and $d = 300$, and we let the sparsity $\tau$ range over the interval $\lbrack 0,0.35\rbrack$. We test the benign case by adding a $\tau$-sparse corruption that is independent from $\mathbf{Q}$. We also consider a particular adversarial corruption in which we set the $\lbrack{\taud}\rbrack$ largest-magnitude entries in the transmitted message ${\mathbf{s}}_{0}$ to zero. The curves indicate the empirical probability that the protocol succeeds as a function of $\tau$.

In the benign case, our theory shows that there exists a phase transition in the success probability of the convex demixing method (1.4) at sparsity level $\tau \approx 0.19$. The empirical $50\%$ failure threshold for benign corruptions closely matches this prediction. In the adversarial case, our results guarantee that with high probability, our protocol will tolerate all corruptions that affect no more than $1.8\%$ of the components in the received message ${\mathbf{z}}_{0}$. This bound is conservative for the type of adversarial corruption in the numerical experiment; this is not surprising because we may not have constructed the worst possible corruption.

### Low-rank matrix recovery with generic sparse corruptions

Figure 4: Low-rank matrix recovery with sparse corruptions. The horizontal axis is the normalized rank ρ = rank(X0)/n, and the vertical axis is the sparsity level τ = nnz (Y0)/n2. The intensity of the background denotes the empirical probability that (1.5) recovers (X0,Y0) from the observation Z0 = X0 + 𝒬 (Y0). In the region below the green curve, the convex demixing method (1.5) recovers a low-rank matrix X0 from a randomly rotated sparse corruption 𝒬 (Y0) with overwhelming probability in high dimensions. See Section 1.3.2 and Section 6.3 for more details.

Consider now the *matrix* observation ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}} \in {\mathbb{R}}^{n \times n}$, where ${\mathbf{X}}_{0}$ has low rank, ${\mathbf{Y}}_{0}$ is sparse, and $\mathcal{Q}$ is a random rotation on ${\mathbb{R}}^{n \times n}$. This type of signal provides a highly stylized model for applications such as latent variable selection, and robust principal component analysis. In these settings, ${\mathbf{X}}_{0}$ has low rank because the underlying data is drawn from a low-dimensional linear model, while $\mathcal{Q}{({\mathbf{Y}}_{0})}$ represents a corruption. (Note, however, that this stylized model is not equivalent to pre- and post-multiplying ${\mathbf{Y}}_{0}$ by independent random rotations of ${\mathbb{R}}^{n}$.) We aim to discover the matrix ${\mathbf{X}}_{0}$ given the corrupted observation ${\mathbf{Z}}_{0}$ and the rotation $\mathcal{Q}$.

We follow the now-familiar pattern of Section 1.2. The Schatten 1-norm $\left. \parallel \cdot \parallel{}_{S_{1}} \right.$ serves as a natural complexity measure for the low-rank structure of ${\mathbf{X}}_{0}$, and the matrix $\ell_{1}$ norm $\left. \parallel \cdot \parallel{}_{\ell_{1}} \right.$ is appropriate for the sparse structure of ${\mathbf{Y}}_{0}$. We further assume the side information $\alpha = \left\| {\mathbf{Y}}_{0} \right\|_{\ell_{1}}$. We then solve

This convex demixing method succeeds if $({\mathbf{X}}_{0},{\mathbf{Y}}_{0})$ is the unique solution to (1.5).

Figure 4 displays the results of a numerical experiment on this approach to rank--sparsity demixing. We take the matrix side length $n = 35$ and draw a random rotation $\mathcal{Q}$ for ${\mathbb{R}}^{n \times n}$. For parameters ${0 \leq \rho},{\tau \leq 1}$, we generate matrices ${\mathbf{X}}_{0}$ and ${\mathbf{Y}}_{0}$ such that ${{rank}{({\mathbf{X}}_{0})}} = {\lbrack{\rhon}\rbrack}$ and ${{nnz}{({\mathbf{Y}}_{0})}} = {\lbrack{\taun^{2}}\rbrack}$. The background shading indicates the empirical probability that (1.5) succeeds given the observation ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}}$. We mark the empirical $50\%$ success probability with a yellow curve. See Section 6.3.1 for the experimental details.

The results of this work show that, with high probability, program (1.5) succeeds so long as the pair $(\rho,\tau)$ lies below the green curve on Figure 4. When the rank parameter $\rho$ is small, our theoretical bound closely tracks the phase transition visible in the numerical experiment, although the bound appears loose when $\rho$ is larger. Section 6.3 provides further details.

### Matrix demixing mix-and-match

Our results are not restricted to the convex demixing methods (1.1), (1.4) or (1.5). Let us mention a few other situations we can analyze using the theory developed in this work. With a tractable convex program, it is possible to demix

An orthogonal matrix from a matrix that is sparse in a random orthogonal basis,

A randomly oriented sign matrix from a sufficiently low-rank matrix, and

A randomly rotated low-rank matrix from an orthogonal matrix.

See Section 6.4 for the details.

### Theoretical insights

Our approach reveals a number of theoretical insights.

Design of convex demixing methods for incoherent structures.

: In the incoherent regime we analyze, the parameters that determine when the convex demixing method (1.2) succeeds reflect the structures in the constituent signals and the associated complexity measures. These summary parameters are independent of the relationship between the two incoherent structures. We discuss this fact and its consequences for the design of demixing procedures in Section 4.2.1.

Connection with linear inverse problems.

: The parameters that determine success of the convex demixing method (1.2) are closely related to number of random linear measurements required to identify a structured signal. In Section 5.2, we leverage this relationship to compute these parameters from Gaussian width bounds developed in.

: Our theory indicates that there is often a phase transition in the behavior of the demixing method (1.2). See Section 4.2.2 for a discussion of this point.

### Outline

This work begins with demixing in the deterministic setting. Section 2 describes the geometry of the convex demixing method (1.2) and provides a geometric characterization of successful demixing.

Section 3 presents a random model for incoherence along with some techniques from spherical integral geometry that allow us to analyze this model. In Section 4, these ideas yield theory that predicts success and failure regimes for the convex demixing method (1.2). Section 5 develops methods for computing the parameters necessary to apply the theorems of Section 4.

In Section 6, we analyze the application problems described in Sections 1.1 and 1.3. Section 7 concludes with a discussion of this work's place in the literature and future directions.

### Notation and conventions

All variables are real valued. We write $\lfloor t\rfloor$, $\lceil t\rceil$, and $\lbrack t\rbrack$ for the floor, ceiling, and rounded integer values of $t$. The signum function is ${{sgn}{(t)}}:={t/|t|}$ for $t \neq 0$ and ${{sgn}{}}:=0$. Bold lowercase letters represent vectors, and bold capital letters are matrices. The $i$th element of a vector is written $x_{i}$ or ${({\mathbf{x}})}_{i}$, while the $(i,j)$th element of a matrix is $X_{ij}$ or ${({\mathbf{X}})}_{ij}$. We express the transpose of $\mathbf{X}$ as ${\mathbf{X}}^{\ast}$. The vector signum ${sgn}{({\mathbf{x}})}$ is defined by applying the signum elementwise.

The symbol $\left. \parallel \cdot \parallel{}_{\ell_{p}} \right.$ stands for the $\ell_{p}$ vector norm on ${\mathbb{R}}^{d}$, defined by $\left. \parallel{\mathbf{x}} \parallel_{\ell_{p}}^{p}: = \sum_{i = 1}^{d}|x_{i}|^{p} \right.$ when $1 \leq p < \infty$ and $\left. \parallel{\mathbf{x}}\parallel{}_{\ell_{\infty}}: = \max_{i = {1,\ldots,d}}|x_{i}| \right.$ when $p = \infty$. The $\ell_{p}$ norm of a matrix treats the matrix as a vector and applies the corresponding vector $\ell_{p}$ norm. The Schatten 1-norm $\left\| {\mathbf{X}} \right\|_{S_{1}}$ is the sum of the singular values of a matrix $\mathbf{X}$, while the operator, or spectral, norm $\left\| {\mathbf{X}} \right\|_{Op}$ returns the maximum singular value of $\mathbf{X}$.

We reserve the symbols $f$ and $g$ for convex functions. A convex function may take the value $+ \infty$, but we assume that all convex functions are *proper*; that is, each convex function takes on at least one finite value and never takes the value $- \infty$.

The Euclidean unit sphere in ${\mathbb{R}}^{d}$ is the set $\mathsf{S}^{d - 1}$. The orthogonal group---the set of $d \times d$ orthogonal matrices---is denoted $\mathsf{O}_{d}$. The subset of $\mathsf{O}_{d}$ with determinant one (the *special* orthogonal group) is ${\mathsf{S}\mathsf{O}}_{d}$. For brevity, we use the term *basis* to refer to an orthogonal matrix from $\mathsf{O}_{d}$. In the sequel, the letter $\mathbf{Q}$ will always refer to a basis.

The symbol $\mathbb{P}$ denotes the probability of an event. Gaussian vectors and matrices have independent standard normal entries. A *random basis* is a matrix drawn from the Haar measure on $\mathsf{O}_{d}$.

A special note is in order when our observations are matrices. The space of matrices ${\mathbb{R}}^{m \times n}$ is equipped with a natural isomorphism to ${\mathbb{R}}^{mn}$ through the ${vec}{( \cdot )}$ operator, which stacks the columns of a matrix on top of one another to form a tall vector. We define a random basis $\mathcal{Q}$ for ${\mathbb{R}}^{m \times n}$ by ${\mathcal{Q}{({\mathbf{Y}})}} = {{vec}^{- 1}\left( {{\mathbf{Q}}{{vec}{({\mathbf{Y}})}}} \right)}$, where $\mathbf{Q}$ is a random basis for ${\mathbb{R}}^{mn}$. It is easily verified that such a $\mathcal{Q}$ is a random basis for ${\mathbb{R}}^{m \times n}$ equipped with the Euclidean structure induced by the Frobenius norm.

We deal frequently with convex cones, which are positively homogeneous convex sets. For any cone $K$, we define the polar cone

A *polyhedral cone* is the intersection of a finite number of closed halfspaces, each containing the origin. One important polyhedral cone is the nonnegative orthant, defined by

For a set $A \subset {\mathbb{R}}^{d}$, we write ${conv}{(A)}$ for its convex hull and $\overline{A}$ for its closure. Two cones ${K_{1},K_{2}} \subset {\mathbb{R}}^{d}$ are *congruent*, written $K_{1} \cong K_{2}$, if there is a basis ${\mathbf{U}} \in \mathsf{O}_{d}$ such that $K_{1} = {{\mathbf{U}}K_{2}}$.

## The geometry of demixing

This short section lays the geometric foundation for the rest of this work. Section 2.1 describes the local behavior of convex functions in terms of special convex cones. In Section 2.2, this geometric view yields a concise characterization of successful demixing in terms of the configuration of two cones. The results in this section are deterministic, that is, they hold for any fixed basis $\mathbf{Q}$.

### Feasible cones

The success of the convex demixing method (1.2) depends on the properties of the complexity measures $f$ and $g$ at the structured vectors ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$. The following definition captures the local behavior of a convex function.

### Definition 2.1 (Feasible cone)

The *feasible cone* of a convex function $f$ at a point ${\mathbf{c}}x$ is defined as the cone of directions at which $f$ is locally nondecreasing about $\mathbf{x}$:

### Example 2.2 (The feasible cone of the $\ell_{\infty}$ norm at sign vectors)

Let ${\mathbf{x}} \in {\{{\pm 1}\}}^{d}$ be a sign vector. Then it is easy to check that $\left\| {{\mathbf{x}} + {\lambda{\mathbf{δ}}}} \right\|_{\ell_{\infty}} \leq \left\| {\mathbf{x}} \right\|_{\ell_{\infty}} = 1$ for some $\lambda > 0$ if and only if ${{sgn}{(\delta_{i})}} = {- x_{i}}$ for all $i = {1,2,\ldots,d}$. Therefore, the feasible cone of the $\ell_{\infty}$ norm at $\mathbf{x}$ is congruent to the nonnegative orthant:

The feasible cone is always a convex cone containing zero, but it is not necessarily closed. If $\mathcal{A}$ is a set of atoms and ${\mathbf{a}} \in \mathcal{A}$, the feasible cone $\mathcal{F}{(f_{\mathcal{A}},{\mathbf{a}})}$ of the atomic gauge $f_{\mathcal{A}}$ at the atom $\mathbf{a}$ tends to be small because the unit ball of $f_{\mathcal{A}}$ is the smallest convex set containing all of the atoms. See Figure 2 for an illustration. The positive homogeneity of atomic gauges further implies that the feasible cones of atomic gauges do not depend on the scaling of a vector, in the sense that

for all ${\mathbf{x}} \in {\mathbb{R}}^{d}$ and any $\lambda > 0$.

### Remark 2.3

Definition 2.1. ‣ 2.1 Feasible cones ‣ 2 The geometry of demixing ‣ Sharp recovery bounds for convex demixing, with applications") is equivalent to the definition of the "tangent cone" appearing in \[15, Eq. \]. However, that definition differs slightly from the standard definition of a tangent cone; cf., \[66, Thm. 6.9\]. The cone of feasible directions \[62, p. 33\] is the closest relative of the feasible cone that we have identified in the literature, and this is the source of our terminology.

Figure 5: Geometry of demixing. [Left] Demixing succeeds: Every feasible perturbation about x0 (gray area) increases the objective function (green level lines). [Right] Demixing fails: Some feasible perturbations decrease the objective value. In each panel, the success or failure of the convex demixing method (1.2) is determined by a configuration of two cones. This fact forms the content of Lemma 2.4.

### A geometric characterization of optimality

The following lemma provides a geometric characterization for success in the convex demixing method (1.2) in terms of the configuration of two feasible cones. This is the main result of this section.

### Lemma 2.4

Program (1.2) succeeds at demixing $(\mathbf{x}_{0},\mathbf{y}_{0})$ if and only if ${{\mathcal{F}{(f,\mathbf{x}_{0})}{\bigcap\left( {- {\mathbf{Q}\mathcal{F}{(g,\mathbf{y}_{0})}}} \right)}} = {\{\mathbf{0}\}}}.$

In words, the demixing method (1.2) succeeds if and only if the two feasible cones are rotated so that they intersect trivially. Intuitively, we expect that many bases $\mathbf{Q}$ satisfy this condition when the two feasible cones are small. This observation provides further support for choosing atomic gauges as our complexity measures. We illustrate Lemma 2.4 in Figure 5.

The proof of Lemma 2.4 requires two technical propositions. The first is an alternative characterization of feasible cones.

### Proposition 2.5

Let $f$ be a convex function. Then ${\mathbf{δ}} \in {\mathcal{F}{(f,\mathbf{x})}}$ if and only if there is a number $\lambda_{0} > 0$ such that, for all $\lambda \in {\lbrack 0,\lambda_{0}\rbrack}$, we have ${f{({\mathbf{x} + {\lambda{\mathbf{δ}}}})}} \leq {f{(\mathbf{x})}}$.

### Proof

The "if" part is immediate: given any such $\lambda_{0}$, the assumption ${f{({{\mathbf{x}} + {\lambda_{0}{\mathbf{δ}}}})}} \leq {f{({\mathbf{x}})}}$ implies ${\mathbf{δ}} \in {\mathcal{F}{(f,{\mathbf{x}})}}$ by the definition of feasible cones. The other direction follows from convexity. Indeed, suppose ${\mathbf{δ}} \in {\mathcal{F}{(f,{\mathbf{x}})}}$, so that there exists a number $\lambda_{0} > 0$ for which ${f{({{\mathbf{x}} + {\lambda_{0}{\mathbf{δ}}}})}} \leq {f{({\mathbf{x}})}}$. By convexity, the map $\lambda\mapsto{f{({{\mathbf{x}} + {\lambda{\mathbf{δ}}}})}}$ lies below the chord connecting $0$ and $\lambda_{0}$, which is the claim. ∎

Our second technical proposition is a change of variables formula for the feasible cone under a nondegenerate affine transformation.

### Proposition 2.6

Let $g$ be any convex function, and define $h{(\mathbf{x})}: = g\left( \mathbf{A}^{- 1}{(\mathbf{z} - \mathbf{x})} \right)$ for some invertible matrix $\mathbf{A}$. Then ${{\mathcal{F}{(h,\mathbf{x})}} = {- {\mathbf{A}\mathcal{F}\left( g,{\mathbf{A}^{- 1}{({\mathbf{z} - \mathbf{x}})}} \right)}}}.$

The proof of Proposition 2.6 follows directly from the definition of a feasible cone. We omit the details.

### Proof of Lemma 2.4

Because $\mathbf{Q}$ is unitary, we may eliminate the variable $\mathbf{y}$ in (1.2) via the equality constraint ${\mathbf{y}} = {{\mathbf{Q}}^{\ast}{({{\mathbf{z}}_{0} - {\mathbf{x}}})}}$. Therefore, $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ is the unique optimum of (1.2) if and only if ${\mathbf{x}}_{0}$ is the unique optimum of

with decision variable $\mathbf{x}$. The equality in (2.1) follows from the definition ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$. The original claim thus reduces to the statement that ${\mathbf{x}}_{0}$ is the unique optimum of (2.1) if and only if ${{\mathcal{F}{(f,{\mathbf{x}}_{0})}} \cap \left( {- {{\mathbf{Q}}\mathcal{F}{(g,{\mathbf{y}}_{0})}}} \right)} = {\{\mathbf{0}\}}$. The rest of the proof is devoted to this claim.

$(\Leftarrow)$ Suppose ${{\mathcal{F}{(f,{\mathbf{x}}_{0})}} \cap \left( {- {{\mathbf{Q}}\mathcal{F}{(g,{\mathbf{y}}_{0})}}} \right)} = {\{\mathbf{0}\}}$. We show that ${\mathbf{x}}_{0}$ is the unique optimum of (2.1) by verifying that the strict inequality ${f{({\mathbf{x}})}} > {f{({\mathbf{x}}_{0})}}$ holds for any feasible point $\mathbf{x}$ of (2.1) with ${\mathbf{x}} \neq {\mathbf{x}}_{0}$.

To this end, assume $\mathbf{x}$ is feasible for (2.1) and ${\mathbf{x}} \neq {\mathbf{x}}_{0}$. Feasibility of $\mathbf{x}$ is equivalent to

By definition of the feasible cone and the transformation rule of Proposition 2.6, the inequality above implies

The final equality above follows from ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$.

Since ${\mathbf{x}} \neq {\mathbf{x}}_{0}$, the assumption ${{\mathcal{F}{(f,{\mathbf{x}}_{0})}} \cap \left( {- {{\mathbf{Q}}\mathcal{F}{(g,{\mathbf{y}}_{0})}}} \right)} = {\{\mathbf{0}\}}$ implies ${{\mathbf{x}} - {\mathbf{x}}_{0}} \notin {\mathcal{F}{(f,{\mathbf{x}}_{0})}}$. By the definition of feasible cones, we must have ${f{({\mathbf{x}})}} = {f\left( {{\mathbf{x}}_{0} + {({{\mathbf{x}} - {\mathbf{x}}_{0}})}} \right)} > {f{({\mathbf{x}}_{0})}}$. We have deduced ${f{({\mathbf{x}})}} > {f{({\mathbf{x}}_{0})}}$ for every feasible ${\mathbf{x}} \neq {\mathbf{x}}_{0}$, and so conclude that ${\mathbf{x}}_{0}$ is the unique optimum of (2.1).

$(\Rightarrow)$ Suppose ${\mathbf{x}}_{0}$ is the unique optimum of (2.1). Let $\mathbf{δ}$ be some vector in the intersection ${\mathcal{F}{(f,{\mathbf{x}}_{0})}} \cap \left( {- {{\mathbf{Q}}\mathcal{F}{(g,{\mathbf{y}}_{0})}}} \right)$. We must show ${\mathbf{δ}} = \mathbf{0}$.

As ${\mathbf{δ}} \in {\mathcal{F}{(f,{\mathbf{x}}_{0})}}$, Proposition 2.5 implies that ${f{({\mathbf{x}}_{0})}} \geq {f{({{\mathbf{x}}_{0} + {\lambda{\mathbf{δ}}}})}}$ for all sufficiently small $\lambda > 0$. Applying Proposition 2.5 to the fact ${- {{\mathbf{Q}}^{\ast}{\mathbf{δ}}}} \in {\mathcal{F}{(g,{\mathbf{y}}_{0})}}$ yields

for all sufficiently small $\lambda > 0$. We have used the relation ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$ again here. In summary, for some small enough $\lambda > 0$, the perturbed point ${\mathbf{x}}_{0} + {\lambda{\mathbf{δ}}}$ is feasible for (2.1), and its objective value is no larger than $f{({\mathbf{x}}_{0})}$. In other words, ${\mathbf{x}}_{0} + {\lambda{\mathbf{δ}}}$ is an optimal point of (2.1). But ${\mathbf{x}}_{0}$ is the unique optimal point of (2.1) by assumption, so we must have ${\mathbf{δ}} = \mathbf{0}$. This is the claim. ∎

## Background from integral geometry

By coupling the random basis model of Section 1.2.2 with the optimality condition of Lemma 2.4, the optimality condition for the demixing method (1.2) boils down to a geometric question: *When does a randomly oriented cone strike a fixed cone?*

This section provides a background in spherical integral geometry, a subfield of integral geometry that studies random configurations of cones and quantities related to these configurations \[69, Section 6.5\]. This theory provides an *exact* expression, called the spherical kinematic formula, for the probability that the convex demixing method (1.2) succeeds under our random model. Unfortunately, the quantities involved in the spherical kinematic formula are typically difficult to compute. To ease this burden, Section 3.3 defines geometric summary parameters that greatly simplify the application of the spherical kinematic formula.

We use subspaces and the nonnegative orthant as running examples to illustrate the concepts from integral geometry. These are not simply toy examples. A subspace plays an important role in the linear inverse problems in Section 5, while the orthant, which is congruent to the feasible cone of the $\ell_{\infty}$ norm at a sign vector, appears at several points in our examples in Section 6.

### Spherical intrinsic volumes

Figure 6: Spherical intrinsic volumes in ℝ2. A convex cone K ⊂ ℝ2 of solid angle θ has four faces: one 2-dimensional face (light blue), two 1-dimensional faces (heavy blue lines), and one 0-dimensional face (blue dot). The projection ΠK (w) of a Gaussian vector ω onto K lies in the 2-dimensional face when ω is in the blue region; a 1-dimensional face when ω is in the white region; and the 0-dimensional face when ω is in the red region. By Definition 3.1 of the spherical intrinsic volumes, we have v1 (K) = θ/(2 π), v0 (K) = 1/2, and v−1 (K) = (π−θ)/(2 π).

We begin our introduction to integral geometry with fundamental geometric parameters known as spherical intrinsic volumes. Spherical intrinsic volumes quantify geometric properties of convex cones such as the fraction of space a cone consumes (a type of volume), the fraction of space taken by the corresponding dual cone, and quantities akin to surface area. The following characterization \[3, Proposition 4.4.6\] is convenient.

### Definition 3.1 (Spherical intrinsic volumes)

Let $K \subset {\mathbb{R}}^{d}$ be a polyhedral convex cone, and define the Euclidean projection onto $K$ by

For $i = {{- 1},0,\ldots,{d - 1}}$, we define the $i$th *spherical intrinsic volume of $K$* by

where the vector $\mathbf{ω}$ is drawn from the standard Gaussian distribution on ${\mathbb{R}}^{d}$.

Although computing spherical intrinsic volumes is often challenging, a direct application of Definition 3.1. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") can bear fruit in some situations. In Figure 6, we demonstrate how to compute spherical intrinsic volumes for cones in ${\mathbb{R}}^{2}$. A subspace of ${\mathbb{R}}^{d}$ provides another simple example.

### Proposition 3.2 (Spherical intrinsic volumes of a subspace)

Suppose $L \subset {\mathbb{R}}^{d}$ is a linear subspace of dimension $n$. Then ${v_{i}{(L)}} = \delta_{i,{n - 1}}$, where $\delta_{i,j}$ is the Kronecker $\delta$ function.

### Proof

A subspace $L$ of dimension $n$ is a polyhedral cone with a single face, with dimension $n$. The projection of any point onto $L$ lies in the relative interior of this face. The claim follows immediately from Definition 3.1. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"). ∎

The computation of the spherical intrinsic volumes for the nonnegative orthant requires only some elementary probability theory. We illustrate the following result in Figure 7.

Figure 7: Spherical intrinsic volumes of the orthant. The spherical intrinsic volumes of the nonnegative orthant are given by scaled binomial coefficients (3.1). The scale on the horizontal axis is the normalized index θ = (i+1)/d.

### Proposition 3.3 (Spherical intrinsic volumes of the orthant \[3, Example 4.4.7\])

The spherical intrinsic volumes of the nonnegative orthant ${\mathbb{R}}_{+}^{d}$ are given by the binomial sequence

### Proof

The Euclidean projection onto the nonnegative orthant is given by the componentwise threshold operation

Therefore, the projection $\Pi_{{\mathbb{R}}_{+}^{d}}{({\mathbf{ω}})}$ lies in the relative interior of an $({i + 1})$-dimensional face of ${\mathbb{R}}_{+}^{d}$ if and only if $\mathbf{ω}$ has exactly $i + 1$ strictly positive values.

When $\mathbf{ω}$ is drawn from a standard Gaussian distribution, the number of positive entries is distributed as a binomial random variable. Hence, $\Pi_{{\mathbb{R}}_{+}^{d}}{({\mathbf{ω}})}$ lies in an $({i + 1})$-dimensional face of ${\mathbb{R}}_{+}^{d}$ with probability $2^{- d}\binom{d}{i + 1}$. This is precisely the definition of the $i$th spherical intrinsic volume $v_{i}{({\mathbb{R}}_{+}^{d})}$. ∎

### Remark 3.4 (Extension to nonpolyhedral cones)

The definition of spherical intrinsic volumes extends to all closed convex cones by approximation with polyhedral cones, but note that the probabilistic characterization above *does not hold* for nonpolyhedral cones. The technical details involve continuity properties of the spherical intrinsic volumes under the spherical Hausdorff metric. This theory is developed in,. See \[69, Ch. 6.5\] for a self-contained overview of spherical integral geometry developed via polyhedral approximation, or see \[3, Sec. 4\] for a development using tools from differential geometry.

### Key facts from integral geometry

We now collect some of the properties of spherical intrinsic volumes that are required for our development. We start with some elementary facts.

### Fact 3.5

Let $K \subset {\mathbb{R}}^{d}$ be a closed convex cone. Then

(Positivity) ${v_{i}{(K)}} \geq 0$ for each $i = {{- 1},0,\ldots,{d - 1}}$,

(Unit-sum) ${\sum_{i = {- 1}}^{d - 1}{v_{i}{(K)}}} = 1$, and

(Basis invariance) For any basis ${\mathbf{U}} \in \mathsf{O}^{d}$ and index $i = {{- 1},0,\ldots,{d - 1}}$, we have ${v_{i}{({{\mathbf{U}}K})}} = {v_{i}{(K)}}$.

### Proof sketch

First, assume $K$ is a polyhedral cone. The positivity of spherical intrinsic volumes follows from the positivity of probability. The unit-sum rule follows immediately from the fact that the projection $\Pi_{K}{({\mathbf{x}})}$ lies in the relative interior of a unique face of $K$. Finally, the basis invariance of spherical intrinsic volumes is immediate from the corresponding invariance of the Gaussian distribution. Continuity of the spherical intrinsic volumes under the spherical Hausdorff metric implies that these facts must hold for all closed convex cones by approximation with polyhedral cones. ∎

We conclude our background discussion with the following remarkable formula for the probability that a randomly oriented cone strikes a fixed cone. In view of Lemma 2.4, this result is fundamental to our understanding of the probability that the convex demixing method (1.2) succeeds under the random basis model.

### Fact 3.6 (Spherical kinematic formula \[69, p. 261\])

Let $K$ and $\overset{\sim}{K}$ be closed convex cones in ${\mathbb{R}}^{d}$, at least one of which is not a subspace, and let $\mathbf{Q}$ be a random basis. Then

### Remark 3.7

Fact 3.6. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") is usually stated for random rotations drawn according to the Haar measure on the special orthogonal group ${\mathsf{S}\mathsf{O}}_{d}$, but the unitary invariance given by Fact 3.5.3 readily implies that the spherical kinematic formula holds for $\mathbf{Q}$ drawn from the Haar measure on the orthogonal group $\mathsf{O}_{d}$.

### Remark 3.8

The spherical Gauss--Bonnet formula (Fact B.2. ‣ B.1 Regions of failure: The proof of Theorem 4.3 ‣ Appendix B Regions of failure and uniform guarantees ‣ Sharp recovery bounds for convex demixing, with applications") in Appendix B.1) can be used to eliminate the apparent asymmetry between $K$ and $\overset{\sim}{K}$ in (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")). In particular, the identity

holds for any convex cones $K$ and $\overset{\sim}{K}$.

### High-dimensional decay of spherical intrinsic volumes

The spherical kinematic formula (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")), coupled with the geometric optimality conditions of Lemma 2.4, provides an exact expression for the probability that the demixing problem (1.2) succeeds. Nevertheless, the formula involves the spherical intrinsic volumes of two cones, and it is challenging to determine these quantities directly from the definition except in simple situations.

To confront this challenge, we seek summary statistics for the intrinsic volumes as the dimension $d\rightarrow\infty$. We motivate our approach with the orthant. In Figure 7, we see that the spherical intrinsic volumes of the orthant $v_{i}{({\mathbb{R}}_{+}^{d})}$ decay rapidly as $d\rightarrow\infty$ when the index $i$ falls outside of the region $i \approx {d/2}$. The intrinsic volumes with indices $i$ far away from $d/2$ will contribute very little to the sum (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")) appearing in the kinematic formula. This observation simplifies the application of the kinematic formula when one of the cones is congruent to the orthant.

In general, we might hope that for some sequence of cones $K^{(d)} \in {\mathbb{R}}^{d}$, the spherical intrinsic volumes $v_{i}{(K^{(d)})}$ decay rapidly as $d\rightarrow\infty$ for indices $i$ outside of some interval $\lbrack{\kappa_{\star}d},{\theta_{\star}d}\rbrack$. We codify this behavior with *decay thresholds* that indicate which intrinsic volumes are very small as the ambient dimension $d$ grows.

### Definition 3.9 (Decay threshold)

Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices, and suppose $\{{K^{(d)}:d \in \mathcal{D}}\}$ is an ensemble of closed convex cones with $K^{(d)} \subset {\mathbb{R}}^{d}$ for each $d \in \mathcal{D}$. We say that $\theta_{\star} \in {\lbrack 0,1\rbrack}$ is an *upper decay threshold* for $\{ K^{(d)}\}$ if, for every $\theta > \theta_{\star}$, there exists an $\varepsilon > 0$ such that, for all sufficiently large $d \in \mathcal{D}$, we have

On the other hand, we say that $\kappa_{\star} \in {\lbrack 0,1\rbrack}$ is a *lower decay threshold* for $\{ K^{(d)}\}$ if, for every $\kappa < \kappa_{\star}$, there exists an $\varepsilon > 0$ such that, for all $d \in \mathcal{D}$ sufficiently large, we have

We extend these definitions to non-closed cones by taking the closure. We say $\theta_{\star}$ is an upper decay threshold for $\{ K^{(d)}\}$ if and only if it is an upper decay threshold for $\left\{ \overline{K}{}_{}^{(d)} \right.$. Similarly, $\kappa_{\star}$ is a lower decay threshold for $\{ K^{(d)}\}$ if and only if it is a lower decay threshold for $\left\{ \overline{K}{}_{}^{(d)} \right.$.

When it will not cause confusion, we omit the index set $\mathcal{D}$.

### Remark 3.10 (Nonuniqueness of decay thresholds)

The upper decay threshold $\theta_{\star}$ for an ensemble $\{ K^{(d)}\}$ defined above is not unique since any $\theta^{\prime} > \theta_{\star}$ is also a decay threshold for $\{ K^{(d)}\}$. An analogous comment holds for the lower decay threshold.

### Examples of decay thresholds

Since the intrinsic volumes are positive and sum to one (Fact 3.5), not every intrinsic volume is exponentially small in the ambient dimension $d$. In particular, the inequality $\kappa_{\star} \leq \theta_{\star}$ between lower and upper decay thresholds always holds. In practice, however, we can often find decay thresholds that satisfy the equality $\kappa_{\star} = \theta_{\star}$, as the following examples demonstrate.

### Proposition 3.11 (Upper decay threshold for subspaces)

Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices, and let $\{{L^{(d)}:d \in \mathcal{D}}\}$ be an ensemble of linear subspaces with $L^{(d)} \subset {\mathbb{R}}^{d}$ for each $d \in \mathcal{D}$. Suppose there exists a parameter $\sigma \in {\lbrack 0,1\rbrack}$ such that ${\dim{(L^{(d)})}} = {\lceil{\sigmad}\rceil}$. Then $\theta_{\star} = \sigma$ is an upper decay threshold for the ensemble $\{ L^{(d)}\}$, and $\kappa_{\star} = \sigma$ is a lower decay threshold for the ensemble $\{ L^{(d)}\}$.

### Proof

Let $n = n^{(d)} = {\dim{(L^{(d)})}}$. By Proposition 3.2. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), we have ${v_{i}{(L^{(d)})}} = \delta_{i,{n - 1}}$. Then for any $\theta > \sigma$, we have ${\lceil{\thetad}\rceil} > {\lceil{\sigmad}\rceil}$ for all large enough $d \in \mathcal{D}$, so that

for all $i \geq {\lceil{\thetad}\rceil}$ and $d$ sufficiently large. By definition, $\theta_{\star} = \sigma$ is an upper decay threshold for the ensemble of subspaces $\{{L^{(d)}:d \in \mathcal{D}}\}$. The demonstration that $\kappa_{\star} = \sigma$ is a lower decay threshold for $\{{L^{(d)}:d \in \mathcal{D}}\}$ follows in the same way. ∎

Figure 8: Normalized spherical intrinsic volumes of the orthant. The graph illustrates the computation in Proposition 3.12. The normalized spherical intrinsic volumes d−1 log (vi (ℝ+d)) appear against the normalized index θ = (i+1)/d for several values of dimension d. The solid curve is the uniform limit H (θ) − log of these rescaled volumes, where H (θ) is the bit entropy (3.6). The smallest possible upper decay threshold is the rightmost point where the solid curve crosses the zero level line (dotted), and the largest possible lower decay threshold is the leftmost point where the zero level line crosses the solid curve. The solid curve takes its unique maximum value of zero at $\theta = \frac{1}{2}$ so that $\theta_{\star} = \frac{1}{2}$ is an upper decay threshold and $\kappa_{\star} = \frac{1}{2}$ is a lower decay threshold for the ensemble {ℝd: d = 1, 2, …} of nonnegative orthants.

### Proposition 3.12 (Upper decay threshold for the nonnegative orthant)

Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite index set. The value $\theta_{\star} = \frac{1}{2}$ is an upper decay threshold for the ensemble $\{{{\mathbb{R}}_{+}^{d}:d \in \mathcal{D}}\}$ of nonnegative orthants, and $\kappa_{\star} = \frac{1}{2}$ is a lower decay threshold for $\{{{\mathbb{R}}_{+}^{d}:d \in \mathcal{D}}\}$.

### Proof

It is well known (see, e.g., \[25, Eq. (3.4)\]) that, for any $\theta \in {\lbrack 0,1\rbrack}$, we have

is the natural entropy; be aware that the logarithms are base-$e$ rather than the customary base-$2$ used in information theory. Basic calculus shows that $H{(\theta)}$ achieves its unique maximum at $\theta_{\star} = \frac{1}{2}$, where it has maximum value ${H\left( \frac{1}{2} \right)} = {\log{}}$.

Let $\theta > \frac{1}{2}$. By continuity of $H$, there is an $\varepsilon > 0$ such that ${H{(\overset{\sim}{\theta})}} < {{\log{}} - \varepsilon}$ for all $\overset{\sim}{\theta} \geq \theta > \theta_{\star}$. Continuity of the exponential and the uniform convergence in (3.5) together imply that, for all sufficiently large $d \in \mathcal{D}$, and any $i \geq {\lceil{\thetad}\rceil}$, we have

The left-hand side is equal to the spherical intrinsic volume $v_{i}{({\mathbb{R}}_{+}^{d})}$ by Proposition 3.3. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), so we see that $\theta_{\star} = \frac{1}{2}$ is an upper decay threshold for $\{{{\mathbb{R}}_{+}^{d}:d \in \mathcal{D}}\}$.

The proof that $\kappa_{\star} = \frac{1}{2}$ is a lower decay threshold for $\{{{\mathbb{R}}_{+}^{d}:d \in \mathcal{D}}\}$ follows along similar lines. Briefly, for any $\kappa < \frac{1}{2}$, there is an $\varepsilon > 0$ such that ${H{(\overset{\sim}{\kappa})}} < {{\log{}} - \varepsilon}$ for every $\overset{\sim}{\kappa} \leq \kappa$. For the same reasons as before, when $d$ is large enough, we have

for all $i \leq {\lceil{\kappad}\rceil}$. We conclude that $\kappa_{\star} = \frac{1}{2}$ is a lower decay threshold for the ensemble of nonnegative orthants $\{{{\mathbb{R}}_{+}^{d}:d \in \mathcal{D}}\}$. ∎

Figure 8 illustrates the computation above. We discuss other approaches for finding decay thresholds in Section 5. Table 1 summarizes the decay thresholds determined in this work.

Feasible cones of ℓ1 norm at τ-sparse vectors

(See Prop. C.3 in Appendix C)

Feasible cones of the Schatten 1-norm at n × n rank ⌈ρ n⌉ matrices

(See also Rem. 5.5.)

Feasible cones of the spectral norm at an orthogonal matrices

Table 1: Decay of intrinsic volumes. The decay thresholds developed in this work appear below. The computations for the orthant and subspace appear in Section 3.3.1, while the computations for the feasible cone of the Schatten 1-nrom and spectral norm appear in Section 5.2.1. Other computations appear where indicated.

## Success and failure

This section synthesizes the material from Sections 2 and 3 to determine whether the convex demixing method (1.2) succeeds, or fails, with high probability. Section 4.1 introduces the concept of a demixing ensemble. Our main results arrive in Section 4.2, where we find that the success and failure of the convex demixing method (1.2) are characterized by decay thresholds. Section 4.3 extends our methods to achieve uniform guarantees on the success of method (1.2).

### Ensembles of demixing problems

A demixing ensemble is a collection of demixing problems that is indexed by the ambient dimension of the observation. We explain this idea in the context of MCA, and we develop the abstract definition in Section 4.1.2.

### Example: The MCA demixing ensemble

Recall from Section 1.1 that MCA seeks to demix a superposition of two sparse vectors. Let us fix sparsity levels $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ in $\lbrack 0,1\rbrack$. For each pair $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$, we construct an ensemble of demixing problems with one problem per dimension. For each $d \in {\mathbb{N}}$, let ${\mathbf{x}}_{0}^{(d)}$ and ${\mathbf{y}}_{0}^{(d)}$ be vectors in ${\mathbb{R}}^{d}$ with

In other words, the sparsity of each vector is proportional to the ambient dimension. Draw a random basis ${\mathbf{Q}}^{(d)}$ from $\mathsf{O}_{d}$. We observe the vector ${\mathbf{z}}_{0}^{(d)} = {{\mathbf{x}}_{0}^{(d)} + {{\mathbf{Q}}^{(d)}{\mathbf{y}}_{0}^{(d)}}}$. To set up a convex demixing method, we need to introduce appropriate complexity measures for ${\mathbf{x}}_{0}^{(d)}$ and ${\mathbf{y}}_{0}^{(d)}$. For both vectors, the $\ell_{1}$ norm on ${\mathbb{R}}^{d}$ is the natural choice for inducing sparsity. Assume we have access to the side information $\alpha^{(d)} = \left\| {\mathbf{y}}_{0}^{(d)} \right\|_{\ell_{1}}$.

Together, these data define a demixing ensemble for MCA. We want to study when the MCA problem (1.2) succeeds with high probability for all members of the ensemble with $d$ sufficiently large.

### Abstract demixing ensembles

It is straightforward to extend this idea to other demixing problems. Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices. A *demixing ensemble* consists of one problem per index. For each $d \in \mathcal{D}$, the data are

Vectors ${{\mathbf{x}}_{0}^{(d)},{\mathbf{y}}_{0}^{(d)}} \in {\mathbb{R}}^{d}$,

A random basis ${\mathbf{Q}}^{(d)} \in \mathsf{O}_{d}$ that is statistically independent of the other ensemble data,

The observation ${{\mathbf{z}}_{0}^{(d)} = {{\mathbf{x}}_{0}^{(d)} + {{\mathbf{Q}}^{(d)}{\mathbf{y}}_{0}^{(d)}}} \in {\mathbb{R}}^{d}},$

Complexity measures $f^{(d)}$ and $g^{(d)}$ defined on ${\mathbb{R}}^{d}$, and

The side information $\alpha^{(d)} = {g^{(d)}{({\mathbf{y}}_{0}^{(d)})}}$.

Given such a demixing ensemble, we seek to determine conditions for which the convex demixing method

succeeds with high probability when the dimension $d$ is large. When it does not cause confusion, we omit the superscript $d$.

Our goal in this paper is to describe regions where the demixing program (4.1) succeeds, or fails, with high probability as the dimension $d\rightarrow\infty$. In order to avoid cumbersome repetition in our theorems, we make a shorthand definition.

### Definition 4.1 (Overwhelming probability in high dimensions)

Given a demixing ensemble as in Section 4.1.2, we say that (4.1) *succeeds with overwhelming probability in high dimensions* if there exists an $\varepsilon > 0$ such that, for every sufficiently large dimension $d \in \mathcal{D}$, program (4.1) succeeds with probability at least $1 - e^{- {\varepsilond}}$ over the randomness in ${\mathbf{Q}}^{(d)}$. Similarly, we say that (4.1) *fails with overwhelming probability in high dimensions* if there exists an $\varepsilon > 0$ such that, for every sufficiently large dimension $d \in \mathcal{D}$, program (4.1) succeeds with probability at most $e^{- {\varepsilond}}$.

Following common practice in asymptotic analysis, the definition above masks the dependence between the probability decay rate $\varepsilon$ and the "sufficiently large" dimension $d_{0}$. This approach represents a tradeoff. We will find that it provides demixing guarantees in terms of only decay thresholds, but it does not provide explicit probabilistic bounds for finite $d$. Nevertheless, our asymptotic analysis proves quite accurate at predicting the behavior in our experiments. See Remark 4.6. ‣ 4.2.3 Proof of Theorem 4.2 ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") for further discussion.

### The main results

We are now in a position to state our main results. The first result shows that the upper decay threshold provides guarantees for the success of demixing under the model of Section 4.1.

### Theorem 4.2 (Success of demixing)

Consider a demixing ensemble as in Section 4.1.2. Suppose the ensembles $\left\{ {{\mathcal{F}{(f^{(d)},\mathbf{x}_{0}^{(d)})}}:d \in \mathcal{D}} \right\}$ and $\left\{ {{\mathcal{F}{(g^{(d)},\mathbf{y}_{0}^{(d)})}}:d \in \mathcal{D}} \right\}$ of feasible cones have upper decay thresholds $\theta_{\mathbf{x}}$ and $\theta_{\mathbf{y}}$. If

then program (4.1) succeeds with overwhelming probability in high dimensions.

The proof of this result appears in Section 4.2.3. This next result shows that the failure of demixing is characterized by the lower decay threshold.

### Theorem 4.3 (Failure of demixing)

Consider a demixing ensemble as in Section 4.1.2. Suppose the ensembles $\left\{ {{\mathcal{F}{(f^{(d)},\mathbf{x}_{0}^{(d)})}}:d \in \mathcal{D}} \right\}$ and $\left\{ {{\mathcal{F}{(g^{(d)},\mathbf{y}_{0}^{(d)})}}:d \in \mathcal{D}} \right\}$ of feasible cones have lower decay thresholds $\kappa_{\mathbf{x}}$ and $\kappa_{\mathbf{y}}$. If

then program (4.1) fails with overwhelming probability in high dimensions.

The proof of this second result is similar in spirit to the proof of Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), but it requires additional technical finesse; we defer the details to Appendix B.1.

### Consequences for the choice of complexity functions

The complementary nature of Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") has striking implications. The success, or failure, of the convex demixing method (4.1) in high dimensions depends only on the sum of the decay thresholds. As a consequence, the upper and lower decay thresholds assess the quality of the complexity measures $f^{(d)}$ and $g^{(d)}$ in high dimensions.

Since the decay thresholds are independent of any interrelationship between the structured vectors ${\mathbf{x}}_{0}^{(d)}$ and ${\mathbf{y}}_{0}^{(d)}$ in the superimposed observation ${\mathbf{z}}_{0}^{(d)}$, the quality of the complexity measure $f^{(d)}$ is independent of the choice $g^{(d)}$. This explains, for instance, the ubiquity of the use of the $\ell_{1}$ norm for inducing sparsity and the Schatten 1-norm as a complexity measure for rank. Simply put, when a complexity measure is good for one incoherent demixing problem, it is good for another.

### Sharp phase transitions

Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") have an important consequence for phase transitions in the convex demixing method (4.1). Equality between the lower and upper decay thresholds holds in cases where we have access to exact formulas for the spherical intrinsic volumes. Proposition 3.11. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") shows that the upper and lower decay thresholds are equal for subspaces whose dimension is proportional to the ambient space, and Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") implies that the upper decay threshold is equal to the lower decay threshold for the ensemble of nonnegative orthants. Moreover, our computations in Appendix C suggest that equality between the upper and lower decay thresholds also holds for the ensemble of feasible cones of the $\ell_{1}$ norm at vectors with a fixed proportion of nonzero elements.

The equality of the upper and lower decay thresholds explains the close agreement between our theoretical bounds and the empirical experiments. For instance, consider Figure 1. For sparsity levels below the green curve, the sum of the upper decay thresholds is less than one, so Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that demixing succeeds with overwhelming probability in high dimensions. On the other hand, with sparsity levels above the green curve, the sum of the lower decay thresholds exceeds one, so demixing fails with overwhelming probability in high dimensions by Theorem 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"). (See Section 6.1 for the details of this calculation.)

One may wonder whether the transition between success and failure is sharp in general. In work undertaken after the submission of this article, with collaborators, we have determined that the answer to this question is *yes* for a large class of demixing ensembles. In essence, the result \[5, Thm. 6.1\] indicates that the upper- and lower-decay thresholds for a sufficiently regular ensemble $\{{K^{(d)}:d \in \mathcal{D}}\}$ are equal. For example, the fact that ${d^{- 1}W{({K^{(d)} \cap \mathsf{S}^{d - 1}})}^{2}}\rightarrow\rho \in {}$ as $d\rightarrow\infty$ is sufficient to guarantee that the upper- and lower-decay thresholds $\theta_{\star}$ and $\kappa_{\star}$ of the ensemble $\{{K^{(d)}:d \in \mathcal{D}}\}$ satisfy $\theta_{\star} = \kappa_{\star} = \rho$. (The function $W$ is the Gaussian width defined in Section 5.2.1.) We refer the reader to this newer work for details.

### Proof of Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications")

The proof of Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") follows readily from a geometric statement concerning the probability that a random cone strikes a fixed cone as the dimension $d$ becomes large.

### Theorem 4.4

Suppose $\mathcal{D}$ is an infinite set of indices, and let $\{{K^{(d)} \subset {\mathbb{R}}^{d}:d \in \mathcal{D}}\}$ and $\{{{\overset{\sim}{K}}^{(d)} \subset {\mathbb{R}}^{d}:d \in \mathcal{D}}\}$ be two ensembles of closed convex cones with upper decay thresholds $\theta_{\star}$ and ${\overset{\sim}{\theta}}_{\star}$. If ${\theta_{\star} + {\overset{\sim}{\theta}}_{\star}} < 1$, then there exists an $\varepsilon > 0$ such that, for all sufficiently large $d$, we have ${{\mathbb{P}}\left\{ {{K^{(d)} \cap {\mathbf{Q}{\overset{\sim}{K}}^{(d)}}} \neq {\{\mathbf{0}\}}} \right\}} \leq e^{- {\varepsilond}}$.

Before proceeding to the proof, let us explain how Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") follows from Theorem 4.4 and the geometric optimality conditions of Lemma 2.4.

### Proof of Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") from Theorem 4.4

By the assumptions in Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), the ensembles $\left\{ {{\overline{\mathcal{F}}{(f^{(d)},{\mathbf{x}}_{0}^{(d)})}}:d \in \mathcal{D}} \right\}$ and $\left\{ {{- {\overline{\mathcal{F}}{(g^{(d)},{\mathbf{y}}_{0}^{(d)})}}}:d \in \mathcal{D}} \right\}$ of closed cones satisfy the hypothesis of Theorem 4.4. Thus, there is an $\varepsilon > 0$ for which

except with probability $e^{- {\varepsilond}}$, for all sufficiently large $d$.

Since cones are contained in their closure, the two feasible cones have a trivial intersection at least as frequently as their closures (but see the remark below). Applying our geometric optimality condition, Lemma 2.4, immediately implies that (4.1) succeeds with probability at least $1 - e^{- {\varepsilond}}$ for every sufficiently large $d$. ∎

### Remark 4.5

In fact, the probability that randomly oriented convex cones strike is *equal* to the probability that their closures strike. This seemingly innocuous claim appears to have no simple proof from first principles. However, this fact readily follows from the discussion of touching probabilities in \[69, pp. 258--259\].

Figure 9 illustrates the main idea behind the following proof.

Figure 9: Main idea behind the proof of Theorem 4.4. When the spherical intrinsic volumes are very small for large i, the product of the outer (top) and inner (bottom) terms in equation (4.2) is always small. In the left panel, the large value of vi (K) is offset by the small inner sum $\sum_{k = {d - i - 1}}{v_{k}{(\overset{\sim}{K})}}$. On the right, the small value of vi (K) counteracts the large sum $\sum_{k = {d - i - 1}}{v_{k}{(\overset{\sim}{K})}}$. This situation always occurs when the upper decay thresholds satisfy ${\theta_{\star} + {\overset{\sim}{\theta}}_{\star}} &lt; 1$ and the ambient dimension d is large.

### Proof of Theorem 4.4

The spherical kinematic formula (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")) only applies when at least one cone is not a subspace, so we split the demonstration into two cases. First, we assume that at least one of the ensembles $\{ K^{(d)}\}$ or $\{{\overset{\sim}{K}}^{(d)}\}$ of cones does not contain any subspace. Then, we consider the case where both ensembles of cones contain only subspaces. The argument readily extends to the general case by considering subsequences where one of the two cases above holds. Throughout the proof, we drop the explicit dependence of $K^{(d)}$ and ${\overset{\sim}{K}}^{(d)}$ on the dimension $d$ for notational clarity.

We start with the first case: assume that either $K$ or $\overset{\sim}{K}$ is not a subspace. Our main tool is the spherical kinematic formula, Fact 3.6. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"). The positivity of the spherical intrinsic volumes and the bound ${({1 + {({- 1})}^{k}})} \leq 2$ imply that the probability $P$ of interest satisfies

The equality follows by a change in the order of summation and a change of the summation index. Since ${\theta_{\star} + {\overset{\sim}{\theta}}_{\star}} < 1$, there exist parameters $\theta > \theta_{\star}$ and $\overset{\sim}{\theta} > {\overset{\sim}{\theta}}_{\star}$ for which ${\theta + \overset{\sim}{\theta}} < 1$. We expand the right-hand sum of (4.2) into four terms, say $\Sigma_{1}$, $\Sigma_{2}$, $\Sigma_{3}$, and $\Sigma_{4}$:

We bound each summand separately. First, the fact ${\theta + \overset{\sim}{\theta}} < 1$ implies that, for all sufficiently large $d$, we have ${{\lceil{\thetad}\rceil} + {\lceil{\overset{\sim}{\theta}d}\rceil}} < {d - 1}$. We conclude that $\Sigma_{1} = 0$ when $d$ is large enough: The inner sum is empty.

To bound $\Sigma_{2}$, apply Facts 3.5.1 and 3.5.2 to the inner sum to find

where the second inequality holds for some $\varepsilon^{\prime} > 0$ and all sufficiently large $d$ owing to the definition of the upper decay threshold $\theta_{\star}$. Through analogous reasoning, the definition of ${\overset{\sim}{\theta}}_{\star}$ gives the exponential bounds

for some ${\varepsilon^{\operatorname{\prime\prime}},\varepsilon^{\operatorname{\prime\prime\prime}}} > 0$ and all sufficiently large $d$. Taking $\varepsilon$ sufficiently small (say $\varepsilon = {\frac{1}{2}{\min{\{\varepsilon^{\prime},\varepsilon^{\operatorname{\prime\prime}},\varepsilon^{\operatorname{\prime\prime\prime}}\}}}}$) and $d$ sufficiently large gives the result for the first case.

For the second case, suppose that both $K$ and $\overset{\sim}{K}$ are subspaces. Set $n: = \dim{(K)}$ and $\overset{\sim}{n}: = \dim{(\overset{\sim}{K})}$. Choose parameters $\theta > \theta_{\star}$ and $\overset{\sim}{\theta} > {\overset{\sim}{\theta}}_{\star}$ such that ${\theta + \overset{\sim}{\theta}} < 1$. The definition of the upper decay threshold and Proposition 3.2. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") imply that

for some $\varepsilon^{\prime} > 0$, all sufficiently large $d$, and every $i \geq {\lceil{\thetad}\rceil}$. In particular, this inequality implies ${n - 1} < {\lceil{\thetad}\rceil}$ for all $d$ large enough. Similarly, we find ${\overset{\sim}{n} - 1} < {\lceil{\overset{\sim}{\theta}d}\rceil}$ for all $d$ sufficiently large.

Since ${\theta + \overset{\sim}{\theta}} < 1$, we have

whenever $d$ is large enough. That is, the sum of the dimensions of the subspaces is less than the ambient dimension. Since two randomly oriented subspaces are almost surely in general position, we see that ${K \cap {{\mathbf{Q}}\overset{\sim}{K}}} = {\{\mathbf{0}\}}$ with probability one, whenever $d$ is large enough. This completes the second case, so we are done. ∎

### Remark 4.6 (Explicit dimensional dependence)

The methods above can provide explicit dependence between the sum of the decay thresholds $\theta_{x} + \theta_{y}$, the "sufficiently large" dimension and the probability decay rate $\varepsilon$ when detailed information about the intrinsic volumes is available. In the case of the orthant, for example, Stirling's formula with remainder \[59, Sec. 5.6.1\] may provide enough information. For the descent cones of the $\ell_{1}$ norm, it may be possible to achieve such explicit dependence using the approach of.

### Uniform demixing guarantees

Suppose that $\mathbf{Q}$ is drawn at random and fixed. For example, in the MCA problem from Section 1.1, we may observe a number of different images, but the structures that we expect to find (encoded by $\mathbf{Q}$) are the same in each image. In this case, we ask whether (1.1) demix *every* sparse pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ from the associated observation ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$, and thus successfully identify the structures in a large family of images.

More generally, we can study the probability that the generic demixing program (1.2) will demix every structured pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ with a random---but fixed---basis $\mathbf{Q}$. (These uniform guarantees go by the name of *strong bounds*.) By the geometric optimality condition of Lemma 2.4, this probability is equal to the probability of the event

In this section, we control the probability of (4.4) by coupling the argument leading to Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") with a union bound. This approach does not necessarily limit our methods to a finite number of structured pairs $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$, however. In the case of a sparse vectors, for example, the set of feasible cones

consists of $\binom{d}{k}2^{k}$ cones because the feasible cone $\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{x}}) \right.$ depends only on the sparsity and sign pattern, and not the magnitude, of the elements of $\mathbf{x}$. (See Section 6.1.1 for more details.) Thus, even the simple union bound can offer insight into the behavior of constrained MCA (1.1) for an *infinite* family of images.

Applying a union bound to a finite, but rather large, set of cones such as (4.5) requires stronger probabilistic information than provided by the decay thresholds. Therefore, we define an extension of the upper decay threshold that provides detailed information on the rate of decay of spherical intrinsic volumes.

### Definition 4.7 (Decay at level $\psi$)

Let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices, let $\{{K^{(d)}:d \in \mathcal{D}}\}$ be an ensemble of closed convex cones with $K^{(d)} \in {\mathbb{R}}^{d}$, and suppose $\psi \geq 0$. We say that $\theta_{\star}$ is an upper decay threshold *at level $\psi$* for the ensemble $\{ K^{(d)}\}$ if, for every $\theta > \theta_{\star}$, there exists an $\varepsilon > 0$ such that, for all sufficiently large $d$, the inequality

holds for all $i \geq {\lceil{\thetad}\rceil}$. When no level is specified, we take $\psi = 0$ for compatibility with Definition 3.9. ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"). As in Definition 3.9. ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), this definition extends to non-closed cones by taking the closure.

Subspaces and orthants again provide useful examples.

### Proposition 4.8 (Decay at level $\psi$ for an ensemble of subspaces)

Let $\{ L^{(d)}\}$ be an infinite ensemble of linear subspaces with $L^{(d)} \subset {\mathbb{R}}^{d}$ and ${\dim{(L^{(d)})}} = {\lceil{\sigmad}\rceil}$, and suppose $\psi \geq 0$. Then $\theta_{\star} = \sigma$ is an upper decay threshold for $\{ L^{(d)}\}$ at level $\psi$.

### Proof

The proof is substantially similar to the proof of Proposition 3.11. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"). Let $n = {\dim{(L^{(d)})}}$, so that ${v_{i}{(L^{(d)})}} = \delta_{i,{n - 1}}$ by Proposition 3.2. ‣ 3.1 Spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"). For any $\theta > \sigma$, we have ${\lceil{\thetad}\rceil} > {\lceil{\sigmad}\rceil}$ for all large enough $d$. Therefore,

for all $i \geq {\lceil{\thetad}\rceil}$ and $d$ sufficiently large. By definition, $\theta_{\star} = \sigma$ is an upper decay threshold at level $\psi$ for $\{ L^{(d)}\}$. ∎

Figure 10: Computation of decay thresholds for the orthant. The solid curve is the limiting behavior of the spherical intrinsic volumes of the orthant ℝ+d from Figure 8. The rightmost point where the horizontal line at level − ψ crosses this curve is an upper decay threshold at level ψ. From the diagram, we see that $\theta_{\star} = \frac{1}{2}$ is an upper decay threshold at level zero, while θ⋆ ≈ 0.72 is an upper decay threshold at level ψ = 0.1.

The computation for the orthant is only slightly more involved. The following result is illustrated in Figure 10.

### Proposition 4.9 (Decay at level $\psi$ for $\{{\mathbb{R}}_{+}^{d}\}$)

Suppose $0 \leq \psi \leq {\log{}}$, and let $\mathcal{D} \subset {\mathbb{N}}$ be an infinite set of indices. Define

where $H{(\theta)}$ is the entropy defined in (3.6). Then $\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}$ is an upper decay threshold at level $\psi$ for the ensemble $\{{\mathbb{R}}_{+}^{d}\}$ of orthants.

### Proof sketch

Let $\theta > {\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}}$. As in the proof of Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), there exists an $\varepsilon > 0$, such that, for all $d$ sufficiently large, we have

for every $i \geq {\lceil{\thetad}\rceil}$. By definition, $\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}$ is an upper decay threshold at level $\psi$ for the ensemble $\{{\mathbb{R}}_{+}^{d}\}$. ∎

We now extend the decay threshold to cover the family of cones considered in condition (4.4). In our applications, the feasible cones appearing in (4.4) are congruent, so we restrict our attention to this case.

### Definition 4.10 (Decay threshold for an ensemble of sets of cones)

For an infinite set of indices $\mathcal{D} \subset {\mathbb{N}}$, let $\{{\mathcal{K}^{(d)}:d \in \mathcal{D}}\}$ be an ensemble of *sets* of congruent cones, indexed by the ambient dimension, and let $\{ K^{(d)}\}$ be an ensemble of exemplars, that is, $K^{(d)} \in \mathcal{K}^{(d)}$ for every $d \in \mathcal{D}$. We say that $\{\mathcal{K}^{(d)}\}$ has upper decay threshold $\theta$ at level $\psi$ if the sequence of exemplars $\{ K^{(d)}\}$ has upper decay threshold $\theta$ at level $\psi$.

By Fact 3.5.3, the decay threshold for an ensemble $\{\mathcal{K}^{(d)}\}$ of sets of congruent cones is independent of the choice of exemplars, so this nomenclature is well defined. We now state an analog to Theorem 4.4 that bounds the probability that a number of cones strike, provided there are not too many cones.

### Theorem 4.11

Let $\{\mathcal{K}^{(d)}\}$ and $\{{\overset{\sim}{\mathcal{K}}}^{(d)}\}$ be two ensembles of sets of congruent closed convex cones, indexed by ambient dimension $d$. Suppose the cardinality of $\mathcal{K}^{(d)}$ and ${\overset{\sim}{\mathcal{K}}}^{(d)}$ grows no faster than exponentially: there exist $\psi,\overset{\sim}{\psi}$ such that, for every $\eta > 0$ and all $d$ sufficiently large, we have the inequalities ${|\mathcal{K}^{(d)}|} \leq e^{d{({\psi + \eta})}}$, and ${|{\overset{\sim}{\mathcal{K}}}^{(d)}|} \leq e^{d{({\overset{\sim}{\psi} + \eta})}}$. Suppose further $\{\mathcal{K}^{(d)}\}$ and $\{{\overset{\sim}{\mathcal{K}}}^{(d)}\}$ have respective upper decay thresholds $\theta_{\star}$ and ${\overset{\sim}{\theta}}_{\star}$, each at level $\psi + \overset{\sim}{\psi}$.

If ${\theta_{\star} + {\overset{\sim}{\theta}}_{\star}} < 1$, then there exists an $\varepsilon > 0$ such that for every sufficiently large $d$,

where the probability is taken over the random basis $\mathbf{Q} \in \mathsf{O}_{d}$.

The proof of Theorem 4.11 simply couples a union bound to the proof of Theorem 4.4, so we defer the demonstration to Appendix B.2. Note that the statement of Theorem 4.11 is equivalent to that of Theorem 4.4 when $\mathcal{K}^{(d)}$ and ${\overset{\sim}{\mathcal{K}}}^{(d)}$ are singletons, because we may take $\psi = \overset{\sim}{\psi} = 0$ in this case.

Theorem 4.11 can be used to verify that event (4.4) holds with high probability when the dimension $d$ becomes large. In Section 6.1.1, we use this approach to verify that the MCA formulation (1.1) can demix all sufficiently sparse vectors, and in Section 6.2.2, we use Theorem 4.11 to show that the channel coding method (1.4) is robust to adversarial sparse corruptions.

## Computing decay thresholds

Section 4.2 demonstrates that the decay thresholds provide a simple way to analyze demixing under the random basis model. This section describes several methods for computing decay thresholds. We begin by considering direct approaches, where precise formulas for the spherical intrinsic volumes give correspondingly precise thresholds.

The direct method is powerful, but its application is limited to regimes where we have access to formulas for spherical intrinsic volumes. In Section 5.2, we observe that known results on linear inverse problems imply bounds on decay thresholds. This observation allows us to study upper decay thresholds for several structural classes, including low-rank matrices.

### Direct approach

There are several situations where the direct approach for calculating decay thresholds is feasible. Propositions 3.11. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") and 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") compute upper and lower decay thresholds for ensembles of subspaces and orthants directly from the definition of spherical intrinsic volumes. In Appendix C, we use the asymptotic polytope angle computations of to compute the decay threshold for ensembles of feasible cones of the $\ell_{1}$ norm at sparse vectors. The approach follows roughly the same lines as Propositions 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") and 4.9. ‣ 4.3 Uniform demixing guarantees ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), but the argument requires a good deal of background information that is tangential to this work.

### Relationship to linear inverse problems

There is a useful link between the number of random linear measurements required to identify a structured signal with a convex complexity measure and the upper decay threshold of the associated feasible cone. Roughly speaking, the upper decay threshold is the ratio between the number of linear measurements required to identify a structured signal and the ambient dimension. This observation provides a powerful method for determining decay thresholds.

Linear inverse problems are closely related to demixing problems. Suppose we observe the linear image ${\mathbf{z}}_{0} = {{\mathbf{A}}{\mathbf{x}}_{0}}$, where $\mathbf{A}$ is a known matrix and ${\mathbf{x}}_{0}$ is a structured vector. Given an associated convex complexity measure $f$, Chandrasekaran et al. study the convex optimization program

These authors consider the question "Given the data ${\mathbf{z}}_{0} = {{\mathbf{A}}{\mathbf{x}}_{0}}$, when is ${\mathbf{x}}_{0}$ the unique optimal point of (5.1)?" The answer to this question is closely related to our demixing problem.

To place the linear inverse problem in our asymptotic framework, we consider an ensemble of problems indexed by the ambient dimension $d$. Fix an undersampling parameter $\sigma \in {\lbrack 0,1\rbrack}$. For each $d$ in some infinite set $\mathcal{D} \subset {\mathbb{N}}$ of indices, assume we are given a structured vector ${\mathbf{x}}_{0}^{(d)} \in {\mathbb{R}}^{d}$, a Gaussian measurement matrix $\mathbf{\Omega}^{(d)} \in {\mathbb{R}}^{{\lceil{\sigmad}\rceil} \times d}$, the observation ${\mathbf{z}}_{0}^{(d)} = {\mathbf{\Omega}^{(d)}{\mathbf{x}}_{0}^{(d)}} \in {\mathbb{R}}^{d}$, and a complexity measure $f^{(d)}$ associated with the structure of ${\mathbf{x}}_{0}^{(d)}$. We attempt to identify ${\mathbf{x}}_{0}^{(d)}$ by solving the optimization problem

with decision variable ${\mathbf{x}} \in {\mathbb{R}}^{d}$. This method succeeds when ${\mathbf{x}}_{0}^{(d)}$ is the unique optimal point of (5.2). The following result shows that the problem of computing the number of random linear measurements needed to identify a structured vector is equivalent to determining an upper decay threshold.

### Lemma 5.1

Consider the ensemble described above.

Suppose the ensemble $\left\{ {\mathcal{F}{(f^{(d)},{\mathbf{x}}_{0}^{(d)})}} \right\}$ of feasible cones has an upper decay threshold $\theta_{\star} < \sigma$. Then (5.2) succeeds with overwhelming probability in high dimensions.

On the other hand, suppose the linear inverse program (5.2) succeeds with overwhelming probability in high dimensions. Then the ensemble $\left\{ {\mathcal{F}{(f^{(d)},{\mathbf{x}}_{0}^{(d)})}} \right\}$ of feasible cones has an upper decay threshold $\theta_{\star} = \sigma$.

The proof of Lemma 5.1 appears in Appendix D, but we sketch the main ideas here. The program (5.1) identifies ${\mathbf{x}}_{0}$ precisely when the null space of $\mathbf{A}$ intersects the feasible cone $\mathcal{F}{(f,{\mathbf{x}}_{0})}$ trivially \[15, Prop. 2.1\]. When ${\mathbf{A}} = \mathbf{\Omega}$ is a Gaussian matrix, its null space is a randomly oriented subspace. Combining this fact with the kinematic formula (3.2. ‣ 3.2 Key facts from integral geometry ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications")) lets us compute the decay threshold using the number of observations required to recover a vector with (5.1) under a Gaussian measurement model.

In Appendix C.3, we describe how our computation of the upper decay threshold for the feasible cone of the $\ell_{1}$ norm at sparse vectors relates to the recovery guarantees for basis pursuit explored in the series of papers. Our approach also yields a sharp transition between success and failure regimes for basis pursuit. See Appendix C.3.2 for the details.

### Remark 5.2

A counterpart to Lemma 5.1 that links the failure of linear inverse problems to the lower decay threshold $\kappa_{\star}$ is readily derivable with the techniques used in this work. This may enable the computation of lower decay thresholds through information-theoretic arguments.

### The upper decay threshold from the Gaussian width

Lemma 5.1 provides a powerful tool for computing upper decay thresholds. Define the *Gaussian width* of a cone $K \subset {\mathbb{R}}^{d}$ by the expression

where the random vector $\mathbf{ω}$ is drawn from the Gaussian distribution on ${\mathbb{R}}^{d}$. The following corollary lets us determine upper decay thresholds from Gaussian width bounds. As usual, $\mathcal{D}$ is an infinite subset of the natural numbers.

### Corollary 5.3

Consider an ensemble $\left\{ {{\mathcal{F}{(f^{(d)},\mathbf{x}_{0}^{(d)})}} \subset {\mathbb{R}}^{d}:d \in \mathcal{D}} \right\}$ of feasible cones. Suppose that

Then $\theta_{\star}$ is an upper decay threshold (at level zero) for $\left\{ {\mathcal{F}{(f^{(d)},\mathbf{x}_{0}^{(d)})}} \right\}$.

The proof relies the result \[15, Cor. 3.3\], which asserts that the linear inverse problem (5.2) succeeds with high probability when the number of measurements $n^{(d)} \gtrsim {W\left( {{\mathcal{F}{(f^{(d)},{\mathbf{x}}_{0}^{(d)})}} \cap \mathsf{S}^{d - 1}} \right)^{2}}$. Since $\lceil{\theta_{\star}d}\rceil$ exceeds the width for large $d$ by assumption (5.3), taking $n^{(d)} = {\lceil{\theta_{\star}d}\rceil}$ results in high-probability success in (5.2). Corollary 5.3 then follows from the second part of Lemma 5.1. The details appear at the end of Appendix D.

This machinery allows us to compute upper decay thresholds in situations involving matrix observations. For simplicity, we consider only the space ${\mathbb{R}}^{n \times n}$ of square $n \times n$ matrices, where $n \in {\mathbb{N}}$. The ambient dimension of this vector space is $d = n^{2}$, but we will index the observations by the parameter $n$. This poses no difficulty, because it is equivalent to indexing over the set $\mathcal{D} = {\{ 1^{2},2^{2},3^{2},\ldots\}}$.

### Proposition 5.4

Fix $\rho \in {\lbrack 0,1\rbrack}$. For each $n \in {\mathbb{N}}$, let $\mathbf{X}_{0}^{(n)} \in {\mathbb{R}}^{n \times n}$ be a matrix with ${{rank}{(\mathbf{X}_{0}^{(n)})}} = {\lceil{\rhon}\rceil}$. Then the corresponding ensemble $\left\{ \mathcal{F}\left. (\parallel \cdot \parallel{}_{S_{1}},\mathbf{X}_{0}^{(n)}) \right. \right\}$ of feasible cones has upper decay threshold $\theta_{\star} = {{6\rho} - {3\rho^{2}}}$.

### Proof

Let $r = r^{(n)} = {{rank}{({\mathbf{X}}_{0}^{(n)})}}$. From \[15, Prop. 3.11\], we have

Dividing both sides by the ambient dimension $n^{2}$ and taking limits, we see that the conditions of Corollary 5.3 hold. This gives the result. ∎

### Remark 5.5

An asymptotically sharp upper bound for the Gaussian width in (5.4) is given by the solution to an implicit equation in \[60, Eq. \]. We use this asymptotically precise formula for computing the location of the green curve in Figure 4. See Section 6.3 for more details.

### Proposition 5.6

For each $n \in {\mathbb{N}}$, let $\mathbf{X}_{0}^{(n)}$ be an orthogonal matrix. Then the corresponding ensemble $\left\{ \mathcal{F}\left. (\parallel \cdot \parallel{}_{Op},\mathbf{X}_{0}^{(n)}) \right. \right\}$ of feasible cones has upper decay threshold $\theta_{\star} = \frac{3}{4}$.

### Proof

From \[15, Prop. 3.13\], we have

The result follows upon dividing by $n^{2}$, taking limits, and applying Corollary 5.3. ∎

We list all of the bounds computed in our work in Table 1 on page 1, but note that several more bounds are readily derivable from the Gaussian width calculations in \[15, Sec. 3.4\].

## Experiments

We can tackle a variety of scenarios using the theory developed in Section 4 and the decay threshold calculations of Section 5.

### Morphological component analysis

Figure 11: Decay threshold for the ℓ1 norm. The left panel shows θℓ1 (τ), the upper decay threshold for the sequence of feasible cones of the ℓ1 norm at ⌈τ d⌉-sparse vectors as a function of the sparsity τ. The narrow lines show that ${\theta_{\ell_{1}}{(\tau)}} &lt; \frac{1}{2}$ for τ &lt; 0.19, while ${\theta_{\ell_{1}}{(\tau)}} &lt; \frac{1}{4}$ for τ &lt; 0.06. The right panel displays level sets of the function θℓ1 (τx) + θℓ1 (τy). The thick curve marks the level set θℓ1 (τx) + θℓ1 (τy) = 1; it corresponds to the green curve in Figure 1.

We return to the MCA model of Section 1.1. Our goal is to analyze when we can demix two signals that are sparse in incoherent bases. To apply our theoretical results, we consider the demixing ensemble from Section 4.1.1.

Fix sparsity levels $\tau_{\mathbf{x}}$ and $\tau_{\mathbf{y}}$ in $\lbrack 0,1\rbrack$. For each dimension $d \in {\mathbb{N}}$, we construct signals ${\mathbf{x}}_{0}$ and ${\mathbf{y}}_{0}$ in ${\mathbb{R}}^{d}$ that satisfy

Draw a random basis $\mathbf{Q}$, and suppose that we observe ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$.

The $\ell_{1}$ norm is a natural complexity measure for sparse vectors. Given the side information $\alpha = \left\| {\mathbf{y}}_{0} \right\|_{\ell_{1}}$, we pose the constrained MCA problem

The theory of Section 4 describes when (6.1) identifies $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ with overwhelming probability in high dimensions in terms of decay thresholds for the ensembles $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{x}}_{0}) \right.\}$ and $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{y}}_{0}) \right.\}$ indexed by the dimension $d$.

Observe that, up to rotations, the geometry of the feasible cone $\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{w}}) \right.$ depends only on the number of nonzero entries in $\mathbf{w}$, but not on the positions or magnitudes of the entries. For a fixed sparsity level $\tau \in {\lbrack 0,1\rbrack}$, consider an ensemble $\{{\mathbf{w}}^{(d)}\}$ with ${\mathbf{w}}^{(d)} \in {\mathbb{R}}^{d}$ and ${{nnz}{({\mathbf{w}}^{(d)})}} = {\lceil{\taud}\rceil}$ for each $d \in {\mathbb{N}}$. In Appendix C, we compute the optimal upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{w}}^{(d)}) \right.\}$. We denote this value by $\theta_{\ell_{1}}{(\tau)}$ (see Figure 11, left panel). Therefore, the ensembles $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{x}}_{0}) \right.\}$ and $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{y}}_{0}) \right.\}$ have decay thresholds $\theta_{\ell_{1}}{(\tau_{\mathbf{x}})}$ and $\theta_{\ell_{1}}{(\tau_{\mathbf{y}})}$.

Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that our demixing method (6.1) for sparse vectors succeeds with overwhelming probability in high dimensions so long as ${{\theta_{\ell_{1}}{(\tau_{\mathbf{x}})}} + {\theta_{\ell_{1}}{(\tau_{\mathbf{y}})}}} < 1$. The right panel of Figure 11 shows the level sets of the function ${\theta_{\ell_{1}}{(\tau_{\mathbf{x}})}} + {\theta_{\ell_{1}}{(\tau_{\mathbf{y}})}}$ for $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ on the unit square ${\lbrack 0,1\rbrack}^{2}$. The green curve is the level set

Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that program (6.1) succeeds with overwhelming probability when the joint sparsity $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ lies below the green curve.

On the other hand, our computations show that the upper decay threshold $\theta_{\ell_{1}}{(\tau)}$ is numerically equal to the lower decay threshold $\kappa_{\ell_{1}}{(\tau)}$---see the discussion in Appendix C.2. Theorem 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that the sparse demixing method (6.1) fails with overwhelming probability for sparsity levels $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ in the region above the green curve. In other words, the green curve on the right panel of Figure 11 delineates a sharp transition between success and failure for constrained MCA (6.1). The green curve in Figure 11(b) is the same as the green curve in Figure 1.

### Strong guarantees

The theory of Section 4.3 allows us to provide a uniform recovery guarantee. For a fixed draw of the random basis, constrained MCA can demix all sufficiently sparse pairs of vectors with overwhelming probability in high dimensions.

Fix the sparsity $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ and the ambient dimension $d$. Suppose ${\mathbf{Q}} \in \mathsf{O}_{d}$ is a random basis. By Lemma 2.4, constrained MCA can identify every $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$-sparse pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ given the observation ${\mathbf{z}}_{0} = {{\mathbf{x}}_{0} + {{\mathbf{Q}}{\mathbf{y}}_{0}}}$, provided that the event

holds. Theorem 4.11 guarantees that the probability of event (6.2) is large when some associated decay thresholds are small enough; let us describe how to verify the required technical assumptions.

First, the results in Appendix C allow us to compute upper decay threshold at levels $\psi \geq 0$ for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{w}}^{(d)}) \right.\}$ from Section 6.1 consisting of feasible cones for the $\ell_{1}$ norm at $\tau$-sparse vectors. We extend our earlier notation by writing this quantity as $\theta_{\ell_{1}}{(\tau,\psi)}$. This is the first element required to check the hypotheses of Theorem 4.11.

We also require information on the total number of feasible cones under consideration. Let

where the unions take place over all $\lceil{\tau_{\mathbf{x}}d}\rceil$-sparse ${\mathbf{x}}_{0} \in {\mathbb{R}}^{d}$ and all $\lceil{\tau_{\mathbf{y}}d}\rceil$-sparse ${\mathbf{y}}_{0} \in {\mathbb{R}}^{d}$. There are exactly $2^{k}\binom{d}{k}$ different---but congruent---feasible cones of the $\ell_{1}$ norm at vectors in ${\mathbb{R}}^{d}$ with $k$ nonzero entries, one for each sign/sparsity pattern. This corresponds to the number of $({k - 1})$-dimensional faces of the crosspolytope; see, e.g., \[25, Sec. 3.3\]. With $k = {\lceil{\taud}\rceil}$, it follows from the proof of Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications") that

uniformly as $d\rightarrow\infty$. By continuity of the exponential, for every $\eta > 0$ and all sufficiently large $d$, the number of feasible cones is bounded above by

for large enough $d$. Similarly, ${|\mathcal{K}_{\mathbf{y}}^{(d)}|} \leq e^{d{({{E{(\tau_{\mathbf{y}})}} + \eta})}}$ for all sufficiently large $d$.

We have now collected enough information to apply our theory. By Theorem 4.11, the event (6.2) holds with overwhelming probability in high dimensions so long as

The blue curve appearing in Figure 1 on page 1 shows the level set

When the sparsity level $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$ lies below the blue curve, inequality (6.4) holds, so that the demixing method (6.1) succeeds at demixing *every* pair $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ of $(\tau_{\mathbf{x}},\tau_{\mathbf{y}})$-sparse vectors with overwhelming probability in high dimensions.

### Numerical experiment for constrained MCA

The following numerical experiment illustrates the accuracy of these theoretical results. We fix the dimension $d = 100$. For each pair ${(k_{\mathbf{x}},k_{\mathbf{y}})} \in {\{ 0,1,\ldots,100\}}^{2}$, we repeat the following procedure $25$ times.

Draw ${{\mathbf{x}}_{0},{\mathbf{y}}_{0}} \in {\mathbb{R}}^{d}$ with $k_{\mathbf{x}}$ or $k_{\mathbf{y}}$ nonzero elements, respectively. The locations of the nonzero elements are chosen at random, and these elements are equally likely to be $+ 1$ or $- 1$.

Generate a random basis ${\mathbf{Q}} \in \mathsf{O}_{d}$; see Remark 6.1 below.

Solve (6.1) for the optimal point $({\mathbf{x}}_{\star},{\mathbf{y}}_{\star})$ with the numerical optimization software CVX,.

Declare success if $\left\| {{\mathbf{x}}_{\star} - {\mathbf{x}}_{0}} \right\|_{\ell_{\infty}} < 10^{- 4}$.

The background of Figure 1 shows the results of this experiment as a function of $\tau_{\mathbf{x}} = {k_{\mathbf{x}}/d}$ and $\tau_{\mathbf{y}} = {k_{\mathbf{y}}/d}$. The yellow curve marks the empirical $50\%$ success line, and we note that it tracks the green theoretical curve closely. It emerges that $d = 100$ is already large enough to see the high dimensional behavior described by our theoretical results.

### Remark 6.1

A random basis in ${\mathbf{Q}} \in \mathsf{O}_{d}$ is often defined through a conceptually simple two-step operation. First, draw a square $d \times d$ Gaussian matrix; second, orthogonalize the columns of this matrix via the Gram--Schmidt procedure. Although this definition has the flavor of a numerical algorithm, the conceptual process is not numerically stable. Moreover, standard procedures for stabilizing the orthogonalization do not preserve the Haar measure. For a straightforward, numerically stable approach to generating random bases, see.

### Secure and robust channel coding

Next, we study the secure channel coding scheme of Section 1.3.1. We want to analyze when the receiver can decode a transmitted message that is subject to a sparse corruption. The difficulty depends on the sparsity level $\tau$ of the corruption, where $\tau \in {\lbrack 0,1\rbrack}$. Let us introduce an ensemble of demixing problems. In each dimension $d \in {\mathbb{N}}$, choose a $d$-bit message ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$ and a corruption ${\mathbf{c}}_{0} \in {\mathbb{R}}^{d}$ with ${{nnz}{({\mathbf{c}}_{0})}} = {\lceil{\taud}\rceil}$. Draw a random basis $\mathbf{Q}$ known to both the receiver and transmitter. The receiver observes ${\mathbf{z}}_{0} = {{{\mathbf{Q}}{\mathbf{m}}_{0}} + {\mathbf{c}}_{0}}$, the encoded message plus the sparse interference.

The natural complexity measure for the sparse corruption ${\mathbf{c}}_{0}$ is the $\ell_{1}$ norm, while the $\ell_{\infty}$ norm is the appropriate complexity measure for the sign vector ${\mathbf{m}}_{0}$. Note that $\left\| {\mathbf{m}}_{0} \right\|_{\ell_{\infty}} = 1$. To recover the original message, the receiver solves the problem

This approach succeeds when $({\mathbf{m}}_{0},{\mathbf{c}}_{0})$ is the unique optimal point of (6.5).

We consider two types of corruptions. *Benign* corruptions are taken in any manner that is independent of $\mathbf{Q}$---this would happen, for instance, when the corruption is generated by an adversary with no knowledge of $\mathbf{Q}$ or the transmission ${\mathbf{Q}}{\mathbf{m}}_{0}$. *Adversarial* corruptions are worst-case sparse corruptions; these corruptions may model malicious interference or an erasure channel that sets some of the coordinates of ${\mathbf{z}}_{0}$ to zero. We first consider with the benign corruption, and then consider the adversarial case in Section 6.2.2.

### Benign corruptions

Since the corruption is chosen independently of the basis $\mathbf{Q}$, the convex demixing method (6.5) succeeds if it can identify the single pair $({\mathbf{c}}_{0},{\mathbf{m}}_{0})$. Theorems 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") and 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") describe where procedure succeeds, or fails, with overwhelming probability in high dimensions, but we must first determine some decay thresholds.

The feasible cone of the $\ell_{\infty}$ norm at a sign vector is congruent to an orthant (Example 2.2. ‣ 2.1 Feasible cones ‣ 2 The geometry of demixing ‣ Sharp recovery bounds for convex demixing, with applications")). From Table 1, we see that the sequence $\{{{\mathbb{R}}_{+}^{d}:d \in {\mathbb{N}}}\}$ of orthants has an upper decay threshold of $\theta_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$ and a matching lower decay threshold $\kappa_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$. Appendix C defines an upper decay threshold $\theta_{\ell_{1}}{(\tau)}$ for the sequence of feasible cones of the $\ell_{1}$ norm at $\tau$-sparse vectors.

With these thresholds in hand, Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") guarantees that (6.5) succeeds with overwhelming probability in high dimensions provided that ${\theta_{{\mathbb{R}}_{+}^{d}} + {\theta_{\ell_{1}}{(\tau)}}} < 1$, or, equivalently, provided that ${{\theta_{\ell_{1}}{(\tau)}} < \frac{1}{2}}.$ On the other hand, Theorem 4.3. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") shows that (6.5) fails with overwhelming probability in high dimensions if the corresponding upper decay threshold satisfies ${{{\kappa_{\ell_{1}}{(\tau)}} + \kappa_{{\mathbb{R}}_{+}^{d}}} > 1}.$ This condition holds when ${\kappa_{\ell_{1}}{(\tau)}} > \frac{1}{2}$.

Numerically, we find that ${\theta_{\ell_{1}}{(\tau)}} < \frac{1}{2}$ when the sparsity level $\tau \lesssim 0.193$; see the left panel of Figure 11. The fact that ${\kappa_{\ell_{1}}{(\tau)}} = {\theta_{\ell_{1}}{(\tau)}}$ to numerical precision implies that ${\kappa_{\ell_{1}}{(\tau)}} > \frac{1}{2}$ for $\tau \gtrsim 0.193$. In other words, if fewer than $19\%$ of the entries of ${\mathbf{c}}_{0}$ are nonzero, the scheme (6.5) succeeds with overwhelming probability in high dimensions; otherwise, it fails with overwhelming probability in high dimensions. This sharp transition corresponds to the location of the dashed line in Figure 3.

### The adversarial case

Figure 12: Calculating the adversarial guarantees for channel coding. The lower two curves in the figure correspond to θℓ1 (τ,E (τ)) and θℝ+d (E (τ)) defined by (C.14) and (4.6). The upper curve indicates the sum θℓ1 (τ,E (τ)) + θℝ+d (E (τ)). For τ &lt; 0.018, the sum lies below one, so Theorem 4.11 implies that event (6.6) holds with overwhelming probability.

In the adversarial case, the corruptions are sparse but may depend on the basis $\mathbf{Q}$ and the message ${\mathbf{m}}_{0}$. To ensure that no corruption with $\lceil{\taud}\rceil$ nonzero entries can cause (6.5) to fail, we must verify that (6.5) succeeds at identifying $({\mathbf{c}}_{0},{\mathbf{m}}_{0})$ for *every* $\lceil{\taud}\rceil$-sparse vector ${\mathbf{c}}_{0}$. From Lemma 2.4, this is equivalent to the event

We can use Theorem 4.11 to verify that event (6.6) holds with overwhelming probability in high dimensions. Let us collect the additional information required to verify the technical assumptions of this theorem.

For ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$, define the singleton $\mathcal{K}_{\mathbf{m}}^{(d)} = {\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{\infty}},{\mathbf{m}}_{0}) \right.\}}$. The feasible cone $\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{\infty}},{\mathbf{m}}_{0}) \right.$ is congruent to the orthant ${\mathbb{R}}_{+}^{d}$, so the sequence $\mathcal{K}_{\mathbf{m}}^{(d)}$ of sets has an upper decay threshold at level $\psi$ of $\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}$ defined in Proposition 4.9. ‣ 4.3 Uniform demixing guarantees ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications").

Define the set $\mathcal{K}_{\mathbf{c}}^{(d)} = \bigcup{\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{c}}_{0}) \right.\}}$, where the union occurs over all vectors ${\mathbf{c}}_{0}$ with $\lceil{\taud}\rceil$ nonzero elements. By (6.3), the size of $\mathcal{K}_{\mathbf{c}}^{(d)}$ is bounded by

for any $\eta > 0$ and all sufficiently large $d$.

Since $\mathcal{K}_{\mathbf{m}}^{(d)}$ is a singleton, Theorem 4.11 implies that event (6.6) holds with overwhelming probability in high dimensions whenever

Computing $\theta_{\ell_{1}}{(\tau,\psi)}$ and $\theta_{{\mathbb{R}}_{+}^{d}}{(\psi)}$ numerically, we find that for all $\tau \lesssim 0.0186$, inequality (6.7) holds. We conclude that our channel coding scheme is robust to all adversarial corruptions so long as the corruptions have no more than about $1.8\%$ nonzero entries. This computation is illustrated in Figure 12.

### Numerical experiment

We perform two numerical experiments to complement our theory, one for the benign corruptions and the other for a specific type of malicious erasure.

For dimensions $d = 100$ and $d = 300$ and for each of $70$ equally spaced values of $\tau \in {\lbrack 0,0.35\rbrack}$, we test the benign corruption case by repeating the following procedure $200$ times:

Draw a binary vector ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$ at random.

Choose a corruption ${\mathbf{c}}_{0}$ with $k = {\lbrack{\taud}\rbrack}$ nonzero elements; the support of ${\mathbf{c}}_{0}$ is random, and the nonzero elements are taken to be $\pm 1$ with equal probability.

Generate a random basis ${\mathbf{Q}} \in \mathsf{O}_{d}$; see Remark 6.1.

Solve (6.5) with the observation ${\mathbf{z}}_{0} = {{{\mathbf{Q}}{\mathbf{m}}_{0}} + {\mathbf{c}}_{0}}$ with the numerical optimization software CVX; call $({\mathbf{m}}_{\star},{\mathbf{c}}_{\star})$ the optimal point.

Declare success if $\left\| {{\mathbf{m}}_{\star} - {\mathbf{m}}_{0}} \right\|_{\ell_{\infty}} < 10^{- 4}$.

The second experiment incorporates a malicious erasure. As in the benign case, the experiment is run for dimensions $d = 100$ and $d = 300$ and for $70$ equally spaced values of $\tau$ between zero and one. For each of these parameters, we repeat the following $200$ times:

Draw a message ${\mathbf{m}}_{0} \in {\{{\pm 1}\}}^{d}$ at random, and generate a random basis ${\mathbf{Q}} \in \mathsf{O}_{d}$.

Set the observation ${\mathbf{z}}_{0} = {{erase}{({{\mathbf{Q}}{\mathbf{m}}_{0}},{\lbrack{\taud}\rbrack})}}$, where ${erase}{({\mathbf{x}},k)}$ sets the $k$ largest-magnitude elements of $\mathbf{x}$ to zero.

Solve (6.5) with CVX for the optimal point $({\mathbf{m}}_{\star},{\mathbf{c}}_{\star})$, and

Declare success if $\left\| {{\mathbf{m}}_{\star} - {\mathbf{m}}_{0}} \right\|_{\ell_{\infty}} < 10^{- 4}$.

The curves in Figure 3 show the results of these experiments. For benign corruptions, the empirical $50\%$ success rate occurs very near the predicted sparsity value $\tau = 0.193$, and the transition region is more narrow for larger $d$. Thus, the experiment closely match our prediction for the location of the asymptotic phase transition.

The empirical evidence suggests that our adversarial guarantees are conservative for the type of malicious corruption used in the experiment. This is expected, as we have no reason to believe that such erasures correspond to the worst-case corruption. However, the empirical transition between success and failure near $\tau \approx 0.05$ suggests that our adversarial bound lies within a factor of two or three of the best possible guarantee.

### Low-rank matrices under sparse corruptions

Consider the problem of separating a low-rank square matrix from a corruption that is sparse in a random basis. The parameters that determine the difficulty are the proportional rank $\rho \in {\lbrack 0,1\rbrack}$ and the sparsity level $\tau \in {\lbrack 0,1\rbrack}$. Let us introduce a demixing ensemble. For each side length $n \in {\mathbb{N}}$, choose a low-rank matrix ${\mathbf{X}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{rank}{({\mathbf{X}}_{0})}} = {\lceil{\rhon}\rceil}$ and a sparse matrix ${\mathbf{Y}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{nnz}{({\mathbf{Y}}_{0})}} = {\lceil{\taun^{2}}\rceil}$. Draw a random basis $\mathcal{Q}$ for ${\mathbb{R}}^{n \times n}$, and suppose we observe ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}}$.

To promote low-rank, we use the Schatten 1-norm, and to promote sparsity, we use the matrix $\ell_{1}$ norm. Given the side information $\alpha = \left\| {\mathbf{Y}}_{0} \right\|_{\ell_{1}}$, we pose the convex demixing method

We study when $({\mathbf{X}}_{0},{\mathbf{Y}}_{0})$ is the unique solution to (6.8) with overwhelming probability in high dimensions.

The feasible cone of the $\ell_{1}$-matrix norm at a matrix ${\mathbf{Y}}_{0} \in {\mathbb{R}}^{n \times n}$ with $k$ nonzero elements is isomorphic to the feasible cone of the $\ell_{1}$ norm at a sparse vector ${\mathbf{y}}_{0}: = {vec}{({\mathbf{Y}}_{0})} \in {\mathbb{R}}^{n^{2}}$ with $k$ nonzero entries. It follows that the value $\theta_{\ell_{1}}{(\tau)}$ from (C.14) is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{Y}}_{0}) \right.\}$ of feasible cones indexed by the ambient dimension $d = n^{2}$ of the matrix space ${\mathbb{R}}^{n \times n}$.

By Proposition 5.4, we see that $\theta_{S_{1}}{(\rho)}: = 6\rho - 3\rho^{2}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{S_{1}},{\mathbf{X}}_{0}) \right.\}$ of feasible cones, indexed by the ambient dimension. However, a smaller upper decay threshold ${\overset{\sim}{\theta}}_{S_{1}}{(\rho)}$ is available using the results of ---see Remark 5.5. The green line in Figure 4 is the level set

where the ${\overset{\sim}{\theta}}_{S_{1}}{(\rho)}$ is given by the asymptotic upper bound on the Gaussian width given implicitly in \[60, Eq. \].^§§^§Our actual computation uses the simpler, but equivalent, formula given in \[5, Prop. 4.9\]. For $(\rho,\tau)$ pairs lying below the curve, Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") implies that our demixing method (6.8) succeeds with overwhelming probability in high dimensions.

### Numerical experiment

Let us summarize the experiment in Figure 4. The matrix side length $n = 35$ is fixed, and for each pair $(\rho,\tau)$ in the set $\left\{ \frac{1}{n},\frac{2}{n},\ldots,1 \right\}^{2}$, we repeat the following procedure $25$ times:

Draw a matrix ${\mathbf{X}}_{0} = {{\mathbf{Q}}_{L}\mathbf{\Lambda}{\mathbf{Q}}_{R}} \in {\mathbb{R}}^{n \times n}$ with rank $r = {\lbrack{\rhon}\rbrack}$, where $\mathbf{\Lambda}$ is a diagonal matrix that satisfies $\Lambda_{ii} = 1$ for $i = {1,{\ldotsr}}$ and $\Lambda_{ii} = 0$ otherwise and ${\mathbf{Q}}_{L}$, ${\mathbf{Q}}_{R}$ are independent random bases in $\mathsf{O}_{n}$.

Generate a random matrix ${\mathbf{Y}}_{0} \in {\mathbb{R}}^{n \times n}$ with $\lbrack{\taun^{2}}\rbrack$ nonzero entries; the nonzero entries in ${\mathbf{Y}}_{0}$ take the values $+ 1$ or $- 1$ with equal probability.

Generate a random basis $\mathcal{Q}$ for ${\mathbb{R}}^{n \times n}$.

Solve (6.8) with the observation ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}}$ with CVX, and set $({\mathbf{X}}_{\star},{\mathbf{Y}}_{\star})$ to the optimal point.

Declare success if $\left\| {{\mathbf{X}}_{\star} - {\mathbf{X}}_{0}} \right\|_{\ell_{\infty}} < 10^{- 4}$.

From Figure 4, we see that the theoretical bound closely matches the empirical success curve throughout the entire regime.

### Assorted matrix demixing problems

We conclude this section with some other combinations of structured square matrices that we can separate using the convex demixing method (1.2). In each of these applications, we observe a superposition of the form ${\mathbf{Z}}_{0} = {{\mathbf{X}}_{0} + {\mathcal{Q}{({\mathbf{Y}}_{0})}}} \in {\mathbb{R}}^{n \times n}$, where $\mathcal{Q}$ is a random basis for the matrix space ${\mathbb{R}}^{n \times n}$. We consider various structures for ${\mathbf{X}}_{0}$ and ${\mathbf{Y}}_{0}$---either low rank, orthogonal, sparse, or sign matrices---and we show that our theory quickly identifies a regime where an appropriate convex demixing method succeeds with overwhelming probability in high dimensions. While we know of no concrete applications for these particular demixing programs, the analysis below illustrates the ease with which our theory extends to new settings.

### Orthogonal and sparse matrices

Fix a sparsity level $\tau$ in $\lbrack 0,1\rbrack$. For each side length $n \in {\mathbb{N}}$, choose an orthogonal matrix ${\mathbf{X}}_{0} \in \mathsf{O}_{n}$ and a sparse matrix ${\mathbf{Y}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{nnz}{({\mathbf{Y}}_{0})}} = {\lceil{\taun^{2}}\rceil}$. We use the operator norm as a complexity measure for ${\mathbf{X}}_{0}$ and the matrix $\ell_{1}$ norm as a complexity measure for ${\mathbf{Y}}_{0}$. Since $\left\| {\mathbf{X}}_{0} \right\|_{Op} = 1$, we pose the convex demixing method

The interchange of the objective and constraint as compared with (1.2) poses no difficulty because the optimality conditions of Lemma 2.4 are symmetric with respect to the objective and constraint.

By Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), the convex demixing method (6.9) succeeds with overwhelming probability in high dimensions so long as

where $\theta_{\ell_{1}}{(\tau)}$, defined in Appendix C, is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{\ell_{1}},{\mathbf{Y}}_{0}) \right.\}$ and $\theta_{Op} = \frac{3}{4}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{Op},{\mathbf{X}}_{0}) \right.\}$ by Proposition 5.6. Therefore, program (6.9) succeeds with overwhelming probability in high dimensions whenever

This occurs for $\tau < 0.06$; see the left panel of Figure 11. We conclude that (6.9) demixes an orthogonal matrix ${\mathbf{X}}_{0}$ from a matrix sparse in a random basis $\mathcal{Q}{({\mathbf{Y}}_{0})}$ with high probability when no more than about $6\%$ of the elements of ${\mathbf{Y}}_{0}$ are nonzero.

### Low-rank and sign matrices

Fix the proportional rank $\rho$ in $\lbrack 0,1\rbrack$. We abbreviate the ambient dimension $d = n^{2}$. For each side length $n \in {\mathbb{N}}$, choose a low-rank matrix ${\mathbf{X}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{rank}{({\mathbf{X}}_{0})}} = {\lceil{\rhon}\rceil}$ and a sign matrix ${\mathbf{Y}}_{0} \in {\{{\pm 1}\}}^{n \times n}$. We use the Schatten 1-norm as a complexity measure for rank and the matrix $\ell_{\infty}$ norm as a complexity measure for sign matrices. Given that $\left\| {\mathbf{Y}}_{0} \right\|_{\ell_{\infty}} = 1$, we consider the convex demixing method

We invoke Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications") to see that (6.10) succeeds with overwhelming probability in high dimensions whenever ${{\theta_{S_{1}}{(\rho)}} + \theta_{{\mathbb{R}}_{+}^{d}}} < 1$. Here, $\theta_{S_{1}}{(\rho)}$ is an upper decay threshold for the ensemble $\{\mathcal{F}\left. (\parallel \cdot \parallel{}_{S_{1}},{\mathbf{X}}_{0}) \right.\}$ of feasible cones, and $\theta_{{\mathbb{R}}_{+}^{d}}$ is an upper decay threshold for the ensemble of nonnegative orthants. By Proposition 3.12. ‣ 3.3.1 Examples of decay thresholds ‣ 3.3 High-dimensional decay of spherical intrinsic volumes ‣ 3 Background from integral geometry ‣ Sharp recovery bounds for convex demixing, with applications"), we have $\theta_{{\mathbb{R}}_{+}^{d}} = \frac{1}{2}$, while Proposition 5.4 gives ${\theta_{S_{1}}{(\rho)}} = {{6\rho} - {5\rho^{2}}}$. Therefore, the convex demixing method (6.10) succeeds with overwhelming probability in high dimensions so long as

This bound is valid when $\rho \leq 0.09$. We conclude that (6.10) can demix a low-rank matrix from a sign matrix in a random basis with overwhelming probability if ${{rank}{({\mathbf{X}}_{0})}} \leq {0.09n}$, where $n$ is side length of ${\mathbf{X}}_{0}$.

### Low-rank and orthogonal matrices

Let $\rho \in {\lbrack 0,1\rbrack}$ be a proportional rank parameter. For each side length $n \in {\mathbb{N}}$, choose a low-rank matrix ${\mathbf{X}}_{0} \in {\mathbb{R}}^{n \times n}$ with ${{rank}{({\mathbf{X}}_{0})}} = {\lceil{\rhon}\rceil}$ and an orthogonal matrix ${\mathbf{Y}}_{0} \in \mathsf{O}_{n}$. With the usual choice of complexity measures, the convex demixing method is

By Theorem 4.2. ‣ 4.2 The main results ‣ 4 Success and failure ‣ Sharp recovery bounds for convex demixing, with applications"), program (6.11) succeeds with overwhelming probability in high dimensions so long as ${{\theta_{S_{1}}{(\rho)}} + \theta_{Op}} < 1$. Propositions 5.4 and 5.6 imply that this occurs whenever

For instance, it suffices that $\rho \leq 0.04$. Therefore, the convex demixing method (6.11) can identify a superposition of a low-rank matrix and an orthogonal matrix with overwhelming probability in high dimensions so long as ${{rank}{({\mathbf{X}}_{0})}} \leq {0.04n}$, where $n$ is the side length of ${\mathbf{X}}_{0}$.

## Prior art and future directions

This work occupies a unique place in the literature on demixing. The analysis is highly general and applies to many problems. At the same time, the results are sharp or nearly sharp. This final section offers a wide-angle view of the field of demixing, from applications to analytical techniques, with a focus on methods based on convex optimization. We conclude by discussing some extensions of our current approach in the hope of encouraging further development in this field.

### A short history of convex demixing and incoherence

The use of convex optimization for signal demixing has a long history. Early predecessors to morphological component analysis come from the work of Claerbout & Muir and Taylor et al., where $\ell_{1}$ minimization is used to identify sparse spike trains from an observed seismic trace.

Demixing methods based on $\ell_{1}$ minimization were put on a rigorous footing in the 1980s with the work of Santosa & Symes and Donoho & Stark. These results, either implicitly or explicitly, rely on incoherence in the form of an uncertainty principle. The work of Donoho & Huo formalizes the notion of incoherence. Incoherent models, both random and deterministic, now pervade the sparse demixing literature.

In the last decade, new classes of convex regularizers have been introduced for solving inverse problems in signal processing. In particular, the Schatten 1-norm is used for problems involving low-rank matrices,. Demixing methods that involve the Schatten 1-norm include robust principal component analysis and latent variable selection. Rigorous theoretical results for these techniques typically involve a spectral incoherence assumption, but no previous work in this area identifies phase transition behavior.

### The neighborhood of this work

We take much of our inspiration from the geometric analysis of linear inverse problems in. Indeed, the geometric optimality condition (Lemma 2.4) is a direct generalization of a geometric result \[15, Prop. 2.1\] for linear inverse problems. Moreover, the Gaussian width bounds from that work prove useful for computing the decay thresholds in this research.

A related line of work, due to Negahban et al. is based on the concept of restricted strong convexity. The results in these papers are sharp within constant factors, but they do not yield bounds as precise as ours. Another general approach to demixing appears in of, where a deterministic incoherence condition leads to recovery guarantees, even in nonconvex settings. The recovery bounds available through this method are not competitive with the guarantees we provide.

Several works also consider demixing two sparse vectors. The works, show that a nearly dense vector could be demixed from a sufficiently sparse vector, but they do not identify phase transition behavior. Recent work also offers demixing guarantees for demixing sparse vectors when the sparsity is mildly sublinear in the dimension. Their model is similar to our MCA formulation in Section 1.1, but again the results do not identify the phase transition between success and failure.

### Random geometry and convex optimization

We now trace the use of methods from integral geometry for understanding randomized convex optimization programs. Vershik & Sporyshev use an asymptotic analysis of polytope angles to analyze the average-case behavior of the simplex method for linear programming. The underlying formulas have their roots in the results of Ruben, although some of the ideas apparently go back to the work Schläfli from the mid-nineteenth century---see Ruben's paper for a discussion.

The analysis of Vershik & Sporyshev fed a line of investigation on the expected face counts of randomly projected polytopes a topic of theoretical interest in combinatorial geometry. These computations resurfaced in convex optimization in the line of work of Donoho & Tanner. These articles characterize the behavior of convex optimization methods for solving several linear inverse problems under a random measurement model. In Appendix C, we leverage the asymptotic polytope angle calculations of Donoho & Tanner to compute decay threshold for the $\ell_{1}$ norm at sparse vectors.

This asymptotic polytope angle approach also yields stability guarantees for basis pursuit. Furthermore, it has been used to establish that iteratively reweighted basis pursuit can provide strictly stronger guarantees than standard basis pursuit.

Our approach to random geometry differs from these earlier works because it starts with the modern theory of spherical integral geometry. Previous research was based on an older theory of polytope angles. Spherical integral geometry reached its current state of development in the dissertation,. Chapter 6.5 of and the notes therein summarize this research. We also draw on insights from the thesis.

### Conclusions and future directions

The results in this work demonstrate the power of spherical integral geometry in the context of demixing. Our bounds are often tight, and they are broadly applicable. This approach raises many questions worth further attention. We conclude with a list of directions for future work. During the period that our original manuscript was under review, several of these areas have seen significant progress. We augment our original list of open problems with a summary of progress made in the interim.

Tight results for Lagrangian demixing.

: The Lagrange penalized demixing method (1.3) is important because it requires less knowledge about the unobserved vectors $({\mathbf{x}}_{0},{\mathbf{y}}_{0})$ than the corresponding constrained method (1.2). The results in this work give information regarding the potential for, and the limits of, the penalized demixing approach (1.2). Nevertheless, a precise analysis of the penalized problem (1.3) and its dependence on the penalty parameter $\lambda$ would have real practical value.

*While a sharp phase transition characterization for the Lagrange demixing problem (1.3) remains open, the recent work offers theoretical guarantees and explicit choices of Lagrange parameters.*

: It would be interesting to study demixing problems involving more than two structured vectors.

*A study of this problem appears in. The present authors provide sharp phase transition characterizations for demixing an arbitrary number of signals in.*

Spherical intrinsic volumes for more cones.

: Computation of additional decay thresholds will provide new bounds for convex demixing methods. The sharpest decay thresholds appear to require formulas for spherical intrinsic volumes. For instance, an asymptotic analysis of the spherical intrinsic volumes for feasible cones of the Schatten 1-norm would provide sharp recovery results for low-rank matrix demixing problems. Amelunxen & Bürgisser have made some recent progress in this direction by developing a formula for the spherical intrinsic volumes for the semidefinite cone.

Log-concavity of spherical intrinsic volumes.

: Bürgisser & Amelunxen \[10, Conj. 2.19\] conjecture that the sequence of spherical intrinsic volumes is log-concave. This conjecture is closely related to the question of whether the upper and lower decay thresholds match.

*In recent work by the present authors and collaborators, the intrinsic volumes are shown to have a nontrivial log-concave upper bound \[5, Sec. 6.1\]. While this result implies that the upper and lower decay thresholds are often equal (Section 4.2.2), the log-concavity conjecture remains open.*

Extensions to more general probability measures.

: The analysis in this work focuses on a specific random model. It would be interesting to incorporate more general probability measures into our framework. This may be a difficult problem; by the results of Section 5.2, this question is closely related to the observed universality phenomenon in basis pursuit.

*Bayati et al. provide a rigorous version the universality property for basis pursuit observed in. It remains unclear whether their methods adapt to demixing problems considered here.*
