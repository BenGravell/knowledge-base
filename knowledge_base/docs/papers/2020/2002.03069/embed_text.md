## INTRODUCTION

Our work focuses on model-free algorithms for learning in *infinite-horizon undiscounted* Markov decision processes (MDPs), also known as average-reward MDPs. Although model-free algorithms have recently achieved impressive advances in multiple applications, few performance guarantees exist, especially in the average-reward case with function approximation. In this work, we propose *Adaptive Approximate Policy Iteration* (AAPI), a model-free learning scheme that can work with function approximation, and utilizes an adaptive data-dependent learning rate. We analyze the performance of AAPI in infinite-horizon undiscounted MDPs in terms of high-probability regret.

Our approach follows the "online MDP" line of work, where the agent iteratively selects policies by running an online learning algorithm in each state, and the loss fed to each algorithm is the policy Q-function in that state. This results in a variant of approximate policy iteration (API), where the policy improvement step produces a policy optimal in hindsight w.r.t. *the average of all previous* Q-functions rather than just the most recent one. The original work of Even-Dar et al. studied this scheme with known dynamics, tabular representation, and adversarial reward functions. More recent works have adapted this approach to the case of unknown dynamics, stochastic rewards, and value function approximation. The averaging of value functions is further justified theoretically and empirically by Vieillard et al. and Vieillard et al..

A notable feature of our algorithm is that we exploit the fact that losses (Q-function estimates) are slow-changing. In particular, our policy improvement step relies on the adaptive optimistic follow-the-regularized-leader (AO-FTRL) update. The resulting policies are Boltzmann distributions over the sum of past estimated Q-functions, coupled with an optimistic prediction of the upcoming loss and a state-dependent adaptive learning rate (softmax temperature). Our policy improvement step can also be seen as regularizing each policy by the KL-divergence to the previous policy; the reduction to online learning offers a principled way to scale such regularization.

On the theoretical side, we prove the first $\overset{\sim}{O}{(T^{2/3})}$ regret upper bound in the undiscounted, continuing setting with function approximation. This is an improvement over the best existing $\overset{\sim}{O}{(T^{3/4})}$ bound of Abbasi-Yadkori et al. for the same setting, which ignores the slow-changing nature of the estimated Q-functions. Our analysis exploits the fact that the change in consecutive Q-function estimates can be bounded by the change in policies. We rely on the results of Rakhlin and Sridharan, but employ a different regret decomposition, with additional information provided by MDP properties. We emphasize that our learning framework is not limited to a particular function approximation method, and that in practice it serves the purpose of appropriately regularizing the policy improvement step of API.

Related work. Most no-regret algorithms for infinite-horizon undiscounted MDPs are model-based, and only applicable to tabular representations. In the model-free tabular setting, Wei et al. show optimistic Q-learning achieves $O{({\text{sp}{(V_{\ast})}{({XA})}^{1/3}T^{2/3}})}$ regret in weakly-communicating MDPs, where $\text{sp}{(V_{\ast})}$ is the span of the optimal state-value function, $X,A$ are the size of state and action spaces. In the case of uniformly ergodic MDPs, they show a bound of $O{(\sqrt{t_{\text{mix}}^{3}\rhoAT})}$ on the *expected regret*, where $t_{\text{mix}}$ is the mixing time and $\rho$ is the stationary distribution mismatch coefficient. In the model-free setting with function approximation, Abbasi-Yadkori et al. achieve $O{({d^{1/2}T^{3/4}})}$ regret in ergodic MDPs. Here $d$ is the size of the compressed state-action space ($XA$ for tabular representation, number of features for linear $Q$-functions).

In episodic MDPs with horizon $H$, Jin et al. show an $O{(\sqrt{H^{3}XAT})}$ regret bound for Q-learning with tabular representation. With linear function approximation, Yang and Wang; Jin et al.; Cai et al. show an $O{(\sqrt{d^{3}H^{3}T})}$ regret bound for an optimistic version of least-squares value/policy iteration under linear MDPs assumption. The RLSVI algorithm performs exploration in the value function parameter space, and therefore can be applied with function approximation. Its worse-case regret bound of $O{(\sqrt{H^{5}X^{3}AT})}$ holds in the tabular setting and $O{({d^{2}\sqrt{H^{4}T}})}$ holds under the linear MDPs assumption.

