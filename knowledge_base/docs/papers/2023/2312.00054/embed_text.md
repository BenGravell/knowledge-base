<!-- arxiv-full-text:v1 {"arxiv_id": "2312.00054", "source": "arxiv-pdf"} -->

## Introduction

Inverse Reinforcement Learning (IRL) aims to recover reward functions from demonstrations of an expert policy, in contrast to standard reinforcement learning which aims to learn optimal policies for a given reward function. IRL has applications in numerous domains such as robotics, target-driven navigation tasks, game AI, and medical decision-making. The learned reward functions in these applications are typically used for replicating the expert behaviors in similar or varying downstream environments. Broadly, the problem of learning reward functions from data is of rising importance beyond the scope of IRL, and is used in procedures such as Reinforcement Learning from Human Feedback (RLHF) for aligning large language models.

Despite the success of IRL in practical applications, theoretical understanding is still in an early stage and presents several unique challenges, especially when compared with standard RL (finding optimal policy under a given reward) where the theory is more established. First, the solution is inherently non-unique for any IRL problem-For example, for any given expert policy, zero reward is always a feasible solution (making the expert policy optimal under this reward). A sensible definition of IRL would require not just recovering a single reward function but instead a set of feasible rewards. Second, theoretical results for IRL is lacking even for some standard learning settings, such as learning from an offline dataset of trajectories from the expert policy (akin to an imitation setting). Finally, as a more nuanced challenge (but related to both challenges above), so far there is no commonly agreed performance metric for measuring the distance between the estimated reward set and the ground truth reward set. Existing performance metrics in the literature either require strong feedback such as a simulator, or do not require the returned solution to be aware of the transition dynamics Lindner et al. (see Section 3.3 for a discussion). These challenges motivate the following open question: ∗ University of Science and Technology of China. Email: zl20071451@mail.ustc.edu.cn.

‡ Salesforce AI Research. Email: yu.bai@salesforce.com.

† Princeton University. Email: mengdiw@princeton.edu.

## Is IRL more difficult than standard RL?

