## Introduction

In robust control problems, we seek absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, and integral quadratic constraints (IQCs).

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

Even when BIBO stable systems are exponentially stable, the estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates.

Another potential application is in time-critical applications such as embedded model predictive control, where it is vital to have robust guarantees that the desired error bounds will be achieved in the allotted time without overflow errors and in spite of fixed-point arithmetic. See and references therein.

### A special case

As previously noted, exponential stability certificates are often conservative when they are derived from $L_{2}$ gain bounds. However, it is well known that exponential stability can be proven directly in some special cases. To illustrate this fact, consider a discrete linear time-invariant (LTI) plant $G$ with state-space realization $(A,B,C,D)$. Suppose $G$ is connected in feedback with a passive nonlinearity $\Delta$. A sufficient condition for BIBO stability is that there exists a positive definite matrix $P \succ 0$ and a scalar $\lambda \geq 0$ satisfying the linear matrix inequality (LMI) If we define ${V{(x)}}{: =}{x^{\mathsf{T}}Px}$, then implies that $V$ decreases along trajectories: ${V{(x_{k + 1})}} \leq {V{(x_{k})}}$ for all $k$. BIBO stability then follows from positivity and boundedness of $V$. But observe that when holds, we may replace the right-hand side by $- {\varepsilonP}$ for some $\varepsilon > 0$ sufficiently small. We then conclude that ${V{(x_{k + 1})}} \leq {{({1 - \varepsilon})}V{(x_{k})}}$ for all $k$ and exponential stability follows. We can then maximize $\varepsilon$ subject to feasibility of to further improve the rate bound.

Unfortunately, the simple trick shown above does not work in the general IQC setting due to the different role played by $P$ in the associated LMI. The LMI used in IQC theory comes from the Kalman-Yakubovich-Popov (KYP) lemma and although it is structurally similar to, $P$ is not positive definite in general and $V$ may not decrease along trajectories.

Our key insight is that with a suitable modification to both the LMI *and* the IQC definition, we obtain a condition that can certify exponential stability.

The paper is organized as follows. We cover some related work in the remainder of the introduction, we explain our notation and some basic results in Section 2, we develop and present our main result in Section 3, and we discuss computational considerations in Section 4. Finally, we present an illustrative example demonstrating the usefulness of our result in Section 5, and we make some concluding remarks in Section 6.

### Related work

It is noted in that BIBO stability often implies exponential stability. In particular, we get exponential stability if the nonlinearity satisfies an additional *fading memory* property. The proof of this result is chiefly concerned with showing *existence* of an exponential decay rate. Although the proof constructs an exponential rate, the construction is based on the assumed $L_{2}$ gain of the linear map, and thus can be very conservative.

Other proofs of exponential stability have appeared in the literature for specific classes of nonlinearities. Some examples include, which treat sector-bounded nonlinearities, and, which treats nonlinearities satisfying a Popov IQC. These works exploit LMI modifications akin to the one shown with earlier in this section.

The sequel is inspired by the recent paper, which presents an approach for proving the robust exponential stability of optimization algorithms. The approach of uses a time-domain formulation of IQCs modified to handle exponential stability. In contrast, the present work develops the aforementioned exponential stability modification entirely in the frequency domain and clarifies its connection to the seminal IQC results .

## Notation and preliminaries

We adopt a setup analogous to the one used , with the exception that we will work in discrete time rather than continuous time. The conjugate transpose of a vector $v \in {\mathbb{C}}^{n}$ is denoted $v^{\ast}$. The unit circle in the complex plane is denoted ${\mathbb{T}}{: =}\left\{ {z \in {\mathbb{C}}} \middle| {{|z|} = 1} \right\}$ The $z$-transform of a time-domain signal $x{: =}{(x_{0},x_{1},\ldots)}$ is denoted $\hat{x}{(z)}$ and defined as ${\hat{x}{(z)}}{: =}{\sum_{k = 0}^{\infty}{x_{k}z^{- k}}}$.

