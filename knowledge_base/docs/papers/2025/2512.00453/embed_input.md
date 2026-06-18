<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample-Efficient Expert Query Control in Active Imitation Learning via Conformal Prediction

Topics include Imitation learning, Robotics, Safety, Robustness, Datasets, Real-time systems, Control, Learning, Sampling, CRSAIL, Active imitation learning, AIL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Active imitation learning (AIL) combats covariate shift by querying an expert during training. However, expert action labeling often dominates the cost, especially in GPU-intensive simulators, human-in-the-loop settings, and robot fleets that revisit near-duplicate states. We present Conformalized Rejection Sampling for Active Imitation Learning (CRSAIL), a querying rule that requests an expert action only when the visited state is under-represented in the expert-labeled dataset. CRSAIL scores state novelty by the distance to the K-th nearest expert state and sets a single global threshold via conformal prediction. This threshold is the empirical (1-alpha) quantile of on-policy calibration scores, providing a distribution-free calibration rule that links alpha to the expected query rate and makes alpha a task-agnostic tuning knob. This state-space querying strategy is robust to outliers and, unlike safety-gate-based AIL, can be run without real-time expert takeovers: we roll out full trajectories (episodes) with the learner and only afterward query the expert on a subset of visited states.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Evaluated on MuJoCo robotics tasks, CRSAIL matches or exceeds expert-level reward while reducing total expert queries by up to 96% vs. DAgger and up to 65% vs. prior AIL methods, with empirical robustness to alpha and K, easing deployment on novel systems with unknown dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning (IL) offers a compelling alternative to reward engineering in reinforcement learning by training a policy to reproduce expert behavior directly from demonstrations \[osa2018algorithmic\]. Its successes range from dexterous robot control to autonomous driving \[hu2022model, ross2013learning, kim2024surgical\]. However, IL suffers from *covariate shift*: as the agent explores, its on-policy state distribution diverges from the expert's, leading to compounding control errors \[ross2011reductionimitationlearningstructured\]. *Active imitation learning* (AIL) addresses this by querying the expert for additional action labels in states where the learner is likely to fail. In practice, those queries can be the chief bottleneck: running a high-fidelity simulator for an expert consumes GPU hours, human-in-the-loop labeling induces operator fatigue, and safety-critical domains may forbid frequent interventions \[laskey2017comparing, zhang2016query\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most existing query-management schemes either ask the expert far too often \[bcfail\], require the expert to seize full control \[hoque2021lazydaggerreducingcontextswitching, hoque2021thriftydaggerbudgetawarenoveltyrisk\], or rely on action-uncertainty thresholds \[menda2019ensembledaggerbayesianapproachsafe\] that do not reliably indicate novelty in state space. Consequently, they inflate both the annotation budget and the aggregated expert dataset with redundant data, slowing training while adding little informational value. For example, multi-agent systems executing the same policy do not need to query an expert again if a similar state has already been labeled; a naive approach would increase the number of expert queries roughly in proportion to the number of agents \[hoque2023fleet\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address this challenge with Conformalized Rejection Sampling for Active Imitation Learning (CRSAIL). CRSAIL casts selective querying as a conformal prediction problem and uses conformal calibration to set a data-driven query threshold. To quantify how new an encountered state is, we use the distance to the $K$-th nearest neighbor in the existing expert-labeled set: a large distance indicates that the agent has entered an unfamiliar region of the state space. During an initial calibration phase, we roll out the initial policy to collect unlabeled on-policy states and set a distance threshold $R$ as an empirical $({1 - \alpha})$ quantile of their nonconformity scores (see Fig. 1 for an overview). This threshold turns $\alpha$ into a principled tuning knob for controlling the expected query rate. At training time, if a visited state's distance lies below $R$ (a region already well represented by expert data), we forgo querying; otherwise, we request the expert action. Queries are issued post hoc in batch after each episode, so no real-time takeovers are required.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This simple rule concentrates expert effort on truly novel and poorly covered regions. As a result, it reduces labeling cost and promotes a more diverse expert dataset by populating the finite replay buffer with a compact set of informative states rather than near-duplicates. Conformal prediction also makes threshold selection robust; because $R$ is defined by a quantile, it is not skewed by extreme outliers caused by covariate shift. By choosing a miscoverage rate $\alpha$, we obtain principled budget control: the fraction of queried states is approximately $\alpha$. This data-driven threshold adapts to the state-space density of each task and reduces per-task retuning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. We will first introduce existing methods that reduce expert queries, then formulate density-based sample rejection as a conformal prediction problem, detail the CRSAIL procedure, present experiments and ablations, and conclude with limitations and future directions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Environment", "weight": 1.0} -->

