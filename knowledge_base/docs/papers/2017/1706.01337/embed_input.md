<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Exponential Stability Analysis via Integral Quadratic Constraints

Topics include Stability analysis, Online algorithms, Generalization, Exponential stability.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The theory of integral quadratic constraints (IQCs) allows verification of stability and gain-bound properties of systems containing nonlinear or uncertain elements. Gain bounds often imply exponential stability, but it can be challenging to compute useful numerical bounds on the exponential decay rate. This work presents a generalization of the classical IQC results of Megretski and Rantzer that leads to a tractable computational procedure for finding exponential rate certificates that are far less conservative than ones computed from L_2 gain bounds alone. An expanded library of IQCs for certifying exponential stability is also provided and the effectiveness of the technique is demonstrated via numerical examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Analysis in the context of robust control is generally concerned with obtaining absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, the structured singular value $\mu$, and integral quadratic constraints (IQCs).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even when BIBO stable systems are exponentially stable, estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates. Another potential application is in time-critical systems. In embedded model predictive control, for example, it is vital to have robust guarantees that desired error bounds will be met in the allotted time without overflow errors and in spite of fixed-point arithmetic. See and references therein.

<!-- chunk {"id": "body-0007", "role": "body", "section": "A special case", "weight": 1.0} -->

While a general treatment of exponential bounds is provided in the sequel, it is worth noting that exponential stability can be proven directly for some special cases. To illustrate this fact, consider a linear time-invariant (LTI) discrete-time plant $G$ with state-space realization $(A,B,C,D)$. Suppose $G$ is connected in feedback with a strictly-input passive nonlinearity $\Delta$. A sufficient condition for BIBO stability is that there exists a positive definite matrix $P \succ 0$ and a scalar $\lambda \geq 0$ satisfying the linear matrix inequality (LMI)

<!-- chunk {"id": "body-0008", "role": "body", "section": "A special case", "weight": 1.0} -->

This result is also related to the Positive Real Lemma (see and references therein). If we define ${V{(x)}}{: =}{x^{\mathsf{T}}Px}$, then implies that $V$ decreases along trajectories: ${V{(x_{k + 1})}} \leq {V{(x_{k})}}$ for all $k$. BIBO stability then follows from positivity and boundedness of $V$. Observe that when holds, we may replace the right-hand side by $- {\varepsilonP}$ for some sufficiently small $\varepsilon > 0$. We then conclude that ${V{(x_{k + 1})}} \leq {{({1 - \varepsilon})}V{(x_{k})}}$ for all $k$ and exponential stability follows. We may then maximize $\varepsilon$ subject to feasibility of to further improve the rate bound.

<!-- chunk {"id": "body-0009", "role": "body", "section": "A special case", "weight": 1.0} -->

Unfortunately, the approach outlined above of including $- {\varepsilonP}$ fails in the general IQC setting due to the different role played by $P$ in the associated LMI. In IQC theory, the LMI comes from the Kalman-Yakubovich-Popov (KYP) lemma and although it is structurally similar to, $P$ is not positive definite in general and $V$ may not decrease along trajectories.

<!-- chunk {"id": "body-0010", "role": "body", "section": "A special case", "weight": 1.0} -->

Our key insight is that by suitably modifying both the LMI *and* the IQC definition, we obtain a more broadly applicable condition for certifying exponential stability.

<!-- chunk {"id": "body-0011", "role": "body", "section": "A special case", "weight": 1.0} -->

The paper is organized as follows. We cover some related work in the remainder of the introduction, we explain our notation and some basic results in Section 2, we develop and present our main result in Section 3, and we discuss computational considerations in Section 4. An explicit construction of the (conservative) rate guarantees implied by finite $L_{2}$ gain is given in Section 5. In Section 6 we provide a library of applicable IQCs. Finally, we present illustrative examples demonstrating the usefulness of our result in Section 7, and we make some concluding remarks in Section 8.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Frequency-domain condition", "weight": 1.0} -->

