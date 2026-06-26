<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Non-asymptotic Identification of LTI Systems from a Single Trajectory

Topics include Stability analysis, Kalman filtering, Accuracy, Sample complexity, Learning, LTI.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of learning a realization for a linear time-invariant (LTI) dynamical system from input/output data. Given a single input/output trajectory, we provide finite time analysis for learning the system's Markov parameters, from which a balanced realization is obtained using the classical Ho-Kalman algorithm. By proving a stability result for the Ho-Kalman algorithm and combining it with the sample complexity results for Markov parameters, we show how much data is needed to learn a balanced realization of the system up to a desired accuracy with high probability.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many modern control design techniques rely on the existence of a fairly accurate state-space model of the plant to be controlled. Although in some cases a model can be obtained from first principles, there are many situations in which a model should be learned from input/output data. Classical results in system identification provide asymptotic convergence guarantees for learning models from data. However, finite sample complexity properties have been rarely discussed in system identification literature; and earlier results are conservative.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is recent interest from the machine learning community in data-driven control and non-asymptotic analysis. Putting aside the reinforcement learning literature and restricting our attention to linear state-space models, the work in this area can be divided into two categories: (i) directly learning the control inputs to optimize a control objective or analyzing the predictive power of the learned representation, (ii) learning the parameters of the system model from limited data. For the former problem, the focus has been on exploration/exploitation type formulations and regret analysis. Since the goal is to learn how to control the system to achieve a specific task, the system is not necessarily fully learned. On the other hand, the latter problem aims to learn a general purpose model that can be used in different control tasks, for instance, by combining it with robust control techniques. The focus for the latter work has been to analyze data--accuracy trade-offs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we focus on learning a realization for an LTI system from a single *input/output* trajectory. This setting is significantly more challenging than earlier studies that assume that (multiple independent) *state* trajectories are available. One of our main contributions is to derive sample complexity results in learning the Markov parameters, to be precisely defined later, of the system using a least squares algorithm. Markov parameters play a central role in system identification and they can also be directly used in control design when the system model itself is not available. In Section 4, we show that using few Markov parameter estimates and leveraging stability assumption, one can approximate system's Hankel operator with near optimal sample size. When only input/output data is available, it is well known that the system matrices can be identified only up to a similarity transformation even in the noise-free case but Markov parameters are identifiable. Therefore, we focus on obtaining a realization. One classical technique to derive a realization from the Markov parameters is the Ho-Kalman (a.k.a., eigensystem realization algorithm -- ERA) algorithm.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Ho-Kalman algorithm constructs a balanced realization^22^2Balanced realizations give a representation of the system in a basis that orders the states in terms of their effect on the input/output behavior. This is relevant for determining the system order and for model reduction. for the system from the singular value decomposition of the Hankel matrix of the Markov parameters. By proving a stability result for the Ho-Kalman algorithm and combining it with the sample complexity results, we show how much data is needed to learn a balanced realization of the system up to a desired accuracy with high probability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We first introduce the basic notation. Spectral norm $\parallel \cdot \parallel$ returns the largest singular value of a matrix. Multivariate normal distribution with mean $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ is denoted by $\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}$. ${\mathbf{X}}^{\ast}$ denotes the transpose of a matrix $\mathbf{X}$. ${\mathbf{X}}^{\dagger}$ returns the Moore--Penrose inverse of the matrix $\mathbf{X}$. Covariance matrix of a random vector $\mathbf{v}$ is denoted by $\mathbf{\Sigma}{({\mathbf{v}})}$. $\text{tr}{( \cdot )}$ returns the trace of a matrix. $c,C,c',c_{1},c_{2},\ldots$ stands for absolute constants.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Suppose we have an observable and controllable linear system characterized by the system matrices ${{\mathbf{A}} \in {\mathbb{R}}^{n \times n}},{{{\mathbf{B}} \in {\mathbb{R}}^{n \times p}},{{{\mathbf{C}} \in {\mathbb{R}}^{m \times n}},{{\mathbf{D}} \in {\mathbb{R}}^{m \times p}}}}$ and this system evolves according to Our goal is to learn the characteristics of this system and to provide finite sample bounds on the estimation accuracy. Given a horizon $T$, we will learn the first $T$ Markov parameters of the system.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The first Markov parameter is the matrix $\mathbf{D}$, and the remaining parameters are the set of matrices ${\{{{\mathbf{C}}{\mathbf{A}}^{i}{\mathbf{B}}}\}}_{i = 0}^{T - 2}$. As it will be discussed later, by learning these parameters, we can provide bounds on how well ${\mathbf{y}}_{t}$ can be estimated for a future time $t$, we can identify the state-space matrices ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}},{\mathbf{D}}$ (up to a similarity transformation).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

