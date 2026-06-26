<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Action Chunking and Exploratory Data Collection Yield Exponential Improvements in Behavior Cloning for Continuous Control

Topics include Imitation learning, Robotics, Stability analysis, Benchmarks, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a theoretical analysis of two of the most impactful interventions in modern learning from demonstration in robotics and continuous control: the practice of action-chunking (predicting sequences of actions in open-loop) and exploratory augmentation of expert demonstrations. Though recent results show that learning from demonstration, also known as imitation learning (IL), can suffer errors that compound exponentially with task horizon in continuous settings, we demonstrate that action chunking and exploratory data collection circumvent exponential compounding errors in different regimes. Our results identify control-theoretic stability as the key mechanism underlying the benefits of these interventions. On the empirical side, we validate our predictions and the role of control-theoretic stability through experimentation on popular robot learning benchmarks. On the theoretical side, we demonstrate that the control-theoretic lens provides fine-grained insights into how compounding error arises, leading to tighter statistical guarantees on imitation learning error when these interventions are applied than previous techniques based on information-theoretic considerations alone.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning (IL) is the problem of learning complex behaviors from data labeled with actions from an expert demonstrator policy. This methodology encompasses both some of the earliest examples and most recent state-of-the-art in control for autonomous robotic systems. Following the rise of large language models (LLMs), IL has also become increasingly prevalent in settings where an agent predicts *discrete tokens*, such as words in a sentence, lines in a proof, or positions on a chessboard. Such methods have also seen adoption in the context of both continuous and discretized-action control of continuous state-space dynamical systems in an autoregressive fashion.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent and dramatic successes of imitation learning in continuous control applications has coincided with a range of algorithmic interventions which appear essential to ensure strong performance: 1. the prediction of open-loop sequences, or "chunks" of actions by the control policy, called *action-chunking* (AC), 2. the careful curation of expert data to be imitated and 3. the adoption of *generative* neural architectures (e.g. conditional diffusion models) as parameterizations of learned policies. While the benefits of 3. have been studied broadly, a precise understanding of how action-chunking and curated expert data improve behavior cloning performance remains elusive. Current hypotheses around AC foreground partial observability as the underlying mechanism, despite its clear benefits in fully-observable, state-based control (see e.g. Figure˜5). Moreover, studies on active data collection, recent and classical, focus on multi-round interactive data collection to witness expert corrections, but do not isolate core mechanisms of how exploratory data can cover susceptibilities of behavior cloning, especially for single or few-shot dataset generation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We discuss these prior works more in Sections˜6 and A In this work, we provide the first theoretical guarantees justifying the practices of AC and exploratory data augmentation during expert data collection (defined formally below) in the minimal setting of imitation of an expert in a state-based continuous-control problem. Our point of departure is the finding in recent work that imitation learning in continuous settings---even those whose dynamics and expert demonstrator appear benign---can be considerably more challenging than imitation in discrete settings, such as those encountered in language modeling, demonstrating compounding errors can grow exponentially with horizon, as opposed to polynomially (or none). As Simchowitz et al. eliminates the possibility of a simple "fix" to the *learning procedure*, we instead consider how changes to either 1. the policy parameterization or 2. the data-collection process can circumvent this negative result. We thereby elucidate both the design space of "sound" offline learning methodologies and better understand the success of widely-deployed practices such as action-chunking and data-augmentation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

We provide the first theoretical guarantees in continuous state-action IL for interventions that provably prevent compounding error without iterative expert feedback. Whereas previous work require either iterative interaction with the expert or knowledge of the underlying system, we establish our results without access to such oracles, using near-"vanilla" behavior cloning. We study two key practices: ˜1. ‣ 3 Action-Chunking Suffices in Open-Loop Stable Systems"): Action-Chunking. When the environment is benign, we show the algorithmic modification of *action-chunking*, i.e., predicting and playing open-loop sequences of actions, mitigates compounding errors without requiring any modification to the expert data (Theorem˜1).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics"): Exploratory Data Collection via Expert Noise-Injection. When the environment is less benign, some alteration of the expert data distribution is necessary. We demonstrate *noise-injection*, i.e., adding noise while executing expert actions, is a simple and practical tool for avoiding compounding errors (Theorem˜2).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Surprising Takeaways", "weight": 1.0} -->

