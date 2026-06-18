## Introduction

Recent advances in robot policy synthesis incorporate increasing complexity throughout the design process, training on large-scale datasets, using sophisticated, stochastic architectures, and requiring commensurate increases in training resources. These advances have led to significant improvements in solving dexterous and long-horizon tasks, inferring semantic information from context, and safely interacting with numerous other autonomous agents. However, this complexity makes design decisions like the choice of dataset, the training or fine-tuning procedure, and the network architecture analytically opaque. The value of a novel intervention cannot be determined from first principles but instead requires rigorous analysis of its effect on empirical performance.

Unfortunately, rigorous analysis of empirical performance is a significant challenge in the robotics setting. Hardware evaluation is the gold-standard measure, but is expensive and slow to collect. Evaluations in simulation reduce the time burden, but continue to suffer from sim-to-real gaps, making them an imperfect proxy. Further, evaluation metrics can be quite coarse. Binary measurement of task success or failure, the *de facto* standard for measuring the performance of robot manipulation policies (particularly on hardware), can obscure valuable information about the robot behavior. For instance, a policy that completes $90\%$ of the task is clearly better than a policy that is frozen the whole time, yet their success rates would be identically $0\%$. Finally, rigorous evaluation must account for inherent uncertainty, including in environment configuration and policy action selection (which is often stochastic ). This uncertainty means that observed empirical performance is a noisy estimate of, and *not equivalent to*, the true expected performance of the policy.

Since the value of design interventions is implicitly counterfactual (see Figure 1), policy comparison is a particularly important form of evaluation to reliably determine the effects of design changes. For example: 'does a change in policy architecture or action tokenization improve downstream performance?' Or: 'what set of expert data is the most valuable to improve policy performance?' Importantly, comparison must account for uncertainty in evaluating both the new design and the baseline. Making rigorous, statistically assured decisions for these problems is necessary to ensure reliable progress within the field.

The costs of robot evaluation and the complexity of the robot policy design space motivate the development of a versatile framework for policy comparison. Ideally, such a framework would apply to very general performance measures, maintain statistical rigor, and ensure maximal sample efficiency via sequentialized evaluation. Current methods are deficient in at least one of these respects. Active learning and asymptotic approaches are not statistically rigorous, particularly in small-data regimes. Batch and fully nonparametric methods are not maximally sample efficient: the former due to the batch evaluation, and the latter due to not tailoring to the comparison setting. Near-optimal approaches are constrained to narrow metrics (e.g., binary success rate), and do not readily generalize.

Figure 1: The evaluation context of the N-SCORE procedure. (Left) We consider the general problem of policy comparison, which arises out of counterfactual design decisions in the policy synthesis process. (Middle) Evaluation on hardware or in high-fidelity simulation is the gold standard to assess the effect of such changes, but is costly to collect. (Right) N-SCORE is a sequential evaluation procedure that is statistically rigorous, sample efficient, and generalizes to rich, diverse measures of robot performance.

This work presents Nonparametric Sequential COmparison for Rigorous Evaluation (N-SCORE) to compare robot policy performance. N-SCORE is designed to address the shortcomings of prior approaches by explicitly accounting for all three of the preceding desiderata -- rigor, sample efficiency, and generality -- within the decision rule synthesis. We summarize our contributions as follows:

We introduce N-SCORE, a novel method for sequential policy comparison with general progress metrics.

We prove that N-SCORE is statistically rigorous in the sense of controlling Type-1 Error, and empirically demonstrate its improved sample efficiency compared to state-of-the-art (SOTA) baselines.

We comprehensively evaluate N-SCORE on large, high-impact evaluation datasets in robotics comprising over 4500 hardware evaluation rollouts and 2000 high-fidelity simulation rollouts. The results demonstrate significant savings in evaluation effort of up to 70% over batch methods and 50% over methods using binary success measures to rigorously certify policy improvements.

## Related Work

Efficient evaluation is increasingly appreciated as a critical aspect of the robot policy design process. The fundamental concern of these approaches is the strict limit on available hardware data. A core focus lies in constructing proxy signals (e.g., using simulations or evaluator preferences) to circumvent this constraint. By contrast, statistical testing approaches seek to employ the available hardware data more efficiently. These approaches are complementary; improvements in one domain augment those in the other.

### II-A Robot Policy Evaluation

