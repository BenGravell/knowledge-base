<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Frequency Domain Identification

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study non-parametric frequency-domain system identification from a finite-sample perspective. We assume an open loop scenario where the excitation input is periodic and consider the Empirical Transfer Function Estimate (ETFE), where the goal is to estimate the frequency response at certain desired (evenly-spaced) frequencies, given input-output samples. We show that under sub-Gaussian colored noise (in time-domain) and stability assumptions, the ETFE estimates are concentrated around the true values. The error rate is of the order of O((d_u+sqrt{d_ud_y})sqrt{M/N_tot}), where N_tot is the total number of samples, M is the number of desired frequencies, and d_u, d_y are the dimensions of the input and output signals respectively. This rate remains valid for general irrational transfer functions and does not require a finite order state-space representation. By tuning M, we obtain a N_tot^(-1/3) finite-sample rate for learning the frequency response over all frequencies in the H_infinity norm. Our result draws upon an extension of the Hanson-Wright inequality to semi-infinite matrices.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the finite-sample behavior of ETFE in simulations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the identification of *unknown* linear, discrete-time, time-invariant systems of the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Frequency domain identification has been extensively studied. The estimation error guarantees (on its distribution) are typically asymptotic, e.g. see Central Limit Theorem in \[, Ch. 16\], and, thus, are valid when the number of samples grows to infinity. Here, we adopt a finite-sample point of view, motivated by advances in modern statistics and statistical learning theory. Asymptotic methods are sharp asymptotically but are often heuristically applied for finite samples. Finite-sample bounds, on the other hand, are valid for any number of samples, but suffer from looser bounding constants. Nonetheless, they can provide a more detailed qualitative characterization of the statistical difficulty of learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While finite-sample system identification has been studied before, most results are focused on time domain identification. Detailed related work and a tutorial on the subject can be found. Frequency domain and time domain identification have many similarities--ignoring initial conditions, transients, or leakage effects, the two domains are equivalent from a prediction error framework perspective. Still, working in one domain may offer some advantages over the other. For example, the frequency domain approach allows a unified treatment of discrete and continuous time systems, simplifies the analysis of systems with delays, and offers a more explicit way of designing the input excitation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite-sample guarantees for the ETFE. We provide finite sample guarantees for the well-established Empirical Transfer Function Estimate (ETFE), a non-parametric method for frequency domain identification, under open-loop periodic excitation. While the mean and variance of the ETFE have been characterized before, we provide guarantees on the distribution of the estimation error, the tail probabilities in particular. Under certain stability conditions, we prove that the estimation error decays with a rate of $\sqrt{M/N_{tot}}$, where $N_{tot}$ is the total number of samples. The parameter $M$ is the number of selected frequencies at which we estimate the frequency response; it controls the frequency resolution. The rate holds for general irrational transfer functions and does not require a finite order state-space representation, unlike prior non-asymptotic bounds.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Guarantees in the $\mathcal{H}_{\infty}$ norm. Based on our finite-sample bound, we tune the number of frequencies $M$ to provide guarantees for learning the frequency response across all frequencies. We provide a non-asymptotic rate of $N_{tot}^{- {1/3}}$ in the $\mathcal{H}_{\infty}$ norm of the estimation error, which reflects optimal rates for non-parametric learning of Lipschitz functions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extension of the Hanson-Wright inequality. To prove our main result we have to deal with quadratic forms of a (countably) infinite number of sub-Gaussian variables. To achieve this, we extend the celebrated Hanson-Wright inequality to semi-infinite matrices; that is, bounded operators mapping sequences to finite vector spaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our paper is related to non-parametric system identification, which includes works on both time and frequency domain. Using Gaussian Processes as, where the unknown frequency response follows a Gaussian prior, we can also obtain finite sample guarantees. Here, we follow a different approach and we do not consider Gaussian priors. Note that in this work we focus on qualitative data-independent bounds linking sample requirements to system theoretic properties. Data-dependent bounds, which are arguably more suitable for applications, have also been studied before.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider the input-output system. We make the following assumption about the noise process $v_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1 (Noise)", "weight": 1.0} -->

The noise process $v_{t}$ is filtered sub-Gaussian white noise, that is,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Noise)", "weight": 1.0} -->

The noise process $v_{t}$ is colored. It is used to model measurement noise as well as any stochastic disturbances acting on the dynamical system.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Noise)", "weight": 1.0} -->

We assume throughout that the input is bounded. This guarantees that any transient phenomena have a limited effect on the estimation problem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2 (Input Bound)", "weight": 1.0} -->

