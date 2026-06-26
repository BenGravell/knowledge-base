<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Tutorial on the Non-Asymptotic Theory of System Identification

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This tutorial serves as an introduction to recently developed non-asymptotic methods in the theory of - mainly linear - system identification. We emphasize tools we deem particularly useful for a range of problems in this domain, such as the covering technique, the Hanson-Wright Inequality and the method of self-normalized martingales. We then employ these tools to give streamlined proofs of the performance of various least-squares based estimators for identifying the parameters in autoregressive models. We conclude by sketching out how the ideas presented herein can be extended to certain nonlinear identification problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning methods are at an ever increasing pace being integrated into domains that have classically been within the purview of controls. There is a wide range of examples, including perception-based control, agile robotics, and autonomous driving and racing. As exciting as these developments may be, they have been most pronounced on the experimental and empirical sides. To deploy these systems safely, stably, and robustly into the real world, we argue that a principled and integrated theoretical understanding of a) fundamental limitations and b) statistical optimality is needed. Under the past few years, a host of new techniques have been introduced to our field. Unfortunately, existing results in this area are relatively inaccessible to a typical first or second year graduate student in control theory, as they require both sophisticated mathematical tools not typically included in a control theorist's training (e.g., high-dimensional statistics and learning theory).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This tutorial seeks to provide a streamlined exposition of some of these recent advances that are most relevant to the non-asymptotic theory of linear system identification. Our aim is not to be encyclopedic but rather to give simple proofs of the main developments and to highlight and collect the key technical tools to arrive at these results. For a broader---and less technical---overview of the literature we point the reader to our recent survey. It is also worth to point out that the classical literature on system identification has done a formidable job at---often very accurately---characterizing the asymptotic performance of identification algorithms. Our aim is not to supplant this literature but rather to complement the asymptotic picture with finite sample guarantees by relaying recently developed technical tools drawn from high-dimensional probability, statistics and learning theory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let us now fix ideas. We are concerned with linear time-series models of the form: where $Y_{1:T}$ is a sequence of outputs (or targets) assuming values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$ and $X_{1:T}$ is a sequence of inputs (or covariates) assuming values in ${\mathbb{R}}^{d_{\mathsf{X}}}$. The goal of the user (or learner) is to recover the a priori unknown linear map $\theta^{\star} \in {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ using only the observations $X_{1:T}$ and $Y_{1:T}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The linear relationship in the regression model (1.1) is perturbed by a stochastic noise sequence $V_{1:T}$ assuming values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$. We refer to the regression model (1.1) as a time-series to emphasize the fact that the observations $X_{1:T}$ and $Y_{1:T}$ may arrive sequentially and in particular that past $X_{t}$ and $Y_{t}$ may influence future $X_{t'}$ and $Y_{t'}$ (i.e. with $t' > t)$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Example: Autoregressive Models", "weight": 1.0} -->

For instance, a model class of particular interest to us which is subsumed by (1.1) are the (vector) autoregressive exogenous models of order $p$ and $q$ (briefly ARX$(p,q)$): where typically $U_{1:{T - 1}}$ is a sequence of user specified inputs taking values in ${\mathbb{R}}^{d_{\mathsf{U}}}$ and $W_{1:T}$ is an iid sequence of noise variables taking values in ${\mathbb{R}}^{d_{\mathsf{W}}}$. If we are only interested in the parameters $\begin{bmatrix} \end{bmatrix}$, we obtain the model (1.2) by setting We point out that that the above discussion presupposes that the order of the model, $(p,q)$, is known (there are ways around this).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Example: Autoregressive Models", "weight": 1.0} -->

In this tutorial we will provide the necessary tools to tackle the following problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem 1.1", "weight": 1.0} -->

Fix $\varepsilon > 0$, $\delta \in {}$, and a norm $\parallel \cdot \parallel$. Fix also a 'reasonable' estimator $\hat{\theta}$ of $\theta_{\star}$ using a sample ${(X,Y)}_{1:T}$ from (1.1). We seek to establish finite sample guarantees of the form where $\varepsilon$ controls the accuracy (or rate) and the failure parameter $\delta$ controls the confidence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem 1.1", "weight": 1.0} -->

In the sequel, 'reasonable' estimator will typically mean some form of least squares estimator (1.7). These are introduced in Section 1.2 below. A bound of the form (1.4) is typically thought of as follows. We fix a priori the failure parameter $\delta$ and then provide guarantees of the form ${\|{\hat{\theta} - \theta^{\star}}\|} \leq {\varepsilon{(T,\delta,\mathsf{P}_{XY})}}$ where $\mathsf{P}_{XY}$ is the joint distribution of ${(X,Y)}_{1:T}$. Hence, the sample size $T$, the failure probability $\delta$ and the distribution of the samples all impact the performance guarantee $\varepsilon$ we are able to establish.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem 1.1", "weight": 1.0} -->

To be more specific, $\varepsilon$ will typically be of the form Thus in principle, the best possible choice of $\varepsilon^{2}$ can be thought of as a high probability version of the (inverse) signal-to-noise ratio of the problem at hand. The fact that the confidence parameter $\delta$ typically affects (1.5) additively in $\log{({1/\delta})}$ is consistent with classical asymptotic normality theory of estimators. One often expects the normalized difference $T^{- {1/2}}{({\hat{\theta} - \theta^{\star}})}$ to converge in law to a normal distribution. In this tutorial we will provide tools that allow us to match such classical asymptotics but with a finite sample twist. Let us also remark that there often is a minimal requirement on the sample size necessary for a bound of the form (1.4)-(1.5) to hold.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem 1.1", "weight": 1.0} -->

Such requirements are typically of the form Requirements such as (1.6) are called burn-in times and are related to the notion of persistence of excitation. They correspond to the rather minimal requirement that the parameter identification problem is feasible in the complete absence of observation noise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Least Squares Regression and the Path Ahead", "weight": 1.0} -->

