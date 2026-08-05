<!-- arxiv-full-text:v1 {"arxiv_id": "1706.01337", "source": "ar5iv"} -->

## Introduction

Analysis in the context of robust control is generally concerned with obtaining absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, the structured singular value $\mu$, and integral quadratic constraints (IQCs).

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

Even when BIBO stable systems are exponentially stable, estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates. Another potential application is in time-critical systems. In embedded model predictive control, for example, it is vital to have robust guarantees that desired error bounds will be met in the allotted time without overflow errors and in spite of fixed-point arithmetic. See and references therein.

### A special case

While a general treatment of exponential bounds is provided in the sequel, it is worth noting that exponential stability can be proven directly for some special cases. To illustrate this fact, consider a linear time-invariant (LTI) discrete-time plant $G$ with state-space realization $(A,B,C,D)$. Suppose $G$ is connected in feedback with a strictly-input passive nonlinearity $\Delta$. A sufficient condition for BIBO stability is that there exists a positive definite matrix $P \succ 0$ and a scalar $\lambda \geq 0$ satisfying the linear matrix inequality (LMI) This result is also related to the Positive Real Lemma (see and references therein). If we define ${V{(x)}}{: =}{x^{\mathsf{T}}Px}$, then implies that $V$ decreases along trajectories: ${V{(x_{k + 1})}} \leq {V{(x_{k})}}$ for all $k$. BIBO stability then follows from positivity and boundedness of $V$. Observe that when holds, we may replace the right-hand side by $- {\varepsilonP}$ for some sufficiently small $\varepsilon > 0$. We then conclude that ${V{(x_{k + 1})}} \leq {{({1 - \varepsilon})}V{(x_{k})}}$ for all $k$ and exponential stability follows. We may then maximize $\varepsilon$ subject to feasibility of to further improve the rate bound.

Unfortunately, the approach outlined above of including $- {\varepsilonP}$ fails in the general IQC setting due to the different role played by $P$ in the associated LMI. In IQC theory, the LMI comes from the Kalman-Yakubovich-Popov (KYP) lemma and although it is structurally similar to, $P$ is not positive definite in general and $V$ may not decrease along trajectories.

Our key insight is that by suitably modifying both the LMI *and* the IQC definition, we obtain a more broadly applicable condition for certifying exponential stability.

The paper is organized as follows. We cover some related work in the remainder of the introduction, we explain our notation and some basic results in Section 2, we develop and present our main result in Section 3, and we discuss computational considerations in Section 4. An explicit construction of the (conservative) rate guarantees implied by finite $L_{2}$ gain is given in Section 5. In Section 6 we provide a library of applicable IQCs. Finally, we present illustrative examples demonstrating the usefulness of our result in Section 7, and we make some concluding remarks in Section 8.

### Related work

It is noted in that BIBO stability often implies exponential stability. In particular, exponential stability follows if the nonlinearity satisfies an additional *fading memory* property. So under mild assumptions, the robust stability guarantee from IQC theory automatically implies exponential stability as well. The proof of this result uses the $L_{2}$ gain from the stability analysis to construct an exponential rate bound. We will see in Section 7 that bounds computed in this way can be very conservative.

Other proofs of exponential stability have appeared in the literature for specific classes of nonlinearities. Some examples include sector-bounded nonlinearities and nonlinearities satisfying a Popov IQC. These works exploit LMI modifications akin to the one shown with earlier in this section.

This work is inspired , which presents an approach for proving the robust exponential stability of optimization algorithms. The approach of uses a time-domain formulation of IQCs modified to handle exponential stability. In contrast, the present work develops the aforementioned exponential stability analysis entirely in the frequency domain and its applicability is not restricted to the analysis of iterative optimization algorithms. Moreover, we clarify the connection to the seminal IQC results . Parts of this work first appeared in the conference paper. Since then, an analogous continuous-time formulation with alternative techniques and motivations also appeared .

## Notation and preliminaries

We adopt a setup analogous to the one used , with the exception that we will work in discrete time rather than continuous time. The conjugate transpose of a vector $v \in {\mathbb{C}}^{n}$ is denoted $v^{\ast}$. The unit circle in the complex plane is denoted ${\mathbb{T}}{: =}\left\{ {z \in {\mathbb{C}}} \middle| {{|z|} = 1} \right\}$ The $z$-transform of a time-domain signal $x{: =}{(x_{0},x_{1},\ldots)}$ is denoted $\hat{x}{(z)}$ and defined as ${\hat{x}{(z)}}{: =}{\sum_{k = 0}^{\infty}{x_{k}z^{- k}}}$. The $i$-th coordinate of the vector $x$ is denoted $x^{(i)}$.

