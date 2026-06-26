<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Complexity of Episodic Fixed-Horizon Reinforcement Learning

Topics include Reinforcement learning, Sample complexity, Learning, Markov decision process, Time horizon.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently, there has been significant progress in understanding reinforcement learning in discounted infinite-horizon Markov decision processes (MDPs) by deriving tight sample complexity bounds. However, in many real-world applications, an interactive learning agent operates for a fixed or bounded period of time, for example tutoring students for exams or handling customer service requests. Such scenarios can often be better treated as episodic fixed-horizon MDPs, for which only looser bounds on the sample complexity exist. A natural notion of sample complexity in this setting is the number of episodes required to guarantee a certain performance with high probability (PAC guarantee). In this paper, we derive an upper PAC bound tilde O(|mathcal S|^ |mathcal A| H^/epsilon^ lnfrac 1 delta) and a lower PAC bound tilde Omega(|mathcal S| |mathcal A| H^/epsilon^ ln frac 1 delta+ c) that match up to log-terms and an additional linear dependency on the number of states |mathcal S|. The lower bound is the first of its kind for this setting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our upper bound leverages Bernstein's inequality to improve on previous bounds for episodic finite-horizon MDPs which have a time-horizon dependency of at least H^.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Consider test preparation software that tutors students for a national advanced placement exam taken at the end of a year, or maximizing business revenue by the end of each quarter. Each individual task instance requires making a sequence of decisions for a fixed number of steps student to take an exam in spring 2015 or maximizing revenue for the end of the second quarter of 2014). Therefore, they can be viewed as a finite-horizon sequential decision making under uncertainty problem, in contrast to an infinite horizon setting in which the number of time steps is infinite. When the domain parameters (e.g. Markov decision process parameters) are not known in advance, and there is the opportunity to repeat the task many times (teaching a new student for each year's exam, maximizing revenue for each new quarter), this can be treated as episodic fixed-horizon One important question is to understand how much experience is required to act well in this setting. We formalize this as the sample complexity of reinforcement learning [Strehl2006], which is the number of time steps on which the algorithm may select an action whose value is not near-optimal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

RL algorithms with a sample complexity that is a polynomial function of the domain parameters are referred to as Probably Approximately Correct (PAC)[Kearns1999,Brafman2003,Kakade2003,Strehl2006]. Though there has been significant work on PAC RL algorithms for the infinite horizon setting, there has been relatively little work on the finite horizon scenario.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

In this paper we present the first, to our knowledge, lower bound, and a new upper bound on the sample complexity of episodic finite horizon PAC reinforcement learning in discrete state-action spaces. Our bounds are tight up to log-factors in the $H$, the accuracy $\epsilon$, the number of actions $|\actionspace|$ and up to an additive constant in the failure probability $\delta$. These bounds improve upon existing results by a factor of at least $H$. Our results also apply when the reward model is a function of the within-episode time step in addition to the state and action space. While we assume a stationary transition model, our results can be extended readily to time-dependent state-transitions. Our proposed \texttt{UCFH}\xspace(Upper-confidence fixed-horizon RL) algorithm that achieves our upper PAC guarantee can be applied directly to wide range of fixed-horizon episodic MDPs with known fn:known\_rewards Previous works have shown that the complexity of learning state transitions usually dominates learning reward functions. We therefore follow existing sample complexity analyses and assume known rewards for simplicity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

The algorithm and PAC bound can be extended readily to the case of unknown reward functions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

It does not require additional structure such as assuming access to a generative model[Azar2012] or that the state transitions are sparse or acyclic[Lattimore2012].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

The limited prior research on upper bound PAC results for finite horizon MDPs has focused on different settings, such as partitioning a longer trajectory into fixed length [Kakade2003,Strehl2006], or considering a sliding time window[Kolter2009a]. The tightest dependence on the horizon in terms of the number of episodes presented in these approaches is at least $H^3$ whereas our dependence is only $H^2$. More importantly, such alternative settings require the optimal policy to be stationary, whereas in general in finite horizon settings the optimal policy is nonstationary (e.g. is a function of both the state and the within The best action will generally depend on the state and the number of remaining time steps. In the tutoring example, even if the student has the same state of knowledge, the optimal tutor decision may be to space practice if there is many days till the test and provide intensive short-term practice if the test is tomorrow.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Fiechter[Fiechter1994,Fiechter1997] and [Reveliotis2007] do tackle a closely related setting, but find a dependence that is at least $H^4$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Our work builds on recent work [Lattimore2012,Azar2012] on PAC infinite horizon discounted RL that offers much tighter upper and lower sample complexity bounds than was previously known. To use an infinite horizon algorithm in a finite change is to augment the state space by the time step (ranging over $1,\dots,H$), which enables the learned policy to be non-stationary in the original equivalently, stationary in the newly augmented space). Unfortunately, since these recent bounds are in general a quadratic function of the state space size, the proposed state space expansion would introduce at least an additional $H^2$ factor in the sample complexity term, yielding at least a $H^4$dependence in the number of episodes for the sample complexity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Somewhat surprisingly, we prove an upper bound on the sample complexity for the finite horizon case that only scales quadratically with the horizon. A key part of our proof is that the variance of the value function in the finite horizon setting satisfies a We also leverage recent insights that state pairs can be estimated to different precisions depending on the frequency to which they are visited under a policy, extending these ideas to also handle when the policy followed is nonstationary. Our lower bound analysis is quite different than some prior infinite-horizon results, and involves a construction of parallel multi-armed bandits where it is required that the best arm in a certain portion of the bandits is identified with high probability to achieve near-optimality.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

fixed-horizon MDPs, which can be formalized as a tuple $M = (\mathcal S, \mathcal A, r, p, p_0, H)$. Both, the statespace $\mathcal S$ and the actionspace $\mathcal A$ are finite sets. The learning agent interacts with the MDP in episodes of $H$ time steps. At time $t=1 \dots H$, the agent observes a state $s_t$ and choses an action $a_t$ based on a policy $\pi$ that potentially depends on the within-episode time step, i.e., $a_t = \pi_t(s_t)$ for $t=1, \dots, H$. The next state is sampled from the stationary transition kernel $s_{t+1} \sim p(\cdot | s_t, a_t)$ and the initial state from $s_1 \sim p_0$. In addition the agent receives a reward drawn It is straightforward to have the reward depend on the state, or state/action or state/action/next state.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