paper, we believe our proof strategy can be adapted to arbitrary covariance matrices..

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

${\mathbf{u}}_{t}$ is the input vector which is known to us. ${\mathbf{w}}_{t}$ and ${\mathbf{z}}_{t}$ are the process and measurement noise vectors respectively. We also assume that the initial condition of the hidden state is ${\mathbf{x}}_{1} = 0$. Observe that Markov parameters can be found if we have access to cross correlations ${\mathbb{E}}{\lbrack{{\mathbf{y}}_{t}{\mathbf{u}}_{t - k}^{\ast}}\rbrack}$. In particular, we have the identities Hence, if we had access to infinitely many independent $({\mathbf{y}}_{t},{\mathbf{u}}_{t - k})$ pairs, our task could be accomplished by a simple averaging. In this work, we will show that, one can robustly learn these matrices from a small amount of data generated from a single realization of the system trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The challenge is efficiently using finite and dependent data points to perform reliable estimation. Observe that, our problem is identical to learning the concatenated matrix $\mathbf{G}$ defined as Next section describes our input and output data. Based on this, we formulate a least-squares procedure that estimates $\mathbf{G}$. The estimate $\hat{\mathbf{G}}$ will play a critical role in the identification of the system matrices.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Least-Squares Procedure", "weight": 1.0} -->

To describe the estimation procedure, we start by explaining the data collection process. Given a single input/output trajectory ${\{{\mathbf{y}}_{t},{\mathbf{u}}_{t}\}}_{t = 1}^{\overline{N}}$, we generate $N$ subsequences of length $T$, where $\overline{N} = {{T + N} - 1}$ and $N \geq 1$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Least-Squares Procedure", "weight": 1.0} -->

To ease representation, we organize the data ${\mathbf{u}}_{t}$ and the noise ${\mathbf{w}}_{t}$ into length $T$ chunks denoted by the following vectors, In a similar fashion to $\mathbf{G}$ define the matrix, To establish an explicit connection to Markov parameters, ${\mathbf{y}}_{t}$ can be expanded recursively until ${t - T} + 1$ to relate the output to the input ${\overline{\mathbf{u}}}_{t}$ and Markov parameter matrix $\mathbf{G}$ as follows, where, ${\mathbf{e}}_{t} = {{\mathbf{C}}{\mathbf{A}}^{T - 1}{\mathbf{x}}_{{t - T} + 1}}$ corresponds to the error due to the effect of the state at time ${t - T} + 1$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Least-Squares Procedure", "weight": 1.0} -->

Ideally, we would like the estimation error ${\|{{\mathbf{G}} - \hat{\mathbf{G}}}\|}_{F}^{2}$ to be small. Our main result bounds the norm of the error as a function of the sample size $N$ and noise levels $\sigma_{w}$ and $\sigma_{z}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Results on Learning Markov Parameters", "weight": 1.0} -->

Let $\rho{(\cdot)}$ denote the spectral radius of a matrix which is the largest absolute value of its eigenvalues. Our results in this section apply to stable systems where ${\rho{({\mathbf{A}})}} < 1$. Additionally we need a related quantity involving $\mathbf{A}$ which is the spectral norm to spectral radius ratio of its exponents defined as ${\Phi{({\mathbf{A}})}} = {\sup_{\tau \geq 0}\frac{\|{\mathbf{A}}^{\tau}\|}{\rho{({\mathbf{A}})}^{\tau}}}$. We will assume ${\Phi{({\mathbf{A}})}} < \infty$ which is a mild condition: For instance, if $\mathbf{A}$ is diagonalizable, $\Phi{({\mathbf{A}})}$ is a function of its eigenvector matrix and is finite.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Results on Learning Markov Parameters", "weight": 1.0} -->

Another important parameter is the steady state covariance matrix of ${\mathbf{x}}_{t}$ which is given by It is rather trivial to show that for all $t \geq 1$, ${\mathbf{\Sigma}{({\mathbf{x}}_{t})}} \preceq \mathbf{\Gamma}_{\infty}$. We will use $\mathbf{\Gamma}_{\infty}$ to bound the error ${\mathbf{e}}_{t}$ due to the unknown state at time ${t - T} + 1$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results on Learning Markov Parameters", "weight": 1.0} -->

