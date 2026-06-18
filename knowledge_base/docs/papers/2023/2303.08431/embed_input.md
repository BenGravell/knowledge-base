<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient Converges to the Globally Optimal Policy for Nearly Linear-Quadratic Regulators

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Online algorithms, Optimization, Control, Learning, Nonlinear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nonlinear control systems with partial information to the decision maker are prevalent in a variety of applications. As a step toward studying such nonlinear systems, this work explores reinforcement learning methods for finding the optimal policy in the nearly linear-quadratic regulator systems. In particular, we consider a dynamic system that combines linear and nonlinear components, and is governed by a policy with the same structure. Assuming that the nonlinear component comprises kernels with small Lipschitz coefficients, we characterize the optimization landscape of the cost function. Although the cost function is nonconvex in general, we establish the local strong convexity and smoothness in the vicinity of the global optimizer. Additionally, we propose an initialization mechanism to leverage these properties. Building on the developments, we design a policy gradient algorithm that is guaranteed to converge to the globally optimal policy with a linear rate.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) is one of the three classical machine learning paradigms, alongside supervised and unsupervised learning. RL is learning via trial and error, through interactions with an environment and possibly with other agents. In RL, an agent takes actions and receives reinforcement signals in terms of numerical rewards encoding the outcome of the chosen action. In order to maximize the accumulated reward over time, the agent learns to select actions based on past experiences (exploitation) and by making new choices (exploration). In recent years, we have witnessed successful development of RL systems in various applications, including robotics control, AlphaGo and Atari games, autonomous driving, and stock trading. Despite its practical success, theoretical understanding of RL is still limited and at its primitive stage.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To establish a better foundation of RL, there has been a surge of theoretical works in recent years on the Linear Quadratic Regulator (LQR) problem. This problem is a special class of control problems with linear dynamics and quadratic cost functions. In the seminal work of, the authors studied an LQR problem with deterministic dynamics over an infinite horizon. They proved that the simple policy gradient method converges to the globally optimal solution with a linear rate (despite nonconvexity of the objective). Their key idea is to utilize the Riccati equation (an algebraic-equation characterization that only works for LQR problems) and show that the cost function enjoys a "gradient dominance" property. This result has been extended to other settings such as linear dynamics with additive or multiplicative Gaussian noise, finite-time horizon, and modifications of the vanilla policy-gradient method in follow-up works. Other aspects in the learning of LQR, such as the trade-off between exploration and exploitation, have also been studied recently.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the desirable theoretical properties of LQR, this setting is limited in practice due to the nonlinear nature of many real-world dynamic systems. From a technical perspective, it is unclear how much we can go beyond the linear setting and still maintain the desirable properties of LQR. Our preliminary attempt in this direction is to study learning-based methods for linear systems perturbed by some nonlinear kernel functions of small magnitude. Such systems are denoted as nearly linear-quadratic systems throughout the paper. The motivations for considering this setting are twofold: Many nonlinear systems can be approximated by an LQR with a small nonlinear correction term via local expansions. Analyzing the nearly linear-quadratic system provides a natural perspective to evaluate the stability of LQR systems. This could further address the question of how robust LQR framework is with respect to model mis-specifications and, more broadly, how reliable the nearly linear-quadratic systems (including LQR problems as a special case) are.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We first study the optimization landscape of a special class of nonlinear control systems and propose a policy-gradient-based algorithm to find the optimal policy. Specifically, we consider the nonlinear dynamics consisting of both linear and nonlinear parts. The nonlinear part is modeled by a linear combination of differentiable kernels with small Lipschitz coefficients. The kernel basis is known to the agent but the coefficients are not available to the agent. Additionally, we allow agents to apply nonlinear control policies in the form of the sum of a linear part and a nonlinear part where the nonlinear part lies in the same span of the kernel basis for the dynamics. Our analysis shows that the cost function is locally strongly convex in a small neighborhood containing both a carefully chosen initial policy and the globally optimal solution. Particularly, a least-squares regression method is proposed to obtain this desirable initial policy when model parameters are unknown. With these results in hand, a zeroth-order policy-gradient method is proposed with guaranteed convergence to the globally optimal solution with a linear rate.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