In this paper, we theoretically study IRL in standard episodic tabular Markov Decision Processes without Rewards (MDP \ R's) under vanilla offline and online learning settings. Our contributions can be summarized as follows.

- The goal of IRL is to output a set of rewards that approximate the ground truth set of feasible rewards, i.e. rewards under which the expert policy is optimal. We define new metrics for both reward functions and for IRL using the concept of reward mapping, which can be viewed as a 'generating function' of the (ground truth) set of feasible rewards (Section 2.1 & 3.1). We show that our metrics are stronger / more appropriate than existing metrics in certain aspects (Section 3.3). - We show that any estimated reward that is similar in our metric and satisfies monotonicity with respect to the true reward admits an approximate planning/learning guarantee (Section 3.2). - We design an algorithm, Reward Learning with Pessimism (RLP) that performs IRL from any given offline demonstration dataset (Section 4). Our algorithm returns an estimated reward mapping that is ϵ -close in our metric and satisfies monotonicity, and requires a number of episodes that is polynomial in the size of the MDP as well as the single-policy concentrability coefficient between the evaluation policy and the behavior policy that generated the states of the offline dataset. To our best knowledge, this is the first provably sample-efficient algorithm for IRL in the standard offline setting.

Technically, the algorithm seamlessly adapts the pessimism principle from the offline RL literature to achieve the desired monotonicity and closeness conditions, demonstrating that IRL is 'not much harder than standard RL' in a certain sense.

- We next design an algorithm Reward Learning with Exploration (RLE), which operates in a natural online setting where the learner can both actively explore the environment and query the expert policy, and achieves IRL guarantee in a stronger metric from polynomial samples (Section 5). Algorithm RLE builds on a simple reduction to reward-free exploration and the RLP algorithm. - We establish sample complexity lower bounds for both the offline and online settings, showing that our upper bounds are nearly optimal up to a small factor (Section 4.4 & 5.3). - We extend our results to a transfer learning setting, where the learned reward mapping is transferred to and evaluated in a target MDP \ R different from the source MDP \ R. We provide guarantees for RLP and RLE under certain similarity assumptions between the source and target MDP \ Rs (Section 6 & Appendix I).

## Related work

Inverse reinforcement learning Inverse reinforcement learning (IRL) was first proposed by Ng and Russell and since then significantly developed in various follow-up approaches such as feature matching, maximum margin, maximum entropy, relative entropy, and generative adversarial imitation learning. Other notable approaches include Bayesian IRL which subsume IRL, and the reduction method.

IRL has been successfully applied in many domains including target-driven navigation tasks, robotics, medical decision-making, and game AI.

Theoretical understandings of IRL Despite their successful applications, theoretical understandings of IRL are still in an early stage. Recently, Metelli et al. pioneered the investigation of the sample complexity of IRL under the simulator (generative model) setting where the learner can directly query feedback from any (state, action) pair. This work was later extended by Metelli et al., who introduced a framework based on Hausdorff-based metrics for measuring distances between reward sets, examined relationships between different metrics, and provided corresponding lower bounds. However, their results critically rely on the simulator setting and do not generalize to more realistic offline/online learning settings. Dexter et al. also performed a theoretical analysis for IRL in the simulator setting with continuous states and discrete actions.

The recent work of Lindner et al. considers IRL in the online setting where the learner can interact with the MDP \ R in an online fashion, which is closely related to our results for the online setting. Compared with our metric, their metric is defined for an estimated IRL problem (instead of an estimated reward set). Further, their metric does not effectively take into account the estimated transitions, which can lead to a family of counter-exmaples where the estimated IRL problem achieves perfect recovery under their metric, but the induced reward sets are actually far from the true feasible reward set in our metric (cf. Section 3.3 for a detailed discussion). Our work improves upon the above works by introducing new performance metrics for IRL, and providing new algorithms for standard learning settings such as offline learning.

Relationship with standard RL theory Our work builds upon various existing techniques from the sample-efficient RL literature to design our algorithms and establish our theoretical results. For the offline setting, our algorithm and analysis build upon the pessimism principle and the single-policy concentrability condition commonly used in offline RL. For the online setting, we adapt the reward-free learning algorithm of Li et al. to find a policy that achieves a certain concentrability-like condition with respect to all policies.

We note theoretical results on imitation learning and RLHF, which are related to but different from (and do not imply) our results. Additional related work is discussed in Appendix A.

## Preliminaries

Markov Decision Processes without Reward We consider episodic Markov Decision Processes without Reward (MDP \ R), specified by M = ( S, A, H, P ), where S is the state space with |S| = S, A is the action space with |A| = A, H is the horizon length, P = { P h } h ∈ [ H ] where P h ( ·| s, a ) ∈ ∆( S ) is the transition probability at step h. Without loss of generality, we assume that the initial state is deterministically some s 1 ∈ S.

Reward functions A reward function r: [ H ] ×S × A → maps a state-action-time step triplet ( h, s, a ) to a reward r h ( s, a ). Given an MDP \ R M and a reward function r, we denote the MDP induced by M and r as M∪ r. A policy π = { π h ( · | s ) } h ∈ [ H ],s ∈S, where π h: S → ∆( A ) maps a state to an action distribution.

Values and visitation distributions A policy π = ( π h ) h ∈ [ H ], where each π h ( ·| s ) ∈ ∆( A ) for each s ∈ S. Let supp( π h ( ·| s )):= { a: π h ( a | s ) > 0 } denote the support set of π h ( ·| s ). For any policy π and any reward function r, we define the value function V π h ( ·; r ): S → R at each time step h ∈ [ H ] by the expected cumulative reward: V π h ( s; r ) = E π [ ∑ H h ′ = h r h ′ ( s h ′, a h ′ ) | s h = s ], where E π denotes the expectation with respect to the random trajectory induced by π in the MDP \ R, that is, ( s 1, a 1, s 2, a 2,..., s H, a H ), where a h ∼ π h ( s h ), r h = r h ( s h, a h ), s h +1 ∼ P h ( · | s h, a h ). Similarly, we denote the Q -function at time step h as: Q π h ( s, a; r ) = E π [ ∑ H h ′ = h r h ′ ( s h ′, a h ′ ) | s h = s, a h = a ]. For any reward r, the corresponding advantage function A π h ( ·; r ): S × A → R is defined as A π h ( s, a; r ):= Q π h ( s, a; r ) -V π h ( s; r ) and we say a policy is an optimal policy of M∪ r if A π h ( s, a; r ) ≤ 0 holds for all ( h, s, a ) ∈ [ H ] ×S × A 1. Additionally, we represent the set of all optimal policies for M∪ r as Π ⋆ M∪ r and denote the set of all deterministic policies for M∪ r as Π det M∪ r.

We introduce d π h to denote the state(-action) visitation distributions associated with policy at time step h ∈ [ H ]: d π h ( s ):= P ( s h = s | π ) and d π h ( s, a ):= P ( s h = s, a h = a | π ). Lastly, we define the operators P h and V h by [ P h V h +1 ]( s, a ):= E [ V h +1 ( s h +1 ) | s h = s, a h = a ] and [ V h V h +1 ]( s, a ):= Var [ V h +1 ( s h +1 ) | s h = s, a h = a ] applying to any value function V h +1 at time step h +1. In this paper, we will frequently employ ̂ P h and ̂ V h to represent empirical counterparts of these operators constructed based on estimated models. For any function f: S → R, define its infinity norm as ∥ f ∥ ∞:= sup s ∈S | f ( s ) | (and we define similarly for any f: S ×A → R ).

## Inverse Reinforcement Learning

An Inverse Reinforcement Learning (IRL) problem is denoted as a pair ( M, π E ), where M is an MDP \ R and π E is a policy called the expert policy. The goal of IRL is to interact with ( M, π E ), and recover reward function r 's that are feasible for ( M, π E ), in the sense that π E an optimal policy for MDP M∪ r.

Reward mapping Noting that learning one feasible reward function is trivial (the zero reward r ≡ 0 is feasible for any π E ), we consider the stronger goal of recovering the set of all feasible rewards, which can be characterized by an explicit formula by the classical result of Ng and Russell. Here we restate this result through the concept of a reward mapping.

Let R all denote the set of all possible reward functions, and R feas [ -B,B ]:= { r ∈ R all: r is feasible and | r | ≤ B } denote the set of all feasible rewards bounded by B for any B > 0. Let V:= V 1 × · · · × V H and A:= A 1 ×···×A H, where V h:= { V h ∈ R S | ∥ V h ∥ ∞ ≤ H -h +1 } and A h:= { A h ∈ R S×A ≥ 0 | ∥ A h ∥ ∞ ≤ H -h +1 } denote the set of all possible 'value functions' and 'advantage functions' respectively.

Definition 2.1 (Reward mapping). The (ground truth) reward mapping R ⋆: V × A ↦→ R all of an IRL 1 This definition of optimal policy requires π to be optimal starting from any time step h and state s ∈ S (not necessarily visitable ones), which is stronger than the standard definition but is commonly adopted in the IRL literature. problem (M, π E) is the mapping that maps any (V, A) ∈ V × A to the following reward function r: where we recall that P h is the transition probability of M at step h ∈ [H].

With the definition of reward mapping ready, we now restate the classical result of Ng and Russell, which shows that the reward mapping R generates a set of rewards that is a superset of R feas -the set of all -bounded feasible rewards-by ranging over ( V, A ) ∈ V × A.

Lemma 2.2 (Reward mapping produces all bounded feasible rewards). The set of rewards R ⋆ (V × A) = { R (V, A): (V, A) ∈ V × A} induced by R ⋆ satisfies In words, R ⋆ always produces feasible rewards bounded in [-3 H, 3 H], and the set R ⋆ (V × A) contains (is a superset of) all -bounded feasible rewards.

As IRL is concerned precisely with the recovery of the set R feas, we consider the recovery of the reward mapping R ⋆ itself as a natural learning goal-An accurate estimator ̂ R ≈ R ⋆ guarantees ̂ R ( V, A ) ≈ R ⋆ ( V, A ) for any ( V, A ) ∈ V × A, and thus imply accurate estimation of R ⋆ ( V × A ) in precise ways which we specify in the sequel.

We will also consider recovering the reward mapping on a subset Θ ⊂ V × A. We use the following standard definition of covering numbers to measure the capacity of such Θ's: Definition 2.3 (Covering number). The ϵ -covering number of Θ ⊂ V × A is defined as where V Θ h:= { V h: (V, A) ∈ Θ } denotes the restriction of Θ onto V h, and N (V Θ h; ϵ) is the ϵ -covering number of V Θ h in ∥·∥ ∞ norm.

Note that log N (Θ; ϵ ) ≤ min { log | Θ |, O ( S log( H/ϵ )) } by combining the (trivial) bound for the finite case and the standard covering number bound for Θ = V × A. In addition, the left-hand side may be much smaller than the right-hand side if Θ admits additional structure (for example, if V Θ h lies in a low-dimensional subspace of R S ).

## Performance metrics for IRL

## Metric for IRL

We now define our performance metric for IRL based on the recovery of reward mapping R ⋆. Fixing any MDP \ R M, we begin by defining our base metric d π (indexed by a policy π ) and d all between two rewards.

Definition 3.1 (Base metric for rewards). We define the metric 2 d π (indexed by any policy π) between any pair of rewards r, r ′ ∈ R all as We further define d all (r, r ′):= sup π d π (r, r ′).

In words, metric d π compares the rewards r and r ′ when executing π. Concretely, (3.1) compares the difference in the value functions V π h ( ·; r ) and V π h ( ·; r ′ ) averaged over the visitation distribution s h ∼ π, which is sensible for our learning settings as it takes into account the transition structure of M (compared with other existing metrics based the sup-distance over all states; cf. Section 3.3). The stronger metric d all takes the supremum of d π over all policy π 's.

We now define our main metric D π Θ for the recovery of reward mappings, which simply takes the supremum of d π between all pairs of rewards induced by the two reward mappings using the same parameter ( V, A ) ∈ Θ.

Definition 3.2 (Metric for reward mappings). Given any policy π and any parameter set Θ, we define the metric 2 D π Θ between any pair of reward mappings R, R ′ as We further define D all Θ (R, R ′):= sup π D π Θ (R, R ′).

(3.2) compares two reward mappings R and R ′ by measuring the distance between R ( V, A ) and R ′ ( V, A ) using our base metric and taking the sup over all ( V, A ) ∈ Θ. Another common choice in the IRL literature is the Hausdorff distance (based on some base metric) between the two sets R ( V × A ) and R ′ ( V × A ). We show that (3.2) is always stronger than the Haussdorff distance in the sense that a metric of the form (3.2) is greater or equal to the Hausdorff distance regardless of the base metric (Lemma D.3), and the inequality can be strict for some base metric (Lemma D.4).

## Implications for learning with estimated reward

For IRL, a natural desire for a base metric between rewards is that, a small metric between r and ̂ r should imply that learning (planning) using reward ̂ r in M should at most incur a small error when the true reward is r. The following result shows that our metric d π satisfies such a desiderata. The proof can be found in Appendix D.5.

Proposition 3.3 (Planning with estimated reward). Given an MDP \ R M, let r, ̂ r be a pair of rewards such that

- (a) (Small d π on near-optimal policy) d π (r, ̂ r) ≤ ϵ for some ¯ ϵ near-optimal policy π for MDP M∪ r; - (b) (Monotonicity) ̂ r h (s, a) ≤ r h (s, a) for any (h, s, a) ∈ [H] ×S × A.

Then, letting ̂ π be any ϵ ′ near-optimal policy for MDP M∪ ̂ r, i.e, V ⋆ 1 (s 1; ̂ r) -V ̂ π 1 (s 1; ̂ r) ≤ ϵ ′, we have i.e. ̂ π is also (ϵ + ϵ ′ +2¯ ϵ) near-optimal for M∪ r.

Proposition 3.3 ensures that any estimated reward ̂ r that satisfies (a) small D π Θ and (b) monotonicity with respect to the true reward will incur a small error when used in planning. We emphasize that monotonicity is necessary in order for (3.3) to hold, similar to how pessimism is necessary for near-optimal learning in offline bandits/RL. Throughout the rest of the paper, we focus on designing IRL algorithms that satisfy (a) & (b). These guarantees can then directly yield planning/learning guarantees as corollaries by Proposition 3.3, and we will omit such statements.

## Relationship with existing metrics

Our metrics d π and d all differ from several metrics for IRL used in existing theoretical work, which we discuss here.

## Algorithm 1 Reward Learning with Pessimism

- 1: Input: Dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1, parameter set Θ ⊂ V ×A, confidence level δ > 0, error tolerance ϵ > 0. - 3: Compute the empirical transition kernel ̂ P h, the empirical expert policy ̂ π E and the penalty term b θ h for all θ ∈ Θ as follows: where the visitation counts N b h (s, a):= ∑ (s h,a h) ∈D 1 { (s h, a h) = (s, a) }, N b h (s):= ∑ a ∈A N b h (s, a), N b h, 1 (s):= ∑ (s h,a h,e h) 1 { (s h, e h) = (s, 1) }, ι:= log (HSA/δ) and C > 0 is an absolute constant. end for

- 5: Output: Estimated reward mapping ̂ R defined as follows: For all (V, A) ∈ Θ, Lindner et al. measures the difference between two reward mappings implicitly by a metric D L (see (D.1)) between the two inducing IRL problems (the ground truth problem (M, π E) and the estimated problem (̂ M, ̂ π E) returned by an algorithm). The following result shows that D L is weaker than our metric D all Θ in a strong sense.

Theorem 3.4 (Relationship with D L; informal). The metric D L defined in (D.1) satisfies the following:

- (a) (Informal version of Prop. D.1) Under the same setting as Theorem 5.1 (in which our algorithm RLE achieves ϵ error in D all Θ), RLE also achieves ϵ error in D L with the same sample complexity therein. - (b) (Informal version of Prop.D.2) Conversely, there exists a family of pairs of IRL problems which has distance 0 in the D L metric but distance 1 in the D all Θ metric between the induced reward mappings.

In a separate thread, the works of Metelli et al. consider IRL under access to a simulator. Their metric between two reward functions requires the induced value/Q functions to be close uniformly over all ( s, a ) ∈ S × A (cf. Appendix D.2), regardless of whether the state is visitable by a policy in this particular MDP \ R), which is tailored to the simulator setting and does not applicable to the standard offline/online settings considered in this work. By contrast, our metrics d π and d all measure the distance between the induced value functions averaged over visitation distributions, which are more tractable for the offline/online settings.

