## Introduction

We revisit the classical problem of smooth convex optimization: solve ${\min_{x \in {\mathbb{R}}^{d}}f}{(x)}$ where $f$ is convex and $M$-smooth (i.e., its gradient is $M$-Lipschitz). A celebrated result is that with a prudent choice of stepsizes $\{\alpha_{t}\}$, the gradient descent algorithm (GD) solves such a convex optimization problem to arbitrary accuracy from any initialization $x_{0}$. How quickly does GD converge? The mainstream approach (see e.g., the textbooks among many others) is to use a constant stepsize schedule $\alpha_{t} \equiv \overline{\alpha} \in {}$ since this ensures where $x^{\ast}$ denotes any minimizer of $f$, $f^{\ast}:={f{(x^{\ast})}}$ denotes the corresponding minimal value, and $c$ is a small constant, e.g., $c = \frac{1}{4}$ for $\overline{\alpha} = 1$.

The main question posed in Part I was: can we accelerate the convergence of GD without changing the algorithm---just by judiciously choosing the stepsizes? Here we continue to investigate this question, now in the setting of smooth convex optimization. Note that this is markedly different from classical approaches to acceleration---starting from Nesterov's seminal result of 1983, those approaches modify the basic GD algorithm by adding momentum, internal dynamics, or other additional building blocks beyond just changing the stepsizes. For this reason, we do not discuss that line of work in detail, and instead refer to for a recent survey of this mainstream approach to acceleration, and to for a full discussion of the relations between these approaches.

### Contribution

Figure 1: Silver Stepsize schedule {α0, α1, α2, …}. See (2.1) for the definition. Only the first n = 63 values are shown (i.e., k = 8). The fractal-like stepsizes are non-monotonic and have increasingly large “spikes” α2k − 1 = 1 + ρk − 1.

This paper provides a concise, self-contained proof that the Silver Stepsize Schedule proposed in Part I directly applies to smooth (non-strongly) convex optimization. This leads to faster convergence rates of GD for smooth convex optimization, as already pointed out in \[3, §1.1.4\].

In this setting, the Silver Stepsize Schedule is particularly simple. For any integer $n = {2^{k} - 1}$, we recursively construct the schedule $h_{{2n} + 1}$ of length ${2n} + 1$ from the schedule $h_{n}$ of length $n$ via where $\rho:={1 + \sqrt{2}}$ denotes the silver ratio, and $h_{1}:={\lbrack\sqrt{2}\rbrack}$. This results in the simple pattern $\lbrack\sqrt{2},\;2,\sqrt{2},{\;1 + \sqrt{2}},\ldots\rbrack$ as depicted in Figure 1. This schedule is exactly the Silver Stepsize Schedule from in the limit that the strong convexity parameter vanishes (see Remark 2.2. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization") for details), and bears similarities to those; see §1.2.

We show that these stepsizes yield an improved convergence rate (1.2) where $\frac{c}{n}$ is replaced by This bound gives the correct asymptotic scaling of $r_{k}$ since the inequality is asymptotically tight.

### Theorem 1.1 (Main result)

For any horizon $n = {2^{k} - 1}$, any dimension $d$, any $M$-smooth convex function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, and any initialization $x_{0} \in {\mathbb{R}}^{d}$, where $x^{\ast}$ denotes any minimizer of $f$, and $x_{n}$ denotes the output of $n$ steps of GD using the Silver Stepsize Schedule. In particular, in order to achieve error ${{f{(x_{n})}} - f^{\ast}} \leqslant \varepsilon$, it suffices to run GD for We make several remarks. 1) This rate $n^{- {\log_{2}\rho}} \approx n^{- 1.2716}$ is intermediate between the textbook unaccelerated rate $n^{- 1}$ and the accelerated rate $n^{- 2}$ due to Nesterov in 1983; see Figure 2 for a visualization. 2) The Silver Stepsize Schedule is independent of the horizon, see §2. 3) We conjecture that, up to a constant factor, the rate $r_{k}$ is optimal among all possible stepsize schedules. This will be addressed in the forthcoming Part III.

Figure 2: Upper bound on the optimality gap f (xn) − f*, as a function of the number of iterations n. The three plots correspond to the rates O (n−1) for the standard constant stepsize 1/M [14, Corollary 2.1.2], O (n−log2ρ) ≈ O (n−1.2716) for the Silver Stepsize Schedule (Theorem 1.1), and O (n−2) for Nesterov acceleration [14, Theorem 2.2.2].

### Related work

