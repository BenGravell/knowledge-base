<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective

Topics include Gradient descent, Robotics, Stability analysis, Uncertainty, Meta-learning, Classification, Sample complexity, Optimization, Control, Learning, Estimation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Meta-learning has been proposed as a promising machine learning topic in recent years, with important applications to image classification, robotics, computer games, and control systems. In this paper, we study the problem of using meta-learning to deal with uncertainty and heterogeneity in ergodic linear quadratic regulators. We integrate the zeroth-order optimization technique with a typical meta-learning method, proposing an algorithm that omits the estimation of policy Hessian, which applies to tasks of learning a set of heterogeneous but similar linear dynamic systems. The induced meta-objective function inherits important properties of the original cost function when the set of linear dynamic systems are meta-learnable, allowing the algorithm to optimize over a learnable landscape without projection onto the feasible set. We provide stability and convergence guarantees for the exact gradient descent process by analyzing the boundedness and local smoothness of the gradient for the meta-objective, which justify the proposed algorithm with gradient estimation error being small. We provide the sample complexity conditions for these theoretical guarantees, as well as a numerical example at the end to corroborate this perspective.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Recent advancements in meta-learning, a machine learning paradigm addressing the learning-to-learn challenge, have shown remarkable success across diverse domains, including robotics, image processing, and cybersecurity. One epitome of the various meta-learning approaches is Model-Agnostic Meta-Learning (MAML). Compared with other deep-learning-based meta-learning approaches, MAML formulates meta-learning as a stochastic compositional optimization problem, aiming to learn an initialization that enables rapid adaptation to new tasks with just a few gradient updates computed using online samples.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Since MAML is model-agnostic (compatible with any model trained with gradient descent), it is a widely applicable framework. In supervised learning (e.g., image recognition, speech processing), where labeled data is scarce, MAML facilitates few-shot learning, enabling models to learn new tasks with minimal examples. In reinforcement learning (RL) (e.g., robotic control, game playing), MAML allows agents to generalize across multiple environments, leading to faster adaptation in dynamic and partially observable settings. Additionally, as a gradient-based optimization method, MAML benefits from its mathematical clarity, making it well-suited for theoretical analysis and highly flexible for further enhancements.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In the RL domain, MAML samples a batch of dynamic systems from an agnostic environment, i.e., a distribution of tasks, then optimizes the policy initialization with regard to the anticipated post-policy-gradient-adaptation performance, averaging over these tasks. The policy initialization will then be fine-tuned at test time. The complete MAML policy gradient methods for such a meta-objective require differentiating through the optimization process, which necessitates the estimation of Hessians or even higher order information, making them computationally expensive and unstable, especially when a large number of gradient updates are needed at test time. This incentivizes us to focus our attention on the first-order implementation of MAML, unlike reptile, which simply neglects the computation of Hessians or higher order information when estimating the gradient for meta-objective, we develop a framework that still approximates the exact gradient of the meta-objective, with controllable bias that benefits from the smoothness of the cost functional. This methodology stems from the zeroth-order methods, more specifically, Stein's Gaussian smoothing technique.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We choose the Linear Quadratic Regulator (LQR) problem as a testbed for our analysis, as it is a fundamental component of optimal control theory. The Riccati equation, derived from the Hamilton-Jacobi equation, provides the linear optimal control gain for LQR problems. While LQR problems are analytically solvable, they can still benefit from reinforcement learning (RL) and meta-RL, particularly in scenarios where model information is incomplete---a setting known as model-free control (see for related works). Our focus is on the policy optimization of LQRs, specifically in refining an initial optimal control policy for a set of similar Linear Time-Invariant (LTI) systems, which share the same control and state space but differ in system dynamics and cost functionals. A practical example of such a scenario is a robotic arm performing a repetitive task, such as picking up and placing multiple block objects in a specific order. Each time the robot places a block, the system dynamics shift, requiring rapid adaptation to maintain optimal performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our contribution is twofold. First, we develop a zeroth-order meta-gradient estimation framework, presented in Algorithm. This Hessian-free approach eliminates the instability and high computational cost associated with exact meta-gradient estimation. Second, we establish theoretical guarantees for our proposed algorithms. Specifically, we prove a stability result (Theorem 1), ensuring that each iteration of Algorithm produces a stable control policy initialization across a wide range of tasks. Additionally, we provide a convergence guarantee (Theorem 2), which ensures that the algorithm successfully finds a local minimum for the meta-objective. Our method is built on simultaneous perturbation stochastic approximation with a close inspection of factors influencing the zero-th order gradient estimation error, including the perturbation magnitude, roll-out length of sample trajectories, batch size of trajectories, and interdependency of estimation errors arising in inner gradient adaptation and outer meta-gradient update. We believe the developed technique in controlling the estimation error and associated high-probability error bounds would benefit the future work on biased meta-learning, which trades estimation bias for lesser computation complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Even though this work studies LQRs, our zero-th order policy optimization method easily lends itself to generic Makrov systems for efficient meta-learning algorithm design.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Policy Optimization (PO)", "weight": 1.0} -->

