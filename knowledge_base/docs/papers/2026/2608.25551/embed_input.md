<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic gradient descent (SGD) is typically analyzed at a deterministic horizon chosen before the algorithm is run, even though practical stopping decisions are made adaptively by inspecting the evolving trajectory. This mismatch creates a fundamental certification problem: fixed-time guarantees do not generally remain valid at data-dependent stopping times, while deterministic horizons derived from worst-case bounds can be highly conservative. We address this problem for strongly convex stochastic optimization by constructing fully observable, trajectory-adaptive upper confidence sequences for the squared distance of the last iterate to the optimizer and the suboptimality of a weighted average. These bounds hold simultaneously over time, attain the optimal 1/t decay rate up to iterated-logarithmic factors in the worst case, and adapt to the realized stochastic gradients, allowing SGD to stop as soon as a prescribed accuracy is certified without sacrificing statistical validity. Our approach treats the evolving SGD trajectory as a sequential experiment whose observations provide evidence about the unknown optimization error.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To formalize this perspective, we develop new recursive confidence-sequence techniques and a general time-uniform empirical Bernstein inequality for adapted processes with time-varying conditional means and predictable ranges that may grow without bound. We further extend these confidence-sequence constructions to minibatch SGD, with the empirical Bernstein bounds exploiting the realized second-moment structure within each minibatch. Numerical experiments show that the resulting stopping rules can require several orders of magnitude fewer iterations than natural deterministic horizons.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic optimization is a foundational computational paradigm across machine learning, operations research, statistics, and scientific computing. When objectives are expectations under unknown distributions or finite sums over prohibitively large datasets, stochastic gradient methods make optimization possible using only samples or noisy first-order information. Their scalability has made them the principal computational workhorses of modern machine learning. Yet a basic operational question remains unresolved: *when should a stochastic optimization algorithm stop?* Existing theoretical analyses of stochastic gradient descent (SGD) are predominantly *ex ante*. Before the algorithm is run, one specifies a stepsize schedule and a deterministic horizon $T$, and then studies its performance at that horizon. This perspective has produced a deep understanding of stochastic first-order methods: it has identified optimal rates, clarified the roles of averaging and strong convexity, and provided principled guidance for selecting stepsizes. Its guarantees, however, are attached to horizons chosen independently of the realized run.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In other words, they answer the forward-looking question of what can be guaranteed if SGD is run until a predetermined time $T$, but not the online question of whether the trajectory observed so far provides enough evidence that the algorithm should stop.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, however, this online question is unavoidable. Practitioners alter stepsizes when progress slows and stop a run when the observed trajectory appears to have stabilized. Yet the quantities that would directly certify optimization progress are usually unknown: the objective is often a population loss defined by an expectation under an unknown distribution, and its optimizer and optimal value are unknown. Consequently, neither the true suboptimality nor the distance to the optimizer is directly observable during the run. Practitioners therefore rely on observable proxies, such as empirical losses computed from validation samples, and use these proxies together with the evolving stochastic trajectory to decide whether to tune, continue, or stop the algorithm. These proxies are themselves random and dependent on the particular samples used to construct them. They may be informative, but favorable behavior of a proxy is not itself a certificate for suboptimality or distance to the optimizer.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing fixed-horizon guarantees do not certify this adaptive mode of operation: a high-probability statement proved at a deterministic time $T$ does not, in general, remain valid at a data-dependent stopping time selected after repeatedly inspecting the iterates, stochastic gradients, or validation losses. The stochastic-oracle assumptions may remain unchanged, but the stopping time is now coupled to the random fluctuations revealed along the observed run. Among the many iterations examined, an unusually favorable fluctuation may be precisely what triggers termination. Therefore, a guarantee calibrated for one predetermined time does not automatically account for this selection over time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

One can preserve validity by fixing the stopping horizon in advance. Given a fixed-time high-probability bound and a target accuracy $\varepsilon$, one may solve for a time $T_{\varepsilon}$ at which the bound falls below $\varepsilon$, and then run SGD for exactly that many iterations. This produces a valid certified stopping rule, but typically a very conservative one. Because $T_{\varepsilon}$ is obtained by inverting a worst-case guarantee before the trajectory is observed, it reflects the most adverse behavior permitted by the assumptions rather than the behavior of the realized run. In practice, SGD can perform substantially better than these guarantees predict, sometimes by several orders of magnitude, so the resulting deterministic horizon may require many more iterations than would be sufficient on the realized run. This limitation is not resolved by choosing a stepsize schedule that attains the optimal worst-case rate: such optimality describes performance over a broad problem class, whereas stopping asks whether the particular run has already reached a prescribed accuracy. Existing theory is therefore indispensable for ex ante algorithm design, but it is not itself an online stopping mechanism.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This leaves a clear gap between rigorous but potentially conservative fixed-horizon guarantees and adaptive early-stopping procedures that generally lack a certificate. Bridging this gap requires more than another fixed-time convergence bound. It requires a theory in which the evolving trajectory is itself allowed to determine, with statistical validity, when sufficient progress has been made. This suggests a different perspective on stochastic optimization: a running SGD trajectory can be viewed as a *sequential experiment*. Its iterates and stochastic gradients do not merely update the decision variable; they also provide evidence about the unknown optimization error. The stopping problem then becomes one of determining whether the observed trajectory has produced enough evidence to certify that a prescribed accuracy has been reached. This leads to the central question of the paper: *Can SGD certify, from its own realized trajectory, when it should stop?* The statistical theory underlying this question has deep roots in anytime-valid sequential inference, which studies how to construct inferential guarantees that remain valid when observations are examined sequentially and the decision to continue or stop depends on what has already been observed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the present setting, the relevant objects are confidence sequences: observable, trajectory-dependent upper bounds that, with high probability, bound a target quantity, such as suboptimality or distance to the optimizer, simultaneously at every iteration. SGD may therefore be monitored continuously and stopped at the first time the bound falls below a prescribed tolerance, while the certificate remains valid at the selected stopping time. Constructing sharp confidence sequences for SGD requires optimization-specific tools because the unknown errors evolve recursively with the iterates and are driven by the same stochastic gradients from which the certificates must be constructed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A first step toward meeting this challenge was taken by Aolaritei and Jordan, who developed anytime-valid confidence sequences and certified stopping rules for SGD under general convexity and smooth nonconvexity. Specifically, that work constructed fully observable certificates for suboptimality in the convex setting and for stationarity in the smooth nonconvex setting. These certificates allow the algorithm to be monitored continuously and stopped at a data-dependent time while retaining a valid guarantee.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the present paper, we substantially expand this line of work by developing a considerably sharper theory for strongly convex stochastic optimization that exploits the contractive structure of the dynamics. Retaining trajectory adaptivity and time-uniform validity in this setting requires new constructions, including a recursive confidence-sequence argument and an empirical Bernstein theory for adapted processes with time-varying conditional means and growing predictable ranges. The resulting fully observable certificates bound the squared distance of the last iterate to the optimizer and the suboptimality of a weighted-average iterate. They recover the canonical $1/t$ rate, up to the generally unavoidable $\log\log t$ factors associated with time-uniform validity, and adapt to the stochastic behavior observed along the realized trajectory. In our numerical experiments, the corresponding stopping rules terminate orders of magnitude earlier than natural deterministic horizons obtained by inverting conventional fixed-time guarantees.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We consider stochastic optimization problems of the form where $\mathcal{X}\subseteq\mathbb{R}^{d}$ is a closed convex set and $f:\mathcal{X}\to\mathbb{R}$ is differentiable.^11^ 1 The analysis extends directly to the nondifferentiable setting by replacing gradients and stochastic gradients with subgradients and stochastic subgradients, respectively. Throughout, we assume that the objective satisfies the following condition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1.1 (Strong convexity)", "weight": 1.0} -->