determined by the reward function. The reward function $r$ is possibly time-dependent and takes values in $$. The quality of a policy $\pi$ is evaluated by the total expected reward of an episode $R^\pi_M = \mathbb E \left[\sum_{t=1}^H r_t(s_t) \right]$. For simplicity,$^{fn:known_rewards}$ we assume that the reward function $r$ is known to the agent but the transition kernel $p$ is unknown. The question we study is how many episodes does a learning agent follow a policy $\pi$ that is not $\epsilon$-optimal, i.e., $R^*_M - \epsilon > R^{\pi}_M$, with probability at least $1 - \delta$ for any chosen accuracy $\epsilon$ and failure probability $\delta$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

In the following sections, we reason about the true MDP $M$, an empirical MDP $\hat M$ and an optimistic MDP $\tilde M$ which are identical except for their transition probabilities $p$, $\hat p$ and $\tilde p_t$. We will provide more details about these MDPs later. We introduce the notation explicitly only for $M$ but the quantities carry over to $\tilde M$ and $\hat M$ with additional tildes or hats by replacing $p$ with $\tilde p_t$ or $\hat p$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

The (linear) operator \sum\_{s' \in \mathcal S} p(s' | s, \pi\_i(s)) f(s')$ takes any function $f: \mathcal S \rightarrow \mathbb R$ and returns the expected value of $f$ with respect to the next The definition also works for time-dependent transition For convenience, we define the multi-step version as $P^\pi_{i:j} f:= P^\pi_i P^\pi_{i+1} \dots P^\pi_j f$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

The value function from time $i$ to time $j$ is defined as $V^\pi\_{i:j}(s):= \mathbb E\left[\sum\_{t=i}^j r\_t(s\_t) | s\_i = s \right] = \sum\_{t=i}^j P^\pi\_{i:t-1} r\_t = \left(P^\pi\_i V^\pi\_{i+1:j}\right)(s) + r\_i(s)$ and $V^*_{i:j}$ is the optimal value-function. When the policy is clear, we omit the superscript $\pi$. $\succS{s,a} \subseteq \mathcal S$ the set of possible successor states of state $s$ and action $a$. The maximum number of them is denoted by $C = \max_{s,a \in \statespace \times \actionspace} \numSucc{s,a}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setting and Notation", "weight": 1.0} -->

In general, without making further assumptions, we have $C = |\statespace|$, though in many practical domains (robotics, user modeling) each state can only transition to a subset of the full set of states (e.g. a robot can't teleport across the building, but can only take local moves). The notation $\tilde O$ is similar to the usual $O$-notation but ignores log-terms. More precisely $f = \tilde O(g)$ if there are constants $c_1$, $c_2$ such that $f \leq c_1 g (\ln g)^{c_2}$ and analogously for $\tilde \Omega$. The natural logarithm is $\ln$ and $\log = \log_2$is the base-2 logarithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

We now introduce a new model-based algorithm, \texttt{UCFH}\xspace, for RL in finite horizon episodic domains. We will later prove \texttt{UCFH}\xspaceis PAC with an upper bound on its sample complexity that is smaller than prior approaches. Like many other PAC RL algorithms[Brafman2003,Strehl2006a,Strehl2009,Auer2009], \texttt{UCFH}\xspaceuses an optimism under uncertainty approach to balance exploration and exploitation. The algorithm generally works in phases comprised of optimistic planning, policy execution and model updating that take several episodes each. Phases are indexed by $k$. As the agent acts in the environment and observes $(s,a,r,s')$ tuples, \texttt{UCFH}\xspacemaintains a confidence set over the possible transition parameters for each state-action pair that are consistent with the observed transitions. Defining such a confidence set that holds with high probability can be be achieved using concentration inequalities like the Hoeffding inequality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

One innovation in our work is to use a particular new set of conditions to define the confidence set that enables us to obtain our tighter bounds. We will discuss the confidence sets further below. The collection of these confidence sets together form a class of MDPs $\mathcal M_k$ that are consistent with the observed data. We define $\hat M_k$as the maximum likelihood estimate of the MDP given the previous observations. $\mathcal M_k$, \texttt{UCFH}\xspacecomputes a policy $\pi^k$ by performing optimistic planning. Specifically, we use a finite horizon variant of extended value iteration (EVI)[AuerOrtner2005,Strehl2009]. EVI performs modified Bellman backups that are optimistic with respect to a given set of parameters. That is, given a confidence set of possible transition model parameters, it selects in each time step the model within that set that maximizes the expected sum of future rewards. Appendix[sec:fhevi]provides more details about fixed horizon EVI.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

\texttt{UCFH}\xspacethen executes $\pi^k$ until there is a state-action pair $(s,a)$ that has been visited often enough since its last update (defined precisely in the until-condition in \texttt{UCFH}\xspace). After updating the model statistics for this $(s,a)$-pair, a new policy $\pi^{k+1}$ is obtained by optimistic planning again. We refer to each such iteration of planning-execution-update as a phase with index $k$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

\log^2\_2 (4 |\statespace|^2 H^2 / \epsilon)}{\delta} $n(s,a) = v(s,a) = n(s,a,s'):= 0 \quad \forall, s \in \mathcal S, a \in \mathcal A, s' \in \succS{s,a}$ $\hat p(s' | s,a):= n(s, a, s') / n(s, a)$, for all $(s,a)$ with $n(s,a) > 0$ and $s' \in \succS{s,a}$ $\mathcal M_k:= \big\{ \tilde{M} \in \mathcal M_{\textrm{nonst.}} \,: \, \forall (s,a) \in \statespace \times \actionspace, t =1\dots H, s' \in \succS{s,a}$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

$\qquad\qquad\qquad{\tilde p}_{t}(s'|s,a) \in \confset{${\hat p}(s' |s,a), n(s, a)$} \big\} $\tilde M_k, \pi^k:= \evi{$\mathcal M_k$}$ there is a $(s,a) \in \statespace \times \actionspace$ with $v(s, a) \geq \max\{ m w_{\min}, n(s, a) \}$ and Update model statistics for one $(s,a)$-pair with condition above $n(s, a, s'):= n(s, a, s') + v(s, a, s') \quad \forall s' \in \succS{s,a}$ $v(s, a):= v(s, a, s'):= 0 \quad \forall s' \in \succS{s,a}$;

<!-- chunk {"id": "body-0024", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

Upper-Confidence Fixed-Horizon episodic reinforcement learning algorithm \texttt{UCFH}\xspaceis inspired by the infinite-horizon UCRL-$\gamma$ algorithm by [Lattimore2012] but has several important differences.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

First, the policy can only be updated at the end of an episode, so there is no need for explicit delay phases as in UCRL-$\gamma$. Second, the policies $\pi^k$ in \texttt{UCFH}\xspaceare Finally, \texttt{UCFH}\xspacecan directly deal with non-sparse transition probabilities, whereas UCRL-$\gamma$ only directly allows two possible successor states for each Confidence sets. The class of MDPs $\mathcal M_k$ consists of fixed-horizon MDPs $M'$ with the known true reward function $r$ and where the transition probability $p'_t(s' | s,a)$ from any $(s,a) \in \statespace \times \actionspace$ to $s' \in \succS{s, a}$ at any time $t$ is in the confidence set induced by $\hat p(s' | s, a)$ of the empirical MDP $\hat M$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

Solely for the purpose of computationally more efficient optimistic planning, we allow time-dependent transitions (allows choosing different transition models in different time steps to maximize reward), but this does not affect the theoretical guarantees as the true stationary MDP is still in $\mathcal M\_k$ with high probability. Unlike the confidence intervals used by [Lattimore2012], we not only include conditions based on Hoeffding's The first condition in the $\min$ in Equationeqn:conf_set_bern is actually not necessary for the theoretical results to hold. It can be removed and all $6/\delta_1$ can be replaced by $4 / \delta_1$. and Bernstein's inequality (Eq.eqn:conf_set_bern), but also require that the standard deviation $\sqrt{p(1-p)}$ of the Bernoulli random variable associated with this transition is close to the empirical one (Eq.eqn:conf_set_var).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Upper PAC-Bound", "weight": 1.0} -->

This additional condition (Eq.eqn:conf_set_var) is key for making the algorithm directly applicable to generic MDPs (in which states can transition to any number of next states, e.g. $C > 2$) while only having a linear dependency on $C$ in the PAC bound.

<!-- chunk {"id": "body-0028", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

For any $0 < \epsilon, \delta \leq 1$, the following holds. With probability at least $1 - \delta$, \texttt{UCFH}\xspace produces a sequence of policies $\pi^k$, that yield at most $$\tilde O\left(\frac{H^2 C| \statespace \times \actionspace|}{\epsilon^2} \ln \frac{1}{\delta} \right)$$ episodes with $R^* - R^{\pi^k} = V^*_{1:H}(s_0) - V^{\pi^k}_{1:H}(s_0) > \epsilon$. The maximum number of possible successor states is denoted by $1 < C \leq |\statespace|$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Similarities to other analyses. The proof of Theorem[thm:upper\_bound] is quite long and involved, but builds on similar techniques for sample-complexity bounds in reinforcement learning (see e.g. [Brafman2003,Strehl2008]). The general proof strategy is closest to the one of UCRL-$\gamma$ [Lattimore2012] and the obtained bounds are similar if we replace the time horizon $H$ with the equivalent in the discounted case $1/(1 - \gamma)$. However, there are important differences that we highlight now briefly.

<!-- chunk {"id": "body-0030", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

- A central quantity in the analysis by [Lattimore2012] is the local variance of the value function. The exact definition for the fixed-horizon case will be given below. The key insight for the almost tight bounds of [Lattimore2012] and [Azar2012] is to leverage the fact that these local variances satisfy a Bellman equation [Sobel1982] and so the discounted sum of local variances can be bounded by $O((1 - \gamma)^{-2})$ instead of Lemma[lem:varV\_bellman] that local value function variances $\sigma^2_{i:j}$ also satisfy a Bellman equation for fixed-horizon MDPs even if transition probabilities and rewards are time-dependent.

<!-- chunk {"id": "body-0031", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

This allows us to bound the total sum of local variances by $O(H^2)$ and obtain similarly strong results in this - [Lattimore2012] assumed there are only two possible successor states (i.e., $C = 2$) which allows them to easily relate the local variances $\sigma_{i:j}^2$ to the difference of the expected value of successor states in the true and optimistic MDP $(P_i - \tilde P_i) \tilde V_{i+1:j}$. For $C > 2$, the relation is less clear, but we address this by proving a bound with tight dependencies on $C$ (Lemma[lem:sigma\_bound\_generic]). - To avoid super-linear dependency on $C$ in the final PAC bound, we add the additional condition in Equation[eqn:conf\_set\_var] to the confidence set.

<!-- chunk {"id": "body-0032", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

We show that this allows us to upper-bound the total reward difference $R^* - R^{\pi^k}$ of policy $\pi^k$ with terms that either depend on $\sigma^2_{i:j}$ or decrease linearly in the number of samples. This gives the desired linear dependency on $C$ in the final bound. We therefore avoid assuming $C = 2$ which makes \texttt{UCFH}\xspacedirectly applicable to generic MDPs with $C >2$ without the impractical transformation argument used by [Lattimore2012].

<!-- chunk {"id": "body-0033", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

We will now introduce the notion of knownness and importance of state-action pairs that is essential for the analysis of \texttt{UCFH}\xspaceand subsequently present several lemmas necessary for the proof of Theorem[thm:upper\_bound]. We only sketch proofs here but detailed proofs for all results are available in the appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Fine-grained categorization of $(s,a)$-pairs. Many PAC RL sample complexity proofs [Brafman2003,Kakade2003,Strehl2006a,Strehl2009] only have a binary notion of knownness, distinguishing between known (transition probability estimated sufficiently accurately) and unknown $(s,a)$-pairs. However, as recently shown by [Lattimore2012] for the infinite horizon setting, it is possible to obtain much tighter sample complexity results by using a more fine grained categorization. In particular, a key idea is that in order to obtain accurate estimates of the value function of a policy from a starting state, it is sufficient to have only a loose estimate of the parameters of $(s,a)$-pairs that are unlikely to be visited under this policy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Note that $\iota_k(s,a) \in \{ 0, 1, 2, 4, 8, 16 \dots \}$ is an integer indicating the influence of the state-action pair on the value function of $\pi^k$. Similarly, we define the knownness \kappa_k(s,a):= \max \left\{ z_i \,: \, z_i \leq \frac{n_k(s,a)}{m w_k(s,a)} \right\} \in \{ 0, 1, 2, 4, \dots \} which indicates how often $(s,a)$ has been observed relative to its importance. The constant $m$ is defined in Algorithm[alg:fhalg].

<!-- chunk {"id": "body-0036", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

We can now categorize $(s,a)$-pairs into subsets X_{k, \kappa, \iota}:= \{(s, a) \in X_k \,: \, \kappa_k(s, a) = \kappa, \iota_k(s, a) = \iota\} \quad \textrm{and} \quad \bar X_k = \statespace \times \actionspace \setminus X_k where $X_k = \{ (s,a) \in \statespace \times \actionspace \,: \, \iota_k(s,a) > 0 \}$ is the active set and $\bar X_k$ the set of state-action pairs that are very unlikely under the current policy. Intuitively, the model of \texttt{UCFH}\xspaceis accurate if only few $(s,a)$ are in categories with low knownness that is, important under the current policy but have not been observed often so far.

<!-- chunk {"id": "body-0037", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Recall that over time observations are generated under many policies (as the policy is recomputed), so this condition does not always hold. We will therefore distinguish between phases $k$ where $|X_{k, \kappa, \iota}| \leq \kappa$ for all $\kappa$ and $\iota$ and phases where this condition is violated. The condition essentially allows for only a few $(s,a)$ in categories that are less known and more and more $(s,a)$ in categories that are more well known. In fact, we will show that the policy is $\epsilon$-optimal with high probability in phases that satisfy this condition.

<!-- chunk {"id": "body-0038", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

We first show the validity of the confidence sets $M \in \mathcal M_k$ for all $k$ with probability at least $1 - \delta / 2$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

By combining Hoeffding's inequality, Bernstein's inequality and the concentration result on empirical standard deviations by [Maurer2009] with the union bound, we get that $p(s'|s,a) \in \mathcal P$ with probability at least $1 - \delta_1$ for a single phase $k$, fixed $s,a \in \statespace \times \actionspace$ and fixed $s' \in \succS{s,a}$. We then show that the number of model updates is bounded by $U_{\max}$ and apply the union bound.

<!-- chunk {"id": "body-0040", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

The following lemma bounds the number of episodes in which $\forall \kappa, \iota: \, |X_{k, \kappa, \iota}| \leq \kappa$ is violated with high probability.

<!-- chunk {"id": "body-0041", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

We first bound the total number of times a fixed pair $(s,a)$ can be observed while being in a particular category $X_{k, \kappa, \iota}$ in all phases $k$ for $1 \leq \kappa < |\statespace|$. We then show that for a particular $(\kappa,\iota)$, the number of episodes where $|X_{k, \kappa, \iota}| > \kappa$ is bounded with high probability, as the value of $\iota$ implies a minimum probability of observing each $(s,a)$ pair in $X_{k, \kappa, \iota}$ in an episode. Since the observations are not independent we use martingale concentration results to show the statement for a fixed $(\kappa,\iota)$. The desired result follows with the union bound over all relevant $\kappa$ and $\iota$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

The next lemma states that in episodes where the condition $\forall \kappa, \iota: \, |X_{k, \kappa, \iota}| \leq \kappa$ is satisfied and the true MDP is in the confidence set, the expected optimistic policy value is close to the true value. This lemma is the technically most involved part of the proof.

<!-- chunk {"id": "body-0043", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Using basic algebraic transformations, we show that $|p - \tilde p| \leq \sqrt{\tilde p (1 - \tilde p) } O\left(\sqrt{\frac{1}{n} \ln \frac 1 {\delta_1}} \right) + O\left(\frac{1}{n} \ln \frac 1 {\delta_1} \right)$ for each $\tilde p, p \in \mathcal P$ in the confidence set as defined in Eq.[eqn:conf\_set\_bern].

<!-- chunk {"id": "body-0044", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Since we assume $M \in \mathcal M_k$, we know that $p(s'|s,a)$ and $\tilde p(s' | s,a)$ satisfy this bound with $n(s,a)$ for all We use that to bound the difference of the expected value function of the successor state in $M$ and $\tilde M$, proving that $ | (P_i - \tilde P_i) \tilde V_{i+1:j}(s)| \leq O\left(\frac{C H}{n(s, \pi(s))} \ln \frac 1 {\delta_1} \right) + O\left(\sqrt{\frac{C}{n(s, \pi(s))} \ln \frac 1 {\delta_1}} \right)\tilde \sigma_{i:j}(s)$, where the local variance of the value function is defined as $ \sigma_{i:j}^2(s,a):= \mathbb

<!-- chunk {"id": "body-0045", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

The basic idea is to split the bound into a sum of two parts by partitioning of the $(s,a)$ space by knownness, e.g. that is $(s_t, a_t) \in \bar X_{\kappa, \iota}$ for all $\kappa$ and $\iota$ and $(s_t, a_t) \in \bar X$. Using the fact that $w(s_t, a_t)$ and $n(s_t, a_t)$ are tightly coupled for each $(\kappa, \iota)$, we can bound the expression eventually by $\epsilon$. The final key ingredient in the remainder of the proof is to bound $\sum\_{t=1}^{H} P\_{1:t-1} \sigma\_{t:H}(s)^2$ by $O(H^2)$ instead of the trivial bound $O(H^3)$. To this end, we show the lemma below.

<!-- chunk {"id": "body-0046", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

The proof works by induction and uses fact that the value function satisfies the Bellman equation and the tower-property of conditional expectations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

Proof Sketch for Theoremthm:upper\_bound.

<!-- chunk {"id": "body-0048", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

- The true MDP is in the set of MDPs $\mathcal M_k$ for all phases $k$ with probability at least $1- \frac{\delta}{2}$ (Lemma[lem:mdp\_capture]). - The algorithm computes a value function whose optimistic value is higher than the optimal reward in the true MDP with probability at least $1-\delta / 2$ (Lemma[lem:planning]). - The number of episodes with $|X_{k, \kappa, \iota}| > \kappa$ for some $\kappa$ and $\iota$ are bounded with probability at least $1 - \delta/2$ by $\tilde O(\left|\saspace\right| m)$ if $m = \tilde \Omega\left(\frac{H^2}{\epsilon} \ln \frac{|\statespace|}{\delta} \right)$ (Lemma[lem:unbalanced\_episodes\_bound]).

<!-- chunk {"id": "body-0049", "role": "body", "section": "PAC Analysis", "weight": 1.0} -->

- If $|X_{k, \kappa, \iota}| \leq \kappa$ for all $\kappa$, $\iota$, i.e., relevant state-action pairs are sufficiently known and $m = \tilde \Omega\left(\frac{C H^2}{\epsilon^2} \ln \frac{1}{\delta_1} \right)$, then the optimistic value computed is $\epsilon$-close to the true MDP value. Together with part 2, we get that with high probability, the policy $\pi^k$ is $\epsilon$-optimal in this case. - From parts3 and 4, with probability $1 - \delta$, there are at most $\tilde O \left(\frac{C \left|\saspace\right| H^2}{\epsilon^2} \ln \frac{1}{\delta}\right)$ episodes that are not $\epsilon$-optimal.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

every state/.style=minimum size=0pt confidence=None created_by=None text="\\begin{tikzpicture}[node distance=1.1cm,>=stealth',bend angle=60,auto,decoration={\n markings,\n mark=at position 0.5 with {\\arrow{>}}}]\n\n \\node [state] (s0) {$0$};\n \\node [state, right of=s0, node distance=3cm] (s2) {$2$};\n \\node [state, above of=s2] (s1) {$1$};\n \\node [below of=s2, node distance=.6cm] (dots) {$\\vdots$};\n \\node [state, below of=s2, node distance=1.4cm] (sn) {$n$};\n \\node [state, right of=s1, node distance=3cm] (sp) {$+$};\n \\node

<!-- chunk {"id": "body-0051", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

[state, right of=sn, node distance=3cm] (sm) {$-$};\n \\node [right of=sp, node distance=2cm] (rp) {$r(+) = 1$};\n \\node [right of=sm, node distance=2cm] (rm) {$r(-) = 0$};\n \\node [above of=s0, node distance=1.2cm, anchor=west] (p0) {$p(i | 0, a) = \\frac 1 n$};\n \\node [below of=rp, node distance=.7cm,] (pp) {$p(+ | i, a) = \\frac 1 2 + \\epsilon'_i(a)$};\n \\node [above of=rm, node distance=.7cm,] (pm) {$p(- | i, a) = \\frac 1 2 - \\epsilon'_i(a)$};\n\\path[->]

<!-- chunk {"id": "body-0052", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

\n(s0) edge (s1)\n(s0) edge (s2)\n(s0) edge (sn)\n(s1) edge (sp)\n(s1) edge (sm)\n(s2) edge (sp)\n(s2) edge (sm)\n(sn) edge (sp)\n(sn) edge (sm)\n(sp) [loop right, looseness=10] edge (sp)\n(sm) [loop right, looseness=10] edge (sm)\n;\n\\end{tikzpicture}" language=<CodeLanguageLabel.TIKZ: 'Tikz'> Class of a hard-to-learn finite horizon MDPs.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

The function $\epsilon'$ is defined as $\epsilon'(a_1) = \epsilon / 2$, $\epsilon'(a_i^*) = \epsilon$ and otherwise $\epsilon'(a) = 0$ where $a_i^*$ is an unknown action per state $i$ and $\epsilon$ is a There exist positive constants $c_1$, $c_2$, $\delta_0$, $\epsilon_0$ such that for every $\delta \in (0, \delta_0)$ and $\epsilon \in (0, \epsilon_0)$ and for every algorithm A that satisfies a PAC guarantee for $(\epsilon, \delta)$ and outputs a deterministic policy, there is a fixed-horizon episodic MDP $M_{hard}$ with \mathbb E[n_A] \geq & \frac{c_1 (H-2)^2 (|\actionspace|-1) (|\statespace| -3)}{\epsilon^2} \ln

<!-- chunk {"id": "body-0054", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

\left(\frac{c_2}{\delta + c_3 }\right) = \Omega\left(\frac{|\statespace \times \actionspace| H^2}{\epsilon^2} \ln \left(\frac{c_2}{\delta + c_3} \right)\right) where $n_A$ is the number of episodes until the algorithm's policy is $(\epsilon, \delta)$-accurate.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

The constants can be set to $ \delta_0 =\frac{ e^{-4}}{80} \approx \frac{1}{5000}$, $\epsilon_0 = \frac{H-2}{640 e^4} \approx H/35000$, The ranges of possible $\delta$ and $\epsilon$ are of similar order than in other state-of-the-art lower bounds for multi-armed bandits [Mannor2004] and discounted MDPs [Strehl2009, They are mostly determined by the bandit result by [Mannor2004] we build. Increasing the parameter limits $\delta_0$ and $\epsilon_0$ for bandits would immediately result in larger ranges in our lower bound, but this was not the focus of our analysis.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

The basic idea is to show that the class of MDPs shown in Figure[fig:finite\_hard\_mdp] require at least a number of observed episodes of the order of Equation[eqn:lower\_bound]. From the start state $0$, the agent ends up in states $1$ to $n$ with equal probability, independent of the action. From each such state $i$, the agent transitions to either a good state $+$ with reward $1$ or a bad state $-$ with reward $0$ and stays there for the rest of the episode. Therefore, each state $i=1, \dots, n$ is essentially a multi-armed bandit with binary rewards of either $0$ or $H-2$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

For each bandit, the probability of ending up in $+$ or $-$ is equal except for the first action $a_1$ with $p(s_{t+1} = +| s_t = i, a_t = a_1) = 1/2 + \epsilon / 2$ and possibly an unknown optimal action $a_i^*$ (different for each state $i$) with $p(s_{t+1} = +| s_t = i, a_t = In the episodic fixed-horizon setting we are considering, taking a suboptimal action in one of the bandits does not necessarily yield a suboptimal episode. We have to consider the average over all bandits instead. In an $\epsilon$-optimal episode, the agent therefore needs to follow a policy that would solve at least a certain portion of all $n$ multi-armed bandits with probability at least $1 - \delta$. We show that the best strategy for the agent to achieve this is to try to solve all bandits with equal probability.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

The number of samples required to do so then results in the lower bound in Equation[eqn:lower\_bound].

<!-- chunk {"id": "body-0059", "role": "body", "section": "Lower PAC Bound", "weight": 1.0} -->

Similar MDPs that essentially solve multiple of such multi-armed bandits have been used to prove lower sample-complexity bounds for discounted MDPs [Strehl2009,Lattimore2012]. However, the analysis in the infinite horizon case as well as for the sliding-window fixed-horizon optimality criterion considered by [Kakade2003] is significantly simpler. For these criteria, every time step the agent follows a policy that is not $\epsilon$-optimal counts as a "mistake". Therefore, every time the agent does not pick the optimal arm in any of the multi-armed bandits counts as a mistake. This contrasts with our fixed-horizon setting where we must instead consider taking an average over all bandits.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have shown upper and lower bounds on the sample complexity of episodic fixed-horizon RL that are tight up to log-factors in the time horizon $H$, the accuracy $\epsilon$, the number of actions $|\actionspace|$ and up to an additive constant in the failure probability $\delta$. These bounds improve upon existing results by a factor of at least $H$. One might hope to reduce the dependency of the upper bound on $|\statespace|$ to be linear by an analysis similar to Mormax [Szita2010] for discounted MDPs which has sample complexity linear in $|\statespace|$ at the penalty of additional dependencies on $H$. Our proposed \texttt{UCFH}\xspacealgorithm that achieves our PAC bound can be applied to directly to a wide range of fixed-horizon episodic MDPs with known rewards and does not require additional structure such as sparse or acyclic state transitions assumed in previous work. The empirical evaluation of \texttt{UCFH}\xspaceis an interesting direction for future work.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgments: We thank Tor Lattimore for the helpful suggestions and comments. We are also grateful to Shiau Hong Lim and Ian Osband for discovering small bugs in previous versions of this paper. This work was supported by an NSF CAREER award and the ONR Young

<!-- chunk {"id": "body-0062", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

We want to find a policy $\pi^k$ and optimistic ${\tilde M}_k \in \mathcal M_k$ which have the highest total reward $R^{\pi^k}_{{\tilde M}_k} = \max_{\pi, M' \in \mathcal M_k} R^{\pi}_{M'}$. Note that $\pi^k$ is an optimal policy for $M_k$ but not necessarily for $M$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

To facilitate planning, we relax this problem and instead compute a policy and optimistic MDP with $R^{\pi^k}_{{\tilde M}_k} = \max_{\pi, M' \in \mathcal M'_k} R^{\pi}_{M'}$ \mathcal M'_k:= \big\{ & \tilde{M} \in \mathcal M_{\textrm{nonst.}} \,: \, \forall (s,a) \in \statespace \times \actionspace, t =1\dots H, s' \in \succS{s,a}\\&{\tilde p}_{t}(s'|s,a) \in \operatorname{conv}(\confset{${\hat p}(s' |s,a), n(s, a)$}) \big\}.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

We only require the transition probabilities to be in the convex hull of the confidence sets instead of the confidence sets. Since this is a relaxation, we have $\mathcal M_k \subseteq \mathcal M'_k$. We can find such a policy by dynamic programming similar to extended value iteration [Strehl2008,AuerOrtner2005].

<!-- chunk {"id": "body-0065", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

The optimal Q-function can be and for $i=H-1, \dots,2, 1$ as \tilde Q_{i:H}^*(s,a) = & r_i(s) + \max_{\tilde p_i \in \mathcal P_{s,a}}\left\{\sum_{s' \in \succS{s, a}} \tilde p_i \max_{b \in \mathcal A} \tilde Q_{i+1:H}^*(s', b) \right\} The feasible set is defined as $\mathcal P_{s,a}:= \{ p \in ^{\numSucc{s,a}} \, | \, \| p \|_1 = 1, \forall s' \in \succS{s,a}: \, p(s') \in \operatorname{conv}(\confset(\hat The optimal policy $\pi^k_t(s)$ at time $t$ is then simply the

<!-- chunk {"id": "body-0066", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

maximizer of the inner $\max$ operator and the transition probability $\tilde p\_t(\cdot | s,a)$ is the maximizer of the outer maximum.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

The inner $\max$ can be solved efficiently by enumeration and the outer maximum similar to extended value The basic idea is to put as much probability mass as possible to successor states with highest value. See the following algorithm for the implementation details.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

\actionspace$$\tilde p\_t(s' | s,a):= \min \confset(\hat p(s' | s,a), n(s,a)) \quad \forall s' \in \succS{s,a}$ $\Delta:= 1 - \sum_{s' \in \succS{s,a}} \tilde p_t(s' | s,a)$ $\Delta':= \min\{ \Delta, \max \confset(\hat p(s' | s,a), n(s,a)) - \tilde p_t(s' | s,a)\}$ $\tilde p_t(s' | s,a):= \tilde p_t(s' | s,a) + \Delta'$ $\Delta:= \Delta - \Delta'; i:= i + 1$ $\tilde Q^*_{t:H}(s,a) = \sum_{s' \in

<!-- chunk {"id": "body-0069", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

\succS{s,a}} \tilde p_t(s' | s, a) \tilde Q_{t+1:H}^*(s', \pi_{t+1}(s'))$ $\pi_{1}(s):= \argmax_{a \in \mathcal A} \tilde Q^*_{1:H}(s, a) \quad \forall s \in \mathcal S$ MDP with transition probabilities $\tilde p_t$, optimal policy $\pi$ Note that due to the nonlinear constraint in Equation [eqn:conf_set_var], $\confset(\hat p(s' | s,a), n(s,a))$ may be the union of two disjoint intervals instead of one interval.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

Still, $\min$- and $\max$-operations on the confidence sets can be computed readily in constant time. Therefore, the transition probabilities $\tilde p_t(\cdot | s, a)$ for a single time step $t$ and state-action pair $s,a$ can be computed in $O(|\statespace| |\actionspace| C)$ given sorted states. Sorting the states takes $O(|\statespace| \log |\statespace|)$ which results in $O(H |\statespace| \log |\statespace| + H |\statespace| |\actionspace| C)$ runtime complexity of (see comments in Function[alg:evi]). The Algorithm requires $O(H |\statespace| |\actionspace| C)$ additional space besides the storage requirements of the input MDP $\mathcal M$ as the transition probabilities $\tilde p_t$ are returned by the algorithm.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

If those are not required and only the optimal policy is of interest, the additional space can be reduced to $O(|\statespace| |\actionspace|)$. $\mathcal M_k$ returns $\tilde M, \pi^k = \argmax_{M \in \mathcal M'_k, \pi} R^\pi_M$. Since $\mathcal M_k \subseteq \mathcal M'_k$, it also holds that $R^{\pi^k}_{\tilde M} \geq \max_{M \in \mathcal M_k, \pi} R^\pi_M$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fixed-Horizon Extended Value Iteration", "weight": 1.0} -->

This result can be proved straight-forwardly by showing that $\pi^k$ is optimal in the last time step $H$ with highest possible reward and then subsequently for all previous time steps inductively. It follows directly from the definition of the algorithm in Function[alg:evi] that the returned MDP is in $\mathcal M_k'$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Runtime- and Space-Complexity of \\texttt{UCFH}\\xspace", "weight": 1.0} -->

Sampling one episode and updating the respective $v$ variables has $O(H)$ runtime. Theorem[thm:upper\_bound] states that after at most O\left(\frac{H^2 C| \statespace \times \actionspace|}{\epsilon^2} \ln \frac{1}{\delta}\right)$ observed episodes, the current policy is $\epsilon$-optimal with sufficiently high probability. This results in a total runtime for sampling of O\left(\frac{H^3 C| \statespace \times \actionspace|}{\epsilon^2} \ln \frac{1}{\delta}\right)$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Runtime- and Space-Complexity of \\texttt{UCFH}\\xspace", "weight": 1.0} -->

Each update of the policy involves updating the $n$ variables and $\mathcal M_k$ which takes runtime $O(C)$ and a call of with runtime cost $O(H |\statespace| |\actionspace| C + H |\statespace| \log |\statespace|)$. From Lemma[lem:num\_total\_updates] below, we know that the policy can be updated at most $U_{\max}$ times which a gives total runtime for policy updates of O(U_{\max} H |\statespace| (|\actionspace| C + \log |\statespace|)) =& O \left(H |\statespace|^2 |\actionspace| (|\actionspace| C + \log |\statespace|) \log \frac{|\statespace|^2 H^2}{\epsilon}\right)\\=& \tilde O \left(H |\statespace|^2 |\actionspace|^2 C \log \frac{1}{ \epsilon} \right).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Runtime- and Space-Complexity of \\texttt{UCFH}\\xspace", "weight": 1.0} -->

The total runtime of \texttt{UCFH}\xspacebefore the policy is $\epsilon$-optimal with probability at least $1- \delta$ is therefore \tilde O \left(\frac{H^3 |\statespace|^2 |\actionspace|^2 C}{\epsilon^2} \ln \frac{1}{ \delta} \right).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Runtime- and Space-Complexity of \\texttt{UCFH}\\xspace", "weight": 1.0} -->

The space complexity of \texttt{UCFH}\xspaceis dominated by the requirement to store statistics for each possible transition which gives $O(|\statespace| |\actionspace| C)$complexity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Bound on the Number of Policy Changes of \\texttt{UCFH}\\xspace", "weight": 1.0} -->

First note that $n(s,a)$ is never never decreasing and no updates happen once $n(s,a) \geq |\statespace| m H$ for all $(s,a)$. In each update, the $n(s,a)$ of exactly one $(s,a)$ pair increases by $\max\{ m w_{\min}, n(s,a)\}$. For a single $(s,a)$ pair, such updates can happen only $\log_2(|\statespace| m H) - \log_2(m w_{\min})$ times. Hence, there are at most $| \mathcal S \times \mathcal A| \log_2 \frac{|\statespace| m H}{w_{\min} m}$ updates in total.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

Before presenting the proof of Lemma[lem:unbalanced\_episodes\_bound] which bounds the total number of episodes where there is a $\kappa$ and $\iota$ such that $\kappa > |X_{k, \kappa, \iota}|$, we establish a bound for each individual $\kappa$ and $\iota$ in the following two additional lemmas.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

The total number of observations of $(s,a) \in X_{k, \kappa, \iota}$ where $\kappa \in [1, |\statespace| -1]$ and $\iota > 0$ over all phases $k$ is at most $3 | \statespace \times \actionspace| m w_\iota \kappa$. The variable $w_\iota$ is the smallest possible weight of a $(s,a)$-pair that has importance $\iota$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

We denote the smallest possible weight for any $(s,a)$ pair such that $\iota(s,a) = \iota$ by $w_\iota:= \min\{ w(s,a): \iota_k(s,a) = \iota \}$. Note that $w_{\iota+1} = 2 w_\iota$ for $\iota > 0$. Consider any phase $k$ and fix $(s,a) \in X_{k, \kappa, \iota}$ with $\iota > 0$. $\iota_k(s,a) = \iota > 0$, we have $w_\iota \leq w_k(s,a) < 2w_{\iota}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

From $\kappa_k(s,a) = \kappa$, it follows that \frac{n_k(s,a)}{2 m w_k(s,a)} \leq \kappa \leq \frac{n_k(s,a)}{m w_k(s,a)} which implies that m w_{\iota}\kappa \leq m w_k(s,a) \kappa \leq n_k(s,a) \leq 2 m w_k(s,a) \kappa \leq 4 m w_{\iota} \kappa.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

Hence, each state can only be observed $3 m w_\iota$ times while being in $\{(s,a) \in X_{k, \kappa, \iota}\,: \, k \in \mathbb N \}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

The number of episodes $E_{\kappa, \iota}$ in phases with $|X_{k, \kappa, \iota}| > \kappa$ is bounded for every $\alpha \geq 3$ with high probability, $$P(E_{\kappa, \iota} > \alpha N) \leq \exp\left(- \frac{\beta w_\iota (\kappa + 1) N}{H} \right)$$ where $N = |\statespace \times \actionspace|m$ and $\beta = \frac{\alpha (3 / \alpha - 1)^2}{7/3 - 1 / \alpha}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

We are now ready to prove Lemma[lem:unbalanced\_episodes\_bound] by combining the bound in the previous lemma for all $\kappa$ and $\iota$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

|\statespace \times \actionspace|}{4 H^2 |\statespace|} \right) Bounding the right hand-side by $1 - \delta / 2$ and solving for $m$ gives 1 - E_{\max} \exp\left(- \frac{\beta \epsilon m |\statespace \times \actionspace|}{4 H^2 |\statespace|} \right) \geq & 1 - \delta / 2\quad \Leftrightarrow \quad m \geq \frac{4 H^2 |\statespace|}{ |\statespace \times \actionspace| \beta \epsilon} \ln \frac{2 E_{\max}}{\delta} Hence, the condition m \geq \frac{4 H^2}{ \beta \epsilon} \ln \frac{2 E_{\max}}{\delta} is sufficient for the desired result to hold.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Bounding the number of episodes with $\\kappa > |X_{k, \\kappa, \\iota}|$ for some $\\kappa, \\iota$", "weight": 1.0} -->

By plugging in $\alpha = 6$ and $\beta = \frac{\alpha (3 / \alpha - 1)^2}{7/3 - 1 / \alpha} = \frac{9}{13} \geq \frac{2}{3}$, we obtain the statement to show.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

[lem:balanced\_eps\_good], it is sufficient to consider a fixed phase $k$. To avoid notational clutter, we therefore omit the phase indices $k$in this section.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

For the proof, we reason about a sequence of MDPs $M_d$ which have the same transition probabilities but different reward functions $r^{(d)}$. For $d=0$, the reward function is the original reward function $r$ of $M$, i.e. $r^{}_t = r_t$ for all $t=1 \dots H$. The following reward functions are then defined recursively as $r^{(2d+2)}_t = \sigma_{t:H}^{(d), 2}$, where $\sigma_{t:H}^{(d), 2}$ is the local variance of the value function w.r.t. the rewards $r^{(d)}$. Note that for every $d$ and $t =1\dots H$ and $s \in \mathcal S$, we have $r_t^{(d)}(s) \in [0, H^d]$. In complete analogy, we define $\tilde M_d$ and $\hat M_d$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

We first prove a sequence of lemmas necessary for Lemma [lem:balanced\_eps\_good].

<!-- chunk {"id": "body-0090", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

Note that the last condition of $\mathcal P_1$ is equivalent to $ \sqrt{\hat p (1 - \hat p)} \leq \sqrt{p' (1-p')} + \sqrt{\frac{2 \ln(6 / \delta_1)}{n-1}} $ as $p' \in $. As an intersection of a polytope and the superlevel set of a concave function $p' (1 - p')$, the set $\mathcal P_1$ is convex. Hence $\operatorname{conv}(\mathcal P) = \operatorname{conv}(\mathcal P_1 \cap \mathcal P_2) \subseteq \operatorname{conv}(\mathcal P_1) = \mathcal P_1$. It therefore follows that $\tilde p \in \mathcal P_1$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

Then |(P_i - \tilde P_i) \tilde V_{i+1:j}(s)| \leq c_1(s,a) \numSucc{s,a} \| \tilde V_{i+1:j} \|_\infty + c_2(s,a) \sqrt{\numSucc{s,a}} \tilde \sigma_{i:j}(s) for any $(s,a) \in \statespace \times \actionspace$ where $\succS{s,a}$ denotes the set of possible successor states of state $s$ and action $a$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

Let $s$ and $a= \pi_i(s)$ be fixed and define for this fixed $s$ the constant function $\bar V(s') = \tilde P_i \tilde V_{i+1:j}(s)$ [sic] as the expected value function of the successor states of $s$. Note that $\bar V(s')$ is a constant function and so $\bar V = \tilde P_i \bar V = P_i \bar V$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

\sigma_{i:j}(s) In Inequality[eqn:sigma\_bound\_trang], we wrote out the definition of $P_i$ and $\tilde P_i$ and applied the triangle inequality.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Bound on the value function difference for episodes with $\\forall \\kappa, \\iota: \\, |X_{k, \\kappa, \\iota}| \\leq \\kappa$", "weight": 1.0} -->

We then applied the assumed bound and bounded $|\tilde V_{i+1:j}(s') - \bar V(s')|$ by $\| V_{i+1:j} \|_\infty$ as all value functions are nonnegative. In Inequality[eqn:sigma\_bound\_cs], we applied the Cauchy-Schwarz inequality and subsequently used the fact that each term is the sum is nonnegative and that $(1 - \tilde p_i(s'| s,a)) \leq 1$. The final equality follows from the definition of $\tilde \sigma_{i:j}$.
