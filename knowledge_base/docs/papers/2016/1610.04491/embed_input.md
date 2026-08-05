<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The End of Optimism? An Asymptotic Analysis of Finite-Armed Linear Bandits

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic linear bandits are a natural and simple generalisation of finite-armed bandits with numerous practical applications. Current approaches focus on generalising existing techniques for finite-armed bandits, notably the optimism principle and Thompson sampling. While prior work has mostly been in the worst-case setting, we analyse the asymptotic instance-dependent regret and show matching upper and lower bounds on what is achievable. Surprisingly, our results show that no algorithm based on optimism or Thompson sampling will ever achieve the optimal rate, and indeed, can be arbitrarily far from optimal, even in very simple cases. This is a disturbing result because these techniques are standard tools that are widely used for sequential optimisation. For example, for generalised linear bandits and reinforcement learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The linear bandit is the simplest generalisation of the finite-armed bandit. $\mathcal A \subset \mathbb R^d$ be a finite set that spans $\mathbb R^d$ with $|\mathcal A| = k$ and $\norm{x}_2 \leq 1$ for all $x \in \cA$. A learner interacts with the bandit over $n$ rounds. In each round $t$ the learner chooses an action (arm) $A_t \in \mathcal A$ and observes a payoff $Y_t = \inner{A_t, \theta} + \eta_t$ where $\eta_t \sim \mathcal N$ is Gaussian noise and $\theta \in \mathbb R^d$ is an unknown parameter. The optimal action is $x^* = \operatornamewithlimits{arg\,max}_{x \in \mathcal A} \inner{x, \theta}$, which is not known since it depends on $\theta$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The assumption that $\cA$ spans $\mathbb R^d$ is non-restrictive, since if $\operatorname{span}(\cA)$ has rank $r < d$, then one can simply use a different basis for which all but $r$ coordinates are always zero and then drop them from the analysis. The Gaussian assumption can be relaxed to $1$-subgaussian for our upper bound, but is needed for the lower bound. Our performance measure is the expected pseudo-regret (from now on just the regret), which is given by where the expectation is taken with respect to the actions of the strategy and the noise. There are a number of algorithms designed for minimising the regret, all of which use one of two algorithmic designs. The first is the principle of optimism in the face of uncertainty, which was originally applied to finite-armed bandits and many others, and more recently to linear bandits. The second algorithm design is Thompson sampling, which is an old algorithm that has experienced a resurgence in popularity because of its impressive practical performance and theoretical guarantees for finite-armed bandits. Thompson sampling has also recently been applied to linear bandits with good empirical performance and near-minimax theoretical guarantees.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

While both approaches lead to practical algorithms (especially Thompson sampling), we will show they are fundamentally flawed in that algorithms based on these ideas cannot be close to asymptotically optimal. Along the way we characterise the optimal achievable asymptotic regret and design a strategy achieving it.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This is an important message because optimism and Thompson sampling are widely used beyond the finite-armed case. Examples include generalised linear bandits, spectral bandits, and even learning in Markov decision processes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The disadvantages of these approaches is obscured in the worst-case regime, where both are quite close to optimal. One might question whether or not the asymptotic analysis is relevant in practice. The gold standard would be instance-dependent finite-time guarantees like what is available for finite-armed bandits, but historically the asymptotic analysis has served as a useful guide towards understanding the trade-offs in finite-time. Besides hiding the structure of specific problems, pushing for optimality in the worst-case regime can also lead to sub-optimal instance-dependent guarantees. For example, the MOSS algorithm for finite-armed bandits is minimax optimal, but far from finite-time optimal. For these reasons we believe that understanding the asymptotics of a problem is a useful first step towards optimal finite-time instance-dependent guarantees that are most desirable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

It is worth mentioning that partial monitoring (a more complicated online learning setting) is a well known example of the failure of optimism Although related, the partial monitoring framework is more general than the bandit setting because the learner may not observe the reward even for the action they take, which means that additional exploration is usually necessary in order to gain information. Basic results in partial monitoring are concerned with characterizing whether an instance is easier or harder than bandit instances. More recently, the question of asymptotic instance optimality was studied in finite stochastic partial monitoring, and the special setting of learning with side information. While the algorithms derived in these works served as inspiration, the analysis and the algorithms do not generalise in a simple direct fashion to the linear setting, which requires a careful study of how information is transferred between actions in a linear setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

We note first that the finite-armed UCB algorithm of can be used on this problem by disregarding the structure on the arms to achieve an This quantity depends linearlyon the number of suboptimal arms, which may be very large (much larger than the dimension) and is very undesirable. Nevertheless we immediately observe that the asymptotic regret should be logarithmic. The following theorem and its corollary characterises the optimal asymptotic regret.