We model the environment as a discrete-time Markov decision process

<!-- chunk {"id": "body-0010", "role": "body", "section": "Environment", "weight": 1.0} -->

where $\mathcal{X}$ is a measurable state space, $\mathcal{U}$ is an action space, $P{( \cdot \mid x,u)}$ is a Markov transition kernel on $\mathcal{X}$, $r:{{\mathcal{X} \times \mathcal{U}}\rightarrow{\mathbb{R}}}$ is a reward used only for evaluation, $\mathcal{X}_{0}$ is a distribution on $\mathcal{X}$ for initial states, $\mathcal{X}_{T} \subseteq \mathcal{X}$ is a terminal set, and $T_{\max} \in {{\mathbb{N}} \cup {\{\infty\}}}$ is the episode horizon.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Environment", "weight": 1.0} -->

A policy may be deterministic $\pi:{\mathcal{X}\rightarrow\mathcal{U}}$ or stochastic, with $\pi{( \cdot \mid x)}$ being a distribution with support over $\mathcal{U}$. An episode begins at $x_{0} \sim \mathcal{X}_{0}$ and evolves, for $t = {0,1,\ldots}$, as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Environment", "weight": 1.0} -->

Rolling out a policy $\pi$ under the dynamics in Eq. 2 yields the random trajectory

<!-- chunk {"id": "body-0013", "role": "body", "section": "Expert and imitation loss", "weight": 1.0} -->

We are given an expert policy $\pi_{E}$, possibly stochastic. When the expert is queried at state $x$, the expert action label is a draw $u_{E} \sim \pi_{E}{( \cdot \mid x)}$. Let $\pi_{\theta}$ be a parametric learner and $\ell:{{\mathcal{U} \times \mathcal{U}}\rightarrow{\mathbb{R}}_{\geq 0}}$ an action loss (e.g., squared error). We define the population imitation loss as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Expert and imitation loss", "weight": 1.0} -->

where the expectation is with respect to $x_{0} \sim \mathcal{X}_{0}$, the trajectory generated by $P$ and $\pi_{\theta}$, and the expert draws $u_{E,t} \sim \pi_{E}{( \cdot \mid x_{t})}$. An extension to stochastic learner policies $\pi_{\theta}{( \cdot \mid x)}$ is possible with minor changes of notation; $\pi_{\theta}$ is deterministic in our experiments. The expert labels $u_{E,t}$ are a conceptual oracle for defining the objective; during training we only observe labels at queried times (defined below). Let $\theta^{\star} \in {{\arg{\min_{\theta}J}}{(\theta)}}$ denote an ideal minimizer; computing $\theta^{\star}$ is generally infeasible due to unknown dynamics and nonconvexity. Our algorithms therefore learn an approximate solution from a subset of expert action labels.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Initial dataset", "weight": 1.0} -->

We obtain our initial learner parameter $\theta_{0}$ and policy $\pi_{\theta_{0}}$ via behavioral cloning (BC) on $D_{\exp}^{}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Admissible querying strategies", "weight": 1.0} -->

where $S_{j}$ denotes the query index set and $Q_{j}$ the corresponding expert-labeled state--action pairs for episode $j$, as defined next. First, a *querying strategy* $\psi$ specifies, for each episode, at which time steps the expert is queried. Given the training history $H_{i}$ in and the current trajectory $\tau^{(i)} = {(x_{0}^{(i)},u_{0}^{(i)},\ldots,x_{L_{i}}^{(i)})}$, we define the *query index set* for episode $i$ as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Admissible querying strategies", "weight": 1.0} -->

so that $t \in S_{i}$ means that the state $x_{t}^{(i)}$ is sent to the expert for labeling. We require $\psi$ to be non-anticipatory across episodes (it does not depend on future episodes). Given $S_{i}$, the per episode query multiset is

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stopping time and training length $C$", "weight": 1.0} -->

