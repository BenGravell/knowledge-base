<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

Topics include Imitation learning, Online learning, No-regret learning, Structured prediction, Policy learning, DAgger.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces DAgger, reducing imitation learning to no-regret online learning by repeatedly aggregating states visited by the learned policy and querying the expert there. The method directly addresses covariate shift between expert demonstrations and learner rollouts.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Sequence Prediction problems arise commonly in practice. For instance, most robotic systems must be able to predict/make a sequence of actions given a sequence of observations revealed to them over time. In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions. Imitation learning techniques, where expert demon- Appearing in Proceedings of the 14 th International Conference on Artificial Intelligence and Statistics (AISTATS) 2011, Fort Lauderdale, FL, USA. Volume 15 of JMLR: W&CP 15. Copyright 2011 by the authors.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Andrew Bagnell", "weight": 1.0} -->

Robotics Institute Carnegie Mellon University Pittsburgh, PA 15213, USA dbagnell@ri.cmu.edu strations of good behavior are used to learn a controller, have proven very useful in practice and have led to stateof-the art performance in a variety of applications. A typical approach to imitation learning is to train a classifier or regressor to predict an expert's behavior given training data of the encountered observations (input) and actions (output) performed by the expert. However since the learner's prediction affects future input observations/states during execution of the learned policy, this violate the crucial i.i.d. assumption made by most statistical learning approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Andrew Bagnell", "weight": 1.0} -->

Ignoring this issue leads to poor performance both in theory and practice. In particular, a classifier that makes a mistake with probability ϵ under the distribution of states/observations encountered by the expert can make as many as T 2 ϵ mistakes in expectation over T -steps under the distribution of states the classifier itself induces. Intuitively this is because as soon as the learner makes a mistake, it may encounter completely different observations than those under expert demonstration, leading to a compounding of errors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Andrew Bagnell", "weight": 1.0} -->

Recent approaches can guarantee an expected number of mistakes linear (or nearly so) in the task horizon T and error ϵ by training over several iterations and allowing the learner to influence the input states where expert demonstration is provided (through execution of its own controls in the system). One approach learns a non-stationary policy by training a different policy for each time step in sequence, starting from the first step. Unfortunately this is impractical when T is large or ill-defined. Another approach called SMILe, similar to SEARN and CPI, trains a stationary stochastic policy (a finite mixture of policies) by adding a new policy to the mixture at each iteration of training. However this may be unsatisfactory for practical applications as some policies in the mixture are worse than others and the learned controller may be unstable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Andrew Bagnell", "weight": 1.0} -->

We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number of mistakes/costs that grows linearly in T and classification cost ϵ ). We take a reduction-based approach that enables reusing existing supervised learning algorithms. Our approach is simple to implement, has no free parameters except the supervised learning algorithm sub-routine, and requires a number of iterations that scales nearly linearly with the effective horizon of the problem. It naturally handles continuous as well as discrete predictions. Our approach is closely related to no regret online learning algorithms (in particular Follow-The-Leader ) but better leverages the expert in our setting. Additionally, we show that any no-regret learner can be used in a particular fashion to learn a policy that achieves similar guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Andrew Bagnell", "weight": 1.0} -->

We begin by establishing our notation and setting, discuss related work, and then present the DAGGER (Dataset Aggregation) method. We analyze this approach using a noregret and a reduction approach. Beyond the reduction analysis, we consider the sample complexity of our approach using online-to-batch techniques. We demonstrate DAGGER is scalable and outperforms previous approaches in practice on two challenging imitation learning problems: 1) learning to steer a car in a 3D racing game ( Super Tux Kart ) and 2) and learning to play Super Mario Bros., given input image features and corresponding actions by a human expert and near-optimal planner respectively. Following Daumé III et al. in treating structured prediction as a degenerate imitation learning problem, we apply DAGGER to the OCR benchmark prediction problem achieving results competitive with the state-of-the-art using only single-pass, greedy prediction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Supervised Approach to Imitation", "weight": 1.0} -->

The traditional approach to imitation learning ignores the change in distribution and simply trains a policy π that performs well under the distribution of states encountered by the expert d π ∗. This can be achieved using any standard supervised learning algorithm. It finds the policy ˆ π sup: Assuming ℓ (s, π) is the 0-1 loss (or upper bound on the 01 loss) implies the following performance guarantee with respect to any task cost function C bounded: Proof. Follows from result in Ross and Bagnell since ϵ is an upper bound on the 0-1 loss of π in d π ∗.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Supervised Approach to Imitation", "weight": 1.0} -->

