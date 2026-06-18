<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite-Time Markov-Parameter Identification of LTI Systems Using Non-Causal FIR Models: A Unified Framework for Stable and Unstable Systems

Topics include System identification, Linear systems, Markov parameters, Finite-time analysis, Least squares.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives finite-time guarantees for identifying stable and unstable LTI systems from a single closed-loop trajectory using non-causal FIR representations. The method avoids requiring the stabilizing controller or a separate stable/unstable decomposition, making the result conceptually tidy for closed-loop identification.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a finite-time framework for identifying stable and unstable linear time-invariant (LTI) systems from a single closed-loop input-output trajectory. The method does not require knowledge of the stabilizing controller, an intermediate observer, or prior separation of the plant into stable and unstable components. The approach uses a non-causal finite impulse response (FIR) model obtained from a Laurent expansion of the transfer function. In this representation, stable dynamics are captured by causal Markov parameters, while unstable dynamics are captured by non-causal coefficients associated with reverse-time stable evolution. This avoids the growth of causal unstable Markov parameters. A key advantage is that the coefficients multiplying both the input and the process noise remain controlled by stable and reverse-time stable decay rates, rather than by growing forward-time unstable dynamics. To handle closed-loop data, we use the injected excitation as an instrumental variable, which removes the bias caused by correlation between the feedback input and the process noise.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Under explicit instrument-strength and closed-loop concentration conditions, we derive a non-asymptotic error bound for the estimated Laurent/FIR Markov parameters with the usual O(1/sqrt(N)) statistical rate, up to logarithmic factors and truncation terms. The bound captures the effects of process noise, measurement noise, FIR horizons, closed-loop state moments, and controller-dependent instrument conditioning. Numerical experiments support the finite-time analysis by showing the predicted Markov-parameter convergence rate and illustrating how controller-dependent instrument conditioning affects the sample complexity of closed-loop identification.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed a surge of interest in the machine learning community in data-driven approaches to control and system identification, particularly for learning unknown dynamical systems from data; Lee and Lamperski, 2020). Linear dynamical systems (LDS) underpin numerous real-world processes ranging from robotics and industrial automation to forecasting time-series data such as financial and climate patterns. Unlike classical approaches that provide only asymptotic convergence guarantees, many practical scenarios---such as large-scale power networks or robotic systems---require finite-time performance guarantees because collecting extensive data or multiple independent trajectories can be prohibitively costly. Consequently, recent attention has shifted towards non-asymptotic analysis, emphasizing the relationship between estimation accuracy and finite-sample complexity. While finite-time guarantees exist for stable systems with partial observability and for unstable systems with full observability, identifying partially observed and potentially unstable LTI systems from a single, finite-length trajectory remains a significant open challenge of profound importance for developing robust, real-world control applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern control systems predominantly operate in closed-loop configurations, making it impractical or unsafe to open the loop for system identification purposes ). This constraint is particularly critical for open-loop unstable systems, where safety considerations strictly prohibit disabling feedback control. Existing closed-loop identification methods with finite-time guarantees impose restrictive assumptions. Approaches like; Jones and Dahleh, 2022; Lale et al., 2021b; Hyuk Park, 2025) employ observers or predictor-based formulations but assume open-loop stability. Even methods that address unstable systems introduce alternative constraints: requires full observability of states, demands a known linear controller while focusing on output estimation rather than model recovery, and relies on a known linear feedback structure. Prior results such as can, in principle, be extended to unstable plants under a stabilizing controller, but this extension requires knowledge of the controller policy to decorrelate the closed-loop data---a requirement that the proposed approach eliminates.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Additionally, most prior works rely on autoregressive models with exogenous inputs (ARX or VARX); Jones and Dahleh, 2022; Lale et al., 2021b). These approaches impose notable constraints: they require prior knowledge of system order or stability characteristics, and exhibit unfavorable sample complexity that scales polynomially with system dimension and past horizon length.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior non-causal FIR approaches established the usefulness of Laurent representations for closed-loop identification of unstable systems. In contrast, our focus is a finite-sample IV analysis of the estimated Laurent/FIR Markov parameters from a single closed-loop trajectory without knowledge of the stabilizing controller.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fundamental difficulty with unstable systems in causal finite-sample identification analyses is that causal Markov parameters and the coefficients multiplying process noise can involve growing forward-time powers of the unstable dynamics. Motivated by earlier non-causal FIR and Laurent-series approaches, we use a two-sided Laurent/FIR representation in which the unstable component is described through reverse-time stable dynamics. The Laurent coefficients multiplying both the input and the process noise are therefore governed by stable and reverse-time stable decay rates, rather than by growing forward-time unstable dynamics. The resulting bounds remain controlled up to transient-amplification and realization-conditioning constants.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We summarize the main contributions below.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop non-causal FIR identification without controller knowledge. We develop a non-causal Laurent/FIR framework for estimating the Markov parameters of stable and unstable LTI systems from a single closed-loop trajectory. The learner uses the measured input and output together with the known injected excitation, but does not require full-state observations, knowledge of the stabilizing controller, an intermediate observer, or a prior stable and unstable decomposition of the plant. The injected excitation is used as an instrumental variable to remove the bias caused by closed-loop correlation between the feedback input and the process noise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite-sample guarantees with controlled unstable and process-noise terms. We prove finite-sample error bounds for the estimated Laurent/FIR Markov parameters, with an $\mathcal{O}{(N^{- {1/2}})}$ statistical rate up to logarithmic factors and truncation terms. The non-causal representation captures unstable dynamics through reverse-time stable coefficients, so the terms multiplying both the input and the process noise are controlled by stable and reverse-time stable decay rates rather than by growing forward-time unstable dynamics. The resulting bound separates the effects of process noise, measurement noise, truncation tails, and instrument conditioning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controller-dependent sample complexity and recursive implementation. The analysis makes explicit how the unknown stabilizing controller affects sample complexity through closed-loop state moments, empirical concentration of the feedback and instrument cross-covariance, and the strength of the injected excitation as an instrument. This shows that a controller may stabilize the plant while still producing weak instrument conditioning and requiring more samples. The proposed formulation also supports recursive updates of the non-causal FIR coefficients with a fixed $d$-sample delay; for closed-loop data, the recursive IV update uses the empirical cross-covariance between the input regressor and the instrument regressor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The feedback interconnection defined by and is well posed and mean-square stable. In particular,

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