Several time-varying stepsize schedules have been considered, e.g., Armijo-Goldstein rules, Polyak-type schedules, Barzilai-Borwein-type schedules, etc. However, until recently, no convergence analyses improved over the textbook unaccelerated rate except in the special case of minimizing convex quadratics. Here we discuss the recent line of work on accelerated GD via time-varying stepsizes. For brevity, we refer to Paper I for a more complete discussion of adjacent bodies of literature.

Beginning with Altschuler's 2018 MS thesis, a line of work designed time-varying stepsize schedules to achieve faster convergence rates for (non-quadratic) convex optimization. The thesis showed that time-varying stepsizes can lead to improvements over the textbook unaccelerated GD rate---by an optimal asymptotic factor in the separable setting by using random stepsizes, and by a constant factor in the strongly convex setting by giving optimal stepsizes for $n = {2,3}$. A key difficulty in the general non-separable setting is that the search for optimal stepsizes is non-convex and computationally difficult for larger horizons $n$.

In 2022, Das Gupta et al. combined Branch & Bound techniques with the PESTO SDP of to develop algorithms that perform this search numerically, and as an example computed good approximate schedules in the convex setting for larger values of $n$ up to $50$. They observed a fit of roughly $O{(n^{- 1.178})}$ and suggested from this that the asymptotic rate may be faster than the textbook rate $O{(n^{- 1})}$.

In July 2023, Grimmer showed how to prove asymptotic rates for the (non-strongly) convex setting by periodically cycling through finite schedules. While in the strongly convex setting composing progress from different cycles just amounts to multiplying contraction rates, in the non-strongly convex setting this can be more subtle depending on the approach.^11^1Cf., our recursive gluing approach, which is a simple way of composing progress that unifies the convex (in §3) and strongly convex settings (in Paper I). This is why our analysis is so compact and completely bypasses the machinery of straightforward patterns. See Remark 3.1. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). To deal with this, he introduced the notion of straightforward stepsize patterns and obtained a constant-factor improvement over the textbook unaccelerated rate by cycling through approximate schedules of length $n = 127$. From these numerics, he conjectured that further optimizing stepsizes might lead to an asymptotic rate of $O{({({n{\log n}})}^{- 1})}$, a milder improvement than that conjectured .

In September 2023, two concurrent papers appeared. Altschuler and Parrilo was Part I: there we proposed the Silver Stepsize Schedule of arbitrary size to prove asymptotic acceleration for the strongly convex setting. This improved the textbook unaccelerated rate $\Theta{(\kappa)}$ to ${\Theta{(\kappa^{\log_{2}\rho})}} \approx {\Theta{(\kappa^{0.7864})}}$ where $\kappa$ is the condition number. We conjectured and provided partial evidence that these rates are optimal among all possible stepsize schedules. This result was achieved by introducing the technique of recursive gluing to establish multi-step descent, which we make use of here. The other paper was Grimmer et al.. By utilizing a certain non-periodic sequence of increasingly large stepsizes and building upon the "straightforwardness" machinery , they proved the rate $O{(n^{- 1.0245})}$ for the convex setting in v1, later improved to $O{(n^{- 1.0564})}$ in v2.

The results in Part I were stated for the strongly convex setting. As pointed out throughout that paper, this is not a restriction because on the one hand those results immediately imply analogously accelerated rates ${\Theta{(n^{- {\log_{2}\rho}})}} \approx {\Theta{(n^{- 1.2716})}}$ for the convex setting via a standard black-box reduction; and on the other hand, this reduction can be bypassed by re-doing the analysis for the convex setting since all the core conceptual ideas extend directly \[3, §1.1.4\]. The present paper provides these details.

### Notation

### Indexing

Throughout, the horizon is $n = {2^{k} - 1}$. This correspondence between $n \in {\{ 1,3,7,15,\ldots\}}$ and $k \in {\{ 1,2,3,4,\ldots\}}$ allows re-indexing in a way that simplifies notation for the recursion.

### Rescaling

For simplicity, we normalize $M = 1$, i.e., ${\|{{{\nabla f}{(x)}} - {{\nabla f}{(y)}}}\|} \leqslant {\|{x - y}\|}$ for all $x,y$. This is without loss of generality since if $h$ is $M$-smooth and convex, then $f:={h/M}$ is $1$-smooth and convex, thus the result we establish ${f_{n} - f^{\ast}} \leqslant {r_{k}{\|{x_{0} - x^{\ast}}\|}^{2}}$ implies ${h_{n} - h^{\ast}} \leqslant {r_{k}M{\|{x_{0} - x^{\ast}}\|}^{2}}$. Note that running GD on $f$ simply amounts to rescaling the Silver Stepsize Schedules for $h$ by $1/M$.

