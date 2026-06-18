<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Convergence and Sample Efficiency of Variance-Reduced Policy Gradient Method

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient (PG) gives rise to a rich class of reinforcement learning (RL) methods. Recently, there has been an emerging trend to accelerate the existing PG methods such as REINFORCE by the variance reduction techniques. However, all existing variance-reduced PG methods heavily rely on an uncheckable importance weight assumption made for every single iteration of the algorithms. In this paper, a simple gradient truncation mechanism is proposed to address this issue. Moreover, we design a Truncated Stochastic Incremental Variance-Reduced Policy Gradient (TSIVR-PG) method, which is able to maximize not only a cumulative sum of rewards but also a general utility function over a policy's long-term visiting distribution. We show an tildeO(epsilon^(-3)) sample complexity for TSIVR-PG to find an epsilon-stationary policy. By assuming the overparameterizaiton of policy and exploiting the hidden convexity of the problem, we further show that TSIVR-PG converges to global epsilon-optimal policy with tildeO(epsilon^(-2)) samples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we investigate the theoretical properties of Policy Gradient (PG) methods for Reinforcement Learning (RL). In view of RL as a policy optimization problem, the PG method parameterizes the policy function and conduct gradient ascent search to improve the policy. In this paper, we consider the soft-max policy parameterization

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $(s,a)$ is a state-action pair and $\psi$ is some smooth function. Potentially, one can set the function $\psi$ to be some deep neural network with weights $\theta$ and input $(s,a)$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $F$ is a general smooth function, and $\lambda^{\pi_{\theta}}$ denotes the unnormalized state-action occupancy measure (also referred to as the visitation measure). For any policy $\pi$ and initial state distribution $\xi$,

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $F$ is linear, the problem reduces to the standard policy optimization problem where the objective is to maximize a cumulative sum of rewards. When $F$ is nonlinear, problem goes beyond standard Markov decision problems: examples include the max-entropy exploration, risk-sensitive RL, certain set constrained RL, and so.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the standard cumulative-return case (i.e., $F$ is linear), numerous works have studied PG methods in various scenarios, see e.g.. To the authors' best knowledge, a most recent variant of PG methods, using the SARAH/Spider stochastic variance reduction technique, finds a local $\epsilon$-stationary policy using $\mathcal{O}{(\epsilon^{- 3})}$ samples. This poses a contrast with the known $\overset{\sim}{O}{(\epsilon^{- 2})}$ sample complexity results that can be achieved by various value-based methods and are provably matching information-theoretic lower bounds. In this paper, we attempt to close this gap and prove an $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ sample complexity bound for a PG method. Most importantly, when it comes to PG estimation, the application of the variance reduction technique typically relies on certain off-policy PG estimator, resulting in the difficulty of distribution shift.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We notice that none of the existing variance-reduced PG methods attempt to address this challenge. Instead, they directly make an uncheckable assumption that the variance of the importance weight is bounded for every policy pair encountered in running the algorithm, see e.g.. In this paper, we propose a simple gradient truncation mechanism to fix this issue.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Next, let us go beyond cumulative return and consider policy optimization for a general utility where $F$ may be nonlinear. However, much less is known in this setting. The nonlinearity of $F$ invalidates the concept of Q-function and value function, leading to the failure of policy gradient theorem. To overcome such difficulty, showed that the policy gradient for the general utilities is the solution to a min-max problem. However, estimating a single PG is highly nontrivial in this case. It is still unclear how to make PG methods to use samples in a most efficient way.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we aim to investigate the convergence and sample efficiency of the PG method, using episodic sampling, for both linear $F$ (i.e., cumulative rewards) and nonlinear $F$ (i.e., general utility).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

which involves an inner expectation that corresponds to the occupancy measure $\lambda^{\pi}$. Motivated by this view point, we attempt to develop stochastic policy gradient method with provable finite-sample efficiency bounds.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Main results. Our main results are summarized below.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the TSIVR-PG algorithm to solve problem via episodic sampling. It provides a conceptually simple stochastic gradient approach for solving general utility RL.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a gradient truncation mechanism to address the distribution shift difficulty in variance-reduced PG methods. Such difficulty has never been addressed in previous works.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that TSIVR-PG finds an $\epsilon$-stationary policy using $\overset{\sim}{O}{(\epsilon^{- 3})}$ samples if $F$ and $\psi$ are general smooth functions. When $F$ is concave and $\psi$ satisfies certain overparameterization condition, we show that TSIVR-PG obtains a gloal $\epsilon$-optimal policy using $\overset{\sim}{O}{(\epsilon^{- 2})}$ samples.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Technical contribution. Our analysis technique is also of independent interest in the relating areas.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