While ˜1. ‣ 3 Action-Chunking Suffices in Open-Loop Stable Systems") and 2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") are reflective of popular practices at the intersection of (reinforcement) learning and control, our analysis additionally uncovers phenomena that contrast with the common perspectives of both literatures. In particular: Figure 2: Visualization of the benefits of action-chunking (˜1) and noise-injection (˜2). Left: even on synthetic globally stable (Definition˜2.1) dynamics f, frequent feedback can cause exponential compounding error, which action-chunking mitigates. Center: HalfCheetah-v5 environment. We see sufficiently large white-noise injection yields significant performance improvement, on par with more advanced iterative methods. Right: Humanoid-v5 environment. Iterative methods like DAgger and Dart can be suboptimal due to poor learned policy rollouts or aggressive noise-covariance shaping, while naive noise-injection reliably provides the necessary local exploration; error bars omitted for clarity. Experiment details in §5 and Appendix˜E.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Surprising Takeaways", "weight": 1.0} -->

Moreover, our analysis of expert-noise injection reveals that, from a theoretical perspective, adaptive iterative interaction or queries with an expert is not needed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Surprising Takeaways", "weight": 1.0} -->

Finally, our results reveal the inadequacy of existing theoretical tools for describing or mitigating compounding errors in continuous state spaces.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Compounding Errors problem", "weight": 1.0} -->

We now formally describe the compounding errors problem. Let $\mathsf{alg}$ be a (possibly randomized) mapping from a sample of $n$ trajectories $S_{n}\overset{\mathrm{i.i.d}}{\sim}\operatorname{\mdmathbb{P}}_{\mathrm{demo}}$ to an imitator policy ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}}\sim\mathrm{alg}(S_{n})$. The problem instance suffers *exponential compounding errors* if: for some $C>1$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Compounding Errors problem", "weight": 1.0} -->

In other words, imitating via empirical risk minimization on a given demonstration distribution $\operatorname{\mdmathbb{P}}_{\mathrm{demo}}$ leads to learned policies ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}}$ that suffer exponentially more trajectory error rolled out in closed-loop compared to their on-expert regression error. As proposed in prior work, compounding error can be understood through the lens of control-theoretic *stability*, which describes the sensitivity of the dynamics to perturbations of the state or input. By the control-theoretic nature of the ensuing definitions and analysis, we provide a concise primer to key control-theoretic concepts in Appendix˜B. We consider a notion of *incremental stability*.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Additional Notation", "weight": 1.0} -->

Blue (e.g. ^⋆^) indicates expert-induced quantities, and red indicates quantities induced by a learned policy (e.g. ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}}$). Positive semi-definite matrices are indicated by $\mathbf{Q}\succeq\mathbf{0}$, and the corresponding partial order $\mathbf{P}\succeq\mathbf{Q}\implies(\mathbf{P}-\mathbf{Q})\succeq\mathbf{0}$. We use $\lesssim,\approx$ to omit universal constants.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Additional Notation", "weight": 1.0} -->

In the main body, we also use $O_{\star}\hskip-1.5pt\left(\cdot\right)$ to omit *polynomial* dependence on instance-dependent constants, but not algorithm-dependent constants or horizon $T$, e.g. $\frac{TC_{{\scriptscriptstyle\mathrm{ISS}}}}{1-\rho}{}_{\mathbf{u}}^{2}=O_{\star}\hskip-1.5pt\left(T{}_{\mathbf{u}}^{2}\right)$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Action-Chunking Suffices in Open-Loop Stable Systems", "weight": 1.0} -->

Action-chunking is a popular practice in modern sequential modeling pipelines, where a policy predicts a sequence of actions, of which some number are played *in open-loop*. There are various intuitions of the practical benefits of action-chunking, ranging: 1. robustness to non-Markovian / partial observability quirks in the data, 2. amenability to multi-modal^77^7In the sense of a distribution having multiple modes. prediction, 3. improved representation learning via multi-step prediction, and 4. simulating receding-horizon control. Yet, we show that even in control settings with *unimodal, Markovian, state-feedback* experts, action-chunking serves a critical role in subverting exponential compounding errors. All proofs and extended details in this section are contained in Appendix˜C. We may conveniently describe chunking as follows.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Practice 1 (Learning over Chunked Policies)", "weight": 1.0} -->

