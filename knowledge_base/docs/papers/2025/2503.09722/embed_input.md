<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Pitfalls of Imitation Learning When Actions Are Continuous

Topics include Imitation learning, Behavior cloning, Action chunking, Continuous control, Diffusion policy.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides theoretical analysis explaining why action chunking and high-capacity policy representations (Transformers, Diffusion Policy) outperform smooth or low-capacity representations in behavior cloning with continuous actions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of imitating an expert demonstrator in a discrete-time, continuous state-and-action space control system. We show that there exist stable dynamics (i.e. contracting exponentially quickly) and smooth, deterministic experts such that any smooth, deterministic imitator policy necessarily suffers error on execution that is exponentially larger, as a function of problem horizon, than the error under the distribution of expert training data. Our negative result applies to both behavior cloning and offline-RL algorithms, unless they produce highly improper imitator policies — those which are non-smooth, non-Markovian, or which exhibit highly state-dependent stochasticity — or unless the expert trajectory distribution is sufficiently spread. We provide preliminary evidence of the benefits of these more complex policy parameterizations, explicating the benefits of today’s popular policy parameterizations in robot learning (e.g. action-chunking and diffusion-policies). We also establish a host of complementary negative and positive results for imitation in control systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation Learning (IL), or learning a multi-step behavior from demonstration, encompasses both the earliest-introduced and most currently popular methodologies for training autonomous robotic systems with machine learning techniques. These successes have been buoyed by a host of new innovations: the uses of generative models (e.g. Diffusion policies) to represent robotic behavior, the practice of "chunking" sequences of predicted actions, and various means of data augmentation beyond raw expert demonstrations. At the same time, with the rise of large language models (LLMs), IL also has become increasingly more prevalent in settings in which the agent predicts *discrete tokens*, such as steps on a chess board, lines on a math proof, or words in a sentence. For robot applications, in contrast, the state and action variables are continuous (but for convenience, time may still be treated discretely). Hence we ask, > *What are the fundamental differences between imitating continuous actions and discrete behaviors?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

How do these differences explain the necessity of common techniques observed in today's robot learning pipelines?* We consider control systems with continuous-valued states $\mathbf{x}\in\mathbb{X}=\mathbb{R}^{d}$, control inputs $\mathbf{u}\in\mathbb{U}=\mathbb{R}^{m}$ and dynamics $\mathbf{x}_{t+1}=f(\mathbf{x}_{t},\mathbf{u}_{t})$, where $t$ denotes timestep. We assume $f$ is unknown to the learner. The key parameter in our study is the task horizon, denoted by $H\in\mathbb{N}$, or number of steps of behavior to be imitated.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The expert provides $n$ length-$H$ demonstration trajectories $(\mathbf{x}_{1},\mathbf{u}_{1},\dots,\mathbf{x}_{H},\mathbf{u}_{H})$, determined by the *expert policy* $\pi^{\star}:\mathbb{X}\to\mathbb{U}$ via $\mathbf{u}_{t}=\pi^{\star}(\mathbf{x}_{t})$ with some initial state distribution of $\mathbf{x}_{1}$. The learner observes these trajectories and selects a policy $\hat{\pi}:\mathbb{X}\to\mathbb{U}$, deployed under the same dynamics, with the goal of emulating the expert: $\hat{\pi}\approx\pi^{\star}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For clarity, we will use imitation learning (IL) to refer to learning from expert demonstration in which the agent cannot interact further with its environment or the expert after demonstrations are given. We will (colloquially) refer to as behavior cloning (BC) those methods which perform IL by fitting the data with pure supervised learning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As learning is imperfect, the learner makes small errors which may add together over time, forcing the learner to stray off-course. Ultimately, the difference between the trajectories deployed by the learner and the expert trajectories may be much larger than the errors of learning the expert's actions under the distribution of demonstration trajectories, typically by a multiplicative factor depending on $H$. This is the compounding error problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While much attention has been devoted to circumventing compounding error via additional interaction with the expert or with the environment, we aim to understand when imitation learning is possible without interactive access to either the environment or the expert; what we deem the "non-interactive setting."

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Continuous vs. Discrete Settings. Even without interaction, existing theoretical literature shows that compounding error is benign in discrete problem domains: it scales at most polynomially in the problem horizon, $H$ and can even be eliminated entirely in some situations, via an appropriate loss function (e.g. the log-loss, ). However, these results are contingent on being able to estimate expert behavior in certain very strong error metrics (e.g. the $\{0,1\}$-loss) which, while feasible for discrete problems, we show are unattainable when actions are continuous. Prior theoretical literature studying IL in continuous-action control systems has required additional assumptions and algorithmic modifications (e.g. expert-interactions, stabilization oracles and score-matching oracles). Hence, a systematic theoretical understanding of the difficulty of non-interactive, continuous-action IL remains absent.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