Another thread of the literature proposes a reduction of model-free RL to any no-regret online learning. While Ross et al. mainly focus on imitation learning, Ross and Bagnell consider the finite-horizon case and uses a generic no-regret online learner that may result in a worse regret guarantee. Very recently, Cheng et al. exploit optimistic mirror descent to speed up policy optimization in RL, but do not provide a regret analysis in average-reward case.

AAPI is also similar to the conservative policy iteration works, which attempt to stabilize API by regularizing each policy towards the previous policy. In particular, Neu et al. identify several state-of-the-art entropy-regularized RL algorithms as approximate variants of mirror descent, and Shani et al. provides convergence rates for a mirror descent like algorithm in the discounted setting. Vieillard et al. provides a systematical analysis of regularization in RL. To the best of the authors' knowledge, none of these works use adaptive data-dependent learning rate to accelerate policy learning.

## PROBLEM SETTING

We first introduce some notation. We use $\Delta_{\mathcal{S}}$ to denote the space of probability distributions defined on the set $\mathcal{S}$ and write ${\lbrack d\rbrack} = {\{ 1,2,\ldots,d\}}$. For vectors ${u,v} \in {\mathbb{R}}^{d}$, we define the weighted $\ell_{2}$-norm as ${\| v\|}_{u}^{2} = {\sum_{i = 1}^{d}{u_{i}v_{i}^{2}}}$ and $\ell_{\infty}$-norm as ${\| u\|}_{\infty} = {\max_{j \in {\lbrack d\rbrack}}u_{j}}$. In general, we treat discrete distributions as row vectors.

Infinite-horizon undiscounted MDPs are often characterized by a finite state space $\mathcal{X}$, a finite action space $\mathcal{A}$, a reward function $r:{{\mathcal{X} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$, and a transition probability function $P:{{\mathcal{X} \times \mathcal{A}}\rightarrow\Delta_{\mathcal{X}}}$. The agent does not know the transition probability and the reward function in advance. A policy $\pi:{\mathcal{X}\rightarrow\Delta_{\mathcal{A}}}$ is a mapping from a state to a distribution over actions. Let ${\{{(x_{t}^{\pi},a_{t}^{\pi})}\}}_{t = 1}^{\infty}$ denote the state-action sequence obtained by following policy $\pi$. The expected average reward of policy $\pi$ is defined as The agent interacts with the environment as follows: at each round $t$, the agent observes a state $x_{t} \in \mathcal{X}$, chooses an action $a_{t} \sim \pi_{t}{(\cdot |x_{t})}$, and receives a reward $r{(x_{t},a_{t})}$. The environment then transitions to the next state $x_{t + 1}$ with probability ${\mathbb{P}}{(\left. x_{t + 1} \middle| {x_{t},a_{t}} \right.)}$. The initial state $x_{1}$ is randomly generated from some unknown distribution. Let $\pi^{\ast}$ be an unknown fixed policy. The regret of an algorithm with respect to this fixed policy is defined as where $a_{t} \sim \pi_{t}{(\cdot |x_{t})}$. The learning goal is to find an algorithm that minimizes the long-term regret $R_{T}$. Note that $R_{T}$ is still a random variable so we will bound it with high probability.

For each policy $\pi$, we denote $\mathcal{P}^{\pi} \in {\mathbb{R}}^{{|\mathcal{X}|} \times {|\mathcal{X}|}}$ to be the Markov chain induced by $\pi$, where the component ${(\mathcal{P}^{\pi})}_{x,x'}$ is the transition probability from $x$ to $x'$ under $\pi$, i.e. ${(\mathcal{P}^{\pi})}_{x,x'} = {\sum_{a \in \mathcal{A}}{\pi{(\left. a \middle| x \right.)}P{(\left. x' \middle| {x,a} \right.)}}}$. For a distribution $\mu$ over $\mathcal{X}$, we let $\mu\mathcal{P}^{\pi}$ be the distribution over $\mathcal{X}$ that results from executing the policy $\pi$ for one step after the initial state is sampled from $\mu$. A stationary distribution $\mu_{\pi}$ of a policy $\pi$ over states satisfies ${\mu_{\pi}\mathcal{P}^{\pi}} = \mu_{\pi}$. For a policy $\pi$, its expected reward can be expressed as In this work, we focus on ergodic MDPs, a sub-class of weakly communicating MDPs. An MDP is ergodic if the Markov chain induced by any policy $\pi$ is both irreducible and aperiodic, which means any state is reachable from any other state by following a suitable policy. It is well-known that all ergodic MDPs have an unique stationary state distribution, and so $\mu_{\pi}$ and $\lambda_{\pi}$ are well-defined. In addition, ergodic MDPs have a finite *mixing time*, defined below.

