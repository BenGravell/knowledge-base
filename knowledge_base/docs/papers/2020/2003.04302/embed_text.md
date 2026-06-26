## Introduction

Reinforcement Learning (RL) is a dynamic learning approach that interacts with the environment and execute actions according to the current state, so that a particular measure of cumulative rewards is maximized. Model-free deep reinforcement learning algorithms have achieved remarkable performance in a range of challenging tasks, including stochastic control, autonomous driving, games, continuous robot control tasks, etc.

Generally, there are two aspects of methods of solving a model-free RL problem: value-based methods such as Q-Learning, SARSA, etc., as well as policy-based methods such as Policy Gradient (PG) algorithm. PG algorithm models the state-to-action transition probabilities as a parameterized family, and the cumulative rewards can be regarded as a function of the parameters. Thus, policy gradient based problem shares a formulation that is analogous to the traditional stochastic optimization problem.

One critical challenge of reinforcement learning algorithms compared to traditional gradient based algorithms lies on the issue of distribution shift, that is, the data sample distribution encounters distributional changes throughout the learning dynamics. To correct this, (an off-policy version of) Policy Gradient (PG) method and Trust Region Policy Optimization (TRPO) method have been proposed as general off-policy algorithms to optimize policy parameters using gradient based methods.^11^1In reinforcement learning literature, on-policy algorithms make use of samples rolled out by the current policy for only once, and hence suffer from high sample complexities. On the contrary, off-policy algorithms in earlier work enjoy reduced sample complexities since they reuse the past trajectory samples. Nevertheless, they are often brittle and sensitive to hyperparameters and hence suffer from reproducibility issues. PG method directly optimizes the policy parameters via gradient based algorithms, and it dates back to the introduction of REINFORCE and GPOMDP estimators that our algorithm is built upon.

The problem of high sample complexity arises frequently in policy gradient based methods due to a combined effect of high variance incurred during the training phase and distribution shift, limiting the ability of model-free deep reinforcement learning algorithms. Such a combined effect signals the potential need of adopting variance-reduced gradient estimators to accelerate off-policy algorithms. Recently proposed variance-reduced policy gradient methods include SVRPG and SRVRPG theoretically improve the sample efficiency over PG. This is corroborated by empirical findings: we observe that the variance-reduced gradient alternatives SVRPG and SRVRPG accelerate and stabilize the training processes, mainly due to their accommodations with larger stepsizes and reduced variances.

Nevertheless compared to the vanilla PG method, one major drawback of the aforementioned variance-reduced policy gradient methods is their alternations between large and small batches of trajectory samples, spelled as the restarting mechanism, so the variance can be effectively controlled. In this paper, we circumvent such a restarting mechanism by introducing a new algorithm named STOchastic Recursive Momentum Policy Gradient (STORM-PG), which utilizes the idea of a recently proposed variance-reduced gradient method STORM and blends with policy gradient methods. STORM is an online variance-reduced gradient method that adopts an exponential moving averaging mechanism that persistently discount the accumulated variance. In the nonconvex smooth stochastic optimization setting, STORM achieves an $O{(\epsilon^{- 3})}$ queries complexity that ties with online SARAH/SPIDER and matches the lower bound for finding an $\epsilon$-first-order stationary point. As a closely related variant, SARAH/SPIDER based stochastic variance-reduced compositional gradient methods also achieve an $O{(\epsilon^{- 3})}$ complexity under a different set of assumptions (hu2019efficient; zhang2019multi). Our proposed STORM-PG algorithm blends such a state-of-the-art variance-reduced gradient estimator with the PG algorithm. Instead of introducing a restarting mechanism in concurrent variance-reduced policy gradient methods, our STORM-PG algorithm guarantees the variance stability by adopting the exponential moving averaging mechanism featured by STORM. In our experiments, we see that the variance stability of our variance-reduced gradient estimator allows our STORM-PG algorithm to achieve a (perhaps surprisingly) overall mean rewards improvement in reinforcement learning tasks.

### Our Contributions

We have designed a novel policy gradient method that enjoys several benign properties, such as using an exponential moving averaging mechanism instead of restarting mechanism to reduce our gradient estimator variance. Theoretically, we prove a state-of-art convergence rate for our proposed STORM-PG algorithm in our setting. Experimentally, our STORM-PG algorithm depicts strikingly desirable performance in many reinforcement learning tasks.

### Notational Conventions

