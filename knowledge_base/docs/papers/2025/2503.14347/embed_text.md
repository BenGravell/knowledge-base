<!-- arxiv-full-text:v1 {"arxiv_id": "2503.14347", "source": "arxiv-html"} -->

## Abstract

We present a new method for proving the norm concentration inequality of sub-Gaussian variables. Our proof is based on an averaged version of the moment generating function, termed the averaged moment generating function. Our method applies to both vector cases to bound the vector norm and matrix cases to bound the operator norm. Compared with the widely adopted $\varepsilon$-net technique-based proof of the sub-Gaussian norm concentration inequality, our method does not rely on the union bound and promises a tighter concentration bound.

## Sub-Gaussian Norm Concentration Inequality

Concentration inequalities are mathematical tools in probability theory that describe how a random variable deviates from some value, typically its expectation. Some commonly used instances include Markov's inequality, Chebyshev's inequality, and Chernoff bounds. These concentration inequalities play an essential role in various fields, including probability theory, statistics, machine learning, finance, etc, providing probabilistic guarantees when dealing with random quantities. Many probability distributions exhibit concentration properties, among which we consider an important class known as sub-Gaussian distribution. The sub-Gaussian random variable is formally defined as follows.

### Definition 1.1

A random variable $X \in {\mathbb{R}}$ is said to be sub-Gaussian with variance proxy $\sigma^{2} > 0$ if A random vector $X \in {\mathbb{R}}^{n}$ is sub-Gaussian with variance proxy $\sigma^{2} > 0$ if $\langle\ell,X\rangle$ is sub-Gaussian for any unit vector $\ell$, that is, where $\mathcal{S}^{n - 1} = {\{{x \in {\mathbb{R}}^{n}}:{{\| x\|} = 1}\}}$ denotes the Euclidean unit sphere in ${\mathbb{R}}^{n}$.

Sub-Gaussian distributions include a wide range of distributions such as Gaussian distribution, uniform distribution, and any distributions with finite supports as special cases. For a Gaussian random variable, the variance proxy equals its variance.

In this work, we consider one important concentration inequality for sub-Gaussian distributions known as norm concentration, which describes the concentration property of the norm $\| X\|$ for a sub-Gaussian random vector $X$.

### Theorem 1

For a sub-Gaussian vector $X \in {\mathbb{R}}^{n}$ with variance proxy $\sigma^{2}$, there exist constants $C_{1}$, $C_{2}$ such that, for any $\delta \in {}$, The choice of constants $C_{1},C_{2}$ depends on the proof techniques. When $n = 1$, a direct application of the Markov's inequality points to for any ${\lambda > 0},{r > 0}$. Minimizing the above over $\lambda$ yields ${{\mathbb{P}}\left({X > r} \right)} \leq e^{- \frac{r^{2}}{2\sigma^{2}}}$. Similarly, ${{\mathbb{P}}\left({X < {- r}} \right)} \leq e^{- \frac{r^{2}}{2\sigma^{2}}}$. Combining them with the union bound, we obtain ${{\mathbb{P}}\left({{\| X\|} > r} \right)} \leq {2e^{- \frac{r^{2}}{2\sigma^{2}}}}$. This corresponds to with constants $C_{1} = {2{\log 2}}$ and $C_{2} = 2$.

When $n \geq 2$, one can follow a similar idea and apply Markov's inequality to bound ${\mathbb{P}}\left({{\ell^{\top}X} > r} \right)$ for each $\ell \in \mathcal{S}^{n - 1}$ and then combine them to establish a probabilistic bound for ${\| X\|} = {\max_{\ell \in \mathcal{S}^{n - 1}}{\ell^{\top}X}}$. However, the union bound is no longer applicable since the maximum is over an unaccountable set $\mathcal{S}^{n - 1}$. To circumvent this issue, the $\varepsilon$-net technique has been developed and has become a standard proof for sub-Gaussian norm concentration. Following this technique, one constructs an $\varepsilon$-net $\mathcal{N}$ \[1, Definition 1.17\] for the Euclidean unit ball such that $\mathcal{N}$ has finite elements and ${\max_{\ell \in \mathcal{S}^{n - 1}}{\ell^{\top}X}} \leq {\frac{1}{1 - \varepsilon}{\max_{\ell \in \mathcal{N}}{\ell^{\top}X}}}$ \[3, Exercise 4.4.2\]. The union bound can be applied since $\mathcal{N}$ is a finite set. This method results in with constants $C_{1}$ and $C_{2}$ determined by where $\varepsilon$ can take any value in the interval $$. When $\varepsilon = \frac{1}{2}$, we have $C_{1} = {8{\log 5}} \approx 16$ and $C_{2} = 8$, which is commonly used in existing literature, e.g..