In this section, we augment Definition 1. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") and the classical result of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") to derive a frequency-domain condition that certifies exponential stability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The operator $\rho_{-} \circ {({{G{(z)}} \circ \rho_{+}})}$ is equivalent to the operator $G{({\rhoz})}$. This follows from the fact that, for any constant $a > 0$ and signal $u_{k}$, the $z$-transform of $a^{- k}u_{k}$ is given by $\hat{u}{({az})}$. See Fig. 2 for an illustration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 4", "weight": 1.0} -->

In order to show exponential stability of the system in Fig. 1, we will relate it to BIBO stability of the modified system shown in Fig. 3. This equivalence is closely related to the theory of stability multipliers.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Computation", "weight": 1.0} -->

As in the classical IQC setting, to guarantee stability, the frequency-domain inequality (FDI) (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) must be verified for every $\omega \in {\lbrack 0,{2\pi})}$. However, if the IQC in question exhibits a particular factorization, then the discrete-time KYP Lemma can be applied to convert the infinite-dimensional FDI to a finite-dimensional LMI. We now review these results.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Definition 9 is similar to J-spectral factorization (see and references therein), except we require them to hold for arbitrary $z \in {\mathbb{C}}$. Spectral factorizations are commonly evaluated on the unit circle for discrete systems (c.f. the imaginary axis for continuous-time systems). In such cases, we have $z^{\ast} = z^{- 1}$ for all $z \in {\mathbb{T}}$ and $s^{\ast} = {- s}$ for all $s \in {j{\mathbb{R}}}$. For this reason, factorizations are conventionally written using the *para-Hermitian conjugate* defined as ${\Psi^{\sim}{(z)}}{: =}{\Psi^{\mathsf{T}}{(z^{- 1})}}$ (c.f.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 10", "weight": 1.0} -->

${\Psi^{\sim}{(s)}}{: =}{\Psi^{\mathsf{T}}{({- s})}}$ for continuous time). Although these definitions are equivalent to $\Psi{(z)}^{\ast}$ (c.f. $\Psi{(s)}^{\ast}$) in general, we cannot use the para-Hermitian conjugate for our factorization because we require it to hold for all $z \in {\mathbb{C}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 11", "weight": 1.0} -->

If $\Pi{(z)}$ has a factorization $(\Psi,M)$ and $\Psi{({\rhoz})}$ is stable, then by Parseval's Theorem, (3. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) is equivalent to

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 11", "weight": 1.0} -->

The KYP lemma, stated below, is attributed to Kalman, Yakubovich, and Popov. A simple proof and further references can be found.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 14", "weight": 1.0} -->

The results above may also be carried through in continuous time. In that case, an equation analogous to (4. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints")) must be satisfied for $G{({s - \lambda})}$ for all $\omega \in {\lbrack 0,\infty)}$, and can be verified by finding $P = P^{\mathsf{T}}$ and $\lambda \geq 0$ such that

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 14", "weight": 1.0} -->

Applying a bisection search on $\rho^{2}$ requires the $\rho$-IQC to obey a certain monotonicity property, which we now define.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Exponential rates from gain bounds", "weight": 1.0} -->

In, IQC analysis is used to certify $L_{2}$ stability of interconnected systems. As noted: "for general classes of ordinary differential equations, exponential stability is equivalent to the input/output stability...".

<!-- chunk {"id": "body-0023", "role": "body", "section": "Exponential rates from gain bounds", "weight": 1.0} -->

While input/output stability often implies exponential stability, we will show through examples that exponential rates constructed from $\ell_{2}$ bounds can be very conservative. This fact justifies the use of a dedicated technique for certifying exponential rates rather than using an $\ell_{2}$ analysis.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Exponential rates from gain bounds", "weight": 1.0} -->

We will need two results. First, a well-known generalization of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints") that allows us to optimize the $\ell_{2}$ gains over any pair of signals. We'll consider the scenario of Fig. 5, which is slightly more general than the setup in Fig. 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Exponential rates from gain bounds", "weight": 1.0} -->

We would like to show that the input $d$ and output $e$ satisfy some IQC of the form

<!-- chunk {"id": "body-0026", "role": "body", "section": "Exponential rates from gain bounds", "weight": 1.0} -->

The following result appears for example in and a complete proof is given.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 17 (see )", "weight": 1.0} -->

In Theorem 16, if $\Pi_{p,22} \preceq 0$ and $(G_{11},\Delta)$ satisfies assumptions (i) and (ii) of Theorem 2. ‣ 2 Notation and preliminaries ‣ Exponential Stability Analysis via Integral Quadratic Constraints"), then stability of the $(G_{11},\Delta)$ interconnection is automatic since the $$ block of the FDI provides the remaining requirement for stability in Theorem 16.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 17 (see )", "weight": 1.0} -->

