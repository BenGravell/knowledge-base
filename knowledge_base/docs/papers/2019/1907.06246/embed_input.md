<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Global Convergence of Actor-Critic: A Case for Linear Quadratic Regulator with Ergodic Cost

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the empirical success of the actor-critic algorithm, its theoretical understanding lags behind. In a broader context, actor-critic can be viewed as an online alternating update algorithm for bilevel optimization, whose convergence is known to be fragile. To understand the instability of actor-critic, we focus on its application to linear quadratic regulators, a simple yet fundamental setting of reinforcement learning. We establish a nonasymptotic convergence analysis of actor-critic in this setting. In particular, we prove that actor-critic finds a globally optimal pair of actor (policy) and critic (action-value function) at a linear rate of convergence. Our analysis may serve as a preliminary step towards a complete theoretical understanding of bilevel optimization with nonconvex subproblems, which is NP-hard in the worst case and is often solved using heuristics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The actor-critic algorithm is one of the most used algorithms in reinforcement learning. Compared with the classical policy gradient algorithm, actor-critic tracks the action-value function (critic) in policy gradient in an online manner, and alternatively updates the policy (actor) and the critic. On the one hand, the online update of critic significantly reduces the variance of policy gradient and hence leads to faster convergence. On the other hand, it also introduces algorithmic instability, which is often observed in practice and parallels the notoriously unstable training of generative adversarial networks. Such instability of actor-critic originates from several intertwining challenges, including (i) function approximation of actor and critic, (ii) improper choice of stepsizes, (iii) the noise arising from stochastic approximation, (iv) the asynchrony between actor and critic, and (v) possibly off-policy data used in the update of critic. As a result, the convergence of actor-critic remains much less well understood than that of policy gradient, which itself is open. Consequently, the practical use of actor-critic often lacks theoretical guidance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we aim to theoretically understand the algorithmic instability of actor-critic. In particular, under a bilevel optimization framework, we establish the global rate of convergence and sample complexity of actor-critic for linear quadratic regulators (LQR) with ergodic cost, a simple yet fundamental setting of reinforcement learning, which captures all the above challenges. Compared with the classical two-timescale analysis of actor-critic, which is asymptotic in nature and requires finite action space, our analysis is fully nonasymptotic and allows for continuous action space. Moreover, beyond the convergence to a stable equilibrium obtained by the classical two-timescale analysis, we for the first time establish the linear rate of convergence to a globally optimal pair of actor and critic. In addition, we characterize the required sample complexity. As a technical ingredient and byproduct, we for the first time establish the sublinear rate of convergence for the gradient temporal difference algorithm for ergodic cost and dependent data, which is of independent interest.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work adds to two lines of works in machine learning, stochastic analysis, and optimization: (i) Actor-critic falls into the more general paradigm of bilevel optimization. Bilevel optimization is defined by two nested optimization problems, where the upper-level optimization problem relies on the output of the lower-level one. As a special case of bilevel optimization, minimax optimization is prevalent in machine learning. Recent instances include training generative adversarial neural networks, (distributionally) robust learning, and imitation learning. Such instances of minimax optimization remain challenging as they lack convexity-concavity in general. The more general paradigm of bilevel optimization remains even more challenging, as there does not exist a unified objective function for simultaneous minimization and maximization. In particular, actor-critic couples the nonconvex optimization of actor (policy gradient) as its upper level and the convex-concave minimax optimization of critic (gradient temporal difference) as its lower level, each of which is challenging to analyze by itself. Most existing convergence analysis of bilevel optimization is based on two-timescale analysis.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, as two-timescale analysis abstracts away most technicalities via the lens of ordinary differential equations, which is asymptotic in nature, it often lacks the resolution to capture the nonasymptotic rate of convergence and sample complexity, which are obtained via our analysis. (ii) As a proxy for analyzing more general reinforcement learning settings, LQR is studied in a recent line of works. In particular, a part of our analysis is based on the breakthrough of Fazel et al., which gives the global convergence of the population-version policy gradient algorithm for LQR and its finite-sample version based on the zeroth-order estimation of policy gradient based on the cumulative reward or cost. However, such zeroth-order estimation of policy gradient often suffers from large variance, as it involves the randomness of an entire trajectory. In contrast, actor-critic updates critic in an online manner, which reduces such variance but also introduces instability and complicates the convergence analysis. In particular, as the update of critic interleaves with the update of actor, the policy gradient for the update of actor is biased due to the inexactness of critic.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Meanwhile, the update of critic has a "moving target", as it attempts to evaluate an actor that evolves along the iterations. A key to our analysis is to handle such asynchrony between actor and critic, which is a ubiquitous challenge in bilevel optimization. We hope our analysis may serve as the first step towards analyzing actor-critic in more general reinforcement learning settings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

