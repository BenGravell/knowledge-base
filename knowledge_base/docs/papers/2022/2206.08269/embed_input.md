<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning with Little Mixing

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study square loss in a realizable time-series framework with martingale difference noise. Our main result is a fast rate excess risk bound which shows that whenever a trajectory hypercontractivity condition holds, the risk of the least-squares estimator on dependent data matches the iid rate order-wise after a burn-in time. In comparison, many existing results in learning from dependent data have rates where the effective sample size is deflated by a factor of the mixing-time of the underlying process, even after the burn-in time. Furthermore, our results allow the covariate process to exhibit long range correlations which are substantially weaker than geometric ergodicity. We call this phenomenon learning with little mixing, and present several examples for when it occurs: bounded function classes for which the L^ and L^+epsilon norms are equivalent, ergodic finite state Markov chains, various parametric models, and a broad family of infinite dimensional ell^(N) ellipsoids. By instantiating our main result to system identification of nonlinear dynamics with generalized linear model transitions, we obtain a nearly minimax optimal excess risk bound after only a polynomial burn-in time.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider regression in the context of the time-series model: Such models are ubiquitous in applications of machine learning, signal processing, econometrics, and control theory. In our setup, the learner is given access to $T \in {\mathbb{N}}_{+}$ pairs ${\{{(X_{t},Y_{t})}\}}_{t = 0}^{T - 1}$ drawn from the model (1.1), and is asked to output a hypothesis $\hat{f}$ from a hypothesis class $\mathcal{F}$ which best approximates the (realizable) regression function $f_{\star} \in \mathcal{F}$ in terms of square loss.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study the least-squares estimator (LSE). This procedure minimizes the empirical risk associated to the square loss over the class $\mathcal{F}$. When each pair of observations $(X_{t},Y_{t})$ is drawn iid from some fixed distribution, this procedure is minimax optimal over a broad set of hypothesis classes. However, much less is known about the optimal rate of convergence for the general time-series model (1.1), as correlations across time in the covariates $\{ X_{t}\}$ complicate the analysis.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With this in mind, we seek to extend our understanding of the minimax optimality of the LSE for the time-series model (1.1). We show that for a broad class of function spaces and covariate processes, the effects of data dependency across time enter the LSE excess risk only as a higher order term, whereas the leading term in the excess risk remains order-wise identical to that in the iid setting. Hence, after a sufficiently long, but finite *burn-in time*, the LSE's excess risk scales as if all $T$ samples are independent. This behavior applies to processes that exhibit correlations which decay slower than geometrically. We refer to this double phenomenon, where the mixing-time only enters as a burn-in time, and where the mixing requirement is mild, as *learning with little mixing*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our result stands in contrast to a long line of work on learning from dependent data (see e.g., and the references within), where the blocking technique is used to create independence amongst the dependent covariates, so that tools to analyze independent learning can be applied. While these aforementioned works differ in their specific setups, the main commonality is that the resulting dependent data rates mimic the corresponding independent rates, but with the caveat that the sample size is replaced by an "effective" sample size that is *decreased* in some way by the mixing-time, even after any necessary burn-in time. Interestingly, the results of Ziemann et al. studying the LSE on the model (1.1) also suffer from such sample degradation, but do not rely on the blocking technique.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The model (1.1) captures learning dynamical systems by setting $Y_{t} = X_{t + 1}$, so that the regression function $f_{\star}$ describes the dynamics of the state variable $X_{t}$. Recent progress in system identification shows that the lack of ergodicity does not necessarily degrade learning rates. Indeed, when the states evolve as a linear dynamical system (i.e., the function $f_{\star}$ is linear), learning rates are not deflated by any mixing times, and match existing rates for iid linear regression. Kowshik et al.; Gao and Raskutti extend results of this flavor to parameter recovery of dynamics driven by a generalized linear model. The extent to which this phenomenon---less ergodicity not impeding learning---generalizes beyond linear and generalized linear models is a key motivation for our work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

