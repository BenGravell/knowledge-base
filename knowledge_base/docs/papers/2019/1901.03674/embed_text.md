<!-- arxiv-full-text:v1 {"arxiv_id": "1901.03674", "source": "ar5iv"} -->

## Introduction

Imitation learning is a paradigm that learns from expert demonstration to perform a task. The most straightforward approach of imitation learning is behavioral cloning, which learns from expert trajectories to predict the expert action at any state. Despite its simplicity, behavioral cloning ignores the accumulation of prediction error over time. Consequently, although the learned policy closely resembles the expert policy at a given point in time, their trajectories may diverge in the long term.

To remedy the issue of error accumulation, inverse reinforcement learning jointly learns a reward function and the corresponding optimal policy, such that the expected cumulative reward of the learned policy closely resembles that of the expert policy. In particular, as a unifying framework of inverse reinforcement learning, generative adversarial imitation learning (GAIL) casts most existing approaches as iterative methods that alternate between (i) minimizing the discrepancy in expected cumulative reward between the expert policy and the policy of interest and (ii) maximizing such a discrepancy over the reward function of interest. Such a minimax optimization formulation of inverse reinforcement learning mirrors the training of generative adversarial networks (GAN), which alternates between updating the generator and discriminator, respectively.

Despite its prevalence, inverse reinforcement learning, especially GAIL, is notoriously unstable in practice. More specifically, most inverse reinforcement learning approaches involve (partially) solving a reinforcement learning problem in an inner loop, which is often unstable, especially when the intermediate reward function obtained from the outer loop is ill-behaved. This is particularly the case for GAIL, which, for the sake of computational efficiency, alternates between policy optimization and reward function optimization without fully solving each of them. Moreover, such instability is exacerbated when the policy and reward function are both parameterized by deep neural networks. In this regard, the training of GAIL is generally more unstable than that of GAN, since policy optimization in deep reinforcement learning is often more challenging than training a standalone deep neural network.

In this paper, we take a first step towards theoretically understanding and algorithmically taming the instability in imitation learning. In particular, under a minimax optimization framework, we for the first time establish the global convergence of GAIL under a fundamental setting known as linear quadratic regulators (LQR). Such a setting of LQR is studied in a line of recent works as a lens for theoretically understanding more general settings in reinforcement learning. See Recht for a thorough review. In imitation learning, particularly GAIL, the setting of LQR captures four critical challenges of more general settings: the minimax optimization formulation, the lack of convex-concave geometry, the alternating update of policy and reward function, and the instability of the dynamical system induced by the intermediate policy and reward function (which differs from the aforementioned algorithmic instability).

Under such a fundamental setting, we establish a global sublinear rate of convergence towards a saddle point of the minimax optimization problem, which is guaranteed to be unique and recovers the globally optimal policy and reward function. Moreover, we establish a local linear rate of convergence, which, combined with the global sublinear rate of convergence, implies a global Q-linear rate of convergence. A byproduct of our theory is the stability of all the dynamical systems induced by the intermediate policies and reward functions along the solution path, which addresses the key challenge in (iv) and plays a vital role in our analysis. At the core of our analysis is a new potential function tailored towards non-convex-concave minimax optimization with alternating update, which is of independent interest. To ensure the decay of potential function, we rely on the aforementioned stability of intermediate dynamical systems along the solution path. To achieve such stability, we unveil an intriguing "self-enforcing" stabilizing mechanism, that is, with a proper configuration of stepsizes, the solution path approaches the critical threshold that separates stable and unstable regimes at a slower rate as it gets closer to such a threshold. In other words, such a threshold forms an implicit barrier, which ensures the stability of the intermediate dynamical systems along the solution path without any explicit regularization.

Our work extends the recent line of works on reinforcement learning under the setting of LQR to imitation learning. In particular, our analysis relies on several geometric lemmas established in Fazel et al., which are listed in §F for completeness. However, unlike policy optimization in reinforcement learning, which involves solving a minimization problem where the objective function itself serves as a good potential function, imitation learning involves solving a minimax optimization problem, which requires incorporating the gradient into the potential function. In particular, the stability argument developed in Fazel et al., which is based on the monotonicity of objective functions along the solution path, is no longer applicable, as minimax optimization alternatively decreases and increases the objective function at each iteration. In a broader context, our work takes a first step towards extending the recent line of works on nonconvex optimization, e.g., Baldi and Hornik; Du and Lee; Wang et al.; Zhao et al.; Ge et al.; Anandkumar et al.; Bandeira et al.; Li et al.; Hajinezhad et al.; Bhojanapalli et al.; Sun et al., to non-convex-concave minimax optimization with alternating update, which is prevalent in reinforcement learning, imitation learning, and generative adversarial learning, and poses significantly more challenges.