Throughout the paper, we treat the parameters $L_{d}$, $C_{\gamma}$, $R$, $M$, $N$, $\Delta$ and $\sigma$ as global constants. Let $h$ denote the index of steps that the agent takes to interact with the environment and $H$ is the maximum length of an episode. Let $\parallel \cdot \parallel$ denote the Euclidean norm of a vector or the operator norm of a matrix induced by Euclidean norm. For fixed $t \geq 0$, let $\mathcal{B}_{t}$ denotes the batch of samples choosen at the $t$'th iteration and $\mathcal{B}_{0:t} = {\{\mathcal{B}_{0},\mathcal{B}_{1},\ldots,\mathcal{B}_{t}\}}$. $\mathcal{F}_{t}$ is the $\sigma$-algebra generated by $\mathcal{B}_{0:t}$ and ${\mathbb{E}}{\lbrack \cdot \mid \mathcal{F}_{t}\rbrack}$ is the conditional expectation based on samples generated up to the $t$'th iteration. Other notations are explained at their first appearances.

### Organization

The rest of our paper is organized as follows. Section 2 introduces the backgrounds and preliminaries of the policy gradient algorithm. Section 3 formally introduces our STORM-PG algorithm design. Section 4 introduces the necessary definitions and assumptions. Section 5 presents the convergence rate analysis, whose corresponding proof is provided in Section 6. Section 7 conducts experimental comparison on continuous control tasks, and Section 8 concludes our results.

STORM-PG (This paper) Table 1: Sample complexities of comparable algorithms for finding an ϵ-accurate solution.

## Policy Gradient Prelimilaries

In this section we introduce the background of policy gradient and the objective function that our algorithm is based . The basic operation of the PG algorithm is similar to the gradient acsent algorithm with some RL specific gradient estimators. In Section 2.1 we introduce the REINFORCE estimator which is the basis of many follow up PG works. In Section 2.2 we introduce the GPOMDP estimator which further reduces the variance and is the fundation of our algorithm. Finally in Section 2.3 we formulate the probability induced by the policy as a Gaussian distribution, which is a special case adopted in our experiments.

### REINFORCE Estimator

We consider the standard reinforcement learning setting of solving a discrete time finite horizon Markov Decision Process (MDP) $\mathcal{M} = {\{\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma,\rho\}}$ which models the behavior of an agent interacting with a given environment. Let $\mathcal{S}$ be the space of states in the environment, $\mathcal{A}$ be the space of actions that the agent can take, $\mathcal{P}:{{\mathcal{S} \times \mathcal{A}}\rightarrow\mathcal{S}}$ be the transition probability from $s \in \mathcal{S}$ to $s' \in \mathcal{S}$ given $a \in \mathcal{A}$, $R:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ be the reward function of taking action $a \in \mathcal{A}$ at state $s \in \mathcal{S}$, $\gamma$ be the discount factor that adds smaller weights to rewards at more distant future, and $\rho$ be the initial state distribution.