We sample $S_{n}$ as denote $n$ i.i.d. trajectories drawn from the expert distribution $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}}$. We aim to find ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\tilde{\pi}}$ from a class of length-$\ell$ chunked policies, ~chunk,ℓ~, defined formally in Definition˜3.2. ‣ 3 Action-Chunking Suffices in Open-Loop Stable Systems") that attains low on-expert error, e.g., by empirical risk minimization. We note that for chunked policies, We now formally define the policies induced by chunking with a dynamics model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3.1 (Regularity and Stability)", "weight": 1.0} -->

We make the following assumptions: The true dynamics $f$ are $(C_{{\scriptscriptstyle\mathrm{ISS}}},\rho)$-EISS in open-loop, without loss of generality with $\rho\geq 1/e$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3.1 (Regularity and Stability)", "weight": 1.0} -->

In other words, we assume the dynamics $f$ are open-loop stable. All ensuing results regarding imitation learning with chunked policies stem from the following key result.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics", "weight": 1.0} -->

We now consider the difficult setting where the ambient dynamics $f$ may not be open-loop stable. In this case, purely algorithmic interventions like action-chunking are generally insufficient, as erroneous actions can quickly lead to unstable behavior. In fact, we recall Theorem˜A). ‣ The Compounding Errors problem. ‣ 2 Preliminaries") states that *no* algorithm, even permitting stochastic and non-Markovian policies, can circumvent exponential compounding errors in the worst-case, provided only data from the expert-induced law $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics", "weight": 1.0} -->

This necessitates altering the demonstration distribution $\operatorname{\mdmathbb{P}}_{\mathrm{demo}}$ beyond the expert's $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}}$, i.e., some form of additional exploratory data collection is required. In particular, prior approaches such as DAgger and Dart can be summarized as attempting to witness *how the expert recovers from errors*, where the former queries the expert along learned-policy rollouts, and the latter injects policy-shaped noise into the expert---similar to the approach we propose.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Exploratory Data Collection", "weight": 1.0} -->

However, beyond the motivating intuition, we still lack fine-grained insights into what kinds of recovery or policy errors need to be witnessed to circumvent compounding errors, if even possible. Furthermore, these works require *iterative* rounds of expert data collection based on learned policy statistics. Our point of departure is the following: if we are tracking the expert sufficiently closely, we should only need to witness how the expert policy recovers *near the expert distribution*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Practice 2 (Exploratory Data Collection via Expert Noise Injection)", "weight": 1.0} -->

Notably, ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") only collects data *once* before fitting the policy ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}}$, and thus does not depend on learned policy rollouts. We now lay out the core assumptions on the expert and dynamics in this section.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 4.1 (Regularity and Stability)", "weight": 1.0} -->

The closed-loop system induced by $({\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}},f)$ is $(C_{{\scriptscriptstyle\mathrm{ISS}}},\rho)$-EISS (Definition˜2.1. ‣ The Compounding Errors problem. ‣ 2 Preliminaries")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 4.1 (Regularity and Stability)", "weight": 1.0} -->

To understand the exploratory role of noise-injection, we gather intuition through linearizations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Analysis via Linearizations", "weight": 1.0} -->

Our analysis of ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") uses smoothness of the dynamics and policy to reason about its local linear approximation to the dynamical system along a given trajectory, called the *Jacobian linearization*.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Suboptimal Approaches", "weight": 1.0} -->

We now remark on subtle but important features of ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics").

<!-- chunk {"id": "body-0027", "role": "body", "section": "Suboptimal Approaches", "weight": 1.0} -->

Actions under $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}},{}_{\mathbf{u}}}$ are executed noisily, but recorded action labels are *noiseless* $\tilde{\mathbf{u}}_{t}={\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}(\tilde{\mathbf{x}}_{t})$, preventing additional regression error.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Suboptimal Approaches", "weight": 1.0} -->

This may run counter to RL theory, where noising the *policy*, e.g. $\tilde{\mathbf{u}}_{t}\sim\mathcal{N}({\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}(\tilde{\mathbf{x}}_{t}),{}_{\mathbf{u}}^{2}\mathbf{I})$ may be desirable to induce *coverage*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Suboptimal Approaches", "weight": 1.0} -->