The function $f$ is $\mu$-strongly convex on $\mathcal{X}$, meaning that Under Assumption 1.1. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), the minimizer is unique; we denote it by $x^{\star}$. We study projected stochastic gradient descent (SGD), defined recursively by and initialized from $x_{1}\in\mathcal{X}$ almost surely. Here, $\Pi_{\mathcal{X}}$ denotes the Euclidean projection onto $\mathcal{X}$, $\{g_{t}\}_{t\geq 1}$ are stochastic gradients, and $\{\eta_{t}\}_{t\geq 1}$ is a stepsize sequence. We work with the natural filtration Thus, $\mathcal{F}_{t}$ contains the complete SGD trajectory observed through iteration $t$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1.1 (Strong convexity)", "weight": 1.0} -->

We assume that each stepsize is selected using only information available before the corresponding stochastic gradient is observed.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1.2 (Predictable stepsizes)", "weight": 1.0} -->

Assumption 1.2. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") permits both deterministic and data-dependent stepsize rules, provided they depend only on the past trajectory. It includes constant and diminishing schedules, as well as adaptive choices based on previously observed iterates and stochastic gradients (e.g., AdaGrad-type schedules and related adaptive methods ). The stochastic gradients satisfy the following standard unbiasedness and tail conditions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1.3 (Stochastic gradients)", "weight": 1.0} -->

For every $t\geq 1$, the stochastic gradient $g_{t}$ satisfies: *Conditional sub-Gaussian noise:* defining $\xi_{t}\coloneqq g_{t}-\nabla f(x_{t})$, there exists a constant $\sigma^{2}>0$ such that, for every $\lambda\in\mathbb{R}$ and every $u\in\mathbb{R}^{d}$, Assumption 1.3. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")(i) is the standard conditional unbiasedness requirement in stochastic approximation. Assumption 1.3. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")(ii) imposes a conditional sub-Gaussian bound on the gradient noise while allowing its distribution to vary along the trajectory. This condition is satisfied by Gaussian and many light-tailed noise models.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1.3 (Stochastic gradients)", "weight": 1.0} -->

It also holds whenever $\left\|g_{t}\right\|\leq G$ almost surely, in which case one may take $\sigma^{2}=G^{2}$ by the conditional Hoeffding lemma.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1.3 (Stochastic gradients)", "weight": 1.0} -->

To ensure that the resulting contraction factors are positive, we impose an upper bound on the stepsizes after an initial period.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1.4 (Upper bound on stepsizes)", "weight": 1.0} -->

There exists a deterministic integer $t_{0}\geq 1$ such that Assumption 1.4. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") is satisfied by the standard diminishing stepsize schedules used for strongly convex stochastic optimization. It is imposed only from the deterministic time $t_{0}$ onward, allowing arbitrary predictable stepsizes during the initial phase of the algorithm. The index $t_{0}$ serves as the starting point of our time-uniform analysis.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1.4 (Upper bound on stepsizes)", "weight": 1.0} -->

Our goal is to provide *anytime-valid, trajectory-adaptive guarantees* for the progress of SGD. Given the stochastic gradients, predictable stepsizes, and observed iterates, we seek upper bounds on suitable performance measures that remain valid simultaneously over the entire run. We formalize this objective through the following definition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our main contributions can be summarized as follows: Confidence sequences under sub-Gaussian noise. Through a time-uniform Hoeffding argument, we construct fully observable, trajectory-adaptive confidence sequences for the two performance measures introduced above. These confidence sequences can be computed online from the observed stochastic gradients and stepsizes. In the worst case, they match the optimal $1/t$ rate for strongly convex stochastic optimization, up to the iterated-logarithmic cost of time-uniform validity, while remaining sensitive to the observed trajectory and therefore potentially smaller than the corresponding worst-case bounds.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contributions", "weight": 1.0} -->

Squared distance to the optimizer. We construct an anytime-valid upper confidence sequence $\bigl\{\widehat{U}^{\mathrm{dist}}_{t+1}(\alpha)\bigr\}_{t\geq t_{0}}$ whose stochastic term depends explicitly on the conditional sub-Gaussian variance proxy $\sigma^{2}$. If $\left\|g_{t}\right\|\leq G$ almost surely and $\eta_{t}=1/(\mu t)$, then its worst-case decay satisfies Weighted average suboptimality.^22^ 2 The same approach can be adapted to other averaging schemes, such as uniform averaging. We use linearly increasing weights because they yield the optimal $O(1/t)$ rate, whereas uniform averaging incurs an additional logarithmic factor and achieves an $O(\log t/t)$ rate.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Contributions", "weight": 1.0} -->

Building on the observable distance confidence sequence, we construct an anytime-valid upper confidence sequence $\bigl\{\widehat{U}^{\mathrm{sub}}_{t}(\alpha)\bigr\}_{t\geq t_{0}}$ for weighted average suboptimality. If $\left\|g_{t}\right\|\leq G$ almost surely and $\eta_{t}=2/(\mu(t+1))$, then its worst-case decay satisfies Refined confidence sequences under bounded stochastic gradients. Through a novel time-uniform empirical Bernstein argument (see item (iv)), we refine both confidence sequences under the assumption that $\left\|g_{t}\right\|\leq G$ almost surely.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Contributions", "weight": 1.0} -->

The resulting bounds replace the fixed worst-case variance proxy $\sigma^{2}=G^{2}$ in the Hoeffding construction by the realized squared stochastic-gradient magnitudes $\left\|g_{t}\right\|^{2}$, together with an additional correction that decays at the faster $t^{-3/2}$ rate, up to iterated-logarithmic factors. The refined confidence sequences are fully observable and preserve the worst-case rates in equations (8 ‣ 1.2 Contributions ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")) and (9 ‣ 1.2 Contributions ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")). At the same time, they adapts more sharply to the observed trajectory: in our numerical experiments, the resulting confidence sequences are generally one order of magnitude smaller than their Hoeffding-based counterparts. This refinement constitutes the central contribution of the paper.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Contributions", "weight": 1.0} -->

Minibatch extensions. We extend both constructions to minibatch SGD with $b$ conditionally independent stochastic gradients per iteration. For the Hoeffding confidence sequences, minibatching reduces the conditional sub-Gaussian variance proxy from $\sigma^{2}$ to $\sigma^{2}/b$. For the empirical Bernstein confidence sequences, we develop a minibatch analogue that pools the observed quadratic variation of the individual stochastic gradients and adapts to the largest eigenvalue of the realized second-moment matrix of each minibatch. The minibatch empirical Bernstein boundary has a leading term that improves at the usual $1/\sqrt{b}$ rate, together with a lower-order correction that improves at the faster $1/b$ rate. In our numerical experiments, the improvement relative to the corresponding worst-case bounds grows with the minibatch size, reaching between two and three orders of magnitude for the larger minibatch sizes considered.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Contributions", "weight": 1.0} -->

The gap relative to existing ex ante guarantees with explicit constants can be substantially larger still; see Figure 4 ‣ 1.2 Contributions ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Contributions", "weight": 1.0} -->

