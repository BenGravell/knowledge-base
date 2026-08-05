<!-- arxiv-full-text:v1 {"arxiv_id": "math/0409186", "source": "ar5iv"} -->

## Introduction

In many applications of practical interest, we often wish to reconstruct an object (a discrete signal, a discrete image, etc.) from incomplete Fourier samples. In a discrete setting, we may pose the problem as follows; let $\hat{f}$ be the Fourier transform of a discrete object $f{(t)}$, $t \in {\mathbb{Z}}_{N}^{d}:={\{ 0,1,\ldots,{N - 1}\}}^{d}$, The problem is then to recover $f$ from partial frequency information, namely, from $\hat{f}{(\omega)}$, where $\omega = {(\omega_{1},\ldots,\omega_{d})}$ belongs to some set $\Omega$ of cardinality less than $N^{d}$---the size of the discrete object.

In this paper, we show that we can recover $f$ exactly from observations ${\hat{f}|}_{\Omega}$ on small set of frequencies provided that $f$ is sparse. The recovery consists of solving a straightforward optimization problem that finds $f^{\sharp}$ of minimal complexity with ${{\hat{f}}^{\sharp}{(\omega)}} = {\hat{f}{(\omega)}}$, ${\forall\omega} \in \Omega$.

### A puzzling numerical experiment

This idea is best motivated by an experiment with surprisingly positive results. Consider a simplified version of the classical 'tomography' problem in medical imaging: we wish to reconstruct a 2D image $f{(t_{1},t_{2})}$ from samples ${\hat{f}|}_{\Omega}$ of its discrete Fourier transform on a star-shaped domain $\Omega$. Our choice of domain is not contrived; many real imaging devices can collect high-resolution samples along radial lines at relatively few angles. Figure 1(b) illustrates a typical case where one gathers $512$ samples along each of $22$ radial lines.

Figure 1: Example of a simple recovery problem. (a) The Logan-Shepp phantom test image. (b) Sampling ’domain’ in the frequency plane; Fourier coefficients are sampled along 22 approximately radial lines. (c) Minimum energy reconstruction obtained by setting unobserved Fourier coefficients to zero. (d) Reconstruction obtained by minimizing the total-variation, as in (1.1). The reconstruction is an exact replica of the image in (a).

Frequently discussed approaches in the literature of medical imaging for reconstructing an object from 'polar' frequency samples are the so-called filtered backprojection algorithms. In a nutshell, one assumes that the Fourier coefficients at all of the unobserved frequencies are zero (thus reconstructing the image of "minimal energy" under the observation constraints). This strategy does not perform very well, and could hardly be used for medical diagnostic. The reconstructed image, shown in Figure 1(c), has severe nonlocal artifacts caused by the angular undersampling. A good reconstruction algorithm, it seems, would have to guess the values of the missing Fourier coefficients. In other words, one would need to interpolate $\hat{f}{(\omega_{1},\omega_{2})}$. This is highly problematic, however; predictions of Fourier coefficients from their neighbors are very delicate, due to the global and highly oscillatory nature of the Fourier transform. Going back to our example, we can see the problem immediately. To recover frequency information near $(\omega_{1},\omega_{2})$, where $\omega_{1}$ is near $\pm \pi$, we would need to interpolate $\hat{f}$ at the Nyquist rate ${2\pi}/N$. However, we only have samples at rate about $\pi/22$; the sampling rate is almost $50$ times smaller than the Nyquist rate!

We propose instead a strategy based on convex optimization. Let ${\| g\|}_{BV}$ be the total-variation norm of a two-dimensional object $g$ which for discrete data $g{(t_{1},t_{2})}$, ${0 \leq t_{1}},{t_{2} \leq {N - 1}}$, takes the form where $D_{1}$ is the finite difference ${D_{1}g} = {{g{(t_{1},t_{2})}} - {g{({t_{1} - 1},t_{2})}}}$ and ${D_{2}g} = {{g{(t_{1},t_{2})}} - {g{(t_{1},{t_{2} - 1})}}}$. To recover $f$ from partial Fourier samples, we find a solution $f^{\sharp}$ to the optimization problem In a nutshell, given partial observation ${\hat{f}}_{|\Omega}$, we seek a solution $f^{\sharp}$ with minimum complexity---here Total Variation (TV)---and whose 'visible' coefficients match those of the unknown object $f$. Our hope here is to partially erase some of the artifacts classical reconstruction methods exhibit (which tend to have large TV norm) while maintaining fidelity to the observed data via the constraints on the Fourier coefficients of the reconstruction.

When we use (1.1) for the recovery problem illustrated in Figure 1 (with the popular Logan-Shepp phantom as a test image), the results are surprising. The reconstruction is exact; that is, $f^{\sharp} = f$! Now this numerical result is not special to this phantom. In fact, we performed a series of experiments of this type and obtained perfect reconstruction on many similar test phantoms.

### Main Results

This paper is about a quantitative understanding of this very special phenomenon. For which classes of signals/images can we expect perfect reconstruction? What are the trade-offs between complexity and number of samples? In order to answer these questions, we first develop a fundamental mathematical understanding of a special one-dimensional model problem; we then exhibit reconstruction strategies which are shown to exactly reconstruct the unknown signal and can be deployed in many related and sophisticated reconstruction setups.

For a signal $f \in \text{C}^{N}$, we define the classical discrete transform Fourier transform ${{\mathcal{F}f} = \hat{f}}:{\text{C}^{N}\rightarrow\text{C}^{N}}$ by If we are given the value of the Fourier coefficients $\hat{f}{(k)}$ for all frequencies $k \in {\mathbb{Z}}_{N}$, then one can obviously reconstruct $f$ exactly via the Fourier inversion formula Now suppose that we are only given the Fourier coefficients ${\hat{f}|}_{\Omega}$ sampled in some partial subset $\Omega \subsetneq {\mathbb{Z}}_{N}$ of all frequencies (here and below we abuse notations and identify the frequencies $\omega_{k} = {{2\pik}/N}$ with the corresponding integers whenever convenient). Of course, this is not enough information by itself to reconstruct $f$ exactly, since $f$ has $N$ degrees of freedom and we are only specifying ${|\Omega|} < N$ of those degrees (here and below $|\Omega|$ denotes the cardinality of $\Omega$).

Suppose, however, that we also specify that $f$ is supported on a small (but a priori unknown) subset $T$ of ${\mathbb{Z}}_{N}$; that is, we assume that $f$ can be written as a sparse superposition of spikes If $|T|$ is small enough, we can recover $f$ exactly:

### Theorem 1.1

Suppose that the signal length $N$ is a prime integer. Let $\Omega$ be a subset of $\{ 0,\ldots,{N - 1}\}$, and let $f$ be a vector supported on $T$ such that Then $f$ can be reconstructed uniquely from $\Omega$ and ${\hat{f}|}_{\Omega}$. Conversely, if $\Omega$ is not the set of all $N$ frequencies, then there exist distinct vectors $f,g$ such that ${{|{\text{supp}{(f)}}|},{|{\text{supp}{(g)}}|}} \leq {{\frac{1}{2}{|\Omega|}} + 1}$ and such that ${\hat{f}|}_{\Omega} = {\hat{g}|}_{\Omega}$.

Proof We will need the following lemma, from which we see that with knowledge of $T$, we can reconstruct $f$ uniquely (using linear algebra) from ${\hat{f}|}_{\Omega}$:

### Lemma 1.2

(, Corollary 1.4) Let $N$ be a prime integer and $T,\Omega$ be subsets of ${\mathbb{Z}}_{N}$. Put $\ell_{2}{(T)}$ (resp. $\ell_{2}{(\Omega)}$) to be the space of signals that are zero outside of $T$ (resp. $\Omega$). The restricted Fourier transform $\mathcal{F}_{T\rightarrow\Omega}:{{\ell_{2}{(T)}}\rightarrow{\ell_{2}{(\Omega)}}}$ is defined as If ${|T|} = {|\Omega|}$, then $\mathcal{F}_{T\rightarrow\Omega}$ is a bijection; as a consequence, we thus see that $\mathcal{F}_{T\rightarrow\Omega}$ is injective for ${|T|} \leq {|\Omega|}$ and surjective for ${|T|} \geq {|\Omega|}$. Clearly, the same claims hold if the Fourier transform $\mathcal{F}$ is replaced by the inverse Fourier transform $\mathcal{F}^{- 1}$.

To prove Theorem 1.1, we start with the former claim. Suppose for contradiction that there were two objects $f,g$ such that ${\hat{f}|}_{\Omega} = {\hat{g}|}_{\Omega}$ and ${{|{\text{supp}{(f)}}|},{|{\text{supp}{(g)}}|}} \leq {\frac{1}{2}{|\Omega|}}$. Then the Fourier transform of $f - g$ vanishes on $\Omega$, and ${|{\text{supp}{({f - g})}}|} \leq {|\Omega|}$. By Lemma 1.2 we see that $\mathcal{F}_{{\text{supp}{({f - g})}}\rightarrow\Omega}$ is injective, and thus ${f - g} = 0$. The uniqueness claim follows.

Now we prove the latter claim. Since ${|\Omega|} < N$, we can find disjoint subsets $T,S$ of $\Omega$ such that ${{|T|},{|S|}} \leq {{\frac{1}{2}{|\Omega|}} + 1}$ and ${{|T|} + {|S|}} = {{|\Omega|} + 1}$. Let $k_{0}$ be some frequency which does not lie in $\Omega$. Applying Lemma 1.2, we have that $\mathcal{F}_{{T \cup S}\rightarrow{\Omega \cup {\{ k_{0}\}}}}$ is a bijection, and thus we can find a vector $h$ supported on $T \cup S$ whose Fourier transform vanishes on $\Omega$ but is non-zero on $k_{0}$; in particular, $h$ is not identically zero. The claim now follows by taking $f:={h|}_{T}$ and $g:={- {h|}_{S}}$.