Next, we'll need a way to convert an $\ell_{2}$ gain into an exponential rate bound. The sequel is similar to \[19, Prop. 1\], but presented here with an explicit rate construction and adapted for discrete time systems.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IQC Library", "weight": 1.0} -->

In this section, we show some classes of nonlinearities that can be described by $\rho$-IQCs and therefore used in Theorem 8. ‣ 3 Frequency-domain condition ‣ Exponential Stability Analysis via Integral Quadratic Constraints") to prove robust exponential stability of an interconnected system. In the case where $\rho = 1$, these $\rho$-IQCs reduce to standard IQCs. This class of IQCs will be constructed for single-input single-output systems, but they may be adapted for square multi-input multi-output systems where the nonlinearity is of the form ${diag}{({\{\Delta_{i}\}})}$ for a scalar $\Delta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Noisy Multiplication", "weight": 1.0} -->

As noted for continuous time, nonlinearities of the form ${\Delta{(y_{k})}} \equiv {\delta_{k}y_{k}}$ for some unknown and/or time-varying $\delta_{k}$ may satisfy $\rho$-IQCs. As $\Delta$ and $\rho_{\pm}$ commute, in the parlance of Prop. 7 we have that $\Delta = \Delta^{\prime}$, so $\Delta \in {{IQC}{(\Pi,1)}}$ implies $\Delta \in {{IQC}{(\Pi,\rho)}}$. See for examples of IQCs for noisy multiplication.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Uncertain Time Delay", "weight": 1.0} -->

The following is a discrete-time analog of the $\rho$-IQC first developed. Let $\Delta$ be the operator defined by

<!-- chunk {"id": "body-0032", "role": "body", "section": "Uncertain Time Delay", "weight": 1.0} -->

for some unknown $\tau$ in $\lbrack 0,\tau_{0}\rbrack$, where $\tau_{0}$ is known. Now, observe that

<!-- chunk {"id": "body-0033", "role": "body", "section": "Uncertain Time Delay", "weight": 1.0} -->

Thus, we may transform the system into one with a block diagonal nonlinearity ${diag}{\{\Delta,\rho^{- \tau}\}}$. We can then use existing IQCs for noisy multiplication and time delays, always using $\Pi{({\rhoz})}$ instead of $\Pi{(z)}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Uncertain Time Delay", "weight": 1.0} -->

Alternatively, with any bounded Hermitian function ${X{({\rhoz})}} = {X{({\rhoz})}^{\ast}} \succeq 0$, we see that

