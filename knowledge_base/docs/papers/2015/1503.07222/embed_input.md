<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Exponential Convergence Bounds Using Integral Quadratic Constraints

Topics include Stability analysis, Online algorithms, Exponential stability.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The theory of integral quadratic constraints (IQCs) allows verification of stability and gain-bound properties of systems containing nonlinear or uncertain elements. Gain bounds often imply exponential stability, but it can be challenging to compute useful numerical bounds on the exponential decay rate. In this work, we present a modification of the classical IQC results of Megretski and Rantzer that leads to a tractable computational procedure for finding exponential rate certificates.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In robust control problems, we seek absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, and integral quadratic constraints (IQCs).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even when BIBO stable systems are exponentially stable, the estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another potential application is in time-critical applications such as embedded model predictive control, where it is vital to have robust guarantees that the desired error bounds will be achieved in the allotted time without overflow errors and in spite of fixed-point arithmetic. See and references therein.

<!-- chunk {"id": "body-0008", "role": "body", "section": "A special case", "weight": 1.0} -->

As previously noted, exponential stability certificates are often conservative when they are derived from $L_{2}$ gain bounds. However, it is well known that exponential stability can be proven directly in some special cases. To illustrate this fact, consider a discrete linear time-invariant (LTI) plant $G$ with state-space realization $(A,B,C,D)$. Suppose $G$ is connected in feedback with a passive nonlinearity $\Delta$. A sufficient condition for BIBO stability is that there exists a positive definite matrix $P \succ 0$ and a scalar $\lambda \geq 0$ satisfying the linear matrix inequality (LMI)

<!-- chunk {"id": "body-0009", "role": "body", "section": "A special case", "weight": 1.0} -->

If we define ${V{(x)}}{: =}{x^{\mathsf{T}}Px}$, then implies that $V$ decreases along trajectories: ${V{(x_{k + 1})}} \leq {V{(x_{k})}}$ for all $k$. BIBO stability then follows from positivity and boundedness of $V$. But observe that when holds, we may replace the right-hand side by $- {\varepsilonP}$ for some $\varepsilon > 0$ sufficiently small. We then conclude that ${V{(x_{k + 1})}} \leq {{({1 - \varepsilon})}V{(x_{k})}}$ for all $k$ and exponential stability follows. We can then maximize $\varepsilon$ subject to feasibility of to further improve the rate bound.

<!-- chunk {"id": "body-0010", "role": "body", "section": "A special case", "weight": 1.0} -->

Unfortunately, the simple trick shown above does not work in the general IQC setting due to the different role played by $P$ in the associated LMI. The LMI used in IQC theory comes from the Kalman-Yakubovich-Popov (KYP) lemma and although it is structurally similar to, $P$ is not positive definite in general and $V$ may not decrease along trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "A special case", "weight": 1.0} -->

Our key insight is that with a suitable modification to both the LMI *and* the IQC definition, we obtain a condition that can certify exponential stability.

<!-- chunk {"id": "body-0012", "role": "body", "section": "A special case", "weight": 1.0} -->

The paper is organized as follows. We cover some related work in the remainder of the introduction, we explain our notation and some basic results in Section 2, we develop and present our main result in Section 3, and we discuss computational considerations in Section 4. Finally, we present an illustrative example demonstrating the usefulness of our result in Section 5, and we make some concluding remarks in Section 6.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Frequency-domain condition", "weight": 1.0} -->

In this section, we augment Definition 1. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") and the classical result of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") to derive a frequency-domain condition that certifies exponential stability.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The operator $\rho_{-} \circ {({{G{(z)}} \circ \rho_{+}})}$ is equivalent to the operator $G{({\rhoz})}$. This follows from the fact that, for any constant $a > 0$ and signal $u_{k}$, the $z$-transform of $a^{- k}u_{k}$ is given by $\hat{u}{({az})}$. See Fig. 2 for an illustration.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 4", "weight": 1.0} -->

In order to show exponential stability of the system in Fig. 1, we will relate it to BIBO stability of the modified system shown in Fig. 3. This equivalence is closely related to the theory of stability multipliers.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Computation", "weight": 1.0} -->

As in the classical IQC setting, to guarantee stability, the frequency-domain inequality (FDI) (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) must be verified for every $\omega \in {\lbrack 0,{2\pi})}$. However, if the IQC in question exhibits a *factorizaton*, then the discrete-time KYP Lemma can be applied to convert the infinite-dimensional FDI to a finite-dimensional LMI. We now review these results.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 10", "weight": 1.0} -->

If $\Pi{(z)}$ has a factorization $(\Psi,M)$ and $\Psi{({\rhoz})}$ is stable, then (3. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) is equivalent to

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 10", "weight": 1.0} -->

This follows immediately from Parseval's theorem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 10", "weight": 1.0} -->

The KYP lemma, stated below, is attributed to Kalman, Yakubovich, and Popov. A simple proof and further references can be found.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 13", "weight": 1.0} -->