A time-uniform empirical Bernstein inequality with growing predictable range. To support the refinement in item (ii), we establish a general time-uniform empirical Bernstein inequality for adapted processes with time-varying conditional means and predictable increment ranges that may grow without bound. This feature is essential for our SGD application: in both the squared-distance and weighted-average suboptimality analyses, the relevant predictable ranges can scale as $\sqrt{t}$ under the worst-case convergence rate. Existing empirical Bernstein confidence-sequence constructions, such as [Howard et al. \[24, Theorem 4\]](#bib.bib1), allow the conditional means to vary but assume a fixed range scale, and therefore do not directly cover this setting. When the predictable range evolves over time, the admissible exponential parameter evolves with it. Starting from the pointwise exponential inequality of [Fan et al. \[15, Lemma 4.1\]](#bib.bib21), we overcome this difficulty through predictable truncation and simultaneous stitching over dyadic scales of the observed quadratic process and the running predictable range.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Contributions", "weight": 1.0} -->

The resulting explicit boundary adapts jointly to both quantities and is nondecreasing in each of them.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Organization and notation", "weight": 1.0} -->

Organization. Section 2 develops our confidence sequences under conditional sub-Gaussian noise using a time-uniform Hoeffding argument. Section 3 refines these constructions under bounded stochastic gradients through a time-uniform empirical Bernstein approach. Section 4 extends both approaches to minibatch SGD. Finally, Section 5 numerically evaluates the resulting confidence sequences and their certified stopping rules. All proofs are deferred to Appendix A.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Confidence Sequences under Sub-Gaussian Noise", "weight": 1.0} -->

We construct anytime-valid upper confidence sequences for the two performance measures of interest: the last-iterate squared distance $Z_{t+1}$ and the suboptimality of the weighted-average iterate, $f(\bar{x}_{t})-f(x^{\star})$. Although the two guarantees arise from different SGD recursions, both reduce to controlling partial sums of directional gradient noise terms. We first isolate the common time-uniform concentration argument, then construct the observable distance confidence sequence, which will in turn be used to make the suboptimality confidence sequence fully observable.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Confidence Sequences under Sub-Gaussian Noise", "weight": 1.0} -->

The common probabilistic ingredient underlying both constructions is a conditional exponential moment bound of sub-Gaussian form. Consider an adapted sequence of real-valued random variables $\{X_{t}\}_{t\geq t_{0}}$ and a nonnegative predictable sequence $\{v_{t}\}_{t\geq t_{0}}$. Suppose that, for some $\gamma\in\mathbb{R}$, for every $\lambda>0$ and every $t\geq t_{0}$. The predictable quantity $v_{t}$ serves as a conditional variance proxy for $X_{t}$, using only information available before $X_{t}$ is observed, while $\gamma$ records the constant arising in the particular application. For each fixed $\lambda>0$, the conditional exponential bound implies that is a nonnegative supermartingale. The cumulative variance proxy $\sum_{s=t_{0}}^{t}v_{s}$ records the conditional fluctuation scale accumulated over the process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Confidence Sequences under Sub-Gaussian Noise", "weight": 1.0} -->

In sequential inference, such a cumulative process is often called an *intrinsic time*: the scale of the concentration boundary for the partial sum adapts to the accumulated variance proxy, rather than being indexed solely by the iteration count.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Confidence Sequences under Sub-Gaussian Noise", "weight": 1.0} -->

This exponential supermartingale is the starting point for a time-uniform concentration bound. Ville's inequality controls its running maximum and, after rearranging, yields for each fixed $\lambda>0$ a linear upper boundary for the partial sums that holds simultaneously over time. No single choice of $\lambda$, however, is well calibrated across all possible scales of the intrinsic time: different values of $\lambda$ yield sharper boundaries in different ranges of the cumulative variance proxy. Dyadic stitching combines these fixed-$\lambda$ boundaries over successive dyadic scales, while allocating the error probability across the scales. The result is a curved boundary that adapts to the realized intrinsic time and remains valid uniformly over the infinite horizon.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Confidence Sequences under Sub-Gaussian Noise", "weight": 1.0} -->

The following lemma formalizes this construction in the precise form used throughout the section. It is a dyadic specialization of the stitching framework developed by Howard et al..

<!-- chunk {"id": "body-0036", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

We begin by constructing an upper confidence sequence for the last-iterate squared distance to the optimizer. Recall from that $Z_{t}=\left\|x_{t}-x^{\star}\right\|^{2}$. To account for the time-varying contraction induced by strong convexity, define By Assumption 1.4. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), $a_{t}\in$ almost surely for every $t\geq t_{0}$, so $A_{t}$ is well defined. Following the notation of Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), for $t\geq t_{0}$ define the adapted term With these definitions, Lemma C.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") yields the following decomposed upper bound on the last-iterate distance: for every $t\geq t_{0}$, This decomposition follows from the standard squared-distance Lyapunov argument for projected stochastic approximation; see, e.g., [Nemirovski et al. \[32, Section 2.1\]](#bib.bib2). A closely related unrolling of the contractive SGD recursion for the classical stepsize $\eta_{t}=1/(\mu t)$ appears in [Rakhlin et al. \[36, Appendix B.7, Lemma 6\]](#bib.bib8); the decomposition records the same telescoping mechanism for general predictable stepsizes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

Thus, following, the last-iterate distance to the optimizer is controlled by an initialization term, an observable accumulation of squared stochastic gradients, and a partial sum of directional gradient noise terms. A time-uniform bound on $\bar{X}_{t}$ therefore translates directly into an upper confidence sequence for $Z_{t+1}$. To control this partial sum, define The sequence $\{v_{t}^{\mathrm{dist}}\}$ is predictable because $x_{t}$, $\eta_{t}$, and $A_{t}$ are $\mathcal{F}_{t-1}$-measurable. Applying the conditional sub-Gaussian bound in Assumption 1.3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")(ii) with the predictable direction $2A_{t}\eta_{t}(x^{\star}-x_{t})$ gives for every $\lambda\geq 0$ and every $t\geq t_{0}$. Thus, $v_{t}^{\mathrm{dist}}$ is the predictable intrinsic-time increment in the generic construction, and Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") applies with $\gamma=1$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

To express the resulting confidence sequences compactly, for $v\geq 0$ define and, for $\alpha\in$, let The function $\mathfrak{H}_{\alpha}$ collects the common dependence of the stitched boundaries on the intrinsic time and its dyadic scale, and is nondecreasing in $v$. For the distance process, define This is the cumulative intrinsic time associated with the directional gradient noise terms. Since the conditional exponential bound corresponds to $\gamma=1$, Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") guarantees that simultaneously for every $t\geq t_{0}$ with probability at least $1-\alpha$. Combining this bound with gives the following proposition.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2.5 (Decay rate under the diameter-based observable bound)", "weight": 1.0} -->

Suppose the conditions of Proposition 2.4. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") hold and that $\mathcal{X}$ is compact with diameter $D$, so that $Z_{t}\leq D^{2}$. Then, under $\eta_{t}=1/(\mu t)$ with $t_{0}=3$ and $A_{t}=t(t-1)/2$, Consequently, using the monotonicity of $\mathfrak{H}_{\alpha}$, Thus, directly replacing the distances $Z_{t}$ by the diameter bound yields only a $t^{-1/2}$-type decay, up to stitched-logarithmic factors, whereas the recursive observable envelope preserves the near-$1/t$ rate.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2.5 (Decay rate under the diameter-based observable bound)", "weight": 1.0} -->

$\clubsuit$ The preceding proposition was stated for the stepsize $\eta_{t}=1/(\mu t)$. In the sequel, it is also useful to have the analogous rate statement for the common alternative schedule $\eta_{t}=2/(\mu(t+1))$. We record this variant here.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2.6 (Alternative polynomial stepsize)", "weight": 1.0} -->

The same rate conclusion holds for the stepsize In this case, $1-2\mu\eta_{t}=(t-3)/(t+1)$, so the natural analysis start time is $t_{0}=4$. Following similar steps to those in the proof of Proposition 2.4. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), there exists a universal constant $C<\infty$ such that, for every $t\geq 4$, The proof is similar to the proof of Proposition 2.4. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") and is omitted. $\clubsuit$

