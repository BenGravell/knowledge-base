<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The connection between control algorithms for Markov decision processes and optimization algorithms has been implicitly and explicitly exploited since the introduction of dynamic programming algorithm by Bellman in the 1950s. Recently, this connection has attracted a lot of attention for developing new control algorithms inspired by well-established optimization algorithms. In this paper, we make this analogy explicit across four problem classes with a unified solution characterization. This novel framework, in turn, allows for a systematic transformation of algorithms from one domain to the other. In particular, we identify equivalent optimization and control algorithms that have already been pointed out in the existing literature, but mostly in a scattered way. We also discuss the issues arising in providing theoretical convergence guarantees for these new control algorithms and provide simple yet effective techniques to solve them. The provided framework and techniques then lay out a concrete methodology for developing new convergent control algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Markov decision processes (MDPs) have become a standard mathematical framework for the formulation of stochastic optimal control problems, that is, the problem of dynamic decision-making under uncertainty. This popularity can be to a large extent attributed to the Bellman principle of optimality and the dynamic programming algorithm \[bellman1957markovian\]. In particular, the fixed-point characterization of the optimal value function of an MDP has led to the development of a large class of iterative value-based algorithms, such as value iteration and policy iteration. This fixed-point characterization has also been used for identifying the fundamental connection between algorithms for optimal control of MDPs and those for optimization. A classic example is the policy iteration algorithm for MDPs which is an instance of the Newton method \[puterman1979convergence, bertsekas2022lessons\]. Recently, the connection between optimization and control problems has attracted a lot of attention for developing new control algorithms, with faster convergence and/or lower complexity, inspired by their counterparts for solving optimization problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, the modifications to the value iteration algorithm in \[goyal2019first\] and the Q-learning algorithm in \[weng2020momentum\] are inspired by momentum-based acceleration in optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The implicit connection between optimization algorithms and control algorithms for MDPs with a finite state-action space has also been studied more systematically. In \[vieillard2019connections\], the authors look at the connection between *constrained* convex optimization algorithms and control algorithms such as Frank-Wolfe algorithm \[frank1956algorithm\] and conservative policy iteration \[kakade2002approximately\]. A detailed comparison between *deterministic* optimization algorithms and *model-based*^11^1In this paper, the terminologies of "model-free" and "model-based" indicate the available information (oracle), i.e., whether we have access to the model or only the system trajectory (samples); see Section 2.2 for more details. We note that this is different from the common terminologies in the RL literature where these terms refer to the solution approach, i.e., whether we identify the model along the way (model-based RL) or directly solve the Bellman equation to find the value function (model-free RL).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

control algorithm is also provided in \[grand2021convex\], where the author looks at a wide range of optimization algorithms including gradient descent, accelerated gradient descent, Newton method, and quasi-Newton method and their counterparts for solving control problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these observations, this study provides an explicit framework unifying the tight link between optimization (stochastic and deterministic, respectively) and optimal control (model-based dynamic programming and model-free reinforcement learning, respectively). Specifically, this goal is achieved by exploiting the (expected) root-finding characterization of optimization problems and the (expected) fixed-point characterization of control problems. The framework yields an explicit transformation of deterministic (stochastic) convex optimization problems to model-based (model-free) control problems, and vice versa (Section 2, Table 1). This explicit relationship, in turn, allows for a systematic transformation of algorithms from one domain to the other, which we will use to identify existing (and mostly known) equivalent algorithms for optimization and control (Section 3, Table 2). Unfortunately, the common formulation for control and optimization algorithms does not allow us to borrow existing theoretical results from one field to another. Indeed, the similarity in the update rule does not carry over to the analysis, particularly when it comes to the convergence of these algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, we also examine general tools for the convergence analysis of control algorithms, as well as some simple yet effective remedies for ensuring the convergence of novel control algorithms (Section 4, Theorems 4.1. ‣ 4.1. Model-based algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective"), 4.2. ‣ 4.1. Model-based algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective"), 4.3. ‣ 4.2. Model-free algorithms ‣ 4. Convergence of Control Algorithms ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective")). The provided framework and techniques then lay out a concrete methodology for developing new algorithms in one domain based on the existing algorithms in the other, along with theoretical convergence guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we restrict attention to control algorithms for *finite* state--action MDPs. For infinite (continuous) state--action spaces, aside from special cases like linear--quadratic regulators (LQR), practical computation typically requires finite-dimensional approximations. One approach is to approximate at the model level by aggregating (discretizing) the state and action spaces, thereby reducing the problem to a finite MDP \[ref:Bert_disc_75, ref:Powell_07\]. Another approach is to approximate the value function directly with a finite parameterization by minimizing (a proxy for) the residual of its Bellman fixed-point equation \[ref:Bert_abstract, szepesvari2022algorithms\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Examples include linear parameterizations \[ref:Bert_temporal, \], nonlinear parameterizations using neural networks \[ref:Bert_neuro-dynamic, SCHMIDHUBER2015, sutton2018reinforcement\], and max-plus methods \[, GONCALVES2021109623, ref:FDP_TAC, ref:FDP_NeurIPS Liu2024fitted\]. There is also an alternative formulation in which the target function solves an infinite-dimensional linear program \[ref:HL1\], enabling approximation via finite, tractable convex programs \[ref:VanRoy_MP, ref:HL2, ref:Moh_SIOPT\]. Viewed this way, most of these approximation strategies can be framed as solving a finite-dimensional fixed-point problem or a convex optimization problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. For a vector $v \in {\mathbb{R}}^{n}$, we use $v{(i)}$ and ${\lbrack v\rbrack}{(i)}$ to denote its $i$-th element. Similarly, $M{(i,j)}$ and ${\lbrack M\rbrack}{(i,j)}$ denote the element in row $i$ and column $j$ of the matrix $M \in {\mathbb{R}}^{m \times n}$. We use $\cdot^{\top}$ to denote the transpose of a vector/matrix. $\left. \parallel \cdot \parallel{}_{2} \right.$ and $\left. \parallel \cdot \parallel{}_{\infty} \right.$ denote the 2-norm and $\infty$-norm of a vector, respectively. $\left. \parallel \cdot \parallel{}_{2} \right.$ and $\left.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

