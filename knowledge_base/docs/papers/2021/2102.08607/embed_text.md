## Introduction

In this paper, we investigate the theoretical properties of Policy Gradient (PG) methods for Reinforcement Learning (RL). In view of RL as a policy optimization problem, the PG method parameterizes the policy function and conduct gradient ascent search to improve the policy. In this paper, we consider the soft-max policy parameterization where $(s,a)$ is a state-action pair and $\psi$ is some smooth function. Potentially, one can set the function $\psi$ to be some deep neural network with weights $\theta$ and input $(s,a)$. The main problem considered in this paper is the policy optimization for a *general utility* function: where $F$ is a general smooth function, and $\lambda^{\pi_{\theta}}$ denotes the unnormalized state-action occupancy measure (also referred to as the visitation measure). For any policy $\pi$ and initial state distribution $\xi$, When $F$ is linear, the problem reduces to the standard policy optimization problem where the objective is to maximize a cumulative sum of rewards. When $F$ is nonlinear, problem goes beyond standard Markov decision problems: examples include the max-entropy exploration, risk-sensitive RL, certain set constrained RL, and so.

In the standard cumulative-return case (i.e., $F$ is linear), numerous works have studied PG methods in various scenarios, see e.g.. To the authors' best knowledge, a most recent variant of PG methods, using the SARAH/Spider stochastic variance reduction technique, finds a local $\epsilon$-stationary policy using $\mathcal{O}{(\epsilon^{- 3})}$ samples. This poses a contrast with the known $\overset{\sim}{O}{(\epsilon^{- 2})}$ sample complexity results that can be achieved by various value-based methods and are provably matching information-theoretic lower bounds. In this paper, we attempt to close this gap and prove an $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ sample complexity bound for a PG method. Most importantly, when it comes to PG estimation, the application of the variance reduction technique typically relies on certain off-policy PG estimator, resulting in the difficulty of distribution shift. We notice that none of the existing variance-reduced PG methods attempt to address this challenge. Instead, they directly make an uncheckable assumption that the variance of the importance weight is bounded for every policy pair encountered in running the algorithm, see e.g.. In this paper, we propose a simple gradient truncation mechanism to fix this issue.

Next, let us go beyond cumulative return and consider policy optimization for a general utility where $F$ may be nonlinear. However, much less is known in this setting. The nonlinearity of $F$ invalidates the concept of Q-function and value function, leading to the failure of policy gradient theorem. To overcome such difficulty, showed that the policy gradient for the general utilities is the solution to a min-max problem. However, estimating a single PG is highly nontrivial in this case. It is still unclear how to make PG methods to use samples in a most efficient way.

In this paper, we aim to investigate the convergence and sample efficiency of the PG method, using episodic sampling, for both linear $F$ (i.e., cumulative rewards) and nonlinear $F$ (i.e., general utility). Observe that problem is an instance of the Stochastic Composite Optimization (SCO) problem: which involves an inner expectation that corresponds to the occupancy measure $\lambda^{\pi}$. Motivated by this view point, we attempt to develop stochastic policy gradient method with provable finite-sample efficiency bounds.

Main results. Our main results are summarized below.

We propose the TSIVR-PG algorithm to solve problem via episodic sampling. It provides a conceptually simple stochastic gradient approach for solving general utility RL.

We provide a gradient truncation mechanism to address the distribution shift difficulty in variance-reduced PG methods. Such difficulty has never been addressed in previous works.

We show that TSIVR-PG finds an $\epsilon$-stationary policy using $\overset{\sim}{O}{(\epsilon^{- 3})}$ samples if $F$ and $\psi$ are general smooth functions. When $F$ is concave and $\psi$ satisfies certain overparameterization condition, we show that TSIVR-PG obtains a gloal $\epsilon$-optimal policy using $\overset{\sim}{O}{(\epsilon^{- 2})}$ samples.

Technical contribution. Our analysis technique is also of independent interest in the relating areas.

For stochastic composite optimization (SCO), most existing algorithms require estimating the Jacobian matrix of the inner mapping, which corresponds to $\nabla_{\theta}\lambda^{\pi_{\theta}}$ in our setting. This is in practice prohibitive if the Jacobian matrix has high dimensions, which is exactly the case in our problem. Unlike SCO algorithms such as \[23, 53, 52, etc.\], our analysis enables us to avoid the Jacobian matrix estimation.

