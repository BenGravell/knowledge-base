## Introduction

In sequence prediction the goal of the learner is to predict the next token accurately according to a specified loss function, such as the mean square error or cross-entropy. This fundamental problem in machine learning has gained increased importance with the rise of large language models, which perform sequence prediction on tokens using cross entropy. The focus of this paper is preconditioning, i.e. modifying the target sequence to make it easier to learn. A classic example is differencing, introduced by Box and Jenkins in the 1970s Box and Jenkins, which transforms observations $\mathbf{y}_{1},\mathbf{y}_{2},\dots$ into successive differences, It is widely acknowledged that learning this sequence can be "easier\" than learning the original sequence for a large number of modalities. In this work we seek a more general framework for sequence preconditioning that captures the same intuition behind differencing and extends it to a broader class of transformations. The question we ask is What is the general form of sequence preconditioning that enables provably accurate learning?

We address this question by introducing a preconditioning method which takes in $n$ fixed coefficients $c_{0},\dots,c_{n}$ and converts the sequence of observations $\mathbf{y}_{1},\dots,\mathbf{y}_{t},\dots$ to the sequence of convolved observations^11^1This recovers differencing when $n=2$, $c_{0}=1$, and $c_{1}=-1$.

From an information-theoretic perspective, approaches of this kind seem futile---predicting $\mathbf{y}_{t}$ or $\sum_{i}c_{i}\mathbf{y}_{t-i}$ seems equally hard in an adversarial setting. Yet we show that when the data arises from a linear dynamical system (LDS), there exists a *universal* form of preconditioning that provably improves learnability, independent of the specific system. In the LDS setting, we show that preconditioning significantly strengthens existing prediction methods, leading to new regret bounds. Here, preconditioning has an elegant effect: the preconditioning filter forms coefficients of an $n$ degree polynomial, and the hidden system transition matrix is evaluated on this polynomial-- potentially shrinking the domain. In this setting, shrinking the learnable domain is akin to making the problem "easier to learn", a relationship that is formalized by Hazan and Singh. This allows us to prove the first dimension-independent sublinear regret bounds for asymmetric linear dynamical systems that are marginally stable.

### Our results

Our main contribution is *Universal Sequence Preconditioning*, a novel method of sequence preconditioning which convolves the target sequence with the coefficients of the $n$-th monic Chebyshev polynomial. We give a more general form of preconditioning, allowing arbitrary user-specified coefficients, in Algorithm 1 and an online version in Algorithm 4 (Appendix C). We analyze the effect of Universal Sequence Preconditioning on two canonical sequence prediction algorithms in the online setting: convex regression and spectral filtering. In either case, the results are impressive-- yielding the first known sublinear regret bounds as compared to the optimal ground-truth predictor that are simultaneously applicable to marginally stable systems, independent of the hidden dimension (up to logarithmic factors), and applicable to systems whose transition matrix is asymmetric^22^2Our results only hold for asymmetric matrices whose eigenvalues have imaginary component bounded above by $O(1/\log(T))$. This is somewhat tight, see Section B. (see Table 1 ).

2: Input: training data (u1: T1: N, y1: T1: N) where (uti, yti) is the t-th input/output pair in the i-th sequence; coefficients c0: n; prediction algorithm 𝒜. 5: y1: Tpreconditioned, i ← convolution(y1: Ti, c0: n) ⊲ $\mathbf{y}^{\textrm{preconditioned},i}_{t}=\mathbf{y}^{i}_{t}+\sum_{j=1}^{n}c_{j}\mathbf{y}^{i}_{t-j}$ 7: Train 𝒜 on preconditioned data (u1: T1: N, y1: Tpreconditioned, 1: N). 11: Predict $\hat{\mathbf{y}}_{t}\leftarrow\mathcal{A}\left(\mathbf{u}_{1:t},\mathbf{y}_{1:(t-1)}\right)-\sum_{i=1}^{n}c_{i}\mathbf{y}_{t-i}$. Algorithm 1 General Sequence Preconditioning (Offline Version) First, applying USP to standard convex regression results in regret $\tilde{O}(T^{-2/13})$, which holds simultaneously across the three settings above and remains dimension-independent. For comparison, a naive analysis of regression yields a vacuous regret bound of $O(T^{5/2})$ on marginally stable systems. Second, combining USP with a variant of *spectral filtering* Hazan et al. that uses novel filters, the algorithm is able learn a broader class of linear dynamical systems-- in particular systems whose hidden transition matrix may be asymmetric. The enhanced method achieves regret $\tilde{O}(T^{-3/13})$, the best known rate under the joint conditions of - discussed above: marginal stability, dimension independence, and asymmetry. Both results require that the transition matrix eigenvalues have imaginary parts bounded by $O(1/\log T)$---a near-tight condition for achieving dimension-free regret. Further discussion on this appears in Appendix B.