Policy optimization (PO) methods date back to the 1970s with the model-based approach known as differential dynamic programming, which requires complete knowledge of system models. In model-free settings, where system matrices are unknown, various estimation techniques have emerged. Among these, finite-difference methods approximate the gradient by directly perturbing the policy parameters, while REINFORCE-type methods estimate the gradient of the expected return using the log-likelihood ratio trick. For LQR tasks, however, analyzing the state-control correlations in REINFORCE-type methods poses significant challenges. Therefore, we build our framework on finite-difference methods and develop a novel meta-gradient estimation procedure tailored specifically for the model-agnostic meta-learning problem. Overall, PO methods have been well established in the literature (see ).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Policy Optimization (PO)", "weight": 1.0} -->

Zeroth-order methods have garnered increasing attention in policy optimization (PO), particularly in scenarios where explicit gradient computation is infeasible or computationally expensive. Rather than relying on REINFORCE-type methods for direct gradient evaluations, zeroth-order techniques estimate gradients using finite-difference methods or random search-based approaches. A foundational work in this domain is the Evolution Strategies (ES) method, which reformulates PO as a black-box optimization problem, obtaining stochastic gradient estimates through perturbed policy rollouts. Similarly, introduces a method that leverages policy perturbation while efficiently utilizing past data, improving scalability. These approaches are particularly valuable in settings where Hessian-based computations or higher-order derivative information are impractical, driving the development of Hessian-free meta-policy optimization frameworks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model-Agnostic Meta-Learning (MAML)", "weight": 1.0} -->

The concept of meta-learning, or learning to learn, involves leveraging past experiences to develop a control policy that can efficiently adapt to novel environments, agents, or dynamics. One of the most prominent approaches in this area is MAML (Model-Agnostic Meta-Learning) as proposed. MAML is an optimization-based method that addresses task diversity by learning a "common policy initialization" from a diverse task environment. Due to its success across various domains in recent years, numerous efforts have been made to analyze its theoretical convergence properties. For instance, the model-agnostic meta-RL framework has been studied in the context of finite-horizon Markov decision processes. However, these results do not directly transfer to the policy optimization (PO) setting for LQR, because key characteristics of the LQR cost objective---such as gradient dominance and local smoothness---do not straightforwardly extend to the meta-objective.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model-Agnostic Meta-Learning (MAML)", "weight": 1.0} -->

For example, demonstrates that the global convergence of MAML over LQR tasks depends on a global property assumption ensuring that the meta-objective has a benign landscape. Similarly, establishes convergence under the condition that all LQR tasks share the same system dynamics. It was not until that comprehensive theoretical guarantees began to emerge: their analysis provided personalization guarantees for MAML in LQR settings by explicitly accounting for heterogeneity across different LQR tasks. The result readily passes the sanity check; the performance of the meta-policy initialization is affected by the diversity of the tasks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model-Agnostic Meta-Learning (MAML)", "weight": 1.0} -->

