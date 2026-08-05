<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stable Signal Recovery from Incomplete and Inaccurate Measurements

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Suppose we wish to recover an n-dimensional real-valued vector x_0 (e.g. a digital signal or image) from incomplete and contaminated observations y = A x_0 + e; A is a n by m matrix with far fewer rows than columns (n << m) and e is an error term. Is it possible to recover x_0 accurately based on the data y? To recover x_0, we consider the solution x* to the l1-regularization problem min \|x\|_1 subject to \|Ax-y\|_2 <= epsilon, where epsilon is the size of the error term e. We show that if A obeys a uniform uncertainty principle (with unit-normed columns) and if the vector x_0 is sufficiently sparse, then the solution is within the noise level \|x* - x_0\|_2 \le C epsilon. As a first example, suppose that A is a Gaussian random matrix, then stable recovery occurs for almost all such A's provided that the number of nonzeros of x_0 is of about the same order as the number of observations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Second, suppose one observes few Fourier samples of x_0, then stable recovery occurs for almost any set of p coefficients provided that the number of nonzeros is of the order of n/[\log m]^6. In the case where the error term vanishes, the recovery is of course exact, and this work actually provides novel insights on the exact recovery phenomenon discussed in earlier papers. The methodology also explains why one can also very nearly recover approximately sparse signals.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Exact recovery of sparse signals", "weight": 1.0} -->

Recent papers have developed a series of powerful results about the exact recovery of a finite signal $x_{0} \in {\mathbb{R}}^{m}$ from a very limited number of observations. As a representative result from this literature, consider the problem of recovering an unknown sparse signal ${x_{0}{(t)}} \in {\mathbb{R}}^{m}$; that is, a signal $x_{0}$ whose support $T_{0} = {\{ t:{{x_{0}{(t)}} \neq 0}\}}$ is assumed to have small cardinality. All we know about $x_{0}$ are $n$ linear measurements of the form where the $a_{k} \in {\mathbb{R}}^{m}$ are known test signals. Of special interest is the vastly underdetermined case, $n \ll m$, where there are many more unknowns than observations. At first glance, this may seem impossible.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Exact recovery of sparse signals", "weight": 1.0} -->

However, it turns out that one can actually recover $x_{0}$ exactly by solving the convex program^11^1$(P_{1})$ can even be recast as a linear program. provided that the matrix $A \in {\mathbb{R}}^{n \times m}$ obeys a uniform uncertainty principle.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Exact recovery of sparse signals", "weight": 1.0} -->

The uniform uncertainty principle, introduced in and refined, essentially states that the $n \times m$ measurement matrix $A$ obeys a "restricted isometry hypothesis." To introduce this notion, let ${A_{T},T} \subset {\{ 1,\ldots,m\}}$ be the $n \times {|T|}$ submatrix obtained by extracting the columns of $A$ corresponding to the indices in $T$. Then defines the $S$-restricted isometry constant $\delta_{S}$ of $A$ which is the smallest quantity such that for all subsets $T$ with ${|T|} \leq S$ and coefficient sequences ${(c_{j})}_{j \in T}$. This property essentially requires that every set of columns with cardinality less than $S$ approximately behaves like an orthonormal system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Exact recovery of sparse signals", "weight": 1.0} -->

It was shown (also in) that if $S$ verifies then solving $(P_{1})$ recovers any sparse signal $x_{0}$ with support size obeying ${|T_{0}|} \leq S$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Stable recovery from imperfect measurements", "weight": 1.0} -->

This paper develops results for the "imperfect" (and far more realistic) scenarios where the measurements are noisy and the signal is not exactly sparse. Everyone would agree that in most practical situations, we cannot assume that $Ax_{0}$ is known with arbitrary precision. More appropriately, we will assume instead that one is given "noisy" data $y = {{Ax_{0}} + e}$, where $e$ is some unknown perturbation bounded by a known amount ${\| e\|}_{\ell_{2}} \leq \epsilon$. To be broadly applicable, our recovery procedure must be stable: small changes in the observations should result in small changes in the recovery. This wish, however, may be quite hopeless. How can we possibly hope to recover our signal when not only the available information is severely incomplete but in addition, the few available observations are also inaccurate?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Stable recovery from imperfect measurements", "weight": 1.0} -->

Consider nevertheless (as in for example) the convex program searching, among all signals consistent with the data $y$, for that with minimum $\ell_{1}$-norm The first result of this paper shows that contrary to the belief expressed above, the solution to $(P_{2})$ recovers an unknown sparse object with an error at most proportional to the noise level. Our condition for stable recovery again involves the restricted isometry constants.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Examples", "weight": 1.0} -->