USP + Spectral Filtering Table 1: Comparison of methods for learning LDS. USP extends learning to mildly asymmetric matrices with bounded complex eigenvalues.

Empirical results in Section 4 demonstrate that USP consistently improves performance across diverse algorithms---including regression, spectral filtering, and neural networks---and across data types extending beyond linear dynamical systems.

### Intuition for Universal Sequence Preconditioning

We now give some brief intuition for the result. Linear dynamical systems (LDS) are perhaps the most basic and well studied dynamical systems in engineering and control science. Given input vectors $\mathbf{u}_{1},\dots,\mathbf{u}_{T}\in\mathbb{C}^{d_{\textrm{in}}}$, the system generates a sequence of output vectors $\mathbf{y}_{1},\dots\mathbf{y}_{T}\in\mathbb{C}^{d_{\textrm{out}}}$ according to the law where $\mathbf{x}_{0},\dots,\mathbf{x}_{T}\in\mathbb{C}^{d_{\textrm{hidden}}}$ is a sequence of hidden states and $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D})$ are matrices which parameterize the LDS. We assume w.l.o.g. that $\mathbf{D}=0$. We can factor out the hidden state $\mathbf{x}_{t}$ so that the observation at time $t$ is Given coefficients $c_{0:n}=(c_{0},\dots,c_{n})$ let Consider a "preconditioned" target at time $t$ to be a linear combination of $\mathbf{y}_{t:t-n}$ with coefficients $c_{0:n}$. A key insight is the following identity, If we take $c_{0}=1$ (i.e. a monic polynomial), we can re-write $\mathbf{y}_{t}$ as This expression highlights our approach as a balance of three terms: The universal preconditioning term: it depends only on the coefficients $c_{0:n}$and not on any learning algorithm.

A term learnable via convex relaxation and regression, for example by denoting The diameter of the coefficient $\mathbf{Q}_{s}$ depends on the magnitude of the coefficients $c_{0:n}$.

The residual term with polynomial $p_{n}^{c}(\mathbf{A})$. By a careful choice of coefficients $c_{0:n}$, we can force this term to be very small.

The main insight we derive from this expression is the inherent tension between two terms $\aleph_{1},\aleph_{2}$. The polynomial $p_{n}^{c}(x)$ and its coefficients $c_{0},\dots,c_{n}$ control two competing effects: The preconditioning coefficients grow larger with the degree $n$ of the polynomial and the magnitude of the coefficients $c_{i}$. A higher degree polynomial and larger coefficients increase the diameter of the search space over the preconditioning coefficients, and therefore increase the regret bound stemming from the $\aleph_{1}$ component learning.

On the other hand, a larger search space can allow a broader class of polynomials $p_{n}(\cdot)$ which can better control of the magnitude of $p_{n}(\mathbf{A})$, and therefore reduce the search space of the $\aleph_{2}$ component.