We start all identification experiments at time $t = 0$. Hence, the initial conditions are determined by all past signals $u_{- 1},u_{- 2},\ldots$ and ${e_{- 1},e_{- 2},\ldots},$, which are nonzero in general, and unknown. Note that our formulation allows general irrational transfer functions and does not assume a state-space representation of finite dimension.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Empirical Transfer Function Estimate", "weight": 1.0} -->

The goal of non-parametric frequency domain identification is to estimate the frequency response $G{(e^{j\omega})}$, given input-output data. We assume access to $d_{u}$ experiments of length $N$, that is, data $(u_{0}^{(i)},y_{0}^{(i)},\ldots,u_{N - 1}^{(i)},y_{N - 1}^{(i)})$, for $i = {1,\ldots,d_{u}}$. This brings the total number of samples to $N_{tot} \triangleq {d_{u}N}$. We assume that the trajectories are *statistically independent* and we leave the single trajectory case for future work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Empirical Transfer Function Estimate", "weight": 1.0} -->

We are interested in the performance of the ETFE, which we review here. Given any signal $z = {\{ z_{t}\}}_{t \in {\lbrack N\rbrack}}$, let

<!-- chunk {"id": "body-0018", "role": "body", "section": "Empirical Transfer Function Estimate", "weight": 1.0} -->

Then, an estimate of $G{(e^{j\omega})}$ at frequency $\omega_{k} = {{2\pi k}/N}$, for $k = {0,\ldots,{N - 1}}$, can be obtained using the *ETFE*

<!-- chunk {"id": "body-0019", "role": "body", "section": "Empirical Transfer Function Estimate", "weight": 1.0} -->

provided that $U_{k}$ is invertible; the estimate is undefined if not. Since the number of frequencies $N$ scales with the number of data, it is generally impossible to estimate the responses at all frequencies consistently (without assuming structure). Instead, we can learn the responses at a smaller frequency set. Given a frequency-resolution parameter $M < N$, we focus on estimating $G{(e^{j\omega})}$ at $\omega = {{2\pi\ell}/M}$, for $\ell \in {\lbrack M\rbrack}$. Based on the ETFE and under some additional Lipschitz assumptions on the frequency response, we can extend the estimation over all frequencies $\omega \in {\lbrack 0,{2\pi})}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Excitation Method", "weight": 1.0} -->

The estimation performance also depends on the excitation method. Since we only need to estimate the frequency responses at ${2\pi\ell}/M$, $\ell \in {\lbrack M\rbrack}$, it is sufficient to excite the system at only these frequencies. Assuming that $M$ divides $N$, the DFT $U_{k}$ of the input can be non-zero at only ${{2\pi k}/N} = {{2\pi\ell}/M}$ or $k = {{\ell N}/M}$. The latter condition is satisfied if and only if the excitation input is periodic with a period equal to $M$. Note that we also need invertibility of $U_{k}$ at $k = {{\ell N}/M}$. To achieve this, we assume the following.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 3 (Excitation)", "weight": 1.0} -->

Let the input signals be periodic with period $M$ such that $u_{t + M}^{(i)} = u_{t}^{(i)}$, for $t \geq 0$ and every experiment $i = {1,\ldots,d_{u}}$. Assume that $M$ divides $N$ with $N_{p} \triangleq {N/M}$. Consider *one period* of the input signals and let the respective $M$-point DFTs be

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3 (Excitation)", "weight": 1.0} -->

for $\ell \in {\lbrack M\rbrack}$, with respective stacked DFTs

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3 (Excitation)", "weight": 1.0} -->

Assume that for all $\ell \in {\lbrack M\rbrack}$ the stacked DFTs satisfy

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3 (Excitation)", "weight": 1.0} -->

By definition, for Assumptions. ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"),. ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") to be consistent, we need ${\sum_{\ell = 0}^{M - 1}\sigma_{u,\ell}^{2}} \leq {MD_{u}^{2}}$, where $D_{u}$ is the input upper bound of Assumption. ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification").

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3 (Excitation)", "weight": 1.0} -->

Such assumptions are standard when dealing with experiment design in frequency domain. For example, Assumption. ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") is satisfied by design (with uniform $\sigma_{u,\ell}^{2}$ across $\ell \in {{\lbrack M\rbrack} - {\{ 0\}}}$) when pseudorandom binary sequence (PRBS) signals are used and we excite one input at a time \[, Ch. 13\]. Another choice could be multisine signals, where the user simply designs the input to have sinusoids with non-zero amplitudes at the required frequencies. Another option is to design the input spectrum and generate the input by passing a white noise realization through the spectral factor.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Objective", "weight": 1.0} -->

