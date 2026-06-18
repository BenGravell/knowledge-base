## Introduction

System identification is an important topic in control theory. Accurate estimation of system dynamics is the basis of control or policy decision problems in tasks varying from linear-quadratic control to deep reinforcement learning. Consider a linear time-invariant system of order $R$ with the *minimal* state-space representation

where $x_{t} \in {\mathbb{R}}^{R}$ is the state, $u_{t} \in {\mathbb{R}}^{p}$ is the input, $y_{t} \in {\mathbb{R}}^{m}$ is the output, $z_{t} \in {\mathbb{R}}^{m}$ is the output noise, $A \in {\mathbb{R}}^{R \times R}$, $B \in {\mathbb{R}}^{R \times p}$, $C \in {\mathbb{R}}^{m \times R}$, $D \in {\mathbb{R}}^{m \times p}$ are the system parameters, and $x_{0}$ is the initial state (in this paper, we assume $x_{0} = 0$). Generally with the same input and output, the dimension of the hidden state $x$ can be any number no less than $R$, and we are interested in the minimum dimensional representation (i.e., minimal realization) in this paper.

*The goal of system identification is to find the system parameters, such as $A,B,C,D$ matrices or impulse response, given input and output observations.* If ${(C,D)} = {(I,0)}$, we directly observe the state. A notable line of work derives statistical bounds for system identification with limited *state* observations from a single output trajectory (defined in Fig. 2) with a random input. The state evolves as $x_{t + 1} = {{Ax_{t}} + \eta_{t}}$ where $\eta_{t}$ is the white noise that provides excitation to states. They recover $A$ by solving a least-squares problem. The main proof approach comes from an analysis of martingales \[4, Thm 2,3\]. assumes that the system is stable whereas removes the assumptions on the spectral radius of $A$.

When we do not directly observe the state $x$ (also known as hidden-state), one has only access to $u_{t}$ and $y_{t}$ and lack the full information on $x_{t}$. We recover the impulse response (also known as the Markov parameters) sequence $h_{0} = D$, $h_{t} = {CA^{t - 1}B} \in {\mathbb{R}}^{m \times p}$ for $t = {1,2,\ldots}$ that uniquely identifies the end-to-end behavior of the system. The impulse response can have infinite length, and we let $h = {\lbrack D,{CB},{CAB},{CA^{2}B},\ldots,{CA^{{2n} - 3}B}\rbrack}^{\top}$ denote its first ${2n} - 1$ entries, which can be later placed into an $n \times n$ Hankel matrix. Without knowing the system order, we consider recovering the first $n$ terms of $h$ where $n$ is larger than system order $R$. To this end, let us also define the Hankel map $\mathcal{H}:{{\mathbb{R}}^{{m \times {({{2n} - 1})}}p}\rightarrow{\mathbb{R}}^{{{mn} \times p}n}}$ as

If $n \geq R$, the Hankel matrix $H$ is of rank $R$ regardless of $n$ \[5, Sec. 5.5\]. Specifically, we will assume that $R$ is small, so the Hankel matrix is low rank. Our goal is to recover a low rank Hankel matrix. It is known that nuclear norm regularization is used to find a low rank matrix, and uses it for recovering a low rank Hankel matrix.

Low-rank Hankel matrices arise in a range of applications, from dynamical systems -- where the rank corresponds to a low order or MacMillan degree for the system -- to signal processing problems. The latter includes recovering sum of complex exponentials (where the rank of the Hankel matrix is the number of summands), shape-from-moments estimation in tomography and geophysical inversion (where the vertices of an object are probed and the output is a sum of exponentials), and video in-painting (where the video is regarded as a low order system).

