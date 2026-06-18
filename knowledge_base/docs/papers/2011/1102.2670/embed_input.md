<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit Problems

Topics include Online least squares, Self-normalized processes, Linear bandits, Confidence sets, UCB algorithms, Vector martingales, Regret bounds.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a self-normalized martingale tail bound for adaptive least-squares estimation and uses it to build tighter high-probability confidence sets. Those confidence sets feed directly into improved UCB-style analyses for stochastic and linear bandits, making the paper a core technical source for optimism-based sequential decision algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The analysis of online least squares estimation is at the heart of many stochastic sequential decision making problems. We employ tools from the self-normalized processes to provide a simple and self-contained proof of a tail bound of a vector-valued martingale. We use the bound to construct a new tighter confidence sets for the least squares estimate. We apply the confidence sets to several online decision problems, such as the multi-armed and the linearly parametrized bandit problems. The confidence sets are potentially applicable to other problems such as sleeping bandits, generalized linear bandits, and other linear control problems. We improve the regret bound of the Upper Confidence Bound (UCB) algorithm of Auer et al. and show that its regret is with high-probability a problem dependent constant. In the case of linear bandits, we improve the problem dependent bound in the dimension and number of time steps. Furthermore, as opposed to the previous result, we prove that our bound holds for small sample sizes, and at the same time the worst case bound is improved by a logarithmic factor and the constant is improved.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The least squares method forms a cornerstone of statistics and machine learning. It is used as the main component of many stochastic sequential decision problems, such as multi-armed bandit, linear bandits, and other linear control problems. However, the analysis of least squares in these online settings is non-trivial because of the correlations between data points. Fortunately, there is a connection between online least squares estimation and the area of self-normalized processes. Study of self-normalized processes has a long history that goes back to Student and is treated in detail in recent book by de la Peña et al.. Using these tools we provide a proof of a bound on the deviation for vector-valued martingales. A less general version of the bound can be found already in de la Peña et al.. Additionally our proof, based on the method of mixtures, is new, simpler and self-contained. The bound improves the previous bound of Rusmevichientong and Tsitsiklis and it is applicable to virtually any online least squares problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The bound that we derive, gives immediately rise to tight confidence sets for the online least squares estimate that can replace the confidence sets in existing algorithms. In particular, the confidence sets can be used in the UCB algorithm for the multi-armed bandit problem, the ConfidenceBall algorithm of Dani et al. for the linear bandit problem, and LinRel algorithm of Auer for the associative reinforcement learning problem. We show that this leads to improved performance of these algorithms. Our hope is that the new confidence sets can be used to improve the performance of other similar linear decision problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The multi-armed bandit problem, introduced by Robbins, is a game between the learner and the environment. At each time step, the learner chooses one of $K$ actions and receives a reward which is generated independently at random from a fixed distribution associated with the chosen arm. The objective of the learner is to maximize his total reward. The performance of the learner is evaluated by the regret, which is defined as the difference between his total reward and the total reward of the best action. Lai and Robbins prove a ${({{\sum_{i \neq i_{\ast}}{{1/D}{(p_{j},p_{i_{\ast}})}}} - {o{}}})}{\log T}$ lower bound on the expected regret of any algorithm, where $T$ is the number of time steps, $p_{i_{\ast}}$ and $p_{i}$ are the reward distributions of the optimal arm and arm $i$ respectively, and $D$ is the KL-divergence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Auer et al. designed the UCB algorithm and proved a finite-time logarithmic bound on its regret. He used Hoeffding's inequality to construct confidence intervals and obtained a $O{({{({K{\log T}})}/\Delta})}$ bound on the expected regret, where $\Delta$ is the difference between the expected rewards of the best and the second best action.color=red, \]Cite high-probability bound for UCB by Bubeck. We modify UCB so that it uses our new confidence sets and we show a stronger result. Namely, we show that with probability $1 - \delta$, the regret of the modified algorithm is $O{({{K{\log{({1/\delta})}}}/\Delta})}$. Seemingly, this result contradicts the lower bound of Lai and Robbins, however our algorithm depends on $\delta$ which it receives as an input. The expected regret of the modified algorithm with $\delta = {1/T}$ matches the regret of the original algorithm.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the linear bandit problem, the learner chooses repeatedly actions from a fixed subset of ${\mathbb{R}}^{d}$ and receives a random reward, expectation of which is a linear function of the action. Dani et al. proposed the ConfidenceBall algorithm and showed that its regret is at most $O{({d{\log{(T)}}\sqrt{T{\log{({T/\delta})}}}})}$ with probability at most $1 - \delta$. We modify their algorithm so that it uses our new confidence sets and we show that its regret is at most $O{({{d{\log{(T)}}\sqrt{T}} + \sqrt{dT{\log{({T/\delta})}}}})}$. Additionally, constants in our bound are smaller, and our bound holds for all $T \geq 1$, as opposed the previous one which holds only for sufficiently large $T$. Dani et al. prove also a problem dependent regret bound.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Vector-Valued Martingale Tail Inequalities", "weight": 1.0} -->