## New Proof based on Averaged Moment Generating Function

To analyze the concentration property of $\| X\|$, the $\varepsilon$-net strategy as described above first analyzes the concentration of the one-dimensional projection $\ell^{\top}X$ of $X$ using the Markov's inequality and then applies the union bound to establish the concentration bound for $\| X\|$. This gives rise to one question: is there a more direct approach to establish the concentration of $\| X\|$?

One natural attempt is to bound ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$ with $\lambda > 0$ and apply the Markov's inequality to get bound ${{\mathbb{P}}\left( {{\| X\|} > r} \right)} \leq {{{\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}}/e^{\lambda r}}$ directly. However, it is not easy to bound ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$ from the definition of the sub-Gaussian random vector. In fact, researchers often follow an opposite direction and bound ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$ using the concentration property of $\| X\|$.

In this paper, we present a new proof of the sub-Gaussian norm concentration inequality that directly analyzes $\| X\|$. The key of our proof is a novel mathematical tool named the averaged moment generating function (AMGF) that bears similarity with ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$.

### Definition 2.1 (AMGF)

The Averaged Moment Generating Function $\Phi_{X}{(\lambda)}$ of a random vector $X \in {\mathbb{R}}^{n}$ is defined as ${\Phi_{X}{(\lambda)}} = {{\mathbb{E}}_{X}{({\Phi_{n}{({\lambda X})}})}}$ where the energy function The AMGF was first introduced in to study Langevin algorithms in sampling problems. The AMGF is an average of the moment generating function (MGF) ${\mathbb{E}}_{X}{(e^{\lambda{\langle\ell,X\rangle}})}$ over the unit sphere $\ell \sim \mathcal{S}^{n - 1}$. It can also be viewed as an MGF with the exponential energy function $e^{\lambda{\langle\ell,X\rangle}}$ being replaced by its average ${\Phi_{n}{({\lambda X})}} = {{\mathbb{E}}_{\ell \sim \mathcal{S}^{n - 1}}\left(e^{\lambda{\langle\ell,X\rangle}} \right)}$.

Similar to $e^{\lambda{\| X\|}}$, the energy function $\Phi_{n}{({\lambda X})}$ only depends on the norm $\| X\|$. In fact, where ${{\phi_{n}{(z)}} = {{\mathbb{E}}_{\ell \sim \mathcal{S}^{n - 1}}\left(e^{\langle\ell,{z\eta}\rangle} \right)}},{{\forall\eta} \in \mathcal{S}^{n - 1}}$ admits a closed-form expression of ${\phi_{1}{(z)}} = {\cosh{(z)}}$ and ${\phi_{n}{(z)}} = {\Gamma{({n/2})}{({2/z})}^{{({n - 2})}/2}I_{{({n - 2})}/2}{(z)}}$ when $n \geq 2$ where $\Gamma$ denotes the Gamma function and $I$ is the modified Bessel function of the first kind. In addition to these similarities to $e^{\lambda{\| x\|}}$, we show below that the value of $\Phi_{n}{({\lambda X})}$ is closely related to $e^{\|{\lambda X}\|}$.

### Lemma 2.1

For any $X \in {\mathbb{R}}^{n}$ and any $\varepsilon \in {}$, $\Phi_{n}{({\lambda X})}$ satisfies

### Proof

In view of ${\Phi_{n}{({\lambda X})}} = {\phi_{n}{({\|{\lambda X}\|})}}$, it suffices to show that holds for any $z \geq 0$ and any $\varepsilon \in {}$. When $n = 1$, ${\phi_{1}{(z)}} = {\cosh{(z)}}$ and becomes This is a straightforward consequence of the convexity of ${\log{\cosh{(z)}}} - {\log\left({\sqrt{1 - \varepsilon^{2}}e^{\varepsilon z}} \right)}$ with respect to $z$. We next focus on the case of $n \geq 2$.

