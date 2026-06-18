<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning

Topics include Imitation learning, Robotics, Autonomous driving, Neural networks, Supervised learning, Online algorithms, Offline algorithms, Sample complexity, Control, Learning, Horizon, Behavior cloning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Imitation learning (IL) aims to mimic the behavior of an expert in a sequential decision making task by learning from demonstrations, and has been widely applied to robotics, autonomous driving, and autoregressive text generation. The simplest approach to IL, behavior cloning (BC), is thought to incur sample complexity with unfavorable quadratic dependence on the problem horizon, motivating a variety of different online algorithms that attain improved linear horizon dependence under stronger assumptions on the data and the learner's access to the expert. We revisit the apparent gap between offline and online IL from a learning-theoretic perspective, with a focus on the realizable/well-specified setting with general policy classes up to and including deep neural networks. Through a new analysis of behavior cloning with the logarithmic loss, we show that it is possible to achieve horizon-independent sample complexity in offline IL whenever (i) the range of the cumulative payoffs is controlled, and (ii) an appropriate notion of supervised learning complexity for the policy class is controlled.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Specializing our results to deterministic, stationary policies, we show that the gap between offline and online IL is smaller than previously thought: (i) it is possible to achieve linear dependence on horizon in offline IL under dense rewards (matching what was previously only known to be achievable in online IL); and (ii) without further assumptions on the policy class, online IL cannot improve over offline IL with the logarithmic loss, even in benign MDPs. We complement our theoretical results with experiments on standard RL tasks and autoregressive language generation to validate the practical relevance of our findings.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning (IL) is the problem of emulating an expert policy for sequential decision making by learning from demonstrations. Compared to reinforcement learning (RL), the learner in IL does not observe reward-based feedback, and must imitate the expert's behavior based on demonstrations alone; their objective is to achieve performance close to that of the expert on an *unobserved* reward function.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning is motivated by the observation that in many domains, demonstrating the desired behavior for a task (e.g., robotic grasping) is simple, while designing a reward function to elicit the desired behavior can be challenging. IL is also often preferable to RL because it removes the need for exploration, leading to empirically reduced sample complexity and often much more stable training. Indeed, the relative ease of applying IL (over RL methods) has led to extensive adoption, ranging from classical applications in autonomous driving and helicopter flight to contemporary works that leverage deep learning to achieve state-of-the-art performance for self-driving vehicles, visuomotor control, navigation, and game AI. Imitation learning also offers a conceptual framework through which to study autoregressive language modeling, and a number of useful empirical insights have arisen as a result of this perspective. However, a central challenge limiting broader real-world deployment is to understand and improve the reliability and stability properties of algorithms that support general-purpose (deep/neural) function approximation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In more detail, imitation learning algorithms can be loosely grouped into *offline* and *online* approaches. Offline imitation learning algorithms only require access to a dataset of logged trajectories from the expert, making them broadly applicable. The most widely used approach, *behavior cloning*, reduces imitation learning to a standard supervised learning problem in which the learner attempts to predict the expert's actions from observations given the collected trajectories. The simplicity of this approach allows the learner to leverage the considerable machinery developed for supervised learning and readily incorporate complex function approximation with deep models. On the other hand, BC seemingly ignores the problem of *distribution shift*, wherein small deviations from the expert policy early in rollout lead the learner off-distribution to regions where they are less able to accurately imitate. This apparent *error amplification* phenomenon has been widely observed empirically, and motivates *online* or *interactive* approaches to imitation learning, which avoid error amplification by interactively querying the expert and learning to correct mistakes on-policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In theory, online imitation learning enables sample complexity guarantees with improved (linear, as opposed to quadratic) dependence on horizon for favorable MDPs. Yet, while online imitation learning has found some empirical success, online access to the expert can be costly or infeasible in many applications, and offline imitation learning remains the dominant empirical paradigm. Motivated by this disconnect between theory and practice, we we aim to understand whether the apparent gap between offline and online imitation learning is fundamental.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Is online imitation learning truly more sample-efficient than offline imitation learning, or can existing algorithms or analyses be improved?*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

A (randomized) policy is a sequence of per-timestep functions $\pi = \left\{ \pi_{h}:{\mathcal{X}\rightarrow{\Delta{(\mathcal{A})}}} \right\}_{h = 1}^{H}$. The policy induces a distribution over trajectories ${(x_{1},a_{1},r_{1})},\ldots,{(x_{H},a_{H},r_{H})}$ via the following process. The initial state is drawn via $x_{1} \sim {P_{0}{(\varnothing)}}$,^11^1We use the convention that $P_{0}{(\varnothing)}$ denotes the initial state distribution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

We let ${\mathbb{E}}^{\pi}\lbrack \cdot \rbrack$ and ${\mathbb{P}}^{\pi}{\lbrack \cdot \rbrack}$ denote expectation and probability law for ${(x_{1},a_{1})},\ldots,{(x_{H},a_{H})}$ under this process, respectively.^22^2To simplify presentation, we assume that $\mathcal{X}$ and $\mathcal{A}$ are countable, but our results trivially extend to general spaces with an appropriate measure-theoretic treatment.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reward normalization", "weight": 1.0} -->

To study the role of horizon in imitation learning in a way that disentangles the effects of reward scaling from other factors, we assume that rewards are normalized such that ${\sum_{h = 1}^{H}r_{h}} \in \lbrack 0,R\rbrack$ for a parameter $R > 0$. We refer to the setting in which $r_{h} \in {\lbrack 0,1\rbrack}$ for all $h \in {\lbrack H\rbrack}$, which is the focus of most prior work, as the *dense reward setting*, which has $R \leq H$; we will frequently specialize our results to this setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

*Behavior cloning*, which reduces the imitation learning problem to supervised prediction, is the dominant offline imitation learning paradigm. To describe the algorithm in its simplest form, consider the case where $\pi^{\star}:=\left\{ \pi_{h}^{\star}:{\mathcal{X}\rightarrow\mathcal{A}} \right\}_{h = 1}^{H}$ is deterministic. For a user-specified policy class $\Pi \subset \left\{ \pi_{h}:{\mathcal{X}\rightarrow{\Delta{(\mathcal{A})}}} \right\}_{h = 1}^{H}$, the most basic version of behavior cloning solves the supervised classification problem