Note that if $N$ is not prime, the lemma (and hence the theorem) fails, essentially because of the presence of non-trivial subgroups of ${\mathbb{Z}}_{N}$ with addition modulo $N$; see, for further discussion. However, it is plausible to think that Lemma 1.2 continues to hold for non-prime $N$ if $T$ and $\Omega$ are assumed to be generic - in particular, they are not subgroups of ${\mathbb{Z}}_{N}$, or cosets of subgroups. If $T$ and $\Omega$ are selected uniformly at random, then it is expected that the theorem holds with probability very close to one; one can indeed presumably quantify this statement by adapting the arguments given above but we will not do so here. However, we refer the reader to section 1.6 for a rapid presentation of informal arguments pointing out in this direction.

A refinement of the argument in Theorem 1.1 shows that for fixed sets $T$, $S$, $\Omega$ in ${\mathbb{Z}}_{N}$, the space of vectors $f,g$ supported on $T$, $S$ such that ${\hat{f}|}_{\Omega} = {\hat{g}|}_{\Omega}$ has dimension ${|{T \cup S}|} - {|\Omega|}$ when ${|{T \cup S}|} \geq {|\Omega|}$, and has dimension $|{T \cap S}|$ otherwise. In particular, if we let $\Sigma{(N_{t})}$ denote those vectors whose support has size at most $N_{t}$, then set of the vectors in $\Sigma{(N_{t})}$ which cannot be reconstructed uniquely in this class from the Fourier coefficients sampled at $\Omega$, is contained in a finite union of linear spaces of dimension at most ${2N_{t}} - {|\Omega|}$. Since $\Sigma{(N_{t})}$ itself is a finite union of linear spaces of dimension $N_{t}$, we thus see that recovery of $f$ from ${\hat{f}|}_{\Omega}$ is in principle possible generically whenever ${|{\text{supp}{(f)}}|} = N_{t} < {|\Omega|}$; once $N_{t} \geq {|\Omega|}$, however, it is clear from simple degrees-of-freedom arguments that unique recovery is no longer possible. While our methods do not quite attain this theoretical upper bound for correct recovery, our numerical experiements suggest that they do come within a constant factor of this bound (see Figure 2).

Theorem 1.1 asserts that $f$ can be reconstructed from ${\hat{f}|}_{\Omega}$ if ${|T|} \leq {{|\Omega|}/2}$ (and that this bound is the best possible). In principle, we can recover $f$ exactly by solving the combinatorial optimization problem where ${\| g\|}_{\ell_{0}}$ is the number of nonzero terms $\#{\{{{t,{g{(t)}}} \neq 0}\}}$. Solving (1.4) directly is infeasible even for modest-sized signals. The algorithm would let $T$ run over all subsets of $\{ 0,\ldots,{N - 1}\}$ of cardinality ${|T|} \leq {\frac{1}{2}{|\Omega|}}$ and for each $T$, checking whether $f$ was in the range of $\mathcal{F}_{T\rightarrow\Omega}$ or not, and then inverting the relevant minor of the Fourier matrix to recover $f$ once $T$ was determined. It is well-known that this procedure would clearly be very computationally expensive, however, since there are exponentially many subsets to check; for instance, for ${|\Omega|} \sim {N/2}$, this number scales like $4^{N} \cdot 3^{- {{3N}/4}}$! As an aside comment, note that it is not clear how to make this algorithm robust, especially since the results in do not provide any effective lower bound on the determinant of the minors of the Fourier matrix, see section 6 for a discussion of this point.

A more computationally efficient strategy for recovering $f$ from $\Omega$ and ${\hat{f}|}_{\Omega}$ is to solve the convex problem The key result in this paper is that the solutions to $(P_{0})$ and $(P_{1})$ are equivalent for an overwhelming percentage of the choices for $T$ and $\Omega$ with ${|T|} \leq {{\alpha \cdot {|\Omega|}}/{\log N}}$ ($\alpha > 0$ is a constant): in these cases, solving the convex problem $(P_{1})$ recovers $f$ exactly.

To establish this upper bound, we will assume that the observed Fourier coefficients are randomly sampled. To make this precise, we introduce a probability parameter $0 < \tau < 1$, and consider the sequence ${(I_{k})}_{1 \leq k \leq N}$ of independent Bernoulli random variables We then define the random set of frequencies $\Omega$ as Clearly, $|\Omega|$ follows the binomial distribution and In fact, classical large deviations arguments (or the central limit theorem) tell us that with high probability, the size of $|\Omega|$ is very close to $\tauN$. Our main theorem can now be stated as follows.

### Theorem 1.3

Let $f \in \text{C}^{N}$ be a discrete signal and $\Omega$ be the random set defined in (1.7). For a given accuracy parameter $M$, if $f$ is supported on $T$ and then with probability at least $1 - {O{(N^{- M})}}$, the minimizer to the problem (1.5) is unique and is equal to $f$.

In light of (1.8) we see that (1.9) is essentially ${|T|} \sim {|\Omega|}$, modulo a constant and a logarithmic factor. Indeed, an easy modification to the second part of Theorem 1.1 shows that the condition (1.9) cannot be weakened to (for instance) ${|{\text{supp}{(f)}}|} \leq {{({\frac{1}{2} + \varepsilon})}\tauN}$, for any $\epsilon > 0$. The paper gives an explicit value of $\alpha{(M)}$, namely, ${\alpha{(M)}} \asymp {1/{\lbrack{29.6{({M + 1})}}\rbrack}}$ although we have not pursued the question of exactly what the optimal value might be.

In Section 5, we present numerical results which suggest that in practice, we can expect to recover $f$ more than $50\%$ of the time if ${|T|} \leq {{|\Omega|}/4}$. For ${|T|} \leq {{|\Omega|}/8}$, the recovery rate is above $90\%$. Empircally, the constants $1/4$ and $1/8$ do not seem to vary for $N$ in the range of a few hundred to a few thousand.

### For Almost Every $\Omega$

As the theorem suggests, there exist sets $\Omega$ and functions $f$ for which the $\ell_{1}$-minimization procedure does not recover $f$ correctly, even if $|{\text{supp}{(f)}}|$ is much smaller than $|\Omega|$. We sketch two counter-examples: Dirac's comb. Suppose that $N$ is a perfect square and consider the picket-fence signal which consists of spikes of unit height and with uniform spacing equal to $\sqrt{N}$. This signal is often used as an extremal point for uncertainty principles as one of its remarkable properties is its invariance through the Fourier transform. Hence suppose that $\Omega$ is the set of all frequencies but the multiples of $\sqrt{N}$, namely, ${|\Omega|} = {N - \sqrt{N}}$. Then ${\hat{f}|}_{\Omega} = 0$ and obviously the reconstruction is identically zero.

Note that the problem here does not really have anything to do with $\ell_{1}$-minimization per se; $f$ cannot be reconstructed from its Fourier samples on $\Omega$ thereby showing that Theorem 1.1 does not work 'as is' for arbitrary sample sizes.

Box signals. The example above suggests that in some sense $|T|$ must not be greater than about $\sqrt{|\Omega|}$. In fact, there exist more extreme examples. Assume the sample size $N$ is large and consider for example the indicator function $f$ of the interval $T:={\{ t:{{- N^{- 0.01}} < t < N^{0.01}}\}}$ and let $\Omega$ be the set $\Omega:={\{ k:{{N/3} < k < {{2N}/3}}\}}$. Let $h$ be a function whose Fourier transform $\hat{h}$ is a non-negative bump function adapted to the interval $\{ k:{{- {N/6}} < k < {N/6}}\}$ which equals 1 when ${- {N/12}} < k < {N/12}$. Then ${|{h{(t)}}|}^{2}$ has Fourier transform vanishing in $\Omega$, and is rapidly decreasing away from $t = 0$; in particular we have ${|{h{(t)}}|}^{2} = {O{(N^{- 100})}}$ for $t \notin T$. On the other hand, one easily computes that ${|{h{}}|}^{2} > c$ for some absolute constant $c > 0$. Because of this, the signal $f - {\varepsilon{|h|}^{2}}$ will have smaller $\ell_{1}$-norm than $f$ for $\varepsilon > 0$ sufficiently small (and $N$ sufficiently large), while still having the same Fourier coefficients as $f$ on $\Omega$. Thus in this case $f$ is not the minimizer to the problem $(P_{1})$, despite the fact that the support of $f$ is much smaller than that of $\Omega$.

The above counterexamples relied heavily on the special choice of $\Omega$ (and to a lesser extent of $\text{supp}{(f)}$); in particular, it needed the fact that the complement of $\Omega$ contained a large interval (or more generally, a long arithmetic progression). But for most sets $\Omega$, large arithmetic progressions in the complement do not exist, and the problem largely disappears. In short, Theorem 1.3 essentially says is that for most sets ${|T|} \sim {|\Omega|}$, the inequality holds.

### Extensions

As mentioned earlier, results on our model problem extend easily to higher dimensions as well as to other setups. To be concrete consider the problem of recovering a one-dimensional piecewise constant signal via where we adopt the convention that ${g{({- 1})}} = {g{({N - 1})}}$. In a nutshell, model (1.5) is obtained from (1.10) after differentiation. Indeed, let $\delta$ be the vector of first difference ${\delta{(t)}} = {{g{(t)}} - {g{({t - 1})}}}$, and note that ${\sum{\delta{(t)}}} = 0$. Obviously, and, therefore, with ${\upsilon{(\omega)}} = {({1 - e^{- {i\omega}}})}^{- 1}$, the problem is identical to which is precisely what we have been studying.