A Hermitian positive definite (semidefinite) matrix $M$ is denoted $M \succ 0$ ($M \succeq 0$). Function composition is denoted ${{({g \circ f})}{(x)}}:={g{({f{(x)}})}}$. A sequence $u = {(u_{0},u_{1},\ldots)}$ is said to be in $\ell_{2}$ if ${\sum_{k = 0}^{\infty}{|u_{k}|}^{2}} < \infty$. A sequence $u_{k}$ is said to be in $\ell_{2}^{\rho}$ for some $\rho \in {}$ if the sequence $({\rho^{- k}u_{k}})$ is in $\ell_{2}$, i.e. ${\sum_{k = 0}^{\infty}{\rho^{- {2k}}{|u_{k}|}^{2}}} < \infty$. Note that $\ell_{2}^{\rho} \subset \ell_{2}$. Let $\mathcal{R}\mathcal{H}_{\infty}^{m \times n}$ be the set of $m \times n$ matrices whose elements are proper rational functions with real coefficients analytic on the closed unit disk.

Consider the standard setup of Fig. 1. The block $G$ contains the known LTI part of the system while $\Delta$ contains the part that is uncertain, unknown, nonlinear, or otherwise troublesome.

Figure 1: Linear time-invariant system G in feedback with a nonlinearity Δ.

The interconnection is said to be *well-posed* if the map ${(v,w)}\mapsto{(e,f)}$ has a causal inverse. The interconnection is said to be BIBO stable if, in addition, there exists some $\gamma > 0$ such that when $G$ is initialized with zero state, for all square-summable inputs $f$ and $e$, and where $\parallel \cdot \parallel$ denotes the $\ell_{2}$ norm. Finally, the interconnection is *exponentially stable* if there exists some $\rho \in {}$ and $c > 0$ such that if $f = 0$ and $e = 0$, the state $x_{k}$ of $G$ will decay exponentially with rate $\rho$. That is, We now present the classical IQC definition and stability result, which will be modified in the sequel to guarantee exponential convergence. These results are the discrete-time analog of the main IQC results of Megretski and Rantzer.

### Definition 1 (IQC)

Signals $y \in \ell_{2}$ and $u \in \ell_{2}$ with associated $z$-transforms $\hat{y}{(z)}$ and $\hat{u}{(z)}$ satisfy the *IQC* defined by a Hermitian complex-valued function $\Pi$ if A bounded operator $\Delta$ satisfies the IQC defined by $\Pi$ if (2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) holds for all $y \in \ell_{2}$ with $u = {\Delta{(y)}}$. We also define ${IQC}{({\Pi{(z)}})}$ to be the set of all $\Delta$ that satisfy the IQC defined by $\Pi$.

### Theorem 2 (Stability result)

Let ${G{(z)}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ and let $\Delta$ be a bounded causal operator. Suppose that: for every $\tau \in {\lbrack 0,1\rbrack}$, the interconnection of $G$ and $\tau\Delta$ is well-posed. for every $\tau \in {\lbrack 0,1\rbrack}$, we have ${\tau\Delta} \in {{IQC}{({\Pi{(z)}})}}$. there exists $\varepsilon > 0$ such that Then, the feedback interconnection of $G$ and $\Delta$ is stable.

## Frequency-domain condition

In this section, we augment Definition 1. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") and the classical result of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") to derive a frequency-domain condition that certifies exponential stability.

### Definition 3

The operators $\rho_{+},\rho_{-}$ are defined as the time-domain, time-dependent multipliers $\rho^{k},\rho^{- k}$, respectively, where $\rho \in {}$ is a defined constant.

### Remark 4

The operator $\rho_{-} \circ {({{G{(z)}} \circ \rho_{+}})}$ is equivalent to the operator $G{({\rhoz})}$. This follows from the fact that, for any constant $a > 0$ and signal $u_{k}$, the $z$-transform of $a^{- k}u_{k}$ is given by $\hat{u}{({az})}$. See Fig. 2 for an illustration.

Figure 2: Illustration of Remark 4.

In order to show exponential stability of the system in Fig. 1, we will relate it to BIBO stability of the modified system shown in Fig. 3. This equivalence is closely related to the theory of stability multipliers.

Figure 3: Modified feedback diagram with additional multipliers and inputs. For appropriately chosen e and f and with zero initial condition, we show how this diagram is equivalent to that of Fig. 1.

### Proposition 5

Suppose $G{(z)}$ has a minimal realization $(A,B,C,D)$. If the interconnection in Fig. 3 is stable with zero initial condition, then the interconnection in Fig. 1 with initial state $x_{0}$ is exponentially stable.