<!-- chunk {"id": "body-0013", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

Naturally, other classification losses (e.g., square loss, logistic loss, or log loss) may be used in place of the indicator loss.^33^3Behavior cloning for stochastic expert policies has received limited attention in theory, but the logarithmic loss is widely used in practice. One contribution of our work is to fill this lacuna. To provide sample complexity bounds for this algorithm, we make a standard *realizability assumption* (e.g., Agarwal et al.; Foster and Rakhlin ). {assumption}\[Realizability\] The policy class $\Pi$ contains the expert policy, i.e. $\pi^{\star} \in \Pi$. This assumption asserts that $\Pi$ is expressive enough to represent the expert policy;^44^4We restrict our attention to the realizable setting to simplify presentation as much as possible, but extension to misspecified policy classes is straightforward, and we remark on the misspecified case at various points.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

depending on the application, $\Pi$ might be parameterized by simple linear models, or by flexible models such as convolutional neural networks or transformers. To simplify presentation, we adopt a standard convention in RL theory and focus on finite classes with ${|\Pi|} < \infty$. A standard uniform convergence argument implies that if we define ${L_{\text{bc}}{(\pi)}} = {\frac{1}{H}{\sum_{h = 1}^{H}{{\mathbb{P}}^{\pi^{\star}}\left\lbrack {{\pi{(x_{h})}} \neq {\pi^{\star}{(x_{h})}}} \right\rbrack}}}$, then with probability at least $1 - \delta$, behavior cloning has

<!-- chunk {"id": "body-0015", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

Combining these bounds, we conclude that

<!-- chunk {"id": "body-0016", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

For the *dense reward setting* where $R = H$, this leads to *quadratic* dependence on horizon; that is, $\Omega{(H^{2})}$ trajectories are required to achieve constant accuracy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

The generalization bound ${L_{\text{bc}}{(\hat{\pi})}} \lesssim \frac{\log{({{|\Pi|}\delta^{- 1}})}}{n}$ is tight even when ${|\Pi|} = 2$ (this is true not just for the indicator loss, but for other standard losses such as square loss, absolute loss, and hinge loss). Since the amount of information in a trajectory grows with $H$, one might hope a-priori that the generalization error would decrease with $H$; alas, this does not occur due to the *dependence* between samples in each trajectory.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

Ross and Bagnell show that the inequality ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \lesssim {{{RH} \cdot L_{\text{bc}}}{(\hat{\pi})}}$ is tight for MDPs with $3$ states; the quadratic scaling in $H$ this induces under dense rewards is often attributed to *error amplification* or *distribution shift* incurred by passing from error under the state distribution of $\pi^{\star}$ to the state distribution of $\hat{\pi}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Behavior cloning", "weight": 1.0} -->

Combining, these observations, Ross and Bagnell conclude that offline imitation learning is fundamentally harder than supervised classification, where linear dependence on horizon might be expected (e.g., if we considered $H$ independent prediction tasks).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

The aforementioned limitations of behavior cloning have motivated *online* approaches to IL. In the online framework, learning proceeds in $n$ episodes in which the learner can directly interact with the underlying MDP $M^{\star}$ and query the expert advice.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

1}^{\star,i})},{(x_{h}^{i},a_{h}^{\star,i})}$ at training time; we adopt the present formulation to keep notation compact.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

After all $n$ episodes conclude, the learner produces a final policy $\hat{\pi}$ whose regret to $\pi^{\star}$ should be small. Online imitation learning can avoid error amplification and achieve improved dependence on horizon for MDPs that satisfy a *recoverability* condition. {definition}\[Recoverability parameter\] The *recoverability parameter* for an MDP $M^{\star}$ and expert $\pi^{\star}$ is given by ^66^6For stochastic policies, we overload notation and write $f{({\pi{(x)}})}$ as shorthand for ${\mathbb{E}}_{a \sim {\pi{(x)}}}\left\lbrack {f{(a)}} \right\rbrack$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

Under recoverability, the Dagger algorithm of Ross et al. leverages online interaction by interactively querying the expert and learning to correct mistakes on-policy, leading to sample complexity

<!-- chunk {"id": "body-0024", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

for any finite class $\Pi$ and deterministic expert policy $\pi^{\star}$, when configured appropriately (for completeness, we include an analysis in Section C.2; see Sections C.2 and C.2).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

For the dense reward setting where $R = H$, we can have $\mu = H$ in the worst case, in which case Eq. 5 matches the quadratic horizon dependence of behavior cloning, but when $\mu = {O{}}$ (informally, this means it is possible to "recover" from a bad action that deviates from $\pi^{\star}$), the bound in Eq. 5 achieves linear dependence on horizon. Other online IL algorithms such as Forward, Smile, and Aggrevate achieve similar guarantees (we are not aware of another approach that improves upon Eq. 5 for general finite classes).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Online Imitation Learning and Recoverability", "weight": 1.0} -->

The improvements of online IL notwithstanding, Eq. 4 is known to be tight for BC, but this is an *algorithm-dependent* (as opposed to information-theoretic) lower bound, and does not preclude the existence of more sample-efficient, purely offline algorithms. In this context, our central question can be restated as: *Can offline imitation learning algorithms achieve sub-quadratic horizon dependence for general policy classes $\Pi$?* While prior work has investigated this question for tabular and linear policies, we approach the problem from a new (learning-theoretic) perspective by considering general policy classes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Contributions", "weight": 1.0} -->

We present several new results that clarify the role of horizon in offline and online imitation learning.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Contributions", "weight": 1.0} -->

Horizon-independent analysis of log-loss behavior cloning. Through a new analysis of behavior cloning with the *logarithmic loss* (LogLossBC), we show that it is possible to achieve *horizon-independent* sample complexity in offline imitation learning whenever (i) the range of the cumulative payoffs is normalized, and (ii) an appropriate notion of supervised learning complexity for the policy class is controlled. Our result is facilitated by a novel information-theoretic analysis which controls policy behavior at the trajectory level, supporting both deterministic and stochastic expert policies.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Contributions", "weight": 1.0} -->

Deterministic policies: Closing the gap between offline and online IL. Specializing LogLossBC to *deterministic stationary* policies (more generally, policies with parameter sharing) and cumulative rewards in the range $\lbrack 0,H\rbrack$, we show that it is possible to achieve sample complexity with *linear* dependence on horizon in offline IL in arbitrary MDPs, matching was was previously only known of *online* IL. We complement this result with a lower bound showing that, without further structural assumptions on the policy class (e.g., no parameter sharing ), online IL cannot improve over offline IL with LogLossBC, even for benign MDPs. Our results are summarized in Table 1. Nonetheless, as observed in prior work, online imitation learning can still be beneficial for *non-stationary* policies.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Contributions", "weight": 1.0} -->

Stochastic policies: Tight understanding of optimal sample complexity. For stochastic expert policies, our analysis of LogLossBC gives the first *variance-dependent* sample complexity bounds for imitation learning with general policy classes, which we prove to be tight in a problem-dependent and minimax sense. Using this result, we show that for stochastic stationary experts, (i) *quadratic dependence on the horizon is necessary* when cumulative rewards lie in the range $\lbrack 0,H\rbrack$, in contrast to the deterministic setting, but (ii) LogLossBC---through our variance-dependent analysis---can sidestep this hardness and achieve linear dependence on horizon under a recoverability-like condition. Finally, we show that, as in the deterministic case, online IL cannot improve over offline IL with LogLossBC without further assumptions on the policy class. Our results are summarized in Footnote 13.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Toward a learning-theoretic understanding of imitation learning", "weight": 1.0} -->

Our findings call into question the conventional wisdom around the benefits of online imitation learning, and highlight the need to develop a fine-grained, problem-dependent understanding of algorithms and complexity for IL. Indeed, instabilities of offline IL and benefits of online IL may indeed arise in practice, but existing assumptions in theoretical research are often too coarse to give insights into the true nature of these phenomena, leading to an important gap between theory and practice. As a first step in this research program, we highlight several under-explored mechanisms through which online IL can lead to improved sample complexity, including representational benefits and exploration (Section 4). We also complement our theoretical results with empirical demonstrations of the phenomena we describe (Section 5).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Section 5, we complement our theoretical results with an empirical demonstration of the horizon-independence of LogLossBC predicted by our theory (under parameter sharing and sparse rewards). We consider tasks where the horizon $H$ can be naturally scaled up and down---for example, an agent walking for a set number of timesteps---and use an expert trained according to RL to generate expert trajectories, before training a policy using LogLossBC. We consider both continuous action space (MuJoCo environment Walker2d) and discrete action space (Atari environment Beamrider) tasks to demonstrate the broad applicability of our theoretical results. As can be seen in Figure 1, the performance of the learned policy is independent or improving with horizon, consistent with our theoretical results. We also perform simplified experiments on autoregressive language generation with transformers. Here, we find that the performance of the imitator is largely independent of $H$, as predicted by our results, though the results are more nuanced.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

Section 2 presents the first of our main results, a horizon-independent sample complexity analysis for LogLossBC for deterministic experts, and discusses implications regarding the gap between offline and online IL as it concerns horizon. Section 3 presents analogous results and implications for stochastic experts. Section 4 discusses mechanisms through which online IL can have benefits over offline IL, beyond horizon dependence, highlighting directions for future research. Section 5 presents an empirical validation, and we conclude with open problems and further directions for future research in Section 6.3. Proofs and additional results are deferred to the appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Horizon-Independent Analysis of Log-Loss Behavior Cloning", "weight": 1.0} -->

This section presents the first of our main results, a horizon-independent sample complexity analysis of log-loss behavior cloning for the case of deterministic experts. Our second main result, handles the case of stochastic experts, builds on our results here, and is presented in Section 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Log-Loss Behavior Cloning and Supervised Learning Guarantees", "weight": 1.0} -->

The workhorse for all of our results (both for deterministic and stochastic experts), is the following simple modification to behavior cloning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Log-Loss Behavior Cloning and Supervised Learning Guarantees", "weight": 1.0} -->

This scheme is ubiquitous in practice, and forms the basis for autoregressive language modeling; we refer to it as LogLossBC. We will show that this seemingly small change---moving from indicator loss to log loss---has significant benefits.^77^7Beginning from Foster and Krishnamurthy, a recent line of work shows that the logarithmic loss can be beneficial for deriving problem-dependent bounds for various reinforcement learning settings. We build upon the information-theoretic machinery of Foster and Krishnamurthy; Foster et al., but use it show that for imitation learning, the log-loss is beneficial even in a minimax sense.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Log-Loss Behavior Cloning and Supervised Learning Guarantees", "weight": 1.0} -->

Following the classical tradition of imitation learning, our analysis proceeds via *reduction* to supervised learning. We first show that LogLossBC satisfies an appropriate supervised learning guarantee, then translate this into rollout performance. Our starting point is to observe that LogLossBC, via Eq. 6, can be interpreted as performing maximum likelihood estimation over the set $\left\{ {\mathbb{P}}^{\pi} \right\}_{\pi \in \Pi}$ in order to estimate the law ${\mathbb{P}}^{\pi^{\star}}$ over trajectories under $\pi^{\star}$ (see Section C.1 for details). As a result, standard guarantees for maximum likelihood estimation imply convergence in distribution whenever $\pi^{\star} \in \Pi$. To be precise, define the squared *Hellinger distance* for probability measures $\mathbb{P}$ and $\mathbb{Q}$ with a common dominating measure $\omega$ by

<!-- chunk {"id": "body-0038", "role": "body", "section": "Log-Loss Behavior Cloning and Supervised Learning Guarantees", "weight": 1.0} -->

Then for any finite policy class $\Pi$, we have the following guarantee.^88^8While unfamiliar readers might expect a bound on KL divergence, Hellinger distance turns out to be more natural due to a connection to the MGF of the log-loss. This facilitates scale-free generalization guarantees in spite of the potential unboundedness of the log-loss.. {proposition}\Supervised learning guarantee for LogLossBC (special case of [Eq. 61)\] For any (potentially stochastic) expert $\pi^{\star} \in \Pi$, the LogLossBC algorithm in Eq. 6 ensures that with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Log-Loss Behavior Cloning and Supervised Learning Guarantees", "weight": 1.0} -->

That is, by performing LogLossBC, we are implicitly estimating the law ${\mathbb{P}}^{\pi^{\star}}$; note that this result holds even if $\pi^{\star}$ is stochastic, as long as $\pi^{\star} \in \Pi$. We will focus on finite, realizable policy classes throughout this section to simplify presentation as much as possible, but guarantees for infinite classes under misspecification are given in Section C.1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Deterministic Experts", "weight": 1.0} -->

We first consider the case where the expert $\pi^{\star}$ is deterministic. Our main result is the following theorem, which translates the supervised learning error $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\hat{\pi}},{\mathbb{P}}^{\pi^{\star}} \right)$ into a bound on rollout performance in a horizon-independent fashion. {theorem}\[Horizon-independent regret decomposition (deterministic case)\] For any deterministic policy $\pi^{\star}$ and potentially stochastic policy $\hat{\pi}$,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Deterministic Experts", "weight": 1.0} -->