We show that imitation learning where both the expert $\pi^{\star}$ and learned policy $\hat{\pi}$ are "simple" suffers from exponential-in-horizon compounding error, even in seemingly benign continuous-state-and-action control systems. This contrasts discrete-token behavior cloning, in which compounding error is at most polynomial in horizon. We also provide evidence that exponential compounding can be mitigated by more sophisticated policy representations. While it has been popular to motivate more sophisticated policies (e.g. action-chunked Transformers and Diffusion policies) by the need to fit "multi-modal " expert data (expert demonstrations with multiple *modes*, or strategies, to solve a given task), this suggests that even the imitation of simple, deterministic, and hence uni-modal experts may benefit from complex policy parameterizations. Importantly, our negative results depend only on the structure of $\hat{\pi}$, but are agnostic to the learning algorithm which produces it.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

In particular, our results apply to behavior cloning, to any any inverse reinforcement approach which does not use additional interaction with the environment, and to offline reinforcement learning (e.g. Kumar et al.; Kostrikov et al. ) approaches.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution 1", "weight": 1.0} -->

We consider smooth, deterministic expert policies and smooth, deterministic dynamical systems that satisfy a control-theoretic property called exponential stability (Definition˜2.1. ‣ 2.2 Control-Theoretic Stability ‣ 2 Preliminaries ‣ The Pitfalls of Imitation Learning when Actions are Continuous")), which stipulates that the effects of perturbations to the system decay exponentially quickly. We colloquially refer to such systems as *stable*. We assume that stability holds both for the dynamics themselves (open-loop stability), and the dynamics in feedback with the expert policy (closed-loop stability). We show that, if the imitator policy is also smooth and deterministic, or more generally, can be written as the sum of a smooth deterministic policy with state-independent noise (we call these "simply-stochastic"), then the learner's execution error is exponentially-in-$H$ larger than the training error under the expert distribution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Informal Version of (Theorems˜1 and 2)", "weight": 1.0} -->

There exists a family of imitation learning problems with exponentially stable, smooth and deterministic experts and dynamics as described above, for which optimal execution error attained by any algorithm constrained to returning simply stochastic policies $\hat{\pi}$ with smooth means is at least $\exp(\Omega(H))$ times the optimal expert-distribution error of *any* (possibly unrestricted) learning algorithm. This holds for a cost of interest that is bounded in $$ and Lipschitz.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Informal Version of (Theorems˜1 and 2)", "weight": 1.0} -->

As noted above, the lower bound depends only on the parameterization of the learned policy $\hat{\pi}$, but not on the learning algorithm used to produce it. Therefore, offline reinforcement learning, behavior cloning, and inverse reinforcement learning without further environmental interaction (e.g. Ho and Ermon ) fail to circumvent the lower bound.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contribution 2", "weight": 1.0} -->

We show that large compounding error occurs for more general stochastic policies, but potentially substantially less than for the "simply-stochastic" policies described above.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Informal Version of (Theorem˜3. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous\"))", "weight": 1.0} -->

For classes of stable, smooth and deterministic experts and dynamics described above, imitation with a general class of smooth, stochastic, but perhaps multi-modal Markovian policies still incurs either exponential error, or else the rate of execution error scales strictly worse than the rate of expert-distribution error.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Informal Version of (Theorem˜3. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous\"))", "weight": 1.0} -->

As described below, we show that a host of more complex policy classes suffice to ameliorate compounding error for our lower bound and validate this finding with numerical simulations (Section˜5).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contribution 3", "weight": 1.0} -->

We show that exponential compounding error is unconditionally unavoidable if system dynamics may be unstable (even if the dynamical system is smooth, Lipschitz and deterministic). Consequently, observation of expert trajectories alone does not suffice for learning in these control systems, no matter what algorithm or policy class are used.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Informal Version of (Theorem˜4. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous\"))", "weight": 1.0} -->

When the system dynamics are permitted to be unstable, exponential compounding error is unavoidable by *any* non-interactive IL procedure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contribution 4", "weight": 1.0} -->

We show that, if expert data are sufficiently "spread" or anti-concentrated, even pure behavior cloning avoids compounding error. Hence, certain conditions on data quality suffice to avoid the pathologies above.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Informal Version of (Theorem˜5. ‣ 3.4 Simple Policies Avoid Compounding Error with Sufficient Coverage ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous\"))", "weight": 1.0} -->

Suppose that the expert demonstrations are smooth and stabilize the dynamics in closed-loop (but dynamics need not be open-loop stable). Then, if the distribution over expert trajectories has a sufficiently "spread" probability density, simple behavior cloning yields low execution error, with limited compounding error.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The benefits of Action-Chunking and Diffusion Policies?", "weight": 1.0} -->

Section˜5 illustrates that our lower bound can be circumvented by using policies that are either non-smooth, non-Markovian, or non simply-stochastic. This provides informal evidence that popular practices in modern robotic imitation learning, such as the use of Diffusion models as policy parameterizations (which are *non simply-stochastic*) and predicting multiple actions per time-step (action-chunking, ) can circumvent these pathologies. In particular, this suggests that multi-modal policies such as diffusion policies can better imitate certain uni-modal expert demonstrations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The benefits of Action-Chunking and Diffusion Policies?", "weight": 1.0} -->