## IRL in the offline setting

## Setting

In the offline setting, the learner does not know (M, π E), and only has access to a dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1 consisting of K iid trajectories without reward from M, where actions are obtained by executing some behavior policy π b in M: a k h ∼ π b h (·| s k h) for all (k, h), and the expert feedback e k h 's are obtained from the expert policy π E using one of the following two options: Option 1, where the learner directly observes an expert action a E,k h, is the commonly employed setting in the IRL literature. In the special case where π b = π E, we can take a E,k h:= a k h, i.e. no need for additional expert feedback when the behavior policy coincides with the expert policy. We also allow option 2, in which e k h indicates whether a k h 'is an expert action' (belongs to the support of π E h (·| s)). As we will see, both options suffice for performing IRL.

Additionally, for option 1, we require the following well-posedness assumption on the expert policy π E.

Assumption 4.1 (Well-posedness). For any ∆ ∈ (0, 1], we say policy π E is ∆ -well-posed if This assumption is also made by Metelli et al., and is necessary for ruling out the edge case where π E h (a | s) is positive but extremely small for some action a ∈ A, in which case a large number of samples is required to determine 1 { a ∈ supp(π E h (·| s)) }.

## Algorithm

We now present our algorithm Reward Learning with Pessimism ( RLP; full description in Algorithm 1) for IRL in the offline setting. RLP returns an estimated reward mapping ̂ R given any offline dataset D. At a high level, RLP consists of two main steps:

- (Empirical MDP) We estimate the transition probabilities P h and expert policy π E by standard empirical estimates ̂ P h and ̂ π E, as in (4.1) and (4.2). - (Pessimism) We compute a bonus function b θ h (s, a) for any θ = (V, A) ∈ Θ, (h, s, a) ∈ [H] ×S × A as in (4.3). The final estimated reward (and thus the reward mapping) (4.4) is defined by the empirical version of the ground truth reward (2.1) combined with the negative bonus -b θ h (s, a), for every parameter (V, A) ∈ Θ.

The specific design of b θ h (s, a) is based on Bernstein's inequality, and ensures that with high probability, for all (h, s, a, θ) simultaneously, Combined with the form of the ground truth reward R (V, A) in (2.1), a standard pessimism argument ensures the monotonicity condition [̂ R (V, A)] h (s, a) ≤ [R (V, A)] h (s, a) for all (h, s, a) and all (V, A).

Therefore, in Algorithm 1, the empirical estimates ensure that the estimated reward (4.4) is close to the ground truth reward (over s h ∼ D or equivalently the behavior policy π b ), whereas the pessimism (negative bonus) ensures the monotonicity condition, both being desired properties for IRL as discussed in Section 3.1.

## Theoretical guarantee

We now state our theoretical guarantee for Algorithm 1. To measure the quality of the recovered reward mappings, we will be considering the d π and D π Θ metric with π = π eval being any given evaluation policy. We assume that π eval satisfies the standard single-policy concentrability condition with respect to the behavior policy π b.