Hardware and Simulation Evaluation. In robot manipulation, evaluation constraints often limit evaluation to 10-60 trials; the statistical validity of such comparisons is often not reported. To address this constraint, recent works have introduced standardized benchmarks, cloud-based evaluation platforms, and distributed evaluation infrastructure to increase available data. Further, recent works have proposed active sampling of policy-task pairs to improve efficiency. However, none of these approaches confer statistical rigor on downstream comparisons. Similarly, though policy evaluation via simulation or via world models show promise, the sim-to-real gap makes rigorous comparison difficult. Some recent works have proposed statistically rigorous methods to combine small-scale hardware testing with large-scale simulation evaluation, but these do not address policy comparison.

Evaluation Metrics. Recent studies emphasize the importance of detailed rubrics and task progress scores over traditional binary success metrics. In parallel, finetuning procedures and policy ranking problems have introduced indirect signals of policy performance, including reinforcement learning (RL) rewards and human preferences. However, none of the approaches give rigorous methods for decision-making. Whereas the state-of-the-art procedure for policy comparison under binary success metrics is rigorous and sample-efficient, current methods for more informative signals are not. This paper introduces a novel test procedure that scales rigorous evaluation to general metrics.

### II-B The Parametric Policy Comparison Problem

The *parametric* setting for policy comparison arises when the evaluator designs the performance measure to have definite distributional structure (e.g., binary success or discrete partial credit). This structure specifies a tradeoff between the generality, sample efficiency, and correctness of the comparison.

Classic tests were designed to optimize power for Bernoulli (binary) outcomes. Some subsequent results use tools from sequential analysis to improve the sample efficiency. In this regime, the STEP procedure is state-of-the-art. Other developments extend the generality of these tests to broader classes of parametric distributions. However, simultaneously extending both parametric generality and sample efficiency is difficult, requiring an exact solution of the Wald-Bellman partial differential equation. For more complex parametric families, finding this solution quickly becomes intractable.

This motivates work that extends generality by making approximations in the large-data regime. A canonical example is Welch's t-Test, which is often used for batch comparison. Further *asymptotic* results can extend generality \[17, 18"), 19")\] *and* improve sample efficiency, at the cost of losing rigorous statistical assurances. This cost is significantly more pronounced in the low-data regime common to robotic evaluation. Thus, in our setting, conclusions derived from asymptotic approaches are difficult to assess, as their validity is not guaranteed in the low-data regime.

### II-C Nonparametric Methods and Safe, Anytime-Valid Inference

Nonparametric methods seek to exchange some exploitable structure for generality in application. Within the batch regime, these are often termed 'distribution free,' as in the case of conformal prediction and related techniques. However, they have two downsides: limited capacity to represent the underlying data distribution, and limited generalization to sequential settings. Kernel density estimation (KDE) addresses the first constraint by directly constructing a representation of the data-generating process; see for an overview. Critically, KDE is more efficient in low-dimensional settings because it can quickly adapt to structure in the data. However, alone, it is not generally valid in finite samples.