What choice of polynomial is best? This work considers the Chebyshev polynomial. The reason is the following property of the $n$-th monic Chebyshev polynomial: As an example, consider any LDS whose hidden transition matrix $\mathbf{A}$ is diagonalizable and has eigenvalues in $$^33^3This work considers a broader class of hidden transition matrices.. By the above property, observe that $\|p_{n}(\mathbf{A})\|_{\infty}~\leq~2\cdot 2^{-n}$, therefore shrinking the $\aleph_{2}$ term at a rate exponential with the number of preconditioning coefficients. We pause to remark on the *universality* of this choice of polynomial. Indeed, one could instead have chosen the preconditioning coefficients to depend on $\mathbf{A}$ so that $p_{n}^{\mathbf{c}}(\cdot)$ is the characteristic polynomial of $\mathbf{A}$. By the Cayley-Hamilton theorem, $p_{n}(\mathbf{A})=0$. This means that $\aleph_{2}$ term is canceled out completely. However this would have required knowledge of the spectrum of $\mathbf{A}$. The Chebyshev polynomial, on the other hand, is agnostic to the particular hidden transition matrix. Moreover, even if the spectrum of $\mathbf{A}$ were known, choosing the preconditioning coefficients to form the characteristic polynomial would result in an algorithm which must learn hidden dimension many parameters, which is prohibitive. Instead, the degree of the Chebyshev polynomial must only grow logarithmically with the hidden dimension.

### Related work

Our manuscript is technically involved and incorporates linear dynamical systems, spectral filtering, complex Chebyshev and Legendre polynomials, Hankel and Toeplitz matrix eigendecay, Gaussian quadrature and other techniques. The related work is thus expansive, and due to space limitations we give a detailed treatment in Appendix A. Preconditioning in the context of time series analysis has roots in the classical work of Box and Jenkins Box and Jenkins. In their foundational text they propose differencing as a method for making the time series stationary, and thus amenable to statistical learning techniques such as ARMA (auto-regressive moving average) Anava et al.. The differencing operator can be applied numerous times, and for different lags, giving rise to the ARIMA family of forecasting models. Identifying the order of an ARIMA model, and in particular the types of differencing needed to make a series stationary, is a hard problem. This is a special case of the problem we consider: differencing corresponds to certain coefficients of preconditioning the time series, whereas we consider arbitrary coefficients. For a thorough introduction to modern control theory and exposition on open loop / closed loop predictors, learning via regression, and spectral filtering, see Hazan and Singh. The fundamental problem of learning in linear dynamical systems has been studied for many decades, and we highlight several key approaches below: System identification refers to the method of recovering $\mathbf{A},\mathbf{B},\mathbf{C}$ from the data. This is a non-convex problem and while many methods have been considered in this setting, they depend polynomially on the hidden dimension.

The (auto) regression method predicts according to $\hat{\mathbf{y}}_{t}=\sum_{i=1}^{h}\mathbf{M}_{i}\mathbf{u}_{t-i}$. The coefficients $\mathbf{M}_{i}$ can be learned using convex regression. The downside of this approach is that if the spectral radius of $\mathbf{A}$ is $1-\delta$, it can be seen that $\sim\frac{1}{\delta}$ terms are needed.

The regression method can be further enhanced with "closed loop\" components, that regress on prior observations $\mathbf{y}_{t-1:1}$. It can be shown using the Cayley-Hamilton theorem that using this method, $d_{h}$ components are needed to learn the system, where $d_{h}$ is the hidden dimension of $\mathbf{A}$.

Filtering involves recovering the state $x_{t}$ from observations. While Kalman filtering is optimal under specific noise conditions, it generally fails in the presence of marginal stability and adversarial noise.

Finally, spectral filtering combines the advantages of all methods above. It is an efficient method, its complexity does not depend on the hidden dimension, and works for marginally stable systems. However, spectral filtering requires $\mathbf{A}$ to be symmetric, or diagonalizable under the real numbers.

## Main Results

In this section we formally state our main algorithms and theorems. We show that the Universal Sequence Preconditioning method provides significantly improved regret bounds for learning linear dynamical systems than previously known when used in conjunction with two distinct methods. The first method is simple convex regression, and the second is spectral filtering. Both algorithms allow for learning in the case of marginally stable linear dynamical systems and allow for certain asymmetric transition matrices of arbitrary high hidden dimension. The regret bounds are free of the hidden dimension (up to logarithmic factors) -- which significantly extends the state of the art.

### Universal Sequence Preconditioning Applied to Regression

Algorithm 2 is an instantiation of Algorithm 4 for the method of convex regression. We set the preconditioning coefficients to be the coefficients of the $n$-th degree (monic) Chebyshev polynomial.