Let us now return to the general setting of (1.1). Fix a subset $\mathsf{M}$ of ${\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$, called the model class. The estimator is the least squares estimator (LSE) of $\theta^{\star}$ (with respect to $\mathsf{M}$). Often we simply set $\mathsf{M} = {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$. In this case, equivalently: and the LSE reduces to the (minimum norm) ordinary least squares (OLS) estimator (1.8).

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Path Ahead", "weight": 1.0} -->

Let us now briefly sketch the path ahead to solve 1.1. If (1.9) is full rank---as required above---the estimator (1.8) admits the convenient error representation: The leftmost term of (1.10) (in square brackets) can be shown to be (almost) time-scale invariant in many situations. For instance, if the noise $V_{1:T}$ is a sub-Gaussian martingale difference sequence with respect to the filtration generated by the covariates $X_{1:T}$, one can invoke methods from the theory of self-normalized processes to show this. These methods are the topic of Section 4.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Path Ahead", "weight": 1.0} -->

Whenever this is the case, the dominant term in the rate of convergence of the least squares estimator is $\left({\sum_{t = 1}^{T}{X_{t}X_{t}^{\mathsf{T}}}} \right)^{- {1/2}}$. In other words, providing control of the smallest eigenvalue of (1.9) effectively yields control of the rate of convergence of the least squares estimator in many situations. Thus, to analyze the rate of convergence of (1.7) when $\mathsf{M} = {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ it suffices to: Analyze the smallest eigenvalue (or lower tail) of (1.9). We provide such analyses in Section 3 Analyze the scale invariant term (in square brackets) of (1.10). This can in many situations be handled for instance by the self-normalized martingale method described in Section 4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview", "weight": 1.0} -->

Before covering these more technical topics in Section 3 and Section 4, we also briefly review some preliminaries from probability theory in Section 2. We then demonstrate how to apply these ideas in the setting of identifying the parameters of an ARX$(p,q)$ model of the form (1.2) in Section 5. An alternative perspective not based on the decomposition (1.10) for more general least squares algorithms is given in Section 6. We conclude with a brief discussion on how the tools in Section 6 can be extended to study more general nonlinear phenomena in Section 7.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sub-Gaussian Concentration and the Hanson-Wright Inequality", "weight": 1.0} -->

In the sequel, we will not want to impose the Gaussian assumption. Instead, we define a class of random variables that admit reasoning analogous to (2.3).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Covering and Discretization Arguments", "weight": 1.0} -->

We will often find ourselves in a situation where it is possible to obtain a scalar concentration bound but need this to hold uniformly for many random variables at once. The $\varepsilon$-net argument, which proceeds via the notion of covering numbers, is a relatively straightforward way of converting concentration inequalities for scalars into their counterparts for vectors, matrices and functions more generally.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Covering and Discretization Arguments", "weight": 1.0} -->

The reader will for instance notice that the quantity being controlled by Theorem 2.1; Rudelson and Vershynin). ‣ 2.1 Sub-Gaussian Concentration and the Hanson-Wright Inequality ‣ 2 Preliminaries: Concentration Inequalities, Packing and Covering ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") is a scalar quadratic form in sub-Gaussian random variables. By contrast, the empirical covariance matrix (1.9) is a matrix and so a conversion step is needed. This idea will be used frequently and in various forms throughout the manuscript, so we review it briefly here for the particular case of controlling the operator norm of a random matrix. To this end, we notice that for any matrix $M \in {\mathbb{R}}^{m \times d}$: Hence, the operator norm of a random matrix is a maximum of scalar random variables indexed by the unit sphere ${\mathbb{S}}^{d - 1}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Covering and Discretization Arguments", "weight": 1.0} -->

Recall now that the union bound states that the probability that the maximum of a *finite collection* (${|S|} < \infty$) ${\{ X_{i}\}}_{i \in S}$ of random variables exceeds a certain threshhold can be bounded by the sum of their probabilities: Unfortunately, the unit sphere appearing (2.7) is not a finite set and so the union bound (2.8) cannot be directly applied. However, when the domain of optimization has geometric structure, one can often exploit this to leverage the union bound not directly but rather in combination with a discretization argument. Returning to our example of the operator norm of a matrix, the set $S$ appearing in (2.8) will be a discretized version of the unit sphere ${\mathbb{S}}^{d - 1}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Concentration of the Covariance Matrix of Linear Systems", "weight": 1.0} -->

To not get lost in the weeds, let us provide an example showcasing the use of Theorem 2.1; Rudelson and Vershynin). ‣ 2.1 Sub-Gaussian Concentration and the Hanson-Wright Inequality ‣ 2 Preliminaries: Concentration Inequalities, Packing and Covering ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") due to Jedra and Proutiere. Recall that the matrix $\hat{\Sigma}$ appearing in (1.9) is crucial to the performance of the least squares estimator. We will now see that this matrix is well-conditioned when we consider stable first order auto-regressions of the form: taking values in ${\mathbb{R}}^{d_{\mathsf{X}}}$. By stable we mean that the largest eigenvalue of $A^{\star}$ has module strictly smaller than 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Concentration of the Covariance Matrix of Linear Systems", "weight": 1.0} -->

The following result is a consequence of the Hanson-Wright inequality together with the discretization strategy outlined in Section 2.2. The full proof is given in Appendix B.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Notes", "weight": 1.0} -->

The basic program carried out in Section 2.3 can be summarized as follows: introduce a discretization of the problem considered---for matrices this is typically a discretization of the unit sphere; prove an exponential inequality for a family of scalar random variables corresponding to one-dimensional projection of the discretization---in our case: prove bounds on the moment generating function of quadratic forms in random matrices; and conclude to obtain a uniform bound by using the union bound across the discretization. This roughly summarizes the proof of Theorem 2.2. These tools are thematic throughout this manuscript.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Lower Spectrum of the Empirical Covariance", "weight": 1.0} -->

Recall that our outline of the analysis of the least squares estimator in Section 1.2 consists of two main components, one of which being the lower tail of the empirical covariance matrix (1.9). In this section we provide a self-contained analysis of this random matrix for a class of \"causal\" systems. Moreover, we will emphasize only the lower tail of this random matrix as to sidestep issues with bounds degrading with the stability of the system considered. This allows us to quantitatively separate the notions of persistence of excitation and stability.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Lower Spectrum of the Empirical Covariance", "weight": 1.0} -->