This result shows that horizon-independent bounds on rollout performance are possible whenever (i) rewards are appropriately normalized, and (ii) the supervised learning error $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\hat{\pi}},{\mathbb{P}}^{\pi^{\star}} \right)$ is appropriately controlled. It is proven using novel trajectory-level control over deviations between $\hat{\pi}$ and $\pi^{\star}$; we will elaborate upon this in the sequel. We emphasize that this result would be trivial if squared Hellinger distance were replaced by total variation distance; that the bound scales with *squared* Hellinger distance is crucial for obtaining fast $1/n$-type rates and linear horizon dependence. We further remark that this reduction is not specific to LogLossBC, and can be applied to any IL algorithm for which we can bound the Hellinger distance. Combining Section 2.2 with Footnote 8, we obtain the following guarantee for finite policy classes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Deterministic Experts", "weight": 1.0} -->

{corollary}\[Regret of LogLossBC (deterministic case)\] For any deterministic expert $\pi^{\star} \in \Pi$, the LogLossBC algorithm in Eq. 6 ensures that with probability at least $1 - \delta$, it holds that

<!-- chunk {"id": "body-0043", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Deterministic Experts", "weight": 1.0} -->

To the best of our knowledge, this is the tightest available sample complexity guarantee for offline imitation learning with general policy classes. This bound improves upon the guarantee for indicator-loss behavior cloning in Eq. 4 by an $O{(H)}$ factor, and improves upon the guarantee for Dagger in Eq. 5 (replacing $H$ with $R \leq H$ under $r_{h} \in {\lbrack 0,1\rbrack}$) in the typical regime where $\mu = {\Omega{}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Interpreting the Sample Complexity of LogLossBC", "weight": 1.0} -->

To understand the behavior of the bound for LogLossBC in Section 2.2 in more detail, we consider two special cases (summarized in Table 1).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Stationary policies and parameter sharing", "weight": 1.0} -->

If ${\log{|\Pi|}} = {O{}}$, the bound in Eq. 10 is *independent of horizon* in the case of sparse rewards ($R = {O{}}$), and *linear in horizon* in the case of dense rewards ($R = {O{(H)}}$).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stationary policies and parameter sharing", "weight": 1.0} -->

*$O{(H)}$ sample complexity can be achieved in offline IL under dense rewards for general $\Pi$,*

<!-- chunk {"id": "body-0047", "role": "body", "section": "Stationary policies and parameter sharing", "weight": 1.0} -->

as long as $\log{|\Pi|}$ is appropriately controlled. This runs somewhat counter to intuition expressed in prior work, but we will show in the sequel that there is no contradiction.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Stationary policies and parameter sharing", "weight": 1.0} -->

Generally speaking, we expect to have ${\log{|\Pi|}} = {O{}}$ if $\Pi$ consists of stationary policies or more broadly, policies with parameter sharing across steps $h \in {\lbrack H\rbrack}$ (as is the case in transformers used for autoregressive text generation).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Stationary policies and parameter sharing", "weight": 1.0} -->

As an example, for a tabular (finite state/action) MDP, if $\Pi$ consists of all stationary policies, we have ${\log{|\Pi|}} = {{|\mathcal{X}|}{\log{|\mathcal{A}|}}}$, so Eq. 10 gives ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \lesssim \frac{R{|\mathcal{X}|}{\log{({{|\mathcal{A}|}\delta^{- 1}})}}}{n}$; that is, stationary policies can be learned with horizon-independent samples complexity under sparse rewards and linear dependence on horizon under dense rewards.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Optimality and Consequences for Online versus Offline Imitation Learning", "weight": 1.0} -->

We now investigate the optimality of Section 2.2 and discuss implications for online versus offline imitation learning, as well as connections to prior work. Our main result here shows that in the dense-reward regime where $r_{h} \in {\lbrack 0,1\rbrack}$ and $R = H$, Section 2.2 cannot be improved when ${\log{|\Pi|}} = {O{}}$---even with online access, recoverability, and known dynamics.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Optimality and Consequences for Online versus Offline Imitation Learning", "weight": 1.0} -->

{theorem}\[Lower bound for deterministic experts\] For any $n \in {\mathbb{N}}$ and $H \in {\mathbb{N}}$, there exists a (reward-free) MDP $M^{\star}$ with ${|\mathcal{X}|} = {|\mathcal{A}|} = 2$, a class of reward functions $\mathcal{R}$ with $|\mathcal{R}| = 2$, and a class of deterministic policies $\Pi$ with ${|\Pi|} = 2$ with the following property.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Optimality and Consequences for Online versus Offline Imitation Learning", "weight": 1.0} -->

For any (online or offline) imitation learning algorithm, there exists a deterministic reward function $r = \left\{ r_{h} \right\}_{h = 1}^{H}$ with $r_{h} \in {\lbrack 0,1\rbrack}$ (in particular, $R \leq H$) and (optimal) expert policy $\pi^{\star} \in \Pi$ with $\mu = 1$ such that the expected suboptimality is lower bounded as

<!-- chunk {"id": "body-0053", "role": "body", "section": "Optimality and Consequences for Online versus Offline Imitation Learning", "weight": 1.0} -->

for an absolute constant $c > 0$. In addition, the dynamics, rewards, and expert policies are stationary. Together, Sections 2.2 and 2.4 show that without further assumptions on $\Pi$, *online imitation learning cannot improve upon offline imitation learning*. That is, even if recoverability is satisfied, there is no online imitation learning algorithm that improves upon Section 2.2 uniformly for all policy classes. See Section G.1 for further lower bounds.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Benefits of online IL for policies with no parameter sharing", "weight": 1.0} -->

How can we reconcile our results with the claim found throughout prior work that online IL improves the horizon dependence of offline IL? The important distinction here is that online IL can still improve on a *policy-class dependent* basis. In particular, methods like Dagger can still lead to improved sample complexity for policy classes with *no parameter sharing* across steps $h \in {\lbrack H\rbrack}$. Let $\Pi_{h}:=\left\{ \pi_{h}\mid{\pi \in \Pi} \right\}$ denote the projection of $\Pi$ onto step $h$. In Section C.2, we prove the following refined guarantee for a variant of Dagger based on the log-loss (LogLossDagger). {proposition}\Special case of [Section C.2\] When $\pi^{\star} \in \Pi$ is deterministic, LogLossDagger ensures that with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0055", "role": "body", "section": "Benefits of online IL for policies with no parameter sharing", "weight": 1.0} -->

This is consistent with Rajaraman et al., who proved a $\muH$ vs. $H^{2}$ gap between online and offline IL for the special case of non-stationary tabular policies (where $\Pi$ is a product class with ${\log{|\Pi|}} \propto H$) under dense rewards. However, for classes with parameter sharing (i.e., where ${\log{|\Pi_{h}|}} \propto {\log{|\Pi|}}$), the bound in Section 2.4 scales as $\frac{\muH{\log{|\Pi|}}}{n}$, which does not improve over Section 2.2 unless $\mu \ll 1$. Since virtually all empirical work on imitation learning uses parameter sharing across steps $h \in {\lbrack H\rbrack}$, we believe the finding that online IL does not improve over offline IL in this regime is quite salient.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Benefits of online IL for policies with no parameter sharing", "weight": 1.0} -->

{remark}\[Known dynamics/inverse RL\] Complementary to our results, various works show improved horizon dependence in offline IL under the assumption that the MDP dynamics are known; see Appendix A for discussion.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

The central object in the proof of Section 2.2 is the following *trajectory-level* distance function between policies. For a pair of potentially stochastic policies $\pi$ and $\pi^{\prime}$, define

<!-- chunk {"id": "body-0058", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

We then show (Section D.1) that whenever $\pi^{\star}$ is deterministic, Hellinger distance satisfies^99^9In fact, the opposite direction of this inequality holds as well, up to an absolute constant.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

Finally, we show (Section D.1) that the trajectory-level distance is symmetric, i.e.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

This step is perhaps the most critical: by considering trajectory-level errors, we can switch from the state distribution induced by $\hat{\pi}$ to that of $\pi^{\star}$ for free, without incurring error amplification or spurious horizon factors. Combining the preceding inequalities yields Section 2.2; see Appendix D for the full proof.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

This analysis is closely related to a result in Rajaraman et al.. For the special case of deterministic, linearly parameterized policies with parameter sharing, Rajaraman et al. consider an algorithm that minimizes an empirical analogue of the trajectory-wise distance in Eq. 13, and show that it leads to a bound similar to Eq. 10 (i.e., linear-in-$H$ sample complexity under dense rewards). Relative to this work, our contributions are threefold: (i) we show that horizon-independent sample complexity can be achieved for *arbitrary* policy classes with parameter sharing, not just linear classes; (ii) we show that said guarantees can be achieved by a natural algorithm, LogLossBC, which is already widely used in practice; and (iii), by virtue of considering the log loss, our results readily generalize to encompass stochastic expert policies, as we will show in the sequel.^1010^10A fourth benefit is that our analysis supports the setting in which $\pi^{\star}$ is deterministic, yet $\Pi$ contains stochastic policies.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Proving \\\\crtcrefthm:bc_deterministic: How Does LogLossBC Avoid Error Amplification?", "weight": 1.0} -->

This is a natural setting which can arise when, for example, $\Pi$ is parameterized by softmax policies. Guarantees under misspecification, which support this setting, are given in Section C.1.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Stochastic Experts", "weight": 1.0} -->

In this section, we turn out attention to the general setting in which the expert policy $\pi^{\star}$ is stochastic. Stochastic policies are widely used in practice, where they are useful for modeling multimodal behavior, but have received relatively little exploration in theory beyond the work of Rajaraman et al. for tabular policies.^1111^11As discussed at length in Rajaraman et al., many prior works state results in a level of generality that allows for stochastic experts, but the notions of supervised learning error found in these works (e.g., TV distance) do not lead to tight rates when instantiated for stochastic experts.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Stochastic Experts", "weight": 1.0} -->

Our main result for this section, Section 3, is a regret decomposition based on the supervised learning error $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\hat{\pi}},{\mathbb{P}}^{\pi^{\star}} \right)$ that is horizon-independent and *variance-dependent*.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Stochastic Experts", "weight": 1.0} -->

Applying this result with LogLossBC leads to the following guarantee. {corollary}\[Regret of LogLossBC \] For any expert $\pi^{\star} \in \Pi$, the LogLossBC algorithm in Eq. 6 ensures that with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0066", "role": "body", "section": "Horizon-Independent Analysis of LogLossBC for Stochastic Experts", "weight": 1.0} -->

As we show in the sequel, when the expert policy is stochastic, we can no longer hope for a "fast" $1/n$-type rate, and must instead settle for a "slow" $1/\sqrt{n}$-type rate. The slow term in Eq. 19 is controlled by the variance $\sigma_{\pi^{\star}}^{2}$ for the optimal policy. In particular, if $\pi^{\star}$ is deterministic, then $\sigma_{\pi^{\star}}^{2} = 0$, and Eq. 19 recovers our bound for the deterministic setting in Section 2.2 up to a $\log{(n)}$ factor.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

To understand the dependence on horizon in Section 3, we restrict our attention to the "parameter sharing" case where ${\log{|\Pi|}} = {O{}}$, and separately discuss the sparse and dense reward settings (results summarized in Footnote 13).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

Consider the sparse reward setting where $R = {O{}}$. Here, at first glance it would appear that the variance $\sigma_{\pi^{\star}}^{2}$ should scale with the horizon. Fortunately, this is not the case: The following result---via a law-of-total-variance-type argument ---implies that Section 3 is *fully horizon-independent*, with no explicit dependence on horizon when $R = {O{}}$ and ${\log{|\Pi|}} = {O{}}$. For a function $f{(x_{1:H},a_{1:H})}$, let ${Var}^{\pi}\lbrack f\rbrack$ denote the variance of $f$ under ${{(x_{1},a_{1})},\ldots,{(x_{H},a_{H})}} \sim \pi$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

For the dense-reward regime where $R = H$, Section 3.1 gives ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \lesssim {H\sqrt{\frac{\log{({|\Pi|})}}{n}}}$. This is somewhat disappointing, as we now require $\Omega{(H^{2})}$ trajectories (quadratic sample complexity) to learn a non-trivial policy, even when ${\log{|\Pi|}} = {O{}}$. The following result shows that the dependence on the variance in Section 2.2 cannot be improved in general, which implies that the quadratic horizon dependence in this regime is tight.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

for an absolute constant $c \geq 1$. Beyond showing that a slow $1/\sqrt{n}$ rate is required for stochastic policies,^1414^14Rajaraman et al. show that for the tabular setting, it is possible to achieve a $1/n$-type rate *in-expectation* for stochastic policies. Their result critically exploits the assumption that $|\mathcal{X}|$ and $|\mathcal{A}|$ are small and finite to argue that it is possible to build an unbiased estimator for $\pi^{\star}$. Table 2 shows that such a result cannot hold with even *constant probability* for the same setting. We believe the fact that a $1/n$-type rate is possible in expectation is an artifact of the tabular setting, and unlikely to hold for general policy classes.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

when specializing to $\sigma^{2} = H^{2}$, this result shows that $\Omega{(H^{2})}$ trajectories are required to learn a non-trivial policy under a stochastic expert, even when ${\log{|\Pi|}} = {O{}}$; this reveals a fundamental difference between deterministic and stochastic experts, since $O{(H)}$ sample complexity is sufficient in the former case.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

Nonetheless, it is possible to obtain linear-in-$H$ sample complexity for dense rewards under a recoverability-like condition. Let us define the *signed recoverability constant* via

<!-- chunk {"id": "body-0073", "role": "body", "section": "Horizon-Independence and Optimality for Stochastic Experts", "weight": 1.0} -->

See Appendix G for further results concerning tightness of Section 3, including instance-dependent lower bounds.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Consequences for online versus offline IL", "weight": 1.0} -->

The lower bound in Table 2 holds even for online imitation learning algorithms. Thus, similar to the deterministic setting, there is no online IL algorithm that improves upon Section 3 uniformly for all policy classes. This means that even for stochastic experts, online imitation learning cannot improve upon offline imitation learning without further assumptions (e.g., no parameter sharing) on the policy class under consideration.

<!-- chunk {"id": "body-0075", "role": "body", "section": "To What Extent is Online Interaction Beneficial?", "weight": 1.0} -->

Our results in Sections 2 and 3 show that the benefits of online interaction in imitation learning---to the extent that horizon is concerned---are more limited than previously thought. We expect that 'in practice, online interaction may still lead to benefits, but in a problem-dependent sense. To this end, we now highlight several special cases in which online interaction *does* indeed lead to benefits over offline imitation learning, but in a policy class-dependent fashion not captured by existing theory. In particular, we identify three phenomena which lead to improved sample complexity: (i) *representational benefits*; (ii) *value-based feedback*; and (iii) *exploration*. Our results in this section can serve as a starting point toward developing a more fine-grained understanding of algorithms and sample complexity of imitation learning.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Representational benefits", "weight": 1.0} -->

The classical intuition behind algorithms like Dagger and Aggrevate (which Footnote 5 attempts to quantify) is *recoverability*: through online access, we can learn to correct the mistakes of an imperfect policy. Our results in Sections 2 and 3 show that recoverability has limited benefits for stationary policy classes as far as horizon is concerned. In spite of this, the following proposition shows that recoverability can have pronounced benefits for *representational* reasons, even with constant horizon. {proposition}\[Representational benefits of online IL\] For any $N \in {\mathbb{N}}$, there exists a class $\mathcal{M}$ of MDPs with $H = 2$ and a policy class $\Pi$ with ${\log{|\Pi|}} = {O{(N)}}$ such that

<!-- chunk {"id": "body-0077", "role": "body", "section": "Representational benefits", "weight": 1.0} -->

There is an online imitation learning algorithm that achieves ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} = 0$ with probability at least $1 - \delta$ using $O{({\log{(\delta^{- 1})}})}$ episodes for any MDP $M^{\star} \in \mathcal{M}$ and expert policy $\pi^{\star} \in \Pi$. In particular, this can be achieved by Dagger.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Representational benefits", "weight": 1.0} -->