We corroborate the findings in Section 5 with numerical simulations (see Figure˜1). For the challenging open-loop stable construction used in Theorem˜1, we demonstrate in Section˜5.1 the poor performance of different imitation learning methods. Our experiments validate the core tenet of this paper: that continuous-action imitation learning is difficult even when the dynamics are open-loop exponentially stable. Furthermore, our experiments suggest that the aforementioned more complex techniques, such as action-chunking, can successfully circumvent our lower bounds.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Organization", "weight": 1.0} -->

Our paper is organized so that the casual reader can extract all main takeaways from the first few sections, whilst readers more familiar with the statistical learning and reinforcement learning literature can find more systematic treatments of findings in the sections that follow. Section˜2 contains all preliminaries and notation. Section˜3 provides formal statements of all main results, namely those stated in the informal theorems in Section˜1.1 above. Section˜4 provides the broad brushstrokes of the proof of our most surprising result: the lower bounds against imitation in stable systems with "simple" experts (Theorems˜1 and 2). Finally, Section˜5 describes how our lower bound construction can be circumvented by more complex policy parameterizations, and provides experimental evidence to this effect. The main body of the paper concludes with a discussion in Section˜6.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Organization", "weight": 1.0} -->

The remainder of the paper contains two parts. First, the Addendum, targeted at experts, reformulates our results (Section˜7) and provides more detailed theorem statements (Section˜8) in the language of minimax risks favored by the statistical learning community. These results are followed by a more detailed proof schematic in Section˜9. Following the Addendum is a more traditional Appendix, which contains the full proofs of all claims made throughout the manuscript, and whose organization is outlined at its beginning.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.1 (Bounded cost)", "weight": 1.0} -->

We stress that our costs of interests are bounded. Hence, our lower bounds do not rely on an unbounded growth on magnitude of the cost.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.2 (Imitation learning v.s. behavior cloning)", "weight": 1.0} -->

For clarity, we will refer to imitation learning (IL) as the general problem setting described above. More precisely, this is the non-interactive imitation learning setting, as the agent cannot interact further with its environment or the expert after demonstrations $\mathrm{S}_{n,H}$ are given. There are a number of popular IL methodologies. We will colloquially refer to behavior cloning (BC) as those methods which train $\hat{\pi}$ via pure supervised learning; e.g. selecting $\hat{\pi}$ to minimize the empirical version of $\bm{\mathsf{R}}_{\mathrm{expert},L_{p}}$ (defined below) on the sample $\mathrm{S}_{n,H}$. Our lower bounds apply to all imitation learning algorithms, while our upper bound is realized by behavior cloning.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2.2 (Imitation learning v.s. behavior cloning)", "weight": 1.0} -->

$M$-smooth) for all unit vectors $\mathbf{v}\in\mathbb{R}^{d_{2}}$. The mean of stochastic policy $\pi$ is the deterministic policy $\mathrm{mean}[\pi](\mathbf{x}):=\mathbb{E}_{\mathbf{u}\sim\pi(\mathbf{x})}[\mathbf{u}]$; note that if $\pi$ is deterministic, $\pi(\mathbf{x})\equiv\mathrm{mean}[\pi](\mathbf{x})$. We use $\mathbf{e}_{i}$ as shorthand for the $i$-th canonical basis vector, where dimension is clear from context. $\mathcal{B}_{d}(r)$ denotes the ball of radius $r$ in $\mathbb{R}^{d}$, and $\mathcal{S}^{d-1}$ the sphere.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2.2 (Imitation learning v.s. behavior cloning)", "weight": 1.0} -->

$C$ is a "universal constant" if it does not depend on any problem parameters; $a=\operatorname{{O}}\left({b}\right)$ if $a\leq Cb$ for a universal constant $C$, and $a=o_{\star}(b)$ means "$a\leq c\cdot b$ for a *sufficiently small* universal constant $c$."

<!-- chunk {"id": "body-0031", "role": "body", "section": "Compounding Error", "weight": 1.0} -->

Compounding error is the phenomenon by which small errors in estimation of $\pi^{\star}$ during training compound, leading to deviations between $\pi^{\star}$ and $\hat{\pi}$ when deployed on horizon $H$. We measure this by comparing $\bm{\mathsf{R}}_{\mathrm{cost}}$ to a natural measure of error under the distribution of expert data collected: Note that, while $\pi^{\star}$ is deterministic, $\bm{\mathsf{R}}_{\mathrm{expert},L_{p}}$ is well-defined even if $\hat{\pi}$ is stochastic.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Compounding Error", "weight": 1.0} -->