We say that $X_{1:T}$ is $k$-causal if the matrix $\mathbf{L}$ has the block lower-triangular form: where each ${\mathbf{L}_{ij} \in {{\mathbb{R}}^{{{dk} \times p}k},i}},{j \in {\lbrack{T/k}\rbrack} \triangleq {\{ 1,2,\ldots,{T/k}\}}}$. In brief, we say that $X_{1:T}$ satisfying the above construction is $k$-causal with independent $K^{2}$-sub-Gaussian increments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Lower Spectrum of the Empirical Covariance", "weight": 1.0} -->

Obviously, every $1$-causal process is $k$-causal for every $k \in {\mathbb{N}}$ as long as the divisibility condition holds.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Lower Spectrum of the Empirical Covariance", "weight": 1.0} -->

To analyze the lower tail of the empirical covariance of $X_{1:T}$ we will also associate a decoupled random process Hence, the process ${\overset{\sim}{X}}_{1:T}$ is generated in much the same way as $X_{1:T}$ but by removing the sub-diagonal entries of $\mathbf{L}$: We emphasize that by our assumptions on $W_{1:T}$ and the block-diagonal structure of $\overset{\sim}{\mathbf{L}}$ the variables ${\overset{\sim}{X}}_{1:k},{\overset{\sim}{X}}_{{k + 1}:{2k}},\ldots,{\overset{\sim}{X}}_{{{T - k} + 1}:T}$ are all independent of each other; they have been decoupled.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Lower Spectrum of the Empirical Covariance", "weight": 1.0} -->

This decoupled process will effectively dictate our lower bound, and we will show under relatively mild assumptions that with probability that approaches $1$ at an exponential rate in the sample size $T$. More precisely, the following statement is the main result of this section.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Since the blocks of $\mathbf{L}$ can be regarded to specify the noise-to-output map, the assumption that the diagonal blocks are constant is for instance satisfied by linear time-invariant (LTI) systems. The assumption can be removed at the cost of a more complicated expression.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

The next example serves as the archetype for the reduction from $\mathbf{L}$ to $\overset{\sim}{\mathbf{L}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

The reduction from $X_{1:T} = {\mathbf{L}W_{1:T}}$ to ${\overset{\sim}{X}}_{1:T} = {{blkdiag}{(\mathbf{L}_{11},\ldots,\mathbf{L}_{{T/k},{T/k}})}W_{1:T}}$ corresponds to replacing a single trajectory from the linear system (3.7) of length $T$ by $T/k$ trajectories of length $k$ each and sampled independently of each other. The price we pay for decoupling these systems is that our lower bound is dictated by the gramians up to range $k$: instead of the gramians up to range $T$: Put differently, the reduction from $\mathbf{L}$ to $\overset{\sim}{\mathbf{L}}$ can be thought of as restarting the system every $k$ steps.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Comparing with Theorem 2.2, the advantage of Theorem 3.1 is that it allows us to provide persistence-of-excitation type guarantees that do not rely strongly on the stability of the underlying system. While Theorem 2.2 gives in principle stronger two-sided concentration results, it comes at the cost of the guarantees becoming vacuous as the spectral radius of $A^{\star}$ in Example 3.1 tends to marginal stability (tends to $1$). By contrast, Theorem 3.1 does not exhibit such a blow-up since the dependence on $C_{\mathsf{s}\mathsf{y}\mathsf{s}}$ in (3.6) is logarithmic (instead of polynomial). The distinction might seem small, but it is qualitatively important as it (almost) decouples the phenomena of stability and persistence of excitation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Decoupling Inequality for sub-Gaussian Quadratic Forms", "weight": 1.0} -->

Our proof of Theorem 3.1 will make heavy use of Proposition 3.1 below. This is the crucial probabilistic inequality that allows us to decouple---or restart as discussed in Example 3.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Lower Tail of the Empirical Covariance of Causal sub-Gaussian Processes", "weight": 1.0} -->

Repeated application of Proposition 3.1 to the process $X_{1:T} = {\mathbf{L}W_{1:T}}$ in combination with the tower property of conditional expectation yields the following exponential inequality that controls the lower tail of (1.9) in any fixed direction.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Notes", "weight": 1.0} -->

In this manuscript we have chosen a perhaps less well-known but conceptually simpler approach to establishing lower bounds on the empirical covariance matrix Equation 3.3. The first proof of a statement similar to Theorem 3.1 is due to Simchowitz et al. which in turn relies on a more advanced notion from probability theory known as the small-ball method, due to Mendelson. The emphasis therein is on anti-concentration---which can hold under milder moment assumptions---rather than concentration. However, the introduction of this tool is not necessary for Gaussian (or sub-Gaussian) system identification. For instance, Sarkar and Rakhlin leverage the method of self-normalized martingales introduced in Section 4 below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Notes", "weight": 1.0} -->

Our motivation for providing a different proof is to streamline the exposition as to fit control of the lower tail into the \"standard machinery\", which roughly consists of: prove a family of scalar exponential inequalities, invoke the Chernoff method, and conclude by a discretization argument and a union bound to port the result from scalars to matrices. Our proof here follows this outline and emphasizes the exponential inequality in Theorem 3.2. We finally remark that the proof presented here is new to the literature and extends a result in Ziemann from the Gaussian setting to the sub-Gaussian setting.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Self-Normalized Martingale Bounds", "weight": 1.0} -->

The objective in this section is to bound the operator and Frobenius norms of the self-normalized term of (1.10): This object has special structure. Firstly, in many cases of interest, e.g. the autoregressive model in (1.2), the noise $V_{t}$ is independent of $X_{k}$ for all $k \leq t$. This is what provides martingale structure, as will be made precise shortly. Secondly, it is self-normalized: if the covariates $X_{t}$ are large for some $t$, then any increase in the left sum will be compensated by an increase in the sum in the term on the right. Together, these properties make the object above a self-normalized martingale term.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Self-Normalized Martingale Bounds", "weight": 1.0} -->

To express results generally and compactly, several definitions are in order.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