To address the second constraint, work in the line of safe, anytime-valid inference (SAVI) considers *sequentialization* of estimation and decision problems, which act in an *online fashion*. A core benefit is safety in the face of p-hacking, or 'data dredging'. Additionally, though not parametric, the framework does allow for methodological fine-tuning to the particular problem setting (as in ). Of these approaches, the WSR method is closest to our own, considering the problem of estimating the mean of a general class of random variables (see 1. ‣ III Preliminaries ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison")). Importantly, N-SCORE utilizes ideas from KDE to tailor a SAVI framework *specifically to the comparison problem*, achieving state-of-the-art generality and sample-efficiency.

## Preliminaries

We model a robot that must complete a task while subject to stochastic uncertainty in its environment as a Partially Observable Markov Decision Process (POMDP). The uncertainty might arise in the initial environment configuration or in the robot's action selection. We assume the existence of a real-valued scalar performance measure $R$ encoding the degree of success the robot demonstrates in completing the task. Conditioned on an arbitrary robot policy $\pi$ mapping state observations to actions, the stochastic environment uncertainty is compressed to uncertainty over performance outcomes (i.e., by running the policy and measuring its level of success).^11^1This can be thought of as a pushforward measure (subject to necessary regularity assumptions). Thus, all the potential complexities of the task, real-world system dynamics, and policy class are compressed to a (possibly complicated) distribution over the performance measure $\mathcal{D}_{R}$. Our goal is to make rigorous comparisons for as general a class of $\mathcal{D}_{R}$ as possible. With this in mind, we make a single restriction: that $R$ be a *progress metric*, defined as a performance measure that is bounded w.p. 1.

### Definition 1 (Generalized Progress Metric)

A real-valued random variable $M{(\omega)}$ is termed a '*generalized progress metric*' if it is bounded; that is, ${{\mathbb{P}}{\lbrack{M \in {\lbrack 0,1\rbrack}}\rbrack}} = 1$.^22^2This immediately extends to real-valued performance measures that are bounded in an interval $\lbrack A,B\rbrack$ via normalization.

Unless stated otherwise, we assume $R$ is a progress metric as per 1. ‣ III Preliminaries ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison") but make no other structural assumptions.

We conclude this section with a formalization of the comparison problem in the robotics context. In the most general form, we are tasked with quickly and accurately comparing the means of two distributions over a progress metric $R$:

This encompasses many practical problems, for example: comparing two policies with different architectures or trained on different data ($\pi_{0}$ and $\pi_{1}$), comparing distribution shift in task realizations for a single policy, or comparing the effects of different hyperparameters in training. Importantly, because the true means are unknown and not directly observable, a testing decision must be made on the basis of empirical performance in evaluation. Due to stochastic uncertainty in gathering this data, any decisions are inherently *probabilistic* over the collection of evaluation data. Thus, we seek statistical assurances that bound the probability of an incorrect inference:

The challenges to obtaining a result in the form of Equation 1 are twofold. First, the decision must be statistically rigorous---it must safeguard against inadvertently reporting statistical noise as genuine improvement. This can require a substantial number of evaluations when the difference is small or the desired confidence $1 - \alpha^{\ast}$ is very high. However, the result also must be obtained as quickly as possible, so that the evaluator can efficiently allocate hardware or computational resources to begin investigating other problems. Indeed, allocating limited evaluation resources is a major bottleneck in improving policy performance. The sequential nature of N-SCORE balances statistical confidence and speed of decision-making, adaptively making decisions when precisely enough evidence has accumulated and minimizing unnecessary evaluation trials.

## Problem Formulation

Section III introduced the policy comparison problem, which seeks guarantees as in Equation 1. The challenge in designing a test is the complexity of $\mathcal{D}_{R}^{\lbrack i\rbrack}$, as our procedure must be robust to *any such progress metrics arising in practice*.

### IV-A The Formal Hypotheses

We formulate the problem in the context of frequentist statistical testing. To do so, we construct a general null (skeptical) hypothesis and an alternative (desired) hypothesis which reflect *all possible* cases of Equation 1.

In the general nonparametric case (see Section II-C), we consider the set $\mathcal{M}_{\lbrack 0,1\rbrack}$ of all Lebesgue-measurable distributions on the real interval $\lbrack 0,1\rbrack$ (i.e., all progress metrics per 1. ‣ III Preliminaries ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison")). We partition $\mathcal{M}_{\lbrack 0,1\rbrack}$ into two parts:^33^3For a parametric family $\Theta$ (e.g., Bernoulli distributions), the same formalism holds with a restriction to $\Theta^{2} \subseteq \mathcal{M}_{\lbrack 0,1\rbrack}^{2}$

Comparing the means amounts to formulating null and alternative hypotheses as $\mathcal{H}_{0}:{{(\mathcal{D}_{R}^{\lbrack 0\rbrack},\mathcal{D}_{R}^{\lbrack 1\rbrack})} \in S^{-}}$ and $\mathcal{H}_{1}:{{(\mathcal{D}_{R}^{\lbrack 0\rbrack},\mathcal{D}_{R}^{\lbrack 1\rbrack})} \in S^{+}}$, respectively.

These can be intuitively understood as "all possible true states of the world in which the novel innovation is not better" ($\mathcal{H}_{0}$, the 'skeptic'), and "all possible true states of the world in which the novel innovation is better" ($\mathcal{H}_{1}$, the 'desired result'). Equation 1 amounts to being $1 - \alpha^{\ast}$ confident that the true state is *not* in $S^{-}$.

### IV-B Measuring the Quality of an Evaluation Algorithm

Having formulated the test hypotheses $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$, we consider how to measure the quality of any potential evaluation scheme. These measures can be understood intuitively: the optimal evaluation protocol should *make correct decisions* and *make the decisions as quickly as possible*.

There are precise mathematical analogues of these desiderata. In particular, there are two types of errors which can be made. First, in the case that $\mathcal{H}_{0}$ is true, the evaluation algorithm may incorrectly decide that $\mathcal{H}_{1}$ is true. This is termed a false positive, or a 'Type-1 Error.' The rate at which such errors occur (under a particular decision-making protocol) is denoted $\alpha \in {}$. Equation 1 precisely amounts to the statement "the Type-1 Error rate of our evaluation method must be less than $\alpha^{\ast}$." In the case that $\mathcal{H}_{1}$ is true, the protocol may incorrectly decide that $\mathcal{H}_{0}$ is true. This is a false negative, or a 'Type-2 Error.' The rate at which this occurs is denoted $\beta \in {}$. Semantically, a Type-1 Error corresponds to reporting a false discovery --- that the new policy is better *when it actually is not*. A Type-2 Error corresponds to a missed discovery --- failing to discern that the new policy is better *when it actually is*. These two error types combine to give a complete accounting of the algorithm's correctness. The last metric pertains to sample efficiency: how long the algorithm takes to make a decision, denoted ${\mathbb{E}}{\lbrack N\rbrack}$.^44^4For technical reasons, sample efficiency must be posed with respect to a measure over $S^{+}$. This amounts in practice to prior beliefs over features like the size of the gap in performance; the reader may safely assume, e.g., an 'uninformative' uniform measure. As presented, an optimal evaluation algorithm --- one that is fast and correct --- minimizes all three of the measures $\{\alpha,\beta,{{\mathbb{E}}{\lbrack N\rbrack}}\}$.

### IV-C Efficient Tests as a Multi-Objective Optimization

Unfortunately, there are fundamental tradeoffs which prevent simultaneous minimization of all of these metrics. Therefore, we adopt the Neyman-Pearson testing approach, which normatively chooses the Type-1 Error rate as the quantity to be rigorously controlled. This amounts to requiring that $\alpha \leq \alpha^{\ast}$ be treated as a hard constraint. Having made this selection, the problem of designing an evaluation procedure reduces to finding (near-)optimal solutions to the following multi-objective optimization problem:

Here, $\Gamma$ denotes a space of decision-making rules (evaluation procedures) and $\lambda \in {\lbrack 0,\infty)}$ is a nonnegative parameter trading off the expected time to decision and false negative rate.

Efficiently solving Equation 2 results in an evaluation procedure that is guaranteed to maintain statistical rigor and quickly and effectively detects changes in performance. This provides the roboticist with the capacity to quickly iterate on new innovations, while ensuring justified and well-calibrated confidence in reported performance improvements.

## Methodology

We motivate the N-SCORE procedure via the construction of a process to distinguish $S^{-}$ from $S^{+}$. Intuitively, we will construct a scalar-valued dynamical system that behaves fundamentally differently when $\mathcal{H}_{0}$ is true than when $\mathcal{H}_{1}$ is true, based on the empirical evidence observed during evaluation. This difference is precisely in the sense of being stable in the former case and unstable in the latter. The testing problem then reduces to assessing the stability properties of the dynamical system; this assessment can be rigorously quantified within the SAVI framework described in Section II-C.

### V-A Constructing an 'Evidence Integrator'

A natural correlate to $\mathcal{H}_{1}$ is the difference in the evaluation reward; if we are on the $n^{th}$ evaluation trial, we consider:

where $\xi > 0$ is a positive scaling factor and $r_{0,n}$, $r_{1,n}$ are the observed progress values. Intuitively, the evidence for $\mathcal{H}_{1}$ is positive when $r_{1,n} > r_{0,n}$ and negative otherwise. Note that by assumed independence of the evaluation trials, this relationship does not depend on $n$. What remains is to design the appropriate rate of integration of this evidence. Results in the SAVI literature and across a variety of statistical estimation contexts suggest that the optimal aggregation rate is *multiplicative*, resulting in a measure of aggregate evidence $X_{n}$ (setting $X_{0} = 1$ w.l.o.g.) that evolves according to:

Therefore, when the evidence is positive for $\mathcal{H}_{1}$, the growth rate is greater than one, and the system is locally unstable. Conversely, when it is negative (i.e., in favor of $\mathcal{H}_{0}$), the growth rate is less than one and the system is stable. We can additionally optimize $\xi_{n} = {g{(\mathcal{F}_{n - 1})}}$ online based on the evidence accumulated so far (the 'natural filtration' $\mathcal{F}_{n - 1}$), as long as the choice of $\xi_{n}$ is independent of $(r_{0,n},r_{1,n})$.

The last step is designating an evidence threshold, amounting to the idea that "$X_{n}$ has become sufficiently unstable as to provide sufficient evidence that the true state of the world is not in $\mathcal{H}_{0}$." We designate the threshold to be $1/\alpha^{\ast}$, for a desired Type-1 Error rate $\alpha^{\ast}$ of the test procedure.

This procedure is operationalized in Algorithm 1. As shown in Section V-B, this evaluation protocol efficiently balances time-to-decision and correctness, while rigorously controlling the Type-1 Error rate at tunable, pre-specified level $\alpha^{\ast}$. These properties enable rigorous confidence in comparison problems (yielding statements of the form of Equation 1) while minimizing the evaluation burden necessary to reliably form them.

Type-1 error limit α* ∈, evaluation limit Nmax &gt; 0.
while $\overline{X} &lt; {1/\alpha^{\ast}}$ and n ≤ Nm a x do
Observe evaluation progress scores: r0, n, r1, n
Update test statistic: $\overline{X}\leftarrow{\max{\{\overline{X},X_{n}\}}}$
if $\overline{X} &lt; {1/\alpha^{\ast}}$ then
return Fail to Reject Null
return Reject Null
Algorithm 1 N-SCORE Evaluation Protocol

### V-B Theoretical Properties of Algorithm 1

We briefly present several key theoretical results of the evaluation protocol effectuated in Algorithm 1. The import of these results, along with proof sketches, are included *in situ*. Detailed proofs are deferred to the Supplement.

We begin with a critical lemma pertaining to a property of the evidence aggregation process in Equation 3. This property amounts to a statement that the stochastic process $X_{n}$ is stable in expectation *for all* elements $h \in \mathcal{H}_{0}$.

### Lemma 1 (Null Stability (NSM) Property)

Consider the stochastic process $\{ X_{n}\}$ defined in Equation 3, setting (w.l.o.g.) $X_{0} = 1$. Then the expectation of $\{ X_{n}\}$ is contracting in time with respect to the current value, for all $h \in S^{-}$ for any $\xi_{n} \in {\lbrack 0,1\rbrack}$. That is:

1 Property). ‣ V-B Theoretical Properties of Algorithm 1 ‣ V Methodology ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison") is necessary for ensuring stability of the process in Equation 3 because it rules out (with high probability) that evidence increments generated by any element of $\mathcal{H}_{0}$ will cause the process to grow by very much. This is a necessary step to ensure Type-1 Error control and enforce the hard constraint in Equation 2, which is formalized in 1. ‣ V-B Theoretical Properties of Algorithm 1 ‣ V Methodology ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison").

