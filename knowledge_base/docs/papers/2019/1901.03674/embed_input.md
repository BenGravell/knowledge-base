<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Global Convergence of Imitation Learning: A Case for Linear Quadratic Regulator

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the global convergence of generative adversarial imitation learning for linear quadratic regulators, which is posed as minimax optimization. To address the challenges arising from non-convex-concave geometry, we analyze the alternating gradient algorithm and establish its Q-linear rate of convergence to a unique saddle point, which simultaneously recovers the globally optimal policy and reward function. We hope our results may serve as a small step towards understanding and taming the instability in imitation learning as well as in more general non-convex-concave alternating minimax optimization that arises from reinforcement learning and generative adversarial learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning is a paradigm that learns from expert demonstration to perform a task. The most straightforward approach of imitation learning is behavioral cloning, which learns from expert trajectories to predict the expert action at any state. Despite its simplicity, behavioral cloning ignores the accumulation of prediction error over time. Consequently, although the learned policy closely resembles the expert policy at a given point in time, their trajectories may diverge in the long term.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To remedy the issue of error accumulation, inverse reinforcement learning jointly learns a reward function and the corresponding optimal policy, such that the expected cumulative reward of the learned policy closely resembles that of the expert policy. In particular, as a unifying framework of inverse reinforcement learning, generative adversarial imitation learning (GAIL) casts most existing approaches as iterative methods that alternate between (i) minimizing the discrepancy in expected cumulative reward between the expert policy and the policy of interest and (ii) maximizing such a discrepancy over the reward function of interest. Such a minimax optimization formulation of inverse reinforcement learning mirrors the training of generative adversarial networks (GAN), which alternates between updating the generator and discriminator, respectively.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its prevalence, inverse reinforcement learning, especially GAIL, is notoriously unstable in practice. More specifically, most inverse reinforcement learning approaches involve (partially) solving a reinforcement learning problem in an inner loop, which is often unstable, especially when the intermediate reward function obtained from the outer loop is ill-behaved. This is particularly the case for GAIL, which, for the sake of computational efficiency, alternates between policy optimization and reward function optimization without fully solving each of them. Moreover, such instability is exacerbated when the policy and reward function are both parameterized by deep neural networks. In this regard, the training of GAIL is generally more unstable than that of GAN, since policy optimization in deep reinforcement learning is often more challenging than training a standalone deep neural network.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take a first step towards theoretically understanding and algorithmically taming the instability in imitation learning. In particular, under a minimax optimization framework, we for the first time establish the global convergence of GAIL under a fundamental setting known as linear quadratic regulators (LQR). Such a setting of LQR is studied in a line of recent works as a lens for theoretically understanding more general settings in reinforcement learning. See Recht for a thorough review. In imitation learning, particularly GAIL, the setting of LQR captures four critical challenges of more general settings: the minimax optimization formulation, the lack of convex-concave geometry, the alternating update of policy and reward function, and the instability of the dynamical system induced by the intermediate policy and reward function (which differs from the aforementioned algorithmic instability).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under such a fundamental setting, we establish a global sublinear rate of convergence towards a saddle point of the minimax optimization problem, which is guaranteed to be unique and recovers the globally optimal policy and reward function. Moreover, we establish a local linear rate of convergence, which, combined with the global sublinear rate of convergence, implies a global Q-linear rate of convergence. A byproduct of our theory is the stability of all the dynamical systems induced by the intermediate policies and reward functions along the solution path, which addresses the key challenge in (iv) and plays a vital role in our analysis. At the core of our analysis is a new potential function tailored towards non-convex-concave minimax optimization with alternating update, which is of independent interest. To ensure the decay of potential function, we rely on the aforementioned stability of intermediate dynamical systems along the solution path. To achieve such stability, we unveil an intriguing "self-enforcing" stabilizing mechanism, that is, with a proper configuration of stepsizes, the solution path approaches the critical threshold that separates stable and unstable regimes at a slower rate as it gets closer to such a threshold.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In other words, such a threshold forms an implicit barrier, which ensures the stability of the intermediate dynamical systems along the solution path without any explicit regularization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work extends the recent line of works on reinforcement learning under the setting of LQR to imitation learning. In particular, our analysis relies on several geometric lemmas established in Fazel et al., which are listed in §F for completeness. However, unlike policy optimization in reinforcement learning, which involves solving a minimization problem where the objective function itself serves as a good potential function, imitation learning involves solving a minimax optimization problem, which requires incorporating the gradient into the potential function. In particular, the stability argument developed in Fazel et al., which is based on the monotonicity of objective functions along the solution path, is no longer applicable, as minimax optimization alternatively decreases and increases the objective function at each iteration.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a broader context, our work takes a first step towards extending the recent line of works on nonconvex optimization, e.g., Baldi and Hornik; Du and Lee; Wang et al.; Zhao et al.; Ge et al.; Anandkumar et al.; Bandeira et al.; Li et al.; Hajinezhad et al.; Bhojanapalli et al.; Sun et al., to non-convex-concave minimax optimization with alternating update, which is prevalent in reinforcement learning, imitation learning, and generative adversarial learning, and poses significantly more challenges.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the rest of this paper, §2 introduces imitation learning, the setting of LQR, and the generative adversarial learning framework. In §3, we introduce the minimax optimization formulation and the gradient algorithm. In §4 and §5, we present the theoretical results and sketch the proof. We defer the detailed proof to §A-§F of the appendix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