Assumption 4.2 (Average form single-policy concentrability). We say π eval satisfies C ⋆ -single-policy concentrability with respect to π b if (with the convention 0 / 0 = 0) Assumption 4.2 is standard in the offline RL literature, though we remark that our (4.7) only requires the average form, instead of the worst-case form made in which requires the distribution ratio to be bounded for all (h, s, a).

We are now ready to present the guarantee for RLP (Algorithm 1). The proof can be found in Appendix E.2.

Theorem 4.3 (Sample complexity of RLP ). Let π eval be any policy that satisfies C ⋆ single-policy concentrability (Assumption 4.2) with respect to π b. Assume that π E is ∆ -well-posed (Assumption 4.1) if we choose option 1 in (4.5).

Then for both options, with probability at least 1 -δ, RLP (Algorithm 1) outputs a reward mapping ̂ R such that for all (V, A) ∈ Θ and (h, s, a) ∈ [H] ×S × A, as long as the number of episodes Above, log N:= log N (Θ; ϵ/H), η:= ∆ -1 1 { option 1 }, and ˜ O (·) hides polylog(H,S,A, 1 /δ) factors.

To our best knowledge, Theorem 4.3 provides the first theoretical guarantee for IRL under the standard offline setting, showing that RLP achieves the desired monotonicity condition and small D π Θ distance for any evaluation policy π eval that satisfies single-policy concentrability with respect to π b. For small enough ϵ, the sample complexity (number of episodes required) scales as ˜ O ( H 4 SC ⋆ log N /ϵ 2 ), which depends on the number of states S, the concentrability coefficient C ⋆, as well as the log-covering number log N which always admits the bound log N ≤ ˜ O ( S ) in the worst case and may be smaller.