For stochastic composite optimization (SCO), most existing algorithms require estimating the Jacobian matrix of the inner mapping, which corresponds to $\nabla_{\theta}\lambda^{\pi_{\theta}}$ in our setting. This is in practice prohibitive if the Jacobian matrix has high dimensions, which is exactly the case in our problem. Unlike SCO algorithms such as \[23, 53, 52, etc.\], our analysis enables us to avoid the Jacobian matrix estimation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the stochastic variance-reduced gradient methods, our analysis implies a convergence of SARAH/Spider methods to global optimality and a new $\mathcal{O}{(\epsilon^{- 2})}$ sample complexity for nonconvex problems with "hidden convexity" structure, which has not been studied in the optimization community yet.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Related Works", "weight": 1.0} -->

Policy gradient gives rises to a rich family of RL algorithms, such as REINFORCE and many of its variants, as well as extensions such as the natural policy gradient methods, the actor-critic methods, the trust-region policy optimization, and the proximal policy optimization method, etc. In this paper we mainly focus on REINFORCE-type methods, where many of them need $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 4})}$ samples to find an $\epsilon$-stationary solution, including the vanilla REINFORCE, as well as its variants with baseline and GPOMDP, etc. By incorporating the stochastic variance reduction techniques, the sample efficiency of PG methods can be further improved. In, the SVRG variance reduction scheme is adopted and an $\mathcal{O}{(\epsilon^{- 4})}$ sample complexity is achieved, which is later improved to $\mathcal{O}{(\epsilon^{- {10/3}})}$. With additional Hessian information, achieved an $\mathcal{O}{(\epsilon^{- 3})}$ complexity.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Related Works", "weight": 1.0} -->

By utilizing a more efficient SARAH/Spider variance reduction scheme, people are able to achieve $\mathcal{O}{(\epsilon^{- 3})}$ sample complexity without second-order information. We would like to comment that these results are only for finding $\epsilon$-stationary (rather than near-optimal) solutions, and all of them requires an uncheckable condition on the importance weights in every iteration.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Related Works", "weight": 1.0} -->

Recently, for cumulative reward, a series of works have started to study the convergence of policy gradient method to global optimal solutions. In particular, exploited the hidden convexity property of the MDP problem and established the convergence to global optimality for general utility RL problem, as long as the policy gradient can be computed exactly.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our approach is related to the stochastic composite optimization (SCO). For the general composition problem, there have been numerous developments, including momentum-based and multi-time-scale algorithms, and various composite stochastic variance-reduced algorithms. Our approach is also inspired by variance reduction techniques that were initially used for stochastic convex optimization, see; and were later on extended to the stochastic nonconvex optimization problems. In particular, we will utilize the SARAH/Spider scheme.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider an MDP with a general utility function, denoted as $\text{MDP}{(\mathcal{S},\mathcal{A},\mathcal{P},\gamma,F)}$, where $\mathcal{S}$ is a finite state space, $\mathcal{A}$ is a finite action space, $\gamma \in {}$ is a discount factor, and $F$ is some general utility function. For each state $s \in \mathcal{S}$, a transition to state $s^{\prime} \in \mathcal{S}$ occurs when selecting an action $a \in \mathcal{A}$ following the distribution $\mathcal{P}{( \cdot |a,s)}$. For each state $s \in \mathcal{S}$, a policy $\pi$ gives a distribution $\pi{( \cdot |s)}$ over the action space $\mathcal{A}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\xi$ be the initial state distribution and let the unnormalized state-action occupancy measure $\lambda^{\pi}$ be defined, we define the general utility function $F$ as a smooth function of the occupancy measure, and the goal of the general utility MDP is to maximize $F{(\lambda^{\pi})}$. With the policy $\pi_{\theta}$ being parameterized, we propose to solve problem, which is

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For notational convenience, we often write $\lambda{(\theta)}$ instead of $\lambda^{\pi_{\theta}}$. Such utility function is very general and includes many important problems in RL. We provide a few examples where $F$ are *concave*.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3.3 (RL with Set Constraint)", "weight": 1.0} -->