A Hermitian positive definite (semidefinite) matrix $M$ is denoted $M \succ 0$ ($M \succeq 0$). Function composition is denoted ${{({g \circ f})}{(x)}}:={g{({f{(x)}})}}$. A sequence $u = {(u_{0},u_{1},\ldots)}$ is said to be in $\ell_{2}$ if ${\sum_{k = 0}^{\infty}{|u_{k}|}^{2}} < \infty$. A sequence $u_{k}$ is said to be in $\ell_{2}^{\rho}$ for some $\rho \in {}$ if the sequence $({\rho^{- k}u_{k}})$ is in $\ell_{2}$, i.e. ${\sum_{k = 0}^{\infty}{\rho^{- {2k}}{|u_{k}|}^{2}}} < \infty$. Note that $\ell_{2}^{\rho} \subset \ell_{2}$. Let $\mathcal{R}\mathcal{H}_{\infty}^{m \times n}$ be the set of $m \times n$ matrices whose elements are proper rational functions with real coefficients analytic outside the closed unit disk.

Consider the standard setup of Fig. 1 (the *Lur'e system*). The block $G$ contains the known LTI part of the system while $\Delta$ contains the part that is uncertain, unknown, nonlinear, or otherwise troublesome.

Figure 1: Linear time-invariant system G in feedback with a nonlinearity Δ.

The interconnection is said to be *well-posed* if the map ${(v,w)}\mapsto{(e,f)}$ has a causal inverse. The interconnection is said to be bounded-input bounded-output (BIBO) stable if, in addition, there exists some $\gamma > 0$ such that when $G$ is initialized with zero state, for all square-summable inputs $f$ and $e$, and where $\parallel \cdot \parallel$ denotes the $\ell_{2}$ norm. Finally, the interconnection is *exponentially stable* if there exists some $\rho \in {}$ and $c > 0$ such that if $f = 0$ and $e = 0$, the state $x_{k}$ of $G$ will decay exponentially with rate $\rho$. That is, We now present the classical IQC definition and stability result, which will be modified in the sequel to guarantee exponential convergence. These results are discrete-time analogs of the main IQC results of Megretski and Rantzer.

### Definition 1 (IQC)

Signals $y \in \ell_{2}$ and $u \in \ell_{2}$ with associated $z$-transforms $\hat{y}{(z)}$ and $\hat{u}{(z)}$ satisfy the *IQC* defined by a Hermitian complex-valued function $\Pi$ if A bounded causal operator $\Delta$ satisfies the IQC defined by $\Pi$ if (2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) holds for all $y \in \ell_{2}$ with $u = {\Delta{(y)}}$. We also define ${IQC}{({\Pi{(z)}})}$ to be the set of all $\Delta$ that satisfy the IQC defined by $\Pi$.

### Theorem 2 (Stability result)

Let ${G{(z)}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ and let $\Delta$ be a bounded causal operator. Suppose that: for every $\tau \in {\lbrack 0,1\rbrack}$, the interconnection of $G$ and $\tau\Delta$ is well-posed. for every $\tau \in {\lbrack 0,1\rbrack}$, we have ${\tau\Delta} \in {{IQC}{({\Pi{(z)}})}}$. there exists $\varepsilon > 0$ such that Then, the feedback interconnection of $G$ and $\Delta$ is BIBO stable.

## Frequency-domain condition

In this section, we augment Definition 1. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") and the classical result of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") to derive a frequency-domain condition that certifies exponential stability.

### Definition 3

The operators $\rho_{+},\rho_{-}$ are defined as the time-domain, time-dependent multipliers $\rho^{k},\rho^{- k}$, respectively, where $\rho \in {}$ is a defined constant.

### Remark 4

The operator $\rho_{-} \circ {({{G{(z)}} \circ \rho_{+}})}$ is equivalent to the operator $G{({\rhoz})}$. This follows from the fact that, for any constant $a > 0$ and signal $u_{k}$, the $z$-transform of $a^{- k}u_{k}$ is given by $\hat{u}{({az})}$. See Fig. 2 for an illustration.

Figure 2: Illustration of Remark 4.

In order to show exponential stability of the system in Fig. 1, we will relate it to BIBO stability of the modified system shown in Fig. 3. This equivalence is closely related to the theory of stability multipliers.

Figure 3: Modified feedback diagram with additional multipliers and inputs. For appropriately chosen e and f and with zero initial condition, we show how this diagram is equivalent to that of Fig. 1.

### Proposition 5

Suppose $G{(z)}$ has a minimal realization $(A,B,C,D)$. If the interconnection in Fig. 3 is BIBO stable, then the interconnection in Fig. 1 with initial state $x_{0}$ is exponentially stable.

Proof. Intuitively, if $v$ and $w$ are *small* in the BIBO sense compared to $e$ and $f$, then $y$ must be even smaller. See Appendix A.1 for a detailed proof.

In an effort to define IQCs for the transformed system shown in Fig. 3, we introduce the concept of the *$\rho$-IQC*.

### Definition 6 ($\rho$-IQC)

Signals $y \in \ell_{2}^{\rho}$ and $u \in \ell_{2}^{\rho}$ with associated $z$-transforms $\hat{y}{(z)}$ and $\hat{u}{(z)}$ satisfy the *$\rho$-IQC* defined by a Hermitian complex-valued function $\Pi$ if A bounded causal operator $\Delta$ satisfies the $\rho$-IQC defined by $\Pi$ if (3. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) holds for all $y \in \ell_{2}^{\rho}$ with $u = {\Delta{(y)}}$. We also define ${IQC}{({\Pi{(z)}},\rho)}$ to be the set of all $\Delta$ that satisfy the $\rho$-IQC defined by $\Pi$.

Note that the concept of a $\rho$-IQC generalizes that of a regular IQC. Indeed, we have ${{IQC}{({\Pi{(z)}},1)}} = {{IQC}{({\Pi{(z)}})}}$. The restriction of $u \in \ell_{2}^{\rho}$ and $y \in \ell_{2}^{\rho}$ corresponds to the restriction of $u \in \ell_{2}$ and $y \in \ell_{2}$ in the classical definition of IQC. Now equipped with $\rho$-IQCs, we can relate $\Delta'$ in Fig. 3 to $\Delta$ in Fig. 1.

### Proposition 7

Let $\Delta$ be a bounded causal operator, and let $\Pi$ be a Hermitian complex-valued function. As in Fig. 3, define $\Delta'{: =}{\rho_{-} \circ {({\Delta \circ \rho_{+}})}}$. Then the following statements are equivalent. $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ $\Delta' \in {{IQC}{({\Pi{({\rhoz})}})}}$ Proof. We define the discrete Fourier transform of the input and output of $\Delta$ as $\hat{y}{(z)}$ and $\hat{u}{(z)}$, respectively. Then, from the definition of $\rho_{+}$ and $\rho_{-}$, we have that ${\hat{w}{(z)}} = {\hat{u}{({\rhoz})}}$ and ${\hat{v}{(z)}} = {\hat{y}{({\rhoz})}}$. Substituting into the IQC definition (2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints")), we obtain (3. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) as required.

Proposition 7 is illustrated in Fig. 4.

Figure 4: Illustration of Proposition 7.

We now state our main result, an exponential stability theorem analogous to the classical result in Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints").

### Theorem 8 (Exponential stability)

Fix $\rho \in {}$. Let ${G{({\rhoz})}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ and $\Delta$ be a bounded causal operator such that $\Delta':={\rho_{-} \circ {({\Delta \circ \rho_{+}})}}$ is also bounded and causal. Furthermore, suppose that: for every $\tau \in {\lbrack 0,1\rbrack}$, the interconnection of $G$ and $\tau\Delta$ is well-posed. for every $\tau \in {\lbrack 0,1\rbrack}$, we have ${\tau\Delta} \in {{IQC}{({\Pi{(z)}},\rho)}}$. there exists $\varepsilon > 0$ such that Then, the interconnection of $G$ and $\Delta$ shown in Fig. 1 is exponentially stable with rate $\rho$.

Proof. We apply Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") to the interconnection in Fig. 3 with operators $G{({\rhoz})}$ and $\Delta'$ and the IQC $\Pi{({\rhoz})}$.

Since Fig. 1 and Fig. 3 have the same interconnection structure, well-posedness is equivalent.

Due to the equivalence of IQCs in Proposition 7, This is condition iii) of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") using $G{({\rhoz})}$ and $\Delta'$.

Thus, these three conditions ensure BIBO stability of the system in Fig. 3. We then apply Proposition 5 to arrive at exponential stability of Fig. 1.

Note that the assumption ${G{({\rhoz})}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ restricts us to verifying rates that are no faster than the rate of convergence of the open-loop $G$, which corresponds to the largest (in magnitude) pole of $G{(z)}$. Assuming WLOG that ${\Delta{}} = 0$, this is clear as $\Delta \equiv 0$ (corresponding to open-loop $G$) satisfies any $\rho$-IQC.

## Computation

As in the classical IQC setting, to guarantee stability, the frequency-domain inequality (FDI) (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) must be verified for every $\omega \in {\lbrack 0,{2\pi})}$. However, if the IQC in question exhibits a particular factorization, then the discrete-time KYP Lemma can be applied to convert the infinite-dimensional FDI to a finite-dimensional LMI. We now review these results.

### Definition 9

We say $\Pi$ has a *factorization* $(\Psi,M)$ if where $\Psi$ is a stable linear time-invariant system, $M$ is a constant Hermitian matrix, and $\Psi{(z)}^{\ast}$ denotes the conjugate transpose of $\Psi{(z)}$.

### Remark 10

Definition 9 is similar to J-spectral factorization (see and references therein), except we require them to hold for arbitrary $z \in {\mathbb{C}}$. Spectral factorizations are commonly evaluated on the unit circle for discrete systems (c.f. the imaginary axis for continuous-time systems). In such cases, we have $z^{\ast} = z^{- 1}$ for all $z \in {\mathbb{T}}$ and $s^{\ast} = {- s}$ for all $s \in {j{\mathbb{R}}}$. For this reason, factorizations are conventionally written using the *para-Hermitian conjugate* defined as ${\Psi^{\sim}{(z)}}{: =}{\Psi^{\mathsf{T}}{(z^{- 1})}}$ (c.f. ${\Psi^{\sim}{(s)}}{: =}{\Psi^{\mathsf{T}}{({- s})}}$ for continuous time). Although these definitions are equivalent to $\Psi{(z)}^{\ast}$ (c.f. $\Psi{(s)}^{\ast}$) in general, we cannot use the para-Hermitian conjugate for our factorization because we require it to hold for all $z \in {\mathbb{C}}$.

### Remark 11

If $\Pi{(z)}$ has a factorization $(\Psi,M)$ and $\Psi{({\rhoz})}$ is stable, then by Parseval's Theorem, (3. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) is equivalent to The KYP lemma, stated below, is attributed to Kalman, Yakubovich, and Popov. A simple proof and further references can be found.

### Lemma 12 (Discrete-time KYP Lemma)

Suppose $A$, $B$, $M$ are given matrices where $M$ is Hermitian and $A$ has no eigenvalues on the unit circle. Then the following FDI: holds for all $z \in {\mathbb{T}}$ if and only if there exists a $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ satisfying the LMI

### Corollary 13

Suppose the realization of $G$ is given by $(A,B,C,D)$ and assume $\Pi$ has a factorization $(\Psi,M)$, where the realization of $\Psi$ is given by Then (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) is equivalent to the existence of $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that where $(\hat{A},\hat{B},\hat{C},\hat{D})$ are defined as Proof. A similar result is proven, which we repeat here for completeness. where $\star$ denotes the repeated part of the quadratic form surrounding $M$. Similarly, we have If $\rho^{- 1}\hat{A}$ has no eigenvalues on the unit circle, we may then invoke Lemma 12. ‣ 4 Computation ‣ Exponential Stability Analysis via Integral Quadratic Constraints") (applied to $\rho^{- 1}\hat{A}$, $\rho^{- 1}\hat{B}$, and the appropriate $M$ term) and multiply through by $\rho^{2}$ to show that (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) is equivalent to the existence of $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that holds, as required.

With the advent of fast interior-point methods to solve LMIs, the feasibility of the LMI can often be quickly ascertained for any fixed $\rho^{2}$. Since the size of the LMI is often on the order of the size of the system $G$ and the IQC $\Pi$, many practical linear systems lead to LMIs of relatively moderate size.

Finding the best upper bound amounts to minimizing $\rho^{2}$ subject to being feasible. This type of problem occurs frequently in robust control and is known as a *generalized eigenvalue optimization problem* (GEVP). The GEVP is not an LMI because is not jointly linear in $\rho^{2}$ and $P$. One simple approach to solving the GEVP is to perform a bisection search on $\rho^{2}$, but there are more sophisticated methods available; see for example.

### Remark 14

The results above may also be carried through in continuous time. In that case, an equation analogous to (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) must be satisfied for $G{({s - \lambda})}$ for all $\omega \in {\lbrack 0,\infty)}$, and can be verified by finding $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that An alternative continuous-time formulation is detailed.

Applying a bisection search on $\rho^{2}$ requires the $\rho$-IQC to obey a certain monotonicity property, which we now define.

### Definition 15 (Monotonicity)

We say an IQC $\Pi{(z)}$ satisfies the *monotonicity property* if for all $0 < \rho \leq \rho' < 1$, we have: All of the $\rho$-IQCs discussed herein satisfy the monotonicity property. If an IQC does not satisfy this property, then a grid search may be used instead of bisection.

## Exponential rates from gain bounds

In, IQC analysis is used to certify $L_{2}$ stability of interconnected systems. As noted : "for general classes of ordinary differential equations, exponential stability is equivalent to the input/output stability...".

While input/output stability often implies exponential stability, we will show through examples that exponential rates constructed from $\ell_{2}$ bounds can be very conservative. This fact justifies the use of a dedicated technique for certifying exponential rates rather than using an $\ell_{2}$ analysis.

We will need two results. First, a well-known generalization of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") that allows us to optimize the $\ell_{2}$ gains over any pair of signals. We'll consider the scenario of Fig. 5, which is slightly more general than the setup in Fig. 1.

Figure 5: Augmented LTI system G in feedback with a nonlinearity Δ.

We would like to show that the input $d$ and output $e$ satisfy some IQC of the form The following result appears for example in and a complete proof is given.

### Theorem 16

Let ${G{(z)}} \in {\mathcal{R}\mathcal{H}_{\infty}^{m \times n}}$ and let $\Delta$ be a bounded causal operator. Suppose $G$ is partitioned according to the dimensions of the input and output channels in Fig. 5. Suppose the interconnection of $G_{11}$ and $\Delta$ is well-posed and stable and $\Delta \in {{IQC}{({\Pi{(z)}})}}$. If there exists $\varepsilon > 0$ such that then for all $d \in \ell_{2}$ and $e \in \ell_{2}$, Equation is satisfied.

### Remark 17 (see )

In Theorem 16, if $\Pi_{p,22} \preceq 0$ and $(G_{11},\Delta)$ satisfies assumptions (i) and (ii) of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints"), then stability of the $(G_{11},\Delta)$ interconnection is automatic since the $$ block of the FDI provides the remaining requirement for stability in Theorem 16.

Next, we'll need a way to convert an $\ell_{2}$ gain into an exponential rate bound. The sequel is similar to \[19, Prop. 1\], but presented here with an explicit rate construction and adapted for discrete time systems.

### Lemma 18

Define the recursion with $x_{0} = 0$: where $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ satisfies ${\phi{}} = 0$. Suppose that there exists a constant $c > 0$ such that whenever $g \in \ell_{2}$, and $(g,x)$ is a valid trajectory of, then Then, we also have the bound Proof. We write ${(x,g)} \in \mathcal{S}$ to denote a valid trajectory of. Define the function $V:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ as follows: The first step is to bound this function. Note that because $x_{0} = 0$ and ${\phi{}} = 0$, we have $\xi = x_{1} = g_{0}$. An easy lower bound is found by specializing to $g_{1} = g_{2} = \cdots = 0$. An upper bound is found by using. The result is that Fix ${(\overline{g},\overline{x})} \in \mathcal{S}$ to be any feasible trajectory of. We may lower-bound $V{({\overline{x}}_{1})}$ by setting $g_{1} = {\overline{g}}_{1}$ and shifting the entire $x$ and $g$ vectors forward one timestep: where we made use of the bound in the final step. Rearranging, we obtain We may lower-bound $V{({\overline{x}}_{3})}$ by setting $g_{1} = {\overline{g}}_{2}$ and using a similar argument. Continuing in this fashion, It follows that for all $k$, we have Applying the bound one more time, we conclude that where we used in the last step that ${\overline{g}}_{0} = {\overline{x}}_{1}$. This completes the proof.

By combining Theorem 16 and Lemma 18, we can find exponential rate bounds for LTI systems in feedback with nonlinearities that satisfy IQCs. First, use the setup of Fig. 5 with $d = g$ and $e = x$. Then, the $\ell_{2}$ bound in is an IQC as, with Then, transform Fig. 1 into augmented form by setting Finally, the appropriate initial condition can be set by using $g = d = \begin{bmatrix} \end{bmatrix}^{\mathsf{T}}$. Applying Lemma 18 leads to a bound of the form ${\| x_{k + 1}\|}_{2}^{2} \leq {c\left({1 - \frac{1}{c}} \right)^{k}{\| x_{0}\|}_{2}^{2}}$. Or, put another way, an exponential rate of $\rho = \sqrt{1 - \frac{1}{c}}$.

The FDI of Theorem 16 can be transformed into an LMI in a manner similar to that described in Section 4. This LMI is linear in $P$ and $c$, so it can be efficiently solved to find the minimal $c$. This in turn allows us to find the smallest exponential rate $\rho$.

## IQC Library

In this section, we show some classes of nonlinearities that can be described by $\rho$-IQCs and therefore used in Theorem 8. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints") to prove robust exponential stability of an interconnected system. In the case where $\rho = 1$, these $\rho$-IQCs reduce to standard IQCs. This class of IQCs will be constructed for single-input single-output systems, but they may be adapted for square multi-input multi-output systems where the nonlinearity is of the form ${diag}{({\{\Delta_{i}\}})}$ for a scalar $\Delta$.

### Noisy Multiplication

As noted for continuous time , nonlinearities of the form ${\Delta{(y_{k})}} \equiv {\delta_{k}y_{k}}$ for some unknown and/or time-varying $\delta_{k}$ may satisfy $\rho$-IQCs. As $\Delta$ and $\rho_{\pm}$ commute, in the parlance of Prop. 7 we have that $\Delta = \Delta'$, so $\Delta \in {{IQC}{(\Pi,1)}}$ implies $\Delta \in {{IQC}{(\Pi,\rho)}}$. See for examples of IQCs for noisy multiplication.

### Uncertain Time Delay

The following is a discrete-time analog of the $\rho$-IQC first developed. Let $\Delta$ be the operator defined by for some unknown $\tau$ in $\lbrack 0,\tau_{0}\rbrack$, where $\tau_{0}$ is known. Now, observe that Thus, we may transform the system into one with a block diagonal nonlinearity ${diag}{\{\Delta,\rho^{- \tau}\}}$. We can then use existing IQCs for noisy multiplication and time delays, always using $\Pi{({\rhoz})}$ instead of $\Pi{(z)}$.

Alternatively, with any bounded Hermitian function ${X{({\rhoz})}} = {X{({\rhoz})}^{\ast}} \succeq 0$, we see that

### Pointwise IQCs

A nonlinearity $\Delta$ satisfies a pointwise IQC with a factorization $(\Psi,M)$ if ${z_{k}^{\mathsf{T}}Mz_{k}} \geq 0$ for each $k$. In other words, the IQC holds pointwise in time. In this case, $\Delta$ also satisfies the associated $\rho$-IQC for all $\rho < 1$. Examples of pointwise IQCs include the $\gamma$ *norm-bounded IQC* and the *$\lbrack\alpha,\beta\rbrack$ sector-bounded IQC*, given by which corresponds to nonlinearities $\Delta$ that satisfy Note that the norm-bounded IQC is a special case of the sector IQC with the sector $\lbrack{- \gamma},\gamma\rbrack$. These IQCs hold even if $\Delta$ is time-varying, if $\Delta$ satisfies the IQC at each $k$.

### Zames--Falb IQCs

A nonlinearity $\Delta$ is *slope-restricted on $\lbrack\alpha,\beta\rbrack$* where $0 \leq \alpha \leq \beta \leq \infty$ if the following relation holds for all $x$, $y$.

This relation states that the chord joining input-output pairs of $\Delta$ has a slope that is bounded between $\alpha$ and $\beta$. This class of functions satisfies the Zames--Falb family of IQCs. We give the definition below.

### Proposition 19

A nonlinearity $\Delta$ that is static and slope-restricted on $\lbrack\alpha,\beta\rbrack$^11^1The $\beta = \infty$ case for this and similar IQCs considers only the $\beta$ terms, i.e. $\Pi_{\lbrack\alpha,\infty\rbrack} = {\lim_{\beta\rightarrow\infty}{\beta^{- 1}\Pi}}$. satisfies the Zames--Falb IQC where $\hat{h}{(z)}$ is any proper transfer function with impulse response $h{: =}{(h_{0},h_{1},\ldots)}$ that satisfies ${\| h\|}_{1} \leq 1$ and $h_{k} \geq 0$ for all $k$. If $\Delta$ is odd (${\Delta{({- x})}} = {- {\Delta{(x)}}}$), then we may remove the constraint that $h_{k} \geq 0$ for all $k$.

Proof. See for example.

### Remark 20

The Zames--Falb IQC admits the factorization In general, for a given fixed $\rho$, only a subset of the Zames--Falb IQCs will be $\rho$-IQCs. We now give a characterization of this subset.

### Theorem 21 (Zames--Falb $\rho$-IQC)

Suppose $\Delta$ is static and slope-restricted on $\lbrack\alpha,\beta\rbrack$. Then $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ where $\Pi$ is the Zames--Falb IQC and $\hat{h}$ satisfies the additional constraint Proof. The proof involves rewriting the IQC as a discrete-time sum which can be split into parts that can separately be shown to be nonnegative. See Appendix A.2 for the full proof of Theorem 21. ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") and related extensions.

Sector-bounded and/or slope-restricted functions show up in various specialized contexts. We will derive $\rho$-IQCs for two such cases: stiction nonlinearities and quasi-monotone/quasi-odd nonlinearities.

### Stiction Nonlinearities

Stiction nonlinearities (shown in Fig. 6) satisfy Zames--Falb $\rho$-IQCs with additional constraints on the coefficients $h_{k}$.

Figure 6: Example stiction nonlinearity (taken .)

### Corollary 22 (Stiction $\rho$-IQC)

Suppose $\Delta$ is a stiction nonlinearity with slope $1/\varepsilon$ and overshoot $\delta$ as defined . Then $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ where $\Pi$ is the $\lbrack 0,{1/\varepsilon}\rbrack$ Zames--Falb IQC and $H$ satisfies the additional constraint

### Quasi-monotone and Quasi-odd Nonlinearities

Following the definition in (shown in Fig. 7), quasi-monotone and quasi-odd nonlinearities also satisfy Zames--Falb $\rho$-IQCs under additional constraints on the $h_{k}$.

Figure 7: Monotone and odd bounds for unknown nonlinearities (modified from ). The nonlinearity must lie within envelopes generated by multiplicative perturbations of a known monotone linearity ${\underset{¯}{n}}_{m}$ (perturbation between 1 and Rm ≥ 1) and a known monotone odd nonlinearity ${\underset{¯}{n}}_{o}$ (perturbation between 1 and Ro ≥ 1). In this example, the nonlinearities of interest lie in the darkest region, the intersection of both envelopes.

### Corollary 23 (Quasi-monotone/odd $\rho$-IQC)

Suppose $\Delta$ is static and is quasi-monotone or quasi-odd as defined. Then $\Delta \in {{IQC}{({\Pi{(z)}},\rho)}}$ where $\Pi$ is the Zames--Falb IQC and $H$ satisfies the additional constraint Given a fixed $\rho$, searching over (finite) $h_{k}$ when solving the feasibility LMI using this IQC is still a convex problem. To see this, observe that we can equivalently write this constraint on the $h_{k}$ (assuming $R_{m} \geq R_{o}$, the other case is similar) as However, the proof of Corollary 23. ‣ 6.4.2 Quasi-monotone and Quasi-odd Nonlinearities ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") will show that these general Zames--Falb $\rho$-IQCs can be written as a nonnegative linear combination off "off-by-$j$" $\rho$-IQCs. Thus, when solving it is sufficient to search over all nonnegative linear combinations of simpler $\rho$-IQCs atoms, rather than formulating the constraint on the $h_{k}$ explicity. Whether this is more efficient depends on the specific problem dimensions. The correct chain of implications for this constraint (and others) is as follows: Compared to the odd Zames--Falb IQC, a quasi-odd IQC as defined in Corollary 23. ‣ 6.4.2 Quasi-monotone and Quasi-odd Nonlinearities ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") gives *less information* about the nonlinearity $\phi$, i.e. we must provide a certificate of stability for every nonlinearity in a *larger class*.

