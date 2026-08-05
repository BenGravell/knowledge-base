<!-- arxiv-full-text:v1 {"arxiv_id": "1102.2670", "source": "ar5iv"} -->

## Introduction

The least squares method forms a cornerstone of statistics and machine learning. It is used as the main component of many stochastic sequential decision problems, such as multi-armed bandit, linear bandits, and other linear control problems. However, the analysis of least squares in these online settings is non-trivial because of the correlations between data points. Fortunately, there is a connection between online least squares estimation and the area of self-normalized processes. Study of self-normalized processes has a long history that goes back to Student and is treated in detail in recent book by de la Peña et al.. Using these tools we provide a proof of a bound on the deviation for vector-valued martingales. A less general version of the bound can be found already in de la Peña et al.. Additionally our proof, based on the method of mixtures, is new, simpler and self-contained. The bound improves the previous bound of Rusmevichientong and Tsitsiklis and it is applicable to virtually any online least squares problem.

The bound that we derive, gives immediately rise to tight confidence sets for the online least squares estimate that can replace the confidence sets in existing algorithms. In particular, the confidence sets can be used in the UCB algorithm for the multi-armed bandit problem, the ConfidenceBall algorithm of Dani et al. for the linear bandit problem, and LinRel algorithm of Auer for the associative reinforcement learning problem. We show that this leads to improved performance of these algorithms. Our hope is that the new confidence sets can be used to improve the performance of other similar linear decision problems.

The multi-armed bandit problem, introduced by Robbins, is a game between the learner and the environment. At each time step, the learner chooses one of $K$ actions and receives a reward which is generated independently at random from a fixed distribution associated with the chosen arm. The objective of the learner is to maximize his total reward. The performance of the learner is evaluated by the regret, which is defined as the difference between his total reward and the total reward of the best action. Lai and Robbins prove a ${({{\sum_{i \neq i_{\ast}}{{1/D}{(p_{j},p_{i_{\ast}})}}} - {o{}}})}{\log T}$ lower bound on the expected regret of any algorithm, where $T$ is the number of time steps, $p_{i_{\ast}}$ and $p_{i}$ are the reward distributions of the optimal arm and arm $i$ respectively, and $D$ is the KL-divergence.

Auer et al. designed the UCB algorithm and proved a finite-time logarithmic bound on its regret. He used Hoeffding's inequality to construct confidence intervals and obtained a $O{({{({K{\log T}})}/\Delta})}$ bound on the expected regret, where $\Delta$ is the difference between the expected rewards of the best and the second best action.color=red, \]Cite high-probability bound for UCB by Bubeck. We modify UCB so that it uses our new confidence sets and we show a stronger result. Namely, we show that with probability $1 - \delta$, the regret of the modified algorithm is $O{({{K{\log{({1/\delta})}}}/\Delta})}$. Seemingly, this result contradicts the lower bound of Lai and Robbins, however our algorithm depends on $\delta$ which it receives as an input. The expected regret of the modified algorithm with $\delta = {1/T}$ matches the regret of the original algorithm.

In the linear bandit problem, the learner chooses repeatedly actions from a fixed subset of ${\mathbb{R}}^{d}$ and receives a random reward, expectation of which is a linear function of the action. Dani et al. proposed the ConfidenceBall algorithm and showed that its regret is at most $O{({d{\log{(T)}}\sqrt{T{\log{({T/\delta})}}}})}$ with probability at most $1 - \delta$. We modify their algorithm so that it uses our new confidence sets and we show that its regret is at most $O{({{d{\log{(T)}}\sqrt{T}} + \sqrt{dT{\log{({T/\delta})}}}})}$. Additionally, constants in our bound are smaller, and our bound holds for all $T \geq 1$, as opposed the previous one which holds only for sufficiently large $T$. Dani et al. prove also a problem dependent regret bound. Namely, they show that the regret of their algorithm is $O{({\frac{d^{2}}{\Delta}{\log^{2}{T{\log{({T/\delta})}}}}})}$ where $\Delta$ is the "gap" as defined . For our modified algorithm we prove an improved $O{({\frac{\log{({1/\delta})}}{\Delta}{({{\log T} + {d{\log{\log T}}}})}^{2}})}$ bound.

### Notation

