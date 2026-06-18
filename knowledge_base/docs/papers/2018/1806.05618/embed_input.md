<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Variance-Reduced Policy Gradient

Topics include Policy gradients, Supervised learning, Learning, Sampling, SVRPG, Stochastic variance-reduced gradient, SVRG, Reinforcement learning, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a novel reinforcement- learning algorithm consisting in a stochastic variance-reduced version of policy gradient for solving Markov Decision Processes (MDPs). Stochastic variance-reduced gradient (SVRG) methods have proven to be very successful in supervised learning. However, their adaptation to policy gradient is not straightforward and needs to account for I) a non-concave objective func- tion; II) approximations in the full gradient com- putation; and III) a non-stationary sampling pro- cess. The result is SVRPG, a stochastic variance- reduced policy gradient algorithm that leverages on importance weights to preserve the unbiased- ness of the gradient estimate. Under standard as- sumptions on the MDP, we provide convergence guarantees for SVRPG with a convergence rate that is linear under increasing batch sizes. Finally, we suggest practical variants of SVRPG, and we empirically evaluate them on continuous MDPs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

On a very general level, artificial intelligence addresses the problem of an agent that must select the right actions to solve a task. The approach of Reinforcement Learning (RL) is to learn the best actions by direct interaction with the environment and evaluation of the performance in the form of a reward signal. This makes RL fundamentally different from Supervised Learning (SL), where correct actions are explicitly prescribed by a human teacher (e.g., for classification, in the form of class labels). However, the two approaches share many challenges and tools. The problem of estimating a model from samples, which is at the core of SL, is equally fundamental in RL, whether we choose to model the environment, a value function, or directly a policy defining the agent's behaviour. Furthermore, when the tasks are characterized by large or continuous state-action spaces, RL needs the powerful function approximators (e.g., neural networks) that are the main subject of study of SL. In a typical SL setting, a performance function $J{({\mathbf{θ}})}$ has to be optimized w.r.t. to model parameters $\mathbf{θ}$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The set of data that are available for training is often a subset of all the cases of interest, which may even be infinite, leading to optimization of finite sums that approximate the expected performance over an unknown data distribution. When generalization to the complete dataset is not taken into consideration, we talk about Empirical Risk Minimization (ERM). Even in this case, stochastic optimization is often used for reasons of efficiency. The idea of stochastic gradient (SG) ascent is to iteratively focus on a random subset of the available data to obtain an approximate improvement direction. At the level of the single iteration, this can be much less expensive than taking into account all the data. However, the sub-sampling of data is a source of variance that can potentially compromise convergence, so that per-iteration efficiency and convergence rate must be traded off with proper handling of meta-parameters. Variance-reduced gradient algorithms such as SAG, SVRG and SAGA offer better ways of solving this trade-off, with significant results both in theory and practice. Although designed explicitly for ERM, these algorithms address a problem that affects more general machine learning problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In RL, stochastic optimization is rarely a matter of choice, since data must be actively sampled by interacting with an initially unknown environment. In this scenario, limiting the variance of the estimates is a necessity that cannot be avoided, which makes variance-reduced algorithms very interesting. Among RL approaches, policy gradient is the one that bears the closest similarity to SL solutions. The fundamental principle of these methods is to optimize a parametric policy through stochastic gradient ascent. Compared to other applications of SG, the cost of collecting samples can be very high since it requires to interact with the environment. This makes SVRG-like methods potentially much more efficient than, e.g., batch learning. Unfortunately, RL has a series of difficulties that are not present in ERM. First, in SL the objective can often be designed to be strongly concave (we aim to maximize). This is not the case for RL, so we have to deal with non-concave objective functions. Then, as mentioned before, the dataset is not initially available and may even be infinite, which makes approximations unavoidable.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This rules out SAG and SAGA because of their storage requirements, which leaves SVRG as the most promising choice. Finally, the distribution used to sample data is not under direct control of the algorithm designer, but it is a function of policy parameters that change over time as the policy is optimized, which is a form of non-stationarity. SVRG has been used in RL as an efficient technique for optimizing the per-iteration problem in Trust-Region Policy Optimization or for policy evaluation. In both the cases, the optimization problems faced resemble the SL scenario and are not affected by all the previously mentioned issues.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