For a fixed querying strategy $\psi \in \Psi$ and budgets $B$ (queries) and $T_{train}$ (steps) in ${\mathbb{N}} \cup {\{\infty\}}$, we define the number of training episodes (which is a random variable) as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stopping time and training length $C$", "weight": 1.0} -->

Training halts once either the total number of queries reaches $B$ or the total number of environment steps reaches $T_{train}$; setting $B = \infty$ or $T_{train} = \infty$ relaxes the corresponding budget constraint. By construction, $C$ is a stopping time with respect to the natural training history, as it depends only on information available up to episode $i$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Objective and the optimal strategy $\\psi^{\\star}$", "weight": 1.0} -->

Let $\Psi$ denote the class of admissible strategies, as defined per Eq. 8. Our goal is to minimize the expected imitation loss of the final policy under budgets $B$ and $T_{train}$. We therefore aim to solve

<!-- chunk {"id": "body-0021", "role": "body", "section": "Objective and the optimal strategy $\\psi^{\\star}$", "weight": 1.0} -->

where the expectation is over the joint randomness of $\mathcal{X}_{0}$, $P$, the learner policies $\{\pi_{\theta_{i}}\}$, the expert $\pi_{E}$, the strategy $\psi$, and the learning operator $\mathsf{U}\mathsf{p}\mathsf{d}\mathsf{a}\mathsf{t}\mathsf{e}$. Both the stopping time $C$ and the terminal parameters $\theta_{C}$ depend on the chosen strategy $\psi$; we suppress this dependence in the notation for readability.

<!-- chunk {"id": "body-0022", "role": "body", "section": "What $C$, $Q$, and $\\psi^{\\star}$ mean operationally", "weight": 1.0} -->

The stopping time $C$ is the data dependent training length induced; it is the first episode at which either the query budget or the interaction budget is exhausted. The multiset $Q$ is the realized collection of expert action labels; its cardinality $\sum_{i = 0}^{C - 1}{|Q_{i}|}$ is the consumed expert budget. The strategy $\psi^{\star}$ is the rule that, for given budgets $(B,T_{train})$, yields the lowest expected final imitation loss among all admissible strategies. One may either fix a query budget $B$ (and take $T_{train} = \infty$) and compare the achieved reward at that budget, or fix an interaction budget $T_{train}$ (and take $B = \infty$) and compare the total number of queries and the reward. The former is more natural in deployment, while the latter is convenient for analysis and is the regime we use in Sec. V.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Intuition for the strategy class used later", "weight": 1.0} -->

In Section IV, we introduce episode-level querying strategies that use state-space coverage to decide when to query the expert. For integers $K \geq 1$ and a threshold $R > 0$, define

<!-- chunk {"id": "body-0024", "role": "body", "section": "Intuition for the strategy class used later", "weight": 1.0} -->

where the novelty score $s_{K}{(x;D_{\exp}^{(i)})}$ is the distance from $x$ to its $K$-th nearest neighbor among the states in the current expert dataset $D_{\exp}^{(i)}$. We set $R$ once by conformal calibration on unlabeled on-policy states so that a user-specified miscoverage $\alpha$ directly controls the expected query rate. Because $\psi_{R,K}$ operates post hoc at the episode level, it requires no real-time expert takeovers and belongs to the admissible class $\Psi$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conformalized Rejection Sampling for Active Imitation Learning", "weight": 1.0} -->

To solve the optimization problem in Eq. 12, we instantiate an admissible post hoc querying strategy $\psi_{R,K}$ (see Eq. 13) that avoids requesting expert action labels in regions of the state space already well represented by the current expert dataset $D_{\exp}^{(i)}$. The strategy is evaluated after each episode, produces the per-episode query multisets $Q_{i}$ in the form of Eq. 9, and, together with the learning operator $\mathsf{U}\mathsf{p}\mathsf{d}\mathsf{a}\mathsf{t}\mathsf{e}$, determines the stopping time $C$ in Eq. 11.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Querying by state-space novelty", "weight": 1.0} -->