We mainly focuses on in this paper the policy gradient setting where there is a policy $\pi{({a \mid s})}$ as the probability of taking action $a$ given state $s$ such that ${\sum_{a \in \mathcal{A}}{\pi{({a \mid s})}}} = 1$; The policy $\pi{(\cdot \mid s)}$ models the agent's behavior after experiencing the environment's state $s$. Given finite state and action spaces, the policy $\pi{({a \mid s})}$ can be coded in a ${|\mathcal{S}|} \times {|\mathcal{A}|}$ tabular. However when the state/action space is large or countably infinite, we adopt a probability mass function class $\pi_{\mathbf{ξ}}{({a \mid s})}$, parameterized by ${\mathbf{ξ}} \in {\mathbb{R}}^{d}$, as an approximated class of functions to such a tabular. Given a policy $\pi_{\mathbf{ξ}}{(\cdot \mid s)}$, the probability of a trajectory $\tau$ can be expressed in terms of the transition probability $p{({s' \mid {s,a}})}$ and the policy $\pi_{\mathbf{ξ}}{({a \mid s})}$: where the trajectory $\tau:={(s_{0},a_{0},s_{1},a_{1},\ldots,s_{H},a_{H})}$ is the sequence that alters between states and actions, and $H$ is the maximum length (episode) of all trajectories.

Policy gradient algorithms target to maximize the expected sum of discounted rewards over trajectories $\tau$: where the expectation is taken over a parameterized probability distribution $p{(\cdot \mid {\mathbf{ξ}})}$ with parameter $\mathbf{ξ}$, as is defined. Standard algorithm for maximizing is the gradient descent algorithm (GD) which updates ${\mathbf{ξ}}_{t}$ on the direction of the objective gradient with a fixed learning rate $\eta$: where the gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$ can be calculated as follows by combining and: | | | ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$ | | \(3\) | | | | $= {\nabla_{\mathbf{ξ}}{\int{p{({\tau \mid {\mathbf{ξ}}})}R{(\tau)}{d\tau}}}} = {\int{{\nabla_{\mathbf{ξ}}p}{({\tau \mid {\mathbf{ξ}}})}R{(\tau)}{d\tau}}}$ | | | | | | $= {\int{\frac{{\nabla_{\mathbf{ξ}}p}{({\tau \mid {\mathbf{ξ}}})}}{p{({\tau \mid {\mathbf{ξ}}})}}R{(\tau)}p{({\tau \mid {\mathbf{ξ}}})}{d\tau}}}$ | | | | | | ${= {{\mathbb{E}}_{\tau \sim p{(\cdot \mid {\mathbf{ξ}})}}\left\lbrack {{{\nabla_{\mathbf{ξ}}\log}p}{({\tau \mid {\mathbf{ξ}}})}R{(\tau)}} \right\rbrack}}.$ | | | To avoid the costly (or infeasible in the case of infinite spaces) full gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$ computations which requires sampling all possible trajectories, we adopt its Monte Carlo estimator as: where the trajectories $\tau_{i}$ are generated according to the trajectory distribution $p{(\cdot \mid {\mathbf{ξ}})}$. The above estimator in policy gradient is known as the REINFORCE estimator.

### GPOMDP Estimator

One of the disadvantage of REINFORCE estimator lies on its excessive variance of trajectories introduced throughout the end of the episode. Using a simple fact that for any constant $b$, ${{\mathbb{E}}{\lbrack{{{\nabla\log}\pi_{\mathbf{ξ}}}{({a \mid s})}b}\rbrack}} = 0$ and the observation that rewards obtained before step $h$ is irrelevant with $\pi{({a \mid s})}$ after step $h$, the REINFORCE estimator can be substituted by the following GPOMDP unbiased estimator which uses a baseline to reduce the variance: where for each $h \in {\lbrack 0,{H - 1}\rbrack}$, $b_{h}$ is a constant. Throughout this paper, we use $d_{i}{({\mathbf{ξ}})}$ to refer to the unbiased GPOMDP estimator of ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$: | | | ${= {\sum\limits_{h = 0}^{H - 1}{\left({\sum\limits_{t = 0}^{h}{{{\nabla\log}\pi_{\mathbf{ξ}}}{({a_{t} \mid s_{t}})}}} \right)\left({{\gamma^{h}r{(s_{h},a_{h})}} - b_{h}} \right)}}}.$ | | | where $(a_{t},s_{t})$ are action-state pairs along the trajectory $\tau_{i}$. We adopt a variance-reduced version of GPOMDP estimator throughout the end of this paper.

### Gaussian Policy

Finally, we introduce the Gaussian policy setting. In control tasks where the state and action spaces can be continuous, one choice of the policy function class is the Gaussian family: where $\sigma^{2}$ is the fixed variance parameter and ${\psi{(s)}}:{\mathcal{S}\rightarrow{\mathbb{R}}^{d}}$ is a bounded feature mapping from the state space $\mathcal{S}$ to ${\mathbb{R}}^{d}$. As the readers will see, the Gaussian policy satisfies all assumptions in Section 4; more detailed discussions can be found in Xu et al., Xu et al. and Papini et al..

## STORM-PG Algorithm

Recall our goal is to solve the general policy optimization problem: and $d_{i}{({\mathbf{ξ}})}$ defined in is an unbiased estimator of the true gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$. The simplest algorithm, stochastic gradient ascent, updates the iterates as where $i$ is chosen randomly from a data set sampled with the current distribution $\pi_{\mathbf{ξ}}$. To further unfold this expression, we note that ${d_{i}{({\mathbf{ξ}})}} = {\sum_{h = 0}^{H - 1}{d_{i,h}{({\mathbf{ξ}})}}}$ where To remedy the distribution shift issue in reinforcement learning tasks, we introduce an importance sampling weight between trajectories generated by $\mathbf{ξ}$ and the ones generated by ${\mathbf{ξ}}'$ as where $\tau_{i,h}$ is a trajectory generated by $p{(\cdot \mid {\mathbf{ξ}}')}$ truncated at time $h$. To further reduce the variance introduced by the randomness in $i$, SVRG introduced a variance-reduced estimator estimator of ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}$ where $\overset{\sim}{\mathbf{ξ}}$ is a fixed point calculated once every $q$ steps and $\overset{\sim}{u}$ is a fixed estimation of the gradient at point $\overset{\sim}{\mathbf{ξ}}$. Instead of the aforementioned SVRG-type estimator which was adopted by Xu et al., Papini et al. adopts instead a recursive estimator to track the gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t + 1})}$ at each time. In above, $\mathbf{g}_{0}$ is scheduled to be updated once every $q$ iterations as a large-batch estimated gradient.