All the aforementioned MAML approaches involve estimating second-order information, which can be problematic in LQR settings where the Hessians become high-dimensional tensors. Although recent studies such as have employed advanced estimation schemes to mitigate these challenges, issues related to computational burden and numerical stability persist. Motivated by Reptile, a first-order meta-learning method, we adopt a double-layered zero-th order meta-gradient estimation scheme that skips the Hessian tensor estimation. Our work extends the original work by providing a comprehensive analysis of the induced first-order method, thereby offering a more computationally efficient and stable alternative for meta-learning in LQR tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Preliminary: Policy Optimization for LQRs", "weight": 1.0} -->

We assume a prior probability distribution $p \in {\Delta{(\mathcal{T})}}$ which we can sample the LQR tasks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Preliminary: Policy Optimization for LQRs", "weight": 1.0} -->

where $x_{t} \in \mathbb{R}^{d}$, $u_{t} \in \mathbb{R}^{k}$, $w_{t}$ are some random i.i.d. zero-mean noise with and covariance matrix $\Psi$, which is symmetric and positive definite.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Preliminary: Policy Optimization for LQRs", "weight": 1.0} -->

For each system $i$, our objective is to minimize the average infinite horizon cost,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Preliminary: Policy Optimization for LQRs", "weight": 1.0} -->

A policy $K \in \mathbb{R}^{d \times k}$ is called stable for system $i$ if and only if ${\rho{({A_{i} - {B_{i}K}})}} < 1$, where $\rho{( \cdot )}$ stands for the spectrum radius of a matrix. Denoted by $\mathcal{K}_{i}$ the set of stable policy for system $i$, let $\mathcal{K}:={\bigcap_{i \in {\lbrack I\rbrack}}\mathcal{K}_{i}}$. For a policy $K \in \mathcal{K}_{i}$, the induced cost over system $i$ is

<!-- chunk {"id": "body-0018", "role": "body", "section": "Preliminary: Policy Optimization for LQRs", "weight": 1.0} -->

can be easily verified through elementary algebra.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Meta-Policy-Optimization", "weight": 1.0} -->

In analogy to, we consider meta-policy-optimization, which draws inspiration from Model-Agnostic-Meta-Learning (MAML) in the machine learning literature.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Meta-Policy-Optimization", "weight": 1.0} -->

where $\overline{\mathcal{K}}$ is the admissible set. At first glance, one might define $\overline{\mathcal{K}}$ as simply the intersection of all $\mathcal{K}_{i}$, however, this approach may render the problem ill-posed, since the functions $J_{i}{( \cdot )}$ can be ill-defined if the one-step gradient adaptation overshoots. Thus, with a given adaptation rate $\eta$, we define $\overline{\mathcal{K}}$ as in Definition 1. ‣ 3.2 Meta-Policy-Optimization ‣ 3 PROBLEM FORMULATION ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective").