In the rest of this paper, §2 introduces imitation learning, the setting of LQR, and the generative adversarial learning framework. In §3, we introduce the minimax optimization formulation and the gradient algorithm. In §4 and §5, we present the theoretical results and sketch the proof. We defer the detailed proof to §A-§F of the appendix.

Notation. We denote by $\parallel \cdot \parallel$ the spectral norm and $\parallel \cdot \parallel_{\text{F}}$ the Frobenius norm of a matrix. For vectors, we denote by $\parallel \cdot \parallel_{2}$ the Euclidean norm. In this paper, we write parameters in the matrix form, and correspondingly, all the Lipschitz conditions are defined in the Frobenius norm.

## Background

In the following, we briefly introduce the setting of LQR in §2.1 and imitation learning in §2.2. To unify the notation of LQR and more general reinforcement learning, we stick to the notion of cost function instead of reward function throughout the rest of this paper.

### Linear Quadratic Regulator

In reinforcement learning, we consider a Markov decision process $\{\mathcal{X},\mathcal{U},c,T,{\mathbb{D}}_{0}\}$, where an agent interacts with the environment in the following manner. At the $t$-th time step, the agent selects an action $u_{t} \in \mathcal{U}$ based on its current state $x_{t} \in \mathcal{X}$, and the environment responds with the cost $c_{t} = {c{(x_{t},u_{t})}}$ and the next state $x_{t + 1} \in \mathcal{X}$, which follows the transition dynamics $T$. Our goal is to find a policy $u_{t} = {\pi_{t}{(x_{t})}}$ that minimizes the expected cumulative cost. In the setting of LQR, we consider $\mathcal{X} = {\mathbb{R}}^{d}$ and $\mathcal{U} = {\mathbb{R}}^{k}$. The dynamics and cost function take the form where $A \in {\mathbb{R}}^{d \times d}$, $B \in {\mathbb{R}}^{d \times k}$, $Q \in {\mathbb{R}}^{d \times d}$, and $R \in {\mathbb{R}}^{k \times k}$ with ${Q,R} \succ 0$. The problem of minimizing the expected cumulative cost is then formulated as the optimization problem where ${\mathbb{D}}_{0}$ is a given initial distribution. Here we consider the infinite-horizon setting with a stochastic initial state $x_{0} \sim {\mathbb{D}}_{0}$. In this setting, the optimal policy $\pi_{t}$ is known to be static and takes the form of linear feedback ${\pi_{t}{(x_{t})}} = {- {Kx_{t}}}$, where $K \in {\mathbb{R}}^{k \times d}$ does not depend on $t$. Throughout the rest of this paper, we also refer to $K$ as policy and drop the subscript $t$ in $\pi_{t}$. To ensure the expected cumulative cost is finite, we require the spectral radius of $({A - {BK}})$ to be less than one, which ensures that the dynamical system is stable. For a given policy $K$, we denote by $C{(K;Q,R)}$ the expected cumulative cost in (2.1). For notational simplicity, we define By (2.3), we have the following equivalent form of $C{(K;Q,R)}$ where $\langle \cdot, \cdot \rangle$ denotes the matrix inner product. Also, throughout the rest of this paper, we assume that the initial distribution ${\mathbb{D}}_{0}$ satisfies ${\sigma_{\text{min}}{(\Sigma_{0})}} > 0$. See Recht for a thorough review of reinforcement learning in the setting of LQR.

### Imitation Learning

