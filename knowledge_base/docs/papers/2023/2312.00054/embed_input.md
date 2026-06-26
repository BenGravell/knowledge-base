<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Inverse Reinforcement Learning Harder than Standard Reinforcement Learning? A Theoretical Perspective

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse Reinforcement Learning (IRL) - the problem of learning reward functions from demonstrations of an expert policy - plays a critical role in developing intelligent systems. While widely used in applications, theoretical understandings of IRL present unique challenges and remain less developed compared with standard RL. For example, it remains open how to do IRL efficiently in standard offline settings with pre-collected data, where states are obtained from a behavior policy (which could be the expert policy itself), and actions are sampled from the expert policy. This paper provides the first line of results for efficient IRL in vanilla offline and online settings using polynomial samples and runtime. Our algorithms and analyses seamlessly adapt the pessimism principle commonly used in offline RL, and achieve IRL guarantees in stronger metrics than considered in existing work. We provide lower bounds showing that our sample complexities are nearly optimal. As an application, we also show that the learned rewards can transfer to another target MDP with suitable guarantees when the target MDP satisfies certain similarity assumptions with the original (source) MDP.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse Reinforcement Learning (IRL) aims to recover reward functions from demonstrations of an expert policy, in contrast to standard reinforcement learning which aims to learn optimal policies for a given reward function. IRL has applications in numerous domains such as robotics, target-driven navigation tasks, game AI, and medical decision-making. The learned reward functions in these applications are typically used for replicating the expert behaviors in similar or varying downstream environments. Broadly, the problem of learning reward functions from data is of rising importance beyond the scope of IRL, and is used in procedures such as Reinforcement Learning from Human Feedback (RLHF) for aligning large language models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the success of IRL in practical applications, theoretical understanding is still in an early stage and presents several unique challenges, especially when compared with standard RL (finding optimal policy under a given reward) where the theory is more established. First, the solution is inherently non-unique for any IRL problem-For example, for any given expert policy, zero reward is always a feasible solution (making the expert policy optimal under this reward). A sensible definition of IRL would require not just recovering a single reward function but instead a set of feasible rewards. Second, theoretical results for IRL is lacking even for some standard learning settings, such as learning from an offline dataset of trajectories from the expert policy (akin to an imitation setting). Finally, as a more nuanced challenge (but related to both challenges above), so far there is no commonly agreed performance metric for measuring the distance between the estimated reward set and the ground truth reward set. Existing performance metrics in the literature either require strong feedback such as a simulator, or do not require the returned solution to be aware of the transition dynamics Lindner et al. (see Section 3.3 for a discussion).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These challenges motivate the following open question: ∗ University of Science and Technology of China. Email: zl20071451@mail.ustc.edu.cn.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

‡ Salesforce AI Research. Email: yu.bai@salesforce.com.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

† Princeton University. Email: mengdiw@princeton.edu.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Is IRL more difficult than standard RL?", "weight": 1.0} -->