Since ${R_{m},R_{o}} \geq 1$, the weights satisfy $\gamma_{k}^{- 1} \geq 1$, so there is *less freedom* in choosing the $h_{k}$.

This restriction in choosing $h_{k}$ leads to a *smaller* feasible set for the LMI. Thus, the upper bound we find for the convergence rate will be *larger*.

### Repeated Sector Nonlinearities

We say a real symmetric matrix $\Gamma$ is *$(\rho,H)$-diagonally dominant* if, for a symmetric matrix of nonnegative proper transfers functions $\hat{H}$ with impulse responses $H_{{ij},k}$, we have that $\Gamma_{ii} \geq 0$, $\Gamma_{ij} \leq 0$ (for $i \neq j$), $H_{{ij},k} \geq 0$, ${\sum_{k = 0}^{\infty}{\rho^{- {2k}}{|H_{{ij},k}|}}} \leq {1{\forall{(i,j)}}}$ and We call $\Gamma$ simply *diagonally dominant*^22^2Note that the conventional definition of "diagonally dominant" does not restrict the diagonal elements to be nonnegative. if the above holds with $H = 0$ and $\rho = 1$.

Now, let $\Delta$ be a repeated monotone scalar nonlinearity in some sector, i.e. ${\Delta{(y)}} = {{diag}{\{{\phi{(y_{i})}}\}}}$.