We consider a Markov decision process, which is defined by $(\mathcal{X},\mathcal{U},P,c,D_{0})$. Here $\mathcal{X}$ and $\mathcal{U}$ are the state and action spaces, respectively, $P:{{\mathcal{X} \times \mathcal{U}}\rightarrow{\mathcal{P}{(\mathcal{X})}}}$ is the Markov transition kernel, $c:{{\mathcal{X} \times \mathcal{U}}\rightarrow{\mathbb{R}}}$ is the cost function, and $D_{0} \in {\mathcal{P}{(\mathcal{X})}}$ is the distribution of the initial state $x_{0}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

For any $t \geq 0$, at the $t$-th time step, the agent takes action $u_{t} \in \mathcal{U}$ at state $x_{t} \in \mathcal{X}$, which incurs a cost $c{(x_{t},u_{t})}$ and moves the environment into a new state $x_{t + 1} \sim P{(\cdot |x_{t},u_{t})}$. A policy specifies how the action $u_{t}$ is taken at a given state $x_{t}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

Specifically, in order to handle infinite state and action spaces, we focus on a parametrized policy class $\{\pi_{\omega}:{{\mathcal{X}\rightarrow{\mathcal{P}{(\mathcal{U})}}},{\omega \in \Omega}}\}$, where $\omega$ is the parameter of policy $\pi_{\omega}$, and the agent takes action $u \sim \pi_{\omega}{(\cdot |x)}$ at a given state $x \in \mathcal{X}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

The agent aims to find a policy that minimizes the infinite-horizon time-average cost, that is, Moreover, for policy $\pi_{\omega}$, we define the (advantage) action-value and state-value functions respectively as where we use ${\mathbb{E}}_{\omega}$ to indicate that the state-action pairs ${\{{(x_{t},u_{t})}\}}_{t \geq 1}$ are obtained from policy $\pi_{\omega}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

Actor-critic is based on the idea of solving the minimization problem in (2.1) via first-order optimization, which uses an estimator of ${\nabla_{\omega}J}{(\omega)}$. In detail, by the policy gradient theorem, we have where $\rho_{\omega} \in {\mathcal{P}{(\mathcal{X})}}$ is the stationary distribution induced by $\pi_{\omega}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

Based on (2.3), actor-critic consists two steps: (i) a policy evaluation step that estimates the action-value function $Q_{\omega}$ (critic) via temporal difference learning, where $Q_{\omega}$ is estimated using a parametrized function class $\{ Q^{\theta}:{\theta \in \Theta}\}$, and (ii) a policy improvement step that updates the parameter $\omega$ of policy $\pi_{\omega}$ (actor) using a stochastic version of the policy gradient in (2.3), where $Q_{\omega}$ is replaced by the corresponding estimator $Q^{\theta}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