In imitation learning, we parameterize the cost function of interest by $c{(x_{t},u_{t};\theta)}$, where $\theta$ denotes the unknown cost parameter. In the setting of LQR, we have $\theta = {(Q,R)}$. We observe expert trajectories in the form of ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$, which are induced by the expert policy $\pi_{\text{E}}$. As a unifying framework of inverse reinforcement learning, GAIL casts max-entropy inverse reinforcement learning and its extensions as the following minimax optimization problem where for ease of presentation, we restrict to deterministic policies in the form of $u_{t} = {\pi{(x_{t})}}$. Here $H{(\pi)}$ denotes the causal entropy of the dynamical system ${\{ x_{t}\}}_{t = 0}^{\infty}$ induced by $\pi$, which takes value zero in our setting of LQR, since the transition dynamics in (2.2) is deterministic conditioning on $x_{t}$. Meanwhile, $\psi{(\theta)}$ is a regularizer on the cost parameter.

The minimax optimization formulation in (2.2) mirrors the training of GAN, which seeks to find a generator of distribution that recovers a target distribution. In the training of GAN, the generator and discriminator are trained simultaneously, in the manner that the discriminator maximizes the discrepancy between the generated and target distributions, while the generator minimizes such a discrepancy. Analogously, in imitation learning, the policy $\pi$ of interest acts as the generator of trajectories, while the expert trajectories act as the target distribution. Meanwhile, the cost parameter $\theta$ of interest acts as the discriminator, which differentiates between the trajectories generated by $\pi$ and $\pi_{\text{E}}$. Intuitively, maximizing over the cost parameter $\theta$ amounts to assigning high costs to the state-action pairs visited more by $\pi$ than $\pi_{\text{E}}$. Minimizing over $\pi$ aims at making such an adversarial assignment of cost impossible, which amounts to making the visitation distributions of $\pi$ and $\pi_{\text{E}}$ indistinguishable.

## Algorithm

In the sequel, we first introduce the minimax formulation of generative adversarial imitation learning in §3.1, then we present the gradient algorithm in §3.2.

### Minimax Formulation

We consider the minimax optimization formulation of the imitation learning problem, Here we denote by $\theta = {(Q,R)}$ the cost parameter, where $Q \in {\mathbb{R}}^{d \times d}$ and $R \in {\mathbb{R}}^{k \times k}$ are both positive definite matrices, and $\Theta$ is the feasible set of cost parameters. We assume $\Theta$ is convex and there exist positive constants $\alpha_{Q}$, $\alpha_{R}$, $\beta_{Q}$, and $\beta_{R}$ such that for any ${(Q,R)} \in \Theta$, it holds that Also, $\mathcal{K}$ consists of all stabilizing policies, such that ${\rho{({A - {BK}})}} < 1$ for all $K \in \mathcal{K}$, where $\rho$ is the spectral radius defined as the largest complex norm of the eigenvalues of a matrix. The expert policy is defined as $K_{\text{E}} = {\operatorname{argmin}_{K}{C{(K;\overset{\sim}{\theta})}}}$ for an unknown cost parameter $\overset{\sim}{\theta} \in \Theta$. However, note that $\overset{\sim}{\theta}$ is not necessarily the unique cost parameter such that $K_{\text{E}}$ is optimal. Hence, our goal is to find one of such cost parameters $\theta^{\ast}$ that $K_{\text{E}}$ is optimal. The term $\psi{(\cdot)}$ is the regularizer on the cost parameter, which is set to be $\gamma$-strongly convex and $\nu$-smooth.

To understand the minimax optimization problem in (3.1), we first consider the simplest case with ${\psi{(\theta)}} \equiv 0$. A saddle point $(K^{\ast},\theta^{\ast})$ of the objective function in (3.1), defined by has the following desired properties. First, we have that the optimal policy $K^{\ast}$ recovers the expert policy $K_{\text{E}}$. By the optimality condition in (3.3), we have where the first inequality follows from the optimality of $\theta^{\ast}$ and the second inequality follows from the optimality of $K^{\ast}$. Since the optimal solution to the policy optimization problem ${\min_{K}C}{(K;\overset{\sim}{\theta})}$ is unique (as proved in §5), we obtain from (3.4) that $K^{\ast} = K_{\text{E}}$. Second, $K_{\text{E}}$ is an optimal policy with respect to the cost parameter $\theta^{\ast}$, since by $K^{\ast} = K_{\text{E}}$ and the optimality condition $K^{\ast} = {\operatorname{argmin}_{K}{C{(K;\theta^{\ast})}}}$, we have $K_{\text{E}} = {\operatorname{argmin}_{K}{C{(K;\theta^{\ast})}}}$. In this sense, the saddle point $(K^{\ast};\theta^{\ast})$ of (3.1) recovers a desired cost parameter and the corresponding optimal policy.

