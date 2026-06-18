## Introduction

We consider the identification of *unknown* linear, discrete-time, time-invariant systems of the form

where $t \in {\mathbb{Z}}$ is the time, $u_{t} \in {\mathbb{R}}^{d_{u}}$ is the input, $y_{t} \in {\mathbb{R}}^{d_{y}}$ is the output, ${q^{- s}u_{t}} = u_{t - s}$ is the backward shift operator, and $g_{t} \in {\mathbb{R}}^{d_{y} \times d_{u}}$ is the impulse response. The noiseless output ${\overline{y}}_{t}$ is perturbed by some random noise process $v_{t} \in {\mathbb{R}}^{d_{y}}$. We are interested in estimating the frequency response $G{(e^{j\omega})}$ from finite input-output data.

Frequency domain identification has been extensively studied \[(https://arxiv.org/html/2404.01100v2#bib.bib1), (https://arxiv.org/html/2404.01100v2#bib.bib2), (https://arxiv.org/html/2404.01100v2#bib.bib3)\]. The estimation error guarantees (on its distribution) are typically asymptotic, e.g. see Central Limit Theorem in \[(https://arxiv.org/html/2404.01100v2#bib.bib3), Ch. 16\], and, thus, are valid when the number of samples grows to infinity. Here, we adopt a finite-sample point of view, motivated by advances in modern statistics \[(https://arxiv.org/html/2404.01100v2#bib.bib4), (https://arxiv.org/html/2404.01100v2#bib.bib5)\] and statistical learning theory. Asymptotic methods are sharp asymptotically but are often heuristically applied for finite samples. Finite-sample bounds, on the other hand, are valid for any number of samples, but suffer from looser bounding constants. Nonetheless, they can provide a more detailed qualitative characterization of the statistical difficulty of learning \[(https://arxiv.org/html/2404.01100v2#bib.bib6)\].

While finite-sample system identification has been studied before, most results are focused on time domain identification \[(https://arxiv.org/html/2404.01100v2#bib.bib7), (https://arxiv.org/html/2404.01100v2#bib.bib8), (https://arxiv.org/html/2404.01100v2#bib.bib9), (https://arxiv.org/html/2404.01100v2#bib.bib10), (https://arxiv.org/html/2404.01100v2#bib.bib11), (https://arxiv.org/html/2404.01100v2#bib.bib12), (https://arxiv.org/html/2404.01100v2#bib.bib13), (https://arxiv.org/html/2404.01100v2#bib.bib14), (https://arxiv.org/html/2404.01100v2#bib.bib15), (https://arxiv.org/html/2404.01100v2#bib.bib16)\]. Detailed related work and a tutorial on the subject can be found in \[(https://arxiv.org/html/2404.01100v2#bib.bib6), (https://arxiv.org/html/2404.01100v2#bib.bib17)\]. Frequency domain and time domain identification have many similarities--ignoring initial conditions, transients, or leakage effects, the two domains are equivalent from a prediction error framework perspective \[(https://arxiv.org/html/2404.01100v2#bib.bib2)\]. Still, working in one domain may offer some advantages over the other \[(https://arxiv.org/html/2404.01100v2#bib.bib2)\]. For example, the frequency domain approach allows a unified treatment of discrete and continuous time systems, simplifies the analysis of systems with delays, and offers a more explicit way of designing the input excitation.

Our contributions are the following:

Finite-sample guarantees for the ETFE. We provide finite sample guarantees for the well-established Empirical Transfer Function Estimate (ETFE) \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\], a non-parametric method for frequency domain identification, under open-loop periodic excitation. While the mean and variance of the ETFE have been characterized before, we provide guarantees on the distribution of the estimation error, the tail probabilities in particular. Under certain stability conditions, we prove that the estimation error decays with a rate of $\sqrt{M/N_{tot}}$, where $N_{tot}$ is the total number of samples. The parameter $M$ is the number of selected frequencies at which we estimate the frequency response; it controls the frequency resolution. The rate holds for general irrational transfer functions and does not require a finite order state-space representation, unlike prior non-asymptotic bounds \[(https://arxiv.org/html/2404.01100v2#bib.bib11)\].

Guarantees in the $\mathcal{H}_{\infty}$ norm. Based on our finite-sample bound, we tune the number of frequencies $M$ to provide guarantees for learning the frequency response across all frequencies. We provide a non-asymptotic rate of $N_{tot}^{- {1/3}}$ in the $\mathcal{H}_{\infty}$ norm of the estimation error, which reflects optimal rates for non-parametric learning of Lipschitz functions \[(https://arxiv.org/html/2404.01100v2#bib.bib18)\].

Extension of the Hanson-Wright inequality. To prove our main result we have to deal with quadratic forms of a (countably) infinite number of sub-Gaussian variables. To achieve this, we extend the celebrated Hanson-Wright inequality \[(https://arxiv.org/html/2404.01100v2#bib.bib4), (https://arxiv.org/html/2404.01100v2#bib.bib19)\] to semi-infinite matrices; that is, bounded operators mapping sequences to finite vector spaces.

Our paper is related to non-parametric system identification, which includes works on both time \[(https://arxiv.org/html/2404.01100v2#bib.bib20)\] and frequency domain \[(https://arxiv.org/html/2404.01100v2#bib.bib21)\]. Using Gaussian Processes as in \[(https://arxiv.org/html/2404.01100v2#bib.bib21)\], where the unknown frequency response follows a Gaussian prior, we can also obtain finite sample guarantees. Here, we follow a different approach and we do not consider Gaussian priors. Note that in this work we focus on qualitative data-independent bounds linking sample requirements to system theoretic properties. Data-dependent bounds, which are arguably more suitable for applications, have also been studied before \[(https://arxiv.org/html/2404.01100v2#bib.bib22), (https://arxiv.org/html/2404.01100v2#bib.bib23), (https://arxiv.org/html/2404.01100v2#bib.bib24)\].

Notation. Let $(H,{\mathbb{F}},{\langle \cdot, \cdot \rangle}_{H})$ be a Hilbert space with field ${\mathbb{F}} =$ or $\mathbb{C}$ and inner product ${\langle \cdot, \cdot \rangle}_{H}$. For any vector $x \in H$, let ${\| x\|} \triangleq \sqrt{{\langle x,x\rangle}_{H}}$ denote the inner product norm. Let $H,V$ be Hilbert spaces with ${\mathbb{F}} =$ or $\mathbb{C}$ and let $\mathcal{A}:{H\rightarrow V}$ be any linear map. Let ${\|\mathcal{A}\|}_{op} \triangleq {\sup_{{\| x\|} = 1}{\|{\mathcal{A}{(x)}}\|}}$ denote the operator norm and $\mathcal{A}^{\ast}$ denote the adjoint operator. If $\left\{ b_{i} \right\}_{i \in \mathcal{I}}$ is an orthonormal basis, the Hilbert-Schmidt or Frobenius norm is defined as ${\|\mathcal{A}\|}_{F}^{2} \triangleq {\sum_{i \in \mathcal{I}}{\|{\mathcal{A}{(b_{i})}}\|}^{2}}$. Let $\mathcal{L}_{2}{(p)} \triangleq {\{\left\{ x_{k} \right\}_{k = 1}^{\infty}:x_{k} \in^{p},\sum_{k = 1}^{\infty} \parallel x_{k} \parallel^{2} < \infty\}}$ be the Hilbert space of $p$-dimensional square summable sequences. A universal constant is a constant that is independent of the problem at hand, e.g., the system or the algorithm. For any integer $M$, let ${\lbrack M\rbrack} \triangleq {0,\ldots,{M - 1}}$. The $\mathcal{H}_{\infty}$ norm of ${G{(e^{j\omega})}}:{{\lbrack 0,{2\pi})}\rightarrow{\mathbb{C}}^{d_{1} \times d_{2}}}$ is given by $\sup_{\omega \in {\lbrack 0,{2\pi})}}{\|{G{(e^{j\omega})}}\|}_{op}$; it is denoted by ${\| G\|}_{\mathcal{H}_{\infty}}$.

## Problem formulation

Consider the input-output system ((https://arxiv.org/html/2404.01100v2#S1.E1 "In 1 Introduction ‣ Finite Sample Frequency Domain Identification")). We make the following assumption about the noise process $v_{t}$.

### Assumption 1 (Noise)

The noise process $v_{t}$ is filtered sub-Gaussian white noise, that is,

where $h_{t} \in {\mathbb{R}}^{d_{y} \times d_{e}}$ are the *unknown* filter coefficients. Let $e_{t} \in {\mathbb{R}}^{d_{e}}$ be i.i.d. zero mean, with covariance ${{\mathbb{E}}e_{t}e_{t}^{\top}} = {\sigma_{e}^{2}I_{d_{e}}}$, and $K^{2}$-sub-Gaussian \[(https://arxiv.org/html/2404.01100v2#bib.bib4)\], i.e., for any $\xi \in^{d_{e}}$

The noise process $v_{t}$ is colored. It is used to model measurement noise as well as any stochastic disturbances acting on the dynamical system.

We assume throughout that the input is bounded. This guarantees that any transient phenomena have a limited effect on the estimation problem.

### Assumption 2 (Input Bound)

All inputs are bounded

for some $D_{u} > 0$ independent of $t$.

We start all identification experiments at time $t = 0$. Hence, the initial conditions are determined by all past signals $u_{- 1},u_{- 2},\ldots$ and ${e_{- 1},e_{- 2},\ldots},$, which are nonzero in general, and unknown. Note that our formulation allows general irrational transfer functions and does not assume a state-space representation of finite dimension.

### Empirical Transfer Function Estimate

The goal of non-parametric frequency domain identification is to estimate the frequency response $G{(e^{j\omega})}$, given input-output data. We assume access to $d_{u}$ experiments of length $N$, that is, data $(u_{0}^{(i)},y_{0}^{(i)},\ldots,u_{N - 1}^{(i)},y_{N - 1}^{(i)})$, for $i = {1,\ldots,d_{u}}$. This brings the total number of samples to $N_{tot} \triangleq {d_{u}N}$. We assume that the trajectories are *statistically independent* and we leave the single trajectory case for future work.

We are interested in the performance of the ETFE, which we review here. Given any signal $z = {\{ z_{t}\}}_{t \in {\lbrack N\rbrack}}$, let

denote its $N$-point Discrete Fourier Transform (DFT), evaluated at $k$. Let $Y_{k}^{(i)},U_{k}^{(i)}$ be the $N$ point DFTs of $y_{t}^{(i)}$ and $u_{t}^{(i)}$ respectively for the $i -$th experiment, $i = {1,\ldots,d_{u}}$. Let ${Y_{k} \in {\mathbb{C}}^{d_{y} \times d_{u}}},{U_{k} \in {\mathbb{C}}^{d_{u} \times d_{u}}}$ denote the stacked DFTs for all experiments

Then, an estimate of $G{(e^{j\omega})}$ at frequency $\omega_{k} = {{2\pi k}/N}$, for $k = {0,\ldots,{N - 1}}$, can be obtained using the *ETFE*

provided that $U_{k}$ is invertible; the estimate is undefined if not. Since the number of frequencies $N$ scales with the number of data, it is generally impossible to estimate the responses at all frequencies consistently (without assuming structure) \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\]. Instead, we can learn the responses at a smaller frequency set. Given a frequency-resolution parameter $M < N$, we focus on estimating $G{(e^{j\omega})}$ at $\omega = {{2\pi\ell}/M}$, for $\ell \in {\lbrack M\rbrack}$. Based on the ETFE and under some additional Lipschitz assumptions on the frequency response, we can extend the estimation over all frequencies $\omega \in {\lbrack 0,{2\pi})}$.

### Excitation Method

The estimation performance also depends on the excitation method. Since we only need to estimate the frequency responses at ${2\pi\ell}/M$, $\ell \in {\lbrack M\rbrack}$, it is sufficient to excite the system at only these frequencies \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\]. Assuming that $M$ divides $N$, the DFT $U_{k}$ of the input can be non-zero at only ${{2\pi k}/N} = {{2\pi\ell}/M}$ or $k = {{\ell N}/M}$. The latter condition is satisfied if and only if the excitation input is periodic with a period equal to $M$. Note that we also need invertibility of $U_{k}$ at $k = {{\ell N}/M}$. To achieve this, we assume the following.

### Assumption 3 (Excitation)

Let the input signals be periodic with period $M$ such that $u_{t + M}^{(i)} = u_{t}^{(i)}$, for $t \geq 0$ and every experiment $i = {1,\ldots,d_{u}}$. Assume that $M$ divides $N$ with $N_{p} \triangleq {N/M}$. Consider *one period* of the input signals and let the respective $M$-point DFTs be

for $\ell \in {\lbrack M\rbrack}$, with respective stacked DFTs

Assume that for all $\ell \in {\lbrack M\rbrack}$ the stacked DFTs satisfy

for some $0 < \sigma_{u,\ell}^{2}$.

By definition, for Assumptions (https://arxiv.org/html/2404.01100v2#Thmassumption2 "Assumption 2 (Input Bound). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") to be consistent, we need ${\sum_{\ell = 0}^{M - 1}\sigma_{u,\ell}^{2}} \leq {MD_{u}^{2}}$, where $D_{u}$ is the input upper bound of Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption2 "Assumption 2 (Input Bound). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification").

Such assumptions are standard when dealing with experiment design in frequency domain. For example, Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") is satisfied by design (with uniform $\sigma_{u,\ell}^{2}$ across $\ell \in {{\lbrack M\rbrack} - {\{ 0\}}}$) when pseudorandom binary sequence (PRBS) signals are used and we excite one input at a time \[(https://arxiv.org/html/2404.01100v2#bib.bib1), Ch. 13\]. Another choice could be multisine signals \[(https://arxiv.org/html/2404.01100v2#bib.bib25)\], where the user simply designs the input to have sinusoids with non-zero amplitudes at the required frequencies. Another option is to design the input spectrum and generate the input by passing a white noise realization through the spectral factor \[(https://arxiv.org/html/2404.01100v2#bib.bib26)\].

### Objective

We can now state our objective, which is providing finite-sample guarantees for estimating the frequency responses. We focus on $\epsilon - \delta$ probabilistic guarantees, where $\epsilon$ controls the estimation accuracy and $\delta$ controls the confidence. {mdframed}\[roundcorner=3pt, backgroundcolor=blue!6,innertopmargin=-2pt\]

### Problem 1 (Finite-Sample ETFE)

Fix a frequency resolution $M < N$ such that $M$ divides $N$ and denote their ratio by $N_{p} = {N/M}$. Consider $d_{u}$ independent input-ouput trajectories of length $N$ ${\{ u_{t}^{(i)},y_{t}^{(i)}\}}_{t \in {\lbrack N\rbrack}}$, for $i = {1,\ldots,d_{u}}$, generated by system ((https://arxiv.org/html/2404.01100v2#S1.E1 "In 1 Introduction ‣ Finite Sample Frequency Domain Identification")) with excitation inputs as in Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"). Fix a failure probability $0 < \delta < 1$. Determine $\epsilon_{\ell} > 0$, $\ell \in {\lbrack M\rbrack}$ such that

where the ETFE ${\hat{G}}_{\ell N_{p}}$ is defined in ((https://arxiv.org/html/2404.01100v2#S2.E5 "In 2.1 Empirical Transfer Function Estimate ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")).

Problem (https://arxiv.org/html/2404.01100v2#Thmproblem1 "Problem 1 (Finite-Sample ETFE). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") only focuses on the desired discretized frequency grid ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$. In Section (https://arxiv.org/html/2404.01100v2#S4 "4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification"), we also study uniform guarantees over all frequencies in the $\mathcal{H}_{\infty}$ norm.

To guarantee a well-defined estimation problem, we consider the following stability conditions.

### Assumption 4 (Strict Stability)

The input-output impulse response is strictly stable \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\], that is,

The auto-correlation function of the noise $R_{t} \triangleq {{\mathbb{E}}v_{s}v_{s - t}^{\top}}$ is also strictly stable

Strict stability guarantees that the derivative of the frequency response $\partial{{G{(e^{j\omega})}}/{\partial\omega}}$ is uniformly bounded over all frequencies. This, in turn, implies that the response $G{(e^{j\omega})}$ is Lipschitz. Strict stability also guarantees that the transient phenomena have a limited effect on the estimation procedure.

## Finite-sample guarantees for the ETFE

In this section, we focus on estimating the frequency response at ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$, that is, the selected frequencies. Following the convention of ((https://arxiv.org/html/2404.01100v2#S2.E4 "In 2.1 Empirical Transfer Function Estimate ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")), we define the stacked DFTs of the noises and the noiseless outputs as

Then, for every frequency $\omega_{k} = {{2\pi k}/N}$ we have

where $T_{k,N} = {{\overline{Y}}_{k} - {G{(e^{j\omega_{k}})}U_{k}}}$ accounts for transient and time-aliasing phenomena since the DFT of ${\{{\overline{y}}_{t}^{(i)}\}}_{t = 0}^{N - 1}$ is different from ${\{{G{(e^{j\omega_{k}})}U_{k}^{(i)}}\}}_{k = 0}^{N - 1}$ for finite $N$. This term vanishes as $N$ grows to infinity.

### Remark 1

The above relation fits the framework of non-parametric function estimation. However, there are some notable differences with standard formulations \[(https://arxiv.org/html/2404.01100v2#bib.bib18), (https://arxiv.org/html/2404.01100v2#bib.bib5)\]. First, we have the presence of the input $U_{k}$, which affects the signal-to-noise ratio (SNR) and is an additional degree of freedom. For example, if the input matrix is not invertible at some $k$, we do not get a well-defined sample of $G{(e^{j\omega_{k}})}$. Second, the noise $V_{k}$ is heteroscedastic since its variance depends on the frequency $k$. Moreover, the sequence ${V_{k},k} \in {\lbrack N\rbrack}$ is non-Gaussian and non-independent across frequencies for finite samples $N$ (only asymptotically as $N$ goes to infinity). Hence, the non-asymptotic techniques of \[(https://arxiv.org/html/2404.01100v2#bib.bib5), Ch. 13\] do not apply directly.

The estimation error is equal to

where the input matrix $U_{k}$ is invertible, and we only look at the frequencies $k = {\ell N_{p}}$, $\ell \in {\lbrack M\rbrack}$. Let ${\Phi_{v,N}{(k)}} \triangleq {{\mathbb{E}}V_{k}^{(i)}{(V_{k}^{(i)})}^{\ast}}$ be the aliased power spectrum of the process $v_{t}$ at frequency $k$, where due to independence, the experiment index $i$ does not affect the definition. Define the signal-to-noise ratio (SNR) at frequency ${k = {\ell N_{p}}},$ $\ell \in {\lbrack M\rbrack}$ as

where ${\|{\Phi_{v,N}{(k)}}\|}_{op}$ is interpreted as the matrix norm for fixed $k$. We obtain the following finite-sample guarantees.

### Theorem 1 (ETFE Finite-Sample)

Consider Problem (https://arxiv.org/html/2404.01100v2#Thmproblem1 "Problem 1 (Finite-Sample ETFE). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") and fix a failure probability $\delta > 0$. Under Assumptions (https://arxiv.org/html/2404.01100v2#Thmassumption1 "Assumption 1 (Noise). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")-(https://arxiv.org/html/2404.01100v2#Thmassumption4 "Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), with probability at least $1 - \delta$ for all $k = {\ell N_{p}}$, $\ell \in {\lbrack M\rbrack}$

where $c$ is a universal constant, ${\| G\|}_{\star}$ is defined in ((https://arxiv.org/html/2404.01100v2#S2.E7 "In Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")), and $D_{u}$ is the maximum input norm.

The exact value of the universal constant can be found in the proof. The first term of the right-hand side captures the transient error $T_{k,N}U_{k}^{- 1}$, while the second one captures the error $V_{k}U_{k}^{- 1}$ due to stochastic noise. Recall that the total number of samples is equal to $N_{tot} = {d_{u}N}$. As we increase the number of samples $N_{tot}$ while keeping $M$ constant, the former term decays at a faster rate of $1/N_{tot}$ compared to the latter's $1/\sqrt{N_{tot}}$. Hence, the non-asymptotic rate is

The rate is similar to the ones for non-asymptotic parametric identification in time-domain \[(https://arxiv.org/html/2404.01100v2#bib.bib17)\]; the optimal rate in that line of work is typically of the order $\sqrt{d}$ for some $d$ scaling with the number of unknown parameters. Here, we have a similar scaling of $\sqrt{M}{({\sqrt{d_{u}} + \sqrt{d_{y}}})}$ (ignoring log terms) times an additional $\sqrt{d_{u}}$ dimensional dependence. This is an artifact of imposing a strict input norm bound in Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption2 "Assumption 2 (Input Bound). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"). If we allow $\sigma_{u},D_{u}$ to scale with $\sqrt{d_{u}}$ (as is the case for white-noise inputs in the time-domain \[(https://arxiv.org/html/2404.01100v2#bib.bib17)\]), we can remove this extra term.

A benefit of frequency-domain identification is that it provides specialized guarantees for every frequency of interest by breaking down the SNR into SNRs for every frequency. This offers direct insights on which frequencies to focus on and how to design the excitation inputs. Note that the inverse ${SNR}_{k,N}^{- 1}$ is upper bounded and converges to a limit as $N$ grows to infinity. This is a consequence of the following result which exploits the strict stability condition ((https://arxiv.org/html/2404.01100v2#S2.E8 "In Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")).

### Lemma 1 (Stochastic Transient \[[1](https://arxiv.org/html/2404.01100v2#bib.bib1), Sec. 6.3\])

Denote the power spectrum of the noise at frequency $\omega_{k} = {{2\pi k}/N}$, for some $k \in {\lbrack N\rbrack}$, by ${\Phi_{v}{(k)}} \triangleq {\sum_{t = {- \infty}}^{\infty}{R_{t}e^{- {j\omega_{k}t}}}}$, with $R_{- t} = R_{t}^{\top}$. We have

In the remainder of the section, we provide a sketch of the proof of Theorem (https://arxiv.org/html/2404.01100v2#Thmtheorem1 "Theorem 1 (ETFE Finite-Sample). ‣ 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification"). We simply bound every term that appears in ((https://arxiv.org/html/2404.01100v2#S3.E10 "In 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification")) separately.

### Deterministic transient

Even in the absence of any stochastic noise, the ETFE suffers from estimation errors due to transient phenomena (e.g. aliasing, leakage) \[(https://arxiv.org/html/2404.01100v2#bib.bib2)\]. Fortunately, the transient error $T_{k,N} = {{\overline{Y}}_{k} - {G{(e^{j\omega_{k}})}U_{k}}}$ decays uniformly to zero as the DFT horizon $N$ goes to infinity.

### Lemma 2 (Deterministic Transient \[[1](https://arxiv.org/html/2404.01100v2#bib.bib1), Sec. 2.2\])

The above result is a consequence of bounded inputs and strict stability (Assumptions (https://arxiv.org/html/2404.01100v2#Thmassumption2 "Assumption 2 (Input Bound). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), (https://arxiv.org/html/2404.01100v2#Thmassumption4 "Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")). Together they guarantee that the deterministic transient phenomena have a vanishing effect on the estimation procedure.

### Input energy

Next, we review a standard result for periodic inputs. The input $U_{k}$ at frequencies $k = {\ell N_{p}}$ is equal to $\sqrt{N_{p}}{\overset{\sim}{U}}_{\ell}$, where ${\overset{\sim}{U}}_{\ell}$ is the $M -$point DFT based on one period of the input signals (see Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification")). As a result, $U_{k}^{- 1}$ is well-defined and vanishes to zero with $N_{p}^{- {1/2}}$. This phenomenon is a direct consequence of periodicity and the properties of DFT.

### Lemma 3 (Input energy)

Let Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification") be in effect. Then, for all $k = {N_{p}\ell}$, $\ell \in {\lbrack M\rbrack}$

Lemma (https://arxiv.org/html/2404.01100v2#Thmlemma3 "Lemma 3 (Input energy). ‣ 3.2 Input energy ‣ 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification") is key to achieving consistency. While the known input is periodic, the noise is not. Hence, at the selected frequencies, the noise is averaged out.

### Noise concentration

Finally, we bound the noise term $V_{k}$ by showing that its norm concentrates around $\sqrt{{tr}{({\Phi_{v,N}{(k)}})}}$.

### Lemma 4 (Concentration of noise)

Fix a $k \in {\lbrack N\rbrack}$. Under Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption1 "Assumption 1 (Noise). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), for any $s > 0$

Prior results show that $V_{k}^{(i)}$ is asymptotically circular Gaussian as $N$ goes to infinity \[(https://arxiv.org/html/2404.01100v2#bib.bib3), Ch. 16\]. We show that even under finite $N$, the tails of the distribution decay exponentially reflecting the properties of the Gaussian distribution.

The proof of Lemma (https://arxiv.org/html/2404.01100v2#Thmlemma4 "Lemma 4 (Concentration of noise). ‣ 3.3 Noise concentration ‣ 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification") is based on a novel extension of the Hanson-Wright inequality \[(https://arxiv.org/html/2404.01100v2#bib.bib19)\], a standard tool for proving concentration of quadratic forms involving random variables. Note that $V_{k}$ is a linear function of an infinite number of random noises $e_{t}^{(i)}$, $i = {1,\ldots,d_{u}}$, ${- \infty} < t \leq {N - 1}$. Hence, we need to extend the Hanson-Wright inequality \[(https://arxiv.org/html/2404.01100v2#bib.bib19), (https://arxiv.org/html/2404.01100v2#bib.bib27)\] to semi-infinite matrices, that is, bounded operators from square summable (real-valued) sequences $\mathcal{L}_{2}$ to finite vector spaces.

### Theorem 2 (Semi-infinite Hanson-Wright)

Consider a sequence $z \triangleq {\{ z_{t}\}}_{t = 1}^{\infty},z_{t} \in^{p}$ of independent, zero-mean, $K^{2}$-sub-Gaussian random variables with covariance ${{\mathbb{E}}z_{t}z_{t}^{\top}} = {\sigma_{e}^{2}I_{p}}$. Let $\mathcal{A}:{{\mathcal{L}_{2}{(p)}}\rightarrow^{d}}$ be a linear map with bounded Frobenius norm ${\|\mathcal{A}\|}_{F} < \infty$. For any $\alpha > 0$

where the extension $\mathcal{A}{(z)}$ to $z$ is defined almost surely and $\parallel \cdot \parallel$ denotes the inner product norm.

The constants that appear in the statement are similar to \[(https://arxiv.org/html/2404.01100v2#bib.bib17)\]; we extend their proof to semi-infinite matrices. The Hanson-Wright inequality can be used to prove concentration of quadratic forms of the form $\xi^{\ast}V_{k}^{\ast}V_{k}\xi$. This, in turn, implies concentration of the norm ${\| V_{k}\|}_{op}$ via the variational representation of the norm ${\| V_{k}\|}_{op}^{2} = {\sup_{{\|\xi\|} = 1}{\xi^{\ast}V_{k}^{\ast}V_{k}\xi}}$.

## Estimation over all frequencies

In the previous section, we derived finite-sample guarantees for estimating the frequency responses at fixed selected frequencies ${2\pi\ell}/M$, $\ell \in {\lbrack M\rbrack}$. Here, we derive guarantees for estimating the function $G{(e^{j\omega})}$ uniformly over all $\omega \in {\lbrack 0,{2\pi})}$ in the $\mathcal{H}_{\infty}$ norm. We consider a naive estimator where to compute $\hat{G}{(e^{j\omega})}$ we use the closest frequency $\hat{G}{(e^{{j2\pi\ell}/M})}$, for some $\ell \in {\lbrack M\rbrack}$.

Let $\chi{(t)}$ be the indicator function of the half-open interval $\lbrack{- {1/2}},{1/2})$. Define the naive estimator

Due to strict stability, it follows that the frequency response is smooth with Lipschitz constant upper bounded by ${\| G\|}_{\star}$. This follows from the fact that

Hence, for any $\omega \in {\lbrack 0,{2\pi})}$, the error is bounded by

for some $\ell \in {\lbrack M\rbrack}$. The first term scales with $1/M$, while the latter scales with $\sqrt{M/N}$, excluding logarithmic terms. Balancing the two terms, we obtain the following guarantees.

### Theorem 3 (Guarantees in $\mathcal{H}_{\infty}$ norm)

Let $M = {c_{1}N^{1/3}}$, for some $c_{1} > 0$ such that $M$, $N/M$ are integers. Consider the naive estimator ((https://arxiv.org/html/2404.01100v2#S4.E16 "In 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification")) and fix a failure probability $\delta$. Under Assumptions (https://arxiv.org/html/2404.01100v2#Thmassumption1 "Assumption 1 (Noise). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), (https://arxiv.org/html/2404.01100v2#Thmassumption2 "Assumption 2 (Input Bound). ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), (https://arxiv.org/html/2404.01100v2#Thmassumption3 "Assumption 3 (Excitation). ‣ 2.2 Excitation Method ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), (https://arxiv.org/html/2404.01100v2#Thmassumption4 "Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"), with probability at least $1 - \delta$:

where $c$ is a universal constant,

is the worst case SNR, and ${\underset{¯}{\sigma}}_{u} = {\min_{\ell \in {\lbrack M\rbrack}}\sigma_{u,\ell}}$ is the worst case excitation among the frequencies of interest.

We can tune the constant $c_{1}$ to guarantee $N_{p}$ is an integer and trade between the Lipschitz constant and the SNR. Excluding logarithmic factors, we obtain a rate of $N_{tot}^{- {1/3}}$ which is the optimal one for non-parametric estimation of Lipschitz functions \[(https://arxiv.org/html/2404.01100v2#bib.bib18), (https://arxiv.org/html/2404.01100v2#bib.bib5)\]. The rate is suboptimal when higher order derivatives exist, which would imply stricter stability conditions than Assumption (https://arxiv.org/html/2404.01100v2#Thmassumption4 "Assumption 4 (Strict Stability). ‣ 2.3 Objective ‣ 2 Problem formulation ‣ Finite Sample Frequency Domain Identification"). For example, for twice differentiable functions, the rate can be improved to $N_{tot}^{- {2/5}}$ \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\]. In the setting of rational functions, strict stability is equivalent to exponential stability, which, in turn, implies the existence of all high-order derivatives of $G$. In this case, it would be suboptimal to employ the naive estimator ((https://arxiv.org/html/2404.01100v2#S4.E16 "In 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification")) without additional smoothing. We leave this for future work.

The $\mathcal{H}_{\infty}$ norm bound picks up the frequency which is the hardest to learn as it depends on the worst-case SNR. Assume that the input excites uniformly all frequencies, that is, $\sigma_{u,\ell} = \sigma_{u}$, for all $\ell \in {\lbrack M\rbrack}$. Then, the worst case SNR scales inversely with $\sup_{\ell}\sqrt{{\|{\Phi_{v,N}{({\ell N_{p}})}}\|}_{op}}$; as we increase the frequency resolution $M$, this quantity scales, in turn, with the $\mathcal{H}_{\infty}$ norm of the noise filter $H{(q)}$.

Figure 1: The (normalized) empirical maximum error of the ETFE over the fixed frequency grid 2πℓ/M, ℓ ∈ [M], for fixed M. The shaded areas show one (empirical) standard deviation. It decays with a rate of N−1/2. Moreover, the error increases as we require more resolution, i.e., larger M. The error for M = 2047 is roughly $\sqrt{2}$ times larger than for M = 1023, verifying the result of Theorem 1.

Figure 2: The (normalized) empirical ℋ∞ norm of the ETFE, based on the naive estimator. The shaded areas show one (empirical) standard deviation. We optimize the value of M for every choice of N. Unlike the error at fixed frequencies, it decays slower, with a rate of N−1/3.

## Simulations

We study the performance of the ETFE and the naive estimator via a numerical example. Consider the system

with noise filter ${H{(q)}} = {({1 - {0.2q^{- 1}}})}^{- 1}$. Let all past inputs be zero ${u_{t} = 0},{t < 0}$. We generate the excitation signal based on PRBS \[(https://arxiv.org/html/2404.01100v2#bib.bib1)\] with an additional offset to excite the zero frequency. Note that PRBS maximal length signals require $M = {2^{d} - 1}$, for some $d \in {\mathbb{N}}$.

In the first simulation, we study the maximum error of the ETFE over the fixed grid ${\{{{2\pi\ell}/M}\}}_{\ell \in {\lbrack M\rbrack}}$

which can be thought as the "discretized" $\mathcal{H}_{\infty}$ norm of the error. We keep $M$ fixed, $\sigma_{e}^{2} = 0.1$, and we vary the total number of samples $N_{tot} = N$. To visualize the results, we perform $100$ Monte Carlo iterations for every number of samples $N$ and we present the empirical mean along with one empirical standard deviation. As shown in Fig. (https://arxiv.org/html/2404.01100v2#S4.F1 "Figure 1 ‣ 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification"), the error decays with a rate of $N^{- {1/2}}$ validating Theorem (https://arxiv.org/html/2404.01100v2#Thmtheorem1 "Theorem 1 (ETFE Finite-Sample). ‣ 3 Finite-sample guarantees for the ETFE ‣ Finite Sample Frequency Domain Identification").

In the second simulation, we study the maximum error of the naive estimator ((https://arxiv.org/html/2404.01100v2#S4.E16 "In 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification")) over all frequencies, that is, the "true" $\mathcal{H}_{\infty}$ norm of the error. For every number of samples $N$, we tune $d$ in $M = {2^{d} - 1}$ to be the optimal one (empirically), and we perform $100$ Monte Carlo simulations. As shown in Fig. (https://arxiv.org/html/2404.01100v2#S4.F2 "Figure 2 ‣ 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification"), the error decays with a rate of $N^{- {1/3}}$ reflecting the result of Theorem (https://arxiv.org/html/2404.01100v2#Thmtheorem3 "Theorem 3 (Guarantees in ℋ_∞ norm). ‣ 4 Estimation over all frequencies ‣ Finite Sample Frequency Domain Identification").

## Conclusion and Future Work

We provide finite-sample guarantees for the ETFE over a selected frequency grid, in the case of open-loop periodic excitation and under strict stability assumptions. By tuning the frequency resolution and exploiting Lipschitz continuity, we also obtain estimation guarantees in the $\mathcal{H}_{\infty}$ norm. An interesting direction for future work is studying finite-sample non-parametric least squares \[(https://arxiv.org/html/2404.01100v2#bib.bib5), (https://arxiv.org/html/2404.01100v2#bib.bib16)\] in the frequency domain. This approach could lead to interesting connections between function class complexity and experiment design. Moreover, adding more structure, beyond Lipschitz continuity, will lead to faster rates. Other topics that are left for future work include the estimation of the noise statistics and extending the guarantees to different variations of the excitation method and the ETFE \[(https://arxiv.org/html/2404.01100v2#bib.bib28)\]. Finally, extending minimax lower bounds to this setting is also open \[(https://arxiv.org/html/2404.01100v2#bib.bib29)\].