Any proper offline imitation learning algorithm requires $n = {\Omega{(N)}}$ trajectories to learn a non-trivial policy with ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \leq c$ for an absolute constant $c > 0$.^1616^16We expect that this result extends to *improper* offline IL algorithms for which $\hat{\pi} \notin \Pi$, but a more complicated construction is required; we leave this for the next version of the paper.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Representational benefits", "weight": 1.0} -->

The idea behind this construction is as follows: The behavior of the (stochastic) expert policy at step $h = 1$ is very complex, and learning to imitate it well in distribution (e.g., with respect to total variation or Hellinger distance) is a difficult representation learning problem (in the language of Section 2, e.g., Section 2.2, we must take $\log{|\Pi_{1}|}$ very large in order to realize $\pi_{1}^{\star}$). For offline imitation learning, we have no choice but to imitate $\pi_{1}^{\star}$ well at $h = 1$, leading to the lower bound in Section 4. With online access though, we can give up on learning $\pi_{1}^{\star}$ well, and instead learn to correct our mistake at step $h = 2$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Representational benefits", "weight": 1.0} -->

For the construction in Section 4, this a much easier representation learning problem, and requires very low sample complexity (i.e., we can realize $\pi_{2}^{\star}$ with a class $\Pi_{2}$ for which $\log{|\Pi_{2}|}$ is small. We conclude that Dagger can indeed lead to substantial benefits over offline IL, but for representational reasons unrelated to horizon, and not captured by existing theory. While this example is somewhat contrived, it suggests that potential to develop a deeper understanding of representational benefits in imitation learning, which we leave as a promising direction for future work.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

Beginning with the work of Ross and Bagnell on Aggrevate, many works (e.g., Sun et al. ) consider a *value-based feedback* variant of the online IL framework (Section 1.1) where in addition to (or instead of) observing $a_{h}^{\star}$, the learner observes the expert's advantage function ${A_{h}^{\pi^{\star}}{(x_{h}, \cdot )}}:={{Q_{h}^{\pi^{\star}}{(x_{h},{\pi_{h}^{\star}{(x_{h})}})}} - {Q_{h}^{\pi^{\star}}{(x_{h}, \cdot )}}}$ or value function $Q_{h}^{\pi^{\star}}{(x_{h}, \cdot )}$ at every state visited by the learner (see Section F.2 for details, which are deferred to the appendix

<!-- chunk {"id": "body-0082", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

While such feedback intuitively seems useful, existing theoretical guarantees---to the best of our knowledge--- only show that algorithms like Aggrevate are no worse than non-value based methods like Dagger, and do not quantify situations in which value-based feedback actually leads to improvement.^1717^17These results are reductions which bound regret in terms of different notions of supervised learning performance, which makes it somewhat difficult to compare them or derive concrete end-to-end guarantees.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

The following result shows that i) value-based feedback can lead to arbitrarily large improvement over non-value based feedback for representational reasons similar to Section 4 (that is for a complicated stochastic expert, learning to optimize a fixed value function can be much easier than learning to imitate the expert well in TV distance), but ii) it is only possible to exploit value-based feedback in this fashion under online interaction (that is, even if we annotate the trajectories for offline imitation learning with $A_{h}^{\pi^{\star}}{(x_{h}, \cdot )}$ for the visited states, this cannot lead to improvement in sample complexity). {proposition}\[Benefits of value-based feedback (informal)\] For any $N \in {\mathbb{N}}$, there is a class of MDPs $\mathcal{M}$ with $H = 2$ and a policy class $\Pi$ with ${\log{|\Pi|}} = {O{(N)}}$ such that