### Corollary 1.4

Put $T = {\{{{t,{f{(t)}}} \neq {f{({t - 1})}}}\}}$. Under the assumptions of Theorem 1.3, the minimizer to the problem (1.10) is unique and is equal $f$ with probability at least $1 - {O{(N^{- M})}}$---provided, of course, that $f$ be adjusted so that ${\sum{f{(t)}}} = {\hat{f}{}}$.

We now explore versions of Theorem 1.3 in higher dimensions. To be concrete, consider the two-dimensional situation (statements in arbitrary dimensions are exactly of the same flavor):

### Theorem 1.5

Put $N = n^{2}$. We let ${{{f{(t_{1},t_{2})}},1} \leq t_{1}},{t_{2} \leq n}$ be a discrete signal and $\Omega$ be the random set defined as in (1.7). Assume that for a given accuracy parameter $M$, $f$ is supported on $T$ obeying (1.9). Then with probability at least $1 - {O{(N^{- M})}}$, the minimizer to the problem (1.5) is unique and is equal to $f$.

We will not prove this result as the strategy is exactly parallel to that of Theorem 1.3. Just as in the one-dimensional case, a similar statement for piecewise constant functions exists provided, of course, that the support of $f$ be replaced by $\{{(t_{1},t_{2})}:{{{|{D_{1}f{(t_{1},t_{2})}}|}^{2} + {|{D_{2}f{(t_{1},t_{2})}}|}^{2}} \neq 0}\}$. We omit the details.

We hope that we managed to suggest that there actually are a variety of results similar to Theorem 1.3, and we only selected a few instances. As a matter of fact, those provide a precise quantitative understanding of the 'surprising result' discussed at the beginning of this paper.

### Relationship to Uncertainty Principles

From a certain point of view, our results are connected to the so-called uncertainty principles which say that it is difficult to localize a signal $f \in \text{C}^{N}$ both in time and frequency at the same time. Indeed, classical arguments show that $f$ is the unique minimizer of $(P_{1})$ if and only if Put $T = {\text{supp}{(f)}}$ and apply the triangle inequality Hence, a sufficient condition to establish that $f$ is our unique solution would be to show that or equivalently ${{\sum_{T}{{|{h{(t)}}|}{<\frac{1}{2}\parallel}h}}\parallel}_{\ell_{1}}$. The connection with the uncertainty principle is now explicit; $f$ is the unique minimizer if it is impossible to 'concentrate' half of the $\ell_{1}$ norm of a signal that is missing frequency components in $\Omega$ on a 'small' set $T$. For example, guarantees exact reconstruction if Take ${|\Omega|} < {N/2}$, then that condition says that $|T|$ must be zero which, of course, is far from being the content of Theorem 1.3. In truth, this paper does not follow this classical approach. Instead, we will use duality theory to study the solution of $(P_{1})$.

### Robust Uncertainty Principles

Underlying our analysis is a new notion of uncertainty principle which holds for almost any pair $({\text{supp}{(f)}},{\text{supp}{(\hat{f})}})$. With $T = {\text{supp}{(f)}}$ and $\Omega = {\text{supp}{(\hat{f})}}$, the classical discrete uncertainty principle says that with equality obtained for signals such as the Dirac's comb. As we mentioned above, such extremal signals correspond to very special pairs $(T,\Omega)$. However, for most choices of $T$ and $\Omega$, the analysis presented in this paper shows that it is impossible to find $f$ such that $T = {\text{supp}{(f)}}$ and $\Omega = {\text{supp}{(\hat{f})}}$ unless which is considerably stronger than (1.11). Here, the statement 'most pairs' says again that the probability of selecting a random pair $(T,\Omega)$ violating (1.12) is at most $O{(N^{- M})}$. (We are of course aware of numerical studies in pointing out the lack of sharpness of the uncertainty principle when $T$ is random.)

In some sense, (1.12) is the typical uncertainty relation one can generally expect (as opposed to (1.11)), hence, justifying the title of this paper. Because of space limitation, we are unable to belaborate on this fact and its implications any further, but will do so in a companion paper.

### Connections with existing work

The idea of relaxing a combinatorial problem into a convex problem is not new and goes back a long way. For example, used the idea of minimizing $\ell_{1}$ norms to recover spike trains. The motivation is that this makes available a host of computationally feasible procedures. For example, a convex problem of the type (1.5) can be practically solved using techniques of linear programming such as interior point methods.

Now, there exists some evidence that in special situations the unique solution to an $\ell_{1}$ minimization problem coincides with that of the unique minimizer of the $\ell_{0}$ problem. For example, a series of beautiful papers is concerned with a special setup where one is given a dictionary $D$ of vectors (waveforms) of $\text{C}^{N}$, $D = {(d_{k})}_{1 \leq k \leq M}$ and one seeks sparse representations of a signal $f \in \text{C}^{N}$ as a superposition of elements of $D$ Suppose that the number of elements $M$ from $D$ is greater than the sample size $N$, then there are many ways in which one can represent $f$ as a superposition of elements from $D$ and one would want to find the 'sparsest' one. Consider the solution which minimizes the $\ell_{0}$ norm of $\alpha$ subject to the constraint (1.13) and that which minimizes the $\ell_{1}$ norm. A typical result of this body of work is as follows: suppose that $s$ can be synthesized out of very few elements from $D$, then the solution to both problems are unique and are equal. We also refer to for very recent results along these lines.

This literature certainly influenced our thinking in the sense it made us suspect that results such as Theorem 1.3 were actually possible. However, we would like to emphasize that the claims presented in this paper are of a substantially different nature. We give essentially two reasons: First, our model problem is different since we need to 'guess' a signal from incomplete data, as opposed to finding the sparsest expansion of a fully specified signal.

And second, our approach is decidedly probabilistic---as opposed to deterministic---and thus calls for very different techniques. For example, underlying our analysis are delicate estimates about the size of random matrices, which may be of independent interest.

Besides the wonderful properties of $\ell_{1}$, there is a second line of research connected to our findings. We can think of recovering a sparse superposition of spikes from an incomplete set of observations in the Fourier domain as a spectral estimation problem proviso swapping time and frequency: $\hat{f}$ is a superposition of a few complex sinusoids whose frequency and amplitude we need to determine from a few samples. From this point of view, our work is related to and where the authors study sampling patterns allowing the exact reconstruction of a signal. These references show that the locations and amplitudes of a sequence of $|T|$ spikes can be recovered exactly from ${2{|T|}} + 1$ consecutive Fourier coefficients (in for example, the recovery requires solving a system of equations and factoring a polynomial). Our results, namely, Theorems 1.1 and 1.3 are quite distinct and far more general since they address the radically different situation in which we do not have the freedom to choose the samples at our convenience.

Finally, it is interesting to note that our results and the references above are also related to recent work in finding near-best $B$-term Fourier approximations (which is in some sense the dual to our recovery problem). The algorithm , which operates by estimating the frequencies present in the signal from a small number of randomly placed samples, produces with high probability an approximation in sublinear time with error within a constant of the best $B$-term approximation. First, in the samples are again selected to be equispaced whereas we are not at liberty to choose the frequency samples at all since they are specified a priori. And second, we wish to produce as a result an entire signal or image of size $N$, so a sublinear algorithm is an impossibility.

## Strategy

It is clear that at least one minimizer to $(P_{1})$ exists. On the other hand, it is not apparent why this minimizer should be unique, and why it should equal $f$. In this section, we outline our strategy for answering these questions. Using duality theory, we will be able to derive necessary and sufficient conditions for $(P_{1})$ to recover $f$. We note that a similar duality approach was independently developed in for finding sparse approximations from general dictionaries.

### Duality

To get a feel for the line of argumentation, consider first the case where $f$ is real-valued. Then (1.5) can be written as the linear program where ${g^{+}{(t)}} = {\max{({g{(t)}},0)}}$, ${g^{-}{(t)}} = {- {\min{({g{(t)}},0)}}}$, and the matrix $\mathcal{F}_{\Omega}$ contains only the rows of the Fourier transform matrix corresponding to entries in $\Omega$. The corresponding Lagrangian is with ${\mu^{+},\mu^{-}} \geq 0$. At a minimum $({\overset{\sim}{g}}^{+},{\overset{\sim}{g}}^{-})$, there will be a saddle point in $L$, and we will have Then for $f$ to be the minimum of (2.1), we need with ${\mu^{+},\mu^{-}} \geq 0$. In fact, for $f$ to be the unique minimizer of (2.1), it is necessary and sufficient for there to exist a $\lambda$ such that for ${P{(t)}} = {{({\mathcal{F}_{\Omega}^{\ast}\lambda})}{(t)}}$, we have Thus, to show that $f^{\sharp}$ is unique and is equal to $f$, it suffices to find a trigonometric polynomial $P$ whose Fourier transform is supported in $\Omega$---in other words, which only uses frequencies in $\Omega$---and which matches $\text{sgn}{(f)}$ on $\text{supp}{(f)}$, and has magnitude strictly less than 1 elsewhere. The following lemma generalizes for the case where $f$ is complex-valued.

### Lemma 2.1

Let $\Omega \subset {\mathbb{Z}}_{N}$. For a vector $f \in \text{C}^{N}$, define the 'sign' vector $\text{sgn}{(f)}$ by ${\text{sgn}{(f)}{(t)}}:={{f{(t)}}/{|{f{(t)}}|}}$ when $t \in {\text{supp}{(f)}}$ and ${\text{sgn}{(f)}} = 0$ otherwise. Suppose there exists a vector $P$ whose Fourier transform $\hat{P}$ is supported in $\Omega$ such that Then if $\mathcal{F}_{{\text{supp}{(f)}}\rightarrow\Omega}$ is injective, the minimizer $f^{\sharp}$ to the problem $(P_{1})$ (1.5) is unique and is equal to $f$.