### Theorem 1 (Type-1 Error Control of Algorithm 1)

Consider the evaluation procedure in Algorithm 1, utilizing the process defined in Equation 3. Then

### Proof

The proof uses 1 Property). ‣ V-B Theoretical Properties of Algorithm 1 ‣ V Methodology ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison") in concordance with Ville's Inequality to bound the probability of observing large values of $X_{n}$. After verifying several ancillary conditions and matching constants, the bound can be computed directly. More detail can be found in the Supplement. ∎

Enforcing Type-1 Error control ensures high confidence (at level $1 - \alpha^{\ast}$) that reported significant innovations and improvements to the state-of-the-art are strictly separated from the inherent noise in robotic evaluation.

### Remark 1 (Efficient Optimization of $\xi_{n}$)

Consider the stochastic process family described in Equation 3, and let $\mathcal{F}_{n}$ be the natural filtration ${\{{(r_{0,i},r_{1,i})}\}}_{i = 1}^{n - 1}$ at step $n$. There exists an efficient algorithm to maximize (online) over ${\{\xi_{n}\}}_{n = 1}^{N}$ the expected growth rate of ${\{ X_{n}\}}_{n = 1}^{N}$.

Intuitively, $\xi_{n}$ modulates the degree of confidence in marginal changes to $X_{n}$. Large $\xi_{n}$ grow the process more quickly when data is favorable, but are penalized more harshly when it is not. Identifying an effective strategy to modulate $\xi_{n}$ online is central to improving sample efficiency across a broad array of evaluation problems. To do this, N-SCORE utilizes intuition from kernel density estimation and the structure of the discrete partial credit setting to optimize $\xi_{n}$ via constructing explicit nonparametric representations of $\mathcal{D}_{R}^{\lbrack i\rbrack}$. This is represented as a family N-SCORE~k~, where $k \in {\mathbb{N}}$ is a real-valued parameter akin to the kernel bandwidth. For brevity, details about this optimization are deferred to the Supplement. However, we emphasize that this optimization has strong practical benefits, yielding a state-of-the-art near-optimal solution to Equation 2 for general progress metrics.