We consider the realizable setting, where $f_{\star}$ is assumed to be contained in a known function space $\mathcal{F}$. Our results rest on two assumptions regarding both the covariate process $\{ X_{t}\}$ and the function space $\mathcal{F}$. The first assumption posits that the process $\{ X_{t}\}$ exhibits some mild form of ergodicity (that is significantly weaker than the typical geometric ergodicity assumption). The second assumption is a hypercontractivity condition that holds uniformly in $\mathcal{F}$ along the trajectory $\{ X_{t}\}$, extending contractivity assumptions for iid learning to dependent processes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Informally, our main result (Theorem 4.1, presented in Section 4), shows that under these two assumptions, letting $\text{comp}{(\mathcal{F})}$ denote some (inverse) measure of complexity of $\mathcal{F}$, the LSE $\hat{f}$ satisfies: The first term in (1.2) matches existing LSE risk bounds for iid learning order-wise, and most importantly, does not include any dependence on the mixing-time of the process. Indeed, all mixing-time dependencies enter only in the higher order term. Since this term scales as $o{({1/T^{\text{comp}{(\mathcal{F})}}})}$, it becomes negligible after a finite burn-in time. This captures the crux of our results: on a broad class of problems, given enough data, the LSE applied to time-series model (1.1) behaves as if all samples are independent.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Section 6 provides several examples for which the trajectory hypercontractivity assumption holds. When the covariate process $\{ X_{t}\}$ is generated by a finite-state irreducible and aperiodic Markov chain, then any function class $\mathcal{F}$ satisfies the requisite condition. More broadly, the condition is satisfied for any bounded function classes for which the $L^{2}$ and $L^{2 + \varepsilon}$ norms (along trajectories) are equivalent. Next, we show that many infinite dimensional function spaces based on $\ell^{2}{({\mathbb{N}})}$ ellipsoids satisfy our hypercontractivity condition, demonstrating that our results are not inherently limited to finite-dimensional hypothesis classes.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

To demonstrate the broad applicability of our framework, Section 7 instantiates our main result on two system identification problems that have received recent attention in the literature: linear dynamical systems (LDS), and systems with generalized linear model (GLM) transitions. For stable LDS, after a polynomial burn-in time, we recover an excess risk bound that matches the iid rate. A more general form of this result was recently established by Tu et al.. For stable GLMs, also after a polynomial burn-in time, we obtain the first excess risk bound for this problem which matches the iid rate, up to logarithmic factors in various problem constants including the mixing-time. In both of these settings, our excess risk bounds also yield nearly optimal rates for parameter recovery, matching known results for LDS and GLMs in the stable case. In Section 8, we show experimentally, using the stable GLM model, that the trends predicted by our theory are indeed realized in practice.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Nonparametric regression with iid data", "weight": 1.0} -->