Let ${\mathbf{z}{(s_{t},a_{t})}} \in {\mathbb{R}}^{d}$ be a vector feedback received in each step. The cumulative feedback is

<!-- chunk {"id": "body-0027", "role": "body", "section": "The TSIVR-PG Algorithm", "weight": 1.0} -->

In this section, we propose a Truncated Stochastic Incremental Variance-Reduced Policy Gradient (TSIVR-PG) method, which is inspired by techniques of variance reduction and off-policy estimation. A gradient truncation mechanism to proposed to provably control the importance weights in off-policy sampling.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

Policy Gradient First, let us derive the policy gradient of the general utility. Let $V^{\pi_{\theta}}{(r)}$ be the cumulative reward under policy $\pi_{\theta}$, initial distribution $\xi$ and reward function $r$. By Example 3.1. ‣ 3 Problem Formulation ‣ On the Convergence and Sample Efficiency of Variance-Reduced Policy Gradient Method"), ${V^{\pi_{\theta}}{(r)}} = {\langle{\lambda{(\theta)}},r\rangle}$, the chain rule and policy gradient theorem indicates that

<!-- chunk {"id": "body-0029", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

where ${\nabla_{\theta}\lambda}{(\theta)}$ is the Jacobian matrix of the vector mapping $\lambda{(\theta)}$. That is, policy gradient theorem actually provides a way for computing the Jacobian-vector product for the occupancy measure. Following the above observation and the chain rule, we have

<!-- chunk {"id": "body-0030", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

Therefore, we can estimate the policy gradient using the typical REINFORCE as long as we pick the "quasi-reward function" as $r:={{\nabla_{\lambda}F}{({\lambda{(\theta)}})}}$. To find this quasi-reward, we need to estimate the state-action occupancy measure $\lambda{(\theta)}$ (unless $F$ is linear).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

Importance Sampling Weight Let $\tau = {\{ s_{0},a_{0},s_{1},a_{1},\cdots,s_{H - 1},a_{H - 1}\}}$ be a length-$H$ trajectory generated under the initial distribution $\xi$ and the behavioral policy $\pi_{\theta_{1}}$. For any target policy $\pi_{\theta_{2}}$, we define the importance sampling weight as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

It is worth noting that such importance sampling weight is inevitable in the stochastic variance reduced policy gradient methods, see. In these works, the authors usually directly assume ${{Var}{({\omega_{H - 1}{(\left. \tau \middle| {\theta_{1},\theta_{2}} \right.)}})}} \leq W$ for all the policy pairs encountered in every iteration of their algorithms. However, such assumption is too strong and is uncheckable.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

Based on the above notation of behavioral and target policies, as long as the importance sampling weights, we present the following off-policy occupancy and policy gradient estimators.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

Off-Policy Occupancy Measure Estimator Denote $\mathbf{e}_{sa}$ the vector with $(s,a)$-th entry being 1 while other entries being 0. We define the following estimator for $\lambda{(\theta_{2})}$

<!-- chunk {"id": "body-0035", "role": "body", "section": "Off-Policy PG Estimation", "weight": 1.0} -->

see details in Appendix E. Therefore the bias due to truncation is almost negligible if $H$ is properly selected.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The TSIVR-PG Algorithm", "weight": 1.0} -->

To achieve the $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ sample complexity, we propose an epoch-wise algorithm called Truncated Stochastic Incremental Variance-Reduced PG (TSIVR-PG) Algorithm. Let $\theta_{0}^{i}$ be the starting point of the $i$-th epoch, TSIVR-PG constructs the estimators for $\lambda{(\theta_{0}^{i})}$, quasi-reward ${\nabla_{\lambda}F}{({\lambda{(\theta_{0}^{i})}})}$ and the policy gradient ${\nabla_{\theta}F}{({\lambda{(\theta_{0}^{i})}})}$ by

<!-- chunk {"id": "body-0037", "role": "body", "section": "The TSIVR-PG Algorithm", "weight": 1.0} -->

1 Input: Initial point $\theta_{0}^{1} = {\overset{\sim}{\theta}}_{0}$; batch sizes N and B; sample trajectory length H; stepsize η; epoch length m; gradient truncation radius δ.
5 Sample N trajectories under policy πθ0i of length H, collected as 𝒩i.
6 Compute estimators λ0i, r0i and g0i. Default r−1i:= r0i.
9 Sample B trajectories under policy πθji with length H, collected as ℬji.
10 Compute estimators λji, rji and gji by and.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The TSIVR-PG Algorithm", "weight": 1.0} -->

where the approximate Hessian matrix is simply chosen as ${(\eta)}^{- 1} \cdot I$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sample Efficiency of TSIVR-PG", "weight": 1.0} -->

In this section, we analyze the finite-sample performance of TSIVR-PG. We first show that TSIVR-PG finds an $\epsilon$-stationary solution with $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 3})}$ samples. Given additional assumptions, we show that TSIVR-PG finds a global $\epsilon$-optimal solution with $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$ samples.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convergence Towards Stationary Points", "weight": 1.0} -->