Only a proportion ($1-\alpha$) of trajectories are noise-injected; the rest are clean expert trajectories.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Suboptimal Approaches", "weight": 1.0} -->

We relegate a detailed description of standard RL and control-theoretic perspectives (and their deficiencies) to Section˜D.1. In either case, i.e. if a noisy policy is adopted, or only noise-injected trajectories are collected, we encounter a fundamental problem. Due to the non-linearity of the dynamics, the noised actions induce a trajectory drift compared to the nominal noiseless expert. This drift means policies fitted on the noisy trajectories, even with clean action labels $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}},{}_{\mathbf{u}}}$, necessarily accrue an additive trajectory error scaling with ~u~, regardless of the on-expert regression error. We visualize this intuition underlying the design of ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") in Figure˜8.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Suboptimal Proposition 4.2", "weight": 1.0} -->

Let Assumption˜4.1. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") hold, and let $\mathbf{W}^{\mathbf{u}}_{1:t}({\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}\mathbf{x}_{1}^{{}^{\star}}})\succeq\underline{\lambda}_{\mathbf{W}}\mathbf{I}_{d_{x}}$, $t\geq 2$ w.p.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Suboptimal Proposition 4.2", "weight": 1.0} -->

For ${}_{\mathbf{u}}^{2}$ that satisfies ${}_{\mathbf{u}}^{2}\lesssim O_{\star}\hskip-1.5pt\left(\mathrm{poly}(1/C,1/C_{\mathrm{reg}})\right)\underline{\lambda}_{\mathbf{W}}$, we have: The full statement and proof can be found in Section˜D.3. Though this bound avoids exponential-in-$T$ compounding trajectory error, it has several shortcomings. Besides the strictness of one-step controllability---or controllability at all (see Appendix˜B)---the bound suffers: 1. a drift term that scales as ${}_{\mathbf{u}}^{2}$, which is even worse than Proposition˜4.1. ‣ 4.1 Suboptimal Approaches ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") suggests, 2.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Suboptimal Proposition 4.2", "weight": 1.0} -->

the requirement on ~u~ and resulting bound scaling with $\underline{\lambda}_{\mathbf{W}}$, which is miniscule for Gramians with fast-decaying spectra. So far, the direct control-theoretic approach possibly provides worse guarantees than an information-theoretic RL one (see Section˜D.7 for details).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Suboptimal Proposition 4.2", "weight": 1.0} -->

As such, a combination of algorithmic (e.g., $\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}},{}_{\mathbf{u}}}\to\operatorname{\mdmathbb{P}}_{{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}},{}_{\mathbf{u}},\alpha}$) and analytical innovations are required to advance the result.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sharp Analysis of Exploratory Data: Exciting the Unstable Directions", "weight": 1.0} -->

In light of ˜4.2, we make a few key observations. Firstly, *compounding errors are not arbitrary state perturbations*: they result from policy errors, and thus enter the state via the input channels. For smooth systems, this implies the trajectory error is primarily contained in the *controllable subspace* $\mathrm{range}(\mathbf{W}^{\mathbf{u}}_{1:t})$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sharp Analysis of Exploratory Data: Exciting the Unstable Directions", "weight": 1.0} -->

However, nonlinearity in the dynamics $f$ and policies ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}},{\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}{}^{\star}}$ means error will leak outside of $\mathrm{range}(\mathbf{W}^{\mathbf{u}}_{1:t})$, which would seem to require PE, i.e. full-dimensional coverage, to detect. Our first key insight is that as long as we enforce low error on the controllable subspace, the nonlinear error automatically regulates itself.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Action Chunking", "weight": 1.0} -->

To validate our predictions about the stability-theoretic benefits of action-chunking, we propose experiments on robotic imitation tasks in the robomimic framework. In particular, we pre-train a performant state-based, deterministic expert policy on robomimic data, which we then roll out to generate training data. We fit models of the same architecture except the final output dimension of varying prediction horizons. We then *execute* varying numbers of the predicted actions in open-loop and evaluate the resulting success rate. We observe the findings in Figure˜5; all experiment details can be found in Appendix˜E. In short, we find that: Executing action chunks matters more than simply predicting longer sequences of actions. This demonstrates the action-chunking is more than a simple consequence of representation learning, or a simulation of receding-horizon control.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Action Chunking", "weight": 1.0} -->