After providing background on policy gradient and SVRG in Section 2, we propose SVRPG, a variant of SVRG for the policy gradient framework, addressing all the difficulties mentioned above (see Section 3). In Section 4 we provide convergence guarantees for our algorithm, and we show a convergence rate that has an $O{({1/T})}$ dependence on the number $T$ of iterations. In Section 5.2 we suggest how to set the meta-parameters of SVRPG, while in Section 5.3 we discuss some practical variants of the algorithm. Finally, in Section 7 we empirically evaluate the performance of our method on popular continuous RL tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

A Reinforcement Learning task can be modelled with a discrete-time continuous Markov Decision Process (MDP) $M = {\{\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma,\rho\}}$, where $\mathcal{S}$ is a continuous state space; $\mathcal{A}$ is a continuous action space; $\mathcal{P}$ is a Markovian transition model, where $\mathcal{P}{(\left.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

s^{\prime} \middle| {s,a} \right.)}$ defines the transition density from state $s$ to $s^{\prime}$ under action $a$; $\mathcal{R}$ is the reward function, where ${\mathcal{R}{(s,a)}} \in {\lbrack{- R},R\rbrack}$ is the expected reward for state-action pair $(s,a)$; $\gamma \in {\lbrack 0,1)}$ is the discount factor; and $\rho$ is the initial state distribution. The agent's behaviour is modelled as a policy $\pi$, where $\pi{( \cdot |s)}$ is the density distribution over $\mathcal{A}$ in state $s$. We consider episodic MDPs with effective horizon $H$.^11^1The episode duration is a random variable, but the optimal policy can reach the target state (i.e., absorbing state) in less than $H$ steps.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

This has not to be confused with a finite horizon problem where the optimal policy is non-stationary. In this setting, we can limit our attention to trajectories of length $H$. A trajectory $\tau$ is a sequence of states and actions $(s_{0},a_{0},s_{1},a_{1},\ldots,s_{H - 1},a_{H - 1})$ observed by following a stationary policy, where $s_{0} \sim \rho$. We denote with $p{(\left.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

\tau \middle| \pi \right.)}$ the density distribution induced by policy $\pi$ on the set $\mathcal{T}$ of all possible trajectories (see Appendix A for the definition), and with $\mathcal{R}{(\tau)}$ the total discounted reward provided by trajectory $\tau$: ${{\mathcal{R}{(\tau)}} = {\sum_{t = 0}^{H - 1}{\gamma^{t}\mathcal{R}{(s_{t},a_{t})}}}}.$ Policies can be ranked based on their expected total reward: ${J{(\pi)}} = {\mathbb{E}_{\tau \sim p{( \cdot |\pi)}}\left\lbrack {\mathcal{R}{(\tau)}} \middle| M \right\rbrack}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

Policy gradient methods restrict the search for the best performing policy over a class of parametrized policies $\Pi_{\mathbf{θ}} = {\{\pi_{\mathbf{θ}}:{{\mathbf{θ}} \in {\mathbb{R}}^{d}}\}}$, with the only constraint that $\pi_{\mathbf{θ}}$ is differentiable w.r.t. $\mathbf{θ}$. For sake of brevity, we will denote the performance of a parametric policy with $J{({\mathbf{θ}})}$ and the probability of a trajectory $\tau$ with $p{(\left. \tau \middle| {\mathbf{θ}} \right.)}$ (in some occasions, $p{(\left. \tau \middle| {\mathbf{θ}} \right.)}$ will be replaced by $p_{\mathbf{θ}}{(\tau)}$ for the sake of readability).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

