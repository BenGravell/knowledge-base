<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies

Topics include Convex optimization, Nonconvex optimization, Reinforcement learning, Robotics, Autonomous driving, Optimization, Learning, Policy gradients, Saddle point, Stationary point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient (PG) methods are a widely used reinforcement learning methodology in many applications such as video games, autonomous driving, and robotics. In spite of its empirical success, a rigorous understanding of the global convergence of PG methods is lacking in the literature. In this work, we close the gap by viewing PG methods from a nonconvex optimization perspective. In particular, we propose a new variant of PG methods for infinite-horizon problems that uses a random rollout horizon for the Monte-Carlo estimation of the policy gradient. This method then yields an unbiased estimate of the policy gradient with bounded variance, which enables the tools from nonconvex optimization to be applied to establish global convergence. Employing this perspective, we first recover the convergence results with rates to the stationary-point policies in the literature. More interestingly, motivated by advances in nonconvex optimization, we modify the proposed PG method by introducing periodically enlarged stepsizes. The modified algorithm is shown to escape saddle points under mild assumptions on the reward and the policy parameterization. Under a further strict saddle points assumption, this result establishes convergence to essentially locally-optimal policies of the underlying problem, and thus bridges the gap in existing literature on the convergence of PG methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Results from experiments on the inverted pendulum are then provided to corroborate our theory, namely, by slightly reshaping the reward function to satisfy our assumption, unfavorable saddle points can be avoided and better limit points can be attained. Intriguingly, this empirical finding justifies the benefit of reward-reshaping from a nonconvex optimization perspective.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning (RL), an autonomous agent moves through a state space and seeks to learn a policy which maps states to a probability distribution over actions to maximize a long-term accumulation of rewards. When the agent selects a given action at a particular state, a reward is revealed and a random transition to a new state occurs according to a probability density that only depends on the current state and action, i.e., state transitions are Markovian. This evolution process is usually modeled as a Markov decision process (MDP). Under this setting, the agent must evaluate the merit of different actions by interacting with the environment. Two dominant approaches to reinforcement learning have emerged: those based on optimizing the accumulated reward directly from the policy space, referred to as "direct policy search", and those based on finding the value function by solving the Bellman fixed point equations. The goal of this work is to rigorously understand the former approach of direct policy search, specifically policy gradient (PG) methods. Policy search has gained traction recently, thanks to its ability to scale gracefully to large and even continuous spaces and to incorporate deep networks as function approximators.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the increasing prevalence of policy gradient methods, their global convergence in the infinite-horizon discounted setting, which is conventional in dynamic programming, is not yet well understood. This gap stems firstly from the fact that obtaining unbiased estimates of the policy gradient through sampling is often elusive. Specifically, following the Policy Gradient Theorem, obtaining an unbiased estimate of the policy gradient requires two significant conditions to hold: (i) the state-action pair is drawn from the discounted state-action occupancy measure of the Markov chain under the policy; (ii) the estimate of the action-value (or $Q$) function induced by the policy is unbiased. This gap also results from the fact that the value function to be maximized in RL is in general *nonconvex* with respect to the policy parameter. In the same vein as our work, there is a surging interest in studying the global convergence of PG methods, see the recent work, and concurrent work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, orthogonal to our work, these work considered convergence to the *global optimum* in several *special* RL settings: considered the linear quadratic setting, considered the tabular setting, focused on the setting with overparameterized neural networks for function approximation, and also considered the setting when the optimality gap of using certain policy class can be quantified. In contrast, our focus is on the case where the nonconvexity might be general, so that solving the problem can be NP-hard.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