In this paper, we theoretically study IRL in standard episodic tabular Markov Decision Processes without Rewards (MDP \ R's) under vanilla offline and online learning settings. Our contributions can be summarized as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Is IRL more difficult than standard RL?", "weight": 1.0} -->

- The goal of IRL is to output a set of rewards that approximate the ground truth set of feasible rewards, i.e. rewards under which the expert policy is optimal. We define new metrics for both reward functions and for IRL using the concept of reward mapping, which can be viewed as a 'generating function' of the (ground truth) set of feasible rewards (Section 2.1 & 3.1). We show that our metrics are stronger / more appropriate than existing metrics in certain aspects (Section 3.3). - We show that any estimated reward that is similar in our metric and satisfies monotonicity with respect to the true reward admits an approximate planning/learning guarantee (Section 3.2). - We design an algorithm, Reward Learning with Pessimism (RLP) that performs IRL from any given offline demonstration dataset (Section 4).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Is IRL more difficult than standard RL?", "weight": 1.0} -->

Our algorithm returns an estimated reward mapping that is ϵ -close in our metric and satisfies monotonicity, and requires a number of episodes that is polynomial in the size of the MDP as well as the single-policy concentrability coefficient between the evaluation policy and the behavior policy that generated the states of the offline dataset. To our best knowledge, this is the first provably sample-efficient algorithm for IRL in the standard offline setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Is IRL more difficult than standard RL?", "weight": 1.0} -->

Technically, the algorithm seamlessly adapts the pessimism principle from the offline RL literature to achieve the desired monotonicity and closeness conditions, demonstrating that IRL is 'not much harder than standard RL' in a certain sense.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Is IRL more difficult than standard RL?", "weight": 1.0} -->

- We next design an algorithm Reward Learning with Exploration (RLE), which operates in a natural online setting where the learner can both actively explore the environment and query the expert policy, and achieves IRL guarantee in a stronger metric from polynomial samples (Section 5). Algorithm RLE builds on a simple reduction to reward-free exploration and the RLP algorithm. - We establish sample complexity lower bounds for both the offline and online settings, showing that our upper bounds are nearly optimal up to a small factor (Section 4.4 & 5.3). - We extend our results to a transfer learning setting, where the learned reward mapping is transferred to and evaluated in a target MDP \ R different from the source MDP \ R. We provide guarantees for RLP and RLE under certain similarity assumptions between the source and target MDP \ Rs (Section 6 & Appendix I).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

An Inverse Reinforcement Learning (IRL) problem is denoted as a pair ( M, π E ), where M is an MDP \ R and π E is a policy called the expert policy. The goal of IRL is to interact with ( M, π E ), and recover reward function r 's that are feasible for ( M, π E ), in the sense that π E an optimal policy for MDP M∪ r.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Reward mapping Noting that learning one feasible reward function is trivial (the zero reward r ≡ 0 is feasible for any π E ), we consider the stronger goal of recovering the set of all feasible rewards, which can be characterized by an explicit formula by the classical result of Ng and Russell. Here we restate this result through the concept of a reward mapping.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Let R all denote the set of all possible reward functions, and R feas [ -B,B ]:= { r ∈ R all: r is feasible and | r | ≤ B } denote the set of all feasible rewards bounded by B for any B > 0. Let V:= V 1 × · · · × V H and A:= A 1 ×···×A H, where V h:= { V h ∈ R S | ∥ V h ∥ ∞ ≤ H -h +1 } and A h:= { A h ∈ R S×A ≥ 0 | ∥ A h ∥ ∞ ≤ H -h +1 } denote the set of all possible 'value functions' and 'advantage functions' respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Definition 2.1 (Reward mapping). The (ground truth) reward mapping R ⋆: V × A ↦→ R all of an IRL 1 This definition of optimal policy requires π to be optimal starting from any time step h and state s ∈ S (not necessarily visitable ones), which is stronger than the standard definition but is commonly adopted in the IRL literature. problem (M, π E) is the mapping that maps any (V, A) ∈ V × A to the following reward function r: where we recall that P h is the transition probability of M at step h ∈ [H].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

With the definition of reward mapping ready, we now restate the classical result of Ng and Russell, which shows that the reward mapping R generates a set of rewards that is a superset of R feas -the set of all -bounded feasible rewards-by ranging over ( V, A ) ∈ V × A.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Lemma 2.2 (Reward mapping produces all bounded feasible rewards). The set of rewards R ⋆ (V × A) = { R (V, A): (V, A) ∈ V × A} induced by R ⋆ satisfies In words, R ⋆ always produces feasible rewards bounded in [-3 H, 3 H], and the set R ⋆ (V × A) contains (is a superset of) all -bounded feasible rewards.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

As IRL is concerned precisely with the recovery of the set R feas, we consider the recovery of the reward mapping R ⋆ itself as a natural learning goal-An accurate estimator ̂ R ≈ R ⋆ guarantees ̂ R ( V, A ) ≈ R ⋆ ( V, A ) for any ( V, A ) ∈ V × A, and thus imply accurate estimation of R ⋆ ( V × A ) in precise ways which we specify in the sequel.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

We will also consider recovering the reward mapping on a subset Θ ⊂ V × A. We use the following standard definition of covering numbers to measure the capacity of such Θ's: Definition 2.3 (Covering number). The ϵ -covering number of Θ ⊂ V × A is defined as where V Θ h:= { V h: (V, A) ∈ Θ } denotes the restriction of Θ onto V h, and N (V Θ h; ϵ) is the ϵ -covering number of V Θ h in ∥·∥ ∞ norm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Note that log N (Θ; ϵ ) ≤ min { log | Θ |, O ( S log( H/ϵ )) } by combining the (trivial) bound for the finite case and the standard covering number bound for Θ = V × A. In addition, the left-hand side may be much smaller than the right-hand side if Θ admits additional structure (for example, if V Θ h lies in a low-dimensional subspace of R S ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

We now define our performance metric for IRL based on the recovery of reward mapping R ⋆. Fixing any MDP \ R M, we begin by defining our base metric d π (indexed by a policy π ) and d all between two rewards.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

Definition 3.1 (Base metric for rewards). We define the metric 2 d π (indexed by any policy π) between any pair of rewards r, r ′ ∈ R all as We further define d all (r, r ′):= sup π d π (r, r ′).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

In words, metric d π compares the rewards r and r ′ when executing π. Concretely, (3.1) compares the difference in the value functions V π h ( ·; r ) and V π h ( ·; r ′ ) averaged over the visitation distribution s h ∼ π, which is sensible for our learning settings as it takes into account the transition structure of M (compared with other existing metrics based the sup-distance over all states; cf. Section 3.3). The stronger metric d all takes the supremum of d π over all policy π 's.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

We now define our main metric D π Θ for the recovery of reward mappings, which simply takes the supremum of d π between all pairs of rewards induced by the two reward mappings using the same parameter ( V, A ) ∈ Θ.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

Definition 3.2 (Metric for reward mappings). Given any policy π and any parameter set Θ, we define the metric 2 D π Θ between any pair of reward mappings R, R ′ as We further define D all Θ (R, R ′):= sup π D π Θ (R, R ′).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Metric for IRL", "weight": 1.0} -->

(3.2) compares two reward mappings R and R ′ by measuring the distance between R ( V, A ) and R ′ ( V, A ) using our base metric and taking the sup over all ( V, A ) ∈ Θ. Another common choice in the IRL literature is the Hausdorff distance (based on some base metric) between the two sets R ( V × A ) and R ′ ( V × A ). We show that (3.2) is always stronger than the Haussdorff distance in the sense that a metric of the form (3.2) is greater or equal to the Hausdorff distance regardless of the base metric (Lemma D.3), and the inequality can be strict for some base metric (Lemma D.4).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Implications for learning with estimated reward", "weight": 1.0} -->

For IRL, a natural desire for a base metric between rewards is that, a small metric between r and ̂ r should imply that learning (planning) using reward ̂ r in M should at most incur a small error when the true reward is r. The following result shows that our metric d π satisfies such a desiderata. The proof can be found in Appendix D.5.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implications for learning with estimated reward", "weight": 1.0} -->

Proposition 3.3 (Planning with estimated reward). Given an MDP \ R M, let r, ̂ r be a pair of rewards such that

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implications for learning with estimated reward", "weight": 1.0} -->

- (a) (Small d π on near-optimal policy) d π (r, ̂ r) ≤ ϵ for some ¯ ϵ near-optimal policy π for MDP M∪ r; - (b) (Monotonicity) ̂ r h (s, a) ≤ r h (s, a) for any (h, s, a) ∈ [H] ×S × A.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implications for learning with estimated reward", "weight": 1.0} -->

Then, letting ̂ π be any ϵ ′ near-optimal policy for MDP M∪ ̂ r, i.e, V ⋆ 1 (s 1; ̂ r) -V ̂ π 1 (s 1; ̂ r) ≤ ϵ ′, we have i.e. ̂ π is also (ϵ + ϵ ′ +2¯ ϵ) near-optimal for M∪ r.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implications for learning with estimated reward", "weight": 1.0} -->

Proposition 3.3 ensures that any estimated reward ̂ r that satisfies (a) small D π Θ and (b) monotonicity with respect to the true reward will incur a small error when used in planning. We emphasize that monotonicity is necessary in order for (3.3) to hold, similar to how pessimism is necessary for near-optimal learning in offline bandits/RL. Throughout the rest of the paper, we focus on designing IRL algorithms that satisfy (a) & (b). These guarantees can then directly yield planning/learning guarantees as corollaries by Proposition 3.3, and we will omit such statements.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Relationship with existing metrics", "weight": 1.0} -->

Our metrics d π and d all differ from several metrics for IRL used in existing theoretical work, which we discuss here.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm 1 Reward Learning with Pessimism", "weight": 1.0} -->

- 1: Input: Dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1, parameter set Θ ⊂ V ×A, confidence level δ > 0, error tolerance ϵ > 0. - 3: Compute the empirical transition kernel ̂ P h, the empirical expert policy ̂ π E and the penalty term b θ h for all θ ∈ Θ as follows: where the visitation counts N b h (s, a):= ∑ (s h,a h) ∈D 1 { (s h, a h) = (s, a) }, N b h (s):= ∑ a ∈A N b h (s, a), N b h, 1 (s):= ∑ (s h,a h,e h) 1 { (s h, e h) = (s, 1) }, ι:= log (HSA/δ) and C > 0 is an absolute constant. end for

<!-- chunk {"id": "body-0035", "role": "body", "section": "Algorithm 1 Reward Learning with Pessimism", "weight": 1.0} -->

- 5: Output: Estimated reward mapping ̂ R defined as follows: For all (V, A) ∈ Θ, Lindner et al. measures the difference between two reward mappings implicitly by a metric D L (see (D.1)) between the two inducing IRL problems (the ground truth problem (M, π E) and the estimated problem (̂ M, ̂ π E) returned by an algorithm). The following result shows that D L is weaker than our metric D all Θ in a strong sense.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm 1 Reward Learning with Pessimism", "weight": 1.0} -->

Theorem 3.4 (Relationship with D L; informal). The metric D L defined in (D.1)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Algorithm 1 Reward Learning with Pessimism", "weight": 1.0} -->

- (a) (Informal version of Prop. D.1) Under the same setting as Theorem 5.1 (in which our algorithm RLE achieves ϵ error in D all Θ), RLE also achieves ϵ error in D L with the same sample complexity therein. - (b) (Informal version of Prop.D.2) Conversely, there exists a family of pairs of IRL problems which has distance 0 in the D L metric but distance 1 in the D all Θ metric between the induced reward mappings.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithm 1 Reward Learning with Pessimism", "weight": 1.0} -->

In a separate thread, the works of Metelli et al. consider IRL under access to a simulator. Their metric between two reward functions requires the induced value/Q functions to be close uniformly over all ( s, a ) ∈ S × A (cf. Appendix D.2), regardless of whether the state is visitable by a policy in this particular MDP \ R), which is tailored to the simulator setting and does not applicable to the standard offline/online settings considered in this work. By contrast, our metrics d π and d all measure the distance between the induced value functions averaged over visitation distributions, which are more tractable for the offline/online settings.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Setting", "weight": 1.0} -->