### Definition 2.1

The mixing time of ergodic MDPs is defined as $t_{\text{mix}}:=$ that characterizes how fast MDPs reach stationary distributions from any state under any policy.

Finally, we define the value function under policy $\pi$ as where ${\mathbb{E}}^{\pi}$ is with respect to the sample path induced by $\pi$. The state-action value function $Q_{\pi}{(x,a)}$ and $V_{\pi}{(x)}$ can also be defined as the unique solutions to the Bellman equation:

## Algorithm

AAPIis a variant of approximate policy iteration and it proceeds in phases. Suppose the total number of rounds is $T$. We divide $T$ into $K$ phases of length $\tau = {T/K}$ and assume $\tau$ is an integer for simplicity. Within each phase, our algorithm performs two tasks: policy evaluation and policy improvement.

Policy evaluation. In each phase $k \in {\lbrack K\rbrack}$, the algorithm executes the current policy $\pi_{k}$ for $\tau$ time steps, and computes an estimate ${\hat{Q}}_{\pi_{k}}$ of the true action-value function $Q_{\pi_{k}}$. We leave unspecified the value function estimation method $\mathcal{G}$; for example, one can use incremental algorithms, or both on-policy and off-policy data. AAPI is better interpreted as a learning schema. Our regret analysis will require that longer phase lengths lead to better estimates (made precise in Lemma 5.3).

Policy improvement. For each state $x \in \mathcal{X}$, the policy improvement step takes the form of the adaptive optimistic follow-the-regularized-leader (AO-FTRL) update: (See Step 3 in Section 5 for a generic description of AO-FTRL.) The terms in Eq. are as follows: The estimates ${{\hat{Q}}_{\pi_{s}}{(x, \cdot)}} \in {\mathbb{R}}^{|\mathcal{A}|}$ are the loss functions fed to the AO-FTRL algorithm. $\mathcal{R}{(f)}$ is the negative entropy regularizer, and $\mathcal{F}$ is the probability simplex.

The side-information ${M_{k + 1}{(x, \cdot )}} \in {\mathbb{R}}^{|\mathcal{A}|}$ is a vector computable based on past information and being predictive of the next loss ${\hat{Q}}_{\pi_{k + 1}}{(x, \cdot )}$. Since the policies are expected to change slowly due to the nature of exponential-weight-average type algorithms, we set ${M_{k + 1}{(x, \cdot )}} = {{\hat{Q}}_{\pi_{k}}{(x, \cdot )}}$ (better guesses such as off-policy estimates can be used if available).

The choice of learning rate $\eta_{k}{(x)}$ is crucial both theoretically and empirically. In particular, we choose $\eta_{k}{(x)}$ in a data-dependent fashion as A notable feature of $\eta_{k}{(x)}$ is that it is also state-dependent. Intuitively, for the choice ${M_{s}{(x, \cdot)}} = {{\hat{Q}}_{\pi_{s - 1}}{(x, \cdot)}}$, the adaptive state-dependent learning rate results in a more exploratory policy for the states on which there is more disagreement between the past consecutive action-value functions.

