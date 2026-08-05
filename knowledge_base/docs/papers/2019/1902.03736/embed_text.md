<!-- arxiv-full-text:v1 {"arxiv_id": "1902.03736", "source": "ar5iv"} -->

## Introduction

Concentration (large deviation) inequalities are one of the most important subjects of study in probability theory. A class of distributions for which sharp concentration inequalities have been developed is the class of subGaussian distributions.

### Definition 1

A random variable $X \in R$ is subGaussian, if there exists $\sigma \in R$ so that:

### Definition 2

A random vector $\mathbf{X} \in R^{d}$ is subGaussian, if there exists $\sigma \in R$ so that: The concentration bounds of subGaussian random vectors/variables depends on the parameter $\sigma$ -- smaller the $\sigma$ better the concentration bounds. While subGaussian distributions arise naturally in several applications, there are settings where the random vectors have nice concentration properties but the subGaussian parameter $\sigma$ is very large (so that applying concentration bounds for general subGaussian random vectors gives loose bounds). In this short note, we consider a related but different class of distributions, called *norm-subGaussian* random vectors and establish tighter concentration bounds for them.

Organization: In Section 2, we introduce norm subGaussian random vectors and some of their properties and we prove our main results in Section 3. We conclude in Section 4.

## Norm SubGaussian Random Vector

The norm subGaussian random vector is defined as follows.

### Definition 3

A random vector $\mathbf{X} \in {\mathbb{R}}^{d}$ is *norm-subGaussian* (or $\text{nSG}{(\sigma)}$), if $\exists\sigma$ so that: Norm subGaussian includes both subGaussian (with a smaller $\sigma$ parameter) and bounded norm random vectors as special cases.

### Lemma 1

There exists absolute constant $c$ so that following random vectors are all $\text{nSG}{({c \cdot \sigma})}$.

A bounded random vector $\mathbf{X} \in {\mathbb{R}}^{d}$ so that ${\|\mathbf{X}\|} \leq \sigma$.

A random vector $\mathbf{X} \in {\mathbb{R}}^{d}$, where $\mathbf{X} = {\xi\mathbf{e}_{1}}$ and random variable $\xi \in {\mathbb{R}}$ is $\sigma$-subGaussian.

A random vector $\mathbf{X} \in {\mathbb{R}}^{d}$ that is $({\sigma/\sqrt{d}})$-subGaussian.

### Proof

The fact that the first two random vectors are $\text{nSG}{({c \cdot \sigma})}$ immediately follows from the arguements in scalar version counterparts. For the third random vector, WLOG, assume ${{\mathbb{E}}\mathbf{X}} = 0$. Let $\{\mathbf{v}_{i}\}$ be a $1/2$-cover of unit sphere ${\mathbb{S}}^{d - 1}$ (thus ${\|\mathbf{v}_{i}\|} = 1$). By property of subGaussian random vector, we know for each fixed $v_{i}$: Then let ${\mathbf{v}{(\mathbf{X})}} = {\mathbf{X}/{\|\mathbf{X}\|}}$, since $\{\mathbf{v}_{i}\}$ is a $1/2$-cover, there always exists a $j{(\mathbf{X})}$ so that $\mathbf{v}_{j{(\mathbf{X})}}$ in cover and ${\|{{\mathbf{v}{(\mathbf{X})}} - \mathbf{v}_{j{(\mathbf{X})}}}\|} \leq {1/2}$. Therefore, we have: Rearranging gives ${\|\mathbf{X}\|} \leq {2{\langle\mathbf{v}_{j{(\mathbf{X})}},\mathbf{X}\rangle}}$. Finally, the covering number of $1/2$-cover over ${\mathbb{S}}^{d - 1}$ can be upper bounded by $4^{d}$. Therefore, by union bound: Now we are ready to check the second claim of Lemma 1, when $t^{2} \leq {8\sigma^{2}{\ln 4}}$, we have, when $t^{2} > {8\sigma^{2}{\ln 4}}$, we let $t^{2} = {{8\sigma^{2}{\ln 4}} + s}$ where $s > 0$, then: In sum, this proves that $\mathbf{X}$ is $\text{nSG}{({{2\sqrt{2}} \cdot \sigma})}$. ∎ The following lemma gives equivalent characterizations of norm subGaussian in terms of moments and moment generating function (MGF).

### Lemma 2 (Properties of norm-subGaussian)

For random vector $\mathbf{X} \in {\mathbb{R}}^{d}$, following statements are equivalent up to absolute constant difference in $\sigma$.

Tails: ${{\mathbb{P}}{({{\|\mathbf{X}\|} \geq t})}} \leq {2e^{- \frac{t^{2}}{2\sigma^{2}}}}$.