When one restricts the focus to *episodic* reinforcement learning, Monte-Carlo rollout may be used to obtain *unbiased* estimates of the Q-function. In particular, the rollout simulates the MDP under certain policy up to a finite time horizon, and then collects the rewards and state-action histories along the trajectory. However, this finite-horizon rollout, though generally used in practice, is known to introduce bias in estimating an *infinite-horizon* discounted value function. Such a bias in estimating the policy gradient for infinite-horizon problems has been identified in the earlier work, both analytically and empirically. To address this bias issue, we employ in this work random geometric time rollout horizons, a technique first proposed. This rollout procedure allows us to obtain unbiased estimates of the $Q$ function, using only rollouts of finite horizons. Moreover, the random rollout horizon also creates an unbiased sampling of the state-action pair from the discounted occupancy measure. With these two challenges addressed, the policy gradient can be estimated unbiasedly.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, the policy gradient methods can be more naturally connected to the classical stochastic programming algorithms, where the unbiasedness of the stochastic gradient is a critical assumption. We refer to our algorithm as *random-horizon* policy gradient (RPG), to emphasize that the finite horizon of the Monte-Carlo rollout is random.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging this connection, we are able to address a noticeably open issue in policy gradient methods: a technical understanding of the effect of the policy parameterization on both the limiting and finite-iteration algorithm behaviors. In particular, it is well known in nonconvex optimization that with only first-order information and no additional hypothesis, convergence to a stationary point with zero gradient-norm is the best one may hope to achieve. Indeed, this is the type of points that most current PG methods are guaranteed to converge to, as pointed out. However, in some asymptotic analyses for policy gradient methods with function approximation, or their variant, actor-critic algorithms, it was claimed that the limit points of the algorithms starting from any initialization constitute the *locally-optimal policies*, i.e., the algorithms enjoy global convergence to the local-optima. However, by the theory of stochastic approximation, such a claim can only be made locally, i.e., the local-optimality can only be obtained if the algorithm starts around a local minima, under the assumption that a *strict* Lyapunov function exists.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, *global* convergence of PG methods to the *actual locally-optimal* policies, though claimed in words in some literature, is still an open question. Another line of theoretical studies of policy gradient methods only focuses on showing the one-step policy improvement, by choosing appropriate stepsizes and/or batch data sizes. Such one-step result still does not imply any global convergence result. In summary, the misuse of the term *locally-optimal policy* and the lack of studying global convergence property of PG methods motivate us to further investigate this problem from a nonconvex optimization perspective. Thanks to the analytical tools from optimization, we are able to first recover the asymptotic convergence, and then provide the convergence rate, to *stationary-point* policies.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Encouraged by this connection between nonconvex optimization and policy search, we then tackle a related question: what implications do recent algorithms that can escape saddle points for nonconvex problems have on policy gradient methods in RL? To answer this question, we identify several structural properties of RL problems that can be exploited to mitigate the underlying nonconvexity, which rely on some key assumptions on the policy parameterization and reward. Specifically, the reward needs to be bounded and either strictly positive or negative, and the policy parameterization need to be *regular*, i.e., its Fisher information matrix is positive definite (a conventional assumption in RL ). Under these mild conditions, we can establish that policy gradient methods can escape saddle points and converge to approximate *second-order* stationary points with high probability, when a *periodically enlarged stepsize* strategy is employed. We refer to the resulting method as Modified RPG (MRPG). Nevertheless, the strict positivity/negativity of reward function may amplify the variance of the gradient estimate, compared to the setting that has reward values with both signs but of smaller magnitude.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This increased variance can be alleviated by introducing a *baseline* in the gradient estimate, as advocated by existing work. Therefore, we propose two further modified updates that include the baselines, both shown to converge to approximate second-order stationary points as well.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Main Contribution: The main contribution of the present work is three-fold: i) we propose a series of random-horizon PG methods that unbiasedly estimate the true policy gradient for *infinite-horizon discounted* MDPs, which facilitates the use of analytical tools from nonconvex optimization to establish their convergence to *stationary-point* policies; ii) by virtue of such a connection of PG methods and nonconvex optimization, we propose modified RPG methods with periodically enlarged stepsizes, with guaranteed convergence to actual *locally-optimal policies* under mild conditions on the reward functions and parametrization of the policies; iii) we connect the condition on the reward function to the reward-reshaping technique advocated in empirical RL studies, justifying its benefit, both analytically and empirically, from a nonconvex optimization perspective. Additionally, we believe such a perspective opens the door to exploiting more advancements in nonconvex optimization to improve the convergence properties of policy gradient methods in RL.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In §2 Locally Optimal Policies"), we clarify the problem setting of reinforcement learning and the technicalities of Markov Decision Processes. In §3 Locally Optimal Policies") we develop the policy gradient method using random geometric Monte-Carlo rollout horizons, i.e., the RPG method. Further, we establish both its limiting (Theorem 4.2. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) and finite-sample (Theorem 4.3. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies") and Corollary 4.4. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) behaviors under standard conditions. We note that Corollary 4.4. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies") provides one of the first constant learning rate results in reinforcement learning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In §5 Locally Optimal Policies"), we focus on problems with positive bounded rewards and policies whose parameterizations are *regular*, and propose a variant of policy gradient method that employs a periodically enlarged stepsize scheme. The salient feature of this modified algorithm is that it is able to escape saddle points, an undesirable subset of stationary points, and converge to approximate second-order stationary points (Theorem 5.6 Locally Optimal Policies")). Numerical experiments in §6 Locally Optimal Policies") corroborate our main findings: for Algorithm 3 Locally Optimal Policies"), the use of random rollout horizons avoids stochastic gradient bias and hence exhibits reliable convergence that matches the theoretically established rates; moreover, for the modified RPG algorithm, use of periodically enlarged stepsizes makes it possible to escape from undesirable saddle points and yields better limiting solutions. All proofs, which constitute an integral part of the paper, are relegated to nine appendices at the end of the paper, so as not to disrupt the flow of the presentation of the main results.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations: We denote the probability distribution over the space $\mathcal{S}$ by $\mathcal{P}{(\mathcal{S})}$, and the set of integers $\{ 1,\cdots,N\}$ by $\lbrack N\rbrack$. We use $R$ to denote the set of real numbers, and $E$ to denote the expectation operator. We let $\parallel \cdot \parallel$ denote the $2$-norm of a vector in $R^{d}$, or the spectral norm of a matrix in $R^{d \times d}$. We use $|\mathcal{A}|$ to denote the cardinality of a finite set $\mathcal{A}$, or the area of a region $\mathcal{A}$, i.e., ${|\mathcal{A}|} = {\int_{\mathcal{A}}{da}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

For any matrix $A \in R^{d \times d}$, we use $A \succ 0$ and $A \succeq 0$ to denote that $A$ is positive definite and positive semi-definite, respectively. We use $\lambda_{\min}{(A)}$ and $\lambda_{\max}{(A)}$ to denote, respectively, the smallest and largest eigenvalues of some square symmetric matrix $A$, respectively. We use $E_{X}$ or $E_{X \sim {f{(x)}}}$ to denote the expectation with respect to random variable $X$. Otherwise specified, we use $E$ to denote the full expectation with respect to all random variables.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In reinforcement learning, an autonomous agent moves through a state space $\mathcal{S}$ and takes actions that belong to some action space $\mathcal{A}$. Here the spaces $\mathcal{S}$ and $\mathcal{A}$ are allowed to be either finite sets, or compact real vector spaces, i.e., $\mathcal{S} \subseteq R^{q}$ and $\mathcal{A} \subseteq R^{p}$. An action at the state causes a transition to the next state, where the transition mapping that depends on the current state and action; every such transition generates a reward revealed by the environment. The goal is for the agent to accumulate as much reward as possible in the long term. This situation can be formalized as a Markov decision process (MDP) characterized by a tuple $(\mathcal{S},\mathcal{A},P,R,\gamma)$ with Markov kernel ${P{(\left.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

s^{\prime} \middle| {s,a} \right.)}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$ that determines the transition probability from $(s,a)$ to state $s^{\prime}$. $\gamma \in {}$ is the discount factor. $R{( \cdot, \cdot )}$ is the reward that is a function^11^1$R{(s_{t},a_{t})}$ may be a random variable given $(s_{t},a_{t})$. Here without loss of generality, we assume that it is deterministic for simplicity. of $s$ and $a$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

At each time $t$, the agent executes an action $a_{t} \in \mathcal{A}$ given the current state $s_{t} \in \mathcal{S}$, following a possibly stochastic policy $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$, i.e., $a_{t} \sim \pi{( \cdot |s_{t})}$. Then, given the state-action pair $(s_{t},a_{t})$, the agent observes a reward $r_{t} = {R{(s_{t},a_{t})}}$. Thus, under any policy $\pi$ that maps states to actions, one can define the value function $V_{\pi}:{\mathcal{S}\rightarrow R}$ as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Given any initial state $s_{0}$, the goal is to find the optimal policy $\pi$ that maximizes the long-term return $V_{\pi}{(s_{0})}$, i.e., to solve the following optimization problem

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

when the model, i.e., the transition probability $P$ and the reward function $R$, is unknown to the agent. In this work, we investigate policy search methods to solve (2.1 Locally Optimal Policies")). In general, we must search over an arbitrarily complicated function class which may include those which are unbounded and discontinuous. To mitigate this issue, we propose to *parameterize* policies $\pi$ in by a vector $\theta \in R^{d}$, i.e., $\pi = \pi_{\theta}$, which gives rise to RL algorithms called *policy gradient methods*. With this parameterization, we may reduce a search over arbitrarily complicated function class in (2.1 Locally Optimal Policies")) to one over the Euclidean space $R^{d}$. Nonparametric parameterizations are also possible \[koppel2017pkgtd, koppel2018kqlearning\], but here we fix the parameterization in order to simplify exposition.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For notational convenience, we define ${J{(\theta)}}:={V_{\pi_{\theta}}{(s_{0})}}$, then the vector-valued optimization problem can be written as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Generally, the value function is nonconvex with respect to the parameter $\theta$, meaning that obtaining a globally optimal solution to (2.2 Locally Optimal Policies")) is NP-hard, unless in several special RL settings that have been identified very recently. In fact, the limit point of most gradient-based methods to nonconvex optimization is a stationary solution, which could either be a saddle point or a local optimum. Usually the local optima achieve reasonably good performance, in some cases comparable to the global optima, whereas the saddle points are undesirable and can stall training procedures. Therefore, it is beneficial to design methods that may escape saddle points -- see recent efforts on escaping saddle points with first-order methods, e.g., perturbed gradient descent, and second-order methods.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our goal in this work is to develop stochastic gradient methods to maximize $J{(\theta)}$ and rigorously understand the interplay between its limiting properties and the necessity of augmenting the algorithmic update, reward function, and policy parameterization, all toward escaping undesirable limit points. This issue was first observed and addressed in by adding random perturbations in the reinforcement learning update (which may amplify variance), based on the asymptotic convergence results. Here we provide a modern perspective and incorporate the latest developments in nonconvex optimization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

In this section, we connect stochastic gradient ascent, as it is called in stochastic optimization, with the policy gradient method, a flavor of direct policy search, in reinforcement learning. We start with the following standard assumption on the regularity of the MDP problem and the smoothness of the parameterized policy $\pi_{\theta}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The policy $\pi_{\theta}$ is differentiable with respect to $\theta$, and ${{\nabla\log}\pi_{\theta}}{(\left. a \middle| s \right.)}$, known as the *score function* corresponding to the distribution $\pi_{\theta}{( \cdot |s)}$, exists. Moreover, it is $L$-Lipschitz and has bounded norm for any ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Note that the boundedness of the reward function in Assumption3.1 Locally Optimal Policies")(i) ‣ Assumption 3.1. ‣ 3 Policy Gradient Methods ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies") is standard in the literature of policy gradient/actor-critic algorithms. The uniform boundedness of $R$ also implies that the absolute value of the Q-function is upper bounded by $U_{R}/{({1 - \gamma})}$, since by definition

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

In addition, the conditions (3.1 ‣ Assumption 3.1. ‣ 3 Policy Gradient Methods ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) and (3.2 ‣ Assumption 3.1. ‣ 3 Policy Gradient Methods ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) have also been adopted in several recent work on the convergence analysis of policy gradient algorithms. Both of the conditions can be readily satisfied by many common parametrized policies such as the Boltzmann policy and the Gaussian policy. For example, for Gaussian policy^22^2Note that in practice, the action space $\mathcal{A}$ is bounded, thus a truncated Gaussian policy over $\mathcal{A}$ is often used; see.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

in continuous spaces, $\pi_{\theta}{( \cdot |s)} = \mathcal{N}{(\phi{(s)}^{\top}\theta,\sigma^{2})}$, where $\mathcal{N}{(\mu,\sigma^{2})}$ denotes the Gaussian distribution with mean $\mu$ and variance $\sigma^{2}$, and $\phi{(s)}$ is the feature vector that incorporates some domain knowledge to approximate the mean action at state $s$. Then the score function has the form ${{\lbrack{a - {\phi{(s)}^{\top}\theta}}\rbrack}\phi{(s)}}/\sigma^{2}$, which satisfies (3.1 ‣ Assumption 3.1. ‣ 3 Policy Gradient Methods ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) and (3.2 ‣ Assumption 3.1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

‣ 3 Policy Gradient Methods ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies")) if the following three conditions hold: the norm of the feature $\|{\phi{(s)}}\|$ is bounded; the parameter $\theta$ lies in some bounded set; and the actions $a \in \mathcal{A}$ is bounded.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Under Assumption 3.1 Locally Optimal Policies"), the gradient of $J{(\theta)}$ with respect to the policy parameter $\theta$, given by the Policy Gradient Theorem, has the following form^33^3Note that here we use $\int$ to represent both summation over finite sets and integral over continuous spaces.:

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

In addition, based on the fact that for any function $b:{\mathcal{S}\rightarrow R}$ independent of action $a$,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

the policy gradient in (3.4 Locally Optimal Policies")) can be written as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

where $b{(s)}$ is usually referred to as a *baseline* function. One common choice of the baseline is the state-value function $V_{\pi_{\theta}}{(s)}$, which gives the following advantage-based policy gradient

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

In this work, we devise methods that can use iterative updates based on the classical policy gradient (3.4 Locally Optimal Policies")) or its variant that makes use of the advantage function (3.5 Locally Optimal Policies")) through the aforementioned identity regarding baselines. First note that under Assumption 3.1 Locally Optimal Policies"), we can establish the Lipschitz continuity of the policy gradient ${\nabla J}{(\theta)}$ as in the following lemma, whose proof is deferred to §A.1 Locally Optimal Policies").

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Thanks to randomness of the horizon, we note that the aforementioned sampling process creates the first unbiased estimate of the Q-function in the *discounted infinite-horizon* setting, using the Monte-Carlo rollouts of *finite horizons*. While in practice, usually finite-horizon rollouts are used to approximate the infinite-horizon Q-function, e.g., in the REINFORCE algorithm, which causes bias in the Q-function estimate, and hence the policy gradient estimate. Our sampling technique addresses this challenge, and ends up with an unbiased estimate of the policy gradient as to be introduced next. We note that the proposed sampling technique for estimating the Q-function improves the one in that uses $\text{Geom}{({1 - \gamma})}$ (instead of $\text{Geom}{({1 - \gamma^{1/2}})}$) to generate the rollout horizon $T^{\prime}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