For the stochastic variance-reduced gradient methods, our analysis implies a convergence of SARAH/Spider methods to global optimality and a new $\mathcal{O}{(\epsilon^{- 2})}$ sample complexity for nonconvex problems with "hidden convexity" structure, which has not been studied in the optimization community yet.

## Related Works

Policy gradient gives rises to a rich family of RL algorithms, such as REINFORCE and many of its variants, as well as extensions such as the natural policy gradient methods, the actor-critic methods, the trust-region policy optimization, and the proximal policy optimization method, etc. In this paper we mainly focus on REINFORCE-type methods, where many of them need $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 4})}$ samples to find an $\epsilon$-stationary solution, including the vanilla REINFORCE, as well as its variants with baseline and GPOMDP, etc. By incorporating the stochastic variance reduction techniques, the sample efficiency of PG methods can be further improved. In, the SVRG variance reduction scheme is adopted and an $\mathcal{O}{(\epsilon^{- 4})}$ sample complexity is achieved, which is later improved to $\mathcal{O}{(\epsilon^{- {10/3}})}$ . With additional Hessian information, achieved an $\mathcal{O}{(\epsilon^{- 3})}$ complexity. By utilizing a more efficient SARAH/Spider variance reduction scheme, people are able to achieve $\mathcal{O}{(\epsilon^{- 3})}$ sample complexity without second-order information. We would like to comment that these results are only for finding $\epsilon$-stationary (rather than near-optimal) solutions, and all of them requires an uncheckable condition on the importance weights in every iteration.

Recently, for cumulative reward, a series of works have started to study the convergence of policy gradient method to global optimal solutions. In particular, exploited the hidden convexity property of the MDP problem and established the convergence to global optimality for general utility RL problem, as long as the policy gradient can be computed exactly.

Our approach is related to the stochastic composite optimization (SCO). For the general composition problem, there have been numerous developments, including momentum-based and multi-time-scale algorithms, and various composite stochastic variance-reduced algorithms. Our approach is also inspired by variance reduction techniques that were initially used for stochastic convex optimization, see; and were later on extended to the stochastic nonconvex optimization problems. In particular, we will utilize the SARAH/Spider scheme.

## Problem Formulation

Consider an MDP with a general utility function, denoted as $\text{MDP}{(\mathcal{S},\mathcal{A},\mathcal{P},\gamma,F)}$, where $\mathcal{S}$ is a finite state space, $\mathcal{A}$ is a finite action space, $\gamma \in {}$ is a discount factor, and $F$ is some general utility function. For each state $s \in \mathcal{S}$, a transition to state $s' \in \mathcal{S}$ occurs when selecting an action $a \in \mathcal{A}$ following the distribution $\mathcal{P}{(\cdot |a,s)}$. For each state $s \in \mathcal{S}$, a policy $\pi$ gives a distribution $\pi{(\cdot |s)}$ over the action space $\mathcal{A}$. Let $\xi$ be the initial state distribution and let the unnormalized state-action occupancy measure $\lambda^{\pi}$ be defined, we define the general utility function $F$ as a smooth function of the occupancy measure, and the goal of the general utility MDP is to maximize $F{(\lambda^{\pi})}$. With the policy $\pi_{\theta}$ being parameterized, we propose to solve problem, which is For notational convenience, we often write $\lambda{(\theta)}$ instead of $\lambda^{\pi_{\theta}}$. Such utility function is very general and includes many important problems in RL. We provide a few examples where $F$ are *concave*.

### Example 3.1 (Cumulative reward)

When ${F\left( \lambda^{\pi_{\theta}} \right)} = \left\langle r,\lambda^{\pi_{\theta}} \right\rangle$, for some $r \in {\mathbb{R}}^{{|\mathcal{S}|}{|\mathcal{A}|}}$. Then we recover the standard cumulative sum of rewards:

### Example 3.2 (Maximal entropy exploration)

Let ${\mu^{\pi_{\theta}}{(s)}} = {{({1 - \gamma})}{\sum_{a}{\lambda^{\pi_{\theta}}{(s,a)}}}}$, ${\forall s} \in \mathcal{S}$ be the state occupancy measure, which is the margin of $\lambda^{\pi_{\theta}}$ over $\mathcal{S}$. Let $F{( \cdot )}$ be the entropy function, then we recover the objective for maximal entropy exploration:

### Example 3.3 (RL with Set Constraint)

Let ${\mathbf{z}{(s_{t},a_{t})}} \in {\mathbb{R}}^{d}$ be a vector feedback received in each step. The cumulative feedback is for some matrix $M \in {\mathbb{R}}^{{d \times {|\mathcal{S}|}}{|\mathcal{A}|}}$. proposed a set-constrained RL problem which aims to find a policy $\pi$ s.t. ${u{(\pi)}} \in U$ for some convex set $U$. This problem can be formulated as an instance of by letting $F{(\cdot)}$ be the negative squared distance:

## The TSIVR-PG Algorithm

In this section, we propose a Truncated Stochastic Incremental Variance-Reduced Policy Gradient (TSIVR-PG) method, which is inspired by techniques of variance reduction and off-policy estimation. A gradient truncation mechanism to proposed to provably control the importance weights in off-policy sampling.

### Off-Policy PG Estimation

Policy Gradient First, let us derive the policy gradient of the general utility. Let $V^{\pi_{\theta}}{(r)}$ be the cumulative reward under policy $\pi_{\theta}$, initial distribution $\xi$ and reward function $r$. By Example 3.1. ‣ 3 Problem Formulation ‣ On the Convergence and Sample Efficiency of Variance-Reduced Policy Gradient Method"), ${V^{\pi_{\theta}}{(r)}} = {\langle{\lambda{(\theta)}},r\rangle}$, the chain rule and policy gradient theorem indicates that where ${\nabla_{\theta}\lambda}{(\theta)}$ is the Jacobian matrix of the vector mapping $\lambda{(\theta)}$. That is, policy gradient theorem actually provides a way for computing the Jacobian-vector product for the occupancy measure. Following the above observation and the chain rule, we have Therefore, we can estimate the policy gradient using the typical REINFORCE as long as we pick the "quasi-reward function" as $r:={{\nabla_{\lambda}F}{({\lambda{(\theta)}})}}$. To find this quasi-reward, we need to estimate the state-action occupancy measure $\lambda{(\theta)}$ (unless $F$ is linear).

Importance Sampling Weight Let $\tau = {\{ s_{0},a_{0},s_{1},a_{1},\cdots,s_{H - 1},a_{H - 1}\}}$ be a length-$H$ trajectory generated under the initial distribution $\xi$ and the behavioral policy $\pi_{\theta_{1}}$. For any target policy $\pi_{\theta_{2}}$, we define the importance sampling weight as It is worth noting that such importance sampling weight is inevitable in the stochastic variance reduced policy gradient methods, see. In these works, the authors usually directly assume ${{Var}{({\omega_{H - 1}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}})}} \leq W$ for all the policy pairs encountered in every iteration of their algorithms. However, such assumption is too strong and is uncheckable.

Based on the above notation of behavioral and target policies, as long as the importance sampling weights, we present the following off-policy occupancy and policy gradient estimators.

Off-Policy Occupancy Measure Estimator Denote $\mathbf{e}_{sa}$ the vector with $(s,a)$-th entry being 1 while other entries being 0. We define the following estimator for $\lambda{(\theta_{2})}$ When $\theta_{2} = \theta_{1}$, ${\omega_{t}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}} \equiv 1$ and ${\hat{\lambda}}_{\omega}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}$ becomes the on-policy (discounted) empirical distribution, for which we use the simplified notion ${\hat{\lambda}{(\left. \tau \middle| \theta_{2} \right.)}}:={{\hat{\lambda}}_{\omega}{(\left. \tau \middle| {\theta_{2},\theta_{2}} \right.)}}$.

Off-Policy Policy Gradient Estimator Let $r \in {\mathbb{R}}^{{|\mathcal{S}|}{|\mathcal{A}|}}$ be any quasi-reward vector. We aim to estimate the Jacobian-vector product ${\lbrack{{\nabla_{\theta}\lambda}{(\theta_{2})}}\rbrack}^{\top}r$ for target policy $\pi_{\theta_{2}}$ by When $\theta_{2} = \theta_{1}$, ${\omega_{t}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}} \equiv 1$ and ${\hat{g}}_{\omega}{(\left. \tau \middle| {\theta_{1},\theta_{2},r} \right.)}$ becomes the on-policy REINFORCE estimator with quasi-reward function $r$. In this case, we use the simplified notion ${\hat{g}{(\left. \tau \middle| {\theta_{2},r} \right.)}}:={{\hat{g}}_{\omega}{(\left. \tau \middle| {\theta_{2},\theta_{2},r} \right.)}}$.