We begin by neglecting the details of the process that generated the data in (4.1). In particular, consider a random matrix $P$ assuming values in ${\mathbb{R}}^{d_{\eta} \times d_{\mathsf{X}}}$ for $d_{\eta} \in {\mathbb{N}}_{+}$ and a random matrix $Q$ assuming values in ${\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{X}}}$ with $Q$ almost surely nonsingular. Bounding the quantities in (4.2) and (4.3) are special cases of bounding ${\parallel{PQ^{- \frac{1}{2}}}\parallel}_{F}$. A naive first approach is to apply a Chernoff bound (2.2. ‣ 2 Preliminaries: Concentration Inequalities, Packing and Covering ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

Doing so results in the inequality If it is possible to bound the moment generating function $\mathbf{E}{\exp\left({\frac{\lambda}{2}{\parallel{PQ^{- {1/2}}}\parallel}_{F}^{2}} \right)}$ by one for some $\lambda > 0$, then the above bound provides an exponential inequality. Obtaining a bound of the form ${\mathbf{E}{\exp\left({\frac{\lambda}{2}{\parallel{PQ^{- {1/2}}}\parallel}_{F}^{2}} \right)}} \leq 1$ requires very strong assumptions on $P$ and $Q$ which would not be suitable for our purposes.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

However, we may observe that ${\frac{1}{2}{\parallel{PQ^{- {1/2}}}\parallel}_{F}^{2}} = {\max_{\Lambda}{{tr}{({{P\Lambda} - {\frac{1}{2}\Lambda^{\top}Q\Lambda}})}}}$. This motivates the following canonical assumption in self-normalized process theory: This inequality is called the canonical assumption because a wide variety of self-normalized processes satisfy it.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

We will demonstrate that it is satisfied for (4.2) and (4.3) in Section 4.2. If we could exchange the order of the maximization with the expectation in (4.4), then the bound ${\mathbf{E}{\exp\left({\frac{1}{2}{\parallel{PQ^{- {1/2}}}\parallel}_{F}^{2}} \right)}} \leq 1$ would be satisfied, and the Chernoff bound above would provide a valuable exponential inequality. As this exchange is not possible, we instead lower bound the maximization over $\Lambda$ by assigning a probability distribution to a random variable $\Psi$ which takes values in ${\mathbb{R}}^{d_{\mathsf{X}} \times d_{\eta}}$, and taking the expectation over this distribution.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

Doing so preserves the inequality (4.4): The order of expectation over $\Psi$ and over the random variables $P$ and $Q$ may then be exchanged by an appeal to Fubini's theorem: By selecting the distribution over $\Psi$ appropriately, the result is a so-called pseudo-maximization.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Exponential Inequalities via Pseudo-maximization", "weight": 1.0} -->

This allows us to apply a Chernoff argument similar to the one sketched above to obtain an exponential bound on a quantity related to ${\parallel{PQ^{- {1/2}}}\parallel}_{F}$. The following lemma demonstrates one such bound that results by selecting the distribution of $\Psi$ as a matrix normal distribution.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Self-Normalized Martingales Satisfy the Canonical Assumption", "weight": 1.0} -->

In order to make use of Lemma 4.1). ‣ 4.1 Exponential Inequalities via Pseudo-maximization ‣ 4 Self-Normalized Martingale Bounds ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") to bound (4.2) or (4.3), we must ensure that the condition (4.4) holds for where $\eta_{t} \in {\mathbb{R}}^{d_{\eta}}$ is either the noise process $V_{t}$ or the scalar process $w^{\top}V_{t}$ for some fixed unit vector $w$. The following lemma shows that it is sufficient for $\eta_{t}$ to be $\sigma^{2}$-conditionally sub-Gaussian.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Notes", "weight": 1.0} -->

Theorem 4.1 holds for a fixed $T \in {\mathbb{N}}_{+}$, which is sufficient for analyzing the system identification error. In contrast, the self-normalized margtingale bound in Abbasi-Yadkori holds for an arbitrary stopping time and thus uniformly for all $T \in {\mathbb{N}}_{+}$ by a stopping time construction. This uniform bound may be required in some settings, e.g. in error bounds for adapative control.

<!-- chunk {"id": "body-0047", "role": "body", "section": "System Identification", "weight": 1.0} -->

In this section, we analyze well-known linear system identification algorithms that rely on the least squares algorithm. Note that the problem formulation changes with the system parameterization (e.g., state space, ARMAX, etc.). However, a nice property of linear systems is that under certain conditions, we can obtain a linear non-parametric ARX model by regressing the system output to past outputs and inputs. Then, depending on the parameterization, we can recover a particular realization. In the following, we first review ARX identification, which can be seen as a fundamental building block for many linear system identification algorithms. Then, we analyze identification of Markov parameters in the case of state-space systems. We focus exclusively on the case of single trajectory data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 5.1 (System and Noise model)", "weight": 1.0} -->

Let the noise covariance $\Sigma_{W} \succ 0$ be full rank. Let the normalized process noise ${W_{t},t} \geq 0$ be independent and identically distributed, $K^{2}$-sub-Gaussian (see Definition 2.1), with zero mean and unit covariance ${\mathbf{E}W_{t}W_{t}^{\top}} = I_{d_{\mathsf{Y}}}$. The orders $p,q$ are known. System (5.1) is non-explosive, that is, the eigenvalues of matrix lie strictly on or inside the unit circle ${\rho{(\mathcal{A}_{11})}} \leq 1$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 5.1 (System and Noise model)", "weight": 1.0} -->

The techniques below can provide meaningful finite-sample bounds only when the system is non-explosive. Deriving finite sample guarantees for identifying open-loop, explosively unstable partially-observed systems from single trajectory data is open to the best of our knowledge.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 5.1 (System and Noise model)", "weight": 1.0} -->

In this tutorial, we focus solely on white-noise excitation inputs. Excitation strategies---experiment designs---beyond this simple structure form a vast literature in system identification and statistics, see for instance Ljung; Gevers; Pukelsheim and Bombois et al. and the references therein. For a recent non-asymptotic treatment see also Wagenmaker and Jamieson.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 5.2 (White-noise excitation policy)", "weight": 1.0} -->