For reasons of technical convenience, we focus on $\bm{\mathsf{R}}_{\mathrm{expert},L_{2}}$ (see Section˜B.5), but qualitatively similar results hold for other choices of $p$ (e.g. $\bm{\mathsf{R}}_{\mathrm{expert},L_{1}}$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Compounding Error", "weight": 1.0} -->

Our paper argues that there exist natural, seemingly benign settings for continuous action IL where, for some choice of $\mathrm{cost}$, imitating a simple expert with a simple policy renders $\bm{\mathsf{R}}_{\mathrm{cost}}$ exponentially larger than $\bm{\mathsf{R}}_{\mathrm{expert},L_{2}}$: Above, "worst-case optimal" means the minimal value attained by a suitable IL algorithm $\mathrm{alg}$, on the worst-case problem instance (formally, the minimax risk, Section˜7).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Control-Theoretic Stability", "weight": 1.0} -->

Adopting a control-theoretic perspective (e.g. ), our notion of "benign-ness" is defined in terms of exponential incremental stability. In general, stability is a control-theoretic property of a dynamical system that describes the sensitivity of the dynamics to perturbations of the state or input (c.f. Kirk ). We focus on an incredibly strong form of stability that we call exponential incremental stability, which corresponds to a dynamical system in which the effects of perturbations on future dynamics diminish exponentially in time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The RL Perspective on Imitation Learning", "weight": 1.0} -->

Given that policies can be measured in terms of total-cost incurred, it has been popular to adopt the formalism of reinforcement learning to study performance of IL methods. Focusing on additive costs $\mathrm{cost}(\mathbf{x}_{1:H},\mathbf{u}_{1:H})=\sum_{h=1}^{H}\mathrm{cost}_{h}(\mathbf{x}_{h},\mathbf{u}_{h})$, define the $Q$-function The $Q$-function formalism gives two natural conditions under which $\bm{\mathsf{R}}_{\mathrm{cost}}$ can be controlled by training risk.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

Eqs.˜2.3 and 2.4 are special cases of a more general principle that the imitation learning error can be related to a certain integral probability metric (IPM) induced by the class of possible $Q$-functions: $L$-Lipschitz $Q$-functions induce an IPM which scales the $L_{1}$ expert-distribution error by a factor of $L$, whereas the condition that the $Q$-functions are bounded by $B$ scales the resulting $\{0,1\}$ loss bound by that same factor.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Control vs. RL Perspectives, and Limitations of the Latter", "weight": 1.0} -->

The control perspective focuses on the properties of the dynamical map $f$, and the closed-loop dynamics between $f$ and the expert policy $\pi^{\star}$. The RL perspective places assumptions directly on the $Q$-functions; these depend implicitly on the dynamics and choice of cost, and, when arguing via the performance difference lemma, on the learner policy $\hat{\pi}$. One connection between the two viewpoints is that, when the learned policy $\hat{\pi}$ is such that $(\hat{\pi},f)$ is E-IISS, the resulting $Q$-functions are Lipschitz, and hence compounding error is avoided (see Section˜B.3

<!-- chunk {"id": "body-0038", "role": "body", "section": "The limitations of prior work", "weight": 1.0} -->

Recall from Eq.˜2.4 that imitation in the $\{0,1\}$ loss (as considered in Eq.˜2.4) yields at most $\mathrm{poly}(H)$ compounding error, a now-classical argument present, e.g., in the the seminal Dagger paper Ross and Bagnell. Recent work by Foster et al. shows improved dependence on horizon when the imitation error is measured in the trajectory-wise Hellinger distance, which can be achieved algorithmically by minimizing a $\log$-loss. Remark˜B.1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The limitations of prior work", "weight": 1.0} -->

‣ B.4 Impossibility of Estimation in the {0,1}-Loss (Section˜2.4) ‣ Appendix B Appendix for Section˜2 ‣ Appendix ‣ The Pitfalls of Imitation Learning when Actions are Continuous") discusses the classical fact that the Hellinger distance is qualitatively equivalent to the Total Variation distance, which, when specialized to per-timestep imitation of deterministic experts, is equal to the $\{0,1\}$-loss considered in Eq.˜2.4. Hence, the findings in both Ross and Bagnell and Foster et al. implicitly require that it be feasible to imitate in the binary, $\{0,1\}$ sense.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The limitations of prior work", "weight": 1.0} -->

However, in Section˜B.4 ‣ Appendix B Appendix for Section˜2 ‣ Appendix ‣ The Pitfalls of Imitation Learning when Actions are Continuous"), we show that non-vacuous $\{0,1\}$ imitation is impossible in continuous action spaces, exposing the limitations of this analysis in such settings.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Main Results", "weight": 1.0} -->

Organization. This section presents our main results in their most concrete forms: Theorems˜1 and 2 are lower bounds against "simple" policies (defined below), Theorem˜3. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous") is a lower bound for more general policies, and Theorem˜4. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous") lower bounds arbitrary policies when dynamics are unstable. Finally, Theorem˜5. ‣ 3.4 Simple Policies Avoid Compounding Error with Sufficient Coverage ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous") shows that compounding error can be avoided when expert data provides sufficient coverage. Each theorem has a corresponding result, labeled as "Theorem #.A" given in Section˜8, which is more granular and formulated in the language of minimax risks better suited to the expert reader. These show that arbitrary families of $L_{2}$ regression problems can be embedded into imitation learning problems which witness the same degree of compounding error. All lower bounds instantiate a common proof schematic, given in Section˜9.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Main Results", "weight": 1.0} -->