<!-- chunk {"id": "body-0021", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

In the model-free setting where knowledge of system matrices is absent, sampling and approximation become necessary. In this case, one can sample roll-out trajectories, from the specific task $i$ to perform the policy evaluation from $K$, then, optimize the system performance index through policy iteration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

The zeroth-order methods are derivative-free optimization techniques that allow us to optimize an unknown smooth function ${J_{i}{( \cdot )}}:{\mathbb{R}^{k \times d}\rightarrow\mathbb{R}}$ by estimating the first-order information. What it requires is to query the function values $J_{i}$ at some input points. A generic procedure is to firstly sample some perturbations $U \sim {{Unif}{({\mathbb{S}}_{r})}}$, where ${\mathbb{S}}_{r}:=\left. \{{r \in {\mathbb{R}}^{k \times d}} \middle| {{\| r\|}_{F} = r}\} \right.$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

Based on Stein's identity and Lemma 2.1, ${{\mathbb{E}}{\lbrack{{\nabla J_{i}}{({K + U})}}\rbrack}} = {{\nabla_{r}J_{i}}{(K)}}$, hence we obtain a perturbed version of the first-order information. The expectation $\mathbb{E}_{U \sim {{Unif}{({\mathbb{S}}_{r})}}}$ can be evaluated through Monte-Carlo sampling. However, as we discussed, a function value oracle, i.e., the value of $J_{i}$ is not always accessible. One can substitute $J_{i}$ with the return estimates obtained from sample roll-outs, as demonstrated in Algorithm, This type of gradient-estimation procedure samples trajectories with a perturbed policy $K + U$, instead of the target policy $K$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

Input: Task simulator i, Policy K, number of trajectories M,
roll out length ℓ, smoothing parameter r.
Sample a perturbed policy K + Um, where Um is drawn uniformly from 𝕊r;
Simulate K + Um for ℓ steps starting from x0 ∼ ρ0.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

where gt and xt are costs and states of the current trajectory m.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

Algorithm enables us to perform inexact gradient iterations such as $K^{\prime} = {K - {\eta\overset{\sim}{\nabla}J_{i}{(K)}}}$, where $\eta$ is the adaptation rate. However, there are two issues that persist. First, one has to restrict $r$ to be small so that the change on $K$ is not drastic, and the perturbed policy is admissible ${K + U} \in \mathcal{K}_{i}$. (We will provide theoretical guarantees later.) Second, the first-order optimization requires that the updated policy $K^{\prime}$ must be stable as well, even if the perturbed policy is stable, it is questionable how small the smoothing parameter $r$ and the adaptation rate $\eta$ should be to prevent the updated policy $K^{\prime}$ from escaping the admissible set. As has been demonstrated, the remedy to this is that when the cost function is locally smooth, it suffices to identify the regime of such smoothness and constrain the gradient steps within such regime.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Zero-th Order Methods", "weight": 1.0} -->

Even though a single LQR task objective becomes infinite as soon as $A_{i} - {B_{i}K}$ becomes unstable, as established as well as in non-convex optimization literature, the (local) smoothness and gradient domination properties almost immediately imply global convergence for the gradient descent dynamics, with a linear convergence rate. We now hash out three core auxiliary results that lead to such properties. These results can be found, we defer the explicit definition of the parameters to the appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hessian-Free Meta-Gradient Estimation", "weight": 1.0} -->

Now we recall and extend the zeroth-order technique to the meta-learning problem. Specifically, for problem, we derive a gradient expression for the perturbed objective function $\mathcal{L}$, thereby eliminating the need to compute the Hessian.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Hessian-Free Meta-Gradient Estimation", "weight": 1.0} -->

To evaluate expectation $\mathbb{E}_{{U \sim {\mathbb{S}}_{r}},{i \sim p}}$ we sample $M$ independent perturbation $U_{m}$ and a batch of tasks $\mathcal{T}_{n}$, then average the samples. To evaluate return $J_{i}{({{K + U} - {\eta{\nabla J_{i}}{({K + U})}}})}$ we first apply algorithm to obtain approximate gradient $\overset{\sim}{\nabla}J_{i}{({K + U})}$ for a single perturbed policy, then sample roll-out trajectories using the one-step updated policy ${K + U} - {\eta\overset{\sim}{\nabla}J_{i}{({K + U})}}$ to estimate its associated return.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hessian-Free Meta-Gradient Estimation", "weight": 1.0} -->

A comprehensive description of the procedure is shown in Algorithm. Essentially we aim to collect $M$ samples for return by perturbed policy $K_{m}^{i}$, which requires the original perturbed policy ${\hat{K}}_{m}$ and the gradient estimate of it. To do so, we use Algorithm as an inner loop procedure. After computing $K_{m}^{i}$ we simulate it for $\ell$ steps to get the empirical estimate of return $J_{i}{({{K + U_{m}} - {\eta{\nabla J_{i}}{({K + U_{m}})}}})}$. The entire procedure of meta-policy-optimization is shown in Algorithm.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Hessian-Free Meta-Gradient Estimation", "weight": 1.0} -->

Further, we can easily extend the results in Lemma 1. ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"), Lemma 2. ‣ 4.1 Zero-th Order Methods ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective") to the meta-objective, to show the boundedness and Lipschitz properties of ${\mathcal{L}{(K)}},{{\nabla\mathcal{L}}{(K)}}$, as in Lemma 4 and Lemma 5). ‣ 4.2 Hessian-Free Meta-Gradient Estimation ‣ 4 METHODOLOGY ‣ Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective"), whose proofs--which we defer to the Appendix A--are straightforward given the previous characterizations. These results provide an initial sanity check for the first-order iterative algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "GRADIENT DESCENT ANALYSIS", "weight": 1.0} -->