Beyond the seminal work of Mendelson, the works all study iid regression with square loss under various moment equivalence conditions. In addition to moment equivalence, we build on the notion of offset Rademacher complexity defined by Liang et al. in the context of iid regression. Indeed, we show that a martingale analogue of the offset complexity (described in Ziemann et al. ) characterizes the LSE rate in (1.1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning from dependent data", "weight": 1.0} -->

As discussed previously, many existing results for learning from dependent data reduce the problem to independent learning via the blocking technique, at the expense of sample complexity deflation by the mixing-time. Nagaraj et al. prove a lower bound for linear regression stating that in a worst case agnostic model, this deflation is unavoidable. Moreover, if the linear regression problem is realizable, Nagaraj et al. provide upper and lower bounds showing that the mixing-time only affects the burn-in time, but not the final risk. We note that their upper bound is an algorithmic result that holds only for a specific modification of SGD. Our work can be interpreted as an upper bound in the more general nonparametric setting, where we put forth sufficient conditions to recover the iid rate after a burn-in time. Our result is algorithm agnostic and directly applies to the empirical risk minimizer. Ziemann et al. also study the model (1.1), and provide an information-theoretic analysis of the nonparametric LSE.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning from dependent data", "weight": 1.0} -->

However, their approach fundamentally reduces to showing two-sided concentration---something our work evades---and therefore their bounds incur worst case dependency on the mixing-time. Roy et al. extend the results from Mendelson to the dependent data setting. While following Mendelson's argument allows their results to handle non-realizability and heavy-tailed noise, their proof ultimately still relies on two-sided concentration for both the "version space" and the "noise interaction". Hence, their rates end up degrading for slower mixing processes. We note that this is actually expected in the non-realizable setting in light of the lower bounds in Nagaraj et al..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning from dependent data", "weight": 1.0} -->

The measure of dependencies we use for the process $\{ X_{t}\}$ is due to Samson. Recently, Dagan et al. use a similar measure to study learning when the covariates have no obvious sequential ordering (e.g., a graph structure or Ising model). However, our results are not directly comparable, other than noting that their risk bounds degrade as the measure of correlation increases.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning from dependent data", "weight": 1.0} -->

Results in linear system identification show that lack of ergodicity does not degrade parameter recovery rates. Beyond linear system identification, Sattar and Oymak; Foster et al.; Kowshik et al.; Gao and Raskutti prove parameter recovery bounds for dynamical systems driven by a generalized linear model (GLM) transition. Most relevant are Kowshik et al. and Gao and Raskutti, who again show that the lack of ergodicity does not hamper rates. Indeed, Gao and Raskutti even manage to do so in a semiparametric setting with an unknown link function. As mentioned previously, our main result instantiated to these problems in the stable case matches existing excess risk and parameter recovery bounds for linear system identification, and actually provides the sharpest known excess risk bound for the GLM setting (when the link function is known). A more detailed comparison to existing LDS results is given in Section 7.1, and to existing GLM results in Section H.1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We assume there exists a filtration $\{\mathcal{F}_{t}\}$ such that (a) $\{ W_{t}\}$ is a square integrable martingale difference sequence (MDS) with respect to this filtration, and (b) $\{ X_{t}\}$ is adapted to $\{\mathcal{F}_{t - 1}\}$. Further tail conditions on this MDS will be imposed as necessary later.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results", "weight": 1.0} -->

This section presents our main result. We first detail the definitions behind our main assumptions in Section 4.1. The main result and two corollaries are then presented in Section 4.2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Hypercontractivity", "weight": 1.0} -->

We first state our main trajectory hypercontractivity condition, which we will use to establish lower isometry. The following definition is heavily inspired by recent work on learning without concentration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Ergodicity via the dependency matrix", "weight": 1.0} -->

We now state the main definition we use to measure the stochastic dependency of a process. Recall that for two measures $\mu,\nu$ on the same measurable space with $\sigma$-algebra $\mathcal{A}$, the total-variation norm is defined as ${\|{\mu - \nu}\|}_{\mathsf{T}\mathsf{V}} \triangleq {\sup_{A \in \mathcal{A}}{|{{\mu{(A)}} - {\nu{(A)}}}|}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Learning with little mixing", "weight": 1.0} -->

A key quantity appearing in our bounds is a martingale variant of the notion of Gaussian complexity.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Lower isometry", "weight": 1.0} -->

The key tool we use is the following exponential inequality, which controls the lower tail of sums of non-negative dependent random variables via the dependency matrix $\Gamma_{\mathsf{d}\mathsf{e}\mathsf{p}}{(\mathsf{P}_{X})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Handling unbounded trajectories", "weight": 1.0} -->

Our main result Theorem 4.1 requires boundedness of both the hypothesis class $\mathcal{F}$ and the covariate process $\{ X_{t}\}$ to hold. However, when this does not hold, Theorem 4.1 can often still be applied via a careful truncation argument. In this section, we outline the key ideas of this argument, with the full details given in Appendix E.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Handling unbounded trajectories", "weight": 1.0} -->

Define the truncated noise process ${\{{\overline{W}}_{t}\}}_{t \geq 0}$ as ${\overline{W}}_{t} \triangleq {W_{t}'\mathbf{1}{\{{{\parallel W_{t}'\parallel}_{2} \leq R}\}}}$, and denote the original process and its truncated process: Setting $R$ appropriately, it is clear that the original process (5.4a) coincides with the truncated process (5.4b) with high probability by standard Gaussian concentration inequalities. Furthermore, the truncated noise process $\{{H{\overline{W}}_{t}}\}$ remains a martingale difference sequence due to the symmetry of the truncation. Additionally, since $\{{H{\overline{W}}_{t}}\}$ is bounded, if $f$ is appropriately Lypaunov stable then the process $\{{\overline{X}}_{t}\}$ becomes bounded.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Handling unbounded trajectories", "weight": 1.0} -->

In turn any class $\mathcal{F}$ containing continuous functions is bounded as well on (5.4b). Hence, the LSE $\hat{f}$ on (5.4a) can be controlled by the LSE $\overline{f}$ on (5.4b).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Handling unbounded trajectories", "weight": 1.0} -->

So far, this is a straightforward reduction. However, a subtle point arises in applying Theorem 4.1 to the LSE $\overline{f}$ on (5.4b): the dependency matrix $\Gamma_{\mathsf{d}\mathsf{e}\mathsf{p}}$ now involves the truncated process (5.4b) instead of the original process (5.4a). This is actually *necessary* for this strategy to work, as the supremum in the dependency matrix coefficients (4.2). ‣ Ergodicity via the dependency matrix ‣ 4.1 Hypercontractivity and the dependency matrix ‣ 4 Results ‣ Learning with little mixing")) is now over the truncated process $\{{\overline{X}}_{t}\}$, instead of the original process $\{ X_{t}\}$ which is unbounded.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Handling unbounded trajectories", "weight": 1.0} -->