Estimators ${\hat{\lambda}}_{\omega}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}$ and ${\hat{g}}_{\omega}{(\left. \tau \middle| {\theta_{1},\theta_{2},r} \right.)}$ are almost unbiased. In details, see details in Appendix E. Therefore the bias due to truncation is almost negligible if $H$ is properly selected.

### The TSIVR-PG Algorithm

To achieve the $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ sample complexity, we propose an epoch-wise algorithm called Truncated Stochastic Incremental Variance-Reduced PG (TSIVR-PG) Algorithm. Let $\theta_{0}^{i}$ be the starting point of the $i$-th epoch, TSIVR-PG constructs the estimators for $\lambda{(\theta_{0}^{i})}$, quasi-reward ${\nabla_{\lambda}F}{({\lambda{(\theta_{0}^{i})}})}$ and the policy gradient ${\nabla_{\theta}F}{({\lambda{(\theta_{0}^{i})}})}$ by where $\mathcal{N}_{i}$ is a set of $N$ independent length-$H$ trajectories sampled under $\pi_{\theta_{0}^{i}}$. When $j \geq 1$, where $\mathcal{B}_{j}^{i}$ is a set of $B$ independent length-$H$ trajectories sampled under $\pi_{\theta_{j}^{i}}$, and we default $r_{- 1}^{i}:=r_{0}^{i}$. Specifically, ${\hat{g}}_{\omega}{(\left. \tau \middle| {\theta_{j}^{i},\theta_{j - 1}^{i},r_{j - 2}^{i}} \right.)}$ is used instead of ${\hat{g}}_{\omega}{(\left. \tau \middle| {\theta_{j}^{i},\theta_{j - 1}^{i},r_{j - 1}^{i}} \right.)}$ for independence issue. The details of the TSIVR-PG algorithm are stated in Algorithm 1.

1 Input: Initial point $\theta_{0}^{1} = {\overset{\sim}{\theta}}_{0}$; batch sizes N and B; sample trajectory length H; stepsize η; epoch length m; gradient truncation radius δ. 5 Sample N trajectories under policy πθ0i of length H, collected as 𝒩i. 6 Compute estimators λ0i, r0i and g0i. Default r−1i:= r0i. 9 Sample B trajectories under policy πθji with length H, collected as ℬji. 10 Compute estimators λji, rji and gji by and. 11 Update the policy parameter by a truncated gradient ascent step: $$\theta_{j + 1}^{i} = \begin{cases} {\theta_{j}^{i} + {\eta \cdot g_{j}^{i}}} & {,\text{~if~}\eta \parallel g_{j}^{i} \parallel \leq \delta,} \\{\theta_{j}^{i} + \left. {\delta \cdot g_{j}^{i}}/\left\| g_{j}^{i} \right\| \right.} & {,\text{~otherwise.}} 12 Set $\theta_{0}^{i + 1} = {\overset{\sim}{\theta}}_{i} = \theta_{m}^{i}$. Algorithm 1 The TSIVR-PG Algorithm It is worth noting that the truncated gradient step is equivalent to a trust region subproblem: where the approximate Hessian matrix is simply chosen as ${(\eta)}^{- 1} \cdot I$.

## Sample Efficiency of TSIVR-PG

In this section, we analyze the finite-sample performance of TSIVR-PG. We first show that TSIVR-PG finds an $\epsilon$-stationary solution with $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 3})}$ samples. Given additional assumptions, we show that TSIVR-PG finds a global $\epsilon$-optimal solution with $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ samples.

### Convergence Towards Stationary Points

Since we focus on the soft-max policy parameterization where ${\pi_{\theta}\left( a \middle| s \right)} = \frac{\exp\left\{ {\psi(s,a;\theta)} \right\}}{\left. \sum{}_{a'} \right.{\exp\left\{ {\psi\left( s,a';\theta \right)} \right\}}}$, we make the following assumptions on the parameterization function $\psi$ and the utility $F$.

### Assumption 5.1