Our theoretical analysis for Algorithm can be divided into two primary objectives: stability and convergence. For stability, we demonstrate that by selecting appropriate algorithm parameters, every iteration $n$ of gradient descent satisfies $K_{n} \in \overline{\mathcal{K}}$, ensuring that both $K_{n + 1}$ and $K_{n}$ remain in $\mathcal{S}$; Regarding convergence, we establish that the learned meta-policy initialization eventually approximates the optimal policies for each specific task, and we provide a quantitative measure of this closeness.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Controlling Estimation Error", "weight": 1.0} -->

In the following, we present our results that characterize the conditions on the step-sizes $\eta,\alpha$ and zeroth-order estimation parameters $M$, $\ell$, $r$, and task batch size $|\mathcal{T}_{n}|$, for controlling gradient and meta-gradient estimation errors. The proofs are deferred to the appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Controlling Estimation Error", "weight": 1.0} -->

The smoothing radius is dictated by the smoothness of the LQR cost and its gradient, as well as the size of the locally smooth set.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Controlling Estimation Error", "weight": 1.0} -->

The roll-out length is determined by the smoothness of the cost function and the level of system noise.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Controlling Estimation Error", "weight": 1.0} -->

The number of sample trajectories and sample tasks is influenced by a broader set of parameters that govern the magnitudes and variances of the gradient estimates.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controlling Estimation Error", "weight": 1.0} -->

Inner loop estimation errors can propagate readily, particularly when the scale of the sample tasks is large.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Theoretical Guarantee", "weight": 1.0} -->

We first provide the conditions on the step-sizes $\eta,\alpha$ and zeroth-order estimation parameters $M$, $\ell$, $r$, and $|\mathcal{T}_{n}|$, such that we can ensure that Algorithm generates stable policies at each iteration. This stability result is shown in Theorem 1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "NUMERICAL RESULTS", "weight": 1.0} -->

We consider three cases of state and control dimensions in the numerical example, but due to computational limits, we consider a moderate system collection size $I = 5$. The collection of systems is randomly generated to behave "similarly", in the sense that the stabilizing sublevel set is admissible for some given initial controller. Specifically, we sample matrices $A_{0},B_{0},Q_{0},R_{0},\Psi_{0}$ from uniform distributions, and adjust $A_{0}$ so that ${\rho{(A_{0})}} < 1$, adjust $Q_{0},R_{0},\Psi_{0}$ to be symmetric and positive definite.

<!-- chunk {"id": "body-0040", "role": "body", "section": "NUMERICAL RESULTS", "weight": 1.0} -->

We report the learning curves for average cost difference ratio $\frac{{\sum_{i \in {\lbrack I\rbrack}}{J_{i}{(K_{n})}}} - {J_{i}{(K_{i}^{\ast})}}}{\sum_{i \in {\lbrack I\rbrack}}{J_{i}{(K_{i}^{\ast})}}}$, this quantity captures the performance difference between a one-fits-all policy and the optimal policy in an average sense. Fig.. demonstrates the evolution of this quantity during learning for three cases. Overall, despite that there are oscillations due to the randomness of meta-gradient estimators, the ratios become sufficiently small after adequate iterations, which implies the effectiveness of the algorithm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this paper, we investigate a zeroth-order meta-policy optimization approach for model-agnostic LQRs. Drawing inspiration from MAML, we formulate the objective with the goal of refining a policy that achieves strong performance across a set of LQR problems using direct gradient methods. Our proposed method bypasses the estimation of the policy Hessian, mitigating potential issues of instability and high variance. We analyze the conditions for meta-learnability and establish finite-time convergence guarantees for the proposed algorithm. To empirically assess its effectiveness, we present numerical experiments demonstrating promising performance under the average cost difference ratio metric. A promising direction for future research is to derive sharper bounds on the iteration and sample complexity of the proposed approach and explore potential improvements.