Conversely, if $f$ is the unique minimizer of $(P_{1})$, then there exists a vector $P$ with the above properties.

Proof We may assume that $\Omega$ is non-empty and that $f$ is non-zero since the claims are trivial otherwise.

Suppose first that such a function $P$ exists. Let $g$ be any vector not equal to $f$ with ${\hat{g}|}_{\Omega} = {\hat{f}|}_{\Omega}$. Write $h:={g - f}$, then $\hat{h}$ vanishes on $\Omega$. Observe that for any $t \in {\text{supp}{(f)}}$ we have while for $t \notin {\text{supp}{(f)}}$ we have ${|{g{(t)}}|} = {|{h{(t)}}|} \geq {\text{Re}{({h{(t)}\overline{P{(t)}}})}}$ since ${|{P{(t)}}|} < 1$. Thus However, the Parseval's formula gives since $\hat{P}$ is supported on $\Omega$ and $\hat{h}$ vanishes on $\Omega$. Thus ${\| g\|}_{\ell_{1}} \geq {\| f\|}_{\ell_{1}}$. Now we check when equality can hold, i.e. when ${\| g\|}_{\ell_{1}} = {\| f\|}_{\ell_{1}}$. An inspection of the above argument shows that this forces ${|{h{(t)}}|} = {\text{Re}{({h{(t)}\overline{P{(t)}}})}}$ for all $t \notin {\text{supp}{(f)}}$. Since ${|{P{(t)}}|} < 1$, this forces $h$ to vanish outside of $\text{supp}{(f)}$. Since $\hat{h}$ vanishes on $\Omega$, we thus see that $h$ must vanish identically (this follows from the assumption about the injectivity of $\mathcal{F}_{{\text{supp}{(f)}}\rightarrow\Omega}$) and so $g = f$. This shows that $f$ is the unique minimizer $f^{\sharp}$ to the problem (1.5).

Conversely, suppose that $f = f^{\sharp}$ is the unique minimizer to (1.5). Without loss of generality we may normalize ${\| f\|}_{\ell_{1}} = 1$. Then the closed unit ball $B:={\{ g:{{\| g\|}_{\ell_{1}} \leq 1}\}}$ and the affine space $V:={\{ g:{{\hat{g}|}_{\Omega} = {\hat{f}|}_{\Omega}}\}}$ intersect at exactly one point, namely $f$. By the Hahn-Banach theorem we can thus find a function $P$ such that the hyperplane $\Gamma_{1}:={\{ g:{{\sum{\text{Re}{({g{(t)}\overline{P{(t)}}})}}} = 1}\}}$ contains $V$, and such that the half-space $\Gamma_{\leq 1}:={\{ g:{{\sum{\text{Re}{({g{(t)}\overline{P{(t)}}})}}} \leq 1}\}}$ contains $B$. By perturbing the hyperplane if necessary (and using the uniqueness of the intersection of $B$ with $V$) we may assume that $\Gamma_{1} \cap B$ is contained in the minimal facet of $B$ which contains $f$, namely $\{{g \in B}:{{\text{supp}{(g)}} \subseteq {\text{supp}{(f)}}}\}$.

Since $B$ lies in $\Gamma_{\leq 1}$, we see that ${\sup_{t}{|{P{(t)}}|}} \leq 1$; since $f \in {\Gamma_{1} \cap B}$, we have ${P{(t)}} = {\text{sgn}{(f)}{(t)}}$ when $t \in {\text{supp}{(f)}}$. Since $\Gamma_{1} \cap B$ is contained in the minimal facet of $B$ containing $f$, we see that ${|{P{(t)}}|} < 1$ when $t \notin {\text{supp}{(f)}}$. Since $\Gamma_{1}$ contains $V$, we see from Parseval that $\hat{P}$ is supported in $\Omega$. The claim follows.

Since the space of functions with Fourier transform supported in $\Omega$ has $|\Omega|$ degrees of freedom, and the condition that $P$ match $\text{sgn}{(f)}$ on $\text{supp}{(f)}$ requires $|{\text{supp}{(f)}}|$ degrees of freedom, one now expects heuristically (if one ignores the open conditions that $P$ has magnitude strictly less than 1 outside of $\text{supp}{(f)}$) that $f^{\sharp}$ should be unique and be equal to $f$ whenever ${|{\text{supp}{(f)}}|} \ll {|\Omega|}$; in particular this gives an explicit procedure for recovering $f$ from $\Omega$ and ${\hat{f}|}_{\Omega}$.

### Architecture of the Argument

Equipped with our duality theorem, we are now in a position to present the main ideas of the argument. Fix $f$. We may assume that ${\tauN} > {M{\log N}}$ since the claim is vacuous otherwise (as we will see, ${\alpha{(M)}} = {O{({1/M})}}$ and thus (1.9) will force $f \equiv 0$, at which point it is clear that the solution to $(P_{1})$ is equal to $f = 0$).

We let $T \subset {\mathbb{Z}}_{N}$ denote the support of $f$, $T:={\text{supp}{(f)}}$. Let $\Omega$ be the random set defined by (1.7). Since ${\tauN} > {M{\log N}}$, a typical application of the large deviation theorem shows that the cardinality of $\Omega$ is if course close to that of its expected value, e.g.

Slightly more precise estimates are possible, see. It then follows that In the sequel it will be convenient to denote by $B_{M}$ the event $\{{{|\Omega|} < {{({1 - \epsilon_{M}})}{|{\tauN}|}}}\}$.

In light of Lemma 2.1, it suffices ---with probability $1 - {O{(N^{- M})}}$--- to show that the matrix $\mathcal{F}_{{\text{supp}{(f)}}\rightarrow\Omega}$ has full rank, and construct a trigonometric polynomial $P{(t)}$, $0 \leq t \leq {N - 1}$, whose Fourier transform is supported on $\Omega$, matches $\text{sgn}{(f)}$ on $T$, and has magnitude strictly less than 1 outside of $T$. To do this we shall need some auxiliary linear transformations (i.e. matrices) as we will see next.

In this section, we will work with vectors restricted to the set $T$ and it will be convenient to let $\ell_{2}{(T)}$ denote the subspace of such restrictions (and similarly ${\ell_{2}{({\mathbb{Z}}_{N})}}:=\text{C}^{N}$). With these notations, we let $H:{{\ell^{2}{(T)}}\rightarrow{\ell_{2}{({\mathbb{Z}}_{N})}}}$ denote the linear transform defined by Let $\iota:{{\ell^{2}{(T)}}\rightarrow{\ell_{2}{({\mathbb{Z}}_{N})}}}$ be the obvious embedding of $\ell^{2}{(T)}$ into $\ell_{2}{({\mathbb{Z}}_{N})}$ (extending by zero outside of $T$), and let $\iota^{\ast}:{{\ell_{2}{({\mathbb{Z}}_{N})}}\rightarrow{\ell^{2}{(T)}}}$ be the dual restriction map, thus ${\iota^{\ast}f}:={f|}_{T}$. Observe that ${\iota^{\ast}\iota}:{{\ell^{2}{(T)}}\rightarrow{\ell^{2}{(T)}}}$ is simply the identity operator on $\ell^{2}{(T)}$, and that the operator ${\iota^{\ast}H}:{{\ell^{2}{(T)}}\rightarrow{\ell^{2}{(T)}}}$ is self-adjoint.

The key point is that the terms in (2.10) are rather oscillatory, since we have stripped out the non-oscillatory diagonal $t = t'$; indeed, the main idea of the argument will be to use the randomization of $\Omega$ to treat $H$ as a "white noise" operator whose eventual effect will be negligible, especially if $H$ is raised to a high power.

To see the relevance of the operator $H$ to our problem, observe that for all $f \in {\ell^{2}{(T)}}$ with $\hat{f}{(\omega)}$ the Fourier coefficient of $f$ evaluated at the frequency $\omega$. In particular, ${({\iota - {\frac{1}{|\Omega|}H}})}f$ has Fourier transform supported in $\Omega$. Next, suppose for the moment that the self-adjoint operator ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ from $\ell^{2}{(T)}$ to itself is invertible, and then set $P{(t)}$, $0 \leq t \leq {N - 1}$, to be the trigonometric polynomial Then by the preceding discussion: Frequency support. $P$ has Fourier transform supported in $\Omega$; Spatial interpolation. $P$ obeys and so $P$ agrees with $\text{sgn}{(f)}$ on $T$.

Consider now the invertibility issue. By definition Hence, the invertibility of ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ implies that $\mathcal{F}_{T\rightarrow\Omega}$ be injective. In summary, to prove the theorem it will suffice to show that: Invertibility. The operator ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ is invertible (with probability $1 - {O{(N^{- M})}}$).

Magnitude on $T^{c}$. The function $P$ defined in (2.11) obeys the bound ${\sup_{t \in T^{c}}{|{P{(t)}}|}} < 1$ (with probability $1 - {O{(N^{- M})}}$).

We first consider the former claim.

## Construction of the Dual Polynomial

### Invertibility