Notice that the distribution defining the gradient is induced by the current policy. This aspect introduces a nonstationarity in the sampling process. Since the underlying distribution changes over time, it is necessary to resample at each update or use weighting techniques such as importance sampling. Here, we consider the *online learning scenario*, where trajectories are sampled by interacting with the environment at each policy change. In this setting, stochastic gradient ascent is typically employed. At each iteration $k > 0$, a batch $\mathcal{D}_{N}^{k} = {\{\tau_{i}\}}_{i = 0}^{N}$ of $N > 0$ trajectories is collected using policy $\pi_{{\mathbf{θ}}_{k}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

where $g{(\left. \tau_{i} \middle| {\mathbf{θ}} \right.)}$ is an estimate of ${{\nabla\log}p_{\mathbf{θ}}}{(\tau_{i})}\mathcal{R}{(\tau_{i})}$. Although the REINFORCE definition is simpler than the G(PO)MDP one, the latter is usually preferred due to its lower variance. We refer the reader to Appendix A for details and a formal definition of $g$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

The main limitation of plain policy gradient is the high variance of these estimators. The naïve approach of increasing the batch size is not an option in RL due to the high cost of collecting samples, i.e., by interacting with the environment. For this reason, literature has focused on the introduction of baselines (i.e., functions $b:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$) aiming to reduce the variance, see Appendix A for a formal definition of $b$. These baselines are usually designed to minimize the variance of the gradient estimate, but even them need to be estimated from data, partially reducing their effectiveness. On the other hand, there has been a surge of recent interest in variance reduction techniques for gradient optimization in supervised learning (SL). Although these techniques have been mainly derived for finite-sum problems, we will show in Section 3 how they can be used in RL.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

In particular, we will show that the proposed SVRPG algorithm can take the best of both worlds (i.e., SL and RL) since it can be plugged into a policy gradient estimate using baselines. The next section has the aim to describe variance reduction techniques for finite-sum problems. In particular, we will present the SVRG algorithm that is at the core of this work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic Variance-Reduced Gradient", "weight": 1.0} -->

This kind of optimization is very common in machine learning, where each $z_{i}$ may correspond to a data sample $x_{i}$ from a dataset $\mathcal{D}_{N}$ of size $N$ (i.e., ${z_{i}{({\mathbf{θ}})}} = {z{(\left. x_{i} \middle| {\mathbf{θ}} \right.)}}$). A common requirement is that $z$ must be smooth and concave in $\mathbf{θ}$.^22^2Note that we are considering a maximization problem instead of the classical minimization one. Under this hypothesis, full gradient (FG) ascent (Cauchy, 1847) with a constant step size achieves a linear convergence rate in the number $T$ of iterations (i.e., parameter updates). However, each iteration requires $N$ gradient computations, which can be too expensive for large values of $N$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic Variance-Reduced Gradient", "weight": 1.0} -->

Stochastic Gradient (SG) ascent overcomes this problem by sampling a single sample $x_{i}$ per iteration, but a vanishing step size is required to control the variance introduced by sampling. As a consequence, the lower per-iteration cost is paid with a worse, sub-linear convergence rate. Starting from SAG, a series of variations to SG have been proposed to achieve a better trade-off between convergence speed and cost per iteration: e.g., SAG, SVRG, SAGA, Finito, and MISO. The common idea is to reuse past gradient computations to reduce the variance of the current estimate. In particular, Stochastic Variance-Reduced Gradient (SVRG) is often preferred to other similar methods for its limited storage requirements, which is a significant advantage when deep and/or wide neural networks are employed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stochastic Variance-Reduced Gradient", "weight": 1.0} -->

The idea of SVRG (Algorithm 1) is to alternate full and stochastic gradient updates. Each $m = {O{(N)}}$ iterations, a snapshot $\overset{\sim}{\mathbf{θ}}$ of the current parameter is saved together with its full gradient ${{\nabla f}{(\overset{\sim}{\mathbf{θ}})}} = {\frac{1}{N}{\sum_{i}{{\nabla z}{(\left. x_{i} \middle| \overset{\sim}{\mathbf{θ}} \right.)}}}}$. Between snapshots, the parameter is updated with $▼f{({\mathbf{θ}})}$, a gradient estimate corrected using stochastic gradient.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stochastic Variance-Reduced Gradient", "weight": 1.0} -->

where $x$ is sampled uniformly at random from $\mathcal{D}_{N}$ (i.e., $x \sim {\mathcal{U}{(\mathcal{D}_{N})}}$). Note that $t = 0$ corresponds to a FG step (i.e., ${▼f{({\mathbf{θ}}_{0})}} = {{\nabla f}{(\overset{\sim}{\mathbf{θ}})}}$) since ${\mathbf{θ}}_{0}:=\overset{\sim}{\mathbf{θ}}$. The corrected gradient $▼f{({\mathbf{θ}})}$ is an unbiased estimate of ${\nabla f}{({\mathbf{θ}})}$, and it is able to control the variance introduced by sampling even with a fixed step size, achieving a linear convergence rate without resorting to a plain full gradient.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stochastic Variance-Reduced Gradient", "weight": 1.0} -->

Under this hypothesis, the convergence rate of SG is $O{({1/\sqrt{T}})}$, i.e., $T = {O{({1/\epsilon^{2}})}}$ iterations are required to get $\left\| {{\nabla f}{({\mathbf{θ}})}} \right\|_{2}^{2} \leq \epsilon$. Again, SVRG achieves the same rate as FG, which is $O{(\frac{1}{T})}$ in this case. The only additional requirement is to select ${\mathbf{θ}}^{\ast}$ uniformly at random among all the ${\mathbf{θ}}_{k}$ instead of simply setting it to the final value ($k$ being the iterations).

<!-- chunk {"id": "body-0022", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

In online RL problems, the usual approach is to tune the batch size of SG to find the optimal trade-off between variance and speed. Recall that, compared to SL, the samples are not fixed in advance but we need to collect them at each policy change. Since this operation may be costly, we would like to minimize the number of interactions with the environment. For these reasons, we would like to apply SVRG to RL problems in order to limit the variance introduced by sampling trajectories, which would ultimately lead to faster convergence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

: the objective function $J{({\mathbf{θ}})}$ is typically non-concave.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

: the RL optimization cannot be expressed as a finite-sum problem. The objective function is an expected value over the trajectory density $p_{\mathbf{θ}}{(\tau)}$ of the total discounted reward, for which we would need an infinite dataset.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

: the distribution of the samples changes over time. In particular, the value of the policy parameter $\mathbf{θ}$ influences the sampling process.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

To deal with non-concavity, we require $J{({\mathbf{θ}})}$ to be $L$-smooth, which is a reasonable assumption for common policy classes such as Gaussian^33^3See Appendix C for more details on the Gaussian policy case. and softmax. Because of the infinite dataset, we can only rely on an estimate of the full gradient. Harikandeh et al. analysed this scenario under the assumptions of $z$ being concave, showing that SVRG is robust to an inexact computation of the full gradient. In particular, it is still possible to recover the original convergence rate if the error decreases at an appropriate rate. Bietti & Mairal performed a similar analysis on MISO. In Section 4 we will show how the estimation accuracy impacts on the convergence results with a non-concave objective. Finally, the non-stationarity of the optimization problem introduces a bias into the SVRG estimator in Eq.. To overcome this limitation we employ importance weighting to correct the distribution shift.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

We can now introduce Stochastic Variance-Reduced Policy Gradient (SVRPG) for a generic policy gradient estimator $g$. Pseudo-code is provided in Algorithm 2. The overall structure is the same as Algorithm 1, but the snapshot gradient is not exact and the gradient estimate used between snapshots is corrected using importance weighting:^44^4Note that $g$ can be any unbiased estimator, with or without baseline. The unbiasedness is required for theoretical results (e.g., Appendix A).

<!-- chunk {"id": "body-0028", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

\tau \middle| {\mathbf{θ}}_{t} \right.)}}$ is an importance weight from $\pi_{{\mathbf{θ}}_{t}}$ to the snapshot policy $\pi_{\overset{\sim}{\mathbf{θ}}}$. Similarly to SVRG, we have that ${\mathbf{θ}}_{0}:=\overset{\sim}{\mathbf{θ}}$, and the update is a FG step. Our update is still fundamentally on-policy since the weighting concerns only the correction term. However, this partial "off-policyness" represents an additional source of variance. This is a well-known issue of importance sampling. To mitigate it, we use mini-batches of trajectories of size $B \ll N$ to average the correction, i.e.,