<!-- chunk {"id": "body-0084", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

There is an online imitation learning algorithm with value-based feedback that achieves ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} = 0$ with probability at least $1 - \delta$ using $O{({\log{(\delta^{- 1})}})}$ episodes for every MDP $M^{\star} \in \mathcal{M}$ and expert $\pi^{\star} \in \Pi$. In particular, this can be achieved by Aggrevate.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

Any proper offline imitation learning algorithm (with value-based feedback) or proper online imitation learning algorithm (without valued-based feedback) requires $n = {\Omega{(N)}}$ trajectories to learn a non-trivial policy with ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \leq c$ for an absolute constant $c > 0$.^1818^18As with Section 4, we expect that this lower bound can be extended to improper learners, but a more complicated construction is required.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Benefits of value-based feedback", "weight": 1.0} -->

As with Section 4, this example calls for a fine-grained policy class-dependent theory, which we hope to explore more deeply in future work.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Benefits from exploration", "weight": 1.0} -->

A final potential benefit of online interaction arises in *exploration*. One might hope that with online access, we can directly guide the MDP to informative states that will help to identify the optimal policy faster. The following proposition gives an example in which deliberate exploration can lead to arbitrarily large improvement over offline imitation learning, as well as over naive online imitation learning algorithms like Dagger that do not deliberately explore. {proposition}\[Benefits of exploration for online IL\] For any $n \in {\mathbb{N}}$ and $H \in {\mathbb{N}}$, there exists an MDP $M^{\star}$ and a class of deterministic policies $\Pi$ with ${|\Pi|} = 2$ with the following properties.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Benefits from exploration", "weight": 1.0} -->