We use $\parallel \cdot \parallel$ to denote the 2-norm. For a positive definite matrix $A \in^{d \times d}$, the weighted $2$-norm is defined by ${\| x\|}_{A}^{2} = {x^{\top}Ax}$, where $x \in^{d}$. The inner product is denoted by $\langle \cdot, \cdot \rangle$ and the weighted inner-product ${x^{\top}Ay} = {\langle x,y\rangle}_{A}$. We use $\lambda_{\min}{(A)}$ to denote the minimum eigenvalue of the positive definite matrix $A$. We use $A \succ 0$ to denote that $A$ is positive definite, while we use $A \succeq 0$ to denote that it is positive semidefinite. The same notation is used to denote the Loewner partial order of matrices. We shall use $\mathbf{e}_{i}$ to denote the $i^{th}$ unit vector, i.e., for all $j \neq i$, $\mathbf{e}_{ij} = 0$ and $\mathbf{e}_{ii} = 1$.

## Vector-Valued Martingale Tail Inequalities

Let $({{\mathcal{F}_{k};k} \geq 0})$ be a filtration, $({{m_{k};k} \geq 0})$ be an ^d^-valued stochastic process adapted to $(\mathcal{F}_{k})$, $({{\eta_{k};k} \geq 1})$ be a real-valued martingale difference process adapted to $(\mathcal{F}_{k})$. Assume that $\eta_{k}$ is conditionally sub-Gaussian in the sense that there exists some $R > 0$ such that for any $\gamma \in$, $k \geq 1$, Consider the martingale and the matrix-valued processes where $V$ is an $\mathcal{F}_{0}$-measurable, positive definite matrix. In particular, assume that with probability one, the eigenvalues of $V$ are larger than $\lambda_{0} > 0$ and that ${\| m_{k}\|} \leq L$ holds a.s. for any $k \geq 0$.

The following standard inequality plays a crucial role in the following developments:

### Lemma 1

Consider $(\eta_{t})$, $(m_{t})$ as defined above and let $\tau$ be a stopping time with respect to the filtration $(\mathcal{F}_{t})$. Let $\lambda \in^{d}$ be arbitrary and consider Then $P_{\tau}$ is almost surely well-defined and

### Proof