We characterize the impact of ${\mathbf{e}}_{t}$ by its "effective standard deviation" $\sigma_{e}$ that is obtained by scaling the bound on $\sqrt{\|{\mathbf{\Sigma}{({\mathbf{e}}_{t})}}\|}$ by an additional factor $\Phi{({\mathbf{A}})}\sqrt{T/{({1 - {\rho{({\mathbf{A}})}^{2T}}})}}$ which yields, Our first result is a simplified version of Theorem 3.2 and captures the problem dependencies in terms of the total standard deviations $\sigma_{z} + \sigma_{e} + {\sigma_{w}{\|{\mathbf{F}}\|}}$ and the total dimensions $m + p + n$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Estimating the Output via Markov Parameters", "weight": 1.0} -->

The following lemma illustrates how learning Markov parameters helps us bound the prediction error.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Markov Parameters to Hankel Matrix: Low Order Approximation of Stable Systems", "weight": 1.0} -->

So far our attention has focused on estimating the impulse response $\mathbf{G}$ for a particular horizon $T$. Clearly, we are also interested in understanding how well we learn the overall behavior of the system by learning a finite impulse approximation. In this section, we will apply our earlier results to approximate the overall system by using as few samples as possible. A useful idea towards this goal is taking advantage of the stability of the system. The Markov parameters decay exponentially fast if the system is stable i.e. ${\rho{({\mathbf{A}})}} < 1$. This means that, most of the Markov parameters will be very small after a while and not learning them might not be a big loss for learning the overall behavior. In particular, $\tau$'th Markov parameter obeys This implies that, the impact of the impulse response terms we don't learn can be upper bounded. For instance, the total spectral norm of the tail terms obey To proceed fix a finite horizon $K$ that will later be allowed to go infinity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Markov Parameters to Hankel Matrix: Low Order Approximation of Stable Systems", "weight": 1.0} -->

Represent the estimate $\hat{\mathbf{G}}$ as $\lbrack\hat{\mathbf{D}},{\hat{\mathbf{G}}}_{0},{\ldots{\hat{\mathbf{G}}}_{T - 2}}\rbrack$ where ${\hat{\mathbf{G}}}_{i}$ corresponds to the noisy estimate of ${\mathbf{C}}{\mathbf{A}}^{i}{\mathbf{B}}$. Now, let us consider the estimated and true order $K$ Markov parameters Similarly we define the associated $K \times K$ block Hankel matrices of size ${{mK} \times p}K$ as follows The following theorem merges results of this section with a specific choice of $T$ to give approximation bounds for the infinite Markov operator ${\mathbf{G}}^{(\infty)}$ and Hankel operator ${\mathbf{H}}^{(\infty)}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Markov Parameters to Hankel Matrix: Low Order Approximation of Stable Systems", "weight": 1.0} -->

For notational simplicity, we shall assume that there is no process noise.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Non-Asymptotic System Identification via Ho-Kalman", "weight": 1.0} -->

In this section, we first describe the Ho-Kalman algorithm that generates ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}},{\mathbf{D}}$ from the Markov parameter matrix $\mathbf{G}$. We also show that the algorithm is stable to perturbations in $\mathbf{G}$ and the output of Ho-Kalman gracefully degrades as a function of $\|{{\mathbf{G}} - \hat{\mathbf{G}}}\|$. Combining this with Theorem 3.1 implies guaranteed non-asymptotic identification of multi-input-multi-output systems from a single trajectory. We remark that results of this section do not assume stability and applies to arbitrary, possibly unstable, systems. We will use the following Hankel matrix definition to introduce the algorithms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "System Identification Algorithm", "weight": 1.0} -->

Given a noisy estimate $\hat{\mathbf{G}}$ of $\mathbf{G}$, we wish to learn good system matrices $\hat{\mathbf{A}},\hat{\mathbf{B}},\hat{\mathbf{C}},\hat{\mathbf{D}}$ from $\hat{\mathbf{G}}$ up to trivial ambiguities. This will be achieved by using Algorithm 1 which admits the matrix $\hat{\mathbf{G}}$, system order $n$ and Hankel dimensions $T_{1},T_{2}$ as inputs. Throughout this section, we make the following two assumptions to ensure that the system we wish to learn is order-$n$ and our system identification problem is well-conditioned. the system is observable and controllable; hence $n > 0$ is the order of the system.