Moments: ${({{\mathbb{E}}{\|\mathbf{X}\|}^{p}})}^{\frac{1}{p}} \leq {\sigma\sqrt{p}}$ for any $p \in {\mathbb{N}}$.

Super-exponential moment: ${{\mathbb{E}}e^{\frac{{\|\mathbf{X}\|}^{2}}{\sigma^{2}}}} \leq e$.

### Proof

Note $\|\mathbf{X}\|$ is a 1-dimensional random variable. This lemma directly follows from the equivalent properties of $1$-dimensional subGaussian, for instance, Lemma 5.5. ∎ The following lemma says that if a random vector is $\text{nSG}{(\sigma)}$, then its norm squared is subexponential and its projection on any direction a is subGaussian random variable.

### Lemma 3

There is an absolute constant $c$ so that if random vector $\mathbf{X} \in R^{d}$ is zero-mean $\text{nSG}{(\sigma)}$, then ${\|\mathbf{X}\|}^{2}$ is $c \cdot \sigma^{2}$-subExponential, and for any fixed unit vector $\mathbf{v} \in {\mathbb{S}}^{d - 1}$, $\langle\mathbf{v},\mathbf{X}\rangle$ is $c \cdot \sigma$-subGaussian.

The undesirable thing about the MGF characterization in Lemma 2. ‣ 2 Norm SubGaussian Random Vector ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm") is that even if $\mathbf{X}$ is a zero mean random vector, $\|\mathbf{X}\|$ is not zero mean, so it is difficult to directly work with MGF of $\|\mathbf{X}\|$. Instead, we first convert the random vector $\mathbf{X}$ to a matrix $\mathbf{Y}$ and characterize the MGF of $\mathbf{Y}$.

### Lemma 4 (MGF Characterization)

There is an absolute constant $c$, if random vector $\mathbf{X} \in R^{d}$ is zero-mean $\text{nSG}{(\sigma)}$, then let we have ${{\mathbb{E}}e^{\theta\mathbf{Y}}} \preceq {e^{{c \cdot \theta^{2}}\sigma^{2}}\mathbf{I}}$ for any $\theta \in {\mathbb{R}}$.

### Proof

Note $\mathbf{Y}$ is a rank-2 matrix whose eigenvalues are ${\|\mathbf{X}\|},{- {\|\mathbf{X}\|}}$, and ${{\mathbb{E}}\mathbf{Y}^{{2p} + 1}} = \mathbf{0}$ for any $p \in {\mathbb{N}}$. On the other hand, we also have ${\|\mathbf{Y}^{2p}\|} \leq {{\|\mathbf{X}\|}^{2}p}$ for any $p \in {\mathbb{N}}$. Therefore, by Lemma 2. ‣ 2 Norm SubGaussian Random Vector ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm"), there exists constant $c$, for any $\theta \in {\mathbb{R}}$: where in the last inequality we used the fact that $\frac{p^{p}}{{({2p})}!} \leq \frac{1}{p!}$, this finishes the proof. ∎

## Vector Martingales with SubGaussian Norm

In this section, we will prove our main result (Lemma 6, Corollaries 7. ‣ 3 Vector Martingales with SubGaussian Norm ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm") and 8) giving concentration bounds for norm subGaussian random vectors. The main tool we use is Lieb's concavity theorem.

### Theorem 5 (Tropp )

Let $\mathbf{A}$ be a fixed symmetric matrix, and let $\mathbf{Y}$ be a random symmetric matrix. Then, We will prove our concentration result for norm subGaussian random vectors in a general setting where the subGaussian parameter $\sigma_{i}$ for the $i^{\text{th}}$ vector can itself be a random variable.

### Condition 4

Let random vectors ${\mathbf{X}_{1},\ldots,\mathbf{X}_{n}} \in {\mathbb{R}}^{d}$, and corresponding filtrations $\mathcal{F}_{i} = {\sigma{(\mathbf{X}_{1},\ldots,\mathbf{X}_{i})}}$ for $i \in {\lbrack n\rbrack}$ satisfy that $\left. \mathbf{X}_{i} \middle| \mathcal{F}_{i - 1} \right.$ is zero-mean $\text{nSG}{(\sigma_{i})}$ with $\sigma_{i} \in \mathcal{F}_{i - 1}$. i.e.,

### Lemma 6

There exists an absolute constant $c$ such that if ${\mathbf{X}_{1},\ldots,\mathbf{X}_{n}} \in {\mathbb{R}}^{d}$ satisfy condition 4, then for any fixed $\delta > 0$, $\theta > 0$, with probability at least $1 - \delta$:

### Proof

According to Lemma 4. ‣ 2 Norm SubGaussian Random Vector ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm"), there exists an absolute constant $c$ so that ${{\mathbb{E}}{\lbrack\left. e^{\theta\mathbf{Y}_{i}} \middle| \mathcal{F}_{i - 1} \right.\rbrack}} \preceq {e^{{c \cdot \theta^{2}}\sigma_{i}^{2}}\mathbf{I}}$ holds for any $i \in {\lbrack n\rbrack}$. Therefore, we have: where step is due to Theorem 5). ‣ 3 Vector Martingales with SubGaussian Norm ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm"), and step used the fact that if matrix $\mathbf{A} \preceq \mathbf{B}$, then $e^{\mathbf{C} + \mathbf{A}} \preceq e^{\mathbf{C} + \mathbf{B}}$. On the other hand, since identity matrix commutes with any matrix, we know: Therefore, for any $t \geq 0$, $\theta \geq 0$, by Markov's inequality, we have: where step is because $\sum_{i = 1}^{n}\mathbf{Y}_{i}$ is a rank-2 matrix whose eigenvalues are ${\|{\sum_{i = 1}^{n}\mathbf{X}_{i}}\|},{- {\|{\sum_{i = 1}^{n}\mathbf{X}_{i}}\|}}$; step is due to all preconditions are symmetric with respect to 0. Finally, setting RHS equal to $\delta$, we finish the proof. ∎