As shown in Yang et al., actor-critic can be cast as solving a bilevel optimization problem, which takes the form where $\mathcal{B}^{\omega}$ is an operator that depends on $\pi_{\omega}$. In this problem, the actor and critic correspond to the upper-level and lower-level variables, respectively. Under this framework, the policy update can be viewed as a stochastic gradient step for the upper-level problem in (2.4). The objective in (2.5) is usually the mean-squared Bellman error or mean-squared projected Bellman error. Moreover, when $\mathcal{B}^{\omega}$ is the Bellman evaluation operator associated with $\pi_{\omega}$ and we solve the lower-level problem in (2.5) via stochastic semi-gradient descent, we obtain the TD update for policy evaluation. Similarly, when $\mathcal{B}^{\omega}$ is the projected Bellman evaluation operator associated with $\pi_{\omega}$, solving the lower level problem naturally recovers the GTD2 and TDC algorithms for policy evaluation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Actor-Critic Algorithm", "weight": 1.0} -->

Therefore, the actor-critic algorithm is a first-order online algorithm for the bilevel optimization problem in (2.4) and (2.5). We remark that bilevel optimization contains a family of extremely challenging problems. Even when the objective functions are linear, bilevel programming is NP-hard. In practice, various heuristic algorithms are applied to solve them approximately.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

As the simplest optimal control problem, linear quadratic regulator serves as a perfect baseline to examine the performance of reinforcement learning methods. Viewing LQR from the lens of MDP, the state and action spaces are $\mathcal{X} = {\mathbb{R}}^{d}$ and $\mathcal{U} = {\mathbb{R}}^{k}$, respectively. Besides, the state transition dynamics and cost function are specified by where $\epsilon_{t} \sim {N{(0,\Psi)}}$ is the random noise that is i.i.d. for each $t \geq 0$, and $A$, $B$, $Q$, $R$, $\Psi$ are matrices of proper dimensions with ${Q,R,\Psi} \succ 0$. Moreover, we assume that the dimensions $d$ and $k$ are fixed throughout this paper.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

For the problem of minimizing the infinite-horizon time-average cost $\operatorname{lim\ sup}_{T\rightarrow\infty}{T^{- 1}{\sum_{t = 0}^{T}{{\mathbb{E}}{\lbrack{c{(x_{t},u_{t})}}\rbrack}}}}$ with $x_{0} \sim D_{0}$, it is known that the optimal action are linear in the corresponding state.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

Specifically, the optimal actions ${\{ u_{t}^{\ast}\}}_{t \geq 0}$ satisfy $u_{t}^{\ast} = {- {K^{\ast}x_{t}}}$ for all $t \geq 0$, where $K^{\ast} \in {\mathbb{R}}^{k \times d}$ can be written as $K^{\ast} = {{({R + {B^{\top}P^{\ast}B}})}^{- 1}B^{\top}P^{\ast}A}$, with $P^{\ast}$ being the solution to the discrete algebraic Riccati equation In the optimal control literature, it is common to solve LQR by first estimating matrices $A$, $B$, $Q$, $R$ and then solving the Riccati equation in (2.7) with these matrices replaced by their estimates.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

Such an approach is known as model-based as it requires estimating the model parameters and the performance of the planning step in (2.7) hinges on how well the true model is estimated. See, e.g, Dean et al.; Tu and Recht for theoretical guarantees of model-based methods.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

In contrast, from a purely data-driven perspective, the framework of model-free reinforcement learning offers a general treatment for optimal control problems without the prior knowledge of the model. Thanks to its simple structure, LQR enables us to assess the performances of reinforcement learning algorithms from a theoretical perspective. Specifically, it is shown that policy iteration, adaptive dynamic programming, and policy gradient methods are all able to obtain the optimal policy of LQR. Also see Recht for a thorough review of reinforcement learning methods in the setting of LQR.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Actor-Critic Algorithm for LQR", "weight": 1.0} -->

In this section, we establish the actor-critic algorithm for the LQR problem introduced in §2.2. Recall that the optimal policy of LQR is a linear function of the state. Throughout the rest of this paper, we focus on the family of linear-Gaussian policies where $\sigma > 0$ is a fixed constant. That is, for any $t \geq 0$, at state $x_{t}$, we could write the action $u_{t}$ by $u_{t} = {{- {Kx_{t}}} + {\sigma \cdot \eta_{t}}}$, where $\eta_{t} \sim {N{(0,I_{k})}}$. We note that if $\sigma = 0$, then the optimal policy $u = {- {K^{\ast}x}}$ belongs to our policy class. Here, instead of focusing on deterministic policies, we adopt Gaussian policies to encourage exploration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Actor-Critic Algorithm for LQR", "weight": 1.0} -->