We assume that the control input is generated by a random i.i.d. Gaussian process, that is, $U_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 5.2 (White-noise excitation policy)", "weight": 1.0} -->

Grouping all covariates into one vector and defining we can re-write (5.1) in terms of (1.1) where $W_{t}$ is independent from $X_{t}$, but $X_{t}$ has the special time-dependent structure induced by (5.1). Given samples $(Y_{1:T},U_{0:{T - 1}})$, the least-squares estimate is given by where we purposely highlight the dependence of the estimate on the number of samples with the subscript $T$. Before we present the main result, let us define some quantities which are related to the quality of system estimates. The covariance at time $t \geq 0$ is defined as It captures the expected richness of the data, i.e., how excited the modes of the system are on average. In particular, the relative excitation of the data compared to the noise magnitude significantly affects the quality of system identification.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 5.2 (White-noise excitation policy)", "weight": 1.0} -->

This motivates the definition of signal-to-noise (SNR) as the ratio of the (directionally) worst-case excitation over the worst-case noise magnitude The following theorem provides a finite-sample upper bound on the performance of the least-square estimator.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Persistency of Excitation in ARX Models", "weight": 1.0} -->

In this subsection, we leverage the result of Theorem 3.1 to prove persistency of excitation. By persistency of excitation, we refer to the case when we have rich input-output data, that is, data which characterize all possible behaviors of the system. Recall the definition (1.9) of the empirical covariance matrix Using this definition, the excitation term in the least squares error can be re-written as ${({T{\hat{\Sigma}}_{T}})}^{- {1/2}}$. We say that persistency of excitation holds if and only if the empirical covariance matrix is strictly positive definite (full rank). In the following, we show that the full rank condition holds with high probability, provided that the number of samples exceeds a certain threshold, i.e., the burn-in time.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 5.1 (Existence of burn-in time.)", "weight": 1.0} -->

For the above result to be meaningful, we need inequality (5.9. ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")) to be feasible. For non-explosive systems, the system theoretic term ${\log C_{\mathsf{s}\mathsf{y}\mathsf{s}}}{(T,\tau)}$ increases at most logarithmically with $T$, since $\Sigma_{t}$ increases polynomially with $t$ in view of Lemma 5.1). ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 5.1 (Existence of burn-in time.)", "weight": 1.0} -->

Hence, for any fixed $\tau$, or, in general, any $\tau$ that increases mildly (sublinearly) with $T$, e.g. $O{(\sqrt{T})}$, it is possible to satisfy (5.9. ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")). Note that ${\rho{(\mathcal{A})}} = {\rho{(\mathcal{A}_{11})}}$ due to the triangular structure of $\mathcal{A}$. Hence, by Assumption 5.1. ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification"), system $\mathcal{A}$ is also non-explosive.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 5.2 (Unknown system orders $p,q$)", "weight": 1.0} -->

The result of Theorem 5.2. ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") still holds if the orders $p,q$ are unknown and we use the wrong orders $\hat{p},\hat{q}$ in the covariates $X_{t}$. We just need to replace $p,q$ with $\hat{p},\hat{q}$ with $\hat{p},\hat{q}$ and revise the size of $\Sigma$ accordingly in (5.9. ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")). The finite-sample bounds of Theorem 5.1.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 5.2 (Unknown system orders $p,q$)", "weight": 1.0} -->

‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") also hold (by revising accordingly), but only if we overestimate $p,q$, that is $\hat{p} \geq p$, $\hat{q} \geq q$. This also generalizes the single trajectory result of Du et al. to non-explosive systems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 5.2 (Unknown system orders $p,q$)", "weight": 1.0} -->

The following supporting lemma proves that the $k$-th powers of non-explosive matrices increase at most polynomially with $k$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Dealing with the Noise Term", "weight": 1.0} -->

In this subsection, we modify the noise term so that we can leverage Theorem 4.1, which cannot be applied directly. We first manipulate the inverse of $T{\hat{\Sigma}}_{T}$ to relate it to the inverse of $\Sigma + {T{\hat{\Sigma}}_{T}}$, for some carefully selected $\Sigma$. Inspired by Sarkar and Rakhlin, we leverage the result of Theorem 5.2. ‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification"). Under the event that persistency of excitation holds we have ${\hat{\Sigma}}_{T} \succeq {{T\Sigma_{\tau}}/16}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Dealing with the Noise Term", "weight": 1.0} -->

Thus, selecting $\Sigma = {{T\Sigma_{\tau}}/16}$ guarantees that We can now apply Theorem 4.1. To finish the proof we need to upper-bound the determinant of $\log{\det{({\Sigma + {T{\hat{\Sigma}}_{T}}})}}$. It is sufficient to establish a crude upper-bound on the empirical covariance $T{\hat{\Sigma}}_{T}$ as in the following lemma.

<!-- chunk {"id": "body-0062", "role": "body", "section": "State-Space Systems", "weight": 1.0} -->

We call the normalized noise process $E_{t}$ the innovation error process. Similar to the ARX case, we focus on white-noise excitation inputs, namely Assumption 5.2. ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") also holds here. Moreover, we assume the following.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 5.3 (System and Noise model)", "weight": 1.0} -->

Let the noise covariance $\Sigma_{E} \succ 0$ be full rank. Let the normalized innovation process $E_{t}$ be independent, identically distributed, $K^{2}$-sub-Gaussian (see Definition 2.1), with zero mean and unit covariance ${\mathbf{E}E_{t}E_{t}^{\top}} = I_{d_{\mathsf{Y}}}$. The order $d_{\mathsf{X}}$ is unknown. System (5.14) is non-explosive, that is, the eigenvalues of matrix $A^{\star}$ lie strictly on or inside the unit circle ${\rho{(A)}} \leq 1$. The system is also minimum-phase, i.e., the closed loop matrix has all eigenvalues inside the unit circle ${\rho{(A_{\mathsf{c}\mathsf{l}}^{\star})}} < 1$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 5.3 (System and Noise model)", "weight": 1.0} -->