Although ${\psi{( \cdot )}} \equiv 0$ brings us desired properties of the saddle point, there are several reasons we can not simply discard this regularizer. The first reason is that a strongly convex regularizer improves the geometry of the problem and makes the saddle point of (3.1) unique, which eliminates the ambiguity in learning the desired cost parameter. Second, the regularizer draws connection to the existing optimization formulations of GAN. For example, as shown in Ho and Ermon, with a specific choice of $\psi{( \cdot )}$, (3.1) reduces to the classical optimization formulation of GAN, which minimizes the Jensen-Shannon divergence bewteen the generator and target distributions.

### Gradient Algorithm

To solve the minimax optimization problem in (3.1), we consider the alternating gradient updating scheme, Here $\Pi_{\Theta}{\lbrack \cdot \rbrack}$ is the projection operator onto the convex set $\Theta$, which ensures that each iterate $\theta_{i}$ stays within $\Theta$.

There are several ways to obatin the gradient in (3.5) without knowing the dynamics $X_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$ but based on the trajectory ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$. One example is the deterministic policy gradient algorithm. In specific, the gradient of the cost function is obtained through the limit where $\pi_{K,\sigma}{(\left. u \middle| x \right.)}$ is a stochastic policy that takes the form $\left. u \middle| x \right. \sim {\mathcal{N}{({- {Kx}},{\sigma^{2}I})}}$. Here $Q^{\pi_{K,\sigma}}{(x,u)}$ is the action-value function associated with the policy $\pi_{K,\sigma}{(\left. u \middle| x \right.)}$, defined as the expected total cost of the policy $\pi_{K,\sigma}{(\left. u \middle| x \right.)}$ starting at state $x$ and action $u$, which can be estimated based on the trajectory ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$. An alternative approach is the evolutionary strategy, which uses zeroth-order information to approximate ${\nabla_{K}C}{(K;\theta)}$ with a random perturbation, where $\varepsilon \in {\mathbb{R}}^{k \times d}$ is a random matrix in ${\mathbb{R}}^{k \times d}$ with a sufficiently small variance $\sigma^{2}$.

To obtain the gradient in (3.6), we have Here $\Sigma_{K} = {{\mathbb{E}}{\lbrack{\sum_{t = 0}^{\infty}{x_{t}x_{t}^{\top}}}\rbrack}}$ with ${\{ x_{t}\}}_{t = 0}^{\infty}$ generated by policy $K$, which can be estimated based on the trajectory ${\{{(x_{t},u_{t},c_{t})}\}}_{t = 0}^{\infty}$.

## Main Results

In this section, we present the convergence analysis of the gradient algorithm in (3.5) and (3.6). We first prove that the solution path ${\{ K_{i}\}}_{i \geq 0}$ are guaranteed to be stabilizing and then establish the global convergence. For notational simplicity, we define the following constants, where $\alpha_{Q}$ and $\alpha_{R}$ are defined in (3.2), and $\Sigma_{0} = {{\mathbb{E}}{\lbrack{x_{0}x_{0}^{\top}}\rbrack}}$. Also, we define which play a key role in upper bounding the cost function $C{(K;\theta)}$.

### Stability Guarantee

A minimum requirement in reinforcement learning is to obtain a stabilizing policy such that the dynamical system does not tend to infinity. Throughout this paper, we employ a notion of uniform stability, which states that there exists a constant $S$ such that ${\|\Sigma_{K_{i}}\|} \leq S$ for all $i$. Moreover, the uniform stability also allows us to establish the smoothness of $m{(K,\theta)}$, which is discussed in §5.2.

Recall that we assume $Q$ and $R$ are positive definite. Therefore, the uniform stability is implied by the boundedness of the cost function $C{(K_{i};\theta_{i})}$, since we have where the second inequality follows from the properties of trace and the assumption $Q \succeq {\alpha_{Q}I}$ in (3.2). However, it remains difficult to show that the cost function $C{(K_{i};\theta_{i})}$ is upper bounded. Although the update of policy in (3.5) decreases the cost function $C{(K_{i};\theta_{i})}$, the update of cost parameter increases $m{(K_{i};\theta_{i})}$, which possibly increases the cost function $C{(K_{i};\theta_{i})}$. To this end, we choose suitable stepsizes as in the next condition to ensure the boundedness of the cost function.