Let the state projection of the current expert dataset be

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Querying by state-space novelty", "weight": 1.0} -->

where ${B{(x,r)}} = {\{{z \in {\mathbb{R}}^{d}}:{{\|{z - x}\|} \leq r}\}}$. In the language of conformal prediction, $s_{K}$ is a *nonconformity score*: larger values mean that $x$ is more atypical relative to the expert data. Equivalently, $s_{K}\left( x;D_{\exp}^{(i)} \right)$ is the radius of the smallest closed ball centered at $x$ that contains at least $K$ elements of $D_{X}^{(i)}$. Larger scores indicate lower local data density and hence greater novelty; increasing $K$ makes the score more robust to outliers and accepting of duplicates.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Querying by state-space novelty", "weight": 1.0} -->

Given a threshold $R > 0$, the post hoc query indices and the queried multiset for episode $i$ are

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Querying by state-space novelty", "weight": 1.0} -->

which match the general definitions in Eqs. 8 and 9.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Intuition", "weight": 1.0} -->

The rule in Eq. 16 concentrates expert effort on under-covered regions: if many expert states already lie in a small neighborhood of $x_{t}^{(i)}$, we skip labeling; if the neighborhood is sparse, we request the expert label. This targets the query budget at states expected to improve generalization while avoiding redundant labels in well-represented areas.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Threshold selection via conformal calibration", "weight": 1.0} -->

The key question is *"How do we set a single threshold $R$ in a task-agnostic and statistically principled way?"* We calibrate $R$ using conformal prediction on unlabeled *on-policy* states from the initial learner $\pi_{\theta_{0}}$ (no expert labels are needed for calibration). We briefly recall only the ingredients needed here and refer the reader to standard introductions to conformal prediction for a more comprehensive treatment; see \[angelopoulos2022gentleintroductionconformalprediction, lindemann2024formal\].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Finite-sample quantile", "weight": 1.0} -->

For a user-chosen miscoverage $\alpha \in {}$, define

<!-- chunk {"id": "body-0033", "role": "body", "section": "Finite-sample quantile", "weight": 1.0} -->

and let $s_{} \leq \cdots \leq s_{(N_{cal})}$ be the order statistics of $\{ s_{j}\}$. Set the calibrated threshold

<!-- chunk {"id": "body-0034", "role": "body", "section": "Finite-sample quantile", "weight": 1.0} -->