In reinforcement learning, we consider a Markov decision process $\{\mathcal{X},\mathcal{U},c,T,{\mathbb{D}}_{0}\}$, where an agent interacts with the environment in the following manner. At the $t$-th time step, the agent selects an action $u_{t} \in \mathcal{U}$ based on its current state $x_{t} \in \mathcal{X}$, and the environment responds with the cost $c_{t} = {c{(x_{t},u_{t})}}$ and the next state $x_{t + 1} \in \mathcal{X}$, which follows the transition dynamics $T$. Our goal is to find a policy $u_{t} = {\pi_{t}{(x_{t})}}$ that minimizes the expected cumulative cost.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

In the setting of LQR, we consider $\mathcal{X} = {\mathbb{R}}^{d}$ and $\mathcal{U} = {\mathbb{R}}^{k}$. The dynamics and cost function take the form where $A \in {\mathbb{R}}^{d \times d}$, $B \in {\mathbb{R}}^{d \times k}$, $Q \in {\mathbb{R}}^{d \times d}$, and $R \in {\mathbb{R}}^{k \times k}$ with ${Q,R} \succ 0$. The problem of minimizing the expected cumulative cost is then formulated as the optimization problem where ${\mathbb{D}}_{0}$ is a given initial distribution. Here we consider the infinite-horizon setting with a stochastic initial state $x_{0} \sim {\mathbb{D}}_{0}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

In this setting, the optimal policy $\pi_{t}$ is known to be static and takes the form of linear feedback ${\pi_{t}{(x_{t})}} = {- {Kx_{t}}}$, where $K \in {\mathbb{R}}^{k \times d}$ does not depend on $t$. Throughout the rest of this paper, we also refer to $K$ as policy and drop the subscript $t$ in $\pi_{t}$. To ensure the expected cumulative cost is finite, we require the spectral radius of $({A - {BK}})$ to be less than one, which ensures that the dynamical system is stable. For a given policy $K$, we denote by $C{(K;Q,R)}$ the expected cumulative cost in (2.1). For notational simplicity, we define By (2.3), we have the following equivalent form of $C{(K;Q,R)}$ where $\langle \cdot, \cdot \rangle$ denotes the matrix inner product.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Quadratic Regulator", "weight": 1.0} -->

Also, throughout the rest of this paper, we assume that the initial distribution ${\mathbb{D}}_{0}$ satisfies ${\sigma_{\text{min}}{(\Sigma_{0})}} > 0$. See Recht for a thorough review of reinforcement learning in the setting of LQR.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

