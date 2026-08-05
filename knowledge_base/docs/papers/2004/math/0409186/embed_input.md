<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the model problem of reconstructing an object from incomplete frequency samples. Consider a discrete-time signal f in C^(N) and a randomly chosen set of frequencies Omega of mean size tauN. Is it possible to reconstruct f from the partial knowledge of its Fourier coefficients on the set Omega? A typical result of this paper is as follows: for each M > 0, suppose that f obeys # t, f(t) != 0 <= alpha(M) * (log N)^(-1) * # Omega, then with probability at least 1-O(N^-M), f can be reconstructed exactly as the solution to the l_1 minimization problem min_g sum_t = 0^(N)-1 |g(t)|, quad s.t. hat g(omega) = hat f(omega) for all omega in Omega. In short, exact recovery may be obtained by solving a convex optimization problem. We give numerical values for alpha which depends on the desired probability of success; except for the logarithmic factor, the condition on the size of the support is sharp.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The methodology extends to a variety of other setups and higher dimensions. For example, we show how one can reconstruct a piecewise constant (one or two-dimensional) object from incomplete frequency samples - provided that the number of jumps (discontinuities) obeys the condition above - by minimizing other convex functionals such as the total-variation of f.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many applications of practical interest, we often wish to reconstruct an object (a discrete signal, a discrete image, etc.) from incomplete Fourier samples. In a discrete setting, we may pose the problem as follows; let $\hat{f}$ be the Fourier transform of a discrete object $f{(t)}$, $t \in {\mathbb{Z}}_{N}^{d}:={\{ 0,1,\ldots,{N - 1}\}}^{d}$, The problem is then to recover $f$ from partial frequency information, namely, from $\hat{f}{(\omega)}$, where $\omega = {(\omega_{1},\ldots,\omega_{d})}$ belongs to some set $\Omega$ of cardinality less than $N^{d}$---the size of the discrete object.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we show that we can recover $f$ exactly from observations ${\hat{f}|}_{\Omega}$ on small set of frequencies provided that $f$ is sparse. The recovery consists of solving a straightforward optimization problem that finds $f^{\sharp}$ of minimal complexity with ${{\hat{f}}^{\sharp}{(\omega)}} = {\hat{f}{(\omega)}}$, ${\forall\omega} \in \Omega$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "A puzzling numerical experiment", "weight": 1.0} -->

This idea is best motivated by an experiment with surprisingly positive results. Consider a simplified version of the classical 'tomography' problem in medical imaging: we wish to reconstruct a 2D image $f{(t_{1},t_{2})}$ from samples ${\hat{f}|}_{\Omega}$ of its discrete Fourier transform on a star-shaped domain $\Omega$. Our choice of domain is not contrived; many real imaging devices can collect high-resolution samples along radial lines at relatively few angles. Figure 1(b) illustrates a typical case where one gathers $512$ samples along each of $22$ radial lines.

<!-- chunk {"id": "body-0007", "role": "body", "section": "A puzzling numerical experiment", "weight": 1.0} -->

Frequently discussed approaches in the literature of medical imaging for reconstructing an object from 'polar' frequency samples are the so-called filtered backprojection algorithms. In a nutshell, one assumes that the Fourier coefficients at all of the unobserved frequencies are zero (thus reconstructing the image of "minimal energy" under the observation constraints). This strategy does not perform very well, and could hardly be used for medical diagnostic. The reconstructed image, shown in Figure 1(c), has severe nonlocal artifacts caused by the angular undersampling. A good reconstruction algorithm, it seems, would have to guess the values of the missing Fourier coefficients. In other words, one would need to interpolate $\hat{f}{(\omega_{1},\omega_{2})}$. This is highly problematic, however; predictions of Fourier coefficients from their neighbors are very delicate, due to the global and highly oscillatory nature of the Fourier transform. Going back to our example, we can see the problem immediately.

<!-- chunk {"id": "body-0008", "role": "body", "section": "A puzzling numerical experiment", "weight": 1.0} -->

To recover frequency information near $(\omega_{1},\omega_{2})$, where $\omega_{1}$ is near $\pm \pi$, we would need to interpolate $\hat{f}$ at the Nyquist rate ${2\pi}/N$. However, we only have samples at rate about $\pi/22$; the sampling rate is almost $50$ times smaller than the Nyquist rate!

<!-- chunk {"id": "body-0009", "role": "body", "section": "A puzzling numerical experiment", "weight": 1.0} -->

To recover $f$ from partial Fourier samples, we find a solution $f^{\sharp}$ to the optimization problem In a nutshell, given partial observation ${\hat{f}}_{|\Omega}$, we seek a solution $f^{\sharp}$ with minimum complexity---here Total Variation (TV)---and whose 'visible' coefficients match those of the unknown object $f$. Our hope here is to partially erase some of the artifacts classical reconstruction methods exhibit (which tend to have large TV norm) while maintaining fidelity to the observed data via the constraints on the Fourier coefficients of the reconstruction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "A puzzling numerical experiment", "weight": 1.0} -->