### Condition 4.1

For the update of policy and cost parameter in (3.5) and (3.6), let Here $\alpha$, $\mu$, $F$, and $M$ are defined in (4.1), (4.2), and (4.3). The constants $\kappa_{1}$ and $\kappa_{2}$ are defined as The next lemma shows that the solution path ${\{ K_{i}\}}_{i \geq 0}$ is uniformly stabilizing, and meanwhile, along the solution path, the cost function $C{(K_{i};\theta_{i})}$ and ${\| K_{i}\|}^{2}$ are both upper bounded.

### Lemma 4.2

Under Condition 4.1, we have for all $i \geq 0$.

### Proof

See §A for a detailed proof. ∎

### Global Convergence

Before showing the gradient algorithm converges to the saddle point $(K^{\ast},\theta^{\ast})$ of (3.1), we establish its uniqueness. We define the proximal gradient of the objective function $m{(K,\theta)}$ in (3.1) as Then a proximal stationary point is defined by ${L{(K,\theta)}} = 0$.

### Lemma 4.3 (Uniqueness of Saddle Point)

There exists a unique proximal stationary point, denoted as $(K^{\ast},\theta^{\ast})$, of the objective function $m{(K,\theta)}$ in (3.1), which is also its unique saddle point.

### Proof

See §D.1 for a detailed proof. ∎ To analyze the convergence of the gradient algorithm, we first need to establish the Lipschitz continuity and smoothness of $m{(K,\theta)}$. However, the cost function $C{(K;\theta)}$ becomes steep as the policy $K$ is close to unstabilizing. Therefore, we do not have such desired Lipschitz continuity and smoothness of $\Sigma_{K}$ and $K\Sigma_{K}K^{\top}$ with respect to $K$. However, given $\|\Sigma_{K}\|$ is upper bounded as in Lemma 4.2, we obtain such desired properties in the following lemma.

For notational simplicity, we slightly abuse the notation and rewrite $\theta$ as a block diagonal matrix and correspondingly define $V{(K)}$, Then the objective function takes the form

### Lemma 4.4

We assume that the initial policy $K_{0}$ of the gradient algorithm is stabilizing. Under Condition 4.1, there exists a compact set $\mathcal{K}^{\dagger} \subsetneqq \mathcal{K}$ such that $K_{i} \in \mathcal{K}^{\dagger}$ for all $i \geq 0$. Also, there exist constants $\tau_{V}$ and $\nu_{V}$ such that the matrix-valued function $V{(K)}$ defined in (4.7) is $\tau_{V}$-Lipschitz continuous and $\nu_{V}$-smooth over $\mathcal{K}^{\dagger}$. That is, for any ${K_{1},K_{2}} \in \mathcal{K}^{\dagger}$ and ${j,\ell} \in {\lbrack{d + k}\rbrack}$, we have

### Proof

See §5.2 for a detailed proof. ∎ Note that the cost parameter $(Q,R)$ is only identifiable up to a multiplicative constant. Recall that we assume ${\alpha_{Q}I} \preceq Q \preceq {\beta_{Q}I}$ and ${\alpha_{R}I} \preceq R \preceq {\beta_{R}I}$. In the sequel, we establish the sublinear rate of convergence with a proper choice of $\alpha_{Q}$, $\alpha_{R}$, $\beta_{Q}$, and $\beta_{R}$, which is characterized by the following condition.

### Condition 4.5

We assume that $\alpha_{Q}$, $\alpha_{R}$, $\beta_{Q}$, and $\beta_{R}$ satisfy where $F$, $M$, and $\sigma_{\theta}$ are defined in (4.1), (4.2) and (4.3), and $\nu_{V}$ is defined in Lemma 4.4.

The following condition, together with Condition 4.1, specifies the required stepsizes to establish the global convergence of the gradient algorithm.

### Condition 4.6

For the stepsizes $\eta$ and $\lambda$ in (3.5) and (3.6), let In the following, we establish the global convergence of the gradient algorithm. Recall that as defined in (4.6), $L{(K,\theta)}$ is the proximal gradient of the objective function $m{(K,\theta)}$ defined in (3.1).

### Theorem 4.7