1: Input: initial parameter Q0; preconditioning coefficients c0: n from the n-th degree (monic) Chebyshev polynomial; convex constraints 𝒦 = {(Q0, …, Qn − 1) s.t. ∥Qj∥ ≤ Cdomain∥c∥1} 5: Predict $\hat{\mathbf{y}}_{t}(\mathbf{Q}^{t})=-\sum_{i=1}^{n}\mathbf{c}_{i}\mathbf{y}_{t-i}+\sum_{j=0}^{n}\mathbf{Q}^{t}_{j}\mathbf{u}_{t-j}$. 6: Observe true output yt and suffer loss $\ell_{t}(\mathbf{Q}^{t})=\|\hat{\mathbf{y}}_{t}(\mathbf{Q}^{t})-\mathbf{y}_{t}\|_{1}$. 7: Update and project: $$\mathbf{Q}^{t+1}\leftarrow\mathrm{proj}_{\mathcal{K}}\left(\mathbf{Q}^{t}-\eta_{t}\nabla\mkern-2.5mu_{\mathbf{Q}}\ell_{t}(\mathbf{Q}^{t})\right).$$ Algorithm 2 Universal Sequence Preconditioning for Regression Theorem 2.1 shows that vanishing loss compared to the optimal ground-truth predictor, at a rate that is independent of the hidden dimension of the system.

### Theorem 2.1

Let $\left\{\mathbf{u}_{t}\right\}_{t=1}^{T}\in\mathbb{C}^{d_{\textrm{in}}}$ be any sequence of inputs which satisfy $\|\mathbf{u}_{t}\|_{2}~\leq~1$ and let $\left\{\mathbf{y}_{t}\right\}_{t=1}^{T}\in\mathbb{C}^{d_{\text{out}}}$ be the corresponding output coming from some linear dynamical system $(\mathbf{A},\mathbf{B},\mathbf{C})$ as defined per Eq. 1. Let $\mathbf{P}$ diagonalize $\mathbf{A}$ (note $\mathbf{P}$ exists w.l.o.g.) and let $\kappa=\|\mathbf{P}\|\|\mathbf{P}^{-1}\|$. Assume that $\|\mathbf{B}\|\|\mathbf{C}\|\kappa~\leq~C_{\textrm{domain}}$. Let $\lambda_{1},\dots,\lambda_{d_{h}}$ denote the spectrum of $\mathbf{A}$. If then the predictions $\hat{\mathbf{y}}_{1},\dots,\hat{\mathbf{y}}_{T}$ from Algorithm 2 where the preconditioning coefficients $\mathbf{c}_{0:n}$ are chosen to be the coefficients of the $n$-th monic Chebyshev polynomial satisfy where $\tilde{O}(\cdot)$ hides polylogarithmic factors in $T$.

The proof of Theorem 2.1 is in Appendix D. For a simple baseline comparison, the regret achieved (via the same proof technique) by the vanilla regression algorithm without preconditioning is $O\left(C_{\textrm{domain}}\sqrt{d_{\text{out}}}T^{5/2}\right)$ which is not sublinear in $T$.

### Universal Sequence Preconditioning Applied to Spectral Filtering

Our second main result is the application of Universal Sequence Preconditioning to the spectral filtering algorithm Hazan et al.. Our results are more general and apply to any choice of polynomial, not just Chebyshev. In addition to applying USP to spectral filtering, we also propose a novel spectral filtering basis. Both changes to the vanilla spectral filtering algorithm are necessary to extend its sublinear regret bounds to the case of underlying systems with asymmetric hidden transition matrices. First we define the spectral domain Given horizon $T$ and $\alpha\in\mathbb{C}_{\beta}$ let where $\overline{\alpha}\in\mathbb{C}$ denotes the complex conjugate. The novel spectral filters are the eigenvectors of $\mathbf{Z}_{T-n-1}$, which we denote as $\phi_{1},\dots,\phi_{T-n-1}$. Note that in the standard spectral filtering literature, the spectral filtering matrix is an integral over the real line and does not involve the complex conjugate. Our new matrix has an entirely different structure and although it looks quite similar, it surprisingly upends the proof techniques to ensure exponential spectral decay, a critical property for the method. Future work examines this matrix more thoroughly, but in this paper we simply provide a standard bound on its eigenvalues.