Setup. Recall from Lemma˜2.1 that if $(\hat{\pi},f)$ is E-IISS, compounding error is avoided. Hence, our negative results necessarily leverage that the learner has uncertainty over the true dynamics $f$, and thus cannot ensure $(\hat{\pi},f)$ is incrementally stable. Indeed, if $f$ is known and $(\pi^{\star},f)$ is guaranteed to be stable, then the (possibly inefficient) algorithm which optimizes only over policies $\hat{\pi}$ for which $(\hat{\pi},f)$ is stable avoids compounding error. To this end, we establish lower bounds against problem families defined as follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "\"Simple\" Policies and Algorithms", "weight": 1.0} -->

We define simple IL policies as a slight generalization of the smooth, deterministic expert policies considered above. Simple algorithms are those that return simple policies.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simple Policies Fail to Imitate Simple Experts", "weight": 1.0} -->

Recall the notation $\mathbb{E}_{[\mathrm{alg},\pi^{\star},f,n,H]}$ denoting expectation under a sample $\mathrm{S}_{n,H}$ drawn from $[\pi^{\star},f,D]$, and policy $\hat{\pi}\sim\mathrm{alg}(\mathrm{S}_{n,H})$. Our main result states that, for any desired fractional rate of estimation, there exist regular problem families with open- and closed-loop stable dynamics for which execution error is exponentially larger than training error.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3.1 (Significance of unknown dynamics)", "weight": 1.0} -->

From Lemma˜2.1, if $\hat{\pi}$ stabilizes $f$, the resulting Q-function is Lipschitz. And we know from Eq.˜2.3 that Lipschitzness of the $Q$-functions prevents compounding error. Crucially, Eq.˜2.3 consider the $Q$ function induced by the learned policy $\hat{\pi}$ and the *actual dynamics*, which we will denote $f_{\star}$. But while $\hat{\pi}\in\Pi(\mathcal{P})$ stabilizes every $f$ such that $(\hat{\pi},f)\in\mathcal{P}$, it does not stabilize every possible $f_{\star}\in\mathcal{F}(\mathcal{P})$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 3.1 (Significance of unknown dynamics)", "weight": 1.0} -->

Stated otherwise, the product instance class $\tilde{}\mathcal{P}:=\Pi(\mathcal{P})\times\mathcal{F}(\mathcal{P})$ contains pairs $(\hat{\pi},f_{\star})$ which are *not* closed loop stable. This may be interpreted as follows: the expert will always act in a way that stabilizes the actual dynamics, but not in a way that stabilizes *every possible dynamics.* Thus, if we cannot resolve the true dynamics $f_{\star}$, we cannot ensure $\hat{\pi}$ stabilizes it, and thus cannot ensure the resulting $Q$-function is Lipschitz. If the true dynamics $f_{\star}$ were known, then we could just restrict only to the set of $\hat{\pi}$ which stabilize it, and avoid compounding error.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 3.2 (RL interpretation of open-loop stability)", "weight": 1.0} -->

The property that $f$ is open-loop stable implies that, under dynamics $f$ and the *zero policy* $\pi_{0}(\mathbf{x})\equiv\mathbf{0}$, the resulting $Q$-function is Lipschitz. In other words, the open-loop stability of all $f\in\mathcal{F}(\mathcal{P})$ is equivalent to the existence of a known, single reference policy $\pi_{0}$ which renders all $Q$-functions associated with $(\pi_{0},f)$ Lipschitz. Thus, our results say that the existence of such a single known stabilizing/Lipschitz-inducing policy is insufficient (given the simplicity requirements).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 3.3 (Error amplification, not unbounded costs)", "weight": 1.0} -->

Crucially, our lower holds for costs that are bounded in $$, and as show in Theorem˜2, the probability of the event on which error is magnified by $\exp(H)$ is at least a universal constant. Thus, our results state that it is error amplification, rather than unbounded growth of the costs, that accounts for the lower bound.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Lower Bounds Against More Complex Policies", "weight": 1.0} -->

We now give two lower bounds for possibly non-simple policies. The first relaxes the simply-stochastic requirement, at the expense of a weaker result, and the second holds unconditionally, but considers unstable open-loop (as opposed to E-IISS) dynamics. Section˜5 presents very preliminary evidence that non-simple policies may indeed be more powerful for imitating simple experts; an observation which the authors find quite surprising.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lower Bounds Against More Complex Policies", "weight": 1.0} -->