Apart from the log N factor, this rate resembles that of standard offline RL under single-policy concentrability. This is no coincidence, as our algorithm and proof (for both the D π eval Θ bound and the monotonicity condition) can be viewed as an adaptation of the pessimism technique for all rewards ( R ( V, A )) ( V,A ) ∈ Θ simultaneously, demonstrating that IRL is 'no harder than standard RL' in this setting. We remark that the ∆ -1 factor brought by Assumption 4.1 appears only in the ˜ O ( ϵ -1 ) burn-in term in the rate when the feedback { e k h } k,h in (4.5) comes from option 1.

Result for π eval = π E In the special case where π eval = π E, we establish a slightly stronger result where we can improve over Theorem 4.3 by one H factor ( H 4 → H 3 ) in the main term. The proof uses the specific form of our Bernstein-like bonus (4.3) combined with a total variance argument, and can be found in Appendix E.3.

Theorem 4.4 (Improved sample complexity for π eval = π E). Suppose π eval = π E which achieves C ⋆ singlepolicy concentrability with respect to π b (Assumption 4.2), and in addition sup (h,s,a) ∈ [H] ×S×A | [R ⋆ (V, A)] h (s, a) | ≤ 1 for all (V, A) ∈ Θ. Then under both options in (4.5), with probability at least 1 -δ, RLP (Algorithm 1) achieves the same guarantee as in Theorem 4.3 (D π eval Θ (R ⋆, ̂ R) ≤ ϵ and monotonicity), as long as the number of episodes Theorem 4.4 no longer requires well-posedness of π E (Assumption 4.1) in option 1. This happens due to the assumed concentrability between π E (= π eval) and π b, which can aid the learning of supp (π E h (·| s)) even without well-posedness.