The innovation form (5.14) might seem puzzling at first. In particular, the correlation between process and measurement noise via $F^{\star}$, and the requirement ${\rho{(A_{\mathsf{c}\mathsf{l}}^{\star})}} < 1$ seem restrictive. However, the representation (5.14) is standard in the system identification literature Verhaegen and Verdult. Moreover, as we review below, standard state-space models have input-output second-order statistics, which are equivalent to the ones generated by system (5.14) (for appropriate $F^{\star}$, $\Sigma_{E}$).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 5.3 (Generality of model)", "weight": 1.0} -->

System class (5.14) captures general state-space systems driven by Gaussian noise. Consider the following state-space model where $W_{t},V_{t}$ are i.i.d., independent of each other, mean-zero Gaussian, with covariances $\Sigma_{W}$ and $\Sigma_{V}$ respectively. Assume that $\Sigma_{V} \succ 0$ is full rank, the pair $(C^{\star},A^{\star})$ is detectable, and the pair $(A^{\star},\Sigma_{W})$ is stabilizable. These three assumptions imply that the Kalman filter of system (5.16. ‣ 5.2 State-Space Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")) is well-defined.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5.3 (Generality of model)", "weight": 1.0} -->

In particular, define the Riccati operator as and let $P^{\star}$ be the unique positive semidefinite solution of $P^{\star} = {{\mathsf{R}\mathsf{I}\mathsf{C}}{(P^{\star})}}$. Then the Kalman filter gain is equal to Assume that the initial state is also mean-zero Gaussian with covariance $P^{\star}$ and independent of the noises. Finally set Under the above assumptions and selection of $F^{\star}$, $\Sigma_{E}$ systems (5.14) and (5.16. ‣ 5.2 State-Space Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")) are statistically equivalent from an input-output perspective, see Qin. Both system descriptions lead to input-output trajectories with identical statistics.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 5.3 (Generality of model)", "weight": 1.0} -->

Moreover, due to the properties of Kalman filter, stability of $A_{\mathsf{c}\mathsf{l}}^{\star}$ (minimum phase property) and independence of $E_{t}$ are satisfied automatically.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 5.3 (Generality of model)", "weight": 1.0} -->

In this tutorial we will only focus on recovering the first few (logarithmic in $T$-many) Markov parameters $C^{\star}{(A_{\mathsf{c}\mathsf{l}}^{\star})}^{i}B^{\star}$, $i \geq 0$ and $C^{\star}{(A_{\mathsf{c}\mathsf{l}}^{\star})}^{j}F^{\star}$, $j \geq 0$ of system (5.14). From a learning theory point of view, this is also known as improper learning, since the search space (finitely many Markov parameters) does not exactly, but only approximately, coincide with the hypothesis class (state space models). In principle, this forms the backbone of the SSARX method introduced by Jansson. One can then proceed to recover the original state-space parameters (up to similarity transformation) from the Markov parameters by employing some realization method.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 5.3 (Generality of model)", "weight": 1.0} -->

We refer to Oymak and Ozay; Tsiamis et al. for a discussion on this approach from a finite sample perspective.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Reduction to ARX learning with Bias", "weight": 1.0} -->

Let $p > 0$ be a past horizon. Denote the Markov parameters up to time $p$ by Note that the innovation errors are equal to ${\Sigma_{E}^{1/2}E_{t}} = {Y_{t} - {C^{\star}X_{t}}}$. Replacing this expression into the state equation (5.14), we obtain Unrolling the state equation $p$ times, we get where $Z_{t}$ includes the past $p$ covariates The above recursion is an approximate ARX equation. There is an additive bias error term on top of the statistical noise. The least-squares solution is given by where we also highlight the dependence on the past $p$. By the minimum phase assumption, the bias term decays exponentially with the past horizon $p$. This follows from the fact that $A_{\mathsf{c}\mathsf{l}}^{\star}$ is asymptotically stable, while $X_{t}$ scales at most polynomially with $t$ (in view of Lemma 5.1).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Reduction to ARX learning with Bias", "weight": 1.0} -->

‣ 5.1.1 Persistency of Excitation in ARX Models ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification")). By selecting $p = {\Omega{({\log T})}}$, we can make the bias term decay very fast, making its contribution to the error $\theta_{p}^{\star} - {\hat{\theta}}_{p,T}$ negligible. On the other hand, increasing the past horizon $p$ increases the statistical error since the search space is larger.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Non-Asymptotic Guarantees", "weight": 1.0} -->

To derive finite-time guarantees for state space systems of the form (5.14), we follow the same steps as in the case of ARX systems. However, we have to account for the bias term and the fact that $p$ grows with $\log T$. Let us define again the covariance at time $t \geq 0$ where we highlight the dependence on both the past horizon $p$ and the time $t$. The covariance of the state is defined similarly Define the SNR as Unlike the ARX case, here the SNR might degrade since we allow $p$ to grow with $\log T$. For this reason, we require the following additional assumption.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Assumption 5.4 (Non-degenerate SNR)", "weight": 1.0} -->

We assume that the SNR is uniformly lower bounded for all possible past horizons Later, in Theorem 5.4, we show that the above condition is non-vacuous and is satisfied for quite general systems.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Notes", "weight": 1.0} -->

The exposition above is inspired by prior work on identifying fully-observed systems and partially-observed systems. For a wider overview of the literature, we refer the reader to Tsiamis et al..

<!-- chunk {"id": "body-0075", "role": "body", "section": "Notes", "weight": 1.0} -->

Let us further remark that the guarantee for the ARX model in Theorem 5.1. ‣ 5.1 ARX Systems ‣ 5 System Identification ‣ A Tutorial on the Non-Asymptotic Theory of System Identification") is almost optimal. The use of Matrix Markov's inequality yields extraneous dependency on the problem dimension multiplying the deviation term $\log{({1/\delta})}$. This can in principle be removed by a more refined analysis (see e.g. the proof of Proposition 6.1 below or the results in Jedra and Proutiere ). Indeed, the signal-to-noise term (5.6) is closely related to the Fisher Information Matrix appearing in the classical asymptotic optimality theory. Let us also point out that the question of optimality in identifying partially observed state-space systems is more subtle, and while consistent, the bounds presented here are not (asymptotically) optimal.

<!-- chunk {"id": "body-0076", "role": "body", "section": "An Alternative Viewpoint: the Basic Inequality", "weight": 1.0} -->

