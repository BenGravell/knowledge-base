## Abstract

The Hanson-Wright inequality establishes exponential concentration for quadratic forms $X^{\mathsf{T}}MX$, where $X$ is a vector with independent sub-Gaussian entries and with parameters depending on the Frobenius and operator norms of $M$. The most elementary proof to date is due to Rudelson & Vershynin ((https://arxiv.org/html/2509.00881v1#bib.bib3)), who still rely on a convex decoupling argument due to Bourgain ((https://arxiv.org/html/2509.00881v1#bib.bib2)), followed by Gaussian comparison to arrive at the result. In this note we sidestep this decoupling and provide an arguably simpler proof reliant only on elementary properties of sub-Gaussian variables and Gaussian rotational invariance. As a consequence we also obtain improved constants.

## The Hanson-Wright Inequality

Let $X_{1:n}$ be a sequence of mean zero, iid-$\sigma^{2}$-sub-Gaussian random variables; ${{\mathbf{E}{\exp\left( {\lambdaX_{i}} \right)}} \leq {\exp\left( \frac{\lambda^{2}\sigma^{2}}{2} \right)}},{{{\forall\lambda} \in {\mathbb{R}}},{i \in {\lbrack n\rbrack}}}$. In this note we prove the following exponential inequality.

### Theorem 1

For every $\lambda \in \left\lbrack 0,\frac{1}{3c_{2}{\| M\|}_{\mathsf{o}\mathsf{p}}\sigma^{2}} \right)$ we have that:

where we take $c_{1} = 2$, $c_{2} = 1$ if $M$ is diagonal-free and $c_{1} = 20$, $c_{2} = 4$ otherwise.

Consequently for $t \geq 0$:

We let $M = {(m_{ij})}$ and define $\frac{M + M^{\mathsf{T}}}{2} \triangleq A = {(a_{ij})}$. Observe that for any quadratic form ${x^{\mathsf{T}}Mx} = {x^{\mathsf{T}}Ax}$ identically. Consequently, we have that

The first term above is easy to analyze, since its just a sum of independent sub-exponential random variables. The second term is a little more tricky, and in the literature a convex decoupling inequality is typically used (Rudelson & Vershynin, (https://arxiv.org/html/2509.00881v1#bib.bib3)). Before we proceed, let us introduce $\overset{\circ}{A}$, the hollow of $A$, which is just a copy of $A$ but with its diagonal elements set to zero. Thus:

A quadratic form in the hollow of a symmetric matrix, such as $\sum_{j = 2}^{n}{X_{j}{\sum_{i < j}{a_{ij}X_{i}}}}$, has a natural martingale structure that allows to directly produce a comparison inequality via repeated application of the tower rule. It is this \"trick\" that we refer to as elementary.

An approach similar in spirit to ours is due Latała (see the appendix of Barthe & Milman, (https://arxiv.org/html/2509.00881v1#bib.bib1)) in which a decoupling inequality for U-statistics is used. This idea is not dissimilar to decoupling ([1.4](https://arxiv.org/html/2509.00881v1#S1.E4 "Equation 1.4 ‣ 1 The Hanson-Wright Inequality ‣ An Elementary Proof of The Hanson-Wright Inequality")) using its martingale structure. We proceed to provide details of our direct approach below.

## The Proof

Let us introduce an auxiliary sequence $G_{1:n}$ of iid Gaussian random variables with mean zero and variance $\sigma^{2}$. We have with $\mathbf{E}_{n}{\lbrack \cdot \rbrack} \triangleq \mathbf{E}{\lbrack \cdot |X_{1:{n - 1}}\rbrack}$:

We can proceed similarly:

Indeed, the step $(\ldots)$ can be established by combining $( \dagger )$, a finite induction argument and the following calculation:

Having established $( \ddagger )$, since $\overset{\circ}{A}$ is symmetric, we can write ${G^{\mathsf{T}}\overset{\circ}{A}G} = {\sum_{i = 1}^{n}{\mu_{i}Z_{i}^{2}}}$ in distribution, where $\sigmaZ_{1:n}$ is equal to $G_{1:n}$ in distribution relying on Gaussian rotational invariance. The next lemma is standard and bounds the moment generating function of this object.

### Lemma 1

Let $Z_{1:n} \sim {N{(0,{\sigma^{2}I_{n}})}}$. For every $\lambda \in \left\lbrack 0,\frac{1}{3{\max_{i \in {\lbrack n\rbrack}}{|\mu_{i}|}}} \right\rbrack$ we have that:

Note that ${\max_{i \in {\lbrack n\rbrack}}{|\mu_{i}|}} = {\sigma^{2}\left\| \overset{\circ}{A} \right\|_{\mathsf{o}\mathsf{p}}}$ and ${\sum_{i = 1}\mu_{i}^{2}} = {\sigma^{4}\left\| \overset{\circ}{A} \right\|_{F}^{2}}$ in our case. Moreover, since $\overset{\circ}{A}$ is diagonal free ${\lambda{\sum_{i = 1}^{n}\mu_{i}}} = {\lambda\sigma^{2}{{tr}\overset{\circ}{A}}} = 0$. Hence we have the bound:

To analyze the diagonal terms we will require the following lemma.

### Lemma 2

Let $X$ be $\sigma^{2}$-sub-Gaussian. We have that

for every nonnegative $\lambda$ satisfying $\lambda \leq \frac{1}{4\sigma^{2}}$.

We proceed to apply the above lemma. On the region $\{\lambda:{{\max{{|{4\lambdaa_{ii}}|}\sigma^{2}}} < 1}\}$ we have that

To finish the proof, we combine ([2.5](https://arxiv.org/html/2509.00881v1#S2.E5 "Equation 2.5 ‣ 2 The Proof ‣ An Elementary Proof of The Hanson-Wright Inequality")) and ([2.7](https://arxiv.org/html/2509.00881v1#S2.E7 "Equation 2.7 ‣ 2 The Proof ‣ An Elementary Proof of The Hanson-Wright Inequality")) with the Cauchy-Schwarz inequality (noting that this is unnecessary if $M$ is diagonal-free):

as long as ${\max{{|{4{({2\lambda})}a_{ii}}|}\sigma^{2}}} < 1$ and $\left. \left. {\left| {3{({2\lambda})}} \right\|\overset{\circ}{A}}\parallel \right._{\mathsf{o}\mathsf{p}} \middle| \sigma^{2} \right. < 1$. The result follows since ${\left\| \overset{\circ}{A} \right\|_{\mathsf{o}\mathsf{p}} \leq {2\left\| A \right\|_{\mathsf{o}\mathsf{p}}}}.$

## Proofs of Auxiliary Lemmata

### Proof of [Lemma˜1](https://arxiv.org/html/2509.00881v1#Thmlemma1 "Lemma 1. ‣ 2 The Proof ‣ An Elementary Proof of The Hanson-Wright Inequality")

For $\lambda \leq \frac{1}{3{\max_{i \in {\lbrack n\rbrack}}{|\mu_{i}|}}}$ we have that:

### Proof of [Lemma˜2](https://arxiv.org/html/2509.00881v1#Thmlemma2 "Lemma 2. ‣ 2 The Proof ‣ An Elementary Proof of The Hanson-Wright Inequality")

We proceed by expanding the moment generating function.

valid on the region $\{\lambda:{{|{2\lambda\sigma^{2}}|} < 1}\}$. In particular for, nonnegative $\lambda \leq \frac{1}{4\sigma^{2}}$ we have that

as was required. The step $( \dagger )$ can be shown as follows:

which finishes the proof. ∎