Proof. Intuitively, if $v$ and $w$ are *small* in the BIBO sense compared to $e$ and $f$, then $y$ must be even smaller. A complete proof is included in the appendix.

Ideally, we would like to find a suitable redefinition of the IQC for this transformed system shown in Fig. 3. To this end, we introduce the concept of the *$\rho$-IQC*.

### Definition 6 ($\rho$-IQC)

Signals $y \in \ell_{2}^{\rho}$ and $u \in \ell_{2}^{\rho}$ with associated $z$-transforms $\hat{y}{(z)}$ and $\hat{u}{(z)}$ satisfy the *$\rho$-IQC* defined by a Hermitian complex-valued function $\Pi$ if A bounded operator $\Delta$ satisfies the $\rho$-IQC defined by $\Pi$ if (3. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) holds for all $y \in \ell_{2}^{\rho}$ with $u = {\Delta{(y)}}$. We also define ${IQC}{({\Pi{(z)}},\rho)}$ to be the set of all $\Delta$ that satisfy the $\rho$-IQC defined by $\Pi$.

Note that the concept of a $\rho$-IQC generalizes that of a regular IQC. Indeed, we have ${{IQC}{({\Pi{(z)}},1)}} = {{IQC}{({\Pi{(z)}})}}$. The restriction of $u \in \ell_{2}^{\rho}$ and $y \in \ell_{2}^{\rho}$ corresponds to the restriction of $u \in \ell_{2}$ and $y \in \ell_{2}$ in the classical definition of IQC. Now equipped with $\rho$-IQCs, we can relate $\Delta'$ in Fig. 3 to $\Delta$ in Fig. 1.

### Proposition 7

Let $\Delta$ be a nonlinearity, and let $\Pi$ be a Hermitian complex-valued function. As in Fig. 3, define $\Delta'{: =}{\rho_{-} \circ {({\Delta \circ \rho_{+}})}}$. Then the following statements are equivalent. $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ $\Delta' \in {{IQC}{({\Pi{({\rhoz})}})}}$ Proof. We define the discrete Fourier transform of the input and output of $\Delta$ as $\hat{y}{(z)}$ and $\hat{u}{(z)}$, respectively. Then, from the definition of $\rho_{+}$ and $\rho_{-}$, we have that ${\hat{w}{(z)}} = {\hat{u}{({\rhoz})}}$ and ${\hat{v}{(z)}} = {\hat{y}{({\rhoz})}}$. Substituting into the IQC definition (2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")), we obtain (3. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) as required.

Proposition 7 is illustrated in Fig. 4.

Figure 4: Illustration of Proposition 7.

We now state our main result, an exponential stability theorem analogous to the classical result in Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints").

### Theorem 8 (Exponential stability)

Fix $\rho \in {}$. Let ${G{({\rhoz})}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ and let $\Delta$ be a bounded causal operator. Suppose that: for every $\tau \in {\lbrack 0,1\rbrack}$, the interconnection of $G$ and $\tau\Delta$ is well-posed. for every $\tau \in {\lbrack 0,1\rbrack}$, we have ${\tau\Delta} \in {{IQC}{({\Pi{(z)}},\rho)}}$. there exists $\varepsilon > 0$ such that Then, the interconnection of $G$ and $\Delta$ shown in Fig. 1 is exponentially stable with rate $\rho$.

Proof. Roughly, we apply Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") to the interconnection in Fig. 3 with operators $G'$ and $\Delta'$ and IQC $\Pi{({\rhoz})}$.

Since Fig. 1 and Fig. 3 have the same interconnection structure, well-posedness is equivalent.

Due to the equivalence of IQCs in Proposition 7, This is condition iii) of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") using $G'$ and $\Delta'$.

Thus, these three conditions ensure BIBO stability of the system in Fig. 3. We then apply Proposition 5 to arrive at exponential stability of Fig. 1.

## Computation

As in the classical IQC setting, to guarantee stability, the frequency-domain inequality (FDI) (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) must be verified for every $\omega \in {\lbrack 0,{2\pi})}$. However, if the IQC in question exhibits a *factorizaton*, then the discrete-time KYP Lemma can be applied to convert the infinite-dimensional FDI to a finite-dimensional LMI. We now review these results.

### Definition 9