In many situations, the choice of the model class $\mathsf{M} = {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ leading to (1.8) is not appropriate. For instance physical or other modelling considerations might have already informed us that the true $\theta^{\star}$ belongs to some smaller model class such as the family of low rank or sparse matrices which are strict subsets of $\mathsf{M}$. Other properties one might wish to enforce include, stable, low norm, or even passivity-type properties. In either of the above examples no error expression of the form (1.10) is directly available. Instead, we observe by optimality of $\hat{M}$ to the optimization program (1.7) that Expanding the squares and re-arranging terms we arrive at the so-called basic inequality of least squares: The inequality (6.2) serves as an alternative to the explicit error equation (1.10).

<!-- chunk {"id": "body-0077", "role": "body", "section": "An Alternative Viewpoint: the Basic Inequality", "weight": 1.0} -->

To drive home this point, let us first re-arrange (6.2) slightly: Note now that $\hat{\theta} - \theta^{\star}$ are elements of $\mathsf{M}_{\star} \triangleq {\mathsf{M} - \theta^{\star}}$. Hence---by considering the worst-case (supremum) right hand side of (6.3)---we obtain: In fact, if $\mathsf{M} = {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$, the optimization on the right hand side of (6.4) has an explicit solution.

<!-- chunk {"id": "body-0078", "role": "body", "section": "An Alternative Viewpoint: the Basic Inequality", "weight": 1.0} -->

Put differently, we may regard (6.4) as a variational (or dual) form of the explicit error (1.10). Now, the advantage of (6.4) is twofold: (6.4) and (6.5) hold for any $\mathsf{M}_{\star} \subset {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ and hence allows us to analyze the LSE (1.7) beyond OLS ($\mathsf{M}_{\star} = {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$). This is important in identification problems where the parameter space is restricted.

<!-- chunk {"id": "body-0079", "role": "body", "section": "An Alternative Viewpoint: the Basic Inequality", "weight": 1.0} -->

We do not have to rely on (6.5) to control (6.4). In fact, for many reasonable classes of $\mathsf{M}_{\star} \subset {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ we are able to give alternative arguments that are much sharper (in terms of e.g. dimensional scaling) than the naive bound (6.5). See Section 6.1 below.

<!-- chunk {"id": "body-0080", "role": "body", "section": "An Alternative Viewpoint: the Basic Inequality", "weight": 1.0} -->

A third advantage of the variational form (6.4) is that it generalizes straightforwardly beyond linear least squares. In fact, none of the steps (6.1),(6.2), (6.3) and (6.4) relied on the linearity of $x\mapsto{\hat{\theta}x}$ or that of $x\mapsto{\theta^{\star}x}$ ($x \in {\mathbb{R}}^{d_{\mathsf{X}}}$). We will explore this theme further in Section 6.1 and Section 7.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

Before we proceed to sketch out how the basic inequality above extends to nonlinear problems in Section 7, let us use it to analyze a simple variation of the autoregression already encountered in Section 5. Namely, the autoregressive model (5.1) which---for simplicity---is further assumed one-dimensional: and assume in addition that it is known that only $s \in {\mathbb{N}}$ of the $p$ entries of $\theta^{\star} = {\lbrack A_{1}^{\star},\ldots,A_{p}^{\star}\rbrack}$ are nonzero. Put differently, the vector $\theta^{\star}$ is known to be $s$-sparse and we write $\theta^{\star} \in {\{{\theta \in {\mathbb{R}}^{p}}:{{\|\theta\|}_{0} \leq s}\}} \triangleq \mathsf{M}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

Hence, in this case the model class $\mathsf{M}$ is the union of $\binom{p}{s}$ subspaces. Clearly, we could use OLS (1.8) but this estimator does not take advantage of the additional information that $A^{\star} = \theta^{\star}$ lies in the $s$-dimensional submanifold $\mathsf{M}$. Intuitively, if $s \ll p$ this set should be much smaller than ${\mathbb{R}}^{p}$ and so one expects that identification occurs at a faster rate.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

In this section we demonstrate that the least squares estimator (1.7) in which the search is restricted to the low-dimensional manifold $\mathsf{M}$ outperforms the OLS. We stress that this is *not* a computationally efficient estimator and the results in this section should be thought of as little more than an illustrative example.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

Returning to the problem of controlling the error of this estimator, we note that in this case there is no closed form for the LSE and we do not have direct access to the error equation (1.10).^55^5Although, in this particular case an alternative analysis based on this equation is possible. Hence, we instead use the offset basic inequality approach from Section 6. As before, it is convenient to set $X_{t} = {\lbrack Y_{t - 1},\ldots,Y_{t - p}\rbrack}^{\mathsf{T}}$. With this additional bit of notation in place, we recall from (6.4) that: where $\mathsf{M}_{\star}$ is the translation $\mathsf{M} - \theta^{\star}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

Notice now that since $\theta$ in $$ is $s$-sparse, the products $\theta X_{t}$ are just ${\theta X_{t}} = {\sum_{i \in S}{\theta_{i}{(X_{t})}_{i}}}$ where we have abused notation and identified $S$ with its support set. Hence, by the same direct calculation as in (6.5), if we denote ${(X_{t})}_{S}$ the $s$-dimensional vector obtained by coordinate projection onto part of $S$ not constrained to be identically zero (i.e. the image of the projection onto $S$ represented as the $s$-dimensional Euclidean space) we find that: The right hand side of (6.9) can be controlled by the self-normalized inequality in Theorem 4.1 for each fixed $S$. Moreover, there are only $\binom{p}{2s}$ such subspaces, so we can apply a union bound to control the maximum over these subspaces.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Sparse Autoregressions", "weight": 1.0} -->

Note also that the left hand side of (6.9) can be controlled by the tools developed in Section 3. Carrying out these steps leads to the following guarantee.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Notes", "weight": 1.0} -->

The variational formulation of the least squares error---the basic inequality (6.2)---is standard in the nonparametric statistics literature. The idea to rewrite the basic inequality (6.2) as (6.3) was introduced to the statistical literature by Liang et al., but has its roots in online learning.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Beyond Linear Models", "weight": 1.0} -->

Let us now make another gradual shift of perspective. Instead of considering the linear model (1.1) introduced in Section 1.1 we consider the following *nonlinear* regression model: As before, $Y_{1:T}$,$X_{1:T}$ and $V_{1:T}$ are stochastic processes taking values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$ and ${\mathbb{R}}^{d_{\mathsf{X}}}$ respectively. However, this time $f^{\star}$ is no longer constrained to be a linear map of the form $x\mapsto{Ax}$ for matrix $A$. Rather, we suppose that $f^{\star}$ in (7.1) belongs to some (square integrable) space of functions $\mathcal{F}$ such that ${\mathcal{F} \ni f}:{x\mapsto{f{(x)}}}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Beyond Linear Models", "weight": 1.0} -->

It is perhaps now that the motivation behind the change of perspective from Section 6 becomes most apparent: the basic inequality (6.3) remains valid. To be precise, let us define the *nonlinear* least squares estimator Let $\mathcal{F}_{\star} \triangleq {\mathcal{F} - f^{\star}}$. By the exact same optimality argument as in Section 6, the reader can now readily verify that: What does (7.3) entail in terms of estimating the unknown function $f^{\star}$? To answer this, we first need to define a performance criterion. The simplest one is small average $L^{2}$-norm-error, where The program we have carried out in the previous sections now generalizes as follows: First, prove a so-called lower uniform law. That is to say, we wish to show that with overwhelming probability for some universal positive constant $C$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Beyond Linear Models", "weight": 1.0} -->

Second, control the supremum of the *empirical process*: in terms of the noise level $\sigma$ and the complexity of the class $\mathcal{F}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Beyond Linear Models", "weight": 1.0} -->

By combining (7.5) and (7.6) we arrive at a high probability bound of the form: A statement of this form is given as Theorem 7.1 below.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Remark 7.1", "weight": 1.0} -->

It is worth to take pause and appreciate the analogy to the analysis of linear regression models. The first step (7.5) exactly corresponds to controlling the lower spectrum of the empirical covariance matrix. Suppose for simplicity that $d_{\mathsf{Y}} = 1$. Then for a linear map ${\mathbb{S}}^{d_{\mathsf{X}} - 1} \ni f\mapsto{\langle f,x\rangle}$ we have: which are just the one-dimensional projections of the empirical covariance matrix (1.9).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark 7.1", "weight": 1.0} -->

Moreover, For linear models, we had: Analyzing terms of this form was the topic of Section 4.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark 7.1", "weight": 1.0} -->

In other words, the approach outlined above is very much in the same spirit as that in the rest of the manuscript. There are a few changes that need to be made since we less access to linearity in our argument, but in principle the key difference is that we will have to replace the indexing set ${\mathbb{S}}^{d - 1}$ with a more general function class $\mathcal{F}_{\star}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Many Trajectories and Finite Hypothesis Classes", "weight": 1.0} -->

In order to make the exposition self-contained, we will now make two simplifying assumptions relating to the finiteness of the hypothesis class and the dependence structure of the covariate process $X_{1:T}$. A more general treatment without these can be found in Ziemann and Tu. Here, we impose the following: The hypothesis class $\mathcal{F}$ is finite; ${|\mathcal{F}|} < \infty$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Many Trajectories and Finite Hypothesis Classes", "weight": 1.0} -->

We have access to $T/k$-many independent trajectories from the same process: there exists an integer $k \in {\mathbb{N}}$ dividing $T$ such that $X_{1:k},X_{{k + 1}:{2k}},\ldots$ are drawn iid.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Many Trajectories and Finite Hypothesis Classes", "weight": 1.0} -->

We will also impose the following rather minimal integrability condition: All functions $f \in \mathcal{F}$ are such that ${\mathbf{E}{\|{f{(X_{t})}}\|}_{2}^{4}} < \infty$ for all $t \in {\lbrack T\rbrack}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Many Trajectories and Finite Hypothesis Classes", "weight": 1.0} -->

Moreover, as in Section 5, we require the noise to be a sub-Gaussian martingale difference sequence: For each $t \in {\lbrack T\rbrack}$, $\left. V_{t} \middle| X_{1:t} \right.$ is $\sigma^{2}$ conditionally-sub-Gaussian and mean zero.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 7.2", "weight": 1.0} -->

Note that A4. above entails that ${f_{\star}{(x)}} = {\mathbf{E}{\lbrack{\left. Y_{t} \middle| X_{t} \right. = x}\rbrack}}$ for every time instance $t$ and so the setup is akin to the study of \"predictor models\" from system identification.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 7.2", "weight": 1.0} -->

Under these assumptions, the main result of Ziemann and Tu essentially simplifies to the following theorem.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Notes", "weight": 1.0} -->

As noted in the previous section, the idea of using the "offset" basic inequality relied on here is due to Rakhlin and Sridharan; Liang et al.. The "many trajectores"-style of analysis used here is due to Tu et al. who introduced it in the linear setting. Here, we have extended their style of analysis to simplify the exposition of Ziemann and Tu who consider the single trajectory setting, but rely on a rather more advanced exponential inequality due to Samson. Alternatively, one can also easily extend the lower uniform law in Proposition F.1 to certain classes of mixing processes by invoking the blocking technique of Yu combined with a truncation style of argument such as that used in the proof of Theorem 14.12 of Wainwright, see also Ziemann et al.. Note however, that all the analyses above and in this section necessitate some degree of stability (mixing). This should be contrasted with the system identification bounds of Section 5, which work even in the marginally regime. In principle, the consequence of this is that while the convergence rates for bounds such as Theorem 7.1 are correct, the burn-ins are deflated by various dependency measures.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Notes", "weight": 1.0} -->

There have also been other, more algorithmically focused, approaches to nonlinear identification problems in the recent literature. Noteably, gradient based methods in generalized linear models of the form $X_{t + 1} = {{\phi{({A^{\star}X_{t}})}} + V_{t}}$ (with $\phi$ a known nonlinearity) have been the topic of a number of recent papers. The sharpest bounds for parameter recovery in this setting are due to Kowshik et al..