where $A \in {\mathbb{R}}^{n \times n}$, $C \in {\mathbb{R}}^{n \times d}$, $B \in {\mathbb{R}}^{n \times p}$, and a kernel basis ${\phi{(x)}} = {({\phi_{1}{(x)}},\cdots,{\phi_{d}{(x)}})}^{\top}$ with ${\phi_{i}{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ $({i = {1,2,\cdots,d}})$. Here, $\phi{(x)}$ satisfies certain Lipschitz continuity conditions (specified later in Assumption 4.1). The system in (2.1) is the summation of a linear part and a "small" nonlinear part. The nonlinear part is a (finite) linear combination of kernel basis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Essentially, the dynamics in (2.1) can be viewed as a nonlinear system that closely approximates a linear model. Additionally, (2.1) is more general than the linear systems considered, and therefore better represents the behaviors of a broader class of dynamic systems in practice. Despite its nonlinearity, we will show that (2.1) still enjoys desirable theoretical properties that are not present in fully nonlinear systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The admissible control set contains a class of stationary Markovian policies that are linear combinations of the current state and kernels of the current state, i.e.,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

with $K_{1} \in {\mathbb{R}}^{p \times n}$ and $K_{2} \in {\mathbb{R}}^{p \times d}$. The form of the Markovian policies in (2.2) is motivated by the additive structure in the system dynamics (2.1), with the same kernel $\phi$ involved. Additionally, we consider the following domain $\Omega$ (i.e.,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

for some ${c_{1} > 1},{\rho_{1} \in {}}$, and $c_{2} > 1$ (to be specified later). In general, characterizing the stabilizing region of a nonlinear system is challenging. Thus, we mirror the notions used to consider the region $\Omega$ such that the control policy enjoys asymptotic stability. We will show that if the nonlinear part $\phi$ is "small", the controller in $\Omega$ is asymptotically stable, i.e., $\left\| x_{t} \right\|\rightarrow 0$ as $t\rightarrow\infty$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

where the expectation is taken with respect to $x_{0}$ (drawn from an unknown distribution $\mathcal{D}$). The state trajectory $\left\{ x_{t} \right\}_{t = 0}^{\infty}$ is generated via the control policy $K$ defined in (2.2). Here, $Q$ and $R$ are symmetric positive-definite matrices. Thus, the running cost $c_{t} = {{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}}$ is quadratic in both the state and control variables. The agent and the environment interact in the following way: At the beginning of each time step $t = {0,1,2,\ldots}$, the agent receives the state $x_{t}$ that encodes the full information of the environment and chooses a control $u_{t}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

At the end of this time step, the agent receives an instantaneous cost $c_{t}$ and a new state $x_{t + 1}$ as a consequence of the control input. The agent has the option to restart the system at any time step. This can be achieved, for example, accessing to a generative model that can generate sample trajectories. The objective is to find the optimal policy $K$ that minimizes the cost function $\mathcal{C}{(K)}$ when the model parameters ($A$, $B$ and $C$) are unknown.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

1: Input: Policy K = (K1,K2), number of trajectories J, smoothing parameter r, and episode length T.
3: Sample a policy K̂j = K + Uj, where Uj is drawn uniformly at random over matrices of size p × (n+d) whose Frobenius norm is r.
7: Receive the cost ct and the next state xt + 1 from the system.
9: Calculate the estimated cost ${\hat{\mathcal{C}}}_{j} = {\sum_{t = 0}^{T}c_{t}}$.
11: return $\hat{{\nabla\mathcal{C}}⁢{(K)}} = {\frac{1}{J}{\sum_{j = 0}^{J}{\frac{\hat{D}}{r^{2}}{\hat{\mathcal{C}}}_{j}U^{j}}}}$, where D̂ = p(n+d).
Algorithm 1 Policy Gradient Estimation

<!-- chunk {"id": "body-0015", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

The main difficulties of the control problem (2.1)--(2.4) are the unknown dynamics (2.1) and the nonconvexity of the objective (2.4), especially in high-dimensional scenarios. Given that any admissible control policy defined in (2.2) can be fully characterized by a policy parameter $K$ in $\Omega$, we leverage policy gradient methods to find the optimal policy $K^{\ast}$. When all the model parameters are known to the decision maker (referred to as the model-based case), policy gradient methods iteratively update the (current) policy $K$ by utilizing the gradient information ${\nabla\mathcal{C}}{(K)}$. When the model parameters are unknown (referred to as the model-free case), the gradient term ${\nabla\mathcal{C}}{(K)}$ can be replaced by an estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ to perform an approximate gradient descent step.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

In both cases, the initial distribution $\mathcal{D}$ is unknown while samples from $\mathcal{D}$ are available to the agent.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

We now present our policy gradient algorithm to learn the optimal control for problem (2.1)-(2.4).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Zeroth-order Optimization Method", "weight": 1.0} -->

Using a zeroth-order optimization framework, Algorithm provides an estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ for the policy gradient ${\nabla\mathcal{C}}{(K)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Zeroth-order Optimization Method", "weight": 1.0} -->

where $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$ is the initial policy, which will be chosen carefully to obtain an efficient convergence to the global optimum, see the next part, Efficient Initialization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Zeroth-order Optimization Method", "weight": 1.0} -->

Our zeroth-order estimate (line in Algorithm ) approximates the gradient of the function $\mathcal{C}$ by using the function values. Note that ${{\mathbb{E}}\lbrack U\rbrack} = 0$ as $U$ is uniformly distributed over a sphere of a ball with radius $r$ (Frobenius norm). The first-order Taylor expansion of $\mathcal{C}$ leads to

<!-- chunk {"id": "body-0021", "role": "body", "section": "Zeroth-order Optimization Method", "weight": 1.0} -->

where $K \in {\mathbb{R}}^{\hat{D}}$ with $\hat{D} = {p{({n + d})}}$ and $U$ is uniformly distributed over a sphere of a ball with radius $r$ (Frobenius norm). Hence, to compute the estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ and to approximate the expectation in (3.2) under an input policy $K$, Algorithm collects $J$ sample trajectories. Each trajectory follows a perturbed policy $\hat{K} = {K + U}$. Finally, the gradient estimate can be obtained by averaging over the sample trajectories $\frac{\hat{D}}{r^{2}}\mathcal{C}{({K + U})}U$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

As recognized, the cost function $\mathcal{C}{(K)}$ may have many spurious local minima due to its nonconvex nature. Consequently, a policy gradient method with an arbitrary initialization may fail to converge to the global minimizer. Interestingly, we present a design for an initialization, denoted by $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$, which ensures it lies within the basin of attraction of the globally optimal solution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

The LQR problem defined in is a special instance of the problem described in (2.1)--(2.4), obtained by setting $C = 0$ and $K_{2} = 0$. The intuition behind this LQR problem is as follows. When the nonlinear term $\phi{(x)}$ is "small" (see Assumption 4.1 for a mathematical description), the optimal policy $K_{1}^{lin}$ for the LQR problem is anticipated to be close to the optimal controller $K_{1}^{\ast}$ for the nonlinear problem (2.1), leading to a potentially useful initialization. Coming back to the LQR problem, it is well-established in the control literature that the policy $K_{1}^{lin}$ is unique when the pair $(A,B)$ is controllable. To define this unique policy, let the positive definite matrix $P$ be the unique solution to the Algebraic Riccati Equation (ARE),

<!-- chunk {"id": "body-0024", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

We will show that the initial policy $K^{lin}$ defined above is close to the optimal solution $K^{\ast}$ when the nonlinear term $\phi{(x)}$ is "small".

<!-- chunk {"id": "body-0025", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

1: Input: Number of samples N.
3: Sample $x_{0}^{(i)}\overset{\text{i.i.d.}}{\sim}\mathcal{D}$, $u_{0}^{(i)}\overset{\text{i.i.d.}}{\sim}\begin{cases}
{{\mathcal{N}{(0,I_{p})}},} &amp; {{\text{w.p.}1}/2} \\
\end{cases}$ and observe x1(i) = Ax0(i) + Bu0(i) + Cϕ(x0(i)).
Algorithm 2 Estimation of the System Dynamics’ Parameters with Independent Data

<!-- chunk {"id": "body-0026", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

Model-free setting. When the model parameters $A,B$ and $C$ are unknown, one key challenge lies in finding an appropriate initialization $K^{lin}$. We address this issue by utilizing the least-squares estimators of the parameters $A,B$ and $C$. This estimation process is described in Algorithm. In iteration $i$ of Algorithm, the system starts at a state $x_{0}^{(i)} \sim \mathcal{D}$, and the dynamics evolve to the next state $x_{1}^{(i)}$ under the control $u_{0}^{(i)}$. Here, we randomly draw the control $u_{0}^{(i)}$ from a certain distribution to guarantee that the parameters $A$, $B$ and $C$ can be recovered with high probability.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

When the cost parameters $Q$ and $R$ are known, we can use the estimated values $\hat{A},\hat{B}$ and $\hat{C}$ to initialize $K_{1}^{lin}$ and $K_{2}^{lin}$ in (3.5) and (3.6), repectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

With high probability, the least-squares regression (3.7) fully recovers the exact parameters, $A,B$ and $C$, with no estimation error, i.e., ${(A,B,C)} = {(\hat{A},\hat{B},\hat{C})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

The optimal solution to the nonlinear control problem (2.1)--(2.4) lies within a small neighborhood of the initial policy $K^{lin}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

The cost function (2.4) is strongly convex and smooth in a neighborhood containing both the initial policy $K^{lin}$ and the globally optimal policy $K^{\ast}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Efficient Initialization", "weight": 1.0} -->

The first result implies that the least-squares regression provides the exact initial policy ${\hat{K}}_{1}^{lin} = K_{1}^{lin}$ and ${\hat{K}}_{2}^{lin} = K_{2}^{lin}$ when the model parameters are unknown. The last two facts will establish the convergence of Algorithm to the global optimum.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we present our main theoretical results. We first prove the recovery property of Algorithm introduced in Section. Next, we proceed to characterize the optimization landscape of the cost function. In particular, we show the local strong convexity of the cost function around its global minimum. Furthermore, we prove that the globally optimal solution is close to our carefully chosen initialization. Finally, we establish the convergence of Algorithm. Before stating our main results, we make the following assumptions for problem (2.1)--(2.4).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Assumption 4.1 states that the kernel function $\phi$ is $\ell$-Lipschitz and $\ell^{\prime}$-gradient-Lipschitz. The examples of $\phi$ are not restrictive. Let us provide two kernel basis examples that satisfy Assumption 4.1. The first example is ${\phi_{i}{(x)}} = {\alpha_{i}{\sin x}}$ with $\alpha_{i} \geq 0$, for which Assumption 4.1 holds automatically. The second example is introduced below.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 4.2", "weight": 1.0} -->

Note that the class of kernel basis in Example 4.2 is used in kernel-based methods for supervised learning, unsupervised learning, nonparametric regression, and offline RL.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

We assume that $Q$ and $R$ are positive definite matrices with ${\left\| Q \right\|,\left\| R \right\|} \leq 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

The first part of the assumption guarantees that the cost function has quadratic growth and therefore renders the problem well-defined. For convenience, we denote $\sigma ≔ {\lambda_{\min}{({R + {B^{\top}QB}})}}$, the smallest eigenvalue of the matrix. The upper bound one (on the norms of $Q$ and $R$) in Assumption 4.3 is for ease of presentation and can be generalized to any arbitrary value by rescaling the cost function. Our subsequent assumption concerns the initial distribution of the state dynamics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 4.4", "weight": 1.0} -->

Assumption 4.4 requires the state initial distribution to be bounded. This assumption simplifies the proof in the subsequent sections, and can be relaxed by assuming an upper bound on the second and the third moments of the initial state. Also, the covariance matrix ${\mathbb{E}}\left\lbrack {\psi{(x_{0})}\psi{(x_{0})}^{\top}} \right\rbrack$ is assumed to be bounded below by a positive constant matrix $\sigma_{x}I$. This "diverse covariate" assumption ensures sufficient exploration (in all directions of the state space) even with a greedy algorithm. Finally, we lay out another regularity condition on the coefficient matrices $(A,B)$ and the initial policy $K^{lin}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Least-Squares Regression for Parameters Recovery", "weight": 1.0} -->

In this subsection, we show that the least-squares regression in Algorithm exactly recovers all the parameters, $A,B$ and $C$, in the system dynamics. For ease of exposition, define ${\varphi{(x,u)}} = {\lbrack x^{\top},u^{\top},{\phi{(x)}^{\top}}\rbrack}^{\top} \in {\mathbb{R}}^{n + p + d}$ and $\Theta = {\lbrack A,B,C\rbrack}^{\top} \in {\mathbb{R}}^{{({n + p + d})} \times n}$. Then the system dynamics at time $t = 1$ can be written as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Least-Squares Regression for Parameters Recovery", "weight": 1.0} -->

If the matrix $\Phi_{N}^{\top}\Phi_{N}$ is invertible, the least-squares estimator can be written as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Least-Squares Regression for Parameters Recovery", "weight": 1.0} -->

Combining the above two results, we conclude that $\hat{\Theta} = \Theta$ if $\Phi_{N}^{\top}\Phi_{N}$ is invertible. Proposition 4.6 guarantees that $\Phi_{N}^{\top}\Phi_{N}$ is invertible with high probability. Furthermore, the number of samples required by Algorithm is much less than solving independent linear equations. Analog to the analysis, we utilize the structure of the system dynamics and leverage recent results in the non-asymptotic analysis of random matrices to establish Proposition 4.6.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Landscape and Convergence Analysis", "weight": 1.0} -->

In this subsection, we study the convergence rate for the policy gradient method introduced in Section. Our first theorem characterizes the landscape of the cost function. It shows that the cost function is strongly convex and smooth in a region of the initialization $K^{lin}$ when the Lipschitz constants $\ell$ and $\ell^{\prime}$ are sufficiently small. Further, we prove the optimal controller $K^{\ast}$ is inside this neighborhood. Denote $\Gamma = {\max\left\{ \left\| A \right\|,\left\| B \right\|,\left\| C \right\|,\left\| K^{lin} \right\|_{F},1 \right\}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we numerically evaluate the performance of our policy gradient method proposed in Section through extensive experiments.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In practice, how fast does the policy gradient algorithm with known model parameters converge to the optimal solution? How sensitive is the policy gradient algorithm to the initialization?

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Does the policy gradient algorithm still converge when the Lipschitz continuity assumption in Theorem 4.8 is violated? How restrictive is the condition in practice?

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

As we will see in this section, our policy gradient algorithm converges to the globally optimal solution and is robust to the magnitude of the nonlinear term and the policy initialization regimes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Model and Parameter Setup", "weight": 1.0} -->

We experiment on (randomly generated) synthetic data. Specifically, we set $n$ (the dimension of state), $p$ (the dimension of control) and $d$ (the dimension of kernel basis) to be $3$. The cost is set to be $Q = R = I_{3 \times 3}$. The matrices $A$, $B$ and $C$ are generated randomly, with each entry drawn from a standard Gaussian distribution. The model parameters are normalized such that the spectral radius is less than $1$ with high probability. The kernel basis is fixed to be ${\phi{(x)}} = {\ell{\sin{(x)}}}$, where the operations are understood as entrywise and $\ell$ is the Lipschitz constant of the nonlinear term. The initial distribution $\mathcal{D}$ of $x_{0}$ is chosen as a standard Gaussian and $\left\| x_{0} \right\|$ is rescaled to be 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation", "weight": 1.0} -->

To study the convergence of the policy gradient method, we consider two different settings. For the first setting, we fix $\ell = 1$ and choose three initialization regimes. In Figure 1(a), $K^{lin}$ is computed by (3.5)--(3.6), where $P$ is obtained by solving the ARE (3.4) as $A$, $B$ and $C$ are assumed to be known. Also, the random policy $K^{rand}$ is generated by drawing a matrix of size $p \times {({n + d})}$ from the unit sphere (in 2-norm) uniformly at random. The gradient estimate is constructed by Algorithm with parameters $J = 300$, $T = 10$ and $r = 0.6$. To measure the performance of each policy, we empirically evaluate the cost function by sampling $J$ trajectories with the same $T$ in each trajectory. We perform the gradient descent step for 200 iterations and choose the step size $\eta = 10^{- 4}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In the second experiment, the initial policy is fixed to be $K^{} = K^{lin}$. We vary the Lipschitz constant $\ell$ from $1$ to $6$ and report the cost across iterations in Figure 1(b). Moreover, we demonstrate the robustness of our algorithm by varying the random seeds for model parameter generation. In this experiment, the model parameters $A$, $B$ and $C$ are randomly generated, while the Lipschitz constant is fixed as $\ell = 3$ and the initial policy is set to be $K^{lin}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

In Figure 1(a), we observe that the policy gradient algorithm converges under all three initialization regimes, with promising accuracy achieved within around 50 iterations. This indicates that the algorithm is relatively stable with small fluctuations and is consistent with the linear convergence rate demonstrated in the theoretical part. We also observe that the initial value obtained by the policy $K^{lin}$ is comparably close to its convergent value. Such a phenomenon implies that $K^{lin}$ is close to the optimal solution $K^{\ast}$ as expected.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

In Figure 1(b), we observe that the policy gradient algorithm converges when $\ell \leq 4$ and the method does not converge for $\ell \geq 5$. Furthermore, Figure suggests the convergence of our policy gradient method under numerous model configurations regardless of the non-linear system dynamics. Therefore, we conclude that the algorithm is robust within a certain magnitude of the nonlinear term, and extends to cases beyond the theoretical requirements.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Proofs", "weight": 1.0} -->

In this section, we prove several technical lemmas that are used in Section.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We consider a nonlinear optimal control problem, characterize the local strong convexity of the cost function, and prove that the globally optimal solution is close to a carefully chosen initialization. Additionally, we design a zeroth-order policy gradient algorithm and establish a convergence result under the proposed policy initialization scheme for the nonlinear control problem. We hope these results would shed light on the efficiency of policy gradient methods for nonlinear optimal control problems when the underlying models are unknown to the decision maker. Future work includes investigating learning problems for highly nonlinear systems and extending the analysis of quadratic cost functions to more general cost functions.