Based , the next policy is a Boltzmann distribution (a consequence of negative entropy regularizer) over the sum of all past state-action value estimates and the side-information:

### Remark 3.1

AAPIis similar to the Politex algorithm Abbasi-Yadkori et al., where the main difference is that Politex sets the next policy to ${\pi_{k + 1}{(\left. a \middle| x \right.)}} \propto {\exp{({\eta^{- 1}{\sum_{s = 1}^{k}{\hat{Q}}_{\pi_{s}}}})}}$ in the improvement step. We demonstrate that the use of side-information and adaptive learning rates improves both the theoretical guarantees (Theorem 4.5. ‣ 4 ANALYSIS")) and empirical performance (Section 6) over Politex. The overall algorithm is summarized in Algorithm 1.

1: Input: phase length τ, number of phase K, initial state x0, turning parameter η, value function estimation algorithm 𝒢. 5: Execute πk for τ time steps and collect dataset 𝒟k. 6: Estimate Q̂πk from 𝒟1, …, 𝒟k using 𝒢. 7: Calculate adaptive learning rate: 9: Update next policy as: Algorithm 1 Adaptive approximate policy iteration (AAPI)

## ANALYSIS

To derive a regret bound for Algorithm 1, we decompose the cumulative regret (2.1) as follows: The first term captures the sum of differences between observed rewards and their long term averages. If policies are changing slowly, or if they are kept fixed for extended periods of time, we expect this term to capture the noise in the regret. The second term is called *pseudo-regret* in literature. It measures the difference between the expected reward of a fixed policy and the policies produced by the algorithm.

We first impose a condition on the quality of policy evaluation at each phase. For a probability distribution $\mu$ on $\mathcal{X}$ and a stochastic policy $\pi$, define $\mu \otimes \pi$ to be the distribution on $\mathcal{X} \times \mathcal{A}$ that puts the probability mass $\mu{(x)}\pi{(\left. a \middle| x \right.)}$ on pair ${(x,a)} \in {\mathcal{X} \times \mathcal{A}}$. Recall that $\mu_{\pi^{\ast}}$ is the stationary distribution of $\pi^{\ast}$ over the states.

### Condition 4.1

For each phase $k \in {\lbrack K\rbrack}$, denote $D_{\pi_{k}} = {{\hat{Q}}_{\pi_{k}} - Q_{\pi_{k}}}$. We assume the following holds with probability $1 - \delta$, where $\varepsilon_{0}$ is the irreducible approximation error and $\overset{\sim}{C}$ is a problem dependent constant. Additionally, there exists a constant $b$ such that ${{\hat{Q}}_{\pi_{k}}{(x,a)}} \in {\lbrack b,{b + Q_{\max}}\rbrack}$ for any pair ${(x,a)} \in {\mathcal{X} \times \mathcal{A}}$ and $k \in {\lbrack K\rbrack}$.

### Remark 4.2

The problem dependent constant $\overset{\sim}{C}$ will in general depend on $d,t_{\text{mix}},\mu_{\pi^{\ast}},\mu_{\pi_{k}}$. Here, $d$ is the dimension of the representation (e.g. ${|\mathcal{X}|}{|\mathcal{A}|}$ for the tabular case, or number of features for the linear value function case).

### Remark 4.3

The requirement for the $\mu_{\pi^{\ast}} \otimes \pi^{\ast}$-norm and $\mu_{\pi^{\ast}} \otimes \pi_{k}$-norm has been shown to hold, for example, with linear value function approximation using the LSPE algorithm, under Assumptions B.1. ‣ Appendix B Linear value function approximation")-B.3. ‣ Appendix B Linear value function approximation") given in the Appendix. Lemma B.4. ‣ Appendix B Linear value function approximation") in the Appendix shows that the requirement for $\ell_{\infty}$-norm can also be satisfied, for example, with linear value functions, under similar conditions.