<!-- chunk {"id": "body-0029", "role": "body", "section": "SVRG in Reinforcement Learning", "weight": 1.0} -->

This property will be used to prove Lemma 3.1. The use of mini-batches is also common practice in SVRG since it can yield a performance improvement even in the supervised case.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence Guarantees of SVRPG", "weight": 1.0} -->

In this section, we state the convergence guarantees for SVRPG with REINFORCE or G(PO)MDP gradient estimator. We mainly leverage on the recent analysis of non-concave SVRG. Each of the three challenges presented at the beginning of Section 3 can potentially prevent convergence, so we need additional assumptions. In Appendix C we show how Gaussian policies satisfy these assumptions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence Guarantees of SVRPG", "weight": 1.0} -->

1\) Non-concavity. A common assumption, in this case, is to assume the objective function to be $L$-smooth. However, in RL we can consider the following assumption which is sufficient for the $L$-smoothness of the objective (see Lemma B.2).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 4.1 (On policy derivatives)", "weight": 1.0} -->

2\) FG Approximation. Since we cannot compute an exact full gradient, we require the variance of the estimator to be bounded. This assumption is similar in spirit to the one.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 4.2 (On the variance of the gradient estimator)", "weight": 1.0} -->

3\) Non-stationarity. Similarly to what is done in SL, we require the variance of the importance weight to be bounded.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 4.3 (On the variance of importance weights)", "weight": 1.0} -->