$\psi{(s,a; \cdot)}$ is twice differentiable for all $s$ and $a$. There ${{\exists\ell_{\psi}},L_{\psi}} > 0$ s.t. where $\parallel \cdot \parallel$ stands for $L_{2}$ norm and spectral norm for vector and matrix respectively.

### Assumption 5.2

$F$ is a smooth and possibly nonconvex function. There exists $\ell_{\lambda,\infty} > 0$ such that ${\|{{\nabla_{\lambda}F}{(\lambda)}}\|}_{\infty} \leq \ell_{\lambda,\infty}$. And there exist constants ${L_{\lambda,\infty},L_{\lambda}} > 0$ s.t. it holds that As a consequence, we have the following lemmas.

### Lemma 5.3

Given Assumption 5.1 and 5.2, the following results hold:\(i). For any policy parameter $\theta$ and any state-action pair $(s,a)$, then it holds for any $s,a$ and $\theta$ that (ii). For any policy parameters $\theta_{1}$ and $\theta_{2}$, it holds that (iii). The objective function ${F \circ \lambda}{(\cdot)}$ is $L_{\theta}$-smooth, with To measure the convergence, we propose to use the gradient mapping defined as follows: where $g = {{\nabla_{\theta}F}{({\lambda{(\theta)}})}}$. We remark that, ${\mathbb{E}}{\lbrack{\|{\mathcal{G}_{\eta}{(\theta_{j}^{i})}}\|}^{2}\rbrack}$ is more suitable for the ascent analysis of the truncated gradient updates, compared with the commonly used ${\mathbb{E}}{\lbrack{\|{{\nabla_{\theta}F}{({\lambda{(\theta_{j}^{i})}})}}\|}^{2}\rbrack}$. Note that ${\mathcal{G}_{\eta}{(\theta)}} = {{\nabla F}{({\lambda{(\theta)}})}}$ if ${\|{\mathcal{G}_{\eta}{(\theta)}}\|} \leq \delta$ and $\|{{\nabla F}{({\lambda{(\theta)}})}}\|$ is bounded for any $\theta$. Based on such observation, we have the following lemma to validate the choice of the proposed stationarity measure.

### Lemma 5.4

For any random vector $\theta$, if ${{\mathbb{E}}{\lbrack{\|{\mathcal{G}_{\eta}{(\theta)}}\|}\rbrack}} \leq \epsilon$, then Based on the notion of $\mathcal{G}_{\eta}$, we characterize the per-iteration ascent as follows.

### Lemma 5.5

Let the iterates be generated by Algorithm 1. Then it holds that This suggests us to bound mean-squared-error ${\mathbb{E}}{\lbrack{\|{{{\nabla_{\theta}F}{({\lambda{(\theta_{j}^{i})}})}} - g_{j}^{i}}\|}^{2}\rbrack}$. For this purpose, we need to bound the importance sampling weight, by utilizing the soft-max form of policy parameterization.

### Lemma 5.6

For any behavioral policy $\pi_{\theta_{1}}$ and target policy $\pi_{\theta_{2}}$ parameterized, the importance weight satisfies for ${\forall 0} \leq t \leq {H - 1}$.

Since TSIVR-PG only uses importance weights for two consecutive iterations $\theta_{j}^{i},\theta_{j - 1}^{i}$ while forcing ${\|{\theta_{j}^{i} - \theta_{j - 1}^{i}}\|} \leq \delta$ by the truncated gradient step, we have ${\omega_{H - 1}{(\left. \tau \middle| {\theta_{j}^{i},\theta_{j - 1}^{i}} \right.)}} \leq {\exp{\{{2H\ell_{\psi}\delta}\}}}$ w.p. 1. As we will see later, the effective horizon $H$ only has a mild magnitude of $\mathcal{O}\left( {{({1 - \gamma})}^{- 1} \cdot {\log{({1/\epsilon})}}} \right)$, the truncation radius only need to satisfy $\delta = {\mathcal{O}{({H^{- 1}\ell_{\psi}^{- 1}})}}$ s.t. ${\omega_{t - 1}{(\left. \tau \middle| {\theta_{j}^{i},\theta_{j - 1}^{i}} \right.)}} = {\mathcal{O}{}}$, for ${{\forall t} \leq {H - 1}}.$ Consequently, combining Lemma 5.3, 5.6 and Lemma B.1 of gives the following result.

### Lemma 5.7