### Proposition 24

$\Delta$ satisfies the pointwise $\rho$-IQC for any symmetric diagonally dominant matrix $\Gamma$.

Proof. The proof is analogous to the proof of Theorem 1 in the Appendix of with $H = 0$.

### Theorem 25

Assume $\Gamma$ is $(\rho,H)$-diagonally dominant. Then, if $\phi$ is in the $\lbrack\alpha,\beta\rbrack$ sector, then ${\Delta{(y)}} = {{diag}{\{{\phi{(y_{i})}}\}}}$ satisfies the $\rho$-IQC Proof. The proof is similar in spirit to that of Theorem 21. ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") but more involved; see Appendix A.3.

### Remark 26

The repeated $\lbrack\alpha,\beta\rbrack$-sector nonlinearity $\rho$-IQC admits the factorization See Appendix A.4 for a note on how to search over general nonnegative combinations of $\rho$-IQCs of the form, which is not immediately apparent.

## Examples

### Using multiple IQCs

Using multiple IQCs can lead to a more refined $L_{2}$ gain bound. Likewise, using multiple $\rho$-IQCs can lead to refined exponential rates. In this section, we present numerical examples using both pointwise and dynamic $\rho$-IQCs.

Consider a stable discrete-time LTI system $G{(z)}$ in feedback with the sigmoidal nonlinearity ${\Delta{(x)}} = {b{\arctan{(x)}}}$. This interconnection is shown in Fig. 8.