It is of course of interest to know which matrices obey the uniform uncertainty principle with good isometry constants. Using tools from random matrix theory, give several examples of matrices such that holds for $S$ on the order of $n$ to within log factors. Examples include (proofs and additional discussion can be found in): Random matrices with i.i.d. entries. Suppose the entries of $A$ are i.i.d. Gaussian with mean zero and variance $1/n$, then show that the condition for Theorem 1 holds with overwhelming probability when In fact, gives numerical values for the constant $C$ as a function of the ratio $n/m$. The same conclusion applies to binary matrices with independent entries taking values $\pm {1/\sqrt{n}}$ with equal probability.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Examples", "weight": 1.0} -->

Fourier ensemble. Suppose now that $A$ is obtained by selecting $n$ rows from the $m \times m$ discrete Fourier transform and renormalizing the columns so that they are unit-normed. If the rows are selected at random, the condition for Theorem 1 holds with overwhelming probability for $S \leq {{C \cdot n}/{({\log m})}^{6}}$. (For simplicity, we have assumed that $A$ takes on real-valued entries although our theory clearly accommodates complex-valued matrices so that our discussion holds for both complex and real-valued Fourier transforms.)

<!-- chunk {"id": "body-0012", "role": "body", "section": "Examples", "weight": 1.0} -->

This case is of special interest as reconstructing a digital signal or image from incomplete Fourier data is an important inverse problem with applications in biomedical imaging (MRI and tomography), Astrophysics (interferometric imaging), and geophysical exploration.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Examples", "weight": 1.0} -->

General orthogonal measurement ensembles. Suppose $A$ is obtained by selecting $n$ rows from an $m$ by $m$ orthonormal matrix $U$ and renormalizing the columns so that they are unit-normed. Then shows that if the rows are selected at random, the condition for Theorem 1 holds with overwhelming probability provided where $\mu:={\sqrt{m}{\max_{i,j}{|U_{i,j}|}}}$. Observe that for the Fourier matrix, $\mu = 1$, and thus is an extension of the Fourier ensemble.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Examples", "weight": 1.0} -->