There exists an online imitation learning algorithm that returns a policy $\hat{\pi}$ such that ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} = 0$ with probability at least $1 - \delta$ using $O{({\log{(\delta^{- 1})}})}$ episodes, for *all possible reward functions* (i.e., even if $\mu = H$).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Benefits from exploration", "weight": 1.0} -->

The idea behind this construction is simple: We take the lower bound construction from Section 2.4 and augment it with a "revealing" which directly reveals the identity of the underlying expert. The true expert never visits this state, so offline imitation learning algorithms cannot exploit it (standard online IL algorithms like Dagger and relatives do not exploit the revealing state for the same reason),^1919^19This phenomenon is also distinct from "active" online imitation learning algorithms which can obtain improved sampling complexity under strong distributional assumptions in the vein of active learning, but still do not deliberately explore. but a well-designed online IL algorithm that deliberately navigates to the revealing state can use it to identify $\pi^{\star}$ extremely quickly.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Benefits from exploration", "weight": 1.0} -->

As with the previous examples, this construction is somewhat contrived, but it suggests that directly maximizing information acquisition may be a useful algorithm design paradigm for online IL, and we hope to explore this more deeply in future work.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we validate our theoretical results empirically. We first provide a detailed overview of our experimental setup, including the control and natural language tasks we consider, then present empirical results for each task individually.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We evaluate the effect of horizon on the performance of LogLossBC in three environments. We begin by describing our training and evaluation protocol (which is agnostic to the environment under consideration), then provide details for each environment.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

In each experiment, we begin with an expert policy $\pi^{\star}$ (which is always a neural network; details below) and construct an offline dataset by rolling out with it $n$ times for $H$ timesteps per episode. To train the imitator policy $\hat{\pi}$, we use the same architecture as the expert, but randomly initialize the weights and use stochastic gradient descent with the Adam optimizer to minimize the LogLossBC objective for the offline dataset. We repeat this entire process for varying values of $H$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

To evaluate the regret ${J{(\pi^{\star})}} - {J{(\hat{\pi})}}$ after training, we approximate the average reward of the imitator policy $\hat{\pi}$ by selecting new random seeds and collecting $n$ trajectories of length $H$ by rolling out with $\hat{\pi}$; we approximate the average reward of the expert $\pi^{\star}$ in the same fashion, and we also compute several auxiliary performance measures (details below) that aim to capture the distance between $\hat{\pi}$ and $\pi^{\star}$. In all environments, we normalize rewards so that the average reward of the expert is at most 1, in order to bring us to the sparse reward setting in Section 1.1 and keep the range of the possible rewards constant as a function of the (varying) horizon.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We consider four diverse environments, with the aim of evaluating LogLossBC in qualitatively different domains: (i) Walker2d, a classical continuous control task from MuJoCo where the learner attempts to make a stick figure-like agent walk to the right by controlling its joints; (ii) Beamrider, a standard discrete-action RL task from the Atari suite, where the learner attempts to play the game of Beamrider; (iii) Car, a top-down discrete car racing environment where the car has to avoid obstacles to reach a goal, and (iv) Dyck, an autoregressive language generation task where the agent is given a sequence of brackets in $\left\{ {\{,\}},{\lbrack,\rbrack},{} \right\}$ and has to close all open brackets in the correct order.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We emphasize diversity in task selection in order to demonstrate the generality of our results, covering discrete and continuous actions spaces, as well as both control and language generation. For some of the environment (Walker2d, Beamrider), the task is intended to be "stateless", in the sense that varying the horizon $H$ does not change the difficulty of the task itself (e.g., complexity of the expert policy $\pi^{\star}$), allowing for an honest evaluation of the difficulty of the *learning* problem as we vary the horizon $H$. For other domains, such as Dyck, horizon dependence is more nuanced, as here the capacity required to represent the expert grows as the horizon increases; this manifests itself in our theoretical results through the realizability condition (Footnote 3), which necessitates a more complex function class $\Pi$ as $H$ increases.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We now provide details for our experimental setup for each environment.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Walker2d", "weight": 1.0} -->