IRL from full expert trajectories An important special case of Theorem 4.4 is when π b further coincides with π E. This represents a natural and clean setting where dataset D consists of full trajectories drawn from the expert policy π E, and our goal is to recover a reward mapping with a small D π E Θ. This case is covered by Theorem 4.4 by taking C ⋆ = 1 and admits a sample complexity ˜ O ( H 3 S log N /ϵ 2 ).

## Lower bound

We present an information-theoretic lower bound showing that the upper bound in Theorem 4.3 is nearly tight.

Theorem 4.5 (Informal version of Theorem H.2). For any ( H,S,A,ϵ ) and any C ⋆ ≥ 1, there exists a family of offline IRL problems where D consists of K episodes, π eval satisfies C ⋆ -concentrability at most C ⋆, Θ = V × A, and π E is ∆ well-posed with ∆ = 1, such that the following holds.

Suppose any IRL algorithm achieves D π eval Θ ( R ⋆, ̂ R ) ≤ ϵ for every problem in this family with probability at least 2 / 3, then we must have K ≥ Ω ( H 2 SC ⋆ min { S, A } /ϵ 2 ).

For Θ = V × A, the upper bound in Theorem 4.3 scales as ˜ O ( H 4 S 2 C ⋆ /ϵ 2 ). Ignoring H and polylogarithmic factors, Theorem 4.5 assert that this rate is tight for S ≤ A (so that min { S, A } = S ). The form of this min { S, A } factor in Theorem 4.5 is due to certain technicalities in the hard instance construction; whether this can be improved to an S factor would be an interesting question for future work.

## IRL in the online setting

## Setting

We now consider IRL in a natural online learning setting (also known as 'active exploration IRL' ). In each episode, the learner interacts with the IRL problem ( M, π E ) as follows: At each h ∈ [ H ], the learner receives the state s h ∈ S and chooses their action a h ∈ A from an arbitrary policy. The environment then provides the expert feedback e h as in (4.5) (from one of the two options) and transits to the next state s h +1 ∼ P h ( ·| s h, a h ). This setting shares the same expert feedback model ( e h ) with the offline setting, and differs in that the learner can interact with the environment, instead of learning from a fixed dataset pre-collected by some fixed behavior policy.

## Algorithm and guarantee

Our algorithm Reward Learning with Exploration ( RLE; Algorithm 2) performs IRL in the online setting by a simple reduction to reward-free learning and the RLP algorithm. RLE consists of two main

## Algorithm 2 Reward Learning with Exploration

- 1: Input: Parameter set Θ ⊆ V × A, confidence level δ > 0, error tolerance ϵ > 0, N,K ∈ Z ≥ 0, threshold ξ = c ξ H 3 S 3 A 3 log 10 HSA δ. - 2: Call Algorithm 3 to play in the environment for NH episodes and obtain an explorative behavior policy π b. - 3: Collect a dataset D = { (s k h, a k h, e k h) } K,H k =1,h =1 by executing π b in M. - 4: Subsampling: subsample D to obtain D trim, such that for each (h, s, a) ∈ [H] × S × A, D trim contains min { ̂ N b h (s, a), N h (s, a) } sample transitions randomly drawn from D, where ̂ N b h (s, a) and N h (s, a) are defined by where ̂ d π h (s, a) is specified in Algorithm 3.