In particular, the proposed Q-function estimate is almost surely bounded thanks to the $\gamma^{1/2}$-discount factor in (3.7 Locally Optimal Policies")), which later leads to almost sure boundedness of the stochastic policy gradient, a necessary assumption required in the convergence analysis to approximate second-order stationary points in §5 Locally Optimal Policies").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Input: s and θ. Initialize V̂ ← 0, s0 ← s, and draw a0 ∼ πθ(⋅|s0).
Draw T from the geometric distribution Geom (1−γ1/2).
Collect the instantaneous reward R (st,at) and add to value V̂; V̂ ← V̂ + γt/2 ⋅ R (st,at).
Simulate the next state st + 1 ∼ P(⋅|st,at) and action at + 1 ∼ π(⋅|st + 1).
Algorithm 2 EstV: Unbiasedly Estimating State-Value function

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Motivated by the form of policy gradient in (3.4 Locally Optimal Policies")), we propose the following stochastic estimate $\hat{\nabla}J{(\theta)}$

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

In addition, we can also estimate the policy gradient using advantage functions as in (3.5 Locally Optimal Policies")), where the advantage function is estimated by either the difference between the value function and the action-value function, or the temporal difference (TD) error. In particular, we propose the following two stochastic policy gradients

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

{\sum_{t = 0}^{T^{\prime}}{{\gamma^{1/2} \cdot R}{(s_{t},a_{t})}}} \middle| s_{0} \right. = s}.$ We refer to this subroutine as EstV, which is summarized in Algorithm 2 Locally Optimal Policies"). The reason for these alternate updates is that the off-set term can be used to reduce the variance of estimating the policy gradient.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

We then establish in the following theorem, which states that all the stochastic policy gradients ${\hat{\nabla}J{(\theta)}},{\check{\nabla}J{(\theta)}}$, and $\overset{\sim}{\nabla}J{(\theta)}$ are unbiased estimates of ${\nabla J}{(\theta)}$ \cf. ([3.4 Locally Optimal Policies"))\]. Additionally, we can also establish the boundedness of ${\|{\hat{\nabla}J{(\theta)}}\|},{\|{\check{\nabla}J{(\theta)}}\|}$, and $\|{\overset{\sim}{\nabla}J{(\theta)}}\|$, as well as $\|{{\nabla J}{(\theta)}}\|$ for any $\theta \in$. The proof is deferred to Appendix A.2 Locally Optimal Policies").

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

We note that in order to estimate the Q-function, it is not very sample-efficient to use Monte-Carlo rollouts to sample states, actions, and rewards. In fact, there exist some methods that can estimate the Q-function in parallel with the policy gradient update, which is usually referred to as *actor-critic* method. This online policy evaluation update is generally performed via *bootstrapping* algorithms such as temporal difference learning, which will introduce biases into the Q-function estimate, and thus the policy gradient estimate. In addition, such policy evaluation updates in concurrence with the policy improvement will inevitably cause correlation between consecutive stochastic policy gradients. Analyzing the non-asymptotic convergence performance of such *biased* RPG with *correlated noise* is still open and challenging, which is left as a future research direction.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

In the next sections, we shift focus to analyzing the theoretical properties of the aforementioned policy learning methods, establishing their asymptotic and finite-time performances, as well as stepsize strategies designed to mitigate the challenges of non-convexity when certain reward structure is present.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Convergence to Stationary Points", "weight": 1.0} -->

In this section, we provide convergence analyses for the policy gradient algorithms proposed in §3 Locally Optimal Policies"). We start with the following assumption for the diminishing stepsize $\alpha_{k}$, which is standard in stochastic approximation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The sequence of stepsize ${\{\alpha_{k}\}}_{k \geq 0}$ satisfies the Robbins-Monro condition

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

We first establish the convergence of Algorithm 3 Locally Optimal Policies") in the following theorem under the aforementioned technical conditions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence to Second-Order Stationary Points", "weight": 1.0} -->

In this section, we provide convergence analyses for several modified policy gradient algorithms based on Algorithm 3 Locally Optimal Policies"), which may escape saddle points and thus converge to the approximate second-order stationary points of the problem. In short, we propose a custom periodically enlarged stepsize rule, which under an additional hypothesis on the incentive structure of the problem and some other standard conditions (see §5.1 Locally Optimal Policies")), allow us to attain improved limiting policy parameters (see §5.2 Locally Optimal Policies")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence to Second-Order Stationary Points", "weight": 1.0} -->