### STORM-PG Estimator

In this paper, we propose to use the STORM estimator as introduced, which is essentially an exponential moving average SARAH estimator When $\alpha = 1$, the STORM-PG estimator reduces to the vanilla stochastic gradient estimator and when $\alpha = 0$, the STORM-PG esimator reduces to the SARAH estimator. As our $\alpha$ is chosen between $$, the estimator is a combination of an variance reduced biased estimator and an unbiased estimator. In addition, can be rewritten as which can be interpreted as an exponentially decaying mechanism via a factor of $({1 - \alpha})$. We can see later in the proof of the convergence rate that the estimation error ${\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla L}{({\mathbf{ξ}})}}}\|}^{2}$ can be controlled by a proper choice of $a$ while in SARAH case to control the convergence speed, the batch size $B$ or the learning rate $\eta$ have to be tuned accordingly. This allows us to operate a single-loop algorithm instead of a double-loop algorithm. We only need a large batch to estimate $\mathbf{g}_{0}$ once, and do mini-batch or single batch updates till the end of the algorithm. This estimator hinders the accumulation of estimation error in each round.

We describe our STORM-PG as in Algorithm 1.

Input: Number of epochs T, initial batch size S0, step size η, mini-batch size B, initial parameter ξ0 Sample S0 trajectories {τi}i ∈ 𝒮0 from p(⋅ ∣ ξ0) Calculate an initial estimate of ∇ξL (ξ0): $$\mathbf{g}_{0} = {\frac{1}{S_{0}}{\sum\limits_{i \in \mathcal{S}_{0}}{d_{i}{({\mathbf{ξ}}_{0})}}}}$$ Sample B trajectories {τi}i ∈ ℬ from p(⋅ ∣ ξt + 1) ${({1 - \alpha})}\left({\frac{1}{B}{\sum\limits_{i \in \mathcal{B}}\left\lbrack {\mathbf{g}_{t} - {d_{i}^{{\mathbf{ξ}}_{t + 1}}{({\mathbf{ξ}}_{t})}}} \right\rbrack}} \right)$ $+ {\frac{1}{B}{\sum\limits_{i \in \mathcal{B}}{d_{i}{({\mathbf{ξ}}_{t + 1})}}}}$ Output $\overset{\sim}{\mathbf{ξ}}$ chosen uniformly at random from {ξt}t = 0T − 1

## Definitions and Assumptions

In this section, we make several definitions and assumptions necessary for analyzing the convergence of the STORM-PG Algorithm. First of all, we define the $\epsilon$-accurate solution of a policy gradient algorithm:

### Definition 1 ($\epsilon$-accurate solution)

We call ${\mathbf{ξ}} \in {\mathbb{R}}^{d}$ an $\epsilon$-accurate solution if and only if We say that an stochastic policy gradient based algorithm reaches an $\epsilon$-accurate solution if and only if where $\hat{\mathbf{ξ}}$ is the output after the algorithm's iteration number $T$, and the expectation is taken over the randomness in $\{\tau_{i}\}$ at each iteration.

To bound the norm of the gradient estimation $\|{d_{i}{({\mathbf{ξ}})}}\|$, we need assumptions on the norm of rewards $\|{r{(s,a)}}\|$ and the norm of gradient ${{\nabla_{\mathbf{ξ}}\log}\pi_{\mathbf{ξ}}}{({a \mid s})}$ as follows:

### Assumption 2 (Boundedness)

We assume that the reward and the gradient of $\log\pi_{\mathbf{ξ}}$ are bounded for any $a \in \mathcal{A}$ and $s \in \mathcal{S}$, and there exists a constant $R$ and a constant $M$ such that: for any ${a \in \mathcal{A}},{s \in \mathcal{S}}$.

### Assumption 3 (Smoothness)

There exists a constant $N$ such that for any $a \in \mathcal{A}$ and $s \in \mathcal{S}$:

### Assumption 4 (Finite-variance)

There exists a $\sigma \geq 0$ such that:

### Assumption 5 (Finite IS variance)

For ${{\mathbf{ξ}}_{1},{\mathbf{ξ}}_{2}} \in {\mathbb{R}}^{d}$, use $w{({\tau \mid {{\mathbf{ξ}}_{1},{\mathbf{ξ}}_{2}}})}$ to denote the importance sampling weight ${{p{({\tau \mid {\mathbf{ξ}}_{1}})}}/p}{({\tau \mid {\mathbf{ξ}}_{2}})}$. Then there exists a constant $\phi$ such that: where the variance is taken over $\tau \sim p{(\cdot \mid {\mathbf{ξ}}_{2})}$.