The proof is standard (and is given only for the sake of completeness). We claim that $P_{t} = P_{t}^{\lambda}$ is a supermartingale. Let Observe that by (1")), we have ${{\mathbb{E}}\left\lbrack D_{k} \middle| \mathcal{F}_{k - 1} \right\rbrack} \leq 1$. Clearly, $D_{k}$ is $\mathcal{F}_{k}$-adapted, as is $P_{k}$. Further, showing that $(P_{t})$ is indeed a supermartingale.

Now, this immediately leads to the desired result when $\tau = t$ for some deterministic time $t$. This is based on the fact that the mean of any supermartingale can be bounded by the mean of its first element. In the case of $(P_{t})$, for example, we have ${{\mathbb{E}}\left\lbrack P_{t} \right\rbrack} = {{\mathbb{E}}\left\lbrack {{\mathbb{E}}\left\lbrack P_{t} \middle| \mathcal{F}_{t - 1} \right\rbrack} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack P_{t - 1} \right\rbrack} \leq \ldots \leq {{\mathbb{E}}\left\lbrack P_{0} \right\rbrack} = {{\mathbb{E}}\left\lbrack D_{0} \right\rbrack} = 1$.

Now, in order to consider the general case, let $S_{t} = P_{\tau \land t}$.^11^1$\tau \land t$ is a shorthand notation for $\min{(\tau,t)}$. It is well known that $(S_{t})$ is still a supermartingale with ${{\mathbb{E}}\left\lbrack S_{t} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack S_{0} \right\rbrack} = {{\mathbb{E}}\left\lbrack P_{0} \right\rbrack} = 1$. Further, since $P_{t}$ was nonnegative, so is $S_{t}$. Hence, by the convergence theorem for nonnegative supermartingales, almost surely, $\lim_{t\rightarrow\infty}S_{t}$ exists, i.e., $P_{\tau}$ is almost surely well-defined. Further, ${{\mathbb{E}}\left\lbrack P_{\tau} \right\rbrack} = {{\mathbb{E}}\left\lbrack {\operatorname{lim\ inf}_{t\rightarrow\infty}S_{t}} \right\rbrack} \leq {\operatorname{lim\ inf}_{t\rightarrow\infty}{{\mathbb{E}}\left\lbrack S_{t} \right\rbrack}} \leq 1$ by Fatou's Lemma. ∎ Before stating our main results, we give some recent results, which can essentially be extracted from the paper by Rusmevichientong and Tsitsiklis.

### Theorem 2

Consider the processes $(S_{t})$, $({\overline{V}}_{t})$ as defined above and let Then, for any $0 < \delta < 1$, $t \geq 2$, with probability at least $1 - \delta$, We now show how to strengthen the previous result using the method of mixtures, originally used by Robbins and Siegmund to evaluate boundary crossing probabilities for Brownian motion.

### Theorem 3 (Self-normalized bound for vector-valued martingales)

Let $(\eta_{t})$, $(m_{t})$, $(S_{t})$, $({\overline{V}}_{t})$, and $(\mathcal{F}_{t})$ be as before and let $\tau$ be a stopping time with respect to the filtration $(\mathcal{F}_{t})$. Assume that $V$ is deterministic. Then, for any $0 < \delta < 1$, with probability $1 - \delta$,

### Proof

Without loss of generality, assume that $R = 1$ (by appropriately scaling $S_{t}$, this can always be achieved). Let Notice that by Lemma 1"), the mean of $M_{\tau}{(\lambda)}$ is not larger than one.

Let $\Lambda$ be a Gaussian random variable which is independent of all the other random variables and whose covariance is $V^{- 1}$. Define Clearly, we still have ${{\mathbb{E}}\left\lbrack M_{\tau} \right\rbrack} = {{\mathbb{E}}\left\lbrack {{\mathbb{E}}\left\lbrack {M_{\tau}{(\Lambda)}} \middle| \Lambda \right\rbrack} \right\rbrack} \leq 1$.

Let us calculate $M_{t}$: Let $f$ denote the density of $\Lambda$ and for a positive definite matrix $P$ let ${c{(P)}} = \sqrt{{({2\pi})}^{d}/{\det{(P)}}} = {\int{{\exp{({- {\frac{1}{2}x^{\top}Px}})}}{dx}}}$. Then, Elementary calculation shows that if $P \succeq 0$, $Q \succ 0$, Now, from ${{\mathbb{E}}\left\lbrack M_{\tau} \right\rbrack} \leq 1$, we obtain thus finishing the proof. ∎

### Corollary 1 (Uniform Bound)

Under the same assumptions as in the previous theorem, for any $0 < \delta < 1$, with probability $1 - \delta$,

### Proof

We will use a stopping time construction, which goes back at least to Freedman. Define the bad event We are interested in bounding the probability that $\bigcup_{t \geq 0}{B_{t}{(\delta)}}$ happens. Define ${\tau{(\omega)}} = {\min{\{{{t \geq 0}:{\omega \in {B_{t}{(\delta)}}}}\}}}$, with the convention that ${\min\varnothing} = \infty$. Then, $\tau$ is a stopping time. Further, Thus, by Theorem 3. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ") Let us now turn our attention to understanding the determinant term on the right-hand side of (6. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ")).

### Lemma 4

Further, we have that Finally, if $\lambda_{0} \geq {\max{(1,L^{2})}}$ then

### Proof