When we use (1.1) for the recovery problem illustrated in Figure 1 (with the popular Logan-Shepp phantom as a test image), the results are surprising. The reconstruction is exact; that is, $f^{\sharp} = f$! Now this numerical result is not special to this phantom. In fact, we performed a series of experiments of this type and obtained perfect reconstruction on many similar test phantoms.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Main Results", "weight": 1.0} -->

This paper is about a quantitative understanding of this very special phenomenon. For which classes of signals/images can we expect perfect reconstruction? What are the trade-offs between complexity and number of samples? In order to answer these questions, we first develop a fundamental mathematical understanding of a special one-dimensional model problem; we then exhibit reconstruction strategies which are shown to exactly reconstruct the unknown signal and can be deployed in many related and sophisticated reconstruction setups.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Main Results", "weight": 1.0} -->

For a signal $f \in \text{C}^{N}$, we define the classical discrete transform Fourier transform ${{\mathcal{F}f} = \hat{f}}:{\text{C}^{N}\rightarrow\text{C}^{N}}$ by If we are given the value of the Fourier coefficients $\hat{f}{(k)}$ for all frequencies $k \in {\mathbb{Z}}_{N}$, then one can obviously reconstruct $f$ exactly via the Fourier inversion formula Now suppose that we are only given the Fourier coefficients ${\hat{f}|}_{\Omega}$ sampled in some partial subset $\Omega \subsetneq {\mathbb{Z}}_{N}$ of all frequencies (here and below we abuse notations and identify the frequencies $\omega_{k} = {{2\pik}/N}$ with the corresponding integers whenever convenient).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main Results", "weight": 1.0} -->

Of course, this is not enough information by itself to reconstruct $f$ exactly, since $f$ has $N$ degrees of freedom and we are only specifying ${|\Omega|} < N$ of those degrees (here and below $|\Omega|$ denotes the cardinality of $\Omega$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "For Almost Every $\\Omega$", "weight": 1.0} -->

As the theorem suggests, there exist sets $\Omega$ and functions $f$ for which the $\ell_{1}$-minimization procedure does not recover $f$ correctly, even if $|{\text{supp}{(f)}}|$ is much smaller than $|\Omega|$. We sketch two counter-examples: Dirac's comb. Suppose that $N$ is a perfect square and consider the picket-fence signal which consists of spikes of unit height and with uniform spacing equal to $\sqrt{N}$. This signal is often used as an extremal point for uncertainty principles as one of its remarkable properties is its invariance through the Fourier transform. Hence suppose that $\Omega$ is the set of all frequencies but the multiples of $\sqrt{N}$, namely, ${|\Omega|} = {N - \sqrt{N}}$. Then ${\hat{f}|}_{\Omega} = 0$ and obviously the reconstruction is identically zero.

<!-- chunk {"id": "body-0015", "role": "body", "section": "For Almost Every $\\Omega$", "weight": 1.0} -->

Note that the problem here does not really have anything to do with $\ell_{1}$-minimization per se; $f$ cannot be reconstructed from its Fourier samples on $\Omega$ thereby showing that Theorem 1.1 does not work 'as is' for arbitrary sample sizes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "For Almost Every $\\Omega$", "weight": 1.0} -->

Box signals. The example above suggests that in some sense $|T|$ must not be greater than about $\sqrt{|\Omega|}$. In fact, there exist more extreme examples. Assume the sample size $N$ is large and consider for example the indicator function $f$ of the interval $T:={\{ t:{{- N^{- 0.01}} < t < N^{0.01}}\}}$ and let $\Omega$ be the set $\Omega:={\{ k:{{N/3} < k < {{2N}/3}}\}}$. Let $h$ be a function whose Fourier transform $\hat{h}$ is a non-negative bump function adapted to the interval $\{ k:{{- {N/6}} < k < {N/6}}\}$ which equals 1 when ${- {N/12}} < k < {N/12}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "For Almost Every $\\Omega$", "weight": 1.0} -->

Then ${|{h{(t)}}|}^{2}$ has Fourier transform vanishing in $\Omega$, and is rapidly decreasing away from $t = 0$; in particular we have ${|{h{(t)}}|}^{2} = {O{(N^{- 100})}}$ for $t \notin T$. On the other hand, one easily computes that ${|{h{}}|}^{2} > c$ for some absolute constant $c > 0$. Because of this, the signal $f - {\varepsilon{|h|}^{2}}$ will have smaller $\ell_{1}$-norm than $f$ for $\varepsilon > 0$ sufficiently small (and $N$ sufficiently large), while still having the same Fourier coefficients as $f$ on $\Omega$. Thus in this case $f$ is not the minimizer to the problem $(P_{1})$, despite the fact that the support of $f$ is much smaller than that of $\Omega$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "For Almost Every $\\Omega$", "weight": 1.0} -->