- 5: Call RLP (Algorithm 1) on dataset D trim with parameters (Θ, δ/ 10, ϵ/ 10) to compute the recovered reward mapping ̂ R. - 6: Output: Estimated reward mapping ̂ R. steps: Call a reward-free exploration subroutine (Algorithm 3, building on the algorithm of Li et al.) to explore the environment M and obtain an explorative behavior policy π b (Line 2); Collect K episodes of data D using π b, subsample the data, and call the RLP algorithm on the subsampled data D trim to obtain the estimated reward mapping ̂ R.

We now present the theoretical guarantee of RLE. The proof can be found in Appendix F.2.

Theorem 5.1 (Sample complexity of RLE). Suppose π E is ∆ -well-posed (Assumption 4.1) when we receive feedback in option 1 of (4.5). Then for the online setting, for sufficiently small ϵ ≤ H -9 (SA) -6, with probability at least 1 -δ, RLE (Algorithm 2) with N = ˜ O (√ H 9 S 7 A 7 K) outputs a reward mapping ̂ R such that for all (V, A) ∈ Θ and (h, s, a) ∈ [H] ×S × A, as long as the total the number of episodes Above, log N:= log N (Θ; ϵ/H), η:= ∆ -1 1 { option 1 }, and ˜ O (·) hides polylog(H,S,A, 1 /δ) factors.

For small enough ϵ, RLE requires ˜ O ( H 4 SA log N /ϵ 2 ) episdoes for finding R with D all Θ ( R ⋆, ̂ R ) ≤ ϵ. Compared with the offline setting (Theorem 4.3), the main differences here are that the metric is stronger ( D all Θ versus D π eval Θ therein), and that the concentrability coefficient C ⋆ in the sample complexity is replaced with the number of actions A. This is because using online interaction, our reward-free exploration subroutine (Algorithm 3) can find a policy π b that achieves a form of 'single-policy concentrability' A with respect to any policy π; see (C.3).

To our best knowledge, the only existing work that studies IRL in the same online setting is Lindner et al., who also achieve a sample complexity 3 of ˜ O ( H 4 S 2 A/ϵ 2 + H 2 SAη/ϵ ) (for Θ = V × A ) in their performance metric D L (cf. (D.1)). However, our metric D all Θ is stronger than their D L and avoids certain indistinguishability issues of theirs, as we have shown in Theorem 3.4.

3 Extracted from the proof of Lindner et al. and taking into account the uniform convergence over V × A and dependence on η = ∆ -1 1 { option 1 }; cf. Appendix D.1.

## Lower bound

We also provide a lower bound for IRL in the online setting in the D all Θ metric. The rate of the lower bound is similar to Theorem 4.5, and ensures that the rate in Theorem 5.1 is tight up to H and polylogarithmic factors when S ≤ A.

Theorem 5.2 (Informal version of Theorem G.2). For any ( H,S,A,ϵ ), there exists a family of online IRL problems where Θ = V × A, and π E is ∆ well-posed with ∆ = 1, such that the following holds. Suppose any IRL algorithm achieves D all Θ ( R ⋆, ̂ R ) ≤ ϵ for every problem in this family with probability at least 2 / 3, then we must have K ≥ Ω ( H 3 SA min { S, A } /ϵ 2 ).

## Transfer learning

As a further application, we consider a transfer learning setting, where rewards learned in a source MDP \ R are transferred to a target MDP \ R (possibly different from the source MDP \ R). Inspired by the singlepolicy concentrability assumption, we define two concepts called weak-transferability and transferability (Definition I.2 & I.3) that measure the similarity between two MDP \ R's.

We show that when the target MDP \ R exhibits a small week-transferability (transferability) with respect to the source MDP \ R, our algorithms RLP and RLE can perform IRL with sample complexity polynomial in these transferability coefficients and other problem parameters (Theorem I.4 & I.5), and provide guarantees for performing RL algorithms with the learned rewards in the target environments (Corollary I.6 & I.7). We defer the detailed setups and results to Appendix I.

## Conclusion

This paper designs the first provably sample-efficient algorithm for inverse reinforcement learning (IRL) in the offline setting. Our algorithms and analyses seamlessly adapt the pessimism principle in standard offline RL, and we also extend it to an online setting by a simple reduction aided by reward-free exploration. We believe our work opens up many important questions, such as generalization to function approximation settings and empirical verifications.