We would like to establish invertibility of the matrix ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ with high probability. One obvious way to proceed would be to show that the operator norm or equivalently the largest eigenvalue of $\iota^{\ast}H$ is less than $|\Omega|$. This is easily done if $|{\text{supp}{(f)}}|$ is extremely small (e.g. much less than $\sqrt{|\Omega|}$), simply by estimating the operator norm directly by the Frobenius norm $\parallel \cdot \parallel_{F}$, which is easy to compute explicitly. Recall that for any squared matrix $M$, the Frobenius norm ${\| M\|}_{F}$ of $M$ is defined by the formula and obeys ${\| M\|} \leq {\| M\|}_{F}$. However, this simple approach does not work well when $|{\text{supp}{(f)}}|$ is large, say equal to $\alpha \cdot {({\log N})}^{- 1} \cdot {|\Omega|}$. In this case, we have to resort to estimating the Frobenius norm of a large power of $\iota^{\ast}H$, taking advantage of cancellations arising from the randomness of the matrix coefficients of $\iota^{\ast}H$.

We state the key estimate of this section.

### Theorem 3.1

Put $H_{0} = {\iota^{\ast}H}$ for short, where $H$ is the operator defined by (2.10). Set $c_{\tau}:={e{\log{({{({1 - \tau})}/\tau})}}}$ and let In most interesting situations $a_{n}$ is less than $b_{n}$ which allows slightly to reformulate (3.1). Note that the classical Stirling approximation to $n!$ gives and, therefore, letting $\phi$ be the 'golden ratio' $\phi:={{({1 + \sqrt{5}})}/2}$, the $2n$th moment obeys provided that $a_{n}$ obeys Theorem 3.1 gives a precise estimate about the operator norm of $H_{0}$. To see why this is true, assume that (3.3) holds; since $H_{0}$ is self-adjoint Now selecting $n = {\lceil{\log{|T|}}\rceil}$ so that Formalizing matters, we proved

### Corollary 3.2

Suppose ${|T|} \leq {{({\log{|{\tauN}|}})}^{- 1}{|{\tauN}|}}$. Then for any $\epsilon > 0$, we have Proof The Markov inequality above bounds the probability by ${({1 + \epsilon})}^{- {2n}}$ which goes to zero as $n = {\lceil{\log{|T|}}\rceil}$ goes to infinity.

We now return to the study of the invertibility of ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}H_{0}}$. Letting $\alpha$ be a positive number $0 < \alpha < 1$, it follows from the Markov inequality that We then apply inequality (3.1) (recall ${\| H_{0}^{n}\|}_{F}^{2} = {\text{Tr}{(H_{0}^{2n})}}$) and obtain We remark that the last inequality holds for any sample size $|T|$ (proviso the condition (3.3)) and we now specialize (3.4) to selected values of $|T|$.

Suppose that $|T|$ obeys We then have the following result.

### Theorem 3.3

Assume that $\tau \leq.44$, say, and suppose that $T$ obeys (3.5). Then (3.3) holds for any $n \geq 4$, and therefore The only thing to establish is that $T$ obeys (3.3). This is merely technical and the proof is in the Appendix.

With the notations of the previous section and especially (2.9), observe now that where we recall that $B_{M}:={\{{{|\Omega|} < {{({1 - \epsilon_{M}})}{|{\tauN}|}}}\}}$ has probability less than $N^{- M}$. Suppose $T$ obeys (3.5) with $\alpha_{M}:={\alpha{({1 - \epsilon_{M}})}}$ instead of $\alpha$,

### Corollary 3.4

Take $n = {{({M + 1})}{\log N}}$. We see from the Neumann series that the operator ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ is invertible with probability at least $1 - {{({1 + {2/\gamma^{2}}})}N^{- M}}$ since $\iota^{\ast}\iota$ is the identity on vectors supported on $T$.

We have thus established the invertibility of ${\iota^{\ast}\iota} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ with high probability, and thus $P$ is well defined with high probability. It remains to show that ${\sup_{t \notin T}{|{P{(t)}}|}} < 1$ with high probability.

### Magnitude of the polynomial on the complement of $T$

We first develop an expression for $P{(t)}$ by making use of the algebraic identity Indeed, we can write so that the inverse is given by the truncated Neumann series The point is that the remainder term $R$ is quite small in the Frobenius norm: suppose that ${\|{\iota^{\ast}H}\|}_{F} \leq {\alpha \cdot {|\Omega|}}$, then In particular, the matrix coefficients of $R$ are all individually less than $\alpha^{n}/{({1 - \alpha^{n}})}$. Introduce the $\ell_{\infty}$-norm of a matrix as ${\| M\|}_{\infty} = {\sup_{{\| x\|}_{\infty} \leq 1}{\|{Mx}\|}_{\infty}}$ which is also given by Now, it follows from the Cauchy-Schwarz inequality that where $\#M{(\text{col})}$ is of course the number of columns of $M$. This observation gives the crude estimate As we shall soon see, the bound (3.8) allows us to effectively neglect the $R$ term in this formula; the only remaining difficulty will be to establish good bounds on the truncated Neumann series $\frac{1}{|\Omega|}H{\sum_{m = 0}^{n - 1}{\frac{1}{{|\Omega|}^{m}}{({\iota^{\ast}H})}^{m}}}$.

### Estimating the truncated Neumann series

From (2.11) we observe that on the complement of $T$ since the $\iota$ component in (2.11) vanishes outside of $T$. Applying (3.7), we may rewrite $P$ as Let ${a_{0},a_{1}} > 0$ be two numbers with ${a_{0} + a_{1}} = 1$. Then and the idea is to bound each term individually. Put $Q_{0} = {S_{n - 1}\text{sgn}{(f)}}$ so that $P_{1} = {\frac{1}{|\Omega|}HR\iota^{\ast}{({{\text{sgn}{(f)}} + Q_{0}})}}$. With these notations, observe that Hence, bounds on the magnitude of $P_{1}$ will follow from bounds on ${\|{HR}\|}_{\infty}$ together with bounds on the magnitude of $\iota^{\ast}Q_{0}$. It will be of course sufficient to derive bounds on ${\| Q_{0}\|}_{\infty}$ (since ${\|{\iota^{\ast}Q_{0}}\|}_{\infty} \leq {\| Q_{0}\|}_{\infty}$) which will follow from those on $P_{0}$ since $Q_{0}$ is nearly equal to $P_{0}$ (they differ by only one very small term term).

Fix $t \in T^{c}$ and write $P_{0}{(t)}$ as The idea is to use moment estimates to control the size of each term $X_{m}{(t)}$.

### Lemma 3.5

Set $n = {km}$. Then $\text{E}{|{X_{m}{(t_{0})}}|}^{2k}$ obeys the same estimate as that in Theorem 3.1 (up to a multiplicative factor ${|T|}^{- 1}$), namely, where $\gamma$ is as before.

The proof of these moment estimates mimics that of Theorem 3.1 and may be found in the Appendix.

### Lemma 3.6

Fix $a_{0} =.91$. Suppose that $|T|$ obeys (3.5) and let $B_{M}$ be the set where ${|\Omega|} < {{({1 - \epsilon_{M}})} \cdot {|{\tauN}|}}$ with $\epsilon_{M}$ as in (2.9). For each $t \in {\mathbb{Z}}_{N}$, there is a set $A_{t}$ with the property and similarly for $Q_{0}$.

Proof We suppose that $n$ is of the form $n = {2^{J} - 1}$ (this property is not crucial and only simply simplifies our exposition). For each $m$ and $k$ such that ${km} \geq n$, it follows from (3.5) and (3.10) together with some simple calculations that Again ${|\Omega|} \approx {|{\tauN}|}$ and we will develop a bound on the set $B_{M}^{c}$ where ${|\Omega|} \geq {{({1 - \epsilon_{M}})}{|{\tauN}|}}$. On this set Fix $\beta_{j} > 0$, $0 \leq j < J$, such that ${\sum_{j = 0}^{J - 1}{2^{j}\beta_{j}}} \leq a_{0}$. Obviously, where $K_{j} = 2^{J - j}$. Observe that for each $m$ with $2^{j} \leq m < 2^{j + 1}$, $K_{j}m$ obeys $n \leq {K_{j}m} < {2n}$ and, therefore, (3.11) gives For example, taking $\beta_{j}^{- K_{j}}$ to be constant for all $j$, i.e. equal to $\beta_{0}^{- n}$, gives with ${\sum_{j = 0}^{J - 1}{2^{j}\beta_{j}}} \leq a_{0}$. Numerical calculations show that for $\beta_{0} =.42$, ${\sum_{j}{2^{j}\beta_{j}}} \leq.91$ which gives The claim for $Q_{0}$ is, of course, identical and the lemma follows.

### Lemma 3.7

Fix $a_{1} =.09$. Suppose that the pair $(\alpha,N)$ obeys ${{|{\tauN}|}^{3/2}\frac{\alpha^{n}}{1 - \alpha^{n}}} \leq {a_{1}/2}$. Then on the event $A \cap {\{{{\|{\iota^{\ast}H}\|}_{F} \leq {\alpha{|\Omega|}}}\}}$, for some $A$ obeying ${\text{P}{(A)}} \geq {1 - {O{(N^{- M})}}}$.

Proof As we observed before, ${\| P_{1}\|}_{\infty} \leq {{\| H\|}_{\infty}{\| R\|}_{\infty}{({1 + {\| Q_{0}\|}_{\infty}})}}$, and $Q_{0}$ obeys the bound stated in Lemma 3.6. Consider then the event $\{{{\| Q_{0}\|}_{\infty} \leq 1}\}$. On this event, ${\| P_{1}\|} \leq a_{1}$ if ${\frac{1}{|\Omega|}{\| H\|}{\| R\|}_{\infty}} \leq {a_{1}/2}$. The matrix $H$ obeys ${\frac{1}{|\Omega|}{\| H\|}_{\infty}} \leq {|T|}$ since $H$ has $|T|$ columns and each matrix element is bounded by $|\Omega|$ (note that far better bounds are possible). It then follows from (3.8) that with probability at least $1 - {O{(N^{- M})}}$. We then simply need to choose $\alpha$ and $n$ such that the right hand-side is less than $a_{1}/2$.