<!-- chunk {"id": "body-0044", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

We next consider the suboptimality of the weighted-average iterate and construct an upper confidence sequence for $f(\bar{x}_{t})-f(x^{\star})$. Recalling the definitions in and, the analysis follows the same basic structure as for the last-iterate distance to the optimizer: the objective gap is bounded by an initialization term, an observable accumulation of squared stochastic gradients, and a partial sum of directional gradient noise terms that can again be controlled using Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules").

<!-- chunk {"id": "body-0045", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

For this construction, we take $t_{0}\geq 4$ and specialize to the stepsize $\eta_{t}=2/(\mu(t+1))$ considered in Remark 2.6. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"). This choice is naturally aligned with the linear weights defining $\bar{x}_{t}$: after the one-step suboptimality inequality is weighted by $t$, the resulting distance terms telescope across consecutive times. Define The resulting weighted decomposition is recorded in Lemma C.3. ‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") and gives This decomposition follows from the standard weighted telescoping argument for strongly convex SGD; see [Lacoste-Julien et al. \[26, Section 3.2\]](#bib.bib24).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

We retain the directional gradient-noise term explicitly, rather than taking expectations, for the anytime-valid analysis.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

The first term on the right-hand side of is observable from the SGD trajectory, the second is an initialization term, and the final term accumulates the gradient noise in the directions $x^{\star}-x_{t}$. Thus, as in the distance analysis, a time-uniform upper bound on $\bar{E}_{t}$ translates directly into an upper confidence sequence for the weighted-average suboptimality.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

To control this final term, define the predictable intrinsic-time increment The sequence $\{E_{t}\}$ is adapted, while $\{v_{t}^{\mathrm{sub}}\}$ is predictable because $x_{t}$ is $\mathcal{F}_{t-1}$-measurable. Applying the conditional sub-Gaussian bound in Assumption 1.3. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")(ii) with the predictable direction $t(x^{\star}-x_{t})$ yields for every $\lambda\geq 0$ and every $t\geq t_{0}$. Since the coefficient in the conditional exponent is $1/2$, this is precisely the setting of Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") with $\gamma=-1$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

Using the notation in and the stitched-boundary function, define, for every $t\geq t_{0}$, In this application, $V_{t}^{\mathrm{sub}}$ is the cumulative intrinsic time associated with the weighted directional-noise terms. Since the conditional exponential bound corresponds to $\gamma=-1$, Lemma 2.1. ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") guarantees that simultaneously for every $t\geq t_{0}$ with probability at least $1-\alpha$. Combining this bound with gives the following proposition.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Refined Confidence Sequences under Bounded Gradients", "weight": 1.0} -->

The preceding section constructed anytime-valid upper confidence sequences for the last-iterate squared distance $Z_{t+1}$ and the suboptimality of the weighted-average iterate, $f(\bar{x}_{t})-f(x^{\star})$, under a conditional sub-Gaussian assumption on the gradient noise. Under bounded stochastic gradients, conditional Hoeffding's lemma verifies this assumption with $\sigma^{2}=G^{2}$, so those confidence sequences remain valid. With this choice, however, the intrinsic times entering the observable distance and suboptimality confidence sequences are driven by the worst-case proxy $G^{2}$ and therefore do not adapt to the realized magnitudes of the stochastic gradients. Because $G$ is a uniform bound, it can be substantially larger than the gradient magnitudes observed along a typical trajectory, making the stochastic contribution to the resulting certificates unnecessarily large.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Refined Confidence Sequences under Bounded Gradients", "weight": 1.0} -->

The natural refinement is to let the stochastic boundaries respond to the gradients actually observed along the trajectory. Under the bounded-gradient assumption, an empirical Bernstein construction makes this possible by replacing the fixed proxy $G^{2}$ with quadratic processes involving the realized values of $\left\|g_{t}\right\|^{2}$. The relevant directional terms, however, have ranges that evolve with the SGD trajectory, so a fixed-range empirical Bernstein bound is not sufficient for our purposes. We therefore develop a time-uniform empirical Bernstein inequality for a growing predictable range, which will provide the common concentration argument for both the last-iterate distance and weighted-average suboptimality. This development builds on the empirical Bernstein supermartingale construction of Howard et al. and the exponential inequality of Fan et al. underlying it. As emphasized, this approach is technically closer to the literature on self-normalized bounds than to classical empirical Bernstein arguments such as Maurer and Pontil. The latter combine a concentration bound for the sample mean involving the true variance with a separate concentration bound for the sample variance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Refined Confidence Sequences under Bounded Gradients", "weight": 1.0} -->

By contrast, Howard et al. construct an exponential supermartingale that directly relates the centered process to an online empirical variance.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Refined Confidence Sequences under Bounded Gradients", "weight": 1.0} -->

We impose the following assumption throughout this section.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 3.1 (Bounded stochastic gradients)", "weight": 1.0} -->

There exists $G<\infty$ such that As shown, Assumption 3.1. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") always yields the observable initialization $R_{0}=G^{2}/\mu^{2}$. This universal choice will be used below, although sharper observable bounds on $Z_{t_{0}}$ may be available in specific applications and can be substituted directly into the construction.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 3.1 (Bounded stochastic gradients)", "weight": 1.0} -->

The concentration mechanism remains the same as in the preceding section: a one-step conditional exponential bound is lifted to a time-uniform boundary through a supermartingale argument and stitching. What changes is the compensating term. Rather than using a predictable variance proxy, the empirical Bernstein inequality below uses the realized square of the increment itself. This is the key mechanism that will allow the resulting confidence sequences to adapt to the stochastic gradients observed along the trajectory.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 3.1 (Bounded stochastic gradients)", "weight": 1.0} -->

The following lemma isolates this one-step ingredient in the precise form needed below. Starting from a pointwise exponential inequality, it yields after conditional centering a bound in which the quadratic compensation depends on the realized square $X^{2}$, while the admissible tuning parameter is restricted by the increment range $b$. These two features will drive the time-uniform construction that follows. To state the lemma, for $\theta\in[0,1)$ define We are now ready to state the lemma.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

We begin with the last-iterate distance to the optimizer. Recall from Lemma C.2. ‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") that the distance analysis reduces to controlling the partial sum of the directional gradient noise terms $X_{t}=2A_{t}\eta_{t}\langle x^{\star}-x_{t},\xi_{t}\rangle$. To bring this term within the scope of Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), define the corresponding uncentered directional stochastic-gradient term By conditional unbiasedness, $H_{t}^{\mathrm{dist}}-\mathbb{E}\left[H_{t}^{\mathrm{dist}}\,\middle|\,\mathcal{F}_{t-1}\right]=X_{t}$. Thus, the centered process appearing in Theorem 3.3.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") is exactly the stochastic term already isolated by the distance decomposition. Under Assumption 3.1. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), For the canonical stepsize $\eta_{t}\asymp 1/t$, we have $A_{t}\asymp t^{2}$, while the distance confidence sequence of the preceding section gives $Z_{t}\lesssim L_{t}/t$. Hence the predictable range can grow as $\sqrt{tL_{t}}$, and in particular need not remain bounded over the infinite horizon. This is precisely the setting covered by Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules").

<!-- chunk {"id": "body-0059", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

Accordingly, define the latent quadratic and range processes These are the distance-specific counterparts of the quadratic process $W_{t}$ and the running predictable range $C_{t}$ in Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"). The generic theorem also requires $H_{t}^{\mathrm{dist}}$ to be integrable. Since $Z_{t}\leq G^{2}/\mu^{2}$ almost surely, it is enough to assume This mild technical condition is automatic for the deterministic stepsize schedules considered below.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Last-iterate squared distance to the optimizer", "weight": 1.0} -->

Combining Lemma C.2. ‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") with Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") gives the latent empirical Bernstein confidence sequence This is the empirical Bernstein counterpart of Proposition 2.2. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") from the preceding section. The argument follows the same overall logic, with Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") providing the corresponding concentration step. We defer the formal proof of this confidence-sequence guarantee to Proposition B.1. ‣ Appendix B Additional Results ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") in the appendix.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

This empirical Bernstein refinement admits a direct comparison with the sub-Gaussian confidence sequence from Proposition 2.2. ‣ 2.1 Last-iterate squared distance to the optimizer ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"). The leading square-root term in $\mathfrak{B}_{\alpha}\left(V_{t}^{\mathrm{dist,EB}},B_{t}^{\mathrm{dist,EB}}\right)$ is the analogue of $4\,\mathfrak{H}_{\alpha}\left(V_{t}^{\mathrm{dist}}\right)$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