This fact is of significant practical relevance because in many situations, signals of interest may not be sparse in the time domain but rather may be (approximately) decomposed as a sparse superposition of waveforms in a fixed orthonormal basis $\Psi$; e.g. in a nice wavelet basis. Suppose that we use as test signals a set of $n$ vectors taken from a second orthonormal basis $\Phi$. We then solve $(P_{1})$ in the coefficient domain where $A$ is obtained by extracting $n$ rows from the orthonormal matrix $U = {\Phi\Psi^{\ast}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Prior work and innovations", "weight": 1.0} -->

The problem of recovering a sparse vector by minimizing $\ell_{1}$ under linear equality constraints has recently received much attention, mostly in the context of Basis Pursuit, where the goal is to uncover sparse signal decompositions in overcomplete dictionaries. We refer the reader to and the references therein for a full discussion.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Prior work and innovations", "weight": 1.0} -->

We would especially like to note two works by Donoho, Elad, and Temlyakov, and Tropp that also study the recovery of sparse signals from noisy observations by solving $(P_{2})$ (and other closely related optimization programs), and give conditions for stable recovery. In, the sparsity constraint on the underlying signal $x_{0}$ depends on the magnitude of the maximum entry of the Gram matrix ${M{(A)}} = {\max_{{i,j}:{i \neq j}}{|{({A^{\ast}A})}|}_{i,j}}$. Stable recovery occurs when the number of nonzeros is at most ${({M^{- 1} + 1})}/4$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Prior work and innovations", "weight": 1.0} -->

For instance, when $A$ is a Fourier ensemble and $n$ is on the order of $m$, we will have $M$ at least of the order $1/\sqrt{n}$ (with high probability), meaning that stable recovery is known to occur when the number of nonzeros is about at most $O{(\sqrt{n})}$. In contrast, the condition for Theorem 1 will hold when this number is about $n/{({\log m})}^{6}$, due to the range of support sizes for which the uniform uncertainty principle holds. In, a more general condition for stable recovery is derived. For the measurement ensembles listed in the previous section, however, the sparsity required is still on the order of $\sqrt{n}$ in the situation where $n$ is comparable to $m$. In other words, whereas these results require at least $O{(\sqrt{m})}$ observations per unknown, our results show that---ignoring log-like factors---only $O{}$ are, in general, sufficient.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Prior work and innovations", "weight": 1.0} -->

More closely related is the very recent work of Donoho who shows a version of in the case where $A \in {\mathbb{R}}^{n \times m}$ is a Gaussian matrix with $n$ proportional to $m$, with unspecified constants for both the support size and that appearing. Our main claim is on a very different level since it is deterministic (it can of course be specialized to random matrices), and widely applicable since it extends to any matrix obeying the condition ${\delta_{3S} + {3\delta_{4S}}} < 2$. In addition, the argument underlying Theorem 1 is short and simple, giving precise and sharper numerical values. Finally, we would like to point out connections with fascinating ongoing work which develops fast randomized algorithms for sparse Fourier transforms. Suppose $x_{0}$ is a fixed vector with $|T_{0}|$ nonzero terms, for example.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Prior work and innovations", "weight": 1.0} -->

Then shows that it is possible to randomly sample the frequency domain ${|T_{0}|}\text{poly}{({\log m})}$ times ($\text{poly}{({\log m})}$ denotes a polynomial term in $\log m$), and reconstruct $x_{0}$ from these frequency data with positive probability. We do not know whether these algorithms are stable in the sense described in this paper, and whether they can be modified to be universal, i.e. reconstruct all signals of small support.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

This section illustrates the effectiveness of the recovery by means of a few simple numerical experiments. Our simulations demonstrate that in practice, the constants in and seem to be quite low.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Our first series of experiments is summarized in Tables 1 and 2. In each experiment, a length $1024$ signal was measured with the same $300 \times 1024$ Gaussian measurement ensemble. The measurements were then corrupted by additive white Gaussian noise: $y_{k} = {{\langle x_{0},a_{k}\rangle} + e_{k}}$ with $e_{k} \sim {\mathcal{N}{(0,\sigma^{2})}}$ for various noise levels $\sigma$. The squared norm of the error ${\| e\|}_{\ell_{2}}^{2}$ is a chi-square random variable with mean $\sigma^{2}n$ and standard deviation $\sigma^{2}\sqrt{2n}$; owing to well known concentration inequalities, the probability that ${\| e\|}_{\ell_{2}}^{2}$ exceeds its mean plus two or three standard deviations is small.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We then solve $(P_{2})$ with and select $\lambda = 2$ although other choices are of course possible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Table 1 charts the results for sparse signals with $50$ nonzero components. Ten signals were generated by choosing $50$ indices uniformly at random, and then selecting either $- 1$ or $1$ at each location with equal probability. An example of such a signal is shown in Figure 2(a). Previous experiments have demonstrated that we were empirically able to recover such signals perfectly from $300$ noiseless Gaussian measurements, which is indeed the case for each of the $10$ signals considered here. The average value of the recovery error (taken over the $10$ signals) is recorded in the bottom row of Table 1. In this situation, the constant in appears to be less than $2$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Table 2 charts the results for $10$ compressible signals whose components are all non-zero, but decay as. The signals were generated by taking a fixed sequence randomly permuting it, and multiplying by a random sign sequence (the constant in was chosen so that the norm of the compressible signals is the same --- $\sqrt{50}$ --- as the sparse signals in the previous set of experiments). An example of such a signal is shown in Figure 2(c). Again, $10$ such signals were generated, and the average recovery error recorded in the bottom row of Table 2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

For small values of $\sigma$, the recovery error is dominated by the approximation error --- the second term on the right hand side of. As a reference, the $50$ term nonlinear approximation errors of these compressible signals is around $0.47$; at low signal-to-noise ratios our recovery error is about $1.5$ times this quantity. As the noise power gets large, the recovery error becomes less than $\epsilon$, just as in the sparse case.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Finally, we apply our recovery procedure to realistic imagery. Photograph-like images, such as the $256 \times 256$ pixel Boats image shown in Figure 3(a), have wavelet coefficient sequences that are compressible (see). The image is a $65536$ dimensional vector, making the standard Gaussian ensemble too unwieldy^33^3Storing a double precision $25000 \times 65536$ matrix would use around $13.1$ gigabytes of memory, about the capacity of three standard DVDs.. Instead, we make $25000$ measurements of the image using a scrambled real Fourier ensemble; that is, the test functions $a_{k}{(t)}$ are real-valued sines and cosines (with randomly selected frequencies) which are temporally scrambled by randomly permuting the $m$ time points. In other words, this ensemble is obtained from the (real-valued) Fourier ensemble by a random permutation of the columns.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

For our purposes here, the test functions behave like a Gaussian ensemble in the sense that from $n$ measurements, one can recover signals with about $n/5$ nonzero components exactly from noiseless data. There is a computational advantage as well, since we can apply $A$ and its adjoint $A^{T}$ to an arbitrary vector by means of an $m$ point FFT. To recover the wavelet coefficients of the object, we simply solve where $A$ is the scrambled Fourier ensemble, and $W$ is the discrete Daubechies-8 orthogonal wavelet transform.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We will attempt to recover the image from measurements perturbed in two different manners. First, as in the 1D experiments, the measurements were corrupted by additive white Gaussian noise with $\sigma = {5 \cdot 10^{- 4}}$ so that ${\sigma \cdot \sqrt{n}} =.0791$. As shown in Figure 4, the noise level is significant; the signal-to-noise ratio is ${{\|{Ax_{0}}\|}_{\ell_{2}}/{\| e\|}_{\ell_{2}}} = 4.5$. With $\epsilon =.0798$ as, the recovery error is ${\|{\alpha^{\sharp} - \alpha_{0}}\|}_{\ell_{2}} = 0.1303$ (the original image has unit norm).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

For comparison, the $5000$ term nonlinear approximation error for the image is ${\|{\alpha_{0,5000} - \alpha_{0}}\|}_{\ell_{2}} = 0.050$. Hence the recovery error is very close to the sum of the approximation error and the size of the perturbation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Another type of perturbation of practical interest is round-off or quantization error. In general, the measurements cannot be taken with arbitrary precision, either because of limitations inherent to the measuring device, or that we wish to communicate them using some small number of bits. Unlike additive white Gaussian noise, round-off error is deterministic and signal dependent---a situation our methodology deals with easily.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

The round-off error experiment was conducted as follows. Using the same scrambled Fourier ensemble, we take $25000$ measurements of Boats, and round (quantize) them to one digit (we restrict the values of the measurements to be one of ten preset values, equally spaced). The measurement error is shown in Figure 4(c), and the signal-to-noise ratio is ${{\|{Ax_{0}}\|}_{\ell_{2}}/{\| e\|}_{\ell_{2}}} = 4.3$. To choose $\epsilon$, we use a rough model for the size of the perturbation. To a first approximation, the round-off error for each measurement behaves like a uniformly distributed random variable on $({- {q/2}},{q/2})$, where $q$ is the distance between quantization levels.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Under this assumption, the size of the perturbation ${\| e\|}_{\ell_{2}}^{2}$ would behave like a sum of squares of uniform random variables Here, ${{mean}{(Y)}} = {{nq^{2}}/12}$ and ${{std}{(Y)}} = {{\sqrt{n}q^{2}}/{\lbrack{6\sqrt{5}}\rbrack}}$. Again, $Y$ is no larger than ${{mean}{(Y)}} + {\lambda{{std}{(Y)}}}$ with high probability, and we select where as before, $\lambda = 2$. The results are summarized in the second column of Table 3. As in the previous case, the recovery error is very close to the sum of the approximation and measurement errors. Also note that despite the crude nature of the perturbation model, an accurate value of $\epsilon$ is chosen.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Although the errors in the recovery experiments summarized in the third row of Table 3 are as we hoped, the recovered images tend to contain visually displeasing high frequency oscillatory artifacts. To address this problem, we can solve a slightly different optimization problem to recover the image from the same corrupted measurements. In place of $(P_{2}')$, we solve is the total variation of the image $x$: the sum of the magnitudes of the (discretized) gradient. By substituting $({TV})$ for $(P_{2}')$, we are essentially changing our model for photograph-like images. Instead of looking for an image with a sparse wavelet transform that explains the observations, program $({TV})$ searches for an image with a sparse gradient (i.e. without spurious high frequency oscillations).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In fact, it is shown in that just as signals which are exactly sparse can be recovered perfectly from a small number of measurements by solving $(P_{2})$ with $\epsilon = 0$, signals with gradients which are exactly sparse can be recovered by solving $({TV})$ (again with $\epsilon = 0$).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

The convex programs $(P_{2})$ and $({TV})$ are simple instances of a class of problems known as second-order cone programs (SOCP's). As an example, one can recast $({TV})$ as where ${G_{i,j}x} = {({x_{{i + 1},j} - x_{i,j}},{x_{i,{j + 1}} - x_{i,j}})}$. SOCP's can nowadays be solved efficiently by interior-point methods and, hence, our approach is computationally tractable.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

From a certain viewpoint, recovering via $(P_{2})$ is using a priori information about the nature of the underlying image, i.e. that it is sparse in some known orthobasis, to overcome the shortage of data. In practice, we could of course use far more sophisticated models to perform the recovery. Obvious extensions include looking for signals that are sparse in overcomplete wavelet or curvelet bases, or for images that have certain geometrical structure. The numerical experiments in Section 3 show how changing the model can result in a higher quality recovery from the same set of measurements.