Under Conditions 4.1, 4.5, and 4.6, we have ${\lim_{i\rightarrow\infty}{\|{L{(K_{i},\theta_{i})}}\|}_{\text{F}}} = 0$, which implies that ${\{{(K_{i},\theta_{i})}\}}_{i = 0}^{\infty}$ converges to the unique saddle point $(K^{\ast},\theta^{\ast})$ of $m{(K,\theta)}$. To characterize the rate of convergence, we define $\Gamma{(\varepsilon)}$ as the smallest iteration index that ${\|{L{(K_{i},\theta_{i})}}\|}_{\text{F}}^{2}$ is below an error $\varepsilon > 0$, Then there exists a constant $\zeta$, which depends on $K_{0}$, $\theta_{0}$, $\eta$, and $\lambda$ (as specified in (5.6)), such that ${\Gamma{(\varepsilon)}} \leq {\zeta/\varepsilon}$ for any $\varepsilon$.

### Proof

See §5.2 for a detailed proof. ∎ To understand Condition 4.5, we consider a simple case where the regularizer $\psi{(\cdot)}$ is the squared penalty centered at some point ${(\overline{Q},\overline{R})} \in \Theta$, that is, Then we have ${\|{{\nabla\psi}{(Q,R)}}\|}_{\text{F}} \leq {2\gamma\omega}$, where $\omega = {\sup_{{\theta,\theta'} \in \Theta}{\|{\theta - \theta'}\|}_{\text{F}}}$. Also, by (4.3) we have Let ${{\max{\{\beta_{Q},\beta_{R}\}}}/\alpha} \leq \iota$ for some constant $\iota$. By (4.2) we have By (4.12) and Lemma 4.2, we obatin for all $i \geq 0$. In §5.2 we further prove that $\nu_{V}$ is determined by the uniform upper bound of $\|\Sigma_{K_{i}}\|$ and $\| K_{i}\|$ along the solution path, which is established in Lemma 4.2. Hence, by (4.13) and (4.14) we have that $\nu_{V}$ is independent of $\alpha$. Meanwhile, by (4.11) and (4.12) we have Thus, for a sufficiently large $\alpha$, we have which leads to Condition 4.5.

Condition 4.5 plays a key role in establishing the convergence. On the one hand, to ensure the boundedness of the cost function $C{(K_{i};\theta_{i})}$, we require an upper bound of $\lambda/\eta$ in Condition 4.1. On the other hand, to ensure the convergence of the gradient algorithm, we require an upper bound of $\eta/\lambda$ in Condtion 4.6. Condition 4.5 ensures such two requirements on stepsizes are compatible.

### Q-Linear Convergence

In this section, we establish the Q-linear convergence of the gradient algorithm in (3.5) and (3.6). Recall that the optimal policy takes the form $K^{\ast} = {{({{B^{\top}PB} + R})}^{- 1}B^{\top}PA}$, where $P$ is the positive definite solution to the discrete-time algebraic Riccati equation, We denote by $P^{\ast}{(Q,R)}$ the corresponding implicit matrix-valued function defined by (4.15). Also, we define $Y \in {\mathbb{R}}^{d^{2} \times d^{2}}$ as for ${i,j,k,\ell} \in {\lbrack d\rbrack}$. We assume the following regularity condition on $f$.

### Condition 4.8

The unique stationary point of cost parameter $(Q^{\ast},R^{\ast})$ is an interior point of $\Theta$. Also, we assume that ${\det{(Y)}} \neq 0$.

We define $K^{\ast}{(\theta)}$ as the unique optimal policy corresponding to the cost parameter $\theta$ and denote by $m^{\ast}{(\theta)}$ the corresponding value of the objective function $m{(K,\theta)}$ defined in (3.1), that is, The following two lemmas characterize the local properties of the functions $K^{\ast}{(\theta)}$ and $m^{\ast}{(\theta)}$ in a neighborhood of the saddle point $(K^{\ast},\theta^{\ast})$ of $m{(K,\theta)}$.

### Lemma 4.9

Under Condition 4.8, there exist constants $\tau_{K^{\ast}}$ and $\nu_{K^{\ast}}$, and a neighborhood $\mathcal{B}_{K}$ of $\theta^{\ast}$, such that $K^{\ast}{(\theta)}$ is $\tau_{K^{\ast}}$-Lipschitz continuous and $\nu_{K^{\ast}}$-smooth with respect to $\theta \in \mathcal{B}_{K}$.