The next result requires two new objects. First, the class $\mathbb{A}_{\mathrm{gen},\mathrm{smooth}}(L,M,\alpha,p)\supset\mathbb{A}_{\mathrm{simple}}(L,M)$ of algorithms which return policies with $L$-Lipschitz, $M$-smooth means, and whose stochasticity satisfies a mild anti-concentration condition parameterized by $\alpha,p\in(0,1]$. For suitable constants $\alpha,p$ bounded away from zero, this class includes all simply-stochastic, Gaussian, and most mixture-policies as special cases. The second is an $L_{2}$-variant of $\bm{\mathsf{R}}_{\mathrm{cost}}$, denoted $\bm{\mathsf{R}}_{\mathrm{cost},L_{2}}$. Formal definitions are deferred to Section˜8.2. Once supplied, the following theorem is entirely formal.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simple Policies Avoid Compounding Error with Sufficient Coverage", "weight": 1.0} -->

Theorem˜1 relies on the indistinguishability of different stabilizing system dynamics from the perspective of the learner. In Theorem˜5. ‣ 3.4 Simple Policies Avoid Compounding Error with Sufficient Coverage ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous"), which follows, we show that this can be circumvented via E-IISS in addition to a strong data coverage requirement, which we term *well-spreadness* (Definition˜3.5. ‣ 3.4 Simple Policies Avoid Compounding Error with Sufficient Coverage ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous")). Well-spread distributions can arise naturally, for instance via additive Gaussian exploration noise in the context of fully controllable systems. Our result, proved in Appendix˜I, can be interpreted as a polynomial upper bound for experts whose own trajectories induce sufficient exploration (see Remark˜I.1 for a more careful explanation).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.1 (Connection to the gap metric)", "weight": 1.0} -->

The gap-metric in control theory allows one to measure the extent to which two different dynamical systems can be stabilized by the same control law. In our case, both transition matrices $\mathbf{A}_{i}$ are stable in the classical sense (see also Definition˜4.2 above), and thus, as noted above, are simultaneously stabilized by the indentically-zero control law. However, neither system can be stabilized by any linear feedback which coincides with the $\mathbf{K}_{i}$'s on the subspace $V=\mathrm{span}(\mathbf{e}_{2})$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

Our formal proof is based on a minimax framework introduced in Section˜7. Then, more detailed statements of results are given in Section˜8, with a detailed proof schematic in Section˜9. Full proof details are given in Appendix˜E. All repurposable technical tools are given in Appendix˜A. Here, we summarize some of the essential technical ingredients. A key theme is the need for compounding error with good enough probability, which is necessary due to the boundedness of costs (if all errors are concentrated on rare events, then any bounded cost must be small in expectation.)

<!-- chunk {"id": "body-0054", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

Statistical Learning. The functions $g^{\star}$ defining the "$R_{2}$ policy" $\pi^{\star}(\mathbf{x})=g^{\star}(\mathbf{x})\mathbf{e}_{1}$ must be chosen from a class that is (a) smooth (to preserve overall system smoothness), and (b) has non-trivial statistical error when learned from *noiseless training examples* $(\mathbf{x}_{0},g^{\star}(\mathbf{x}_{0}))$. In particular, linear $g^{\star}$ does not suffice. A key subtlety is that (c) we require the estimation error of $g^{\star}$ to be large with constant probability; otherwise, the large errors can only compound by a limited amount before saturating the bound on the cost magnitude. In Proposition˜7.1, we show that non-parametric function classes of $\{g\}$ satisfy requirements (a), (b), and (c).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

This requires operating in the "interpolation," or noise-free, setting of nonparametric regression.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

Bump functions. We use bump functions to stitch together the aforementioned $R_{1},R_{2}$ regions in a smooth manner. Doing so requires care to ensure that the system remains globally stable, and we accomplish this by making the magnitude of the nonlinear terms sufficiently small, so that they are dominated by the stable linear dynamics.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

By smoothness of $\hat{\pi}$, and by making $\Delta$ sufficiently small, classical arguments for zero-order gradient estimation ensure $\nabla\mathrm{mean}[\hat{\pi}(\mathbf{0})]\mathbf{P}_{V}\approx\mathbf{K}_{i}\mathbf{P}_{V}$, where $\mathbf{P}_{V}$ is the projection onto $V$ (note: $\mathbf{K}_{1}\mathbf{P}_{V}=\mathbf{K}_{2}\mathbf{P}_{V}$). To ensure compounding error with constant probability, we leverage anti-concentration due to the Carbery-Wright and Paley-Zygmund inequalities; these use the convenient fact that the uniform distribution on the unit ball is log-concave.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

Compounding error in nonlinear systems. The most significant technical obstacle is generalizing our compounding error argument from linear to nonlinear systems. First, consider deterministic policies $\hat{\pi}$. Define the autonomous dynamical system $F_{i}(\mathbf{x})=f_{i}(\mathbf{x},\hat{\pi}(\mathbf{x}))=\mathbf{A}_{i}\mathbf{x}+\hat{\pi}(\mathbf{x})$, and $\hat{\mathbf{K}}:=\nabla\hat{\pi}(\mathbf{0})$, we see that $\nabla F_{i}(\mathbf{0})=\mathbf{A}_{i}+\hat{\mathbf{K}}$ must be unstable along the $\mathbf{e}_{1}$ direction for one $i\in\{1,2\}$, by Proposition˜4.1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

‣ 4 Proof Overview ‣ The Pitfalls of Imitation Learning when Actions are Continuous"). To show that the resulting *nonlinear* system is unstable, we adopt an argument due to Jin et al. to bound the rate at which gradient-based optimizers escape strict saddle points. This can be viewed as a quantitative analogue of the classical unstable manifold theorem. When policies are simply-stochastic, their randomness can be coupled such that the joint distribution $(\hat{\mathbf{u}},\hat{\mathbf{u}}^{\prime})\sim(\pi(\mathbf{x}),\pi(\mathbf{x}^{\prime}))$ ensures the differences $\hat{\mathbf{u}}-\hat{\mathbf{u}}^{\prime}=\mathrm{mean}[\pi](\mathbf{x})-\mathrm{mean}[\pi](\mathbf{x}^{\prime})$ are deterministic. Beyond simply-stochastic policies, as in the proof of Theorem˜3.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Overview of Additional Proof Techniques", "weight": 1.0} -->

‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous"), we use a considerably more subtle coupling to witness our stipulated anti-concentration condition, described in Section˜8.2.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Potential Benefits of Complex Policy Parameterizations", "weight": 1.0} -->

In this section, we evaluate the extent to which policies that violate the simplicity condition (Definition˜3.3. ‣ 3.1 “Simple” Policies and Algorithms ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous")) can improve over those which abide by it.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experimental Findings", "weight": 1.0} -->

First, we conduct a series of experiments using the open-loop stable construction Construction˜E.1. ‣ E.1 Lower Bound Construction ‣ Appendix E Proof for Simple Policies, Theorems˜1, 1.A and 2 ‣ Appendix ‣ The Pitfalls of Imitation Learning when Actions are Continuous") underlying Theorem˜1, demonstrating that our construction can be used as a benchmark for common behavior cloning pipelines. See Appendix˜J for details. We visualize in Figure˜2 the cost $\max_{t}\langle\mathbf{e}_{1},\mathbf{x}_{t}\rangle$ (a) for different checkpoints over the course of a single training run, (b) as a function of the number of rollout timesteps for different methods, and (c) on Diffusion policy with larger action-chunks. The experiments highlight several counterintuitive aspects of our construction: The rollout cost increases although validation loss decreases throughout training.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experimental Findings", "weight": 1.0} -->

Random noise outperforms all policy learning methods and avoids exponential-in-time error, due to the E-IISS open-loop stability of the dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experimental Findings", "weight": 1.0} -->

More complex techniques such as Diffusion Policy, replica noising, and action-chunking outperform regular behavior cloning.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experimental Findings", "weight": 1.0} -->

Notably, action-chunking does not suffer from exponential error, which we attribute to the open-loop stability of each chunk. These results affirm our theory and suggest that imitators must be non-simple in order to avoid exponential error.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Three Stylized, Non-Simple Policies", "weight": 1.0} -->

Next, we provide an informal discussion of how non-simple policies can circumvent exponential compounding error. Each strategy can be applied to the construction underpinning our main theorem, Theorem˜1, and we show that the lower bounds based on that construction can be circumvented (see Appendix˜H). In particular, this shows that Theorem˜3. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous") is qualitatively unimprovable without appealing to a different construction.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Three Stylized, Non-Simple Policies", "weight": 1.0} -->

Any smooth, deterministic policy $\hat{\pi}$ suffers from exponential compounding error on this problem: approximating $\hat{\pi}(\mathbf{x})\approx k\mathbf{x}+\mathbf{u}_{0}$, where $k\in\mathbb{R}$, around the origin $\mathbf{x}\approx\mathbf{0}$, we see that the dynamics compound with either $(\rho+k)^{t}$ or $(\rho-k)^{t}$, one of which must have an exponent of base $>1$. This same pathology extends to simply-stochastic policies by considering *differences* in trajectories, and coupling them so that their randomness cancels. We further recall from Theorem˜4. ‣ 3.3 Lower Bounds Against More Complex Policies ‣ 3 Main Results ‣ The Pitfalls of Imitation Learning when Actions are Continuous") that in $d=\Omega(\log H)$-dimensions, compounding error is unconditionally unavoidable.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Three Stylized, Non-Simple Policies", "weight": 1.0} -->

However, for the one-dimensional case described here, removing the constraints of either Markovianity, simple-stochasticity, or smoothness can evade this challenge.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Action-Switching", "weight": 1.0} -->

Consider a time-dependent strategy $\pi(\mathbf{x},t)$, which alternates between $\pi(\mathbf{x},t)=-\rho\mathbf{x}$ if $t$ is odd and $\pi(\mathbf{x},t)=\rho\mathbf{x}$ if $t$ is even. By time-step $t=3$, the system will have converged to state $\mathbf{x}_{3}=0$, and will remain at rest there. This strategy uses time-dependence to hedge over dynamical uncertainty; time-dependence can be replaced by stochasticity as shown below.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Action-Switching", "weight": 1.0} -->