### Proof of Theorem 1.3

It is now clear that we have assembled all the intermediate results to prove our theorem. Indeed, we proved the invertibility of ${i^{\ast}i} - {\frac{1}{|\Omega|}\iota^{\ast}H}$ with probability $O{(N^{- M})}$ and ${|{P{(t)}}|} < 1$ for all $t \in T^{c}$ (again with high probability), provided that $\alpha$ and $n$ be selected appropriately as we now explain.

Fix $M > 0$. We choose $\alpha =.42$ and $n$ to be the nearest integer to ${({M + 1})}{\log N}$.

From the discussion following Theorem 3.3, it follows that ${i^{\ast}i} - {{|\Omega|}^{- 1}\iota^{\ast}H}$ is invertible with probability $O{(N^{- M})}$.

With this special choice, $\epsilon_{n} = {{2{\lbrack{{({M + 1})}{\log N}}\rbrack}^{2}} \cdot N^{- {({M + 1})}}}$ and, therefore, Lemma 3.6 implies that both $P_{0}$ and $Q_{0}$ are bounded .91 outside of $T^{c}$ with probability at least $1 - {{\lbrack{1 + {2{({{({M + 1})}{\log N}})}^{2}}}\rbrack} \cdot N^{- M}}$.

And finally, to prove that ${|{P_{1}{(t)}}|} <.09$ outside $T^{c}$, Lemma 3.6 assures that it is sufficient to have ${{N^{3/2}\alpha^{n}}/{({1 - \alpha^{n}})}} \leq.045$. Because ${\log{(.42)}} \approx {-.87}$ and ${\log{(.045)}} \approx {- 3.10}$, this condition is approximately equivalent to Take $M \geq 2$, for example; then the above inequality is satisfied as soon as $N \geq 17$.

To conclude, we proved that if $T$ obeys then the reconstruction with probability exceeding $1 - O{({\lbrack{(M + 1)}\log N)}^{2}\rbrack} \cdot N^{- M})$. In other words, we may take $\alpha{(M)}$ in Theorem 1.3 to be of the form

## Moments of Random Matrices

### First Formula for the Expected Value of the Trace of ${(H_{0})}^{2n}$

Recall that $H_{0}{(t,t')}$, ${t,t'} \in T$, is the ${|T|} \times {|T|}$ matrix whose entries are defined by A diagonal element of the $2n$th power of $H_{0}$ may be expressed as where we adopt the convention that $t_{{2n} + 1} = t_{1}$ whenever convenient and, therefore, Using (1.7) and linearity of expectation, we can write this as The idea is to use the independence of the $I_{\{{\omega_{j} \in \Omega}\}}$'s to simplify this expression substantially; however, one has to be careful with the fact that some of the $\omega_{j}$'s may be the same, at which point one loses independence of those indicator variables. These difficulties require a certain amount of notation. We let ${\mathbb{Z}}_{N} = {\{ 0,1,\ldots,{N - 1}\}}$ be the set of all frequencies as before, and let $A$ be the finite set $A:={\{ 1,\ldots,{2n}\}}$. For all ${\mathbf{ω}}:={(\omega_{1},\ldots,\omega_{2n})}$, we define the equivalence relation $\sim_{\mathbf{ω}}$ on $A$ by saying that $j \sim_{\mathbf{ω}}j'$ if and only if $\omega_{j} = \omega_{j'}$. We let $\mathcal{P}{(A)}$ be the set of all equivalence relations on $A$. Note that there is a partial ordering on the equivalence relations as one can say that $\sim_{1} \leq \sim_{2}$ if $\sim_{1}$ is coarser than $\sim_{2}$, i.e. $a \sim_{2}b$ implies $a \sim_{1}b$ for all ${a,b} \in A$. Thus, the coarsest element in $\mathcal{P}{(A)}$ is the trivial equivalence relation in which all elements of $A$ are equivalent (just one equivalence class), while the finest element is the equality relation $=$, i.e. each element of $A$ belongs to a distinct class ($|A|$ equivalence classes).