There is a constant $W < \infty$ such that, for each pair of policies encountered in Algorithm 2 and for each trajectory,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 4.3 (On the variance of importance weights)", "weight": 1.0} -->

Differently from Assumptions 4.1. ‣ 4 Convergence Guarantees of SVRPG ‣ Stochastic Variance-Reduced Policy Gradient") and 4.2. ‣ 4 Convergence Guarantees of SVRPG ‣ Stochastic Variance-Reduced Policy Gradient"), Assumption 4.3. ‣ 4 Convergence Guarantees of SVRPG ‣ Stochastic Variance-Reduced Policy Gradient") must be enforced by a proper handling of the epoch size $m$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 4.3 (On the variance of importance weights)", "weight": 1.0} -->

We can now state the convergence guarantees for SVRPG.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remarks on SVRPG", "weight": 1.0} -->

The convergence guarantees presented in the previous section come with requirements on the meta-parameters (i.e., $\alpha$ and $m$) that may be too conservative for practical applications. Here we provide a practical and automatic way to choose the step size $\alpha$ and the number of sub-iterations $m$ performed between snapshots. Additionally, we provide a variant of SVRPG exploiting a variance-reduction technique for importance weights. Despite lacking theoretical guarantees, we will show in Section 7 that this method can outperform the baseline SVRPG (Algorithm 2).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Full Gradient Update", "weight": 1.0} -->

As noted in Section 3, the update performed at the beginning of each epoch is equivalent to a full-gradient update. In our setting, where collecting samples is particularly expensive, the $B$ trajectories collected using the snapshot trajectory $\pi_{{\overset{\sim}{\mathbf{θ}}}^{s}}$ feels like a waste of data (the term ${{\sum_{i}{g{(\tau_{i})}}} - {\omega{(\tau_{i})}g{(\tau_{i})}}} = 0$ since ${\mathbf{θ}}_{0} = \overset{\sim}{\mathbf{θ}}$). In practice, we just perform an approximate full gradient update using the $N$ trajectories sampled to compute ${\hat{\nabla}}_{N}J{({\overset{\sim}{\mathbf{θ}}}^{s})}$, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Full Gradient Update", "weight": 1.0} -->