In addition, the only system unknown is $\xi$. Hence, one can consider a history dependent policy $\pi(\mathbf{x}_{1:t},\mathbf{u}_{1:t-1})$. Then $\pi$ can selects, for $t\geq 2$, $\mathbf{u}_{t}=-\left(\frac{\mathbf{x}_{2}-\mathbf{u}_{1}}{\mathbf{x}_{1}}\right)\mathbf{x}_{t}$. The above is always equal to $-\xi\rho\mathbf{x}_{t}$, sending $\mathbf{x}_{t}$ to zero for $t\geq 2$. This is essentially an adaptive control strategy: learning the unknown underlying dynamics to stabilize it (and it succeeds for $\rho$ unknown!).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Benevolent Gambler's Ruin", "weight": 1.0} -->

Gambler's Ruin is the classical paradox where a gambler's wealth $W_{t}\in\mathbb{R}$ either doubles or is made zero at successive time steps $t\geq 1$ with equal probability $1/2$. In expectation, $\mathbb{E}[W_{t}]=W_{1}$ for all times $t$. But, with probability one, there exists a finite $t_{\star}$ for which the gambler loses their funds: $W_{t_{\star}}=0$. Concretely, $\operatorname{\mathbb{P}}[t_{\star}>t]=\operatorname{\mathbb{P}}[W_{t+1}\neq 0]=2^{-t}\to 0$. While gambling ultimately ruins the gambler in finite time, a stochastic policy can enact the same strategy to its benefit.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Benevolent Gambler's Ruin", "weight": 1.0} -->

For $t\geq 1$, we consider the Benevolent Gambler's Ruin policy $\pi_{\textsc{bgr}}(\mathbf{x})$ which selects $\rho\mathbf{x}$ with probability $1/2$ and $-\rho\mathbf{x}$ with the remaining probability. Crucially, such a policy's randomization depends on the state, and therefore is not simply-stochastic. This policy has an identically zero, and therefore smooth, mean $\mathrm{mean}[\pi_{\textsc{bgr}}](\mathbf{x})\equiv\mathbf{0}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 5.1 (Other notions of smoothness)", "weight": 1.0} -->

We notice that (in dimension $1$) the Gambler's Ruin policy satisfies $W_{1}(\pi_{\textsc{bgr}}(\mathbf{x}),\pi_{\textsc{bgr}}(\mathbf{x}^{\prime}))=W_{2}(\pi_{\textsc{bgr}}(\mathbf{x}),\pi_{\textsc{bgr}}(\mathbf{x}^{\prime}))=||\mathbf{x}|-|\mathbf{x}^{\prime}||$, which is *non-smooth* in the Wasserstein distance. This suggests that more stringent notions of smoothness may preclude these strategies.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Concentric Stabilization", "weight": 1.0} -->

Concentric stabilization swaps randomization/alternation for non-smoothness. For integers $j\in\mathbb{Z}$, define intervals $\mathcal{I}_{j}=((2\rho)^{-2j},(2\rho)^{-2(j-1)}]$. For any $\mathbf{x}\in\mathbb{R}\setminus\{0\}$, there exists a unique $j(\mathbf{x})$ such that $|\mathbf{x}|\in\mathcal{I}_{j(\mathbf{x})}$. We define the concentric stabilization policy, $\pi_{\textsc{cs}}(\mathbf{x})$ which selects $\rho\mathbf{x}$ if $j(\mathbf{x})$ is even, and $-\rho\mathbf{x}$ if $j(\mathbf{x})$ is odd.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Concentric Stabilization", "weight": 1.0} -->

This policy is deterministic, but highly non-smooth as $\mathbf{x}\to 0$.^55^5For $\mathbf{x}$ bounded away from zero, it can be smoothed out via bump functions, with smoothness proportional to $1/|\mathbf{x}|^{2}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

We demonstrate that imitation learning in a continuous-action control system can exhibit exponential-in-horizon compounding error, even if the dynamics are stable in both open- and closed-loop. We provide preliminary evidence that more complex policy parameterizations may be able to avoid this pitfall, and that expert data with good coverage avoids compounding error even under unstable dynamics. There are many exciting questions for future work: (a) When precisely can complex policies mitigate compounding error? (b) How can the expert provide optimal agents from suboptimal states? (c) What is the sample complexity of offline RL, e.g. from *suboptimal data*, in control systems. A final pressing question is understanding the benefits and limitations of online environment interaction (e.g. RL finetuning) in continuous-action control.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

Lastly, our work corroborates a provocative empirical finding from Block et al.: what makes behavior cloning challenging is not instability in the dynamics themselves, but rather instabilities arising from the closed-loop feedback between dynamics and an imperfect imitation policy. As shown in Section˜5, the design choices in the behavior cloning policy (Diffusion, data-augmentation, action-chunking) lead to meaningful differences in performance; Block et al. finds similarly that the choice of *optimizer* can have similar effects on downstream performance as well. Thus, better understanding the interactions between the design space of algorithms, optimizers, and data is an important direction for future theoretical, empirical, and methodological work.