Elementary algebra gives where we used that all the eigenvalues of a matrix of the form $I + {xx^{\top}}$ are one except one eigenvalue, which is $1 + \left\| x \right\|^{2}$ and which corresponds to the eigenvector $x$. Using ${\log{({1 + t})}} \leq t$, we can bound $\log{\det{({\overline{V}}_{t})}}$ by Combining $x \leq {2{\log{({1 + x})}}}$, which holds when $x \in {\lbrack 0,1\rbrack}$, and (9")), we get The trace of ${\overline{V}}_{t}$ is bounded by ${\operatorname{trace}{(V)}} + {tL^{2}}$, assuming ${\| m_{k}\|} \leq L$. Hence, ${\det{({\overline{V}}_{t})}} = {\prod_{i = 1}^{d}\lambda_{i}} \leq \left(\frac{{\operatorname{trace}{(V)}} + {tL^{2}}}{d} \right)^{d}$ and therefore, finishing the proof of the second inequality. The sum $\sum_{k = 1}^{t}\left\| m_{k - 1} \right\|_{{\overline{V}}_{k - 1}^{- 1}}^{2}$ can itself be upper bounded as a function of $\log{\det{({\overline{V}}_{t})}}$ provided that $\lambda_{0}$ is large enough. Notice $\left\| m_{k - 1} \right\|_{{\overline{V}}_{k - 1}^{- 1}}^{2} \leq {\lambda_{\min}^{- 1}{({\overline{V}}_{k - 1})}\left\| m_{k - 1} \right\|^{2}} \leq {L^{2}/\lambda_{0}}$. Hence, we get that if $\lambda_{0} \geq {\max{(1,L^{2})}}$, Most of this argument can be extracted from the paper of Dani et al.. However, the idea goes back at least to Lai et al., Lai and Wei (a similar argument is used around Theorem 11.7 in the book by Cesa-Bianchi and Lugosi). Note that Lemmas B.9--B.11 of Rusmevichientong and Tsitsiklis also give a bound on $\sum_{k = 1}^{t}\left\| m_{k - 1} \right\|_{{\overline{V}}_{k - 1}^{- 1}}^{2}$, with an essentially identical argument. Alternatively, one can use the bounding technique of Auer (see the proof of Lemma 13 there on pages 412--413) to derive a bound like ${\sum_{k = 1}^{t}\left\| m_{k - 1} \right\|_{{\overline{V}}_{k - 1}^{- 1}}^{2}} \leq {Cd{\log t}}$ for a suitable chosen constant $C > 0$.

### Remark 5

By combining Corollary 1. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ") and Lemma 4"), we get a simple worst case bound that holds with probability $1 - \delta$: Still, the new bound is considerably better than the previous one given by Theorem 2"). Note that the $\log{(t)}$ factor cannot be removed, as shown by Problem 3, page 203 in the book by de la Peña et al..

## Optional Skipping

Consider the case when $d = 1$, $m_{k} = \varepsilon_{k} \in {\{ 0,1\}}$, i.e., the case of an optional skipping process. Then, using again $V = I = 1$, ${\overline{V}}_{t} = {1 + {\sum_{k = 1}^{t}\varepsilon_{k - 1}}}\overset{\text{def}}{=}{1 + N_{t}}$ and thus the expression studied becomes Thus, we get, with probability $1 - \delta$ If we apply Doob's optional skipping and Hoeffding-Azuma, with a union bound (see, e.g., the paper of Bubeck et al.), we would get, for any $0 < \delta < 1$, $t \geq 2$, with probability $1 - \delta$, The major difference between these bounds is that (12")) depends explicitly on $t$, while (11")) does not. This has the positive effect that one need not recompute the bound if $N_{t}$ does not grow, which helps e.g. in the paper of Bubeck et al. to improve the computational complexity of the HOO algorithm. Also, the coefficient of the leading term in (11")) under the square root is $1$, whereas in (12")) it is $2$.

Instead of a union bound, it is possible to use a "peeling device" to replace the conservative $\log t$ factor in the above bound by essentially $\log{\log t}$. This is done e.g. in Garivier and Moulines in their Theorem 22.^22^2They give their theorem as ratios, which they should not, since their inequality then fails to hold for $N_{t} = 0$. However, this is easy to remedy by reformulating their result as we do it here. From their derivations, the following one sided, uniform bound can be extracted (see Remark 24, page 19): For any $0 < \delta < 1$, $t \geq 2$, with probability $1 - \delta$, As noted by Garivier and Moulines, due to the law of iterated logarithm, the scaling of the right-hand side as a function of $t$ cannot be improved in the worst-case. However, this leaves open the possibility of deriving a maximal inequality which depends on $t$ only through $N_{t}$.

## The Multi-Armed Bandit Problem

Now we turn our attention to the multi-armed bandit problem. Let $\mu_{i}$ denote the expected reward of action $i$ and $\Delta_{i} = {\mu_{\ast} - \mu_{i}}$, where $\mu_{\ast}$ is the expected reward of the optimal action. We assume that if we choose action $I_{t}$ in round $t$, we obtain reward $\mu_{I_{t}} + \eta_{t}$. Let $N_{i,t}$ denote the number of times that we have played action $i$ up to time $t$, and ${\overline{X}}_{i,t}$ denote the average of the rewards received by action $i$ up to time $t$. From (11")) with $\delta/K$ instead of $\delta$ and a union bound over the actions, we have the following confidence intervals that hold with probability at least $1 - \delta$: Modify the UCB Algorithm of Auer et al. to use the confidence intervals (14")) and change the action selection rule accordingly. Hence, at time $t$, we choose the action We call this algorithm UCB($\delta$).