1: Input: initial Q1: n1, M1: k1, horizon T, convex constraints 2: Let pnc(x) = c0xn + c1xn − 1 + … + cn and p̃nc(x) = (1 − x2)pnc(x). Let $\tilde{\mathbf{c}}_{0},\dots,\tilde{\mathbf{c}}_{n+2}$ be the coefficients of p̃nc(x). 3: Let ϕ1,..., ϕn be the top n eigenvectors of ZT − n − 1. 4: Assert $\tilde{\mathbf{c}}_{0}=1$. 6: Let $\tilde{\mathbf{u}}_{t-n-1:1}$ be ut − n − 1: 1 padded with zeros so it has dimension T − n − 1 × din. 7: Predict $\hat{\mathbf{y}}_{t}(\mathbf{Q}^{t},\mathbf{M}^{t})=-\sum_{i=1}^{n+2}\tilde{\mathbf{c}}_{i}\mathbf{y}_{t-i}+\sum_{j=0}^{n}\mathbf{Q}^{t}_{j}\mathbf{u}_{t-j}+\frac{1}{\sqrt{T}}\sum_{j=1}^{k}\mathbf{M}_{j}^{t}\phi_{j}^{\top}\tilde{\mathbf{u}}_{t-n-1:1}$. 8: Observe true yt, define loss $\ell_{t}(\hat{\mathbf{y}}_{t})=\|\hat{\mathbf{y}}_{t}(\mathbf{Q}^{t},\mathbf{M}^{t})-\mathbf{y}_{t}\|_{1}$. 9: Update and project: $(\mathbf{Q}^{t+1},\mathbf{M}^{t+1})=\mathrm{proj}_{\mathcal{K}}\left(\mathbf{Q}^{t},\mathbf{M}^{t})-\eta_{t}\nabla\mkern-2.5mu\ell_{t}(\mathbf{Q}^{t},\mathbf{M}^{t})\right)$ Algorithm 3 Universal Sequence Preconditioning for Spectral Filtering

### Theorem 2.2

Let $\left\{\mathbf{u}_{t}\right\}_{t=1}^{T}\in{\mathcal{R}}^{d_{\textrm{in}}}$ be any sequence of inputs which satisfy $\|\mathbf{u}_{t}\|_{2}~\leq~1$ and let $\left\{\mathbf{y}_{t}\right\}_{t=1}^{T}$ be the corresponding output coming from some linear dynamical system $(\mathbf{A},\mathbf{B},\mathbf{C})$ as defined per Eq. 1. Let $\mathbf{P}$ diagonalize $\mathbf{A}$ (note $\mathbf{P}$ exists w.l.o.g.) and let $\kappa=\|\mathbf{P}\|\|\mathbf{P}^{-1}\|$. Suppose the radius parameters of Algorithm 3 satisfy $R_{Q}~\geq~\|\mathbf{C}\|\|\mathbf{B}\|\|\mathbf{c}\|_{1}$ and $R_{M}~\geq~2\|\mathbf{C}\|\|\mathbf{B}\|\kappa\log(T)\left(\max_{j\in[d_{h}]}|\arg(\lambda_{j})|\right)^{4/3}T^{7/6}\left(\max_{\alpha\in\mathbb{C}_{\beta}}|p_{n}^{\mathbf{c}}(\alpha)|\right)$. Further suppose that the eigenvalues of $\mathbf{A}$ have bounded argument: Then the predictions $\hat{\mathbf{y}}_{1},\dots,\hat{\mathbf{y}}_{T}$ from Algorithm 3 where the preconditioning coefficients $\mathbf{c}_{0:n}$ are chosen to be the coefficients of the $n$-th monic Chebyshev polynomial satisfy We remark that the result of Theorem 2.2 is rather weak. Although the complex eigenvalues of $\mathbf{A}$ are not trivially bounded (trivial would be a bound of $1/T$), they still must be polynomially small in $T$. Moreover we note that the proof technique for the result does not make use of the critical properties of spectral filtering and relies much more on the power of preconditioning. The proof of Theorem 2.2 is in Section E.

## Proof Overview