\parallel \cdot \parallel{}_{F} \right.$ denote the induced 2-norm and the Frobenius norm of a matrix, respectively. The identity operator is denoted by $Id$. We use $\mathbf{1}$ and $I$ to denote the all-ones vector and the identity matrix, respectively. We denote the $i$-th unit vector by $e_{i}$, that is, the vector with its $i$-th element equal to $1$ and all other elements equal to $0$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problems: Optimization vs. Control", "weight": 1.0} -->

In this section, we provide the generic framework that connects optimization problems to control problems. In particular, we provide the explicit transformations between different variables and operations in these problems. Table 1 provides a condensed summary of this framework.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problems: Optimization vs. Control", "weight": 1.0} -->

Table 1. Equivalence transformations. See Section 2 for details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

We first look at the root-finding characterization of the solution to convex optimization problems. Consider the minimization problem

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

where $\hat{f}:{{{\mathbb{R}}^{\ell} \times \Xi}\rightarrow{\mathbb{R}}}$ is a sample-wise function and $\xi$ is random vector with a fixed probability distribution $\mathbb{P}$ over $\Xi$. We assume that the resulting function $f:{{\mathbb{R}}^{\ell}\rightarrow{\mathbb{R}}}$ is twice continuously differentiable and strongly convex.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

Deterministic optimization: Assume that $\mathbb{P}$ in is known and that the corresponding expectation can be computed. The unique minimizer $x^{\star}$ is the root of the gradient operator, i.e.,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

Stochastic optimization: Now assume that $\mathbb{P}$ in is unknown but can be sampled. In this case, the minimizer $x^{\star}$ satisfies the expected root-finding problem

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimization problem", "weight": 1.0} -->

where $\nabla$ now denotes the partial derivative w.r.t. $x$. We note that, above, there is an underlying assumption that the differentiation w.r.t. $x$ and expectation w.r.t. $\xi$ can be operated in any order.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Control problem", "weight": 1.0} -->

The standard modeling framework for stochastic optimal control problems is the *Markov decision process* (MDP). An MDP is characterized by the tuple $(\mathcal{S},\mathcal{A},{\mathbb{P}},c,\gamma)$, where

<!-- chunk {"id": "body-0021", "role": "body", "section": "Control problem", "weight": 1.0} -->

$\mathbb{P}$ is the transition probability kernel such that ${\mathbb{P}}{(\left. s^{+} \middle| {s,a} \right.)}$ is the probability of the transition to state $s^{+}$ given that the system is in state $s$ and the chosen control is $a$ for each ${(s,a,s^{+})} \in {\mathcal{S} \times \mathcal{A} \times \mathcal{S}}$,

<!-- chunk {"id": "body-0022", "role": "body", "section": "Control problem", "weight": 1.0} -->

$c \in {\mathbb{R}}^{\mathcal{S} \times \mathcal{A}}$ is the stage cost function such that $c{(s,a)}$ is the cost of taking the control action $a$ while the system is in state $s$, and,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Control problem", "weight": 1.0} -->

$\gamma \in {}$ is the discount factor acting as a trade-off between short- and long-term costs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Control problem", "weight": 1.0} -->

Let us also define the *action-value function* (a.k.a. the *Q-function*) $q^{\pi} \in {\mathbb{R}}^{\mathcal{S} \times \mathcal{A}}$ for the policy $\pi$ by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Control problem", "weight": 1.0} -->

The problem of interest is to control the MDP optimally, that is, to find an optimal policy $\pi^{\ast}$ with the optimal (action-)value functions

<!-- chunk {"id": "body-0026", "role": "body", "section": "Control problem", "weight": 1.0} -->