## Silver Stepsize Schedule

The Silver Stepsize Schedule is defined recursively in (1.3). Here we mention an equivalent direct expression and make several remarks. Let $\nu{(t)}$ denote the $2$-adic valuation of $t$, i.e., the smallest non-negative integer $i$ such that $2^{i}$ is in the binary expansion of $t$. For example, ${\nu{}} = 0$, ${\nu{}} = 1$, ${\nu{}} = 0$, ${\nu{}} = 2$, etc.

### Definition 2.1 (Silver Stepsize Schedule for smooth convex optimization)

For $t \in {\{ 0,1,2,\ldots\}}$, the $t$-th stepsize of the Silver Stepsize Schedule is This schedule is non-monotonic, fractal-like, and has increasingly large spikes that grow exponentially (by a factor of $\rho$) yet become exponentially less frequent (by a factor of $2$). See Figure 1. It can also be easily implemented^22^2For instance, in Python the command \[1+rho\*\*((k & -k).bit_length-2) for k in range\] generates the first $63$ steps of the Silver Schedule shown in Figure 1. in any computer language.

### Remark 2.2 (Limit of Silver Stepsize Schedules in the strongly convex case)

The schedule (2.1. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) is simply the Silver Stepsize Schedule for smooth *strongly*-convex optimization in Part I, in the limit as the strong convexity parameter tends to $0$. The stepsizes simplify in the limit: they increase by a factor of $\rho$, shorter schedules are prefixes of longer schedules, neither $a_{1}$ nor any of the $b_{n}$ sequence in is needed, and they are non-periodic (hence why there is no rate saturation here).

We also record a simple closed-form expression for the sum of the first $n = {2^{k} - 1}$ Silver Stepsizes.

### Lemma 2.3 (Sum of Silver Stepsizes)

${\sum_{t = 0}^{n - 1}\alpha_{t}} = {\rho^{k} - 1}$ for any $k \in {\mathbb{N}}$.

### Proof

The base case $k = 1$ is trivial. The inductive step follows from the recursion (1.3). ∎

## Recursive gluing

Here we prove that the Silver Stepsize Schedule has convergence rate $r_{k}$ for smooth convex optimization. The analysis closely mirrors the strongly convex setting in Part I: we prove the advantage of time-varying stepsizes via multi-step descent rather than iterating the greedy 1-step bound, show multi-step descent by exploiting long-range consistency conditions along the GD trajectory, certify multi-step descent via recursive gluing, and recursively glue by combining the same three components in the same way. In the interest of brevity, we refer to for a detailed discussion of all these concepts.

Briefly, the idea behind multi-step descent is that it is essential to capture how different iterations affect other iterations' progress. We do this by exploiting long-range consistency conditions between the iterates along GD's trajectory, as encoded by the co-coercivities The significance of these co-coercivities is that the constraints ${\{{Q_{ij} \geqslant 0}\}}_{i \neq j \in {\{ 0,1,\ldots,n, \ast \}}}$ are necessary and sufficient for the existence of a $1$-smooth convex function $f$ satisfying $f_{i} = {f{(x_{i})}}$ and $g_{i} = {{\nabla f}{(x_{i})}}$ for each $i \in {\{ 0,1,\ldots,n, \ast \}}$. In other words, the co-coercivity conditions ${\{{Q_{ij} \geqslant 0}\}}_{i \neq j \in {\{ 0,1,\ldots,n, \ast \}}}$ generate all possible long-range consistency constraints on the objective function $f$. Or, said another way, the co-coercivity conditions generate all possible valid inequalities with which one can prove convergence rates for GD. For a further discussion, see \[3, §2.2\].

Concretely, to prove Theorem 1.1. ‣ 1.1 Contribution ‣ 1 Introduction ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), we exhibit explicit non-negative multipliers $\lambda_{ij}$ satisfying where we use the shorthand $c_{k}:=\frac{1}{2r_{k}}$. Since ${\sum_{ij}{\lambda_{ij}Q_{ij}}} \geqslant 0$ for any $1$-smooth convex function, and since ${\|{x_{n} - {c_{k}g_{n}} - x^{\ast}}\|}^{2} \geqslant 0$ trivially as it is a square, this immediately implies the desired rate

### Remark 3.1 (The importance of a composable formulation)