Since we focus on the soft-max policy parameterization where ${\pi_{\theta}\left( a \middle| s \right)} = \frac{\exp\left\{ {\psi(s,a;\theta)} \right\}}{\left. \sum{}_{a^{\prime}} \right.{\exp\left\{ {\psi\left( s,a^{\prime};\theta \right)} \right\}}}$, we make the following assumptions on the parameterization function $\psi$ and the utility $F$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

where $\parallel \cdot \parallel$ stands for $L_{2}$ norm and spectral norm for vector and matrix respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

As a consequence, we have the following lemmas.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Convergence Towards Global Optimality", "weight": 1.0} -->

Next, we provide a mechanism to establish the convergence of TSIVR-PG to global optimality. For this purpose, we introduce the hidden convexity of the general utility RL problem. In addition to the smoothness of $F$ (Assumption 5.2), we further assume its concavity, formally stated as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 5.10", "weight": 1.0} -->

$F$ is a concave function of the state-action occupancy measure.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 5.10", "weight": 1.0} -->

Let $\mathcal{L}$ be the image of the mapping $\lambda{(\theta)}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 5.10", "weight": 1.0} -->

When the policy parameterization is powerful enough to represent any policy, the image $\mathcal{L}$ is a convex polytope, see e.g.. Since $F$ is concave, the occupancy optimization problem is a *convex optimization* problem. In this case, if the mapping $\lambda{( \cdot )}$ is invertible (see ), we may view the original problem as a reformulation of a convex problem by a change of variable: $\theta = {\lambda^{- 1}{(\mu)}}$. We call this property "hidden convexity". However, requiring $\lambda{( \cdot )}$ to be invertible is too restrictive, and it doesn't even hold for simple soft-max policy with ${\psi{(s,a;\theta)}} = \theta_{sa}$ where multiple $\theta$ correspond to a same policy. Therefore, we adopt a weaker assumption where (i). $\pi_{\theta}$ can represent any policy (ii).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 5.10", "weight": 1.0} -->

a continuous inverse $\lambda^{- 1}{( \cdot )}$ can be locally defined over a subset of $\theta$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 5.11", "weight": 1.0} -->

Based on Assumption 5.11, we replace Lemma 5.5 with the following lemma.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Maximizing Cumulative Reward", "weight": 1.0} -->

In this experiment, we aim to evaluate the performance of the TSIVR-PG algorithm for maximizing the cumulative sum of reward. As the benchmarks, we also implement the SVRPG, the SRVR-PG, the HSPGA, and the REINFORCE algorithms. Our experiment is performed on benchmark RL environments including the FrozenLake, Acrobot and Cartpole that are available from OpenAI gym, which is a well-known toolkit for developing and comparing reinforcement learning algorithms. For all the algorithms, their batch sizes are chosen according to their theory. In details, let $\epsilon$ be any target accuracy. For both TSIVR-PG and SRVR-PG, we set $N = {\Theta{(\epsilon^{- 2})}}$, $B = m = {\Theta{(\epsilon^{- 1})}}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Maximizing Cumulative Reward", "weight": 1.0} -->

For SVRPG, we set $N = {\Theta{(\epsilon^{- 2})}}$, $B = {\Theta{(\epsilon^{- {4/3}})}}$ and $m = {\Theta{(\epsilon^{- {2/3}})}}$. For HSPGA, we set $B = {\Theta{(\epsilon^{- 1})}}$, other parameters are calculated according to formulas in given $B$. For REINFORCE, we set the batchsize to be $N = {\Theta{(\epsilon^{- 2})}}$. The parameter $\varepsilon$ and the stepsize/learning rate are tuned for each individual algorithm using a grid search. For each algorithm, we run the experiment for multiple times with random initialization of the policy parameters. The curve is obtained by first calculating the moving average of the most recent 50 episodes, and then calculate the median of the return over the outcomes of different runs.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Maximizing Cumulative Reward", "weight": 1.0} -->