Let $({{\mathcal{F}_{k};k} \geq 0})$ be a filtration, $({{m_{k};k} \geq 0})$ be an ^d^-valued stochastic process adapted to $(\mathcal{F}_{k})$, $({{\eta_{k};k} \geq 1})$ be a real-valued martingale difference process adapted to $(\mathcal{F}_{k})$. Assume that $\eta_{k}$ is conditionally sub-Gaussian in the sense that there exists some $R > 0$ such that for any $\gamma \in$, $k \geq 1$,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Vector-Valued Martingale Tail Inequalities", "weight": 1.0} -->

where $V$ is an $\mathcal{F}_{0}$-measurable, positive definite matrix. In particular, assume that with probability one, the eigenvalues of $V$ are larger than $\lambda_{0} > 0$ and that ${\| m_{k}\|} \leq L$ holds a.s. for any $k \geq 0$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Still, the new bound is considerably better than the previous one given by Theorem 2"). Note that the $\log{(t)}$ factor cannot be removed, as shown by Problem 3, page 203 in the book by de la Peña et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optional Skipping", "weight": 1.0} -->

Thus, we get, with probability $1 - \delta$

<!-- chunk {"id": "body-0013", "role": "body", "section": "Optional Skipping", "weight": 1.0} -->

If we apply Doob's optional skipping and Hoeffding-Azuma, with a union bound (see, e.g., the paper of Bubeck et al. ), we would get, for any $0 < \delta < 1$, $t \geq 2$, with probability $1 - \delta$,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Optional Skipping", "weight": 1.0} -->

The major difference between these bounds is that (12")) depends explicitly on $t$, while (11")) does not. This has the positive effect that one need not recompute the bound if $N_{t}$ does not grow, which helps e.g. in the paper of Bubeck et al. to improve the computational complexity of the HOO algorithm. Also, the coefficient of the leading term in (11")) under the square root is $1$, whereas in (12")) it is $2$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optional Skipping", "weight": 1.0} -->

Instead of a union bound, it is possible to use a "peeling device" to replace the conservative $\log t$ factor in the above bound by essentially $\log{\log t}$. This is done e.g. in Garivier and Moulines in their Theorem 22.^22^2They give their theorem as ratios, which they should not, since their inequality then fails to hold for $N_{t} = 0$. However, this is easy to remedy by reformulating their result as we do it here. From their derivations, the following one sided, uniform bound can be extracted (see Remark 24, page 19): For any $0 < \delta < 1$, $t \geq 2$, with probability $1 - \delta$,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optional Skipping", "weight": 1.0} -->

As noted by Garivier and Moulines, due to the law of iterated logarithm, the scaling of the right-hand side as a function of $t$ cannot be improved in the worst-case. However, this leaves open the possibility of deriving a maximal inequality which depends on $t$ only through $N_{t}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Multi-Armed Bandit Problem", "weight": 1.0} -->

Now we turn our attention to the multi-armed bandit problem. Let $\mu_{i}$ denote the expected reward of action $i$ and $\Delta_{i} = {\mu_{\ast} - \mu_{i}}$, where $\mu_{\ast}$ is the expected reward of the optimal action. We assume that if we choose action $I_{t}$ in round $t$, we obtain reward $\mu_{I_{t}} + \eta_{t}$. Let $N_{i,t}$ denote the number of times that we have played action $i$ up to time $t$, and ${\overline{X}}_{i,t}$ denote the average of the rewards received by action $i$ up to time $t$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Multi-Armed Bandit Problem", "weight": 1.0} -->