Let policy $\pi_{\theta}$ be parameterized by with function $\psi$ satisfying Assumption 5.1. Suppose behavioral policy $\pi_{\theta_{1}}$ and target policy $\pi_{\theta_{2}}$ satisfy ${\|{\theta_{1} - \theta_{2}}\|} \leq \delta$, then where $\tau$ is sampled under policy $\pi_{\theta_{1}}$, and ${C_{\omega}{(t)}} = {t\left({{4\ell_{\psi}^{2}{({t + \frac{1}{2}})}} + {2L_{\psi}}} \right){({e^{4\deltat} + 1})}}$.

As a result, we can bound the mean-squared-error of the $g_{j}^{i}$ as follows.

### Lemma 5.8

For the PG estimators $g_{j}^{i}$, we have for some constants $C_{1},..,C_{4} > 0$. In case $j = 0$, we default $\sum_{j' = 1}^{0} \cdot = 0$.

The expression of constants $C_{i}$'s are complicated, we provide their detailed formula in the appendix. If we set $H = {\mathcal{O}\left( \frac{\log{({1/\epsilon})}}{1 - \gamma} \right)}$ and $\delta \leq \frac{1}{2H\ell_{\psi}}$, then $C_{i}$ only depends polynomially on the Lipschitz constants, $\log{(\epsilon^{- 1})}$, and ${({1 - \gamma})}^{- 1}$. Combining Lemma 5.5, 5.8, and 5.4 gives the following theorem.

### Theorem 5.9

For Algorithm 1, we choose $H = \frac{2{\log{({1/\epsilon})}}}{1 - \gamma}$, $\delta = \frac{1}{2H\ell_{\psi}}$, $B = m = \epsilon^{- 1}$, $N = \epsilon^{- 2}$, $\eta = {\frac{1}{1 + {{({C_{3} + C_{4}})}/L_{\theta}^{2}}} \cdot \frac{1}{2L_{\theta}}}$. After running the algorithm for $T = \epsilon^{- 1}$ epochs and output $\theta_{out}$ from ${\{\theta_{j}^{i}\}}_{j = {0,\cdots,{m - 1}}}^{i = {1,\cdots,T}}$ uniformly at random, then ${{\mathbb{E}}{\lbrack{\|{\mathcal{G}_{\eta}{(\theta_{out})}}\|}\rbrack}} \leq {\mathcal{O}{(\epsilon)}}$. The total number of samples used is ${{{Tm} \cdot {({{BH} + N})}} = {\overset{\sim}{\mathcal{O}}{(\epsilon^{- 3})}}}.$ By Lemma 5.4, we also have ${{\mathbb{E}}{\lbrack{\|{{\nabla_{\theta}F}{({\lambda{(\theta_{out})}})}}\|}\rbrack}} \leq {\mathcal{O}{(\epsilon)}}$.

### Convergence Towards Global Optimality

Next, we provide a mechanism to establish the convergence of TSIVR-PG to global optimality. For this purpose, we introduce the hidden convexity of the general utility RL problem. In addition to the smoothness of $F$ (Assumption 5.2), we further assume its concavity, formally stated as follows.

### Assumption 5.10

$F$ is a concave function of the state-action occupancy measure.

Let $\mathcal{L}$ be the image of the mapping $\lambda{(\theta)}$. Then the parameterized *policy optimization* problem can be rewritten as an equivalent *occupancy optimization* problem: When the policy parameterization is powerful enough to represent any policy, the image $\mathcal{L}$ is a convex polytope, see e.g.. Since $F$ is concave, the occupancy optimization problem is a *convex optimization* problem. In this case, if the mapping $\lambda{(\cdot)}$ is invertible (see), we may view the original problem as a reformulation of a convex problem by a change of variable: $\theta = {\lambda^{- 1}{(\mu)}}$. We call this property "hidden convexity". However, requiring $\lambda{(\cdot)}$ to be invertible is too restrictive, and it doesn't even hold for simple soft-max policy with ${\psi{(s,a;\theta)}} = \theta_{sa}$ where multiple $\theta$ correspond to a same policy. Therefore, we adopt a weaker assumption where (i). $\pi_{\theta}$ can represent any policy (ii). a continuous inverse $\lambda^{- 1}{(\cdot)}$ can be locally defined over a subset of $\theta$.

### Assumption 5.11

For policy parameterization of form, $\theta$ overparametrizes the set of policies in the following sense. (i). For any $\theta$ and $\lambda{(\theta)}$, there exist (relative) neighourhoods $\theta \in \mathcal{U}_{\theta} \subset {B{(\theta,\delta)}}$ and ${\lambda{(\theta)}} \in \mathcal{V}_{\lambda{(\theta)}} \subset {\lambda{({B{(\theta,\delta)}})}}$ s.t. $\left( {\lambda|}_{\mathcal{U}_{\theta}} \right){( \cdot )}$ forms a bijection between $\mathcal{U}_{\theta}$ and $\mathcal{V}_{\lambda{(\theta)}}$, where $\left( {\lambda|}_{\mathcal{U}_{\theta}} \right){( \cdot )}$ is the confinement of $\lambda$ onto $\mathcal{U}_{\theta}$. We assume ${({\lambda|}_{\mathcal{U}_{\theta}})}^{- 1}{( \cdot )}$ is $\ell_{\theta}$-Lipschitz continuous for any $\theta$. (ii). Let $\pi_{\theta^{\ast}}$ be the optimal policy. Assume there exists $\overline{\epsilon}$ small enough, s.t. ${{{({1 - \epsilon})}\lambda{(\theta)}} + {\epsilon\lambda{(\theta^{\ast})}}} \in \mathcal{V}_{\lambda{(\theta)}}$ for ${\forall\epsilon} \leq \overline{\epsilon}$, $\forall\theta$.

Based on Assumption 5.11, we replace Lemma 5.5 with the following lemma.

### Lemma 5.12

For ${\forall\epsilon} < \overline{\epsilon}$ with $\overline{\epsilon}$ defined in Assumption 5.11, it holds for all iterations that The analysis of Lemma 5.12 is very different from its nonconvex optimization counterpart (Lemma 5.5). Next, we derive the sample complexity of the TSIVR-PG algorithm given Lemma 5.12 and 5.8.

### Theorem 5.13

For TSIVR-PG method (Algorithm 1), let $\epsilon \in {(0,\overline{\epsilon})}$ be the target accuracy. If we choose $H,m,B,N$ and $\delta$ according to Theorem 5.9. and we let the stepsize to be small enough s.t. $\eta \leq \frac{1}{{2L_{\theta}} + {{8{({C_{3} + C_{4}})}}/L_{\theta}}}$, then after at most $T = {\log_{2}{(\epsilon^{- 1})}}$ epochs, ${{\mathbb{E}}\left\lbrack {{F{({\lambda{(\theta^{\ast})}})}} - {F{({\lambda{({\overset{\sim}{\theta}}_{T})}})}}} \right\rbrack} \leq {\mathcal{O}{(\epsilon)}}$. The total number of samples taken is ${T \times {({{{({m - 1})}B} + N})} \times H} = {\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}}$.