We can now state our objective, which is providing finite-sample guarantees for estimating the frequency responses. We focus on $\epsilon - \delta$ probabilistic guarantees, where $\epsilon$ controls the estimation accuracy and $\delta$ controls the confidence. {mdframed}\[roundcorner=3pt, backgroundcolor=blue!6,innertopmargin=-2pt\]

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1 (Finite-Sample ETFE)", "weight": 1.0} -->

Fix a frequency resolution $M < N$ such that $M$ divides $N$ and denote their ratio by $N_{p} = {N/M}$. Consider $d_{u}$ independent input-ouput trajectories of length $N$ ${\{ u_{t}^{(i)},y_{t}^{(i)}\}}_{t \in {\lbrack N\rbrack}}$, for $i = {1,\ldots,d_{u}}$, generated by system with excitation inputs as in Assumption. ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"). Fix a failure probability $0 < \delta < 1$. Determine $\epsilon_{\ell} > 0$, $\ell \in {\lbrack M\rbrack}$ such that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1 (Finite-Sample ETFE)", "weight": 1.0} -->

Problem. ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") only focuses on the desired discretized frequency grid ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$. In Section, we also study uniform guarantees over all frequencies in the $\mathcal{H}_{\infty}$ norm.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1 (Finite-Sample ETFE)", "weight": 1.0} -->

To guarantee a well-defined estimation problem, we consider the following stability conditions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 4 (Strict Stability)", "weight": 1.0} -->

The input-output impulse response is strictly stable, that is,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 4 (Strict Stability)", "weight": 1.0} -->

The auto-correlation function of the noise $R_{t} \triangleq {{\mathbb{E}}v_{s}v_{s - t}^{\top}}$ is also strictly stable

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 4 (Strict Stability)", "weight": 1.0} -->

Strict stability guarantees that the derivative of the frequency response $\partial{{G{(e^{j\omega})}}/{\partial\omega}}$ is uniformly bounded over all frequencies. This, in turn, implies that the response $G{(e^{j\omega})}$ is Lipschitz. Strict stability also guarantees that the transient phenomena have a limited effect on the estimation procedure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Finite-sample guarantees for the ETFE", "weight": 1.0} -->

In this section, we focus on estimating the frequency response at ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$, that is, the selected frequencies. Following the convention of, we define the stacked DFTs of the noises and the noiseless outputs as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Finite-sample guarantees for the ETFE", "weight": 1.0} -->

Then, for every frequency $\omega_{k} = {{2\pi k}/N}$ we have

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The above relation fits the framework of non-parametric function estimation. However, there are some notable differences with standard formulations. First, we have the presence of the input $U_{k}$, which affects the signal-to-noise ratio (SNR) and is an additional degree of freedom. For example, if the input matrix is not invertible at some $k$, we do not get a well-defined sample of $G{(e^{j\omega_{k}})}$. Second, the noise $V_{k}$ is heteroscedastic since its variance depends on the frequency $k$. Moreover, the sequence ${V_{k},k} \in {\lbrack N\rbrack}$ is non-Gaussian and non-independent across frequencies for finite samples $N$ (only asymptotically as $N$ goes to infinity). Hence, the non-asymptotic techniques of \[, Ch. 13\] do not apply directly.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where the input matrix $U_{k}$ is invertible, and we only look at the frequencies $k = {\ell N_{p}}$, $\ell \in {\lbrack M\rbrack}$. Let ${\Phi_{v,N}{(k)}} \triangleq {{\mathbb{E}}V_{k}^{(i)}{(V_{k}^{(i)})}^{\ast}}$ be the aliased power spectrum of the process $v_{t}$ at frequency $k$, where due to independence, the experiment index $i$ does not affect the definition. Define the signal-to-noise ratio (SNR) at frequency ${k = {\ell N_{p}}},$ $\ell \in {\lbrack M\rbrack}$ as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where ${\|{\Phi_{v,N}{(k)}}\|}_{op}$ is interpreted as the matrix norm for fixed $k$. We obtain the following finite-sample guarantees.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deterministic transient", "weight": 1.0} -->

Even in the absence of any stochastic noise, the ETFE suffers from estimation errors due to transient phenomena (e.g. aliasing, leakage). Fortunately, the transient error $T_{k,N} = {{\overline{Y}}_{k} - {G{(e^{j\omega_{k}})}U_{k}}}$ decays uniformly to zero as the DFT horizon $N$ goes to infinity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Input energy", "weight": 1.0} -->