In this section we give a high level overview of the proofs for Theorem 2.1 and Theorem 2.2. We start by recalling the intuition for Universal Sequence Preconditioning developed in Section 1.2 which shows that if $\left\{\mathbf{y}_{t}\right\}_{t=1}^{T}$ evolves as a linear dynamical system parameterized by matrices $(\mathbf{A},\mathbf{B},\mathbf{C})$ with inputs $\left\{\mathbf{u}_{t}\right\}_{t=1}^{T}$ then by Equation 3, Recall that $\aleph_{0}$ is the universal preconditioning component, $\aleph_{1}$ is the term that can easily be learned by convex relaxation and regression, and $\aleph_{2}$ is the critical term that contains $p_{n}^{c}(\mathbf{A})$. Both Theorem 2.1 and Theorem 2.2 use the standard result from online convex optimization (Theorem 3.1 from Hazan) that online gradient descent over convex domain $\mathcal{K}$ achieves regret $\frac{3}{2}GD\sqrt{T}$ as compared to the best point in $\mathcal{K}$, where $D$ denotes the diameter of $\mathcal{K}$ and $G$ denotes the maximum gradient norm.

### Regression: Proof of Theorem 2.1

In the case of regression, the domain is chosen so that $\aleph_{2}$ may be learned and the proof proceeds by bounding the diameter of such a domain and its corresponding maximum gradient norm to get regret $Cn^{2}\sqrt{d_{\text{out}}}\|c\|_{1}\sqrt{T}$ for a universal constant $C>0$ which depends on the norms of matrices $\mathbf{B}$ and $\mathbf{C}$ from the underlying system. Then $\aleph_{3}$ is treated as an un-learnable error term. Let $\lambda(\mathbf{A})$ denote the set of eigenvalues of $\mathbf{A}$. By the simple magnitude bound of the error of ignoring this term can be very small if $\max_{\lambda(\mathbf{A})}|p_{n}(\lambda(\mathbf{A}))|$ is small. In the proof of Theorem 2.1 in Appendix D we show that the regret for a generic polynomial $p_{n}^{c}$ defined by coefficients $c_{0:n}$ is where $\mathcal{D}$ is the region where $\mathbf{A}$ is allowed to have eigenvalues (see Theorem D.1. ‣ Appendix D Proof of Convolutional Preconditioned Regression Performance Theorem 2.1 ‣ Universal Sequence Preconditioning")). Therefore, to get sublinear regret, we must choose a polynomial which has bounded $\ell_{1}$ norm of its coefficients, while also exhibits very small infinity norm on the domain of $\mathbf{A}$'s eigenvalues.

### Spectral Filtering: Proof of Theorem 2.2

In the case of spectral filtering, the domain is chosen so that both $\aleph_{2}$ and $\aleph_{3}$ may be learned. Because spectral filtering learns $\aleph_{3}$, it is able to accumulate less error and hence achieves a better regret bound of $O(T^{-3/13})$ as compared to regression's $O(T^{-2/13})$. At a high level, the proof proceeds by exploiting the fact that $p_{n}(\mathbf{A})$ shrinks the size of the learnable domain. However this is not enough, in order to extend the result to systems where $\mathbf{A}$ may have complex eigenvalues, the spectral filters must be eigenvalues of a new matrix, defined in Eq. 5, whose domain of integration includes the possibly complex eigenvalues of $\mathbf{A}$. To get the dimension-independent regret bounds enjoyed by spectral filtering in this new setting where complex eigenvalues may occur, the exponential decay of $\mathbf{Z}_{T}$ from Eq. 5 must be established. This is nontrivial and requires several novel techniques inspired by Beckermann and Townsend. The details are in Appendix E.3.1. Theorem 2.2 gives the main guarantee for the spectral filtering algorithm, which states that Algorithm 3 instantiated with some choice of polynomial $p_{n}^{c}(\cdot)$ achieves regret Both this theorem, as well as our new guarantee for convex regression, leads us to the following question: Is there a universal choice of polynomial $p_{n}(x)$, where $n$ is independent of hidden dimension, which guarantees sublinear regret?\

### Using the Chebyshev Polynomial over the Complex Plane

For the real line, the answer to this question is known to be positive using the Chebyshev polynomials of the first kind. In general, the $n^{\textrm{th}}$ (monic) Chebyshev polynomial $M_{n}(x)$ satisfies $\max_{x\in}|M_{n}(x)|~\leq~2^{-(n-1)}$. However, we are interested in a more general question over the complex plane. Since we care about linear dynamical systems that evolve according to a general asymetric matrix, we need to extending our analysis to $\mathbb{C}_{\beta}$. This is a nontrivial extension since, in general, functions that are bounded on the real line can grow exponentially on the complex plane. Indeed, $2^{n-1}M_{n}(x)=\cos(n\arccos(x))$ and while $\cos(x)$ is bounded within $$ for any $x\in{\mathcal{R}}$, over the complex numbers we have $\cos(z)=\frac{1}{2}(e^{iz}+e^{-iz}),$ which is unbounded. Thus, we analyze the Chebyshev polynomial on the complex plane and provide the following bound.

### Lemma 3.1

Let $z\in\mathbb{C}$ be some complex number with magnitude $|\alpha|~\leq~1$. Let $M_{n}(\cdot)$ denote the $n$-th monic Chebyshev polynomial. If $|\arg(z)|~\leq~1/64n^{2}$, then $|M_{n}(z)|~\leq~1/2^{n-2}$.

We provide the proof in Appendix G. We also must analyze the magnitude of the coefficients of the Chebyshev polynomial, which can grow exponentially with $n$. We provide the following result.

### Lemma 3.2

Let $M_{n}(\cdot)$ have coefficients $c_{0},\dots,c_{n}$. Then $\max_{k=0,\dots,n}|c_{k}|~\leq~2^{0.3n}$.

The proof of Lemma 3.2 is in Appendix G. Together, these two lemmas are the fundamental building block for universal sequence preconditioning and for obtaining our new regret bounds.

## Experimental Evaluation

We empirically validate that convolutional preconditioning with Chebyshev or Legendre coefficients yields significant online regret improvements across various learning algorithms and data types. Below we summarize our data generation, algorithm variants, hyperparameter tuning, and evaluation metrics.

### Synthetic Data Generation

We generate $N=200$ sequences of length $T=2000$ via three mechanisms: (i) a noisy linear dynamical system, (ii) a noisy nonlinear dynamical system, and (iii) a noisy deep RNN. Inputs $\mathbf{u}_{1:T}\sim\mathcal{N}(0,I)$.

### Linear Dynamical System

Sample $(\mathbf{A},\mathbf{B},\mathbf{C})$ with $\mathbf{A}\in{\mathcal{R}}^{300\times 300}$ having eigenvalues $\{z_{j}\}$ drawn uniformly in the complex plane subject to $\mathrm{Im}(z_{j})\leq\tau_{\rm thresh}$ and $L\leq|z_{j}|\leq U$, and $\mathbf{B},\mathbf{C}\in{\mathcal{R}}^{300}$. Then

### Nonlinear Dynamical System

Similarly sample $(\mathbf{A}_{1},\mathbf{B}_{1},\mathbf{C})$ and $(\mathbf{A}_{2},\mathbf{B}_{2})$ with $\mathbf{A}_{i}\in{\mathcal{R}}^{10\times 10}$, $\mathbf{B}_{i},\mathbf{C}\in{\mathcal{R}}^{10}$. Then

### Deep RNN

We randomly initialize a sparse 10-layer stack of LSTMs with hidden dimension $100$ and ReLU nonlinear activations. Given $\mathbf{u}_{1:T}$ we use this network to generate $\mathbf{y}_{1:T}$.

### Algorithms and Preconditioning Variants

We evaluate the following methods: Regression (Alg. 2), Spectral Filtering (Alg. 3), DNN Predictor: $n$-layer LSTM with dims $[d_{1},\dots,d_{n}]$, ReLU. Each method is applied with one of: *Chebyshev:* $\mathbf{c}_{0:n}$ are the coefficients for the $n$th-Chebyshev polynomial. Note that when $n=2$ we have $\mathbf{c}_{0}=1$ and $\mathbf{c}_{1}=-1$ and therefore this is the method of *differencing* discussed in the introduction.

*Legendre:* $\mathbf{c}_{0:n}$ are the coefficients for the $n$th-Legendre polynomial *Learned:* $\mathbf{c}_{0:n}$ is a parameter learned jointly with the model parameters We test polynomial degrees $n\in\{2,5,10,20\}$. This choice of degrees shows a rough picture of the impact of $n$.

### Hyperparameter Tuning

To ensure fair comparison, for each algorithm and conditioning $\mathbf{c}$ variant we perform a grid search over learning rates $\eta\in\{10^{-3},10^{-2},10^{-1}\}$, selecting the one minimizing average regret across the $N$ sequences. In the case of the learned coefficients, we sweep over the 9 pairs of learning rates $(\eta_{\textrm{model}},\eta_{\textrm{coefficients}})\in\{10^{-3},10^{-2},10^{-1}\}\times\{10^{-3},10^{-2},10^{-1}\}$.

### Results

Tables 2--4 report the mean $\pm$ std of the absolute error over the final 200 predictions, averaged across 200 runs. In the linear and nonlinear cases we train a 2-layer DNN (dims $$); for RNN-generated data we match the 10-layer (100-dim) generator.

Preconditioning drastically reduces baseline errors for all algorithms and data types.

Chebyshev and Legendre yield nearly identical gains.

For Chebyshev and Legendre, once the degree is higher than $5-10$ the performance degrades since $\|\mathbf{c}\|_{1}$ gets very large (see our Lemma 3.2 which shows that these coefficients grow exponentially fast).

Improvements decay as the complex threshold $\tau_{\rm thresh}$ increases, consistent with our theoretical results which must bound $\mathrm{Im}(z_{j})$.

Learned coefficients excel with regression and spectral filtering but destabilize the DNN on nonlinear and RNN‐generated data.

Table 2: Linear dynamical system data (detailed in Sec. 4.1) across varying complex threshold $\tau_{\rm thres}$.

Table 3: Nonlinear data (detailed in Sec. 4.1) across varying complex threshold $\tau_{\rm thres}$.

Table 4: Performance (average absolute error of the last 200 predictions) of a 10-layer DNN (detailed in Sec. 4.2) on data generated from the same model (detailed in Sec. 4.1).

### ETTh1 Dataset

To evaluate whether our proposed preconditioning approach generalizes to real-world time series, we conduct experiments on the well-established ETTh1 dataset from the Electricity Transformer Temperature (ETT) benchmark Zhou et al.. The ETTh1 dataset consists of continuous hourly measurements of load and oil temperature collected from electricity transformers and has been used in several recent works Zhou et al.; Wu et al.; Nie et al.; Gu et al.; Gupta and et al.; Zeng et al.; Nguyen et al.. We study the effect of preconditioning on a $10$-layer LSTM with hidden dimension $100$ per layer using the Adam optimizer. We set the horizon to be $T=5000$ and we sweep over a broader range of learning rates $\eta\in\{10^{-j}\}_{j=0,1,2,3,4,5}$. As before we consider (i) no preconditioning (baseline), (ii) fixed Chebyshev coefficients, (iii) fixed Legendre coefficients, and (iv) coefficients learned jointly with model parameters. As seen in Figure 1, preconditioning with Chebyshev and Legendre for degree $5$ the best performance after only the first $1000$ iterations, while the performance of jointly learning the coefficients is worse at this stage. The performance of all three preconditioning methods are roughly on par with each other by $2500$ iterations and by the full horizon $T=5000$, jointly learning the coefficients results in the best average prediction error.

Figure 1: Absolute prediction error on final 200 predictions averaged over 10 independent runs for 10-layer LSTM with layer dimension 100 using Adam optimizer and sweeping over learning rates for each run.

## Discussion

There are many settings in machine learning where universal, rather than learned, rules have proven very efficient. For example, physical laws of motion can be learned directly from observation data. However, Newton's laws of motion succinctly crystallize very general phenomenon, and have proven very useful for large scale physics simulation engines. Similarly, in the theory of mathematical optimization, adaptive gradient methods have revolutionized deep learning. Their derivation as a consequence of regularization in online regret minimization is particularly simple Duchi et al., and thousands of research papers have not dramatically improved the initial basic ideas. These optimizers are, at the very least, a great way to initialize learned optimizers Wichrowska et al..

By analogy, our thesis in this paper is that universal preconditioning based on the solid theory of dynamical systems can be applicable to many domains or, at the very least, an initialization for other learning methods.