### Remark 4.4

The estimation error generally depends on the mismatch between distributions $\mu_{\pi_{k}}$ and $\mu_{\pi^{\ast}}$. With value functions linear in features ${\phi{(x,a)}} \in {\mathbb{R}}^{d}$, this mismatch depends on the spectra of matrices ${\mathbb{E}}_{\nu}{\lbrack{\phi{(x,a)}\phi{(x,a)}^{\top}}\rbrack}$ for different distributions $\nu$, and need not scale in the number of state-action pairs. See Assumption A4 in Abbasi-Yadkori et al. for a more detailed explanation.

### Theorem 4.5 (Main result)

Consider an ergodic MDP and suppose Condition 4.1 holds. By choosing the phase length $\tau = {{({{\overset{\sim}{C}/\rho}t_{\text{mix}}^{3}})}^{2/3}T^{2/3}}$, we have with probability at least $1 - {1/T}$, where $\rho$ is the distribution mismatch coefficient that has used in previous work and $\overset{\sim}{\mathcal{O}}{(\cdot)}$ hides universal constants and poly-logarithmic factors.

### Remark 4.6

It is worth comparing the above result with the regret bound presented in Abbasi-Yadkori et al.. Ignoring the irreducible error $\varepsilon_{0}$, we improve the leading order of their general result (Corollary 4.6 in Abbasi-Yadkori et al. ) from $\overset{\sim}{O}{(T^{3/4})}$ to $\overset{\sim}{O}{(T^{2/3})}$. When specialized to linear value function approximation where $\overset{\sim}{C}$ scales with $d^{1/2}$ (Theorem 5 in Abbasi-Yadkori et al. ), we improve their results from $\overset{\sim}{O}{({d^{1/2}T^{3/4}})}$ to $\overset{\sim}{O}{({d^{1/3}T^{2/3}})}$.

### Remark 4.7

It is worth to mention that Wei et al. obtains $\overset{\sim}{O}{(\sqrt{T})}$ regret in terms of *expected regret* in the tabular case for ergodic MDPs while we consider *high-probability regret*. In particular, their analysis does not account for the estimation and approximation errors in Q-functions that will significantly complicate the analysis and result in a worse regret bound.

## PROOF SKETCH

In this section, we provide a proof sketch for Theorem 4.5. ‣ 4 ANALYSIS"). Technical details are deferred to Appendix A. At a high level, we bound the two terms in the regret decomposition Eq. (4.1) separately. While the first term is bounded by the fast mixing condition, the second term is split into the regret due to value function estimation error and the regret due to online learning reduction.

Step 1: fast mixing. To bound the first term in Eq. (4.1), we require the following uniform fast mixing condition, which is used frequently in online MDP literature. Note that ergodic MDPs that this paper focuses on automatically satisfy this condition.

### Condition 5.1 (Uniform fast mixing)

There exists a number $t_{\text{mix}} > 0$ such that for any policy $\pi$ and any pair of distributions $\mu$ and $\mu'$ over $\mathcal{X}$, it holds that The following lemma provides upper bounds for the first term (see e.g. Lemma 4.4 in Abbasi-Yadkori et al. for a proof).

### Lemma 5.2

Suppose that Condition 5.1. ‣ 5 PROOF SKETCH") holds. The following inequality holds with probability at least $1 - \delta$, where $K$ is the number of phases.