We start with the definition of (approximate) second-order stationary points ^44^4Note that Definition 5.1 Locally Optimal Policies") is based on the maximization problem we consider here, which is slightly different from the definition for minimization problems where ${\lambda_{\max}{\lbrack{{\nabla^{2}J}{(\theta)}}\rbrack}} \leq \epsilon_{h}$ is replaced by ${\lambda_{\min}{\lbrack{{\nabla^{2}J}{(\theta)}}\rbrack}} \geq {- \epsilon_{h}}$..

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The modified RPG (MRPG) algorithms are built upon the RPG algorithm (Algorithm 3 Locally Optimal Policies")) discussed in Section 3 Locally Optimal Policies"). These modifications can yield escape from saddle points under certain conditions, and hence convergence to approximate local extrema.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In order to reduce the variance of the RPG update (3.11 Locally Optimal Policies")), we employ the stochastic gradients $\check{\nabla}J{(\theta)}$ and $\overset{\sim}{\nabla}J{(\theta)}$ as defined in (3.9 Locally Optimal Policies")) and (3.10 Locally Optimal Policies")), respectively. Note that the evaluations of both $\check{\nabla}J{(\theta)}$ and $\overset{\sim}{\nabla}J{(\theta)}$ need to estimate the state-value function ${\hat{V}}_{\pi_{\theta}}{(s)}$ for any given $\theta$ and $s$. Built upon the subroutines EstQ and EstV, we summarize the subroutine for calculating all three types of stochastic policy gradients as EvalPG in Algorithm 4 Locally Optimal Policies").

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In order to converge to the approximate second-order stationary points, we modify the RPG algorithm, i.e., Algorithm 3 Locally Optimal Policies"), by *periodically enlarging* the *constant* stepsize of the update, once every $k_{\text{thre}}$ steps. The larger stepsize can amplify the variance along the eigenvector corresponding to the largest eigenvalue of the Hessian, which provides a direction for the update to escape at the saddle points. This idea was first introduced in for general stochastic gradient methods, and is outlined in Algorithm 5 Locally Optimal Policies"). Note that $\alpha$ and $\beta$ are the constant stepsizes with $\beta > \alpha > 0$, whose values will be given in §5.2 Locally Optimal Policies") to obtain certain convergence rates. To design this behavior while avoiding unnecessarily large variance, we propose updates that make use of the advantage function, i.e., $\check{\nabla}J{(\theta)}$ and $\overset{\sim}{\nabla}J{(\theta)}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The resulting algorithm, with periodically enlarged stepsizes, and stochastic policy gradients that use advantage functions, is summarized as Algorithm 5 Locally Optimal Policies"). Subsequently, we shift focus to characterizing its policy learning performance analysis.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Input: s, a, θ and the gradient type ♢.
if gradient type $\diamondsuit = \hat{}$ then
Obtain an estimate Q̂πθ (s,a) ← EstQ (s,a,θ).
Calculate $\hat{\nabla}J{(\theta)}$, i.e., let

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm", "weight": 1.0} -->

