<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Near Optimal Signal Recovery from Random Projections: Universal Encoding Strategies?

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Suppose we are given a vector f in R^(N). How many linear measurements do we need to make about f to be able to recover f to within precision epsilon in the Euclidean (l_2) metric? Or more exactly, suppose we are interested in a class F of such objects - discrete digital signals, images, etc; how many linear measurements do we need to recover objects from this class to within accuracy epsilon? This paper shows that if the objects of interest are sparse or compressible in the sense that the reordered entries of a signal f in F decay like a power-law (or if the coefficient sequence of f in a fixed basis decays like a power-law), then it is possible to reconstruct f to within very high accuracy from a small number of random measurements.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction and Overview of the Main Results", "weight": 1.5} -->

This paper considers the fundamental problem of recovering a finite signal $f \in {\mathbb{R}}^{N}$ from a limited set of measurements. Specifically, given a class of signals $\mathcal{F} \subset {\mathbb{R}}^{N}$, one is interested in the minimum number of linear measurements one has to make to be able to reconstruct objects from $\mathcal{F}$ to within a fixed accuracy $\epsilon$, say, in the usual Euclidean $\ell_{2}$-distance. In other words, how can one specify $K = {K{(\epsilon)}}$ linear functionals where ${(\psi_{k})}_{k \in \Omega}$ is a set of vectors with cardinality ${|\Omega|} = K$, so that it is possible to reconstruct an object $f^{\sharp}$ from the data ${(y_{k})}_{k \in \Omega}$ obeying for each element $f$ taken from $\mathcal{F}$?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Overview of the Main Results", "weight": 1.5} -->

The primary goal is of course, to find appropriate functionals ${(\psi_{k})}_{k \in \Omega}$ so that the required number $K$ of measurements is as small as possible. In addition, we are also interested in concrete and practical recovery algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Overview of the Main Results", "weight": 1.5} -->

The new results in this paper will address this type of question for signals $f$ whose coefficients with respect to a fixed reference basis obey a power-law type decay condition, and for random measurements ${(y_{k})}_{k \in \Omega}$ sampled from a specified ensemble. However, before we discuss these results, we first recall some earlier results concerning signals of small support. (See also Sections 1.7 and 9.2 for a more extensive discussion of related results.)