These results may also be carried through in continuous time. In that case, an equation analogous to (4. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints")) must be satisfied for $G{({s - \lambda})}$ for all $\omega \in {\lbrack 0,\infty)}$, and can be verified by finding $P = P^{\mathsf{T}}$, $\lambda \geq 0$ such that

<!-- chunk {"id": "body-0021", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section, we show some classes of nonlinearities that can be described by $\rho$-IQCs and therefore used in Theorem 8. ‣ 3 Frequency-domain condition ‣ Exponential Convergence Bounds using Integral Quadratic Constraints") to prove robust exponential stability of an interconnected system. In the case where $\rho = 1$, these $\rho$-IQCs reduce to standard IQCs. This class of IQCs will be constructed for SISO systems, but they may be adapted for square MIMO systems where the nonlinearity is of the form ${diag}{({\{\Delta\}})}$ for a scalar $\Delta$, with little modification.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

A nonlinearity $\Delta$ satisfies a pointwise IQC with a factorization $(\Psi,M)$ if ${z_{k}^{\mathsf{T}}Mz_{k}} \geq 0$ for each $k$. In other words, the IQC holds pointwise in time. In this case, $\Delta$ also satisfies the associated $\rho$-IQC for all $\rho \leq 1$. Examples of pointwise IQCs include the $\gamma$ *norm-bounded IQC*

<!-- chunk {"id": "body-0023", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

and the *$\lbrack\alpha,\beta\rbrack$ sector bounded IQC*, given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

Note that the norm-bounded IQC is a special case of the sector IQC with the sector $\lbrack{- \gamma},\gamma\rbrack$. These IQCs hold even if $\Delta$ is time-varying.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Zames-Falb IQCs", "weight": 1.0} -->

A nonlinearity $\Delta$ is *slope-restricted on $\lbrack\alpha,\beta\rbrack$* where $0 \leq \alpha \leq \beta$ if the following relation holds for all $x$, $y$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Zames-Falb IQCs", "weight": 1.0} -->

This relation states that the chord joining input-output pairs of $\Delta$ has a slope that is bounded between $\alpha$ and $\beta$. This class of functions satisfies the so-called Zames-Falb family of IQCs. We give the definition below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 15", "weight": 1.0} -->

The Zames-Falb IQC admits the factorization

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 15", "weight": 1.0} -->

In general, for a given fixed $\rho$, only a subset of the Zames-Falb IQCs will be $\rho$-IQCs. We now give a characterization of this subset.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Multiple IQCs", "weight": 1.0} -->

Much like how multiple IQCs can give more precise $L_{2}$ gain bounds, multiple $\rho$-IQCs can give more precise convergence rates. We present numerical examples with both pointwise and dynamic $\rho$-IQCs. Consider a stable discrete-time LTI system $G{(z)}$ in feedback with the sigmoidal nonlinearity ${\Delta{(x)}} = {b{\arctan{(x)}}}$. This interconnection is shown in Fig. 5.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Multiple IQCs", "weight": 1.0} -->

Since this nonlinearity is static, in the $\lbrack 0,b\rbrack$ sector, and $\lbrack 0,b\rbrack$ slope-restricted, it satisfies the following $\rho$-IQCs

<!-- chunk {"id": "body-0031", "role": "body", "section": "Multiple IQCs", "weight": 1.0} -->

where we can choose any $k = {1,2,\ldots}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "A tight bound", "weight": 1.0} -->

For our first example, we analyzed the following LTI system^11^1This example was inspired by the continuous time example given, which showed that adding more IQCs yields better $L_{2}$ gain bounds.

<!-- chunk {"id": "body-0033", "role": "body", "section": "A tight bound", "weight": 1.0} -->

We solved the feasibility LMI using MATLAB together with the CVX package to find the fastest guaranteed rate of convergence. We searched over positive linear combinations of subsets of the IQCs --. Fig. 6 shows the rate bounds achieved as a function of which IQCs were used. For the particular choice $b = 1$, Fig. 7 shows sample state trajectories.

<!-- chunk {"id": "body-0034", "role": "body", "section": "A tight bound", "weight": 1.0} -->

The true exponential rate can be found by linearizing the system about its equilibrium point. Namely, ${\Delta{(x)}} \approx {bx}$. Formally, this is an application of Lyapunov's indirect method \[10, Thm. 4.13\]. The result is that the decay rate should correspond to the maximal pole magnitude of the closed-loop map ${G{(z)}}/{({1 - {bG{(z)}}})}$. We display the true exponential rate as the dashed black curve in Fig. 6 and Fig. 7.

<!-- chunk {"id": "body-0035", "role": "body", "section": "A tight bound", "weight": 1.0} -->

For this example, the $\rho$-IQC approach yields a tight upper bound to the true exponential rate when we use a combination of the sector and off-by-1 IQCs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "A loose bound", "weight": 1.0} -->

The $\rho$-IQC approach does not always achieve tight bounds as in the previous example. Consider the same problem as before but this time using

<!-- chunk {"id": "body-0037", "role": "body", "section": "A loose bound", "weight": 1.0} -->

The rate bounds for various $\rho$-IQCs are shown in Fig. 8. This time, we again observe that using more IQCs achieves better rate bounds, but the bound is not tight even after using six IQCs.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a modification of IQC theory that allows the certification of exponential rates. Although we only gave the $\rho$-IQC specialization for pointwise and Zames-Falb IQCs, the concept can in principle be extended to other IQCs such as, for example, uncertain time delays or slowly varying systems. As the dictionary of $\rho$-IQCs is further populated, the applicability of the technique outlined herein would be correspondingly expanded.
