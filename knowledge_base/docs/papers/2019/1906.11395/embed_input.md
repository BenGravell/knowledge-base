<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Tutorial on Concentration Bounds for System Identification

Topics include System identification, Learning, State space.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide a brief tutorial on the use of concentration inequalities as they apply to system identification of state-space parameters of linear time invariant systems, with a focus on the fully observed setting. We draw upon tools from the theories of large-deviations and self-normalized martingales, and provide both data-dependent and independent bounds on the learning rate.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key feature in modern reinforcement learning is the ability to provide high-probability guarantees on the finite-data/time behavior of an algorithm acting on a system. The enabling technical tools used in providing such guarantees are concentration of measure results, which should be interpreted as quantitative versions of the strong law of large numbers. This paper provides a brief introduction to such tools, as motivated by the identification of linear-time-invariant (LTI) systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we focus on the identifying the parameters $(A,B)$ of the LTI system

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

assuming *perfect* state measurements. This is in some sense the simplest possible system identification problem, making it the perfect case study for such a tutorial. Our companion paper shows how the results derived in this paper can then be integrated into self-tuning and adaptive control policies with finite-data guarantees. We also refer the reader to Section II of for an in-depth and comprehensive literature review of classical and contemporary results in system identification. Finally, we note that most of the results we present below are not the sharpest available in the literature, but are rather chosen for the pedagogical value.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is structured as follows: in Section II, we study the simplified setting when system is defined for a scalar state $x$, and data is drawn from independent experiments. Section III extends these ideas to the vector valued settings. In Section IV we study the performance of an estimator using all data from a single trajectory -- this is significantly more challenging as all covariates are strongly correlated. Finally, in Section V, we provide data-dependent bounds that can be used in practical algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Scalar Random Variables", "weight": 1.0} -->

Consider the scalar dynamical system

<!-- chunk {"id": "body-0008", "role": "body", "section": "Scalar Random Variables", "weight": 1.0} -->

for $w_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,\sigma_{w}^{2})}}$, and $a \in {\mathbb{R}}$ an unknown parameter. Our goal is to estimate $a$, and to do so we inject excitatory Gaussian noise via $u_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,\sigma_{u}^{2})}}$. We run $N$ experiments over a horizon of $T + 1$ time-steps, and then solve for our estimate $\hat{a}$ via the least-squares problem

<!-- chunk {"id": "body-0009", "role": "body", "section": "Scalar Random Variables", "weight": 1.0} -->

Notice that we are using only the last two data-points from each trial -- this simplifies the analysis of the error term $e_{N}$ greatly as each of the summands in the numerator and denominator are now i.i.d. random variables. Our goal is to provide high-probability bounds on this error term, and return to the single trajectory estimator later in the paper.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-1 Bounded Random Variables", "weight": 1.0} -->

To build some intuition we begin by studying the behavior of almost surely (a.s.) bounded random variables. In particular, let ${\{ X_{i}\}}_{i = 1}^{N}$ be drawn i.i.d. from a distribution $p$, and let $X_{i} \in {\lbrack a,b\rbrack}$ a.s. for all $i$. Our goal is to quantify, with high-probability, the gap between the empirical and true means, i.e., to find a bound on

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-1 Bounded Random Variables", "weight": 1.0} -->

When working with bounded random variables *McDiarmid's inequality* is a very powerful tool for establishing concentration of measure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 1 (Probability Estimation)", "weight": 1.0} -->