### Proof

See §D.4 for a detailed proof. ∎

### Lemma 4.10

Under Condition 4.8, there exist a constant $\nu_{m^{\ast}}$ and a neighborhood $\mathcal{B}_{m^{\ast}}$ of $\theta^{\ast}$ such that $m^{\ast}{(\theta)}$ is $\gamma$-strongly concave and $\nu_{m^{\ast}}$-smooth with respect to $\theta \in \mathcal{B}_{m^{\ast}}$.

### Proof

See §D.5 for a detailed proof. ∎ To establish the Q-linear convergence, we need an additional condition, which upper bounds the stepsizes $\eta$ and $\lambda$.

### Condition 4.11

For the stepsizes $\eta$ and $\lambda$ in (3.5) and (3.6), let We define the following potential function where $a = {\gamma/{({3\tau_{K^{\ast}}\nu_{m^{\ast}}})}}$. Note that ${\lim_{i\rightarrow\infty}Z_{i}} = 0$ implies that ${\{{(K_{i},\theta_{i})}\}}_{i = 0}^{\infty}$ converges to $(K^{\ast},\theta^{\ast})$, since we have ${K^{\ast}{(\theta^{\ast})}} = K^{\ast}$. Also, we define The following theorem establishes the Q-linear convergence of the gradient algorithm.

### Theorem 4.12

Under Conditions 4.1, 4.5, 4.6, 4.8, and 4.11, we have $\upsilon \in {}$ in (4.18). There exists an iteration index $N > 0$ such that $Z_{i + 1} \leq {\upsilon \cdot Z_{i}}$ for all $i > N$.

### Proof

See §5.3 for a detailed proof. ∎

## Proof Sketch

In this section, we sketch the proof of the main results in §4.

### Proof of Stability Guarantee

To prove Lemma 4.2, we lay out two auxiliary lemmas that characterize the geometry of the cost function $C{(K;\theta)}$ with respect to $K$. The first lemma characterizes the stationary point of policy optimization. The second lemma shows that $C{(K;\theta)}$ is gradient dominated with respect to $K$.

### Lemma 5.1

If ${{\nabla_{K}C}{(K;\theta)}} = 0$, then $K$ is the unique optimal policy corresponding to the cost parameter $\theta$.

### Proof

See §D.2 for a detailed proof. ∎

### Lemma 5.2 (Corollary 5 in Fazel et al. )

The cost function $C{(K;\theta)}$ is gradient dominated with respect to $K$, that is, where $\mu_{C} = {{\|\Sigma_{K^{\ast}{(\theta)}}\|}/{({\mu^{2}\sigma_{\min}{(R)}})}}$ and $K^{\ast}{(\theta)}$ is defined in (4.16).

### Proof

See Fazel et al. for a detailed proof. ∎ Lemma 5.2). ‣ 5.1 Proof of Stability Guarantee ‣ 5 Proof Sketch ‣ On the Global Convergence of Imitation Learning: A Case for Linear Quadratic Regulator") allows us to upper bound the increment of the cost function at each iteration in (3.5) and (3.6) by choosing a sufficiently small $\lambda$ relative to $\eta$. In fact, we construct a threshold such that when $C{(K_{i};\theta_{i})}$ is close to such a threshold, an upper bound of the increment ${C{(K_{i + 1};\theta_{i + 1})}} - {C{(K_{i};\theta_{i})}}$ goes to zero. Thus, $C{(K_{i};\theta_{i})}$ is upper bounded by such a threshold. See §A for a detailed proof.

### Proof of Global Convergence

To prove Theorem 4.7, we first establish the Lipschitz continuity and smoothness of $m{(K,\theta)}$ in $K$ within a restricted domain $K^{\dagger}$ as in Lemma 4.4. Recall that $V{(K)}$ is defined in (4.7) and $m{(K,\theta)}$ takes the form in (4.8). Since the matrix-valued function $\Sigma_{K}$ plays a key role in $V{(K)}$, in the sequel we characterize the smoothness of $\Sigma_{K}$ with respect to $K$ within a restricted set.

### Lemma 5.3