Note that this bound is tight, i.e. there exist problems such that a policy π with ϵ 0-1 loss on d π ∗ can incur extra cost that grows quadratically in T. Kääriäinen demonstrated this in a sequence prediction setting 1 and Ross and Bagnell provided an imitation learning example where J (ˆ π sup ) = (1 -ϵT ) J ( π ∗ ) + T 2 ϵ. Hence the traditional supervised learning approach has poor performance guarantees due to the quadratic growth in T. Instead we would prefer approaches that can guarantee growth linear or near-linear in T and ϵ. The following two approaches from Ross and Bagnell achieve this on some classes of imitation learning problems, including all those where surrogate loss ℓ upper bounds C.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Supervised Approach to Imitation", "weight": 1.0} -->

1 In their example, an error rate of ϵ > 0 when trained to predict the next output in sequence with the previous correct output as input can lead to an expected number of mistakes of T 2 -1 -(1 -2 ϵ) T +1 4 ϵ + 1 2 over sequences of length T at test time. This is bounded by T 2 ϵ and behaves as Θ(T 2 ϵ) for small ϵ.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Forward Training", "weight": 1.0} -->

The forward training algorithm introduced by Ross and Bagnell trains a non-stationary policy (one policy π t for each time step t ) iteratively over T iterations, where at iteration t, π t is trained to mimic π ∗ on the distribution of states at time t induced by the previously trained policies π 1, π 2,..., π t -1. By doing so, π t is trained on the actual distribution of states it will encounter during execution of the learned policy. Hence the forward algorithm guarantees that the expected loss under the distribution of states induced by the learned policy matches the average loss during training, and hence improves performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Forward Training", "weight": 1.0} -->

We here provide a theorem slightly more general than the one provided by Ross and Bagnell that applies to any policy π that can guarantee ϵ surrogate loss under its own distribution of states. This will be useful to bound the performance of our new approach presented in Section 3.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Forward Training", "weight": 1.0} -->

Let Q π ′ t (s, π) denote the t -step cost of executing π in initial state s and then following policy π ′ and assume ℓ (s, π) is the 0-1 loss (or an upper bound on the 0-1 loss), then we have the following performance guarantee with respect to any task cost function C bounded: Proof. We here follow a similar proof to Ross and Bagnell. Given our policy π, consider the policy π 1: t, which executes π in the first t -steps and then execute the expert π ∗. Then The inequality follows from the fact that ℓ (s, π) upper bounds the 0-1 loss, and hence the probability π and π ∗ pick different actions in s; when they pick different actions, the increase in cost-to-go ≤ u.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Forward Training", "weight": 1.0} -->

In the worst case, u could be O ( T ) and the forward algorithm wouldn't provide any improvement over the tra- ditional supervised learning approach. However, in many cases u is O or sub-linear in T and the forward algorithm leads to improved performance. For instance if C is the 0-1 loss with respect to the expert, then u ≤ 1. Additionally if π ∗ is able to recover from mistakes made by π, in the sense that within a few steps, π ∗ is back in a distribution of states that is close to what π ∗ would be in if π ∗ had been executed initially instead of π, then u will be O. 2 A drawback of the forward algorithm is that it is impractical when T is large (or undefined) as we must train T different policies sequentially and cannot stop the algorithm before we complete all T iterations. Hence it can not be applied to most real-world applications.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic Mixing Iterative Learning", "weight": 1.0} -->

SMILe, proposed by Ross and Bagnell, alleviates this problem and can be applied in practice when T is large or undefined by adopting an approach similar to SEARN where a stochastic stationary policy is trained over several iterations. Initially SMILe starts with a policy π 0 which always queries and executes the expert's action choice. At iteration n, a policy ˆ π n is trained to mimic the expert under the distribution of trajectories π n -1 induces and then updates π n = π n -1 + α (1 -α ) n -1 (ˆ π n -π 0 ). This update is interpreted as adding probability α (1 -α ) n -1 to executing policy ˆ π n at any step and removing probability α (1 -α ) n -1 of executing the queried expert's action. At iteration n, π n is a mixture of n policies and the probability of using the queried expert's action is (1 -α ) n.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic Mixing Iterative Learning", "weight": 1.0} -->