The merits of action-chunking remain showcased in deterministic, state-based control. This reveals that action-chunking still improves performance independently of partial observability or compatibility with generative control policies.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Action Chunking", "weight": 1.0} -->

End-effector control enables the benefits of action-chunking. This is because end-effector control renders the closed-loop between system state and end-effector prediction incrementally stable. Hence, the low-level end-effector controller transforms imitating the position policy to taking place in an open-loop stable dynamical system, precisely the regime where we prescribe our AC guarantees. Accordingly, in MuJoCo tasks that lack this property, we find that naively action-chunking hurts, not helps, performance---see Figure˜10.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Action Chunking", "weight": 1.0} -->

We emphasize the above remarks are not to rule out the role of non-Markovianity and representation learning; it is likely that these contribute further, e.g. AC can demonstrably prevent "stalling" from demonstrations with pauses. Rather, our results should be understood as stating that, instead of the benefits of action-chunking existing *in tension* with control---as controls folk-knowledge typically cautions against open-loop execution---it can be *naturally explained* by a control-theoretic perspective.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Noise Injection", "weight": 1.0} -->

We seek to validate our hypotheses about the exploratory benefits of noise-injection, making particular note to the algorithmic suggestions that our theoretical analysis reveal. We propose experiments on MuJoCo continuous control environments, where we seek to imitate pre-trained expert policies. We observe the findings across Figure˜2 and 10. To summarize: Noise injection as in ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") provides the exploration necessary to mitigate compounding errors, increasing performance on par with iteratively interactive methods such as DAgger and DART. We note ˜2. ‣ Exploratory Data Collection. ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") collects data in one shot, without ever observing learned policy rollouts.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Noise Injection", "weight": 1.0} -->

Larger noise scales ~u~ (within tolerance) improve performance, in contrast to prior understanding (cf. Proposition˜4.1. ‣ 4.1 Suboptimal Approaches ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics"), ˜4.2) which necessitates ~u~ set proportional to $\bm{\mathsf{J}}_{\textsc{Demo},T}({\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}};\operatorname{\mdmathbb{P}}_{\mathrm{demo}})$, i.e. very small for policies with low on-expert error.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Noise Injection", "weight": 1.0} -->

A *mixture* of noise-injected and clean expert trajectories is beneficial, and the difference is small when provided more data, as suggested by Eq.˜4.3. This matches the theoretical intuition that noise-injection is necessary up until ${\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}}$ is "locally stabilized" *sufficiently well* around ${\color[rgb]{0,0,0.7}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0.7}\mathbf{x}_{t}^{{}^{\star}}}$ (Proposition˜4.3 and 4.4), and thus only enters the trajectory error as a higher-order term, i.e., we only need "a sufficient amount" of noise-injection.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

Our action-chunking guarantees rely on a structural assumption of $({\color[rgb]{0.6,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.6,0,0}\hat{\pi}},\hat{f})\in\mathcal{P}$ being an EISS pair. We believe either explicitly enforcing this, e.g., via regularization or hierarchy, or attaining it indirectly via implicit biases, are interesting directions of inquiry. We assume smoothness in Section˜4, which is not strictly satisfied in some applications, such as in model-predictive control. We remark our lower bound Proposition˜4.1. ‣ 4.1 Suboptimal Approaches ‣ 4 Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics") depends on smoothness in $C$, which implies it is in some sense a fundamental aspect of noise-injection. However, we believe our results should extend to piece-wise notions, and note ongoing research exploring *smoothing* for learning in dynamical systems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

In general, we leave a sharp characterization of the role of smoothness and control-theoretic quantities in IL as an open problem. We also note though our theory suggests isotropic noise injection suffices, this may not be desirable in some practical contexts, such as highly dexterous robotics. In light of our findings elucidating the precise role of local exploration, we leave designing robust practical recipes for perturbative data collection as future inquiry. Lastly, we leave investigating the marginal benefit of *iterative* interaction as future work.