Figure 8: LTI system G in feedback with the static sigmoidal nonlinearity Δ (x) = b arctan (x).

Since this nonlinearity is static, in the $\lbrack 0,b\rbrack$ sector, and $\lbrack 0,b\rbrack$ slope-restricted, it satisfies the following $\rho$-IQCs: where we may choose any $k \geq 1$.

### A simple bound

For our first case study, we analyzed the interconnection of Fig. 8 with the LTI system^33^3This example was inspired by the continuous-time example given , which showed that adding more IQCs yields better $L_{2}$ gain bounds.

We solved the feasibility LMI using MATLAB together with CVX to find the fastest guaranteed rate of convergence and we searched over positive linear combinations of subsets of the IQCs --. Fig. 9 shows the rate bounds achieved as a function of which IQCs were used. Fig. 10 shows sample state trajectories for the case $b = 1$.

The true exponential rate can be found by linearizing the system about its equilibrium point. Namely, ${\Delta{(x)}} \approx {bx}$. Formally, this is an application of Lyapunov's indirect method \[15, Thm. 4.13\]. The result is that the decay rate should correspond to the maximal pole magnitude of the closed-loop map ${G{(z)}}/{({1 - {bG{(z)}}})}$. We display the true exponential rate as the dashed black curve in Fig. 9 and Fig. 10.