In the offline setting, the learner does not know (M, π E), and only has access to a dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1 consisting of K iid trajectories without reward from M, where actions are obtained by executing some behavior policy π b in M: a k h ∼ π b h (·| s k h) for all (k, h), and the expert feedback e k h 's are obtained from the expert policy π E using one of the following two options: Option 1, where the learner directly observes an expert action a E,k h, is the commonly employed setting in the IRL literature. In the special case where π b = π E, we can take a E,k h:= a k h, i.e. no need for additional expert feedback when the behavior policy coincides with the expert policy. We also allow option 2, in which e k h indicates whether a k h 'is an expert action' (belongs to the support of π E h (·| s)).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Setting", "weight": 1.0} -->

As we will see, both options suffice for performing IRL.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Setting", "weight": 1.0} -->

Additionally, for option 1, we require the following well-posedness assumption on the expert policy π E.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Setting", "weight": 1.0} -->

Assumption 4.1 (Well-posedness). For any ∆ ∈ (0, 1], we say policy π E is ∆ -well-posed if This assumption is also made by Metelli et al., and is necessary for ruling out the edge case where π E h (a | s) is positive but extremely small for some action a ∈ A, in which case a large number of samples is required to determine 1 { a ∈ supp(π E h (·| s)) }.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We now present our algorithm Reward Learning with Pessimism ( RLP; full description in Algorithm 1) for IRL in the offline setting. RLP returns an estimated reward mapping ̂ R given any offline dataset D.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm", "weight": 1.0} -->