<!-- chunk {"id": "body-0035", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

A nonlinearity $\Delta$ satisfies a pointwise IQC with a factorization $(\Psi,M)$ if ${z_{k}^{\mathsf{T}}Mz_{k}} \geq 0$ for each $k$. In other words, the IQC holds pointwise in time. In this case, $\Delta$ also satisfies the associated $\rho$-IQC for all $\rho < 1$. Examples of pointwise IQCs include the $\gamma$ *norm-bounded IQC*

<!-- chunk {"id": "body-0036", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

and the *$\lbrack\alpha,\beta\rbrack$ sector-bounded IQC*, given by

<!-- chunk {"id": "body-0037", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

which corresponds to nonlinearities $\Delta$ that satisfy

<!-- chunk {"id": "body-0038", "role": "body", "section": "Pointwise IQCs", "weight": 1.0} -->

Note that the norm-bounded IQC is a special case of the sector IQC with the sector $\lbrack{- \gamma},\gamma\rbrack$. These IQCs hold even if $\Delta$ is time-varying, if $\Delta$ satisfies the IQC at each $k$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Zames--Falb IQCs", "weight": 1.0} -->

A nonlinearity $\Delta$ is *slope-restricted on $\lbrack\alpha,\beta\rbrack$* where $0 \leq \alpha \leq \beta \leq \infty$ if the following relation holds for all $x$, $y$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Zames--Falb IQCs", "weight": 1.0} -->

This relation states that the chord joining input-output pairs of $\Delta$ has a slope that is bounded between $\alpha$ and $\beta$. This class of functions satisfies the Zames--Falb family of IQCs. We give the definition below.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 20", "weight": 1.0} -->

The Zames--Falb IQC admits the factorization

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 20", "weight": 1.0} -->

In general, for a given fixed $\rho$, only a subset of the Zames--Falb IQCs will be $\rho$-IQCs. We now give a characterization of this subset.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stiction Nonlinearities", "weight": 1.0} -->

Stiction nonlinearities (shown in Fig. 6) satisfy Zames--Falb $\rho$-IQCs with additional constraints on the coefficients $h_{k}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Quasi-monotone and Quasi-odd Nonlinearities", "weight": 1.0} -->

Following the definition in (shown in Fig. 7), quasi-monotone and quasi-odd nonlinearities also satisfy Zames--Falb $\rho$-IQCs under additional constraints on the $h_{k}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Repeated Sector Nonlinearities", "weight": 1.0} -->

We call $\Gamma$ simply *diagonally dominant*^22^2Note that the conventional definition of "diagonally dominant" does not restrict the diagonal elements to be nonnegative. if the above holds with $H = 0$ and $\rho = 1$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 26", "weight": 1.0} -->

The repeated $\lbrack\alpha,\beta\rbrack$-sector nonlinearity $\rho$-IQC admits the factorization

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 26", "weight": 1.0} -->

See Appendix A.4 for a note on how to search over general nonnegative combinations of $\rho$-IQCs of the form, which is not immediately apparent.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Using multiple IQCs", "weight": 1.0} -->

Using multiple IQCs can lead to a more refined $L_{2}$ gain bound. Likewise, using multiple $\rho$-IQCs can lead to refined exponential rates. In this section, we present numerical examples using both pointwise and dynamic $\rho$-IQCs.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Using multiple IQCs", "weight": 1.0} -->

Consider a stable discrete-time LTI system $G{(z)}$ in feedback with the sigmoidal nonlinearity ${\Delta{(x)}} = {b{\arctan{(x)}}}$. This interconnection is shown in Fig. 8.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Using multiple IQCs", "weight": 1.0} -->

where we may choose any $k \geq 1$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "A simple bound", "weight": 1.0} -->

For our first case study, we analyzed the interconnection of Fig. 8 with the LTI system^33^3This example was inspired by the continuous-time example given, which showed that adding more IQCs yields better $L_{2}$ gain bounds.

<!-- chunk {"id": "body-0052", "role": "body", "section": "A simple bound", "weight": 1.0} -->

We solved the feasibility LMI using MATLAB together with CVX to find the fastest guaranteed rate of convergence and we searched over positive linear combinations of subsets of the IQCs --. Fig. 9 shows the rate bounds achieved as a function of which IQCs were used. Fig. 10 shows sample state trajectories for the case $b = 1$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "A simple bound", "weight": 1.0} -->

The true exponential rate can be found by linearizing the system about its equilibrium point. Namely, ${\Delta{(x)}} \approx {bx}$. Formally, this is an application of Lyapunov's indirect method \[15, Thm. 4.13\]. The result is that the decay rate should correspond to the maximal pole magnitude of the closed-loop map ${G{(z)}}/{({1 - {bG{(z)}}})}$. We display the true exponential rate as the dashed black curve in Fig. 9 and Fig. 10.

<!-- chunk {"id": "body-0054", "role": "body", "section": "A simple bound", "weight": 1.0} -->

For this example, the $\rho$-IQC approach yields a tight upper bound to the true exponential rate when we use a combination of the sector and off-by-1 IQCs. We also computed the exponential rate derived from $\ell_{2}$ gain as described in Section 5 (dotted line). The $\ell_{2}$ bound is very conservative despite being computed using all available IQCs.

<!-- chunk {"id": "body-0055", "role": "body", "section": "A more complex bound", "weight": 1.0} -->

The $\rho$-IQC approach does not always achieve tight bounds as in the previous example. Consider the same interconnection of Fig. 8 but this time using

<!-- chunk {"id": "body-0056", "role": "body", "section": "A more complex bound", "weight": 1.0} -->

The rate bounds for various $\rho$-IQCs are shown in Fig. 11. This time, we again observe that using more IQCs achieves better rate bounds, but the bound is not tight even after using six IQCs. However, if we add the Zames--Falb IQCs corresponding to odd monotone nonlinearities, the rate improves to within a small tolerance of the true rate.

<!-- chunk {"id": "body-0057", "role": "body", "section": "A more complex bound", "weight": 1.0} -->

As in the previous example, the best achievable rate derived from an $\ell_{2}$ gain bound as detailed in Section 5 is still very conservative when compared to the rates obtained by using the $\rho$-IQC approach.

<!-- chunk {"id": "body-0058", "role": "body", "section": "A quasi-odd nonlinearity", "weight": 1.0} -->

Consider the asymmetric nonlinearity in Fig. 12, shown with the associated monotone and odd bounds as defined. In this example, we have $R_{m} = 1$ and $R_{o} = 2$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "A quasi-odd nonlinearity", "weight": 1.0} -->