As pointed out, directly from the definition, the derivative of $\log\phi_{n}$ admits an elegant expression The ratio of Bessel functions can be bounded below as Since $g{(z)}$ is monotonically increasing over $z > 0$, $G{(z)}$ is convex on $z > 0$. Thus, by the definition of convexity, given any $z_{0} > 0$, Set $z_{0} = \frac{\varepsilon n}{1 - \varepsilon^{2}}$, then Plugging into - yields The conclusion and thus follow by taking the exponential of. This completes the proof. ∎ By Lemma 2.1, the AMGF can be viewed as a surrogate function of ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$. One distinguishing feature of the AMGF compared with ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$ is that the AMGF shares the same bound as the MGF. More specifically,, ${{\mathbb{E}}_{X}{(e^{\lambda{\langle\ell,X\rangle}})}} \leq e^{\frac{\lambda^{2}\sigma^{2}}{2}}$ for any $\ell \in \mathcal{S}^{n - 1}$, and thus the AMGF satisfies By combining with Lemma 2.1, an upper bound on ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$ can be established, based on which Markov's inequality can be applied to bound ${\mathbb{P}}\left({{\| X\|} > r} \right)$, formalized as follows.

### Theorem 2

Let $X \in {\mathbb{R}}^{n}$ be a sub-Gaussian vector with variance proxy $\sigma^{2}$, then for any $\delta \in {}$ and any $\varepsilon \in {}$,

### Proof

By Lemma 2.1, the AMGF of $X$ satisfies Denote $t = {\varepsilon{|\lambda|}} > 0$, then becomes Applying Markov's inequality, we obtain that, for any $r > 0$ and $\varepsilon \in {}$, Minimizing the exponent $\frac{\sigma^{2}t^{2}}{2\varepsilon^{2}} - {rt}$ over $t$ yields the minimum $- \frac{\varepsilon^{2}r^{2}}{2\sigma^{2}}$. Plugging the minimum into we arrive at Define $\delta = {{({1 - \varepsilon^{2}})}^{- \frac{n}{2}}e^{- \frac{\varepsilon^{2}r^{2}}{2\sigma^{2}}}}$, then $r$ can be expressed as The conclusion follows by plugging this expression of $r$ into. This completes the proof. ∎ Clearly, Theorem 2 is a special case of Theorem 1 with constants The choice of $C_{1},C_{2}$ appears to be better than obtained by the $\varepsilon$-net technique. Indeed, shares the same $C_{2}$ as, and $C_{1}$ in is smaller by for any $\varepsilon \in {(0,\, 1)}$.

Theorem 2 represents a class of concentration inequalities parameterized by $\varepsilon \in {(0,\, 1)}$. In practice, one can choose $\varepsilon$ according to the value of $n$ and $\delta$. With slight modifications, one can derive a more elegant concentration inequality based on AMGF as follows.

### Theorem 3

Let $X \in {\mathbb{R}}^{n}$ be a sub-Gaussian vector with variance proxy $\sigma^{2}$, then for any $\delta \in {}$,

### Proof

Combining and the fact that ${\log{({1 - \varepsilon^{2}})}} \geq \frac{\varepsilon^{2}}{\varepsilon^{2} - 1}$ holds for any $\varepsilon \in {}$, we know for any $\varepsilon \in {}$ and $t > 0$: where the minimizer is $\varepsilon^{\ast} = \sqrt{\frac{\sigma t}{{\sigma t} + \sqrt{n}}} \in {}$. By Markov's inequality, implies that for any $t > 0$: Set $t = \frac{r}{\sigma}$, then it follows The proof is concluded by setting $\delta = e^{- \frac{r^{2}}{2}}$. ∎ Unlike, the concentration inequality does not depend on $\varepsilon$ due to the additional optimization step. In practice, applying Theorem 2 or Theorem 3 can depend on the value of $n$ and $\delta$.

Interestingly, Theorem 3 coincides with a concentration bound established in \[6, Remark 6\] based on variational inequality. Theorem 3 is only slightly worse than the tightest existing result of sub-Gaussian norm concentration stated in \[7, Theorem 1\] which states that ${{\mathbb{P}}\left( {{\| X\|} \geq {\sigma\sqrt{n + {2\sqrt{n{\log{({1/\delta})}}}} + {2{\log{({1/\delta})}}}}}} \right)} \leq \delta$. It is worth pointing out that the proof in is based on bounding ${\mathbb{E}}_{X}{\mathbb{E}}_{\ell \sim {\mathcal{N}{(0,I)}}}{(e^{\lambda{\langle\ell,X\rangle}})}$, which is an average of the MGF over the standard Gaussian distribution rather than the uniform distribution on $\mathcal{S}^{n - 1}$ as in AMGF.

## Generalization to Sub-Gaussian Random Matrices