and the initial state satisfies ${x{}} = 0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

By Assumption 2.1, the closed-loop state has uniformly bounded second moments. We denote this bound by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

Under Assumptions 2.3 and 2.4, $G$ can be uniquely decomposed as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

where $D\overset{\Delta}{=}{G{(\infty)}}$, $G_{s}$ is the strictly proper stable part, whose poles lie inside the open unit disk, and $G_{u}$ is the strictly proper unstable part, whose poles lie outside the closed unit disk.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

Equivalently, after a similarity transformation, the realization can be written as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

The key insight is that $G_{s}{(z)}$ admits a causal power series in $z^{- 1}$, while $G_{u}{(z)}$ admits a non-causal power series in $z$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

For $i \geq 1$, the positive-lag Markov parameters are

<!-- chunk {"id": "body-0022", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

so their norms decay geometrically with $i$ because ${\rho{(A_{s})}} < 1$. For the negative-lag coefficients, let $i = {- j}$ with $j \geq 1$. Then

<!-- chunk {"id": "body-0023", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

Thus the negative-lag coefficients decay geometrically with $j$ because ${\rho{(A_{u}^{- 1})}} < 1$. Hence, although $A_{u}$ is unstable in forward time, its contribution to the Laurent series is governed by the stable reverse-time dynamics $A_{u}^{- 1}$. This is why the non-causal FIR representation can approximate unstable dynamics using bounded, decaying coefficients.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

The Laurent expansion of the transfer function ${G_{y,w}{(z)}} = {C{({{zI} - A})}^{- 1}B_{w}}$ from the process noise $w$ to the output $y$ is

<!-- chunk {"id": "body-0025", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

As above, the negative-lag coefficients contain powers of $A_{u}^{- 1}$ rather than growing powers of $A_{u}$. Thus the process-noise coefficients are controlled by the reverse-time stable dynamics, up to realization-conditioning constants.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

Using and, the output can be written as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

The causal tail decays as $\rho{(A_{s})}^{r}$ with the lookback horizon $r$, and the non-causal tail decays as $\rho{(A_{u}^{- 1})}^{d}$ with the preview $d$. The regressor $\phi_{w,r,d}{(k)}$ is used only for the analysis of the process-noise contribution; the estimator does not require observing $w{(k)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Non-causal FIR representation via Laurent expansion", "weight": 1.0} -->

The representation reduces identification to estimating the finite block of Laurent coefficients $\theta_{r,d}$. If the input were generated independently of the process noise, ordinary least squares could be applied directly to. In closed loop, however, the input is generated from past outputs, and those outputs are affected by the process noise. Thus the regressor $\phi_{r,d}{(k)}$ can be correlated with the error terms. The next subsection introduces an instrumental-variable estimator that removes this closed-loop bias by using the injected excitation $c$ as an instrument.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The goal of this subsection is to construct an estimator for $\theta_{r,d}$ that remains valid when the data are collected under feedback. The key observation is that the known excitation $c$ is independent of the process and measurement noises, but it is still correlated with the measured input $u$ through the identity $u = {f + c}$. Therefore, $c$ can be used as an instrument for the input regressor. Recall from that

<!-- chunk {"id": "body-0030", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The feedback component $f{(k)}$ depends on past measured outputs and can therefore be correlated with process noise through the closed-loop dynamics. Consequently, ordinary least squares using the input regressor $\phi_{r,d}{(k)}$ can be biased. To remove this closed-loop bias, we use the injected excitation $c$ as an instrumental variable.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The feedback signal $f{(k)}$ is not an additional input observed separately from $u{(k)}$. It is a conceptual decomposition of the measured input into the unknown feedback action and the known injected excitation. This decomposition is used to analyze the population cross-covariance, while the estimator itself uses the observed signals $u$, $y$, and $c$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

For $\ell = {{N + r + d} - 1}$, define the data matrices

<!-- chunk {"id": "body-0033", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The IV estimator in normalizes by the empirical input and instrument cross-covariance $\Phi_{r,d,\ell}\Phi_{c,r,d,\ell}^{\top}$. Hence, the population counterpart of this matrix determines whether the instrument is informative enough to identify $\theta_{r,d}$. This motivates the following definition. Define the finite-horizon input and instrument cross-covariance

<!-- chunk {"id": "body-0034", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The first term comes from the direct excitation $c$ in $u = {f + c}$. The second term captures how past injected excitations propagate through the feedback loop and reappear in the feedback signal.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

We now inspect the block structure of $R_{uc}$. The following indexing simply maps a block position in the non-causal regressor to the corresponding time instant.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

Thus ${t_{1}{(k)}} = {k + d}$ corresponds to the first, most future, block of the regressor, while ${t_{\mu}{(k)}} = {k - r}$ corresponds to the last, most past, block. The $(i,j)$ block of $R_{uc}$ is

<!-- chunk {"id": "body-0037", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

The direct excitation term in $u = {f + c}$ contributes $\sigma_{c}^{2}I_{p}$ when $i = j$ and zero otherwise. The remaining term is

<!-- chunk {"id": "body-0038", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

Because the controller is strictly causal, $f{({t_{i}{(k)}})}$ depends only on outputs before time $t_{i}{(k)}$. Those outputs may depend on past values of $c$, but they cannot depend on $c{({t_{i}{(k)}})}$ or on future values of $c$. If $j \leq i$, then ${t_{j}{(k)}} \geq {t_{i}{(k)}}$, so $c{({t_{j}{(k)}})}$ is current or future relative to $f{({t_{i}{(k)}})}$. Therefore,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

When $j > i$, ${t_{j}{(k)}} < {t_{i}{(k)}}$, so $c{({t_{j}{(k)}})}$ is a past excitation and may influence $f{({t_{i}{(k)}})}$ through the closed-loop dynamics. Hence the feedback contribution can be nonzero only above the block diagonal.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

Consequently, $S_{fc}$ is block strictly upper triangular and

<!-- chunk {"id": "body-0041", "role": "body", "section": "Instrumental-variable estimation for closed-loop data", "weight": 1.0} -->

This triangular structure explains why strict causality is useful: the diagonal blocks of $R_{uc}$ are fixed by the injected excitation, while feedback affects only the upper-triangular off-diagonal blocks. The matrix is therefore invertible at every finite horizon, but its smallest singular value can still be small. This is why we impose a quantitative conditioning assumption below.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

The finite-horizon input and instrument cross-covariance is quantitatively well conditioned. Specifically,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

We also define the normalized instrument-strength parameter

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

The normalized parameter $\lambda_{IV}$ is used to express the statistical error in a scale-invariant way. In the IV error identity, the inverse cross-covariance contributes a factor proportional to $1/s_{IV}$, while products involving the instrument have scale $\sigma_{c}$. Therefore the relevant ratio is

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Small values of $\lambda_{IV}$ correspond to weak instruments and lead to larger estimation error.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Controller interpretations and instrument conditioning. The construction above only uses strict causality, the independence of the injected excitation from the noise sequences, and the conditioning of the finite-horizon cross-covariance $R_{uc}$. The following observations clarify how the same definitions specialize to nonlinear, linear, and open-loop settings.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Nonlinear controllers. For a general strictly causal nonlinear controller, no differentiability or impulse-response representation of $\mathcal{K}$ is assumed. The blocks of $\mathcal{U}$ are defined directly by the cross-covariances. Strict causality gives the triangular population structure because $f{(t)}$ cannot depend on $c{(t)}$ or on future values of $c$. The additional difficulty for nonlinear controllers is finite-sample concentration of the empirical feedback and instrument cross-covariance. This is handled explicitly in Assumption 3.1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Linear closed-loop interpretation. The definition of $f{(k)}$ in is the general definition used throughout the paper. The triangular argument above does not require a linear controller. It only uses strict causality and the independence of the injected excitation from the noise sequences.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

When the closed-loop map from the exogenous signals to the feedback action is linear and stable, the same feedback signal can be interpreted through impulse responses. In particular, its component driven by the injected excitation can be written as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

where $\mathcal{T}_{s}^{c}$ is the closed-loop impulse response from the injected excitation $c$ to the feedback action $f$. The remaining part of $f{(k)}$ is driven by the process and measurement noises. These noise-driven components do not contribute to ${\mathbb{E}}{\lbrack{f{(t)}c{(\tau)}^{\top}}\rbrack}$ because $w$, $v$, and $c$ are mutually independent. Therefore, in the linear case,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

This linear impulse-response interpretation is useful for understanding the off-diagonal blocks of $\mathcal{U}$, but it is not an additional assumption in the IV estimator or in the finite-sample analysis below.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

A conservative conditioning bound. In the linear interpretation above, define

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

This quantity measures the total closed-loop gain from the injected excitation $c$ to the feedback signal $f$. Since the strictly upper triangular blocks of $\mathcal{U}$ are generated by these lagged responses, one obtains the conservative bound

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

This condition is only sufficient. It is not required by the IV estimator or by the finite-sample analysis below. Large values of $\mathcal{T}_{\infty}$ should be interpreted as an indication that the instrument may be weakly conditioned, which increases the sample size needed for accurate estimation.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Open-loop stable case. If the system is open-loop stable and no feedback is used, then ${f{(k)}} = 0$ and ${u{(k)}} = {c{(k)}}$. Therefore,

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

In this case, the IV estimator reduces to ordinary least squares.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

As the number of data samples increases, constructing the full data matrices may be impractical. Recursive updates address this by incrementally updating the estimates and the corresponding inverse matrices. Because the non-causal regressor

<!-- chunk {"id": "body-0058", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

contains the future inputs ${u{({k + 1})}},\ldots,{u{({k + d})}}$, the update associated with the output sample $y{(k)}$ can be performed only after time $k + d$. Thus the implementation is online with a fixed delay of $d$ samples. When $d = 0$, it reduces to the usual causal online update.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

The vector $\varphi_{k}$ is the non-causal input regressor, while $z_{k}$ is the corresponding instrument regressor. For ordinary least squares, the standard RLS update rules apply directly to $\varphi_{k}$. For each admissible output index $k = {r,\ldots,{\ell - d}}$, define

<!-- chunk {"id": "body-0060", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

This recursion is memory efficient because it avoids explicitly storing the full regressor matrix. However, for closed-loop data, LS may still be biased because $\varphi_{k}$ can be correlated with the effective regression error.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

For closed-loop data, the recursive IV update is different from simply substituting $z_{k}$ for $\varphi_{k}$ in the LS gain. The batch IV estimate satisfies the normal equation

<!-- chunk {"id": "body-0062", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

Thus, the recursive implementation must update the empirical cross-covariance between the input regressor and the instrument regressor. Define

<!-- chunk {"id": "body-0063", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

Using the Sherman-Morrison formula, define

<!-- chunk {"id": "body-0064", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

Then the recursive IV update can be written as

<!-- chunk {"id": "body-0065", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

Unlike the LS recursion, $P_{k}^{IV}$ is the inverse of a generally non-symmetric cross-covariance matrix. Therefore, the recursion should be initialized with a regularized matrix, for example

<!-- chunk {"id": "body-0066", "role": "body", "section": "Recursive least squares and recursive IV implementation", "weight": 1.0} -->

must remain nonzero. This recursive IV implementation is the online counterpart of the batch estimator. The finite-sample analysis below is stated for the batch IV estimator.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

We now derive a finite-sample error bound for the IV estimator. The goal is to quantify how accurately the finite block of Laurent coefficients $\theta_{r,d}$ can be estimated from one closed-loop trajectory. The unknown controller affects this error through the closed-loop state moments, the concentration of the feedback and instrument cross-covariance, and the instrument-strength parameter $\lambda_{IV}$. The remaining terms in the bound capture the sample size, the FIR horizons, the process and measurement noise levels, and the stable and reverse-time unstable truncation tails.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

Under Assumption 2.1, the closed-loop state has bounded second moments. We use the stable and unstable components of the state-space decomposition and define

<!-- chunk {"id": "body-0069", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

Here $x_{s}{(k)}$ and $x_{u}{(k)}$ are the stable and unstable state components associated with the stable and unstable realization of $G$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

Why closed-loop stability enters. If an unstable plant is excited in open loop, the unstable state component can grow without bound. Then the non-causal truncation error $C_{u}A_{u}^{{- d} - 1}x_{u}{({k + d + 1})}$ may have uncontrolled variance. Closed-loop stabilization is therefore needed to keep the state moments bounded, while the non-causal representation makes the multiplier $A_{u}^{{- d} - 1}$ contractive as $d$ increases.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

The stable and reverse-time unstable truncation scales are

<!-- chunk {"id": "body-0072", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

where ${\Phi{(A)}}\overset{\Delta}{=}{\sup_{\tau \geq 0}\frac{\| A^{\tau}\|}{\rho{(A)}^{\tau/2}}}$ measures transient amplification. The quantities in decay geometrically with $r$ and $d$, up to transient-amplification and closed-loop covariance factors.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

For the process-noise and instrument product, define

<!-- chunk {"id": "body-0074", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

The four error scales used in the theorem are then

<!-- chunk {"id": "body-0075", "role": "body", "section": "Finite-Time Guarantees for Markov Parameter Estimation", "weight": 1.0} -->

The constants $c_{w},c_{v},c_{e,s},c_{e,u}$ are universal positive constants.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Here $S_{fc}$ is the population feedback and instrument cross-covariance defined. The matrices $\Psi_{e_{s},\ell}$ and $\Psi_{e_{u},\ell}$ are formed from the stable and reverse-time unstable truncation tails.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Interpretation of Assumption 3.1. Assumption 3.1 is a closed-loop concentration condition. It is used to control empirical cross-products involving the feedback component and the truncation tails. The first inequality requires the empirical feedback and instrument cross-covariance to concentrate around its population value. The second and third inequalities require the stable and reverse-time unstable truncation tails to have controlled empirical correlation with the instrument.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

For stable linear closed loops driven by Gaussian or sub-Gaussian signals, such concentration bounds can be verified using standard results for geometrically stable linear processes, possibly with different universal constants. Related finite-sample IV analyses for closed-loop state-space identification appear. For general nonlinear controllers, mean-square stability alone does not imply empirical concentration. In that case, Assumption 3.1 should be read as an explicit regularity condition on the closed-loop process.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section we consider numerical and real-world examples.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

Consider the seventh-order unstable transfer function

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

Consider also a corresponding state space realization ${(A,B,C,D)}.$ We stabilize the plant with an LQR law ($Q = I_{7}$, $R = 1$)and collect a single closed-loop trajectory: a Gaussian excitation ${c{(k)}} \sim {\mathcal{N}{(0,\sigma_{c}^{2})}}$ is added to the control input, so that ${u{(k)}} = {{- {Kx{(k)}}} + {c{(k)}}}$, and the measured output ${y{(k)}} = {{Cx{(k)}} + {Du{(k)}} + {v{(k)}}}$ is corrupted by zero-mean Gaussian measurement noise. The feedback gain $K$ is used only to generate the closed-loop data and is not used by the identification algorithm. The recorded signals are the measured input and output together with the injected excitation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

A seventh-order IIR model via IV: MATLAB's iv4 is used with ARX structure $n_{a} = n_{b} = 7$; the instruments are simulated outputs from an auxiliary ARX model estimated in a preliminary step.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

A seventh-order IIR model via PEM, representing predictor-based approaches; Jones and Dahleh, 2022; Lale et al., 2021b; Lee and Lamperski, 2020). MATLAB's pem is used with state-space model order $n = 7$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

Note that both IIR baselines are given the true system order $n = 7$, whereas the proposed IV-FIR approach only requires the chosen FIR horizons $r$ and $d$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Example 4.1", "weight": 1.0} -->

We then split ${\hat{\theta}}_{r,d,\ell}$ into causal and non-causal parts and apply the Ho-Kalman algorithm to recover separate stable and unstable realizations, that is, $({\hat{A}}_{s},{\hat{B}}_{s},{\hat{C}}_{s})$ and $({\hat{A}}_{u},{\hat{B}}_{u},{\hat{C}}_{u})$, respectively, which can be combined to reconstruct the transfer function ${\hat{G}{(z)}} = {{{\hat{G}}_{s}{(z)}} + {{\hat{G}}_{u}{(z)}}}$. Figure 2 compares the frequency response of the estimated transfer function $\hat{G}$ with the true transfer function $G$. The close agreement in both magnitude and phase supports the quality of the estimated Laurent/FIR Markov parameters.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Example 4.2", "weight": 1.0} -->

We next consider input-output data from a hair dryer system DaISy, where the input is the heater voltage and the output is the air temperature. This benchmark is useful because no stability information is provided to the estimator a priori. The purpose of this example is to illustrate that the non-causal FIR parameterization can be used without knowing in advance whether the underlying dynamics are stable or unstable.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Example 4.2", "weight": 1.0} -->

We estimate a non-causal FIR model with $r = d = 25$ using the recursive least-squares implementation described in Section 2.3. Since the regressor contains future inputs, the recursive update is available with a fixed $d$-sample delay. We compare the resulting RLS-FIR estimate with IV-IIR and PEM-IIR baselines. Figure 3 shows that the non-causal RLS-FIR estimator converges faster and reaches a lower steady-state prediction error than the IIR baselines.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Example 4.3", "weight": 1.0} -->

The DaISy CD-player arm benchmark is a $2 \times 2$ MIMO system with actuator force inputs and laser-based position outputs. The data were collected in closed loop. This example is used as a real-data illustration of the non-causal FIR parameterization in a MIMO setting, rather than as a direct validation of the finite-sample IV theorem.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Example 4.3", "weight": 1.0} -->

We estimate a non-causal FIR model with $r = d = 50$ using the recursive least-squares implementation of Section 2.3. Since the regressor contains future inputs, the recursive update is available with a fixed $d$-sample delay. Figure 5 shows the measured and predicted outputs, together with the estimated Laurent/FIR coefficients. The predicted outputs are obtained directly from the estimated non-causal FIR model.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Example 4.3", "weight": 1.0} -->

The left panel of Figure 5 shows strong agreement between the predicted and measured outputs. The estimated coefficients in the right panel contain significant values at both positive and negative lags. The positive-lag coefficients represent the causal stable component, while the negative-lag coefficients represent the non-causal component associated with reverse-time stable dynamics. Thus, although some standard preprocessing may suggest a stable model, the estimated Laurent/FIR coefficients indicate that a non-causal component is useful for explaining the closed-loop MIMO data. This supports the role of the proposed representation as a diagnostic and modeling tool for systems whose stability structure is not known a priori.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Example 4.4", "weight": 1.0} -->

In this example, we examine how the choice of stabilizing controller affects the sample complexity of closed-loop identification. As discussed in Section 2.2, the controller influences the IV estimator through the feedback and instrument cross-covariance. In the linear case, the quantity $\mathcal{T}_{\infty}$ provides a conservative measure of how strongly past injected excitations are recirculated through the feedback signal.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Example 4.4", "weight": 1.0} -->

Consider the third-order plant $A = {{diag}{(0.3,\, 1.5,\, 2.0)}}$, $B = {\lbrack 1\;\;1\;\;1\rbrack}^{\top}$, $C = {\lbrack 1\;\;1\;\;1\rbrack}$ with two unstable poles. We design eight stabilizing linear controllers: one LQR law and seven pole-placement designs. The closed-loop spectral radii range from $\rho_{cl} = 0.50$ to $\rho_{cl} = 0.96$, producing $\mathcal{T}_{\infty}$ values ranging from approximately $6$ to $1258$. For each controller, we run $80$ simulation trials at SNR$= 20$ using $r = d = 20$ and $N \in {\{ 50,\ldots,6400\}}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Example 4.4", "weight": 1.0} -->

The Markov parameters are estimated using the non-causal IV-FIR estimator with the injected excitation $c$ as the instrument.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Example 4.4", "weight": 1.0} -->

The barely stabilizing controller ($\mathcal{T}_{\infty} \approx 1258$) requires substantially more samples than the LQR design ($\mathcal{T}_{\infty} \approx 6$) to reach comparable accuracy. Since all controllers in this experiment are linear and strictly causal, the finite-horizon population cross-covariance $R_{uc}$ retains the triangular structure described in Section 2.2. Thus large $\mathcal{T}_{\infty}$ does not make the IV construction invalid; rather, it worsens the conditioning and therefore increases the sample complexity. This experiment highlights that controller design is an important degree of freedom in closed-loop identification: a controller may stabilize the plant while still leading to weak instrument conditioning and slower learning.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Example 4.5", "weight": 1.0} -->

Following the benchmark of, consider the SISO plant

<!-- chunk {"id": "body-0096", "role": "body", "section": "Example 4.5", "weight": 1.0} -->

This system is open-loop stable. Therefore, a purely causal FIR model would be sufficient if the stability information were known in advance. Here, however, we intentionally apply the full non-causal FIR parameterization with $r = d = 10$ to illustrate that the proposed representation does not require prior knowledge of the stability structure. In this stable case, the estimated negative-lag coefficients ${\hat{H}}_{- 1},\ldots,{\hat{H}}_{- d}$ are close to zero, so the non-causal model effectively reduces to a causal FIR model.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Example 4.5", "weight": 1.0} -->

Since this benchmark is open-loop stable and no feedback-induced correlation is present, the IV estimator reduces to ordinary least squares. We therefore report the LS implementation of the FIR estimator for this example. This experiment is intended to illustrate the computational simplicity and predictive accuracy of the FIR parameterization, rather than the closed-loop IV bias-removal effect.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Example 4.5", "weight": 1.0} -->

We compare the proposed FIR estimator with six deep generative state-space models that learn latent dynamics through variational inference and recurrent architectures: STORN, VAE-RNN, VRNN-Gauss, VRNN-Gauss-I, VRNN-GMM, and VRNN-GMM-I. Figure 7 shows the test-set RMSE versus the number of training samples $N$. The FIR estimator achieves the lowest RMSE with substantially fewer parameters and negligible training time compared with the deep state-space baselines, as reported in Table 1. This highlights the practical advantage of the proposed representation when a compact linear model is appropriate.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduced a non-causal FIR framework for finite-time identification of stable and unstable LTI systems from a single closed-loop trajectory. The Laurent/FIR representation captures unstable dynamics through reverse-time stable coefficients, which keeps the input and process-noise terms controlled by stable decay rates rather than by growing unstable dynamics. To address closed-loop bias, we used the injected excitation as an instrumental variable, without requiring knowledge of the stabilizing controller. Under explicit instrument-strength and closed-loop concentration conditions, we established an $\mathcal{O}{(N^{- {1/2}})}$ Markov-parameter error bound, up to logarithmic factors and truncation terms. The analysis also shows how the controller affects sample complexity through instrument conditioning, and the numerical results support the predicted finite-sample behavior.