We can stop the algorithm at any iteration N by returning the re-normalized policy ˜ π N = π N -(1 -α ) N π 0 1 -(1 -α ) N which doesn't query the expert anymore. Ross and Bagnell showed that choosing α in O ( 1 T 2 ) and N in O ( T 2 log T ) guarantees near-linear regret in T and ϵ for some class of problems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

We now present DAGGER (Dataset Aggregation), an iterative algorithm that trains a deterministic policy that achieves good performance guarantees under its induced distribution of states.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

In its simplest form, the algorithm proceeds as follows. At the first iteration, it uses the expert's policy to gather a dataset of trajectories D and train a policy ˆ π 2 that best mimics the expert on those trajectories. Then at iteration n, it uses ˆ π n to collect more trajectories and adds those trajectories to the dataset D. The next policy ˆ π n +1 is the policy that best mimics the expert on the whole dataset D.

<!-- chunk {"id": "body-0021", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

2 This is the case for instance in Markov Desision Processes (MDPs) when the Markov Chain defined by the system dynamics and policy π ∗ is rapidly mixing. In particular, if it is α -mixing with exponential decay rate δ then u is O ( 1 1 -exp( -δ ) ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Initialize D ← ∅. Initialize ˆ π 1 to any policy in Π. for i = 1 to N do Let π i = β i π ∗ +(1 -β i )ˆ π i. Sample T -step trajectories using π i. Get dataset D i = { ( s, π ∗ ( s )) } of visited states by π i and actions given by expert. Aggregate datasets: D ← D ⋃ D i. Train classifier ˆ π i +1 on D. end for Return best ˆ π i on validation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

In other words, DAGGER proceeds by collecting a dataset at each iteration under the current policy and trains the next policy under the aggregate of all collected datasets. The intuition behind this algorithm is that over the iterations, we are building up the set of inputs that the learned policy is likely to encounter during its execution based on previous experience (training iterations). This algorithm can be interpreted as a Follow-The-Leader algorithm in that at iteration n we pick the best policy ˆ π n +1 in hindsight, i.e. under all trajectories seen so far over the iterations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

To better leverage the presence of the expert in our imitation learning setting, we optionally allow the algorithm to use a modified policy π i = β i π ∗ +(1 -β i )ˆ π i at iteration i that queries the expert to choose controls a fraction of the time while collecting the next dataset. This is often desirable in practice as the first few policies, with relatively few datapoints, may make many more mistakes and visit states that are irrelevant as the policy improves.

<!-- chunk {"id": "body-0025", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Wewill typically use β 1 = 1 so that we do not have to specify an initial policy ˆ π 1 before getting data from the expert's behavior. Then we could choose β i = p i -1 to have a probability of using the expert that decays exponentially as in SMILe and SEARN. We show below the only requirement is that { β i } be a sequence such that β N = 1 N ∑ N i =1 β i → 0 as N → ∞. The simple, parameter-free version of the algorithm described above is the special case β i = I (i = 1) for I the indicator function, which often performs best in practice (see Section 5). The general DAGGER algorithm is detailed in Algorithm 3.1. The main result of our analysis in the next section is the following guarantee for DAGGER. Let π 1: N denote the sequence of policies π 1, π 2,..., π N. Assume ℓ is strongly convex and bounded over Π.

<!-- chunk {"id": "body-0026", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Suppose β i ≤ (1 -α) i -1 for all i for some constant α independent of T. Let ϵ N = min π ∈ Π 1 N ∑ N i =1 E s ∼ d π i [ℓ (s, π)] be the true loss of the best policy in hindsight. Then the following holds in the infinite sample case (infinite number of sample trajectories at each iteration): Theorem 3.1. For DAGGER, if N is ˜ O (T) there exists a policy ˆ π ∈ ˆ π 1: N s.t. E s ∼ d ˆ π [ℓ (s, ˆ π)] ≤ ϵ N + O (1 /T) In particular, this holds for the policy ˆ π = arg min π ∈ ˆ π 1: N E s ∼ d π [ℓ (s, π)].

<!-- chunk {"id": "body-0027", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

3 If the task cost function C corresponds to (or is upper bounded by) the surrogate loss ℓ then this bound tells us directly that J (ˆ π) ≤ Tϵ N + O. For arbitrary task cost function C, then if ℓ is an upper bound on the 0-1 loss with respect to π ∗, combining this result with Theorem 2.2 yields that: Theorem 3.2. For DAGGER, if N is ˜ O (uT) there exists a policy ˆ π ∈ ˆ π 1: N s.t. J (ˆ π) ≤ J (π ∗) + uTϵ N + O.

<!-- chunk {"id": "body-0028", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Finite Sample Results In the finite sample case, suppose we sample m trajectories with π i at each iteration i, and denote this dataset D i. Let ˆ ϵ N = min π ∈ Π 1 N ∑ N i =1 E s ∼ D i [ℓ (s, π)] be the training loss of the best policy on the sampled trajectories, then using AzumaHoeffding's inequality leads to the following guarantee: Theorem 3.3. For DAGGER, if N is O (T 2 log(1 /δ)) and m is O then with probability at least 1 -δ there exists a policy ˆ π ∈ ˆ π 1: N s.t. E s ∼ d ˆ π [ℓ (s, ˆ π)] ≤ ˆ ϵ N + O (1 /T) Amore refined analysis taking advantage of the strong convexity of the loss function may lead to tighter generalization bounds that require N only of order ˜ O (T log(1 /δ)).

<!-- chunk {"id": "body-0029", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Similarly: Theorem 3.4. For DAGGER, if N is O (u 2 T 2 log(1 /δ)) and m is O then with probability at least 1 -δ there exists a policy ˆ π ∈ ˆ π 1: N s.t. J (ˆ π) ≤ J (π ∗)+ uT ˆ ϵ N + O.

<!-- chunk {"id": "body-0030", "role": "body", "section": "THEORETICAL ANALYSIS", "weight": 1.0} -->

The theoretical analysis of DAGGER only relies on the noregret property of the underlying Follow-The-Leader algorithm on strongly convex losses which picks the sequence of policies ˆ π 1: N. Hence the presented results also hold for any other no regret online learning algorithm we would apply to our imitation learning setting. In particular, we can consider the results here a reduction of imitation learning to no-regret online learning where we treat mini-batches of trajectories under a single policy as a single online-learning example. We first briefly review concepts of online learning and no regret that will be used for this analysis.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Online Learning", "weight": 1.0} -->

In online learning, an algorithm must provide a policy π n at iteration n which incurs a loss ℓ n (π n). After observing this loss, the algorithm can provide a different policy π n +1 for the next iteration which will incur loss ℓ n +1 (π n +1). The loss functions ℓ n +1 may vary in an unknown or even adversarial fashion over time. A no-regret algorithm is an algorithm that produces a sequence of policies π 1, π 2,..., π N such that the average regret with respect to the best policy in hindsight goes to 0 as N goes to ∞: 3 It is not necessary to find the best policy in the sequence that minimizes the loss under its distribution; the same guarantee holds for the policy which uniformly randomly picks one policy in the sequence ˆ π 1: N and executes that policy for T steps. for lim N →∞ γ N = 0. Many no-regret algorithms guarantee that γ N is ˜ O (1 N) (e.g. when ℓ is strongly convex).

<!-- chunk {"id": "body-0032", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Now we show that no-regret algorithms can be used to find a policy which has good performance guarantees under its own distribution of states in our imitation learning setting. To do so, we must choose the loss functions to be the loss under the distribution of states of the current policy chosen by the online algorithm: ℓ i ( π ) = E s ∼ d π i [ ℓ ( s, π )].

<!-- chunk {"id": "body-0033", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

For our analysis of DAGGER, we need to bound the total variation distance between the distribution of states encountered by ˆ π i and π i, which continues to call the expert. The following lemma is useful: Proof. Let d the distribution of states over T steps conditioned on π i picking π ∗ at least once over T steps. Since π i always executes ˆ π i over T steps with probability (1 -β i) T we have d π i = (1 -β i) T d ˆ π i +(1 -(1 -β i) T) d. Thus The last inequality follows from the fact that (1 -β) T ≥ 1 -βT for any β ∈.

<!-- chunk {"id": "body-0034", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

This is only better than the trivial bound || d π i -d ˆ π i || 1 ≤ 2 for β i ≤ 1 T. Assume β i is non-increasing and define n β the largest n ≤ N such that β n > 1 T. Let ϵ N = min π ∈ Π 1 N ∑ N i =1 E s ∼ d π i [ℓ (s, π)] the loss of the best policy in hindsight after N iterations and let ℓ max be an upper bound on the loss, i.e. ℓ i (s, ˆ π i) ≤ ℓ max for all policies ˆ π i, and state s such that d ˆ π i (s) > 0. We have the following: Theorem 4.1. For DAGGER, there exists a policy ˆ π ∈ ˆ π 1: N s.t. E s ∼ d ˆ π [ℓ (s, ˆ π)] ≤ ϵ N + γ N + 2 ℓ max N [n β + T ∑ N i = n β +1 β i], for γ N the average regret of ˆ π 1: N.

<!-- chunk {"id": "body-0035", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Proof. The last lemma implies E s ∼ d ˆ π i (ℓ i (s, ˆ π i)) ≤ E s ∼ d π i (ℓ i (s, ˆ π i)) + 2 ℓ max min(1, T β i). Then: Under an error reduction assumption that for any input distribution, there is some policy π ∈ Π that achieves surrogate loss of ϵ, this implies we are guaranteed to find a policy ˆ π which achieves ϵ surrogate loss under its own state distribution in the limit, provided β N → 0. For instance, if we choose β i to be of the form (1 -α) i -1, then 1 N [n β + T ∑ N i = n β +1 β i] ≤ 1 Nα [log T + 1] and this extra penalty becomes negligible for N as ˜ O (T). As we need at least ˜ O (T) iterations to make γ N negligible, the number of iterations required by DAGGER is similar to that required by any no-regret algorithm.

<!-- chunk {"id": "body-0036", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Note that this is not as strong as the general error or regret reductions considered in which require only classification: we require a no-regret method or strongly convex surrogate loss function, a stronger (albeit common) assumption.

<!-- chunk {"id": "body-0037", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Finite Sample Case: The previous results hold if the online learning algorithm observes the infinite sample loss, i.e. the loss on the true distribution of trajectories induced by the current policy π i. In practice however the algorithm would only observe its loss on a small sample of trajectories at each iteration. We wish to bound the true loss under its own distribution of the best policy in the sequence as a function of the regret on the finite sample of trajectories.

<!-- chunk {"id": "body-0038", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

At each iteration i, we assume the algorithm samples m trajectories using π i and then observes the loss ℓ i (π) = E s ∼ D i (ℓ (s, π)), for D i the dataset of those m trajectories. The online learner guarantees 1 N ∑ N i =1 E s ∼ D i (ℓ (s, π i)) -min π ∈ Π 1 N ∑ N i =1 E s ∼ D i (ℓ (s, π)) ≤ γ N. Let ˆ ϵ N = min π ∈ Π 1 N ∑ N i =1 E s ∼ D i [ℓ (s, π)] the training loss of the best policy in hindsight. Following a similar analysis to Cesa-Bianchi et al., we obtain: Theorem 4.2. For DAGGER, with probability at least 1 -δ, there exists a policy ˆ π ∈ ˆ π 1: N s.t.

<!-- chunk {"id": "body-0039", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Proof. Let Y ij be the difference between the expected per step loss of ˆ π i under state distribution d π i and the average per step loss of ˆ π i under the j th sample trajectory with π i at iteration i. The random variables Y ij over all i ∈ { 1, 2,..., N } and j ∈ { 1, 2,..., m } are all zero mean, bounded in [-ℓ max, ℓ max] and form a martingale (considering the order Y 11, Y 12,..., Y 1 m, Y 21,..., Y Nm). By Azuma-Hoeffding's inequality 1 mN ∑ N i =1 ∑ m j =1 Y ij ≤ ℓ max √ 2 log(1 /δ) mN with probability at least 1 -δ. Hence, we obtain that with probability at least 1 -δ: The use of Azuma-Hoeffding's inequality suggests we need Nm in O (T 2 log(1 /δ)) for the generalization error to be O (1 /T) and negligible over T steps.

<!-- chunk {"id": "body-0040", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Leveraging the strong convexity of ℓ as in may lead to a tighter bound requiring only O (T log(T/δ)) trajectories.

<!-- chunk {"id": "body-0041", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To demonstrate the efficacy and scalability of DAGGER, we apply it to two challenging imitation learning problems and a sequence labeling task (handwriting recognition).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

Super Tux Kart is a 3D racing game similar to the popular Mario Kart. Our goal is to train the computer to steer the kart moving at fixed speed on a particular race track, based on the current game image features as input (see Figure 1). A human expert is used to provide demonstrations of the correct steering (analog joystick value in) for each of the observed game images. For all methods, we use a linear Figure 1: Image from Super Tux Kart's Star Track. controller as the base learner which updates the steering at 5Hz based on the vector of image features 4.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

4 Features x: LAB color values of each pixel in a 25x19 resized image of the 800x600 image; output steering: ˆ y = w T x + b where w, b minimizes ridge regression objective: L ( w,b ) = 1 n ∑ n i =1 ( w T x i + b -y i ) 2 + λ 2 w T w, for regularizer λ = 10 -3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

We compare performance on a race track called Star Track. As this track floats in space, the kart can fall off the track at any point (the kart is repositioned at the center of the track when this occurs). We measure performance in terms of the average number of falls per lap. For SMILe and DAGGER, we used 1 lap of training per iteration (∼ 1000 data points) and run both methods for 20 iterations. For SMILe we choose parameter α = 0. 1 as in Ross and Bagnell, and for DAGGER the parameter β i = I (i = 1) for I the indicator function. Figure 2 shows 95% confidence intervals on the average falls per lap of each method after 1, 5, 10, 15 and 20 iterations as a function of the total number of training data collected. We first observe that with the baseline Figure 2: Average falls/lap as a function of training data. supervised approach where training always occurs under the expert's trajectories that performance does not improve as more data is collected. This is because most of the training laps are all very similar and do not help the learner to learn how to recover from mistakes it makes.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

With SMILe we obtain some improvements but the policy after 20 iterations still falls off the track about twice per lap on average. This is in part due to the stochasticity of the policy which sometimes makes bad choices of actions. For DAGGER, we were able to obtain a policy that never falls off the track after 15 iterations of training. Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised approach. Furthermore, the policy obtained by DAGGER is smoother and looks qualitatively better than the policy obtained with SMILe. A video available on YouTube shows a qualitative comparison of the behavior obtained with each method.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

Super Mario Bros. is a platform video game where the character, Mario, must move across each stage by avoid- ing being hit by enemies and falling into gaps, and before running out of time. We used the simulator from a recent Mario Bros. AI competition which can randomly generate stages of varying difficulty (more difficult gaps and types of enemies). Our goal is to train the computer to play this game based on the current game image features as input (see Figure 3). Our expert in this scenario is a near-optimal planning algorithm that has full access to the game's internal state and can simulate exactly the consequence of future actions. An action consists of 4 binary variables indicating which subset of buttons we should press in { left,right,jump,speed }. For all methods, we use 4 independent linear SVM as the base learner which update the 4 binary actions at 5Hz based on the vector of image features 5.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

We compare performance in terms of the average distance travelled by Mario per stage before dying, running out of time or completing the stage, on randomly generated stages of difficulty 1 with a time limit of 60 seconds to complete the stage. The total distance of each stage varies but is around 4200-4300 on average, so performance can vary roughly. Stages of difficulty 1 are fairly easy for an average human player but contain most types of enemies and gaps, except with fewer enemies and gaps than stages of harder difficulties. We compare performance of DAgger, SMILe and SEARN 6 to the supervised approach (Sup). With each approach we collect 5000 data points per iteration (each stage is about 150 data points if run to completion) and run the methods for 20 iterations. For SMILe we choose parameter α = 0. 1 (Sm0.1) as in Ross and Bag- nell. For DAGGER we obtain results with different choice of the parameter β i: 1) β i = I ( i = 1) for I the indicator function (D0); 2) β i = p i -1 for all values of p ∈ { 0. 1, 0. 2,..., 0. 9 }.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

We report the best results obtained with p = 0. 5 (D0.5). We also report the results with p = 0. 9 (D0.9) which shows the slower convergence of using the expert more frequently at later iterations. Similarly for SEARN, we obtain results with all choice of α in { 0. 1, 0. 2,..., 1 }. We report the best results obtained with α = 0. 4 (Se0.4). We also report results with α = 1. 0 (Se1), which shows the unstability of such a pure policy iteration approach. Figure 4 shows 95% confidence intervals on the average distance travelled per stage at each iteration as a function of the total number of training data collected. Again here we observe that with the supervised approach, performance stagnates as we collect more data from the expert demonstrations, as this does not help the particular errors the learned controller makes. In particular, a reason the supervised approach gets such a low score is that under the learned controller, Mario is often stuck at some location against an obstacle instead of jumping over it.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

Since the expert always jumps over obstacles at a significant distance away, the controller did not learn how to get unstuck in situations where it is right next to an obstacle. On the other hand, all the other iterative methods perform much better as they eventually learn to get unstuck in those situations by encountering them at the later iterations. Again in this experiment, DAGGER outperforms SMILe, and also outperforms SEARN for all choice of α we considered. When using β i = 0. 9 i -1, convergence is significantly slower could have benefited from more iterations as performance was still improving at the end of the 20 iterations. Choosing 0. 5 i -1 yields slightly better performance then with the indicator function. This is potentially due to the large number of data generated where mario is stuck at the same location in the early iterations when using the indicator; whereas using the ex- pert a small fraction of the time still allows to observe those locations but also unstucks mario and makes it collect a wider variety of useful data. A video available on YouTube also shows a qualitative comparison of the behavior obtained with each method.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

5 For the input features x: each image is discretized in a grid of 22x22 cells centered around Mario; 14 binary features describe each cell (types of ground, enemies, blocks and other special items); a history of those features over the last 4 images is used, in addition to other features describing the last 6 actions and the state of Mario (small,big,fire,touches ground), for a total of 27152 binary features (very sparse). The k th output binary variable ˆ y k = I ( w T k x + b k > 0), where w k, b k optimizes the SVMobjective with regularizer λ = 10 -4 using stochastic gradient descent.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

6 Weuse the same cost-to-go approximation in Daumé III et al.; in this case SMILe and SEARN differs only in how the weights in the mixture are updated at each iteration.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

Finally, we demonstrate the efficacy of our approach on a structured prediction problem involving recognizing handwritten words given the sequence of images of each character in the word. We follow Daumé III et al. in adopting a view of structured prediction as a degenerate form of imitation learning where the system dynamics are deterministic and trivial in simply passing on earlier predictions made as inputs for future predictions. We use the dataset of Taskar et al. which has been used extensively in the literature to compare several structured prediction approaches. This dataset contains roughly 6600 words (for a total of over 52000 characters) partitioned in 10 folds. We consider the large dataset experiment which consists of training on 9 folds and testing on 1 fold and repeating this over all folds. Performance is measured in terms of the character accuracy on the test folds.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

Weconsider predicting the word by predicting each character in sequence in a left to right order, using the previously predicted character to help predict the next and a linear SVM 7, following the greedy SEARN approach in Daumé III et al.. Here we compare our method to SMILe, as well as SEARN (using the same approximations used in Daumé III et al. ). We also compare these approaches to two baseline, a non-structured approach which simply predicts each character independently and the supervised training approach where training is conducted with the previous character always correctly labeled. Again we try all choice of α ∈ { 0. 1, 0. 2,..., 1 } for SEARN, and report results for α = 0. 1, α = 1 (pure policy iteration) and the best α = 0. 8, and run all approaches for 20 iterations. Figure 5 shows the performance of each approach on the test folds after each iteration as a function of training data. The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

When adding the previous character feature, but training with always the previous character correctly labeled (supervised approach), performance increases up to 83.6%. Using DAgger increases performance further to 85.5%. Surprisingly, we observe SEARN with α = 1, which is a pure policy iteration approach performs very well on this experiment, similarly to the best α = 0. 8 and DAgger. Because there is only a small part of the input that is influenced by the current policy (the previous predicted character feature) this makes this approach not as unstable as in general reinforcement/imitation learning problems (as we saw in the previous experiment). SEARN and SMILe with small α = 0. 1 performs similarly but significantly worse than DAgger. Note that we chose the simplest (greedy, one-pass) decoding to illustrate the benefits of the DAGGER approach with respect to existing reductions. Similar techniques can be applied to multi-pass or beam-search decoding leading to results that are competitive with the state-of-the-art.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

7 Each character is 8x16 binary pixels (128 input features); 26 binary features are used to encode the previously predicted letter in the word. We train the multiclass SVM using the all-pairs reduction to binary classification.

<!-- chunk {"id": "body-0056", "role": "body", "section": "FUTURE WORK", "weight": 1.5} -->

We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAGGER approach can provide a learning reduction with strong performance guarantees in both imitation learning and structured prediction. In future work, we will consider more sophisticated strategies than simple greedy forward decoding for structured prediction, as well as using base classifiers that rely on Inverse Optimal Control techniques to learn a cost function for a planner to aid prediction in imitation learning. Further we believe techniques similar to those presented, by leveraging a cost-to-go estimate, may provide an understanding of the success of online methods for reinforcement learning and suggest a similar data-aggregation method that can guarantee performance in such settings.