However, there is a trade-off, as bounding the coefficients for $\{{\overline{X}}_{t}\}$ is generally more complex than for $\{ X_{t}\}$.^44^4The clearest example of this is when the dynamics function $f$ is linear: in this case, $\{ X_{t}\}$ is jointly Gaussian (and hence (4.2). ‣ Ergodicity via the dependency matrix ‣ 4.1 Hypercontractivity and the dependency matrix ‣ 4 Results ‣ Learning with little mixing")) can be bounded by closed-form expressions), whereas $\{{\overline{X}}_{t}\}$ is not due to the truncation operator. Nevertheless, a coupling argument allows us to switch back to bounding the dependency matrix coefficients for $\{ X_{t}\}$, but crucially keep the supremum over the truncated $\{{\overline{X}}_{t}\}$. This reduction substantially broadens the scope of Theorem 4.1 without any modification to the proof.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Examples of trajectory hypercontractivity", "weight": 1.0} -->

Similarly, processes evolving on a finite state space can also be verified to be hypercontractive.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Ellipsoids in $\\ell^{2}{({\\mathbb{N}})}$", "weight": 1.0} -->

Given that equivalence of norms is typically a finite-dimensional phenomenon, one may wonder whether examples of hypercontractivity exist in an infinite-dimensional setting. Here we show that such examples are actually rather abundant. The key is that hypercontractivity need only be satisfied on an $\varepsilon$-cover of $\mathcal{F}_{\star}$. As discussed above, every finite hypothesis class (and thus every finite cover) is automatically $(C,2)$-hypercontractive for some $C > 0$. The issue is to ensure that this constant does not grow too fast as one refines the cover. The next result shows that the growth can be controlled for $\ell^{2}{({\mathbb{N}})}$ ellipsoids of orthogonal expansions. By Mercer's theorem, these ellipsoids correspond to unit balls in reproducing kernel Hilbert spaces.

<!-- chunk {"id": "body-0030", "role": "body", "section": "System identification in parametric classes", "weight": 1.0} -->

To demonstrate the sharpness of our main result, we instantiate Theorem 4.1 on two parametric system identification problems which have received recent attention in the literature: linear dynamical systems (LDS) and generalized linear model (GLM) dynamics.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linear dynamical systems", "weight": 1.0} -->

Consider the setting where the process ${\{ X_{t}\}}_{t \geq 0}$ is described by a linear dynamical system: In this setting, the system identification problem is to recover the dynamics matrix $A_{\star}$ from ${\{ X_{t}\}}_{t = 0}^{T - 1}$ evolving according to (7.1). We derive rates for recovering $A_{\star}$ by first deriving an excess risk bound on the least-squares estimator via Theorem 4.1, and then converting the risk bound to a parameter error bound. Since Theorem 4.1 relies on the process being ergodic, we consider the case when $A_{\star}$ is stable. We start by stating a few standard definitions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Generalized linear models", "weight": 1.0} -->

We next consider the following non-linear dynamical system: Here, $A_{\star} \in {\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{X}}}$ is the dynamics matrix and $\sigma:{{\mathbb{R}}^{d_{\mathsf{X}}}\rightarrow{\mathbb{R}}^{d_{\mathsf{X}}}}$ is a coordinate wise link function. The notation $\sigma$ will also be overloaded to refer to the individual coordinate function mapping ${\mathbb{R}}\rightarrow{\mathbb{R}}$. We study the system identification problem where the link function $\sigma$ is assumed to be known, but the dynamics matrix $A_{\star}$ is unknown and to be recovered from ${\{ X_{t}\}}_{t = 0}^{T - 1}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Generalized linear models", "weight": 1.0} -->

We will apply Theorem 4.1 to derive a nearly optimal excess risk bound for the LSE on this problem in the stable case.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Generalized linear models", "weight": 1.0} -->

We start by stating a few assumptions that are again standard in the literature.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 7.1", "weight": 1.0} -->

Suppose that $A_{\star}$, $H$, and $\sigma$ from the GLM process (7.6) satisfy: (One-step controllability). The matrix $H \in {\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{X}}}$ is full rank.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 7.1", "weight": 1.0} -->