For policy $\pi_{K}$, the corresponding time-average cost $J{(K)}$, state-value function $V_{K}$, and action-value function $Q_{K}$ are specified as in (2.1) and (2.2), respectively.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Actor-Critic Algorithm for LQR", "weight": 1.0} -->

In the following, we first establish the policy gradient and value functions for the ergodic LQR in §3.1. Then, in §3.2, we present the on-policy natural actor-critic algorithm, which is further extended to the off-policy setting in §3.3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Policy Gradient Theorem for Ergodic LQR", "weight": 1.0} -->

For any policy $\pi_{K}$, by (2.6), the state dynamics is given by a linear dynamical system Here we define $\Psi_{\sigma}:={\Psi + {{\sigma^{2} \cdot B}B^{\top}}}$ in (3.2) to simplify the notation. It is known that, when ${\rho{({A - {BK}})}} < 1$, the Markov chain in (3.2) has stationary distribution $N{(0,\Sigma_{K})}$, denoted by $\rho_{K}$ hereafter, where $\Sigma_{K}$ is the unique positive definite solution to the Lyapunov equation In the following proposition, we establish $J{(K)}$, the value functions, and the gradient ${\nabla_{K}J}{(K)}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

Natural policy gradient updates the variable along the steepest direction with respect to Fisher metric. For the Gaussian policies defined in (3.1), by (3.10), the Fisher's information of policy $\pi_{K}$, denoted by $\mathcal{I}{(K)}$, is given by where ${i,i'} \in {\lbrack k\rbrack}$, ${j,j'} \in {\lbrack d\rbrack}$, $K_{ij}$ and $K_{i'j'}$ are the $(i,j)$- and $(i',j')$-th entries of $K$, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

Thus, in view of (3.9) in Proposition 3.1 and (3.2), natural policy gradient algorithm updates the policy parameter in the direction of By (3.7), we can write $E_{K}$ as ${\Theta_{K}^{22}K} - \Theta_{K}^{21}$, where $\Theta_{K}$ is the coefficient matrix of the quadratic component of $Q_{K}$. Such a connection lays the foundation of the natural actor-critic algorithm. Specifically, in each iteration of the algorithm, the actor updates the policy via $K - {\gamma \cdot {({{{\hat{\Theta}}^{22}K} - {\hat{\Theta}}^{21}})}}$, where $\gamma$ is the stepsize and $\hat{\Theta}$ is an estimator of $\Theta_{K}$ returned by any policy evaluation algorithm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

We present such a general natural actor-critic method in Algorithm 1, under the assumption that we are given a stable policy $K_{0}$ for initialization. Such an assumption is standard in literatures on model-free methods for LQR.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

Input: Initial policy πK0 such that ρ (A − B K0) < 1, stepsizes γ for policy update, and a policy evaluation algorithm. Initialization: Set the current policy πK by letting K ← K0. while updating current policy do Critic step. Estimate ΘK in (3.7) via a policy evaluation algorithm, e.g., the on-policy GTD algorithm (Algorithm 2), which returns an estimator Θ̂ of ΘK. Actor step. Update the policy parameter by K ← K − γ ⋅ (Θ̂22 K − Θ̂21). Output: The final policy πK, matrix Θ̂ that estimates ΘK, and Ĵ that approximates J (K). Algorithm 1 Natural Actor-Critic Algorithm for Linear Quadratic Regulator To obtain an online actor-critic algorithm, in the sequel, we propose an online policy evaluation algorithm for ergodic LQR based on temporal difference learning. Let $\pi_{K}$ be the policy of interest.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

For notational simplicity, for any state-action pair ${(x,u)} \in {\mathbb{R}}^{d + k}$, we define the feature function and denote by $\text{svec}{(\Theta_{K})}$ by $\theta_{K}^{\ast}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

Using this notation, the quadratic component in $Q_{K}$ can be written as $\phi{(x,u)}^{\top}\theta_{K}^{\ast}$, and the Bellman equation for $Q_{K}$ becomes In order to further simplify the notation, hereafter, we define $\vartheta_{K}^{\ast} = {({J{(K)}},\theta_{K}^{\ast \top})}^{\top}$, denote by ${\mathbb{E}}_{(x,u)}$ the expectation with respect to $x \sim \rho_{K}$ and $u \sim \pi_{K}{(\cdot |x)}$, and let $(x',u')$ be the state-action pair subsequent to $(x,u)$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Natural Actor-Critic Algorithm", "weight": 1.0} -->

Furthermore, to estimate $J{(K)}$ and $\theta_{K}^{\ast}$ in (3.14) simultaneously, we define Notice that ${J{(K)}} = {{\mathbb{E}}_{(x,u)}{\lbrack{c{(x,u)}}\rbrack}}$. By direct computation, it can be shown that $\vartheta_{K}^{\ast}$ satisfies the following linear equation whose solution is unique if and only if $\Xi_{K}$ in (3.15) is invertible. The following lemma shows that, when $\pi_{K}$ is a stable policy, $\Xi_{K}$ is indeed invertible.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Extension to the Off-Policy Setting", "weight": 1.0} -->

Recall that in our natural actor-critic algorithm, the critic can apply any policy evaluation algorithm to estimate ${\hat{\Theta}}_{K}$. When using an off-policy method, we obtain an off-policy actor-critic algorithm. In this section, we extend Algorithm 2 to the off-policy setting using importance sampling. Specifically, let $\pi_{b}$ be the behavior policy and suppose it induces a stationary distribution $\rho_{b}$ over the state space ${\mathbb{R}}^{d}$. Moreover, let $\pi_{K}$ be the policy of interest and let ${\tau_{K}{(x,u)}} = {{{\pi_{K}{(\left. u \middle| x \right.)}}/\pi_{b}}{(\left. u \middle| x \right.)}}$ be the importance sampling ratio.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Extension to the Off-Policy Setting", "weight": 1.0} -->

Then, the Bellman equation in (3.14) can be written as where $x'$ is the next state given $(x,u)$, and $u' \sim \pi_{b}{(\cdot |x)}$. In the following, we denote by ${\mathbb{E}}_{(x,u)}$ the expectation with respect to $x \sim \rho_{b}$ and $u \sim \pi_{b}{(\cdot |x)}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Extension to the Off-Policy Setting", "weight": 1.0} -->

Similar to $\Xi_{K}$ and $b_{K}$ defined in (3.15), for the off-policy setting, we define Based on (3.23) and direct computation, it can be shown that $\vartheta_{K}^{\ast} = {({J{(K)}},{\text{svec}{(\Theta_{K})}^{\top}})}^{\top}$ is the solution to linear equation Similar to the derivations in §3.2, we propose to estimate $\vartheta_{K}^{\ast}$ by solving a minimax optimization problem: Notice that both $\overline{F}{(\vartheta,\omega)}$ and its gradient can be estimated unbiasedly using transitions sampled from the behavior policy. Solving (3.24) using stochastic gradient method, we obtain the off-policy GTD algorithm for the ergodic setting. Due to the similarity to Algorithm 2, we defer the details of off-policy GTD to Algorithm 3 in the appendix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Extension to the Off-Policy Setting", "weight": 1.0} -->

Combining this policy evaluation method with Algorithm 1, we establish the off-policy on-line natural actor-critic algorithm.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

In this section, we establish the global convergence of the natural actor-critic algorithm. To this end, we first focus on the problem of policy evaluation by assessing the finite sample performance of the on-policy GTD algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

Note that only $\hat{\Theta}$ returned by the GTD algorithm is utilized in the natural actor-critic algorithm for policy update. Thus, in the policy evaluation problem for a linear policy $\pi_{K}$, we only need to study the estimation error ${\|{\hat{\Theta} - \Theta_{K}}\|}_{F}^{2}$, which characterizes the closeness between the direction of policy update in Algorithm 1 and the true natural policy gradient.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

Furthermore, recall that we restrict the primal and dual variables respectively to compact sets $\mathcal{X}_{\Theta}$ and $\mathcal{X}_{\Omega}$ for algorithmic stability. We make the following assumption on $\mathcal{X}_{\Theta}$ and $\mathcal{X}_{\Omega}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Let $\pi_{K_{0}}$ be the initial policy in Algorithm 1. We assume that $\pi_{K_{0}}$ is a stable policy such that ${\rho{({A - {BK_{0}}})}} < 1$. Consider the policy evaluation problem for $\pi_{K}$. We assume that ${J{(K)}} \leq {J{(K_{0})}}$. Moreover, let $\mathcal{X}_{\Theta}$ and $\mathcal{X}_{\Omega}$ in (3.2) be defined as Here, ${\overset{\sim}{R}}_{\Theta}$ and ${\overset{\sim}{R}}_{\Omega}$ are two parameters that does not depend on $K$. Specifically, we have The assumption that we have access to a stable policy $K_{0}$ for initialization is commonly made in literatures on model-free methods for LQR.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Besides, ${\rho{({A - {BK_{0}}})}} < 1$ implies that $J{(K_{0})}$ is finite. Here we assume ${J{(K)}} \leq {J{(K_{0})}}$ for simplicity. Even if ${J{(K)}} > {J{(K_{0})}}$, we can replace $J{(K_{0})}$ in (4.1) -- (4.4) by $J{(K)}$ and the theory of policy evaluation still holds. Moreover, as we will show in Theorem 4.3. ‣ 4 Theoretical Results ‣ On the Global Convergence of Actor-Critic: A Case for Linear Quadratic Regulator with Ergodic Cost"), the actor-critic algorithm creates a sequence policies whose objective values decreases monotonically. Thus, here we assume ${J{(K)}} \leq {J{(K_{0})}}$ without loss of generality.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Furthermore, as shown in the proof, the construction of ${\overset{\sim}{R}}_{\Theta}$ and ${\overset{\sim}{R}}_{\Omega}$ ensures that $(\vartheta_{K}^{\ast},0)$ is the saddle-point of the minimax optimization in (3.2). In other words, the solution to (3.2) is the same as the unconstrained problem ${\min_{\vartheta}{\max_{\omega}F}}{(\vartheta,\omega)}$. When replacing the population problem by a sample-based optimization problem, restrictions on the primal and dual variables ensures that the iterates of the GTD algorithm remains bounded.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

We present the theoretical result for the online GTD algorithm as follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Proofs of the Main Results", "weight": 1.0} -->

In this section, we provide the proofs of the main results, namely, Theorems 4.2. ‣ 4 Theoretical Results ‣ On the Global Convergence of Actor-Critic: A Case for Linear Quadratic Regulator with Ergodic Cost") and 4.3. ‣ 4 Theoretical Results ‣ On the Global Convergence of Actor-Critic: A Case for Linear Quadratic Regulator with Ergodic Cost"), which are proved in §5.1 and §5.2, respectively. The proofs of the supporting results are deferred to the appendix.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For linear quadratic regulator with ergodic cost, we propose an online natural actor-critic algorithm with GTD policy evaluation updates. The proposed algorithm is shown to find the optimal policy with linear rate of convergence. Our results provide nonasymptotic theoretical justifications for actor-critic methods with function approximation, which have received tremendous empirical success recently. A future direction is to extend our analysis to linear-quadratic-Gaussian control problems, which seems to be the simplistic model of partially observable Markov decision process. Another future direction is to develop model-free reinforcement learning methods for linear-quadratic dynamic games, a classical example of multi-agent reinforcement learning.