We say $\Pi$ has a *factorization* $(\Psi,M)$ if where $\Psi$ is a stable linear time-invariant system, $M$ is a constant Hermitian matrix, and $\Psi{(z)}^{\ast}$ denotes the conjugate transpose of $\Psi{(z)}$.

### Remark 10

If $\Pi{(z)}$ has a factorization $(\Psi,M)$ and $\Psi{({\rhoz})}$ is stable, then (3. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) is equivalent to This follows immediately from Parseval's theorem.

The KYP lemma, stated below, is attributed to Kalman, Yakubovich, and Popov. A simple proof and further references can be found .

### Lemma 11 (Discrete-time KYP Lemma)

Given matrices $A,B$ and a Hermitian matrix $M$, and assuming $A$ has no eigenvalues on the unit circle, the FDI holds for all $z \in {\mathbb{T}}$ if and only if there exists a solution $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ to the LMI

### Corollary 12

Suppose the realization of $G$ is given by $(A,B,C,D)$ and assume $\Pi$ has a factorization $(\Psi,M)$, where the realization of $\Psi$ is given by Then (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) is equivalent to the existence of $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that where $(\hat{A},\hat{B},\hat{C},\hat{D})$ are given by Proof. A similar result is proven, which we repeat here for completeness. where $\star$ denotes the repeated part of the quadratic form. Similarly, we have If $\rho^{- 1}\hat{A}$ has no eigenvalues on the unit circle, we may then invoke Lemma 11. ‣ 4 Computation ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") (applied to $\rho^{- 1}\hat{A}$, $\rho^{- 1}\hat{B}$, and the appropriate $M$ term) and multiply through by $\rho^{2}$ to show that (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) is equivalent to the existence of $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that holds, as required.

With the advent of fast interior-point methods to solve LMIs, the feasibility of the LMI can be quickly ascertained for any fixed $\rho^{2}$. Since the size of the LMI is on the order of the size of the system $G$ and the IQC $\Pi$, most practical linear systems lead to relatively small LMIs.

Finding the best upper bound amounts to minimizing $\rho^{2}$ subject to being feasible. This type of problem occurs frequently in robust control and is known as a *generalized eigenvalue optimization problem* (GEVP). The GEVP is not an LMI because is not jointly linear in $\rho^{2}$ and $P$. One simple approach to solving the GEVP is to perform a bisection search on $\rho^{2}$, but there are more sophisticated methods available; see for example.

### Remark 13

These results may also be carried through in continuous time. In that case, an equation analogous to (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) must be satisfied for $G{({s - \lambda})}$ for all $\omega \in {\lbrack 0,\infty)}$, and can be verified by finding $P = P^{\mathsf{T}}$, $\lambda \geq 0$ such that

## Examples

In this section, we show some classes of nonlinearities that can be described by $\rho$-IQCs and therefore used in Theorem 8. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") to prove robust exponential stability of an interconnected system. In the case where $\rho = 1$, these $\rho$-IQCs reduce to standard IQCs. This class of IQCs will be constructed for SISO systems, but they may be adapted for square MIMO systems where the nonlinearity is of the form ${diag}{({\{\Delta\}})}$ for a scalar $\Delta$, with little modification.

### Pointwise IQCs

A nonlinearity $\Delta$ satisfies a pointwise IQC with a factorization $(\Psi,M)$ if ${z_{k}^{\mathsf{T}}Mz_{k}} \geq 0$ for each $k$. In other words, the IQC holds pointwise in time. In this case, $\Delta$ also satisfies the associated $\rho$-IQC for all $\rho \leq 1$. Examples of pointwise IQCs include the $\gamma$ *norm-bounded IQC* and the *$\lbrack\alpha,\beta\rbrack$ sector bounded IQC*, given by Note that the norm-bounded IQC is a special case of the sector IQC with the sector $\lbrack{- \gamma},\gamma\rbrack$. These IQCs hold even if $\Delta$ is time-varying.

### Zames-Falb IQCs

A nonlinearity $\Delta$ is *slope-restricted on $\lbrack\alpha,\beta\rbrack$* where $0 \leq \alpha \leq \beta$ if the following relation holds for all $x$, $y$.

This relation states that the chord joining input-output pairs of $\Delta$ has a slope that is bounded between $\alpha$ and $\beta$. This class of functions satisfies the so-called Zames-Falb family of IQCs. We give the definition below.