In imitation learning, we parameterize the cost function of interest by $c{(x_{t},u_{t};\theta)}$, where $\theta$ denotes the unknown cost parameter. In the setting of LQR, we have $\theta = {(Q,R)}$. We observe expert trajectories in the form of ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$, which are induced by the expert policy $\pi_{\text{E}}$. As a unifying framework of inverse reinforcement learning, GAIL casts max-entropy inverse reinforcement learning and its extensions as the following minimax optimization problem where for ease of presentation, we restrict to deterministic policies in the form of $u_{t} = {\pi{(x_{t})}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

Here $H{(\pi)}$ denotes the causal entropy of the dynamical system ${\{ x_{t}\}}_{t = 0}^{\infty}$ induced by $\pi$, which takes value zero in our setting of LQR, since the transition dynamics in (2.2) is deterministic conditioning on $x_{t}$. Meanwhile, $\psi{(\theta)}$ is a regularizer on the cost parameter.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

The minimax optimization formulation in (2.2) mirrors the training of GAN, which seeks to find a generator of distribution that recovers a target distribution. In the training of GAN, the generator and discriminator are trained simultaneously, in the manner that the discriminator maximizes the discrepancy between the generated and target distributions, while the generator minimizes such a discrepancy. Analogously, in imitation learning, the policy $\pi$ of interest acts as the generator of trajectories, while the expert trajectories act as the target distribution. Meanwhile, the cost parameter $\theta$ of interest acts as the discriminator, which differentiates between the trajectories generated by $\pi$ and $\pi_{\text{E}}$. Intuitively, maximizing over the cost parameter $\theta$ amounts to assigning high costs to the state-action pairs visited more by $\pi$ than $\pi_{\text{E}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

Minimizing over $\pi$ aims at making such an adversarial assignment of cost impossible, which amounts to making the visitation distributions of $\pi$ and $\pi_{\text{E}}$ indistinguishable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In the sequel, we first introduce the minimax formulation of generative adversarial imitation learning in §3.1, then we present the gradient algorithm in §3.2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimax Formulation", "weight": 1.0} -->

We consider the minimax optimization formulation of the imitation learning problem, Here we denote by $\theta = {(Q,R)}$ the cost parameter, where $Q \in {\mathbb{R}}^{d \times d}$ and $R \in {\mathbb{R}}^{k \times k}$ are both positive definite matrices, and $\Theta$ is the feasible set of cost parameters. We assume $\Theta$ is convex and there exist positive constants $\alpha_{Q}$, $\alpha_{R}$, $\beta_{Q}$, and $\beta_{R}$ such that for any ${(Q,R)} \in \Theta$, it holds that Also, $\mathcal{K}$ consists of all stabilizing policies, such that ${\rho{({A - {BK}})}} < 1$ for all $K \in \mathcal{K}$, where $\rho$ is the spectral radius defined as the largest complex norm of the eigenvalues of a matrix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimax Formulation", "weight": 1.0} -->

The expert policy is defined as $K_{\text{E}} = {\operatorname{argmin}_{K}{C{(K;\overset{\sim}{\theta})}}}$ for an unknown cost parameter $\overset{\sim}{\theta} \in \Theta$. However, note that $\overset{\sim}{\theta}$ is not necessarily the unique cost parameter such that $K_{\text{E}}$ is optimal. Hence, our goal is to find one of such cost parameters $\theta^{\ast}$ that $K_{\text{E}}$ is optimal. The term $\psi{(\cdot)}$ is the regularizer on the cost parameter, which is set to be $\gamma$-strongly convex and $\nu$-smooth.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimax Formulation", "weight": 1.0} -->

To understand the minimax optimization problem in (3.1), we first consider the simplest case with ${\psi{(\theta)}} \equiv 0$. A saddle point $(K^{\ast},\theta^{\ast})$ of the objective function in (3.1), defined by has the following desired properties. First, we have that the optimal policy $K^{\ast}$ recovers the expert policy $K_{\text{E}}$. By the optimality condition in (3.3), we have where the first inequality follows from the optimality of $\theta^{\ast}$ and the second inequality follows from the optimality of $K^{\ast}$. Since the optimal solution to the policy optimization problem ${\min_{K}C}{(K;\overset{\sim}{\theta})}$ is unique (as proved in §5), we obtain from (3.4) that $K^{\ast} = K_{\text{E}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Minimax Formulation", "weight": 1.0} -->

Although ${\psi{( \cdot )}} \equiv 0$ brings us desired properties of the saddle point, there are several reasons we can not simply discard this regularizer. The first reason is that a strongly convex regularizer improves the geometry of the problem and makes the saddle point of (3.1) unique, which eliminates the ambiguity in learning the desired cost parameter. Second, the regularizer draws connection to the existing optimization formulations of GAN. For example, as shown in Ho and Ermon, with a specific choice of $\psi{( \cdot )}$, (3.1) reduces to the classical optimization formulation of GAN, which minimizes the Jensen-Shannon divergence bewteen the generator and target distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Gradient Algorithm", "weight": 1.0} -->

To solve the minimax optimization problem in (3.1), we consider the alternating gradient updating scheme, Here $\Pi_{\Theta}{\lbrack \cdot \rbrack}$ is the projection operator onto the convex set $\Theta$, which ensures that each iterate $\theta_{i}$ stays within $\Theta$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Gradient Algorithm", "weight": 1.0} -->

There are several ways to obatin the gradient in (3.5) without knowing the dynamics $X_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$ but based on the trajectory ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$. One example is the deterministic policy gradient algorithm. In specific, the gradient of the cost function is obtained through the limit where $\pi_{K,\sigma}{(\left. u \middle| x \right.)}$ is a stochastic policy that takes the form $\left. u \middle| x \right. \sim {\mathcal{N}{({- {Kx}},{\sigma^{2}I})}}$. Here $Q^{\pi_{K,\sigma}}{(x,u)}$ is the action-value function associated with the policy $\pi_{K,\sigma}{(\left.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Gradient Algorithm", "weight": 1.0} -->

u \middle| x \right.)}$, defined as the expected total cost of the policy $\pi_{K,\sigma}{(\left. u \middle| x \right.)}$ starting at state $x$ and action $u$, which can be estimated based on the trajectory ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$. An alternative approach is the evolutionary strategy, which uses zeroth-order information to approximate ${\nabla_{K}C}{(K;\theta)}$ with a random perturbation, where $\varepsilon \in {\mathbb{R}}^{k \times d}$ is a random matrix in ${\mathbb{R}}^{k \times d}$ with a sufficiently small variance $\sigma^{2}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we present the convergence analysis of the gradient algorithm in (3.5) and (3.6). We first prove that the solution path ${\{ K_{i}\}}_{i \geq 0}$ are guaranteed to be stabilizing and then establish the global convergence. For notational simplicity, we define the following constants, where $\alpha_{Q}$ and $\alpha_{R}$ are defined in (3.2), and $\Sigma_{0} = {{\mathbb{E}}{\lbrack{x_{0}x_{0}^{\top}}\rbrack}}$. Also, we define which play a key role in upper bounding the cost function $C{(K;\theta)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stability Guarantee", "weight": 1.0} -->

A minimum requirement in reinforcement learning is to obtain a stabilizing policy such that the dynamical system does not tend to infinity. Throughout this paper, we employ a notion of uniform stability, which states that there exists a constant $S$ such that ${\|\Sigma_{K_{i}}\|} \leq S$ for all $i$. Moreover, the uniform stability also allows us to establish the smoothness of $m{(K,\theta)}$, which is discussed in §5.2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Stability Guarantee", "weight": 1.0} -->

Recall that we assume $Q$ and $R$ are positive definite. Therefore, the uniform stability is implied by the boundedness of the cost function $C{(K_{i};\theta_{i})}$, since we have where the second inequality follows from the properties of trace and the assumption $Q \succeq {\alpha_{Q}I}$ in (3.2). However, it remains difficult to show that the cost function $C{(K_{i};\theta_{i})}$ is upper bounded. Although the update of policy in (3.5) decreases the cost function $C{(K_{i};\theta_{i})}$, the update of cost parameter increases $m{(K_{i};\theta_{i})}$, which possibly increases the cost function $C{(K_{i};\theta_{i})}$. To this end, we choose suitable stepsizes as in the next condition to ensure the boundedness of the cost function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Condition 4.1", "weight": 1.0} -->

For the update of policy and cost parameter in (3.5) and (3.6), let Here $\alpha$, $\mu$, $F$, and $M$ are defined in (4.1), (4.2), and (4.3). The constants $\kappa_{1}$ and $\kappa_{2}$ are defined as The next lemma shows that the solution path ${\{ K_{i}\}}_{i \geq 0}$ is uniformly stabilizing, and meanwhile, along the solution path, the cost function $C{(K_{i};\theta_{i})}$ and ${\| K_{i}\|}^{2}$ are both upper bounded.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Before showing the gradient algorithm converges to the saddle point $(K^{\ast},\theta^{\ast})$ of (3.1), we establish its uniqueness. We define the proximal gradient of the objective function $m{(K,\theta)}$ in (3.1) as Then a proximal stationary point is defined by ${L{(K,\theta)}} = 0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Condition 4.5", "weight": 1.0} -->

The following condition, together with Condition 4.1, specifies the required stepsizes to establish the global convergence of the gradient algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Condition 4.6", "weight": 1.0} -->

For the stepsizes $\eta$ and $\lambda$ in (3.5) and (3.6), let In the following, we establish the global convergence of the gradient algorithm. Recall that as defined in (4.6), $L{(K,\theta)}$ is the proximal gradient of the objective function $m{(K,\theta)}$ defined in (3.1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Q-Linear Convergence", "weight": 1.0} -->

In this section, we establish the Q-linear convergence of the gradient algorithm in (3.5) and (3.6). Recall that the optimal policy takes the form $K^{\ast} = {{({{B^{\top}PB} + R})}^{- 1}B^{\top}PA}$, where $P$ is the positive definite solution to the discrete-time algebraic Riccati equation, We denote by $P^{\ast}{(Q,R)}$ the corresponding implicit matrix-valued function defined by (4.15). Also, we define $Y \in {\mathbb{R}}^{d^{2} \times d^{2}}$ as for ${i,j,k,\ell} \in {\lbrack d\rbrack}$. We assume the following regularity condition on $f$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Condition 4.8", "weight": 1.0} -->

The unique stationary point of cost parameter $(Q^{\ast},R^{\ast})$ is an interior point of $\Theta$. Also, we assume that ${\det{(Y)}} \neq 0$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Condition 4.8", "weight": 1.0} -->

We define $K^{\ast}{(\theta)}$ as the unique optimal policy corresponding to the cost parameter $\theta$ and denote by $m^{\ast}{(\theta)}$ the corresponding value of the objective function $m{(K,\theta)}$ defined in (3.1), that is, The following two lemmas characterize the local properties of the functions $K^{\ast}{(\theta)}$ and $m^{\ast}{(\theta)}$ in a neighborhood of the saddle point $(K^{\ast},\theta^{\ast})$ of $m{(K,\theta)}$.