## Experimental Results

We evaluate N-SCORE across a broad suite of evaluation settings, including some of the largest available datasets for real-world robot comparison with task progress metrics, such as RoboArena and the LBM 1.0 study. To organize the results, we tie them to three core research questions (RQs):

(Sequential Evaluation) Are there sample efficiency benefits of sequential evaluation?

(Informative Metrics) Are there sample efficiency benefits from using more informative evaluation metrics than coarse binary success?

(Technical Novelty) What are the benefits of N-SCORE with respect to statistically valid sequential policy comparison approaches?

### VI-A Baseline Methods

We introduce three relevant baselines, proceeding in order of increasing generality. The recently proposed STEP procedure demonstrated SOTA performance in the setting of binary success metrics. However, STEP is tailored to this narrow, but important setting and does not generalize to more informative metrics. Another recent work proposed a safe, anytime-valid inference approach to parametric comparison problems, motivated by settings with discrete partial credit. This method, termed $\theta$-SAVI to denote its parametric nature, is more general than STEP, as it retains validity for any parametric comparison setting (defined in Section II-B). As with STEP, $\theta$-SAVI cannot extend to nonparametric performance metrics such as continuous-valued progress scores. The most general evaluation procedure is the test dual to the WSR estimation method, which is also most similar among the baselines to our approach. Thus, the key comparison between WSR and N-SCORE will center on sample efficiency.