Under the bounded-gradient choice $\sigma^{2}=G^{2}$, the latter uses the fixed worst-case scale $G^{2}$, whereas the former is driven by the realized directional quantities $\langle g_{s},x^{\star}-x_{s}\rangle^{2}\leq\left\|g_{s}\right\|^{2}Z_{s}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

In the worst case, when $\left\|g_{s}\right\|=G$ and the directional bound is attained, $V_{t}^{\mathrm{dist,EB}}=4V_{t}^{\mathrm{dist}}$, so the leading factor $2$ in $\mathfrak{B}_{\alpha}\left(V_{t}^{\mathrm{dist,EB}},B_{t}^{\mathrm{dist,EB}}\right)$ exactly recovers the outer factor $4$ in $4\,\mathfrak{H}_{\alpha}\left(V_{t}^{\mathrm{dist}}\right)$, up to the additional iterated-logarithmic factor required to stitch over the predictable range.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

Away from this worst case, the leading term in $\mathfrak{B}_{\alpha}\left(V_{t}^{\mathrm{dist,EB}},B_{t}^{\mathrm{dist,EB}}\right)$ adapts to the realized stochastic-gradient magnitudes and directions, as desired. Beyond this additional logarithmic factor, the only new additive contribution is the linear range term in $\mathfrak{B}_{\alpha}\left(V_{t}^{\mathrm{dist,EB}},B_{t}^{\mathrm{dist,EB}}\right)$. For the observable construction below, Proposition 3.6.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

‣ 3.1 Last-iterate squared distance to the optimizer ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") shows that the corresponding range contribution is lower order, scaling as $(L_{t}/t)^{3/2}$ rather than $L_{t}/t$. $\clubsuit$ The bound is not yet observable, however, because $Z_{t_{0}}$, the directions $x^{\star}-x_{s}$, and the distances entering $B_{t}^{\mathrm{dist,EB}}$ all depend on the unknown optimizer. We remove this dependence using the same recursive domination principle as in the preceding section, now applied simultaneously to the two arguments of $\mathfrak{B}_{\alpha}$. We formalize this construction.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 3.4 (Comparison with the sub-Gaussian construction)", "weight": 1.0} -->

Fix $\alpha\in$, and let $R_{0}$ be any $\mathcal{F}_{t_{0}-1}$-measurable quantity satisfying $R_{0}\geq Z_{t_{0}}$ almost surely. Define recursively the observable distance envelopes For $t\geq t_{0}$, set The recursion is sequentially well defined: when the envelope at time $t+1$ is computed, all $R_{s}^{\mathrm{EB}}$ with $s\leq t$ are already available. As in the sub-Gaussian construction, simultaneous domination of the unknown distances $Z_{s}$ by these observable distance envelopes yields observable upper bounds on both the latent quadratic process and the predictable range; monotonicity of $\mathfrak{B}_{\alpha}$ then propagates the domination through the recursion.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 3.7 (Alternative polynomial stepsize)", "weight": 1.0} -->

The same conclusion holds for the stepsize In this case, $1-2\mu\eta_{t}=(t-3)/(t+1)$, so the natural analysis start time is $t_{0}=4$. Following similar steps to those in the proof of Proposition 3.6. ‣ 3.1 Last-iterate squared distance to the optimizer ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), there exists a universal constant $C<\infty$ such that, almost surely, for every $t\geq 4$, The analogue of (47. ‣ 3.1 Last-iterate squared distance to the optimizer ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")) holds as well, with a different universal constant. The proof is similar and is omitted. $\clubsuit$

<!-- chunk {"id": "body-0068", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

We now turn to the weighted-average suboptimality. Recall from Lemma C.3. ‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") that the suboptimality analysis reduces to controlling the partial sum of the directional gradient noise terms $E_{t}=t\,\langle x^{\star}-x_{t},\xi_{t}\rangle$. To bring this term within the scope of Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), define the corresponding uncentered directional stochastic-gradient term By conditional unbiasedness, $H_{t}^{\mathrm{sub}}-\mathbb{E}\left[H_{t}^{\mathrm{sub}}\,\middle|\,\mathcal{F}_{t-1}\right]=E_{t}$. Thus, the centered process appearing in Theorem 3.3.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") is exactly the stochastic term already isolated by the suboptimality decomposition. Under Assumption 3.1. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), As in the distance construction, the bound $Z_{t}\lesssim L_{t}/t$ implies that the predictable range can grow as $\sqrt{tL_{t}}$ and need not remain bounded over the infinite horizon. Accordingly, define the latent quadratic and range processes These are the corresponding quadratic and predictable-range processes for the suboptimality analysis. Moreover, since $Z_{t}\leq G^{2}/\mu^{2}$ almost surely, $H_{t}^{\mathrm{sub}}$ is integrable for every deterministic $t\geq t_{0}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

Combining Lemma C.3. ‣ Appendix C Supporting Lemmas ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") with Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") gives the latent empirical Bernstein confidence sequence This is the empirical Bernstein counterpart of Proposition 2.7-𝑓(𝑥^⋆)). ‣ 2.2 Suboptimality of the weighted-average iterate ‣ 2 Confidence Sequences under Sub-Gaussian Noise ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") from the preceding section. The argument follows the same overall logic, with Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") providing the corresponding concentration step. We defer the formal proof of this confidence-sequence guarantee to Proposition B.2-𝑓(𝑥^⋆)). ‣ Appendix B Additional Results ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") in the appendix.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

As in the distance construction, the latent bound is not observable because $Z_{t_{0}}$, the directions $x^{\star}-x_{s}$, and the distances entering $B_{t}^{\mathrm{sub,EB}}$ depend on the unknown optimizer. Here this dependence can be removed directly using the observable distance confidence sequence constructed above. Let $R_{0}$ be any $\mathcal{F}_{t_{0}-1}$-measurable quantity satisfying $R_{0}\geq Z_{t_{0}}$ almost surely. For $\beta\in$, define the observable distance envelopes For $t\geq t_{0}$, set Given $\alpha\in$, define As in the distance construction, the observable distance envelopes dominate the unknown distances simultaneously and therefore yield observable upper bounds on both latent arguments of $\mathfrak{B}_{\alpha/2}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Suboptimality of the weighted-average iterate", "weight": 1.0} -->

The use of confidence level $\alpha/2$ accounts for the simultaneous validity of the distance and suboptimality confidence sequences.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Minibatch Extensions", "weight": 1.0} -->

The confidence sequences developed in the preceding two sections admit natural extensions to minibatch SGD. Fix an integer $b\geq 1$. At every iteration $t\geq 1$, conditionally on $\mathcal{F}_{t-1}$, suppose that we observe independent and identically distributed stochastic gradients $g_{t}^{},\ldots,g_{t}^{(b)}$ satisfying Let $\mathcal{F}_{t}\coloneqq\sigma\left(\mathcal{F}_{t-1},g_{t}^{},\ldots,g_{t}^{(b)}\right)$ denote the filtration generated by the history through iteration $t$. Define the minibatch gradient and its noise by and let the SGD update use $\bar{g}_{t}$ in place of $g_{t}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Minibatch Extensions", "weight": 1.0} -->

For the sub-Gaussian confidence sequences of Section 2, the effect of minibatching is immediate. Suppose, in addition, that the individual noises $\xi_{t}^{(i)}\coloneqq g_{t}^{(i)}-\nabla f(x_{t})$ satisfy the conditional sub-Gaussian condition in Assumption 1.3. ‣ 1.1 Problem formulation ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") with the same variance proxy $\sigma^{2}$. Conditional independence then implies that their average $\bar{\xi}_{t}$ satisfies the same conditional sub-Gaussian bound with variance proxy $\sigma^{2}/b$. Consequently, the confidence sequences of Section 2 extend directly to minibatch SGD by replacing $\sigma^{2}$ with $\sigma^{2}/b$ in the corresponding variance processes and replacing $g_{t}$ with $\bar{g}_{t}$ in the SGD recursions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Minibatch Extensions", "weight": 1.0} -->