### Theorem 6

With probability at least $1 - \delta$, the total regret of the UCB($\delta$) algorithm with the action selection rule (15")) is constant and is bounded by where $i_{\ast}$ is the index of the optimal action.

### Proof

Suppose the confidence intervals do not fail. If we play action $i$, the upper estimate of the action is above $\mu^{\ast}$. Hence, Substituting $c_{i,s}$ and squaring gives By using Lemma 8 of Antos et al., we get that Thus, using ${R{(T)}} = {\sum_{i \neq i_{\ast}}{\Delta_{i}N_{i,T}}}$, we get that with probability at least $1 - \delta$, the total regret is bounded by

### Remark 7

Lai and Robbins prove that for any suboptimal arm $j$, where, $p_{\ast}$ and $p_{j}$ are the reward density of the optimal arm and arm $j$ respectively, and $D$ is the KD-divergence. This lower bound does not contradict Theorem 6"), as Theorem 6") only states a high probability upper bound for the regret. Note that UCB($\delta$) takes delta as its input. Because with probability $\delta$, the regret in time $t$ can be $t$, on expectation, the algorithm might have a regret of $t\delta$. Now if we select $\delta = {1/t}$, then we get $O{({\log t})}$ upper bound on the expected regret.

## Application to Least Squares Estimation and Linear Bandit Problem

In this section we first apply Theorem 3. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ") to derive confidence intervals for least-squares estimation, where the covariate process is an arbitrary process and then use these confidence intervals to improve the regret bound of Dani et al. for the linear bandit problem. In particular, our assumption on the data is as follows: Assumption A1 Let $(\mathcal{F}_{i})$ be a filtration, $(x_{1},y_{1})$, $\ldots$, $(x_{t},y_{t})$ be a sequence of random variables over ${}_{}^{d} \times$ such that $x_{i}$ is $\mathcal{F}_{i}$-measurable, and $y_{i}$ is $\mathcal{F}_{i + 1}$-measurable $({i = {1,2,\ldots}})$. Assume that there exists $\theta_{\ast} \in^{d}$ such that ${{\mathbb{E}}\left\lbrack y_{i} \middle| \mathcal{F}_{i} \right\rbrack} = {x_{i}^{\top}\theta_{\ast}}$, i.e., $\varepsilon_{i} = {y_{i} - {x_{i}^{\top}\theta_{\ast}}}$ is a martingale difference sequence (${{\mathbb{E}}\left\lbrack \varepsilon_{i} \middle| \mathcal{F}_{i} \right\rbrack} = 0$, $i = {1,2,\ldots}$) and that $\varepsilon_{i}$ is sub-Gaussian: There exists $R > 0$ such that for any $\gamma \in$, We shall call the random variables $x_{i}$ covariates and the random variables $y_{i}$ the responses. Note that the assumption allows any sequential generation of the covariates.

Let ${\hat{\theta}}_{t}$ be the $\ell^{2}$-regularized least-squares estimate of $\theta_{\ast}$ with regularization parameter $\lambda > 0$: where $X$ is the matrix whose rows are $x_{1}^{\top},\ldots,x_{t - 1}^{\top}$ and $Y = {(y_{1},\ldots,y_{t - 1})}^{\top}$. We further let $\varepsilon = {(\varepsilon_{1},\ldots,\varepsilon_{t - 1})}^{\top}$.

We are interested in deriving a confidence bound on the error of predicting the mean response $x^{\top}\theta_{\ast}$ at an arbitrarily chosen random covariate $x$ using the least-squares predictor $x^{\top}{\hat{\theta}}_{t}$. Using where $V_{t} = {{X^{\top}X} + {\lambdaI}}$. Note that $V_{t}$ is positive definite (thanks to $\lambda > 0$) and hence so is $V_{t}^{- 1}$, so the above inner product is well-defined. Using the Cauchy-Schwartz inequality, we get where we used that $\left\| \theta_{\ast} \right\|_{V_{t}^{- 1}}^{2} \leq {{1/\lambda_{\min}}{(V_{t})}\left\| \theta_{\ast} \right\|^{2}} \leq {{1/\lambda}\left\| \theta_{\ast} \right\|^{2}}$. Fix any $0 < \delta < 1$. By Corollary 1. ‣ 2 Vector-Valued Martingale Tail Inequalities ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory "), with probability at least $1 - \delta$, Therefore, on the event where this inequality holds, one also has Similarly, we can derive a worst-case bound. The result is summarized in the following statement:

### Theorem 8

Let ${(x_{1},y_{1})},\ldots,{(x_{t - 1},y_{t - 1})}$, $x_{i} \in^{d}$, $y_{i} \in$ satisfy the linear model Assumption 5") with some $R > 0$, $\theta_{\ast} \in^{d}$ and let $(\mathcal{F}_{t})$ be the associated filtration. Assume that w.p.1 the covariates satisfy $\left\| x_{i} \right\| \leq L$, $i = {1,\ldots,n}$ and $\left\| \theta_{\ast} \right\| \leq S$. Consider the $\ell^{2}$-regularized least-squares parameter estimate ${\hat{\theta}}_{n}$ with regularization coefficient $\lambda > 0$ (cf. (16"))). Let $x$ be an arbitary, ^d^-valued random variable. Let $V_{t} = {{\lambdaI} + {\sum_{i = 1}^{t - 1}{x_{i}x_{i}^{\top}}}}$ be the regularized design matrix underlying the covariates. Then, for any $0 < \delta < 1$, with probability at least $1 - \delta$, Similarly, with probability $1 - \delta$,

### Remark 9

We see that $\lambda\rightarrow\infty$ increases the second term (the "bias term") in the parenthesis of the estimate. In fact, $\lambda\rightarrow\infty$ for $n$ fixed gives ${\lambda^{1/2}\left\| x \right\|_{V_{t}^{- 1}}}\rightarrow{const}$ (as it should be). Decreasing $\lambda$, on the other hand increases $\left\| x \right\|_{V_{t}^{- 1}}$ and the $\log$ term, while it decreases the bias term $\lambda^{1/2}S$.

From the above result, we immediately obtain confidence bounds for $\theta_{\ast}$:

### Corollary 10

Under the condition of Theorem 8"), with probability at least $1 - \delta$, Also, with probability at least $1 - \delta$,

### Proof

Plugging in $x = {V_{t}{({{\hat{\theta}}_{t} - \theta_{\ast}})}}$ into (17")), we get Now, $\left\| {V_{t}{({{\hat{\theta}}_{t} - \theta_{\ast}})}} \right\|_{V_{t}^{- 1}}^{2} = \left\| {{\hat{\theta}}_{t} - \theta_{\ast}} \right\|_{V_{t}}^{2}$ and therefore either $\left\| {{\hat{\theta}}_{t} - \theta_{\ast}} \right\|_{V_{t}} = 0$, in which case the conclusion holds, or we can divide both sides of (19")) by $\left\| {{\hat{\theta}}_{t} - \theta_{\ast}} \right\|_{V_{t}}$ to obtain the desired result. ∎

### Remark 11

In fact, the theorem and the corollary are equivalent. To see this note that ${x^{\top}{({{\hat{\theta}}_{t} - \theta_{\ast}})}} = {{({{\hat{\theta}}_{t} - \theta_{\ast}})}^{\top}V_{t}^{1/2}V_{t}^{- {1/2}}x}$, thus

### Remark 12

The above bound could be compared with a similar bound of Dani et al. whose bound, under identical conditions, states that (with appropriate initialization) with probability $1 - \delta$, where large enough means that $t$ satisfies $0 < \delta < {t^{2}e^{- {1/16}}}$. Denote by $\sqrt{\beta_{t}{(\delta)}}$ the right-hand side in the above bound. The restriction on $t$ comes from the fact that ${\beta_{t}{(\delta)}} \geq {2d{({1 + {2{\log{(t)}}}})}}$ is needed in the proof of the last inequality of their Theorem 5.

On the other hand, Theorem 2") gives rise to the following result: For any fixed $t \geq 2$, for any $0 < \delta < 1$, with probability at least $1 - \delta$, where $\kappa$ is as in Theorem 2"). To get a uniform bound one can use a union bound with $\delta_{t} = {\delta/t^{2}}$. Then ${\sum_{t = 2}^{\infty}\delta_{t}} = {\delta{({\frac{\pi^{2}}{6} - 1})}} \leq \delta$. This thus gives that for any $0 < \delta < 1$, with probability at least $1 - \delta$, This looks tighter than (20")), but is still lagging beyond the result of Corollary 10").