and notice that ${{\mathbb{E}}{\hat{P}}_{N}} = {{\mathbb{P}}\left\lbrack {x \in \Omega} \right\rbrack}$. As $\mathbb{1}_{{\mathbb{x}} \in \mathbb{\Omega}} \in {\{\mathbb{0},\mathbb{1}\}}$ for all $x$, it follows by equation (7. ‣ II-1 Bounded Random Variables ‣ II Scalar Random Variables ‣ A Tutorial on Concentration Bounds for System Identification")) that

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1 (Probability Estimation)", "weight": 1.0} -->

We can obtain a similar bound on the probability of the event $\left\{ {{{\hat{P}}_{N} - {{\mathbb{P}}\left\lbrack {x \in \Omega} \right\rbrack}} \leq {- t}} \right\}$ occurring: it then follows by union bounding over these two events that

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1 (Probability Estimation)", "weight": 1.0} -->

Thus we have seen that in the case of a.s. bounded random variables, concentration of measure does indeed occur. We will now see that similar concentration occurs for random variables drawn from distributions with sufficiently rapidly decaying tails.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-2 Sub-Gaussian Random Variables", "weight": 1.0} -->

We begin by recalling the Chernoff bound, which states that for a random variable $X$ with mean ${\mathbb{E}}X$, and moment generating function (MGF) ${\mathbb{E}}\left\lbrack e^{\lambda{({X - {{\mathbb{E}}X}})}} \right\rbrack$ defined for all ${|\lambda|} \leq b$, it holds that

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-2 Sub-Gaussian Random Variables", "weight": 1.0} -->

We now turn our attention to Gaussian random variables, and recall that for $X \sim {\mathcal{N}{(\mu,\sigma^{2})}}$, we have that ${{\mathbb{E}}\left\lbrack e^{\lambda{({X - \mu})}} \right\rbrack} = {\exp\left( \frac{\sigma^{2}\lambda^{2}}{2} \right)}$ for all $\lambda \in {\mathbb{R}}$. Substituting this into the Chernoff bound and solving for $\lambda^{\star} = {t/\sigma^{2}}$, we immediately obtain

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-2 Sub-Gaussian Random Variables", "weight": 1.0} -->

Once again, a similar bound can be obtained on the probability of event $\left\{ {{{\frac{1}{N}{\sum_{i = 1}^{N}X_{i}}} - \mu} \leq {- t}} \right\}$ occurring: it then follows by union bounding over these two events that

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-2 Sub-Gaussian Random Variables", "weight": 1.0} -->

We now generalize these results to random variables with MGFs dominated by that of a Gaussian random variable.

<!-- chunk {"id": "body-0019", "role": "body", "section": "An aside on probability inversion and two sided bounds", "weight": 1.0} -->

Rather than statements about the probability of large deviations, as in bound (14. ‣ II-2 Sub-Gaussian Random Variables ‣ II Scalar Random Variables ‣ A Tutorial on Concentration Bounds for System Identification")), we are often interested in the probability that a random variable concentrates near its mean. To do so, we employ probability inversion: if we are willing to tolerate a large deviation occurring with probability at most $\delta$, one may invert bound (14. ‣ II-2 Sub-Gaussian Random Variables ‣ II Scalar Random Variables ‣ A Tutorial on Concentration Bounds for System Identification")) by setting $\delta =$ RHS of (14. ‣ II-2 Sub-Gaussian Random Variables ‣ II Scalar Random Variables ‣ A Tutorial on Concentration Bounds for System Identification")) and solving for $t$. This allows us to certify that with probability at least $1 - \delta$ that

<!-- chunk {"id": "body-0020", "role": "body", "section": "An aside on probability inversion and two sided bounds", "weight": 1.0} -->

Applying the same reasoning to the event $\{{{X - {{\mathbb{E}}X}} \leq {- t}}\}$ yields a similar bound, from which it follows, by the union bound, that with probability at least $1 - {2\delta}$ that

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-3 Sub-Exponential Random Variables", "weight": 1.0} -->

Revisiting the error term defined, we see that we still do not have the requisite tools to perform the desired analysis.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 2 (Products of Gaussians are not Sub-Gaussian)", "weight": 1.0} -->

Motivated by the error term, we compute the MGFs for $X^{2}$ and $XW$, where ${X,W}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{}}$. Direct computation of the resulting integrals show that

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 2 (Products of Gaussians are not Sub-Gaussian)", "weight": 1.0} -->

These random variables are clearly not sub-Gaussian, as their MGFs do not exist for all $\lambda \in {\mathbb{R}}$. However, notice that they can be bounded by the MGF of a Gaussian random variable in a neighborhood of the origin. In particular we have that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 2 (Products of Gaussians are not Sub-Gaussian)", "weight": 1.0} -->

The first inequality follows from some calculus, and the second by leveraging that ${- {\log{({1 - x})}}} \leq {x{({1 - x})}^{- 1}}$ for $0 \leq x < 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2 (Products of Gaussians are not Sub-Gaussian)", "weight": 1.0} -->

We now show that MGFs exhibiting behavior as above also concentrate.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

Consider a linear dynamical system described by