The above counterexamples relied heavily on the special choice of $\Omega$ (and to a lesser extent of $\text{supp}{(f)}$); in particular, it needed the fact that the complement of $\Omega$ contained a large interval (or more generally, a long arithmetic progression). But for most sets $\Omega$, large arithmetic progressions in the complement do not exist, and the problem largely disappears. In short, Theorem 1.3 essentially says is that for most sets ${|T|} \sim {|\Omega|}$, the inequality holds.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Extensions", "weight": 1.0} -->

As mentioned earlier, results on our model problem extend easily to higher dimensions as well as to other setups. To be concrete consider the problem of recovering a one-dimensional piecewise constant signal via where we adopt the convention that ${g{({- 1})}} = {g{({N - 1})}}$. In a nutshell, model (1.5) is obtained from (1.10) after differentiation. Indeed, let $\delta$ be the vector of first difference ${\delta{(t)}} = {{g{(t)}} - {g{({t - 1})}}}$, and note that ${\sum{\delta{(t)}}} = 0$. Obviously, and, therefore, with ${\upsilon{(\omega)}} = {({1 - e^{- {i\omega}}})}^{- 1}$, the problem is identical to which is precisely what we have been studying.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Relationship to Uncertainty Principles", "weight": 1.0} -->

From a certain point of view, our results are connected to the so-called uncertainty principles which say that it is difficult to localize a signal $f \in \text{C}^{N}$ both in time and frequency at the same time. Indeed, classical arguments show that $f$ is the unique minimizer of $(P_{1})$ if and only if Put $T = {\text{supp}{(f)}}$ and apply the triangle inequality Hence, a sufficient condition to establish that $f$ is our unique solution would be to show that or equivalently ${{\sum_{T}{{|{h{(t)}}|}{<\frac{1}{2}\parallel}h}}\parallel}_{\ell_{1}}$. The connection with the uncertainty principle is now explicit; $f$ is the unique minimizer if it is impossible to 'concentrate' half of the $\ell_{1}$ norm of a signal that is missing frequency components in $\Omega$ on a 'small' set $T$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Relationship to Uncertainty Principles", "weight": 1.0} -->

For example, guarantees exact reconstruction if Take ${|\Omega|} < {N/2}$, then that condition says that $|T|$ must be zero which, of course, is far from being the content of Theorem 1.3. In truth, this paper does not follow this classical approach. Instead, we will use duality theory to study the solution of $(P_{1})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Robust Uncertainty Principles", "weight": 1.0} -->

Underlying our analysis is a new notion of uncertainty principle which holds for almost any pair $({\text{supp}{(f)}},{\text{supp}{(\hat{f})}})$. With $T = {\text{supp}{(f)}}$ and $\Omega = {\text{supp}{(\hat{f})}}$, the classical discrete uncertainty principle says that with equality obtained for signals such as the Dirac's comb. As we mentioned above, such extremal signals correspond to very special pairs $(T,\Omega)$. However, for most choices of $T$ and $\Omega$, the analysis presented in this paper shows that it is impossible to find $f$ such that $T = {\text{supp}{(f)}}$ and $\Omega = {\text{supp}{(\hat{f})}}$ unless which is considerably stronger than (1.11).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robust Uncertainty Principles", "weight": 1.0} -->

Here, the statement 'most pairs' says again that the probability of selecting a random pair $(T,\Omega)$ violating (1.12) is at most $O{(N^{- M})}$. (We are of course aware of numerical studies in pointing out the lack of sharpness of the uncertainty principle when $T$ is random.)

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robust Uncertainty Principles", "weight": 1.0} -->

In some sense, (1.12) is the typical uncertainty relation one can generally expect (as opposed to (1.11)), hence, justifying the title of this paper. Because of space limitation, we are unable to belaborate on this fact and its implications any further, but will do so in a companion paper.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

The idea of relaxing a combinatorial problem into a convex problem is not new and goes back a long way. For example, used the idea of minimizing $\ell_{1}$ norms to recover spike trains. The motivation is that this makes available a host of computationally feasible procedures. For example, a convex problem of the type (1.5) can be practically solved using techniques of linear programming such as interior point methods.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