### The Linear Bandit Problem

We now turn our attention to the linear bandit problem. Assume the actions lie in $\mathcal{D} \subset^{d}$ and for any $x \in \mathcal{D}$, $\left\| x \right\|^{2} \leq L$. Assume the reward of taking action $x \in \mathcal{D}$ has the form of and assume ${{\forall x} \in \mathcal{D}},{{\theta_{\ast}^{\top}x} \in {\lbrack{- 1},1\rbrack}}$. Define the regret by where $x_{\ast}$ is the optimal action ($x_{\ast} = {\operatorname{argmax}_{x \in \mathcal{D}}{\theta_{\ast}^{\top}x}}$). Define the confidence set Consider the ConfidenceBall algorithm of Dani et al.. We use the confidence intervals (21")) and change the action selection rule accordingly. Hence, at time $t$, we define ${\overset{\sim}{\theta}}_{t}$ and $x_{t}$ by the following equation: The algorithm is shown in Table 1").

Input: Confidence 0 < δ < 1. for t:= 1, 2, … do ${({\overset{\sim}{\theta}}_{t},x_{t})} = {\operatorname{argmax}_{{(\theta,x)} \in {{\mathcal{C}_{t}{(\delta)}} \times \mathcal{D}}}{\theta^{\top}x}}$. Play xt and observe reward ht (xt). Update Vt and Ct. end for Table 1: The Linear Bandit Algorithm

### Theorem 13

With probability at least $1 - \delta$, the regret of the Linear Bandit Algorithm shown in Table 1") satisfies

### Proof

Lets decompose the instantaneous regret as follows: where the last step holds by Cauchy-Schwarz. Using (5.1")) and the fact that $r_{t} \leq 2$, we get that Thus, with probability at least $1 - \delta$, ${\forall T} \geq 1$ where the last two steps follow from Lemma 4"). ∎

### Saving Computation

The action selection rule (22")) is NP-hard in general. In this section, we show that we essentially need to solve this problem only $O{({\log t})}$ times up to time $t$ and hence saving computations. Algorithm 2") achieves this objective by changing its policy only when the volume of the confidence set is halved and still enjoyes almost the same regret bound as for Algorithm 1").

Input: Confidence 0 < δ < 1. τ = 1 {This is the last timestep that we changed the action} for t:= 1, 2, … do if det (Vt) > 2 det (Vτ) then ${({\overset{\sim}{\theta}}_{t},x_{t})} = {\operatorname{argmax}_{{(\theta,x)} \in {{\mathcal{C}_{t}{(\delta)}} \times \mathcal{D}}}{\theta^{\top}x}}$. τ = t. end if xt = xτ. Play xt and observe reward ht (xt). end for Table 2: The Linear Bandit Algorithm

### Theorem 14

With probability at least $1 - \delta$, ${\forall T} \geq 1$, the regret of the Linear Bandit Algorithm shown in Table 2") satisfies First, we prove the following lemma:

### Lemma 15

Let $A$, $B$ and $C$ be positive semi-definite matrices such that $A = {B + C}$. Then, we have that

### Proof

We consider first a simple case. Let $A = {B + {mm^{\top}}}$, $B$ positive definite. Let $x \neq 0$ be an arbitrary vector. Using the Cauchy-Schwartz inequality, we get We also have that thus finishing the proof of this case.

By the above argument, since all the terms are positive, we get This finishes the proof of this case.

Now, if $C$ is a positive definite matrix, then the eigendecomposition of $C$ gives $C = {U^{\top}\LambdaU}$, where $U$ is orthonormal and $\Lambda$ is positive diagonal matrix. This, in fact gives that $C$ can be written as the sum of at most $d$ rank-one matrices, finishing the proof for the general case.

### Proof of Theorem 14")

Let $\tau_{t}$ be the smallest timestep $\leq t$ such that $x_{t} = x_{\tau_{t}}$. By an argument similar to the one used in Theorem 13"), we have We also have that for all $\theta \in \mathcal{C}_{\tau_{t}}$ and $x$, where the second step follows from Lemma 15"), and the third step follows from the fact that at time $t$ we have ${\det{(V_{t})}} < {2{\det{(V_{\tau_{t}})}}}$. The rest of the argument is identical to that of Theorem 13"). We conclude that with probability at least $1 - \delta$, ${\forall T} \geq 1$,