For this example, the $\rho$-IQC approach yields a tight upper bound to the true exponential rate when we use a combination of the sector and off-by-1 IQCs. We also computed the exponential rate derived from $\ell_{2}$ gain as described in Section 5 (dotted line). The $\ell_{2}$ bound is very conservative despite being computed using all available IQCs.

Figure 9: Upper bounds on the exponential convergence rate ρ for the system G1 (z) given in in feedback as in Fig. 8. A tight bound is achieved using two ρ-IQCs. The bound derived from the ℓ2 gain is very conservative.

Figure 10: State decay over time of the system G1 (z) in feedback as in Fig. 8 with b = 1 for various initial conditions x0 ∈ [−15, 15]. The dashed black line is ρk, where ρ =.7058 is the true rate at b = 1 in Fig. 9.

### A more complex bound

The $\rho$-IQC approach does not always achieve tight bounds as in the previous example. Consider the same interconnection of Fig. 8 but this time using The rate bounds for various $\rho$-IQCs are shown in Fig. 11. This time, we again observe that using more IQCs achieves better rate bounds, but the bound is not tight even after using six IQCs. However, if we add the Zames--Falb IQCs corresponding to odd monotone nonlinearities, the rate improves to within a small tolerance of the true rate.

Figure 11: Upper bounds on the exponential convergence rate ρ for the system G2 (z) given in in feedback as in Fig. 8. As we include more ρ-IQCs, we can certify tighter bounds. Once again, the ℓ2-derived bound is more conservative.