## Numerical Experiments

### Maximizing Cumulative Reward

In this experiment, we aim to evaluate the performance of the TSIVR-PG algorithm for maximizing the cumulative sum of reward. As the benchmarks, we also implement the SVRPG, the SRVR-PG, the HSPGA, and the REINFORCE algorithms. Our experiment is performed on benchmark RL environments including the FrozenLake, Acrobot and Cartpole that are available from OpenAI gym, which is a well-known toolkit for developing and comparing reinforcement learning algorithms. For all the algorithms, their batch sizes are chosen according to their theory. In details, let $\epsilon$ be any target accuracy. For both TSIVR-PG and SRVR-PG, we set $N = {\Theta{(\epsilon^{- 2})}}$, $B = m = {\Theta{(\epsilon^{- 1})}}$. For SVRPG, we set $N = {\Theta{(\epsilon^{- 2})}}$, $B = {\Theta{(\epsilon^{- {4/3}})}}$ and $m = {\Theta{(\epsilon^{- {2/3}})}}$. For HSPGA, we set $B = {\Theta{(\epsilon^{- 1})}}$, other parameters are calculated according to formulas in given $B$. For REINFORCE, we set the batchsize to be $N = {\Theta{(\epsilon^{- 2})}}$. The parameter $\varepsilon$ and the stepsize/learning rate are tuned for each individual algorithm using a grid search. For each algorithm, we run the experiment for multiple times with random initialization of the policy parameters. The curve is obtained by first calculating the moving average of the most recent 50 episodes, and then calculate the median of the return over the outcomes of different runs. The upper and lower bounds of the shaded area are calculated as the $\frac{1}{4}$ and $\frac{3}{4}$ quantiles over the outcomes. We run the experiment for 10 times for the FrozenLake environment and 50 times for the other environments. The detailed parameters used in the experiments are presented in the Appendix.