<!-- chunk {"id": "body-0025", "role": "body", "section": "System Identification Algorithm", "weight": 1.0} -->

$(T_{1},T_{2})$ Hankel matrix ${\mathbf{H}}{({\mathbf{G}})}$ formed from $\mathbf{G}$ is rank-$n$. This can be ensured by choosing sufficiently large $T_{1},T_{2}$. In particular ${T_{1} \geq n},{T_{2} \geq n}$ is guaranteed to work by the first assumption above.

<!-- chunk {"id": "body-0026", "role": "body", "section": "System Identification Algorithm", "weight": 1.0} -->

This procedure (Ho-Kalman) returns the true balanced realization of the system when Markov parameters are known i.e. $\hat{\mathbf{G}} = {\mathbf{G}}$. Our goal is to show that even with noisy Markov parameters, this procedure returns good estimates of the true balanced realization. We remark that there are variations of this procedure; however the core idea is the same and they are equivalent when the true Markov parameters are used as input. For instance, when constructing $\hat{\mathbf{H}}$, one can attempt to improve the noise robustness of the algorithm by picking balanced dimensions ${mT_{1}} \approx {pT_{2}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We considered a MIMO (multiple input, multiple output) system with $m = 2$ sensors, $n = 5$ hidden states and input dimension $p = 3$. To assess the typical performance of the least-squares and the Ho-Kalman algorithms, we consider random state-spaces as follows. We generate ${\mathbf{C}},{\mathbf{D}}$ with independent $\mathcal{N}{(0,{1/m})}$ entries. We generate $\mathbf{B}$ with independent $\mathcal{N}{(0,{1/n})}$ entries.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The most critical component of an LTI system is the $\mathbf{A}$ matrix. We picked $\mathbf{A}$ to be a diagonal matrix with its $n$ eigenvalues (i.e. diagonal entries) are generated to be uniform random variables between $\lbrack 0,0.9\rbrack$. The upper bound $0.9$ implies that we are working with stable matrices and the effect of unknown state vanishes for large $T$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Finally, we conduct experiments for different $T$ values of $T \in {\{ 6,12,18\}}$. During Ho-Kalman procedure, we create a Hankel matrix $\hat{\mathbf{H}}$ of size ${{{{mT}/2} \times p}T}/2$ and apply Algorithm 1. Due to random generation of problem data, even for $T = 6$, the ground truth Hankel matrix ${\mathbf{H}}^{-} \in {\mathbb{R}}^{6 \times 6}$ has rank $n = 5$ so that Ho-Kalman procedure can indeed learn a good realization.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In our experimental setup, we pick a hyperparameter configuration of $T,\sigma_{w},\sigma_{z}$ and generate a single rollout of the system until some time $t_{\infty}$. For each $T \leq \overline{N} \leq t_{\infty}$, we solve the system via (2.7) to obtain the estimate of $\mathbf{G}$ and use Algorithm 1 to obtain a state-space realization $\hat{\mathbf{A}},\hat{\mathbf{B}},\hat{\mathbf{C}},\hat{\mathbf{D}}$. The $x$-axis displays $N$ (which is the amount of available data at time $t = \overline{N}$) and the $y$-axis displays the estimation error. Each curve in the figures is generated by averaging the outcomes of $20$ independent realizations of single trajectories.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 1, we considered the problem of estimating the matrices ${\mathbf{D}},{{\mathbf{C}}{\mathbf{B}}},{\mathbf{G}},{\mathbf{H}}$ when $T = 18$. ${\mathbf{D}},{{\mathbf{C}}{\mathbf{B}}}$ are the first two impulse responses. Estimating $\mathbf{G}$ and the associated Hankel matrix $\mathbf{H}$ helps verify our findings in Theorem 3.2. We plotted curves for varying noise levels $\sigma_{w} = \sigma_{z} \in {\{ 0,{1/4},{1/2},1\}}$. The main conclusion is that indeed estimation accuracy drastically improves as we observe the system for a longer period of time and collect more data. Note that estimation errors on $\mathbf{D}$ and ${\mathbf{C}}{\mathbf{B}}$ are in the same ballpark.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

These are submatrices of $\mathbf{G}$ hence their associated spectral norm errors are strictly lower compared to $\|{{\mathbf{G}} - \hat{\mathbf{G}}}\|$. Per Definition 5.1 ‣ 5 Non-Asymptotic System Identification via Ho-Kalman ‣ Non-asymptotic Identification of LTI Systems from a Single Trajectory"), $\mathbf{H}$ is constructed from the blocks of $\mathbf{G}$ and its spectral norm error is in lines with $\mathbf{G}$. The other observation is that estimation error decays gracefully as a function of the noise levels for all matrices of interest. Since we picked a large $T$, the error due to unknown initial conditions (i.e. ${\mathbf{e}}_{t}$) is fairly negligible. Hence when $\sigma_{w} = \sigma_{z} = 0$, we quickly achieve near $0$ estimation error as the impact of the ${\mathbf{e}}_{t}$ term is also small.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure 2 we study the stability of the Ho-Kalman procedure which returns a realization up to a unitary transformation as described in Theorem 5.3. Hence, rather than focusing on individual outputs $\hat{\mathbf{A}},\hat{\mathbf{B}},\hat{\mathbf{C}}$ we directly study the LTI systems $\mathcal{S} = {\text{LTI-sys}{({\mathbf{A}},{\mathbf{B}},{\mathbf{C}},{\mathbf{D}})}}$ and $\hat{\mathcal{S}} = {\text{LTI-sys}{(\hat{\mathbf{A}},\hat{\mathbf{B}},\hat{\mathbf{C}},\hat{\mathbf{D}})}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In particular, we focus on the $\mathcal{H}_{\infty}$ norm of the error $\mathcal{S} - \hat{\mathcal{S}}$. During this process, we clipped the singular values of $\hat{\mathbf{A}}$ at $0.99$ i.e. if $\hat{\mathbf{A}}$ has a singular value larger than $0.99$, we replace it by $0.99$ in the SVD of $\hat{\mathbf{A}}$ which returns a new $\hat{\mathbf{A}}$ whose singular vectors are same but singular values are clipped. This essentially corresponds to projecting the estimated system on the set of stable systems. While we verified that ${\|\hat{\mathbf{A}}\|} > 0.99$ rarely happens for large $N$, clipping ensures that $\mathcal{H}_{\infty}$ norm is always bounded and smooths out the results.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Figure 2 illustrates the normalized $\mathcal{H}_{\infty}$ error $\frac{{\|{\hat{\mathcal{S}} - \mathcal{S}}\|}_{\mathcal{H}_{\infty}}}{{\|\mathcal{S}\|}_{\mathcal{H}_{\infty}}}$ for varying $\sigma_{w} = \sigma_{z}$ and $T \in {\{ 6,12,18\}}$. For zero-noise regime, $T = 18$ outperforms the rest demonstrating the benefit of using a larger $T$ to overcome the contribution of the $\sigma_{e}$ term. In the other regimes, all $T$ choices perform fairly similar; however $T = 6$ appears to suffer less from increasing noise levels $\sigma_{w},\sigma_{z}$. Another observation is that for very small sample size $N$, $T = 6$ converges faster than the others.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This is supported by our Theorem 3.2 as $T = 6$ has less unknowns and the minimal $N$ is in the order of $Tp$, hence smaller $T$ means faster estimation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We remark that one might be interested in other metrics to assess the error such as Frobenius norm. While not shown in the figures, we also verified that the Frobenius norm ${\|{{\mathbf{G}} - \hat{\mathbf{G}}}\|}_{F}$ (and the errors for ${{\mathbf{C}}{\mathbf{B}}},{\mathbf{D}},{\mathbf{H}}$ as well as ${\|{\mathcal{S} - \hat{\mathcal{S}}}\|}_{\mathcal{H}_{2}}$) behaves in a similar fashion to spectral norm and $\mathcal{H}_{\infty}$ norm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we analyzed the sample complexity of linear system identification from input/output data. Our analysis neither requires multiple independent trajectories nor relies on splitting the trajectory into non-overlapping intervals, therefore makes very efficient use of the available data from a single trajectory. More crucially, it does not rely on state measurements and works with only the inputs and outputs. Based on this analysis, we showed that one can approximate system's Hankel operator using near optimal amount of samples and shed light on the stability of finding a balanced realization.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusions", "weight": 1.0} -->

There are many directions for future work. First, we are interested in combining our results with control synthesis techniques based on Markov parameters. Second, it is shown empirically that minimizing the rank or nuclear norm of the estimated Hankel matrix as a denoising step (see e.g., ) works better than Ho-Kalman. It is of interest to analyze the stability of such optimization-based algorithms. Finally, it would be interesting to see what type of recovery guarantees can be obtained if additional constraints, such as subspace constraints, on the system matrices are known.