For each equivalence relation $\sim$ in $\mathcal{P}$, we can then define the sets ${\Omega{(\sim)}} \subset {\mathbb{Z}}_{N}^{2n}$ by and the sets ${\Omega_{\leq}{(\sim)}} \subset {\mathbb{Z}}_{N}^{2n}$ by Thus the sets $\{\Omega{(\sim)}: \sim \in \mathcal{P}\}$ form a partition of ${\mathbb{Z}}_{N}^{2n}$. The sets $\Omega_{\leq}{(\sim)}$ can also be defined as For comparison, the sets $\Omega{(\sim)}$ can be defined as We give an example: suppose $n = 2$ and fix $\sim$ such that $1 \sim 4$ and $2 \sim 3$ (exactly 2 equivalence classes); then ${\Omega{(\sim)}}:={\{{{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{4}}:{{\omega_{1} = \omega_{4}},{{\omega_{2} = \omega_{3}},{{\text{~and~}\omega_{1}} \neq \omega_{2}}}}\}}$ while ${\Omega_{\leq}{(\sim)}}:={\{{{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{4}}:{{\omega_{1} = \omega_{4}},{\omega_{2} = \omega_{3}}}\}}$.

Now, let us return to the computation of the expected value. Because the random variables $I_{k}$ (1.6) are independent and have all the same distribution, the quantity $\text{E}{\lbrack{\prod_{j = 1}^{2n}I_{\omega_{j}}}\rbrack}$ depends only on the equivalence relation $\sim_{\mathbf{ω}}$ and not on the value of $\mathbf{ω}$ itself. Indeed, we have where $A/ \sim$ denotes the equivalence classes of $\sim$. Thus we can rewrite the preceding expression as where $\sim$ ranges over all equivalence relations.

We would like to pause here and consider (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")). Take $n = 1$, for example. There are only two equivalent classes on $\{ 1,2\}$ and, therefore, the right hand-side is equal to Our goal is to rewrite the expression inside the brackets so that the exclusion $\omega_{1} \neq \omega_{2}$ does not appear any longer, i.e. we would like to rewrite the sum over ${{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}}:{\omega_{1} \neq \omega_{2}}$ in terms of sums over ${{\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}}:{\omega_{1} = \omega_{2}}$, and over ${\mathbf{ω}} \in {\mathbb{Z}}_{N}^{2}$. In this special case, this is quite easy as The motivation is quite clear. Removing the exclusion allows to rewrite sums as product, e.g. and each factor is equal to either $N$ or $0$ depending on whether $t_{1} = t_{2}$ or not.

The next section generalizes these ideas and develop an identity, which allows us to rewrite sums over $\Omega{( \sim )}$ in terms of sums over $\Omega_{\leq}{( \sim )}$.

### Inclusion-Exclusion formulae

### Lemma 4.1 (Inclusion-Exclusion principle for equivalence classes)

Let $A$ and $G$ be non-empty finite sets. For any equivalence class $\sim \in \mathcal{P}{(A)}$ on ${\mathbf{ω}} \in G^{|A|}$, we have Thus, for instance, if $A = {\{ 1,2,3\}}$ and $\sim$ is the equality relation, i.e. $j \sim k$ if and only if $j = k$, this identity is saying that where we have omitted the summands $f{(\omega_{1},\omega_{2},\omega_{3})}$ for brevity.

Proof By passing from $A$ to the quotient space $A/ \sim$ if necessary we may assume that $\sim$ is the equality relation $=$. Now relabeling $A$ as $\{ 1,\ldots,n\}$, $\sim_{1}$ as $\sim$, and $A'$ as $A$, it suffices to show that We prove this by induction on $n$. When $n = 1$ both sides are equal to $\sum_{{\mathbf{ω}} \in G}{f{({\mathbf{ω}})}}$. Now suppose inductively that $n > 1$ and the claim has already been proven for $n - 1$. We observe that the left-hand side of (4.4) can be rewritten as where ${\mathbf{ω}}':={(\omega_{1},\ldots,\omega_{n - 1})}$. Applying the inductive hypothesis, this can be written as Now we work on the right-hand side of (4.4). If $\sim$ is an equivalence class on $\{ 1,\ldots,n\}$, let $\sim '$ be the restriction of $\sim$ to $\{ 1,\ldots,{n - 1}\}$. Observe that $\sim$ can be formed from $\sim '$ either by adjoining the singleton set $\{ n\}$ as a new equivalence class (in which case we write $\sim = {\{ \sim ',{\{ n\}}\}}$, or by choosing a $j \in {\{ 1,\ldots,{n - 1}\}}$ and declaring $n$ to be equivalent to $j$ (in which case we write $\sim = {\{ \sim ',{\{ n\}}\}}/{(j = n)}$). Note that the latter construction can recover the same equivalence class $\sim$ in multiple ways if the equivalence class ${\lbrack j\rbrack}_{\sim '}$ of $j$ in $\sim '$ has size larger than 1, however we can resolve this by weighting each $j$ by $\frac{1}{|{\lbrack j\rbrack}_{\sim '}|}$. Thus we have the identity for any complex-valued function $F$ on $\mathcal{P}{({\{ 1,\ldots,n\}})}$. Applying this to the right-hand side of (4.4), we see that we may rewrite this expression as the sum of where we adopt the convention ${\mathbf{ω}}' = {(\omega_{1},\ldots,\omega_{n - 1})}$. But observe that and thus the right-hand side of (4.4) matches (4.5) as desired.

### Stirling Numbers

As emphasized earlier, our goal is to use our inclusion-exclusion formula to rewrite the sum (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) as a sum over $\Omega_{\leq}{( \sim )}$. In order to do this, it is best to introduce another element of combinatorics, which will prove to be very useful.

For any ${n,k} \geq 0$, we define the Stirling number of the second kind $S{(n,k)}$ to be the number of equivalence relations on a set of $n$ elements which have exactly $k$ equivalence classes, thus Thus for instance ${S{}} = {S{}} = {S{}} = {S{}} = 1$, ${S{}} = 3$, and so forth. We observe the basic recurrence This simply reflects the fact that if $a$ is an element of $A$ and $\sim$ is an equivalence relation on $A$ with $k$ equivalence classes, then either $a$ is not equivalent to any other element of $A$ (in which case $\sim$ has $k - 1$ equivalence classes on $A\backslash{\{ a\}}$), or $a$ is equivalent to one of the $k$ equivalence classes of $S\backslash{\{ a\}}$.

We now need an identity for the Stirling numbers^11^1We found this identity by modifying a standard generating function identity for the Stirling numbers which involved the polylogarithm. It can also be obtained from the formula ${S{(n,k)}} = {\frac{1}{k!}{\sum_{i = 0}^{k - 1}{{({- 1})}^{i}\binom{k}{i}{({k - i})}^{n}}}}$, which can be verified inductively from (4.6)..

### Lemma 4.2

For any $n \geq 1$ and $0 \leq \tau < {1/2}$, we have the identity Note that the condition $0 \leq \tau < {1/2}$ ensures that the right-hand side is convergent.

Proof We prove this by induction on $n$. When $n = 1$ the left-hand side is equal to $\tau$, and the right-hand side is equal to as desired. Now suppose inductively that $n \geq 1$ and the claim has already been proven for $n$. Applying the operator ${({\tau^{2} - \tau})}\frac{d}{d\tau}$ to both sides (which can be justified by the hypothesis $0 \leq \tau < {1/2}$) we obtain (after some computation) and the claim follows from (4.6).

We shall refer to the quantity in (4.7) as $F_{n}{(\tau)}$, thus and so forth. When $\tau$ is small we have the approximation ${F_{n}{(\tau)}} \approx {{({- 1})}^{n + 1}\tau}$, which is worth keeping in mind. Some more rigorous bounds in this spirit are as follows.

### Lemma 4.3

Let $n \geq 1$ and $0 \leq \tau < {1/2}$. If $\frac{\tau}{1 - \tau} \leq e^{1 - n}$, then we have ${|{F_{n}{(\tau)}}|} \leq \frac{\tau}{1 - \tau}$. If instead $\frac{\tau}{1 - \tau} > e^{1 - n}$, then Proof Elementary calculus shows that for $x > 0$, the function ${g{(x)}} = \frac{\tau^{x}x^{n - 1}}{{({1 - \tau})}^{x}}$ is increasing for $x < x_{\ast}$ and decreasing for $x > x^{\ast}$, where $x_{\ast}:={{({n - 1})}/{\log\frac{1 - \tau}{\tau}}}$. If $\frac{\tau}{1 - \tau} \leq e^{1 - n}$, then $x_{\ast} \leq 1$, and so the alternating series ${F_{n}{(\tau)}} = {\sum_{k = 1}^{\infty}{{({- 1})}^{n + k}g{(k)}}}$ has magnitude at most ${g{}} = \frac{\tau}{1 - \tau}$. Otherwise the series has magnitude at most and the claim follows.

Roughly speaking, this means that $F_{n}{(\tau)}$ behaves like $\tau$ for $n = {O{({\log{\lbrack{1/\tau}\rbrack}})}}$ and behaves like ${({n/{\log{\lbrack{1/\tau}\rbrack}}})}^{n}$ for $n \gg {\log{\lbrack{1/\tau}\rbrack}}$.

### Second Formula for the Expected Value of the Trace of $H_{0}^{2n}$

Let us return to (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")). The inner sum of (4.2^{2⁢𝑛} ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) can be rewritten as with ${f{({\mathbf{ω}})}}:=e^{i{\sum_{1 \leq j \leq {2n}}{\omega_{j}{({t_{j} - t_{j + 1}})}}}}$. We prove the following useful identity:

### Lemma 4.4

Proof Applying (4.3 ‣ 4.2 Inclusion-Exclusion formulae ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) and rearranging, we may rewrite this as Splitting $A$ into equivalence classes $A'$ of $A/ \sim_{1}$, we observe that splitting $\sim '$ based on the number of equivalence classes $|A'/ \sim '|$, we can write this as by (4.8). Gathering all this together, we have proven the identity (4.9).

We specialize (4.9) to the function ${f{({\mathbf{ω}})}}:={\exp{({i{\sum_{1 \leq j \leq {2n}}{\omega_{j}{({t_{j} - t_{j + 1}})}}}})}}$ and obtain For every equivalence class $A' \in A/ \sim$, let $t_{A'}$ denote the expression $t_{A'}:={\sum_{a \in A'}{({t_{a} - t_{a + 1}})}}$, and let $\omega_{A'}$ denote the expression $\omega_{A'}:=\omega_{a}$ for any $a \in A'$ (these are all equal since ${\mathbf{ω}} \in {\Omega_{\leq}{(\sim)}}$). Then We now see the importance of (4.10) as the inner sum equals ${|{\mathbb{Z}}_{N}|} = N$ when $t_{A'} = 0$ and vanishes otherwise. Hence, we proved the following:

### Lemma 4.5

For every equivalence class $A' \in A/ \sim$, let $t_{A'}:={\sum_{a \in A'}{({t_{a} - t_{a + 1}})}}$. Then This formula will serve as a basis for all of our estimates. In particular, because of the constraint $t_{j} \neq t_{j + 1}$, we see that the summand vanishes if $A/ \sim$ contains any singleton equivalence classes. This means, in passing, that the only equivalence classes which contribute to the sum obey $|A/ \sim | \leq n$.

### First Bound on $\text{E}{\lbrack{\text{Tr}{(H_{0}^{2n})}}\rbrack}$

Let $\sim$ be an equivalence which does not contain any singleton. Then the following inequality holds To see why this is true, observe that as linear combinations of $t_{1},\ldots,t_{2n}$, the expressions $t_{j} - t_{j + 1}$ are all linearly independent of each other except for the constraint ${{\sum_{j = 1}^{2n}t_{j}} - t_{j + 1}} = 0$. Thus we have $|A/ \sim | - 1$ independent constraints in the above sum, and so the number of $t$'s obeying the constraints is bounded by ${|T|}^{2n - |A/ \sim | + 1}$.

All the equivalence classes in the sum (4.11) are without singletons as otherwise $t_{A'} \neq 0$. Thus, for ${n,k} \geq 0$, we let $P{(n,k)}$ be the number of equivalence classes on a set of $n$ elements which have exactly $k$ equivalence classes and no singletons There is a simple recursion on these numbers, namely, which is valid for all ${n,k} \geq 0$. This simply reflects the fact that if $\alpha$ is an element of $A$ and $\sim$ is an equivalence relation on $A$ with $k$ equivalence classes, then either $\alpha$ belongs to a class which has only one other element $\beta$ of $A$ (in which case $\sim$ has $k - 1$ equivalence classes and no singleton on $A\backslash{\{\alpha,\beta\}}$), or $\alpha$ is equivalent to one of the $k$ equivalence classes of $A\backslash{\{\alpha\}}$, each of which having at least two elements.

With these notations, we established The following lemma provides an upper bound on those $P{(n,k)}$'s.

### Lemma 4.6

The numbers $P{(n,k)}$ obey Proof The proof operates by induction. The bound (4.14] ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) is obvious for $n = 1$. Suppose the claim is established for all pairs $(m,k)$ with $m \leq n$. We will show that this implies the property for $m = {n + 1}$. Indeed, The claim follows since for $\lambda \geq \frac{1 + \sqrt{5}}{2}$, we have ${\lambda^{n - 1} + \lambda^{n - 2}} \leq \lambda^{n}$.

This lemma gives us an idea of how large the $P{({2n},k)}$'s appearing in the sum (4.13] ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) really are. To derive an upper bound on the whole sum, we also need to understand the behavior of $\prod_{{A' \in A}{/ \sim}}{F_{|A'|}{(\tau)}}$. This is the subject of our next section.

### Convex analysis

We start with a useful and classical lemma.

### Lemma 4.7

Let $f$ be a convex function on $\lbrack 0,1\rbrack$, say. Consider the problem Then the maximum value $f^{\ast}$ is obtained by allocating one $x_{j}$ to 1 and all the others to 0, i.e. $f^{\ast} = {{{({k - 1})}f{}} + {f{}}}$.

Proof For each $x_{j}$, $0 \leq x_{j} \leq 1$, the convexity of $f$ implies Summing this inequality over all indices gives which is what we sought to establish.

### Corollary 4.8

Suppose that $f = {\log F}$ is a convex function on $\lbrack 0,1\rbrack$, say, and consider Then the maximum value $F^{\ast}$ is obtained by allocating one $x_{j}$ to 1 and all the others to 0, i.e. $F^{\ast} = {{({F{}})}^{k - 1}F{}}$.

Proof Take the logarithm of $\prod_{j = 1}^{k}{F{(x_{j})}}$ and apply Lemma 4.7.

Note that both the lemma and the corollary hold for 'discrete' functions; that is, suppose that $f{(j)}$ obeys Then the maximum value of $\sum_{j = 1}^{k}{f{(n_{j})}}$ where the $n_{j}$'s are now integer values obeying $n_{j} \geq 0$ and ${\sum_{j = 1}^{k}n_{j}} = n$ is of course achieved by taking all the $n_{j}$'s equal to zero but one equal to $n$.

With these preliminaries in place, recall now the bound obtained in Lemma 4.3, Note that we voluntarily exchanged the subscripts, namely, $\tau$ and $n$ to reflect the idea that we shall view $G$ as a function of $n$ while $\tau$ will serve as a parameter. It is clear that $\log G$ is convex and, therefore, Set $G = G_{\tau/{({1 - \tau})}}$ for short. Then for any equivalence class such that $|A/ \sim | = k$, the above argument yields which, on the one hand, gives On the other hand, ${P{({2n},k)}} \leq {\phi^{2n}{({{2n} - 1})}\ldots{({{{2n} - {2k}} + 1})}}$ (see Lemma 4.6] ‣ 4 Moments of Random Matrices ‣ Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information")) and, therefore, We prove that the summand $f$ is in some sense convex.

### Lemma 4.9

For each $k \leq {n - 1}$, $f$ obeys As a consequence of this lemma, the maximum of $f{(k)}$, $1 \leq k \leq n$ is of course attained at either the left-end point ($k = 1$) or the right-end point ($k = n$); in short, Proof We need to establish that for each $1 \leq k \leq {n - 1}$, with $\alpha = {{NG{}}/{|T|}}$ and and, therefore, it is sufficient to establish that ${\rho_{k + 1}\rho_{k - 1}} \geq 1$. Put $m = {n - k}$, then It is now a simple exercise to check that for each $m \geq 2$, the logarithm of the right-hand is nonnegative, i.e.

We omit the proof of this fact.

### Proof of Theorem 3.1

The previous section established where letting $c_{\tau}:={e{\log{({{({1 - \tau})}/\tau})}}}$ This is exactly the content of Theorem 3.1.

## Numerical Experiments

In this section, we present numerical experiments in order to derive empirical bounds on $|T|$ relative to $|\Omega|$ for a signal $f$ supported on $T$ to be the unique minimizer of $(P_{1})$. The results can be viewed as a set of practical guidelines for situations where one can expect perfect recovery from partial Fourier information using convex optimization.

Our experiments are of the following form: Choose constants $N$ (the length of the signal), $N_{t}$ (the number of spikes in the signal), and $N_{\omega}$ (the number of observed frequencies).

Randomly generate the subdomain $T$ by sampling $\{ 0,\ldots,{N - 1}\}$ $N_{t}$ times without replacement (we have ${|T|} = N_{t}$).

Randomly generate $f$ by setting ${{f{(t)}} = 0},{t \in T^{c}}$ and drawing both the real and imaginary parts of ${{f{(t)}},t} \in T$ from independent Gaussian distributions with mean zero and variance one^22^2The results here, as in the rest of the paper, seem to rely only on the sets $T$ and $\Omega$. The actual values that $f$ takes on $T$ can be arbitrary; choosing them to be random emphasizes this. Figures 2 remain the same if we take ${{f{(t)}} = 1},{t \in T}$, say..

Randomly generate the subdomain $\Omega$ of observed frequencies by again sampling $\{ 0,\ldots,{N - 1}\}$ $N_{\omega}$ times without replacement (${|\Omega|} = N_{\omega}$).

Solve $(P_{1})$, and compare the solution to $f$.

The $\ell_{1}$-norm is not strictly convex, so solving $(P_{1})$ using a Newton-type method that relies on local quadratic approximations of $\parallel \cdot \parallel_{\ell_{1}}$ is problematic. Instead, we use a very simple gradient descent with projection algorithm. The number of iterations needed for convergence is high (on the order of $10^{5}$), but since we can rapidly project onto the constraint set (using two fast Fourier transforms), each iteration takes a short amount of time. As an indication, the algorithm typically converges in less than $10$ seconds on a standard desktop computer for signals of length $N = 1024$.

Figure 2 illustrates the recovery rate for varying values of $|T|$ and $|\Omega|$ for $N = 512$. From the plot, we can see that for ${|\Omega|} \geq 32$, if ${|T|} \leq {{|\Omega|}/5}$, we recover $f$ perfectly about $80\%$ of the time. For ${|T|} \leq {{|\Omega|}/8}$, the recovery rate is practically $100\%$. We remark that these numerical results are consistent with earlier findings.

Figure 2: Recovery experiment for N = 512. (a) The image intensity represents the percentage of the time solving (P1) recovered the signal f exactly as a function of |Ω| (vertical axis) and |T|/|Ω| (horizontal axis); in white regions, the signal is recovered approximately 100% of the time, in black regions, the signal is never recovered. For each |T|, |Ω| pair, 100 experiments were run. (b) Cross-section of the image in (a) at |Ω| = 64. We can see that we have perfect recovery with very high probability for |T| ≤ 16.

One source of slack in the theoretical analysis is the way in which we choose the polynomial $P{(t)}$ (as in (2.11)). Theorem 2.1 states that $f$ is a minimizer of $(P_{1})$ if and only if there exists any trigonometric polynomial that has ${{P{(t)}} = {\text{sgn}{(f)}{(t)}}},{t \in T}$ and ${{|{P{(t)}}|} < 1},{t \in T^{c}}$. In (2.11) we choose $P{(t)}$ that minimizes the $\ell_{2}$ norm on $T^{c}$ under the linear constraints ${{P{(t)}} = {\text{sgn}{(f)}{(t)}}},{t \in T}$. However, the condition ${|{P{(t)}}|} < 1$ suggests that a minimal $\ell_{\infty}$ choice would be more appropriate (but is seemingly intractable analytically).

Figure 3 illustrates how often the sufficient condition of $P{(t)}$ chosen as (2.11) meets the constraint ${{|{P{(t)}}|} < 1},{t \in T^{c}}$ for the same values of $\tau$ and $|T|$. The empirical bound on $T$ is stronger by about a factor of two; for ${|T|} \leq {{|\Omega|}/10}$, the success rate is very close to $100\%$.

Figure 3: Sufficient condition test for N = 512. (a) The image intensity represents the percentage of the time P (t) chosen as in (2.11) meets the condition |P (t)| < 1, t ∈ Tc. (b) A cross-section of the image in (a) at |Ω| = 64. Note that the axes are scaled differently than in Figure 2.

As a final example of the effectiveness of this recovery framework, we show two more results of the type presented in Section 1.1; piecewise constant phantoms reconstructed from Fourier samples on a star. The phantoms, along with the minimum energy and minimum total-variation reconstructions (which are exact), are shown in Figure 4. Note that the total-variation reconstruction is able to recover very subtle image features; for example, both the short and skinny ellipse in the upper right hand corner of Figure 4(d) and the very faint ellipse in the bottom center are preserved. (We invite the reader to check for related types of experiments.)

Figure 4: Two more phantom examples for the recovery problem discussed in Section 1.1. On the left is the original phantom ((d) was created by drawing ten ellipses at random), in the center is the minimum energy reconstruction, and on the right is the minimum total-variation reconstruction. The minimum total-variation reconstructions are exact.

## Discussion

We would like to close this paper by offering a few comments about the results obtained in this paper and by discussing the possibility of generalizations and extensions.

### Stability

In the introduction section, we argued that even if one knew the support $T$ of $f$, the reconstruction might be unstable. Indeed with knowledge of $T$, a reasonable strategy might be to recover $f$ by the method of least-squares, namely, In practice, the matrix inversion might be problematic. Now observe that with the notations of this paper Hence, for stability we would need ${\frac{1}{|\Omega|}H_{0}} \leq {1 - \delta}$ for some $\delta > 0$. This is of course exactly the problem we studied, compare Theorem 3.3. In fact, selecting $\alpha_{M}$ as suggested in the proof of our main theorem (see section 3.4) gives ${\frac{1}{|\Omega|}H_{0}} \leq.42$ with probability at least $1 - {O{(N^{- M})}}$. This shows that selecting $|T|$ as to obey (1.9), ${|T|} \approx {{|\Omega|}/{\log N}}$ actually provides stability.

### Robustness

An important question concerns the robustness of the reconstruction procedure vis a vis measurement errors. For example, we might want to consider the model problem which says that instead of observing the Fourier coefficients of $f$, one is given those of $f + h$ where $h$ is some small perturbation. Then one might still want to reconstruct $f$ via In this setup, of course, one cannot expect exact recovery. Instead, one would like to know whether or not our reconstruction strategy is well-behaved or more precisely, how far is the minimizer $f^{\sharp}$ from the true object $f$. In short, what is the typical size of the error? Our preliminary calculations suggest that the reconstruction is robust in the sense that the error ${\|{f - f^{\sharp}}\|}_{1}$ is small for small perturbations $h$ obeying ${\| h\|}_{1} \leq \delta$, say. We hope to be able to report on these early findings in a follow-up paper.

### Extensions

Finally, work in progress shows that similar exact reconstruction phenomena hold for other synthesis/measurement pairs. Suppose one is given a pair of of bases $(\mathcal{B}_{1},\mathcal{B}_{2})$ and randomly selected coefficients of an object $f$ in one basis, say $\mathcal{B}_{2}$. (From this broader viewpoint, the special cases discussed in this paper assume that $\mathcal{B}_{1}$ is the canonical basis of ${\mathbb{R}}^{N}$ or ${\mathbb{R}}^{N} \times {\mathbb{R}}^{N}$ (spikes in 1D, 2D), or is the basis of Heavysides as in the Total-variation reconstructions, and $\mathcal{B}_{2}$ is the standard 1D, 2D Fourier basis.) Then, it seems that $f$ can be recovered exactly provided that it may be synthesized as a sparse superposition of elements in $\mathcal{B}_{1}$. The relationship between the number of nonzero terms in $\mathcal{B}_{1}$ and the number of observed coefficients depends upon the incoherence between the two bases. The more incoherent, the fewer coefficients needed. Again, we hope to report on such extensions in a separate publication.
