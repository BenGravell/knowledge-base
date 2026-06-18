## INTRODUCTION

Recent advancements in meta-learning, a machine learning paradigm addressing the learning-to-learn challenge \[(https://arxiv.org/html/2503.00385v1#bib.bib22)\], have shown remarkable success across diverse domains, including robotics \[(https://arxiv.org/html/2503.00385v1#bib.bib51), (https://arxiv.org/html/2503.00385v1#bib.bib25)\], image processing \[(https://arxiv.org/html/2503.00385v1#bib.bib35), (https://arxiv.org/html/2503.00385v1#bib.bib26)\], and cybersecurity \[(https://arxiv.org/html/2503.00385v1#bib.bib18)\]. One epitome of the various meta-learning approaches is Model-Agnostic Meta-Learning (MAML) \[(https://arxiv.org/html/2503.00385v1#bib.bib15)\]. Compared with other deep-learning-based meta-learning approaches \[(https://arxiv.org/html/2503.00385v1#bib.bib23)\], MAML formulates meta-learning as a stochastic compositional optimization problem \[(https://arxiv.org/html/2503.00385v1#bib.bib47), (https://arxiv.org/html/2503.00385v1#bib.bib10)\], aiming to learn an initialization that enables rapid adaptation to new tasks with just a few gradient updates computed using online samples.

Since MAML is model-agnostic (compatible with any model trained with gradient descent), it is a widely applicable framework. In supervised learning (e.g., image recognition, speech processing), where labeled data is scarce, MAML facilitates few-shot learning \[(https://arxiv.org/html/2503.00385v1#bib.bib42)\], enabling models to learn new tasks with minimal examples. In reinforcement learning (RL) (e.g., robotic control, game playing), MAML allows agents to generalize across multiple environments, leading to faster adaptation in dynamic and partially observable settings \[(https://arxiv.org/html/2503.00385v1#bib.bib25), (https://arxiv.org/html/2503.00385v1#bib.bib18)\]. Additionally, as a gradient-based optimization method, MAML benefits from its mathematical clarity, making it well-suited for theoretical analysis and highly flexible for further enhancements.

In the RL domain, MAML samples a batch of dynamic systems from an agnostic environment, i.e., a distribution of tasks, then optimizes the policy initialization with regard to the anticipated post-policy-gradient-adaptation performance, averaging over these tasks. The policy initialization will then be fine-tuned at test time. The complete MAML policy gradient methods for such a meta-objective require differentiating through the optimization process, which necessitates the estimation of Hessians or even higher order information, making them computationally expensive and unstable, especially when a large number of gradient updates are needed at test time \[(https://arxiv.org/html/2503.00385v1#bib.bib13), (https://arxiv.org/html/2503.00385v1#bib.bib33), (https://arxiv.org/html/2503.00385v1#bib.bib26)\]. This incentivizes us to focus our attention on the first-order implementation of MAML, unlike reptile \[(https://arxiv.org/html/2503.00385v1#bib.bib33)\], which simply neglects the computation of Hessians or higher order information when estimating the gradient for meta-objective, we develop a framework that still approximates the exact gradient of the meta-objective, with controllable bias that benefits from the smoothness of the cost functional. This methodology stems from the zeroth-order methods, more specifically, Stein's Gaussian smoothing \[(https://arxiv.org/html/2503.00385v1#bib.bib44)\] technique.

We choose the Linear Quadratic Regulator (LQR) problem as a testbed for our analysis, as it is a fundamental component of optimal control theory. The Riccati equation, derived from the Hamilton-Jacobi equation \[(https://arxiv.org/html/2503.00385v1#bib.bib7)\], provides the linear optimal control gain for LQR problems. While LQR problems are analytically solvable, they can still benefit from reinforcement learning (RL) and meta-RL, particularly in scenarios where model information is incomplete---a setting known as model-free control (see \[(https://arxiv.org/html/2503.00385v1#bib.bib1), (https://arxiv.org/html/2503.00385v1#bib.bib2), (https://arxiv.org/html/2503.00385v1#bib.bib11)\] for related works). Our focus is on the policy optimization of LQRs, specifically in refining an initial optimal control policy for a set of similar Linear Time-Invariant (LTI) systems, which share the same control and state space but differ in system dynamics and cost functionals. A practical example of such a scenario is a robotic arm performing a repetitive task, such as picking up and placing multiple block objects in a specific order. Each time the robot places a block, the system dynamics shift, requiring rapid adaptation to maintain optimal performance.

Our contribution is twofold. First, we develop a zeroth-order meta-gradient estimation framework, presented in Algorithm (https://arxiv.org/html/2503.00385v1#alg2 "Algorithm 2 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"). This Hessian-free approach eliminates the instability and high computational cost associated with exact meta-gradient estimation. Second, we establish theoretical guarantees for our proposed algorithms. Specifically, we prove a stability result ([Theorem 1](https://arxiv.org/html/2503.00385v1#Thmtheorem1 "Theorem 1. ‣ 5.2 Theoretical Guarantee ‣ 5 GRADIENT DESCENT ANALYSIS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")), ensuring that each iteration of Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") produces a stable control policy initialization across a wide range of tasks. Additionally, we provide a convergence guarantee ([Theorem 2](https://arxiv.org/html/2503.00385v1#Thmtheorem2 "Theorem 2. ‣ 5.2 Theoretical Guarantee ‣ 5 GRADIENT DESCENT ANALYSIS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")), which ensures that the algorithm successfully finds a local minimum for the meta-objective. Our method is built on simultaneous perturbation stochastic approximation \[(https://arxiv.org/html/2503.00385v1#bib.bib43), (https://arxiv.org/html/2503.00385v1#bib.bib17)\] with a close inspection of factors influencing the zero-th order gradient estimation error, including the perturbation magnitude, roll-out length of sample trajectories, batch size of trajectories, and interdependency of estimation errors arising in inner gradient adaptation and outer meta-gradient update. We believe the developed technique in controlling the estimation error and associated high-probability error bounds would benefit the future work on biased meta-learning (in contrast to debiased meta-learning \[(https://arxiv.org/html/2503.00385v1#bib.bib13)\]), which trades estimation bias for lesser computation complexity. Even though this work studies LQRs, our zero-th order policy optimization method easily lends itself to generic Makrov systems (e.g., \[(https://arxiv.org/html/2503.00385v1#bib.bib26)\]) for efficient meta-learning algorithm design.

## RELATED WORK

### Policy Optimization (PO)

Policy optimization (PO) methods date back to the 1970s with the model-based approach known as differential dynamic programming \[(https://arxiv.org/html/2503.00385v1#bib.bib19)\], which requires complete knowledge of system models. In model-free settings, where system matrices are unknown, various estimation techniques have emerged. Among these, finite-difference methods approximate the gradient by directly perturbing the policy parameters, while REINFORCE-type methods \[(https://arxiv.org/html/2503.00385v1#bib.bib48)\] estimate the gradient of the expected return using the log-likelihood ratio trick. For LQR tasks, however, analyzing the state-control correlations in REINFORCE-type methods poses significant challenges \[(https://arxiv.org/html/2503.00385v1#bib.bib14), (https://arxiv.org/html/2503.00385v1#bib.bib21)\]. Therefore, we build our framework on finite-difference methods and develop a novel meta-gradient estimation procedure tailored specifically for the model-agnostic meta-learning problem. Overall, PO methods have been well established in the literature (see \[(https://arxiv.org/html/2503.00385v1#bib.bib14), (https://arxiv.org/html/2503.00385v1#bib.bib29), (https://arxiv.org/html/2503.00385v1#bib.bib20), (https://arxiv.org/html/2503.00385v1#bib.bib24)\]).

Zeroth-order methods have garnered increasing attention in policy optimization (PO), particularly in scenarios where explicit gradient computation is infeasible or computationally expensive. Rather than relying on REINFORCE-type methods for direct gradient evaluations, zeroth-order techniques estimate gradients using finite-difference methods or random search-based approaches. A foundational work in this domain is the Evolution Strategies (ES) method \[(https://arxiv.org/html/2503.00385v1#bib.bib41)\], which reformulates PO as a black-box optimization problem, obtaining stochastic gradient estimates through perturbed policy rollouts. Similarly, \[(https://arxiv.org/html/2503.00385v1#bib.bib5)\] introduces a method that leverages policy perturbation while efficiently utilizing past data, improving scalability. These approaches are particularly valuable in settings where Hessian-based computations or higher-order derivative information are impractical, driving the development of Hessian-free meta-policy optimization frameworks.

### Model-Agnostic Meta-Learning (MAML)

The concept of meta-learning, or learning to learn, involves leveraging past experiences to develop a control policy that can efficiently adapt to novel environments, agents, or dynamics. One of the most prominent approaches in this area is MAML (Model-Agnostic Meta-Learning) as proposed by \[(https://arxiv.org/html/2503.00385v1#bib.bib15), (https://arxiv.org/html/2503.00385v1#bib.bib16)\]. MAML is an optimization-based method that addresses task diversity by learning a "common policy initialization" from a diverse task environment. Due to its success across various domains in recent years, numerous efforts have been made to analyze its theoretical convergence properties. For instance, the model-agnostic meta-RL framework has been studied in the context of finite-horizon Markov decision processes by \[(https://arxiv.org/html/2503.00385v1#bib.bib12), (https://arxiv.org/html/2503.00385v1#bib.bib13), (https://arxiv.org/html/2503.00385v1#bib.bib28), (https://arxiv.org/html/2503.00385v1#bib.bib8)\]. However, these results do not directly transfer to the policy optimization (PO) setting for LQR, because key characteristics of the LQR cost objective---such as gradient dominance and local smoothness---do not straightforwardly extend to the meta-objective.

For example, \[(https://arxiv.org/html/2503.00385v1#bib.bib31)\] demonstrates that the global convergence of MAML over LQR tasks depends on a global property assumption ensuring that the meta-objective has a benign landscape. Similarly, \[(https://arxiv.org/html/2503.00385v1#bib.bib32)\] establishes convergence under the condition that all LQR tasks share the same system dynamics. It was not until \[(https://arxiv.org/html/2503.00385v1#bib.bib45)\] that comprehensive theoretical guarantees began to emerge: their analysis provided personalization guarantees for MAML in LQR settings by explicitly accounting for heterogeneity across different LQR tasks. The result readily passes the sanity check; the performance of the meta-policy initialization is affected by the diversity of the tasks.

All the aforementioned MAML approaches involve estimating second-order information, which can be problematic in LQR settings where the Hessians become high-dimensional tensors. Although recent studies such as \[(https://arxiv.org/html/2503.00385v1#bib.bib45), (https://arxiv.org/html/2503.00385v1#bib.bib6)\] have employed advanced estimation schemes to mitigate these challenges, issues related to computational burden and numerical stability persist. Motivated by Reptile \[(https://arxiv.org/html/2503.00385v1#bib.bib33)\], a first-order meta-learning method, we adopt a double-layered zero-th order meta-gradient estimation scheme that skips the Hessian tensor estimation. Our work extends the original work in \[(https://arxiv.org/html/2503.00385v1#bib.bib39)\] by providing a comprehensive analysis of the induced first-order method, thereby offering a more computationally efficient and stable alternative for meta-learning in LQR tasks.

## PROBLEM FORMULATION

### Preliminary: Policy Optimization for LQRs

Let $\mathcal{T} = {\{{(A_{i},B_{i},Q_{i},R_{i})}\}}_{i \in {\lbrack I\rbrack}}$ be the finite set of LQR tasks, where ${\lbrack I\rbrack}:={\{ 1,\ldots,I\}}$ is the task index set, ${A_{i} \in \mathbb{R}^{d \times d}},{B_{i} \in \mathbb{R}^{d \times k}}$ are system dynamics matrices of the same dimensions, ${Q_{i} \in \mathbb{R}^{d \times d}},{R_{i} \in \mathbb{R}^{k \times k}}$, and ${Q_{i},R_{i}} \succeq 0$ are the associated cost matrices. We assume a prior probability distribution $p \in {\Delta{(\mathcal{T})}}$ which we can sample the LQR tasks from. For each LQR task $i$, the system is assumed to share the same state space $\mathbb{R}^{d}$ and control space $\mathbb{R}^{k}$, and is governed by the stochastic linear dynamics associated with some quadratic cost functions:

where $x_{t} \in \mathbb{R}^{d}$, $u_{t} \in \mathbb{R}^{k}$, $w_{t}$ are some random i.i.d. zero-mean noise with and covariance matrix $\Psi$, which is symmetric and positive definite.

For each system $i$, our objective is to minimize the average infinite horizon cost,

where $\rho_{0}$ is the initial state distribution $\mathcal{N}{(0,\Sigma_{0})}$ with $\Sigma_{0} \geq {\mu I}$ for some $\mu \geq 0$. For task $\mathcal{T}_{i}$, the optimal control ${\{ u_{t}^{i \ast}\}}_{t \geq 0}$ can be expressed as $u_{t}^{i \ast} = {- {K_{i}^{\ast}x_{t}}}$, where $K_{i}^{\ast} \in \mathbb{R}^{k \times d}$ satisfies $K_{i}^{\ast} = {\left( {R_{i} + {B_{i}^{\top}P_{i}^{\ast}B_{i}}} \right)^{- 1}B_{i}^{\top}P_{i}^{\ast}A_{i}}$, and $P_{\ast}^{i}$ is the unique solution to the following discrete algebraic Riccati equation $P_{\ast}^{i} = {Q_{i} + {A_{i}^{\top}P_{i}^{\ast}A_{i}} + {A_{i}^{\top}P_{\ast}^{i}B_{i}\left( {R_{i} + {B_{i}^{\top}P_{\ast}^{i}B_{i}}} \right)^{- 1}B_{i}^{\top}P_{\ast}^{i}A_{i}}}$.

A policy $K \in \mathbb{R}^{d \times k}$ is called stable for system $i$ if and only if ${\rho{({A_{i} - {B_{i}K}})}} < 1$, where $\rho{( \cdot )}$ stands for the spectrum radius of a matrix. Denoted by $\mathcal{K}_{i}$ the set of stable policy for system $i$, let $\mathcal{K}:={\bigcap_{i \in {\lbrack I\rbrack}}\mathcal{K}_{i}}$. For a policy $K \in \mathcal{K}_{i}$, the induced cost over system $i$ is

where the limiting stationary distribution of $x_{t}$ is denoted by $\rho_{K}^{i}$, ${Tr}{( \cdot )}$ stands for the trace operator. The Gramian matrix $\Sigma_{K}^{i}:={{\mathbb{E}}_{x \sim \rho_{K}^{i}}{\lbrack{xx^{\top}}\rbrack}} = {\lim_{T\rightarrow\infty}{\mathbb{E}_{x_{0} \sim \rho_{0}}{\lbrack{\frac{1}{T}{\sum_{t = 0}^{T - 1}{x_{t}x_{t}^{\top}}}}\rbrack}}}$ satisfies the following Lyapunov equation

((https://arxiv.org/html/2503.00385v1#S3.E1 "Equation 1 ‣ 3.1 Preliminary: Policy Optimization for LQRs ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")) can be easily verified through elementary algebra.

### Proposition 1 (Policy Gradient for LQR \[[14](https://arxiv.org/html/2503.00385v1#bib.bib14), [49](https://arxiv.org/html/2503.00385v1#bib.bib49), [9](https://arxiv.org/html/2503.00385v1#bib.bib9)\])

For any task $\mathcal{T}_{i}$, the expression for average cost is ${J_{i}{(K)}} = {{Tr}{(P_{K}^{i})}}$, and the expression of ${\nabla J_{i}}{(K)}$ is

where $\Sigma_{K}^{i}$ satisfies ((https://arxiv.org/html/2503.00385v1#S3.E1 "Equation 1 ‣ 3.1 Preliminary: Policy Optimization for LQRs ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")), $E_{K}^{i}$ is defined to be

and $P_{K}^{i}$ is the unique positive definite solution to the Lyapunov equation.

The Hessian operator ${\nabla J_{i}}{(K)}$ acting on some $X \in \mathbb{R}^{k \times d}$ is given by,

where ${\overset{\sim}{P}}_{K}^{i}{\lbrack X\rbrack}$ is the solution to

It is, therefore, possible to employ the first- and second-order algorithms to find the optimal controller for each specific task, in the model-based setting where the gradient/Hessian expressions are computable, see, e.g., in \[(https://arxiv.org/html/2503.00385v1#bib.bib14)\] for the following three first-order methods:

Our discussion hitherto has focused on the deterministic policy gradient, where the policy is of linear form and depends on the policy gain $K$ deterministically. Yet, we remark that a common practice in numerical implementations is to add a Gaussian noise to the policy to encourage exploration, arriving at the linear-Gaussian policy class \[(https://arxiv.org/html/2503.00385v1#bib.bib50)\]:

Such a stochastic policy class often relies on properly crafted regularization for improved sample complexity and convergence rate \[(https://arxiv.org/html/2503.00385v1#bib.bib3)\]. For stochastic policies, entropy-based regularization receives a significant amount of attention due to its empirical success \[(https://arxiv.org/html/2503.00385v1#bib.bib4)\], of which softmax policy parametrization \[(https://arxiv.org/html/2503.00385v1#bib.bib30), (https://arxiv.org/html/2503.00385v1#bib.bib3)\] and entropy-based mirror descent \[(https://arxiv.org/html/2503.00385v1#bib.bib37), (https://arxiv.org/html/2503.00385v1#bib.bib36), (https://arxiv.org/html/2503.00385v1#bib.bib38)\] are well-received regularized policy gradient methods. We refer the reader to \[(https://arxiv.org/html/2503.00385v1#bib.bib27), Sec. 2\] for the connection between softmax and mirror descent methods. Finally, we remark that the policy gradient characterization in the stochastic case admits the same expression as in the deterministic counterpart. Hence, we limit our focus to the deterministic case to avoid additional discussion on the variance introduced by the stochastic policy.

### Meta-Policy-Optimization

In analogy to \[(https://arxiv.org/html/2503.00385v1#bib.bib15), (https://arxiv.org/html/2503.00385v1#bib.bib12)\], we consider meta-policy-optimization, which draws inspiration from Model-Agnostic-Meta-Learning (MAML) in the machine learning literature. Our objective is to find a meta-policy initialization, such that one step of (stochastic) policy gradient adaptation still attains optimized on-average performance for the tasks $\mathcal{T}$:

where $\overline{\mathcal{K}}$ is the admissible set. At first glance, one might define $\overline{\mathcal{K}}$ as simply the intersection of all $\mathcal{K}_{i}$, however, this approach may render the problem ill-posed, since the functions $J_{i}{( \cdot )}$ can be ill-defined if the one-step gradient adaptation overshoots. Thus, with a given adaptation rate $\eta$, we define $\overline{\mathcal{K}}$ as in [Definition 1](https://arxiv.org/html/2503.00385v1#Thmdefinition1 "Definition 1 (MAML-stablizing ). ‣ 3.2 Meta-Policy-Optimization ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective").

### Definition 1 (MAML-stablizing \[[32](https://arxiv.org/html/2503.00385v1#bib.bib32)\])

With a proper selection of adaptation rate $\eta$, a policy $K$ is MAML-stabilizing if for every task $i \in \mathcal{T}$, ${\rho{({A_{i} - {B_{i}K}})}} < 1$ and ${\rho{({A_{i} - {B{({K - {\eta{\nabla J_{i}}{(K)}}})}}})}} < 1$, we denote this set by $\overline{\mathcal{K}}$.

Definition (https://arxiv.org/html/2503.00385v1#Thmdefinition1 "Definition 1 (MAML-stablizing ). ‣ 3.2 Meta-Policy-Optimization ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") prepares us to adopt the first-order method to solve this problem, with learning iteration defined as follows:

In general, an arbitrary collection of LQRs is not necessarily meta-learnable using gradient-based optimization techniques, as one might not be able to find an admissible initialization of policy gain. For instance, consider a two-system scalar case where ${A_{1} = 3},{B_{1} = 4}$ and ${A_{2} = 1},{B_{2} = {- 1}}$. The policy evaluation requires an initialization $K$ to be stable for both system, which means $K \in {{(\frac{1}{2},1)} \cap {({- 2},0)}} = \varnothing$! This example illustrates that in regards to LQR cases, not all collections of LTIs are meta-learnable using MAML.

Therefore, it is reasonable to assume that the systems exhibit a degree of similarity such that the set of tasks remains MAML-learnable. This assumption not only necessitates that the joint stabilizing sets are nonempty, i.e., ${\bigcap_{i \in {\lbrack I\rbrack}}\mathcal{K}_{i}} \neq \varnothing$, but also requires the existence of a set of MAML-stabilizing policies, $\overline{\mathcal{K}} \neq \varnothing$. We formalize such requirements in the definition below.

### Definition 2 (Stabilizing sub-level set \[[45](https://arxiv.org/html/2503.00385v1#bib.bib45)\])

The task-specific and MAML stabilizing sub-level sets are defined as follows:

Given a task $\mathcal{T}_{i}$, the task-specific sub-level set $\mathcal{S}_{i} \subseteq \mathcal{K}_{i}$ is

where $K_{0}$ denotes an initial control gain for the first-order method and $\gamma_{i}$ being any positive constant.

The MAML stabilizing sub-level set $\mathcal{S} \subseteq \overline{\mathcal{K}}$ is defined as the intersection between each task-specific stabilizing sub-level set, i.e., $\mathcal{S}:={\cap_{i \in {\lbrack I\rbrack}}\mathcal{S}_{i}}$.

It is not hard to observe that, once $K \in \mathcal{S}$, it is possible to select a small adaptation rate $\eta$, such that $K^{\prime} \in \mathcal{S}$, in other words, $\eta$ controls whether $K \in \overline{\mathcal{K}}$. This property will be formalized later in section (https://arxiv.org/html/2503.00385v1#S5 "5 GRADIENT DESCENT ANALYSIS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"). For now, we simply assume that we have access to an admissible initial policy $K_{0} \in \mathcal{S}$. Readers can refer to \[(https://arxiv.org/html/2503.00385v1#bib.bib40)\] and \[(https://arxiv.org/html/2503.00385v1#bib.bib34)\] for details on how to find an initial stabilizing controller for the single LQR instance.

## METHODOLOGY

### Zero-th Order Methods

In the model-free setting where knowledge of system matrices is absent, sampling and approximation become necessary. In this case, one can sample roll-out trajectories, from the specific task $i$ to perform the policy evaluation from $K$, then, optimize the system performance index through policy iteration.

The zeroth-order methods are derivative-free optimization techniques that allow us to optimize an unknown smooth function ${J_{i}{( \cdot )}}:{\mathbb{R}^{k \times d}\rightarrow\mathbb{R}}$ by estimating the first-order information \[(https://arxiv.org/html/2503.00385v1#bib.bib17), (https://arxiv.org/html/2503.00385v1#bib.bib43)\]. What it requires is to query the function values $J_{i}$ at some input points. A generic procedure is to firstly sample some perturbations $U \sim {{Unif}{({\mathbb{S}}_{r})}}$, where ${\mathbb{S}}_{r}:=\left. \{{r \in {\mathbb{R}}^{k \times d}} \middle| {{\| r\|}_{F} = r}\} \right.$ is a $r$-radius $k \times d$-dimensional sphere, and estimate the gradient of the perturbed function through equation:

Based on Stein's identity \[(https://arxiv.org/html/2503.00385v1#bib.bib44)\] and Lemma 2.1 \[(https://arxiv.org/html/2503.00385v1#bib.bib17)\], ${{\mathbb{E}}{\lbrack{{\nabla J_{i}}{({K + U})}}\rbrack}} = {{\nabla_{r}J_{i}}{(K)}}$, hence we obtain a perturbed version of the first-order information. The expectation $\mathbb{E}_{U \sim {{Unif}{({\mathbb{S}}_{r})}}}$ can be evaluated through Monte-Carlo sampling. However, as we discussed, a function value oracle, i.e., the value of $J_{i}$ is not always accessible. One can substitute $J_{i}$ with the return estimates obtained from sample roll-outs, as demonstrated in Algorithm (https://arxiv.org/html/2503.00385v1#alg1 "Algorithm 1 ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"), (adapted from \[(https://arxiv.org/html/2503.00385v1#bib.bib14)\].) This type of gradient-estimation procedure samples trajectories with a perturbed policy $K + U$, instead of the target policy $K$.

Input: Task simulator i, Policy K, number of trajectories M,
roll out length ℓ, smoothing parameter r.
Sample a perturbed policy K + Um, where Um is drawn uniformly from 𝕊r;
Simulate K + Um for ℓ steps starting from x0 ∼ ρ0. Let Ĵi(ℓ)(K+Um) and ${\overset{\sim}{\Sigma}}_{K + U_{m}}^{i,{(\ell)}}$ be empirical estimates:

${\overset{\sim}{J}}_{i}^{(\ell)}{({K + U_{m}})}$

${\overset{\sim}{\Sigma}}_{K + U_{m}}^{i,{(\ell)}}$
${= {\frac{1}{\ell}{\sum\limits_{l = 1}^{\ell}{x_{l}x_{l}^{\top}}}}},$

where gt and xt are costs and states of the current trajectory m.
Return the (biased) estimates:

$${{\overset{\sim}{\nabla}J_{i}{(K)}} = {\frac{1}{M}{\sum\limits_{m = 1}^{M}{\frac{dk}{r^{2}}{\overset{\sim}{J}}_{i}^{(\ell)}{({K + U_{m}})}U_{m}}}}},$$

Algorithm 1 Gradient Estimation

Algorithm (https://arxiv.org/html/2503.00385v1#alg1 "Algorithm 1 ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") enables us to perform inexact gradient iterations such as $K^{\prime} = {K - {\eta\overset{\sim}{\nabla}J_{i}{(K)}}}$, where $\eta$ is the adaptation rate. However, there are two issues that persist. First, one has to restrict $r$ to be small so that the change on $K$ is not drastic, and the perturbed policy is admissible ${K + U} \in \mathcal{K}_{i}$. (We will provide theoretical guarantees later.) Second, the first-order optimization requires that the updated policy $K^{\prime}$ must be stable as well, even if the perturbed policy is stable, it is questionable how small the smoothing parameter $r$ and the adaptation rate $\eta$ should be to prevent the updated policy $K^{\prime}$ from escaping the admissible set. As has been demonstrated in \[(https://arxiv.org/html/2503.00385v1#bib.bib14)\], the remedy to this is that when the cost function is locally smooth, it suffices to identify the regime of such smoothness and constrain the gradient steps within such regime.

Even though a single LQR task objective becomes infinite as soon as $A_{i} - {B_{i}K}$ becomes unstable, as established in \[(https://arxiv.org/html/2503.00385v1#bib.bib14)\] as well as in non-convex optimization literature, the (local) smoothness and gradient domination properties almost immediately imply global convergence for the gradient descent dynamics, with a linear convergence rate. We now hash out three core auxiliary results that lead to such properties. These results can be found in \[(https://arxiv.org/html/2503.00385v1#bib.bib14), (https://arxiv.org/html/2503.00385v1#bib.bib46), (https://arxiv.org/html/2503.00385v1#bib.bib9), (https://arxiv.org/html/2503.00385v1#bib.bib32)\], we defer the explicit definition of the parameters to the appendix.

### Lemma 1 (Uniform bounds \[[45](https://arxiv.org/html/2503.00385v1#bib.bib45)\])

Given a LQR task $\mathcal{T}_{i}$ and an stabilizing controller $K \in \mathcal{S}$, the Frobenius norm of gradient ${\nabla J_{i}}{(K)}$, Hessian ${\nabla^{2}J_{i}}{(K)}$ and control gain $K$ can be bounded as follows:

where ${h_{G},h_{H}},$ and $h_{c}$ are problem dependent parameters.

### Lemma 2 (Perturbation Analysis \[[45](https://arxiv.org/html/2503.00385v1#bib.bib45), [32](https://arxiv.org/html/2503.00385v1#bib.bib32)\])

Let ${K,K^{\prime}} \in \mathcal{S}$ such that ${\|\Delta\|}:={\|{K^{\prime} - K}\|} \leq {h_{\Delta}{(K)}} < \infty$, then, we have the following set of local smoothness properties:

for all tasks $i \in {\lbrack I\rbrack}$, where ${h_{\text{cost}}{(K)}},{h_{\text{grad}}{(K)}},{h_{\text{hess}}{(K)}}$ are problem-dependent parameters.

### Lemma 3 (Gradient Domination \[[14](https://arxiv.org/html/2503.00385v1#bib.bib14), [50](https://arxiv.org/html/2503.00385v1#bib.bib50)\])

For any LQR task $i \in {\lbrack I\rbrack}$, let $K_{i}^{\ast}$ be the optimal policy. Suppose $K \in \mathcal{S}$ has finite cost. Then, it holds that

### Hessian-Free Meta-Gradient Estimation

Now we recall ((https://arxiv.org/html/2503.00385v1#S4.E5 "Equation 5 ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")) and extend the zeroth-order technique to the meta-learning problem. Specifically, for problem ((https://arxiv.org/html/2503.00385v1#S3.E4 "Equation 4 ‣ 3.2 Meta-Policy-Optimization ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")), we derive a gradient expression for the perturbed objective function $\mathcal{L}$, thereby eliminating the need to compute the Hessian.

To evaluate expectation $\mathbb{E}_{{U \sim {\mathbb{S}}_{r}},{i \sim p}}$ we sample $M$ independent perturbation $U_{m}$ and a batch of tasks $\mathcal{T}_{n}$, then average the samples. To evaluate return $J_{i}{({{K + U} - {\eta{\nabla J_{i}}{({K + U})}}})}$ we first apply algorithm (https://arxiv.org/html/2503.00385v1#alg1 "Algorithm 1 ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") to obtain approximate gradient $\overset{\sim}{\nabla}J_{i}{({K + U})}$ for a single perturbed policy, then sample roll-out trajectories using the one-step updated policy ${K + U} - {\eta\overset{\sim}{\nabla}J_{i}{({K + U})}}$ to estimate its associated return.

A comprehensive description of the procedure is shown in Algorithm (https://arxiv.org/html/2503.00385v1#alg2 "Algorithm 2 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"). Essentially we aim to collect $M$ samples for return by perturbed policy $K_{m}^{i}$, which requires the original perturbed policy ${\hat{K}}_{m}$ and the gradient estimate of it. To do so, we use Algorithm (https://arxiv.org/html/2503.00385v1#alg1 "Algorithm 1 ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") as an inner loop procedure. After computing $K_{m}^{i}$ we simulate it for $\ell$ steps to get the empirical estimate of return $J_{i}{({{K + U_{m}} - {\eta{\nabla J_{i}}{({K + U_{m}})}}})}$. The entire procedure of meta-policy-optimization is shown in Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective").

Input: Meta-environment p, policy K, number of perturbations M, learning rate η, roll-out length ℓ, parameter r;
Randomly draw systems batch 𝒯n from meta-environment p;
Sample a policy K̂m = K + Um, where Um is drawn uniformly from 𝕊r;
Estimate ${\overset{\sim}{\nabla}J_{i}{({\hat{K}}_{m})}}\leftarrow{\text{Gradient Estimation}{(i,{\hat{K}}_{m},M,\ell,r)}}$;
Perform one-step gradient adaptation:

$${K_{m}^{i} = {{\hat{K}}_{m} - {\eta\overset{\sim}{\nabla}J_{i}{({\hat{K}}_{m})}}}};$$

Estimate ${\overset{\sim}{J}}_{i}^{(\ell)}{(K_{m}^{i})}$ from simulating Kmi for ℓ steps starting with x0 ∼ ρ0:

The meta-gradient estimation:

$${\overset{\sim}{\nabla}\mathcal{L}{(K)}} = {\frac{1}{|\mathcal{T}_{n}|}{\sum\limits_{i \in \mathcal{T}_{n}}{\frac{1}{M}{\sum\limits_{m = 1}^{M}{\frac{dk}{r^{2}}{\overset{\sim}{J}}_{i}^{(\ell)}{(K_{m}^{i})}U_{m}}}}}}$$

Algorithm 2 Meta-Gradient Estimation

Further, we can easily extend the results in [Lemma 1](https://arxiv.org/html/2503.00385v1#Thmlemma1 "Lemma 1 (Uniform bounds ). ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"), [Lemma 2](https://arxiv.org/html/2503.00385v1#Thmlemma2 "Lemma 2 (Perturbation Analysis ). ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") to the meta-objective, to show the boundedness and Lipschitz properties of ${\mathcal{L}{(K)}},{{\nabla\mathcal{L}}{(K)}}$, as in [Lemma 4](https://arxiv.org/html/2503.00385v1#Thmlemma4 "Lemma 4. ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") and [Lemma 5](https://arxiv.org/html/2503.00385v1#Thmlemma5 "Lemma 5 (Perturbation analysis of ∇ℒ⁢(𝐾)). ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"), whose proofs--which we defer to the Appendix [A](https://arxiv.org/html/2503.00385v1#A1 "Appendix A Auxiliary Results ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")--are straightforward given the previous characterizations. These results provide an initial sanity check for the first-order iterative algorithm.

### Lemma 4

Given a prior $p$ over LQR task set $\mathcal{T}$, adaptation rate $\eta$, and an MAML stabilizing controller $K \in \mathcal{S}$, the Frobenius norm of gradient ${\nabla\mathcal{L}}{(K)}$ and control gain $K$ can be bounded as follows:

where $h_{G,\mathcal{L}}:={{({k + {\eta h_{H}{(K)}}})}{({1 + {\eta h_{grad}{(K)}}})}h_{G}{(K)}}$ is dependent on the problem parameters.

### Lemma 5 (Perturbation analysis of ${\nabla\mathcal{L}}{(K)}$)

Let ${K,K^{\prime}} \in \mathcal{S}$ such that ${\|\Delta\|}:={\|{K^{\prime} - K}\|} \leq {h_{\Delta}{(K)}} < \infty$, then, we have the following set of local smoothness properties,

where $h_{\mathcal{L},{cost}}:={h_{cost}{({1 + {\eta h_{grad}{(K)}}})}}$ and $h_{\mathcal{L},{grad}}:={{\eta h_{hess}{(K)}{({1 + {\eta h_{grad}}})}h_{G}{(K)}} + {{({k + {\eta h_{H}{(K^{\prime})}}})}h_{hess}{(K)}{({1 + {\eta h_{hess}{(K)}}})}}}$ are problem dependent parameters.

Input: Task prior p, number of perturbations M, adaptation rate η,
learning rate α, roll-out length ℓ, parameter r, tolerance ε;
initialize feasible policy K0 ∈ 𝒮;
while $\parallel \overset{\sim}{\nabla}\mathcal{L}{(K)} \leq \varepsilon \parallel$ do
${\overset{\sim}{\nabla}\mathcal{L}{(K)}}\leftarrow$ Meta-Gradient Estimation(p,Kn,M,η,ℓ,r);

$${K_{n + 1} = {K_{n} - {\alpha\overset{\sim}{\nabla}\mathcal{L}{(K_{n})}}}}.$$

Algorithm 3 Model-Agnostic Meta-Policy-Optimization

## GRADIENT DESCENT ANALYSIS

Our theoretical analysis for Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") can be divided into two primary objectives: stability and convergence. For stability, we demonstrate that by selecting appropriate algorithm parameters, every iteration $n$ of gradient descent satisfies $K_{n} \in \overline{\mathcal{K}}$, ensuring that both $K_{n + 1}$ and $K_{n}$ remain in $\mathcal{S}$; Regarding convergence, we establish that the learned meta-policy initialization eventually approximates the optimal policies for each specific task, and we provide a quantitative measure of this closeness.

### Controlling Estimation Error

In the following, we present our results that characterize the conditions on the step-sizes $\eta,\alpha$ and zeroth-order estimation parameters $M$, $\ell$, $r$, and task batch size $|\mathcal{T}_{n}|$, for controlling gradient and meta-gradient estimation errors. The proofs are deferred to the appendix. Overall, our observations are as follows:

The smoothing radius is dictated by the smoothness of the LQR cost and its gradient, as well as the size of the locally smooth set.

The roll-out length is determined by the smoothness of the cost function and the level of system noise.

The number of sample trajectories and sample tasks is influenced by a broader set of parameters that govern the magnitudes and variances of the gradient estimates.

Inner loop estimation errors can propagate readily, particularly when the scale of the sample tasks is large.

### Lemma 6 (Gradient Estimation)

For sufficiently small numbers ${\epsilon,\delta} \in {}$, given a control policy $K$, let $\ell$, radius $r$, number of trajectories $M$ satisfying the following dependence,

Then, with probability at least $1 - {2\delta}$, the gradient estimation error is bounded by

for any task $i \in {\lbrack I\rbrack}$.

### Lemma 7 (Meta-gradient Estimation)

For sufficiently small numbers ${\epsilon,\delta} \in {}$, given a control policy $K$, let $\ell$, radius $r$, number of trajectory $M$ satisfies that

where ${h_{M}^{2}{(\frac{1}{\epsilon},\delta)}}:={h_{sample}{(\frac{1}{\epsilon^{^{\operatorname{\prime\prime}}}},\frac{\delta^{\prime}}{4})}}$, $\delta^{\prime} = {{\delta/h_{{sample},{task}}}{(\frac{2}{\epsilon},\frac{\delta}{2})}}$, and $\epsilon^{\prime} = \frac{\epsilon}{6\frac{dk}{r}h_{cost}{\overline{J}}_{max}}$. Then, for each iteration the meta-gradient estimation is $\epsilon$-accurate, i.e.,

with probability at least $1 - \delta$.

### Theoretical Guarantee

We first provide the conditions on the step-sizes $\eta,\alpha$ and zeroth-order estimation parameters $M$, $\ell$, $r$, and $|\mathcal{T}_{n}|$, such that we can ensure that Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") generates stable policies at each iteration. This stability result is shown in [Theorem 1](https://arxiv.org/html/2503.00385v1#Thmtheorem1 "Theorem 1. ‣ 5.2 Theoretical Guarantee ‣ 5 GRADIENT DESCENT ANALYSIS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective").

### Theorem 1

Given an initial stabilizing controller $K_{0} \in \mathcal{S}$ and scalar $\delta \in {}$, let $\varepsilon_{i}:=\frac{\lambda_{i}\Delta_{0}^{i}}{6}$, the adaptation rate $\eta \leq {\min{\{\sqrt{\frac{1}{4{({{{\overline{h}}_{grad}^{2}k^{2}} + {{\overline{h}}_{grad}^{2}{\overline{h}}_{H}^{2}} + {\overline{h}}_{H}^{2}})}}},\frac{1}{4{\overline{h}}_{\text{grad}}}\}}}$, and $\varepsilon:=\frac{{\overline{\lambda}}_{i}{\overline{\Delta}}_{0}^{i}{({1 - {2\phi_{1}}})}\phi_{2}}{2{({{1 + {4\phi_{2}}} - {2\phi_{1}}})}}$ where $\phi_{1}:={{2{({k^{2} + {\eta^{2}{\overline{h}}_{H}^{2}}})}\eta^{2}{\overline{h}}_{grad}^{2}} + {2\eta^{2}{\overline{h}}_{H}^{2}}}$ and $\phi_{2}:=k^{2} + \eta^{2}{\overline{h}}_{H}^{2})(2 + 2{\overline{h}}_{grad}^{2}\eta^{2}$; let the learning rate $\alpha \leq \frac{\frac{1}{2} - \phi_{1}}{2\phi_{2}{\overline{h}}_{grad}}$. In addition, let the task batch size $|\mathcal{T}_{n}|$, the smoothing radius $r$, roll-out length $\ell$, and the number of sample trajectories satisfy:

where ${h_{M}^{2}{(\frac{1}{\varepsilon},\delta)}}:={h_{sample}{(\frac{1}{\varepsilon^{^{\operatorname{\prime\prime}}}},\frac{\delta^{\prime}}{4})}}$, $\delta^{\prime} = {{\delta/h_{{sample},{task}}}{(\frac{2}{\varepsilon},\frac{\delta}{2})}}$, $\varepsilon^{\prime} = \frac{\varepsilon}{6\frac{dk}{r}h_{cost}{\overline{J}}_{max}}$, $\varepsilon^{^{\operatorname{\prime\prime}}} = \frac{\varepsilon}{6}$. Then, with probability at least $1 - \delta$, Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") yields a MAML stabilizing controller $K_{n}$ for every iteration, i.e., ${K_{n}^{i},K_{n}} \in \mathcal{S}$, for all $n \in {\{ 0,1,\ldots,N\}}$, where $K_{n}^{i} = {K_{n} - {\eta\overset{\sim}{\nabla}J_{i}{(K_{n})}}}$ is the updated policy for specific tasks $i \in {\lbrack I\rbrack}$.

The proof of stability result indicates that the learned MAML-LQR controller $K_{N}$ is sufficiently close to each task-specific optimal controller $K_{i}^{\star}$. The closeness of $K_{N}$ and $K_{i}^{\ast}$ can be measured by ${J_{i}{(K_{N})}} - {J_{i}{(K_{i}^{\ast})}}$, and because it is monotonically decreasing, we obtain stability for every iteration.

We proceed to give another set of conditions on the learning parameters, which ensure that the learned meta-policy initialization $K_{N}$ is sufficiently close to the optimal MAML policy-initialization $K^{\star}:={{{\arg\min}_{K \in \overline{\mathcal{K}}}\mathcal{L}}{(K)}}$. For this purpose, we study the difference term ${\mathcal{L}{(K_{N})}} - {\mathcal{L}{(K^{\star})}}$.

### Theorem 2

(Convergence) Given an initial stabilizing controller $K_{0} \in \mathcal{S}$ and scalar $\delta \in {}$, let the parameters for Algorithm (https://arxiv.org/html/2503.00385v1#alg3 "Algorithm 3 ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") satisfy the conditions in [Theorem 1](https://arxiv.org/html/2503.00385v1#Thmtheorem1 "Theorem 1. ‣ 5.2 Theoretical Guarantee ‣ 5 GRADIENT DESCENT ANALYSIS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"). If, in addition,

where $\overline{\varepsilon}:=\frac{{\overline{\lambda}}_{i}{({1 - {\eta^{2}{\overline{h}}_{H}^{2}}})}\psi_{0}}{6}$, $\psi_{0}:={{\mathcal{L}{(K_{0})}} - {\mathcal{L}{(K^{\star})}}}$, ${h_{M}^{2}{(\frac{1}{\overline{\varepsilon}},\delta)}}:={h_{sample}{(\frac{1}{{\overline{\varepsilon}}^{^{\operatorname{\prime\prime}}}},\frac{\delta^{\prime}}{4})}}$, $\delta^{\prime} = {{\delta/h_{{sample},{task}}}{(\frac{2}{\overline{\varepsilon}},\frac{\delta}{2})}}$, ${\overline{\varepsilon}}^{\prime} = \frac{\varepsilon}{6\frac{dk}{r}h_{cost}{\overline{J}}_{max}}$, ${\overline{\varepsilon}}^{^{\operatorname{\prime\prime}}} = \frac{\overline{\varepsilon}}{6}$, Then, when $N \geq {\frac{8}{\alpha{\overline{\lambda}}_{i}{({1 - {\eta^{2}{\overline{h}}_{H}^{2}}})}}{\log{(\frac{2\psi_{0}}{\epsilon_{0}})}}}$, with probability $1 - \overline{\delta}$, it holds that,

## NUMERICAL RESULTS

We consider three cases of state and control dimensions in the numerical example, but due to computational limits, we consider a moderate system collection size $I = 5$. The collection of systems is randomly generated to behave "similarly", in the sense that the stabilizing sublevel set is admissible for some given initial controller. Specifically, we sample matrices $A_{0},B_{0},Q_{0},R_{0},\Psi_{0}$ from uniform distributions, and adjust $A_{0}$ so that ${\rho{(A_{0})}} < 1$, adjust $Q_{0},R_{0},\Psi_{0}$ to be symmetric and positive definite. Then, we sample the rest of systems $i$ independently such that their system matrices are centered around $A_{0},B_{0},Q_{0},R_{0},\Psi_{0}$, (for example ${\lbrack A_{i}\rbrack}_{m,n} \sim {\mathcal{N}{({\lbrack A_{0}\rbrack}_{m,n},0.25)}}$ for some $i$, $m$ and $n$.) and follow the same procedure to make ${\rho{(A_{i})}} < 1$ and $Q_{i},R_{i},\Psi_{i}$ positive definite.

Figure 1: The plot shows three curves encapsulating the changing of average performance during gradient descent, each corresponds to a particular dimension setting of state and action space, (green: d = 20, k = 10, orange: d = 2, k = 2, blue: d = 1, k = 1.) constant learning rates α = 1e − 3, η = 1e − 5 for orange and blue cases and α = 1e − 5, η = 1e − 7 for green curve, numbers of meta and inner perturbation M = 100, gradient smooth parameter r = 0.05, roll out length ℓ = 50.

We report the learning curves for average cost difference ratio $\frac{{\sum_{i \in {\lbrack I\rbrack}}{J_{i}{(K_{n})}}} - {J_{i}{(K_{i}^{\ast})}}}{\sum_{i \in {\lbrack I\rbrack}}{J_{i}{(K_{i}^{\ast})}}}$, this quantity captures the performance difference between a one-fits-all policy and the optimal policy in an average sense. Fig. (https://arxiv.org/html/2503.00385v1#S6.F1 "Figure 1 ‣ 6 NUMERICAL RESULTS ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"). demonstrates the evolution of this quantity during learning for three cases. Overall, despite that there are oscillations due to the randomness of meta-gradient estimators, the ratios become sufficiently small after adequate iterations, which implies the effectiveness of the algorithm.

## CONCLUSIONS

In this paper, we investigate a zeroth-order meta-policy optimization approach for model-agnostic LQRs. Drawing inspiration from MAML, we formulate the objective ((https://arxiv.org/html/2503.00385v1#S3.E4 "Equation 4 ‣ 3.2 Meta-Policy-Optimization ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective")) with the goal of refining a policy that achieves strong performance across a set of LQR problems using direct gradient methods. Our proposed method bypasses the estimation of the policy Hessian, mitigating potential issues of instability and high variance. We analyze the conditions for meta-learnability and establish finite-time convergence guarantees for the proposed algorithm. To empirically assess its effectiveness, we present numerical experiments demonstrating promising performance under the average cost difference ratio metric. A promising direction for future research is to derive sharper bounds on the iteration and sample complexity of the proposed approach and explore potential improvements.