else if gradient type $\diamondsuit = \check{}$ then
Obtain estimates Q̂πθ (s,a) ← EstQ (s,a,θ) and V̂πθ (s) ← EstV (s,θ).
Calculate $\check{\nabla}J{(\theta)}$, i.e., let

<!-- chunk {"id": "body-0057", "role": "body", "section": "Algorithm", "weight": 1.0} -->

else if gradient type $\diamondsuit = \overset{\sim}{}$ then
Simulate the next state: s′ ∼ P(⋅|s,a).
Obtain estimates V̂πθ (s) ← EstV (s,θ) and V̂πθ (s′) ← EstV (s′,θ).
Calculate $\overset{\sim}{\nabla}J{(\theta)}$, i.e., let

<!-- chunk {"id": "body-0058", "role": "body", "section": "Algorithm", "weight": 1.0} -->

return Stochastic policy gradient gθ
Algorithm 4 EvalPG: Calculating the Three Types of Stochastic Policy Gradients

<!-- chunk {"id": "body-0059", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Input: s0, θ0, and the gradient type ♢, initialize k ← 0, return set ${\hat{}}^{\ast}\leftarrow\varnothing$.
Draw Tk + 1 from the geometric distribution Geom (1−γ), and draw a0 ∼ πθk(⋅|s0).
Simulate the next state st + 1 ∼ P(⋅|st,at) and action at + 1 ∼ πθk(⋅|st + 1).
Calculate the stochastic gradient gk ← EvalPG (sTk + 1,aTk + 1,θk,♢).
if (k mod kthre) = 0 then

<!-- chunk {"id": "body-0060", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Update the iteration counter k = k + 1.
return θ uniformly at random from the set ${\hat{}}^{\ast}$.
Algorithm 5 MRPG: Modified Random-horizon Policy Gradient Algorithm

<!-- chunk {"id": "body-0061", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In this subsection, we provide a finite-iteration convergence result for the modified RPG algorithm, i.e., Algorithm 5 Locally Optimal Policies"). To this end, we first introduce the following condition, built upon Assumption 3.1 Locally Optimal Policies"), which is required in the sequel.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

The score function ${\nabla\log}\pi_{\theta}$ exists, and its norm is bounded by ${\|{{\nabla\log}\pi_{\theta}}\|} \leq B$ for any $\theta$. Also, the Jacobian of ${\nabla\log}\pi_{\theta}$ has bounded norm and is Lipschitz continuous, i.e., there exist constants $\rho > 0$ and $L < \infty$ such that for any ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

The integral of the Fisher information matrix induced by $\pi_{\theta}{( \cdot |s)}$ is positive-definite uniformly for any $\theta \in R^{d}$, i.e., there exists a constant $L_{I} > 0$ such that

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

We note that Assumption 5.2 Locally Optimal Policies") is indeed standard, and can be readily satisfied in practice. First, the strict positivity (or negativity) of the reward function in Assumption 5.2 Locally Optimal Policies")(i) ‣ Assumption 5.2. ‣ 5.2 Convergence Analysis ‣ 5 Convergence to Second-Order Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies") can be easily satisfied by adding (or subtracting) an offset to the original non-negative and upper-bounded reward. In fact, it can be justified in the following lemma that adding any offset does not change the optimal policy of the original MDP.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we present several experiments to corroborate the results of the previous two sections. Focused on the discounted infinite-horizon setting, we use the Pendulum environment in the OpenAI gym as the test environment. In particular, the pendulum starts in a random position, and the goal is to swing it up so that it stays upright. The state is a vector of dimension three, i.e., $s_{t} = {({\cos{(\theta_{t})}},{\sin{(\theta_{t})}},{\overset{˙}{\theta}}_{t})}^{\top}$, where $\theta_{t}$ is the angle between the pendulum and the upright direction, and ${\overset{˙}{\theta}}_{t}$ is the derivative of $\theta_{t}$. The action $a_{t}$ is a one-dimensional scalar representing the joint effort. In addition, the reward $R{(s_{t},a_{t})}$ is defined as

<!-- chunk {"id": "body-0066", "role": "body", "section": "Simulations", "weight": 1.0} -->

which lies in $\lbrack{- 17.1736044},{- 0.5}\rbrack$, since $\theta$ is normalized between $\lbrack{- \pi},\pi\rbrack$ and $a_{t}$ lies in $\lbrack{- 20},20\rbrack$. Different from the reward in the original Pendulum environment, we shift the reward by $- 0.5$, so that the negativity of $R{(s,a)}$ in Assumption 5.2 Locally Optimal Policies") is satisfied, i.e., $L_{R} = 0.5$. The transition probability follows the physical rules of Newton's Second Law. We choose the discounted factor $\gamma$ to be $0.97$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Simulations", "weight": 1.0} -->