Thus, we may invoke Corollary 23. ‣ 6.4.2 Quasi-monotone and Quasi-odd Nonlinearities ‣ 6.4 Zames–Falb IQCs ‣ 6 IQC Library ‣ Exponential Stability Analysis via Integral Quadratic Constraints") and use the associated $\rho$-IQC. Using this system in feedback with the $G{(z)}$ from the second example, we see in Fig. 13 that the quasi-odd Zames--Falb IQCs yield better performance than the monotone Zames--Falb IQCs of the same order (which requires all filter coefficients $h_{k}$ to be positive).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Repeated nonlinearities", "weight": 1.0} -->

To illustrate the need for repeated nonlinearity IQCs, first instantiate some stable SISO system $G$ with realization $(A,B,C,D)$. Now, consider the "extended" 2-input 2-output system

<!-- chunk {"id": "body-0061", "role": "body", "section": "Repeated nonlinearities", "weight": 1.0} -->

and connect this system in positive feedback with the block-diagonal nonlinearity $\Delta = {{diag}{\{\Delta_{1},\Delta_{2}\}}}$. If we constrain $\Delta_{1} = \Delta_{2}$, then the nonlinearities cancel each other out and the system is in open loop. The convergence rate of the state is therefore determined by the largest magnitude eigenvalue of $A$. However, if our IQC does not capture that the nonlinearity is repeated and instead only assumes each individual nonlinearity is (say) $\lbrack 0,b\rbrack$-slope restricted, then $G$ must essentially be robust to $b$-norm bounded nonlinearities in the feedback loop. This will result in a worse rate certificate or even none at all (if $G$ is made unstable by positive feedback).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Repeated nonlinearities", "weight": 1.0} -->

Indeed, constructing $G_{\text{ext}}$ using our previous "tight bound" example with $b = 0.3$ leads to a rate certificate of $\approx 0.825$ using only the odd monotone IQC; replacing it with the repeated odd monotone nonlinearity IQC gives a certificate matching the true convergence rate, $0.5$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

IQC theory is the most general tool available for certifying robust stability of systems in feedback with unknown, uncertain, or otherwise difficult nonlinearities. As stable systems are often exponentially stable, it is reasonable to want finer control over not only stability, but also exponential decay rate.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The generalization presented herein enables the certification of robust exponential stability with precise control over the decay rate. Moreover, the library of $\rho$-IQCs provided shows how this approach can be applied as broadly and efficiently as the classical IQC theory.