## Convergence Analysis

In this section, we introduce the lemmas neccessary for proving the convergence results of our STORM-PG Algorithm and finally state our main theorem of convergence. We recall that our goal is to achieve an $\epsilon$-accurate solution of function $L{({\mathbf{ξ}})}$, whose gradient can be estimated unbiasedly by $d_{i}{({\mathbf{ξ}})}$. First of all, given Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), we can derive the boundedness, Liptchizness of $d_{i}{({\mathbf{ξ}})}$ and the smoothness of $L{({\mathbf{ξ}})}$, which are necessary conditions for proving convergence of nonconvex stochastic optimization problems. From the definition in equation, $d_{i}{({\mathbf{ξ}})}$ can be written as a linear combination of ${{\nabla_{\mathbf{ξ}}\log}\pi_{\mathbf{ξ}}}{({a_{h} \mid s_{h}})}$: Similarily, ${\nabla_{\mathbf{ξ}}d_{i}}{({\mathbf{ξ}})}$ can be written as a linear combination of ${{\nabla_{\mathbf{ξ}}^{2}\log}\pi_{\mathbf{ξ}}}{({a_{h} \mid s_{h}})}$. Using the fact that ${\sum_{h = 0}^{H - 1}{\sum_{t = h}^{H - 1}\gamma^{t}}} \leq {1/{({1 - \gamma})}^{2}}$ and the bound derived in Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), it is direct to see that Equation implies that if we define $L_{d} = \frac{NR}{{({1 - \gamma})}^{2}}$, ${\|{{d_{i}{({\mathbf{ξ}}_{1})}} - {d_{i}{({\mathbf{ξ}}_{2})}}}\|} \leq {L_{d}{\|{{\mathbf{ξ}}_{1} - {\mathbf{ξ}}_{2}}\|}}$ and $L{({\mathbf{ξ}})}$ is $L_{d}$-smooth. With the boundedness and smoothness results, we further estimate the accumulated estimation error $\sum_{t = 0}^{T - 1}{{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$. In Lemma 6). ‣ 5 Convergence Analysis ‣ Stochastic Recursive Momentum for Policy Gradient Methods") below we establish the variance bound of the importance sampling weight:

### Lemma 6 (Lemma A.1 in )

Let Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 5. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") hold. Use $w_{h}{({\tau \mid {{\mathbf{ξ}}_{1},{\mathbf{ξ}}_{2}}})}$ to denote the importance sampling weight ${{p{({\tau_{h} \mid {\mathbf{ξ}}_{1}})}}/p}{({\tau_{h} \mid {\mathbf{ξ}}_{2}})}$. Then there exists a constant $C = {h{({{2hM^{2}} + N})}{({\phi + 1})}}$ such that: where the trajectory $\tau_{h}$ is the trajectory generated following the distribution $p{(\cdot \mid {\mathbf{ξ}}_{2})}$ and truncated up to time $h$. The variance is taken over $\tau \sim p{(\cdot \mid {\mathbf{ξ}}_{2})}$.

The proof of Lemma 6). ‣ 5 Convergence Analysis ‣ Stochastic Recursive Momentum for Policy Gradient Methods") can be found . Combining Lemma 6). ‣ 5 Convergence Analysis ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and Equation, we get the following bound of difference between two consecutive estimations:

### Lemma 7

where $C_{\gamma}$ is a constant depending on $\gamma$.

Lemma 7 shows that the expected squared error between $d_{i}^{{\mathbf{ξ}}_{t + 1}}{({\mathbf{ξ}}_{t})}$ and $d_{i}{({\mathbf{ξ}}_{t + 1})}$ is bounded by the squared distance between ${\mathbf{ξ}}_{t}$ and ${\mathbf{ξ}}_{t + 1}$ by a constant dependent of $\gamma$ while independent of $H$. The specific choice of $C_{\gamma}$ and the proof of Lemma 7 can be found in Appendix A.3.

To estimate the estimation error ${\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}$, we recursively calculate the relation between ${\mathbb{E}}{\|{\mathbf{g}_{t + 1} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t + 1})}}}\|}^{2}$ and ${\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}$ by bringing in the recursive definition of $\mathbf{g}_{t + 1}$ in Equation. The result is shown in Lemma 8 below:

### Lemma 8