### FrozenLake

The FrozenLake8x8 environment is a tabular MDP with finite state and action spaces. For this environment, the policy is parameterized with ${\psi{(s,a;\theta)}} = \theta_{sa}$.

### Cartpole and Acrobot

Both the Cartpole environment and the Acrobot environment are environments with a discrete action space and a continuous state space. For both environments, we use a neural network with two hidden layers with width 64 for both layers to model the policy.

### Result

We plot our experiment outcomes in Figure 1. The experiments show that given enough episodes, all of the algorithms are able to solve the tasks, achieving nearly optimal returns. And as expected, the REINFORCE algorithm takes the longest time to find the optimal policy. While the other algorithms yield a faster convergence speed, the TSIVR-PG algorithm consistently outperforms the other benchmark algorithms under all of the environments, showing the advantage of our method.

Figure 1: The performance curves of TSIVR-PG and benchmark algorithms under different environments. The curve is the median return over multiple runs and the shaded areas are calculated as the $\frac{1}{4}$ and $\frac{3}{4}$ quantiles of the experiment outcomes.

### Validating the $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ Sample Complexity

Besides the comparison between different benchmark algorithms, we also perform a validation experiment showing that for certain environments, the convergence rate of TSIVR-PG is close to the theoretical guarantee. Because the parameters $N,B,m$ are dependent on the target accuracy $\epsilon$, in this section we adopt a different way to set up these parameters: We first set a fixed epoch $E$, and perform experiments using different values of the parameter $N$. The parameter $B$ and $m$ are set according to our choice of $N$ by $B = m = \sqrt{N}$. The performance of the algorithm output is calculated as the average score of the last few episodes, which is then averaged over 10 independent runs. Again, we use the FrozenLake8x8 environment to do the experiment. Because FrozenLake8x8 is a tabular environment whose transition and reward function can be easily obtained from the document, we can calculate it's optimal value simply by value iteration, which takes $0.4146$ when we choose $\gamma = 0.99$. In this way, we calculate the gap between the algorithm return and the optimal value, and get log-log figure w.r.t. the gap and the number of episodes calculated by ${E{({N + {Bm}})}} = {2EN}$.

### Result

The result is shown in the first sub-figure of Figure 2, where the blue curve is the gap between the average return of experiment outcome and the optimal value and the shaded area is the range of one standard deviation of the logarithm value. In addition, we add a orange dotted line to fit the convergence curve, whose slope takes value $- 0.496$, which nearly matches the $O{(\epsilon^{- 2})}$ theoretical bound (slope $- 0.5$).

### Maximizing Non-linear Objective Function

The TSIVR-PG algorithm is designed not only to solve typical RL problems, but is also able to solve a broader class of problems where the objective function is a general concave function. Unfortunately, none of the benchmark algorithms proposed in the previous section have the ability to solve this kind of problem. To evaluate the performance of our algorithm, we choose another benchmark algorithm, which is the MaxEnt algorithm. In the experiment, we use FrozenLake8x8 environment since it's more tractable to compute $\lambda$ for a discrete state space. We set the objective function as where $\sigma$ is a fixed small constant. We choose $\sigma = 0.125$ in our experiment. The orders of $N,B,m$ are set in the same way as those in section 6.1. For the MaxEnt algorithm, note that in the original paper, the nonlinear objective function assumes the input value is the stationary state distribution $d^{\pi}$, but the input value can easily be changed into our $\lambda$ without changing the steps of the algorithm much. The result is illustrated in Fig. 2. From the result, we may see that our algorithm consistently outperforms the benchmark.

Figure 2: Left: Empirical Evaluation of the Convergence Rate of TSIVR-PG. The optimality gap achieved by TSIVR-PG decreases as the sample size increases, nearly matching the ϵ−2 sample complexity theory (orange line). Right: Performance Curve ofTSIVR-PG and MaxEnt for Maximizing Non-linear Objective Functions. The curve is the median return over 10 runs and the shaded areas are calculated as the $\frac{1}{4}$ and $\frac{3}{4}$ quantiles of the experiment outcomes.
