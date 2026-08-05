<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The connection between control algorithms for Markov decision processes and optimization algorithms has been implicitly and explicitly exploited since the introduction of dynamic programming algorithm by Bellman in the 1950s. Recently, this connection has attracted a lot of attention for developing new control algorithms inspired by well-established optimization algorithms. In this paper, we make this analogy explicit across four problem classes with a unified solution characterization. This novel framework, in turn, allows for a systematic transformation of algorithms from one domain to the other. In particular, we identify equivalent optimization and control algorithms that have already been pointed out in the existing literature, but mostly in a scattered way. We also discuss the issues arising in providing theoretical convergence guarantees for these new control algorithms and provide simple yet effective techniques to solve them. The provided framework and techniques then lay out a concrete methodology for developing new convergent control algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Markov decision processes (MDPs) have become a standard mathematical framework for the formulation of stochastic optimal control problems, that is, the problem of dynamic decision-making under uncertainty. This popularity can be to a large extent attributed to the Bellman principle of optimality and the dynamic programming algorithm. In particular, the fixed-point characterization of the optimal value function of an MDP has led to the development of a large class of iterative value-based algorithms, such as value iteration and policy iteration. This fixed-point characterization has also been used for identifying the fundamental connection between algorithms for optimal control of MDPs and those for optimization. A classic example is the policy iteration algorithm for MDPs which is an instance of the Newton method. Recently, the connection between optimization and control problems has attracted a lot of attention for developing new control algorithms, with faster convergence and/or lower complexity, inspired by their counterparts for solving optimization problems. For instance, the modifications to the value iteration algorithm in and the Q-learning algorithm in are inspired by momentum-based acceleration in optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The implicit connection between optimization algorithms and control algorithms for MDPs with a finite state-action space has also been studied more systematically. In, the authors look at the connection between *constrained* convex optimization algorithms and control algorithms such as Frank-Wolfe algorithm and conservative policy iteration. A detailed comparison between *deterministic* optimization algorithms and *model-based*^11^1In this paper, the terminologies of "model-free" and "model-based" indicate the available information (oracle), i.e., whether we have access to the model or only the system trajectory (samples); see Section 2.2 for more details. We note that this is different from the common terminologies in the RL literature where these terms refer to the solution approach, i.e., whether we identify the model along the way (model-based RL) or directly solve the Bellman equation to find the value function (model-free RL). control algorithm is also provided, where the author looks at a wide range of optimization algorithms including gradient descent, accelerated gradient descent, Newton method, and quasi-Newton method and their counterparts for solving control problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these observations, this study provides an explicit framework unifying the tight link between optimization (stochastic and deterministic, respectively) and optimal control (model-based dynamic programming and model-free reinforcement learning, respectively). Specifically, this goal is achieved by exploiting the (expected) root-finding characterization of optimization problems and the (expected) fixed-point characterization of control problems. The framework yields an explicit transformation of deterministic (stochastic) convex optimization problems to model-based (model-free) control problems, and vice versa (Section 2, Table 1). This explicit relationship, in turn, allows for a systematic transformation of algorithms from one domain to the other, which we will use to identify existing (and mostly known) equivalent algorithms for optimization and control (Section 3, Table 2). Unfortunately, the common formulation for control and optimization algorithms does not allow us to borrow existing theoretical results from one field to another. Indeed, the similarity in the update rule does not carry over to the analysis, particularly when it comes to the convergence of these algorithms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, we also examine general tools for the convergence analysis of control algorithms, as well as some simple yet effective remedies for ensuring the convergence of novel control algorithms (Section 4, Theorems 4.1. ‣ 4.1. Model-based algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective"), 4.2. ‣ 4.1. Model-based algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective"), 4.3. ‣ 4.2. Model-free algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective")). The provided framework and techniques then lay out a concrete methodology for developing new algorithms in one domain based on the existing algorithms in the other, along with theoretical convergence guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we restrict attention to control algorithms for *finite* state--action MDPs. For infinite (continuous) state--action spaces, aside from special cases like linear--quadratic regulators (LQR), practical computation typically requires finite-dimensional approximations. One approach is to approximate at the model level by aggregating (discretizing) the state and action spaces, thereby reducing the problem to a finite MDP. Another approach is to approximate the value function directly with a finite parameterization by minimizing (a proxy for) the residual of its Bellman fixed-point equation. Examples include linear parameterizations, nonlinear parameterizations using neural networks, and max-plus methods. There is also an alternative formulation in which the target function solves an infinite-dimensional linear program, enabling approximation via finite, tractable convex programs. Viewed this way, most of these approximation strategies can be framed as solving a finite-dimensional fixed-point problem or a convex optimization problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. For a vector $v\in\mathbb{R}^{n}$, we use $v(i)$ and $[v](i)$ to denote its $i$-th element. Similarly, $M(i,j)$ and $[M](i,j)$ denote the element in row $i$ and column $j$ of the matrix $M\in\mathbb{R}^{m\times n}$. We use $\cdot^{\top}$ to denote the transpose of a vector/matrix. $\left\|\cdot\right\|_{2}$ and $\left\|\cdot\right\|_{\infty}$ denote the 2-norm and $\infty$-norm of a vector, respectively. $\left\|\cdot\right\|_{2}$ and $\left\|\cdot\right\|_{F}$ denote the induced 2-norm and the Frobenius norm of a matrix, respectively. The identity operator is denoted by $\operatorname{Id}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use $\bm{1}$ and $I$ to denote the all-ones vector and the identity matrix, respectively. We denote the $i$-th unit vector by $e_{i}$, that is, the vector with its $i$-th element equal to $1$ and all other elements equal to $0$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problems: Optimization vs. Control", "weight": 1.0} -->