### VI-B RQ1 and RQ2: Sequential Evaluation with Informative Metrics

Our experiments support the observations in Snyder et al. that sequential test procedures save significant time and resources for robotics evaluations under binary success metrics. We further observe the benefit of sequential procedures to extend to more fine-grained evaluation metrics.

TABLE I: Average time-to-decision (TTD) and empirical power for each method on simulated data. For Bernoulli data (left), TTD is averaged over all 35 alternative hypotheses, while Power is averaged only the 9 hardest alternative hypotheses corresponding to a gap of 0.1 (all other 26 alternatives have empirical power 1). For each alternative, metrics are averaged over 250 independent redraws; each redraw has N = 1000. We observe similar statistical power for all methods except WSR, which lags substantially due to high variance in the Bernoulli regime. For nonparametric data (right), TTD and power are averaged over 3000 independent redraws (there is only one alternative). Only N-SCORE∞ and WSR are valid in the nonparametric regime; the remaining methods cannot be adapted to this case. We observe that N-SCORE∞ outperforms WSR by approximately 15% on average in terms of time-to-decision, while improving the empirical power by approximately 5 percentage points.

### VI-B1 Results on Artificial Bernoulli Sequences

The left-hand side of Table I shows the average time-to-decision for each baseline and N-SCORE on artificially generated Bernoulli data comprising 35 different distributions, where each baseline is tested on each distribution 250 times. In each instance, the batch evaluation size was set to $N = 1000$ samples per test. Further visualizations of these tests are deferred to the Supplement. The average time-to-decision is shown to be significantly less than 1000 samples, illustrating the practical benefit of early stopping when the evaluation problem is sufficiently easy as to not require the full batch allocation.

Figure 2: Policy performance comparisons on crowd-sourced real-world evaluations on the DROID setup from RoboArena. The violin plots represent empirical distributions of observed results. Policies with different letters are statistically distinguishable by the method. Policies are compared at a global error bound of α = 0.05 with a Bonferroni correction.

### VI-B2 Results on LBM 1.0 Binary Evaluation

We now consider real-world binary evaluation data for robot policies from the LBM 1.0 study results. The binary success metric results are on the right side of Table II. In this example, a pretrained and then finetuned policy is compared to a single-task policy trained from scratch to evaluate performance; it is desired to test whether the pretrained policy outperforms the single-task policy on challenging, long-horizon tasks. The tasks and rollout data come from the experimental setup of LBM 1.0. The top half considers robot performance comparison in high-fidelity simulator data. For each task and method, the time-to-decision (TTD) is recorded in terms of the number of evaluations per policy before a comparison outcome at level $\alpha = 0.05$ was reached. The total number of nominal batch evaluations is $2000$. We observe savings of ${25\%} - 35$% from the use of sequential evaluation procedures, resulting in an empirical reduction in the requisite number of simulations of approximately 500-700. In the bottom half, we consider the same comparison on hardware. In this setting, the nominal batch evaluation burden is $500$. We again observe significant savings, on the order of ${16\%} - 25$%, corresponding to a savings of up to $125$ total evaluations on this task suite.

Binary Success/Failure Metrics

TABLE II: Time-to-decision for all simulation (top) and hardware (bottom) policy comparisons for evaluation context . If a decision is not reached, the entry is left blank; for the purpose of computing evaluation savings, any blank entry is counted at N trials. All simulation tasks utilize N = 200; all hardware tasks utilize N = 50. The total number of trials is the column sum multiplied by two (because there are two policies being evaluated, and each must be run). Thus, a column in the top half could require up to 2000 simulated trajectories; one in the bottom half could require up to 500 hardware evaluations. Several important observations are: sequential evaluation saves significant evaluation effort over batch methods (right); more informative partial credit metrics can provide even greater savings (left). In fact, for these evaluations, the savings are up to 50% on hardware and 70% in simulation.