### Corollary 7 (Hoeffding type inequality for norm-subGaussian)

There exists an absolute constant $c$ such that if ${\mathbf{X}_{1},\ldots,\mathbf{X}_{n}} \in {\mathbb{R}}^{d}$ satisfy condition 4 with fixed $\{\sigma_{i}\}$, then for any $\delta > 0$, with probability at least $1 - \delta$:

### Proof

Since now $\{\sigma_{i}\}$ are fixed which are not random, we can pick $\theta$ in Lemma 6 as a function of $\{\sigma_{i}\}$. Indeed, pick $\theta = \sqrt{\frac{1}{\sum_{i = 1}^{n}\sigma_{i}^{2}}{\log\frac{2d}{\delta}}}$ finishes the proof. ∎

### Corollary 8

There exists an absolute constant $c$ such that if ${\mathbf{X}_{1},\ldots,\mathbf{X}_{n}} \in {\mathbb{R}}^{d}$ satisfy condition 4, then for any fixed $\delta > 0$, and $B > b > 0$, with probability at least $1 - \delta$:

### Proof

For simplicity, denote log factor $\iota: = \log\frac{2d}{\delta} + \log\log\frac{B}{b}$ By Lemma 6, we know for any fixed $\theta$, with probability $1 - {\delta \cdot {\log^{- 1}{({B/b})}}}$, we have: Construct two sets of $\Psi = {\{\psi_{1},\ldots,\psi_{s}\}}$ and $\Theta = {\{\theta_{1},\ldots,\theta_{s}\}}$, where $\psi_{j} = {2^{j - 1} \cdot b}$ and $\theta_{j} = \sqrt{\frac{\iota}{\psi_{j}}}$ with last element $\psi_{s} \leq B$, ${2\psi_{s}} > B$. It is easy to see ${|\Psi|} = {|\Theta|} \leq {\log{({B/b})}}$. By union bound, we have with probability $1 - \delta$: Consider following two cases: ${\sum_{i = 1}^{n}\sigma_{i}^{2}} \in {\lbrack b,B\rbrack}$. Then, there exists $j \in {\lbrack s\rbrack}$ such that $\psi_{j} \leq {\sum_{i = 1}^{n}\sigma_{i}^{2}} < {2\psi_{j}}$: \(2\) ${\sum_{i = 1}^{n}\sigma_{i}^{2}} \in {\lbrack 0,b)}$. In this case we know $\psi_{1} = b$ and: Combining two cases we finish the proof.

## Conclusion

In this short note, we introduced the notion of norm subGaussian random vectors, which include subGaussian random vectors and bounded random vectors as special cases. While it is true that ${\text{subGaussian}\left( \frac{\sigma}{\sqrt{d}} \right)} \subseteq {\text{nSG}{(\sigma)}} \subseteq {\text{subGaussian}{(\sigma)}}$, applying concentration bounds for $\text{subGaussian}{(\sigma)}$ would yield bounds which have at least linear dependence on $d$. In contrast, the bounds we develop (in Lemma 6 and Corollaries 7. ‣ 3 Vector Martingales with SubGaussian Norm ‣ A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm") and 8) have only logarithmic dependence on $d$. It is not clear if this logarithmic dependence is tight -- totally eliminating this dependence is an interesting open problem.