We use the Gymnasium environment Walker2d-v4, which has continuous state and action spaces of dimensions 17 and 6 respectively. The agent is rewarded for moving to the right and staying alive as well as being penalized for excessively forceful actions; because we vary the horizon $H$, in order to make the comparison fair, we normalize the rewards so that our trained expert always has average reward 1. Our expert is a depth-2 MLP with width 64. We use the Stable-Baselines3 implementation of the Proximal Policy Optimization (PPO) algorithm with default settings to train the expert for 500K steps. The policy's action distribution is Gaussian, with the mean and covariance determined by the MLP; we use this for computation of the logarithmic loss. For data collection, we enforce a *deterministic* expert by always playing the mean of the Gaussian distribution produced by their policy. Our imitator policy uses the same architecture as the expert policy, with the weights re-initialized randomly.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Walker2d", "weight": 1.0} -->

We train the imitator using the logarithmic loss by default, but as an ablation, we also evaluate the effect of training with the mean-squared-error loss on the Euclidean norm over the actions. We train using the Adam optimizer with a learning rate of $10^{- 3}$ and a batch size of 128. We stop training early based on the validation loss on a held out set of expert trajectories. Note that the expert and imitator policies above are both *stationary policies*.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Beamrider", "weight": 1.0} -->

We use the Gymnasium environment BeamRiderNoFrameskip-v4, which has 9 discrete actions and a 210x160x3 image as the state; the rewards are computed as a function of how many enemies are destroyed. As in the case of the previous setup, we account for the varying of $H$ by normalizing expert rewards to be 1. Here we do not train our expert ourselves, but instead use the trained PPO agent provided by Raffin, which is a convolutional neural network. We use the same architecture for our imitator policy, with the weights re-initialized randomly. Here, the expert (and imitator) policies map the observation to a point on the probability simplex over actions, and so logarithmic loss computation is immediate. Similar to the case of Walker2d, we enforce a deterministic expert for collecting trajectories by taking the action with maximal probability. We then train our imitators using the same setup as in the Walker2d environment. As with Walker2d, the expert and imitator here are both stationary policies.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Car", "weight": 1.0} -->

We introduce a simple top-down navigation task where the agent is a "car" that always moves forward by one step, but can take actions to move left, right, or remain in its lane to avoid obstacles and reach the desired destination. There are $M$ possible lanes. At timestep $h \in {\lbrack{H + 1}\rbrack}$, if the agent is in lane $i \in {\lbrack M\rbrack}$, then the agent's state is $(i,h)$. We view the state space as a $M \times {({H + 1})}$ grid; a given point $(i,j)$ in the grid can be empty, or contain an obstacle, or contain the agent.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Car", "weight": 1.0} -->

The agent's action space consists of 3 possible actions: stay in the current lane (${(i,h)}\mapsto{(i,{h + 1})}$), move one step left (${(i,h)}\mapsto{({i - 1},{h + 1})}$), or move one step right (${(i,h)}\mapsto{({i + 1},{h + 1})}$). If the agent's action causes it to collide with an obstacle or the boundary of the grid, it is sent to an absorbing state. The agent gets a reward of 1 for reaching the goal state for the first time, and a reward of 0 otherwise. When the agent occupies a state $(i,h)$, it observes an image-based observation $x_{h}$ showing the state of all lanes for $V$ steps ahead where $V$ is the size of the viewing field. At the start of each episode, we randomly sample obstacles positions, the start position, and the goal position.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Car", "weight": 1.0} -->

The goal can be reached after $H$ actions, and it is always possible to reach the goal.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Dyck", "weight": 1.0} -->

In addition to the RL environments above, we evaluate LogLossBC for autoregressive language generation with transformers (cf. Section A.3), where the goal of the "agent" is to complete a valid word of a given length in a Dyck language; this has emerged as a popular sandbox for understanding the nuances of autoregressive text generation in theory and empirically. We recall that a Dyck language ${\mathsf{D}\mathsf{y}\mathsf{c}\mathsf{k}}_{k}$ consists of $2k$ matched symbols thought of as open and closed parentheses, with concatenations being valid words if the parentheses are closed in the correct order. For example, if we define the space of characters as '', '', and '{}', then '${({\lbrack{}\rbrack})}{\{\}}$' is a valid word, whereas '$({\lbrack)}\rbrack$' and '((({}' are not.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Dyck", "weight": 1.0} -->

Our experiments use the Dyck language ${\mathsf{D}\mathsf{y}\mathsf{c}\mathsf{k}}_{3}$. For our expert, we train an instance of GPT-2 small with 6 layers, 3 heads, and 96 hidden dimensions from scratch to produce valid Dyck words. In particular, the training dataset consists of random Dyck prefixes that require exactly $H$ actions (symbols) to complete. To imitate this expert, we train a GPT-2 small model with the same architecture, but with randomly initialized weights on an offline dataset of sequences generated by the expert. We assign a reward $1$ to each trajectory if the generated word is valid, and assign reward $0$ otherwise. We use Adam optimization for training, with our experts trained for 40K iterations in order to ensure their quality. Note that in this environment, the expert and imitator policies are non-stationary, but use *parameter sharing* via the transformer architecture.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Results", "weight": 1.0} -->

We summarize our main findings below.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Effect of horizon on regret", "weight": 1.0} -->

Figures 1 and 2 plot the relationship between expected regret and the number of expert trajectories for the Walker2d (MuJoCo), and BeamriderNoFrameskip (Atari) environments, as the horizon $H$ is varied from $50$ to $500$. For both environments, we find regret is largely independent of the horizon, consistent with our theoretical results. In fact, in the case of BeamriderNoFrameskip, we find that increasing the horizon leads to *better* regret. To understand this, note that our theory provides horizon-agnostic *upper bounds* independent of the environment. Our lower bounds are constructed for specific worst-case environments, and not rule out the possibility of improved performance with longer horizons environments with favorable structure. We conjecture that this phenomenon is related to the fact that longer horizons yield fundamentally more data, as the total number of state-action pairs in the expert dataset is equal to $nH$.^2020^20For example, if we repeat a fixed contextual bandit instance $H$ times across the horizon and train a stationary policy, it is clear that regret should decrease with $H$ under sparse rewards.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Effect of horizon on regret", "weight": 1.0} -->

Less trivial instances where increasing horizon provably leads to better performance are known in some special cases.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Effect of horizon on regret", "weight": 1.0} -->

Fig. 3(a) plots our findings for the Dyck environment. Here, we see that with the number of trajectories $n$ fixed, regret does increase with $H$, which might appear to contradict our theory at first glance. However, we note that the policy class itself must become larger as $H$ increases, as the task itself becomes more difficult (equivalently, the supervised learning error $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\pi^{\star}},{\mathbb{P}}^{\hat{\pi}} \right)$ must grow with $H$). As a result, the regret is not expected to be independent of $H$ for this environment, in spit of parameter sharing.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Effect of horizon on regret", "weight": 1.0} -->

To verify whether supervised learning error is indeed the cause for horizon dependence for Dyck, Fig. 3(b) plots the logarithm of the product of the Frobenius norms of the weight matrices of the expert for varying values of $H$, as a proxy for supervised learning performance.^2121^21We only include log-product-norm plots for Dyck and Car because for the other environments (Walker2d and BeamriderNoFrameskip), we do not change the expert as a function of $H$. We find that the log-product-norms do in fact grow with $H$, consistent with the fact that the regret grows with $H$ in this case.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Effect of horizon on regret", "weight": 1.0} -->

For the Car environment, we observe similar behavior to the Dyck environment, visualized in Fig. 4. We find that performance degrades slightly as a function of the horizon $H$, but that this increase in regret can be explained by an increase in the log-product-norm (Fig. 3(b)). However, the effect is mild compared to Dyck.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Comparison between log loss and square loss", "weight": 1.0} -->