### Problem Dependent Bound ($\Delta > 0$)

Let $\Delta$ be as defined . In this section we assume that $\Delta > 0$. This includes the case when the action set is a polytope. First we state a matrix perturbation theorem from Stewart and Sun that will be used later.

### Theorem 16 (Stewart and Sun, Corollary 4.9)

Let $A$ be a symmetric matrix with eigenvalues $\nu_{1} \geq \nu_{2} \geq \ldots \geq \nu_{d}$, $E$ be a symmetric matrix with eigenvalues $e_{1} \geq e_{2} \geq \ldots \geq e_{d}$, and $V = {A + E}$ denote a symmetric perturbation of $A$ such that the eigenvalues of $V$ are ${\overset{\sim}{\nu}}_{1} \geq {\overset{\sim}{\nu}}_{2} \geq \ldots \geq {\overset{\sim}{\nu}}_{d}$. Then, for $i = {1,\ldots,d}$,

### Theorem 17

Assume that $\Delta > 0$ for the gap $\Delta$ defined . Further assume that $\lambda \geq 1$ and $S \geq 1$. With probability at least $1 - \delta$, ${\forall T} \geq 1$, the regret of the algorithm shown in Table 1") satisfies

### Proof

First we bound the regret in terms of $\log{\det{(V_{T})}}$. We have that where the first inequality follows from the fact that either $r_{t} = 0$ or $\Delta < r_{t}$, and the second inequality can be extracted from the proof of Theorem 13"). Let $b_{t}$ be the number of times we have played a sub-optimal action (an action $x_{s}$ for which ${{\theta_{\ast}^{\top}x_{\ast}} - {\theta_{\ast}^{\top}x_{s}}} \geq \Delta$) up to time $t$. Next we bound $\log{\det{(V_{t})}}$ in terms of $b_{t}$. We bound the eigenvalues of $V_{t}$ by using Theorem 16, Corollary 4.9). ‣ 5.3 Problem Dependent Bound (Δ>0) ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ").

Let $E_{t} = {\sum_{s:{x_{s} \neq x_{\ast}}}^{t}{x_{s}x_{s}^{\top}}}$ and $A_{t} = {V_{t} - E_{t}} = {{({t - b_{t}})}x_{\ast}x_{\ast}^{\top}}$. The only non-zero eigenvalue of ${({t - b_{t}})}x_{\ast}x_{\ast}^{\top}$ is ${({t - b_{t}})}L^{\ast}$, where $L^{\ast} = {x_{\ast}^{\top}x_{\ast}} \leq L$. Let the eigenvalues of $V_{t}$ and $E_{t}$ be $\lambda_{1} \geq \cdots \geq \lambda_{d}$ and $e_{1} \geq \cdots \geq e_{d}$ respectively. By Theorem 16, Corollary 4.9). ‣ 5.3 Problem Dependent Bound (Δ>0) ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory "), we have that Because ${\operatorname{trace}{(E)}} = {\sum_{s:{x_{s} \neq x_{\ast}}}^{t}{\operatorname{trace}{({x_{s}x_{s}^{\top}})}}} \leq {Lb_{t}}$, we conclude that $e_{1} \leq {Lb_{t}}$. Thus, With some calculations, we can show that where the second inequality follows from Lemma 4"). Hence, where the first inequality follows from ${R{(t)}} \geq {b_{t}\Delta}$. Thus, with probability $1 - \delta$, ${\forall T} \geq 1$, where the first step follows from (24 ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ")), the second step follows from the first inequality in (26 ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ")), the third step follows from (5.3 ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ")), and the last step follows from the second inequality in (27 ‣ 5 Application to Least Squares Estimation and Linear Bandit Problem ‣ Online Least Squares Estimation with Self-Normalized Processes: An Application to Bandit ProblemsSubmitted to the 24th Annual Conference on Learning Theory ")). ∎

### Remark 18

The problem dependent regret of scales like $O{({\frac{d^{2}}{\Delta}{\log^{3}T}})}$, while our bound scales like $O{({\frac{1}{\Delta}{({{\log^{2}T} + {d{\log T}} + {d^{2}{\log{\log T}}}})}})}$.