RQ2 considers the efficiency of evaluation in settings which go beyond binary metrics. Following the structure of RQ1, we again consider significant evidence from both simulated and real-world evaluation data. Here, however, the core purpose is to illustrate the generality of nonparametric approaches, which open up opportunities for rigorous comparison of richer metrics, including RL rewards and continuous progress metrics.

### VI-B3 Results on Simulated Nonparametric Data

We again start with results on simulated data, now generated from nonparametric densities. Random polynomials of order up to 10 are generated, and then rectified into an appropriate density (they are shifted and scaled to be everywhere nonnegative on $\lbrack 0,1\rbrack$ and to integrate to 1). This process is analytically opaque, making it difficult to express the resulting family of distributions in any parametric form. Thus, only N-SCORE and WSR are applicable. We run $3000$ comparison sequences of pairs of these distributions, limiting to cases where the gap in mean performance is at least $0.01$. $N = 1000$ for each sequence. The right-hand side of Table I shows summary statistics for N-SCORE and WSR, respectively. Again, the average time-to-decision is very low in comparison to the batch allocation, suggesting that distribution complexity does not impede efficient comparison, and does not attenuate the sample efficiency benefits of this evaluation paradigm.

### VI-B4 Results on LBM 1.0 Partial Credit Evaluation

We repeat the analysis of the task and rollout data obtained from Barreiros et al., as described in the preceding section, but using the discrete partial credit rubric instead of binary success metrics. Before each task was evaluated, partial credit measures (e.g., completion rate of $K$ subtasks) were designed to provide fine-grained information on the policy performance. In every task, this varied between six and eight partial credit outcomes; each subtask was weighted equally in the scoring. As before, the top half corresponds to policy evaluation in high-fidelity simulation, with a total evaluation budget of $2000$ rollouts. As shown in the left-hand side of Table II, partial credit metrics yield savings of approximately $70$%, corresponding to a nearly $1400$-sample reduction in the number of evaluations for each sequential procedure. Further, this corresponds to an equivalent improvement over sequential binary methods, such as STEP, of over $50$%. On hardware trials, the results are similar in trend. We observe approximately $45$% reduction in the number of required evaluations with respect to the batch procedure (which arbitrarily chooses 50 runs per task per policy). This corresponds to a ${24\%} - {30\%}$ reduction in evaluation burden with respect to SOTA binary procedures like STEP. The preceding evaluation gives strong empirical evidence for answering RQ1 and RQ2 in the affirmative: sequentialized evaluation reliably improves sample efficiency on artificial and real-world data across a wide range of metrics and uncertainty distributions.

### VI-C RQ3: Improving Sample Complexity Over Baselines

Finally, we discuss instances of performance differences between N-SCORE and related baselines.

### VI-C1 Simulated Nonparametric Data

From the right-hand side of Table I, there is a moderate gap in average time-to-decision, corresponding to average savings of around 15% in evaluation burden. This can be understood as the aggregate effect of the efficient mechanism to optimize $\xi_{n}$ (see Algorithm 1), which does not have a clear analogue in the WSR approach. Furthermore, neither STEP nor the $\theta$-SAVI approaches can be applied in this setting.

Due to the generality of the nonparametric testing paradigm, the times-to-decision can be statistically compared using the N-SCORE framework. To do this, the 3000 runs are randomly partitioned into two sets, each of size 1500, corresponding to the time-to-decision of one of the two methods (N-SCORE or WSR) on that data. These can be sequentially compared using the metrics $r_{i,n} = \frac{\text{ttd}_{i,n}}{N}$. Note that to run this evaluation in a parametric model would require dimension ${N + 1} = 1001$. The N-SCORE procedure returns a decision at $\alpha = 0.05$ in approximately $525$ evaluations, corresponding to the hypothesis: "the N-SCORE procedure has a lower time-to-decision than WSR on this class of nonparametric densities w.p. $\geq 0.95$."

### VI-C2 Simulated Bernoulli Data

We consider the left-hand side of Table I to specifically consider the differences between sequential evaluation methods. Here, all baselines are applicable. We observe that STEP is optimal, as expected in this setting. However, among the remaining methods, $\theta$-SAVI and N-SCORE perform nearly identically, suggesting that our approach is able to efficiently approximate the available parametric structure. WSR, conversely, suffers substantially in the time-to-decision as compared to these approaches.

### VI-C3 LBM 1.0 Success and Partial Credit