In the following, we will always use this practical variant.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Meta-Parameter Selection", "weight": 1.0} -->

The step size $\alpha$ is crucial to balance variance reduction and efficiency, while the epoch length $m$ influences the variance introduced by the importance weights. Low values of $m$ are associated with small variance but increase the frequency of snapshot points (which means many FG computations). High values of $m$ may move policy $\pi_{{\mathbf{θ}}_{t}}$ far away from the snapshot policy $\pi_{\overset{\sim}{\mathbf{θ}}}$, causing large variance in the importance weights. We will jointly set the two meta-parameters.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Meta-Parameter Selection", "weight": 1.0} -->

Adaptive step size. A standard way to deal with noisy gradients is to use adaptive strategies to compute the step size. ADAptive Moment estimation (ADAM) stabilizes the parameter update by computing learning rates for each parameter based on an incremental estimate of the gradient variance. Due to this feature, we would like to incorporate ADAM in the structure of the SVRPG update. Recall that SVRPG performs two different updates of the parameters $\mathbf{θ}$: I) FG update in the snapshot; II) corrected gradient update in the sub-iterations.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Meta-Parameter Selection", "weight": 1.0} -->

where $\alpha_{s}^{\text{FG}}$ is associated with the snapshot and $\alpha_{{s + 1},t}^{\text{SI}}$ with the sub-iterations (see Appendix D for details). By doing so, we decouple the contribution of the variance due to the approximate FG from the one introduced by the sub-iterations. Note that these two terms have different orders of magnitude since are estimated with a different number of trajectories ($B \ll N$) and the estimator in the snapshot does not require importance weights. The use of two ADAM estimators allows to capture and exploit this property.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Meta-Parameter Selection", "weight": 1.0} -->

Adaptive epoch length. It is easy to imagine that a predefined schedule (e.g., $m$ fixed in advance or changed with a policy-independent process) may poorly perform due to the high variability of the updates. In particular, given a fixed number of sub-iterations $m$, the variance of the updates in the sub-iterations depends on the snapshot policy and the sampled trajectories. Since the ADAM estimate partly captures such variability, we propose to take a new snapshot (i.e., interrupt the sub-iterations) whenever the step size $\alpha^{\text{SI}}$ proposed by ADAM for the sub-iterations is smaller than the one for the FG (i.e., $\alpha^{\text{FG}}$). If the latter condition is verified, it amounts to say that the noise in the corrected gradient has overcome the information of the FG. Formally, the stopping condition is as follows

<!-- chunk {"id": "body-0044", "role": "body", "section": "Meta-Parameter Selection", "weight": 1.0} -->

where we have introduced $N$ and $B$ to take into account the trajectory efficiency (i.e., weighted advantage). The less the number of trajectories used to update the policy, the better. Including the batch sizes in the stopping condition allows us to optimize the trade-off between the quality of the updates and the cost of performing them.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Normalized Importance Sampling", "weight": 1.0} -->

As mentioned in Section 5.2, importance weights are an additional source of variance. A standard way to cope with this issue is self-normalization. This technique can reduce the variance of the importance weights at the cost of introducing some bias. Whether the trade-off is advantageous depends on the specific task. Introducing self-normalization in the context of our algorithm, we switch from Eq.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate the performance of SVRPG and compare it with policy gradient (PG) on well known continuous RL tasks: Cart-pole balancing and Swimmer. We consider G(PO)MDP since it has a smaller variance than REINFORCE. For our algorithm, we use a batch size $N = 100$, a mini-batch size $B = 10$, and the jointly adaptive step size $\alpha$ and epoch length $m$ proposed in Section 5.2. Since the aim of this comparison is to show the improvement that SVRG-flavored variance reduction brings to SG in the policy gradient framework, we set the batch size of the baseline policy gradient algorithm to $B$. In this sense, we measure the improvement yielded by computing snapshot gradients and using them to adjust parameter updates. Since we evaluate on-line performance over the number of sampled trajectories, the cost of computing such snapshot gradients is automatically taken into consideration. To make the comparison fair, we also use Adam in the baseline PG algorithm, which we will denote simply as G(PO)MDP in the following.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