Let Assumption 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 4. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 5. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") hold. Suppose that $\mathbf{g}_{t}$ and ${\mathbf{ξ}}_{t}$ are the iteration sequence as defined in Algorithm 1 at time $t$. $L{({\mathbf{ξ}})}$ is the objective function to be optimized. Then the estimation error can be bounded by | | | $\leq {{({1 - \alpha})}^{2}{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}}}\|}^{2}}$ | | | The above lemma shows that the estimation error between $\mathbf{g}_{t + 1}$ and ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t + 1})}$ can be bounded by ${({1 - \alpha})}^{2}$ times the estimation error of the previous iteration $\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}$ plus a factor of the norm of ${\|\mathbf{g}_{t}\|}^{2}$ plus a variance controlling term.

Lemma 9 follows Lemma 8 and is the main ingredients of proving the main theorem:

### Lemma 9

Let Assumption 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 4. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 5. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") hold. Then the accumulated sum of expected estimation error $\sum_{t = 0}^{T - 1}{{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$ satisfies the following inequality: | | | $\leq \frac{2}{\alpha}\left\lbrack \frac{C_{\gamma}^{2}\eta^{2}}{B}\sum\limits_{t = 0}^{T - 1}{\mathbb{E}} \parallel \mathbf{g}_{t} \parallel^{2} + \frac{T\alpha^{2}\sigma^{2}}{B} \right.$ | | | | | | $\left. + {\mathbb{E}}\left\lbrack \parallel \mathbf{g}_{0} - \nabla_{\mathbf{ξ}}L{({\mathbf{ξ}}_{0})} \parallel^{2} \right\rbrack \right\rbrack.$ | | |

### Remark 10