The upper and lower bounds of the shaded area are calculated as the $\frac{1}{4}$ and $\frac{3}{4}$ quantiles over the outcomes. We run the experiment for 10 times for the FrozenLake environment and 50 times for the other environments. The detailed parameters used in the experiments are presented in the Appendix.

<!-- chunk {"id": "body-0052", "role": "body", "section": "FrozenLake", "weight": 1.0} -->

The FrozenLake8x8 environment is a tabular MDP with finite state and action spaces. For this environment, the policy is parameterized with ${\psi{(s,a;\theta)}} = \theta_{sa}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Cartpole and Acrobot", "weight": 1.0} -->

Both the Cartpole environment and the Acrobot environment are environments with a discrete action space and a continuous state space. For both environments, we use a neural network with two hidden layers with width 64 for both layers to model the policy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Result", "weight": 1.0} -->

We plot our experiment outcomes in Figure 1. The experiments show that given enough episodes, all of the algorithms are able to solve the tasks, achieving nearly optimal returns. And as expected, the REINFORCE algorithm takes the longest time to find the optimal policy. While the other algorithms yield a faster convergence speed, the TSIVR-PG algorithm consistently outperforms the other benchmark algorithms under all of the environments, showing the advantage of our method.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Validating the $\\overset{\\sim}{\\mathcal{O}}{(\\epsilon^{- 2})}$ Sample Complexity", "weight": 1.0} -->

Besides the comparison between different benchmark algorithms, we also perform a validation experiment showing that for certain environments, the convergence rate of TSIVR-PG is close to the theoretical guarantee. Because the parameters $N,B,m$ are dependent on the target accuracy $\epsilon$, in this section we adopt a different way to set up these parameters: We first set a fixed epoch $E$, and perform experiments using different values of the parameter $N$. The parameter $B$ and $m$ are set according to our choice of $N$ by $B = m = \sqrt{N}$. The performance of the algorithm output is calculated as the average score of the last few episodes, which is then averaged over 10 independent runs. Again, we use the FrozenLake8x8 environment to do the experiment. Because FrozenLake8x8 is a tabular environment whose transition and reward function can be easily obtained from the document, we can calculate it's optimal value simply by value iteration, which takes $0.4146$ when we choose $\gamma = 0.99$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Validating the $\\overset{\\sim}{\\mathcal{O}}{(\\epsilon^{- 2})}$ Sample Complexity", "weight": 1.0} -->

In this way, we calculate the gap between the algorithm return and the optimal value, and get log-log figure w.r.t. the gap and the number of episodes calculated by ${E{({N + {Bm}})}} = {2EN}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Result", "weight": 1.0} -->

The result is shown in the first sub-figure of Figure 2, where the blue curve is the gap between the average return of experiment outcome and the optimal value and the shaded area is the range of one standard deviation of the logarithm value. In addition, we add a orange dotted line to fit the convergence curve, whose slope takes value $- 0.496$, which nearly matches the $O{(\epsilon^{- 2})}$ theoretical bound (slope $- 0.5$).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Maximizing Non-linear Objective Function", "weight": 1.0} -->

The TSIVR-PG algorithm is designed not only to solve typical RL problems, but is also able to solve a broader class of problems where the objective function is a general concave function. Unfortunately, none of the benchmark algorithms proposed in the previous section have the ability to solve this kind of problem. To evaluate the performance of our algorithm, we choose another benchmark algorithm, which is the MaxEnt algorithm. In the experiment, we use FrozenLake8x8 environment since it's more tractable to compute $\lambda$ for a discrete state space. We set the objective function as

<!-- chunk {"id": "body-0059", "role": "body", "section": "Maximizing Non-linear Objective Function", "weight": 1.0} -->

where $\sigma$ is a fixed small constant. We choose $\sigma = 0.125$ in our experiment. The orders of $N,B,m$ are set in the same way as those in section 6.1. For the MaxEnt algorithm, note that in the original paper, the nonlinear objective function assumes the input value is the stationary state distribution $d^{\pi}$, but the input value can easily be changed into our $\lambda$ without changing the steps of the algorithm much. The result is illustrated in Fig. 2. From the result, we may see that our algorithm consistently outperforms the benchmark.