We use Gaussian policy $\pi_{\theta}$ truncated over the support $\lbrack{- 20},20\rbrack$, which is parameterized as $\pi_{\theta}{( \cdot |s)} = \mathcal{N}{(\mu_{\theta}{(s)},\sigma^{2})}$, where $\sigma = 1.0$ and ${\mu_{\theta}{(s)}}:{\mathcal{S}\rightarrow\mathcal{A}}$ is a neural network with two hidden layers. Each hidden layer contains $10$ neurons and uses *softmax* as activation functions. The output layer of $\mu_{\theta}{(s)}$ uses $\tanh$ as the activation function. One can verify that such parameterization satisfies Assumption 5.2 Locally Optimal Policies").

<!-- chunk {"id": "body-0068", "role": "body", "section": "Simulations", "weight": 1.0} -->

We first compare the performance of our algorithms with that of the popular REINFORCE algorithm. To make the comparison fair, we choose the length of the rollout horizon of REINFORCE to be the expected value of the geometric distribution with success probability $1 - \gamma^{1/2}$, i.e., $T = {\gamma^{1/2}/{({1 - \gamma^{1/2}})}} = 66$. Recall that the length of the rollout horizon for Q-function estimate in our algorithm is drawn from $\text{Geom}{({1 - \gamma^{1/2}})}$. After each rollout, i.e., one episode, the policy parameter $\theta_{k}$ is updated and then evaluated by calculating the value of $J{(\theta)}$ using the Monte-Carlo method.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Simulations", "weight": 1.0} -->