We emphasize that while there are several alternative formulations to (3.2) that imply a rate like (3.3) after dropping terms, our formulation (3.2) is "canonical" because it composes well under recurrence (Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")). This enables a quite short and simple proof. Another reason this formulation is particularly nice is because the base case $n = 0$ amounts to a re-writing of the definition of $Q_{\ast 0}$, which is an improvement over the standard bound ${f_{0} - f^{\ast}} \leqslant {\frac{1}{2}{\|{x_{0} - x^{\ast}}\|}^{2}}$. In fact, this improvement is precisely what makes recursive gluing work so seamlessly.

### Example 3.2 ($n = 0$)

For $n = 0$, the identity (3.2) is Here, $r_{0} = \frac{1}{2}$, $c_{0} = 1$, and the only non-zero multiplier is $\lambda_{\ast 0} = 1$.

### Example 3.3 ($n = 1$)

For $n = 1$, the identity (3.2) is For larger horizons $n$, we construct $\lambda_{ij}$ via the recursive gluing technique of. See Figure 3. Below, we say that the multipliers ${\{\sigma_{ij}\}}_{{i,j} \in {\{ 0,\ldots,n, \ast \}}}$ satisfy the $\ast$-sparsity property if $\sigma_{i \ast} = 0$ for all $i < n$. This is satisfied by construction and simplifies part of the proof (isolated in Lemma 3.5. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")).

Figure 3: Components of the recursively glued certificate in Theorem 3.4, illustrated here for combining two copies of the n = 3 certificate (shaded) to create the 2 n + 1 = 7 certificate. The structure of this recursive gluing is identical to the strongly convex setting from Part I, modulo re-indexing for horizons of the form n = 2k − 1 rather than 2k.

### Theorem 3.4 (Recursive gluing)

Let $n = {2^{k} - 1}$. Suppose ${\{\sigma_{ij}\}}_{{i,j} \in {\{ 0,\ldots,n, \ast \}}}$ satisfies $\ast$-sparsity and certifies the $n$-step rate, i.e., Then there exists ${\{\lambda_{ij}\}}_{{i,j} \in {\{ 0,\ldots,{{2n} + 1}, \ast \}}}$ that satisfies $\ast$-sparsity and certifies the ${2n} + 1$-step rate, i.e., Moreover, this certificate is explicitly given by The "gluing component" $\Theta$ is defined as The "rank-one correction" $\Xi$ is zero except the entries ${\{\Xi_{ij}\}}_{{i \in {\{ n,{{2n} + 1}, \ast \}}},{j \in {\{{n + 1},\ldots,{2n}\}}}}$ which are The "sparse correction" $\Delta$ is zero except the entries ${\{\Delta_{ij}\}}_{i \neq j \in {\{ n,{{2n} + 1}, \ast \}}}$ which are We remark that using this recursion, one can also write out the $n$-step certificate directly. The value of each multiplier then depends on the binary expansion of its indices.

This recursive gluing immediately implies the main result of the paper, Theorem 1.1. ‣ 1.1 Contribution ‣ 1 Introduction ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization").

### Proof of Theorem 1.1. ‣ 1.1 Contribution ‣ 1 Introduction ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")

It suffices to prove (3.2); we prove this by induction. The base case $n = 1$ is Example 3.3. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). The inductive step is Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). ∎ The rest of the section is dedicated to proving Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). We first isolate two helper lemmas in §3.1, and then we combine them to prove the result in §3.2 ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). For notational simplicity, henceforth we assume $x^{\ast} = 0$; this is without loss of generality after translating.

### Helper lemmas

Here we provide three helper lemmas for the proof of Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). The first lemma explicitly computes all multipliers involving $x^{\ast}$ for the $n$-step certificate.

### Lemma 3.5 (Multipliers involving $x^{\ast}$)

$\sigma_{n \ast} = {\rho^{k} - 1}$, $\sigma_{\ast n} = \frac{1}{2r_{k}}$, and $\sigma_{\ast t} = \alpha_{t}$ for $t \in {\{ 0,\ldots,{n - 1}\}}$.

### Proof