Now, there exists some evidence that in special situations the unique solution to an $\ell_{1}$ minimization problem coincides with that of the unique minimizer of the $\ell_{0}$ problem. For example, a series of beautiful papers is concerned with a special setup where one is given a dictionary $D$ of vectors (waveforms) of $\text{C}^{N}$, $D = {(d_{k})}_{1 \leq k \leq M}$ and one seeks sparse representations of a signal $f \in \text{C}^{N}$ as a superposition of elements of $D$ Suppose that the number of elements $M$ from $D$ is greater than the sample size $N$, then there are many ways in which one can represent $f$ as a superposition of elements from $D$ and one would want to find the 'sparsest' one.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

Consider the solution which minimizes the $\ell_{0}$ norm of $\alpha$ subject to the constraint (1.13) and that which minimizes the $\ell_{1}$ norm. A typical result of this body of work is as follows: suppose that $s$ can be synthesized out of very few elements from $D$, then the solution to both problems are unique and are equal. We also refer to for very recent results along these lines.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

This literature certainly influenced our thinking in the sense it made us suspect that results such as Theorem 1.3 were actually possible. However, we would like to emphasize that the claims presented in this paper are of a substantially different nature. We give essentially two reasons: First, our model problem is different since we need to 'guess' a signal from incomplete data, as opposed to finding the sparsest expansion of a fully specified signal.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

And second, our approach is decidedly probabilistic---as opposed to deterministic---and thus calls for very different techniques. For example, underlying our analysis are delicate estimates about the size of random matrices, which may be of independent interest.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

Besides the wonderful properties of $\ell_{1}$, there is a second line of research connected to our findings. We can think of recovering a sparse superposition of spikes from an incomplete set of observations in the Fourier domain as a spectral estimation problem proviso swapping time and frequency: $\hat{f}$ is a superposition of a few complex sinusoids whose frequency and amplitude we need to determine from a few samples. From this point of view, our work is related to and where the authors study sampling patterns allowing the exact reconstruction of a signal. These references show that the locations and amplitudes of a sequence of $|T|$ spikes can be recovered exactly from ${2{|T|}} + 1$ consecutive Fourier coefficients (in for example, the recovery requires solving a system of equations and factoring a polynomial). Our results, namely, Theorems 1.1 and 1.3 are quite distinct and far more general since they address the radically different situation in which we do not have the freedom to choose the samples at our convenience.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connections with existing work", "weight": 1.0} -->

Finally, it is interesting to note that our results and the references above are also related to recent work in finding near-best $B$-term Fourier approximations (which is in some sense the dual to our recovery problem). The algorithm, which operates by estimating the frequencies present in the signal from a small number of randomly placed samples, produces with high probability an approximation in sublinear time with error within a constant of the best $B$-term approximation. First, in the samples are again selected to be equispaced whereas we are not at liberty to choose the frequency samples at all since they are specified a priori. And second, we wish to produce as a result an entire signal or image of size $N$, so a sublinear algorithm is an impossibility.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Strategy", "weight": 1.0} -->

It is clear that at least one minimizer to $(P_{1})$ exists. On the other hand, it is not apparent why this minimizer should be unique, and why it should equal $f$. In this section, we outline our strategy for answering these questions. Using duality theory, we will be able to derive necessary and sufficient conditions for $(P_{1})$ to recover $f$. We note that a similar duality approach was independently developed in for finding sparse approximations from general dictionaries.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Duality", "weight": 1.0} -->

To get a feel for the line of argumentation, consider first the case where $f$ is real-valued. Then (1.5) can be written as the linear program where ${g^{+}{(t)}} = {\max{({g{(t)}},0)}}$, ${g^{-}{(t)}} = {- {\min{({g{(t)}},0)}}}$, and the matrix $\mathcal{F}_{\Omega}$ contains only the rows of the Fourier transform matrix corresponding to entries in $\Omega$. The corresponding Lagrangian is with ${\mu^{+},\mu^{-}} \geq 0$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Duality", "weight": 1.0} -->

In fact, for $f$ to be the unique minimizer of (2.1), it is necessary and sufficient for there to exist a $\lambda$ such that for ${P{(t)}} = {{({\mathcal{F}_{\Omega}^{\ast}\lambda})}{(t)}}$, we have Thus, to show that $f^{\sharp}$ is unique and is equal to $f$, it suffices to find a trigonometric polynomial $P$ whose Fourier transform is supported in $\Omega$---in other words, which only uses frequencies in $\Omega$---and which matches $\text{sgn}{(f)}$ on $\text{supp}{(f)}$, and has magnitude strictly less than 1 elsewhere. The following lemma generalizes for the case where $f$ is complex-valued.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

Equipped with our duality theorem, we are now in a position to present the main ideas of the argument. Fix $f$. We may assume that ${\tauN} > {M{\log N}}$ since the claim is vacuous otherwise (as we will see, ${\alpha{(M)}} = {O{({1/M})}}$ and thus (1.9) will force $f \equiv 0$, at which point it is clear that the solution to $(P_{1})$ is equal to $f = 0$).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