Now, we revisit the results in Table II to consider the implications for each evaluation procedure. Here, we observe that STEP is again optimal for binary success measures, consistent with the previous section. For this data, $\theta$-SAVI, N-SCORE, and WSR are equally effective in both binary and discrete partial credit evaluation on this dataset.

### VI-C4 Results on RoboArena

We continue the analysis of real-world evaluation data by illustrating the efficacy of N-SCORE, in addition to its applicability to multi-policy comparisons using continuous progress evaluation scores, in simultaneously comparing four policies from the open-source RoboArena benchmark. Further details of the dataset are deferred to the Supplement. Because the rewards are continuous, only N-SCORE and WSR can be applied. Figure 2 illustrates the time-to-decision (TTD) in terms of the number of trials required for each policy by N-SCORE and WSR. N-SCORE is able to distinguish the performance of all policies. In contrast, while WSR is able to correctly distinguish the best policy as $\pi_{0}$-FAST, it is unable to separate $\pi_{0}$ and PG-Diff even after exhausting all available 641 trials. Notably, N-SCORE requires over 200 fewer trials of $\pi_{0}$, and results in a total savings of at least 450 trials (1419 vs. 1881). The efficacy of our method can be attributed to efficient optimization of $\xi_{n}$ (see 1. ‣ V-B Theoretical Properties of Algorithm 1 ‣ V Methodology ‣ Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison")) with the available data, and due to WSR not being optimized for policy comparison.

TABLE III: Time-to-decision for selected reinforcement learning policy comparisons on Mujoco benchmarks. If a decision is not reached, the entry is left blank; for the purpose of computing evaluation savings, any blank entry is counted at N trials. All simulated tasks utilize N = 1000. We observe similar behavior between N-SCORE and WSR on easier instances (with lower times-to-decision); however, in harder instances significant improvements can be observed. In aggregate, the hard instances dominate sample complexity, resulting in substantial savings in evaluation burden.

### VI-C5 Real-valued Continuous Metrics

The final example we consider is determining the best reinforcement learning (RL) policy based on continuous-valued episodic rewards, whose underlying distribution is difficult to model. Table III lists the time-to-decision in distinguishing popular RL algorithms (PPO, TD3, DDPG, and SAC) on Mujoco benchmarks. Due to the continuous nature of the reward metric, only N-SCORE and WSR are applicable. We observe significant improvement over the WSR baseline when policies perform similarly but have high variance such as in the case of InvertedPendulum-v4. In this instance, N-SCORE saves over 400 trials when comparing PPO with DDPG. For the same benchmark, SAC and TD3 are highly effective, returning the maximum possible reward in each rollout, thereby leading to no statistical separation by either method. We provide further experimental details including mean episodic return and violin plots in the Supplement.

As demonstrated by these extensive empirical validations, the key impact of our novel approach lies in effectively matching the sample efficiency of $\theta$-SAVI in parametric contexts (e.g., Table I and Table II), while maintaining the generality of, and improving sample efficiency over, the WSR procedure in nonparametric contexts (e.g., Table III and Figure 2).

## Limitations and Future Work

There are several current limitations of N-SCORE, which suggest the possibility for valuable future investigation. First, unlike STEP, any procedure using tools from safe, anytime-valid inference (SAVI) tends to achieve tighter Type-1 error control than specified, leaving some 'risk budget' unused. This both explains the gap to STEP in the regime of binary evaluation metrics and the capacity for robust generalization to complex and nonparametric measures. Developing a finite-$N$ rectification to use the full available risk budget would be exceedingly valuable for a host of problems for which SAVI is currently applied. Similarly, the current method for optimizing $\xi_{n}$ has connections to ideas in kernel density estimation, but at present the full insight of developments in the latter have not been applied to our approach. Using these tools and domain knowledge promises more efficiency and potential generalization to unbounded performance measures.

We note that, while SAVI methods naturally hinder some avenues towards inadvertent data dredging, they rely crucially on i.i.d. evaluation data. Moreover, rigorous guarantees are only meaningful if the evaluation paradigm is similarly rigorous and reproducible. As such, these methods are inherently dependent on careful and measured evaluation procedures.

## Conclusion

We have introduced and validated a novel procedure for statistically rigorous sequential evaluation of robot policies, generalized to metrics that go beyond binary success and failure rates. In so doing, we have highlighted the practical benefits of sequential methods and informative metrics to reduce evaluation burden, and situated our approach as a novel synthesis of two state-of-the-art sequential evaluation procedures. Each of these results is validated by substantial empirical evidence spanning simulated and real-world evaluation data. The promise of such results is to both codify *and accelerate* progress within the field, by ensuring reliable performance improvements and minimizing the requisite evaluation burden necessary to confirm them.