- (Empirical MDP) We estimate the transition probabilities P h and expert policy π E by standard empirical estimates ̂ P h and ̂ π E, as in (4.1) and (4.2). - (Pessimism) We compute a bonus function b θ h (s, a) for any θ = (V, A) ∈ Θ, (h, s, a) ∈ [H] ×S × A as in (4.3). The final estimated reward (and thus the reward mapping) (4.4) is defined by the empirical version of the ground truth reward (2.1) combined with the negative bonus -b θ h (s, a), for every parameter (V, A) ∈ Θ.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The specific design of b θ h (s, a) is based on Bernstein's inequality, and ensures that with high probability, for all (h, s, a, θ) simultaneously, Combined with the form of the ground truth reward R (V, A) in (2.1), a standard pessimism argument ensures the monotonicity condition [̂ R (V, A)] h (s, a) ≤ [R (V, A)] h (s, a) for all (h, s, a) and all (V, A).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Therefore, in Algorithm 1, the empirical estimates ensure that the estimated reward (4.4) is close to the ground truth reward (over s h ∼ D or equivalently the behavior policy π b ), whereas the pessimism (negative bonus) ensures the monotonicity condition, both being desired properties for IRL as discussed in Section 3.1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

We now state our theoretical guarantee for Algorithm 1. To measure the quality of the recovered reward mappings, we will be considering the d π and D π Θ metric with π = π eval being any given evaluation policy. We assume that π eval satisfies the standard single-policy concentrability condition with respect to the behavior policy π b.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Assumption 4.2 (Average form single-policy concentrability). We say π eval satisfies C ⋆ -single-policy concentrability with respect to π b if (with the convention 0 / 0 = 0) Assumption 4.2 is standard in the offline RL literature, though we remark that our (4.7) only requires the average form, instead of the worst-case form made in which requires the distribution ratio to be bounded for all (h, s, a).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