<!-- chunk {"id": "body-0010", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

Fix $\theta\in \mathbb R^d$ such that there is a unique optimal arm. Let $\pi$ be a consistent policy and let which we assume is invertible for sufficiently large $n$. Then for all suboptimal $x \in \mathcal A$ it holds that The astute reader may recognize $\norm{x-x^*}_{\bar G_n^{-1}}$ as the leading factor in the width of the confidence interval for estimating the gap $\Delta_x$ using a linear least squares estimator. The result says that this width has to shrink at least logarithmically with a specific constant. Before the proof of Theorem [thm:lower] we present a trivial corollary and some consequences. The assumption that $\bar G_n$ is eventually invertible can be relaxed. In fact, if $\bar G_n$ is not eventually invertible, then the algorithm must suffer linear regret on some problem. This is quite natural because a singular $\bar G_n$ implies the algorithm has not explored at all in some direction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

The proof of this fact may be found in Appendix [app:singular]. the supplementary material.

<!-- chunk {"id": "body-0012", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

Let $\pi$ be a consistent policy, $\theta\in \mathbb R^d$ such that there is a unique optimal arm in $\cA$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

As with the previous result, in[eq:confwidth] the reader may recognize the leading term of the confidence width for estimating the mean reward of $x$. Unsurprisingly, the width of this confidence interval has to shrink at least as fast as the width of the confidence interval for estimating the gap $\Delta_x$. The intuition underlying the optimisation problem[eq:optproblem] is that no consistent strategy can escape allocating samples so that the gaps of all suboptimal actions are identified with high confidence, while a good strategy will also minimise the regret subject to the identifiability condition. The proof of Corollary [cor:regretlb] is given in Appendix [app:cor:regretlb]. the supplementary material. [Finite armed bandits] Suppose $k = d$ and $\mathcal A = \set{e_1,\ldots,e_k}$ be the standard basis vectors. which recovers the lower bound.

<!-- chunk {"id": "body-0014", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

Let $\alpha >1$ and $d = 2$ and $\cA = \set{x_1, x_2, x_3}$ with $x_1 = $ and $x_2 = $ and $x_3 = (1-\epsilon, \alpha \epsilon)$ and $\theta = $. Then $c(\mathcal A, \theta) = 2\alpha^2$ for all sufficiently small $\epsilon$. The example serves to illustrate the interesting fact that $c(\mathcal A - \set{x_2}, \theta) = 2\epsilon^{-1} \gg c(\cA, \theta)$, which means that the problem becomes significantly harder if $x_2$ is removed from the action-set. The reason is that $x_1$ and $x_3$ are pointing in nearly the same direction, so learning the difference is very challenging. But determining which of $x_1$ and $x_3$ is optimal is easy by playing $x_2$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

So we see that in linear bandits there is a complicated trade-off between information and regret that makes the structure of the optimal strategy more interesting than in the finite setting.

<!-- chunk {"id": "body-0016", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

The closest prior work to our lower bound is by and [:pmon]. The latter consider stochastic partial monitoring when the reward is part of the observation. In this setting in each round, the learner selects one of finitely many actions and receives an observation from a distribution that depends on the action chosen and an unknown parameter, but is otherwise known. While this model could cover our setting, the results in the paper are developed only for the case when the unknown parameter belongs to a finite set, an assumption that all the results of the paper heavily depend. on the other hand restricts partial monitoring to the case when the observations belong to a finite set, while the parameter belongs to the unit simplex. While this problem also has a linear structure, their results do not generalize beyond the discrete

<!-- chunk {"id": "body-0017", "role": "body", "section": "CONCENTRATION", "weight": 1.0} -->

Before introducing the new algorithm we analyse the concentration properties of the least squares estimator. Our results refine the existing guarantees, and are necessary in order to obtain asymptotic optimality. Let $G_t$ be the Gram matrix after round $t$ defined by $G_t = \sum_{s \leq t} A_s A_s^\top$ and $\hat \theta(t) = G_t^{-1} \sum_{s=1}^t A_s Y_s$ be the empirical (least squares) estimate, where $A_s$ is selected based on $A_1,Y_1,\dots,A_{s-1},Y_{s-1}$ and $Y_s = \ip{A_s,\theta} + \eta_s$, $\eta_s\sim N$. [size=,color=blue!20!white,#1]Csaba: #2This is not super precise. We will only use $\hat \theta(t)$ for rounds $t$ when $G_t$ is invertible.

<!-- chunk {"id": "body-0018", "role": "body", "section": "CONCENTRATION", "weight": 1.0} -->

The empirical estimate of the sub-optimal gaps is $\hat \Delta_x(t) = \max_{y \in \mathcal A} \hat \mu_y(t) - \hat \mu_x(t)$, where $\hat \mu_x(t) = \shortinner{x, \hat \theta(t)}$. We will also use the notation $\hat \mu(t)$ and $\hat \Delta(t) \in \mathbb R^k$for vectors of empirical means and sub-optimality gaps (indexed by the arms).

<!-- chunk {"id": "body-0019", "role": "body", "section": "CONCENTRATION", "weight": 1.0} -->

For any $\delta\in [1/n,1)$, $n$ sufficiently large and $t_0\in \mathbb N$ such that $G_{t_0}$ is almost surely non-singular, where for some $c>0$ universal constant The result improves on the elegant concentration guarantee of because asymptotically we have $f_{n,1/n} \sim 2 \log(n)$, while there it was $2d \log(n)$. Note that the restriction on $\delta$ may be relaxed with a small additional argument. The proof of Theorem [thm:conc] relies on a peeling argument and is given in Appendix [app:conc]. the supplementary material.

<!-- chunk {"id": "body-0020", "role": "body", "section": "CONCENTRATION", "weight": 1.0} -->

For the remainder we abbreviate $f_n = f_{n,1/n}$ and $g_n = f_{n,1/\log(n)}$, which are chosen so that \begin{align}eq:conc-cor P (t t\_0,x: |\_x(t) - \_x| x\_G\_t^-1^2 f\_n) 1 n,

<!-- chunk {"id": "body-0021", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

A barycentric spanner of the action space is a set $B = \set{x_1,\ldots,x_d} \subseteq A$ such that for any $x \in \cA$ there exists an $\alpha \in ^d$ with $x = \sum_{i=1}^d \alpha_i x_i$. The existence of a barycentric spanner is guaranteed because $\cA$ is finite and spans $\mathbb R^d$. We propose a simple strategy that operates in three phases called the warm-up phase, the success phase and the recoveryphase. In the warm-up the algorithm deterministically chooses its actions from a barycentric spanner to obtain a rough estimate of the sub-optimality gaps. The algorithm then uses the estimated gaps as a substitute for the true gaps to determine the optimal pull counts for each action, and starts implementing this strategy. Finally, if an anomaly is detected that indicates the inaccuracy of the estimated gaps then the algorithm switches to the recovery phase where it simply plays UCB.

<!-- chunk {"id": "body-0022", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

Input: $\mathcal A$ and $n$ Find a barycentric spanner: $B = \set{x_1,\ldots,x_d}$ Choose each arm in $B$ exactly $\lceil\log^{1/2}(n)\rceil$ times $\displaystyle \epsilon_n \leftarrow \max_{x \in \mathcal A} \norm{x}_{G_{n}^{-1}} g_n^{1/2}$, $t \leftarrow n+1$ $\hat \Delta \leftarrow \hat \Delta(t-1)$ and $\hat T \leftarrow T_n(\hat \Delta)$ and $\hat \mu \leftarrow \hat \mu(t-1)$ $t \le n$ and $\shortnorm{\hat \mu - \hat \mu(t-1)}_\infty \leq 2\epsilon_n$ Play actions $x$ with $T_x(t) \leq \hat T_x$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

$t\leftarrow t+1$ Discard all data and play UCB until $t = n$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

Assuming that $x^*$ is unique, the strategy given in Algorithm [alg:optimal] satisfies

<!-- chunk {"id": "body-0025", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

We now argue that algorithms based on optimism or Thompson sampling cannot be close to asymptotically optimal. $t$ an optimistic algorithm constructs a confidence set $\cC_t \subseteq \mathbb R^d$ and chooses $A_t$ according to $A_t = \operatornamewithlimits{arg\,max}_{x \in \mathcal A} \max_{\tilde \theta \in \cC_t} \shortinner{x, \tilde \theta}$. In order to proceed we need to make some assumptions on $\cC_t$, otherwise one can define a confidence set to ensure any behaviour at all. First of all, we will assume that $\P{\exists t \leq n: \theta \notin \cC_t} = O(1/n)$. That is, that the probability that the true parameter is ever outside the confidence set is not too large.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

Second, we assume that $\cC_t \subseteq \cE_t$ where $\cE_t$ is the ellipsoid about the least squares estimator given by where $\alpha$ is some constant and $\hat \theta(t)$ is the empirical estimate of $\theta$ based on the observations so far. Existing algorithms based on confidence all use such confidence sets. Standard wisdom when designing optimistic algorithms is to use the smallest confidence set possible, so an alternative algorithm that used a different form of confidence set would normally be advised to use the intersection $\cC_t \cap \cE_t$, which remains valid with high probability by a union bound. If the optimistic algorithm is not consistent, then its regret is not logarithmic on some problem and so diverges relative to the optimal strategy. Suppose now that the algorithm is consistent. Then we design a bandit on which its asymptotic regret is worse than optimal by an arbitrarily large constant factor. $d = 2$ and $e_1 = $ and $e_2 = $ be the standard basis vectors.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

The counter-example (illustrated in Figure [fig:example]) is very simple with $\mathcal A = \set{e_1, e_2, x}$ where $x = (1 - \epsilon, 8\alpha \epsilon)$. The true parameter is given by $\theta = e_1$, which means that $x^* = e_1$ and $\Delta_{e_2} = 1$ and $\Delta_x = \epsilon$. Suppose a consistent optimistic algorithm has chosen $T_{e_2}(t-1) \geq 4\alpha \log(n)$ and that $\theta \in C_t$. Then, But because $\theta \in C_t$, the optimistic value of the optimal action is at least $\shortinner{e_1, \theta} = 1$, which means that $A_t \neq e_2$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

We conclude that if $\theta \in C_t$ for all rounds, then the optimistic algorithm satisfies $T_{e_2}(t-1) \leq 1 + 4\alpha \log(n)$. By the assumption that $\theta \in C_t$ with probability at least $1 - 1/n$ we bound $\mathbb E[T_{e_2}(n)] \leq 2 + 4\alpha \log(n)$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

By consistency of the optimistic algorithm and our lower bound (Theorem [thm:lower]) we have Therefore by choosing $\epsilon$ sufficiently small we conclude that $\limsup_{n\to\infty} \mathbb E[T_x(n)] / \log(n) = \Omega(1/\epsilon^2)$ and so the asymptotic regret of the optimistic algorithm is at least However, for small $\epsilon$ the optimal regret for this problem is $c(\mathcal A, \theta) = 128 \alpha^2$ and so by choosing $\epsilon \ll \alpha$ we can see that the optimistic approach is sub-optimal by an arbitrarily large constant factor. The intuition is that the optimistic algorithms very quickly learn that $e_2$ is a sub-optimal arm and stop playing it. But as it turns out, the information gained by choosing $e_2$is sufficiently valuable that an optimal algorithm should use it for exploration.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[scale=0.4]\n\\draw[->] --;\n\\draw[->] --;\n\\draw[->] -- (5.4, 1.2);\n\\draw[densely dotted] -- (5.4, 1.2);\n\\draw[densely dotted] (5.4,1.2) --;\n\\draw[densely dotted] (5.4,1.2) -- (5.4,0);\n\\draw[densely dotted,->] (5.7,0.6) -- (7.7,1.6);\n\\node at (5.85, -0.4) {\\scriptsize $\\epsilon$};\n\\node[xshift=0.5cm,yshift=0.4cm] at (5.4,1.2) {\\scriptsize $(1-\\epsilon,

<!-- chunk {"id": "body-0031", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

2\\epsilon)$};\n\\node[xshift=0.5cm] at {\\scriptsize $$};\n\\node[yshift=0.3cm] at (0.3, 6) {\\scriptsize $$};\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Thompson sampling has also been proposed for the linear bandit problem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

The standard approach uses a nearly flat Gaussian prior (and so posterior), which means that essentially the algorithm operates by sampling $\theta_t$ from $\mathcal N(\hat \mu(t), \alpha G_t^{-1})$ and choosing the arm $A_t = \operatornamewithlimits{arg\,max}_{x \in \mathcal A} \shortinner{x, \theta_t}$. Why does this approach fail? By the assumption of consistency we expect that the optimal arm will be played all but logarithmically often, which means that the posterior will concentrate quickly about the value of the optimal action so that $\shortinner{x^*, \theta_t} \approx \mu^*$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

Then using the same counter-example as for the optimistic algorithm we see that the likelihood that $\shortinner{e_2 - e_1, \theta_t} \geq 0$ is vanishingly small once $T_{e_2}(t-1) = \Omega(\alpha \log(n))$ and so Thompson sampling will also fail to sample action $e_2$sufficiently often.

<!-- chunk {"id": "body-0034", "role": "body", "section": "SUMMARY", "weight": 1.0} -->

We characterised the optimal asymptotic regret for linear bandits with Gaussian noise and finitely many actions in the sense of The results highlight a surprising fact that all reasonable algorithms based on optimism can be arbitrarily worse than optimal. While this behaviour has been observed before in more complicated settings (notably, partial monitoring), our results are the first to illustrate this issue in a setting only barely more complicated than finite-armed bandits. Besides this we improve the self-normalised concentration guarantees by a factor of $d$asymptotically.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SUMMARY", "weight": 1.0} -->

As usual, we open more questions than we answer. While the proposed strategy is asymptotically optimal, it is also extraordinarily naive and the analysis is far from showing finite-time optimality. For this reason we think the most pressing task is to develop efficient and practical algorithms that exploit the available information in a way that Thompson sampling and optimism do not. There are two natural research directions towards this goal. The first is to push the optimisation approach used here and also, but applied more smoothly without discarding data or long phases. The second is to generalise information-theoretic ideas used (for instance) or.