The empirical Bernstein construction of Section 3 allows the information contained in the minibatch to be used more finely. The sub-Gaussian construction summarizes the stochastic fluctuations through the fixed conditional variance proxy $\sigma^{2}/b$. By contrast, the empirical Bernstein argument can be applied to the $b$ individual observations before they are averaged. Conditional independence allows the corresponding one-step exponential bounds to be combined while retaining the sum of the individual realized quadratic contributions. Thus, the leading square-root term enjoys the usual $1/\sqrt{b}$ minibatch reduction while continuing to adapt to the realized directional second moments within each minibatch, whereas the linear range term carries an explicit factor $1/b$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Minibatch Extensions", "weight": 1.0} -->

This observation yields a general minibatch extension of Theorem 3.3. ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"), in which the centered process is formed from the minibatch averages while the realized quadratic process retains the individual observations within each minibatch. The resulting form will apply directly to both the distance and suboptimality confidence sequences.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Assumption 4.2 (Bounded minibatch stochastic gradients)", "weight": 1.0} -->

There exists $G<\infty$ such that We now specialize Proposition 4.1. ‣ 4 Minibatch Extensions ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") to the SGD confidence sequences, beginning with the last-iterate distance. For every $t\geq t_{0}$, define the observable within-minibatch second-moment matrix As in the single-gradient construction of Section 3, set Their averaged centered increment is exactly the stochastic term arising from the distance decomposition with $\bar{g}_{s}$ in place of $g_{s}$. Moreover, while Assumption 4.2. ‣ 4 Minibatch Extensions ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") gives Thus, the minibatch quadratic process retains the realized directional second moment encoded by $\widehat{\Sigma}_{s}$, rather than reducing the stochastic fluctuations to a fixed variance proxy.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Assumption 4.2 (Bounded minibatch stochastic gradients)", "weight": 1.0} -->

To make the resulting bound fully observable, we use the same recursive domination argument as in the distance construction of Section 3. Since the unknown distance can again be replaced by a previously constructed distance envelope. Fix $\alpha\in$, and let $R_{0}$ be any $\mathcal{F}_{t_{0}-1}$-measurable quantity satisfying $R_{0}\geq Z_{t_{0}}$ almost surely. Define recursively For every $t\geq t_{0}$, set As in the single-gradient case, the construction is recursive: $R_{s}^{\mathrm{EB,MB}}$ is available before the minibatch at iteration $s$ is observed, and the quantities above determine the distance envelope for the next iterate. The following corollary is the minibatch analogue of Theorem 3.5. ‣ 3.1 Last-iterate squared distance to the optimizer ‣ 3 Refined Confidence Sequences under Bounded Gradients ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules").

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiments", "weight": 1.0} -->