<!-- chunk {"id": "body-0027", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

where one can easily verify that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

the $T$-time-step controllability Gramian of $(A,B)$. To lighten notation we let $\Sigma_{x}$ denote the $$ block of the above covariance, i.e.,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

Our objective is to derive high-probability bounds on the spectral norm of the error terms

<!-- chunk {"id": "body-0030", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

reducing our task to finding (i) an upper bound on the norm of the cross term $\sum_{i}{y_{i}w_{i}^{\top}}$, and (ii) a lower bound on the minimum eigenvalue of the empirical Gramian matrix $\sum_{i}{y_{i}y_{i}^{\top}}$. These can be obtained using tail bounds for sub-gaussian and sub-exponential random variables, as formalized in the following propositions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

We begin our analysis by fixing a ${(u,v)} \in {\mathcal{S}^{n - 1} \times \mathcal{S}^{m - 1}}$, and notice that each $({u^{\top}x_{i}})$ and $({w_{i}^{\top}v})$ are sub-Gaussian random variables with parameter $\sigma^{2} = 1$ if the components $x_{i,j}$, $j = {1,\ldots,n}$, and $w_{i,k}$, $k = {1,\ldots,m}$, are themselves sub-Gaussian random variables with parameters $\sigma^{2} = 1$. From Example 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

‣ II-3 Sub-Exponential Random Variables ‣ II Scalar Random Variables ‣ A Tutorial on Concentration Bounds for System Identification"), we conclude that ${({u^{\top}x_{i}})}{({w_{i}^{\top}v})}$ is a zero-mean sub-exponential random variabled with parameters $(2,\sqrt{2})$. It then follows immediately from a one-sided version of Proposition 23, that for a fixed ${(u,v)} \in {\mathcal{S}^{n - 1} \times \mathcal{S}^{m - 1}}$, if $N \geq {\frac{1}{2}{\log{({1/\delta})}}}$, then with probability at least $1 - \delta$, that

<!-- chunk {"id": "body-0033", "role": "body", "section": "Vector Valued Random Variables", "weight": 1.0} -->

We now use this observation in conjunction with a *covering argument* to bound ${\parallel M\parallel}_{2}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Single Trajectory Results", "weight": 1.0} -->

The previous sections made a very strong simplifying assumption: that all of the covariates used in the system-identification step were independent. To satisfy this assumption, we needed several independent trajectories, from which we only used two-data points. This is both impractical and data-inefficient -- however, analyzing single trajectory estimators is much more challenging, and is a current active area of research. This section aims to provide the reader with a survey of some of the tools being used to extend the ideas discussed above to the single-trajectory setting.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-1 Linear Response", "weight": 1.0} -->

In this section we study single trajectory results for LTI systems. We will frame the problem in a more general setting from and specialize the results to LTI systems. Suppose that ${\{ z_{t}\}} \subseteq {\mathbb{R}}^{n}$ is a stochastic process.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-1 Linear Response", "weight": 1.0} -->

Notice that covers the case of an autonomous LTI system $x_{t + 1} = {{Ax_{t}} + w_{t}}$ where we want to learn the parameter $A$ by setting $y_{t} = x_{t + 1}$. It also covers the case of a controlled LTI system $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + w_{t}}$ where we want to learn $\Theta = \begin{bmatrix}
\end{bmatrix}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-1 Linear Response", "weight": 1.0} -->

The term appearing in the numerator of is a *self-normalized martingale* (see e.g. ). On the other hand, the term appearing in the denominator of is the minimum eigenvalue of the empirical covariance matrix. The analysis of proceeds by upper bounding the martingale term and lower bounding the minimum eigenvalue. We note that the martingale term can be handled with the self-normalized inequality from Theorem 1 of Abbasi-Yadkori et al. (see Theorem V.3. ‣ Single trajectory bounds ‣ V Data-Dependent Bounds and the Bootstrap ‣ A Tutorial on Concentration Bounds for System Identification") below). We will focus on controlling the minimum eigenvalue.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-1 Linear Response", "weight": 1.0} -->

Before we present (a simplified version of) the technique used in Simchowitz et al., we discuss a first attempt at controlling the minimum eigenvalue. One could in principle leverage the results of the previous subsection by appealing to mixing time arguments (see e.g. ) which allow us to treat the process $\{ z_{t}\}$ as nearly independent across time by arguing that long term dependencies do not matter. However, such arguments yield bounds that degrade as the system mixes slower. For the LTI case, this leads to bounds that degrade as the spectral radius of $A$ approaches one (and is not applicable to unstable $A$). Instead, we will present the small-ball style of argument used in Simchowitz et al..

<!-- chunk {"id": "body-0039", "role": "body", "section": "Case $A$ is marginally stable", "weight": 1.0} -->

This case is more delicate. It is possible to give a general rate that depends on various properties of the Jordan blocks of $A$, as is done in Corollary A.2 of. Here, we present a special case when $A$ is an orthogonal matrix In this case, $\Gamma_{t} = {{\sigma_{w}^{2}t} \cdot I}$. Hence if we set $k = T/{(n\log{(n/\delta)}}$, then if $T \gtrsim {n{\log{({n/\delta})}}}$, we have that ${\parallel{\hat{A} - A}\parallel} \lesssim \frac{n{\log{({n/\delta})}}}{T}$. Observe that the rate in this case is actually the faster $O{({1/T})}$ rate instead of $O{({1/\sqrt{T}})}$ when $A$ is strictly stable.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data-Dependent Bounds and the Bootstrap", "weight": 1.0} -->

The previous results characterize upper bounds on the rates of convergence of ordinary least-squares based estimates of system parameters. Although informative from a theoretical perspective, they cannot be used to implement control algorithms as they depend on properties of the true underlying system. In this section, we present two data-dependent approaches to computing error estimates.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data-Dependent Bounds and the Bootstrap", "weight": 1.0} -->

We begin with the multiple-trajectory independent data setting. The following proposition from provides refined confidence sets on the estimates $(\hat{A},\hat{B})$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Single trajectory bounds", "weight": 1.0} -->

To derive similar data-dependent bounds for the single-trajectory setting, we exploit the decomposition and find a data-dependent bound to the self-normalized martingale term

<!-- chunk {"id": "body-0043", "role": "body", "section": "Single trajectory bounds", "weight": 1.0} -->

where for convenience, we use the transpose of the previously defined expressions. To do so, we need the following result.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Bootstrap", "weight": 1.0} -->

The Bootstrap is a technique used to estimate population statistics (such as confidence intervals) by sampling from synthetic data generated from empirical estimates of the underlying distribution. Algorithm 1,^11^1We assume that $\sigma_{u}$ and $\sigma_{w}$ are known. Otherwise they can be estimated from data., as suggested, can be used to estimate the error bounds $\epsilon_{A}:={\parallel{\hat{A} - A}\parallel}_{2}$ and $\epsilon_{B}:={\parallel{\hat{B} - B}\parallel}_{2}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Bootstrap", "weight": 1.0} -->

For $\epsilon_{A}$ and $\epsilon_{B}$ estimated by Algorithm 1 we intuitively have

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Bootstrap", "weight": 1.0} -->

Although we do not do so here, these results can be formalized: for more details see texts by Van Der Vaart and Wellner, Shao and Tu, and Hall.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 3 (Data-driven bounds)", "weight": 1.0} -->

Consider the discrete-time double integrator system

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 3 (Data-driven bounds)", "weight": 1.0} -->

driven by noise process $w_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{w}^{2}I_{2}})}}$ and exploratory input $u_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,\sigma_{u}^{2})}}$, with $\sigma_{w} = 0.1$ and $\sigma_{u} = 1$. Figure 1. ‣ The Bootstrap ‣ V Data-Dependent Bounds and the Bootstrap ‣ A Tutorial on Concentration Bounds for System Identification") illustrates the resulting error and bound trajectories.

<!-- chunk {"id": "body-0049", "role": "body", "section": "conclusion", "weight": 1.5} -->

In this paper, we provided a brief introduction to tools useful for the finite-time analysis of system identification algorithms. We studied the full information setting, and showed how concentration of measure of sub-Gaussian and sub-exponential random variables are sufficient to analyze the independent trajectory estimator. We further showed that the analysis becomes much more challenging in the single-trajectory setting, but that tools from self-normalized martingale theory and small-ball probability are useful in this context. Finally, we provided computable data-dependent bounds that can be used in practical algorithms. In our companion paper, we show how these tools can be used to design and analyze self-tuning and adaptive control methods with finite-data guarantees. Although we focused on the full information setting, we note that many of the techniques described extend naturally to the partially observed setting.