Step 2: decomposition. We bound the second term (pseudo regret) in Eq. (4.1). Since the policy is only updated at the end of each phase of length $\tau$ (see line 9 in Algorithm 1), we have $\pi_{t} = \pi_{k}$ for $t \in {\{{\tau{({k - 1})}},\ldots,{\tauk}\}}$. Thus, the pseudo-regret term can be rewritten as We slightly abuse the notation by writing ${Q_{\pi}{(x,\pi')}} = {\sum_{a}{\pi'{(\left. a \middle| x \right.)}Q_{\pi}{(x,a)}}}$. In particular, $Q_{\pi}{(x,\pi)}$ is exactly the value function $V_{\pi}{(x)}$ by Definition 2.2. Applying the performance difference lemma (Lemma C.1. ‣ Appendix C Supporting lemmas") in the supplementary material), we have Bridging by empirical estimations, we decompose (5.2) into $R_{1T} + R_{2T}$, where Step 3: estimation error. The term $R_{1T}$ quantifies the regret incurred in the policy evaluation step due to the estimation error and function approximation error of Q-function in each phase. It can be bounded as in Theorem 4.1 of Abbasi-Yadkori et al. under similar assumptions, which we reproduce here for completeness.

### Lemma 5.3

Suppose Condition 4.1 holds. Then with probability at least $1 - \delta$.

Step 4: online learning reduction. Minimizing $R_{2T}$ can be cast into an online learning problem, and this observation determines the choice of our algorithm. Previous work has tackled this subproblem using mirror descent, resulting in $\overset{\sim}{O}{(T^{3/4})}$ regret after optimizing $\tau$ ignoring the irreducible error $\varepsilon_{0}$. Here we instead use the AO-FTRL framework, which allows us to show an improved $\overset{\sim}{O}{(T^{2/3})}$ regret bound. As we show, the reason we can benefit from optimism is that the losses (Q-functions) change slowly, and we carefully transfer this knowledge to the adaptive learning rate. This is the main technical contribution of the paper.

First, we state the framework of AO-FTRL and its regret results. Let ${\{ q_{t}\}}_{t = 1}^{T}$ be a sequence of loss vectors and let ${\{ f_{t}\}}_{t = 1}^{T} \subseteq \mathcal{F}$ be a sequence of prediction vectors, where $\mathcal{F}$ is the probability simplex. At the beginning of each round, the algorithm receives a side-information vector $M_{t}$. In literature, ${\{ M_{s}\}}_{s = 1}^{t}$ are also called predictable sequences, and the algorithm can be seen as a way of utilizing prior knowledge about loss sequences. The algorithm then selects an action $f_{t}$, and suffers a cost $\langle f_{t},q_{t}\rangle$. The goal of this online learning problem is to minimize the cumulative regret with respect to the best action in hindsight $f^{\ast}$, defined as ${\overset{\sim}{R}}_{T} = {\sum_{t = 1}^{T}{\langle{f_{t} - f^{\ast}},q_{t}\rangle}}$.

Let $\mathcal{R}:{\mathcal{F}\rightarrow{\mathbb{R}}}$ be a 1-strongly convex regularizer on $\mathcal{F}$ with respect to some norm $\parallel \cdot \parallel$ and denote by $\parallel \cdot \parallel_{\ast}$ its dual norm. Initialize $f_{1} = {\operatorname{argmin}_{f \in \mathcal{F}}{\mathcal{R}{(f)}}}$. At each round $t$, AO-FTRL has the following form: where $\eta$ is an absolute constant. It's easy to see that $\eta_{t}$ is non-decreasing. For simplicity, we assume ${M_{1} = 0},{\eta_{0} = 0}$. Next lemma provides a generic regret bound for AO-FTRL. The detailed proof is deferred to Appendix A.2 ‣ Appendix A Proofs of main results") in the supplementary material.

### Lemma 5.4

Choose $\eta = \sqrt{{2/\mathcal{R}}{(f^{\ast})}}$ and denote $R_{\max} = {{\max_{f}\mathcal{R}}{(f)}}$. The cumulative regret for AO-FTRL is upper-bounded by

### Remark 5.5

Unlike the AO-FTRL analyses of Rakhlin and Sridharan; Mohri and Yang, but similarly to, e.g., the analysis of Joulani et al., Eq. (5.5) has a key negative term (at the expense of a slightly larger constant factor in the main positive term). These negative terms, which are retained from a tight regret bound on the forward regret of AO-FTRL, track the evolution of the policy $f_{t}$. With the proper choice of $M_{t}$, the norm terms ${\|{q_{t} - M_{t}}\|}_{\ast}$ will also be controlled by the evolution of $f_{t}$ (see Lemma 5.6. ‣ 5 PROOF SKETCH")), and the aforementioned negative terms allow us to greatly reduce the contribution of the norm terms ${\|{q_{t} - M_{t}}\|}_{\ast}$ to the overall regret.

The reason that minimizing $R_{2T}$ can be cast into an online learning problem is as follows. By the definition of $Q_{\pi}{(x,\pi')}$ in Step 2, we rewrite $R_{2T}$ in (5.3) as For each state $x \in \mathcal{X}$, we view $\pi_{k}{(\cdot |x)}$ as the prediction vector and ${\hat{Q}}_{\pi_{k}}{(x, \cdot)}$ as the loss vector. The equivalence between $R_{2T}$ and ${\overset{\sim}{R}}_{T}$ enables us to utilize the generic regret bound for AO-FTRL in Lemma 5.4 for each individual state.

Next, we will show that under some conditions, the change in the true Q values can be bounded by the change of policies. This is a unique property of ergodic MDPs that allows us to benefit from the negative term in (5.5). To ensure $Q_{\pi}$ is unique, we assume ${\sum_{x}{\mu_{\pi}{(x)}V_{\pi}{(x)}}} = 0$.

### Lemma 5.6 (Relative Q-function Error)

For any two successive policies $\pi_{k - 1}$ and $\pi_{k}$, the following holds for any state-action pair $(x,a)$, The detailed proof of Lemma 5.6. ‣ 5 PROOF SKETCH") is deferred to Appendix A.4. Combining the result in Lemmas 5.4 and 5.6. ‣ 5 PROOF SKETCH"), we can derive the following lemma.

### Lemma 5.7

Suppose Condition 4.1 holds. Then the following upper bound holds with probability at least $1 - \delta$, where $\lesssim$ hides universal constant factors.

The detailed proof of Lemma 5.7 is deferred to Appendix A.3 in the supplementary material. Finally, we optimize $\tau$ to be ${({{\overset{\sim}{C}/\rho}t_{\text{mix}}^{3}})}^{2/3}T^{2/3}$ and reach our conclusion.

### Remark 5.8

Within the upper bound (5.6), ${{{\overset{\sim}{C}}^{2}{\log{({1/\delta})}}}/\tau} + \varepsilon_{0}^{2}$ stands for the approximation error and estimation error per round. When value functions can be computed exactly (known MDP) and for phase length $\tau = 1$, the online learning reduction regret for AAPI scales logarithmically in the number of phases $K$, while POLITEX scales as $\sqrt{K}$. This is the main reason that we can improve the regret from $\overset{\sim}{O}{(T^{3/4})}$ to $\overset{\sim}{O}{(T^{2/3})}$.

## EXPERIMENTS

In this section we provide an empirical evaluation of AAPIon several environments. We compare AAPIto POLITEX, which corresponds to updating policies using a mirror descent rule rather than AO-FTRL. We also evaluate RLSVI (, Algorithms 1 and 2 with $\sigma^{2} = 1$ and tuned $\lambda$), where policies are greedy w.r.t. a randomized estimate of $Q_{\ast}$. Overall, we find that AAPI performs well in discrete-state environments such as DeepSea, whereas the adaptive per-state learning rate is less helpful in environments such as CartPole with continuous states and smooth dynamics.

Figure 1: Evaluation on a tabular ergodic MDP.

Figure 2: Evaluation on DeepSea environments of different sizes.

Figure 3: Evaluation on the CartPole environment.

We approximate all value functions using least-squares Monte Carlo, i.e. linear regression from state-action features to empirical returns. For MDPs with a large or continuous state space $\mathcal{X}$, updating per-state learning rates can be impractical. Instead, we store the weights of past Q-functions in memory, and for each state in the trajectory, we compute the learning rate using a subset of $n_{k} \leq 30$ randomly-selected past weight vectors (we correct the scale of the estimate by multiplying with $\sqrt{k/n_{k}}$. With rich function approximation such that neural networks, one can keep a fixed buffer with a subset of the previous Q-functions (chosen in a randomized way, or keeping the most recent K networks as in Abbasi-Yadkori et al. ), or train distillation networks that summarize the sum of previous Q-functions. Another possibility is to parameterize $\pi_{k}$ and optimize the objective w.r.t. the parameters. For Boltzmann policies, we tune the constant $\eta$ for the learning rate $\eta_{k}{(x)}$ in the range $\lbrack 0.01,100\rbrack$. For each environment and algorithm we evaluate $- {\sum_{s = 1}^{t}{r_{t}/t}}$ and plot the mean and standard deviation over 50 runs. The environments we evaluate on are as follows.

Tabular ergodic MDPs. We consider a simple tabular MDP where ${r{(1,a)}} = 1$, ${r{(x,a)}} = 0$ for $x \neq 1$. On any action in state 1, the environment transitions to a randomly chosen state $x \neq 1$. On action 1 in a state $x \neq 1$, the environment transitions to state $x - 1$ with probability 0.9, and to a randomly chosen state with probability 0.1. On all other actions in $x \neq 1$, the environment transitions to a randomly chosen state. We represent state-action pairs using one-hot indicator vectors of size ${|\mathcal{X}|}{|\mathcal{A}|}$, and experiment with different sizes of the state and action spaces $\mathcal{X}$ and $\mathcal{A}$.

DeepSea. In the DeepSea environment, states comprise an $N \times N$ grid, and there are two actions. The environment transitions and costs are deterministic. The agent starts in the top-left cell $$. On action 0, the agent transitions down and left, and receives reward 0. On action 1, the agent transitions down and right, and receives reward -1. On transitioning to the bottom-right cell $({N - 1},{N - 1})$, the agent receives reward $2N$. The infinite-horizon version of the environment wraps the environment around the vertical axis. An optimal strategy first takes the action 1 $N$ times (to get to $({N - 1},{N - 1})$) and then takes an equal number of 0 and 1 actions, and has expected average reward close to $1.5$. A simple strategy that always takes action 1 has an average reward $1$, and a suboptimal strategy that only takes action 0 has an average reward of $0$. We represent states as length-$2N$ vectors containing one-hot indicators for each grid coordinate, and estimate linear $Q$-functions.

CartPole. In the CartPole environment, the goal is to balance an inverted pole attached by an unactuated joint to a cart, which moves along a frictionless rail. There are two actions, corresponding to pushing the cart to the left or right. The observation consists of the position and velocity of the cart, pole angle, and pole velocity at the tip. There is a reward of +1 for every timestep that the pole remains upright. The episodic version of the environment ends if the pole angle is more than 15 degrees from vertical, if the cart moves more than 2.4 units from the center, or after 200 steps. In the infinite-horizon version, if the episode ends after $h$ steps, we return a reward of $h - 200$ and reset. For this task, in addition to the given observation, we extract multivariate Fourier basis features Konidaris et al. of order 4.

Discussion. In most of our experiments, adaptive learning rate speeds up the convergence of approximate policy iteration, compared to using a constant learning rate as in Politex. The adaptive per-state learning rate is less helpful in CartPole, possibly because observations are continuous and dynamics are smooth, so there is higher generalization across states.

## CONCLUSION

We have presented AAPI, a model-free learning scheme that can work with function approximation, and enjoys a $\overset{\sim}{O}{(T^{2/3})}$ regret guarantee in infinite-horizon undiscounted, ergodic MDPs. AAPIimproves upon previous results for this setting by using the slow-changing property of policies in both theory and practice. One direction for future work is improving the policy evaluation stage. While we estimate each value function solely using the $\tau$ on-policy transitions, better estimates can potentially be obtained using all data. Using more sophisticated side-information, such as a weighted average of past Q-estimates or an off-policy estimate of the Q-function may also be helpful in practice. Other future work may include practical implementations of the algorithm when trained with neural networks that maintain only a subset of past networks in memory; one possible practical approach is given by Vieillard et al..