To study the empirical performance of our confidence sequences, we run a series of experiments on a primal support vector machine (SVM) problem, using both real-world and synthetic data. Section 5.1 details the optimization problem, the experimental protocol, and the bounds we compare against. Section 5.2 then discusses the introductory figure (Figure 4 ‣ 1.2 Contributions ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules")), which illustrates the improvement in certified stopping on a single instance. Section 5.3 (Figure 2) varies the minibatch size $b$, exhibiting its effect on the relative behavior of the bounds. Section 5.4 (Figure 3) compares three synthetic datasets of increasing difficulty while keeping all constants entering the bounds fixed, thereby isolating trajectory adaptivity. We conclude with two verifications. Section 5.5 (Figures 4 and 5) checks the sensitivity of our bounds to conservatively chosen constants, and Section 5.6 (Figure 6) examines whether the same behavior persists in a single-pass regime beyond the finite-dataset formulation used in the preceding experiments.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider the SVM primal optimization problem where $z$ follows a probability distribution $\mathbb{Q}$ on $\mathbb{R}^{d}$ and satisfies $\|z\|\leq M$ almost surely. This problem is $\mu$-strongly convex and nonsmooth. For a minibatch size $b\geq 1$, at each time $t\geq 1$ we sample $z_{t}^{},\ldots,z_{t}^{(b)}$ independently from $\mathbb{Q}$, conditionally on $\mathcal{F}_{t-1}$, and define where $\bar{g}_{t}$ is used in the SGD update. For $b=1$, this reduces to the single-gradient setting; in that case, we simply write $g_{t}$. Since is not differentiable in general, each $g_{t}^{(i)}$ is an unbiased stochastic subgradient rather than a stochastic gradient.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Although we assume differentiability throughout the paper for notational convenience, the same arguments apply with unbiased stochastic subgradients.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the explicit constants, first notice that We therefore take $\mathcal{X}=\{x\in\mathbb{R}^{d}:\|x\|\leq\sqrt{2/\mu}\}$, which contains $x^{\star}$ and hence has the same minimizer as the unconstrained problem. On $\mathcal{X}$, Thus the bounded-gradient conditions required by the empirical-Bernstein-based confidence sequences hold. In particular, the conditional Hoeffding lemma gives the valid minibatch sub-Gaussian proxy $\sigma^{2}=G^{2}/b$ for $\bar{g}_{t}$. Finally, we use $R_{0}=8/\mu$, the squared diameter of $\mathcal{X}$, as a deterministic bound on $Z_{t_{0}}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Data and protocol. We run experiments on the *covertype.binary* dataset, obtained from the LIBSVM data websitem^88^ 8 and on synthetic datasets generated with scikit-learn's make_classification.^99^ 9 A bias term is appended to every dataset, and dense features are standardized to zero mean and unit variance.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

To account for the fact that we work with finite datasets, we take $\mathbb{Q}$ to be the uniform distribution over the dataset, rather than the unknown data-generating distribution. Sampling independently from $\mathbb{Q}$, i.e., with replacement, makes the empirical risk problem a special case of our general setting. To confirm that the performance of our confidence sequences is not an artifact of this special case, we also conduct a *true single-pass* experiment in which SGD uses each data point exactly once, directly targeting the expected risk under the data-generating distribution. The full details and results of this experiment are discussed in Section 5.6.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

In all experiments we set $\mu=0.1$, choose the confidence level $1-\alpha=99\%$, use $t_{0}=4$, and take the stepsize schedule $\eta_{t}=2/(\mu(t+1))$. For the finite-dataset experiments, the ground-truth quantities $x^{\star}$ and $f(x^{\star})$ are computed beforehand with LIBLINEAR. The resulting numerical error is several orders of magnitude below the smallest values appearing in our plots, so these quantities can be treated as exact.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Each figure reports a single trajectory of SGD. This is deliberate: our goal is to illustrate how the confidence sequences and the resulting stopping certificates evolve along an individual realized trajectory, rather than to average away their trajectory dependence across runs. Repeating the experiments with several seeds yields essentially identical qualitative behavior, and we therefore report a single run. Similarly, the horizon $T_{\max}$ at which our plots stop is arbitrary: all the confidence sequences we display remain valid beyond it and do not depend on it.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Theorem 2.3 1010 10 In the minibatch experiments, we use the direct minibatch extension described at the beginning of Section 4, replacing σ2 with σ2/b in the corresponding variance processes and gt with ḡt in the SGD recursions.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Compared bounds. For both the squared distance to the optimum $Z_{t+1}=\|x_{t+1}-x^{\star}\|^{2}$ and the suboptimality $f(\bar{x}_{t})-f(x^{\star})$ of the weighted average, we compare the quantities listed in Table 1. The two worst-case baselines are obtained from our Hoeffding-based confidence sequences by replacing the realized squared-gradient terms by their a priori upper bound $G^{2}$ and propagating this replacement through the recursive distance envelopes. With $\sigma^{2}=G^{2}$ denoting the individual-gradient sub-Gaussian proxy, so that $\sigma^{2}/b$ is the corresponding minibatch proxy, this yields for squared distance, and for suboptimality. Under the deterministic stepsize schedule used in our experiments, these sequences are deterministic and trajectory-independent.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

They are also well defined recursively: the distance sequence is initialized at $\check{U}^{\text{dist}}_{t_{0}}(\alpha)=R_{0}$, and the suboptimality sequence uses the already defined distance sequence at level $\alpha/2$. Moreover, since $\|\bar{g}_{t}\|^{2}\leq G^{2}$ almost surely and $\mathfrak{H}_{\alpha}$ is nondecreasing, the same recursive domination argument used for the Hoeffding-based confidence sequences shows that the worst-case baselines remain valid confidence sequences. Comparing H with the corresponding worst-case baseline therefore isolates the effect of adapting the Hoeffding-based construction to the realized trajectory.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the distance to the optimum, we additionally compare against the high-probability bound of [Rakhlin et al. \[36, Proposition 1\]](#bib.bib8), which states that, for any fixed horizon $T\geq 4$, with probability at least $1-\alpha$, simultaneously for all $t\leq T$, This bound stems from the same standard one-step recursion underlying our distance analysis, but differs from $\check{U}^{\text{dist}}$ in several respects. First, is stated in closed form, at the price of a multiplicative constant that is not necessarily optimized, whereas $\check{U}^{\text{dist}}$ is defined recursively. Second, does not account for the variance reduction due to minibatching, whereas $\check{U}^{\text{dist}}$ uses the minibatch variance proxy $\sigma^{2}/b$. The effect of this difference will be illustrated in Section 5.3 by varying $b$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Third, is a finite-horizon simultaneous guarantee rather than a confidence sequence in our sense, since the horizon $T$ must be fixed in advance. We take $T=T_{\max}$, the most favorable valid choice for covering the entire plotted horizon. More recently, Pham et al. obtained an infinite-horizon time-uniform analogue that removes the need to specify $T$, but with a larger leading constant ($1008$ instead of $624$). Since our goal is to compare against a favorable explicit literature benchmark, we therefore use in the experiments.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

The bound is stated for the stepsize schedule $\eta_{t}=1/(\mu t)$, while our experiments use $\eta_{t}=2/(\mu(t+1))$. Both belong to the standard $1/t$ stepsize regime for strongly convex stochastic optimization, and we use as the corresponding explicit literature benchmark. Overall, the two baselines serve different purposes: provides an explicit finite-horizon literature benchmark, while $\check{U}^{\text{dist}}$ is the natural non-adaptive counterpart of our Hoeffding-based confidence sequence under the same stepsize schedule and minibatch variance proxy.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the suboptimality of the weighted average, we are not aware of a high-probability bound in the literature stated with explicit constants. Harvey et al. establish such a bound for the same linearly weighted averaging scheme and stepsize schedule, but only up to unspecified absolute constants, which makes a direct quantitative comparison impossible without further analysis. We therefore compare only against the worst-case baseline $\check{U}^{\text{sub}}_{t}$ above.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Introductory plot", "weight": 1.0} -->

We begin with an experiment illustrating our main findings. We run SGD on *covertype.binary* with minibatch size $b=256$. Figure 4 ‣ 1.2 Contributions ‣ 1 Introduction ‣ Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules") reports, on log-log axes, the squared distance to the optimum (left) and the suboptimality of the weighted average (right), with the bounds of Table 1 evaluated along the same trajectory. On the right panel, we mark for each bound the first time it drops below the threshold $\varepsilon=10^{-3}$. Stopping SGD at this time certifies, with probability $1-\alpha$, that the returned weighted average satisfies $f(\bar{x}_{t})-f(x^{\star})\leq\varepsilon$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Introductory plot", "weight": 1.0} -->

Note first that $\check{U}^{\text{dist}}$ lies several orders of magnitude below. As explained in Section 5.1, this reflects the larger explicit constants in together with the fact that it does not account for the variance reduction due to minibatching. The role of minibatching is examined separately in Section 5.3.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Introductory plot", "weight": 1.0} -->

Turning to the confidence sequences, the Hoeffding-based bound $\widehat{U}^{\text{sub}}$ (H) certifies the threshold $6.1$ times earlier than the worst-case baseline, while the empirical Bernstein minibatch bound $\widehat{U}^{\text{sub,EB,MB}}$ (EB) does so $312$ times earlier. In terms of gradient lookups, this corresponds to $5.1\times 10^{6}$ lookups for EB, $2.6\times 10^{8}$ for H, and $1.6\times 10^{9}$ for the worst-case baseline, all for the same confidence level and target accuracy.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Introductory plot", "weight": 1.0} -->

These improvements illustrate the adaptivity of our confidence sequences, which make use of observed quantities along the trajectory rather than their a priori upper bounds. The further improvement of the empirical Bernstein sequence over the Hoeffding-based one reflects its ability to exploit the realized second-moment structure within each minibatch, rather than relying only on the fixed sub-Gaussian variance proxy. Overall, the experiment shows that trajectory adaptation can substantially tighten the resulting certificates while preserving their anytime-valid guarantees.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Effect of the minibatch size", "weight": 1.0} -->

We now repeat the previous experiment on *covertype.binary* with $b\in\{1,32,1024\}$, all other parameters being unchanged. All three runs are given the same budget of $10^{7}$ gradient lookups. Although the performance of SGD may differ, the goal of this experiment is not to isolate how fast the algorithm converges, but how tightly its progress can be certified. The question of choosing the minibatch size $b$ is beyond the scope of this paper; here we only study its effect on the confidence sequences.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Effect of the minibatch size", "weight": 1.0} -->

Hoeffding-based H is indistinguishable from worst-case at $b=1$. The adaptive contribution in H comes from retaining the realized squared minibatch-gradient norms $\|\bar{g}_{s}\|^{2}$ in the deterministic accumulation, whereas the recursive deviation term uses the fixed variance proxy $\sigma^{2}/b$. At $b=1$, the latter dominates, so replacing $\|g_{s}\|^{2}$ by $G^{2}$ changes little. As $b$ increases, the deviation term shrinks and the trajectory-dependent accumulation becomes relatively more important, making the effect of adaptivity increasingly visible.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Effect of the minibatch size", "weight": 1.0} -->

Empirical-Bernstein-based EB improves on H by about one order of magnitude already at $b=1$, and this gap widens with $b$. Unlike H, whose deviation term is controlled by the fixed variance proxy $\sigma^{2}/b$, EB exploits the realized second-moment structure within each minibatch through $\lambda_{\max}(\widehat{\Sigma}_{t})$. The contribution of each minibatch to the leading square-root term therefore carries the usual $1/\sqrt{b}$ scaling while adapting to $\lambda_{\max}(\widehat{\Sigma}_{t})\leq\operatorname{tr}(\widehat{\Sigma}_{t})\leq G^{2}$. In addition, the lower-order range term carries an explicit factor $1/b$ and hence decreases faster with the minibatch size.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Effect of the minibatch size", "weight": 1.0} -->

The gap between the ground truth and the worst-case baseline also widens with $b$. The EB confidence sequence nevertheless recovers a growing share of this gap. Define the fraction of the gap between the worst-case bound and the ground truth recovered by EB on a logarithmic scale. At the end of the budget, we obtain $\rho=24.8\%$, $43.6\%$, and $53.8\%$ for $b=1,32,1024$, respectively.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Adaptivity across problem instances", "weight": 1.0} -->

In this experiment, we aim to isolate the trajectory adaptivity of the empirical Bernstein confidence sequence. We generate three datasets with make_classification, of increasing class separability, and report the evolution of the ground-truth quantities $Z_{t}$ and $f(\bar{x}_{t})-f(x^{\star})$, together with EB (Figure 3).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Adaptivity across problem instances", "weight": 1.0} -->

The dataset parameters are given in Table 2. For all three, we set $\texttt{n_samples}=10^{5}$, $\texttt{n_features}=20$, and $\texttt{n_clusters_per_class}=1$. Each dataset is then rescaled so that $G$ has the same value across all three. Since $\mu$, $\alpha$, $b=256$, and $R_{0}$ are also fixed, the worst-case bound is identical across the three instances.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Adaptivity across problem instances", "weight": 1.0} -->

On these instances, SGD makes faster progress on the more highly separated datasets, and the confidence sequences follow the same ordering. The relationship between the geometry of the data and the performance of SGD on the SVM primal problem is outside the scope of this paper; what matters here is that this variation in performance is invisible to the worst-case analysis but reflected by the trajectory-adaptive confidence sequences. The same deterministic bound applies to all three runs, whereas EB separates them and, after $10^{6}$ SGD iterations, is roughly $17$ times tighter for C than for A in suboptimality: $\widehat{U}^{\mathrm{sub,EB,MB}}=1.9\times 10^{-6}$ for C, compared with $3.2\times 10^{-5}$ for A.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Adaptivity across problem instances", "weight": 1.0} -->

This behavior is consistent with the empirical Bernstein construction, which adapts to the realized second-moment structure within each minibatch through $\lambda_{\max}(\widehat{\Sigma}_{t})$. Better separated datasets have fewer samples with an active hinge loss, and in our experiments this is accompanied by substantially smaller realized values of $\lambda_{\max}(\widehat{\Sigma}_{t})$. The average value of $\lambda_{\max}(\widehat{\Sigma}_{t})$ over the last $1\%$ of the run decreases by approximately $73\%$ from A to B, and by approximately $98\%$ from A to C. A deterministic bound depending on $G$ alone cannot distinguish these trajectories.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

The bounds considered above depend on deterministic problem constants such as $G$, $\sigma^{2}$, and $R_{0}$, whose roles differ across the different constructions. These quantities are rarely available exactly in practice. The situation is not symmetric: choosing a value that is too small can invalidate the corresponding guarantee, whereas a conservative upper bound preserves validity at the price of tightness. The practical question is therefore what is lost when these constants are chosen too conservatively. We do not vary $\mu$, since it enters the stepsize schedule and changing it would therefore also change the SGD trajectory itself.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

Misspecification of the gradient bound $G$. We first compare the bounds computed with the correct value of $G$ to the same bounds computed with $G$ overestimated by a factor of $10$. For H and the worst-case baseline, we use the valid individual-gradient proxy $\sigma^{2}=G^{2}$, so overestimating $G$ by a factor of $10$ also overestimates $\sigma^{2}$ by a factor of $100$. The experiment is run on dataset B from the previous subsection, with the SGD trajectory itself unchanged. Figure 4 reports both families of curves.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

The worst-case bounds degrade as expected for both squared distance and suboptimality. Their leading asymptotic terms scale with $G^{2}$, and the misspecified curves lie approximately a factor of $100$ above their well-specified counterparts. A similarly strong effect is observed for Hoeffding-based H, reflecting the dependence of its deviation term on the fixed variance proxy $\sigma^{2}/b$ rather than on the realized second-moment structure of the stochastic gradients.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

Empirical-Bernstein-based EB behaves differently. Its leading deviation term adapts to the realized second-moment structure within each minibatch through $\lambda_{\max}(\widehat{\Sigma}_{t})$, while $G$ enters only through the lower-order range term of the empirical Bernstein boundary. The misspecified and well-specified EB curves are consequently asymptotically equivalent. They differ noticeably only at first and agree within a factor of $1.06$ after $10^{7}$ iterations, for both $\widehat{U}^{\mathrm{dist,EB,MB}}$ and $\widehat{U}^{\mathrm{sub,EB,MB}}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

Misspecification of the initial distance bound $R_{0}$. We repeat the experiment with $R_{0}$ overestimated by factors $10$, $100$, and $1000$, while keeping all other quantities fixed, and report EB in each case in Figure 5. Unlike $G$, $R_{0}$ enters through the initialization of the recursive distance envelope, and its influence therefore diminishes as the trajectory-dependent terms accumulate. For the squared-distance confidence sequence, the effect is pronounced initially but vanishes rapidly: with $R_{0}$ overestimated by a factor of $1000$, the confidence sequence initially differs from the correctly specified one by the same factor, but their relative difference is only $4\%$ after $100$ iterations and $0.01\%$ after $10^{3}$ iterations.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Robustness to parameter misspecification", "weight": 1.0} -->

Taken together, these two experiments show that, along the trajectories considered here, the effect of conservative choices of $G$ and $R_{0}$ on EB is largely transient. This reflects the trajectory adaptivity of the empirical Bernstein construction: its leading deviation term is driven by realized second-moment quantities, while $G$ enters through the lower-order range term and the influence of $R_{0}$ is rapidly attenuated by the recursive construction. In practice, this suggests that safe upper bounds on $G$ and $R_{0}$ need not be specified very precisely for the resulting EB certificates to become largely insensitive to them later in the run.

<!-- chunk {"id": "body-0112", "role": "body", "section": "True single-pass", "weight": 1.0} -->

All experiments above sample with replacement from the empirical distribution of a finite dataset, which makes the empirical risk and allows $x^{\star}$ to be computed beforehand. We now turn to the population setting, where the observations are modeled as i.i.d. samples from an unknown data-generating distribution $\mathbb{P}$. Under this standard model, processing the dataset once in an order chosen independently of the observations has the same distribution as sequential i.i.d. sampling from $\mathbb{P}$. Two consequences follow: the minimizer of the expected risk cannot be computed beforehand, so no ground truth is available, and the run is necessarily limited by the available sample size.

<!-- chunk {"id": "body-0113", "role": "body", "section": "True single-pass", "weight": 1.0} -->

We run this experiment on *covertype.binary*, which contains $N=581012$ observations, with minibatch size $b=256$, and report the evolution of worst-case, H, and EB in Figure 6. Using complete minibatches, the run stops after $\lfloor N/b\rfloor=2269$ SGD iterations, with no observation reused. The picture is essentially the same as the one observed throughout this section. For suboptimality, $\widehat{U}_{t}^{\mathrm{sub}}$ is $6.4$ times tighter than $\check{U}_{t}^{\mathrm{sub}}$, while $\widehat{U}_{t}^{\mathrm{sub,EB,MB}}$ is $2.7\times 10^{2}$ times tighter. For comparison, in the experiment of Section 5.2, the corresponding factors are also $6.4$ and $2.7\times 10^{2}$ after the same number of iterations.

<!-- chunk {"id": "body-0114", "role": "body", "section": "True single-pass", "weight": 1.0} -->

The improvements reported above are therefore not an artifact of repeatedly sampling from a finite empirical distribution and persist in this single-pass expected-risk setting.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Summary of the empirical findings", "weight": 1.0} -->

As shown in these experiments, on real-world data our confidence sequences can certify a target accuracy several orders of magnitude earlier than the trajectory-independent bounds against which they are compared. This improvement reflects their ability to adapt to the realized SGD trajectory. When all problem constants are fixed and only the problem instance varies, the worst-case bounds remain unchanged while our confidence sequences adapt to the instance. Minibatching further amplifies these differences, and our bounds recover a growing share of the gap between the worst-case bounds and the ground truth as $b$ increases.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Summary of the empirical findings", "weight": 1.0} -->

The two constructions nevertheless behave differently. The empirical-Bernstein-based sequences are consistently tighter than their Hoeffding-based counterparts in our experiments and appear particularly attractive when the stochastic gradients can be uniformly bounded. Their leading deviation terms adapt to realized second-moment quantities, while the effects of conservative choices of $G$ and $R_{0}$ become negligible later in the runs considered above. By contrast, the Hoeffding-based sequences retain an asymptotic dependence on the fixed sub-Gaussian variance proxy $\sigma^{2}$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Summary of the empirical findings", "weight": 1.0} -->

Even with these improvements, a considerable gap remains between the confidence sequences and the ground truth in the experiments where the latter is available. Whether this residual gap can be reduced through a sharper analysis of the SGD dynamics is an interesting question that we leave open.