We notice that in the proof of SARAH algorithm we have: | | ${\mathbb{E}}{\|{\mathbf{g}_{t + 1} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t + 1})}}}\|}^{2}$ | $\leq {{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$ | | \(21\) | | | | ${+ {L^{2}\eta^{2}{\mathbb{E}}{\|\mathbf{g}_{t}\|}^{2}}},$ | | | | | $\sum\limits_{t = 0}^{T - 1}{{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$ | $\leq {L^{2}\eta^{2}{\sum\limits_{t = 0}^{T - 1}{\sum\limits_{s = 1}^{t}{{\mathbb{E}}{\|\mathbf{g}_{s - 1}\|}^{2}}}}}$ | | \(22\) | Hence, to control the growth of function value, $\eta$ should be chosen with an order of $\mathcal{O}{(T^{- {1/2}})}$. With infinitely increasing $T$, $\eta$ have to be chosen to be infinitely small. SARAH/SPIDER algorithm uses an restart machenism to remedy for this problem. However in our STORM-PG Algorithm, by introducing a exponential moving average, we bring in a shrinkage term ${({1 - \alpha})}^{2}$ on the accumulation speed of ${\mathbb{E}}{\|\mathbf{g}_{t}\|}^{2}$, allowing the order of $\sum_{t = 0}^{T - 1}{{\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$ to decrease from $T$ to $\frac{1}{\alpha}$.

For $\alpha$, we only need to control $\alpha \geq {4C_{\gamma}^{2}\eta^{2}}$ so that $\eta$ is no longer related with $T$. This allows us to do continuous training without restarting the iterations.

Next we come to our main theorem in this paper, which conclude that after $T$ iterations, the expected gradient norm satisfies a bound described below:

### Theorem 11

Let Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 4. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods")and 5. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") hold. When ${\alphaB} \geq {4\eta^{2}L_{d}^{2}}$, the resulting point after $T$ iterates satisfies: where $\Delta:={{L{({\mathbf{ξ}}_{0})}} - f^{\ast}}$ is a constant representing the function value gap between the initialization and the optimal value $f^{\ast}$.

Choose $S_{0} = {\mathcal{O}{({\sigma^{2}\epsilon^{- 2}})}}$ and $B = {\mathcal{O}{({\sigma^{2}\epsilon^{- 1}})}}$ In the theorem, the $\alpha/B$ term can be controlled by letting $a$ to be proportional with $B/S_{0}$. Thus the third term is of order $\mathcal{O}{(\frac{1}{TB})}$ and the second term is of order $\mathcal{O}{(\frac{1}{S_{0}})}$. If we choose ${S_{0}\alpha} = B$ and $\eta$ is of order $\mathcal{O}{}$, We have that after $T$ iterates, the algorithm reaches a point with expected gradient norm of order $\mathcal{O}{({\frac{1}{T} + \frac{\sigma^{2}}{S_{0}} + \frac{\sigma^{2}}{TB}})}$. Compared with $\mathcal{O}{({\frac{1}{T} + \frac{\sigma^{2}}{S_{0}} + \frac{1}{B}})}$ in and $\mathcal{O}{({\frac{1}{T} + \frac{\sigma^{2}}{S_{0}}})}$ in Xu et al.. However, The sample complexity in Xu et al. is ${\sqrt{T}S_{0}} + {TB}$ while in our algorithm is $S_{0} + {TB}$, which makes the algorithm converges faster.

The detailed analysis of the convergence rate is shown in the next section. Corollary 12 is a direct result after Theorem 11. By controlling the estimated gradient to be in the $\epsilon$-neighborhood of 0, and minimizing $S_{0}$, we get the IFO complexity bound of STORM-PG algorithm:

### Corollary 12

Let Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), 4. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 5. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") hold. Choose $\eta = \frac{\varepsilon}{2\sqrt{6}\sigmaL_{d}}$, $\alpha = \frac{\varepsilon^{2}}{6\sigma^{2}}$, and $S_{0} = {\frac{2\sqrt{3}}{3}\sigma^{2}\varepsilon^{- 2}}$. The IFO complexity of achieving an $\epsilon$-accurate solution is $\mathcal{O}{({{{\DeltaL_{d}} \cdot \frac{\sigma}{\epsilon^{3}}} + \frac{\sigma^{2}}{\epsilon^{2}}})}$.

### Remark 13

In the case of Gaussian policy, one can also obtain an $O{({{({1 - \gamma})}^{- 4}\varepsilon^{- 3}})}$ trajectories sample upper bound to output an $\overset{\sim}{\mathbf{ξ}}$ such that ${{\mathbb{E}}{\|{{\nabla_{\mathbf{ξ}}L}{(\overset{\sim}{\mathbf{ξ}})}}\|}^{2}} \leq \epsilon^{2}$. We omit the detailed discussions and refer the reader to for more details.

## Proof of Main Results

In this section, we prove the main results in this paper. More auxiliary proofs are located in the supplementary section.

### Proof of Theorem 11

### Proof of Theorem 11

By applying the $L_{d}$-smoothness of $L{({\mathbf{ξ}})}$, we get a general estimation bound of $L{({\mathbf{ξ}}_{t + 1})}$: | | | $\geq {{{L{({\mathbf{ξ}}_{t})}} + {\eta{\langle\mathbf{g}_{t},{{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}\rangle}}} - {\frac{\eta^{2}L_{d}}{2}{\|\mathbf{g}_{t}\|}^{2}}}$ | | | | | | ${\overset{(a)}{\geq}L{({\mathbf{ξ}}_{t})}} + {\left({\frac{\eta}{2} - \frac{\eta^{2}L_{d}}{2}} \right){\|\mathbf{g}_{t}\|}^{2}}$ | | | | | | ${+ {\frac{\eta}{2}{\|{{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}\|}^{2}}} - {\frac{\eta}{2}{\|{\mathbf{g}_{t} - {{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}}\|}^{2}}$ | | | | | | ${\overset{(b)}{\geq}L{({\mathbf{ξ}}_{t})}} + {\frac{\eta}{4}{\|\mathbf{g}_{t}\|}^{2}} + {\frac{\eta}{2}{\|{{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}\|}^{2}}$ | | | In $(a)$ we apply the properties of inner product: | | | $\langle\mathbf{g}_{t},{{\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}}\rangle$ | | \(25\) | and in $(b)$ we set ${L_{d}\eta} \leq {1/2}$.

Summing ${L{({\mathbf{ξ}}_{t + 1})}} - {L{({\mathbf{ξ}}_{t})}}$ over $T$. We result in the inequality below: Since the LHS of is $\geq {- \Delta}$, taking its expectation along with in Lemma 9 gives Our pick of $\eta$ satisfies ${4C_{\gamma}^{2}\eta^{2}} \leq {\alphaB}$ so ${1 - \frac{4C_{\gamma}^{2}\eta^{2}}{\alphaB}} \geq 0$ and hence Multiply both sides of Equation by $\frac{2}{\etaT}$: which completes our proof. ∎

### Proof of Corollary 12

### Proof of Corollary 12

For choosing parameters of correct dependency over $\varepsilon$, by Equation, one requires: and we recall that previously we have a lower bound on $\alpha$: ${4C_{\gamma}^{2}\eta^{2}} \leq {\alphaB}$. So finally we choose Bring Equation into Equation we have two lower bounds over $T$ to reach an $\epsilon$-accurate solution: Our goal is to minimize the IFO complexity which is approximately equivalent to Our best choice of $S_{0}$ is obviously $S_{0} = {{2\sigma^{2}\varepsilon^{- 2}}/\sqrt{3}}$. So the IFO complexity of reaching an $\epsilon$-accurate solution is

## Experiments

Figure 1: A comparison between different policy gradient algorithms on Cart-Pole task. The x-axis is the trajectories sampled, the y-axis is the average return of the policy parameter.

In this section, we design a set of experiments to validate the superiority of our STORM-PG Algorithm. Our implementation is based on the rllab library^22^2 and the initial implementation of Papini et al. ^33^3 We test the performance of our algorithms as well as the baseline algorithms on the Cart-Pole^44^4 environment and the Mountain-Car environment.

For baseline algorithms, We choose GPOMDP and two variance-reduced policy gradient algorithms SVRPG and SRVRPG. The results and detailed experimental design are described as follows:

### Comparison of different Algorithms

In SRVRPG and SVRPG, adjustable parameters include the large batch size $S_{0}$, the mini batch size $B$, the inner iteration number $m$ and the learning rate $\eta$. In STORM-PG Algorithm, we have to tune the large batch size $S_{0}$, the momentum factor $a$ and the learning rate $\eta$. Notice that we do not tune the mini batch size $B$ in STORM-PG, and fix it to be the same with the best $B$ tuned on SVRPG, as shown in the theory.

We adaptively choose the learning rate by adam optimizer and learning rate decay. The initial learning rate and decay discount are chosen between $(0.0001,0.1)$ and $(0.5,0.99)$ respectively. The environment related parameters: the discount factor $\gamma$ and the horizon $H$ varies according to tasks. We list the specific choice of $\gamma$, $H$, together with the initial batch size $S_{0}$ and the inner batch size $B$ in the supplementary materials.

We use a Gaussian policy with a neural network with one hidden layer of size 64. For each algorithm in one environment, we choose ten best independent runs to collect the rewards and plot the confidence interval together with the average rewards at each iteration of the training process.

### Cart-Pole environment

The Cart-Pole environment describes the interaction of a pendulum pole attached to a cart. By pushing the cart leftward or rightward, a reward of +1 is obtained by keeping the pole upright and the episode ends when the cart or the pole is too far away from a given center.

Under this environment setting, figure 1 shows the growth of the average return according to the training trajectories.

Figure 2: A comparison between different policy gradient algorithms on Mountain-Car task. The x-axis is the trajectories sampled, the y-axis is the average return of the policy parameter.

From Figure 1, we see that our STORM-PG algorithm ourperforms other variance-reduced policy gradient methods in convergence speed. It reaches the maximum value at approximately 500 trajectories while SRVRPG and SVRPG reaches the maximum value at approximately 1500 trajectories. GPOMDP converges at about 3000 trajectories.

### Mountain-Car Environment

We use the Mountain Car environment provided in rllab environments. The task is to push a car to a certain position on a hill. The agent takes continuous actions to move leftward or rightward and gets a reward according to it's current position and height, every step it takes gets a penalty -1 and the episode ends when a target position is reached.

Figure 2 shows the growth of the average return according to the training trajectories. The GPOMDP algorithm in the Mountain-Car environment does not converge well. For illustrative purpose we only present the plot of the STORM-PG algorithm and two variance-reduced baselines.

From Figure 2, we see that STORM-PG algorithm outperforms other baselines within the first 200 trajectories and reaches a stable zone within 600 trajectories, while for the algorithms it takes at least 1000 trajectories to reach a reasonable result. The two figures 1 and 2 verifies our theory that our STORM-PG algorithm brings significant improvement to the policy gradient training.

Specifically, as we have mentioned at the beginning of Section 7, previous variance-reduced policy gradient methods requires carefully tuning of the inner loop iteration number. SVRPG uses adaptive number of iterations while after tuning SRVRPG fixes a very small number of inner loops.

On the contrary, we do not tune the mini batch size $B$. In practice, we fix both the initial batch $S_{0}$ and the mini batch $B$. The high stability with respect to hyper-parameters saves lots of efforts during the training process, The tolerance to the choice of parameters allows us to design a highly user friendly while efficient policy gradient algorithm.

## Final Remarks

In this paper, we propose a new STORM-PG algorithm that adopts a recently proposed variance-reduced gradient method called STORM. STORM-PG enjoys advantage both theoretically and experimentally. From the final experimental results, our STORM-PG algorithm is significantly better than all other baseline methods, both in aspects of training stability and parameter tuning (the user time of tuning STORM-PG is much shorter). The superiority of STORM-PG in experimental results over SVRPG breaks the curse that stochastic recursive gradient method, namely SARAH, often fails to outperform SVRG in practice even though it has better theoretical convergence rate. Future works include proving the lower bounds of our algorithm and further improvement of the experimental performance on other statistical learning tasks. We hope this work can inspire both reinforcement learning and optimization communities for future explorations.