We let $T \subset {\mathbb{Z}}_{N}$ denote the support of $f$, $T:={\text{supp}{(f)}}$. Let $\Omega$ be the random set defined by (1.7). Since ${\tauN} > {M{\log N}}$, a typical application of the large deviation theorem shows that the cardinality of $\Omega$ is if course close to that of its expected value, e.g.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

Slightly more precise estimates are possible, see. It then follows that In the sequel it will be convenient to denote by $B_{M}$ the event $\{{{|\Omega|} < {{({1 - \epsilon_{M}})}{|{\tauN}|}}}\}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

In light of Lemma 2.1, it suffices ---with probability $1 - {O{(N^{- M})}}$--- to show that the matrix $\mathcal{F}_{{\text{supp}{(f)}}\rightarrow\Omega}$ has full rank, and construct a trigonometric polynomial $P{(t)}$, $0 \leq t \leq {N - 1}$, whose Fourier transform is supported on $\Omega$, matches $\text{sgn}{(f)}$ on $T$, and has magnitude strictly less than 1 outside of $T$. To do this we shall need some auxiliary linear transformations (i.e. matrices) as we will see next.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

The key point is that the terms in (2.10) are rather oscillatory, since we have stripped out the non-oscillatory diagonal $t = t'$; indeed, the main idea of the argument will be to use the randomization of $\Omega$ to treat $H$ as a "white noise" operator whose eventual effect will be negligible, especially if $H$ is raised to a high power.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

To see the relevance of the operator $H$ to our problem, observe that for all $f \in {\ell^{2}{(T)}}$ with $\hat{f}{(\omega)}$ the Fourier coefficient of $f$ evaluated at the frequency $\omega$. In particular, ${({\iota - {\frac{1}{|\Omega|}H}})}f$ has Fourier transform supported in $\Omega$. Next, suppose for the moment that the self-adjoint operator ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ from $\ell^{2}{(T)}$ to itself is invertible, and then set $P{(t)}$, $0 \leq t \leq {N - 1}$, to be the trigonometric polynomial Then by the preceding discussion: Frequency support. $P$ has Fourier transform supported in $\Omega$; Spatial interpolation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

Consider now the invertibility issue. By definition Hence, the invertibility of ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ implies that $\mathcal{F}_{T\rightarrow\Omega}$ be injective. In summary, to prove the theorem it will suffice to show that: Invertibility. The operator ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ is invertible (with probability $1 - {O{(N^{- M})}}$).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Architecture of the Argument", "weight": 1.0} -->

We first consider the former claim.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Invertibility", "weight": 1.0} -->

We would like to establish invertibility of the matrix ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ with high probability. One obvious way to proceed would be to show that the operator norm or equivalently the largest eigenvalue of $\iota^{\ast}H$ is less than $|\Omega|$. This is easily done if $|{\text{supp}{(f)}}|$ is extremely small (e.g. much less than $\sqrt{|\Omega|}$), simply by estimating the operator norm directly by the Frobenius norm $\parallel \cdot \parallel_{F}$, which is easy to compute explicitly. Recall that for any squared matrix $M$, the Frobenius norm ${\| M\|}_{F}$ of $M$ is defined by the formula and obeys ${\| M\|} \leq {\| M\|}_{F}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Invertibility", "weight": 1.0} -->

However, this simple approach does not work well when $|{\text{supp}{(f)}}|$ is large, say equal to $\alpha \cdot {({\log N})}^{- 1} \cdot {|\Omega|}$. In this case, we have to resort to estimating the Frobenius norm of a large power of $\iota^{\ast}H$, taking advantage of cancellations arising from the randomness of the matrix coefficients of $\iota^{\ast}H$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Invertibility", "weight": 1.0} -->

We state the key estimate of this section.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Magnitude of the polynomial on the complement of $T$", "weight": 1.0} -->

We first develop an expression for $P{(t)}$ by making use of the algebraic identity Indeed, we can write so that the inverse is given by the truncated Neumann series The point is that the remainder term $R$ is quite small in the Frobenius norm: suppose that ${\|{\iota^{\ast}H}\|}_{F} \leq {\alpha \cdot {|\Omega|}}$, then In particular, the matrix coefficients of $R$ are all individually less than $\alpha^{n}/{({1 - \alpha^{n}})}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Magnitude of the polynomial on the complement of $T$", "weight": 1.0} -->