### Proposition 14

A nonlinearity $\Delta$ that is static and slope-restricted on $\lbrack\alpha,\beta\rbrack$ satisfies the Zames-Falb IQC where $H{(z)}$ is any proper transfer function with impulse response $h{: =}{(h_{0},h_{1},\ldots)}$ that satisfies ${\| h\|}_{1} \leq 1$ and $h_{k} \geq 0$ for all $k$.

Proof. See for example.

### Remark 15

The Zames-Falb IQC admits the factorization In general, for a given fixed $\rho$, only a subset of the Zames-Falb IQCs will be $\rho$-IQCs. We now give a characterization of this subset.

### Theorem 16 (Zames-Falb $\rho$-IQC)

Suppose $\Delta$ is static and slope-restricted on $\lbrack\alpha,\beta\rbrack$. Then $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ where $\Pi$ is the Zames-Falb IQC and $H$ satisfies the additional constraint Proof. The proof involves rewriting the IQC as a discrete-time sum which can be split into parts that can separately be shown to be nonnegative. See the Appendix for the full proof.

### Multiple IQCs

Much like how multiple IQCs can give more precise $L_{2}$ gain bounds, multiple $\rho$-IQCs can give more precise convergence rates. We present numerical examples with both pointwise and dynamic $\rho$-IQCs. Consider a stable discrete-time LTI system $G{(z)}$ in feedback with the sigmoidal nonlinearity ${\Delta{(x)}} = {b{\arctan{(x)}}}$. This interconnection is shown in Fig. 5.

Figure 5: LTI system G in feedback with the static nonlinearity Δ (x) = b arctan (x).

Since this nonlinearity is static, in the $\lbrack 0,b\rbrack$ sector, and $\lbrack 0,b\rbrack$ slope-restricted, it satisfies the following $\rho$-IQCs where we can choose any $k = {1,2,\ldots}$.

### A tight bound

For our first example, we analyzed the following LTI system^11^1This example was inspired by the continuous time example given , which showed that adding more IQCs yields better $L_{2}$ gain bounds.

We solved the feasibility LMI using MATLAB together with the CVX package to find the fastest guaranteed rate of convergence. We searched over positive linear combinations of subsets of the IQCs --. Fig. 6 shows the rate bounds achieved as a function of which IQCs were used. For the particular choice $b = 1$, Fig. 7 shows sample state trajectories.

The true exponential rate can be found by linearizing the system about its equilibrium point. Namely, ${\Delta{(x)}} \approx {bx}$. Formally, this is an application of Lyapunov's indirect method \[10, Thm. 4.13\]. The result is that the decay rate should correspond to the maximal pole magnitude of the closed-loop map ${G{(z)}}/{({1 - {bG{(z)}}})}$. We display the true exponential rate as the dashed black curve in Fig. 6 and Fig. 7.

For this example, the $\rho$-IQC approach yields a tight upper bound to the true exponential rate when we use a combination of the sector and off-by-1 IQCs.

Figure 6: Upper bounds on the exponential convergence rate ρ for the system G1 (z) given in in feedback as in Fig. 5. A tight bound is achieved using two ρ-IQCs.

Figure 7: State decay over time of the system G1 (z) in feedback as in Fig. 5 with b = 1 for various initial conditions x0 ∈ [−15, 15]. The dashed black line is ρk, where ρ =.7058 is the true rate at b = 1 in Fig. 6.

### A loose bound

The $\rho$-IQC approach does not always achieve tight bounds as in the previous example. Consider the same problem as before but this time using The rate bounds for various $\rho$-IQCs are shown in Fig. 8. This time, we again observe that using more IQCs achieves better rate bounds, but the bound is not tight even after using six IQCs.

Figure 8: Upper bounds on the exponential convergence rate ρ for the system G2 (z) given in in feedback as in Fig. 5. As we include more ρ-IQCs, we can certify tighter bounds.

## Conclusion

We presented a modification of IQC theory that allows the certification of exponential rates. Although we only gave the $\rho$-IQC specialization for pointwise and Zames-Falb IQCs, the concept can in principle be extended to other IQCs such as, for example, uncertain time delays or slowly varying systems. As the dictionary of $\rho$-IQCs is further populated, the applicability of the technique outlined herein would be correspondingly expanded.