As an ablation, Figures 4 and 5 compare LogLossBC to the original behavior cloning objective of Pomerleau, which uses the mean squared error (MSE) to regress expert actions to observations in the offline dataset. Focusing on the Walker2d environment (Fig. 5) and Car environment (Fig. 4) (other environments presented difficulties in training^2222^22In particular, we attempted a similar result in the Atari environment, using MSE loss being between vectors on the probability simplex over $|\mathcal{A}|$ actions. For MSE loss, we found that the imitator did not train, in the sense that even with 500 expert trajectories, the performance of the cloner did not improve. We suspect this was due to numerical instability in optimization for the MSE loss in this setup or a failure of hyperparameter optimization.), we find that performance with the MSE loss is comparable to that of the logarithmic loss.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Comparison between log loss and square loss", "weight": 1.0} -->

For Walker2d, a possible explanation is that under the Gaussian policy parameterization we use, the MSE loss is the same as the logarithmic loss up to state-dependent heteroskedasticity.^2323^23In theory, the MSE loss can still underperform the logarithmic loss when the heteroskedasticity is severe, but this may not manifest for this environment. Another possible explanation is that this is an instance of the phenomenon described in Section 6.1.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Relationship between regret and Hellinger distance to expert", "weight": 1.0} -->

Finally, we directly evaluate the quality of (i) Hellinger distance $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\pi^{\star}},{\mathbb{P}}^{\hat{\pi}} \right)$, and (ii) validation loss as proxies for rollout performance. We estimate the Hellinger distance using sample trajectories. Fig. 6 displays our findings for Walker2d with $H = n = 500$, where we observe that both metrics, particularly the Hellinger distance, are well correlated with rollout performance, as measured by average reward. In Figure 6(a), we see that under LogLossBC, Hellinger distance and validation loss are highly correlated with each other, and negatively correlated with expected reward, thereby acting as excellent proxies for rollout performance.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Relationship between regret and Hellinger distance to expert", "weight": 1.0} -->

Meanwhile, in Figure 6(b), we find that under behavior cloning with the MSE loss, validation error is less well correlated with the expected reward of the imitator policy, as evinced by the cluster in the upper left corner, where there are policies with roughly the same validation loss, but variable expected reward. On the other hand, the Hellinger distance $D_{\mathsf{H}}^{2}$ still appears to predict the performance of the policy well, as is consistent with our theoretical results.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Discussion", "weight": 1.5} -->

We conclude with additional technical remarks and directions for future research.

<!-- chunk {"id": "body-0117", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

In this case, we observe that ${{\hat{L}}_{\text{bc}}{(\hat{\pi})}} = 0$ (i.e., $\hat{\pi}$ agrees with $\pi^{\star}$ on every instance in the dataset). Consequently, $\hat{\pi}$ can also be viewed as minimizing an empirical version of the trajectory-wise loss in Eq. 13, i.e.

<!-- chunk {"id": "body-0118", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

From here, a standard uniform convergence argument implies that ${\rho\left( {\pi^{\star} \parallel \hat{\pi}} \right)} \lesssim \frac{\log{({{|\Pi|}\delta^{- 1}})}}{n}$, and by combining this with Eq. 14, we obtain the following result. {proposition} For any deterministic expert $\pi^{\star} \in \Pi$, the indicator loss behavior cloning policy $\hat{\pi} = {{{\arg\min}_{\pi \in \Pi}{\hat{L}}_{\text{bc}}}{(\pi)}}$ ensures that with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0119", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

This result, which shows that indicator-loss BC attains a similar horizon-independent rate toLogLossBC under the conditions of Section 2.2, is novel to our knowledge. While this would seem to suggest that indicator-loss BC can match the performance of LogLossBC, there are number of important caveats.

<!-- chunk {"id": "body-0120", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

First, Section 6.1 is not robust to optimization errors or misspecification errors. For example, if $\hat{\pi}$ only minimizes the indicator loss ${\hat{L}}_{\text{bc}}{(\pi)}$ up to error $\varepsilon_{\text{opt}}$, i.e.

<!-- chunk {"id": "body-0121", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

then by adapting the construction of Ross and Bagnell, one can show that in general the algorithm can have ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \geq {{RH} \cdot \varepsilon_{\text{opt}}}$, meaning it no longer achieves horizon dependence. Indeed, in this case, it is no longer possible to translate the bound on ${\hat{L}}_{\text{bc}}{(\hat{\pi})}$ to a bound on the trajectory-level loss in Eq. 29 without incurring an $H$ factor. On the other hand, as we show in Appendix C, if the LogLossBC objective is solved only approximately, i.e.

<!-- chunk {"id": "body-0122", "role": "body", "section": "When is Indicator-Loss Behavior Cloning Suboptimal?", "weight": 1.0} -->

the regret of the algorithm degrades only to ${{J{(\pi^{\star})}} - {J{(\hat{\pi})}}} \lesssim {R \cdot \left( {\frac{\log{({{|\Pi|}\delta^{- 1}})}}{n} + \varepsilon_{\text{opt}}} \right)}$, and thus remains horizon-independent. Similar remarks apply to the case of misspecification. Of course, perhaps the greatest advantage of LogLossBC is that it readily supports stochastic policies, and is far more practical to implement.

<!-- chunk {"id": "body-0123", "role": "body", "section": "The Role of Misspecification", "weight": 1.0} -->

This paper (for both deterministic and stochastic experts) focuses on the realizable setting in which $\pi^{\star} \in \Pi$. It is natural to ask how the role of horizon in imitation learning changes under misspecification. This is a subtle issue, as there are various incomparable notions of misspecification error which can lead to different forms of horizon dependence.

<!-- chunk {"id": "body-0124", "role": "body", "section": "The Role of Misspecification", "weight": 1.0} -->

We leave a detailed investigation of tradeoffs between misspecification and horizon (as well as interplay with online versus offline IL) for future work; by giving the first horizon-independent treatment for the realizable setting, we hope that our results can serve as a starting point.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Our results clarify the role of horizon in offline and online imitation learning, and show that---at least under standard assumptions in theoretical research into imitation learning---the gap between online and offline IL is smaller than previously thought. Instabilities of offline IL and benefits of online IL may indeed arise in practice, but existing assumptions in theoretical research on imitation learning appear be too coarse to give insights into the true nature of these phenomena, highlighting the need to develop a fine-grained, problem-dependent understanding of algorithms and complexity for IL.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

To this end, natural directions include (i) Building upon the initial results in Section 4, and investigating new mechanisms such as exploration and representational benefits through which online IL can improve over offline IL; (ii) Developing and analyzing imitation learning algorithms under control-theoretic assumptions that more directly capture practical notions of instability; (iii) Developing a more refined theory in the context of language models, via the connection in Section A.3. For the latter two directions, an important question is to understand whether the notion of supervised learning error $D_{\mathsf{H}}^{2}\left( {\mathbb{P}}^{\hat{\pi}},{\mathbb{P}}^{\pi^{\star}} \right)$ we consider is a suitable proxy for real-world performance, or whether more refined notions are required.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Our results also highlight the importance of developing *learning-theoretic* foundations for imitation learning that support general, potentially neural function classes. To this end, a natural question left open by our work is to develop complexity measures (analogous to VC dimension or Rademacher complexity) that characterize the minimax sample complexity of online and offline IL for *any policy class*.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Additional Results", "weight": 1.0} -->

Secondary results deferred to the appendix for space include (i) examples and additional guarantees for LogLossBC and LogLossDagger (Appendix C); and (ii) additional lower bounds and results concerning the tightness of Sections 2.4 and 3 (Appendix G).