In this section, we provide the generic framework that connects optimization problems to control problems. In particular, we provide the explicit transformations between different variables and operations in these problems. Table 1 provides a condensed summary of this framework.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problems: Optimization vs. Control", "weight": 1.0} -->

s+ ∼ ℙ(⋅|s, a) Available oracle/information T(v) (Prob. kernel ℙ, Cost c) Table 1. Equivalence transformations. See Section 2 for details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

We first look at the root-finding characterization of the solution to convex optimization problems. Consider the minimization problem where $\widehat{f}:\mathbb{R}^{\ell}\times\Xi\to\mathbb{R}$ is a sample-wise function and $\xi$ is random vector with a fixed probability distribution $\mathds{P}$ over $\Xi$. We assume that the resulting function $f:\mathbb{R}^{\ell}\to\mathbb{R}$ is twice continuously differentiable and strongly convex. Much like the control problem, this problem can be considered in two settings: Deterministic optimization: Assume that $\mathds{P}$ in is known and that the corresponding expectation can be computed. The unique minimizer $x^{\star}$ is the root of the gradient operator, i.e., Stochastic optimization: Now assume that $\mathds{P}$ in is unknown but can be sampled.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

In this case, the minimizer $x^{\star}$ satisfies the expected root-finding problem where $\nabla$ now denotes the partial derivative w.r.t. $x$. We note that, above, there is an underlying assumption that the differentiation w.r.t. $x$ and expectation w.r.t. $\xi$ can be operated in any order.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Control problem", "weight": 1.0} -->

The standard modeling framework for stochastic optimal control problems is the *Markov decision process* (MDP).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Control problem", "weight": 1.0} -->

An MDP is characterized by the tuple $(\mathcal{S},\mathcal{A},\mathds{P},c,\gamma)$, where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $\mathds{P}$ is the transition probability kernel such that $\mathds{P}(s^{+}|s,a)$ is the probability of the transition to state $s^{+}$ given that the system is in state $s$ and the chosen control is $a$ for each $(s,a,s^{+})\in\mathcal{S}\times\mathcal{A}\times\mathcal{S}$, $c\in\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ is the stage cost function such that $c(s,a)$ is the cost of taking the control action $a$ while the system is in state $s$, and, $\gamma\in$ is the discount factor acting as a

<!-- chunk {"id": "body-0016", "role": "body", "section": "Control problem", "weight": 1.0} -->

trade-off between short- and long-term costs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Control problem", "weight": 1.0} -->

Let us now fix a *control policy* $\pi:\mathcal{S}\rightarrow\mathcal{A}$, i.e., a mapping from states to actions. The stage cost of the policy $\pi$ is denoted by $c^{\pi}\in\mathbb{R}^{\mathcal{S}}$, where $c^{\pi}(s)\coloneqq c\big(s,\pi(s)\big)$ for $s\in\mathcal{S}$. The transition probability kernel of the resulting Markov chain under the policy $\pi$ is denoted by $\mathds{P}^{\pi}$, where $\mathds{P}^{\pi}(s^{+}|s)=\mathds{P}\big(s^{+}|s,\pi(s)\big)$ for $s,s^{+}\in\mathcal{S}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Control problem", "weight": 1.0} -->

We also define $P^{\pi}\in^{\mathcal{S}\times\mathcal{S}}$, with $P^{\pi}(s,s^{+})\coloneqq\mathds{P}^{\pi}(s^{+}|s)$ for each $(s,s^{+})\in\mathcal{S}\times\mathcal{S}$, to be the corresponding transition probability *matrix*. The value $v^{\pi}\in\mathbb{R}^{\mathcal{S}}$ of the policy $\pi$ is then the expected, discounted, accumulative cost of following this policy over an infinite-horizon trajectory, that is, Let us also define the *action-value function* (a.k.a.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Control problem", "weight": 1.0} -->

the *Q-function*) $q^{\pi}\in\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ for the policy $\pi$ by so that $v^{\pi}(s)=q^{\pi}\big(s,\pi(s)\big)$ for each $s\in\mathcal{S}$. Given a value function $v\in\mathbb{R}^{\mathcal{S}}$, let us also define the *greedy policy $\pi_{v}:\mathcal{S}\rightarrow\mathcal{A}$ w.r.t. $v$* denoted and given by Similarly, for a Q-function $q\in\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$, we define the *greedy policy $\pi_{q}:\mathcal{S}\rightarrow\mathcal{A}$ w.r.t.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Control problem", "weight": 1.0} -->