so that the expected, discounted, infinite-horizon cost is minimized. Let us also note that the optimal policy, that is a minimizer of the preceding optimization problems, is greedy w.r.t. $v^{\star}$ and $q^{\star}$, i.e., $\pi^{\star} = \pi_{v^{\star}} = \pi_{q^{\star}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Control problem", "weight": 1.0} -->

Model-based control: When we have access to the transition kernel and the cost function, the problem is usually characterized by the fixed-point problem. Indeed, defining the *Bellman optimality operator* $T:{{\mathbb{R}}^{\mathcal{S}}\rightarrow{\mathbb{R}}^{\mathcal{S}}}$ by

<!-- chunk {"id": "body-0028", "role": "body", "section": "Control problem", "weight": 1.0} -->

or, equivalently, $v^{\star} = {T{(v^{\star})}}$, that is, the optimal value function $v^{\star}$ is the *unique* fixed-point of $T$. The uniqueness follows from the fact that the operator $T$ is a $\gamma$-contraction in $\infty$-norm. Observe that, in this case, $T$ can be exactly computed given the model of the underlying MDP.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control problem", "weight": 1.0} -->

Model-free control: In real applications, the model is often unknown, and instead, one can generate samples. Examples of this are very large systems where identifying the model is prohibitively expensive but transitions between states can be observed and recorded, such as those in video games. This problem has been studied extensively in the reinforcement learning community and is often formulated as the *expected* fixed-point problem. To provide this characterization, let us define the *vector of sampled next states* $\varsigma^{+} \in \mathcal{S}^{\mathcal{S} \times \mathcal{A}}$ where

<!-- chunk {"id": "body-0030", "role": "body", "section": "Transformation", "weight": 1.0} -->

In what follows, we focus on *tabular MDPs with a finite state-action space*. We thus consider $\mathcal{S} = {\{ 1,2,\ldots,n\}}$ and $\mathcal{A} = {\{ 1,2,\ldots,m\}}$. Recall the Bellman optimality operator $T:{{\mathbb{R}}^{\mathcal{S}}\rightarrow{\mathbb{R}}^{\mathcal{S}}}$ with

<!-- chunk {"id": "body-0031", "role": "body", "section": "Transformation", "weight": 1.0} -->

where $e_{(s,a)} \in {\mathbb{R}}^{\mathcal{S} \times \mathcal{A}}$ is the unit vector for the state-action pair ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$, and $\varsigma^{+} \in \mathcal{S}^{\mathcal{S} \times \mathcal{A}}$ is the vector of sampled next states defined in (6 ‣ 2.2. Control problem ‣ 2. Problems: Optimization vs. Control ‣ Control and Reinforcement Learning through the Lens of Optimization: An Algorithmic Perspective")).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Transformation", "weight": 1.0} -->

Before providing the equivalence relations between optimization and control problems, let us provide an important result for the Bellman optimality operator.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

We now look at existing algorithms for optimization and control and their equivalence within the proposed framework. We start with the well-known baseline first-order and second-order algorithms and show how the application of the proposed transformations to well-established optimization algorithms, such as gradient descent and Newton method, leads to well-known control algorithms such as value iteration and policy iteration. We then cover a wide range of modifications to optimization algorithms, from momentum to spectral decomposition of the Hessian, and their counterpart control algorithms. We note that most of these equivalences have already been pointed out in the existing literature, however, mostly in a scattered way. An exception is \[grand2021convex\], which studies the relation between *deterministic* optimization algorithms and *model-based* control algorithms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

To ease the exposition, we unify iterative algorithms by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

where $y_{k} = x_{k}$, $v_{k}$ or $q_{k}$ based on the context. In all considered settings, $d_{k}$ represents the update vector between iterations $k$ and $k + 1$. This form allows us to characterize algorithms in terms of $d_{k}$. Moreover, we use Greek letters $\alpha_{k},\beta_{k},\ldots$ as scalar coefficients (e.g., step-size, learning rate, etc.) in the update vectors. We note that the specific values of these parameters may differ between equivalent algorithms. A compact summary of this can be found in Table 2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithms: Optimization vs. Control", "weight": 1.0} -->

Some remarks are in order regarding the following equivalence relationships. First, the following list of algorithms is not meant to be an exhaustive review of the literature. Instead, our aim is to provide illustrative examples of the application of transformations of Table 1 in identifying equivalent algorithms for optimization and control. Second, the provided update rules for the cited algorithms, although covering the main characteristic of interest, are occasionally not exact. This is particularly the case in stochastic/model-free settings where other techniques, such as batch estimation or variance reduction, are also used in the original algorithms. Finally, the equivalence between optimization and control algorithms does not imply that these algorithms enjoy similar theoretical guarantees, particularly when it comes to convergence. We will discuss this issue in more detail in Section 4.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

We start our discussion with the vanilla first-order and second-order algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Vanilla first-order methods. The celebrated *Gradient Descent (GD)* \[lemarechal2012cauchy\] method is characterized by

<!-- chunk {"id": "body-0039", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

where $\alpha_{k}$ is a properly chosen step-size. Applying the transformations of Table 1 to GD, we derive the so-called *Relaxed Value Iteration (Rel-VI)* \[kushner1971accelerated, porteus1978accelerated, goyal2019first\] with

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

for model-based control. In particular, for the constant step-size $\alpha_{k} = 1$, we have the standard VI algorithm $v_{k + 1} = {T{(v_{k})}}$ \[bellman1957markovian\]. Correspondingly, *Stochastic GD (SGD)* \[robbins1951stochastic\] is characterized by

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Under the transformations of Table 1, SGD leads to the *synchronous* *Q-Learning (QL)* algorithm \[watkins1992q, kearns1998finite\] with^44^4This is the so-called *synchronous* update of the Q-function in *all* state-action pairs in each iteration, corresponding to the *parallel sampling model* introduced by \[kearns1998finite\].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Vanilla second-order methods. In second-order algorithms, $d_{k}$ is specified by both the gradient and the Hessian oracles. The *damped* *Newton Method (NM)* is one such algorithm with

<!-- chunk {"id": "body-0043", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

The *pure* Newton step with $\alpha_{k} = 1$ has a *local* quadratic convergence if, in addition to $f$ being strongly convex, the Hessian is Lipschitz-continuous \[bubeck2015convex, Thm. 5.3\]. Globally, however, the pure Newton method can lead to divergence. This is the reason behind introducing the step-size $\alpha_{k} < 1$ in the damped version which can be used to guarantee a global linear convergence. We can use the transformations of Table 1 in order to transform the Newton method into a model-based control algorithm with

<!-- chunk {"id": "body-0044", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

where $P{(v_{k})}$ is the transition probability matrix of the Markov chain under the greedy policy w.r.t. $v_{k}$. The derived model-based control algorithm then corresponds to the well-known *Policy Iteration (PI)* algorithm \[puterman1979convergence\] with $v_{k + 1} = {\left( {I - {\gammaP{(v_{k})}}} \right)^{- 1}c^{\pi_{v_{k}}}}$, where $c^{\pi_{v_{k}}}$ is the vector of stage costs corresponding to the greedy policy $\pi_{v_{k}}$ w.r.t. $v_{k}$. Indeed, the PI algorithm is equivalent to the semi-smooth Newton method with a local quadratic convergence rate \[gargiani2022dynamic\].

<!-- chunk {"id": "body-0045", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

In the model-free case, the stochastic version of the Newton method \[ruppert1985newton\] has been a source of inspiration for developing second-order-type Q-learning algorithms. In particular, the *Stochastic Newton-Raphson (SNR)* \[ruppert1985newton\] algorithm with

<!-- chunk {"id": "body-0046", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

was used for developing the *Zap QL (ZQL)* algorithm \[DevrajMeyn2017NIPS\] with

<!-- chunk {"id": "body-0047", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

Note that the preceding algorithm involves updating one entry of the action-value function $q_{k}$ at each iteration $k$, corresponding to the state-action pair $(s_{k},a_{k})$ chosen at iteration $k$ -- recall that $e_{(s,a)} \in {\mathbb{R}}^{\mathcal{S} \times \mathcal{A}}$ is the unit vector corresponding to the state-action pair $(s,a)$. Moreover, ZQL in \[DevrajMeyn2017NIPS\] implements an eligibility trace with a decaying factor which we omit (i.e., set to $0$) for simplicity of the representation. The implementation of zap QL algorithm with *synchronous* update of the Q-function in all state-action pairs in each iteration is then characterized by

<!-- chunk {"id": "body-0048", "role": "body", "section": "Baseline methods", "weight": 1.0} -->

where $\hat{P}{(q,\varsigma^{+})}$ is the synchronously sampled state-action transition probability matrix of the Markov chain under the greedy policy w.r.t. $q$. Note that is exactly the SNR algorithm under the transformations of Table 1.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

We now focus on classic acceleration techniques such as momentum and anchoring in optimization. These techniques have recently attracted a lot of attention in developing control algorithms with improved convergence and complexity properties. We also look at a classic control engineering approach, namely, proportional-integral-derivative (PID) control, and its application in optimization and control algorithms.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Momentum methods. In the so-called momentum-based algorithms, the update vector $d_{k}$ is specified by gradient oracles but also depends on $d_{k - 1}$. One such algorithm is *GD with Polyak Momentum (Mom-GD)* \[polyak1964some\], a.k.a. heavy ball method, characterized by

<!-- chunk {"id": "body-0051", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Another well-known momentum-based algorithm is *GD with Nesterov Acceleration (Acc-GD)* \[nesterov1983method\] with update vector

<!-- chunk {"id": "body-0052", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

With a proper choice of the step-sizes $\alpha_{k}$ and $\beta_{k}$, these schemes can be shown to accelerate the convergence rate, compared to the standard GD, for particular classes of objective functions \[polyak1964some, nesterov2018lectures\]. The corresponding model-based control algorithms, using the transformations of Table 1, are *Momentum VI (Mom-VI)* \[goyal2019first\] with

<!-- chunk {"id": "body-0053", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

and *Accelerated VI (Acc-VI)* \[goyal2019first\] with

<!-- chunk {"id": "body-0054", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

However, the convergence of the preceding accelerated schemes is in general not guaranteed. In \[goyal2019first\], the authors address this issue by *safeguarding*, i.e., combining the accelerated VI with the standard VI; see Section 4 for more details.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For accelerating SGD, a direct combination of Polyak momentum or Nesterov acceleration with SGD has been shown to lead to no better (and even worse) performance in terms of convergence rate \[yang2016unified, kidambi2018insufficiency\]. At least for almost sure convergence, \[liu2022almost\] reports the same rate of convergence for SGD with Polyak momentum and SGD with Nesterov acceleration as for standard SGD. Nevertheless, modifications of momentum-based acceleration methods have led to a range of accelerated SGD algorithms with faster convergence rates with specific assumptions on the problem data \[kidambi2018insufficiency, liu2018accelerating, allen2017katyusha\]. The idea of using momentum for accelerating QL has also attracted some interest. In particular, applying the transformations of Table 1 on a generic *Momentum SGD (Mom-SGD)* \[yang2016unified\] with

<!-- chunk {"id": "body-0056", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

and step-sizes $\alpha_{k},\beta_{k},\delta_{k}$, we obtain the *Speedy QL (SQL)* \[ghavamzadeh2011speedy\], *Nesterov Stochastic Approximation (NeSA)* \[devraj2019matrix\], and *Momentum QL (Mom-QL)* \[weng2020momentum\] algorithms with

<!-- chunk {"id": "body-0057", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

The difference between these three algorithms is in the choice of the step-sizes $\alpha_{k},\beta_{k},\delta_{k}$. For example, by setting $\beta_{k} = \delta_{k} = {({1 - {2\alpha_{k}}})} = {{({k - 1})}/{({k + 1})}}$, we recover SQL.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Anchoring & Halpern iteration. Halpern iteration \[halpern1967fixed\] is an acceleration scheme originally developed for fixed-point iterations involving *non-expansive* maps. In particular, it modifies the updates by gradually pulling the iterates toward a reference point, a.k.a. *anchor*. In the case of deterministic optimization, modifying the standard GD using Halpern iteration, we derive the *Anchored GD (Anc-GD)* \[tran2022connection\]

<!-- chunk {"id": "body-0059", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where $x \in {\mathbb{R}}^{n}$ is the anchor, $\beta_{k} \in {}$ is a properly chosen decaying step-size, and $\delta_{k}$ is the step-size corresponding to the standard GD update. The canonical choices for the anchor and the step-size are $x = x_{0}$ and $\beta_{k} = \frac{1}{k + 2}$ \[lieder2021convergence\]. Using our standard characterization, Anc-GD (with the anchor $x = x_{0}$) corresponds to the update vector

<!-- chunk {"id": "body-0060", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where $\alpha_{k} = {\delta_{k}{({1 - \beta_{k}})}}$. Under certain conditions on the objective function $f$ and the step-sizes $\alpha_{k}$ and $\beta_{k}$, Anc-GD improves the rate of convergence compared to standard GD. Indeed, Anc-GD can be shown to be equivalent to Nesterov acceleration with a correction term \[tran2022connection\]. However, when the operation corresponding to standard GD is a *contraction*, the modification via anchoring in Anc-GD does *not* improve the convergence rate \[park2022exact\]. The corresponding model-based control algorithm is *Anchored VI (Anc-VI)* \[lee2023accelerating\] defined by the update vector

<!-- chunk {"id": "body-0061", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where $\alpha_{k} = {({1 - \beta_{k}})}$. A similar, undesired situation arises for Anc-VI algorithm. Since the Bellman operator is a contraction, there is no improvement in the convergence rate for $\gamma < 1$ and the iterates of Anc-VI converge to the optimal value function $v^{\star}$ linearly with rate $\gamma$ (i.e., similar to standard VI). However, of importance is the polynomial (i.e., with rate $\mathcal{O}{({1/k})}$) convergence of the Bellman residual ${\|{v_{k} - {T{(v_{k})}}}\|}_{\infty}$ to zero in the *long-horizon* setting with $\gamma\rightarrow 1$ \[lee2023accelerating, Thm. 2\].

<!-- chunk {"id": "body-0062", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

In particular, even in the *undiscounted* setting (i.e., $\gamma = 1$), the Bellman residual in Anc-VI converges to zero with rate $\mathcal{O}{({1/k})}$, assuming the corresponding undiscounted Bellman operator has a fixed point \[lee2023accelerating, Thm. 3\]. As a result, in long-horizon and undiscounted settings, Anc-VI maintains robust convergence guarantees, while the geometric rate of standard VI deteriorates.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

The corresponding *Stochastic Halpern Iteration (SHI)* \[cai2022stochastic, alacaoglu2025towards\], characterized by

<!-- chunk {"id": "body-0064", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

with step-sizes $\alpha_{k},\beta_{k}$, has been recently studied extensively in the stochastic optimization setting. In particular, under certain conditions and in combination with other techniques such as variance reduction and restarting, anchoring leads to improved sample complexity \[cai2022stochastic\]. Moreover, anchoring has been shown to be instrumental in providing guarantees for the last iterate, as opposed to a weighted average of iterates, under relaxed bounded-variance assumptions \[alacaoglu2025towards\]. Applying the transformations of Table 1 on SHI, we derive the *Halpern QL (HQL)* \[bravo2024stochastic\] and *Stochastic Anchored Value Iteration for Discounted MDPs (SAVID)* \[lee2025near\] algorithms with

<!-- chunk {"id": "body-0065", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where $\alpha_{k} = {1 - \beta_{k}}$. To be precise, HQL uses batch estimation with multiple samples for the sampled Bellman operation in this update rule to reduce the variance, while SAVID incorporates the recursive sampling technique \[jin2024truncated\] to reduce the sample complexity. Of importance is again that both HQL and SAVID algorithms (with minor modifications) can also be used in the *averaged cost* setting in which the corresponding Bellman optimality operator is non-expansive but *not* contractive.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

PID control. An alternative to standard acceleration methods is to use proportional-integral-derivative (PID) controllers for designing the update rule. This is a well-established technique in automatic control for set-point tracking. The basic idea is to treat the iterates $x_{k}$ as the "state" of the system and define the "error" signal in terms of the gradient ${\nabla f}{(x_{k})}$ and possibly the finite difference of the state, i.e., $d_{k}$. This idea has recently been explored in training deep networks in \[an2018pid, chen2024accelerated\]. In particular, the *full batch* version of the *PID Optimizer (PID-Opt)* \[an2018pid\] algorithm is a deterministic optimization algorithm characterized by

<!-- chunk {"id": "body-0067", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where $\alpha_{k}$ is the step-size and $\beta_{k}$ is the decay coefficient in the integral term. The corresponding model-based control algorithm is *PID accelerated VI (PID-VI)* \[farahmand2021pid\] with

<!-- chunk {"id": "body-0068", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

Above, we see all three terms of the PID controller with the corresponding parameters $\kappa_{k}^{P},\kappa_{k}^{I},\kappa_{k}^{D}$. In particular, observe that, compared to PID-Opt, PID-VI uses the finite difference of the state (i.e., $d_{k - 1}$) as opposed to the finite difference of the gradient (i.e., $d_{k - 1}^{\prime} = {{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}}$) in its derivative term. Moreover, in \[farahmand2021pid\], the authors provide an adaptive scheme for tuning the PID parameters. The close connection between the PID acceleration schemes above and the momentum-based algorithms can be readily seen in their update rules. Indeed, PID-Opt and PID-VI provided above can recover standard momentum-based algorithms for specific values of the PID parameters.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For instance, Acc-GD can be derived by removing the derivative term in PID-Opt (i.e., setting $\kappa_{k}^{D} = 0$) \[an2018pid\]. Similarly, Mom-VI is an instance of PID-VI without the integral term (i.e., with $\kappa_{k}^{I} = 0$) \[farahmand2021pid\].

<!-- chunk {"id": "body-0070", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

For stochastic optimization, we can use the *mini-batch* version of PID-Opt \[an2018pid\], characterized by

<!-- chunk {"id": "body-0071", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

where the stochastic gradient operation is evaluated using a mini-batch of samples. In particular, observe that the derivative term also includes averaging to reduce the effect of noise in gradient evaluations. The corresponding model-free control algorithm is *PID accelerated QL (PID-QL)* \[bedaywi2024pid\] with

<!-- chunk {"id": "body-0072", "role": "body", "section": "Accelerated methods", "weight": 1.0} -->

In particular, observe that PID-QL also uses a stochastic approximation $q_{k - 1}^{\prime}$ of $q_{k - 1}$ in forming the derivative term based on the finite difference of the state $q_{k}$. Moreover, a scheme similar to that used in PID-VI \[farahmand2021pid\] is used to tune the PID parameters in PID-QL adaptively. We also note that PID-QL can recover Mom-QL \[weng2020momentum\] and SQL \[ghavamzadeh2011speedy\] in by setting the PID parameters accordingly \[bedaywi2024pid\]. Finally, while the empirical results reported for PID-Opt, PID-VI, and PID-QL show a significant improvement in the convergence rate compared to the corresponding standard methods, theoretical guarantees for the convergence of these algorithms are still lacking.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Quasi-Newton methods (QNMs) are a class of methods that allow for a trade-off between computational complexity and (local) convergence rate in solving optimization problems. To do so, these methods use a Newton-type update vector

<!-- chunk {"id": "body-0074", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where ${\overset{\sim}{H}}_{k}$ (or ${\overset{\sim}{H}}_{k}^{- 1}$) is a computationally efficient approximation of the true Hessian ${\nabla^{2}f}{(x_{k})}$ (or its inverse) at iteration $k$. Different QNMs use different approximations of the Hessian or its inverse. Some "classical" examples of QNMs include Broyden approximation \[broyden1965class\], Power symmetric Broyden approximation \[powell1970new\], Davidon-Fletcher-Powell approximation \[davidon1991variable, fletcher1963rapidly\]. All of these examples approximate the Hessian (or its inverse) as the "closest" matrix to a prior matrix within an affine set defined by (multi-)secant constraints (and possibly other structural constraints such as symmetry, sparsity, etc.). Under certain conditions, these methods lead to a local *superlinear* rate of convergence.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Not surprisingly, different types of QNMs have been (directly or with some modifications) employed in solving model-based and model-free control problems. Some recent examples include the Sketched Newton VI \[liu2024sketched\] and Quasi-PI \[kolarijani2023optimization\] algorithms. In what follows, we focus on two illustrative examples, namely, Anderson mixing and spectral preconditioning.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Anderson mixing. Anderson mixing, originally developed as an acceleration scheme for fixed-point iterations \[anderson1965iterative\], provides an update rule in which the next iterate is constructed as a linear combination of a finite number of most recent iterates and their images. In particular, *Anderson Accelerated GD (AA-GD)* \[mai2020anderson\], with memory $m \geq 0$ and $m_{k} = {\min{\{ k,m\}}}$, is characterized by the update vector

<!-- chunk {"id": "body-0077", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where $\mathbf{1}$ is the all-ones vector, $\alpha_{k}$ is a properly chosen step-size, and $G_{k}$ is assumed to be of full column rank (otherwise, we need to either use the pseudo-inverse or some form of regularization). Observe that for $m = 0$, we recover the standard GD. Applying the transformations of Table 1, we derive the *Anderson Accelerated VI (AA-VI)* \[geist2018anderson\] with

<!-- chunk {"id": "body-0078", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where $\alpha_{k} = 1$ and $G_{k}$ is assumed to be of full column rank. The preceding update rules correspond to the so-called *type-II* Anderson mixing. To be precise, the update vector of AA-GD/VI admits a QNM characterization of the form $d_{k} = {- {D_{k}g{(y_{k})}}}$, where $D_{k}$ is an approximation of the *inverse* of the Hessian, i.e., $H_{k}^{- 1}$ \[fang2009two\]. In \[zhang2020globally\], the authors consider the *type-I* Anderson mixing scheme in combination with GD/VI in which the update vector is of the form $d_{k} = {- {D_{k}^{- 1}g{(y_{k})}}}$ with $D_{k}$ being an approximation of the Hessian $H_{k}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

We note that the combination of Anderson mixing (type-I or type-II) with VI also lacks convergence guarantees. In \[zhang2020globally\], this issue is again addressed via *safeguarding*.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Anderson mixing has also been used in the stochastic optimization setting. In particular, in \[NEURIPS2021_c203e4a1\], the authors use (type-II) Anderson mixing to develop the *Stochastic Anderson Mixing (SAM)* algorithm with update vector

<!-- chunk {"id": "body-0081", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where $\alpha_{k},\beta_{k}$ are properly chosen step-sizes and $R_{k} = {\delta_{k}{(D_{k}^{x})}^{\top}D_{k}^{x}}$, with an adaptive coefficient $\delta_{k}$, acts as a *regularizer*. To be precise, SAM uses a batch of samples for estimation of the stochastic gradient operator. Note that the formulation above aligns with the QNM characterization of Anderson mixing. The corresponding model-free control algorithm is *QL with Stable Anderson Acceleration (SAA-QL)* \[sun2021damped\] with

<!-- chunk {"id": "body-0082", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where $\alpha_{k} = 1$ and $R_{k} = {\delta_{k}{({{\| D_{k}^{q}\|}_{F}^{2} + {\| D_{k}^{g}\|}_{F}^{2}})}I}$ as the regularizer. To be precise, SAA-QL in \[sun2021damped\] utilizes a *smoothed* version of the Bellman optimality operator based on the *mellow-max* operator; see Section 4.2 for more details. Moreover, in \[sun2021damped\], the proposed SAA is integrated within the Dueling Deep Q-Network (Duel-DQN) \[wang2016dueling\] algorithm for *continuous-state* model-free control. In particular, the SAA-Duel-DQN algorithm stores the last $m_{k}$ target networks (i.e., their parameters) and uses for computing the target values in each iteration.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Finally, let us note that several works have incorporated the original form of the Anderson mixing similar to for model-free control; see, e.g., \[shi2019regularized, zuo2022offline\].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

Spectral preconditioning. This class of QNMs involves another computationally efficient approximation of the Hessian. To be precise, they use an approximation of the form

<!-- chunk {"id": "body-0085", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where ${U_{k},W_{k}} \in {\mathbb{R}}^{\ell \times r}$ are tall matrices with $r \ll \ell$. Such approximations readily allow for application of the Woodbury matrix identity \[hager1989updating\] for computing ${\overset{\sim}{H}}_{k}^{- 1}$ with a low computational cost. In spectral preconditioning techniques, the matrices $U_{k}$ and $W_{k}$ are particularly formed based on the spectral decomposition of the true Hessian. For instance, *GD with Spectral Preconditioning (SP-GD)* \[doikov2024spectral\] is characterized by

<!-- chunk {"id": "body-0086", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

with $\alpha_{k}$ being a properly chosen regularizer parameter, ${(\lambda_{k,i})}_{i = 1}^{r}$ the largest eigenvalues of the Hessian ${\nabla^{2}f}{(x_{k})}$ and ${(u_{k,i})}_{i = 1}^{r}$ the corresponding eigenvectors. For model-based control, we can mention the recently developed *Rank-One Modified VI (R1-VI)* \[kolarijani2025rank\] with

<!-- chunk {"id": "body-0087", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where $w_{k}$ is the stationary distribution estimate of the Markov chain induced by the greedy policy w.r.t. $v_{k}$. The preceding update rule particularly exploits the structure ${H{(v)}} = {I - {\gammaP{(v)}}}$ of the "Hessian" in the control problem and employs the spectral decomposition of the matrix $P{(v)}$. In this regard, we note that $w_{k}$ and the all-one vector $\mathbf{1}$ are, respectively, the left and right eigenvectors of $P{(v_{k})}$ corresponding to the largest eigenvalue, i.e., $1$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

A similar idea has also been used in stochastic optimization. In particular, *Newton-Sampling Method via Rank Thresholding (NewSamp)* \[erdogdu2015convergence\] is characterized by

<!-- chunk {"id": "body-0089", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

with eigenvalues ${({\hat{\lambda}}_{k,i})}_{i = 1}^{r + 1}$ and the corresponding eigenvectors ${({\hat{u}}_{k,i})}_{i = 1}^{r}$ computed using eigenvalue decomposition of the *batch-sampled* Hessian, that is, $\frac{1}{B}{\sum_{j = 1}^{B}{{\nabla^{2}\hat{f}}{(x_{k},\xi_{k,j})}}}$. For model-free control, the same idea is used in *Rank-One Modified QL (R1-QL)* \[kolarijani2025rank\] with

<!-- chunk {"id": "body-0090", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

where ${\hat{w}}_{k}$ is now the state-action stationary distribution of the Markov chain induced by the greedy policy w.r.t. $q_{k}$ and estimated using the sample transitions. Once again, the preceding update rule exploits the structure of the "Hessian" in the control problem.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Quasi-Newton methods", "weight": 1.0} -->

We note that the spectral preconditioning technique is closely related to the *matrix splitting* method for solving linear equations. In particular, Deflated Dynamics VI (DDVI) and Temporal Difference (DDTD) algorithms \[lee2024deflated\] also use a spectral decomposition of the transition probability matrix to form a low-rank approximation of it. They then use this low-rank approximation in combination with matrix splitting for the *policy evaluation* problem. In effect, the corresponding update rules follow the same structure as R1-VI/QL, except with rank-$r$ approximation of the transition probability matrix where $r > 1$ (as opposed to $r = 1$).

<!-- chunk {"id": "body-0092", "role": "body", "section": "Convergence of Control Algorithms", "weight": 1.0} -->

One of the promises of building a common formulation for control and optimization algorithms is to borrow existing theoretical results from one field to another. However, as several other studies have pointed out, the similarity in the update rule does not carry over to the analysis. One of the main reasons for this discrepancy is the *non-differentiability* of the Bellman optimality operator $T$. Another complicating factor is that the operator $T$ is a contraction in $\infty$-norm, which is also *non-differentiable*. This forces the convergence analysis of the control algorithms to rely more on fixed-point theory and contraction mappings than on gradient-based smooth analysis.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Convergence of Control Algorithms", "weight": 1.0} -->

In what follows, we examine general tools for the convergence analysis of control algorithms, as well as some simple yet effective remedies for ensuring the convergence of novel control algorithms.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

For *finite* state-action MDPs, the non-differentiability of the operator $T$ is "manageable." Indeed, for such MDPs, $T$ is piece-wise affine and we have

<!-- chunk {"id": "body-0095", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

where the minimization is over the finite set of all deterministic control policies, each corresponding to a linear function $c^{\pi} + {\gammaP^{\pi}v}$. Equivalently, the finite family of policies admits an affine switching system \[liberzon2003switching\], a connection leveraged by \[lee2020unified\] to establish convergence guarantees for asynchronous Q-learning. Moreover, by Rademacher's Theorem \[villani2008optimal, Thm. 10.8\], $T$ is differentiable almost everywhere. This property allows one to use tools from semismooth analysis for deriving local convergence results. In particular, in \[gargiani2022dynamic\], the authors use the fact that the PI algorithm is an instance of the semi-smooth Newton method to show that it has a local quadratic convergence rate. Similarly, in \[kolarijani2023optimization\], the semismoothness of $T$ is used for deriving a local superlinear convergence rate for one of the proposed quasi-PI algorithms.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

A more general approach, however, is to completely get rid of the non-differentiability by *smoothing* the Bellman optimality operator. Not surprisingly, a similar technique has been extensively used to develop algorithms for solving non-smooth optimization problems; see, e.g., the seminal work \[nesterov2005smooth\]. The smoothing of $T$ is achieved by approximating the minimization operation by a differentiable function. As an example, by using the *log-sum-exp* (a.k.a. *soft-max*) function \[rust1994structural\], we can define

<!-- chunk {"id": "body-0097", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

where $\beta > 0$ is the so-called temperature parameter. The operator ${\overline{T}}_{\beta}$ is an over-approximation of the true Bellman optimality operator $\overline{T} = {{\mathbb{E}}_{\varsigma^{+}}{\lbrack{\hat{T}{( \cdot,\varsigma^{+})}}\rbrack}}$ and, in particular, ${\overline{T}}_{\beta}\rightarrow\overline{T}$ as $\beta\rightarrow\infty$. Accordingly, its fixed-point $q^{\beta}$ is not the optimal Q-function, while the gap ${\|{q^{\beta} - q^{\star}}\|}_{\infty}$ can be controlled via the temperature parameter $\beta$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

However, such smoothing allows for a direct application of the second-order scheme for finding the fixed-point of ${\overline{T}}_{\beta}$ \[rust1994structural\]. This idea has been recently used to propose the generalized second-order VI with a quadratic convergence rate \[kamanchi2021generalized\].

<!-- chunk {"id": "body-0099", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

Besides the general tools discussed above, there are simple yet efficient "safeguarding" techniques for ensuring the convergence of novel model-based algorithms that lack convergence guarantees. These techniques specifically exploit the fact that the Bellman optimality operator $T$ is a $\gamma$-contraction. To be precise, let us consider a generic model-based update rule

<!-- chunk {"id": "body-0100", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

characterized by the novel update vector $d_{k}$. One simple technique for ensuring the convergence of the preceding update rule is to safeguard it against VI \[goyal2019first\]. For some $\gamma^{\prime} \in {\lbrack\gamma,1)}$, we consider the *safeguarded update rule*

<!-- chunk {"id": "body-0101", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

The preceding update rule has the following convergence guarantee (for completeness, we provide the proof in Appendix A.1; see also \[goyal2019first, Thm.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Similar to a model-based case, one can benefit from smoothing approaches in model-free scenarios. In simple words, smoothing out the kinks in the Bellman optimality operator or the optimal policies allows us to borrow well-developed tools for stochastic optimization of smooth functions. The recently proposed *mellow-max* operator \[AsadiLittman2017AltSoftmax\] is another excellent example of such smoothing that can be used as a differentiable approximation of the minimization within the Bellman optimality operator. Besides being a smooth operator, the mellow-max operator is, more importantly, non-expansive in the $\infty$-norm. This property then streamlines the usage of standard convergence techniques seamlessly. The corresponding smoothed Bellman optimality operator using the mellow-max is defined as

<!-- chunk {"id": "body-0103", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

with $\omega > 0$ being the temperature parameter that can be used to control the gap ${\|{q^{\omega} - q^{\star}}\|}_{\infty}$ between the fixed-point $q^{\omega}$ of $T_{\omega}$ and the true optimal Q-function $q^{\star} = {\overline{T}{(q^{\star})}}$. The smoothed operator $T_{\omega}$ is an under-approximation of the true Bellman optimality operator $\overline{T}$ and, in particular, we have $T_{\omega}\rightarrow\overline{T}$ as $\omega\rightarrow\infty$. The operator $T_{\omega}$ has been recently used in combination with Anderson mixing to improve the convergence behavior in policy iteration \[sun2021damped\].

<!-- chunk {"id": "body-0104", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

In the model-free case, algorithmic updates are inherently noisy, being driven by samples of the dynamics and costs. This stochasticity naturally places these algorithms within the scope of *stochastic approximation* (*SA*). A standard SA iteration is

<!-- chunk {"id": "body-0105", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

where $\alpha_{k}$ is the step-size (or the so-called *learning rate*), $h:{{\mathbb{R}}^{\ell}\rightarrow{\mathbb{R}}^{\ell}}$ is the *mean field* (expected update), and $M_{k}$ is a martingale-difference noise. A common approach to studying the limiting behavior of an SA method is the *ordinary differential equation* (*ODE*) method. The ODE method (with a dynamical-systems viewpoint), originating with Ljung \[Ljung1977\], analyzes by comparing it with the flow of

<!-- chunk {"id": "body-0106", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

and drawing conclusions about the iterates from the asymptotics of this ODE. The interested reader is referred to \[Chen2002StochasticApproximation, KushnerYin2003, Borkar2008\] for comprehensive treatments. Invariance principles from nonlinear systems (e.g., LaSalle's invariance principle; see \[Khalil2002, Ch. 4\]) then identify invariant/limit sets of the ODE toward which trajectories converge \[Benaim1996, Benaim1999\]. Under standard SA assumptions, the SA iterates track these sets. To guarantee almost-sure boundedness (or Lyapunov stability of the iterates), one imposes verifiable drift/Lyapunov conditions. See \[BorkarMeyn2000\] for the ODE method with drift at infinity and \[AndrieuMoulinesPriouret2005\] for global Lyapunov constructions.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

It is worth mentioning that an important RL-specific deviation from otherwise standard SA conditions is *ergodicity of the state process* for policy evaluation and *sufficient exploration* for control.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Over the years, the ODE framework, in particular the framework introduced by \[BorkarMeyn2000\], has become a standard tool for establishing stability and convergence of a broad class of model-free control/RL algorithms. Considering the *average cost problems*, in \[AbounadiBertsekasBorkar2001\], the authors provided for the first time a complete analysis of two Q-learning algorithms by coupling the ODE style analysis with Kushner-Clark argumentation style \[KushnerClark1978\]. Another major subclass of RL methods is the well-known *actor-critic* methods, which can be characterized as *coupled*, *two-timescale* stochastic iterations: the critic evolves on a *fast* scale to track the value of the current policy, and the actor evolves on a *slow* scale using the critic's signal to adjust the policy. The ODE viewpoint makes this decomposition explicit, which, under the usual SA conditions together with the RL ones, yields clean convergence guarantees to a stationary policy \[BhatnagarEtAl2009NAC, PerkinsLeslie2012\].

<!-- chunk {"id": "body-0109", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Another example is the use of the ODE method to show the convergence of *gradient temporal difference* (*TD*) *approaches* under the general setup of off-policy learning and linear function approximation \[SuttonEtAl2009ICML\]. This work has then been extended to any smooth value function approximation in \[MaeiEtAl2009NIPS\] and to a control setting (policy improvement) under a stationary behavioral policy in \[MaeiEtAl2010ICML\]. Recently, ODE-style arguments have been used not only to prove convergence but also to *design* RL algorithms. In \[DevrajMeyn2017NIPS\], the authors introduce a *matrix preconditioning* for the TD direction, improving the transient behavior of the proposed algorithm. This matrix gain is learned on a faster timescale and tracks the inverse Jacobian of the mean field. This design extends to nonlinear function approximation under standard regularity assumptions \[ChenEtAl2019arXiv\].

<!-- chunk {"id": "body-0110", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

As an example of application of results developed using ODE methods for SAs, namely \[PerkinsLeslie2012\], we finish this section by providing a simple and efficient "safeguarding" technique for ensuring the convergence of novel model-free algorithms that lack convergence guarantees. To this end, let us consider a generic update rule

<!-- chunk {"id": "body-0111", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

characterized by the novel update vector $d_{k} = {\alpha_{k}b_{k}}$. Here, $\alpha_{k}$ is the learning rate satisfying the standard Robbins--Monro condition (i.e., ${\sum_{k}\alpha_{k}} = \infty$ and ${\sum_{k}\alpha_{k}^{2}} < \infty$) and $b_{k}$ is a vector depending on the sampled Bellman error, a.k.a. temporal difference (i.e., ${\hat{T}{(q_{k},\varsigma_{k}^{+})}} - q_{k}$). To address the convergence issue, one possibility is to consider a convex combination of the standard QL algorithm update rule (3.1) with this novel update rule with a diminishing effect \[kolarijani2023optimization\]. To be precise, we modify the update rule as follows

<!-- chunk {"id": "body-0112", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

This leads to the *safeguarded update rule*

<!-- chunk {"id": "body-0113", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

with the following convergence property (for completeness, we provide the proof in Appendix A.3; see also \[kolarijani2023optimization, Sec. III.C\]):