In all the experiments, we use deep Gaussian policies with adaptive standard deviation (details on network architecture in Appendix E). Each experiment is run $10$ times with a random policy initialization and seed, but this initialization is shared among the algorithms under comparison. The length of the experiment, i.e., the total number of trajectories, is fixed for each task. Performance is evaluated by using test-trajectories on a subset of the policies considered during the learning process. We provide average performance with 90% bootstrap confidence intervals. Task implementations are from the rllab library, on which our agents are also based.^77^7Code available at [github.com/Dam930/rllab](github.com/Dam930/rllab). More details on meta-parameters and exhaustive task descriptions are provided in Appendix E.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

The Swimmer task is a 3D continuous-control locomotion task. This task is more difficult than cart-pole. In particular, the longer horizon and the more complex dynamics can have a dangerous impact on the variance of importance weights. In this case, the self-normalization technique proposed in Section 5.3 brings an improvement (even if not statistically significant), as shown in Figure 1(b). Figure 1(c) shows self-normalized SVRPG against G(PO)MDP. Our algorithm outperforms G(PO)MDP for almost the entire learning process. Also here, we note an increase of speed in early iterations, and, toward the end of the learning process, the improvement becomes statistically significant.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments", "weight": 1.0} -->

Preliminary results on actor-critic. Another variance-reduction technique in policy gradient consists of using baselines or critics. This tool is orthogonal to the methods described in this paper, and the theoretical results of Section 4 are general in this sense. In the experiments described so far, we compared against the so-called actor-only G(PO)MDP, i.e., without the baseline. To move towards a more general understanding of the variance issue in policy gradient, we also test SVRPG in an actor-critic scenario. To do so, we consider the more challenging MuJoCo Half-cheetah task, a 3D locomotion task that has a larger state-action space than Swimmer. Figure 1(d) compares self-normalized SVRPG and G(PO)MDP on Half-cheetah, using the critic suggested in for both algorithms. Results are promising, showing that a combination of the baseline usage and SVRG-like variance reduction can yield an improvement that the two techniques alone are not able to achieve. Moreover, SVRPG presents a noticeably lower variance. The performance of actor-critic G(PO)MDP^88^8Duan et al. report results on REINFORCE.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments", "weight": 1.0} -->

However, inspection on rllab code and documentation reveals that it is actually PGT, which is equivalent to G(PO)MDP. Using the name REINFORCE in a general way is inaccurate, but widespread. on Half-Cheetah is coherent with the one reported. Other results are not comparable since we did not use the critic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduced SVRPG, a variant of SVRG designed explicitly for RL problems. The control problem considered in the paper has a series of difficulties that are not common in SL. Among them, non-concavity and approximate estimates of the FG have been analysed independently in SL but never combined. Nevertheless, the main issue in RL is the non-stationarity of the sampling process since the distribution underlying the objective function is policy-dependent. We have shown that by exploiting importance weighting techniques, it is possible to overcome this issue and preserve the unbiasedness of the corrected gradient. We have additionally shown that, under mild assumptions that are often verified in RL applications, it is possible to derive convergence guarantees for SVRPG. Finally, we have empirically shown that practical variants of the theoretical SVRPG version can outperform classical actor-only approaches on benchmark tasks. Preliminary results support the effectiveness of SVRPG also with a commonly used baseline for the policy gradient. Despite that, we believe that it will be possible to derive a baseline designed explicitly for SVRPG to exploit the RL structure and the SVRG idea jointly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Another possible improvement would be to employ the natural gradient to better control the effects of parameter updates on the variance of importance weights. Future work should also focus on making batch sizes $N$ and $B$ adaptive, as suggested.