Introduce the $\ell_{\infty}$-norm of a matrix as ${\| M\|}_{\infty} = {\sup_{{\| x\|}_{\infty} \leq 1}{\|{Mx}\|}_{\infty}}$ which is also given by Now, it follows from the Cauchy-Schwarz inequality that where $\#M{(\text{col})}$ is of course the number of columns of $M$. This observation gives the crude estimate As we shall soon see, the bound (3.8) allows us to effectively neglect the $R$ term in this formula; the only remaining difficulty will be to establish good bounds on the truncated Neumann series $\frac{1}{|\Omega|}H{\sum_{m = 0}^{n - 1}{\frac{1}{{|\Omega|}^{m}}{({\iota^{\ast}H})}^{m}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Estimating the truncated Neumann series", "weight": 1.0} -->

Fix $t \in T^{c}$ and write $P_{0}{(t)}$ as The idea is to use moment estimates to control the size of each term $X_{m}{(t)}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

Recall that $H_{0}{(t,t')}$, ${t,t'} \in T$, is the ${|T|} \times {|T|}$ matrix whose entries are defined by A diagonal element of the $2n$th power of $H_{0}$ may be expressed as where we adopt the convention that $t_{{2n} + 1} = t_{1}$ whenever convenient and, therefore, Using (1.7) and linearity of expectation, we can write this as The idea is to use the independence of the $I_{\{{\omega_{j} \in \Omega}\}}$'s to simplify this expression substantially; however, one has to be careful with the fact that some of the $\omega_{j}$'s may be the same, at which point one loses independence of those indicator variables. These difficulties require a certain amount of notation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

Note that there is a partial ordering on the equivalence relations as one can say that $\sim_{1} \leq \sim_{2}$ if $\sim_{1}$ is coarser than $\sim_{2}$, i.e. $a \sim_{2}b$ implies $a \sim_{1}b$ for all ${a,b} \in A$. Thus, the coarsest element in $\mathcal{P}{(A)}$ is the trivial equivalence relation in which all elements of $A$ are equivalent (just one equivalence class), while the finest element is the equality relation $=$, i.e. each element of $A$ belongs to a distinct class ($|A|$ equivalence classes).

<!-- chunk {"id": "body-0051", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

Now, let us return to the computation of the expected value. Because the random variables $I_{k}$ (1.6) are independent and have all the same distribution, the quantity $\text{E}{\lbrack{\prod_{j = 1}^{2n}I_{\omega_{j}}}\rbrack}$ depends only on the equivalence relation $\sim_{\mathbf{ω}}$ and not on the value of $\mathbf{ω}$ itself. Indeed, we have where $A/ \sim$ denotes the equivalence classes of $\sim$. Thus we can rewrite the preceding expression as where $\sim$ ranges over all equivalence relations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

We would like to pause here and consider (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")). Take $n = 1$, for example.

<!-- chunk {"id": "body-0053", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

There are only two equivalent classes on $\{ 1,2\}$ and, therefore, the right hand-side is equal to Our goal is to rewrite the expression inside the brackets so that the exclusion $\omega_{1} \neq \omega_{2}$ does not appear any longer, i.e. we would like to rewrite the sum over ${{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}}:{\omega_{1} \neq \omega_{2}}$ in terms of sums over ${{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}}:{\omega_{1} = \omega_{2}}$, and over ${\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}$. In this special case, this is quite easy as The motivation is quite clear.

<!-- chunk {"id": "body-0054", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

Removing the exclusion allows to rewrite sums as product, e.g. and each factor is equal to either $N$ or $0$ depending on whether $t_{1} = t_{2}$ or not.

<!-- chunk {"id": "body-0055", "role": "body", "section": "First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$", "weight": 1.0} -->

The next section generalizes these ideas and develop an identity, which allows us to rewrite sums over $\Omega{( \sim )}$ in terms of sums over $\Omega_{\leq}{( \sim )}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Stirling Numbers", "weight": 1.0} -->

As emphasized earlier, our goal is to use our inclusion-exclusion formula to rewrite the sum (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) as a sum over $\Omega_{\leq}{( \sim )}$. In order to do this, it is best to introduce another element of combinatorics, which will prove to be very useful.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Stirling Numbers", "weight": 1.0} -->

For any ${n,k} \geq 0$, we define the Stirling number of the second kind $S{(n,k)}$ to be the number of equivalence relations on a set of $n$ elements which have exactly $k$ equivalence classes, thus Thus for instance ${S{}} = {S{}} = {S{}} = {S{}} = 1$, ${S{}} = 3$, and so forth. We observe the basic recurrence This simply reflects the fact that if $a$ is an element of $A$ and $\sim$ is an equivalence relation on $A$ with $k$ equivalence classes, then either $a$ is not equivalent to any other element of $A$ (in which case $\sim$ has $k - 1$ equivalence classes on $A\backslash{\{ a\}}$), or $a$ is equivalent to one of the $k$ equivalence classes of $S\backslash{\{ a\}}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Stirling Numbers", "weight": 1.0} -->

We now need an identity for the Stirling numbers^11^1We found this identity by modifying a standard generating function identity for the Stirling numbers which involved the polylogarithm. It can also be obtained from the formula ${S{(n,k)}} = {\frac{1}{k!}{\sum_{i = 0}^{k - 1}{{({- 1})}^{i}\binom{k}{i}{({k - i})}^{n}}}}$, which can be verified inductively from (4.6)..

<!-- chunk {"id": "body-0059", "role": "body", "section": "Second Formula for the Expected Value of the Trace of $H_{0}^{2n}$", "weight": 1.0} -->

Let us return to (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")). The inner sum of (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) can be rewritten as with ${f{({\mathbf{ω}})}}:=e^{i{\sum_{1 \leq j \leq {2n}}{\omega_{j}{({t_{j} - t_{j + 1}})}}}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "First Bound on $\\text{E}{\\lbrack{\\text{Tr}{(H_{0}^{2n})}}\\rbrack}$", "weight": 1.0} -->

Let $\sim$ be an equivalence which does not contain any singleton. Then the following inequality holds To see why this is true, observe that as linear combinations of $t_{1},\ldots,t_{2n}$, the expressions $t_{j} - t_{j + 1}$ are all linearly independent of each other except for the constraint ${{\sum_{j = 1}^{2n}t_{j}} - t_{j + 1}} = 0$. Thus we have $|A/ \sim | - 1$ independent constraints in the above sum, and so the number of $t$'s obeying the constraints is bounded by ${|T|}^{2n - |A/ \sim | + 1}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "First Bound on $\\text{E}{\\lbrack{\\text{Tr}{(H_{0}^{2n})}}\\rbrack}$", "weight": 1.0} -->

All the equivalence classes in the sum (4.11) are without singletons as otherwise $t_{A'} \neq 0$. Thus, for ${n,k} \geq 0$, we let $P{(n,k)}$ be the number of equivalence classes on a set of $n$ elements which have exactly $k$ equivalence classes and no singletons There is a simple recursion on these numbers, namely, which is valid for all ${n,k} \geq 0$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "First Bound on $\\text{E}{\\lbrack{\\text{Tr}{(H_{0}^{2n})}}\\rbrack}$", "weight": 1.0} -->

This simply reflects the fact that if $\alpha$ is an element of $A$ and $\sim$ is an equivalence relation on $A$ with $k$ equivalence classes, then either $\alpha$ belongs to a class which has only one other element $\beta$ of $A$ (in which case $\sim$ has $k - 1$ equivalence classes and no singleton on $A\backslash{\{\alpha,\beta\}}$), or $\alpha$ is equivalent to one of the $k$ equivalence classes of $A\backslash{\{\alpha\}}$, each of which having at least two elements.

<!-- chunk {"id": "body-0063", "role": "body", "section": "First Bound on $\\text{E}{\\lbrack{\\text{Tr}{(H_{0}^{2n})}}\\rbrack}$", "weight": 1.0} -->

With these notations, we established The following lemma provides an upper bound on those $P{(n,k)}$'s.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

We start with a useful and classical lemma.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments in order to derive empirical bounds on $|T|$ relative to $|\Omega|$ for a signal $f$ supported on $T$ to be the unique minimizer of $(P_{1})$. The results can be viewed as a set of practical guidelines for situations where one can expect perfect recovery from partial Fourier information using convex optimization.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Our experiments are of the following form: Choose constants $N$ (the length of the signal), $N_{t}$ (the number of spikes in the signal), and $N_{\omega}$ (the number of observed frequencies).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Randomly generate the subdomain $T$ by sampling $\{ 0,\ldots,{N - 1}\}$ $N_{t}$ times without replacement (we have ${|T|} = N_{t}$).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Randomly generate $f$ by setting ${{f{(t)}} = 0},{t \in T^{c}}$ and drawing both the real and imaginary parts of ${{f{(t)}},t} \in T$ from independent Gaussian distributions with mean zero and variance one^22^2The results here, as in the rest of the paper, seem to rely only on the sets $T$ and $\Omega$. The actual values that $f$ takes on $T$ can be arbitrary; choosing them to be random emphasizes this. Figures 2 remain the same if we take ${{f{(t)}} = 1},{t \in T}$, say..

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Randomly generate the subdomain $\Omega$ of observed frequencies by again sampling $\{ 0,\ldots,{N - 1}\}$ $N_{\omega}$ times without replacement (${|\Omega|} = N_{\omega}$).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Solve $(P_{1})$, and compare the solution to $f$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The $\ell_{1}$-norm is not strictly convex, so solving $(P_{1})$ using a Newton-type method that relies on local quadratic approximations of $\parallel \cdot \parallel_{\ell_{1}}$ is problematic. Instead, we use a very simple gradient descent with projection algorithm. The number of iterations needed for convergence is high (on the order of $10^{5}$), but since we can rapidly project onto the constraint set (using two fast Fourier transforms), each iteration takes a short amount of time. As an indication, the algorithm typically converges in less than $10$ seconds on a standard desktop computer for signals of length $N = 1024$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

One source of slack in the theoretical analysis is the way in which we choose the polynomial $P{(t)}$ (as in (2.11)). Theorem 2.1 states that $f$ is a minimizer of $(P_{1})$ if and only if there exists any trigonometric polynomial that has ${{P{(t)}} = {\text{sgn}{(f)}{(t)}}},{t \in T}$ and ${{|{P{(t)}}|} < 1},{t \in T^{c}}$. In (2.11) we choose $P{(t)}$ that minimizes the $\ell_{2}$ norm on $T^{c}$ under the linear constraints ${{P{(t)}} = {\text{sgn}{(f)}{(t)}}},{t \in T}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

However, the condition ${|{P{(t)}}|} < 1$ suggests that a minimal $\ell_{\infty}$ choice would be more appropriate (but is seemingly intractable analytically).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

As a final example of the effectiveness of this recovery framework, we show two more results of the type presented in Section 1.1; piecewise constant phantoms reconstructed from Fourier samples on a star. The phantoms, along with the minimum energy and minimum total-variation reconstructions (which are exact), are shown in Figure 4. Note that the total-variation reconstruction is able to recover very subtle image features; for example, both the short and skinny ellipse in the upper right hand corner of Figure 4(d) and the very faint ellipse in the bottom center are preserved. (We invite the reader to check for related types of experiments.)

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

We would like to close this paper by offering a few comments about the results obtained in this paper and by discussing the possibility of generalizations and extensions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Stability", "weight": 1.0} -->

In the introduction section, we argued that even if one knew the support $T$ of $f$, the reconstruction might be unstable. Indeed with knowledge of $T$, a reasonable strategy might be to recover $f$ by the method of least-squares, namely, In practice, the matrix inversion might be problematic. Now observe that with the notations of this paper Hence, for stability we would need ${\frac{1}{|\Omega|}H_{0}} \leq {1 - \delta}$ for some $\delta > 0$. This is of course exactly the problem we studied, compare Theorem 3.3. In fact, selecting $\alpha_{M}$ as suggested in the proof of our main theorem (see section 3.4) gives ${\frac{1}{|\Omega|}H_{0}} \leq.42$ with probability at least $1 - {O{(N^{- M})}}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Stability", "weight": 1.0} -->

This shows that selecting $|T|$ as to obey (1.9), ${|T|} \approx {{|\Omega|}/{\log N}}$ actually provides stability.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Robustness", "weight": 1.0} -->

An important question concerns the robustness of the reconstruction procedure vis a vis measurement errors. For example, we might want to consider the model problem which says that instead of observing the Fourier coefficients of $f$, one is given those of $f + h$ where $h$ is some small perturbation. Then one might still want to reconstruct $f$ via In this setup, of course, one cannot expect exact recovery. Instead, one would like to know whether or not our reconstruction strategy is well-behaved or more precisely, how far is the minimizer $f^{\sharp}$ from the true object $f$. In short, what is the typical size of the error? Our preliminary calculations suggest that the reconstruction is robust in the sense that the error ${\|{f - f^{\sharp}}\|}_{1}$ is small for small perturbations $h$ obeying ${\| h\|}_{1} \leq \delta$, say. We hope to be able to report on these early findings in a follow-up paper.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Extensions", "weight": 1.0} -->

Finally, work in progress shows that similar exact reconstruction phenomena hold for other synthesis/measurement pairs. Suppose one is given a pair of of bases $(\mathcal{B}_{1},\mathcal{B}_{2})$ and randomly selected coefficients of an object $f$ in one basis, say $\mathcal{B}_{2}$. (From this broader viewpoint, the special cases discussed in this paper assume that $\mathcal{B}_{1}$ is the canonical basis of ${\mathbb{R}}^{N}$ or ${\mathbb{R}}^{N} \times {\mathbb{R}}^{N}$ (spikes in 1D, 2D), or is the basis of Heavysides as in the Total-variation reconstructions, and $\mathcal{B}_{2}$ is the standard 1D, 2D Fourier basis.) Then, it seems that $f$ can be recovered exactly provided that it may be synthesized as a sparse superposition of elements in $\mathcal{B}_{1}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Extensions", "weight": 1.0} -->

The relationship between the number of nonzero terms in $\mathcal{B}_{1}$ and the number of observed coefficients depends upon the incoherence between the two bases. The more incoherent, the fewer coefficients needed. Again, we hope to report on such extensions in a separate publication.