We are now ready to present the guarantee for RLP (Algorithm 1). The proof can be found in Appendix E.2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Theorem 4.3 (Sample complexity of RLP ). Let π eval be any policy that satisfies C ⋆ single-policy concentrability (Assumption 4.2) with respect to π b. Assume that π E is ∆ -well-posed (Assumption 4.1) if we choose option 1 in (4.5).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Then for both options, with probability at least 1 -δ, RLP (Algorithm 1) outputs a reward mapping ̂ R such that for all (V, A) ∈ Θ and (h, s, a) ∈ [H] ×S × A, as long as the number of episodes Above, log N:= log N (Θ; ϵ/H), η:= ∆ -1 1 { option 1 }, and ˜ O (·) hides polylog(H,S,A, 1 /δ) factors.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

To our best knowledge, Theorem 4.3 provides the first theoretical guarantee for IRL under the standard offline setting, showing that RLP achieves the desired monotonicity condition and small D π Θ distance for any evaluation policy π eval that satisfies single-policy concentrability with respect to π b. For small enough ϵ, the sample complexity (number of episodes required) scales as ˜ O ( H 4 SC ⋆ log N /ϵ 2 ), which depends on the number of states S, the concentrability coefficient C ⋆, as well as the log-covering number log N which always admits the bound log N ≤ ˜ O ( S ) in the worst case and may be smaller.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Apart from the log N factor, this rate resembles that of standard offline RL under single-policy concentrability. This is no coincidence, as our algorithm and proof (for both the D π eval Θ bound and the monotonicity condition) can be viewed as an adaptation of the pessimism technique for all rewards ( R ( V, A )) ( V,A ) ∈ Θ simultaneously, demonstrating that IRL is 'no harder than standard RL' in this setting. We remark that the ∆ -1 factor brought by Assumption 4.1 appears only in the ˜ O ( ϵ -1 ) burn-in term in the rate when the feedback { e k h } k,h in (4.5) comes from option 1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Result for π eval = π E In the special case where π eval = π E, we establish a slightly stronger result where we can improve over Theorem 4.3 by one H factor ( H 4 → H 3 ) in the main term. The proof uses the specific form of our Bernstein-like bonus (4.3) combined with a total variance argument, and can be found in Appendix E.3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