Several remarks on 7.1 are in order. First, the rank condition on $H$ ensures that the noise process ${\{{HV_{t}}\}}_{t \geq 0}$ is non-degenerate. Viewing (7.6) as a control system mapping ${\{ V_{t}\}}_{t \geq 0}\mapsto{\{ X_{t}\}}_{t \geq 0}$, this condition ensures that this system is one-step controllable. Next, the link function assumption is standard in the literature (see e.g. Sattar and Oymak; Foster et al.; Kowshik et al. ). The expansiveness condition ${|{{\sigma{(x)}} - {\sigma{(y)}}}|} \geq {\zeta{|{x - y}|}}$ ensures that the link function is increasing at a uniform rate. For efficient parameter recovery, some extra assumption other than Lipschitzness and monotonicity is needed, and expansiveness yields a sufficient condition.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 7.1", "weight": 1.0} -->

However, for excess risk, it is unclear if any extra requirements are necessary. We leave resolving this issue to future work. Finally, the Lyapunov stability condition is due to Foster et al., and yields a certificate for global exponential stability (GES) to the origin. It is weaker than requiring that ${\| A_{\star}\|}_{\mathsf{o}\mathsf{p}} < 1$, which amounts to taking $P_{\star} = I$. The assumption $P_{\star} \succcurlyeq I$ is without loss of generality by rescaling $P_{\star}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 7.1", "weight": 1.0} -->

With our assumptions in place, we are ready to state our main result concerning the excess risk for the LSE applied to the process (7.6).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We conduct a simple numerical simulation to illustrate the phenomenon of learning with little mixing empirically. We consider system identification of the GLM dynamics described in Section 7.2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

This ensures that the $L^{2}$ risk of a fixed hypothesis ${f{(x)}} = {\sigma{({Ax})}}$ is the same under both the independent baseline and the single trajectory distribution, so that our experiment singles out the effect of learning from correlated data. In practice, each ${\overline{X}}_{t}$ is sampled from a new independent rollout up to time $t$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Given a dataset ${\{{(X_{t},Y_{t})}\}}_{t = 0}^{T - 1}$, we search for the empirical risk minimizer (ERM) of the loss by running scipy.optimize.minimize with the L-BFGS-B method, using the default linesearch and termination criteria options. To calculate the $L^{2}$ excess risk $\frac{1}{T}{\sum_{t = 0}^{T - 1}{\mathbf{E}{\parallel{{\sigma{({\hat{A}X_{t}})}} - {\sigma{({A_{\star}X_{t}})}}}\parallel}_{2}^{2}}}$ of a hypothesis $\hat{A}$, we draw $1000$ new trajectories and average the excess risk over these trajectories.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The experimental code is implemented with jax, and run using the CPU backend with float64 precision on a single machine.^66^6Code available: Figure 1: L2 excess risk as a function of dataset length T of the empirical risk minimizer on the single trajectory (Trajectory) dataset versus the independent baseline (Ind Baseline) dataset.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The results of this experiment are shown in Figure 1 and Figure 2. In Figure 1, we plot the $L^{2}$ excess risk of the ERM $\hat{A}$ from (8.1) on both the trajectory dataset $\{{(X_{t},Y_{t})}\}$ and the independent baseline dataset $\{{({\overline{X}}_{t},{\overline{Y}}_{t})}\}$, varying $\rho \in {\{ 0.9,0.99\}}$. The shaded region indicates $\pm$ one standard deviation from the mean over $20$ training datasets. In Figure 2, we plot the $L^{2}$ excess risk *ratio* of the estimator $\hat{A}$ from the single trajectory dataset over the estimator $\hat{A}$ from the independent baseline trajectory, again varying $\rho \in {\{ 0.9,0.99\}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Here, the shaded region is constructed using $\pm$ one standard deviation of the numerator and denominator taken over $20$ training datasets.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed a framework for showing when the mixing-time of the covariates plays a relatively small role in the rate of convergence of the least-squares estimator. In many situations, after a finite burn-in time, this learning procedure exhibits an excess risk that scales as if all the samples were independent (Theorem 4.1). As a byproduct of our framework, by instantiating our results to system identification for dynamics with generalized linear model transitions (Section 7.2), we derived the sharpest known excess risk rate for this problem; our rates are nearly minimax optimal after only a polynomial burn-in time.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

To arrive at Theorem 4.1, we leveraged insights from Mendelson via a one-sided concentration inequality (Theorem 5.2). As mentioned in Section 4.1, hypercontractivity is closely related to the small-ball condition. Such conditions can be understood as quantitative identifiability conditions by providing control of the "version space" (cf. Mendelson ). Given that identifiability conditions also play a key role in linear system identification---a setting in which a similar phenomenon as studied here had already been reported---this suggests an interesting direction for future work: are such conditions actually necessary for learning with little mixing?
