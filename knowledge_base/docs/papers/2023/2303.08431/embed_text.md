## Introduction

Reinforcement learning (RL) is one of the three classical machine learning paradigms, alongside supervised and unsupervised learning. RL is learning via trial and error, through interactions with an environment and possibly with other agents. In RL, an agent takes actions and receives reinforcement signals in terms of numerical rewards encoding the outcome of the chosen action. In order to maximize the accumulated reward over time, the agent learns to select actions based on past experiences (exploitation) and by making new choices (exploration). In recent years, we have witnessed successful development of RL systems in various applications, including robotics control \[(https://arxiv.org/html/2303.08431v5#bib.bib22), (https://arxiv.org/html/2303.08431v5#bib.bib24)\], AlphaGo and Atari games \[(https://arxiv.org/html/2303.08431v5#bib.bib29), (https://arxiv.org/html/2303.08431v5#bib.bib34)\], autonomous driving \[(https://arxiv.org/html/2303.08431v5#bib.bib23)\], and stock trading \[(https://arxiv.org/html/2303.08431v5#bib.bib8)\]. Despite its practical success, theoretical understanding of RL is still limited and at its primitive stage.

To establish a better foundation of RL, there has been a surge of theoretical works in recent years on the Linear Quadratic Regulator (LQR) problem. This problem is a special class of control problems with linear dynamics and quadratic cost functions \[(https://arxiv.org/html/2303.08431v5#bib.bib5), (https://arxiv.org/html/2303.08431v5#bib.bib12), (https://arxiv.org/html/2303.08431v5#bib.bib17), (https://arxiv.org/html/2303.08431v5#bib.bib27), (https://arxiv.org/html/2303.08431v5#bib.bib30), (https://arxiv.org/html/2303.08431v5#bib.bib37), (https://arxiv.org/html/2303.08431v5#bib.bib38), (https://arxiv.org/html/2303.08431v5#bib.bib42)\]. In the seminal work of \[(https://arxiv.org/html/2303.08431v5#bib.bib12)\], the authors studied an LQR problem with deterministic dynamics over an infinite horizon. They proved that the simple policy gradient method converges to the globally optimal solution with a linear rate (despite nonconvexity of the objective). Their key idea is to utilize the Riccati equation (an algebraic-equation characterization that only works for LQR problems) and show that the cost function enjoys a "gradient dominance" property. This result has been extended to other settings such as linear dynamics with additive or multiplicative Gaussian noise, finite-time horizon, and modifications of the vanilla policy-gradient method in follow-up works \[(https://arxiv.org/html/2303.08431v5#bib.bib5), (https://arxiv.org/html/2303.08431v5#bib.bib17), (https://arxiv.org/html/2303.08431v5#bib.bib27), (https://arxiv.org/html/2303.08431v5#bib.bib30)\]. Other aspects in the learning of LQR, such as the trade-off between exploration and exploitation, have also been studied recently \[(https://arxiv.org/html/2303.08431v5#bib.bib37), (https://arxiv.org/html/2303.08431v5#bib.bib38), (https://arxiv.org/html/2303.08431v5#bib.bib42)\].

Despite the desirable theoretical properties of LQR, this setting is limited in practice due to the nonlinear nature of many real-world dynamic systems. From a technical perspective, it is unclear how much we can go beyond the linear setting and still maintain the desirable properties of LQR. Our preliminary attempt in this direction is to study learning-based methods for linear systems perturbed by some nonlinear kernel functions of small magnitude. Such systems are denoted as nearly linear-quadratic systems throughout the paper. The motivations for considering this setting are twofold: Many nonlinear systems can be approximated by an LQR with a small nonlinear correction term via local expansions. Analyzing the nearly linear-quadratic system provides a natural perspective to evaluate the stability of LQR systems. This could further address the question of how robust LQR framework is with respect to model mis-specifications and, more broadly, how reliable the nearly linear-quadratic systems (including LQR problems as a special case) are.

### Our Contributions

We first study the optimization landscape of a special class of nonlinear control systems and propose a policy-gradient-based algorithm to find the optimal policy. Specifically, we consider the nonlinear dynamics consisting of both linear and nonlinear parts. The nonlinear part is modeled by a linear combination of differentiable kernels with small Lipschitz coefficients. The kernel basis is known to the agent but the coefficients are not available to the agent. Additionally, we allow agents to apply nonlinear control policies in the form of the sum of a linear part and a nonlinear part where the nonlinear part lies in the same span of the kernel basis for the dynamics. Our analysis shows that the cost function is locally strongly convex in a small neighborhood containing both a carefully chosen initial policy and the globally optimal solution. Particularly, a least-squares regression method is proposed to obtain this desirable initial policy when model parameters are unknown. With these results in hand, a zeroth-order policy-gradient method is proposed with guaranteed convergence to the globally optimal solution with a linear rate.

### Related Work

Our work is related to three categories of prior work:

First, our framework and analysis tools are closely related to learning-based methods for the LQR problem and its variants. This includes policy gradient methods in \[(https://arxiv.org/html/2303.08431v5#bib.bib5), (https://arxiv.org/html/2303.08431v5#bib.bib12), (https://arxiv.org/html/2303.08431v5#bib.bib15), (https://arxiv.org/html/2303.08431v5#bib.bib17), (https://arxiv.org/html/2303.08431v5#bib.bib19), (https://arxiv.org/html/2303.08431v5#bib.bib27), (https://arxiv.org/html/2303.08431v5#bib.bib30), (https://arxiv.org/html/2303.08431v5#bib.bib50)\] and actor-critic methods in \[(https://arxiv.org/html/2303.08431v5#bib.bib20), (https://arxiv.org/html/2303.08431v5#bib.bib47), (https://arxiv.org/html/2303.08431v5#bib.bib51)\]. All these works focus on linear systems and linear policies, and show the property of global convergence. In contrast, we step into the nonlinear world by examining the policy gradient method for nonlinear systems that are "near-linear" in a certain sense.

Second, our work lies within the literature on nonlinear control systems. The work \[(https://arxiv.org/html/2303.08431v5#bib.bib32)\] provides a comprehensive review on this topic and \[(https://arxiv.org/html/2303.08431v5#bib.bib39), (https://arxiv.org/html/2303.08431v5#bib.bib40), (https://arxiv.org/html/2303.08431v5#bib.bib44), (https://arxiv.org/html/2303.08431v5#bib.bib48)\] offer recent advances such as feedback linearization and neural network approximations. Although largely inspired by \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\], our work differs from it. In \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\], the dynamics consist of a linear component and a small, unknown nonlinear component. However, the authors only consider linear policies, whereas our framework allows for exploration of nonlinear control policies, which is more general and potentially leads to a better solution. Furthermore, in \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\], the model parameters for the linear component are assumed to be known, which precludes the development of RL algorithms in a more general setting where the agent does not fully know the environment. In contrast, we model the linear component as unknown, and represent the nonlinear component as a linear combination of known kernel basis with unknown coefficients. We also propose a least-squares regression method to recover the system dynamics with no error (under high probability). This approach allows us to develop sample-based analysis in an unknown environment setting, which is not possible with the above-mentioned assumption in \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\]. To the best of our knowledge, this is the first theoretical study that demonstrates the global convergence of an RL method for a system with both nonlinear dynamics (with continuous state and action spaces) and nonlinear control policies in the learning context.

Finally, our work is related to the line of work on policy gradient methods. In addition to LQR, policy gradient methods have been applied to learn Markov decision processes (MDPs) with finite state and action spaces. The recent developments that provide global convergence guarantees for policy gradient methods and their variants can be found in \[(https://arxiv.org/html/2303.08431v5#bib.bib4), (https://arxiv.org/html/2303.08431v5#bib.bib1), (https://arxiv.org/html/2303.08431v5#bib.bib6), (https://arxiv.org/html/2303.08431v5#bib.bib9), (https://arxiv.org/html/2303.08431v5#bib.bib14), (https://arxiv.org/html/2303.08431v5#bib.bib25), (https://arxiv.org/html/2303.08431v5#bib.bib26), (https://arxiv.org/html/2303.08431v5#bib.bib43), (https://arxiv.org/html/2303.08431v5#bib.bib45), (https://arxiv.org/html/2303.08431v5#bib.bib46), (https://arxiv.org/html/2303.08431v5#bib.bib49), (https://arxiv.org/html/2303.08431v5#bib.bib51), (https://arxiv.org/html/2303.08431v5#bib.bib11)\].

### Notation

In this work, $\left. \parallel \cdot \parallel \right.$ is always the 2-norm of vectors and matrices, and $\left. \parallel \cdot \parallel{}_{F} \right.$ is the Frobenius norm of matrices. Additionally, ${y_{1} \lesssim y_{2}},{y_{1} \asymp y_{2}}$ and $y_{1} \gtrsim y_{2}$ mean ${y_{1} \leq {cy_{2}}},{y_{1} = {cy_{2}}}$ and $y_{1} \geq {cy_{2}}$ for some absolute constant $c > 0$, respectively.

## Problem Setup

We consider a dynamical system with the state variable $x_{t} \in {\mathbb{R}}^{n}$ and the control variable $u_{t} \in {\mathbb{R}}^{p}$:

where $A \in {\mathbb{R}}^{n \times n}$, $C \in {\mathbb{R}}^{n \times d}$, $B \in {\mathbb{R}}^{n \times p}$, and a kernel basis ${\phi{(x)}} = {({\phi_{1}{(x)}},\cdots,{\phi_{d}{(x)}})}^{\top}$ with ${\phi_{i}{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ $({i = {1,2,\cdots,d}})$. Here, $\phi{(x)}$ satisfies certain Lipschitz continuity conditions (specified later in Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). The system in ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is the summation of a linear part and a "small" nonlinear part. The nonlinear part is a (finite) linear combination of kernel basis. Essentially, the dynamics in ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) can be viewed as a nonlinear system that closely approximates a linear model. Additionally, ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is more general than the linear systems considered in \[(https://arxiv.org/html/2303.08431v5#bib.bib12), (https://arxiv.org/html/2303.08431v5#bib.bib17), (https://arxiv.org/html/2303.08431v5#bib.bib27)\], and therefore better represents the behaviors of a broader class of dynamic systems in practice. Despite its nonlinearity, we will show that ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) still enjoys desirable theoretical properties that are not present in fully nonlinear systems.

The admissible control set contains a class of stationary Markovian policies that are linear combinations of the current state and kernels of the current state, i.e.,

with $K_{1} \in {\mathbb{R}}^{p \times n}$ and $K_{2} \in {\mathbb{R}}^{p \times d}$. The form of the Markovian policies in ([2.2](https://arxiv.org/html/2303.08431v5#S2.E2 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is motivated by the additive structure in the system dynamics ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), with the same kernel $\phi$ involved. Additionally, we consider the following domain $\Omega$ (i.e., the admissible control set) for $K = {(K_{1},K_{2})}$:

for some ${c_{1} > 1},{\rho_{1} \in {}}$, and $c_{2} > 1$ (to be specified later). In general, characterizing the stabilizing region of a nonlinear system is challenging. Thus, we mirror the notions used in \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\] to consider the region $\Omega$ such that the control policy enjoys asymptotic stability. We will show that if the nonlinear part $\phi$ is "small", the controller in $\Omega$ is asymptotically stable, i.e., $\left\| x_{t} \right\|\rightarrow 0$ as $t\rightarrow\infty$. Furthermore, we consider the quadratic cost function $\mathcal{C}:{{\mathbb{R}}^{p \times {({n + d})}}\rightarrow{\mathbb{R}}}$ with $K = {(K_{1},K_{2})}$:

where the expectation is taken with respect to $x_{0}$ (drawn from an unknown distribution $\mathcal{D}$). The state trajectory $\left\{ x_{t} \right\}_{t = 0}^{\infty}$ is generated via the control policy $K$ defined in ([2.2](https://arxiv.org/html/2303.08431v5#S2.E2 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Here, $Q$ and $R$ are symmetric positive-definite matrices. Thus, the running cost $c_{t} = {{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}}$ is quadratic in both the state and control variables. The agent and the environment interact in the following way: At the beginning of each time step $t = {0,1,2,\ldots}$, the agent receives the state $x_{t}$ that encodes the full information of the environment and chooses a control $u_{t}$. At the end of this time step, the agent receives an instantaneous cost $c_{t}$ and a new state $x_{t + 1}$ as a consequence of the control input. The agent has the option to restart the system at any time step. This can be achieved by, for example, accessing to a generative model that can generate sample trajectories. The objective is to find the optimal policy $K$ that minimizes the cost function $\mathcal{C}{(K)}$ when the model parameters ($A$, $B$ and $C$) are unknown.

1: Input: Policy K = (K1,K2), number of trajectories J, smoothing parameter r, and episode length T.
3: Sample a policy K̂j = K + Uj, where Uj is drawn uniformly at random over matrices of size p × (n+d) whose Frobenius norm is r.
7: Receive the cost ct and the next state xt + 1 from the system.
9: Calculate the estimated cost ${\hat{\mathcal{C}}}_{j} = {\sum_{t = 0}^{T}c_{t}}$.
11: return $\hat{{\nabla\mathcal{C}}⁢{(K)}} = {\frac{1}{J}{\sum_{j = 0}^{J}{\frac{\hat{D}}{r^{2}}{\hat{\mathcal{C}}}_{j}U^{j}}}}$, where D̂ = p(n+d).
Algorithm 1 Policy Gradient Estimation

## Proposed Algorithm

The main difficulties of the control problem ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) are the unknown dynamics ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and the nonconvexity of the objective ([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), especially in high-dimensional scenarios. Given that any admissible control policy defined in ([2.2](https://arxiv.org/html/2303.08431v5#S2.E2 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) can be fully characterized by a policy parameter $K$ in $\Omega$, we leverage policy gradient methods in \[(https://arxiv.org/html/2303.08431v5#bib.bib36)\] to find the optimal policy $K^{\ast}$. When all the model parameters are known to the decision maker (referred to as the model-based case), policy gradient methods iteratively update the (current) policy $K$ by utilizing the gradient information ${\nabla\mathcal{C}}{(K)}$. When the model parameters are unknown (referred to as the model-free case), the gradient term ${\nabla\mathcal{C}}{(K)}$ can be replaced by an estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ to perform an approximate gradient descent step. In both cases, the initial distribution $\mathcal{D}$ is unknown while samples from $\mathcal{D}$ are available to the agent.

We now present our policy gradient algorithm to learn the optimal control for problem ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))-([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Zeroth-order Optimization Method

Using a zeroth-order optimization framework, Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") provides an estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ for the policy gradient ${\nabla\mathcal{C}}{(K)}$. This estimate will later be used in the following policy gradient update rule:

where $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$ is the initial policy, which will be chosen carefully to obtain an efficient convergence to the global optimum, see the next part, Efficient Initialization.

Our zeroth-order estimate (line (https://arxiv.org/html/2303.08431v5#alg1.l11 "In Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") in Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) approximates the gradient of the function $\mathcal{C}$ by using the function values. Note that ${{\mathbb{E}}\lbrack U\rbrack} = 0$ as $U$ is uniformly distributed over a sphere of a ball with radius $r$ (Frobenius norm). The first-order Taylor expansion of $\mathcal{C}$ leads to

where $K \in {\mathbb{R}}^{\hat{D}}$ with $\hat{D} = {p{({n + d})}}$ and $U$ is uniformly distributed over a sphere of a ball with radius $r$ (Frobenius norm). Hence, to compute the estimate $\hat{{\nabla\mathcal{C}}⁢{(K)}}$ and to approximate the expectation in ([3.2](https://arxiv.org/html/2303.08431v5#S3.E2 "In Zeroth-order Optimization Method. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) under an input policy $K$, Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") collects $J$ sample trajectories. Each trajectory follows a perturbed policy $\hat{K} = {K + U}$ (line (https://arxiv.org/html/2303.08431v5#alg1.l3 "In Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Finally, the gradient estimate can be obtained by averaging over the sample trajectories $\frac{\hat{D}}{r^{2}}\mathcal{C}{({K + U})}U$. Lemma [6.12](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.12. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") in Section (https://arxiv.org/html/2303.08431v5#S6 "6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") will show that if $J \gtrsim {\frac{{\hat{D}}^{2}}{e_{grad}^{2}}{\log\frac{4\hat{D}}{\nu}}}$, it holds with probability at least $1 - \nu$ that

### Efficient Initialization

As recognized in \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\], the cost function $\mathcal{C}{(K)}$ may have many spurious local minima due to its nonconvex nature. Consequently, a policy gradient method with an arbitrary initialization may fail to converge to the global minimizer. Interestingly, we present a design for an initialization, denoted by $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$, which ensures it lies within the basin of attraction of the globally optimal solution. Specifically, we choose $K_{1}^{lin}$ to be the optimal control policy of the following linear-quadratic problem:

The LQR problem defined in ((https://arxiv.org/html/2303.08431v5#S3.Ex2 "Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is a special instance of the problem described in ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), obtained by setting $C = 0$ and $K_{2} = 0$. The intuition behind this LQR problem is as follows. When the nonlinear term $\phi{(x)}$ is "small" (see Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") for a mathematical description), the optimal policy $K_{1}^{lin}$ for the LQR problem is anticipated to be close to the optimal controller $K_{1}^{\ast}$ for the nonlinear problem ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), leading to a potentially useful initialization. Coming back to the LQR problem, it is well-established in the control literature \[(https://arxiv.org/html/2303.08431v5#bib.bib2), (https://arxiv.org/html/2303.08431v5#bib.bib3)\] that the policy $K_{1}^{lin}$ is unique when the pair $(A,B)$ is controllable. To define this unique policy, let the positive definite matrix $P$ be the unique solution to the Algebraic Riccati Equation (ARE),

Model-based setting. When all the model parameters, ${Q,R,A,B},$ and $C$, are known, the optimal controller for the problem ((https://arxiv.org/html/2303.08431v5#S3.Ex2 "Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is given as:

We will show that the initial policy $K^{lin}$ defined above is close to the optimal solution $K^{\ast}$ when the nonlinear term $\phi{(x)}$ is "small".

1: Input: Number of samples N.
3: Sample $x_{0}^{(i)}\overset{\text{i.i.d.}}{\sim}\mathcal{D}$, $u_{0}^{(i)}\overset{\text{i.i.d.}}{\sim}\begin{cases}
{{\mathcal{N}{(0,I_{p})}},} &amp; {{\text{w.p.}1}/2} \\
\end{cases}$ and observe x1(i) = Ax0(i) + Bu0(i) + Cϕ(x0(i)).
Algorithm 2 Estimation of the System Dynamics’ Parameters with Independent Data

Model-free setting. When the model parameters $A,B$ and $C$ are unknown, one key challenge lies in finding an appropriate initialization $K^{lin}$. We address this issue by utilizing the least-squares estimators of the parameters $A,B$ and $C$. This estimation process is described in Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). In iteration $i$ of Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") (see line (https://arxiv.org/html/2303.08431v5#alg2.l3 "In Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), the system starts at a state $x_{0}^{(i)} \sim \mathcal{D}$, and the dynamics evolve to the next state $x_{1}^{(i)}$ under the control $u_{0}^{(i)}$. Here, we randomly draw the control $u_{0}^{(i)}$ from a certain distribution (line (https://arxiv.org/html/2303.08431v5#alg2.l3 "In Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) to guarantee that the parameters $A$, $B$ and $C$ can be recovered with high probability. This operation is repeated for $N$ times, resulting in a dataset of the form $\left\{ \left( x_{0}^{(i)},u_{0}^{(i)},x_{1}^{(i)} \right):{1 \leq i \leq N} \right\}$. Based on this dataset, we estimate the system parameters through the following least-squares minimization procedure:

When the cost parameters $Q$ and $R$ are known \[(https://arxiv.org/html/2303.08431v5#bib.bib7)\], we can use the estimated values $\hat{A},\hat{B}$ and $\hat{C}$ to initialize $K_{1}^{lin}$ and $K_{2}^{lin}$ in ([3.5](https://arxiv.org/html/2303.08431v5#S3.E5 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([3.6](https://arxiv.org/html/2303.08431v5#S3.E6 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), repectively. Precisely, this is achieved by setting:

where $\hat{P}$ is the solution to the ARE, ${\hat{P} = {{{{\hat{A}}^{\top}\hat{P}\hat{A}} + Q} - {{\hat{A}}^{\top}\hat{P}\hat{B}{({R + {{\hat{B}}^{\top}\hat{P}\hat{B}}})}^{- 1}{\hat{B}}^{\top}\hat{P}\hat{A}}}}.$

In the next section, we will show that:

With high probability, the least-squares regression ([3.7](https://arxiv.org/html/2303.08431v5#S3.E7 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) fully recovers the exact parameters, $A,B$ and $C$, with no estimation error, i.e., ${(A,B,C)} = {(\hat{A},\hat{B},\hat{C})}$.

The optimal solution to the nonlinear control problem ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) lies within a small neighborhood of the initial policy $K^{lin}$.

The cost function ([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is strongly convex and smooth in a neighborhood containing both the initial policy $K^{lin}$ and the globally optimal policy $K^{\ast}$.

The first result implies that the least-squares regression provides the exact initial policy ${\hat{K}}_{1}^{lin} = K_{1}^{lin}$ and ${\hat{K}}_{2}^{lin} = K_{2}^{lin}$ when the model parameters are unknown. The last two facts will establish the convergence of Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") to the global optimum.

## Main Results

In this section, we present our main theoretical results. We first prove the recovery property of Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") introduced in Section (https://arxiv.org/html/2303.08431v5#S3 "3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Next, we proceed to characterize the optimization landscape of the cost function. In particular, we show the local strong convexity of the cost function around its global minimum. Furthermore, we prove that the globally optimal solution is close to our carefully chosen initialization. Finally, we establish the convergence of Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Before stating our main results, we make the following assumptions for problem ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([2.4](https://arxiv.org/html/2303.08431v5#S2.E4 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Assumption 4.1

We assume that $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{d}}$ is differentiable, ${\phi{}} = 0$ and $\left\| {{\phi{(x)}} - {\phi{(x^{\prime})}}} \right\| \leq {\ell\left\| {x - x^{\prime}} \right\|}$ for any ${x,x^{\prime}} \in {\mathbb{R}}^{n}$ with $\ell > 0$. Moreover, we assume that $\left\| {{{\nabla\phi}{(x)}} - {{\nabla\phi}{(x^{\prime})}}} \right\| \leq {\ell^{\prime}\left\| {x - x^{\prime}} \right\|}$ for any ${x,x^{\prime}} \in {\mathbb{R}}^{n}$ with $\ell^{\prime} > 0$.

Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") states that the kernel function $\phi$ is $\ell$-Lipschitz and $\ell^{\prime}$-gradient-Lipschitz. The examples of $\phi$ are not restrictive. Let us provide two kernel basis examples that satisfy Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). The first example is ${\phi_{i}{(x)}} = {\alpha_{i}{\sin x}}$ with $\alpha_{i} \geq 0$, for which Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") holds automatically. The second example is introduced below.

### Example 4.2

Let ${N_{i} \geq 0},{i = {1,\ldots,d}}$, be non-negative integers. For fixed ${w_{j}^{i} \in \left\{ {- 1},1 \right\}^{n}},{j = {1,\ldots,N_{i}}}$, define ${\phi_{i}{(x)}} = {\alpha_{i}{\prod_{j = 1}^{N_{i}}{x^{\top}w_{j}^{i}}}}$ with $\alpha_{i} \geq 0$. Then if $\left\| x \right\| \leq M_{0}$, the kernel basis ${\phi{(x)}} = {({\phi_{1}{(x)}},\ldots,{\phi_{d}{(x)}})}^{\top}$ satisfies Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") with $\ell = \left( {\sum_{i = 1}^{d}{n^{2}\alpha_{i}^{2}N_{i}^{2}M_{0}^{2{({N_{i} - 1})}}}} \right)^{1/2}$ and $\ell^{\prime} = \left( {\sum_{i = 1}^{d}{n^{3}\alpha_{i}^{2}N_{i}^{2}{({N_{i} - 1})}^{2}M_{0}^{2{({N_{i} - 2})}}}} \right)^{1/2}$.

Note that the class of kernel basis in Example [4.2](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem2 "Example 4.2. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") is used in kernel-based methods for supervised learning, unsupervised learning, nonparametric regression, and offline RL \[(https://arxiv.org/html/2303.08431v5#bib.bib21), (https://arxiv.org/html/2303.08431v5#bib.bib35), (https://arxiv.org/html/2303.08431v5#bib.bib10), (https://arxiv.org/html/2303.08431v5#bib.bib18), (https://arxiv.org/html/2303.08431v5#bib.bib33)\].

### Proof of Example [4.2](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem2 "Example 4.2. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

It is straightforward to check that ${\phi{}} = 0$. To prove the Lipschitz and gradient-Lipschitz properties, it suffices to show that the properties hold for each $\phi_{i}{(x)}$. Indeed, if $\phi_{i}{(x)}$ is $\ell_{i}$-Lipschitz and $\ell_{i}^{\prime}$-gradient-Lipschitz, then we have

It follows that $\phi{(x)}$ is $\left( {\sum_{i = 1}^{d}\ell_{i}^{2}} \right)^{1/2}$-Lipschitz. To see $\phi$ is also gradient-Lipschitz, note that

It follows that ${\nabla\phi}{(x)}$ is $\left( {\sum_{i = 1}^{d}{(\ell_{i}^{\prime})}^{2}} \right)^{1/2}$-Lipschitz.

The rest of the proof is to show the Lipschitz continuity of $\phi_{i}$ and $\nabla\phi_{i}$. We first compute the Lipschitz constant of $\phi_{i}$. Since ${{\nabla\phi_{i}}{(x)}} = {\alpha_{i}{\sum_{j = 1}^{N_{i}}{{({\prod_{k \neq j}{x^{\top}w_{k}^{i}}})}w_{j}^{i}}}}$, we have

Also, we have ${{\nabla^{2}\phi_{i}}{(x)}} = {\alpha_{i}{\sum_{j = 1}^{N_{i}}{{\nabla_{x}\left( {\prod_{k \neq j}{x^{\top}w_{k}^{i}}} \right)}w_{j}^{i}}}} = {\alpha_{i}{\sum_{j = 1}^{N_{i}}{\sum_{k \neq j}{\prod_{l \neq {k,j}}{{({x^{\top}w_{l}^{i}})}w_{k}^{i}{(w_{j}^{i})}^{\top}}}}}}$. Thus,

Finally, we conclude the proof with $\ell_{i} = {n\alpha_{i}N_{i}M_{0}^{N_{i} - 1}}$ and $\ell_{i}^{\prime} = {n^{3/2}\alpha_{i}N_{i}{({N_{i} - 1})}M_{0}^{N_{i} - 2}}$. ∎

Next, we make the following standard assumption on the matrices $Q$ and $R$ (see also \[(https://arxiv.org/html/2303.08431v5#bib.bib28)\]).

### Assumption 4.3

We assume that $Q$ and $R$ are positive definite matrices with ${\left\| Q \right\|,\left\| R \right\|} \leq 1$.

The first part of the assumption guarantees that the cost function has quadratic growth and therefore renders the problem well-defined \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\]. For convenience, we denote $\sigma ≔ {\lambda_{\min}{({R + {B^{\top}QB}})}}$, the smallest eigenvalue of the matrix. The upper bound one (on the norms of $Q$ and $R$) in Assumption [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") is for ease of presentation and can be generalized to any arbitrary value by rescaling the cost function. Our subsequent assumption concerns the initial distribution of the state dynamics.

### Assumption 4.4

We assume that the initial distribution $\mathcal{D}$ is supported in a region with radius $D_{0}$, i.e., $\left\| x \right\| \leq D_{0}$ for $x \sim \mathcal{D}$ with probability one. Also, we assume ${{\mathbb{E}}\left\lbrack {\psi{(x_{0})}\psi{(x_{0})}^{\top}} \right\rbrack} \succeq {\sigma_{x}I}$ for some $\sigma_{x} > 0$, where ${\psi{(x_{0})}} = {(x_{0}^{\top},{\phi{(x_{0})}^{\top}})}^{\top}$.

Assumption [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") requires the state initial distribution to be bounded. This assumption simplifies the proof in the subsequent sections, and can be relaxed by assuming an upper bound on the second and the third moments of the initial state \[(https://arxiv.org/html/2303.08431v5#bib.bib31)\]. Also, the covariance matrix ${\mathbb{E}}\left\lbrack {\psi{(x_{0})}\psi{(x_{0})}^{\top}} \right\rbrack$ is assumed to be bounded below by a positive constant matrix $\sigma_{x}I$. This "diverse covariate" assumption ensures sufficient exploration (in all directions of the state space) even with a greedy algorithm. Finally, we lay out another regularity condition on the coefficient matrices $(A,B)$ and the initial policy $K^{lin}$.

### Assumption 4.5

The pair $(A,B)$ is controllable.

The controllablity assumption on the pair $(A,B)$ is standard in the literature \[(https://arxiv.org/html/2303.08431v5#bib.bib5)\]. Assumption [4.5](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem5 "Assumption 4.5. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") implies that the initial controller $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$ defined in Section (https://arxiv.org/html/2303.08431v5#S3 "3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") enjoys a stability property; that is, $\left\| {({A - {BK_{1}^{lin}}})}^{t} \right\| \leq {c_{1}^{lin}{(\rho_{1}^{lin})}^{t}}$ for all $t \geq 1$, and $\left\| {C - {BK_{2}^{lin}}} \right\| \leq c_{2}^{lin}$ for some $\rho_{1}^{lin} \in {}$ and ${c_{1}^{lin},c_{2}^{lin}} > 0$.

### Least-Squares Regression for Parameters Recovery

In this subsection, we show that the least-squares regression in Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") exactly recovers all the parameters, $A,B$ and $C$, in the system dynamics. For ease of exposition, define ${\varphi{(x,u)}} = {\lbrack x^{\top},u^{\top},{\phi{(x)}^{\top}}\rbrack}^{\top} \in {\mathbb{R}}^{n + p + d}$ and $\Theta = {\lbrack A,B,C\rbrack}^{\top} \in {\mathbb{R}}^{{({n + p + d})} \times n}$. Then the system dynamics at time $t = 1$ can be written as

In lines (https://arxiv.org/html/2303.08431v5#alg2.l2 "In Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")--(https://arxiv.org/html/2303.08431v5#alg2.l4 "In Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") of Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we collect $N$ samples $\left\{ \left( x_{0}^{(i)},u_{0}^{(i)},x_{1}^{(i)} \right):{1 \leq i \leq N} \right\}$. By denoting

If the matrix $\Phi_{N}^{\top}\Phi_{N}$ is invertible, the least-squares estimator can be written as

Combining the above two results, we conclude that $\hat{\Theta} = \Theta$ if $\Phi_{N}^{\top}\Phi_{N}$ is invertible. Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") guarantees that $\Phi_{N}^{\top}\Phi_{N}$ is invertible with high probability. Furthermore, the number of samples required by Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") is much less than solving independent linear equations. Analog to the analysis in \[(https://arxiv.org/html/2303.08431v5#bib.bib7)\], we utilize the structure of the system dynamics and leverage recent results in the non-asymptotic analysis of random matrices to establish Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators").

### Proposition 4.6

Assume Assumptions [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") hold. For any $\nu \in {}$, $\Phi_{N}^{\top}\Phi_{N}$ is invertible for all $N \gtrsim {n + p + d}$ with probability at least $1 - \nu$. In consequence, $\hat{\Theta} = \Theta$ with probability at least $1 - \nu$.

Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") implies that, with high probability, least-squares regression recovers all the model parameters, $A,B$ and $C$, with no estimation error. As a consequence, we conclude ${\hat{K}}_{1}^{lin} = K_{1}^{lin}$ and ${\hat{K}}_{2}^{lin} = K_{2}^{lin}$ with high probability. Note that in Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), there are $n{({n + p + d})}$ parameters to be estimated. Our results guarantee that $\mathcal{O}{({n + p + d})}$ samples of dimension $n$ are sufficient to recover the exact values of the parameters. This bound appears to be optimally dependent on the parameters $n,p$, and $d$. The proof of Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") relies on Lemmas [6.1](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem1 "Lemma 6.1 ([41, Theorem 5.39]). ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [6.2](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem2 "Lemma 6.2. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") which are deferred to Section [6.1](https://arxiv.org/html/2303.08431v5#S6.SS1 "6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators").

### Proof of Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

By a slight abuse of notation, let $\Sigma = {{\mathbb{E}}\left\lbrack {\varphi^{(i)}\left( \varphi^{(i)} \right)^{\top}} \right\rbrack}$ with $\varphi^{(i)} = {\varphi{(x_{0}^{(i)},u_{0}^{(i)})}}$. With the choice of $u_{0}^{(i)}$ in Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), the matrix $\Sigma$ is invertible by Lemma [6.2](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem2 "Lemma 6.2. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Let $Y_{N} = {\Phi_{N}\Sigma^{- {1/2}}}$. The $i$-th row of the matrix $Y_{N}$ is

Since $\left\| x_{0}^{(i)} \right\| \leq D_{0}$ with probability one and $\phi$ is $\ell$-Lipschitz, the rows of $Y_{N}$ are independent sub-Gaussian random vectors. Furthermore, note that

By Lemma [6.1](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem1 "Lemma 6.1 ([41, Theorem 5.39]). ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), for each $\nu \in {}$, $Y_{N}^{\top}Y_{N}$ is invertible with probability at least $1 - \nu$ for any $N \geq N_{0} ≔ \left( {{d_{1}\sqrt{n + p + d}} - \sqrt{\frac{1}{d_{2}}{\log\frac{2}{\nu}}}} \right)^{2}$. As a consequence, we have

holds with probability at least $1 - \nu$. ∎

### Landscape and Convergence Analysis

In this subsection, we study the convergence rate for the policy gradient method introduced in Section (https://arxiv.org/html/2303.08431v5#S3 "3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Our first theorem characterizes the landscape of the cost function. It shows that the cost function is strongly convex and smooth in a region of the initialization $K^{lin}$ when the Lipschitz constants $\ell$ and $\ell^{\prime}$ are sufficiently small. Further, we prove the optimal controller $K^{\ast}$ is inside this neighborhood. Denote $\Gamma = {\max\left\{ \left\| A \right\|,\left\| B \right\|,\left\| C \right\|,\left\| K^{lin} \right\|_{F},1 \right\}}$. Recall that the initial policy $K^{lin} = {(K_{1}^{lin},K_{2}^{lin})}$ satisfies $\left\| {({A - {BK_{1}^{lin}}})}^{t} \right\| \leq {c_{1}^{lin}{(\rho_{1}^{lin})}^{t}}$ for all $t \geq 1$, and $\left\| {C - {BK_{2}^{lin}}} \right\| \leq c_{2}^{lin}$ for some $\rho_{1}^{lin} \in {}$ and ${c_{1}^{lin},c_{2}^{lin}} > 0$. Having these definitions in mind, let us formally state our main result:

### Theorem 4.7

Assume Assumptions [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")--[4.5](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem5 "Assumption 4.5. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), ${{c_{1} \geq {2c_{1}^{lin}}},{\rho_{1} \in \left\lbrack \frac{\rho_{1}^{lin} + 1}{2},1 \right)}},$ and $c_{2} \geq {2c_{2}^{lin}}$. If $\ell \lesssim \frac{{({1 - \rho_{1}})}^{7}{({\sigma_{x}\sigma})}^{2}}{{({c_{1} + c_{2}})}c_{2}c_{1}^{7}{({1 + \Gamma})}^{8}D_{0}^{3}}$ and $\ell^{\prime} \lesssim \frac{{({1 - \rho_{1}})}^{8}{({\sigma_{x}\sigma})}^{2}}{{({c_{1} + c_{2}})}^{2}c_{2}^{2}c_{1}^{16}{({1 + \Gamma})}^{6}D_{0}^{4}}$, then

there exists a region ${\Lambda{(\delta)}} = \left\{ K:{\left\| {K - K^{lin}} \right\|_{F} \leq \delta} \right\}$ with $\delta \asymp \frac{{({1 - \rho_{1}})}^{4}\sigma_{x}\sigma}{{({c_{1} + c_{2}})}c_{1}^{6}\Gamma^{2}D_{0}}$ such that ${\Lambda{(\delta)}} \subset \Omega$ and $\mathcal{C}{(K)}$ is $\mu$-strongly-convex and $h$-smooth in $\Lambda{(\delta)}$ with $\mu = {\sigma_{x}\sigma}$ and $h \asymp \frac{\Gamma^{4}c_{1}^{4}D_{0}^{2}}{{({1 - \rho_{1}})}^{2}}$;

the global minimum of $\mathcal{C}{(K)}$ is achieved at a point $K^{\ast} \in {\Lambda{({\delta/3})}}$.

Part (a) of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") indicates that the cost function $\mathcal{C}{(K)}$ is strongly convex and smooth within a $\delta$-neighborhood of the initializer $K^{lin}$. Part (b) shows that the optimal controller $K^{\ast}$ lies in a $\delta/3$-neighborhood of the initialization $K^{lin}$. Consequently, the cost function is strongly convex and smooth in a region that contains both the initialization $K^{lin}$ and the global optimizer $K^{\ast}$. These facts are crucial in establishing the global convergence of the proposed algorithm. We also remark that the bounds derived in Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") are only sufficient conditions and thus can be loose. Indeed, our numerical results in Section LABEL:sec:experiments show that the algorithm may still converge even when the Lipschitz constants are larger than the bounds required in Theorem 4.7. The proof of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") relies on Lemmas [6.3](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem3 "Lemma 6.3 (Value Function). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")--[6.11](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.11. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") which are detailed in Section [6.2](https://arxiv.org/html/2303.08431v5#S6.SS2 "6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Roughly speaking, Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") implies $\left\| {\nabla^{2}\phi} \right\| \leq \ell^{\prime}$ (assuming the second-order derivative exists). Consequently, we expect that $\left\| {{\nabla^{2}C}{(K^{\ast})}} \right\| \geq {\sigma - \ell^{\prime}} > 0$ when $\ell^{\prime}$ is sufficiently small, which is the key idea for the proof.

### Proof of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

We first show that ${\Lambda{(\delta)}} \subset \Omega$ for any $\delta \leq {\min\left\{ \frac{1 - \rho_{1}}{2\Gamma c_{1}^{lin}},\frac{c_{2}^{lin}}{\Gamma} \right\}}$. Consider the following dynamics for $y_{t} \in {\mathbb{R}}^{n}$:

Define a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ as ${f{(y)}} = {B{({K_{1}^{lin} - K_{1}})}y}$. Simple algebraic manipulations show that $f$ is $\ell_{f}$-Lipschitz with $\ell_{f} = {\Gamma\delta}$. Following the same argument in \[(https://arxiv.org/html/2303.08431v5#bib.bib31), Lemma 4(a)\], together with the assumption that $K \in \Omega$, we have

$\left\| y_{t} \right\|$ $\leq {2c_{1}^{lin}{({\rho_{1}^{lin} + {2c_{1}^{lin}\ell_{f}}})}^{t}\left\| y_{0} \right\|}$ (4.2a)
${\leq {c_{1}\rho_{1}^{t}\left\| y_{0} \right\|}}.$ (4.2c)

Here, Eq. ([4.2a](https://arxiv.org/html/2303.08431v5#S4.E2.1 "In 4.2 ‣ Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) follows \[(https://arxiv.org/html/2303.08431v5#bib.bib31), Lemma 4(a)\], Eq. ([4.2b](https://arxiv.org/html/2303.08431v5#S4.E2.2 "In 4.2 ‣ Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) follows from the facts $c_{1} \geq {2c_{1}^{lin}}$ and $\delta \leq \frac{1 - \rho_{1}}{2\Gamma c_{1}^{lin}}$, and in Eq. ([4.2c](https://arxiv.org/html/2303.08431v5#S4.E2.3 "In 4.2 ‣ Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) we have used the fact $\rho_{1} \geq \frac{\rho_{1}^{lin} + 1}{2}$. Hence, we obtain

Additionally, since $\left\| {C - {BK_{2}^{lin}}} \right\| \leq c_{2}^{lin}$ and $\left\| {K_{2}^{lin} - K^{2}} \right\| \leq \delta$, it follows

Here, the penultimate inequality holds since $\delta \leq {c_{2}^{lin}/\Gamma}$ and the ultimate inequality follows from the fact that $c_{2} \geq {2c_{2}^{lin}}$. Combining Eq. ([4.3](https://arxiv.org/html/2303.08431v5#S4.E3 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([4.4](https://arxiv.org/html/2303.08431v5#S4.E4 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we conclude that ${\Lambda{(\delta)}} \subset \Omega$.

Next, we prove the local strong convexity of $\mathcal{C}{(K)}$. Let $H = {(A,C)} \in {\mathbb{R}}^{n \times {({n + d})}}$ and ${\psi{(x)}} = {(x^{\top},{\phi{(x)}^{\top}})}^{\top} \in {\mathbb{R}}^{n + d}$. Since $\phi$ is $\ell$-Lipschitz, we know that $\psi$ is $\ell_{\psi}$-Lipschitz with $\ell_{\psi} = \sqrt{1 + \ell^{2}}$. By Lemma [6.4](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem4 "Lemma 6.4 (Gradient of 𝒞⁢(𝐾)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), the policy gradient satisfies

where we have defined

Here, ${\{ x_{t}\}}_{t = 0}^{\infty}$ is the trajectory generated by the policy $K = {(K_{1},K_{2})}$ starting with the initial position $x_{0}$. By Lemma [6.5](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem5 "Lemma 6.5 (Cost Difference Lemma). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have

Moreover, since $\phi$ is $\ell$-Lipschitz with $\ell \leq 1$, Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") implies

As $K \in {\Lambda{(\delta)}}$, Eq. ([4.10](https://arxiv.org/html/2303.08431v5#S4.E10 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) implies that we can apply Lemma [6.8](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem8 "Lemma 6.8 (Local Lipschitz Continuity of ∇{𝐺_𝐾}⁢(𝑥)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") to conclude

where we have defined

with $D = {{({c_{1} + c_{2}})}c^{2}D_{0}}$. Using Eq. ([4.5](https://arxiv.org/html/2303.08431v5#S4.E5 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([4.11](https://arxiv.org/html/2303.08431v5#S4.E11 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we can rewrite Eq. ([4.9](https://arxiv.org/html/2303.08431v5#S4.E9 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) as

Furthermore, one can see that

where $\mu = {\sigma_{x}\sigma}$. Eq. ([4.14](https://arxiv.org/html/2303.08431v5#S4.E14 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds because $\Sigma_{K^{\prime}}^{\psi\psi} \succ 0$. Noting $P_{K_{1}} \succeq Q$ and ${R + {B^{\top}QB}} \succeq {\sigma I}$, we obtain Eq. ([4.15](https://arxiv.org/html/2303.08431v5#S4.E15 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([4.16](https://arxiv.org/html/2303.08431v5#S4.E16 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Finally, Eq. ([4.17](https://arxiv.org/html/2303.08431v5#S4.E17 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds due to the fact $\Sigma_{K^{\prime}}^{\psi\psi} \succeq {{\mathbb{E}}\left\lbrack {\psi{(x_{0})}\psi{(x_{0})}^{\top}} \right\rbrack} \succeq {\sigma_{x}I}$. Combining Eq. ([4.13](https://arxiv.org/html/2303.08431v5#S4.E13 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([4.17](https://arxiv.org/html/2303.08431v5#S4.E17 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), and applying Lemmas [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [6.10](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), it follows

where $c = {2c_{1}}$, $\rho = \frac{\rho_{1} + 1}{2}$, and $C_{E}$, $C_{1}$ and $C_{2}$ are defined as

To establish the local strong convexity of $\mathcal{C}{( \cdot )}$, it remains to show that

Notice by Lemma [6.8](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem8 "Lemma 6.8 (Local Lipschitz Continuity of ∇{𝐺_𝐾}⁢(𝑥)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), $L = {{\ell C_{\ell}} + {\ell^{\prime}C_{\ell^{\prime}}}}$ with $C_{\ell} = \frac{5c_{2}c^{5}{({1 + \Gamma})}^{4}}{16{({1 - \rho})}^{2}}$ and $C_{\ell^{\prime}} = \frac{3Dc_{2}^{2}c^{6}{({1 + \Gamma})}^{2}}{16{({1 - \rho})}^{3}}$, where $D = {{({c_{1} + c_{2}})}c^{2}D_{0}}$. Also, since $\ell_{\psi} \leq \sqrt{2}$, we observe $\frac{\Gamma\ell_{\psi}^{2}c^{2}D_{0}^{2}}{1 - \rho} \leq C_{1}$. Consequently, we conclude

where the last inequality holds as long as

In a similar manner to the analysis of local strong convexity, we will demonstrate next that $\mathcal{C}{(K)}$ is locally $h$-smooth. First note Eq. ([4.10](https://arxiv.org/html/2303.08431v5#S4.E10 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and Lemma [6.8](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem8 "Lemma 6.8 (Local Lipschitz Continuity of ∇{𝐺_𝐾}⁢(𝑥)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") imply

Then it follows from Lemma [6.5](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem5 "Lemma 6.5 (Cost Difference Lemma). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") that

${\mathcal{C}{(K^{\prime})}} - {\mathcal{C}{(K)}}$
$= {{Tr}\left( {{({K^{\prime} - K})}^{\top}{({R + {B^{\top}P_{K_{1}}B}})}{({K^{\prime} - K})}\Sigma_{K^{\prime}}^{\psi\psi}} \right)}$
$+ {2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}\Sigma_{K^{\prime}}^{\psi\psi}} \right)}}$
$+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}\left\lbrack {{G_{K}{({{({H - {BK^{\prime}}})}\psi{(x_{t}^{\prime})}})}} - {G_{K}{({{({H - {BK}})}\psi{(x_{t}^{\prime})}})}}} \right\rbrack} \right\rbrack}$
$= {{2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}\Sigma_{K}^{\psi\psi}} \right)}} + {2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}{({\Sigma_{K^{\prime}}^{\psi\psi} - \Sigma_{K}^{\psi\psi}})}} \right)}}}$
$+ {{Tr}\left( {{({K^{\prime} - K})}^{\top}{({R + {B^{\top}P_{K_{1}}B}})}{({K^{\prime} - K})}\Sigma_{K^{\prime}}^{\psi\psi}} \right)}$
${+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}\left\lbrack {{G_{K}{({{({H - {BK^{\prime}}})}\psi{(x_{t}^{\prime})}})}} - {G_{K}{({{({H - {BK}})}\psi{(x_{t}^{\prime})}})}}} \right\rbrack} \right\rbrack}}.$ (4.22a)
Applying Eq. ([4.21](https://arxiv.org/html/2303.08431v5#S4.E21 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) to further upper bound

$()$ $\leq {{2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}\Sigma_{K}^{\psi\psi}} \right)}} + {2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}{({\Sigma_{K^{\prime}}^{\psi\psi} - \Sigma_{K}^{\psi\psi}})}} \right)}}}$
$+ {{Tr}\left( {{({K^{\prime} - K})}^{\top}{({R + {B^{\top}P_{K_{1}}B}})}{({K^{\prime} - K})}\Sigma_{K^{\prime}}^{\psi\psi}} \right)}$
$+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{{Tr}\left( {{({K - K^{\prime}})}^{\top}B^{\top}{\nabla G_{K}}{(x_{t + 1}^{\prime})}\psi{(x_{t}^{\prime})}^{\top}} \right)}} \right\rbrack}$
$+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{\frac{L}{2}\left\| {B{({K^{\prime} - K})}\psi{(x_{t}^{\prime})}} \right\|^{2}}} \right\rbrack}$
$= {{{Tr}\left( {{({K^{\prime} - K})}^{\top}{\nabla\mathcal{C}}{(K)}} \right)} + {2{{Tr}\left( {{({K^{\prime} - K})}^{\top}E_{K}{({\Sigma_{K^{\prime}}^{\psi\psi} - \Sigma_{K}^{\psi\psi}})}} \right)}}}$
$+ {{Tr}\left( {{({K^{\prime} - K})}^{\top}{({R + {B^{\top}P_{K_{1}}B}})}{({K^{\prime} - K})}\Sigma_{K^{\prime}}^{\psi\psi}} \right)}$
$+ {\mathbb{E}}\left\lbrack \sum\limits_{t = 0}^{\infty}{Tr}\left( {(K^{\prime} - K)}^{\top}B^{\top}\left( \nabla G_{K}{(x_{t + 1})}\psi{(x_{t})}^{\top} \right. \right. \right.$
$\left. \left. \left. - \nabla G_{K}{(x_{t + 1}^{\prime})}\psi{(x_{t}^{\prime})}^{\top} \right) \right) \right\rbrack$
${+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{\frac{L}{2}\left\| {B{({K^{\prime} - K})}\psi{(x_{t}^{\prime})}} \right\|^{2}}} \right\rbrack}}.$ (4.22b)
The Cauchy-Schwarz inequality leads to

$()$ $\leq {{{Tr}\left( {{({K^{\prime} - K})}^{\top}{\nabla\mathcal{C}}{(K)}} \right)} + {2\left\| {K^{\prime} - K} \right\|_{F}\left\| E_{K} \right\|\left\| {\Sigma_{K^{\prime}}^{\psi\psi} - \Sigma_{K}^{\psi\psi}} \right\|_{F}}}$
$+ {\left\| {K^{\prime} - K} \right\|_{F}^{2}\left\| {R + {B^{\top}P_{K_{1}}B}} \right\|\left\| \Sigma_{K^{\prime}}^{\psi\psi} \right\|}$
$+ \left. {\left\| {K^{\prime} - K} \right\|_{F}\left\| B \right\|}\parallel{{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{{\nabla G_{K}}{(x_{t + 1})}\psi{(x_{t})}^{\top}}} \right\rbrack} \right.$
$- \left. {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{{\nabla G_{K}}{(x_{t + 1}^{\prime})}\psi{(x_{t}^{\prime})}^{\top}}} \right\rbrack}\parallel \right._{F}$
${+ {{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{\infty}{\frac{L}{2}\left\| B \right\|^{2}\left\| {K^{\prime} - K} \right\|_{F}^{2}\left\| {\psi{(x_{t}^{\prime})}} \right\|^{2}}} \right\rbrack}}.$ (4.22c)
Next, we apply Lemmas [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [6.10](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") to derive

$()$ $\leq {Tr}\left( {(K^{\prime} - K)}^{\top}\nabla\mathcal{C}{(K)} \right) + \left( 2C_{1}C_{E}\delta + \Gamma C_{2} + \frac{L}{2}\frac{\Gamma^{2}\ell_{\psi}^{2}c^{2}D_{0}^{2}}{1 - \rho} \right.$
$\left. \left. + \parallel R + B^{\top}P_{K_{1}}B\parallel\parallel\Sigma_{K^{\prime}}^{\psi\psi}\parallel \right)\parallel K^{\prime} - K\parallel_{F}^{2} \right.$
$\left. \leq {Tr}{(K^{\prime} - K)}^{\top}\nabla\mathcal{C}{(K)} + \left( \frac{\mu}{2} + \parallel R + B^{\top}P_{K_{1}}B\parallel\parallel\Sigma_{K^{\prime}}^{\psi\psi}\parallel \right)\parallel K^{\prime} - K \parallel_{F}^{2}, \right.$ (4.22d)

where Eq. ([4.22d](https://arxiv.org/html/2303.08431v5#S4.E22.4 "In 4.22 ‣ Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is a consequence of Eq. ([4.19](https://arxiv.org/html/2303.08431v5#S4.E19 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Finally, applying the upper bounds on $\left\| P_{K_{1}} \right\|$ and $\left\| \Sigma_{K^{\prime}}^{\psi\psi} \right\|$ from Lemmas [6.7](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem7 "Lemma 6.7. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [6.11](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.11. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we obtain

Therefore, combining Eq. ([4.20](https://arxiv.org/html/2303.08431v5#S4.E20 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([4.23](https://arxiv.org/html/2303.08431v5#S4.E23 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we finish the proof of part (a) of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators").

In the following, we will prove part (b) of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). We first observe that $E_{K^{lin}} = {{RK^{lin}} - {B^{\top}P_{K_{1}^{lin}}{({H - {BK^{lin}}})}}} = 0$ by Eq. ([3.5](https://arxiv.org/html/2303.08431v5#S3.E5 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([3.6](https://arxiv.org/html/2303.08431v5#S3.E6 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Then it follows from Lemma [6.5](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem5 "Lemma 6.5 (Cost Difference Lemma). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") that

Additionally, Eq. ([4.17](https://arxiv.org/html/2303.08431v5#S4.E17 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) with $K^{\prime} = K^{lin}$ implies that

Also, note that

Hence, we can apply Lemma [6.8](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem8 "Lemma 6.8 (Local Lipschitz Continuity of ∇{𝐺_𝐾}⁢(𝑥)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") to obtain

where we have used the fact that ${{\nabla G_{K^{lin}}}{}} = 0$ to reach the second inequality. As such, we can deduce

Here, Eq. ([4.25](https://arxiv.org/html/2303.08431v5#S4.E25 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds since $\left\| B \right\| \leq \Gamma$ and $\left\| {\psi{(x_{t})}} \right\| \leq {\ell_{\psi}\left\| x_{t} \right\|}$, Eq. ([4.26](https://arxiv.org/html/2303.08431v5#S4.E26 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) follows from $\left\| x_{t} \right\| \leq {c\rho^{t}D_{0}}$, and we have used the fact that ${1/2} < \rho < 1$ to obtain Eq ([4.27](https://arxiv.org/html/2303.08431v5#S4.E27 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). By leveraging Eq. ([4.27](https://arxiv.org/html/2303.08431v5#S4.E27 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we can rewrite Eq. ([4.24](https://arxiv.org/html/2303.08431v5#S4.E24 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) as

Since $\left\| {K - K^{lin}} \right\|_{F} > {\delta/3}$, it suffices to show that

Indeed, this inequality holds since

as long as the following conditions are satisfied

Choose $\delta$ as in the proof of part (a), we finish the proof of part (b) of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). ∎

Given the landscape results, if ${\nabla\mathcal{C}}{(K)}$ is assumed to be known, starting from the initialization $K^{lin}$, the policy gradient method leads to the global minimum of the cost function $\mathcal{C}{(K)}$. Hence, it is not surprising that the policy gradient method ([3.1](https://arxiv.org/html/2303.08431v5#S3.E1 "In Zeroth-order Optimization Method. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) converges to the globally optimal solution with the gradient estimation in Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). This result is formally stated in Theorem [4.8](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem8 "Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Recall the policy update rule $K^{({m + 1})} = {K^{(m)} - {\eta\hat{{\nabla\mathcal{C}}⁢{(K^{(m)})}}}}$.

### Theorem 4.8

Assume the conditions in Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") hold. Let $\epsilon > 0$ and $\nu \in {}$ be given. Suppose the step size $\eta < \frac{1}{h}$ and the number of gradient descent steps $M \geq {\frac{2}{\eta\mu}{\log\left( {\frac{\delta}{3}\sqrt{\frac{2h}{\epsilon}}} \right)}}$. Further, assume the gradient estimator parameter in Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") satisfies $r \leq {\min\left\{ \frac{\delta}{3},{\frac{1}{3h}e_{\text{grad}}} \right\}}$, $T \geq {\frac{1}{1 - \rho_{1}}{\log\frac{6\hat{D}C_{\text{max}}}{e_{\text{grad}}r}}}$, and

where $C_{\max} = \frac{24{({1 + \Gamma})}^{2}c_{1}^{2}D_{0}^{2}}{1 - \rho_{1}}$, and $e_{\text{grad}} = {\min\left\{ \frac{\delta\mu}{6},{\frac{\mu}{2}\sqrt{\frac{\epsilon}{2h}}} \right\}}$. Then with probability at least $1 - \nu$, we have ${{\mathcal{C}{(K^{(M)})}} - {\mathcal{C}{(K^{\ast})}}} < \epsilon$.

This result shows that, despite the existence of nonlinear terms, finding the optimal control policy is still tractable when nonlinear terms are "sufficiently small". Moreover, we comment that the convergence rate $\mathcal{O}\left( {\frac{h}{\mu}{\log\left( \frac{1}{\epsilon} \right)}} \right)$ matches that of LQR \[(https://arxiv.org/html/2303.08431v5#bib.bib12)\] in terms of the dependency on $\mu$ and $\epsilon$. Furthermore, the policy gradient approach requires a total number of $MJT$ samples to perform the gradient estimation for $M$ times. Here, the dependency of parameters in Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") are given by $r = {\mathcal{O}\left( {\frac{\mu}{h}\sqrt{\frac{\epsilon}{h}}} \right)}$, $T = {\mathcal{O}\left( {\log\left( \frac{h^{2}}{\epsilon\mu^{2}} \right)} \right)}$ and $J = {\overset{\sim}{\mathcal{O}}\left( \frac{h^{4}}{\epsilon^{2}\mu^{4}} \right)}$. Finally, we remark that our zeroth-order optimization framework is one of many possibilities of policy-based methods. One can improve the sample complexity by incorporating variance reduction techniques into our framework. The proof of Theorem [4.8](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem8 "Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") relies on Lemma [6.12](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.12. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") which is deferred to Section [6.3](https://arxiv.org/html/2303.08431v5#S6.SS3 "6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators").

### Proof of Theorem [4.8](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem8 "Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

Let $\mathcal{F}_{m}$ be the filtration generated by $\left\{ \hat{{\nabla\mathcal{C}}⁢{(K^{(m^{\prime})})}} \right\}_{m^{\prime} = 0}^{m - 1}$. Define the following event:

where ${\text{Ball}{(K^{\ast},{\delta/3})}} = \left\{ K:{\left\| {K - K^{\ast}} \right\|_{F} \leq {\delta/3}} \right\}$. Apparently, both $K^{(m)}$ and the event $\mathcal{E}_{m}$ are $\mathcal{F}_{m}$-measurable. We want to show the following inequality:

Namely, if event $\mathcal{E}_{m}$ is true, conditioned on $\mathcal{F}_{m}$, the event $\mathcal{E}_{m + 1}$ happens with probability at least $1 - {\nu/M}$. Note that conditioned on event $\mathcal{E}_{m}$, we have $\left\| {K^{(m)} - K^{lin}} \right\|_{F} \leq {\left\| {K^{(m)} - K^{\ast}} \right\|_{F} + \left\| {K^{lin} - K^{\ast}} \right\|_{F}} \leq {{2\delta}/3}$, which follows that $K^{(m)} \in {\Lambda{({{2\delta}/3})}}$. Next, we show that $K^{({m + 1})} \in {\text{Ball}{(K^{\ast},{\delta/3})}}$. Note that by $\mu$-strong convexity of the cost function $\mathcal{C}$, it holds

Furthermore, since $\mathcal{C}{( \cdot )}$ is $h$-smooth, we have

Thus, Eq. ([4.29](https://arxiv.org/html/2303.08431v5#S4.E29 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

where ${\eta{({1 - {h\eta}})}} > 0$ since $0 < \eta < {1/h}$. Note under our selection of parameters, by Lemma [6.12](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.12. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have $\left\| {{\hat{\nabla\mathcal{C}}{(K^{(m)})}} - {{\nabla\mathcal{C}}{(K^{(m)})}}} \right\|_{F} \leq e_{\text{grad}}$ with probability at least $1 - {\nu/M}$. Together with Eq. ([4.30](https://arxiv.org/html/2303.08431v5#S4.E30 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), with probability at least $1 - {\nu/M}$, we have

Here, Eq. ([4.32](https://arxiv.org/html/2303.08431v5#S4.E32 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) follows from the fact $\left\| {K^{(m)} - K^{\ast}} \right\|_{F} \leq \frac{\delta}{3}$. We have used the facts ${({1 - x})}^{1/2} \leq {1 - {\frac{1}{2}x}}$ and $e_{grad} \leq \frac{\delta\mu}{6}$ to derive Eq. ([4.33](https://arxiv.org/html/2303.08431v5#S4.E33 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). As such, taking the expectation of ([4.28](https://arxiv.org/html/2303.08431v5#S4.E28 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) on both sides, we have

Unrolling Eq. ([4.34](https://arxiv.org/html/2303.08431v5#S4.E34 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we obtain ${{\mathbb{P}}{(\mathcal{E}_{M})}} \geq {\left( {1 - \frac{\nu}{M}} \right)^{M}{\mathbb{P}}{(\mathcal{E}_{0})}} = \left( {1 - \frac{\nu}{M}} \right)^{M} \geq {1 - \nu}$. Now, on event $\mathcal{E}_{M}$, by Eq. ([4.31](https://arxiv.org/html/2303.08431v5#S4.E31 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we also have

Here, Eq. ([4.35](https://arxiv.org/html/2303.08431v5#S4.E35 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds since $\left\| {K^{} - K^{\ast}} \right\| \leq {\delta/3}$, and Eq. ([4.36](https://arxiv.org/html/2303.08431v5#S4.E36 "In Proof of Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) follows from the assumptions that $M \geq {\frac{2}{\eta\mu}{\log\left( {\frac{\delta}{3}\sqrt{\frac{2h}{\epsilon}}} \right)}}$ and $e_{\text{grad}} \leq {\frac{\mu}{2}\sqrt{\frac{\epsilon}{2h}}}$. Finally, by the $h$-smoothness of $\mathcal{C}{( \cdot )}$ again, we conclude that with probability at least $1 - \nu$,

which finishes the proof. ∎

## Numerical Experiments

In this section, we numerically evaluate the performance of our policy gradient method proposed in Section (https://arxiv.org/html/2303.08431v5#S3 "3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") through extensive experiments. In particular, we focus on addressing the following questions:

In practice, how fast does the policy gradient algorithm with known model parameters converge to the optimal solution? How sensitive is the policy gradient algorithm to the initialization?

Does the policy gradient algorithm still converge when the Lipschitz continuity assumption in Theorem [4.8](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem8 "Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") is violated? How restrictive is the condition in practice?

As we will see in this section, our policy gradient algorithm converges to the globally optimal solution and is robust to the magnitude of the nonlinear term and the policy initialization regimes.

### Model and Parameter Setup

We experiment on (randomly generated) synthetic data. Specifically, we set $n$ (the dimension of state), $p$ (the dimension of control) and $d$ (the dimension of kernel basis) to be $3$. The cost is set to be $Q = R = I_{3 \times 3}$. The matrices $A$, $B$ and $C$ are generated randomly, with each entry drawn from a standard Gaussian distribution. The model parameters are normalized such that the spectral radius is less than $1$ with high probability. The kernel basis is fixed to be ${\phi{(x)}} = {\ell{\sin{(x)}}}$, where the operations are understood as entrywise and $\ell$ is the Lipschitz constant of the nonlinear term. The initial distribution $\mathcal{D}$ of $x_{0}$ is chosen as a standard Gaussian and $\left\| x_{0} \right\|$ is rescaled to be 1.

### Evaluation

To study the convergence of the policy gradient method, we consider two different settings. For the first setting, we fix $\ell = 1$ and choose three initialization regimes. In Figure [1(a)](https://arxiv.org/html/2303.08431v5#S5.F1.sf1 "In Figure 1 ‣ Evaluation ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), $K^{lin}$ is computed by ([3.5](https://arxiv.org/html/2303.08431v5#S3.E5 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"))--([3.6](https://arxiv.org/html/2303.08431v5#S3.E6 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), where $P$ is obtained by solving the ARE ([3.4](https://arxiv.org/html/2303.08431v5#S3.E4 "In Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) as $A$, $B$ and $C$ are assumed to be known. Also, the random policy $K^{rand}$ is generated by drawing a matrix of size $p \times {({n + d})}$ from the unit sphere (in 2-norm) uniformly at random. The gradient estimate is constructed by Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") with parameters $J = 300$, $T = 10$ and $r = 0.6$. To measure the performance of each policy, we empirically evaluate the cost function by sampling $J$ trajectories with the same $T$ in each trajectory. We perform the gradient descent step for 200 iterations and choose the step size $\eta = 10^{- 4}$. In the second experiment, the initial policy is fixed to be $K^{} = K^{lin}$. We vary the Lipschitz constant $\ell$ from $1$ to $6$ and report the cost across iterations in Figure [1(b)](https://arxiv.org/html/2303.08431v5#S5.F1.sf2 "In Figure 1 ‣ Evaluation ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Moreover, we demonstrate the robustness of our algorithm by varying the random seeds for model parameter generation (see Figure (https://arxiv.org/html/2303.08431v5#S5.F2 "Figure 2 ‣ Discussion ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). In this experiment, the model parameters $A$, $B$ and $C$ are randomly generated, while the Lipschitz constant is fixed as $\ell = 3$ and the initial policy is set to be $K^{lin}$.

(b) Impact of Lipschitz constants

Figure 1: Convergence of the policy gradient algorithm

### Discussion

In Figure [1(a)](https://arxiv.org/html/2303.08431v5#S5.F1.sf1 "In Figure 1 ‣ Evaluation ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we observe that the policy gradient algorithm converges under all three initialization regimes, with promising accuracy achieved within around 50 iterations. This indicates that the algorithm is relatively stable with small fluctuations and is consistent with the linear convergence rate demonstrated in the theoretical part. We also observe that the initial value obtained by the policy $K^{lin}$ is comparably close to its convergent value. Such a phenomenon implies that $K^{lin}$ is close to the optimal solution $K^{\ast}$ as expected.

In Figure [1(b)](https://arxiv.org/html/2303.08431v5#S5.F1.sf2 "In Figure 1 ‣ Evaluation ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we observe that the policy gradient algorithm converges when $\ell \leq 4$ and the method does not converge for $\ell \geq 5$. Furthermore, Figure (https://arxiv.org/html/2303.08431v5#S5.F2 "Figure 2 ‣ Discussion ‣ 5 Numerical Experiments ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") suggests the convergence of our policy gradient method under numerous model configurations regardless of the non-linear system dynamics. Therefore, we conclude that the algorithm is robust within a certain magnitude of the nonlinear term, and extends to cases beyond the theoretical requirements.

Figure 2: Robustness of policy gradient algorithm.

## Proofs

In this section, we prove several technical lemmas that are used in Section (https://arxiv.org/html/2303.08431v5#S4 "4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators").

### Proof of Proposition [4.6](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem6 "Proposition 4.6. ‣ 4.1 Least-Squares Regression for Parameters Recovery ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

We start by presenting a standard non-asymptotic bound on the minimum singular value of a random matrix with sub-Gaussian rows. Denote $\lambda_{\min}{({Y^{\top}Y})}$ as the smallest singular value of a matrix $Y$.

### Lemma 6.1 (\[[41](https://arxiv.org/html/2303.08431v5#bib.bib41), Theorem 5.39\])

Let $Y \in {\mathbb{R}}^{N \times k}$ be a matrix whose rows are independent sub-Gaussian isotropic random vectors in ${\mathbb{R}}^{k}$. Then for every $\nu \in {}$, with probability at least $1 - \nu$, one has

Here $d_{1},d_{2}$ are absolute constants that only depend on the sub-Gaussian norm of the rows. In particular, ${d_{1} = 1},{d_{2} = {1/2}}$ if $Y$ has i.i.d. $\mathcal{N}{}$ entries.

The next result shows that the second-moment matrix of the row vectors of $\Phi_{N}^{\top}\Phi_{N}$ is invertible. Recall $\Sigma = {{\mathbb{E}}\left\lbrack {\varphi^{(i)}\left( \varphi^{(i)} \right)^{\top}} \right\rbrack}$ with $\varphi^{(i)} = {\varphi{(x_{0}^{(i)},u_{0}^{(i)})}}$.

### Lemma 6.2

Assume Assumption [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") holds. If the random vector $u_{0}^{(i)} \in {\mathbb{R}}^{p}$ is such that $0 < {{\mathbb{P}}\left( {\left| {w^{\top}u_{0}^{(i)}} \right| > 0} \right)} < 1$ for all $w \neq 0$, then the matrix $\Sigma$ is invertible.

### Proof

Since $\Sigma$ is a symmetric matrix, it is equivalent to show that $\Sigma$ is positive definite. Let $s = {(s_{1}^{\top},s_{2}^{\top},s_{3}^{\top})}^{\top} \neq 0$. The matrix $\Sigma$ is positive definite if and only if

We consider two cases of $(s_{1},s_{3})$. If ${(s_{1},s_{3})} \neq 0$, by Assumption [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have

Moreover, since $x_{0}^{(i)}$ and $u_{0}^{(i)}$ are independent, Eq. ([6.1](https://arxiv.org/html/2303.08431v5#S6.E1 "In Proof. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

By Eq. ([6.2](https://arxiv.org/html/2303.08431v5#S6.E2 "In Proof. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and the fact that ${{\mathbb{P}}\left( {\left| {s_{2}^{\top}u_{0}^{(i)}} \right| > 0} \right)} < 1$ for all $s_{2}$, Eq. ([6.1](https://arxiv.org/html/2303.08431v5#S6.E1 "In Proof. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds when ${(s_{1},s_{3})} \neq 0$. Furthermore, if ${(s_{1},s_{3})} = 0$, Eq. ([6.1](https://arxiv.org/html/2303.08431v5#S6.E1 "In Proof. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) simplifies to ${{\mathbb{P}}\left( {\left| {s_{2}^{\top}u_{0}^{(i)}} \right| > 0} \right)} > 0$ for all $s_{2} \neq 0$, which holds by definition of $u_{0}^{(i)}$ in Algorithm (https://arxiv.org/html/2303.08431v5#alg2 "Algorithm 2 ‣ Efficient Initialization. ‣ 3 Proposed Algorithm ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Therefore, we conclude that $\Sigma$ is positive definite and thus invertible. ∎

### Proof of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

We devote this subsection to the missing proofs of Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). We begin by proving several auxiliary lemmas. Denote the value function and $Q$ function conditioned on the initial position as

First, we provide a characterization of the value function below.

### Lemma 6.3 (Value Function)

The value function takes the form

where $P_{K_{1}}$ satisfies Eq. ([4.7](https://arxiv.org/html/2303.08431v5#S4.E7 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and $G_{K}{(x)}$ is defined as in Eq. ([4.8](https://arxiv.org/html/2303.08431v5#S4.E8 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Proof

By the Bellman equation, the value function satisfies,

Define ${G_{K}{(x)}} = {{V_{K}{(x)}} - {x^{\top}P_{K_{1}}x}}$. Replacing $V_{K}{(x)}$ by ${G_{K}{(x)}} + {x^{\top}P_{K_{1}}x}$ on both sides of Eq. ([6.6](https://arxiv.org/html/2303.08431v5#S6.E6 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

with $x_{1} = {{{({A - {BK_{1}}})}x} + {{({C - {BK_{2}}})}\phi{(x)}}}$. Since $P_{K_{1}}$ satisfies ([4.7](https://arxiv.org/html/2303.08431v5#S4.E7 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

Here, we have used the matrix trace property in Eq. ([6.8](https://arxiv.org/html/2303.08431v5#S6.E8 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). By unrolling the recursive relation ([6.8](https://arxiv.org/html/2303.08431v5#S6.E8 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we obtain Eq. ([6.8](https://arxiv.org/html/2303.08431v5#S6.E8 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Therefore, Eq. ([4.8](https://arxiv.org/html/2303.08431v5#S4.E8 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds. ∎

Recall that we have defined the coefficient matrix $H = {(A,C)}$, and the feature map ${\psi{(x)}} = {(x^{\top},{\phi{(x)}^{\top}})}^{\top}$. Then the dynamics ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) can be written as

Since $\phi{(x)}$ is $\ell$-Lipschitz by Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we know that $\psi{(x)}$ is also $\ell_{\psi}$-Lipschitz with $\ell_{\psi}:=\sqrt{1 + \ell^{2}}$. The following lemma gives us the gradient of the cost function $\mathcal{C}{(K)}$.

### Lemma 6.4 (Gradient of $\mathcal{C}{(K)}$)

The gradient of $\mathcal{C}{(K)}$ satisfies

where $E_{K}$, $\Sigma_{K}^{\psi\psi}$ and $\Sigma_{K}^{G\psi}$ are defined as in Eq. ([4.6](https://arxiv.org/html/2303.08431v5#S4.E6 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Proof

Recall the Bellman equation

Taking gradient in $K$ on both sides of Eq. ([6.11](https://arxiv.org/html/2303.08431v5#S6.E11 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

where ${{\nabla_{K}V}{(x_{1})}} = \left. \frac{\partial{V_{K}{(x_{1})}}}{\partial K} \right|_{x_{1} = {{({H - {BK}})}\psi{(x)}}}$. Note the directional derivative of $x_{1}$ in $K$ along the direction $\Delta$ is ${x_{1}^{\prime}\lbrack\Delta\rbrack} = {- {B\Delta\psi{(x)}}}$. Since ${{\nabla_{x}V_{K}}{(x)}} = {{2P_{K_{1}}x} + {{\nabla G}{(x)}}}$, we have

Since $x_{1} = {{({H - {BK}})}\psi{(x)}}$, it follows that

Substituting Eq. ([6.13](https://arxiv.org/html/2303.08431v5#S6.E13 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) back into Eq. ([6.12](https://arxiv.org/html/2303.08431v5#S6.E12 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we obtain

Unrolling this recursive relation and apply the definition of $E_{K}$ in ([4.6](https://arxiv.org/html/2303.08431v5#S4.E6 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we conclude that

Take expectation w.r.t. $x_{0} = x$ and then we finish the proof. ∎

With Lemma [6.3](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem3 "Lemma 6.3 (Value Function). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and Lemma [6.4](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem4 "Lemma 6.4 (Gradient of 𝒞⁢(𝐾)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we provide a formula for ${\mathcal{C}{(K^{\prime})}} - {\mathcal{C}{(K)}}$ in the following lemma.

### Lemma 6.5 (Cost Difference Lemma)

For $K = {(K_{1},K_{2})}$ and $K^{\prime} = {(K_{1}^{\prime},K_{2}^{\prime})}$, we have

### Proof

By \[(https://arxiv.org/html/2303.08431v5#bib.bib12), Lemma 10\], we have

where $\left\{ x_{t}^{\prime} \right\}$ is the trajectory generated by $x_{0}^{\prime} = x$ and $u_{t}^{\prime} = {- {K^{\prime}\psi{(x_{t}^{\prime})}}}$, and ${A_{K}{(x,u)}} = {{Q_{K}{(x,u)}} - {V_{K}{(x)}}}$ is the advantage function.

For given $u = {- {K^{\prime}\psi{(x)}}}$, by definition ([6.3](https://arxiv.org/html/2303.08431v5#S6.E3 "In 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([6.4](https://arxiv.org/html/2303.08431v5#S6.E4 "In 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

We next compute the last two terms in Eq. ([6.15](https://arxiv.org/html/2303.08431v5#S6.E15 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). By Lemma [6.3](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem3 "Lemma 6.3 (Value Function). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we notice

Substitution it back into Eq. ([6.15](https://arxiv.org/html/2303.08431v5#S6.E15 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we obtain

Finally, we take expectation of both sides of Eq. ([6.14](https://arxiv.org/html/2303.08431v5#S6.E14 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) w.r.t. $x_{0}$, yielding

Next, we show that the state trajectory has an exponential decay property regardless of the initial state. In consequence, the cost function $\mathcal{C}{( \cdot )}$ is bounded.

### Lemma 6.6 (Stability of the Trajectory $\left\{ x_{t} \right\}$)

Assume Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") holds, $K \in \Omega$ and $\ell \leq \frac{1 - \rho_{1}}{4c_{1}c_{2}}$. The following results hold for each $t \geq 0$:

For any $x_{0} \in {\mathbb{R}}^{n}$, we have $\left\| x_{t} \right\| \leq {c\rho^{t}\left\| x_{0} \right\|}$, where $c = {2c_{1}}$ and $\rho = \frac{\rho_{1} + 1}{2}$.

Let $\left\{ x_{t} \right\}$ and $\left\{ x_{t}^{\prime} \right\}$ be the state trajectories starting from $x_{0}$ and $x_{0}^{\prime}$, respectively. Then $\left\| {x_{t} - x_{t}^{\prime}} \right\| \leq {c\rho^{t}\left\| {x_{0} - x_{0}^{\prime}} \right\|}$, and consequently, $\left\| \frac{\partial x_{t}}{\partial x_{0}} \right\| \leq {c\rho^{t}}$.

Let $\left\{ x_{t} \right\}$ and $\left\{ x_{t}^{\prime} \right\}$ be trajectories defined as above. Then $\left\| {\frac{\partial x_{t}}{\partial x_{0}} - \frac{\partial x_{t}^{\prime}}{\partial x_{0}^{\prime}}} \right\| \leq {\frac{c_{2}\ell^{\prime}c^{3}}{1 - \rho}\rho^{t - 1}\left\| {x_{0} - x_{0}^{\prime}} \right\|}$.

### Proof

Let ${{f{(x)}} = {{({C - {BK_{2}}})}\phi{(x)}}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$. Then, the dynamics ([2.1](https://arxiv.org/html/2303.08431v5#S2.E1 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) become $x_{t + 1} = {{{({A - {BK_{1}}})}x_{t}} + {f{(x_{t})}}}$. Also, by definition of $\Omega$ in ([2.3](https://arxiv.org/html/2303.08431v5#S2.E3 "In 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

Apply \[(https://arxiv.org/html/2303.08431v5#bib.bib31), Lemma 4\] and then we finish the proof. ∎

We provide an upper bound on $\left\| P_{K_{1}} \right\|$ that will be used in the rest of this subsection.

### Lemma 6.7

Assume Assumption [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") holds. If $\left\| {K - K^{lin}} \right\|_{F} \leq \delta \leq 1$, we have

where $P_{K_{1}}$ is the solution to the Lyapunov equation ([4.7](https://arxiv.org/html/2303.08431v5#S4.E7 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Proof

By unrolling the Lyapunov equation ([4.7](https://arxiv.org/html/2303.08431v5#S4.E7 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we have

Since $\left\| {({A - {BK_{1}}})}^{t} \right\| \leq {c_{1}\rho_{1}^{t}}$ for some $c_{1} > 1$ and $\rho_{1} \in {}$, it follows

Moreover, by Assumption [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have ${\left\| Q \right\|,\left\| R \right\|} \leq 1$, leading to

Also, since $\left\| K^{lin} \right\|_{F} \leq \Gamma$ and $\left\| {K - K^{lin}} \right\|_{F} \leq \delta \leq 1$, we have

Finally, combining Eq. ([6.18](https://arxiv.org/html/2303.08431v5#S6.E18 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([6.19](https://arxiv.org/html/2303.08431v5#S6.E19 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), Eq. ([6.17](https://arxiv.org/html/2303.08431v5#S6.E17 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

which finishes the proof. ∎

The key property to guarantee the local strong convexity of the cost function $\mathcal{C}{( \cdot )}$ is the local Lipschitz continuity of ${\nabla G_{K}}{(x)}$. Recall $c = {2c_{1}}$ and $\rho = {{({\rho_{1} + 1})}/2}$.

### Lemma 6.8 (Local Lipschitz Continuity of ${\nabla G_{K}}{(x)}$)

Assume Assumptions [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") hold. When $\left\| {K - K^{lin}} \right\|_{F} \leq \delta$ and ${\left\| x \right\|,\left\| x^{\prime} \right\|} \leq {{({c_{1} + c_{2}})}cD_{0}}$, we have

where $L$ is defined as in Eq. ([4.12](https://arxiv.org/html/2303.08431v5#S4.E12 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")).

### Proof

By the definition of $G_{K}{(x)}$ in Eq. ([4.8](https://arxiv.org/html/2303.08431v5#S4.E8 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we first compute its gradient as follows

As such, for two states $x$ and $x^{\prime}$, we have

We compute the bounds one by one. Firstly, since $\left\| {x_{t} - x_{t}^{\prime}} \right\| \leq {c\left\| {x - x^{\prime}} \right\|}$ and $\phi$ is $\ell$-Lipschitz, we have

Thus, it suffices to establish a bound on $\left\| F_{K}^{21} \right\|$. Note

Since $K \in {\Lambda{(\delta)}} \subset \Omega$, we have $\left\| {A - {BK_{1}}} \right\| \leq c_{1}$ and $\left\| {C - {BK_{2}}} \right\| \leq c_{2}$. Also, by Lemma [6.7](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem7 "Lemma 6.7. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have $\left\| P_{K_{1}} \right\| \leq C_{P}$. Thus, Eq. ([6.23](https://arxiv.org/html/2303.08431v5#S6.E23 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

It follows from Eq. ([6.22](https://arxiv.org/html/2303.08431v5#S6.E22 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and the fact $c = {2c_{1}}$ that

Next, note that $\left\| {\pi_{K}{(x)}} \right\| \leq {{({\left\| K_{1} \right\| + {\ell\left\| K_{2} \right\|}})}\left\| x \right\|}$ and $\left\| {{\pi_{K}{(x)}} - {\pi_{K}{(x^{\prime})}}} \right\| \leq {\left( {\left\| K_{1} \right\| + {\ell\left\| K_{2} \right\|}} \right)\left\| {x - x^{\prime}} \right\|}$ for any $x$ and $x^{\prime}$. Then, it follow from Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") that

Furthermore, let $D$ be such that $\left\| x_{t} \right\| \leq {c\left\| x_{0} \right\|} \leq {{({c_{1} + c_{2}})}c^{2}D_{0}} ≕ D$. Since ${\left\| K_{1} \right\|\left\| K_{2} \right\|} \leq {\frac{1}{2}\left\| K \right\|_{F}^{2}}$ and by Lemma [6.12](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.12. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") that $\left\| {x_{t} - x_{t}^{\prime}} \right\| \leq {c\left\| {x - x^{\prime}} \right\|}$, Eq. ([6.25](https://arxiv.org/html/2303.08431v5#S6.E25 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

Moreover, note that

Recall that $\phi$ is $\ell$-Lipschitz and $\ell^{\prime}$-gradient-Lipschitz. Also, we have $\left\| P_{K_{1}} \right\| \leq C_{P}$ and $\left\| {C - {BK_{2}}} \right\| \leq c_{2}$. Based on these facts, by applying Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), Eq. ([6.26](https://arxiv.org/html/2303.08431v5#S6.E26 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) can be bounded as

Finally, by Lipschitz property of $\phi$ and $\pi_{K}$, we obtain

Plugging all these results into Eq. ([6.32](https://arxiv.org/html/2303.08431v5#S6.E32 "In Proof of Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), and using the facts that $\left\| \frac{\partial x_{t}}{\partial x} \right\| \leq {c\rho^{t}}$ and $\left\| {\frac{\partial x_{t}}{\partial x} - \frac{\partial x_{t}^{\prime}}{\partial x^{\prime}}} \right\| \leq {\frac{c_{2}\ell^{\prime}c^{3}}{1 - \rho}\rho^{t - 1}\left\| {x - x^{\prime}} \right\|}$, we conclude that

which shows that ${\nabla G_{K}}{(x)}$ is $L$-Lipschitz in $x$. ∎

The following result establishes a bound on the directional derivative of the state.

### Lemma 6.9

Assume Assumption [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") holds. The directional derivative of $x_{t}$ w.r.t. $K = {(K_{1},K_{2})}$ along the direction $\Delta = {(\Delta_{1},\Delta_{2})}$ satisfies

### Proof

Recall the dynamics are

We compute the directional of $x_{t + 1}$ derivative w.r.t $K = {(K_{1},K_{2})}$ along the direction $\Delta = {(\Delta_{1},\Delta_{2})}$:

Note that for $K \in \Omega$, we have $\left\| {A - {BK_{1}}} \right\|^{t} \leq {c_{1}\rho_{1}^{t}}$ for each $t \geq 0$ and $\left\| {C - {BK_{2}}} \right\| \leq c_{2}$. Also, the Lipschitz property of $\phi$ implies that $\left\| \frac{\partial{\phi{(x)}}}{\partial x} \right\| \leq \ell$ and $\left\| {\phi{(x)}} \right\| \leq {\ell\left\| x \right\|}$. Hence, taking the norm of both sides of Eq. ([6.28](https://arxiv.org/html/2303.08431v5#S6.E28 "In Proof. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) results in

Since $\left\| x_{k} \right\| \leq {c\rho^{k}\left\| x_{0} \right\|}$ by part (a) of Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), it follows

To prove Eq. ([6.27](https://arxiv.org/html/2303.08431v5#S6.E27 "In Lemma 6.9. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we assume that ${x_{t}^{\prime}{\lbrack\Delta\rbrack}} \leq {\alpha\rho^{t}}$,where $\alpha = \frac{2c_{1}c\left\| x_{0} \right\|\left\| B \right\|{({\left\| \Delta_{1} \right\| + {\ell\left\| \Delta_{2} \right\|}})}}{({\rho - \rho_{1}})}$. Consequently, we have

Since $\rho = {{({\rho_{1} + 1})}/2}$, one can see that $0 < {1 - {({\rho_{1}/\rho})}^{t + 1}} < 1$. Therefore, it holds from $\ell \leq \frac{1 - \rho_{1}}{4c_{1}c_{2}}$ that

By induction, we know that for each $t \geq 1$, it holds

Since $\ell \leq 1$, we have ${\left\| \Delta_{1} \right\| + {\ell\left\| \Delta_{2} \right\|}} \leq {\sqrt{2}\left\| \Delta \right\|}$. Additionally, by the definition of $c$ and $\rho$, we have $\frac{2c_{1}c}{\rho - \rho_{1}} = \frac{c^{2}}{1 - \rho}$. Consequently, we conclude that

where we have used the fact $\left\| B \right\| \leq \Gamma$.

With Lemma [6.9](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem9 "Lemma 6.9. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we establish the perturbation analysis of the covariance matrices $\Sigma_{K}^{\psi\psi}$ and $\Sigma_{K}^{G\psi}$ and provide an upper bound on $\left\| E_{K} \right\|$.

### Lemma 6.10

Assume Assumptions [4.1](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), [4.3](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem3 "Assumption 4.3. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [4.4](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem4 "Assumption 4.4. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") hold. For ${K,K^{\prime}} \in {\Lambda{(\delta)}}$, there exist constants $C_{E},C_{1}$ and $C_{2}$ defined as in Eq. ([4.18](https://arxiv.org/html/2303.08431v5#S4.E18 "In Proof of Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) such that

### Proof of Lemma [6.10](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem10 "Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

First, we prove $\left\| {\Sigma_{K^{\prime}}^{\psi\psi} - \Sigma_{K}^{\psi\psi}} \right\|_{F} \leq {C_{1}\left\| {K^{\prime} - K} \right\|_{F}}$. Note that the directional derivative of $\Sigma_{K}^{\psi\psi}$ w.r.t. $K$ along the direction $\Delta$ is

Taking the norm of both sides, since $\psi$ is $\ell_{\psi}$-Lipschitz, we obtain

Here, Eq. ([6.30](https://arxiv.org/html/2303.08431v5#S6.E30 "In Proof of Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) is a consequence of Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and [6.9](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem9 "Lemma 6.9. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Also, we have employed the facts that $\ell_{\psi} \leq \sqrt{2}$ and ${{\mathbb{E}}\left\lbrack \left\| x_{0} \right\| \right\rbrack} \leq D_{0}$ to derive Eq. ([6.31](https://arxiv.org/html/2303.08431v5#S6.E31 "In Proof of Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). Now, set ${g{(t)}} = \Sigma_{K + {t{({K^{\prime} - K})}}}^{\psi\psi}$. Then, its derivative in $t$ is ${g^{\prime}{(t)}} = {\left( \Sigma_{K + {t{({K^{\prime} - K})}}}^{\psi\psi} \right)^{\prime}{\lbrack{K^{\prime} - K}\rbrack}}$. Since Eq. ([6.31](https://arxiv.org/html/2303.08431v5#S6.E31 "In Proof of Lemma 6.10. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) holds for arbitrary $K$, we deduce

Next, we show $\left\| {{{\mathbb{E}}\left\lbrack {\sum_{t = 0}^{\infty}{{\nabla G_{K}}{(x_{t + 1})}{(x_{t})}^{\top}}} \right\rbrack} - {{\mathbb{E}}\left\lbrack {\sum_{t = 0}^{\infty}{{\nabla G_{K}}{(x_{t + 1}^{\prime})}{(x_{t}^{\prime})}^{\top}}} \right\rbrack}} \right\|_{F} \leq {C_{2}\left\| {K^{\prime} - K} \right\|_{F}}$. Since $\left\| x_{t} \right\| \leq {c\left\| x_{0} \right\|} \leq {cD_{0}}$, we apply Lemma [6.8](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem8 "Lemma 6.8 (Local Lipschitz Continuity of ∇{𝐺_𝐾}⁢(𝑥)). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") to obtain

Moreover, as a consequence of Lemma [6.9](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem9 "Lemma 6.9. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have $\left\| {x_{t} - x_{t^{\prime}}} \right\| \leq {\frac{\sqrt{2}c^{2}\Gamma}{1 - \rho}\rho^{t}\left\| x_{0} \right\|\left\| {K^{\prime} - K} \right\|}$ for any $t \geq 1$. Thus, together with the fact $\left\| x_{t} \right\| \leq {c\rho^{t}\left\| x_{0} \right\|}$, we have

From this, we conclude that

Finally, we establish the bound on $\left\| E_{K} \right\|$. Recall that $P_{K_{1}^{lin}}$ satisfies

From this, we observe that $E_{K^{lin}} = {{RK^{lin}} - {B^{\top}P_{K_{1}^{lin}}{({H - {BK^{lin}}})}}} = 0$. It follows from the definition of $E_{K}$ that

Recall that $\left\| P_{K_{1}^{lin}} \right\| \leq C_{P}$ by Lemma [6.7](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem7 "Lemma 6.7. ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). Also, observe that $\left\| {H - {BK}} \right\| \leq {\left\| {A - {BK_{1}}} \right\| + \left\| {C - {BK_{2}}} \right\|}$. Consequently, we have

The last result on $\Sigma_{K}^{\psi\psi}$ is useful in proving the $h$-smoothness of the cost function $\mathcal{C}{(K)}$. Recall $\Sigma_{K}^{\psi\psi} = {{\mathbb{E}}\left\lbrack {\sum_{t = 0}^{\infty}{\psi{(x_{t})}\psi{(x_{t})}^{\top}}} \right\rbrack}$.

### Lemma 6.11

Under the same conditions as in Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have

### Proof

Note $\left\| {\psi{(x)}} \right\| \leq {\ell_{\psi}\left\| x \right\|}$ by Lipschitz continuity. Also, by Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), $\left\| x_{t} \right\| \leq {c\rho^{t}\left\| x_{0} \right\|}$. Consequently, we have

Since $\ell_{\psi} \leq \sqrt{2}$ and $\left\| x_{0} \right\| \leq D_{0}$, we conclude that ${\left\| \Sigma_{K}^{\psi\psi} \right\| \leq {\frac{2c^{2}}{1 - \rho^{2}}D_{0}^{2}} \leq {\frac{2c^{2}}{1 - \rho}D_{0}^{2}}}.$

### Proof of Theorem [4.8](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem8 "Theorem 4.8. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")

In this section, we characterize the gradient estimation, a key step in establishing the convergence rate, in the following lemma.

### Lemma 6.12

Let $e_{grad} > 0$ and $\nu \in {}$ be given. Suppose $K \in {\Lambda{({{2\delta}/3})}}$. Under the same conditions as in Theorem [4.7](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem7 "Theorem 4.7. ‣ 4.2 Landscape and Convergence Analysis ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), when $r \leq {\min\left\{ \frac{\delta}{3},{\frac{1}{3h}e_{\text{grad}}} \right\}}$, $T \geq {\frac{1}{1 - \rho_{1}}{\log\frac{6\hat{D}C_{\text{max}}}{e_{\text{grad}}r}}}$, and

where $\hat{D} = {p{({n + d})}}$ and $C_{\max} = \frac{24{({1 + \Gamma})}^{2}c_{1}^{2}D_{0}^{2}}{1 - \rho_{1}}$, the following holds with probability at least $1 - \nu$,

### Proof

Let $\text{Ball}{(r)}$ be the uniform distribution over the ball with radius $r$ (in Frobenius norm) centered at the origin and $\text{Sphere}{(r)}$ be the uniform distribution over the sphere with radius $r$. Denote ${\mathcal{C}_{r}{(K)}} = {{\mathbb{E}}_{U \sim {\text{Ball}{(r)}}}\left\lbrack {\mathcal{C}{({K + U})}} \right\rbrack}$. By \[(https://arxiv.org/html/2303.08431v5#bib.bib13), Lemma 1\], we have

Define $\mathcal{C}_{j} = {\mathcal{C}{({K + U^{j}})}}$ with $U^{j} \sim {\text{Sphere}{(r)}}$. Recall $\hat{{\nabla\mathcal{C}}⁢{(K)}} = {\frac{1}{J}{\sum_{j = 1}^{J}{\frac{\hat{D}}{r^{2}}{\hat{\mathcal{C}}}_{j}U^{j}}}}$ defined in Algorithm (https://arxiv.org/html/2303.08431v5#alg1 "Algorithm 1 ‣ 2 Problem Setup ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"). We can decompose the gradient estimation error into three terms,

In the following, we will show that $e_{1} \leq {e_{grad}/3}$ almost surely, $e_{2} \leq {e_{grad}/3}$ with probability at least $1 - {\nu/2}$, and $e_{3} \leq {e_{grad}/3}$ with probability at least $1 - {\nu/2}$. Firstly, since $r \leq \frac{\delta}{3}$, we have ${K + U} \in {\Lambda{(\delta)}}$, in which the cost function $\mathcal{C}{( \cdot )}$ is $h$-smooth. By the definition of ${\nabla\mathcal{C}_{r}}{(K)}$, we can deduce with probability one,

where we have used that $r \leq {\frac{1}{3h}e_{\text{grad}}}$ to reach the last inequality.

Next, notice that $\left\{ {\frac{\hat{D}}{r^{2}}\mathcal{C}_{j}U^{j}} \right\}_{j = 1}^{J}$ are i.i.d. copies with expectation ${\nabla\mathcal{C}_{r}}{(K)}$. Since $\left\| U^{j} \right\| \leq r$, the $h$-smoothness of $\mathcal{C}{( \cdot )}$ implies with probability one,

Since ${\left\| {K + U^{j}} \right\|,\left\| K^{\ast} \right\|} \leq \delta$, we conclude that $\left\| {\frac{\hat{D}}{r^{2}}\mathcal{C}_{j}U^{j}} \right\|_{F} \leq {\frac{\hat{D}}{r}\left( {{\mathcal{C}{(K^{\ast})}} + {2h\delta^{2}}} \right)}$ almost surely. Furthermore, by the matrix Bernstein inequality \[(https://arxiv.org/html/2303.08431v5#bib.bib16), Theorem 12\], we have

where we have used the fact that $J \geq {\frac{36{\hat{D}}^{2}}{e_{\text{grad}}^{2}r^{2}}\left( {{\mathcal{C}{(K^{\ast})}} + {2h\delta^{2}}} \right)^{2}{\log\frac{4\hat{D}}{\nu}}}$ to derive the second inequality.

Finally, to upper bound $e_{3}$, we further decompose it into two parts. Defining ${\overset{\sim}{\mathcal{C}}}_{j} = {{\mathbb{E}}\left\lbrack {\sum_{t = 0}^{T}\left( {{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}} \right)} \right\rbrack}$ with $u_{t} = {- {{({K + U^{j}})}\psi{(x_{t})}}}$, we have the following inequality

To bound $e_{4}$, note that with probability one,

where we have used the $\ell_{\psi}$-Lipschitz property of $\psi$. Since ${K + U^{j}} \in {\Lambda{(\delta)}}$, we have $\left\| {K + U^{j}} \right\| \leq {1 + \Gamma}$. Also, by Lemma [6.6](https://arxiv.org/html/2303.08431v5#S6.ThmTheorem6 "Lemma 6.6 (Stability of the Trajectory {𝑥_𝑡}). ‣ 6.2 Proof of Theorem 4.7 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") and Assumption [4.5](https://arxiv.org/html/2303.08431v5#S4.ThmTheorem5 "Assumption 4.5. ‣ 4 Main Results ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), we have $\left\| x_{t} \right\| \leq {c\rho^{t}\left\| x_{0} \right\|} \leq {c\rho^{t}D_{0}}$ almost surely. Consequently, by using the facts $\left\| Q \right\| \leq 1$ and $\ell_{\psi} \leq \sqrt{2}$, Eq. ([6.35](https://arxiv.org/html/2303.08431v5#S6.E35 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) becomes

As such, since $\left. {\mathbb{E}}\left\lbrack {\hat{\mathcal{C}}}_{j}U^{j} - {\overset{\sim}{\mathcal{C}}}_{j}U^{j} \right|U^{j} \right\rbrack = 0$, by the matrix Bernstein inequality, it holds

where we have used the fact that $J \geq {\frac{144{\hat{D}}^{2}C_{\text{max}}^{2}}{e_{\text{grad}}^{2}r^{2}}{\log\frac{4\hat{D}}{\nu}}}$ in the ultimate inequality. Moreover, since $\psi{( \cdot )}$ is $\ell_{\psi}$-Lipschitz and $\left\| x_{t} \right\| \leq {c\rho^{t}\left\| x_{0} \right\|}$, we notice that

where the final inequality follows from Eq. ([6.36](https://arxiv.org/html/2303.08431v5#S6.E36 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). As such, almost surely we have

where we have used the fact that $T \geq {\frac{1}{1 - \rho_{1}}{\log\frac{6\hat{D}C_{\text{max}}}{e_{\text{grad}}r}}}$ to obtain the final inequality. Hence, combining Eq. ([6.37](https://arxiv.org/html/2303.08431v5#S6.E37 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([6.38](https://arxiv.org/html/2303.08431v5#S6.E38 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")), we conclude $e_{3} \leq {\frac{1}{3}e_{\text{grad}}}$ with probability at least $1 - \frac{\nu}{2}$, which completes the proof of Lemma [6.12](https://arxiv.org/html/2303.08431v5#S6. "Lemma 6.12. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators") together with Eq.([6.33](https://arxiv.org/html/2303.08431v5#S6.E33 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")) and ([6.34](https://arxiv.org/html/2303.08431v5#S6.E34 "In Proof. ‣ 6.3 Proof of Theorem 4.8 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators")). ∎

## Conclusions

We consider a nonlinear optimal control problem, characterize the local strong convexity of the cost function, and prove that the globally optimal solution is close to a carefully chosen initialization. Additionally, we design a zeroth-order policy gradient algorithm and establish a convergence result under the proposed policy initialization scheme for the nonlinear control problem. We hope these results would shed light on the efficiency of policy gradient methods for nonlinear optimal control problems when the underlying models are unknown to the decision maker. Future work includes investigating learning problems for highly nonlinear systems and extending the analysis of quadratic cost functions to more general cost functions.