Theorem 4.4 (Improved sample complexity for π eval = π E). Suppose π eval = π E which achieves C ⋆ singlepolicy concentrability with respect to π b (Assumption 4.2), and in addition sup (h,s,a) ∈ [H] ×S×A | [R ⋆ (V, A)] h (s, a) | ≤ 1 for all (V, A) ∈ Θ. Then under both options in (4.5), with probability at least 1 -δ, RLP (Algorithm 1) achieves the same guarantee as in Theorem 4.3 (D π eval Θ (R ⋆, ̂ R) ≤ ϵ and monotonicity), as long as the number of episodes Theorem 4.4 no longer requires well-posedness of π E (Assumption 4.1) in option 1. This happens due to the assumed concentrability between π E (= π eval) and π b, which can aid the learning of supp (π E h (·| s)) even without well-posedness.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Theoretical guarantee", "weight": 1.0} -->

IRL from full expert trajectories An important special case of Theorem 4.4 is when π b further coincides with π E. This represents a natural and clean setting where dataset D consists of full trajectories drawn from the expert policy π E, and our goal is to recover a reward mapping with a small D π E Θ. This case is covered by Theorem 4.4 by taking C ⋆ = 1 and admits a sample complexity ˜ O ( H 3 S log N /ϵ 2 ).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Lower bound", "weight": 1.0} -->

We present an information-theoretic lower bound showing that the upper bound in Theorem 4.3 is nearly tight.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Lower bound", "weight": 1.0} -->

Theorem 4.5 (Informal version of Theorem H.2). For any ( H,S,A,ϵ ) and any C ⋆ ≥ 1, there exists a family of offline IRL problems where D consists of K episodes, π eval satisfies C ⋆ -concentrability at most C ⋆, Θ = V × A, and π E is ∆ well-posed with ∆ = 1, such that the following holds.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Lower bound", "weight": 1.0} -->

Suppose any IRL algorithm achieves D π eval Θ ( R ⋆, ̂ R ) ≤ ϵ for every problem in this family with probability at least 2 / 3, then we must have K ≥ Ω ( H 2 SC ⋆ min { S, A } /ϵ 2 ).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Lower bound", "weight": 1.0} -->

For Θ = V × A, the upper bound in Theorem 4.3 scales as ˜ O ( H 4 S 2 C ⋆ /ϵ 2 ). Ignoring H and polylogarithmic factors, Theorem 4.5 assert that this rate is tight for S ≤ A (so that min { S, A } = S ). The form of this min { S, A } factor in Theorem 4.5 is due to certain technicalities in the hard instance construction; whether this can be improved to an S factor would be an interesting question for future work.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Setting", "weight": 1.0} -->

We now consider IRL in a natural online learning setting (also known as 'active exploration IRL' ). In each episode, the learner interacts with the IRL problem ( M, π E ) as follows: At each h ∈ [ H ], the learner receives the state s h ∈ S and chooses their action a h ∈ A from an arbitrary policy. The environment then provides the expert feedback e h as in (4.5) (from one of the two options) and transits to the next state s h +1 ∼ P h ( ·| s h, a h ). This setting shares the same expert feedback model ( e h ) with the offline setting, and differs in that the learner can interact with the environment, instead of learning from a fixed dataset pre-collected by some fixed behavior policy.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Algorithm and guarantee", "weight": 1.0} -->

Our algorithm Reward Learning with Exploration ( RLE; Algorithm 2) performs IRL in the online setting by a simple reduction to reward-free learning and the RLP algorithm. RLE consists of two main