In this section, we extend our AMGF-based method to study the norm concentration property of sub-Gaussian matrices. In particular, we focus on the operator norm, which plays a pivotal role in applications related to random matrix theory. Recall that a random matrix $A \in {\mathbb{R}}^{m \times n}$ is said to be sub-Gaussian with variance proxy $\sigma^{2}$ if ${{\mathbb{E}}{(A)}} = 0$ and for any $\lambda \in {\mathbb{R}}$ \[1, Section 1.2\] Following Definition 2.1. ‣ 2 New Proof based on Averaged Moment Generating Function ‣ A New Proof of Sub-Gaussian Norm Concentration Inequality"), we define the AMGF of a random matrix $A$ as ${\Phi_{A}{(\lambda)}} = {{\mathbb{E}}_{A}{({\Phi_{m,n}{({\lambda A})}})}}$, where the energy function Similar to the vector setting, the property of exponential growth holds for $\Phi_{m,n}{({\lambda A})}$.

### Lemma 3.1

Given $A \in {\mathbb{R}}^{m \times n}$, for any $\varepsilon \in {}$, $\Phi_{m,n}{({\lambda A})}$ satisfies

### Proof

Without loss of generality, assume $m \leq n$. Consider the singular value decomposition $A = {U\Sigma V}$, where $U \in {\mathbb{R}}^{m \times m}$ and $V \in {\mathbb{R}}^{n \times n}$ are unitary matrices, and $\Sigma = \begin{bmatrix} {\text{diag}{(\sigma_{1},\ldots,\sigma_{m})}} & 0_{m \times {({n - m})}} \end{bmatrix}$ with singular values $\sigma_{1},\ldots,\sigma_{m}$ arranged in a descending order. Note the operator norm of $A$ satisfies ${\| A\|} = \sigma_{1}$. Since for any unit vectors $u \in \mathcal{S}^{m - 1}$ and $v \in \mathcal{S}^{n - 1}$, $u^{\top}U$ and $Vv$ remain unit vectors, $\Phi_{m,n}{(A)}$ can be expressed as where the last "$\geq$" follows from Lemma 2.1. Since ${\|{\Sigma v}\|} \geq {\sigma_{1}v_{1}} = {{\| A\|}{\langle\ell_{1},v\rangle}}$ where $\ell_{1}$ is the unit vector along the first coordinate, can be further bounded as Based on Lemma 3.1, we present the following norm concentration inequality for sub-Gaussian matrices.

### Theorem 4

Let $A \in {\mathbb{R}}^{m \times n}$ be a sub-Gaussian matrix with variance proxy $\sigma^{2}$, then for any $r > 0$:

### Proof

By Lemma 3.1, ${\Phi_{A}{(\lambda)}} \geq {{({1 - \varepsilon^{2}})}^{\frac{m + n}{2}}{\mathbb{E}}_{A}\left(e^{\varepsilon^{2}{\|{\lambda A}\|}} \right)}$. By the definition of sub-Gaussian matrix, ${\Phi_{A}{(\lambda)}} \leq e^{\frac{\lambda^{2}\sigma^{2}}{2}}$. Combining the upper and lower bounds on $\Phi_{A}{(\lambda)}$, we get Define $t = {\varepsilon^{2}{|\lambda|}}$, then becomes By Markov's inequality, implies that for any $t > 0$: Set $t = \frac{\varepsilon^{4}r}{\sigma^{2}}$, which is the minimizer of the exponent $\frac{\sigma^{2}t^{2}}{2\varepsilon^{4}} - {rt}$, then it follows that Denote $\delta = {{({1 - \varepsilon^{2}})}^{- \frac{m + n}{2}}{\exp\left({- \frac{\varepsilon^{4}r^{2}}{2\sigma^{2}}} \right)}}$, then Theorem 4 follows by plugging this expression into. ∎ We point out that in Theorem 4, we do not require the elements of $A$ to be independent, as assumed in the proof of the Sub-Gaussian norm concentration based on the $\varepsilon$-net method \[3, Chapter 4\].

## Conclusion

This paper presents an alternative proof of the sub-Gaussian norm concentration inequality that applies to both random vectors and random matrices. The key to our proof is a modified MGF dubbed AMGF. The AMGF depends solely on the distribution of the norm of a random vector/matrix $X$, making it particularly suitable for analyzing the concentration properties of $\| X\|$. Unlike existing methods that rely on the union bound, our proof directly addresses ${\mathbb{P}}\left( {{\| X\|} > r} \right)$, leading to a more refined analysis. Our method can also be applied to study the norm concentration of some other classes of distributions such as sub-exponential distributions. Beyond its immediate application to the norm concentration, the AMGF and the associated energy function $\Phi_{n}$ hold the potential for broader and lasting contributions to probability theory and related fields.