Performance criteria for system identification: To explain our contributions, we introduce common performance metrics. Refs. and recover the system from single rollout/trajectory (\"rollout\" is defined in Sec. 3) of the input signal, whereas our work, and require multiple rollouts. To ensure a standardized comparison, we define *sample complexity* to be the number of equations (equality constraints in variables $h_{t}$) used in the problem formulation, which is same as the number of observed outputs (see Fig. 2 and Sec. 3). With this, we explore the following performance metrics for learning the system from $T$ output measurements.

Sample complexity: The minimum sample size $T$ for recovering system parameters with zero error when the noise is set to $z = 0$. This quantity is lower bounded by the system order. System order can be seen as the "degrees of freedom\" of the system.

Impulse Response (IR) Estimation Error: The Frobenius norm error ${\|{\hat{h} - h}\|}_{F}$ for the IR. A good estimate of IR enables the accurate prediction of the system output.

Hankel Estimation Error: The spectral norm error $\|{\mathcal{H}{({\hat{h} - h})}}\|$ of the Hankel matrix. This metric is particularly important for system identification as described below.

The Hankel spectral norm error is a critical quantity for several reasons. First, the Hankel spectral norm error connects to the $\mathcal{H}_{\infty}$ estimation of the system. Secondly, bounding this error allows for robustly finding balanced realizations of the system; for example, the error in reconstructing state-space matrices ($A,B,C,D$) via the Ho-Kalman procedure is bounded by the Hankel spectral error. Finally, it is beneficial in model selection, as a small spectral error helps distinguish the true singular values of the system from the spurious ones caused by estimation error. Indeed, as illustrated in the experiments, the Hankel singular value gap of the solution of the regularized algorithm is more visible compared to least-squares, which aids in identifying the true order of the system as explored in Sec. 7.

Algorithms: Hankel-regularization & OLS. In our analysis, we consider a multiple rollout setup where we measure the system dynamics with $T$ separate rollouts. For each rollout, the input sequence is $u^{(i)} = {\lbrack u_{{2n} - 1}^{(i)},\ldots,u_{1}^{(i)}\rbrack} \in {\mathbb{R}}^{{({{2n} - 1})}p}$ and we measure the system output at time ${2n} - 1$. Note that the $i^{th}$ output at time ${2n} - 1$ is simply $h^{\top}u^{(i)}$. Define $\overline{\mathbf{U}} \in {\mathbb{R}}^{{T \times {({{2n} - 1})}}p}$ where the $i^{th}$ row is $u^{(i)}$. Let $y \in {\mathbb{R}}^{T \times m}$ denote the corresponding observed outputs. Hankel-regularization refers to the nuclear norm regularized problem (HNN).

Finally, setting $\lambda = 0$, we obtain the special case of ordinary least-squares (OLS).

## Contributions

Our main contribution is establishing data-driven guarantees for Hankel nuclear norm regularization and shedding light on the benefit of regularization through a comparison to the ordinary least-squares (OLS) estimator. Specifically, a summary of our findings are as follows.

$\bullet$ Hankel nuclear norm (Sec. 4 & 4.2): For multi-input/single-output (MISO) systems ($p$ input channels), we establish *near-optimal sample complexity* bounds for the Hankel-regularized system identification, showing the required sample size grows as $\mathcal{O}{({pR{\log^{2}n}})}$ where $R$ is the system order and $n$ is the Hankel size. This result utilizes an *input-shaping* strategy (rather than i.i.d. excitation, see Fig. 1a) and builds on who studied the recovery of a sum-of-exponentials signal. Our bound significantly improves over naive bounds. For instance, without Hankel structure, enforcing low-rank would require $\mathcal{O}{({nR})}$ samples and enforcing Hankel structure without low-rank would require $\mathcal{O}{(n)}$ samples.

We also establish finite sample bounds on the IR and Hankel spectral errors. Our rates are on par with the OLS rates; however, unlike OLS, they also apply in the small sample size regime ${pn} \gtrsim T \gtrsim {pR{\log^{2}n}}$.

Surprisingly, Sec. 4.2 shows that the *input-shaping* is necessary for the logarithmic sample complexity in $n$. Specifically, we prove that if the inputs are i.i.d. standard normal (Fig. 1b), the minimum number of observations to exactly recover the impulse response in the noiseless case grows as $T \gtrsim n^{1/6}$.

Figure 1: (a) Shaped input (where variance of u (t) changes over time): recovery is guaranteed when T ≈ R; (b) i.i.d input (fixed variance): recovery fails with high probability when T ≲ n1/6. See Sec. 4.2.

$\bullet$ Sharpening OLS bounds (Sec. 5): For multi-input/multi-output (MIMO) systems, we establish a *near-optimal spectral error rate* for the Hankel matrix when $T \gtrsim {np}$. Our error rate improves over that of and our sample complexity improves over and which require $\mathcal{O}{(n^{2})}$ samples rather than $\mathcal{O}{(n)}$. This refinement is accomplished by relating the IR and Hankel errors. Specifically, using the fact that rows of the Hankel matrix are subsets of the IR sequence, we always have the inequality

Observe that there is a factor of $\sqrt{n}$ gap between the left-hand and right-hand side inequalities. We show that the left-hand side is typically the tighter one, thus ${\|{\hat{h} - h}\|}_{F} \sim {\|{\mathcal{H}{({\hat{h} - h})}}\|}$.

$\bullet$ Guarantees on accurate model-selection (Sec. 6): The Hankel-regularized algorithm requires a proper choice of the regularization parameter $\lambda$. In practice, the optimal choice is data dependent and one usually estimates $\lambda$ via trial and error based on the validation error. We provide a complete procedure for model selection (training & validation phases), and establish statistical guarantees for it.

$\bullet$ Contrasting Hankel regularization and OLS (Sec. 7): Finally, we assess the benefits of regularization via numerical experiments on system identification focusing on data collected from a single-trajectory.

We first consider synthetic data and focus on low-order systems with slow impulse-response decay. The slow-decay is intended to exacerbate the FIR approximation error arising from truncating the impulse-response at ${2n} - 1$ terms. In this setting, OLS as well as are shown to perform poorly. In constrast, Hankel-regularization better avoids the truncation error as it allows for fitting a long impulse-response with few data (due to logarithmic dependence on $n$).

Our real-data experiments (on a low-order example from the DaISy datasets ) suggest that the regularized algorithm has empirical benefits in sample complexity, estimation error, and Hankel spectral gap, and demonstrate that the regularized algorithm is less sensitive to the choice of the tuning parameter, compared to OLS whose tuning parameter is the Hankel size $n$. Finally, comparison of least-squares approaches in (OLS) and reveals that OLS (which directly estimates the impulse response) performs substantially better than the latter (which estimates the Hankel matrix). This highlights the role of proper parameterization in system identification.

### Prior Art

The traditional unregularized methods include Cadzow approach, matrix pencil method, Ho-Kalman approach and the subspace method raised in, further modified as frequency domain subspace method in when the inputs are single frequency (sine/cosine) signals. Recent works show that least-squares can be used to recover the Markov parameters and reconstruct $A,B,C,D$ from the Hankel matrix via the previously known Ho-Kalman algorithm. To identify a stable system from a single trajectory, estimates the impulse response and estimates the Hankel matrix via least-squares. The latter provides optimal Hankel spectral norm error rates, however has suboptimal sample complexity (see the table in Section 3). While use random input, \[15, Thm 1.1, 1.2\] use impulse and single frequency signal respectively as input. They both recover impulse response. These works assume known system order, or traverse the Hankel size $n$ to fit the system order. Ref. proves that least-squares can identify any (including unstable) linear systems with multiple rollout data. Ref. studies online system identification. It applies online gradient descent on least-squares loss and shows the identification error. Ref. shows that, when the system is strictly stable (${\rho{(A)}} < 1$), the sample complexity is only polynomial in ${({1 - {\rho{(A)}}})}^{- 1}$ and logarithmic in dimension.

There are several interesting generalizations of least squares with non-asymptotic guarantees for different goals. Refs. and introduce filtering strategies on top of least squares. The filters in is the top eigenvectors of a special deterministic matrix, used for output prediction in stable systems. Ref. uses filters in frequency domain to recover the system parameters of a stable system, gives a non-asymptotic analysis for learning a Kalman filter system, which can also be applied to an auto-regressive setting. As an extension, and apply system identification guarantee for robust control, where the system is identified and controlled in an episodic way. Ref. extended the online LQR to a non-episodic way. Ref. studies online control and regret analysis in adversarial setting, whose algorithm directly learns the policy in an end-to-end way. Ref. controls an unknown unstable system with no initial stabilizing controller. Another area is system identification with non-linearity. Ref. learns a linear system using nonlinear output observations. Refs. consider guarantees for certain nonlinear systems with state observations and study active learning where the new input adapts with respect to previous observations. Ref. studies the estimation and proposes the subsequent model-based control algorithm with missing data. Refs. study clustering and identification for Markov jump system and Ref. further analyzes the optimal control strategy based on the estimated system parameters.

Nuclear norm regularization has been shown to recover an unstructured low-rank matrix in a sample-efficient way in many settings (e.g., ). The regularized subspace method are introduced in. Refs. propose slightly different algorithms which recover low rank output Hankel matrix. Ref. specifies the application of Hankel nuclear norm regularization when some output data are missing. Ref. proposes a fast algorithm on solving the regularization algorithm. All above regularization works emphasize on optimization algorithm implementation and have no statistical bounds. More recently theoretically proves that a low order SISO system from multi-trajectory input-outputs can be recovered by this approach. Ref. gives a thorough analysis on Hankel nuclear norm regularization applied in system identification, including discussion on proper error metrics, role of rank/system order in formulating the problem, implementable algorithm and selection of tuning parameters.

The rest of the paper is organized as follows. Next section introduces the technical setup. Sections 4 proposes our results on nuclear norm regularization. Section 4.2 discusses the role of the input distribution and establishes lower bounds. Section 5 provides our results on least-squares estimator. Section 6 discusses model selection algorithms. Finally Section 7 presents the numerical experiments^11^1The code for experiments is in https://github.com/sunyue93/sunyue93.github.io/blob/main/sysIdFiles.zip..

## Problem Setup and Algorithms

Let $\parallel \cdot \parallel, \parallel \cdot \parallel_{\ast}, \parallel \cdot \parallel_{F}$ denote the spectral norm, nuclear norm and Frobenius norm respectively. Throughout, we estimate the first ${2n} - 1$ terms of the impulse response denoted by $h$. The system is excited by an input $u$ over the time interval $\lbrack 0,t\rbrack$ and the output $y$ is measured at time $t$, i.e.,

We start by describing data acquisition models. Generally there are several rounds ($i$th round is denoted with super script $(i)$ in Fig. 2) of inputs sent into the system, and the output can be collected or neglected at arbitrary time. In the setting that we refer to as "multi-rollout\" (Fig. 2(b)), for each input signal $u^{(i)}$ we take only one output measurement $y_{t}$ at time $t = {{2n} - 1}$ and then the system is restarted with a new input. Here the *sample complexity* is $T$, the number of output measurements as well as the round of inputs. Recent papers (e.g., and ) use the "single rollout\" model (Fig. 2(c)) where we apply an input signal from time $1$ to ${T + {2n}} - 2$ without restart, and collect all output from time ${2n} - 1$ to ${T + {2n}} - 2$, in total $T$ output measurements; we use this model in the numerical experiments in Sec. 7.

Figure 2: (a) Arbitrary sampling on output data, and two specific data aqcuisition models: (b) multi-rollout, and (c) single rollout.

We consider two estimators in this paper: the *nuclear norm regularized estimator* and the *least squares estimator* defined later.

We will bound the various error metrics mentioned earlier in terms of the sample complexity $T$, the true system order $R$, the dimension of impulse response $n \gg R$, and signal to noise ratio (SNR) defined as $\text{snr} = {{{\mathbb{E}}{\lbrack{{\| u\|}_{F}^{2}/n}\rbrack}}/{{\mathbb{E}}{\lbrack{\| z\|}_{F}^{2}\rbrack}}}$. Table 1 provides a summary and comparison of these bounds. All bounds are order-wise and hide constants and log factors. We can see that, with nuclear norm regularization, our paper matches the least squares impulse response and Hankel spectral error bound while sample complexity can be as small as $\mathcal{O}{(R^{2})}$, and we can recover the impulse response with guaranteed suboptimal error when sample complexity is $\mathcal{O}{(R)}$. Our least square error bound matches the best error bounds among and, which is proven optimal for least squares.

Impulse response error

Hankel spectral error

Table 1: Comparison of recovery error of impulse response. The Hankel matrix is n × n, the system order is R, and the number of samples is T, and $\sigma = {1/\sqrt{\text{snr}}}$ denotes the noise level. LS-IR and LS-Hankel stands for least squares regression on the impulse response and on the Hankel matrix.

Next, we discuss the design of the input signal and introduce *input shaping matrix*.

Input shaping: Note that the $\mathcal{H}$ operator does not preserve the Euclidean norm, so proposes using a normalized operator $\mathcal{G}$, where they first define the weights

and let $K \in {\mathbb{R}}^{{{{({{2n} - 1})}p} \times {({{2n} - 1})}}p}$ be a block diagonal matrix where the $j$th diagonal block of size $p \times p$ is equal to $K_{j}I_{p \times p}$. In other words,

Define the mapping ${\mathcal{G}{(h)}} = {\mathcal{H}{({K^{- 1}h})}}$. In other words, if $\beta = {Kh}$ then ${\mathcal{G}{(\beta)}} = {\mathcal{H}{(h)}}$. Define $\mathcal{G}^{\ast}:{{\mathbb{R}}^{{{mn} \times n}p}\rightarrow{\mathbb{R}}^{{m \times {({{2n} - 1})}}p}}$ as the adjoint of $\mathcal{G}$, where ${\lbrack{\mathcal{G}^{\ast}{(M)}}\rbrack}_{i} = {\sum_{{{j + k} - 1} = i}{M_{{(j)}{(k)}}/K_{i}}}$ if we denote the $j,k$-th block of $M$ (defined in ) by $M_{{(j)}{(k)}}$. Using this change of variable and letting ${\mathbf{U}} = {\overline{\mathbf{U}}K^{- 1}}$, problem (HNN) can be written as

## Hankel Nuclear Norm Regularization

To promote a low-rank Hankel matrix, we add nuclear norm regularization to the quadratic-loss objective and solve the regularized regression problem. Here we give a finite sample analysis for the recovery of the Hankel matrix and the impulse response found via this approach. We consider a random input matrix $\overline{\mathbf{U}}$ and observe the corresponding noisy output vector $y$ as in.

### Statistical guarantees for Hankel-regularization

The theorem below shows that Hankel-regularization achieves near-optimal sample complexity with similarly strong estimation error rates that decay as $1/\sqrt{T}$.

### Theorem 1

Consider the problem (HNN) in the MISO (multi-input single-output) setting ($m = 1$, $p$ input channels). Suppose the system order is $R$, $\overline{\mathbf{U}} \in {\mathbb{R}}^{{T \times {({{2n} - 1})}}p}$, each row consists of an input rollout $u^{(i)} \in {\mathbb{R}}^{{({{2n} - 1})}p}$, and the scaled input $\mathbf{U} = {\overline{\mathbf{U}}K^{- 1}}$ has i.i.d Gaussian entries. Let $\text{snr} = {{{\mathbb{E}}{\lbrack{{\| u\|}^{2}/n}\rbrack}}/{{\mathbb{E}}{\lbrack{\| z\|}^{2}\rbrack}}}$ and $\sigma = {1/\sqrt{\text{snr}}}$. For some constant $C$, let $\lambda = {C\sigma\sqrt{\frac{pn}{T}}{\log{(n)}}}$. Then, with probability $1 - {\mathcal{O}{({R{\log{(n)}}\sqrt{p/T}})}}$, solving (HNN) returns $\hat{h}$ such that^22^2In this theorem, we make the dependence on $\log{(n)}$ explicit.

where $\overline{R} = {\min{({R^{2}{\log^{2}{(n)}}},n)}}$.

Theorem 1 jointly bounds the impulse response and Hankel spectral errors of the system under mild conditions. We highlight the improvements that our bounds provide: When the system is low order, the sample complexity $T$ is logarithmic in $n$ and improves upon the $\mathcal{O}{(n)}$ bound of the least-squares algorithm. The number of samples for recovering an order-$R$ system is $\mathcal{O}{({R{\log{(n)}}})}$, where the SISO case is also proven in, and we follow a similar proof. The error rate with respect to the system parameters $n,R,T$ is same as (e.g. compare to Thm. 3). We can choose $\lambda$ from a range of a constant multiplicative factors, like $\lambda = {{{\lbrack 1,2\rbrack} \cdot C}\sigma\sqrt{\frac{pn}{T}}{\log{(n)}}}$. When $\lambda$ is in this range, there is always a sample complexity $T$ such that holds. The flexibility of $\lambda$ makes tuning $\lambda$ for Algorithm 1 easier.

The regularized method also has the intrinsic advantage that it does not require knowledge of the rank or the singular values of the Hankel matrix beforehand. Tuning method Algorithm 1 and numerical experiments on real data in Sec. 7 demonstrate the performance and robustness of the regularized method.

### Sample complexity lower bounds for IID inputs and the Importance of Input Shape

Theorem 1 uses shaped inputs whereas, in practice, one might expect that i.i.d. input sequence (without shaping matrix $K$) should be sufficient for recovering the impulse response with near-optimal sample size. For instance, proves an optimal sample complexity bound for system identification via least-squares and i.i.d. standard normal inputs. Naturally, we ask: Does Hankel-regularization enjoy similar performance guarantees with i.i.d. inputs? Do we really need input design?

The following theorem proves that for a special system with order $r = 1$, the sample complexity of the problem under i.i.d. input is no less than $n^{1/3}$, compared to $O{({\log n})}$ under the shaped input setting. This is accomplished by carefully lower bounding the Gaussian width induced by the Hankel-regularization. Gaussian width directly corresponds to the square-root of the sample complexity of the problem required for recovery in high probability \[57, Thm. 1\]. Thus, Theorem 2 shows that the sample complexity with i.i.d. input can indeed be provably larger than with shaped input.

### Theorem 2

Suppose the impulse response $h$ of the system is ${h_{t} = 1},{{\forall t} \geq 1}$, which is order $1$. Consider the tangent cone associated with Hankel-regularization (normalized to unit $\ell_{2}$-norm) defined as $\{ x/ \parallel x \parallel | \parallel \mathcal{H}{(h + x)} \parallel_{\ast} \leq \parallel \mathcal{H}{(h)} \parallel_{\ast}\}$. The Gaussian width of this set is lower bounded by $Cn^{1/6}$ for some constant $C > 0$.

This implies that, in the noiseless setting, the sample complexity to recover the impulse response is $T \gtrsim n^{1/3}$, which is larger than $\log n$ dependence with shaped input. This result is rather counter-intuitive since i.i.d. inputs are often optimal for structured parameter estimation tasks (e.g. compressed sensing, low-rank matrix estimation). In contrast, our result shows the provable benefit of input shaping.

## Refined Bounds for the Least-Squares Estimator

To better understand the Hankel-regularization bound of Theorem 1, one can contrast it with the performance of unregularized least-squares. Interestingly, the existing least-squares bounds are not tight when it comes to Hankel spectral norm. In this section, we revisit the least-squares estimator, tighten existing bounds, and contrast the result with our Theorem 1. We consider the MIMO setup where $y \in {\mathbb{R}}^{T \times m}$ and $h \in {\mathbb{R}}^{{{({{2n} - 1})}p} \times m}$. This is obtained by setting $\lambda = 0$ in (HNN), hence the estimator is given via the pseudo-inverse

The next theorem bounds the error when inputs and noise are randomly generated.

### Theorem 3

Denote the solution to as $\hat{h}$. Let $\overline{\mathbf{U}} \in {\mathbb{R}}^{{T \times {({{2n} - 1})}}p}$ be input matrix obtained from multiple rollouts, with i.i.d. standard normal entries, $y \in {\mathbb{R}}^{T \times m}$ be the corresponding outputs and $z \in {\mathbb{R}}^{T \times m}$ be the noise matrix with i.i.d. $\mathcal{N}{(0,\sigma_{z}^{2})}$ entries. Then the spectral norm error obeys ${\|{\mathcal{H}{({\hat{h} - h})}}\|} \lesssim {\sigma_{z}\sqrt{\frac{mnp}{T}}{\log{({np})}}}$ when $T \gtrsim {mnp}$.

This theorem improves the spectral norm bound compared to, which naively bounds the spectral norm in terms of IR error using the right-hand side of. Instead, we show that spectral error is same as the IR error up to a log factor (when there is only output noise). We remark that $O{({\sigma_{z}\sqrt{{np}/T}})}$ is a tight lower bound for $\|{\mathcal{H}{({h - \hat{h}})}}\|$ as well as $\|{h - \hat{h}}\|$. The proof of the theorem above is in Appendix D ‣ System Identification via Nuclear Norm Regularization"). Note that, we apply the i.i.d input here for least squares which is different from regularized algorithm. It works with at least $\mathcal{O}{(n)}$ samples, whereas the sample complexity for the regularized algorithm in Theorem 1 is $\mathcal{O}{(R)}$.

## Model Selection for Hankel-Regularized System ID

In Thm. 1, we established the recovery error for system's impulse response for a particular parameter choice $\lambda$, which depends on the noise level $\sigma$. In practice, we do not know the noise level and the optimal $\lambda$ choice is data-dependent. Thus, given a set of parameter candidates $\Lambda \subset {\mathbb{R}}^{+}$, one can evaluate $\lambda \in \Lambda$ and minimize the validation error to perform model selection. Algorithm 1 summarizes our training and validation procedure where $|\Lambda|$ denotes the cardinality of $\Lambda$. The theorem below states the performance guarantee for this algorithm.

### Theorem 4

Consider the setting of Theorem 1. Sample $T$ i.i.d. training rollouts $(\mathbf{U},y)$ and $T_{\text{val}}$ i.i.d. validation rollouts $(\mathbf{U}_{\text{val}},y_{\text{val}})$. Set $\lambda^{\ast} = {C\sigma\sqrt{\frac{pn}{T}}{\log{(n)}}}$ which is the choice in Thm. 1. Fix failure probability $P \in {}$. Suppose that:

\(a\) There is a candidate $\hat{\lambda} \in \Lambda$ obeying ${\lambda^{\ast}/2} \leq \hat{\lambda} \leq {2\lambda^{\ast}}$.

\(b\) Validation set obeys $T_{\text{val}} \gtrsim \left( \frac{T{\log^{2}{({{|\Lambda|}/P})}}}{R{\log^{2}{(n)}}} \right)^{1/3}$.

Set $\overline{R} = {\min{(R^{2},n)}}$. With probability at least $1 - P$, Algorithm 1 achieves an estimation error equivalent to:

0: T training rollouts: Input features $\overline{\mathbf{U}}$, outputs yT validation rollouts: Input features ${\overline{\mathbf{U}}}_{val}$, outputs yval Hyperparameters: Hankel dimension n, candidate set Λ.
% Train a model for each λ ∈ Λ
Training phase: Solve (HNN). Record the solution ĥλ.
% Return the minimum validation error
Model selection: $\hat{h} = {\underset{{\hat{h}}_{\lambda}:{\lambda\in\Lambda}}{\arg ⁡\min}{\|{{{\overline{\mathbf{U}}}_{val}{\hat{h}}_{\lambda}} - y_{val}}\|}_{2}^{2}}$.
Algorithm 1 Joint System Identification &amp; Model Selection

In a nutshell, this result shows that as long as candidate set contains a reasonable hyperparameter (Condition (a)), using few validation data (Condition (b)), one can compete with the hindsight parameter choice of Theorem 1. $T_{\text{val}}$ mildly depends on $T$ and only scales poly-logarithmically in $|\Lambda|$ which is consistent with the model selection literature.

In Algorithm 1, we fix the size of the Hankel matrix (which is usually large/overparameterized) and tune $\lambda > 0$. In contrast to this, for OLS and the least-squares procedure of, model selection is accomplished by varying the size of the Hankel matrix. The next section provides experiments and contrasts these methods and provides insights on how regularization can improve over least-squares for certain class of dynamical systems.

In Appendix E ‣ System Identification via Nuclear Norm Regularization"), we further compare the model selection methods of Hankel-regularization and least-squares, and argue that, the proposed Algorithm 1 requires less data than tuning the least squares method.

## Experiments and Insights

### Experiments with Synthetic Data

When does regularization beat least-squares? Low-order slow-decay systems (Fig. 3). We use an experiment with synthetic data to answer this question. So far, we showed that for fixed Hankel size, nuclear norm regularization requires less data than unregularized least-squares especially when the Hankel size is set to be large (Table 1). However, for least squares, one can choose to use a *smaller Hankel size* with $n \approx R$, so that we solve a problem of small dimension compared to $n \gg R$. We ask if there is a scenario in which fine-tuned nuclear norm regularization strictly outperforms fine-tuned least-squares.

In what follows, we discuss a single trajectory scenario. An advantage of the Hankel-regularization is that, it addresses scenarios which can benefit from large $n$ while both the sample complexity $T$ and the system order $R$ are small. Given choice of $n$, in a single trajectory setting, least-squares suffers an error of order $\rho{(A)}^{2n}{({1 - {\rho{(A)}^{n}}})}^{- 1}$ (Thm 3.1 of ). This error arises from FIR truncation of impulse response (to $n$ terms) and occurs for both regularized and unregularized algorithms. In essence, due to FIR truncation, the problem effectively incurs an output noise of order $\rho{(A)}^{2n}{({1 - {\rho{(A)}^{n}}})}^{- 1}$. Thus, if the system decays slowly, i.e., ${\rho{(A)}} \approx 1$, we will suffer from significant truncation error.

Figure 3: Synthetic data, single rollout. Order-1 system with pole = 0.98. Recovery by Hankel-regularized algorithm varying λ and least squares varying Hankel size n. Training sample size is 40 and validation sample size is 800. The figures are the training/validation error with Hankel-regularized algorithm, varying λ with n = 45; and least-squares with varying n; Hankel-regularized algorithm, varying λ with n = 20 (small Hankel size). Black line is the best validation error achieved in the first figure.

As an example, suppose sample size is $T = 40$ and ${\rho{(A)}} = 0.98$. If the problem is kept over-determined (i.e. $n < 40$), then $n$ will not be large enough to make the truncation error ${\rho{(A)}^{2n}{({1 - {\rho{(A)}^{n}}})}^{- 1}} \approx 0.36$ vanishingly small. In contrast, Hankel-regularization can intuitively recover such slowly-decaying systems by choosing a large Hankel size $n$ as its sample complexity is (mostly) independent of $n$ (as in the setting of Theorem 1). This motivates us to compare the performance on recovering systems with *low-order slow-decay*. In Fig. 3, we set up an order-$1$ system with a pole at $0.98$ and generate single rollout data with size $40$. We tune $\lambda$ when applying regularized algorithm with $n = 45$ (as it is safe to choose a large Hankel dimension), whereas in unregularized method, Hankel size cannot be larger than $20$ ($n \times n$ Hankel has ${2n} - 1$ parameters and we need least squares to remain overdetermined). With these in mind, in the first two figures we can see that the best validation error of regularization algorithm is $0.44$, which is significantly smaller than the unregularized validation error $0.73$. In the third figure, we use regularized least squares with $n = 20$, which also causes large truncation error (due to large $\rho{(A)}$) compared to the initial choice of $n = 45$ (the first figure). In this case, the best validation error is $0.56$ which is again noticeably worse than the $0.44$ error in the first figure.

When the number of variables ${2n} - 1$ is larger than $T$, the system identification problem is overparameterized and there can be infinitely many impulse responses that achieve zero squared loss on the training dataset. This happens in the first figure when $\lambda\rightarrow 0$, and in the second figure when $n$ is large. In this case, regularized algorithm chooses the solution with the smallest Hankel nuclear norm and the least squares chooses the one with smallest $\ell_{2}$ norm. The first figure has smaller validation error when $1/\lambda$ tends to infinity. We verified that, when regularization weight is $0$, the setup in the first figure achieves validation error $0.58$, which is better than least squares for $n = 45$ with validation error $1.60$. So among the solutions that overfits the training dataset, the one with small Hankel nuclear norm has better generalization performance when the true system is low order.

### Experiments with DaISy Dataset

Our experiment uses the DaISy dataset, where a known input signal (not random) is applied and the resulting noisy output trajectory is measured. Using the input and output matrices

we solve the optimization problem (HNN) using single trajectory data.

While the input model is single instead of multiple rollout, experiments will demonstrate the advantage of Hankel-regularization over least-squares in terms of sample complexity, singular value gap and ease of tuning.

Figure 4: System identification for CD player arm data. Training data size = 200 and validation data size = 600. The first two figures are the training/validation errors of varying λ in Hankel regularized algorithm (n = 10), and training/validation errors of varying Hankel size n in least squares. The last figure is the output trajectory of the true system and the recovered systems (best validation chosen for each).

Figure 5: The first two: CD player arm data, singular values of the Hankel matrix with Hankel regularized algorithm and least squares. The last two: Recovery by Hankel regularized algorithm and least squares when Hankel matrix is 10 × 10. Training data size is 50 and validation data size is 400.

Figure 6: The first two: Stabilized inverted pendulum data, singular values of the Hankel regularized algorithm and least squares. The last two: Recovery by Hankel regularized algorithm and least squares when Hankel matrix is 40 × 40. Training data size is 16 and validation data size is 600.

Large data regime: Both Hankel and least-squares algorithms work well (Fig. 4). The first two figures in Fig. 4 show the training and validation errors of Hankel-regularized and unregularized methods with hyperparameters $\lambda$ and $n$ respectively. We then choose the best system by tuning the hyperparameters to achieve the smallest validation error. The third figure in Fig. 4 plots the training and validation output sequence of the dataset for these algorithms. We see that with sufficient sample size, the system is recovered well. However, the validation error is more flat as a function of $1/\lambda$ (first figure) whereas it is sensitive to the choice of $n$ (second figure), thus $\lambda$ is easier to tune compared to $n$.

Small data regime: Hankel-regularization succeeds while least-squares may fail due to overfitting (Fig. 5). The first two figures in Fig. 5 show that the Hankel spectrums of the two algorithms have a notable difference: The system recovered by Hankel-regularization is low-order and has larger singular value gap. The last two figures in Fig. 5 show the advantage of regularization with much better validation performance. As expected from our theory, the difference is most visible in small sample size (this experiment uses 50 training samples). When the number of observations $T$ is small, Hankel-regularization still returns a solution close to the true system while least-squares cannot recover the system properly.

Learning a linear approximation of a nonlinear system with few data (Fig. 6). Finally, we show that Hankel-regularization can identify a stable nonlinear system via its linearized approximation as well. We consider the inverted pendulum as the experimental environment. First we use a linearized controller to stabilize the system around the equilibrium, and apply single rollout input to the closed-loop system, which is i.i.d. random input of dimension $1$. The dimension of the state is $4$, and we observe the output of dimension $1$, which is the displacement of the system. We then use the Hankel-regularization and least-squares to estimate the closed-loop system with a linear system model and predict the trajectory using the estimated impulse response. We use $T = 16$ observations for training, and set the dimension to $n = 45$. Fig. 6 shows the singular values and estimated trajectory of these two methods. Despite the nonlinearity of the ground-truth system, the regularized algorithm finds a linear model with order $6$ and the predicted output has small error, while the correct order is not visible in the singular value spectrum of the unregularized least-squares.

## Future directions

This paper established new sample complexity and estimation error bounds for system identification. We showed that nuclear norm penalization works well with small sample size regardless of the misspecification of the problem (i.e. fitting impulse response with a much larger length rather than the true order). For least-squares, we provided the first guarantee that is optimal in sample complexity and the Hankel spectral norm error. These results can be refined in several directions. In the proof of Theorem 1, we used a weighted Hankel operator. We expect that directly computing the Gaussian width of the original Hankel operator will also lead to improvements over least-squares. We also hope to extend the results to account for single trajectory analysis and process noise. In both cases, an accurate analysis of the regularized problem will likely lead to new algorithmic insights.