First, we compare the performance of RPG ( Algorithm 3 Locally Optimal Policies")) with that of the popular REINFORCE algorithm. Recall that REINFORCE creates bias in the policy gradient estimate. To make a fair comparison, we set the rollout horizon of REINFORCE to be the expected value of the geometric distribution with success probability $1 - \gamma^{1/2}$, the same distribution that the rollout horizon for Q-function estimate in Algorithm 1 Locally Optimal Policies") is drawn, i.e., $T = {\gamma^{1/2}/{({1 - \gamma^{1/2}})}} = 66$. For RPG, we test both diminishing and constant stepsizes, where the former is set as $\alpha_{k} = {1/\sqrt{k}}$ and the latter is set as $\alpha_{k} = 0.05$ for all $k \geq 0$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Simulations", "weight": 1.0} -->

Fig. 1 Locally Optimal Policies")(left) plots the discounted return obtained along the iterations of REINFORCE and our proposed RPG algorithms. The return is estimated by running the algorithms $30$ times. The bar areas represent the standard deviation region calculated using the $30$ simulations. It is shown that our proposed algorithms perform slightly better than REINFORCE in terms of discounted return, but with higher variance. This is expected since our policy gradient estimates are unbiased, compared to REINFORCE. Moreover, the higher variance possibly comes from the additional randomness of the rollout horizon in RPG.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Simulations", "weight": 1.0} -->