Expand both sides of the identity (3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) using the $\ast$-sparsity assumption, the definition of the co-coercivities, and the definition of GD, i.e., $x_{t} = {x_{0} - {\sum_{s = 0}^{t - 1}{\alpha_{s}g_{s}}}}$. Matching coefficients for the $\langle x_{0},g_{t}\rangle$ terms yields the claimed formulas for $\sigma_{\ast t}$. Matching coefficients for the $f^{\ast}$ term gives the identity $\sigma_{n \ast} = {{\sum_{j = 0}^{n}\sigma_{\ast j}} - \frac{1}{2r_{k}}}$. This equals $\rho^{k} - 1$ by Lemma 2.3. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). ∎ The next two lemmas are more substantial. These help us verify (3.5. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"))---which consists of a linear form in all ${2n} + 3$ function values and a quadratic form in all ${2n} + 3$ gradients and iterates. Naïvely verifying such an identity requires checking $\Theta{(n)}$ coefficients for the linear form and $\Theta{(n^{2})}$ coefficients for the quadratic form. The following two lemmas show that due to the recursive construction of the Silver Stepsize Schedule and the gluing, these forms only affect the indices $n,{{2n} + 1}, \ast$. This reduces verifying the rate certificate (3.5. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) to checking only $\Theta{}$ coefficients, as detailed below in §3.2 ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). Below, for shorthand, let $F_{ij}:={2{({f_{i} - f_{j}})}}$ and $P_{ij}:={{2{\langle g_{j},{x_{j} - x_{i}}\rangle}} - {\|{g_{i} - g_{j}}\|}^{2}}$ denote the linear and quadratic components of $Q_{ij}$, respectively. For bookkeeping purposes, we use $3$-dimensional vectors and $4 \times 4$ matrices to denote the coefficients of these forms.

### Lemma 3.6 (Succinct linear forms)

Let $u:={\lbrack f_{n},f_{{2n} + 1},f^{\ast}\rbrack}^{T}$, and let ${e,s,\ell} \in {\mathbb{R}}^{3}$ be the vectors defined in Appendix A.1 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization").

Gluing error. ${\frac{f^{\ast} - f_{{2n} + 1}}{r_{k + 1}} - {\sum_{ij}{\Theta_{ij}F_{ij}}}} = {\langle e,u\rangle}$ Sparse correction. ${\sum_{ij}{\Delta_{ij}F_{ij}}} = {\langle s,u\rangle}$ Rank-one correction. ${\sum_{ij}{\Xi_{ij}F_{ij}}} = {\langle\ell,u\rangle}$

### Proof

Expand the definition of co-coercivities, simplify the rank-one correction using Lemma 2.3. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), and simplify the sparse correction using the Pell recurrence $\rho^{k + 1} = {{2\rho^{k}} + \rho^{k - 1}}$. ∎

### Lemma 3.7 (Succinct quadratic forms)

Let $v:={\lbrack x_{n},g_{n},x_{{2n} + 1},g_{{2n} + 1}\rbrack}^{T}$, and let $E$, $S$, $L$ be the $4 \times 4$ matrices defined in Appendix A.2 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization").

Sparse correction. ${\sum_{ij}{\Delta_{ij}P_{ij}}} = {\langle S,{vv^{T}}\rangle}$ Rank-one correction. ${\sum_{ij}{\Xi_{ij}P_{ij}}} = {\langle L,{vv^{T}}\rangle}$

### Proof

Deferred to Appendix A.2 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization") for brevity. ∎

### Proof of recursive gluing (Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"))

### Non-negativity

We verify $\lambda_{ij} \geqslant 0$ for all $i \neq j \in {\{ 0,\ldots,{{2n} + 1}, \ast \}}$. For nearly all entries, this is obvious since $\lambda_{ij}$ is constructed by adding and multiplying non-negative numbers. For the remaining entries where either $\Xi$ or $\Delta$ is negative, compute the corresponding entry of $\lambda$ by summing the corrections and using Lemma 3.5. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). This gives $\lambda_{n \ast} = 0$, $\lambda_{{{2n} + 1}, \ast} = {\rho^{k + 1} - 1}$, $\lambda_{\ast,n} = {\rho^{k - 1} + 1}$, $\lambda_{\ast,{{2n} + 1}} = \frac{1}{2r_{k + 1}}$, and $\lambda_{\ast,t} = \alpha_{t}$ for all $t \in {\{{n + 1},\ldots,{2n}\}}$. All these entries are clearly non-negative.

### Rate certificate

The identity (3.5. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) has two components: a linear form in the function values and a quadratic form in the iterates and gradients. For the linear form, it suffices to verify ${e - s - \ell} = 0$ by Lemma 3.6. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), where ${e,s,\ell} \in {\mathbb{R}}^{3}$ are the vectors defined in Appendix A.1 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). This is obvious by inspection. For the quadratic form, it suffices to verify ${E - S - L} = 0$, where ${E,S,L} \in {\mathbb{R}}^{4 \times 4}$ are the matrices in Lemma 3.7. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization") defined in Appendix A.2 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). By plugging in the explicit values for $r_{k}$ and $\Delta$, this is straightforward to check by hand. For brevity, we provide a simple Mathematica script that verifies these identities at the URL.