Modify the UCB Algorithm of Auer et al. to use the confidence intervals (14")) and change the action selection rule accordingly. Hence, at time $t$, we choose the action

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Multi-Armed Bandit Problem", "weight": 1.0} -->

We call this algorithm UCB($\delta$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Lai and Robbins prove that for any suboptimal arm $j$,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 7", "weight": 1.0} -->

where, $p_{\ast}$ and $p_{j}$ are the reward density of the optimal arm and arm $j$ respectively, and $D$ is the KD-divergence. This lower bound does not contradict Theorem 6"), as Theorem 6") only states a high probability upper bound for the regret. Note that UCB($\delta$) takes delta as its input. Because with probability $\delta$, the regret in time $t$ can be $t$, on expectation, the algorithm might have a regret of $t\delta$. Now if we select $\delta = {1/t}$, then we get $O{({\log t})}$ upper bound on the expected regret.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

In this section we first apply Theorem 3. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ") to derive confidence intervals for least-squares estimation, where the covariate process is an arbitrary process and then use these confidence intervals to improve the regret bound of Dani et al. for the linear bandit problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

We shall call the random variables $x_{i}$ covariates and the random variables $y_{i}$ the responses. Note that the assumption allows any sequential generation of the covariates.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

We are interested in deriving a confidence bound on the error of predicting the mean response $x^{\top}\theta_{\ast}$ at an arbitrarily chosen random covariate $x$ using the least-squares predictor $x^{\top}{\hat{\theta}}_{t}$. Using

<!-- chunk {"id": "body-0025", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

where $V_{t} = {{X^{\top}X} + {\lambdaI}}$. Note that $V_{t}$ is positive definite (thanks to $\lambda > 0$) and hence so is $V_{t}^{- 1}$, so the above inner product is well-defined. Using the Cauchy-Schwartz inequality, we get

<!-- chunk {"id": "body-0026", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

where we used that $\left\| \theta_{\ast} \right\|_{V_{t}^{- 1}}^{2} \leq {{1/\lambda_{\min}}{(V_{t})}\left\| \theta_{\ast} \right\|^{2}} \leq {{1/\lambda}\left\| \theta_{\ast} \right\|^{2}}$. Fix any $0 < \delta < 1$. By Corollary 1. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory "), with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

Therefore, on the event where this inequality holds, one also has

<!-- chunk {"id": "body-0028", "role": "body", "section": "Application to Least Squares Estimation and Linear Bandit Problem", "weight": 1.0} -->

Similarly, we can derive a worst-case bound.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 9", "weight": 1.0} -->

We see that $\lambda\rightarrow\infty$ increases the second term (the "bias term") in the parenthesis of the estimate. In fact, $\lambda\rightarrow\infty$ for $n$ fixed gives ${\lambda^{1/2}\left\| x \right\|_{V_{t}^{- 1}}}\rightarrow{const}$ (as it should be). Decreasing $\lambda$, on the other hand increases $\left\| x \right\|_{V_{t}^{- 1}}$ and the $\log$ term, while it decreases the bias term $\lambda^{1/2}S$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 12", "weight": 1.0} -->

The above bound could be compared with a similar bound of Dani et al. whose bound, under identical conditions, states that (with appropriate initialization) with probability $1 - \delta$,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 12", "weight": 1.0} -->

where large enough means that $t$ satisfies $0 < \delta < {t^{2}e^{- {1/16}}}$. Denote by $\sqrt{\beta_{t}{(\delta)}}$ the right-hand side in the above bound. The restriction on $t$ comes from the fact that ${\beta_{t}{(\delta)}} \geq {2d{({1 + {2{\log{(t)}}}})}}$ is needed in the proof of the last inequality of their Theorem 5.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 12", "weight": 1.0} -->

On the other hand, Theorem 2") gives rise to the following result: For any fixed $t \geq 2$, for any $0 < \delta < 1$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 12", "weight": 1.0} -->

where $\kappa$ is as in Theorem 2"). To get a uniform bound one can use a union bound with $\delta_{t} = {\delta/t^{2}}$. Then ${\sum_{t = 2}^{\infty}\delta_{t}} = {\delta{({\frac{\pi^{2}}{6} - 1})}} \leq \delta$. This thus gives that for any $0 < \delta < 1$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 12", "weight": 1.0} -->

This looks tighter than (20")), but is still lagging beyond the result of Corollary 10").

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Linear Bandit Problem", "weight": 1.0} -->

We now turn our attention to the linear bandit problem. Assume the actions lie in $\mathcal{D} \subset^{d}$ and for any $x \in \mathcal{D}$, $\left\| x \right\|^{2} \leq L$. Assume the reward of taking action $x \in \mathcal{D}$ has the form of

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Linear Bandit Problem", "weight": 1.0} -->

Consider the ConfidenceBall algorithm of Dani et al.. We use the confidence intervals (21")) and change the action selection rule accordingly.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Linear Bandit Problem", "weight": 1.0} -->

Input: Confidence 0 &lt; δ &lt; 1. for t:= 1, 2, … do ${({\overset{\sim}{\theta}}_{t},x_{t})} = {\operatorname{argmax}_{{(\theta,x)} \in {{\mathcal{C}_{t}{(\delta)}} \times \mathcal{D}}}{\theta^{\top}x}}$. Play xt and observe reward ht (xt). Update Vt and Ct. end for
Table 1: The Linear Bandit Algorithm

<!-- chunk {"id": "body-0038", "role": "body", "section": "Saving Computation", "weight": 1.0} -->

The action selection rule (22")) is NP-hard in general. In this section, we show that we essentially need to solve this problem only $O{({\log t})}$ times up to time $t$ and hence saving computations. Algorithm 2") achieves this objective by changing its policy only when the volume of the confidence set is halved and still enjoyes almost the same regret bound as for Algorithm 1").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Saving Computation", "weight": 1.0} -->

Input: Confidence 0 &lt; δ &lt; 1. τ = 1 {This is the last timestep that we changed the action} for t:= 1, 2, … do if det (Vt) &gt; 2 det (Vτ) then ${({\overset{\sim}{\theta}}_{t},x_{t})} = {\operatorname{argmax}_{{(\theta,x)} \in {{\mathcal{C}_{t}{(\delta)}} \times \mathcal{D}}}{\theta^{\top}x}}$. τ = t. end if xt = xτ. Play xt and observe reward ht (xt). end for
Table 2: The Linear Bandit Algorithm

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem Dependent Bound ($\\Delta > 0$)", "weight": 1.0} -->

Let $\Delta$ be as defined. In this section we assume that $\Delta > 0$. This includes the case when the action set is a polytope. First we state a matrix perturbation theorem from Stewart and Sun that will be used later.