For any constant $S > 0$, there exist constants $\tau_{\Sigma}$ and $\nu_{\Sigma}$ depending on $S$ such that for any ${K,K'} \in \left. \{{K \in {\mathbb{R}}^{k \times d}} \middle| {{\|\Sigma_{K}\|} \leq S}\} \right.$ and ${j,\ell} \in {\lbrack d\rbrack}$.

### Proof

See §D.3 for a detailed proof. ∎ Based on Lemmas 5.3 and 4.2, we now prove Lemma 4.4.

### Proof

Let the set $K^{\dagger}$ in Lemma 4.4 be Then by Lemma 4.2, we have for all $i \geq 0$, which implies $K_{i} \in \mathcal{K}^{\dagger}$ for all $i \geq 0$. By Lemma 5.3, we obtain the Lipschitz continuity and smoothness of $\Sigma_{K}$ over $\mathcal{K}^{\dagger}$. Furthermore, by the definition of $V{(K)}$ in (4.7) and the boundedness of $K_{i}$ established in Lemma 4.2, $V{(K)}$ is also Lipschitz continuous and smooth over $\mathcal{K}^{\dagger}$. Thus, we conclude the proof of Lemma 4.4. ∎ Based on Lemma 4.4, we prove the global convergence in Theorem 4.7. To this end, we construct a potential function that decays monotonically along the solution path, which takes the form for some constant $s > 0$, which is specified in the next lemma. Meanwhile, we define three constants $\phi_{1}$, $\phi_{2}$, and $\phi_{3}$ as The following lemma characterizes the decrement of the potential function defined in (5.1) at each iteration.

### Lemma 5.4

Under Conditions 4.1, 4.5, and 4.6, we have Moreover, we have ${\phi_{1},\phi_{2},\phi_{3}} > 0$ for $s = {12/{({13\eta^{2}\nu_{V}\sigma_{\theta}})}}$.

### Proof

See §B for a detailed proof. ∎ Based on Lemma 5.4, we now prove Theorem 4.7.

### Proof

By the definitions of $P_{i}$ and $m{(K,\theta)}$ in (5.1) and (3.1), we have $P_{i} \geq \underset{¯}{P}$ for all $i \geq 0$, where $\underset{¯}{P}$ is Here we use the fact ${C{(K;\theta)}} \geq 0$ for any $K \in \mathcal{K}$ and $\theta \in \Theta$. Let $\phi = {1/{\min{\{\phi_{1},\phi_{2}\}}}}$, where $\phi_{1}$ and $\phi_{2}$ are defined in (5.2) and (5.3). By rearranging the terms in (5.5), we obtain where $\phi' = {\max{\{ 1,{1/\eta^{2}},{1/\lambda^{2}}\}}}$, which implies that ${\{{\|{L{(K_{i},\theta_{i})}}\|}_{\text{F}}\}}_{i = 0}^{\infty}$ converges to zero. Also, let For any $\varepsilon > 0$, by the definition of $\Gamma{(\varepsilon)}$ in (4.10), we have which implies ${\Gamma{(\varepsilon)}} \leq {\zeta/\varepsilon}$. Hence, we conclude the proof of Lemma 4.7. ∎

### Proof of Q-Linear Convergence

Theorem 4.7 states that ${\{{(K_{i},\theta_{i})}\}}_{i = 0}^{\infty}$ converges to the unique saddle point $(K^{\ast},\theta^{\ast})$ starting from any stabilizing initial policy$(K_{0},\theta_{0})$. To establish the Q-linear rate of convergence in Theorem 4.12, we first prove that the cost function $C{(K;\theta)}$ is locally strongly convex over a neighborhood of the optimal policy $K^{\ast}{(\theta)}$ in the following lemma. Recall that $K^{\ast}{(\theta)}$ is defined in (4.16).

### Lemma 5.5

For any cost parameter $\theta \in \Theta$, its corresponding optimal policy $K^{\ast}{(\theta)}$ has a neighborhood $\mathcal{K}_{\theta}^{\ast}$ such that $C{(K;\theta)}$ is $({\alpha_{R}\mu})$-strongly convex with respect to $K \in \mathcal{K}_{\theta}^{\ast}$.

### Proof

See §D.6 for a detailed proof. ∎ With Lemmas 4.9, 4.10, and 5.5, we establish Theorem 4.12 based on the local strongly convex-concave property of $m{(K,\theta)}$ defined in (3.1). See §C for a detailed proof.