<!-- chunk {"id": "body-0006", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

In a previous article, the authors together with J. Romberg studied the recovery of sparse signals from limited measurements; i.e. of signals which have relatively few nonzero terms or whose coefficients in some fixed basis have relatively few nonzero entries. This paper discussed some surprising phenomena, and we now review a special instance of those. In order to do so, we first need to introduce the discrete Fourier transform which is given by the usual formula^11^1Strictly speaking, the Fourier transform is associated to an orthonormal basis in $\text{C}^{N}$ rather than ${\mathbb{R}}^{N}$. However all of our analysis here extends easily to complex signals instead of real signals (except for some negligible changes in the absolute constants $C$). For ease of exposition we shall focus primarily on real-valued signals $f \in {\mathbb{R}}^{N}$, except when referring to the Fourier basis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

Suppose then that we wish to recover a signal $f \in {\mathbb{R}}^{N}$ made out of $|T|$ spikes, where the set $T$ denotes the support of the signal We do not know where the spikes are located nor do we know their amplitudes. However, we are given information about $f$ in the form of 'only' $K$ randomly sampled Fourier coefficients ${F_{\Omega}f}:={({\hat{f}{(k)}})}_{k \in \Omega}$ where $\Omega$ is a random set of $K$ frequencies sampled uniformly at random. In, it was shown that $f$ could be reconstructed exactly from these data provided that the expected number of frequency samples obeyed the lower bound for all sufficiently small $\alpha > 0$ (i.e. $\alpha \leq \alpha_{0}$ for some small absolute constant $\alpha_{0}$).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

To recover $f$ from $F_{\Omega}f$, we simply minimize the $\ell_{1}$-norm of the reconstructed signal subject to the constraints Moreover, the probability that exact recovery occurs exceeds $1 - {O{(N^{- {\rho/\alpha}})}}$; $\rho > 0$ is here a universal constant and it is worth noting that the aforementioned reference gave explicit values for this constant. The implied constant in the $O{}$ notation is allowed to depend on $\alpha$, but is independent of $N$. In short, exact recovery may be achieved by solving a simple convex optimization problem---in fact, a linear program for real-valued signals--- which is a result of practical significance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

In a following paper, Candès and Romberg extended these results and showed that exact reconstruction phenomena hold for other synthesis/measurement pairs. For clarity of presentation, it will be convenient to introduce some notations that we will use throughout the remainder of the paper. We let $F_{\Omega}$ denote the $|\Omega|$ by $N$ matrix which specifies the set of those $|\Omega|$ linear functionals which describe the measurement process so that the available information $y$ about $f$ is of the form For instance, in our previous example, $F_{\Omega}$ is the $|\Omega|$ by $N$ partial Fourier matrix whose rows are the sampled sinusoids More generally, suppose that one is given an orthonormal basis $\Psi$ and that one has available partial information about $f$ in the sense that we have knowledge about a randomly selected set $\Omega \subset {\{ 0,\ldots,{N - 1}\}}$ of coefficients in basis $\Psi$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

For convenience, define $\Psi$ to be the $N$ by $N$ synthesis matrix with entries ${\Psi{(t,k)}}:={\psi_{k}{(t)}}$. Then $F_{\Omega}$ is now obtained from $\Psi^{\ast}$ by extracting the $|\Omega|$ rows with indices $k$ obeying $k \in \Omega$. Suppose as before that there is another (fixed) orthonormal basis $\Phi$ in which the coefficients ${\theta{(f)}} = {({\theta_{t}{(f)}})}_{1 \leq t \leq N}$ of $f$ in this basis, defined by are sparse in the sense that only few of the entries of $\theta{(f)}$ are nonzero.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

Then it was shown in that with overwhelming probability, $f$ is the solution to That is, exact reconstruction still occurs; the relationship here between the number of nonzero terms in the basis $\Phi$ and the number of observed coefficients $|\Omega|$ depends upon the incoherence between the two bases. The more incoherent, the fewer coefficients needed; in the other direction, in the maximally coherent case, e.g. $\Psi = \Phi$, one in fact needs to sample essentially all of the coefficients in order to ensure exact reconstruction (the same holds true if $\Phi$ and $\Psi$ share only one element with nonzero inner product with $f$).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

A special instance of these results concerns the case where the set of measurements is generated completely at random; that is, we sample a random orthonormal basis of ${\mathbb{R}}^{N}$ and observe only the first $K$ coefficients in that basis (note that there is no advantage in randomizing $\Omega$ as in Section 1.1 since the basis is already completely random). As before, we let $F_{\Omega}$ be the submatrix enumerating those sampled vectors and solve (1.6). Then a consequence of the methodology developed in this paper is that exact reconstruction occurs with probability at least $1 - {O{(N^{- {\rho/\alpha}})}}$ (for a different value of $\rho$) provided that where $\alpha > 0$ is sufficiently small, and the $\ell_{0}$-norm is of course the size of the support of the vector $\theta$ see for sharper results. In summary, $\ell_{1}$ seems to recover sparse unknown signals in a variety of different situations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

The number of measurements simply needs to exceed the number of unknown nonzero coefficients by a proper amount.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Exact Reconstruction of Sparse Signals", "weight": 1.0} -->

Observe that a nice feature of the random basis discussed above is its statistical invariance by rotation. Let $\Phi$ be any basis so that $\theta{(f)}$ are the coefficients of $f$ in that basis: ${\theta{(f)}}:={\Phi^{\ast}f}$. The constraints in (1.6) impose and since the distribution of $F_{\Omega}\Phi$ is that of $F_{\Omega}$, the choice of the basis $\Phi$ is actually irrelevant. Exact reconstruction occurs (with overwhelming probability) when the signal is sparse in any fixed basis; of course, the recovery algorithm requires knowledge of this basis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Power laws", "weight": 1.0} -->

In general, signals of practical interest may not be supported in space or in a transform domain on a set of relatively small size. Instead, the coefficients of elements taken from a signal class decay rapidly, typically like a power law. We now give two examples leaving mathematical rigor aside in the hope of being more concise.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Power laws", "weight": 1.0} -->

Smooth signals. It is well-known that if a continuous-time object has $s$ bounded derivatives, then the $n$th largest entry of the wavelet or Fourier coefficient sequence is of size about $1/n^{s + {1/2}}$ in one dimension and more generally, $1/n^{{s/d} + {1/2}}$ in $d$ dimensions. Hence, the decay of Fourier or wavelet coefficients of smooth signals exhibits a power law.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Power laws", "weight": 1.0} -->

Signals with bounded variations. A popular model for signal/analysis is the space of objects with bounded variations. At the level of the continuum, the total-variation norm of an object is approximately the $\ell_{1}$ norm of its gradient. In addition, there are obvious discrete analogs for finite signals where the gradient is replaced by finite differences. Now a norm which is almost equivalent to the total-variation norm is the weak-$\ell_{1}$ norm in the wavelet domain; that is, the reordered wavelet coefficients of a compactly supported object $f$ approximately decay like $1/n$. At the discrete level, ${\| f\|}_{BV}$ essentially behaves like the $\ell_{1}$-norm of the Haar wavelet coefficients up to a multiplicative factor of at most $\log N$. Moreover, it is interesting to note that studies show that the empirical wavelet coefficients of photographs of natural scenes actually exhibit the $1/n$-decay.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Power laws", "weight": 1.0} -->

In fact, finding representations with rapidly decaying coefficients is a very active area of research known as Computational Harmonic Analysis and there are of course many other such examples. For instance, certain classes of oscillatory signals have rapidly decaying Gabor coefficients, certain types of images with discontinuities along edges have rapidly decaying curvelet coefficients and so.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Power laws", "weight": 1.0} -->

Whereas considered signals $f$ of small support, we now consider objects whose coefficients in some basis decay like a power-law. We fix an orthonormal basis $\Phi = {(\phi_{t})}_{1 \leq t \leq N}$ (which we call the reference basis), and rearrange the entries ${\theta_{t}{(f)}}:={\langle f,\phi_{t}\rangle}$ of the coefficient vector $\theta{(f)}$ in decreasing order of magnitude ${|\theta|}_{} \geq {|\theta|}_{} \geq \ldots \geq {|\theta|}_{(N)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Power laws", "weight": 1.0} -->

We say that $\theta{(f)}$ belongs to the weak-$\ell_{p}$ ball or radius $R$ (and we will sometimes write $f \in {w\ell_{p}{(R)}}$) for some $0 < p < \infty$ and $C > 0$ if for each $1 \leq n \leq N$, In other words, $p$ controls the speed of the decay: the smaller $p$, the faster the decay. The condition (1.8) is also equivalent to the estimate holding for all $\lambda > 0$. We shall focus primarily on the case $0 < p < 1$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Power laws", "weight": 1.0} -->

It is well-known that the decay rate of the coefficients of $f$ is linked to the 'compressibility' of $f$, compare the widespread use of transform coders in the area of lossy signal or image compression. Suppose for instance that all the coefficients ${({\theta_{t}{(f)}})}_{1 \leq n \leq N}$ are known and consider the partial reconstruction $\theta_{K}{(f)}$ (where $1 \leq K \leq N$ is fixed) obtained by keeping the $K$ largest entries of the vector $\theta{(f)}$ (and setting the others to zero). Then it immediately follows from (1.8) that the approximation error obeys for some constant $C_{p}$ which only depends on $p$. And thus, it follows from Parseval that the approximate signal $f_{K}$ obtained by keeping the largest coefficients in the expansion of $f$ in the reference basis $\Phi$ obeys the same estimate, namely, where $C_{p}$ only depends on $p$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Recovery of objects with power-law decay", "weight": 1.0} -->

We now return to the setup we discussed earlier, where we select $K$ orthonormal vectors $\psi_{1},\ldots,\psi_{K}$ in ${\mathbb{R}}^{N}$ uniformly at random. Since applying a fixed orthonormal transform does not change the problem, we may just as well assume that $\Phi$ is the identity and solve where as usual, ${F_{\Omega}f} = {({\langle f,\psi_{k}\rangle})}_{k \in \Omega}$. In the setting where $f$ does not have small support, we do not expect the recovery procedure (1.10) to recover $f$ exactly, but our first main theorem asserts that it will recover $f$ approximately.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Recovery of objects with power-law decay", "weight": 1.0} -->

Note. From now on and for ease of exposition, we will take $(P_{1})$ as our abstract recovery procedure where it is understood that $f$ is the sparse object of interest to be recovered; that is, $f$ could be a signal in ${\mathbb{R}}^{N}$ or its coefficients in some fixed basis $\Phi$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Precedents", "weight": 1.0} -->

A natural question is whether the number of random samples we identified in Theorem 1.4 is, in some sense, optimal. Or would it be possible to obtain similar accuracies with far fewer observations? To make things concrete, suppose we are interested in the recovery of objects with bounded $\ell_{1}$-norm, e.g. the $\ell_{1}$-ball Suppose we can make $K$ linear measurements about $f \in \mathcal{B}_{1}$ of the form $y = {F_{\Omega}f}$. Then what is the best measurement/reconstruction pair so that the error is minimum? In (1.12), $D$ is the reconstruction algorithm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Precedents", "weight": 1.0} -->

To develop an insight about the intrinsic difficulty of our problem, consider the following geometric picture. Suppose we take $K$ measurements $F_{\Omega}f$; this says that $f$ belongs to an affine space $f_{0} + S$ where $S$ is a linear subspace of co-dimension less or equal to $K$. Now the data available for the problem cannot distinguish any object belonging to that plane. Assume $f$ is known to belong to the $\ell_{1}$-ball $\mathcal{B}_{1}$, say, then the data cannot distinguish between any two points in the intersection ${\mathcal{B}_{1} \cap f_{0}} + S$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Precedents", "weight": 1.0} -->

Therefore, any reconstruction procedure $f^{\ast}{(y)}$ based upon $y = {F_{\Omega}f}$ would obey (When we take the supremum over all $f$, we may just assume that $f$ be orthogonal to the measurements $({y = 0})$ since the diameter will of course be maximal in that case.) The goal is then to find $S$ such that the above diameter be minimal. This connects with the agenda of approximation theory where this problem is known as finding the Gelfand $n$-width of the class $\mathcal{B}_{1}$, as we explain below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Precedents", "weight": 1.0} -->

The Gelfand numbers of a set $\mathcal{F}$ are defined as where $P_{S}$ is, of course, the orthonormal projection on the subspace $S$. Then it turns out that ${d_{K}{(\mathcal{F})}} \leq {E_{K}{(\mathcal{F})}} \leq {d_{K}{(\mathcal{F})}}$. Now a seminal result of Kashin and improved by Garnaev and Gluskin shows that for the $\ell_{1}$ ball, the Gelfand numbers obey where $C$, $C'$ are universal constants. Gelfand numbers are also approximately known for weak-$\ell_{p}$ balls as well.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Precedents", "weight": 1.0} -->

Viewed differently, Kashin, Garnaev and Gluskin assert that with $K$ measurements, the minimal reconstruction error (1.12) one can hope for is bounded below by a constant times ${({K/{\log{({N/K})}}})}^{- {1/2}}$. In this sense, Theorem 1.4 is optimal (within a multiplicative constant) at least for $K \asymp N^{\beta}$, with $\beta < 1$^22^2Note added in proof: since submission of this paper, we proved in that Theorem 1.4 holds with $\log{({N/K})}$ instead of $\log N$ in (1.11 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?"))..

<!-- chunk {"id": "body-0029", "role": "body", "section": "Precedents", "weight": 1.0} -->

Kashin also shows that if we take a random projection, $\text{diam}{(\mathcal{B}_{1} \cap S}$ is bounded above by the right-hand side of (1.15). We would also like to emphasize that similar types of recovery have also been known to be possible in the literature of theoretical computer science, at least in principle, for certain types of random measurements. On the one hand, finding the Chebyshev center of $\text{diam}{({\mathcal{B}_{1} \cap S})}$ is a convex problem, which would yield a near-optimal reconstruction algorithm. On the other hand, this problem is computationally intractable when $p < 1$. Further, one would need to know $p$ and the radius of the weak-$\ell_{p}$ ball which is not realistic in practical applications.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Precedents", "weight": 1.0} -->

The novelty here is that the information about $f$ can be retrieved from those random coefficients by minimizing a simple linear program (1.10), and that the decoding algorithm adapts automatically to the weak-$\ell_{p}$ signal class, without knowledge thereof. Minimizing the $\ell_{1}$-norm gives nearly the best possible reconstruction error simultaneously over a wide range of sparse classes of signals; no information about $p$ and the radius $R$ are required. In addition and as we will see next, another novelty is the general nature of the measurement ensemble.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Precedents", "weight": 1.0} -->

It should also be mentioned that when the measurement ensemble consists of Fourier coefficients on a random arithmetic progression, a very fast recovery algorithm that gives near-optimal results for arbitrary $\ell_{2}$ data has recently been given. Since the preparation of this manuscript, we have learnt that results closely related to those in this paper have appeared. We compare our results with both these works in Section 9.2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Other Measurement Ensembles", "weight": 1.0} -->

Underlying our results is a powerful machinery essentially relying on properties of random matrices which gives us very precise tools allowing to quantify how much of a signal one can reconstruct from random measurements. In fact, Theorem 1.1 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?") holds for other measurement ensembles. For simplicity, we shall consider three types of measured data: The Gaussian ensemble: Here, we suppose that $1 \leq K \leq N$ and $\Omega:={\{ 1,\ldots,K\}}$ are fixed, and the entries of $F_{\Omega}$ are identically and independently sampled from a standard normal distribution The Gaussian ensemble is invariant by rotation since for any fixed orthonormal matrix $\Phi$, the distribution of $F_{\Omega}$ is that of $F_{\Omega}\Phi$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Other Measurement Ensembles", "weight": 1.0} -->

The binary ensemble: Again we take $1 \leq K \leq N$ and $\Omega:={\{ 1,\ldots,K\}}$ to be fixed. But now we suppose that the entries of $F_{\Omega}$ are identically and independently sampled from a symmetric Bernoulli distribution The Fourier ensemble: This ensemble was discussed earlier, and is obtained by randomly sampling rows from the orthonormal $N$ by $N$ Fourier matrix ${\mathcal{F}{(k,t)}} = {{\exp{({- {{i2\pikt}/N}})}}/\sqrt{N}}$. Formally, we let $0 < \tau < 1$ be a fixed parameter, and then let $\Omega$ be the random set defined by where the $I_{k}$'s are i.i.d. Bernoulli variables with ${\text{P}{({I_{k} = 1})}} = \tau$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Other Measurement Ensembles", "weight": 1.0} -->

(In fact $|\Omega|$ is usually very close to $K$; see Lemma 6.6).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Other Measurement Ensembles", "weight": 1.0} -->

Just as Theorem 1.1 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?") suggests, this paper will show that it is possible to derive recovery rates for all three measurement ensembles. The ability to recover a signal $f$ from partial random measurements depends on key properties of those measurement ensembles that we now discuss.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Axiomatization", "weight": 1.0} -->

We shall now unify the treatment of all these ensembles by considering an abstract measurement matrix $F_{\Omega}$, which is a random ${|\Omega|} \times N$ matrix following some probability distribution (e.g. the Gaussian, Bernoulli, or Fourier ensembles). We also allow the number of measurements $|\Omega|$ to be a random variable taking values between $1$ and $N$, and set $K:={\text{E}{({|\Omega|})}}$--- the expected number of measurements. For ease of exposition we shall restrict our attention to real-valued matrices $F_{\Omega}$; the modifications required to cover complex matrices such as those given by the Fourier ensemble are simple. We remark that we do not assume that the rows of the matrix $F_{\Omega}$ form an orthogonal family.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Axiomatization", "weight": 1.0} -->

This section introduces two key properties on $F_{\Omega}$ which---if satisfied---will guarantee that the solution to the problem (1.10) will be a good approximation to the unknown signal $f$ in the sense of Theorem 1.1 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?").

<!-- chunk {"id": "body-0038", "role": "body", "section": "Axiomatization", "weight": 1.0} -->

First, as, our arguments rely, in part, on the quantitative behavior of the singular values of the matrices ${F_{\OmegaT}:={F_{\Omega}R_{T}^{\ast}}}:{{\ell_{2}{(T)}}\rightarrow{\ell_{2}{(\Omega)}}}$ which are the $|\Omega|$ by $|T|$ matrices obtained by extracting $|T|$ columns from $F_{\Omega}$ (corresponding to indices in a set $T$). More precisely, we shall need to assume the following hypothesis concerning the minimum and maximum eigenvalues of the square matrix ${F_{\OmegaT}^{\ast}F_{\OmegaT}}:{{\ell_{2}{(T)}}\rightarrow{\ell_{2}{(T)}}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "About the $\\ell_{1}$ norm", "weight": 1.0} -->

We would like to emphasize that the simple nonlinear reconstruction strategy which minimizes the $\ell_{1}$-norm subject to consistency with the measured observations is well-known in the literature of signal processing. For example in the mid-eighties, Santosa and Symes proposed this rule to reconstruct spike trains from incomplete data, see also. We would also like to point out connections with total-variation approaches in the literature of image processing which are methods based on the minimization of the $\ell_{1}$-norm of the discrete gradient. Note that minimizing the $\ell_{1}$-norm is very different than standard least squares (i.e. $\ell_{2}$) minimization procedures. With incomplete data, the least square approach would simply set to zero the 'unobserved' coefficients. Consider the Fourier case, for instance. The least-squares solution would set to zero all the unobserved frequencies so that the minimizer would have much smaller energy than the original signal. As is well known, the minimizer would also contain a lot of artifacts.

<!-- chunk {"id": "body-0040", "role": "body", "section": "About the $\\ell_{1}$ norm", "weight": 1.0} -->

More recently, $\ell_{1}$-minimization perhaps best known under the name of Basis Pursuit, has been proposed as a convex alternative to the combinatorial norm $\ell_{0}$, which simply counts the number of nonzero entries in a vector, for synthesizing signals as sparse superpositions of waveforms. Interestingly, these methods provided great practical success and were shown to enjoy remarkable theoretical properties and to be closely related to various kinds of uncertainty principles.

<!-- chunk {"id": "body-0041", "role": "body", "section": "About the $\\ell_{1}$ norm", "weight": 1.0} -->

On the practical side, an $\ell_{1}$-norm minimization problem (for real-valued signals) can be recast as a linear program (LP). For example, (1.10) is equivalent to minimizing $\sum_{t}{u{(t)}}$ subject to ${F_{\Omega}g} = {F_{\Omega}f}$ and ${- {u{(t)}}} \leq {g{(t)}} \leq {u{(t)}}$ for all $t$. This is interesting since there is a wide array of ever more effective computational strategies for solving LPs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Applications", "weight": 1.0} -->

In many applications of practical interest, we often wish to reconstruct an object (a discrete signal, a discrete image and so on) from incomplete samples and it is natural to ask how much one can hope to recover. Actually, this work was motivated by the problem of reconstructing biomedical images from vastly undersampled Fourier data. Of special interest are problems in magnetic resonance (MR) angiography but it is expected that our methodology and algorithms will be suitable for other MR imagery, and to other acquisition techniques, such as tomography. In MR angiography, however, we observe few Fourier samples, and therefore if the images of interest are compressible in some transform domain such as in the wavelet domain for example, then $\ell_{1}$-based reconstructions might be especially well-suited.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Applications", "weight": 1.0} -->

Another application of these ideas might be to view the measurement/reconstruction procedure as a kind of lossy encoder/decoder pair where the measurement process would play the role of an encoder and the linear program $(P_{1})$ that of a decoder. We postpone this discussion to Section 8.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Organization of the Paper", "weight": 1.0} -->

This paper is roughly divided into three parts and is organized as follows. The first part (Sections 2 and 3), shows how UUP together with ERP give our main result, namely, Theorem 1.4. In Section 2, we establish that the solution to (1.10) is in some sense stable in the $\ell_{1}$-norm, while Section 3 introduces some $\ell_{2}$-theory and proves our main result. In the second part (Sections 4, 5, 6 and 7), we show that all three measurement ensembles obey UUP and ERP. Section 4 studies singular values of random matrices and shows that the UUP holds for the Gaussian and binary ensembles. Section 5 presents a weaker ERP which, in practice, is far easier to check. In Section 6, we prove that all three ensembles obey the ERP.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Organization of the Paper", "weight": 1.0} -->

In the case of the Fourier ensemble, the strategy for proving the UUP is very different than for Gaussian and binary measurements, and is presented in a separate Section 7. Finally, we will argue in the third part of the paper that one can think of the random measurement process as some kind of universal encoder (Section 8) and briefly discuss some of its very special properties. We conclude with a discussion section (Section 9) whose main purpose is to outline further work and point out connections with the work of others. The Appendix provides proofs of technical lemmas.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stability in the $\\ell_{1}$-norm", "weight": 1.0} -->

In this section, we establish $\ell_{1}$-properties of any minimizer to the problem $(P_{1})$, when the initial signal is mostly concentrated (in an $\ell_{1}$ sense) on a small set.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Extension lemma", "weight": 1.0} -->

As essentially observed, a matrix obeying (1.17 ‣ 1.6 Axiomatization ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?"))---

<!-- chunk {"id": "body-0048", "role": "body", "section": "Uniqueness of the minimizer for the Gaussian ensemble", "weight": 1.0} -->

The claim that the minimizer $f^{\sharp}$ is unique with probability 1, for Gaussian measurements, can be easily established as follows. The claim is trivial for $f \equiv 0$ so we may assume $f$ is not identically zero. Then $F_{\Omega}f$ is almost surely non-zero. Furthermore, if one considers each of the (finitely many) facets of the unit ball of $\ell_{1}{({\mathbb{Z}}_{N})}$, we see that with probability 1 the random Gaussian matrix $F_{\Omega}$ has maximal rank on each of these facets (i.e. the image of each facet under $F_{\Omega}$ has dimension equal to either $K$ or the dimension of the facet, whichever is smaller). From this we see that every point on the boundary of the image of the unit $\ell_{1}$-ball under $F_{\Omega}$ arises from a unique point on that ball. Similarly for non-zero dilates of this ball.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Uniqueness of the minimizer for the Gaussian ensemble", "weight": 1.0} -->

Thus the solution to the problem (1.10) is unique as claimed.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Uniqueness of the minimizer for the Gaussian ensemble", "weight": 1.0} -->

We remark that the question of establishing uniqueness with high probability for discretely randomized ensembles such as the binary and Fourier ensembles discussed below is an interesting one, but one which we will not pursue here.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Eigenvalues of random matrices", "weight": 1.0} -->

In this section, we show that all three ensembles obey the uniform uncertainty principle UUP.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Gaussian ensemble", "weight": 1.0} -->

Let $X$ be an $n$ by $p$ matrix with $p \leq n$ and with i.i.d. entries sampled from the normal distribution with mean zero and variance $1/n$. We are interested in the singular values of $X$ or the eigenvalues of $X^{\ast}X$. A famous result due to Marchenko and Pastur states that the eigenvalues of $X^{\ast}X$ have a deterministic limit distribution supported by the interval $\lbrack{({1 - \sqrt{c}})}^{2},{({1 + \sqrt{c}})}^{2}\rbrack$ as ${n,p}\rightarrow\infty$, with ${p/n}\rightarrow c < 1$. In fact, results from show that the smallest (resp. largest) eigenvalue converges a.s. to ${({1 - \sqrt{c}})}^{2}$ (resp.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Gaussian ensemble", "weight": 1.0} -->

${({1 + \sqrt{c}})}^{2}$). In other words, the smallest singular value of $X/\sqrt{n}$ converges a.s. to $1 - \sqrt{c}$ and the largest to $1 + \sqrt{c}$. In addition, there are remarkably fine statements concerning the speed of the convergence of the largest singular value.

<!-- chunk {"id": "body-0054", "role": "body", "section": "The Gaussian ensemble", "weight": 1.0} -->

To derive the UUP, we need a result about the concentration of the extreme singular values of a Gaussian matrix, and we borrow a most elegant estimate due to Davidson and Szarek. We let ${\lambda_{1}{(X)}} \leq \ldots \leq {\lambda_{p}{(X)}}$ be the ordered list of the singular values of $X$. Then, the authors prove that Such inequalities about the concentration of the largest and smallest singular values of Gaussian matrices have been known for at least a decade or so. Estimates similar to (4.1)-(4.2) may be found in the work of Szarek, see also Ledoux.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

The analysis is more complicated in the case where the matrix $X$ is an $n$ by $p$ array with i.i.d. symmetric Bernoulli entries taking on values in $\{{- {1/\sqrt{n}}},{1/\sqrt{n}}\}$. To study the concentration of the largest singular values of $X$, we follow an approach proposed by Ledoux which makes a simple use of the concentration property, see also.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

As before, we let $\lambda_{p}{(X)}$ be the mapping that associates to a matrix $X$ its largest singular values. Equip ${\mathbb{R}}^{np}$ with the Frobenius norm (the Euclidean norm over ${\mathbb{R}}^{np}$). Then the mapping $\lambda_{p}$ is convex and 1-Lipschitz in the sense that for all pairs $(X,X')$ of $n$ by $p$ matrices. A classical application of the concentration inequality for binary measures then gives $m{({\lambda_{p}{(X)}})}$ is either the mean or the median of $\lambda_{p}{(X)}$. Now the singular values still exhibit the same behavior; that is $\lambda_{\min}{({X/\sqrt{n}})}$ and $\lambda_{\max}{({X/\sqrt{n}})}$ converge a.s.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

to $1 - \sqrt{c}$ and $1 + \sqrt{c}$ respectively, as ${n,p}\rightarrow\infty$ with ${p/n}\rightarrow c$. As a consequence, for each $\epsilon_{0}$ and $n$ sufficiently large, one can show that the medians belong to the fixed interval $\lbrack{1 - \sqrt{p/n} - \epsilon_{0}},{1 + \sqrt{p/n} + \epsilon_{0}}\rbrack$ which gives This is a fairly well-established result.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

The problem is that this method does not apply to the minimum singular value which is 1-Lipshitz but not convex. Fortunately, Litvak, Pajor, Rudelson and Tomczak-Jaegermann \[Theorem 3.1\] have recently announced a result which gives exponential concentration for the lowest singular value. They proved that whenever $n \geq {{({1 + \delta})}p}$ where $\delta$ is greater than a small constant, where $c_{1}$ and $c_{2}$ are universal positive constants.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

Just as (4.1)-(4.2) implied the uniform uncertainty principle UUP for Gaussian matrices, (4.4)-(4.4) gives the same conclusion for the binary ensemble with the proviso that the condition about the lowest singular value reads ${\lambda_{\min}{({F_{\OmegaT}^{\ast}F_{\OmegaT}})}} > {{c_{1}K}/N}$; i.e., $c_{1}$ substitutes 1/2 (recall the remark following the definition of the UUP).

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Fourier ensemble", "weight": 1.0} -->

The analysis for the Fourier ensemble is much more delicate than that for the Gaussian and binary cases, in particular requiring entropy arguments as used for instance by Bourgain,. We prove the following lemma in the separate Section 7.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

In some cases, it might be difficult to prove that the exact reconstruction principle ERP holds, and it is interesting to observe that UUP actually implies ERP for 'generic' sign functions $\sigma = {\pm 1}$ supported on a small set $T$. More precisely, if we fix $T$ and define $\sigma$ to be supported on $T$ with the i.i.d. Bernoulli distribution (independently of $F_{\Omega}$), thus then we shall construct a $P$ obeying the conditions (i)-(iii) in the definition of ERP. Indeed, we shall construct $P$ explicitly as one can view this choice of $P = {F_{\Omega}^{\ast}V}$ as the unique solution to (i) and (ii) which minimizes the $\ell_{2}$ norm of $V$, and can thus be viewed as a kind of least-squares extension of $\sigma$ using the rows of $F_{\Omega}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

It is immediate to check that $P$ obeys (i) and (ii) above. Indeed, the restriction of $P$ to $T$ is given by and, therefore, (i) is verified. Further, it follows from the definition that $P$ is a linear combination of the columns of $F_{\Omega}^{\ast}$ and thus, (ii) holds. Therefore, we only need to check that for all $t \in T^{c}$, ${|{P{(t)}}|} \leq \frac{1}{2}$ with sufficiently high probability. In order to do this, we rewrite $P{(t)}$ as where for each $t \in T^{c}$, $W_{t}$ is the $|T|$ dimensional vector and $F_{t}$ is the $t$-th column of $F_{\Omega}$. We now introduce another condition which is far easier to check than ERP.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

WERP (Weak ERP). We say the the measurement process obeys the weak ERP, if for each fixed $T$ obeying (1.16 ‣ 1.6 Axiomatization ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")) and any $0 < \gamma \leq 1$, $F_{\Omega}$ obeys with probability at least $1 - {O{(N^{- {\rho/\gamma}})}}$ for some fixed positive constant $\rho > 0$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

For example, it is an easy exercise in large deviation theory to show that WERP holds for Gaussian and binary measurements. One can also check that WERP holds for random frequency samples. We omit the proof of these facts, however, since we will show the stronger version, namely, ERP in all three cases. Instead, we would like to emphasize that UUP together with WERP actually imply ERP for most sign patterns $\sigma$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

We begin by recalling the classical Hoeffding inequality: let ${X_{1},\ldots,X_{N}} = {\pm 1}$ be independent symmetric Bernoulli random variables and consider the sum $S = {\sum_{j = 1}^{N}{a_{j}X_{j}}}$. Then Suppose now that the $\sigma{(t)}$'s are independent Bernoulli, and independent from $F$. Then (5.3) gives If we now assume that both UUP and WERP hold, then for any $0 < \gamma \leq 1$ we have with probability at least $1 - {O{(N^{- {\rho/\gamma}})}}$. This shows that Hence, if ${|T|} \leq {{\alphaK}/{\log N}}$, then Therefore, if $\alpha$ is chosen small enough, then for some small $\rho' > 0$ In other words, ERP holds for most sign patterns $\sigma$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Generic signals and the weak ERP", "weight": 1.0} -->

That is, if one is only interested in providing good reconstruction to nearly all signals (but not all) in the sense discussed above, then it is actually sufficient to check that both conditions UUP and WERP are valid.

<!-- chunk {"id": "body-0067", "role": "body", "section": "About the exact reconstruction principle", "weight": 1.0} -->

In this section, we show that all the three ensembles obey the exact reconstruction principle ERP.

<!-- chunk {"id": "body-0068", "role": "body", "section": "The Gaussian ensemble", "weight": 1.0} -->

To show that there is function $P$ obeying the conditions (i)-(iii) in the definition of ERP, we take an approach that resembles that of Section 5, and establish that $P$ defined as in (5.1), obeys the three conditions (i)-(iii).

<!-- chunk {"id": "body-0069", "role": "body", "section": "The Gaussian ensemble", "weight": 1.0} -->

We already argued that $P$ obeys (i) and (ii). Put $P^{c} = {R_{T^{c}}P}$ to be the restriction of $P$ to $T^{c}$. We need to show that with high probability. Begin by factorizing $P^{c}$ as The crucial observation is that the random matrix $F_{\OmegaT^{c}}^{\ast}$ and the random variable $V$ are independent since they are functions of disjoint sets of independent variables.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The binary ensemble", "weight": 1.0} -->

The strategy in the case where the entries of $F$ are independent Bernoulli variables is nearly identical and we only discuss the main differences. Define $P$ and $V$ as above; obviously, $F_{\OmegaT^{c}}^{\ast}$ and $V$ are still independent.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The Fourier ensemble", "weight": 1.0} -->

It turns out that the exact reconstruction principle also holds for the Fourier ensemble although the argument is considerably more involved. We do not reproduce the proof here but merely indicate the strategy for proving that $P$ (defined as before) also obeys the desired bound on the complement of $T$ with sufficiently high probability. We first remark that $|\Omega|$ is concentrated around $K$. To see this, recall the Bernstein's inequality which states that if $X_{1},\ldots,X_{m}$ are independent random variables with mean-zero and obeying ${|X_{i}|} \leq c$, then where $\sigma^{2} = {\sum_{i = 1}^{m}{\text{Var}{(X_{i})}}}$. Specializing this inequality gives the following lemma which we shall need later in this paper.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

In this section, we prove Lemma 4.3. The ideas here are inspired by an entropy argument sketched, as well as by related arguments,. These methods have since become standard in the high-dimensional geometry literature, but we shall give a mostly self-contained presentation here.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

We remark that the arguments in this section (and those in the Appendix) do not use any algebraic properties of the Fourier transform other than the Plancherel identity and the fact that the maximum entry of the Fourier matrix is bounded by $1/\sqrt{N}$. Indeed a simple modification of the arguments we give below also gives the UUP for randomly sampled rows of orthonormal matrices, see also and for further discussion of this issue. Suppose that ${\sup_{i,j}{|U_{ij}|}} \leq \mu$ and let $U_{\Omega}$ be the matrix obtained by randomly selected rows. Then the UUP holds for In the case where one observes a few coefficients in the basis $\Phi$ when the signal is sparse in another basis $\Psi$, $\mu = {\sqrt{N}{\sup_{i,j}{|{\langle\phi_{i},\psi_{j}\rangle}|}}}$ is interpreted as the mutual coherence between $\Phi$ and $\Psi$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

For sake of concreteness, we now return to the Fourier ensemble. Let us first set up what we are trying to prove. Fix $\alpha > 0$, which we shall assume to be sufficiently small. We may take $N$ to be large depending on $\alpha$, as the claim is vacuous when $N$ is bounded depending on $\alpha$. If $T$ is empty then the claim is trivial, so from (1.16 ‣ 1.6 Axiomatization ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")) we may assume that for some (possibly) large constant $C$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

We need to prove (1.17 ‣ 1.6 Axiomatization ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")). By self-adjointness, it would suffice to show that with probability at least $1 - {O{(N^{- {\rho/\alpha}})}}$ for all $f \in {\ell_{2}{(T)}}$ and all $T$ obeying (1.16 ‣ 1.6 Axiomatization ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")), thus ${|T|} \leq m$, where For any fixed $T$ and $f$, the above type of estimate can easily be established with high probability by standard tools such as Lemma 6.6. The main difficulty is that there are an exponentially large number of possible $T$ to consider, and for each fixed $T$ there is a $|T|$-dimensional family of $f$ to consider.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

The strategy is to cover the set of all $f$ of interest by various finite nets at several scales, obtain good bounds on the size of such nets, obtain large deviation estimates for the contribution caused by passing from one net to the net at the next scale, and sum using the union bound.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

We turn to the details. We can rewrite our goal as whenever ${|T|} \leq m$. From Parseval's identity, this is the same as asking that whenever ${|T|} \leq m$. Now let $U_{m} \subseteq {\ell_{2}{(\text{Z}_{N})}}$ denote the set Then the previous goal is equivalent to showing that with probability at least $1 - {O{(N^{- {\rho/\alpha}})}}$ for some $\rho > 0$. In fact we shall obtain the stronger estimate for some constant $\beta > 0$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

It remains to prove (7.3). The left-hand side of (7.3) is the large deviation probability of a supremum of random sums over $U_{m}$. This type of expression can be handled by entropy estimates on $U_{m}$, as was done. To follow their approach, we need some notation. For any $f \in {\ell_{2}{(\text{Z}_{N})}}$, we let $\hat{f}$ be its discrete Fourier transform (1.3) and define the $X$ norm of $f$ by Intuitively, if $f$ is a "generic" function bounded in $\ell_{2}{(\text{Z}_{N})}$ we expect the $X$ norm of $f$ to be also be bounded (by standard large deviation estimates). We shall need this type of control in order to apply Lemma 6.6 effectively. To formalize this intuition we shall need entropy estimates on $U_{m}$ in the $X$ norm.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Uniform Uncertainty Principles for the Fourier Ensemble", "weight": 1.0} -->

Let $B_{X}$ be the unit ball of $X$ in $\ell_{2}{(\text{Z}_{N})}$. Thus for instance $U_{m}$ is contained inside the ball $\sqrt{m} \cdot B_{X}$, thanks to Cauchy-Schwarz. However we have much better entropy estimates available on $U_{m}$ in the $X$ norm, which we now state.

<!-- chunk {"id": "body-0080", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Our results interact with the agenda of coding theory. In fact, one can think of the process of taking random measurements as a kind of universal coding strategy that we explain below. In a nutshell, consider an encoder/decoder pair which would operate roughly as follows: The Encoder and the Decoder share a collection of random vectors $(X_{k})$ where the $X_{k}$'s are independent Gaussian vectors with standard normal entries. In practice, we can imagine that the encoder would send the seed of a random generator so that the decoder would be able to reconstruct those 'pseudo-random' vectors.

<!-- chunk {"id": "body-0081", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Encoder. To encode a discrete signal $f$, the encoder simply calculates the coefficients $y_{k} = {\langle f,X_{k}\rangle}$ and quantizes the vector $y$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Decoder. The decoder then receives the quantized values and reconstructs a signal by solving the linear program (1.10).

<!-- chunk {"id": "body-0083", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

This encoding/decoding scheme is of course very different from those commonly discussed in the literature of information theory. In this scheme, the encoder would not try to know anything about the signal, nor would exploit any special structure of the signal; it would blindly correlate the signal with noise and quantize the output---effectively doing very little work. In other words, the encoder would treat each signal in exactly the same way, hence the name "universal encoding." There are several aspects of such a strategy which seem worth exploring: Robustness. A fundamental problem with most existing coding strategies is their fragility vis a vis bit-loss. Take JPEG 2000, the current digital still-picture compression standard, for example. All the bits in JPEG 2000 do not have the same value and if important bits are missing (e.g. because of packet loss), then there is simply no way the information can be retrieved accurately.

<!-- chunk {"id": "body-0084", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

The situation is very different when one is using the scheme suggested above. Suppose for example that with a little more than $K$ coefficients one achieves the distortion obeying the power-law (This would correspond to the situation where our objects are bounded in $\ell_{1}$.) Thus receiving a little more than $K$ random coefficients essentially allows to reconstruct a signal as precisely as if one knew the $K$ largest coefficients.

<!-- chunk {"id": "body-0085", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Now suppose that in each packet of information, we have both encoded the (quantized) value of the coefficients $y_{k}$ but also the label of the corresponding coefficients $k$. Consider now a situation in which half of the information is lost in the sense that only half of the coefficients are actually received. What is the accuracy of the decoded message $f_{50\%}^{\sharp}$? This essentially corresponds to reducing the number of randomly sampled coefficients by a factor of two, and so by (8.1) we see that the distortion would obey and, therefore, losses would have minimal effect.

<!-- chunk {"id": "body-0086", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Security. Suppose that someone would intercept the message. Then he/she would not be able to decode the message because he/she would not know in which random basis the coefficients are expressed. (In practice, in the case where one would exchange the seed of a random generator, one could imagine protecting it with standard technologies such as RSA. Thus this scheme can be viewed as a variant of the standard stream cipher, based on applying a XOR operation between the plain text and a pseudorandom keystream, but with the advantage of robustness.)

<!-- chunk {"id": "body-0087", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Cost Efficiency. Nearly all coding scenarios work roughly as follows: we acquire a large number of measurements about an object of interest, which we then encode. This encoding process effectively discards most of the measured data so that only a fraction of the measurement is being transmitted. For concreteness, consider JPEG 2000, a prototype of a transform coder. We acquire a large number $N$ of sample values of a digital image $f$. The encoder then computes all the $N$ wavelet coefficients of $f$, and quantizes only the $B \ll N$ largest, say. Hence only a very small fraction of the wavelet coefficients of $f$ are actually transmitted.

<!-- chunk {"id": "body-0088", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

In stark contrast, our encoder makes measurements that are immediately used. Suppose we could design sensors which could actually measure the correlations $\langle f,X_{k}\rangle$. Then not only the decoded object would be nearly as good (in the $\ell_{2}$-distance) as that obtained by knowing all the wavelet coefficients and selecting the largest (it is expected that the $\ell_{1}$-reconstruction is well-behaved vis a vis quantization), but we would effectively encode all the measured coefficients and thus, we would not discard any data available about $f$ (except for the quantization).

<!-- chunk {"id": "body-0089", "role": "body", "section": "'Universal' Encoding", "weight": 1.0} -->

Even if one could make all of this practical, a fundamental question remains: is this an efficient strategy? That is, for a class of interesting signals, e.g. a class of digital images with bounded variations, would it be possible to adapt the ideas presented in this paper to show that this scheme does not use many more bits than what is considered necessary? In other words, it appears interesting to subject this compression scheme to a rigorous information theoretic analysis. This analysis would need to address 1) how one would want to efficiently quantize the values of the coefficients $\langle f,X_{k}\rangle$ and 2) how the quantization quantitatively affects the precision of the reconstructed signal.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Robustness", "weight": 1.0} -->

To be widely applicable, we need noise-aware variants of the ideas presented in this paper which are robust against the effects of quantization, measurement noise and modeling error, as no real-world sensor can make perfectly accurate measurements. We view these issues as important research topics. For example, suppose that the measurements $y_{k} = {\langle f,\psi_{k}\rangle}$ are rounded up to the nearest multiple of $q$, say, so that the available information is of the form $y_{k}^{q}$ with ${- {q/2}} \leq {y_{k}^{q} - y_{k}} \leq {q/2}$. Then we would like to know whether the solution $f^{\#}$ to (1.10) or better, of the variant still obeys error estimates such as those introduced in Theorem 1.4. Our analysis seems to be amenable to this situation and work in progress shows that the quality of the reconstruction degrades gracefully as $q$ increases.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Robustness", "weight": 1.0} -->

Precise quantitative answers would help establishing the information theoretic properties of the scheme introduced in Section 8.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

Our results are connected with very recent work of A. Gilbert, S. Muthukrishnan, and M. Strauss,. In this work, one considers a discrete signal of length $N$ which one would like to represent as a sparse superposition of sinusoids. In, the authors develop a randomized algorithm that essentially samples the signal $f$ in the time domain $O{({B^{2}\text{poly}{({\log N})}})}$ times ($\text{poly}{({\log N})}$ denotes a polynomial term in $\log N$) and returns a vector of approximate Fourier coefficients. They show that under certain conditions, this vector gives, with positive probability, an approximation to the discrete Fourier transform of $\hat{f}$ which is almost as good as that obtained by keeping the $B$-largest entries of the discrete Fourier transform of $\hat{f}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

In, the algorithm was refined so that only $O{({B\text{poly}{({\log N})}})}$ samples are needed and so that the algorithm runs in $O{({B\text{poly}{({\log N})}})}$ time which truly is a remarkable feat. To achieve this gain, however, one has to sample the signal on highly structured random grids.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

Our approach is different in several aspects. First and foremost, we are given a fixed set of nonadaptive measurements. In other words, the way in which we stated the problem does not give us the 'luxury' of adaptively sampling the signals as. In this context, it is unclear how the methodology presented in would allow reconstructing the signal $f$ from $O{({B\text{poly}{({\log N})}})}$ arbitrary sampled values. In contrast, our results guarantee that an accurate reconstruction is possible for nearly all possible measurements sets taken from ensembles obeying UUP and ERP. Second, the methodology there essentially concerns the recovery of spiky signals from frequency samples and do not address other setups. Yet, there certainly is a similar flavor in the statements of their results. Of special interest is whether some of the ideas developed by this group of researchers might be fruitful to attack problems such as those discussed in this article.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

While finishing the write-up of this paper, we became aware of very recent and independent work by David Donoho on a similar project. In that paper which appeared one month before ours, Donoho essentially proves Theorem 1.1 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?") for Gaussian ensembles. He also shows that if a measurement matrix obeys 3 conditions (CS1-CS3), then one can obtain the estimate (1.11 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")). There is some overlap in methods, in particular the estimates of Szarek on the condition numbers of random matrices (CS1) also play a key role in those papers, but there is also a greater reliance in those papers on further facts from high-dimensional geometry, in particular in understanding the shape of random sections of the $\ell_{1}$ ball (CS2-CS3).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

Our proofs are completely different in style and approach, and most of our claims are different. While only derives results for the Gaussian ensemble, this paper establishes that other types of ensembles such as the binary and the Fourier ensembles and even arbitrary measurement/synthesis pairs will work as well. This is important because this shows that concrete sensing mechanisms may be used in concrete applications.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

In a companion to this paper we actually improve on the results presented here and show that Theorem 1.4 holds for general measurement ensembles obeying the UUP. The implication for the Gaussian ensemble is that the recovery holds with an error in (1.11 ‣ 1.3 Recovery of objects with power-law decay ‣ 1 Introduction and Overview of the Main Results ‣ Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?")) of size at most a constant times ${({K/{\log{({N/K})}}})}^{- r}$.