We also evaluate the convergence of the expected gradient norm square studied in Theorem 4.3. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies") and Corollary 4.4. ‣ 4 Convergence to Stationary Points ‣ Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies"). Fig. 1 Locally Optimal Policies")(right) plots the empirical estimates of $E{\|{{\nabla J}{(\theta_{m})}}\|}^{2}$ after $30$ runs of the algorithms. It is verified that using diminishing stepsize results in convergence of the gradient norm to zero a.s. (the curve keeps decreasing), while using constant stepsizes leads to an error that is lower-bounded above zero (the curves stay mostly unchanged after certain episodes). Moreover, it is shown that a smaller constant stepsize indeed creates a smaller size of the error neighborhood. Convergence rates under both diminishing and constant stepsize choices are sublinear, as identified in our theoretical results.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Simulations", "weight": 1.0} -->

We further evaluate the performance of Algorithm 5 Locally Optimal Policies") that uses intermittently larger stepsizes with stochastic policy gradient $\hat{\nabla}J{(\theta)}$ as *MRPG~1~*, which theoretically we expect to yield favorable performance under appropriately designed incentive structure. Thus, in order to verify the significance of the CNC condition in escaping saddle points, we also test the MRPG~1~ algorithm in the environment that has mixed reward, i.e., the reward can be both positive and negative. We generate such an environment by adding a constant $10.0$ onto the reward defined in (6.1 Locally Optimal Policies")). Each learning curve in Figure 2 Locally Optimal Policies") is run for $30$ times, and the bar area in the figure represents plus or minus one sample standard deviation of $30$ trajectories.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Simulations", "weight": 1.0} -->

First, it can be seen from Figure 2 Locally Optimal Policies")(left) that RPG achieves almost identical performance as REINFORCE, which shows that the *unbiasedness* of the RPG update seems to not hold great advantages over the biased PG obtained from REINFORCE, in finding the first-order stationary points. On the other hand, Figure 2 Locally Optimal Policies")(left) illustrates that MRPG~1~ achieves greater return than RPG, substantiating the necessity of finding approximate second-order stationary points than first-order ones. To the best of our knowledge, this appears to be the first empirical observation in RL that saddle-escaping techniques may benefit the policy learning. Interestingly, when the reward is "mixed", the MRPG~1~ algorithm suffers from lower discounted return and larger variance across $30$ trajectories. This may be explained by the fact that different trajectories may converge to different saddle points or stationary points that may be of very different qualities. This observation also justifies the necessity of escaping undesirable saddle points for policy gradient updates.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Simulations", "weight": 1.0} -->

We have also evaluated the performance of the other two MRPG algorithms that use the policy gradients $\check{\nabla}J{(\theta)}$ and $\overset{\sim}{\nabla}J{(\theta)}$, which we refer to as *MRPG~2~* and *MRPG~3~*, respectively, in Figure 2 Locally Optimal Policies")(right). Recall that the key differences of these alternative gradient updates is that they subtract a baseline or use Bellman's evaluation equation, respectively, to replace the $Q$ function that multiplies the score function with the advantage function. As shown in Figure 2 Locally Optimal Policies")(right), the update with baselines does not always benefit the variance reduction, at least in this experiment.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Simulations", "weight": 1.0} -->

In particular, the policy gradient $\check{\nabla}J{(\theta)}$ that uses $V{(s)}$ as the baseline indeed outperforms the MRPG~1~ algorithm; however, the policy gradient $\check{\nabla}J{(\theta)}$ that uses TD error to estimate the advantage function performs even worse. Even so, all the MRPG algorithms beat the REINFORCE algorithm in terms of discounted return, and MRPG~1~ and MRPG~2~ also beat REINFORCE in terms of variance.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Despite its tremendous popularity, policy gradient methods in RL have rarely been investigated in terms of their global convergence, i.e., there seems to be a gap in the literature regarding the limiting properties of policy search and how this is a function of the initialization. Motivated by this gap, we have adopted the perspective and tools from nonconvex optimization to clarify and partially overcome some of the challenges of policy search for MDPs over continuous spaces. In particular, we have developed a series of random-horizon policy gradient algorithms, which generate *unbiased* estimates of the policy gradient for the *infinite-horizon* setting. Under standard assumptions for RL, we have first recovered the convergence to stationary-point policies for such first-order optimization algorithms. Moreover, by virtue of the recent results in nonconvex optimization, we have proposed the modified RPG algorithms by introducing periodically enlarged stepsizes, which are shown to be able to escape saddle points and converge to actual *local optimal* policies under mild conditions that are satisfied for most modern reinforcement learning applications. Specifically, we have given an optimization-based explanation of why reward-reshaping is beneficial: it improves the curvature profile of the problem in neighborhoods of saddle points.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions", "weight": 1.0} -->

On the inverted pendulum balancing task, we have experimentally corroborated our theoretical findings. Many enhancements are possible for future research directions via the link between policy search and nonconvex optimization: rate improvements through acceleration, trust region methods, variance reduction, and Quasi-Newton methods.