Next, we review a standard result for periodic inputs. The input $U_{k}$ at frequencies $k = {\ell N_{p}}$ is equal to $\sqrt{N_{p}}{\overset{\sim}{U}}_{\ell}$, where ${\overset{\sim}{U}}_{\ell}$ is the $M -$point DFT based on one period of the input signals ). As a result, $U_{k}^{- 1}$ is well-defined and vanishes to zero with $N_{p}^{- {1/2}}$. This phenomenon is a direct consequence of periodicity and the properties of DFT.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Noise concentration", "weight": 1.0} -->

Finally, we bound the noise term $V_{k}$ by showing that its norm concentrates around $\sqrt{{tr}{({\Phi_{v,N}{(k)}})}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Estimation over all frequencies", "weight": 1.0} -->

In the previous section, we derived finite-sample guarantees for estimating the frequency responses at fixed selected frequencies ${2\pi\ell}/M$, $\ell \in {\lbrack M\rbrack}$. Here, we derive guarantees for estimating the function $G{(e^{j\omega})}$ uniformly over all $\omega \in {\lbrack 0,{2\pi})}$ in the $\mathcal{H}_{\infty}$ norm. We consider a naive estimator where to compute $\hat{G}{(e^{j\omega})}$ we use the closest frequency $\hat{G}{(e^{{j2\pi\ell}/M})}$, for some $\ell \in {\lbrack M\rbrack}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Estimation over all frequencies", "weight": 1.0} -->

Let $\chi{(t)}$ be the indicator function of the half-open interval $\lbrack{- {1/2}},{1/2})$. Define the naive estimator

<!-- chunk {"id": "body-0043", "role": "body", "section": "Estimation over all frequencies", "weight": 1.0} -->

Due to strict stability, it follows that the frequency response is smooth with Lipschitz constant upper bounded by ${\| G\|}_{\star}$. This follows from the fact that

<!-- chunk {"id": "body-0044", "role": "body", "section": "Estimation over all frequencies", "weight": 1.0} -->

Hence, for any $\omega \in {\lbrack 0,{2\pi})}$, the error is bounded by

<!-- chunk {"id": "body-0045", "role": "body", "section": "Estimation over all frequencies", "weight": 1.0} -->

for some $\ell \in {\lbrack M\rbrack}$. The first term scales with $1/M$, while the latter scales with $\sqrt{M/N}$, excluding logarithmic terms. Balancing the two terms, we obtain the following guarantees.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Simulations", "weight": 1.0} -->

We study the performance of the ETFE and the naive estimator via a numerical example. Consider the system

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simulations", "weight": 1.0} -->

with noise filter ${H{(q)}} = {({1 - {0.2q^{- 1}}})}^{- 1}$. Let all past inputs be zero ${u_{t} = 0},{t < 0}$. We generate the excitation signal based on PRBS with an additional offset to excite the zero frequency. Note that PRBS maximal length signals require $M = {2^{d} - 1}$, for some $d \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Simulations", "weight": 1.0} -->

In the first simulation, we study the maximum error of the ETFE over the fixed grid ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$

<!-- chunk {"id": "body-0049", "role": "body", "section": "Simulations", "weight": 1.0} -->

which can be thought as the "discretized" $\mathcal{H}_{\infty}$ norm of the error. We keep $M$ fixed, $\sigma_{e}^{2} = 0.1$, and we vary the total number of samples $N_{tot} = N$. To visualize the results, we perform $100$ Monte Carlo iterations for every number of samples $N$ and we present the empirical mean along with one empirical standard deviation. As shown in Fig., the error decays with a rate of $N^{- {1/2}}$ validating Theorem. ‣ 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification").

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulations", "weight": 1.0} -->

In the second simulation, we study the maximum error of the naive estimator over all frequencies, that is, the "true" $\mathcal{H}_{\infty}$ norm of the error. For every number of samples $N$, we tune $d$ in $M = {2^{d} - 1}$ to be the optimal one (empirically), and we perform $100$ Monte Carlo simulations. As shown in Fig., the error decays with a rate of $N^{- {1/3}}$ reflecting the result of Theorem. ‣ 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We provide finite-sample guarantees for the ETFE over a selected frequency grid, in the case of open-loop periodic excitation and under strict stability assumptions. By tuning the frequency resolution and exploiting Lipschitz continuity, we also obtain estimation guarantees in the $\mathcal{H}_{\infty}$ norm. An interesting direction for future work is studying finite-sample non-parametric least squares in the frequency domain. This approach could lead to interesting connections between function class complexity and experiment design. Moreover, adding more structure, beyond Lipschitz continuity, will lead to faster rates. Other topics that are left for future work include the estimation of the noise statistics and extending the guarantees to different variations of the excitation method and the ETFE. Finally, extending minimax lower bounds to this setting is also open.