<!-- chunk {"id": "body-0063", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

- 1: Input: Parameter set Θ ⊆ V × A, confidence level δ > 0, error tolerance ϵ > 0, N,K ∈ Z ≥ 0, threshold ξ = c ξ H 3 S 3 A 3 log 10 HSA δ. - 2: Call Algorithm 3 to play in the environment for NH episodes and obtain an explorative behavior policy π b. - 3: Collect a dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1 by executing π b in M. - 4: Subsampling: subsample D to obtain D trim, such that for each (h, s, a) ∈ [H] × S × A, D trim contains min { ̂ N b h (s, a), N h (s, a) } sample transitions randomly drawn from D, where ̂ N b h (s, a) and N h (s, a) are defined by where ̂ d π h (s, a) is specified in Algorithm 3.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

- 5: Call RLP (Algorithm 1) on dataset D trim with parameters (Θ, δ/ 10, ϵ/ 10) to compute the recovered reward mapping ̂ R. - 6: Output: Estimated reward mapping ̂ R. steps: Call a reward-free exploration subroutine (Algorithm 3, building on the algorithm of Li et al.) to explore the environment M and obtain an explorative behavior policy π b (Line 2); Collect K episodes of data D using π b, subsample the data, and call the RLP algorithm on the subsampled data D trim to obtain the estimated reward mapping ̂ R.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

We now present the theoretical guarantee of RLE. The proof can be found in Appendix F.2.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

Theorem 5.1 (Sample complexity of RLE). Suppose π E is ∆ -well-posed (Assumption 4.1) when we receive feedback in option 1 of (4.5). Then for the online setting, for sufficiently small ϵ ≤ H -9 (SA) -6, with probability at least 1 -δ, RLE (Algorithm 2) with N = ˜ O (√ H 9 S 7 A 7 K) outputs a reward mapping ̂ R such that for all (V, A) ∈ Θ and (h, s, a) ∈ [H] ×S × A, as long as the total the number of episodes Above, log N:= log N (Θ; ϵ/H), η:= ∆ -1 1 { option 1 }, and ˜ O (·) hides polylog(H,S,A, 1 /δ) factors.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

For small enough ϵ, RLE requires ˜ O ( H 4 SA log N /ϵ 2 ) episdoes for finding R with D all Θ ( R ⋆, ̂ R ) ≤ ϵ. Compared with the offline setting (Theorem 4.3), the main differences here are that the metric is stronger ( D all Θ versus D π eval Θ therein), and that the concentrability coefficient C ⋆ in the sample complexity is replaced with the number of actions A. This is because using online interaction, our reward-free exploration subroutine (Algorithm 3) can find a policy π b that achieves a form of 'single-policy concentrability' A with respect to any policy π; see (C.3).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

To our best knowledge, the only existing work that studies IRL in the same online setting is Lindner et al., who also achieve a sample complexity 3 of ˜ O ( H 4 S 2 A/ϵ 2 + H 2 SAη/ϵ ) (for Θ = V × A ) in their performance metric D L (cf. (D.1)). However, our metric D all Θ is stronger than their D L and avoids certain indistinguishability issues of theirs, as we have shown in Theorem 3.4.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Algorithm 2 Reward Learning with Exploration", "weight": 1.0} -->

3 Extracted from the proof of Lindner et al. and taking into account the uniform convergence over V × A and dependence on η = ∆ -1 1 { option 1 }; cf. Appendix D.1.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Lower bound", "weight": 1.0} -->

We also provide a lower bound for IRL in the online setting in the D all Θ metric. The rate of the lower bound is similar to Theorem 4.5, and ensures that the rate in Theorem 5.1 is tight up to H and polylogarithmic factors when S ≤ A.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Lower bound", "weight": 1.0} -->

Theorem 5.2 (Informal version of Theorem G.2). For any ( H,S,A,ϵ ), there exists a family of online IRL problems where Θ = V × A, and π E is ∆ well-posed with ∆ = 1, such that the following holds. Suppose any IRL algorithm achieves D all Θ ( R ⋆, ̂ R ) ≤ ϵ for every problem in this family with probability at least 2 / 3, then we must have K ≥ Ω ( H 3 SA min { S, A } /ϵ 2 ).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Transfer learning", "weight": 1.0} -->

As a further application, we consider a transfer learning setting, where rewards learned in a source MDP \ R are transferred to a target MDP \ R (possibly different from the source MDP \ R). Inspired by the singlepolicy concentrability assumption, we define two concepts called weak-transferability and transferability (Definition I.2 & I.3) that measure the similarity between two MDP \ R's.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Transfer learning", "weight": 1.0} -->

We show that when the target MDP \ R exhibits a small week-transferability (transferability) with respect to the source MDP \ R, our algorithms RLP and RLE can perform IRL with sample complexity polynomial in these transferability coefficients and other problem parameters (Theorem I.4 & I.5), and provide guarantees for performing RL algorithms with the learned rewards in the target environments (Corollary I.6 & I.7). We defer the detailed setups and results to Appendix I.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper designs the first provably sample-efficient algorithm for inverse reinforcement learning (IRL) in the offline setting. Our algorithms and analyses seamlessly adapt the pessimism principle in standard offline RL, and we also extend it to an online setting by a simple reduction aided by reward-free exploration. We believe our work opens up many important questions, such as generalization to function approximation settings and empirical verifications.