In practice, Eq. 20 is equivalent to a non-interpolating empirical quantile of level $q = {m/N_{cal}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Coverage guarantee and interpretation", "weight": 1.0} -->

If the calibration states and future on-policy states were exchangeable for a fixed policy, classical conformal prediction would imply

<!-- chunk {"id": "body-0036", "role": "body", "section": "Coverage guarantee and interpretation", "weight": 1.0} -->

for any future on-policy state $x_{new}$. Thus, a fraction of at least $1 - \alpha$ of such states would lie in $R$-dense regions and would not be queried by Eq. 16, so $\alpha$ specifies a nominal query rate. In our actual training procedure the policy evolves over iterations and, even for a fixed policy, states along a trajectory are temporally correlated and not identically distributed across time steps, so exchangeability is violated and should be viewed as an idealized reference rather than a strict guarantee. Nevertheless, varying $\alpha$ affects the empirical quantile $R$: increasing $\alpha$ lowers the target coverage level, thus decreases $R$ and marks a larger fraction of states as "novel," leading to more expert queries. *This makes $\alpha$ an effective knob for trading off coverage and query rate* even without a formal guarantee under policy shift.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Why not recalibrate with an updated policy?", "weight": 1.0} -->

As learning progresses, the learner policy $\pi_{\theta_{i}}$ typically spends more time in regions of the state space that are already well covered by the aggregated expert dataset $D_{\exp}^{(i)}$. One might consider periodically re-running the conformal calibration step with the current policy and dataset to obtain updated thresholds $R_{i}$. However, this continually re-normalizes the distance scores to the states that are currently visited, forcing the query rate to remain approximately constant rather than decaying as coverage improves. Such periodic recalibration largely removed the desirable decay of the query rate over training duration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Why not recalibrate with an updated policy?", "weight": 1.0} -->

For this reason we calibrate once using $\pi_{\theta_{0}}$ and keep a single threshold $R$ fixed; as $\pi_{\theta_{i}}$ improves and $D_{\exp}^{(i)}$ grows around expert-like regions, an increasing fraction of visited states falls within the region where ${s_{K}{(x;D_{\exp}^{(i)})}} \leq R$ and no longer triggers queries.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Why not recalibrate with an updated policy?", "weight": 1.0} -->

1:Inputs: initial learner πθ0; expert dataset Dexp; integer K; miscoverage α ∈; calibration episodes Mcal.
2:Roll out πθ0 for Mcal episodes; collect Xcal = {xj}j = 1Ncal.
4: sj ← sK (xj;Dexp) ⊳ distance to the Kth neighbor
Algorithm 1 CRSAIL radius calibration

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C The CRSAIL training algorithm", "weight": 1.0} -->

After behavioral cloning on $D_{\exp}^{}$ and a single calibration to compute $R$, CRSAIL iterates episodes with post hoc batch querying and dataset aggregation. Algorithms 1 and 2 summarize the radius-calibration step and the full CRSAIL training loop, respectively. Each iteration instantiates $\psi_{R,K}$ and forms $Q_{i}$ via Eq. 16, updates $D_{\exp}^{({i + 1})}$ and advances the learner by Eq. 10. Training halts at the stopping time $C$, i.e., as soon as either the query budget $B$ or the step budget $T_{train}$ is exhausted.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C The CRSAIL training algorithm", "weight": 1.0} -->

1:Inputs: expert policy πE; initial dataset Dexp; miscoverage α; integer K (K-th neighbor order); calibration episodes Mcal; query budget B; step budget Ttrain.
3:R ← CRSAIL_Calibration (πθ0,Dexp,K,α,Mcal)
4:i ← 0, t ← 0, q ← 0 ⊳ iterations, steps and queries
5:while t &lt; Ttrain and q &lt; B do
6: Roll out πθi to obtain states x0(i), …, xLi(i)
14:return πθi ⊳ final policy πθC

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computational notes", "weight": 1.0} -->

We construct tensors for the learner states and expert states and use the GPU to compute their pairwise distance matrix. We then take per-state K-th-order statistics. Since K is small and the queries are post hoc, this adds only minor overhead compared with simulation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Link back to the objective", "weight": 1.0} -->

CRSAIL sets $\psi = \psi_{R,K}$ in Eq. 12. In our experiments, when $\Psi$ is restricted to CRSAIL and the baseline strategies, $\psi_{R,K}$ consistently achieves near-expert reward while using dramatically fewer expert queries, so it serves as an empirical surrogate for $\psi^{\star}$ within this restricted class.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

We evaluate on three MuJoCo control tasks for stabilization, manipulation, and locomotion with randomized initial states. The expert for each task is an RL model trained with Stable Baselines3 to near-convergence. We compare CRSAIL against DAgger, EnsembleDAgger, and ThriftyDAgger. We omit SafeDAgger, LazyDAgger, and RNDAgger: SafeDAgger's gating is subsumed by later baselines, while LazyDAgger (by the same authors as Thrifty) was highly sensitive and unstable in our pilots (often failing to query and stagnating). Thrifty demonstrably improves upon LazyDAgger, so we treat Thrifty as its successor baseline. RNDAgger had no public implementation, and any speculative reimplementation would risk an unfair comparison.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

All learned policies (and auxiliary networks) use an MLP with a single hidden layer of size $64$. After each training episode, we evaluate the learner over 100 episodes and compute its average episodic return; a run is deemed to have *converged to expert level* once this average reaches at least $95\%$ of the expert's. For each baseline, we use the hyperparameters reported in the original paper on any environment they benchmarked; on environments not covered there, we sweep the gating hyperparameters to span query rates from near $0\%$ upward and choose the smallest value that yields convergence on most runs (for a fixed offline dataset), in order to maximize query efficiency. The final choices are listed in Table I. For CRSAIL we fix $K = 5$ and choose $\alpha$ from a coarse sweep, selecting a slightly conservative value in the range $\alpha \in {\lbrack 0.9,0.95\rbrack}$ where performance and query counts are stable (see Table II).

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

We report (i) convergence rate, (ii) the number of expert queries issued until the run first reaches expert-level performance, and (iii) the total number of expert queries over the entire training run. For each dataset size $M$, we create five independent offline datasets drawn from the same expert as discussed in Eq. 6. All methods are run with a fixed interaction budget $T_{train}$ and $B = \infty$. Thus all methods see the same number of environment steps, while their total expert queries $\sum_{i = 0}^{C - 1}{|Q_{i}|}$ may differ.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

*Task 1: Inverted Double Pendulum (InvDP)*. We apply horizontal force to balance a double pendulum (9-dimensional state space, scalar action space). Episodes last up to 1,000 steps with early termination on failure, emphasizing query efficiency when trajectories bifurcate to quick failures with zero reward vs. long sequences with large rewards. This causes challenges as our expert is imperfect ($90\%$ success rate). Offline datasets use $M \in {\{{1\text{k}},{2\text{k}},{3\text{k}},{5\text{k}},{10\text{k}}\}}$ states (five datasets per $M$); training runs for $T_{\text{train}} = {15,000}$ steps.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

*Task 2: Pusher*. We control a 7-DoF arm to push a cylinder to a target (23-dimensional state space, 7-dimensional action space). The dense shaping and randomized targets stress novelty detection in higher-dimensional state spaces; episodes are 100 steps. Offline datasets use $M \in {\{{1\text{k}},{2\text{k}},{5\text{k}},{10\text{k}},{20\text{k}}\}}$ (five per $M$); training runs for $T_{\text{train}} = {2,000}$ steps.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

*Task 3: Hopper*. We control a planar one-legged robot that must hop forward without falling (11-dimensional state space, 3-dimensional action space), emphasizing long-horizon stability. The expert typically makes a few hops before falling, so trajectories mix successful and failing behavior; this makes state-space novelty less informative for CRSAIL, while action-based gates can still exploit the small action space. We therefore view Hopper as a challenging, near worst-case benchmark for our method. Offline datasets use $M \in {\{{1\text{k}},{2\text{k}},{5\text{k}},{10\text{k}},{20\text{k}}\}}$ states (five datasets per $M$); training runs for $T_{\text{train}} = {10,000}$ steps.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

#M
#M
#M

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

#M
#M
#M

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Effect of $\\alpha$", "weight": 1.0} -->

On Pusher, Table II shows that the convergence probability increases with both $\alpha$ and the initial dataset size $M$; for $\alpha \geq 0.9$ all runs converge for all $M$, indicating that CRSAIL is robust to the choice of $\alpha$. As expected from the calibration rule, larger $\alpha$ yields more total queries by lowering the target coverage level and marking more states as novel, while the dependence of queries-to-converge on $\alpha$ is much weaker, so higher $\alpha$ mainly drives additional queries after convergence. This robustness to $\alpha$ is a practical advantage over existing AIL methods, which typically require careful per-task tuning of query thresholds. In practice, choosing a mid-range $\alpha$ (e.g., $0.9$--$0.95$) balances convergence and budget. Similar trends exist across the other tasks and more $\alpha$ values, but have been omitted due to space limitations in order to focus on algorithm comparisons.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Effect of $K$", "weight": 1.0} -->

On Pusher, we fix the miscoverage level at $\alpha = 0.93$ and sweep the neighbor order $K$ (Table III). *For every $K$ and initial dataset size $M$, CRSAIL converges to expert-level reward on all runs*, and both the queries-to-expert and total queries are nearly flat in $K$, indicating that performance is largely insensitive to the neighbor order. Intuitively, increasing $K$ averages over more neighbors and should mitigate the effect of isolated outliers at the cost of slightly more queries; the empirical flatness suggests that such isolated outliers are rare in these sequential trajectories and that even a small neighborhood already captures the relevant local geometry of the expert data. Similar behavior is observed on the other environments and omitted for space.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

As previously mentioned, we compare our work against DAgger, EnsembleDAgger and ThriftyDAgger through our suite of environments.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

(a) Inverted Double Pendulum (Ttrain = 15, 000 steps)

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

Table IV compares convergence, queries-to-expert, and total expert queries across tasks and initial expert set sizes. On *Inverted Double Pendulum* and *Pusher*, CRSAIL achieves 100% convergence for every $M$ while querying dramatically less than all baselines. On *Pusher* specifically, CRSAIL is uniformly the most query-efficient method *for all $M$*---it requires the fewest queries to reach expert-level performance and the fewest total queries. On *InvDP*, it uses the fewest *total* queries at every $M$ and attains the fewest *queries to converge to expert* in $4/5$ cases (second-best in the remaining setting). By contrast, ThriftyDAgger struggles to converge on *Pusher* as $M$ increases (convergence falling to ${80\%},{40\%},{20\%}$) despite a relatively high target query rate ${TQR} = 0.4$; increasing $TQR$ could improve convergence but would inflate query counts toward DAgger-like levels.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

On *Hopper*---our most challenging domain---CRSAIL remains modestly successful: it converges in $\mathbf{2}\mathbf{4}/\mathbf{2}\mathbf{5}$ runs overall and achieves the lowest *total* query counts at the two smallest initial datasets ($M = {{1k},{2k}}$), while remaining competitive at larger $M$. Unless noted otherwise, $K = 5$ and the threshold parameters $\alpha$ follow the table caption. We report *queries until convergence to expert* as the mean over only those runs that did converge (non-converged runs are excluded from that average).

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

Best Reward (% Expert)
Total Queries (% DAgger)
Total Queries (% SOTA)

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

Table V aggregates across all $M$ values to paint a clear picture: In Inverted Double Pendulum and Pusher, *CRSAIL requests $66.3\%$ and $47.8\%$ fewer expert labels respectively compared to the previous state of the art*, without a meaningful loss of reward. In the hopper task, which as discussed previously is the most challenging to our method, CRSAIL still holds its own: We require fewer queries than EnsembleDAgger, and we achieve better performance than ThriftyDAgger. Note that state-of-the-art is chosen as the algorithm (aside from CRSAIL) that makes the fewest queries on average.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

On Inverted Double Pendulum, Fig. 22(a) ‣ Figure 2 ‣ V-D Comparisons ‣ V Experiments ‣ Sample-Efficient Expert Query Control in Active Imitation Learning via Conformal Prediction") plots how fast each method approaches expert-like behavior as a function of the cumulative number of expert queries. Because all methods share the same step budget $T_{train}$, a vertical slice at a given query budget $B_{0}$ can be interpreted as a fixed-budget comparison: it shows the reward each method achieves before exceeding $B_{0}$. As we can see, CRSAIL converges to the expert the fastest and would score higher than other algorithms for any fixed query budget in this range. We can also see that CRSAIL's curve terminates earliest, indicating that the method stops querying once the desired behavior is achieved. Figure 22(b) ‣ Figure 2 ‣ V-D Comparisons ‣ V Experiments ‣ Sample-Efficient Expert Query Control in Active Imitation Learning via Conformal Prediction") shows the number of queries across training steps. In contrast to other algorithms, CRSAIL intuitively starts with a high query rate as additional information is needed and slowly plateaus.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

Qualitatively similar trends are observed on Pusher and Hopper, but we omit those plots for space. DAgger is omitted as it coincides with the line $y = x$, which dominates the vertical scale.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Comparisons", "weight": 1.0} -->

On InvDP, the initial expert dataset mostly consists of successful episodes, and going off-policy results in failure. A query-efficient method should need fewer queries in longer episodes whose states are already well represented; Fig. 3 confirms this effect. The effect is stronger for larger initial datasets, which contain more successful trajectories.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We presented CRSAIL, a conformal prediction--based framework for query-efficient active imitation learning. Using distance-based nonconformity scores and a principled calibration step, CRSAIL reduces redundant expert queries while maintaining robust convergence across tasks. Our experiments on Inverted Double Pendulum and Pusher demonstrate that CRSAIL is significantly more query efficient than state-of-the-art baselines, while maintaining expert-like performance. Moreover, ablations confirm that CRSAIL is robust to hyperparameter choices and adapts naturally to different dataset sizes and episode structures.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Future work includes incorporating action similarity into the distance metric to better handle critical regions where the policy is less stable, exploring time-varying miscoverage along recalibration to obtain principled control over the decay of the query rate, and applying conformal calibration to other out-of-distribution scores.