As in the previous example, the best achievable rate derived from an $\ell_{2}$ gain bound as detailed in Section 5 is still very conservative when compared to the rates obtained by using the $\rho$-IQC approach.

### A quasi-odd nonlinearity

Consider the asymmetric nonlinearity in Fig. 12, shown with the associated monotone and odd bounds as defined . In this example, we have $R_{m} = 1$ and $R_{o} = 2$.

Figure 12: Plot of the monotone and quasi-odd asymmetric nonlinearity ϕ (x) = max {arctan (x), −1} with its associated bounds.

Thus, we may invoke Corollary 23. ‣ 6.4.2 Quasi-monotone and Quasi-odd Nonlinearities ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") and use the associated $\rho$-IQC. Using this system in feedback with the $G{(z)}$ from the second example, we see in Fig. 13 that the quasi-odd Zames--Falb IQCs yield better performance than the monotone Zames--Falb IQCs of the same order (which requires all filter coefficients $h_{k}$ to be positive).

Figure 13: Comparison of monotone Zames–Falb and quasi-odd (denoted with superscript q) Zames–Falb IQC rate certificates.

### Repeated nonlinearities

To illustrate the need for repeated nonlinearity IQCs, first instantiate some stable SISO system $G$ with realization $(A,B,C,D)$. Now, consider the "extended" 2-input 2-output system and connect this system in positive feedback with the block-diagonal nonlinearity $\Delta = {{diag}{\{\Delta_{1},\Delta_{2}\}}}$. If we constrain $\Delta_{1} = \Delta_{2}$, then the nonlinearities cancel each other out and the system is in open loop. The convergence rate of the state is therefore determined by the largest magnitude eigenvalue of $A$. However, if our IQC does not capture that the nonlinearity is repeated and instead only assumes each individual nonlinearity is (say) $\lbrack 0,b\rbrack$-slope restricted, then $G$ must essentially be robust to $b$-norm bounded nonlinearities in the feedback loop. This will result in a worse rate certificate or even none at all (if $G$ is made unstable by positive feedback).

Indeed, constructing $G_{\text{ext}}$ using our previous "tight bound" example with $b = 0.3$ leads to a rate certificate of $\approx 0.825$ using only the odd monotone IQC; replacing it with the repeated odd monotone nonlinearity IQC gives a certificate matching the true convergence rate, $0.5$.

## Conclusion

IQC theory is the most general tool available for certifying robust stability of systems in feedback with unknown, uncertain, or otherwise difficult nonlinearities. As stable systems are often exponentially stable, it is reasonable to want finer control over not only stability, but also exponential decay rate.

The generalization presented herein enables the certification of robust exponential stability with precise control over the decay rate. Moreover, the library of $\rho$-IQCs provided shows how this approach can be applied as broadly and efficiently as the classical IQC theory.