$q$* by The problem of interest is to control the MDP optimally, that is, to find an optimal policy $\pi^{*}$ with the optimal (action-)value functions so that the expected, discounted, infinite-horizon cost is minimized. Let us also note that the optimal policy, that is a minimizer of the preceding optimization problems, is greedy w.r.t. $v^{\star}$ and $q^{\star}$, i.e., $\pi^{\star}=\pi_{v^{\star}}=\pi_{q^{\star}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Control problem", "weight": 1.0} -->

Interestingly, the optimal (action-)value functions introduced in can be equivalently characterized as the fixed-point of two different operators each of which is useful depending on the available information (oracle): Model-based control: When we have access to the transition kernel and the cost function, the problem is usually characterized by the fixed-point problem. Indeed, defining the *Bellman optimality operator* $T:\mathbb{R}^{\mathcal{S}}\rightarrow\mathbb{R}^{\mathcal{S}}$ by or, equivalently, $v^{\star}=T(v^{\star})$, that is, the optimal value function $v^{\star}$ is the *unique* fixed-point of $T$. The uniqueness follows from the fact that the operator $T$ is a $\gamma$-contraction in $\infty$-norm. Observe that, in this case, $T$ can be exactly computed given the model of the underlying MDP.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Control problem", "weight": 1.0} -->

Model-free control: In real applications, the model is often unknown, and instead, one can generate samples. Examples of this are very large systems where identifying the model is prohibitively expensive but transitions between states can be observed and recorded, such as those in video games. This problem has been studied extensively in the reinforcement learning community and is often formulated as the *expected* fixed-point problem. To provide this characterization, let us define the *vector of sampled next states* $\varsigma^{+}\in\mathcal{S}^{\mathcal{S}\times\mathcal{A}}$ where is a sample of the next state drawn from the distribution $\mathds{P}(\cdot|s,a)$ for each $(s,a)\in\mathcal{S}\times\mathcal{A}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Control problem", "weight": 1.0} -->

Then, defining the *sampled* Bellman optimality operator $\widehat{T}:\mathbb{R}^{\mathcal{S}\times\mathcal{A}}\times\mathcal{S}^{\mathcal{S}\times\mathcal{A}}\rightarrow\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ by^22^2Strictly speaking, the provided sampled Bellman optimality operator is the empirical version of the Bellman optimality operator for the Q-function, given by $[\bar{T}(q)](s,a)\coloneqq c(s,a)+\gamma\mathds{E}_{s^{+}}\left[\min_{a^{+}\in\mathcal{A}}q(s^{+},a^{+})\mid(s,a)\right]$ for each $(s,a)\in\mathcal{S}\times\mathcal{A}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Transformation", "weight": 1.0} -->

In what follows, we focus on *tabular MDPs with a finite state-action space*. We thus consider $\mathcal{S}=\{1,2,\ldots,n\}$ and $\mathcal{A}=\{1,2,\ldots,m\}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Transformation", "weight": 1.0} -->

and $\varsigma^{+}\in\mathcal{S}^{\mathcal{S}\times\mathcal{A}}$ is the vector of sampled next states defined in (6 ‣ 2.2. Control problem ‣ 2. Problems: Optimization vs. Control ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective")).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Transformation", "weight": 1.0} -->

Before providing the equivalence relations between optimization and control problems, let us provide an important result for the Bellman optimality operator.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

We now look at existing algorithms for optimization and control and their equivalence within the proposed framework. We start with the well-known baseline first-order and second-order algorithms and show how the application of the proposed transformations to well-established optimization algorithms, such as gradient descent and Newton method, leads to well-known control algorithms such as value iteration and policy iteration. We then cover a wide range of modifications to optimization algorithms, from momentum to spectral decomposition of the Hessian, and their counterpart control algorithms. We note that most of these equivalences have already been pointed out in the existing literature, however, mostly in a scattered way. An exception is, which studies the relation between *deterministic* optimization algorithms and *model-based* control algorithms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

To ease the exposition, we unify iterative algorithms by where $y_{k}=x_{k}$, $v_{k}$ or $q_{k}$ based on the context. In all considered settings, $d_{k}$ represents the update vector between iterations $k$ and $k+1$. This form allows us to characterize algorithms in terms of $d_{k}$. Moreover, we use Greek letters $\alpha_{k},\beta_{k},\ldots$ as scalar coefficients (e.g., step-size, learning rate, etc.) in the update vectors. We note that the specific values of these parameters may differ between equivalent algorithms. A compact summary of this can be found in Table 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

Some remarks are in order regarding the following equivalence relationships. First, the following list of algorithms is not meant to be an exhaustive review of the literature. Instead, our aim is to provide illustrative examples of the application of transformations of Table 1 in identifying equivalent algorithms for optimization and control. Second, the provided update rules for the cited algorithms, although covering the main characteristic of interest, are occasionally not exact. This is particularly the case in stochastic/model-free settings where other techniques, such as batch estimation or variance reduction, are also used in the original algorithms. Finally, the equivalence between optimization and control algorithms does not imply that these algorithms enjoy similar theoretical guarantees, particularly when it comes to convergence. We will discuss this issue in more detail in Section 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

We start our discussion with the vanilla first-order and second-order algorithms.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Vanilla first-order methods. The celebrated *Gradient Descent (GD)* method is characterized by where $\alpha_{k}$ is a properly chosen step-size. Applying the transformations of Table 1 to GD, we derive the so-called *Relaxed Value Iteration (Rel-VI)* with for model-based control. In particular, for the constant step-size $\alpha_{k}=1$, we have the standard VI algorithm $v_{k+1}=T(v_{k})$. Correspondingly, *Stochastic GD (SGD)* is characterized by Under the transformations of Table 1, SGD leads to the *synchronous* *Q-Learning (QL)* algorithm with^44^4This is the so-called *synchronous* update of the Q-function in *all* state-action pairs in each iteration, corresponding to the *parallel sampling model* introduced.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Vanilla second-order methods. In second-order algorithms, $d_{k}$ is specified by both the gradient and the Hessian oracles. The *damped* *Newton Method (NM)* is one such algorithm with The *pure* Newton step with $\alpha_{k}=1$ has a *local* quadratic convergence if, in addition to $f$ being strongly convex, the Hessian is Lipschitz-continuous \[23, Thm. 5.3\]. Globally, however, the pure Newton method can lead to divergence. This is the reason behind introducing the step-size $\alpha_{k}<1$ in the damped version which can be used to guarantee a global linear convergence. We can use the transformations of Table 1 in order to transform the Newton method into a model-based control algorithm with where $P(v_{k})$ is the transition probability matrix of the Markov chain under the greedy policy w.r.t. $v_{k}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

The derived model-based control algorithm then corresponds to the well-known *Policy Iteration (PI)* algorithm with $v_{k+1}=\big(I-\gamma P(v_{k})\big)^{-1}c^{\pi_{v_{k}}}$, where $c^{\pi_{v_{k}}}$ is the vector of stage costs corresponding to the greedy policy $\pi_{v_{k}}$ w.r.t. $v_{k}$. Indeed, the PI algorithm is equivalent to the semi-smooth Newton method with a local quadratic convergence rate.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

In the model-free case, the stochastic version of the Newton method has been a source of inspiration for developing second-order-type Q-learning algorithms. In particular, the *Stochastic Newton-Raphson (SNR)* algorithm with was used for developing the *Zap QL (ZQL)* algorithm with where $\pi_{k}(s^{+}_{k})\in\operatorname*{\arg\!\min}_{a\in\mathcal{A}}q_{k}(s^{+}_{k},a)$ is a greedy action w.r.t. $q_{k}$ evaluated at the sampled next state $\varsigma^{+}_{k}(s_{k},a_{k})=s^{+}_{k}\sim\mathds{P}(\cdot|s_{k},a_{k})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Note that the preceding algorithm involves updating one entry of the action-value function $q_{k}$ at each iteration $k$, corresponding to the state-action pair $(s_{k},a_{k})$ chosen at iteration $k$ -- recall that $e_{(s,a)}\in\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ is the unit vector corresponding to the state-action pair $(s,a)$. Moreover, ZQL in implements an eligibility trace with a decaying factor which we omit (i.e., set to $0$) for simplicity of the representation. The implementation of zap QL algorithm with *synchronous* update of the Q-function in all state-action pairs in each iteration is then characterized by where $\widehat{P}(q,\varsigma^{+})$ is the synchronously sampled state-action transition probability matrix of the Markov chain under the greedy policy w.r.t. $q$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Note that is exactly the SNR algorithm under the transformations of Table 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

We now focus on classic acceleration techniques such as momentum and anchoring in optimization. These techniques have recently attracted a lot of attention in developing control algorithms with improved convergence and complexity properties. We also look at a classic control engineering approach, namely, proportional-integral-derivative (PID) control, and its application in optimization and control algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Momentum methods. In the so-called momentum-based algorithms, the update vector $d_{k}$ is specified by gradient oracles but also depends on $d_{k-1}$. One such algorithm is *GD with Polyak Momentum (Mom-GD)*, a.k.a. heavy ball method, characterized by Another well-known momentum-based algorithm is *GD with Nesterov Acceleration (Acc-GD)* \[79")\] with update vector With a proper choice of the step-sizes $\alpha_{k}$ and $\beta_{k}$, these schemes can be shown to accelerate the convergence rate, compared to the standard GD, for particular classes of objective functions. The corresponding model-based control algorithms, using the transformations of Table 1, are *Momentum VI (Mom-VI)* with and *Accelerated VI (Acc-VI)* with However, the convergence of the preceding accelerated schemes is in general not guaranteed. In, the authors address this issue by *safeguarding*, i.e., combining the accelerated VI with the standard VI; see Section 4 for more details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For accelerating SGD, a direct combination of Polyak momentum or Nesterov acceleration with SGD has been shown to lead to no better (and even worse) performance in terms of convergence rate. At least for almost sure convergence, reports the same rate of convergence for SGD with Polyak momentum and SGD with Nesterov acceleration as for standard SGD. Nevertheless, modifications of momentum-based acceleration methods have led to a range of accelerated SGD algorithms with faster convergence rates with specific assumptions on the problem data. The idea of using momentum for accelerating QL has also attracted some interest. In particular, applying the transformations of Table 1 on a generic *Momentum SGD (Mom-SGD)* with and step-sizes $\alpha_{k},\beta_{k},\delta_{k}$, we obtain the *Speedy QL (SQL)*, *Nesterov Stochastic Approximation (NeSA)*, and *Momentum QL (Mom-QL)* algorithms with The difference between these three algorithms is in the choice of the step-sizes $\alpha_{k},\beta_{k},\delta_{k}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For example, by setting $\beta_{k}=\delta_{k}=(1-2\alpha_{k})=(k-1)/(k+1)$, we recover SQL.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Anchoring & Halpern iteration. Halpern iteration is an acceleration scheme originally developed for fixed-point iterations involving *non-expansive* maps. In particular, it modifies the updates by gradually pulling the iterates toward a reference point, a.k.a. *anchor*. In the case of deterministic optimization, modifying the standard GD using Halpern iteration, we derive the *Anchored GD (Anc-GD)* where $x\in\mathbb{R}^{n}$ is the anchor, $\beta_{k}\in$ is a properly chosen decaying step-size, and $\delta_{k}$ is the step-size corresponding to the standard GD update. The canonical choices for the anchor and the step-size are $x=x_{0}$ and $\beta_{k}=\tfrac{1}{k+2}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Using our standard characterization, Anc-GD (with the anchor $x=x_{0}$) corresponds to the update vector where $\alpha_{k}=\delta_{k}(1-\beta_{k})$. Under certain conditions on the objective function $f$ and the step-sizes $\alpha_{k}$ and $\beta_{k}$, Anc-GD improves the rate of convergence compared to standard GD. Indeed, Anc-GD can be shown to be equivalent to Nesterov acceleration with a correction term. However, when the operation corresponding to standard GD is a *contraction*, the modification via anchoring in Anc-GD does *not* improve the convergence rate. The corresponding model-based control algorithm is *Anchored VI (Anc-VI)* defined by the update vector where $\alpha_{k}=(1-\beta_{k})$. A similar, undesired situation arises for Anc-VI algorithm.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Since the Bellman operator is a contraction, there is no improvement in the convergence rate for $\gamma<1$ and the iterates of Anc-VI converge to the optimal value function $v^{\star}$ linearly with rate $\gamma$ (i.e., similar to standard VI). However, of importance is the polynomial (i.e., with rate $\mathcal{O}(1/k)$) convergence of the Bellman residual $\|v_{k}-T(v_{k})\|_{\infty}$ to zero in the *long-horizon* setting with $\gamma\rightarrow 1$ \[65, Thm. 2\]. In particular, even in the *undiscounted* setting (i.e., $\gamma=1$), the Bellman residual in Anc-VI converges to zero with rate $\mathcal{O}(1/k)$, assuming the corresponding undiscounted Bellman operator has a fixed point \[65, Thm. 3\].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

As a result, in long-horizon and undiscounted settings, Anc-VI maintains robust convergence guarantees, while the geometric rate of standard VI deteriorates.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

The corresponding *Stochastic Halpern Iteration (SHI)*, characterized by with step-sizes $\alpha_{k},\beta_{k}$, has been recently studied extensively in the stochastic optimization setting. In particular, under certain conditions and in combination with other techniques such as variance reduction and restarting, anchoring leads to improved sample complexity. Moreover, anchoring has been shown to be instrumental in providing guarantees for the last iterate, as opposed to a weighted average of iterates, under relaxed bounded-variance assumptions. Applying the transformations of Table 1 on SHI, we derive the *Halpern QL (HQL)* and *Stochastic Anchored Value Iteration for Discounted MDPs (SAVID)* algorithms with where $\alpha_{k}=1-\beta_{k}$. To be precise, HQL uses batch estimation with multiple samples for the sampled Bellman operation in this update rule to reduce the variance, while SAVID incorporates the recursive sampling technique to reduce the sample complexity.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Of importance is again that both HQL and SAVID algorithms (with minor modifications) can also be used in the *averaged cost* setting in which the corresponding Bellman optimality operator is non-expansive but *not* contractive.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

PID control. An alternative to standard acceleration methods is to use proportional-integral-derivative (PID) controllers for designing the update rule. This is a well-established technique in automatic control for set-point tracking. The basic idea is to treat the iterates $x_{k}$ as the "state" of the system and define the "error" signal in terms of the gradient $\nabla f(x_{k})$ and possibly the finite difference of the state, i.e., $d_{k}$. This idea has recently been explored in training deep networks. In particular, the *full batch* version of the *PID Optimizer (PID-Opt)* algorithm is a deterministic optimization algorithm characterized by where $\alpha_{k}$ is the step-size and $\beta_{k}$ is the decay coefficient in the integral term.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

The corresponding model-based control algorithm is *PID accelerated VI (PID-VI)* with Above, we see all three terms of the PID controller with the corresponding parameters $\kappa^{P}_{k},\ \kappa^{I}_{k},\ \kappa^{D}_{k}$. In particular, observe that, compared to PID-Opt, PID-VI uses the finite difference of the state (i.e., $d_{k-1}$) as opposed to the finite difference of the gradient (i.e., $d^{\prime}_{k-1}=\nabla f(x_{k})-\nabla f(x_{k-1})$) in its derivative term. Moreover the authors provide an adaptive scheme for tuning the PID parameters. The close connection between the PID acceleration schemes above and the momentum-based algorithms can be readily seen in their update rules. Indeed, PID-Opt and PID-VI provided above can recover standard momentum-based algorithms for specific values of the PID parameters.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For instance, Acc-GD can be derived by removing the derivative term in PID-Opt (i.e., setting $\kappa^{D}_{k}=0$). Similarly, Mom-VI is an instance of PID-VI without the integral term (i.e., with $\kappa^{I}_{k}=0$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For stochastic optimization, we can use the *mini-batch* version of PID-Opt, characterized by where the stochastic gradient operation is evaluated using a mini-batch of samples. In particular, observe that the derivative term also includes averaging to reduce the effect of noise in gradient evaluations. The corresponding model-free control algorithm is *PID accelerated QL (PID-QL)* with In particular, observe that PID-QL also uses a stochastic approximation $q^{\prime}_{k-1}$ of $q_{k-1}$ in forming the derivative term based on the finite difference of the state $q_{k}$. Moreover, a scheme similar to that used in PID-VI is used to tune the PID parameters in PID-QL adaptively. We also note that PID-QL can recover Mom-QL and SQL in by setting the PID parameters accordingly.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Finally, while the empirical results reported for PID-Opt, PID-VI, and PID-QL show a significant improvement in the convergence rate compared to the corresponding standard methods, theoretical guarantees for the convergence of these algorithms are still lacking.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Quasi-Newton methods (QNMs) are a class of methods that allow for a trade-off between computational complexity and (local) convergence rate in solving optimization problems. To do so, these methods use a Newton-type update vector where $\widetilde{H}_{k}$ (or $\widetilde{H}_{k}^{-1}$) is a computationally efficient approximation of the true Hessian $\nabla^{2}f(x_{k})$ (or its inverse) at iteration $k$. Different QNMs use different approximations of the Hessian or its inverse. Some "classical" examples of QNMs include Broyden approximation, Power symmetric Broyden approximation, Davidon-Fletcher-Powell approximation. All of these examples approximate the Hessian (or its inverse) as the "closest" matrix to a prior matrix within an affine set defined by (multi-)secant constraints (and possibly other structural constraints such as symmetry, sparsity, etc.). Under certain conditions, these methods lead to a local *superlinear* rate of convergence.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Not surprisingly, different types of QNMs have been (directly or with some modifications) employed in solving model-based and model-free control problems. Some recent examples include the Sketched Newton VI and Quasi-PI algorithms. In what follows, we focus on two illustrative examples, namely, Anderson mixing and spectral preconditioning.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Anderson mixing. Anderson mixing, originally developed as an acceleration scheme for fixed-point iterations, provides an update rule in which the next iterate is constructed as a linear combination of a finite number of most recent iterates and their images. In particular, *Anderson Accelerated GD (AA-GD)*, with memory $m\geq 0$ and $m_{k}=\min\{k,m\}$, is characterized by the update vector where $\bm{1}$ is the all-ones vector, $\alpha_{k}$ is a properly chosen step-size, and $G_{k}$ is assumed to be of full column rank (otherwise, we need to either use the pseudo-inverse or some form of regularization). Observe that for $m=0$, we recover the standard GD. Applying the transformations of Table 1, we derive the *Anderson Accelerated VI (AA-VI)* with where $\alpha_{k}=1$ and $G_{k}$ is assumed to be of full column rank. The preceding update rules correspond to the so-called *type-II* Anderson mixing.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

To be precise, the update vector of AA-GD/VI admits a QNM characterization of the form $d_{k}=-D_{k}g(y_{k})$, where $D_{k}$ is an approximation of the *inverse* of the Hessian, i.e., $H_{k}^{-1}$. In, the authors consider the *type-I* Anderson mixing scheme in combination with GD/VI in which the update vector is of the form $d_{k}=-D_{k}^{-1}g(y_{k})$ with $D_{k}$ being an approximation of the Hessian $H_{k}$. We note that the combination of Anderson mixing (type-I or type-II) with VI also lacks convergence guarantees. In, this issue is again addressed via *safeguarding*.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Anderson mixing has also been used in the stochastic optimization setting. In particular the authors use (type-II) Anderson mixing to develop the *Stochastic Anderson Mixing (SAM)* algorithm with update vector where $\alpha_{k},\beta_{k}$ are properly chosen step-sizes and $R_{k}=\delta_{k}(D^{x}_{k})^{\top}D^{x}_{k}$, with an adaptive coefficient $\delta_{k}$, acts as a *regularizer*. To be precise, SAM uses a batch of samples for estimation of the stochastic gradient operator. Note that the formulation above aligns with the QNM characterization of Anderson mixing.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

The corresponding model-free control algorithm is *QL with Stable Anderson Acceleration (SAA-QL)* with where $\alpha_{k}=1$ and $R_{k}=\delta_{k}(\|D^{q}_{k}\|_{F}^{2}+\|D^{g}_{k}\|_{F}^{2})I$ as the regularizer. To be precise, SAA-QL in utilizes a *smoothed* version of the Bellman optimality operator based on the *mellow-max* operator; see Section 4.2 for more details. Moreover the proposed SAA is integrated within the Dueling Deep Q-Network (Duel-DQN) algorithm for *continuous-state* model-free control. In particular, the SAA-Duel-DQN algorithm stores the last $m_{k}$ target networks (i.e., their parameters) and uses for computing the target values in each iteration. Finally, let us note that several works have incorporated the original form of the Anderson mixing similar to for model-free control; see, e.g.,.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Spectral preconditioning. This class of QNMs involves another computationally efficient approximation of the Hessian. To be precise, they use an approximation of the form where $U_{k},W_{k}\in\mathbb{R}^{\ell\times r}$ are tall matrices with $r\ll\ell$. Such approximations readily allow for application of the Woodbury matrix identity for computing $\widetilde{H}_{k}^{-1}$ with a low computational cost. In spectral preconditioning techniques, the matrices $U_{k}$ and $W_{k}$ are particularly formed based on the spectral decomposition of the true Hessian.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

For instance, *GD with Spectral Preconditioning (SP-GD)* is characterized by with $\alpha_{k}$ being a properly chosen regularizer parameter, $(\lambda_{k,i})_{i=1}^{r}$ the largest eigenvalues of the Hessian $\nabla^{2}f(x_{k})$ and $(u_{k,i})_{i=1}^{r}$ the corresponding eigenvectors. For model-based control, we can mention the recently developed *Rank-One Modified VI (R1-VI)* with where $w_{k}$ is the stationary distribution estimate of the Markov chain induced by the greedy policy w.r.t. $v_{k}$. The preceding update rule particularly exploits the structure $H(v)=I-\gamma P(v)$ of the "Hessian" in the control problem and employs the spectral decomposition of the matrix $P(v)$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

In this regard, we note that $w_{k}$ and the all-one vector $\bm{1}$ are, respectively, the left and right eigenvectors of $P(v_{k})$ corresponding to the largest eigenvalue, i.e., $1$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

A similar idea has also been used in stochastic optimization. In particular, *Newton-Sampling Method via Rank Thresholding (NewSamp)* is characterized by with eigenvalues $(\widehat{\lambda}_{k,i})_{i=1}^{r+1}$ and the corresponding eigenvectors $(\widehat{u}_{k,i})_{i=1}^{r}$ computed using eigenvalue decomposition of the *batch-sampled* Hessian, that is, $\frac{1}{B}\sum_{j=1}^{B}\nabla^{2}\widehat{f}(x_{k},\xi_{k,j})$. For model-free control, the same idea is used in *Rank-One Modified QL (R1-QL)* with where $\widehat{w}_{k}$ is now the state-action stationary distribution of the Markov chain induced by the greedy policy w.r.t. $q_{k}$ and estimated using the sample transitions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Once again, the preceding update rule exploits the structure of the "Hessian" in the control problem.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

We note that the spectral preconditioning technique is closely related to the *matrix splitting* method for solving linear equations. In particular, Deflated Dynamics VI (DDVI) and Temporal Difference (DDTD) algorithms also use a spectral decomposition of the transition probability matrix to form a low-rank approximation of it. They then use this low-rank approximation in combination with matrix splitting for the *policy evaluation* problem. In effect, the corresponding update rules follow the same structure as R1-VI/QL, except with rank-$r$ approximation of the transition probability matrix where $r>1$ (as opposed to $r=1$).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Convergence of Control Algorithms", "weight": 1.0} -->

One of the promises of building a common formulation for control and optimization algorithms is to borrow existing theoretical results from one field to another. However, as several other studies have pointed out, the similarity in the update rule does not carry over to the analysis. One of the main reasons for this discrepancy is the *non-differentiability* of the Bellman optimality operator $T$. Another complicating factor is that the operator $T$ is a contraction in $\infty$-norm, which is also *non-differentiable*. This forces the convergence analysis of the control algorithms to rely more on fixed-point theory and contraction mappings than on gradient-based smooth analysis.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Convergence of Control Algorithms", "weight": 1.0} -->

In what follows, we examine general tools for the convergence analysis of control algorithms, as well as some simple yet effective remedies for ensuring the convergence of novel control algorithms.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

For *finite* state-action MDPs, the non-differentiability of the operator $T$ is "manageable." Indeed, for such MDPs, $T$ is piece-wise affine and we have where the minimization is over the finite set of all deterministic control policies, each corresponding to a linear function $c^{\pi}+\gamma P^{\pi}v$. Equivalently, the finite family of policies admits an affine switching system, a connection leveraged by to establish convergence guarantees for asynchronous Q-learning. Moreover, by Rademacher's Theorem \[102, Thm. 10.8\], $T$ is differentiable almost everywhere. This property allows one to use tools from semismooth analysis for deriving local convergence results. In particular the authors use the fact that the PI algorithm is an instance of the semi-smooth Newton method to show that it has a local quadratic convergence rate. Similarly the semismoothness of $T$ is used for deriving a local superlinear convergence rate for one of the proposed quasi-PI algorithms.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

A more general approach, however, is to completely get rid of the non-differentiability by *smoothing* the Bellman optimality operator. Not surprisingly, a similar technique has been extensively used to develop algorithms for solving non-smooth optimization problems; see, e.g., the seminal work. The smoothing of $T$ is achieved by approximating the minimization operation by a differentiable function. As an example, by using the *log-sum-exp* (a.k.a. *soft-max*) function, we can define where $\beta>0$ is the so-called temperature parameter. The operator $\bar{T}_{\beta}$ is an over-approximation of the true Bellman optimality operator $\bar{T}=\mathds{E}_{\varsigma^{+}}[\widehat{T}(\cdot,\varsigma^{+})]$ and, in particular, $\bar{T}_{\beta}\rightarrow\bar{T}$ as $\beta\rightarrow\infty$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

Accordingly, its fixed-point $q^{\beta}$ is not the optimal Q-function, while the gap $\|q^{\beta}-q^{\star}\|_{\infty}$ can be controlled via the temperature parameter $\beta$. However, such smoothing allows for a direct application of the second-order scheme for finding the fixed-point of $\bar{T}_{\beta}$. This idea has been recently used to propose the generalized second-order VI with a quadratic convergence rate.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

Besides the general tools discussed above, there are simple yet efficient "safeguarding" techniques for ensuring the convergence of novel model-based algorithms that lack convergence guarantees. These techniques specifically exploit the fact that the Bellman optimality operator $T$ is a $\gamma$-contraction. To be precise, let us consider a generic model-based update rule characterized by the novel update vector $d_{k}$. One simple technique for ensuring the convergence of the preceding update rule is to safeguard it against VI. For some $\gamma^{\prime}\in[\gamma,1)$, we consider the *safeguarded update rule* The preceding update rule has the following convergence guarantee (for completeness, we provide the proof in Appendix A.1; see also \[42, Thm.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Similar to a model-based case, one can benefit from smoothing approaches in model-free scenarios. In simple words, smoothing out the kinks in the Bellman optimality operator or the optimal policies allows us to borrow well-developed tools for stochastic optimization of smooth functions. The recently proposed *mellow-max* operator is another excellent example of such smoothing that can be used as a differentiable approximation of the minimization within the Bellman optimality operator. Besides being a smooth operator, the mellow-max operator is, more importantly, non-expansive in the $\infty$-norm. This property then streamlines the usage of standard convergence techniques seamlessly.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

The corresponding smoothed Bellman optimality operator using the mellow-max is defined as with $\omega>0$ being the temperature parameter that can be used to control the gap $\|q^{\omega}-q^{\star}\|_{\infty}$ between the fixed-point $q^{\omega}$ of $T_{\omega}$ and the true optimal Q-function $q^{\star}=\bar{T}(q^{\star})$. The smoothed operator $T_{\omega}$ is an under-approximation of the true Bellman optimality operator $\bar{T}$ and, in particular, we have $T_{\omega}\rightarrow\bar{T}$ as $\omega\rightarrow\infty$. The operator $T_{\omega}$ has been recently used in combination with Anderson mixing to improve the convergence behavior in policy iteration.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

In the model-free case, algorithmic updates are inherently noisy, being driven by samples of the dynamics and costs. This stochasticity naturally places these algorithms within the scope of *stochastic approximation* (*SA*). A standard SA iteration is where $\alpha_{k}$ is the step-size (or the so-called *learning rate*), $h:\mathbb{R}^{\ell}\!\to\!\mathbb{R}^{\ell}$ is the *mean field* (expected update), and $M_{k}$ is a martingale-difference noise. A common approach to studying the limiting behavior of an SA method is the *ordinary differential equation* (*ODE*) method. The ODE method (with a dynamical-systems viewpoint), originating with Ljung, analyzes by comparing it with the flow of and drawing conclusions about the iterates from the asymptotics of this ODE. The interested reader is referred to for comprehensive treatments. Invariance principles from nonlinear systems (e.g., LaSalle's invariance principle; see \[53, Ch.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

4\]) then identify invariant/limit sets of the ODE toward which trajectories converge. Under standard SA assumptions, the SA iterates track these sets. To guarantee almost-sure boundedness (or Lyapunov stability of the iterates), one imposes verifiable drift/Lyapunov conditions. See for the ODE method with drift at infinity and for global Lyapunov constructions. It is worth mentioning that an important RL-specific deviation from otherwise standard SA conditions is *ergodicity of the state process* for policy evaluation and *sufficient exploration* for control.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Over the years, the ODE framework, in particular the framework introduced, has become a standard tool for establishing stability and convergence of a broad class of model-free control/RL algorithms. Considering the *average cost problems* the authors provided for the first time a complete analysis of two Q-learning algorithms by coupling the ODE style analysis with Kushner-Clark argumentation style. Another major subclass of RL methods is the well-known *actor-critic* methods, which can be characterized as *coupled*, *two-timescale* stochastic iterations: the critic evolves on a *fast* scale to track the value of the current policy, and the actor evolves on a *slow* scale using the critic's signal to adjust the policy. The ODE viewpoint makes this decomposition explicit, which, under the usual SA conditions together with the RL ones, yields clean convergence guarantees to a stationary policy. Another example is the use of the ODE method to show the convergence of *gradient temporal difference* (*TD*) *approaches* under the general setup of off-policy learning and linear function approximation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

This work has then been extended to any smooth value function approximation in and to a control setting (policy improvement) under a stationary behavioral policy. Recently, ODE-style arguments have been used not only to prove convergence but also to *design* RL algorithms. In, the authors introduce a *matrix preconditioning* for the TD direction, improving the transient behavior of the proposed algorithm. This matrix gain is learned on a faster timescale and tracks the inverse Jacobian of the mean field. This design extends to nonlinear function approximation under standard regularity assumptions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

As an example of application of results developed using ODE methods for SAs, namely, we finish this section by providing a simple and efficient "safeguarding" technique for ensuring the convergence of novel model-free algorithms that lack convergence guarantees. To this end, let us consider a generic update rule characterized by the novel update vector $d_{k}=\alpha_{k}b_{k}$. Here, $\alpha_{k}$ is the learning rate satisfying the standard Robbins--Monro condition (i.e., $\sum_{k}\alpha_{k}=\infty$ and $\sum_{k}\alpha_{k}^{2}<\infty$) and $b_{k}$ is a vector depending on the sampled Bellman error, a.k.a. temporal difference (i.e., $\widehat{T}(q_{k},\varsigma^{+}_{k})-q_{k}$).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

To address the convergence issue, one possibility is to consider a convex combination of the standard QL algorithm update rule (3.1) with this novel update rule with a diminishing effect. To be precise, we modify the update rule as follows where $\beta_{k}$ is a diminishing coefficient (i.e., $\beta_{k}\rightarrow 0$). Finally, to ensure convergence, we need to bound the effect of the extra term $p_{k}=b_{k}+q_{k}-\widehat{T}(q_{k},\varsigma^{+}_{k})$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

For that, given some $\rho>0$, we employ the operator $B_{\rho}:\mathbb{R}^{\mathcal{S}\times\mathcal{A}}\rightarrow\mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ defined by This leads to the *safeguarded update rule* with the following convergence property (for completeness, we provide the proof in Appendix A.3; see also \[58, Sec. III.C\]):
